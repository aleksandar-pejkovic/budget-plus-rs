# Pregled izmene početne strane (12.11.2026)

- Glavna poruka: „Knjiženje SPIRI izvoda. Direktno iz programa.”
- Umesto isečka konta: jasno označen šematski postupak, bez izmišljanja ekrana programa. Pravi postojeći nalog ostaje kao opcioni, uvećivi primer u celini.
- Istaknuti SPIRI izvodi, priprema fajla za kumulativno plaćanje i uplate učenika uz proveru predložene raspodele.
- Usklađeni izvori generatora i pripadajuće stranice o izvodima/uplatama. Forme, video-zapisi, kontakti i kalendar nisu menjani.
- Izvor mogućnosti: izdanje v1.14.0 (25.10.2026), https://github.com/aleksandar-pejkovic/budgetplus-updates/releases/tag/v1.14.0 i provereni aktuelni kod, uključujući pages/spiri-izvodi.vue. Za SPIRI pristup navedeni nalog i VPN. Fajl za plaćanje nije samo izvršenje plaćanja.

## Provere

Prošli: generatori i SEO/link/JSON-LD provera svih 12 stranica; generisanje Worker tipova i TypeScript; 12 unit testova kontakt servisa; Worker build dry-run; git diff --check.

U podržanom cloud browser-u vizuelno pregledani desktop i mobilni prikaz (390 px iframe), otvaranje glavnog SPIRI linka i povratak, mobilni meni otvaranje/zatvaranje Escape, prelazak na kontakt sa vidljivim prvim poljem. Nije slata forma niti kontaktirana škola.

Puna Playwright/WCAG automatizovana UI provera NIJE izvršena: browser ne može da pokrene socket u okruženju. Pre merge treba izvršiti CI test:ui (testovi su ažurirani za novi sadržaj i novu navigaciju). Dodatni PLAYWRIGHT_CHROMIUM_EXECUTABLE opcioni parametar omogućava upotrebu postojećeg browser-a, bez promene CI podrazumevanja.

Bez spajanja na main, bez objave i bez slanja kampanje. Čeka se odobrenje vlasnika.
