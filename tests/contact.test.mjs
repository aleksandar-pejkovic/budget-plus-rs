import { test } from 'node:test';
import assert from 'node:assert/strict';
import { handleContact as contactHandler, verifyTurnstile, sendContactMail, openSmtpSocket } from '../worker/src/index.ts';
import { EventEmitter } from 'node:events';
const handleContact = (request, env, verify) => contactHandler(request, { SMTP_USER: 'demo@example.com', SMTP_PASSWORD: 'test-password', ...env }, verify, (_env, mail) => env.EMAIL.send(mail));
import { validateContact } from '../assets/contact-validation.js';

const valid = { kind: 'presentation', name: 'Demo korisnik', org: 'Demo škola', jbkjs: '00123', email: 'demo@example.com', phone: '', message: '', source: '/', token: 'token-demo' };
const verified = async () => Response.json({ success: true, action: 'contact', hostname: 'budzetplus.rs' });
function setup(overrides = {}) {
  const sent = [];
  const env = { ALLOWED_ORIGINS: 'https://budzetplus.rs,https://www.budzetplus.rs', TURNSTILE_HOSTNAMES: 'budzetplus.rs,www.budzetplus.rs', TURNSTILE_SECRET: 'test-secret', CONTACT_FROM: 'prijave@notify.budzetplus.rs', CONTACT_TO: 'owner@example.com', EMAIL: { send: async data => { sent.push(data); return { messageId: 'test' }; } }, CONTACT_LIMITER: { limit: async () => ({ success: true }) }, ...overrides };
  return { env, sent };
}
const request = (data = valid, extra = {}) => new Request('https://api.budzetplus.rs/contact', { method: 'POST', headers: { Origin: 'https://budzetplus.rs', 'Content-Type': 'application/json', 'CF-Connecting-IP': '192.0.2.1' }, body: JSON.stringify(data), ...extra });

test('valid submission preserves JBKJS and fixes recipient / reply-to', async () => {
  const { env, sent } = setup();
  const result = await handleContact(request({ ...valid, to: 'attacker@example.com' }), env, verified);
  assert.equal(result.status, 200);
  assert.equal(sent.length, 1); assert.equal(sent[0].to, 'owner@example.com');
  assert.equal(sent[0].replyTo, valid.email); assert.match(sent[0].text, /00123/);
  assert.equal(result.headers.get('Access-Control-Allow-Origin'), 'https://budzetplus.rs');
});
test('invalid form is rejected before verification or email', async () => {
  const { env, sent } = setup();
  const result = await handleContact(request({ ...valid, email: 'bad', jbkjs: 123 }), env, () => { throw new Error('must not verify'); });
  assert.equal(result.status, 422); assert.equal(sent.length, 0);
  assert.ok((await result.json()).fields.jbkjs);
  assert.ok(validateContact({ ...valid, kind: 'question' }).fields.message);
  assert.deepEqual(validateContact(valid).fields, {});
});
test('siteverify fails closed for replay, wrong hostname/action and upstream errors', async () => {
  const { env, sent } = setup();
  for (const result of [{ success: false, 'error-codes': ['timeout-or-duplicate'] }, { success: true, action: 'other', hostname: 'budzetplus.rs' }, { success: true, action: 'contact', hostname: 'localhost' }, { success: 'true', action: 'contact', hostname: 'budzetplus.rs' }]) {
    assert.equal((await handleContact(request(), env, async () => Response.json(result))).status, 403);
  }
  assert.equal(await verifyTurnstile('x', env, '', async () => new Response('bad')), false);
  assert.equal(await verifyTurnstile('x', env, '', async () => { throw new Error('offline'); }), false);
  assert.equal(await verifyTurnstile('x'.repeat(2049), env, '', verified), false);
  assert.equal(sent.length, 0);
});
test('token cannot be reused after successful verification', async () => {
  const { env, sent } = setup(); let redeemed = false;
  const singleUse = async () => { const success = !redeemed; redeemed = true; return Response.json({ success, action: 'contact', hostname: 'budzetplus.rs' }); };
  assert.equal((await handleContact(request(), env, singleUse)).status, 200);
  assert.equal((await handleContact(request(), env, singleUse)).status, 403);
  assert.equal(sent.length, 1);
});
test('origin, method, request size and rate limit restrictions', async () => {
  const { env, sent } = setup();
  const badOrigin = request(valid, { headers: { Origin: 'https://evil.example', 'Content-Type': 'application/json' } });
  const result = await handleContact(badOrigin, env, verified);
  assert.equal(result.status, 403); assert.equal(result.headers.has('Access-Control-Allow-Origin'), false);
  assert.equal((await handleContact(request(valid, { method: 'GET', body: undefined }), env, verified)).status, 405);
  assert.equal((await handleContact(request(valid, { body: 'x'.repeat(17000) }), env, verified)).status, 413);
  assert.equal((await handleContact(request(valid, { body: '{' }), env, verified)).status, 400);
  const limited = setup({ CONTACT_LIMITER: { limit: async () => ({ success: false }) } });
  const throttled = await handleContact(request(), limited.env, verified);
  assert.equal(throttled.status, 429); assert.equal(throttled.headers.get('Retry-After'), '60');
  assert.equal(sent.length, 0);
});
test('failed email or missing secret never produces a success response', async () => {
  const failed = setup({ EMAIL: { send: async () => { throw new Error('provider'); } } });
  assert.equal((await handleContact(request(), failed.env, verified)).status, 503);
  const missing = setup({ TURNSTILE_SECRET: '' });
  assert.equal((await handleContact(request(), missing.env, verified)).status, 503);
  const missingSmtp = setup({ SMTP_PASSWORD: '' });
  assert.equal((await handleContact(request(), missingSmtp.env, verified)).status, 503);
});

