import { validateContact } from '../../assets/contact-validation.js';
import nodemailer from 'nodemailer';

type ContactMail = { from: { name: string; address: string }; to: string; replyTo: string; subject: string; text: string; html: string };

export async function sendContactMail(env: Env, mail: ContactMail, createTransport = nodemailer.createTransport): Promise<void> {
  const transport = createTransport({
    host: 'smtp.gmail.com', port: 465, secure: true,
    auth: { user: env.SMTP_USER, pass: env.SMTP_PASSWORD },
    connectionTimeout: 8000, greetingTimeout: 8000, socketTimeout: 10000,
    disableFileAccess: true, disableUrlAccess: true,
    logger: false, debug: false,
  });
  try {
    const result = await transport.sendMail(mail);
    if (!result.accepted.includes(mail.to)) {
      throw new Error('SMTP recipient not accepted');
    }
  } finally { transport.close(); }
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
      from: { address: env.CONTACT_FROM, name: 'Budžet+ sajt' }, to: env.CONTACT_TO,
      replyTo: data.email, subject: title, text,
      html: `<div style="font-family:Arial,sans-serif;white-space:pre-wrap">${escapeHtml(text)}</div>`,
    });
  } catch {
    console.error(JSON.stringify({ event: 'contact_email_failed' }));
    return reply(503, { ok: false, code: 'delivery_unavailable' });
  }
  console.log(JSON.stringify({ event: 'contact_accepted', kind: data.kind }));
  return reply(200, { ok: true });
}

export default {
  fetch(request: Request, env: Env) { return handleContact(request, env); },
} satisfies ExportedHandler<Env>;
