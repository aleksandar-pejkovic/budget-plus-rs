# Dorada sadržaja — 19. septembar 2026.

## Prikazi avansa — 25. septembar 2026.

Dodati su snimci stvarnog lokalnog interfejsa Budžet+ 1.11.1: `demo-avans-isplata.png` (1024 × 744) uz SPIRI izvode i `demo-avans-zatvaranje.png` (1024 × 952) uz konačne e-fakture. Slike su uz odgovarajuće odeljke `#avansi`, sa opisom demonstracionih podataka i postojećim uvećavanjem.

Izvor je postojeći `budget-plus-client/.output` build od 23.09.2026. u 17:43:30 UTC. Radno stablo klijenta bilo je čisto, HEAD `201913e`; postupak je proveren prema `components/file/AutoPostingUploader.vue` i `utils/directReports.ts`. Snimljeni paneli odgovaraju tim komponentama. Izvorni kod i build aplikacije nisu menjani.

Headless Chromium je radio na lokalnoj adresi sa lokalnim simuliranim API odgovorima, izmišljenim korisnikom i partnerom „Primer dobavljača“. Primer povezuje avans od 12.000 dinara sa konačnom fakturom od 20.000 dinara i ostatkom od 8.000 dinara. Izabrana je demonstraciona kategorija „Avansi za materijal“, sa saldom 12.000 dinara i datumom naloga 25.09.2026.

Dozvoljeni su samo lokalni zahtevi za podatke i simulirani preview pozivi. Potvrda knjiženja nije pozvana; nijedan produkcioni servis nije kontaktiran. PNG snimci su napravljeni direktno iz relevantnih panela u svetloj temi, pri dvostrukoj gustini piksela, bez naknadne izmene sadržaja.

## Zamena starih prikaza programa — 20. septembar 2026.

Ova dopuna zamenjuje odluku iz prethodnog koraka da se stare samostalne slike zadrže. Dodata su četiri nova snimka lokalnog FE-a 1.11.1. Tri ranije dodate slike iz uputstava 1.11.0 ostaju. Nisu menjani opisi procesa niti dodavani novi mediji na ostale stranice.

| Stranica | Nova datoteka u `assets/img` | Dimenzije | Snimljeni prikaz |
| --- | --- | --- | --- |
| Početna | `demo-kontrolna-tabla.png` | 1280 × 617 | Odeljak „Svi moduli“ kontrolne table |
| Povezano računovodstvo | `demo-nalog.png` | 1760 × 557 | Nalog 0042 sa dve demonstracione stavke, ukupno 12.000,00 na obe strane |
| Izvršenje budžeta | `demo-grafikoni.png` | 1280 × 1033 | Četiri grafikona, plan 6.000.000, troškovi 4.200.000 i prihodi 4.800.000 |
| Zatvaranje godine | `demo-zatvaranje-godine.png` | 768 × 803 | Opciona priprema amortizacije i koraci 1–2, bez izvršavanja radnji |

**Poreklo:** postojeći lokalni FE build `budget-plus-client/.output`, napravljen 19.09.2026. u 20:37:23 UTC (`.output/nitro.json`), sa verzijom 1.11.1. Prikazi su provereni prema čistom radnom stablu na commitu `3cf41e8b7e564f2a56b849ebacc9fcc1fe205079`; poslednja izmena relevantnih stranica i komponenti je `888d73dd4116e13b91abd5984e578b8529d4879c` od 14.09.2026. Posle neuspelog pokretanja razvojnog servera iz privremene kopije, korišćen je taj postojeći build bez ponovnog buildovanja ili izmene FE izvora.

