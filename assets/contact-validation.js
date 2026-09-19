/** Shared browser/server validation. JBKJS remains text to preserve leading zeros. */
export function validateContact(raw) {
  /** @type {Record<string, string>} */
  const fields = {};
  const limits = { name: 100, org: 200, jbkjs: 5, email: 254, phone: 40, message: 2000, source: 200 };
  const data = { name: '', org: '', jbkjs: '', email: '', phone: '', message: '', source: '', kind: '' };
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) return { data, fields: { form: 'Proverite podatke u formi.' } };
  for (const [field, limit] of Object.entries(limits)) {
    const value = raw[field] ?? '';
    if (typeof value !== 'string' || value.length > limit || /[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/.test(value)) {
      fields[field] = `Unesite najviše ${limit} znakova.`;
      data[field] = '';
    } else data[field] = value.trim();
  }
  data.kind = typeof raw.kind === 'string' ? raw.kind : '';
  if (!['presentation', 'question'].includes(data.kind)) fields.form = 'Izaberite vrstu upita.';
  if (!data.name) fields.name = 'Unesite ime i prezime.';
  if (!data.org) fields.org = 'Unesite naziv škole.';
  if (!/^\d{5}$/.test(data.jbkjs)) fields.jbkjs = 'JBKJS mora imati tačno pet cifara.';
  if (!/^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/.test(data.email)) fields.email = 'Unesite ispravnu email adresu.';
  if (data.kind === 'question' && !data.message) fields.message = 'Napišite pitanje koje želite da postavite.';
  if (data.source && !/^\/[a-z0-9/-]*$/.test(data.source)) fields.source = 'Neispravna stranica upita.';
  return { data, fields };
}
