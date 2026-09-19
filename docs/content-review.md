# Dorada sadržaja — 19. septembar 2026.

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
