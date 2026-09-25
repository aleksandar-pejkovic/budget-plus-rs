"""Generate the homepage body while preserving its product/organization metadata."""
import json
import re
from pathlib import Path
from html import escape
from site_layout import header, footer, INSTALLATION_URL

ROOT = Path(__file__).resolve().parents[1]

MODULES = [
    ("knjizenje", "Knjiženje", "E-fakture, SPIRI izvodi i ISKRA obračuni, uključujući knjiženje isplata avansa i zatvaranje avansa konačnom fakturom — uz vašu proveru.", [
        ("program-za-racunovodstvo-skola", "Povezane evidencije"),
        ("knjizenje-e-faktura-za-skole", "SEF i masovno knjiženje"),
        ("spiri-izvodi-skole", "SPIRI izvodi"),
        ("iskra-obracuni-knjizenje", "ISKRA obračuni")]),
    ("spiri-placanja", "Priprema plaćanja", "Pripremite više SPIRI plaćanja odjednom i sačuvajte šablone redovnih obaveza.", [
        ("spiri-kumulativno-placanje", "Plaćanje više e-faktura"),
        ("rucni-unos-spiri-placanja", "Ručni unos i šabloni")]),
    ("budzet", "Planiranje i izvršenje budžeta", "Učitajte finansijski plan iz IFISUP-a i pratite izvršenje i odstupanja.", [
        ("izvrsenje-budzeta-skola", "Plan i izvršenje")]),
    ("izvestaji", "Računovodstveni izveštaji", "Glavna knjiga, kartice i bilansi, Obrazac 5 za ISPFI i ORIS izvoz iz postojećih knjiženja.", [
        ("obrazac-5-ispfi", "Obrazac 5 za ISPFI"),
        ("oris-izvoz-za-skole", "ORIS izvoz")]),
    ("sredstva", "Osnovna sredstva", "Iz e-fakture pripremite povezano knjiženje i evidenciju osnovnih sredstava. Obračunajte amortizaciju i pripremite popis.", [
        ("osnovna-sredstva-skola", "Evidencija, amortizacija i popis")]),
    ("ucenici", "Uplate učenika", "Pratite zaduženja i uplate po učeniku, odeljenju i aktivnosti.", [
        ("uplate-ucenika", "Zaduženja i uplate")]),
    ("godina", "Zatvaranje poslovne godine", "Pripremite završne naloge i prenesite salda u novu poslovnu godinu.", [
        ("zatvaranje-poslovne-godine", "Zatvaranje i prenos salda")]),
]

VIDEOS = [
    ("knjizenje-faktura", "E-fakture", "rucni-unos-promene.png"),
    ("knjizenje-izvoda", "SPIRI izvodi", "kon-tabla.png"),
    ("knjizenje-plate", "Obračun plate", "nalog-za-knjizenje.jpg"),
    ("knjizenje-bolovanja", "Obračun bolovanja", "nalog-za-knjizenje.jpg"),
    ("knjizenje-obracuna-prevoza", "Obračun prevoza", "rucni-unos-promene.png"),
    ("generisanje-spiri-fajla", "Priprema SPIRI plaćanja", "kon-tabla.png"),
    ("ucitavanje-fajla-za-kumulativno-placanje", "Učitavanje u SPIRI", "kon-tabla.png"),
    ("generisanje-obrazac-5-fajla", "Obrazac 5", "kon-tabla.png"),
    ("izvrsenje-budzeta", "Izvršenje budžeta", "grafikoni.png"),
    ("kreiranje-naloga-za-knjizenje", "Nalog za knjiženje", "nalog-za-knjizenje.jpg"),
    ("tema-i-boje", "Izgled programa", "kon-tabla.png"),
]

