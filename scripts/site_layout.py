"""Shared site chrome for the homepage and generated solution pages."""
from html import escape


def header(prefix="", topic=""):
    signup = f'{prefix}?tema={escape(topic)}#kontakt' if topic else '#kontakt'
    return f'''<a class="skip-link" href="#main-content">Pređite na sadržaj</a>
<header class="site-header"><div class="container header-inner">
  <a class="brand" href="{prefix or './'}" aria-label="Budžet+ — početna"><img src="{prefix}assets/img/budget_plus_logo.ico" width="36" height="36" alt=""><span>Budžet<span class="brand-plus">+</span></span></a>
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" hidden>Meni <span aria-hidden="true">☰</span></button>
  <nav class="site-nav" id="site-nav" aria-label="Glavna navigacija">
    <a href="{prefix}#mogucnosti">Mogućnosti</a><a href="{prefix}#resenja">Rešenja</a><a href="{prefix}#video">Program u radu</a><a href="{prefix}#podrska">Podrška</a>
    <a class="btn primary nav-cta" href="{signup}">Prijavite se za prezentaciju <span aria-hidden="true">↗</span></a>
  </nav>
</div></header>'''


def footer(prefix=""):
    return f'''<footer class="site-footer"><div class="container footer-top">
  <div><a class="brand" href="{prefix or './'}">Budžet<span class="brand-plus">+</span></a><p>Budžetsko računovodstvo za škole.<br>Od dokumenta do izveštaja.</p></div>
  <div><p class="footer-label">Razgovarajmo</p><a href="mailto:aleksandar.pejkovic@budzetplus.rs">aleksandar.pejkovic@budzetplus.rs</a><a href="tel:+381659170989">065 917 0989</a></div>
  <div><p class="footer-label">Sledeći korak</p><a href="{prefix}#kontakt">Prijava za prezentaciju</a><a href="https://calendar.app.google/avk76s3wR3UF75UR6" target="_blank" rel="noopener">Zakažite instalaciju ↗</a><a href="{prefix}#privatnost">Privatnost</a></div>
</div><div class="container footer-bottom"><p>© Alpeon Softver · Budžet+</p><details><summary>Podaci o preduzetniku</summary><p>ALEKSANDAR PEJKOVIĆ PR IZDAVANJE SOFTVERA ALPEON SOFTVER OBREŽ<br>PIB: 115450263 · MB: 68375762<br>Prvomajska 14, 37266 Obrež, Varvarin, Srbija</p></details></div></footer>
<dialog class="image-dialog" aria-labelledby="image-caption"><button class="dialog-close" type="button" aria-label="Zatvorite prikaz">Zatvori <span aria-hidden="true">×</span></button><figure><img alt=""><figcaption id="image-caption"></figcaption></figure></dialog>
<script src="{prefix}assets/main.js" defer></script>'''
