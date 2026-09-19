(() => {
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');
  if (menu && nav) {
    menu.hidden = false;
    nav.classList.add('menu-ready');
    const closeMenu = () => { nav.classList.remove('is-open'); menu.setAttribute('aria-expanded', 'false'); };
    menu.addEventListener('click', () => {
      const open = menu.getAttribute('aria-expanded') !== 'true';
      nav.classList.toggle('is-open', open);
      menu.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && nav.classList.contains('is-open')) { closeMenu(); menu.focus(); }
    });
    window.matchMedia('(min-width: 961px)').addEventListener('change', closeMenu);
  }

  // Keep native anchors/history; reveal folded destinations before navigation.
  document.querySelectorAll('a[href="#privatnost"]').forEach(link => link.addEventListener('click', () => {
    const disclosure = document.querySelector('#privatnost details');
    if (disclosure) disclosure.open = true;
  }));

  const dialog = document.querySelector('.image-dialog');
  if (dialog && typeof dialog.showModal === 'function') {
    let opener;
    document.querySelectorAll('.zoom-image').forEach(link => link.addEventListener('click', event => {
      event.preventDefault();
      opener = link;
      const image = link.querySelector('img');
      dialog.querySelector('img').src = link.href;
      dialog.querySelector('img').alt = image?.alt || 'Prikaz programa';
      dialog.querySelector('figcaption').textContent = image?.alt || 'Prikaz programa';
      document.body.classList.add('dialog-open');
      dialog.showModal();
      dialog.querySelector('.dialog-close').focus();
    }));
    dialog.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => {
      if (event.target !== dialog) return;
      const box = dialog.getBoundingClientRect();
      if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close();
    });
    dialog.addEventListener('close', () => {
      document.body.classList.remove('dialog-open');
      dialog.querySelector('img').removeAttribute('src');
      opener?.focus({ preventScroll: true });
    });
  }

  const video = document.getElementById('demo-video');
  const choices = document.querySelectorAll('.video-choice');
  choices.forEach(button => {
    button.setAttribute('aria-pressed', String(button.classList.contains('is-active')));
    button.addEventListener('click', () => {
      if (!video) return;
      video.pause();
      video.src = button.dataset.video;
      video.poster = button.dataset.poster;
      video.setAttribute('aria-label', button.dataset.title);
      document.getElementById('demo-title').textContent = button.dataset.title;
      choices.forEach(choice => {
        choice.classList.toggle('is-active', choice === button);
        choice.setAttribute('aria-pressed', String(choice === button));
      });
      video.load();
      video.focus({ preventScroll: true });
      video.scrollIntoView({ block: 'center', behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
    });
  });
})();
