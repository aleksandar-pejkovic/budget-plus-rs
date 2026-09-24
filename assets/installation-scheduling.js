(() => {
  const target = document.getElementById('installation-scheduling-target');
  const link = document.getElementById('installation-calendar-link');
  if (!target || !link) return;

  const stylesheet = document.createElement('link');
  stylesheet.rel = 'stylesheet';
  stylesheet.href = 'https://calendar.google.com/calendar/scheduling-button-script.css';
  document.head.append(stylesheet);

  const script = document.createElement('script');
  script.src = 'https://calendar.google.com/calendar/scheduling-button-script.js';
  script.async = true;
  script.addEventListener('load', () => {
    if (!window.calendar?.schedulingButton?.load) return;
    window.calendar.schedulingButton.load({
      url: link.href,
      color: '#1d4ed8',
      label: link.textContent.trim(),
      target,
    });
  });
  document.head.append(script);
})();