Snimanje je izvršeno Chromium/Playwright pregledačem na lokalnoj adresi, sa lokalnim simuliranim GET API odgovorima, izmišljenim korisnikom i dobavljačem i poslovnom godinom 2026. Sat pregledača postavljen je na 31.12.2026. Pregledaču su dozvoljeni samo lokalni FE i simulator; ostali zahtevi su blokirani. Nije kontaktiran produkcioni backend, korišćen stvarni korisnički token niti izvršeno knjiženje. Sačekani su hidratacija i završetak animacija grafikona. Snimljeni su relevantni paneli, bez naknadne izmene njihovih podataka, boja ili proporcija.

`docs/pdf-guides/assets/year-end.png` nije korišćen: FE `AUDIT.md` izričito ga označava kao zastarelog zbog stare numeracije i potvrđuje da nije deo aktuelnog PDF-a 19. Novi snimak prikazuje „Priprema — amortizacija / Opciono“, zatim „1. Zatvaranje rashoda i prihoda“ i „2. Otvaranje naredne godine“. Statusi „Nije kreiran“ i onemogućen prenos predstavljaju stanje pre završnih knjiženja.

Generatori koriste nove datoteke i stvarne dimenzije. Uvodni prikaz više ne koristi fiksni odnos stranica ni isecanje slike. Svih sedam samostalnih slika ima napomenu o demonstracionim podacima i verziji. Video-snimci, njihove putanje i naslovne slike ostaju isti, uz izričitu napomenu da prikazuju stariju verziju. Stare datoteke su sačuvane zbog tih referenci i postojećih direktnih linkova.

**Provera:** svih 10 UI i 8 kontakt testova prolazi; linkovi i metapodaci su ispravni na svih 13 stranica. Generisanje početne i detaljnih stranica je bajt-po-bajt ponovljivo. Svih sedam slika dodatno je provereno na 390 i 1440 px: učitavanje, proporcije, ograničenje prirodnom širinom, napomena, otvaranje dijaloga tastaturom, Escape i povratak fokusa. Vizuelno su pregledane četiri zamene i njihovi dijalozi na obe širine, kao i početni ekran na 360 i 1440 px. Proverena je promena videa i očuvanje njegovog starog postera. Sitni detalji širokih prikaza na telefonu ostaju ograničeni širinom ekrana. Lokalni FE server je ugašen nakon snimanja. Nema commita, push-a ili objave.

## Slike iz FE uputstava — 20. septembar 2026.

U odeljak „Pogledajte program“ dodate su tri postojeće slike iz `budget-plus-client/docs/pdf-guides/assets`, iz uputstava za verziju 1.11.0. Sadrže demonstracione podatke i nisu predstavljene kao snimci najnovije verzije. Izvorne FE datoteke nisu menjane; PNG kopije su bajt-po-bajt identične, bez isecanja, izmene podataka ili boja.

| Izvor | Kopija u `assets/img` | Izvorne dimenzije |
| --- | --- | --- |
| `invoices.png` | `uputstvo-e-fakture.png` | 2040 × 1502 |
| `assets.png` | `uputstvo-osnovna-sredstva.png` | 1728 × 618 |
| `form5.png` | `uputstvo-obrazac-5.png` | 672 × 599 |

Kratki opisi su „Pregled e-faktura i knjiženje iz programa“, „Pregled evidencije osnovnih sredstava“ i „Priprema Obrasca 5 za ISPFI“. Svaki ima napomenu „Demonstracioni podaci. Izgled zavisi od verzije.“ E-faktura prikazuje status „Nije knjiženo“ i dostupno dugme za knjiženje, ne dokaz izvršenog knjiženja. Evidencija sredstava prikazuje vrednosti i lokaciju; Obrazac 5 izbor perioda, podatke izveštaja i dugme za preuzimanje.

Slike su definisane kroz `scripts/solution_content.py`, sa stvarnim dimenzijama i postojećim dijalogom za uvećanje. CSS zadržava prirodnu širinu slike uz ograničenje širinom sadržaja; Obrazac 5 se na računaru prikazuje najviše na 672 px. Ostali mediji, početna strana, opisi procesa i javni API-ji ostaju nepromenjeni.

