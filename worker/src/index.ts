import { validateContact } from '../../assets/contact-validation.js';
import nodemailer from 'nodemailer';
import { connect, type TLSSocket } from 'node:tls';

type ContactMail = { from: { name: string; address: string }; to: string; replyTo: string; subject: string; text: string; html: string };

const SMTP_CODES = new Set(['EAUTH', 'ECONNECTION', 'ESOCKET', 'ETIMEDOUT', 'EDNS', 'ETLS', 'EPROTOCOL', 'EENVELOPE', 'EMESSAGE', 'ESTREAM', 'ECONNRESET', 'ECONNREFUSED', 'ENOTFOUND', 'EAI_AGAIN']);
type MailPhase = 'setup' | 'send' | 'acceptance' | 'close';

function smtpDiagnostic(error: unknown, phase: MailPhase) {
  const details = error !== null && typeof error === 'object' ? error as Record<string, unknown> : {};
  const code = typeof details.code === 'string' && SMTP_CODES.has(details.code) ? details.code : 'UNKNOWN';
  const smtpStatus = typeof details.responseCode === 'number' && Number.isInteger(details.responseCode) && details.responseCode >= 200 && details.responseCode <= 599 ? details.responseCode : null;
  // Never log command text: AUTH commands may contain credentials.
  const command = details.command;
  let stage: string = phase;
  if (phase === 'send') {
    if (code === 'EAUTH' || (typeof command === 'string' && /^AUTH(?: |$)/.test(command))) stage = 'authentication';
    else if (code === 'ETLS' || command === 'STARTTLS') stage = 'tls';
    else if (command === 'EHLO' || command === 'HELO') stage = 'greeting';
    else if (command === 'MAIL FROM') stage = 'sender';
    else if (command === 'RCPT TO') stage = 'recipient';
    else if (command === 'DATA') stage = 'message';
    else if (command === 'CONN' || ['ECONNECTION', 'ESOCKET', 'ETIMEDOUT', 'EDNS', 'ECONNRESET', 'ECONNREFUSED', 'ENOTFOUND', 'EAI_AGAIN'].includes(code)) stage = 'connection';
  }
  return { code, smtpStatus, stage };
}

class ContactMailError extends Error {
  readonly diagnostic: ReturnType<typeof smtpDiagnostic>;
  constructor(error: unknown, phase: MailPhase) {
    super('Contact email failed');
    this.diagnostic = smtpDiagnostic(error, phase);
  }
}

type SocketCallback = (error: Error | null, options?: { connection: TLSSocket; secured: true }) => void;

export function openSmtpSocket(callback: SocketCallback, connectSocket = connect): void {
  // Preserve the hostname at the Workers socket boundary. Nodemailer's default
  // DNS resolution passes an IP to TLS, which fails on the production edge.
  let socket: TLSSocket;
  try {
    socket = connectSocket({ host: 'smtp.gmail.com', port: 465, servername: 'smtp.gmail.com', rejectUnauthorized: true });
  } catch {
    callback(Object.assign(new Error('SMTP TLS connection failed'), { code: 'ETLS' }));
    return;
  }
  let settled = false;
  const fail = (code: 'ETLS' | 'ETIMEDOUT') => {
    if (settled) return;
    settled = true;
    clearTimeout(timer);
    socket.destroy();
    callback(Object.assign(new Error('SMTP TLS connection failed'), { code }));
  };
  const timer = setTimeout(() => fail('ETIMEDOUT'), 8000);
  // Keep the listener to absorb late teardown errors; callback is invoked once.
  socket.on('error', () => fail('ETLS'));
  socket.once('close', () => fail('ETLS'));
  socket.once('secureConnect', () => {
    if (settled) return;
    settled = true;
    clearTimeout(timer);
    callback(null, { connection: socket, secured: true });
  });
}

export async function sendContactMail(env: Env, mail: ContactMail, createTransport = nodemailer.createTransport): Promise<void> {
  let phase: MailPhase = 'setup';
  let transport: ReturnType<typeof createTransport> | undefined;
  let failure: ContactMailError | undefined;
  try {
    transport = createTransport({
      host: 'smtp.gmail.com', port: 465, secure: true,
      auth: { user: env.SMTP_USER, pass: env.SMTP_PASSWORD },
      connectionTimeout: 8000, greetingTimeout: 8000, socketTimeout: 10000,
      disableFileAccess: true, disableUrlAccess: true,
      logger: false, debug: false,
      getSocket: (_options, callback) => openSmtpSocket(callback),
    });
    phase = 'send';
    const result = await transport.sendMail(mail);
    phase = 'acceptance';
    if (!result.accepted.includes(mail.to)) {
      throw Object.assign(new Error('SMTP recipient not accepted'), { code: 'EENVELOPE' });
    }
  } catch (error) {
    failure = new ContactMailError(error, phase);
  } finally {
    try { transport?.close(); }
    catch (error) { failure ??= new ContactMailError(error, 'close'); }
  }
  if (failure) throw failure;
}

const MAX_BODY_BYTES = 16 * 1024;
const split = (value: string) => new Set(value.split(',').map(item => item.trim()).filter(Boolean));

class BodyTooLarge extends Error {}