FAQ = [
    ("Kako izgleda prezentacija?", "Prolazimo kroz mogućnosti programa i konkretne poslove školskog računovodstva. Prijavite interesovanje, a o terminu naredne prezentacije obavestićemo vas emailom."),
    ("Da li su podaci kod nas?", "Program radi lokalno na vašem računaru. Za povezivanje sa državnim sistemima i preuzimanje podataka iz njih potrebna je internet veza."),
    ("Da li program zamenjuje proveru računovođe?", "Ne. Automatizacija smanjuje prepisivanje podataka, a računovođa proverava dokument, klasifikaciju i rezultat knjiženja."),
    ("Kako počinje korišćenje?", "Posle prezentacije dogovaramo uvođenje i instalaciju. Ako ste već spremni, termin instalacije možete izabrati preko linka za zakazivanje."),
    ("Kakva podrška je dostupna?", "Podrška obuhvata instalaciju, podešavanje i korišćenje Budžet+ programa. Dostupna je radnim danima od 9 do 15 časova, telefonom, emailom, putem Viber-a ili WhatsApp-a. Rad na daljinu dogovaramo prema potrebi."),
]


def render_body():
    videos = "".join(f'<button type="button" class="video-choice" data-video="assets/media/{slug}.mp4" data-poster="assets/img/{poster}" data-title="{label}"><span class="play-small" aria-hidden="true">▷</span>{label}<span aria-hidden="true">↗</span></button>' for slug, label, poster in VIDEOS)
    faq = "".join(f'<details class="faq-item"><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q, a in FAQ)
    module_html = "".join(
        f'<article class="capability" id="{anchor}"><div class="capability-copy"><h3>{title}</h3><p>{description}</p></div><div class="capability-links">'
        + "".join(f'<a href="{slug}/">{label} <span aria-hidden="true">↗</span></a>' for slug, label in links)
        + '</div></article>' for anchor, title, description, links in MODULES
    )
    return f'''<body>
{header()}
<main id="main-content">
<section class="hero" id="pocetna"><div class="container hero-grid">
  <div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> Za računovođe u osnovnim i srednjim školama</p>
    <h1>Budžetsko računovodstvo za škole <span>— od dokumenta do izveštaja.</span></h1>
    <div class="hero-intro"><p>Budžet+ priprema naloge za knjiženje na osnovu e-faktura, SPIRI izvoda i ISKRA obračuna. Vi proveravate i potvrđujete pripremljene naloge.</p><p>Iz proknjiženih podataka pripremate računovodstvene izveštaje, Obrazac 5 za ISPFI i ORIS izvoz.</p></div>
    <p class="hero-benefit">Manje vremena za unos. Više vremena za kontrolu.</p>
    <div class="cta-group"><a class="btn primary" href="#kontakt">Prijavite se za prezentaciju <span aria-hidden="true">↗</span></a><a class="text-link" href="#video"><span aria-hidden="true">▷</span> Pogledajte program</a></div>
    <p class="hero-phone">Radije biste razgovarali? <a href="tel:+381659170989">065 917 0989</a></p>
  </div>
  <div class="trust-strip"><p>Razvija ga <strong>školski računovođa</strong> u saradnji sa kolegama iz prakse.</p><p>Koristi ga <strong>više od 50 škola.</strong></p><p>Lokalna instalacija. <strong>Podaci ostaju u ustanovi.</strong></p></div>
  <figure class="hero-product"><div class="product-label"><span class="status-dot"></span> Budžet+ <span>Pregled modula</span></div><a class="zoom-image" href="assets/img/demo-kontrolna-tabla.png"><img src="assets/img/demo-kontrolna-tabla.png" alt="Pregled modula u Budžet+ programu: nalozi, e-fakture, izveštaji i evidencije" width="1280" height="617" fetchpriority="high"></a><figcaption><div>Knjiženje. Evidencije. Izveštaji.<small>Demonstracioni podaci. Izgled zavisi od verzije.</small></div><span aria-hidden="true">↗</span></figcaption></figure>
</div></section>

<section class="section author-section" aria-labelledby="autor-naslov"><div class="container author-grid">
  <div><p class="eyebrow">Aleksandar Pejković · autor programa</p><h2 id="autor-naslov">Iz svakodnevnog rada u školskom računovodstvu.</h2></div>
  <div class="author-copy"><p>Ja sam Aleksandar Pejković, računovođa u osnovnoj školi i autor programa Budžet+. Program je nastao iz potreba mog svakodnevnog rada, a razvijam ga u saradnji sa kolegama iz prakse.</p><p>Polazim od konkretnih poslova koje obavljamo: knjiženja faktura i izvoda, pripreme plaćanja, praćenja izvršenja finansijskog plana i sastavljanja izveštaja.</p></div>
</div></section>

<section class="section capabilities-section" id="mogucnosti"><div class="container" id="resenja"><div class="section-heading"><div><p class="eyebrow">Jedan program, povezane evidencije</p><h2>Poslovi koje obavljate u Budžet+ programu</h2></div></div><div class="capabilities">{module_html}</div></div></section>

<section class="section demo-section" id="video"><div class="container"><div class="section-heading"><div><p class="eyebrow">Pogledajte pre nego što odlučite</p><h2>Program u svakodnevnom radu.</h2></div><p>Stvarni prikazi programa, od unosa dokumenta do pregleda rezultata.</p></div><div class="demo-layout"><div class="demo-player"><div class="video-frame"><video id="demo-video" controls playsinline preload="none" poster="assets/img/kon-tabla.png" aria-label="Prezentacija programa Budžet+"><source src="assets/media/budget-plus-prezentacija.mp4" type="video/mp4"><a href="assets/media/budget-plus-prezentacija.mp4">Preuzmite prezentaciju</a></video></div><div class="demo-caption"><h3 id="demo-title">Upoznajte Budžet+</h3><p>Video-prikazi su iz starije verzije programa. Aktuelni izgled pojedinih ekrana može se razlikovati.</p></div></div><div class="video-library" aria-label="Izbor video-prikaza"><button class="video-choice is-active" type="button" aria-pressed="true" data-video="assets/media/budget-plus-prezentacija.mp4" data-poster="assets/img/kon-tabla.png" data-title="Upoznajte Budžet+"><span class="play-small" aria-hidden="true">▷</span> Pregled programa <span aria-hidden="true">↗</span></button>{videos}</div></div><noscript><p>Kratke prikaze možete pogledati tokom prezentacije. Glavni video je dostupan iznad.</p></noscript></div></section>

<section class="section" id="podrska"><div class="container"><div class="section-heading"><div><p class="eyebrow">Od prvog razgovora do svakodnevnog rada</p><h2>Uvođenje i pomoć u korišćenju programa.</h2></div><p>Dogovaramo instalaciju, pripremu za početak rada i prolazimo kroz korišćenje Budžet+ programa.</p></div><div class="onboarding-grid"><article><span class="step-number">01</span><h3>Upoznajte program</h3><p>Prijavite se za prezentaciju i pogledajte mogućnosti koje su važne vašoj školi.</p></article><article><span class="step-number">02</span><h3>Dogovorite uvođenje</h3><p>Prolazimo kroz instalaciju i pripremu za početak rada.</p><div class="installation-scheduling"><span id="installation-scheduling-target"></span><a class="text-link" id="installation-calendar-link" href="{INSTALLATION_URL}" target="_blank" rel="noopener">Otvorite kalendar za instalaciju ↗</a></div></article><article><span class="step-number">03</span><h3>Podrška za rad u programu</h3><p>Za pitanja o korišćenju Budžet+ programa podrška je dostupna radnim danima od 9 do 15 časova.</p><a class="text-link" href="tel:+381659170989">065 917 0989</a></article></div></div></section>

<section class="section faq-section" id="faq"><div class="container faq-grid"><div><p class="eyebrow">Pre nego što se upoznamo</p><h2>Odgovori na česta pitanja.</h2><p>Za sve ostalo, tu smo.</p><a class="text-link js-question" href="#kontakt">Postavite pitanje <span aria-hidden="true">↗</span></a></div><div class="faq-list">{faq}</div></div></section>

<section class="section contact-section" id="kontakt"><div class="container contact-grid"><div class="contact-copy"><p class="eyebrow">Sledeći korak</p><h2>Pogledajte kako bi izgledao vaš rad uz Budžet+.</h2><p>Prijavite se za narednu prezentaciju. O terminu ćemo vas obavestiti emailom.</p><div class="contact-direct"><p>Više vam odgovara razgovor?</p><a class="contact-phone" href="tel:+381659170989">065 917 0989 <span aria-hidden="true">↗</span></a><a href="mailto:aleksandar.pejkovic@budzetplus.rs">aleksandar.pejkovic@budzetplus.rs</a><div class="contact-channels"><a href="viber://chat?number=381659170989">Viber</a><a href="https://wa.me/381659170989" target="_blank" rel="noopener">WhatsApp ↗</a></div><small>Radnim danima 9–15h</small></div></div>
<form id="contact-form" class="contact-form" novalidate><div class="form-heading"><p class="eyebrow">Upoznajmo se</p><h3 id="form-title">Prijava za prezentaciju</h3><p id="form-description">Unesite podatke škole i email na koji možemo da vam se javimo.</p><button class="form-mode-switch text-link" type="button">Želim da postavim pitanje</button></div><div class="form-fields">
<label for="contact-name">Ime i prezime<input id="contact-name" name="name" autocomplete="name" required maxlength="100" aria-describedby="error-name"><small class="field-error" id="error-name"></small></label>
<label for="contact-org">Naziv škole<input id="contact-org" name="org" autocomplete="organization" required maxlength="200" aria-describedby="error-org"><small class="field-error" id="error-org"></small></label>
<label for="contact-jbkjs">JBKJS<input id="contact-jbkjs" name="jbkjs" inputmode="numeric" pattern="[0-9]{{5}}" maxlength="5" required aria-describedby="jbkjs-hint error-jbkjs"><small class="field-hint" id="jbkjs-hint">Petocifreni broj korisnika javnih sredstava.</small><small class="field-error" id="error-jbkjs"></small></label>
<label for="contact-email">Email za odgovor<input id="contact-email" name="email" type="email" autocomplete="email" required maxlength="254" aria-describedby="error-email"><small class="field-error" id="error-email"></small></label>
<label for="contact-phone">Telefon <span class="optional">(opciono)</span><input id="contact-phone" name="phone" type="tel" autocomplete="tel" maxlength="40" aria-describedby="error-phone"><small class="field-error" id="error-phone"></small></label>
<label class="full-width" for="contact-message"><span id="message-label">Napomena <span class="optional">(opciono)</span></span><textarea id="contact-message" name="message" rows="3" maxlength="2000" aria-describedby="error-message"></textarea><small class="field-error" id="error-message"></small></label></div>
<div id="turnstile-container" role="group" aria-label="Provera protiv neželjenih prijava"></div><p class="form-privacy">Podatke koristimo za odgovor na vaš upit i dogovor o prezentaciji. <a href="#privatnost">Kako obrađujemo podatke</a></p><button class="btn primary full" type="submit">Prijavite se za prezentaciju <span aria-hidden="true">↗</span></button><p class="form-feedback" role="status" aria-live="polite" tabindex="-1"></p><p class="form-fallback">Možete nam i <a href="mailto:aleksandar.pejkovic@budzetplus.rs">poslati email</a>.</p><noscript><p>Za slanje forme uključite JavaScript ili nam pišite direktno emailom.</p></noscript></form></div></section>
<section class="privacy-section" id="privatnost"><div class="container"><details><summary>Privatnost i obrada podataka</summary><div><p>Alpeon Softver koristi podatke koje unesete da odgovori na upit i dogovori prezentaciju. Slanjem forme ne prijavljujete se na marketinšku listu.</p><p>Prijava se obrađuje preko Cloudflare servisa i prosleđuje na naš poslovni email. Ne formiramo posebnu bazu prijava na sajtu. Cloudflare Turnstile služi za zaštitu forme od neželjenih zahteva.</p><p>Za pitanja o vašim podacima i zahtev za brisanje prepiske pišite na <a href="mailto:aleksandar.pejkovic@budzetplus.rs">aleksandar.pejkovic@budzetplus.rs</a>. Sajt koristi Google Analytics za statistiku poseta; sadržaj forme ne šaljemo u analitiku.</p></div></details></div></section>
</main>{footer()}
<script src="assets/contact-config.js"></script><script src="assets/contact.js" type="module"></script>
<script src="assets/installation-scheduling.js" defer></script>
</body></html>'''


def main():
    target = ROOT / "index.html"
    head = target.read_text(encoding="utf-8").split("<body", 1)[0]
    # Keep business identity metadata; FAQ must match the redesigned visible content.
    def update_schema(match):
        data = json.loads(match.group(1))
        if data.get('@type') == 'FAQPage':
            data['mainEntity'] = [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]
            return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'
        return match.group(0)
    head = re.sub(r'<script type="application/ld\+json">(.*?)</script>', update_schema, head, flags=re.S)
    target.write_text(head + render_body() + '\n', encoding="utf-8")


if __name__ == "__main__":
    main()
