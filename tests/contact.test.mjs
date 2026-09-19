import { test } from 'node:test';
import assert from 'node:assert/strict';
import { handleContact as contactHandler, verifyTurnstile, sendContactMail } from '../worker/src/index.ts';
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
