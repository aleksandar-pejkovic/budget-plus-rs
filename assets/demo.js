(function () {
  const root = document.querySelector('[data-demo-root]');
  if (!root) return;

  const accountNames = {
    '011222': 'Računarska oprema', '015122': 'Oprema u pripremi', '121112': 'Žiro račun',
    '121712': 'Ostala potraživanja', '122192': 'Potraživanja od RFZO', '123211': 'Dati avansi za materijal',
    '131211': 'Obračunati neplaćeni rashodi', '231111': 'Obaveze za neto plate',
    '232111': 'Obaveze po osnovu neto naknada zaposlenima', '232211': 'Obaveze za poreze na naknade',
    '233111': 'Obaveze po osnovu neto isplata nagrada', '233211': 'Obaveze za poreze na nagrade',
    '234111': 'Obaveze za porez na zarade', '236122': 'Obaveze po osnovu naknade zarade',
    '236211': 'Obaveze za porez na naknadu zarade', '252111': 'Dobavljači u zemlji',
    '291211': 'Razgraničeni rashodi za materijal', '291911': 'Ostala pasivna vremenska razgraničenja',
    '311112': 'Kapital u opremi', '311151': 'Nefinansijska imovina u pripremi',
    '411111': 'Plate i dodaci zaposlenih', '412111': 'Doprinos za PIO',
    '414121': 'Bolovanje preko 30 dana', '415112': 'Naknade troškova za prevoz na posao i sa posla',
    '416111': 'Jubilarne nagrade', '423411': 'Usluge informisanja', '426111': 'Kancelarijski materijal',
    '733121': 'Tekući transferi od drugih nivoa vlasti',
  };

  const r = (account, debit, credit, options) => ({
    date: '18.09.2026.', document: 'DEMO-2026', account, name: accountNames[account] || 'Konto iz dokumenta',
    debit, credit, cost: '009990101', partner: '—', source: '01', program: '2003', activity: '0001',
    ...options,
  });

  const stories = {
    ordinary: {
      icon: '▤', title: 'Obična faktura i izvod', short: 'Od eFakture do rashoda i zatvaranja obaveze.',
      journal: 'DEMO-01', date: '18.09.2026.',
      steps: [
        {
          title: 'Najpre knjižimo eFakturu', help: 'Kliknite „Knjiži iz dokumenta“ i učitajte probnu eFakturu.',
          file: 'assets/demo/obicna-efaktura.xml', accept: '.xml',
          note: 'Budžet+ je pronašao partnera i pripremio obračunati neplaćeni rashod i obavezu prema dobavljaču.',
          rows: [
            r('131211', 65750, 0, { document: 'EF-DEMO-01', cost: '—', source: '—', program: '—', activity: '—' }),
            r('252111', 0, 65750, { document: 'EF-DEMO-01', cost: '—', partner: 'Demo dobavljač d.o.o.', source: '—', program: '—', activity: '—' }),
          ],
        },
        {
          title: 'Sada učitavamo SPIRI izvod', help: 'Izvod zatvara obavezu i prenosi iznos na stvarni rashod.',
          file: 'assets/demo/obicna-faktura-izvod.json', accept: '.json',
          note: 'Obaveza je zatvorena, račun je umanjen, a rashod je prepoznat kao kancelarijski materijal.',
          rows: [
            r('252111', 65750, 0, { document: 'IZVOD-118', partner: 'Demo dobavljač d.o.o.', cost: '—', source: '—', program: '—', activity: '—' }),
            r('121112', 0, 65750, { document: 'IZVOD-118', source: '—', program: '—', activity: '—' }),
            r('426111', 65750, 0, { document: 'IZVOD-118' }),
            r('131211', 0, 65750, { document: 'IZVOD-118', cost: '—', source: '—', program: '—', activity: '—' }),
          ],
        },
      ],
    },
    advance: {
      icon: '↗', title: 'Dati avans i konačna faktura', short: 'Isplata avansa, saldo partnera i pravilno zatvaranje.',
      journal: 'DEMO-02', date: '04.09.2026.',
      steps: [
        {
          title: 'Knjižimo isplatu avansa iz izvoda', help: 'Program prepoznaje šifru plaćanja i materijalni avans.',
          file: 'assets/demo/avans-izvod.json', accept: '.json',
          note: 'Isplata je evidentirana na kontu datog avansa, uz partnera, mesto troška i klasifikacije.',
          rows: [
            r('123211', 75000, 0, { date: '02.09.2026.', document: 'P-AV-001-2026', partner: 'Demo usluge d.o.o.', cost: '—', source: '—', program: '—', activity: '—' }),
            r('121112', 0, 75000, { date: '02.09.2026.', document: 'P-AV-001-2026', source: '—', program: '—', activity: '—' }),
            r('426111', 75000, 0, { date: '02.09.2026.', document: 'P-AV-001-2026', source: '07' }),
            r('291211', 0, 75000, { date: '02.09.2026.', document: 'P-AV-001-2026', partner: 'Demo usluge d.o.o.', cost: '—', source: '—', program: '—', activity: '—' }),
          ],
        },
        {
          title: 'Povezujemo konačnu fakturu', help: 'Budžet+ vidi saldo avansa od 75.000,00 RSD i u celosti ga zatvara kroz konačnu fakturu.',
          file: 'assets/demo/avans-konacna-faktura.xml', accept: '.xml',
          note: 'Materijalni avans od 75.000,00 RSD je u celosti zatvoren. Na dobavljaču nema preostale obaveze.',
          rows: [
            r('131211', 75000, 0, { date: '04.09.2026.', document: 'KF-001-2026', cost: '—', source: '—', program: '—', activity: '—' }),
            r('252111', 0, 75000, { date: '04.09.2026.', document: 'KF-001-2026', partner: 'Demo usluge d.o.o.', cost: '—', source: '—', program: '—', activity: '—' }),
            r('252111', 75000, 0, { date: '04.09.2026.', document: 'KF-001-2026', partner: 'Demo usluge d.o.o.', cost: '—', source: '—', program: '—', activity: '—' }),
            r('123211', 0, 75000, { date: '04.09.2026.', document: 'KF-001-2026', partner: 'Demo usluge d.o.o.', cost: '—', source: '—', program: '—', activity: '—' }),
            r('291211', 75000, 0, { date: '04.09.2026.', document: 'KF-001-2026', partner: 'Demo usluge d.o.o.', cost: '—', source: '—', program: '—', activity: '—' }),
            r('131211', 0, 75000, { date: '04.09.2026.', document: 'KF-001-2026', cost: '—', source: '—', program: '—', activity: '—' }),
          ],
        },
      ],
    },
    transport: {
      icon: '⌁', title: 'Prevoz zaposlenih', short: 'ISKRA obračun, obaveze i grupisan SPIRI izvod.', journal: 'DEMO-03', date: '30.11.2026.',
      steps: [
        { title: 'Učitavamo ISKRA obračun prevoza', help: 'Obračun formira obaveze prema zaposlenima i porezu.', file: 'assets/demo/iskra-prevoz.xlsx', accept: '.xlsx', note: 'Obračun je prepoznat kao prevoz na izvoru 07.', rows: [r('131211', 30000, 0, { document: 'PREVOZ-11-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('232111', 0, 25000, { document: 'PREVOZ-11-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('232211', 0, 5000, { document: 'PREVOZ-11-2026', cost: '—', source: '—', program: '—', activity: '—' })] },
        { title: 'Zatvaramo obaveze izvodom', help: 'Više pojedinačnih isplata program bezbedno grupiše po istim dimenzijama.', file: 'assets/demo/prevoz-izvod.json', accept: '.json', note: 'Stavke prevoza su grupisane, a nalog ostaje pregledan i izbalansiran.', rows: [r('232111', 25000, 0, { document: 'IZVOD-204', cost: '—', source: '—', program: '—', activity: '—' }), r('232211', 5000, 0, { document: 'IZVOD-204', cost: '—', source: '—', program: '—', activity: '—' }), r('121112', 0, 30000, { document: 'IZVOD-204', source: '—', program: '—', activity: '—' }), r('415112', 30000, 0, { document: 'IZVOD-204', source: '07' }), r('131211', 0, 30000, { document: 'IZVOD-204', cost: '—', source: '—', program: '—', activity: '—' })] },
      ],
    },
    jubilee: {
      icon: '★', title: 'Jubilarna nagrada', short: 'Obračun nagrade, poreza i isplata kroz izvod.', journal: 'DEMO-04', date: '30.04.2026.',
      steps: [
        { title: 'Učitavamo obračun jubilarne nagrade', help: 'Budžet+ odvaja neto nagradu i pripadajući porez.', file: 'assets/demo/iskra-jubilarna.xlsx', accept: '.xlsx', note: 'Obračun je pripremljen na kontima obaveze za nagrade.', rows: [r('131211', 50000, 0, { document: 'JUB-04-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('233111', 0, 45000, { document: 'JUB-04-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('233211', 0, 5000, { document: 'JUB-04-2026', cost: '—', source: '—', program: '—', activity: '—' })] },
        { title: 'Knjižimo isplatu sa izvoda', help: 'Izvod zatvara obe obaveze i prenosi iznos na konto jubilarnih nagrada.', file: 'assets/demo/jubilarna-izvod.json', accept: '.json', note: 'Neto nagrada, porez, račun i rashod povezani su u jednom nalogu.', rows: [r('233111', 45000, 0, { document: 'IZVOD-174', cost: '—', source: '—', program: '—', activity: '—' }), r('233211', 5000, 0, { document: 'IZVOD-174', cost: '—', source: '—', program: '—', activity: '—' }), r('121112', 0, 50000, { document: 'IZVOD-174', source: '—', program: '—', activity: '—' }), r('416111', 50000, 0, { document: 'IZVOD-174', source: '07' }), r('131211', 0, 50000, { document: 'IZVOD-174', cost: '—', source: '—', program: '—', activity: '—' })] },
      ],
    },
    salary: {
      icon: '▦', title: 'Plata iz ISKRA obračuna', short: 'Program pravi odvojeni nalog obračuna i nalog isplate.', journal: 'OBR-09', date: '31.08.2026.',
      steps: [
        { title: 'Pravimo nalog obračuna', help: 'ISKRA fajl se proverava i razdvaja na rashode i obaveze.', file: 'assets/demo/iskra-plata.xlsx', accept: '.xlsx', note: 'Zbir obaveza odgovara iznosu na kontu 131211.', rows: [r('131211', 100000, 0, { document: 'PLATA-08-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('231111', 0, 70000, { document: 'PLATA-08-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('234111', 0, 30000, { document: 'PLATA-08-2026', cost: '—', source: '—', program: '—', activity: '—' })] },
        { title: 'Budžet+ otvara poseban nalog isplate', help: 'Prelazimo na drugi nalog koji program priprema iz istog obračuna.', file: 'assets/demo/iskra-plata.xlsx', accept: '.xlsx', replace: true, journal: 'ISP-09', date: '05.09.2026.', note: 'Ovo je odvojeni nalog isplate. Obračunski nalog ostaje sačuvan.', rows: [r('121112', 100000, 0, { document: 'PLATA-08-2026', source: '01', program: '—', activity: '—' }), r('733121', 0, 100000, { document: 'PLATA-08-2026', cost: '—', source: '01', program: '—', activity: '—' }), r('231111', 70000, 0, { document: 'PLATA-08-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('234111', 30000, 0, { document: 'PLATA-08-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('121112', 0, 100000, { document: 'PLATA-08-2026', source: '01', program: '—', activity: '—' }), r('411111', 80000, 0, { document: 'PLATA-08-2026' }), r('412111', 20000, 0, { document: 'PLATA-08-2026' }), r('131211', 0, 100000, { document: 'PLATA-08-2026', cost: '—', source: '—', program: '—', activity: '—' })] },
      ],
    },
    sick: {
      icon: '+', title: 'Bolovanje preko 30 dana', short: 'Poseban RFZO tok iz obračuna, sa ugrađenim kontrolama.', journal: 'OBR-10', date: '31.07.2026.',
      steps: [
        { title: 'Knjižimo obračun bolovanja', help: 'Program proverava obaveze, potraživanje od RFZO i ukupan rashod.', file: 'assets/demo/iskra-bolovanje.xlsx', accept: '.xlsx', note: 'Sve tri kontrole ISKRA obračuna su prošle.', rows: [r('131211', 40000, 0, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('236122', 0, 30000, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('236211', 0, 10000, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('122192', 40000, 0, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('291911', 0, 40000, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' })] },
        { title: 'Pregledamo nalog isplate', help: 'Budžet+ priprema drugi nalog sa potraživanjem, obavezama i rashodom bolovanja.', file: 'assets/demo/iskra-bolovanje.xlsx', accept: '.xlsx', replace: true, journal: 'ISP-10', date: '05.08.2026.', note: 'Obračun i isplata su odvojeni, a oba naloga ostaju proverljiva.', rows: [r('121712', 40000, 0, { document: 'BOLOVANJE-07-2026', source: '01', program: '—', activity: '—' }), r('122192', 0, 40000, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('236122', 30000, 0, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('236211', 10000, 0, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('121712', 0, 40000, { document: 'BOLOVANJE-07-2026', source: '01', program: '—', activity: '—' }), r('414121', 40000, 0, { document: 'BOLOVANJE-07-2026', source: '03' }), r('131211', 0, 40000, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' }), r('414121', -40000, 0, { document: 'BOLOVANJE-07-2026', source: '03' }), r('291911', 40000, 0, { document: 'BOLOVANJE-07-2026', cost: '—', source: '—', program: '—', activity: '—' })] },
      ],
    },
    asset: {
      icon: '▣', title: 'Osnovno sredstvo iz eFakture', short: 'Faktura, zavisni trošak, evidencija sredstva i kompletan nalog.', journal: 'DEMO-07', date: '31.08.2026.', asset: true,
      steps: [{ title: 'Pokrećemo evidenciju osnovnog sredstva', help: 'Učitajte eFakturu, proverite predloženu vrstu opreme i stopu amortizacije.', file: 'assets/demo/osnovno-sredstvo-efaktura.xml', accept: '.xml', note: 'Faktura i osnovno sredstvo sačuvani su zajedno. Instalacija je uključena u nabavnu vrednost servera.', rows: [r('131211', 264000, 0, { document: 'OS-DEMO-01', cost: '—', source: '—', program: '—', activity: '—' }), r('252111', 0, 264000, { document: 'OS-DEMO-01', partner: 'Demo tehnika d.o.o.', cost: '—', source: '—', program: '—', activity: '—' }), r('015122', 264000, 0, { document: 'OS-DEMO-01', cost: '—', source: '—', program: '—', activity: '—' }), r('311151', 0, 264000, { document: 'OS-DEMO-01', cost: '—', source: '—', program: '—', activity: '—' }), r('011222', 264000, 0, { document: 'OS-DEMO-01', cost: '—', source: '—', program: '—', activity: '—' }), r('015122', 0, 264000, { document: 'OS-DEMO-01', cost: '—', source: '—', program: '—', activity: '—' }), r('311151', 264000, 0, { document: 'OS-DEMO-01', cost: '—', source: '—', program: '—', activity: '—' }), r('311112', 0, 264000, { document: 'OS-DEMO-01', cost: '—', source: '—', program: '—', activity: '—' })] }],
    },
  };

  const $ = (selector) => root.querySelector(selector);
  const $$ = (selector) => Array.from(root.querySelectorAll(selector));
  const dashboard = $('[data-demo-dashboard]'); const workspace = $('[data-demo-workspace]');
  const featureView = $('[data-demo-feature-view]'); const storyGrid = $('[data-demo-story-grid]');
  const rowsBody = $('[data-demo-rows]'); const uploadModal = $('[data-demo-upload-modal]');
  const fileInput = $('[data-demo-file-input]'); const feedback = $('[data-demo-feedback]');
  const uploadButton = $('[data-demo-upload]'); const assetModal = $('[data-demo-asset-modal]');
  const lockModal = $('[data-demo-lock-modal]'); const toast = $('[data-demo-toast]');
  const resultNote = $('[data-demo-result-note]');
  let guided = true; let activeStory = null; let stepIndex = 0; let journalRows = []; let assetReview = false; let toastTimer; let pointerRevision = 0;
  const completedStories = new Set();
  const knownHashes = {
    'obicna-efaktura.xml': '734EEFEC46D87EA9525A2AA841260E29BBFD48CB0B57483C7983154FE6B38B89',
    'obicna-faktura-izvod.json': '4F9A09EFE5A8CFF28F28C5FDD26A754E97C877526C1A5A69D97786BCD1D17FF6',
    'avans-izvod.json': 'CB2486837ECF39599D4F581895A3951C4B79B993CA7F86BB11A5F917A2D050BC',
    'avans-konacna-faktura.xml': '26F4FC476A50E350BA125A7FA6B8258BF23412FDD767270AB27E8FFA143B4990',
    'iskra-prevoz.xlsx': 'E0382B1120B6609D79BF737CE78CB7BAFF31F9C5878AF6059BF39BA2B4042614',
    'prevoz-izvod.json': 'B9F01DA0C313463EFE3F3F3F6022B4664358C03B6794B264CEEAF5EC63404E28',
    'iskra-jubilarna.xlsx': '293AEB1E06409AB0D7E97922807A3C08D0F002297E460DA1696A4E619422B624',
    'jubilarna-izvod.json': 'CE6A01A1BA3E27F2E9893A468C5F3E799853E35D1FC500A25CFE84B71B92C2AE',
    'iskra-plata.xlsx': '3F390AEDB57A37960162972D7D8B15891ACABD4063216855EF067401A386E668',
    'iskra-bolovanje.xlsx': '6C6503D01716EBB7701855D450CB31375B58AA63896010891B8C986F3809A1E8',
    'osnovno-sredstvo-efaktura.xml': '921104A39852C86147BC8D8F10ED00D0E8AB728654539A8D234F7B78BA906697',
  };

  const money = (value) => new Intl.NumberFormat('sr-RS', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(value);
  const track = (action, label) => { if (typeof window.gtag === 'function') window.gtag('event', action, { event_category: 'interactive_demo', event_label: label }); };
  function showToast(message) { clearTimeout(toastTimer); toast.textContent = message; toast.hidden = false; toastTimer = setTimeout(() => { toast.hidden = true; }, 3800); }
  function setNav(view) { $$('[data-demo-view]').forEach((button) => button.classList.toggle('is-active', button.dataset.demoView === view)); }

  function syncPointer() {
    const revision = ++pointerRevision;
    root.querySelectorAll('.demo-click-cue').forEach((cue) => cue.remove());
    root.querySelectorAll('.demo-click-target').forEach((target) => target.classList.remove('demo-click-target'));
    // Vodič je miran i nalazi se u zaglavlju radnog prostora; ništa ne prekriva aplikaciju.
  }

  function renderStories() {
    storyGrid.innerHTML = Object.entries(stories).map(([key, story]) => `<button type="button" class="demo-story-card${completedStories.has(key) ? ' is-complete' : ''}" data-story="${key}"><span class="demo-story-icon">${story.icon}</span><strong>${story.title}</strong><span>${story.short}</span><small>${completedStories.has(key) ? 'Proknjiženo ✓' : story.steps.length > 1 ? `${story.steps.length} koraka` : '1 korak'}</small></button>`).join('');
    storyGrid.querySelectorAll('[data-story]').forEach((button) => button.addEventListener('click', () => startStory(button.dataset.story)));
    syncPointer();
  }

  function showDashboard() { activeStory = null; dashboard.hidden = false; workspace.hidden = true; featureView.hidden = true; setNav('dashboard'); renderStories(); }
  function startStory(key) {
    activeStory = key; stepIndex = 0; journalRows = []; assetReview = false;
    dashboard.hidden = true; featureView.hidden = true; workspace.hidden = false; setNav('journal');
    $('[data-demo-journal-number]').textContent = stories[key].journal; $('[data-demo-journal-date]').textContent = stories[key].date;
    $('[data-demo-locked-badge]').hidden = true; $('[data-demo-lock]').hidden = false; $('[data-demo-lock]').disabled = false;
    resultNote.hidden = true; renderJournal(); updateGuide(); track('demo_story_started', key);
  }

  function updateGuide() {
    if (!activeStory) return;
    const story = stories[activeStory]; const complete = stepIndex >= story.steps.length; const step = story.steps[Math.min(stepIndex, story.steps.length - 1)];
    $('[data-demo-guide]').hidden = !guided;
    $('[data-demo-step-count]').textContent = complete ? 'Dokumenti su obrađeni' : `Korak ${stepIndex + 1} od ${story.steps.length}`;
    $('[data-demo-step-title]').textContent = complete ? 'Pregledajte nalog i proknjižite ga kada ste spremni' : step.title;
    $('[data-demo-step-help]').textContent = complete ? 'Možete da proverite konta, klasifikacije i zbir pre potvrde.' : step.help;
    const download = $('[data-demo-download]'); download.href = step.file; download.setAttribute('download', step.file.split('/').pop()); download.hidden = complete;
    $('[data-demo-auto-load]').disabled = complete; $('[data-demo-assets-button]').disabled = activeStory !== 'asset';
    $('[data-demo-progress]').innerHTML = [...Array(story.steps.length + 1)].map((_, index) => `<span class="${index < stepIndex ? 'is-done' : index === stepIndex ? 'is-current' : ''}"></span>`).join('');
    syncPointer();
  }

  function renderJournal(newStart) {
    let debit = 0; let credit = 0;
    if (!journalRows.length) rowsBody.innerHTML = '<tr class="demo-empty-row"><td colspan="12">Nalog trenutno nema poslovnih promena.</td></tr>';
    else rowsBody.innerHTML = journalRows.map((row, index) => {
      debit += row.debit; credit += row.credit;
      return `<tr class="${newStart != null && index >= newStart ? 'is-new' : ''}"><td>${index + 1}</td><td>${row.date}</td><td>${row.document}</td><td>${row.account}</td><td>${row.name}</td><td>${money(row.debit)}</td><td>${money(row.credit)}</td><td>${row.cost}</td><td>${row.partner}</td><td>${row.source}</td><td>${row.program}</td><td>${row.activity}</td></tr>`;
    }).join('');
    $('[data-demo-count]').textContent = String(journalRows.length); $('[data-demo-debit]').textContent = money(debit); $('[data-demo-credit]').textContent = money(credit);
    const balance = debit - credit; $('[data-demo-balance]').textContent = money(Math.abs(balance)); $('[data-demo-balance-status]').textContent = balance === 0 ? 'RSD · izbalansirano' : 'RSD · proverite nalog';
  }

  function applyStep() {
    const story = stories[activeStory]; if (!story || stepIndex >= story.steps.length) return;
    const step = story.steps[stepIndex]; const start = step.replace ? 0 : journalRows.length;
    journalRows = step.replace ? step.rows.slice() : journalRows.concat(step.rows);
    if (step.journal) $('[data-demo-journal-number]').textContent = step.journal;
    if (step.date) $('[data-demo-journal-date]').textContent = step.date;
    renderJournal(start); resultNote.textContent = step.note; resultNote.hidden = false; stepIndex += 1; updateGuide();
    showToast(stepIndex === story.steps.length ? 'Dokument je proknjižen. Nalog je spreman za proveru.' : 'Dokument je proknjižen. Nastavimo na sledeći korak.');
    track('demo_step_completed', `${activeStory}_${stepIndex}`);
  }

  function openUpload() {
    if (!activeStory || stepIndex >= stories[activeStory].steps.length) return;
    const step = stories[activeStory].steps[stepIndex]; fileInput.value = ''; fileInput.accept = step.accept; uploadButton.disabled = true; feedback.textContent = '';
    $('[data-demo-file-help]').textContent = `Podržan format: ${step.accept}. Fajl ostaje na vašem računaru.`; uploadModal.hidden = false; fileInput.focus(); syncPointer();
  }
  function useSample() { uploadModal.hidden = true; if (stories[activeStory].asset) openAssetWizard(); else applyStep(); }
  async function hashFile(file) { const digest = await crypto.subtle.digest('SHA-256', await file.arrayBuffer()); return Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, '0')).join('').toUpperCase(); }

  async function uploadSelected() {
    const file = fileInput.files && fileInput.files[0]; if (!file) return;
    uploadButton.disabled = true; uploadButton.textContent = 'Provera…';
    try {
      const digest = await hashFile(file);
      if (knownHashes[file.name] !== digest) { feedback.textContent = 'Izaberite neizmenjen anonimizovani probni dokument iz ovog demoa.'; return; }
      uploadModal.hidden = true; stories[activeStory].asset ? openAssetWizard() : applyStep();
    } catch (_) { feedback.textContent = 'Dokument nije moguće pročitati u ovom pregledaču.'; }
    finally { uploadButton.textContent = '⇧ Proknjiži'; uploadButton.disabled = !(fileInput.files && fileInput.files[0]); }
  }

  function openAssetWizard() { assetReview = false; renderAssetWizard(); assetModal.hidden = false; syncPointer(); }
  function renderAssetWizard() {
    $('[data-demo-asset-step]').textContent = assetReview ? 'Korak 2 od 2' : 'Korak 1 od 2';
    $('[data-demo-asset-subtitle]').textContent = assetReview ? 'Proverite kompletan nalog pre upisa.' : 'Označite i rasporedite stavke fakture.';
    $('[data-demo-asset-back]').textContent = assetReview ? 'Nazad' : 'Odustani'; $('[data-demo-asset-next]').textContent = assetReview ? 'Potvrdi i proknjiži' : 'Pregled naloga';
    $('[data-demo-asset-body]').innerHTML = assetReview
      ? `<div class="demo-asset-review"><p><strong>Server sa instalacijom</strong> · konačna vrednost ${money(264000)} RSD</p><table><thead><tr><th>Konto</th><th>Duguje</th><th>Potražuje</th></tr></thead><tbody>${stories.asset.steps[0].rows.map((row) => `<tr><td>${row.account} · ${row.name}</td><td>${money(row.debit)}</td><td>${money(row.credit)}</td></tr>`).join('')}</tbody></table></div>`
      : `<div class="demo-asset-line"><h4>Server · bruto ${money(240000)} RSD</h4><p>Predlog je pripremljen iz eFakture. Proverite prema računovodstvenoj politici ustanove.</p><div class="demo-asset-form"><label>Vrsta sredstva<select><option>Računarska oprema</option></select></label><label>Stopa amortizacije (%)<input value="20" type="number"></label><label>Konto pripreme<input value="015122"></label><label>Konačno konto sredstva<input value="011222"></label></div></div><div class="demo-asset-line" style="margin-top:10px"><h4>Instalacija servera · ${money(24000)} RSD</h4><p>Zavisni trošak biće dodat nabavnoj vrednosti servera.</p></div>`;
    syncPointer();
  }

  function feature(view) {
    dashboard.hidden = true; workspace.hidden = true; featureView.hidden = false; setNav(view);
    if (view === 'assets') { startStory('asset'); return; }
    if (view === 'payments') featureView.innerHTML = `<div class="demo-feature-card"><button class="demo-app-button is-muted" data-feature-back>← Kontrolna tabla</button><h3>SPIRI plaćanje iz eFakture</h3><p>Budžet+ prenosi partnera, račun, iznos i klasifikacije. Vi proveravate i preuzimate XML za SPIRI.</p><div class="demo-feature-grid"><article><strong>1. Izaberite fakturu</strong><span>EF-DEMO-01 · Demo dobavljač d.o.o.</span></article><article><strong>2. Proverite podatke</strong><span>426111 · izvor 01 · program 2003 · aktivnost 0001</span></article><article><strong>3. Preuzmite XML</strong><span>Zahtev je spreman za učitavanje u SPIRI.</span></article></div></div>`;
    else featureView.innerHTML = `<div class="demo-feature-card"><button class="demo-app-button is-muted" data-feature-back>← Kontrolna tabla</button><h3>Izveštaji koje računovođa stvarno koristi</h3><p>Od istih poslovnih promena dobijate karticu konta, izvršenje budžeta i fajlove za predaju.</p><div class="demo-feature-grid"><article><strong>Kartica konta</strong><span>Filter po periodu, kontu, izvoru, programu, aktivnosti, mestu troška i partneru.</span></article><article><strong>Izvršenje budžeta</strong><span>Plan i realizacija po ekonomskim klasifikacijama.</span></article><article><strong>ORIS i Obrazac 5</strong><span>Pripremljeni izvozi iz već proknjiženih podataka.</span></article></div><div class="demo-feature-preview demo-report-bars"><div><span>Plate i dodaci</span><i style="--value:82%"></i><b>82%</b></div><div><span>Stalni troškovi</span><i style="--value:64%"></i><b>64%</b></div><div><span>Materijal</span><i style="--value:57%"></i><b>57%</b></div></div></div>`;
    const back = featureView.querySelector('[data-feature-back]'); if (back) back.addEventListener('click', showDashboard);
    syncPointer();
  }

  $$('[data-demo-mode]').forEach((button) => button.addEventListener('click', () => { guided = button.dataset.demoMode === 'guided'; $$('[data-demo-mode]').forEach((item) => { const selected = item === button; item.classList.toggle('is-active', selected); item.setAttribute('aria-pressed', String(selected)); }); if (activeStory) updateGuide(); else syncPointer(); }));
  $$('[data-demo-view]').forEach((button) => button.addEventListener('click', () => button.dataset.demoView === 'dashboard' ? showDashboard() : button.dataset.demoView === 'journal' && activeStory ? (workspace.hidden = false, dashboard.hidden = true, featureView.hidden = true, setNav('journal')) : feature(button.dataset.demoView)));
  $('[data-demo-home]').addEventListener('click', showDashboard); $('[data-demo-back]').addEventListener('click', showDashboard);
  const startButton = document.querySelector('[data-demo-start]');
  if (startButton) startButton.addEventListener('click', () => {
    startStory('ordinary');
    track('interactive_demo_start', 'primary_flow');
    root.querySelector('.demo-app').scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
  });
  $('[data-demo-guide-close]').addEventListener('click', () => { guided = false; $('[data-demo-mode="free"]').click(); });
  $('[data-demo-auto-load]').addEventListener('click', openUpload); $('[data-demo-assets-button]').addEventListener('click', () => activeStory === 'asset' && openUpload());
  $('[data-demo-use-sample]').addEventListener('click', useSample); $('[data-demo-upload-cancel]').addEventListener('click', () => { uploadModal.hidden = true; syncPointer(); });
  fileInput.addEventListener('change', () => { uploadButton.disabled = !(fileInput.files && fileInput.files[0]); feedback.textContent = ''; }); uploadButton.addEventListener('click', uploadSelected);
  $('[data-demo-lock]').addEventListener('click', () => { if (!activeStory || stepIndex < stories[activeStory].steps.length) return showToast('Najpre završite sve dokumente u ovom primeru.'); lockModal.hidden = false; syncPointer(); });
  $('[data-demo-lock-cancel]').addEventListener('click', () => { lockModal.hidden = true; syncPointer(); });
  $('[data-demo-lock-confirm]').addEventListener('click', () => { lockModal.hidden = true; $('[data-demo-lock]').hidden = true; $('[data-demo-locked-badge]').hidden = false; completedStories.add(activeStory); $('[data-demo-step-count]').textContent = 'Primer je završen'; $('[data-demo-step-title]').textContent = 'Nalog je spreman'; $('[data-demo-step-help]').textContent = 'Videli ste ceo tok od dokumenta do proverenog naloga.'; const conversion = document.querySelector('[data-demo-conversion]'); if (conversion) { conversion.hidden = false; conversion.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'nearest' }); } syncPointer(); showToast('Nalog je proknjižen. Primer je završen.'); track('interactive_demo_complete', activeStory); });
  $('[data-demo-asset-back]').addEventListener('click', () => { if (assetReview) { assetReview = false; renderAssetWizard(); } else { assetModal.hidden = true; syncPointer(); } });
  $('[data-demo-asset-next]').addEventListener('click', () => { if (!assetReview) { assetReview = true; renderAssetWizard(); } else { assetModal.hidden = true; applyStep(); } });
  [uploadModal, lockModal, assetModal].forEach((modal) => modal.addEventListener('click', (event) => { if (event.target === modal) { modal.hidden = true; syncPointer(); } }));
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape') { [uploadModal, lockModal, assetModal].forEach((modal) => { modal.hidden = true; }); syncPointer(); } });
  renderStories(); showDashboard();
})();
