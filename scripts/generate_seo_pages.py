#!/usr/bin/env python3
"""Generate static SEO landing pages from a reviewed school-focused model."""
from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://budzetplus.rs"
LASTMOD = "2026-08-02"

PAGES = [
    {
        "slug": "program-za-racunovodstvo-skola",
        "title": "Program za računovodstvo škola | Budžet+ za škole",
        "description": "Budžet+ ubrzava školsko knjigovodstvo, eFakture, SPIRI, ORIS, izveštaje i pomoćne evidencije.",
        "kicker": "Budžet+ za škole",
        "h1": "Program za računovodstvo škola",
        "intro": "Budžet+ povezuje knjiženje, eFakture, SPIRI, ORIS, izveštaje, osnovna sredstva i školske evidencije.",
        "summary_title": "Računovodstveni tok škole",
        "summary": ["Budžetsko knjigovodstvo i kontni plan", "SEF/eFakture, XML fakture i SPIRI izvodi", "SPIRI XML za kumulativno plaćanje, ORIS fajl i Obrazac 5", "Osnovna sredstva, izveštaji i pomoćne evidencije"],
        "sections": [
            ("Napravljen za školsko računovodstvo", "Konta, izvori, programske aktivnosti, eFakture, SPIRI i ORIS nalaze se u istom toku rada."),
            ("Računovođa drži kontrolu", "Budžet+ priprema podatke i naloge. Računovođa proverava i potvrđuje."),
            ("Od dokumenta do naloga", "eFakture, SPIRI izvodi, obračuni i planovi ulaze u obradu bez ponovnog kucanja."),
            ("Izveštaji iz istih podataka", "Kartice, knjige, bilansi, KUR, izvršenje budžeta i popisne liste nastaju iz uređene evidencije."),
        ],
        "process_title": "Kako škola počinje",
        "process": ["Podesimo nalog, šifarnike, konta i izvore.", "Unesu se početna stanja i potrebne evidencije.", "Prvi dokument se knjiži uz proveru.", "Računovođa nastavlja rad kroz poznat tok."],
        "faq": [
            ("Kome je Budžet+ namenjen?", "Budžet+ je namenjen računovođama u školama i poslovima koje one vode ili pripremaju kroz računovodstvenu evidenciju."),
            ("Šta zamenjuje paralelne evidencije?", "Ne zamenjuje svaku pomoćnu evidenciju, ali povezuje poslove koji treba da prate knjiženje, izveštaje i kontrole."),
        ],
        "related": [("Računovodstvo škole", "../finansijski-sistem-za-skole/"), ("Budžetsko knjigovodstvo škola", "../budzetsko-knjigovodstvo-skola/"), ("Uplate učenika", "../uplate-ucenika/")],
    },
    {
        "slug": "finansijski-sistem-za-skole",
        "title": "Računovodstveni sistem za škole | Budžet+",
        "description": "Računovodstvo škole: knjiženje, eFakture, SPIRI, izveštaji i kontrole u jednom toku rada.",
        "kicker": "Bez ručnog prepisivanja",
        "h1": "Računovodstvo škole",
        "intro": "Budžet+ pomaže računovođi da dokumente, rokove, knjiženja, kontrole i izveštaje drži u jednom toku.",
        "summary_title": "Šta povezuje",
        "summary": ["Plan i realizacija budžeta", "Knjiženje, nalozi i analitike", "eFakture, SPIRI i ORIS", "PDF izveštaji i izvoz za kontrolu"],
        "sections": [
            ("Manje rasutih podataka", "Plan, fakture, izvodi, knjiženja i izveštaji koriste isti računovodstveni tok."),
            ("Manje traženja, više rada", "Računovođa ne gubi vreme na proveru gde je poslednja verzija podataka."),
            ("Automatizacija sa kontrolom", "Budžet+ priprema nalog. Računovođa vidi, proverava i potvrđuje."),
        ],
        "process_title": "Tipičan školski tok",
        "process": ["Dokument ili izvod ulazi u sistem.", "Budžet+ prepoznaje podatke i predlaže obradu.", "Računovođa proverava klasifikaciju i kontrole.", "Iz istih podataka nastaju knjige, pregledi i izveštaji."],
        "faq": [
            ("Ko koristi ovaj tok rada?", "Tok rada je usmeren na računovođu koja priprema, proverava i koristi finansijske podatke škole."),
            ("Da li sistem ukida stručnu proveru?", "Ne. Cilj je da ukloni mehaničko prepisivanje, a ne računovodstvenu odluku."),
        ],
        "related": [("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("Izvršenje budžeta škole", "../izvrsenje-budzeta-skola/"), ("SPIRI izvodi za škole", "../spiri-izvodi-skole/")],
    },
    {
        "slug": "budzetsko-knjigovodstvo-skola",
        "title": "Budžetsko knjigovodstvo škola | Budžet+",
        "description": "Budžet+ podržava školsko budžetsko knjigovodstvo: kontni plan, izvore finansiranja, projekte, programske aktivnosti i izveštaje.",
        "kicker": "Budžetsko knjigovodstvo",
        "h1": "Budžetsko knjigovodstvo škole bez paralelnih evidencija",
        "intro": "Budžet+ je napravljen za školsko budžetsko računovodstvo u Srbiji: konta, izvori, projekti, programske aktivnosti, nalozi, kontrole i izveštaji rade zajedno.",
        "summary_title": "Za računovodstvo",
        "summary": ["Kontni plan i klasifikacije", "Izvori finansiranja i projekti", "Glavna knjiga, dnevnik i bruto bilans", "Analitičke kartice i knjiga faktura"],
        "sections": [
            ("Knjigovodstvo škole nije generičko poslovno knjigovodstvo", "Škola mora da prati budžetske klasifikacije, izvore, programe i obavezne izveštaje. Kada softver razume te dimenzije, manje vremena odlazi na naknadno prepravljanje i usklađivanje."),
            ("Jedan unos nosi više značenja", "Knjiženje treba da bude korisno za nalog, analitiku, izvršenje budžeta i izveštaje. Budžet+ povezuje te preglede da isti posao ne počinje iznova u svakoj evidenciji."),
            ("Kontrola pre završnog knjiženja", "Automatski pripremljeni podaci se proveravaju pre potvrde. To čuva stručnu odgovornost računovođe, a uklanja najzamorniji deo posla."),
        ],
        "process_title": "Od naloga do izveštaja",
        "process": ["Unose se ili uvoze dokumenti.", "Biraju se konta, izvori i potrebne klasifikacije.", "Budžet+ proverava i čuva knjiženje.", "Iz istih podataka nastaju knjige, analitike i izveštaji."],
        "faq": [
            ("Da li podržava PDF izveštaje i izvoz?", "Da. Sistem je namenjen pregledima, kontroli i predaji podataka."),
            ("Da li može da radi sa postojećim podacima?", "Početna stanja i radni podaci mogu se pripremiti kroz dogovorene uvoze i šablone."),
        ],
        "related": [("Računovodstvo škole", "../finansijski-sistem-za-skole/"), ("Izvršenje budžeta škole", "../izvrsenje-budzeta-skola/"), ("ORIS izvoz za škole", "../oris-izvoz-za-skole/")],
    },
    {
        "slug": "spiri-kumulativno-placanje",
        "title": "SPIRI kumulativno plaćanje e-faktura | Budžet+",
        "description": "Budžet+ za škole povlači podatke sa e-faktura i kreira SPIRI fajl za kumulativno plaćanje: više faktura u jednom plaćanju.",
        "kicker": "Kumulativno plaćanje više faktura",
        "h1": "SPIRI kumulativno plaćanje iz e-faktura",
        "intro": "Budžet+ povuče podatke sa e-faktura, objedini obaveze i kreira SPIRI fajl za kumulativno plaćanje. Računovođa pregleda rezultat.",
        "summary_title": "Tačan tok rada",
        "summary": ["Podaci dolaze sa e-faktura", "Bira se više faktura za plaćanje", "Budžet+ kreira SPIRI fajl za kumulativno plaćanje", "Računovođa učitava fajl i zadržava kontrolu"],
        "sections": [
            ("Više obaveza, jedno kumulativno plaćanje", "Izabrane e-fakture se objedine u SPIRI fajl za kumulativno plaćanje, uz manji rizik greške u iznosu, partneru ili pozivu na broj."),
            ("Računovođa bira i proverava", "Budžet+ koristi podatke sa e-faktura. Računovođa odlučuje šta ulazi u plaćanje."),
            ("Priprema, ne automatsko slanje", "Program priprema fajl za učitavanje. Završna kontrola ostaje kod računovođe."),
        ],
        "process_title": "Od e-faktura do SPIRI kumulativnog plaćanja",
        "process": ["Budžet+ preuzme podatke sa dostupnih e-faktura.", "Računovođa označi fakture koje ulaze u kumulativno plaćanje.", "Program objedini podatke u jedan SPIRI fajl za kumulativno plaćanje.", "Računovođa pregleda rezultat i učita fajl u SPIRI."],
        "faq": [
            ("Da li se plaćanje izvršava automatski?", "Ne. Budžet+ priprema fajl, a računovođa ga proverava i učitava u SPIRI."),
            ("Zašto je ovo važno školama?", "Zato što se isti tip posla ponavlja često, a greška u rutinskom prepisivanju može napraviti nepotreban zastoj."),
        ],
        "related": [("SEF i eFakture za škole", "../sef-efakture-skole/"), ("SPIRI izvodi za škole", "../spiri-izvodi-skole/"), ("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/")],
    },
    {
        "slug": "sef-efakture-skole",
        "title": "SEF i eFakture za škole | Budžet+",
        "description": "Budžet+ pomaže školama da eFakture i XML fakture pretvore u kontrolisano knjiženje, SPIRI plaćanje i knjigu ulaznih faktura.",
        "kicker": "SEF i eFakture",
        "h1": "eFakture za škole pretvorene u kontrolisano knjiženje",
        "intro": "Podaci sa eFakture ulaze u nalog, kontrole, knjigu ulaznih faktura i SPIRI tok.",
        "summary_title": "Bez duplog rada",
        "summary": ["Učitavanje SEF/eFaktura i XML faktura", "Prepoznavanje partnera i stavki", "Priprema naloga za knjiženje", "Veza sa SPIRI kumulativnim plaćanjem"],
        "sections": [
            ("Digitalni dokument treba da skrati posao", "Budžet+ koristi podatke sa eFakture za nalog, knjigu faktura i plaćanje."),
            ("Računovođa i dalje odlučuje", "Partner, konta, klasifikacija i kontrole proveravaju se pre knjiženja."),
            ("Jedan dokument, više koristi", "Ista eFaktura služi za knjiženje, pregled obaveza, KUF i SPIRI kumulativno plaćanje."),
        ],
        "process_title": "Kako se obrađuje eFaktura",
        "process": ["Učita se eFaktura ili XML dokument.", "Budžet+ prepozna dostupne podatke.", "Računovođa proveri nalog i klasifikaciju.", "Podaci se koriste za knjiženje, preglede i po potrebi SPIRI kumulativno plaćanje."],
        "faq": [
            ("Da li se partneri mogu kreirati iz faktura?", "Da, podaci sa faktura mogu pomoći u radu sa partnerima i pripremi evidencije."),
            ("Da li je potreban ručni unos?", "Stručne odluke se proveravaju ručno, ali rutinsko prepisivanje podataka se smanjuje."),
        ],
        "related": [("Knjiženje e-faktura za škole", "../knjizenje-e-faktura-za-skole/"), ("SPIRI kumulativno plaćanje", "../spiri-kumulativno-placanje/"), ("Budžetsko knjigovodstvo škola", "../budzetsko-knjigovodstvo-skola/")],
    },
    {
        "slug": "knjizenje-e-faktura-za-skole",
        "title": "Automatsko knjiženje e-faktura za škole | Budžet+",
        "description": "Učitajte podatke sa e-faktura, formirajte kontrolisan nalog i pripremite SPIRI kumulativno plaćanje bez ručnog prepisivanja.",
        "kicker": "Od e-fakture do naloga",
        "h1": "Knjiženje e-faktura uz pripremljen nalog",
        "intro": "Budžet+ preuzima podatke sa e-fakture, priprema nalog i ostavlja računovođi završnu proveru.",
        "summary_title": "Šta se automatizuje",
        "summary": ["Učitavanje podataka sa e-fakture", "Prepoznavanje partnera i stavki", "Priprema naloga i kontrola", "Podaci za SPIRI kumulativno plaćanje"],
        "sections": [
            ("Bez prepisivanja istog dokumenta", "Iznos, datum, partner i stavke koriste se iz e-fakture kada su dostupni."),
            ("Partneri i klasifikacija", "Budžet+ priprema podatke. Računovođa proverava klasifikaciju i stručne odluke."),
            ("Kontrola pre knjiženja", "Računovođa vidi stavke, kontrole i nalog pre potvrde."),
        ],
        "process_title": "Kako se knjiži e-faktura",
        "process": ["Učitajte ili preuzmite podatke sa e-fakture.", "Budžet+ pripremi partnera, stavke i nalog.", "Pregledajte klasifikaciju i označene kontrole.", "Potvrdite knjiženje i po potrebi uključite fakturu u SPIRI kumulativno plaćanje."],
        "faq": [
            ("Da li program sam knjiži bez provere?", "Ne. Računovođa pregleda pripremljeni nalog i potvrđuje knjiženje."),
            ("Da li se isti podaci koriste za plaćanje?", "Da, izabrane fakture mogu da uđu u tok za SPIRI kumulativno plaćanje."),
        ],
        "related": [("SEF i eFakture za škole", "../sef-efakture-skole/"), ("SPIRI kumulativno plaćanje", "../spiri-kumulativno-placanje/"), ("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/")],
    },
    {
        "slug": "spiri-izvodi-skole",
        "title": "SPIRI izvodi i knjiženje za škole | Budžet+",
        "description": "Budžet+ pomaže školama da SPIRI izvode, poređenja i knjiženja povežu sa budžetskim evidencijama i izveštajima.",
        "kicker": "SPIRI izvodi",
        "h1": "SPIRI izvodi povezani sa knjiženjem",
        "intro": "Budžet+ povezuje SPIRI izvode sa knjiženjem, realizacijom budžeta i kontrolama.",
        "summary_title": "Za kontrolu toka novca",
        "summary": ["Uvoz i obrada izvoda", "Poređenja sa evidencijom", "Knjiženje kroz kontrolisan nalog", "Pregled realizacije bez čekanja"],
        "sections": [
            ("Izvod ulazi u evidenciju", "Podaci iz SPIRI izvoda koriste se za knjiženje, analitiku i izveštaje."),
            ("Poređenje otkriva odstupanja", "SPIRI podaci se porede sa evidencijom, pa se razlike vide ranije."),
            ("Pregledi bez dodatnog obračuna", "Prihodi, rashodi i realizacija nastaju iz povezanih podataka."),
        ],
        "process_title": "Od izvoda do pregleda",
        "process": ["Učita se SPIRI izvod.", "Budžet+ priprema obradu i poređenja.", "Računovođa proverava stavke i nalog.", "Podaci ulaze u knjiženje, analitiku i realizaciju budžeta."],
        "faq": [
            ("Da li se izvodi mogu povezati sa izveštajima?", "Da. Cilj je da se podaci iz izvoda koriste za knjiženje i preglede, ne samo za arhivu."),
            ("Da li ovo menja rad računovođe?", "Menja rutinu, ne odgovornost. Računovođa proverava i potvrđuje podatke."),
        ],
        "related": [("Izvršenje budžeta škole", "../izvrsenje-budzeta-skola/"), ("Budžetsko knjigovodstvo škola", "../budzetsko-knjigovodstvo-skola/"), ("Računovodstvo škole", "../finansijski-sistem-za-skole/")],
    },
    {
        "slug": "oris-izvoz-za-skole",
        "title": "ORIS fajl za škole | Budžet+",
        "description": "Budžet+ priprema fajl za učitavanje na ORIS portal, uz proveru podataka pre predaje.",
        "kicker": "ORIS kontrole",
        "h1": "Fajl za ORIS portal sa kontrolom pre predaje",
        "intro": "Budžet+ priprema fajl za učitavanje na ORIS portal iz podataka koje računovođa već kontroliše.",
        "summary_title": "Manje stresa pred rok",
        "summary": ["ORIS priprema po potrebi", "Validacije i stavke za proveru", "Fajl za učitavanje na ORIS portal", "Pregled pre konačne predaje"],
        "sections": [
            ("Greška treba da se vidi ranije", "ORIS kontrole prate podatke pre pripreme fajla za portal."),
            ("Fajl iz uređene evidencije", "Budžet+ priprema fajl za ORIS portal iz podataka u sistemu."),
            ("Kontrola ostaje kod računovođe", "Program pomaže da se podaci provere i pripreme. Računovođa pregleda rezultat."),
        ],
        "process_title": "Kako nastaje fajl za ORIS portal",
        "process": ["Podaci se vode kroz redovno knjiženje i evidencije.", "ORIS kontrole označavaju stavke za proveru.", "Računovođa ispravlja ili potvrđuje podatke.", "Budžet+ priprema fajl za učitavanje na ORIS portal."],
        "faq": [
            ("Da li je ORIS priprema obavezna?", "Ne mora biti uključena za svaki način rada; koristi se kada školi treba fajl za ORIS portal."),
            ("Da li se fajl radi iz posebne evidencije?", "Cilj je da fajl nastaje iz uređenih podataka u sistemu."),
        ],
        "related": [("Budžetsko knjigovodstvo škola", "../budzetsko-knjigovodstvo-skola/"), ("Izvršenje budžeta škole", "../izvrsenje-budzeta-skola/"), ("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/")],
    },
    {
        "slug": "obrazac-5-ispfi",
        "title": "Obrazac 5 za ISPFI bez ručnog unosa | Budžet+",
        "description": "Budžet+ priprema Obrazac 5 za škole iz proknjiženih podataka, a računovođa preuzima fajl spreman za učitavanje u ISPFI.",
        "kicker": "Iz proknjiženih podataka",
        "h1": "Obrazac 5 spreman za ISPFI",
        "intro": "Budžet+ priprema Obrazac 5 iz proknjiženih podataka. Računovođa preuzima fajl za učitavanje na ISPFI portal.",
        "summary_title": "Manje koraka do izveštaja",
        "summary": ["Nema ponovnog unosa istih podataka", "Brza priprema Obrasca 5", "Kontrola kroz prethodna knjiženja", "Fajl spreman za ISPFI"],
        "sections": [
            ("Jedan izvor podataka", "Obrazac 5 nastaje iz knjiženja koja su već u sistemu."),
            ("Manje stresa pred rok", "Kada su knjiženja ažurna, priprema Obrasca 5 je kraća."),
            ("Fajl za ISPFI portal", "Program formira fajl koji se zatim učitava na ISPFI portal."),
        ],
        "process_title": "Kako nastaje Obrazac 5",
        "process": ["Budžet+ koristi podatke iz završenih knjiženja.", "Program formira Obrazac 5 iz postojećih podataka.", "Računovođa preuzima fajl.", "Fajl se učitava na ISPFI portal."],
        "faq": [
            ("Da li se podaci ponovo kucaju?", "Ne. Izveštaj se priprema iz podataka koji su već u sistemu."),
            ("Gde se proverava Obrazac 5?", "Obrazac 5 se proverava nakon učitavanja na ISPFI portal. U Budžet+ se priprema fajl iz proknjiženih podataka."),
        ],
        "related": [("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("Izvršenje budžeta škole", "../izvrsenje-budzeta-skola/"), ("ORIS izvoz za škole", "../oris-izvoz-za-skole/")],
    },
    {
        "slug": "iskra-obracuni-knjizenje",
        "title": "ISKRA obračuni i automatsko knjiženje | Budžet+",
        "description": "Budžet+ priprema ISKRA obračune plata, bolovanja i prevoza za precizno knjiženje u školama bez ručnog unosa svake stavke.",
        "kicker": "Plate, bolovanja i prevoz",
        "h1": "ISKRA obračuni u školama spremni za knjiženje u sekundama",
        "intro": "Budžet+ učitava ISKRA obračune i priprema nalog koji računovođa pregleda i potvrđuje.",
        "summary_title": "Jedan kontrolisan proces",
        "summary": ["Obračuni plata", "Knjiženje bolovanja", "Obračun prevoza", "Pregled naloga pre potvrde"],
        "sections": [
            ("Manje rutine u složenom obračunu", "Podaci iz ISKRA obračuna koriste se za pripremu knjiženja."),
            ("Plate, RFZO i povezani podaci", "Program koristi postojeće obračunske podatke i smanjuje ponovno kucanje."),
            ("Preciznost pre brzine", "Računovođa vidi pripremljeni nalog i potvrđuje ga tek nakon pregleda."),
        ],
        "process_title": "Od ISKRA fajla do naloga",
        "process": ["Izaberite odgovarajući ISKRA obračun.", "Budžet+ učita podatke i pripremi računovodstvene stavke.", "Pregledajte nalog i kontrole.", "Potvrdite precizno pripremljeno knjiženje."],
        "faq": [
            ("Da li podržava bolovanja i prevoz?", "Da. Tok obuhvata plate, bolovanja, prevoz i povezane obračunske podatke."),
            ("Da li je unos potpuno automatski?", "Program priprema knjiženje, a računovođa proverava i potvrđuje rezultat."),
        ],
        "related": [("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("Budžetsko knjigovodstvo škola", "../budzetsko-knjigovodstvo-skola/"), ("Obrazac 5 za ISPFI", "../obrazac-5-ispfi/")],
    },
    {
        "slug": "uplate-ucenika",
        "title": "Evidencija uplata učenika po aktivnosti | Budžet+",
        "description": "Budžet+ omogućava školama brzu evidenciju uplata učenika, aktivnosti, statusa uplata, importa i PDF pregleda.",
        "kicker": "Pomoćna evidencija uplata",
        "h1": "Uplate učenika pregledne po učeniku, odeljenju i aktivnosti",
        "intro": "Budžet+ pomaže računovođi da prati učenike, odeljenja, aktivnosti, uplate, statuse i PDF preglede.",
        "summary_title": "Za računovodstvenu kontrolu",
        "summary": ["Evidencija po učeniku i odeljenju", "Pregled po aktivnosti", "Statusi i import uplata", "PDF pregledi za kontrolu"],
        "sections": [
            ("Ko je uplatio i za šta?", "Uplata se povezuje sa učenikom, odeljenjem i aktivnošću."),
            ("Brz unos i lakša provera", "Forma prati podatke koji računovođi trebaju za kontrolu uplata."),
            ("Pregledi bez dodatne evidencije", "Pregledi po učeniku, odeljenju i aktivnosti nastaju iz unetih podataka."),
        ],
        "process_title": "Kako se vodi evidencija",
        "process": ["Definišite aktivnosti za koje se prate uplate.", "Povežite učenike, odeljenja i statuse uplata.", "Evidentirajte ili uvezite uplate.", "Koristite PDF i zbirne preglede za kontrolu."],
        "faq": [
            ("Da li je ovo deo računovodstvene kontrole?", "Modul je napravljen za školski rad sa učenicima i aktivnostima, uz preglede koji olakšavaju proveru uplata."),
            ("Da li postoje PDF pregledi?", "Da. Pregledi se mogu koristiti za svakodnevnu proveru i komunikaciju unutar škole."),
        ],
        "related": [("Računovodstvo škole", "../finansijski-sistem-za-skole/"), ("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("Izvršenje budžeta škole", "../izvrsenje-budzeta-skola/")],
    },
    {
        "slug": "osnovna-sredstva-skola",
        "title": "Osnovna sredstva i amortizacija za škole | Budžet+",
        "description": "Budžet+ vodi osnovna sredstva škole, uvoz postojećih podataka, obračun amortizacije i popisne liste za preglednu evidenciju.",
        "kicker": "Osnovna sredstva",
        "h1": "Osnovna sredstva škole pod kontrolom",
        "intro": "Budžet+ vodi osnovna sredstva, postojeće podatke, amortizaciju i popisne liste u istom toku rada.",
        "summary_title": "Za popis i kontrolu",
        "summary": ["Evidencija osnovnih sredstava", "Uvoz postojećih podataka", "Obračun amortizacije", "Popisne liste i pregledi"],
        "sections": [
            ("Popis iz uređene evidencije", "Kada su sredstva u sistemu, popisna lista ne počinje ručnim sastavljanjem."),
            ("Uvoz postojećih podataka", "Postojeći podaci mogu da se pripreme za početni unos."),
            ("Amortizacija bez dodatnog usklađivanja", "Obračun amortizacije i pregledi ostaju u istom kontrolisanom toku."),
        ],
        "process_title": "Od evidencije do popisa",
        "process": ["Unose se ili uvoze osnovna sredstva.", "Proveravaju se potrebni podaci i klasifikacija.", "Budžet+ priprema obračun amortizacije.", "Računovođa dobija popisne liste i preglede."],
        "faq": [
            ("Da li se mogu uvesti postojeći podaci?", "Da. Uvoz postojećih podataka je namenjen početnom unosu ili prenosu postojeće evidencije."),
            ("Da li postoje popisne liste?", "Da. Popisne liste su deo očekivanih pregleda modula osnovnih sredstava."),
        ],
        "related": [("Program za računovodstvo škola", "../program-za-racunovodstvo-skola/"), ("Budžetsko knjigovodstvo škola", "../budzetsko-knjigovodstvo-skola/"), ("Izvršenje budžeta škole", "../izvrsenje-budzeta-skola/")],
    },
    {
        "slug": "izvrsenje-budzeta-skola",
        "title": "Izvršenje budžeta i izveštaji za škole | Budžet+",
        "description": "Budžet+ prikazuje realizaciju plana, prihode, rashode, odstupanja, projekcije i izveštaje za škole.",
        "kicker": "Izvršenje budžeta",
        "h1": "Izvršenje budžeta škole bez ručnog sabiranja",
        "intro": "Budžet+ pomaže računovođi da prati prihode, rashode, realizaciju plana, odstupanja i budžetske projekcije iz podataka koji se već vode u sistemu.",
        "summary_title": "Za računovodstvenu kontrolu",
        "summary": ["Dashboard i grafikoni", "Realizacija plana i odstupanja", "Bilansi, dnevnici i analitike", "PDF izveštaji i izvoz"],
        "sections": [
            ("Pregled iz postojećih podataka", "Plan, realizacija i odstupanja nastaju iz finansijskih podataka u sistemu."),
            ("Računovodstvo čuva detalje", "Iza pregleda stoje knjiženja, analitike, konta, izvori i dokumenti."),
            ("Izveštaji za svakodnevni rad", "Bilansi, glavna knjiga, dnevnik, bruto bilans, izvršenje budžeta i kartice služe za redovnu kontrolu."),
        ],
        "process_title": "Kako nastaje pregled",
        "process": ["Podaci ulaze kroz knjiženje i uvoze.", "Budžet+ ih povezuje sa planom i klasifikacijama.", "Dashboard prikazuje realizaciju i odstupanja.", "Izveštaji se koriste za kontrolu i predaju."],
        "faq": [
            ("Da li je pregled namenjen računovođi?", "Da. Pregled je namenjen računovođi koja priprema, proverava i koristi podatke za kontrolu i izveštaje."),
            ("Da li postoje grafikoni?", "Da. Dashboard i grafikoni su namenjeni brzom razumevanju realizacije i odstupanja."),
        ],
        "related": [("Računovodstvo škole", "../finansijski-sistem-za-skole/"), ("SPIRI izvodi za škole", "../spiri-izvodi-skole/"), ("Budžetsko knjigovodstvo škola", "../budzetsko-knjigovodstvo-skola/")],
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
                "dateModified": LASTMOD,
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
    faq = "\n".join(
        f'''<article class="faq-item">
          <h3>{e(question)}</h3>
          <p>{e(answer)}</p>
        </article>'''
        for question, answer in page["faq"]
    )
    related = "".join(f'<a href="{e(href)}">{e(label)} &rarr;</a>' for label, href in page["related"])
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
  <meta property="og:image:alt" content="Budžet+ za škole">
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
        <h2>Česta pitanja</h2>
        <div class="faq-list landing-faq">
          {faq}
        </div>
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
      <p><strong>Budžet+ za škole</strong><br>Program za računovodstvo škola</p>
      <p>Alpeon Softver · 065 917 0989<br><a href="mailto:aleksandar.pejkovic@budzetplus.rs">aleksandar.pejkovic@budzetplus.rs</a></p>
    </div>
  </footer>
</body>
</html>
'''


def write_sitemap() -> None:
    urls = [f"{BASE}/"] + [f"{BASE}/{page['slug']}/" for page in PAGES]
    body = "\n".join(f"  <url><loc>{url}</loc><lastmod>{LASTMOD}</lastmod></url>" for url in urls)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n',
        encoding="utf-8",
    )


def main() -> None:
    for page in PAGES:
        target = ROOT / page["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(page), encoding="utf-8")
    write_sitemap()


if __name__ == "__main__":
    main()
