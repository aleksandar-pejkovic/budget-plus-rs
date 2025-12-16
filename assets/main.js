// Smooth scroll offset correction and contact form feedback
(function () {
  const form = document.getElementById('contact-form');
  const feedback = form ? form.querySelector('.form-feedback') : null;
  const inputs = form ? Array.from(form.querySelectorAll('input, textarea')) : [];

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

  if (!form || !feedback) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const missing = inputs.some((input) => !input.value.trim());
    if (missing) {
      feedback.textContent = 'Molimo popunite sva polja.';
      feedback.style.color = '#dc2626';
      return;
    }

    feedback.textContent = 'Hvala, javljamo se uskoro.';
    feedback.style.color = '#2563eb';
    form.reset();
  });
})();