async function readBody(request: Request): Promise<unknown> {
  if (Number(request.headers.get('content-length')) > MAX_BODY_BYTES) throw new BodyTooLarge();
  if (!request.body) throw new SyntaxError();
  const reader = request.body.getReader();
  const chunks: Uint8Array[] = [];
  let length = 0;
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    length += value.byteLength;
    if (length > MAX_BODY_BYTES) { await reader.cancel(); throw new BodyTooLarge(); }
    chunks.push(value);
  }
  const buffer = new Uint8Array(length);
  let offset = 0;
  for (const chunk of chunks) { buffer.set(chunk, offset); offset += chunk.byteLength; }
  return JSON.parse(new TextDecoder('utf-8', { fatal: true, ignoreBOM: false }).decode(buffer));
}

export async function verifyTurnstile(token: unknown, env: Env, clientIp: string, verifyFetch: typeof fetch = fetch): Promise<boolean> {
  const hosts = split(env.TURNSTILE_HOSTNAMES);
  if (typeof token !== 'string' || !token.trim() || token.length > 2048 || !env.TURNSTILE_SECRET || !hosts.size) return false;
  try {
    const body = new URLSearchParams({ secret: env.TURNSTILE_SECRET, response: token });
    if (clientIp) body.set('remoteip', clientIp);
    const response = await verifyFetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body, signal: AbortSignal.timeout(10000),
    });
    if (!response.ok) return false;
    const result = await response.json() as { success?: boolean; action?: string; hostname?: string };
    return result.success === true && result.action === 'contact' && typeof result.hostname === 'string' && hosts.has(result.hostname);
  } catch { return false; }
}

const escapeHtml = (value: string) => value.replace(/[&<>"']/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[char]!);

export async function handleContact(request: Request, env: Env, verifyFetch: typeof fetch = fetch, sendMail = sendContactMail): Promise<Response> {
  const origin = request.headers.get('Origin') || '';
  const allowed = split(env.ALLOWED_ORIGINS).has(origin);
  const headers = new Headers({ 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'Vary': 'Origin', 'X-Content-Type-Options': 'nosniff' });
  if (allowed) headers.set('Access-Control-Allow-Origin', origin);
  const reply = (status: number, payload: object) => new Response(JSON.stringify(payload), { status, headers });
  if (new URL(request.url).pathname !== '/contact') return reply(404, { ok: false, code: 'not_found' });
  if (!allowed) return reply(403, { ok: false, code: 'origin' });
  if (request.method === 'OPTIONS') {
    headers.set('Access-Control-Allow-Methods', 'POST');
    headers.set('Access-Control-Allow-Headers', 'Content-Type');
    headers.set('Access-Control-Max-Age', '600');
    return new Response(null, { status: 204, headers });
  }
  if (request.method !== 'POST') { headers.set('Allow', 'POST, OPTIONS'); return reply(405, { ok: false, code: 'method' }); }
  if (request.headers.get('Content-Type')?.split(';')[0].trim().toLowerCase() !== 'application/json') return reply(415, { ok: false, code: 'content_type' });
  if (!env.TURNSTILE_SECRET || !env.SMTP_PASSWORD || !env.SMTP_USER || !env.CONTACT_LIMITER || !env.CONTACT_FROM || !env.CONTACT_TO) return reply(503, { ok: false, code: 'unavailable' });
  const clientIp = request.headers.get('CF-Connecting-IP') || 'unknown';
  try {
    const limit = await env.CONTACT_LIMITER.limit({ key: `contact:${clientIp}` });
    if (!limit.success) { headers.set('Retry-After', '60'); return reply(429, { ok: false, code: 'rate_limit' }); }
  } catch { return reply(503, { ok: false, code: 'unavailable' }); }

  let raw: unknown;
  try { raw = await readBody(request); }
  catch (error) { return reply(error instanceof BodyTooLarge ? 413 : 400, { ok: false, code: 'invalid_body' }); }
  const { data, fields } = validateContact(raw);
  if (Object.keys(fields).length) return reply(422, { ok: false, fields });
  const token = (raw as { token?: unknown }).token;
  if (!await verifyTurnstile(token, env, clientIp, verifyFetch)) return reply(403, { ok: false, code: 'verification' });

  const title = data.kind === 'presentation' ? 'Prijava za Budžet+ prezentaciju' : 'Pitanje o programu Budžet+';
  const text = [title, '', `Ime i prezime: ${data.name}`, `Škola: ${data.org}`, `JBKJS: ${data.jbkjs}`, `Email: ${data.email}`, `Telefon: ${data.phone || 'Nije naveden'}`, `Stranica: ${data.source || '/'}`, '', data.message || 'Bez dodatne napomene.'].join('\n');
  try {
    // Await acceptance by the email service. Never report delivery to an inbox.
    await sendMail(env, {
      from: { address: env.CONTACT_FROM, name: 'Budžet+ Prijava' }, to: env.CONTACT_TO,
      replyTo: data.email, subject: title, text,
      html: `<div style="font-family:Arial,sans-serif;white-space:pre-wrap">${escapeHtml(text)}</div>`,
    });
  } catch (error) {
    const diagnostic = error instanceof ContactMailError ? error.diagnostic : smtpDiagnostic(error, 'send');
    console.error(JSON.stringify({ event: 'contact_email_failed', ...diagnostic }));
    return reply(503, { ok: false, code: 'delivery_unavailable' });
  }
  console.log(JSON.stringify({ event: 'contact_accepted', kind: data.kind }));
  return reply(200, { ok: true });
}

export default {
  fetch(request: Request, env: Env) { return handleContact(request, env); },
} satisfies ExportedHandler<Env>;