Provera: prošlo je svih 10 postojećih UI testova (prikaz na pet širina, WCAG A/AA, navigacija, dijalog i forma), svih 8 kontakt testova, provera linkova i metapodataka za 13 stranica i bajt-po-bajt ponovljivost generisanja. Za sve tri nove slike dodatno su provereni učitavanje, proporcije, prirodna širina, otvaranje dijaloga tastaturom, Escape i povratak fokusa na 390 i 1440 px. Vizuelno su pregledani prikazi slika i dijalozi na obe širine. Široke tabele na telefonu služe kao pregled; sitni tekst je ograničen širinom ekrana i u postojećem dijalogu. Nisu pokretani FE ni backend, niti su izvršeni commit, push ili objava.

## Fokus na korist i automatizaciju — 20. septembar 2026.

Ova dorada zamenjuje prethodni prikaz kroz tri koraka na detaljnim stranicama. Svih 12 rešenja sada sadrži kratak odeljak „Kako radi“, uz uvod, koristi, poziv za prezentaciju i povezana rešenja. Uklonjeni su ilustrativni primeri i tabele, priprema, kontrolne liste, numerisani koraci i bočna navigacija. Nepotrebna polja i prikaz tih odeljaka uklonjeni su iz generatora.

Automatsko knjiženje je u prvom planu na stranicama izvoda, e-faktura i ISKRA obračuna. Zadržana su kratka objašnjenja avansa, IFISUP uvoza i zajedničkog čuvanja knjiženja i evidencije sredstava. Priprema dokumenata za SPIRI, ORIS i ISPFI nije predstavljena kao izvršavanje plaćanja ili predaja izveštaja. Stvarne slike i video ostaju u opcionom odeljku „Pogledajte program“; stranice bez medija nemaju prazan odeljak.

Prošlo je svih 10 UI testova i 8 kontakt testova, provere linkova i metapodataka na 13 stranica i ponovljivost generisanja. Test navigacije sada proverava link između avansa iz izvoda i konačne fakture, povezano rešenje i prijavu sa izabranom temom. Sačuvana je provera vidljivosti trake sistema u prvom ekranu. Vizuelno su pregledani mobilna stranica SPIRI izvoda bez medija i desktop stranica izvršenja budžeta sa slikom. Izmene nisu objavljene.

## Pojednostavljen prikaz — 20. septembar 2026.

Najnovija dorada predstavlja po jedan najjednostavniji podržani postupak kroz tri kratka koraka na svih 12 detaljnih stranica. Koraci sada imaju naslov i kratko objašnjenje, a tehničke kontrole su izdvojene ispod primera. Početna strana ima tri koraka i rezultat prikazan kao rečenicu.

E-fakture se predstavljaju kroz SEF pregled i direktno knjiženje (`budget-plus-client/pages/e-fakture/index.vue`), a finansijski plan kroz učitavanje Excel plana iz IFISUP-a (`pages/finansijski-plan/[id].vue`). IFISUP nije predstavljen kao direktna sinhronizacija. Alternativni ručni/XML unos e-faktura, ručni unos plana i alternativni unos sredstava nisu deo glavnog prezentacionog opisa. Za osnovna sredstva zadržan je potvrđeni tok jedne XML e-fakture.

Avansi su istaknuti na početnoj i u otvorenim blokovima na stranicama e-faktura i SPIRI izvoda, sa međusobnim linkovima. Opis je zasnovan na odeljku „Knjiženje avansa“ u README-u proizvoda, `components/file/AutoPostingUploader.vue` i SEF pregledu: isplata iz izvoda, zatvaranje uz konačnu fakturu, izbor kategorije samo kada je potreban i pregled salda na datum naloga. Zasebno knjiženje avansnog računa nije obećano.

