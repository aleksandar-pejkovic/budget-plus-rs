# Direktna prijava — Cloudflare podešavanje

Sajt ostaje na GitHub Pages. Worker `budzetplus-contact` prima zahteve na `/contact` i prosleđuje ih na poslovni email. Nema baze prijava, automatskog odgovora posetiocu ni zapisivanja sadržaja forme u logove.

## Status integracije

- Javni Turnstile sitekey: `0x4AAAAAAE9Nwd4FcUgAfd87`.
- Forma: `assets/contact.js`; javna konfiguracija: `assets/contact-config.js`.
- Obrada: `worker/src/index.ts`; konfiguracija: `worker/wrangler.jsonc`.
- Akcija: `contact`. Produkcijski hostname-ovi: `budzetplus.rs`, `www.budzetplus.rs`.
- Backend proverava `success === true`, akciju i hostname. Istečene ili ponovljene tokene odbacuje Siteverify. Browser resetuje widget posle svakog zahteva.
- Korisnik je potvrdio da je sačuvao `TURNSTILE_SECRET` u Worker-u. Primalac je postojeći Google alias `prijava@budzetplus.rs`, a pošiljalac postojeći alias `prijava@budzetplus.rs`; oba pripadaju nalogu `aleksandar.pejkovic@budzetplus.rs` na Google Workspace Business Standard. Slanje prelazi na Google Workspace. Kod koristi Nodemailer preko TLS veze sa smtp.gmail.com:465. SMTP_USER je glavni Google nalog, a SMTP_PASSWORD je app password u Worker secret store-u; korisnik je potvrdio da ga je sačuvao. Cloudflare EMAIL binding je uklonjen. Lokalni testovi koriste simulirane Cloudflare odgovore; to nije dokaz stvarnog slanja ili validacije widgeta.
- Lokalna provera: 8 serverskih/validacionih testova i 8 browser testova prolaze, kao i TypeScript provera, Worker dry-run i provera 13 HTML stranica.

## Podešavanje u Cloudflare panelu

1. Workers & Pages → Create application → Create Worker / Hello World. Naziv: `budzetplus-contact`. Privremeni Hello World nije završen servis za prijave.
2. U Worker Settings → Variables and Secrets dodati **Secret** `TURNSTILE_SECRET`, sa tajnim ključem postojećeg widgeta. Ne slati ključ u chat i ne unositi ga u frontend ili GitHub.
3. Ne aktivirati Cloudflare Email Routing niti plaćeni Email Sending. Panel je ponudio MX zapise za glavni domen, što ne odgovara postojećem Google mailu. Sačuvati Google MX i SPF. Podesiti autorizovano slanje preko Google Workspace-a sa aliasa `prijava@budzetplus.rs`; autentifikacija koristi SMTP_USER i SMTP_PASSWORD, bez čitanja tajni u ovoj sesiji.
4. Objaviti Worker sa Google SMTP transportom. Konfiguracija postavlja dozvoljene origine, hostname-ove, fiksnog pošiljaoca/primaoca i ograničenje od 5 zahteva u 60 sekundi po IP adresi. Rate limiting je Cloudflare lokalno ograničenje, ne globalni brojač.
5. Forma koristi `https://budzetplus-contact.pejko89-ap.workers.dev/contact`. Poseban `api` poddomen nije potreban. Objaviti i statički sajt sa ažuriranim `assets/contact-config.js`.
6. Proveriti Turnstile hostname-ove i Google autorizaciju za slanje sa aliasa. Zatim probati prijavu sa pravog domena i potvrditi prijem u poslovnom sandučetu.