test('SMTP requires recipient acceptance and closes the transport on all outcomes', async () => {
  const mail = { from: { address: 'prijava@budzetplus.rs', name: 'Budžet+' }, to: 'prijava@budzetplus.rs', replyTo: valid.email, subject: 'Test', text: 'Test', html: 'Test' };
  for (const outcome of ['accepted', 'rejected', 'error']) {
    let closed = false;
    const factory = options => {
      assert.equal(options.host, 'smtp.gmail.com');
      assert.equal(options.port, 465); assert.equal(options.secure, true);
      assert.equal(options.auth.user, 'demo@example.com');
      assert.equal(options.logger, false); assert.equal(options.debug, false);
      assert.equal(typeof options.getSocket, 'function');
      return { close: () => { closed = true; }, sendMail: async data => {
        assert.equal(data.replyTo, valid.email);
        if (outcome === 'error') throw new Error('SMTP failure');
        return { accepted: outcome === 'accepted' ? [mail.to] : [] };
      } };
    };
    const send = sendContactMail({ SMTP_USER: 'demo@example.com', SMTP_PASSWORD: 'test-password' }, mail, factory);
    if (outcome === 'accepted') await send; else await assert.rejects(send);
    assert.equal(closed, true);
  }
});
test('email HTML is escaped and no user input enters the subject', async () => {
  const { env, sent } = setup();
  await handleContact(request({ ...valid, message: '<img src=x onerror=alert(1)>' }), env, verified);
  assert.ok(!sent[0].html.includes('<img')); assert.match(sent[0].html, /&lt;img/);
  assert.equal(sent[0].subject, 'Prijava za Budžet+ prezentaciju');
});

