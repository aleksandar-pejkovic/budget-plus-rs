// Smooth scroll offset correction and contact form feedback
(function () {
  const form = document.getElementById('contact-form');
  const feedback = form ? form.querySelector('.form-feedback') : null;
  const jbkjsInput = form ? form.querySelector('[name="jbkjs"]') : null;
  let presentationMode = false;
  const allInputs = form ? Array.from(form.querySelectorAll('input, textarea')) : [];

  // Smooth scroll with slight offset for sticky nav
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const targetId = anchor.getAttribute('href');
      if (!targetId || targetId === '#') return;
      const el = document.querySelector(targetId);
      if (!el) return;
      e.preventDefault();
      const top = el.getBoundingClientRect().top + window.scrollY - 70;
      window.scrollTo({ top, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
    });
  });

  function setFormMode(presentation) {
      if (!form) return;
      presentationMode = presentation;
      const message = form.querySelector('[name="message"]');
      const heading = form.querySelector('.form-heading h3');
      const description = form.querySelector('.form-heading p');
      const submitButton = form.querySelector('[type="submit"]');
      if (!message) return;
      message.required = !presentation;
      message.placeholder = presentation ? 'Dodatna napomena (opciono)' : 'Šta vam je potrebno';
      form.querySelector('#message-label').textContent = presentation ? 'Napomena (opciono)' : 'Poruka';
      form.querySelector('.form-mode-switch').hidden = !presentation;
      if (heading) heading.textContent = presentation ? 'Prijava za prezentaciju' : 'Imate pitanje?';
      if (description) description.textContent = presentation ? 'Termin još nije određen. Unesite svoje podatke da bismo vas obavestili kada bude zakazana naredna prezentacija.' : 'Za pitanja koja nisu vezana za zakazivanje termina, pošaljite nam poruku.';
      if (submitButton) submitButton.textContent = presentation ? 'Pripremite prijavu' : 'Pripremite poruku';
      if (feedback) feedback.textContent = '';
      const firstEmpty = Array.from(form.querySelectorAll('[required]')).find(input => !input.value.trim());
      (firstEmpty || message).focus({ preventScroll: true });
  }

  document.querySelectorAll('.js-presentation-interest').forEach((link) => {
    link.addEventListener('click', () => {
      setFormMode(true);
    });
  });

  if (!form || !feedback) return;
  form.querySelector('.form-mode-switch').addEventListener('click', () => setFormMode(false));

  if (jbkjsInput) {
    jbkjsInput.addEventListener('input', () => {
      jbkjsInput.value = jbkjsInput.value.replace(/\D/g, '').slice(0, 5);
    });
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const missing = Array.from(form.querySelectorAll('[required]')).find(input => !input.value.trim());
    if (missing) {
      feedback.textContent = 'Molimo popunite obavezna polja.';
      feedback.style.color = '#dc2626';
      missing.focus();
      return;
    }

    if (!jbkjsInput || !/^\d{5}$/.test(jbkjsInput.value.trim())) {
      feedback.textContent = 'JBKJS mora imati tačno 5 cifara.';
      feedback.style.color = '#dc2626';
      if (jbkjsInput) jbkjsInput.focus();
      return;
    }

    const formData = allInputs.reduce((acc, input) => {
      acc[input.name] = input.value.trim();
      return acc;
    }, {});

    const lines = [
      `Ime i prezime: ${formData.name || ''}`,
      `Škola: ${formData.org || ''}`,
      formData.jbkjs ? `JBKJS: ${formData.jbkjs}` : null,
      formData.city ? `Mesto: ${formData.city}` : null,
      formData.phone ? `Telefon: ${formData.phone}` : null,
      '',
      presentationMode ? 'Želim da se prijavim za narednu prezentaciju programa Budžet+. Molim vas da me obavestite kada bude određen termin.' : null,
      formData.message || '',
    ].filter(Boolean);

    const subject = presentationMode ? 'Prijava za Budžet+ prezentaciju - ' : 'Budžet+ upit - ';
    const mailto = `mailto:aleksandar.pejkovic@budzetplus.rs?subject=${encodeURIComponent(subject + (formData.name || ''))}&body=${encodeURIComponent(lines.join('\n'))}`;

    try {
      window.location.href = mailto;
      feedback.textContent = 'Pošaljite pripremljeni email iz svoje email aplikacije. Ako se aplikacija nije otvorila, pišite na aleksandar.pejkovic@budzetplus.rs. Vaši podaci su sačuvani u formi.';
      feedback.style.color = '#2563eb';
    } catch (err) {
      feedback.textContent = 'Nismo mogli da otvorimo email klijent. Pošaljite nas ručno na aleksandar.pejkovic@budzetplus.rs.';
      feedback.style.color = '#dc2626';
    }

  });

  // Lazy-load videos on click to avoid mreža zahtev dok korisnik ne zatraži
  const lazyVideos = Array.from(document.querySelectorAll('.lazy-video'));
  lazyVideos.forEach((video) => {
    const wrapper = video.closest('.lazy-video-wrap');
    const trigger = wrapper ? wrapper.querySelector('.video-play') : null;
    const src = video.dataset.src;
    const poster = video.dataset.poster;
    if (poster) {
      video.setAttribute('poster', poster);
    }
    const loadAndPlay = () => {
      if (!src) return;
      if (!video.dataset.loaded) {
        video.src = src;
        video.dataset.loaded = 'true';
        video.setAttribute('controls', 'controls');
      }
      wrapper && wrapper.classList.add('is-playing');
      video.play().catch(() => {
        /* ignore autoplay block */
      });
    };
    trigger && trigger.addEventListener('click', loadAndPlay);
    video.addEventListener('click', loadAndPlay);
  });

  // Lightbox za screenshotove
  const screenshots = Array.from(document.querySelectorAll('.card.screenshot img'));
  if (screenshots.length) {
    const overlay = document.createElement('div');
    overlay.className = 'lightbox hidden';
    overlay.innerHTML = '<div class="lightbox-backdrop"></div><img class="lightbox-img" alt="">';
    document.body.appendChild(overlay);
    const lightboxImg = overlay.querySelector('.lightbox-img');

    const close = () => {
      overlay.classList.add('hidden');
      if (lightboxImg) lightboxImg.src = '';
    };

    overlay.addEventListener('click', close);
    document.addEventListener('keyup', (e) => {
      if (e.key === 'Escape') close();
    });

    screenshots.forEach((img) => {
      const parentLink = img.closest('a');
      const targetSrc = parentLink ? parentLink.getAttribute('href') || img.src : img.src;
      img.style.cursor = 'zoom-in';
      (parentLink || img).addEventListener('click', (e) => {
        e.preventDefault();
        if (!lightboxImg || !targetSrc) return;
        lightboxImg.src = targetSrc;
        lightboxImg.alt = img.alt || '';
        overlay.classList.remove('hidden');
      });
    });
  }
})();