Ako automatski preuzimamo postojeći secret, pratiti [Turnstile existing-widget flow](https://developers.cloudflare.com/turnstile/spin/prompt.md): odobren apsolutni Wrangler izvan repozitorijuma, tačna verzija, account ID, postojeći Worker i manifest odredišta pre preuzimanja/upisa. Lokalni Wrangler u projektu služi za generisanje tipova, dry-run i razvoj bez tajni; ne koristiti ga za automatsko preuzimanje widget secret-a.

## Lokalna provera

Worker je objavljen 19. septembra 2026, verzija `012e9a2d-1d9e-4c11-aa9b-6f5bfef1c81f`. Javne provere: CORS preflight 204 sa ispravnim originom, prazna prijava 422, neispravan Turnstile token 403. Nije poslat email. Stvarno SMTP slanje i prijava sa svežim Turnstile tokenom ostaju za proveru nakon objave statičke forme. Sačuvani secrets nisu čitani niti menjani.

```sh
npm ci
npm run worker:types
npm run typecheck
npm test
npm run worker:check
python scripts/home_page.py
python scripts/generate_seo_pages.py
python scripts/check_site.py
npx playwright install chromium
npm run test:ui
```

Ne dodavati `localhost` u produkcijsku serversku listu hostname-ova. UI testovi simuliraju widget i email endpoint i ne šalju email. Za ručno lokalno testiranje sa Cloudflare test ključevima koristiti zasebnu lokalnu konfiguraciju, bez promena produkcijskih dozvola.

## Prihvatanje i održavanje

### SMTP dijagnostika (20. septembar 2026)

Prva dijagnostička verzija: `436ed7e1-2e50-4b15-8eea-009b0c847a62`.
Ponovljena prijava je zabeležila `ESOCKET`, `smtpStatus: null`, `stage: connection`.
Cloudflare remote preview je bez kredencijala i slanja mejla ponovio isti neuspeh
sa podrazumevanim Nodemailer transportom; direktna TLS veza na hostname prošla je
SMTP `verify()`. Nodemailer podrazumevano razrešava hostname i prosleđuje IP TLS-u.

Ispravka koristi `getSocket` i `node:tls.connect` sa hostname-om `smtp.gmail.com`,
portom 465, eksplicitnim SNI i uključenom proverom sertifikata. Socket se predaje
Nodemailer-u tek posle TLS handshake-a, uz `secured: true`, rok od 8 sekundi i
zatvaranje pri neuspehu. Nema promene provajdera, DNS-a, aliasa ili secrets.
I stvarni helper ispravke je prošao SMTP proveru u remote preview-u.

Objavljena verzija sa ispravkom: `4cf71ec8-982e-4401-a81a-421b308f61fb`.
Prošlo je 12 serverskih testova, 10 browser testova, TypeScript provera i Worker dry-run.
Korisnik je nakon objave ponovio prijavu i potvrdio uspeh forme i prijem mejla u
sandučetu. Time je potvrđena stvarna isporuka, pored SMTP provere transporta.

`contact_email_failed` sada sadrži samo `event`, `code`, `smtpStatus` i `stage`.
Kod mora biti na dozvoljenoj listi; ostali postaju `UNKNOWN`. SMTP status je ceo broj
od 200 do 599 ili `null` kada nije poznat. Faza je kontrolisana oznaka, nikada sirova
SMTP komanda. Ne beleže se exception message/stack/cause, server response, adrese,
sadržaj forme, lozinke ili tokeni. Nodemailer `logger` i `debug` ostaju isključeni.
Javni odgovor ostaje HTTP 503 sa kodom `delivery_unavailable`, a unos ostaje u formi.

Praćenje jedne ponovljene prijave:

```sh
npx wrangler tail budzetplus-contact --config worker/wrangler.jsonc --format pretty --search contact_
```

- `authentication` / `EAUTH`: proveriti Google app password za postojeći `SMTP_USER`; ne slati lozinku u chat ili logove.
- `connection` / `tls`: proveriti vezu i TLS transport prema postojećem Google SMTP serveru.
- `sender`: proveriti autorizaciju pošiljaočevog aliasa; `recipient`: proveriti odbijanje primaoca.
- `acceptance`: poziv je završen bez očekivanog primaoca u listi prihvaćenih adresa.
- `setup`, `greeting`, `message`, `close` ili `send`: koristiti kod i status za dalju ciljanu proveru; `send` znači da preciznija faza nije dostupna.

Početna putanja Worker-a `/` očekivano vraća `not_found`; prijava se šalje putem
forme na sajtu na `/contact`. Nakon ciljane ispravke ponoviti prijavu, proveriti
HTTP 200 i zasebno potvrditi prijem u sandučetu. Ne menjati provajdera ili DNS bez dogovora.

- Testirati jednu stvarnu uspešnu prijavu i odbijanje ponovnog korišćenja istog tokena; potvrditi rezultat u sandučetu. Ne tvrditi da je poruka isporučena samo zato što ju je email servis prihvatio.
- Proveriti pogrešan domen/akciju, istekao token, mrežnu grešku, ograničenje zahteva i neuspeh email servisa. Unos ostaje u formi pri grešci.
- Email sadrži samo podatke upita; adresa posetioca koristi se kao Reply-To, nikada kao pošiljalac ili odredište.
- Posmatrati događaje `contact_accepted` i `contact_email_failed` bez ličnih podataka. Ne uključivati request-body logovanje.
- U slučaju problema vratiti prethodnu verziju Worker-a; email i telefon u formi ostaju dostupni kao rezerva.
