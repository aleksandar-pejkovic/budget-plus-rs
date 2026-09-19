#!/usr/bin/env python3
"""Generate the twelve canonical solution pages."""
from __future__ import annotations

from pathlib import Path

from solution_renderer import render_solution

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://budzetplus.rs"
LASTMOD = "2026-09-20"

# slug, title, description, kicker, h1, intro, benefits, related slugs
PAGES = [
    ("program-za-racunovodstvo-skola", "Program za računovodstvo škola | Budžet+", "Budžet+ povezuje knjigovodstvo, finansijsko planiranje, plaćanja i izveštavanje za škole, uz osnovna sredstva, uplate učenika i kontrolu računovođe.", "Povezane računovodstvene evidencije", "Program za računovodstvo škola", "Budžet+ povezuje knjiženje, finansijsko planiranje, plaćanja i izveštavanje. U istom programu vodite osnovna sredstva i pomoćnu evidenciju uplata učenika, uz automatizaciju unosa i kontrolu računovođe.", ["Finansijski plan iz IFISUP-a i pregled realizacije", "E-fakture, SPIRI izvodi, avansi i ISKRA obračuni", "Glavna knjiga, dnevnik, kartice, bilansi i pomoćne evidencije", "SPIRI, ORIS i ISPFI fajlovi iz proverenih podataka"], ["knjizenje-e-faktura-za-skole", "spiri-izvodi-skole", "iskra-obracuni-knjizenje"]),
    ("knjizenje-e-faktura-za-skole", "eFakture za automatsko knjiženje | Budžet+", "Preuzmite e-fakture iz SEF-a i knjižite ih direktno u programu, uz zatvaranje avansa po konačnoj fakturi i proveru računovođe.", "SEF i e-fakture", "eFakture za automatsko knjiženje", "Preuzmite e-fakture iz SEF-a i proknjižite ih direktno iz programa. Budžet+ preuzima podatke i povezuje partnere, bez ponovnog kucanja.", ["Preuzimanje podataka sa e-faktura iz SEF-a", "Prepoznavanje i kreiranje partnera", "Knjiženje odabranih faktura direktno iz pregleda", "Zatvaranje avansa uz konačnu fakturu"], ["program-za-racunovodstvo-skola", "spiri-kumulativno-placanje", "spiri-izvodi-skole"]),
    ("spiri-izvodi-skole", "SPIRI izvodi za automatsko knjiženje | Budžet+", "Automatsko knjiženje SPIRI izvoda i isplata avansa u Budžet+ programu, bez ručnog prepisivanja stavki.", "SPIRI izvodi", "SPIRI izvodi za automatsko knjiženje", "Učitajte izvod — Budžet+ automatski knjiži njegove stavke, uključujući isplate avansa. Vi pregledate rezultat.", ["Učitavanje SPIRI izvoda", "Knjiženje isplata avansa iz izvoda", "Povezivanje sa partnerima i evidencijom", "Kontrolisan nalog bez ručnog prepisivanja"], ["program-za-racunovodstvo-skola", "izvrsenje-budzeta-skola", "knjizenje-e-faktura-za-skole"]),
    ("iskra-obracuni-knjizenje", "ISKRA obračuni za automatsko knjiženje | Budžet+", "Automatski proknjižite podržane ISKRA obračune plata i bolovanja iz Excel dokumenta, bez prepisivanja stavki.", "Plate i bolovanja iz ISKRA sistema", "ISKRA obračuni za automatsko knjiženje", "Učitajte podržani ISKRA obračun plata ili bolovanja — Budžet+ automatski knjiži stavke u izabrani nalog. Vi pregledate rezultat.", ["Obračuni plata i bolovanja", "Provera strukture Excel dokumenta", "Knjiženje u izabrani nalog", "Pregled rezultata bez prepisivanja obračuna"], ["program-za-racunovodstvo-skola", "spiri-izvodi-skole", "zatvaranje-poslovne-godine"]),
    ("spiri-kumulativno-placanje", "SPIRI plaćanje iz e-faktura | Budžet+", "Objedinite više e-faktura u jedan dokument za SPIRI kumulativno plaćanje, uz pregled računovođe pre učitavanja.", "Kumulativno plaćanje", "SPIRI plaćanje iz e-faktura", "Izaberite više e-faktura i pripremite jedan dokument za kumulativno plaćanje u SPIRI, bez ponovnog unosa podataka.", ["Podaci se preuzimaju sa e-faktura", "Više obaveza u jednom dokumentu", "Manji rizik greške pri prepisivanju", "Pregled pre učitavanja u SPIRI"], ["knjizenje-e-faktura-za-skole", "rucni-unos-spiri-placanja", "spiri-izvodi-skole"]),
    ("rucni-unos-spiri-placanja", "Ručni SPIRI unos sa šablonima | Budžet+", "Pripremite SPIRI plaćanja za partnere i fizička lica, učitajte poresku prijavu i sačuvajte šablone za ponovljena plaćanja.", "Plaćanja koja ne polaze od e-fakture", "Ručni SPIRI sa šablonima", "Kada plaćanje ne polazi od e-fakture, Budžet+ vodi kroz izbor primaoca i podataka, a ponovljena plaćanja ubrzava sačuvanim šablonima.", ["Izbor partnera ili fizičkog lica", "Učitavanje podataka iz poreske prijave", "Lista sačuvanih šablona", "Dokument spreman za proveru i SPIRI"], ["spiri-kumulativno-placanje", "spiri-izvodi-skole", "program-za-racunovodstvo-skola"]),
    ("oris-izvoz-za-skole", "ORIS izvoz za škole | Budžet+", "Izaberite mesec i godinu i pripremite dokument za ORIS iz postojećih knjiženja, uz proveru evidencije i rezultata na portalu.", "ORIS izvoz", "Mesečne promene za ORIS iz postojećih knjiženja", "Budžet+ priprema ORIS fajl iz podataka koji se već vode i proveravaju u računovodstvu škole.", ["Podaci dolaze iz postojeće evidencije", "Izbor meseca i godine", "Manje naknadnog usklađivanja", "Fajl spreman za učitavanje na ORIS portal"], ["program-za-racunovodstvo-skola", "obrazac-5-ispfi", "izvrsenje-budzeta-skola"]),
    ("obrazac-5-ispfi", "Obrazac 5 za ISPFI | Budžet+", "Pripremite obavezni Obrazac 5 za ISPFI iz postojećih proknjiženih podataka bez ponovnog ručnog unosa.", "Iz postojećih podataka", "Obrazac 5 spreman za ISPFI", "Budžet+ koristi postojeća knjiženja za pripremu Obrasca 5, a računovođa proverava rezultat pre učitavanja u ISPFI.", ["Bez ponovnog unosa istih podataka", "Priprema iz završenih knjiženja", "Kraći rad pred rok", "Fajl spreman za ISPFI"], ["oris-izvoz-za-skole", "izvrsenje-budzeta-skola", "program-za-racunovodstvo-skola"]),
    ("izvrsenje-budzeta-skola", "Izvršenje budžeta za škole | Budžet+", "Učitajte finansijski plan iz IFISUP-a i pratite realizaciju, odstupanja i grafikone bez ručnog prepisivanja stavki plana.", "Plan i realizacija", "Izvršenje budžeta pod kontrolom", "Učitajte Excel plan preuzet iz IFISUP-a. Budžet+ povezuje plan sa evidentiranim podacima za pregled realizacije, odstupanja i grafikona.", ["Učitavanje plana iz IFISUP-a bez prepisivanja", "Odstupanja koja se brzo uočavaju", "Grafikoni i pregledi", "Poređenje evidencije sa SPIRI"], ["spiri-izvodi-skole", "oris-izvoz-za-skole", "obrazac-5-ispfi"]),
    ("osnovna-sredstva-skola", "Osnovna sredstva iz e-fakture i amortizacija | Budžet+", "Od XML e-fakture do povezanog knjiženja i evidencije osnovnih sredstava uz proveru računovođe. Amortizacija, pregledi i popis.", "Povezano knjiženje i evidencija", "Od e-fakture do knjiženja i evidencije osnovnih sredstava", "Učitajte jednu XML e-fakturu, rasporedite stavke i proverite kompletan nalog. Potvrdom se zajedno čuvaju knjiženje i evidencija osnovnih sredstava.", ["Knjiženje i evidencija iz jedne e-fakture", "Pregled kompletnog naloga pre potvrde", "Zajedničko čuvanje knjiženja i evidencije", "Amortizacija, popisne liste i pregledi"], ["knjizenje-e-faktura-za-skole", "zatvaranje-poslovne-godine", "program-za-racunovodstvo-skola", "izvrsenje-budzeta-skola"]),
    ("uplate-ucenika", "Uplate učenika po aktivnosti | Budžet+", "Pratite učenike, aktivnosti, zaduženja i uplate uz jasne preglede po učeniku, odeljenju i aktivnosti.", "Školska pomoćna evidencija", "Uplate učenika pregledne po aktivnosti", "Budžet+ povezuje učenike, aktivnosti, zaduženja i uplate, pa su pregledi dostupni bez dodatnih tabela.", ["Učenici i odeljenja", "Aktivnosti i zaduženja", "Evidentiranje i uvoz uplata", "Pregledi po učeniku i aktivnosti"], ["program-za-racunovodstvo-skola", "izvrsenje-budzeta-skola", "osnovna-sredstva-skola"]),
    ("zatvaranje-poslovne-godine", "Zatvaranje godine i prenos salda | Budžet+", "Završite poslovnu godinu kroz obračun amortizacije, zatvaranje konta, prenos salda i otvaranje nove godine.", "Kontrolisan završni tok", "Zatvaranje godine i prenos salda", "Budžet+ priprema završne naloge i prenos salda u novu godinu. Vi pregledate rezultat i početna stanja.", ["Obračun amortizacije", "Zatvaranje konta", "Prenos salda i početnih stanja", "Otvaranje nove poslovne godine"], ["osnovna-sredstva-skola", "program-za-racunovodstvo-skola", "izvrsenje-budzeta-skola"]),
]

LABELS = {p[0]: p[4] for p in PAGES}


def render(page: tuple) -> str:
    return render_solution(page, BASE, LASTMOD, LABELS)


def main() -> None:
    for page in PAGES:
        target = ROOT / page[0] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(page), encoding="utf-8")
    urls = [f"{BASE}/"] + [f"{BASE}/{p[0]}/" for p in PAGES]
    body = "\n".join(f"  <url><loc>{u}</loc><lastmod>{LASTMOD}</lastmod></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n', encoding="utf-8")


if __name__ == "__main__":
    main()