Traka sistema je u prvom ekranu na 1366×768, 1440×900, 360×800 i 390×844; na telefonu prethodi slici programa. Dodata je regresiona provera njenih granica nakon učitavanja fontova. Prošlo je svih 10 UI testova i 8 testova kontakt funkcionalnosti, provera metapodataka i linkova za 13 stranica, kao i provera ponovljivosti generisanja. Svih 12 oblasti je sačuvano. Pregledani su snimci prvog ekrana na telefonu i računaru, mobilne stranice e-faktura i desktop stranice izvršenja budžeta. Nema objave.

## Dopuna — 20. septembar 2026.

Šest kartica odmah iza uvoda sada prikazuje konkretne koristi bez dodatne interakcije. Poslednja ima odvojene linkove za uplate učenika i završetak godine. Postojeći pregled rešenja i sve naredne sekcije su sačuvani; pregled i dalje obuhvata svih 12 oblasti.

Postupak osnovnih sredstava proveren je u `budget-plus-client/components/file/AutoPostingUploader.vue` (jedan XML, priprema, pregled i potvrda), `components/invoice/FixedAssetWizard.vue` (raspored stavki, vrsta, stopa, kompletan nalog i zajedničko čuvanje) i `pages/osnovna-sredstva/index.vue` (Excel uvoz bez knjiženja). Stranica opisuje ovaj tok i ilustrativnu nabavku projektora; ručni unos i Excel uvoz ostaju zasebne mogućnosti. Stranica e-faktura vodi direktno na postupak.

Provera: svih 13 stranica prolazi proveru metapodataka i linkova; ponovno generisanje daje iste datoteke. Svih 12 oblasti je prisutno u pregledu početne strane. Prošlo je 9 postojećih UI testova (pet širina 360–1440 px bez prelivanja, WCAG A/AA uključujući kontrast, navigacija i forma) i 8 testova kontakt funkcionalnosti. Vizuelno su pregledani snimci početne i stranice osnovnih sredstava na 390 i 1440 px. Izmena nije objavljena.

Početna strana sada predstavlja Budžet+ kao program za budžetsko računovodstvo škola. Svih 12 tematskih stranica dobilo je pripremu ulaza, stvarni postupak, ilustrativan rezultat i provere računovođe. URL-ovi su sačuvani.

## Izvori i granice tvrdnji

Izvori su lokalna dokumentacija i implementacija proizvoda, ne pretpostavljena računovodstvena pravila. Putanje ispod su relativne prema odgovarajućem repozitorijumu.

| Oblast | Provereni izvor |
| --- | --- |
| Obim programa i povezane evidencije | `budget-plus-client/README.md` |
| Učitavanje e-faktura, izvoda i obračuna | `budget-plus-client/components/file/AutoPostingUploader.vue` i README odeljak o avansima |
| ISKRA zaglavlja i validacija | `budget-plus/src/main/java/com/budgetplus/feature/automation/posting/xlsx/parser/IskraTemplateValidator.java` i `IskraTemplateSupport.java` |
| Jedan ili dva ISKRA naloga | `budget-plus-client/components/file/IskraSplitUploader.vue` i README odeljak „Opciono razdvajanje ISKRA obračuna“ |
| Kumulativno i ručno plaćanje | `budget-plus-client/pages/spiri/xml.vue` i `manual.vue` |
| ORIS i Obrazac 5 | `budget-plus-client/pages/izvestaji/oris-export.vue` i `trezor.vue` |
| Izvršenje budžeta | `budget-plus-client/pages/izvestaji/izvrsenje-budzeta.vue`, README i postojeći prikaz grafikona |
| Osnovna sredstva | `budget-plus-client/pages/osnovna-sredstva/index.vue` i README |
| Uplate učenika | `budget-plus-client/pages/ucenicki-servis/placanja/index.vue` |
| Zatvaranje godine | `budget-plus-client/docs/year-end-guidance.md` |

