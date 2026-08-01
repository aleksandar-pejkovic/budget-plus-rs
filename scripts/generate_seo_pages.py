#!/usr/bin/env python3
"""Generate the static SEO landing pages from a small, reviewed content model."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://budzetplus.rs"

PAGES = [
    {
        "slug": "program-za-racunovodstvo-skola",
        "title": "Program za računovodstvo škola | Budžet+ za škole",
        "description": "Program za računovodstvo osnovnih i srednjih škola: e-fakture, SPIRI, ISKRA, Obrazac 5, kontrole i izveštaji bez ručnog prepisivanja.",
        "kicker": "Budžet+ za škole",
        "h1": "Program za računovodstvo škola napravljen za stvarni školski rad",
        "intro": "Budžet+ povezuje svakodnevno knjiženje, e-fakture, SPIRI, ISKRA obračune i Obrazac 5. Program radi lokalno, podatke obrađuje precizno i računovođi ostavlja kontrolu umesto prepisivanja.",
        "summary_title": "Na jednom mestu",
        "summary": ["Automatsko knjiženje e-faktura", "SPIRI izvodi i kumulativno plaćanje", "ISKRA obračuni i Obrazac 5", "Kontrole, analitike i izveštaji"],
        "sections": [
            ("Zašto poseban program za škole?", "Školsko računovodstvo ima sopstvene rokove, klasifikacije i tokove podataka. Budžet+ je usmeren na te procese, pa se isti podatak ne unosi ponovo u različite evidencije. Iz jednog preciznog knjiženja nastaju pregledi po izvoru, mestu troška, partneru i programu."),
            ("Od dokumenta do kontrolisanog naloga", "Program učitava dostupne podatke iz e-faktura, SPIRI izvoda i ISKRA fajlova, priprema nalog i primenjuje kontrole. Računovođa proverava rezultat pre konačnog knjiženja, umesto da svaku stavku ručno prepisuje."),
            ("Izveštaji koji ne počinju novim unosom", "Obrazac 5, bilansi i pregledi izvršenja budžeta koriste već proknjižene podatke. Time se skraćuje priprema izveštaja i smanjuje rizik da se dve evidencije razlikuju."),
            ("Uvođenje bez prekida rada", "Instalaciju i početno podešavanje radimo zajedno. Početna stanja se mogu uvesti kroz pripremljene Excel šablone, a podrška je dostupna telefonom, emailom, Viberom, WhatsAppom, AnyDesk-om ili Teams-om."),
        ],
        "process_title": "Kako izgleda početak",
        "process": ["Zakažemo prezentaciju i utvrdimo koje procese škola koristi.", "Instaliramo program i podešavamo nalog i šifarnike.", "Uvozimo početno stanje i proveravamo podatke.", "Prvi dokument knjižimo zajedno, uz objašnjenje kontrola."],
        "related": [("SPIRI kumulativno plaćanje", "../spiri-kumulativno-placanje/"), ("Obrazac 5 za ISPFI", "../obrazac-5-ispfi/"), ("Knjiženje e-faktura", "../knjizenje-e-faktura-za-skole/")],
    },
    {
        "slug": "spiri-kumulativno-placanje",
        "title": "SPIRI kumulativno plaćanje e-faktura | Budžet+",
        "description": "Budžet+ povlači podatke sa e-faktura i kreira fajl za kumulativno plaćanje koji korisnik učitava u SPIRI — više faktura, jedan fajl.",
        "kicker": "Više faktura, jedan fajl",
        "h1": "SPIRI kumulativno plaćanje bez ručnog prepisivanja",
        "intro": "Budžet+ povuče podatke sa e-faktura, objedini izabrane obaveze i kreira fajl za kumulativno plaćanje. Korisnik proveri podatke i gotov fajl učita u SPIRI.",
        "summary_title": "Tačan tok rada",
        "summary": ["Podaci se preuzimaju sa e-faktura", "Bira se više faktura za plaćanje", "Budžet+ kreira kumulativni fajl", "Korisnik učitava fajl u SPIRI"],
        "sections": [
            ("Šta znači kumulativno plaćanje?", "Umesto pripreme zasebnog fajla za svaku obavezu, više izabranih e-faktura objedinjeno je u jedan fajl za kumulativno plaćanje. Time se skraćuje administrativni deo posla, dok računovođa zadržava završnu proveru."),
            ("Odakle dolaze podaci?", "Budžet+ koristi podatke dostupne na e-fakturama. Iznosi, partneri i drugi potrebni elementi ne prepisuju se ručno u novi dokument, čime se smanjuje mogućnost zamene cifre ili partnera."),
            ("Šta Budžet+ radi, a šta radi korisnik?", "Program priprema fajl; korisnik pregleda podatke i učitava kreirani fajl u SPIRI. Budžet+ ne šalje plaćanje samostalno i ne uklanja obaveznu računovodstvenu kontrolu."),
            ("Samostalni SPIRI modul", "Kumulativno plaćanje i rad sa SPIRI izvodima mogu se koristiti kao samostalni modul, bez uvođenja kompletnog računovodstvenog paketa."),
        ],
        "process_title": "Od e-faktura do SPIRI fajla",
        "process": ["Budžet+ preuzme podatke sa dostupnih e-faktura.", "Korisnik označi fakture koje ulaze u kumulativno plaćanje.", "Program proveri i objedini podatke u jedan fajl.", "Korisnik pregleda rezultat i učita fajl u SPIRI."],
        "related": [("Knjiženje e-faktura", "../knjizenje-e-faktura-za-skole/"), ("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("Obrazac 5 za ISPFI", "../obrazac-5-ispfi/")],
    },
    {
        "slug": "obrazac-5-ispfi",
        "title": "Obrazac 5 za ISPFI bez ručnog unosa | Budžet+",
        "description": "Budžet+ priprema Obrazac 5 iz proknjiženih podataka, uz kontrole i izvoz fajla spremnog za učitavanje u ISPFI.",
        "kicker": "Iz proknjiženih podataka",
        "h1": "Obrazac 5 spreman za ISPFI bez ponovnog kucanja",
        "intro": "Budžet+ koristi već kontrolisane i proknjižene podatke da pripremi Obrazac 5. Korisnik proverava rezultat i izvozi fajl spreman za učitavanje u ISPFI.",
        "summary_title": "Manje koraka do izveštaja",
        "summary": ["Nema ponovnog unosa istih podataka", "Kontrole pre izvoza", "Brza priprema Obrasca 5", "Fajl spreman za ISPFI"],
        "sections": [
            ("Zašto je važan jedan izvor podataka?", "Kada se Obrazac 5 priprema iz postojećih knjiženja, nema paralelne evidencije koju treba ponovo usklađivati. Promene u nalogu odražavaju se na podatke iz kojih nastaje izveštaj."),
            ("Kontrola pre izvoza", "Pre završnog izvoza računovođa može da pregleda podatke i reaguje na označene neusaglašenosti. Automatizacija ubrzava pripremu, ali odluka o konačnoj tačnosti ostaje kod korisnika."),
            ("Fajl za ISPFI", "Nakon provere Budžet+ generiše fajl u formatu predviđenom za dalji rad u ISPFI. Tako se izbegava ručno kucanje Obrasca 5 u više koraka."),
            ("Izveštaj bez događaja u kalendaru", "Obrazac 5 više ne mora da bude višesatni poseban posao pred rok. Kada su knjiženja ažurna, priprema se svodi na pregled, kontrolu i izvoz."),
        ],
        "process_title": "Kako nastaje Obrazac 5",
        "process": ["Budžet+ koristi podatke iz završenih knjiženja.", "Program formira potrebne stavke i pokreće kontrole.", "Računovođa pregleda rezultat i ispravlja eventualne neusaglašenosti.", "Program izvozi fajl spreman za učitavanje u ISPFI."],
        "related": [("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("SPIRI kumulativno plaćanje", "../spiri-kumulativno-placanje/"), ("ISKRA obračuni", "../iskra-obracuni-knjizenje/")],
    },
    {
        "slug": "knjizenje-e-faktura-za-skole",
        "title": "Automatsko knjiženje e-faktura za škole | Budžet+",
        "description": "Učitajte podatke sa e-faktura, formirajte kontrolisan nalog i pripremite SPIRI kumulativno plaćanje bez ručnog prepisivanja.",
        "kicker": "Od e-fakture do naloga",
        "h1": "Knjiženje e-faktura za škole bez prepisivanja",
        "intro": "Budžet+ preuzima dostupne podatke sa e-fakture, priprema nalog za knjiženje i omogućava računovođi da proveri rezultat pre evidentiranja.",
        "summary_title": "Šta se automatizuje",
        "summary": ["Učitavanje podataka sa e-fakture", "Prepoznavanje partnera i stavki", "Priprema naloga i kontrola", "Podaci za SPIRI kumulativni fajl"],
        "sections": [
            ("Bez prepisivanja istog dokumenta", "Podaci koji već postoje na e-fakturi koriste se za pripremu naloga. Time se uklanja rutinski unos i smanjuje mogućnost greške pri prepisivanju iznosa, datuma ili partnera."),
            ("Partneri i klasifikacija", "Budžet+ može da koristi podatke sa dokumenta za rad sa partnerima i pripremu knjiženja. Računovođa proverava klasifikaciju i dopunjava ono što zahteva stručnu odluku."),
            ("Kontrola pre knjiženja", "Automatski pripremljen nalog nije crna kutija: korisnik vidi stavke i potvrđuje rezultat. Kontrole pomažu da se neusaglašenosti uoče pre završnog knjiženja."),
            ("Veza sa SPIRI plaćanjem", "Isti podaci sa e-faktura mogu se koristiti za kreiranje fajla za kumulativno plaćanje. Izabrane fakture se objedinjuju, a korisnik gotov fajl učitava u SPIRI."),
        ],
        "process_title": "Kako se knjiži e-faktura",
        "process": ["Učitajte ili preuzmite podatke sa e-fakture.", "Budžet+ pripremi partnera, stavke i nalog.", "Pregledajte klasifikaciju i označene kontrole.", "Potvrdite knjiženje i po potrebi uključite fakturu u SPIRI fajl."],
        "related": [("SPIRI kumulativno plaćanje", "../spiri-kumulativno-placanje/"), ("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("Obrazac 5 za ISPFI", "../obrazac-5-ispfi/")],
    },
    {
        "slug": "iskra-obracuni-knjizenje",
        "title": "ISKRA obračuni i automatsko knjiženje | Budžet+",
        "description": "Budžet+ priprema ISKRA obračune plata, bolovanja i prevoza za precizno knjiženje bez ručnog unosa svake stavke.",
        "kicker": "Plate, bolovanja i prevoz",
        "h1": "ISKRA obračuni spremni za knjiženje u sekundama",
        "intro": "Umesto ručnog unosa stavku po stavku, Budžet+ učitava podatke iz ISKRA obračuna i priprema nalog koji računovođa može da pregleda i potvrdi.",
        "summary_title": "Jedan kontrolisan proces",
        "summary": ["Obračuni plata", "Knjiženje bolovanja", "Obračun prevoza", "Pregled naloga pre potvrde"],
        "sections": [
            ("Manje rutine u složenom obračunu", "ISKRA fajlovi sadrže podatke koji bi se inače ponovo unosili u računovodstveni nalog. Budžet+ ih koristi za pripremu knjiženja, dok računovođa proverava rezultat."),
            ("Plate i naknade", "Program podržava rad sa obračunima plata i povezanim stavkama. Cilj nije da zameni stručnu kontrolu obračuna, već da ukloni ponovno kucanje već postojećih podataka."),
            ("Bolovanja i prevoz", "Posebni obračuni bolovanja i prevoza mogu se pripremiti za knjiženje kroz isti kontrolisani tok, uz jasne stavke naloga pre konačne potvrde."),
            ("Preciznost pre brzine", "Ušteda vremena ima vrednost samo ako su podaci proverljivi. Zato korisnik vidi pripremljeni nalog i potvrđuje ga tek nakon pregleda."),
        ],
        "process_title": "Od ISKRA fajla do naloga",
        "process": ["Izaberite odgovarajući ISKRA obračun.", "Budžet+ učita podatke i pripremi računovodstvene stavke.", "Pregledajte nalog i kontrole.", "Potvrdite precizno pripremljeno knjiženje."],
        "related": [("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("Obrazac 5 za ISPFI", "../obrazac-5-ispfi/"), ("Knjiženje e-faktura", "../knjizenje-e-faktura-za-skole/")],
    },
    {
        "slug": "uplate-ucenika",
        "title": "Evidencija uplata učenika po aktivnosti | Budžet+",
        "description": "Samostalni Budžet+ modul za brzu evidenciju uplata učenika i preglede po učeniku, aktivnosti i blagajničkom radu.",
        "kicker": "Samostalni modul za blagajnika",
        "h1": "Uplate učenika pregledne po učeniku i aktivnosti",
        "intro": "Modul za uplate učenika omogućava brz unos i jasan pregled bez uvođenja kompletnog računovodstvenog paketa.",
        "summary_title": "Pregled koji prati stvarni rad",
        "summary": ["Evidencija po učeniku", "Pregled po aktivnosti", "Brz rad blagajnika", "Samostalno korišćenje modula"],
        "sections": [
            ("Ko je uplatio i za koju aktivnost?", "Evidencija povezuje uplatu sa učenikom i aktivnošću, pa se stanje može proveriti bez pretraživanja više odvojenih tabela."),
            ("Brz unos za blagajnika", "Forma je usmerena na podatke koji su potrebni u svakodnevnom blagajničkom radu. Cilj je da unos bude brz, a naknadna provera jednostavna."),
            ("Pregledi bez dodatne evidencije", "Iz unetih podataka dobijaju se pregledi po učeniku i aktivnosti. Nema potrebe da se ista uplata ponovo prepisuje radi zbirnog pregleda."),
            ("Modul koji radi samostalno", "Škola može da koristi evidenciju uplata učenika bez pune Budžet+ aplikacije, a kasnije da proširi paket ako joj zatrebaju računovodstveni moduli."),
        ],
        "process_title": "Kako se vodi evidencija",
        "process": ["Definišite aktivnosti za koje se prate uplate.", "Izaberite učenika i evidentirajte uplatu.", "Pregledajte stanje po učeniku ili aktivnosti.", "Koristite zbirni pregled za blagajničku kontrolu."],
        "related": [("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("SPIRI kumulativno plaćanje", "../spiri-kumulativno-placanje/"), ("Knjiženje e-faktura", "../knjizenje-e-faktura-za-skole/")],
    },
]


def e(value: str) -> str:
    return html.escape(value, quote=True)


def render(page: dict) -> str:
    canonical = f"{BASE}/{page['slug']}/"
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": canonical,
                "url": canonical,
                "name": page["title"],
                "description": page["description"],
                "isPartOf": {"@id": f"{BASE}/#website"},
                "about": {"@id": f"{BASE}/#software"},
                "inLanguage": "sr",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Početna", "item": f"{BASE}/"},
                    {"@type": "ListItem", "position": 2, "name": page["h1"], "item": canonical},
                ],
            },
        ],
    }
    summary = "".join(f"<li>{e(item)}</li>" for item in page["summary"])
    sections = "\n".join(f"<h2>{e(title)}</h2>\n        <p>{e(text)}</p>" for title, text in page["sections"])
    process = "".join(f"<li>{e(item)}</li>" for item in page["process"])
    related = "".join(f'<a href="{e(href)}">{e(label)} →</a>' for label, href in page["related"])
    return f'''<!doctype html>
<html lang="sr">
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-KW2SPZWVH4"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-KW2SPZWVH4');
  </script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(page["title"])}</title>
  <meta name="description" content="{e(page["description"])}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{e(page["title"])}">
  <meta property="og:description" content="{e(page["description"])}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/assets/img/budzet-plus-social.svg">
  <meta property="og:locale" content="sr_RS">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(page["title"])}">
  <meta name="twitter:description" content="{e(page["description"])}">
  <meta name="twitter:image" content="{BASE}/assets/img/budzet-plus-social.svg">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, indent=2)}</script>
  <link rel="icon" href="../assets/img/budget_plus_logo.ico" sizes="any">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/styles.css">
</head>
<body class="landing-body">
  <header class="landing-header">
    <div class="container landing-nav">
      <a class="landing-brand" href="../"><img src="../assets/img/budget_plus_logo.ico" alt=""><span>Budžet+ za škole</span></a>
      <a class="btn primary" href="../#kontakt">Zakažite prezentaciju</a>
    </div>
  </header>
  <main>
    <nav class="container breadcrumbs" aria-label="Putanja">
      <ol><li><a href="../">Početna</a></li><li aria-hidden="true">/</li><li aria-current="page">{e(page["kicker"])}</li></ol>
    </nav>
    <section class="landing-hero">
      <div class="container landing-hero-grid">
        <div>
          <p class="landing-kicker">{e(page["kicker"])}</p>
          <h1>{e(page["h1"])}</h1>
          <p class="lede">{e(page["intro"])}</p>
          <a class="btn primary" href="../#kontakt">Zatražite prezentaciju</a>
        </div>
        <aside class="landing-summary">
          <h2>{e(page["summary_title"])}</h2>
          <ul>{summary}</ul>
        </aside>
      </div>
    </section>
    <section class="section alt">
      <div class="container content-narrow">
        {sections}
        <h2>{e(page["process_title"])}</h2>
        <ol class="process-list">{process}</ol>
        <div class="landing-cta">
          <h2>Pogledajte Budžet+ u radu</h2>
          <p>Na prezentaciji prolazimo kroz proces koji je važan baš vašoj školi.</p>
          <a class="btn primary" href="../#kontakt">Zakažite prezentaciju</a>
        </div>
        <h2>Povezana rešenja</h2>
        <div class="related-links">{related}</div>
      </div>
    </section>
  </main>
  <footer class="landing-footer">
    <div class="container landing-footer-inner">
      <p><strong>Budžet+ za škole</strong><br>Program za automatizovano knjiženje</p>
      <p>Alpeon Softver · 065 917 0989<br><a href="mailto:aleksandar.pejkovic@budzetplus.rs">aleksandar.pejkovic@budzetplus.rs</a></p>
    </div>
  </footer>
</body>
</html>
'''


def main() -> None:
    for page in PAGES:
        destination = ROOT / page["slug"] / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(render(page), encoding="utf-8")
        print(destination.relative_to(ROOT))


if __name__ == "__main__":
    main()
