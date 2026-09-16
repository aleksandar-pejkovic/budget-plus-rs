// Smooth scroll offset correction and contact form feedback
(function () {
  const form = document.getElementById('contact-form');
  const feedback = form ? form.querySelector('.form-feedback') : null;
  const jbkjsInput = form ? form.querySelector('[name="jbkjs"]') : null;
  const requiredInputs = form ? Array.from(form.querySelectorAll('[required]')) : [];
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
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });

  document.querySelectorAll('.js-presentation-interest').forEach((link) => {
    link.addEventListener('click', () => {
      if (!form) return;
      const message = form.querySelector('[name="message"]');
      const heading = form.querySelector('.form-heading h3');
      const description = form.querySelector('.form-heading p');
      const submitButton = form.querySelector('[type="submit"]');
      if (!message) return;
      message.value = 'Želim da se prijavim za narednu prezentaciju programa Budžet+. Molim vas da me obavestite kada bude određen termin.';
      if (heading) heading.textContent = 'Prijava za prezentaciju';
      if (description) description.textContent = 'Unesite svoje podatke da bismo vas obavestili kada bude određen termin.';
      if (submitButton) submitButton.textContent = 'Pošalji prijavu';
      window.setTimeout(() => message.focus(), 500);
    });
  });

  if (!form || !feedback) return;

  if (jbkjsInput) {
    jbkjsInput.addEventListener('input', () => {
      jbkjsInput.value = jbkjsInput.value.replace(/\D/g, '').slice(0, 5);
    });
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const missing = requiredInputs.some((input) => !input.value.trim());
    if (missing) {
      feedback.textContent = 'Molimo popunite sva polja.';
      feedback.style.color = '#dc2626';
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
      formData.message || '',
    ].filter(Boolean);

    const isPresentationSignup = (formData.message || '').startsWith('Želim da se prijavim za narednu prezentaciju');
    const subject = isPresentationSignup ? 'Prijava za Budžet+ prezentaciju - ' : 'Budžet+ upit - ';
    const mailto = `mailto:aleksandar.pejkovic@budzetplus.rs?subject=${encodeURIComponent(subject + (formData.name || ''))}&body=${encodeURIComponent(lines.join('\n'))}`;

    try {
      window.location.href = mailto;
      feedback.textContent = 'Otvorili smo email sa popunjenim detaljima — pošaljite ga da stigne do nas.';
      feedback.style.color = '#2563eb';
    } catch (err) {
      feedback.textContent = 'Nismo mogli da otvorimo email klijent. Pošaljite nas ručno na aleksandar.pejkovic@budzetplus.rs.';
      feedback.style.color = '#dc2626';
    }

    setTimeout(() => {
      form.reset();
      const heading = form.querySelector('.form-heading h3');
      const description = form.querySelector('.form-heading p');
      const submitButton = form.querySelector('[type="submit"]');
      if (heading) heading.textContent = 'Imate pitanje?';
      if (description) description.textContent = 'Za pitanja koja nisu vezana za zakazivanje termina, pošaljite nam poruku.';
      if (submitButton) submitButton.textContent = 'Pošalji zahtev';
    }, 300);
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