ISKRA format nije izjednačen sa opštim Excel šablonom. Prevoz nije oglašen kao podržana varijanta istog ISKRA ulaza jer pregledani parseri potvrđuju plate i bolovanja. ORIS postupak prati postojeći izbor meseca i godine, bez izmišljenog posebnog dugmeta za kontrole.

Tabele su označene kao ilustracije, ne kao snimci aplikacije. Ne sadrže stvarne učenike, ustanove, račune za plaćanje ili identifikatore. Postojeće slike naloga, grafikona i završnih radnji pregledane su pre ponovnog korišćenja; ne prikazuju imena zaposlenih ili učenika. Video plate je postojeća demonstracija rezultata, ne uputstvo za aktuelni dijalog uvoza; pregledani su reprezentativni kadrovi. Uz vizuale je naznačeno da izgled zavisi od verzije.

## Održavanje i provera

- `scripts/solution_content.py`: priprema, postupak, primeri, provere i opciona slika/video po temi.
- `scripts/solution_renderer.py`: zajednički semantički HTML prikaz.
- `scripts/reorganize_pages.py`: metapodaci, povezana rešenja, generisanje HTML-a i sitemap-a. `generate_seo_pages.py` ostaje kompatibilna ulazna tačka.
- Pokrenuti generator, zatim `scripts/check_site.py`. Ponovno generisanje mora dati identične datoteke.
- Izolovani Chromium testovi proverili su svih 13 stranica na širinama 360, 390, 768, 1024 i 1440 px: nema horizontalnog prelivanja i svaka stranica ima jedan glavni naslov. Automatske WCAG A/AA provere su prošle. Provereni su mobilni meni, tastatura, dijalog za slike i ponašanje forme; sačuvani su snimci stranica na 390 i 1440 px. Ručno je pregledan desktop uvod početne stranice; potpuna ručna vizuelna provera svih stranica ostaje zaseban korak.

Ovo je opis proizvoda, ne novi stručni vodič niti tumačenje propisa. Datum u sitemap-u i strukturiranim podacima odgovara ovoj izmeni sadržaja.

## Novi prikazi — 25. septembar 2026.

Dodato je sedam prikaza na šest tematskih stranica: izbor e-faktura za SPIRI, plaćanje iz sačuvanog šablona, raspored osnovnih sredstava i pregled naloga, ORIS period, tabela izvršenja budžeta i promet konta za partnera. Postojeće slike su sačuvane. Početna strana i uplate učenika nisu menjane.

Pet snimaka interfejsa napravljeno je u headless Chromium-u iz izolovano izgrađene kopije lokalnog `budget-plus-client` 1.11.1 (HEAD `05fe76d`, uz tadašnje lokalne izvore). Originalni projekat nije menjan. Lokalni demonstracioni API vraćao je izmišljene ustanove, partnere i dokumente; pristup spoljnim servisima bio je blokiran. Nije pokrenuto stvarno knjiženje, plaćanje ili izvoz. Primer stavki osnovnog sredstva prati konta i strane knjiženja iz `InvoiceAssetPostingService.createAsset`; nazivi konta provereni su u izvornom kontnom planu.

Tabela izvršenja i promet partnera su prikazi originalnih backend HTML šablona izveštaja (`budgetExecution.html`, `account.html`, `layout.html` i `main.css`), popunjenih demonstracionim podacima kroz Thymeleaf i snimljenih u Chromium-u. Nisu snimci PDF preglednika. Na sajtu su označeni kao primeri izveštaja. Postupak snimanja i demo podaci ostaju u lokalnim `.cache/capture-product.mjs` i `.cache/report-runtime/DemoReports.java`.

Provere: metapodaci i lokalni linkovi za 13 stranica, svih 10 postojećih UI testova (pet širina, WCAG A/AA, navigacija i forma), učitavanje i uvećavanje svih sedam novih slika na 390 i 1440 px. Slike imaju opis, dimenzije i odloženo učitavanje; uži obrasci imaju ograničenu širinu prikaza. Izmene nisu objavljene.