test('SMTP diagnostics classify failures without exposing private data or changing the public response', async t => {
  const privateText = 'private-address@example.com password token message server-response';
  const cases = [
    [{ code: 'EAUTH', command: `AUTH PLAIN ${privateText}`, responseCode: 535 }, 'EAUTH', 535, 'authentication'],
    [{ code: 'ESOCKET', command: 'CONN' }, 'ESOCKET', null, 'connection'],
    [{ code: 'ETLS', command: 'STARTTLS', responseCode: 454 }, 'ETLS', 454, 'tls'],
    [{ code: 'EENVELOPE', command: 'MAIL FROM', responseCode: 550 }, 'EENVELOPE', 550, 'sender'],
    [{ code: 'EENVELOPE', command: 'RCPT TO', responseCode: 553 }, 'EENVELOPE', 553, 'recipient'],
    [{ code: 'EMESSAGE', command: 'DATA', responseCode: 554 }, 'EMESSAGE', 554, 'message'],
    [{ code: 'ETIMEDOUT', command: 'EHLO' }, 'ETIMEDOUT', null, 'greeting'],
    [{ code: privateText, command: privateText, responseCode: privateText }, 'UNKNOWN', null, 'send'],
    ...[199, 600, 535.5, NaN, Infinity, '535'].map(responseCode => [{ responseCode }, 'UNKNOWN', null, 'send']),
    [null, 'UNKNOWN', null, 'send'],
    [privateText, 'UNKNOWN', null, 'send'],
  ];
  const logs = [];
  t.mock.method(console, 'error', (...args) => logs.push(args));
  for (const [details, code, smtpStatus, stage] of cases) {
    logs.length = 0;
    const error = details && typeof details === 'object'
      ? Object.assign(new Error(privateText), { response: privateText, envelope: privateText, cause: privateText, ...details }) : details;
    let closed = false;
    const factory = () => ({ sendMail: async () => { throw error; }, close: () => { closed = true; } });
    const { env } = setup();
    const result = await contactHandler(request(), { ...env, SMTP_USER: 'test', SMTP_PASSWORD: privateText }, verified,
      (env, mail) => sendContactMail(env, mail, factory));
    assert.equal(result.status, 503);
    assert.deepEqual(await result.json(), { ok: false, code: 'delivery_unavailable' });
    assert.equal(closed, true);
    assert.deepEqual(logs, [[JSON.stringify({ event: 'contact_email_failed', code, smtpStatus, stage })]]);
    assert.ok(!JSON.stringify(logs).includes(privateText));
  }
});

test('SMTP diagnostics retain setup, acceptance and cleanup phases and preserve the original failure', async () => {
  const mail = { to: 'recipient@example.com' };
  const failure = Object.assign(new Error('private data'), { code: 'EAUTH', responseCode: 535 });
  const cases = [
    [() => { throw failure; }, 'EAUTH', 535, 'setup'],
    [() => ({ sendMail: async () => ({ accepted: [] }), close() {} }), 'EENVELOPE', null, 'acceptance'],
    [() => ({ sendMail: async () => ({ accepted: [mail.to] }), close() { throw failure; } }), 'EAUTH', 535, 'close'],
    [() => ({ sendMail: async () => { throw failure; }, close() { throw new Error('cleanup'); } }), 'EAUTH', 535, 'authentication'],
  ];
  for (const [factory, code, smtpStatus, stage] of cases) {
    await assert.rejects(sendContactMail({}, mail, factory), error => {
      assert.equal(error.message, 'Contact email failed');
      assert.deepEqual(error.diagnostic, { code, smtpStatus, stage });
      assert.equal(error.cause, undefined);
      return true;
    });
  }
});

test('SMTP socket uses verified hostname TLS and hands off only after the handshake', () => {
  const socket = new EventEmitter();
  socket.destroy = () => assert.fail('healthy socket must stay open');
  const calls = [];
  openSmtpSocket((...args) => calls.push(args), options => {
    assert.deepEqual(options, { host: 'smtp.gmail.com', port: 465, servername: 'smtp.gmail.com', rejectUnauthorized: true });
    return socket;
  });
  assert.equal(calls.length, 0);
  socket.emit('secureConnect');
  assert.deepEqual(calls, [[null, { connection: socket, secured: true }]]);
  socket.emit('error', new Error('late error'));
  socket.emit('close');
  assert.equal(calls.length, 1);
});

test('SMTP socket closes on timeout, TLS error or early close and calls back once', t => {
  t.mock.timers.enable({ apis: ['setTimeout'] });
  for (const outcome of ['timeout', 'error', 'close']) {
    const socket = new EventEmitter();
    let destroyed = false;
    socket.destroy = () => { destroyed = true; socket.emit('close'); };
    const calls = [];
    openSmtpSocket((...args) => calls.push(args), () => socket);
    if (outcome === 'timeout') t.mock.timers.tick(8000);
    else socket.emit(outcome, new Error('private data'));
    socket.emit('secureConnect');
    socket.emit('error', new Error('late error'));
    assert.equal(destroyed, true);
    assert.equal(calls.length, 1);
    assert.equal(calls[0][0].code, outcome === 'timeout' ? 'ETIMEDOUT' : 'ETLS');
    assert.equal(calls[0][0].message, 'SMTP TLS connection failed');
    assert.equal(calls[0][1], undefined);
  }
  let error;
  openSmtpSocket(value => { error = value; }, () => { throw new Error('private data'); });
  assert.equal(error.code, 'ETLS');
});
