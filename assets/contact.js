import { validateContact } from './contact-validation.js';

const form = document.getElementById('contact-form');
if (form) {
  const config = window.BUDZET_CONTACT || {};
  const previewNotice = 'Lokalni pregled: možete proveriti unos, ali email se ne šalje. Stvarno slanje proverite na budzetplus.rs nakon objave forme.';
  const feedback = form.querySelector('.form-feedback');
  const submit = form.querySelector('[type="submit"]');
  const switcher = form.querySelector('.form-mode-switch');
  const message = form.elements.namedItem('message');
  let kind = 'presentation';
  let pending = false;
  let token = '';
  let widgetId;
  let widgetLoading = false;
  const sourceTopic = new URLSearchParams(location.search).get('tema');
  const source = sourceTopic && /^[a-z0-9-]+$/.test(sourceTopic) ? `/${sourceTopic}/` : location.pathname;
  const label = () => kind === 'presentation' ? 'Prijavite se za prezentaciju ↗' : 'Pošaljite pitanje ↗';
  const status = (text, state = 'error') => {
    feedback.textContent = text;
    feedback.dataset.state = state;
  };
  const clearErrors = () => {
    form.querySelectorAll('.field-error').forEach(el => { el.textContent = ''; });
    form.querySelectorAll('[aria-invalid]').forEach(el => el.removeAttribute('aria-invalid'));
  };
  const showErrors = fields => {
    clearErrors();
    for (const [name, text] of Object.entries(fields)) {
      const field = form.elements.namedItem(name);
      const error = document.getElementById(`error-${name}`);
      if (field && error) { field.setAttribute('aria-invalid', 'true'); error.textContent = text; }
    }
    status('Proverite označena polja. Vaši podaci su sačuvani u formi.');
    form.querySelector('[aria-invalid="true"]')?.focus();
  };
  const setMode = next => {
    if (pending) return;
    kind = next;
    const question = kind === 'question';
    document.getElementById('form-title').textContent = question ? 'Postavite pitanje' : 'Prijava za prezentaciju';
    document.getElementById('form-description').textContent = question ? 'Napišite šta vas zanima. Odgovorićemo na vaš email.' : 'Unesite podatke škole i email na koji možemo da vam se javimo.';
    switcher.textContent = question ? 'Želim da se prijavim za prezentaciju' : 'Želim da postavim pitanje';
    document.getElementById('message-label').textContent = question ? 'Vaše pitanje' : 'Napomena (opciono)';
    message.required = question;
    submit.textContent = label();
    clearErrors();
    status(config.preview ? previewNotice : '', 'idle');
  };
  if (config.preview) status(previewNotice, 'idle');
  switcher.addEventListener('click', () => setMode(kind === 'question' ? 'presentation' : 'question'));
  document.querySelectorAll('.js-question').forEach(link => link.addEventListener('click', () => { setMode('question'); message.focus({ preventScroll: true }); }));
  document.querySelectorAll('a[href="#kontakt"]:not(.js-question)').forEach(link => link.addEventListener('click', () => setMode('presentation')));
  form.elements.namedItem('jbkjs').addEventListener('input', event => { event.target.value = event.target.value.replace(/\D/g, '').slice(0, 5); });
  form.addEventListener('input', event => {
    const field = event.target;
    field.removeAttribute('aria-invalid');
    const error = document.getElementById(`error-${field.name}`);
    if (error) error.textContent = '';
  });

  function loadWidget() {
    if (widgetLoading || !config.sitekey) return;
    widgetLoading = true;
    window.budzetTurnstileReady = () => {
      widgetId = window.turnstile.render('#turnstile-container', {
        sitekey: config.sitekey, action: 'contact', theme: 'light', size: 'flexible',
        callback: value => { token = value; },
        'expired-callback': () => { token = ''; },
        'error-callback': () => { token = ''; status('Provera trenutno nije dostupna. Pokušajte ponovo ili nam pošaljite email.'); },
      });
    };
    const script = document.createElement('script');
    script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?onload=budzetTurnstileReady&render=explicit';
    script.async = true;
    script.onerror = () => { widgetLoading = false; script.remove(); status('Provera se nije učitala. Proverite vezu i pokušajte ponovo ili nam pošaljite email.'); };
    document.head.appendChild(script);
  }
  if (config.sitekey) {
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(entries => {
        if (entries.some(entry => entry.isIntersecting)) { loadWidget(); observer.disconnect(); }
      }, { rootMargin: '300px' });
      observer.observe(form);
    } else loadWidget();
    form.addEventListener('focusin', loadWidget, { once: true });
  }

  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (pending) return;
    const raw = { ...Object.fromEntries(new FormData(form)), kind, source };
    const { data, fields } = validateContact(raw);
    if (Object.keys(fields).length) { showErrors(fields); return; }
    clearErrors();
    if (config.preview) {
      status('Podaci su ispravni. ' + previewNotice, 'idle');
      return;
    }
    if (!config.sitekey || !config.endpoint) {
      status('Direktna prijava trenutno nije dostupna. Pišite nam na aleksandar.pejkovic@budzetplus.rs ili pozovite 065 917 0989.');
      return;
    }
    if (!token) { loadWidget(); status('Sačekajte proveru iznad dugmeta, pa ponovite slanje.'); return; }
    pending = true;
    submit.disabled = true;
    switcher.disabled = true;
    // Freeze the submitted fields so later edits cannot be erased by a successful response.
    const controls = [...form.querySelectorAll('input, textarea')];
    controls.forEach(control => { control.readOnly = true; });
    submit.textContent = 'Slanje je u toku…';
    status('Sačekajte trenutak, šaljemo vaš upit.', 'pending');
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 25000);
    try {
      const response = await fetch(config.endpoint, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...data, token }), signal: controller.signal, credentials: 'omit',
      });
      const result = await response.json();
      if (response.status === 422 && result.fields) { showErrors(result.fields); return; }
      if (!response.ok || result.ok !== true) {
        const errors = {
          403: 'Provera je istekla ili nije uspela. Ponovite proveru i pokušajte ponovo.',
          429: 'Poslali ste više zahteva za kratko vreme. Sačekajte minut pre novog pokušaja.',
          503: 'Slanje trenutno nije dostupno. Podaci su sačuvani u formi; pokušajte kasnije ili nam pošaljite email.',
        };
        status(errors[response.status] || 'Nismo mogli da pošaljemo upit. Pokušajte ponovo ili nam pošaljite email.');
        return;
      }
      form.reset();
      status(kind === 'presentation' ? 'Hvala! Vaša prijava je prihvaćena. O terminu prezentacije obavestićemo vas emailom.' : 'Hvala! Vaše pitanje je prihvaćeno. Odgovorićemo na navedeni email.', 'success');
      feedback.focus({ preventScroll: true });
      if (typeof window.gtag === 'function') window.gtag('event', 'generate_lead', { lead_type: kind });
    } catch {
      status('Nismo dobili potvrdu slanja. Podaci su ostali u formi. Proverite vezu; ako niste sigurni da li je prijava stigla, javite nam se emailom ili telefonom.');
    } finally {
      clearTimeout(timeout);
      token = '';
      if (widgetId !== undefined && window.turnstile) window.turnstile.reset(widgetId);
      pending = false;
      submit.disabled = false;
      switcher.disabled = false;
      controls.forEach(control => { control.readOnly = false; });
      submit.textContent = label();
    }
  });
}
