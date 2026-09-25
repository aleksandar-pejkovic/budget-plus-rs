"""Concise product benefits and real visuals. Sources: docs/content-review.md."""

DETAILS = {'knjizenje-e-faktura-za-skole': {'how': 'Preuzmite e-fakture iz SEF-a direktno u Budžet+, označite do 30 faktura i izaberite nalog. Jednim klikom pokrenite knjiženje: program preuzima podatke, povezuje ili kreira partnere i automatski knjiži odabrane fakture. Vi pregledate rezultat — ako je knjiženje ispravno, nema dodatnog unosa ni potvrđivanja.',
                                  'workflow_image': {'file': 'uputstvo-e-fakture.png',
                                             'alt': 'Pregled e-faktura sa odabranim nalogom, statusom Nije knjiženo i dugmetom Proknjiži',
                                             'width': 2040,
                                             'height': 1502,
                                             'caption': 'Pregled e-faktura i knjiženje iz programa. Demonstracioni podaci. Izgled zavisi od verzije.'},
                                  'workflow_link': {'slug': 'osnovna-sredstva-skola',
                                                    'label': 'Od e-fakture do knjiženja i evidencije '
                                                             'osnovnih sredstava',
                                                    'text': 'Za nabavku osnovnih sredstava možete zajedno '
                                                            'sačuvati knjiženje i evidenciju sredstava.'},
                                  'advance': {'title': 'Konačna faktura i zatvaranje avansa',
                                              'image': {'file': 'demo-avans-zatvaranje.png',
                                                        'alt': 'Konačna faktura od 20.000 dinara, avans i saldo od 12.000 dinara i ostatak za plaćanje od 8.000 dinara',
                                                        'width': 1024, 'height': 952,
                                                        'caption': 'Izbor kategorije i pregled salda pri zatvaranju avansa konačnom fakturom. Demonstracioni podaci, Budžet+ 1.11.1. Izgled zavisi od verzije.'},
                                              'text': 'Program obuhvata i zatvaranje avansa. Kategoriju '
                                                      'birate samo kada program zatraži izbor, uz dostupan '
                                                      'pregled salda avansa na datum naloga.',
                                              'slug': 'spiri-izvodi-skole',
                                              'label': 'Kako se knjiži isplata avansa iz izvoda'}},
 'spiri-izvodi-skole': {'how': 'Dodajte SPIRI izvod u JSON formatu u izabrani nalog i pokrenite knjiženje. Budžet+ automatski knjiži stavke prema podacima izvoda i pravilima knjiženja, a vi pregledate rezultat. Ako je knjiženje ispravno, nema dodatnog unosa ni potvrđivanja.',
                        'workflow_image': {'file': 'demo-spiri-izvod.png',
                                           'alt': 'Nalog iz SPIRI izvoda: plaćanje dobavljaču za kancelarijski materijal, zatvaranje obaveze i evidentiranje rashoda',
                                           'width': 4032, 'height': 1296,
                                           'caption': 'Knjiženje redovnog plaćanja dobavljaču iz SPIRI izvoda. Demonstracioni podaci. Izgled zavisi od verzije.'},
                        'advance': {'title': 'Automatsko knjiženje isplata avansa',
                                    'image': {'file': 'demo-avans-isplata.png',
                                              'alt': 'Isplata avansa od 12.000 dinara iz SPIRI izvoda sa izabranom kategorijom Avansi za materijal',
                                              'width': 1024, 'height': 744,
                                              'caption': 'Izbor kategorije pri knjiženju isplate avansa iz SPIRI izvoda. Demonstracioni podaci, Budžet+ 1.11.1. Izgled zavisi od verzije.'},
                                    'text': 'Isplate avansa knjiže se iz izvoda. Kategoriju birate samo kada '
                                            'program zatraži izbor, bez unosa brojeva konta i iznosa '
                                            'raspodele.',
                                    'slug': 'knjizenje-e-faktura-za-skole',
                                    'label': 'Konačna faktura i zatvaranje avansa'}},
 'iskra-obracuni-knjizenje': {'how': 'U izabranom nalogu učitajte podržani Excel obračun iz ISKRA sistema i pokrenite knjiženje. Za plate i bolovanja program iz jednog fajla automatski knjiži i stavke obračuna i pripadajuće stavke izvoda. Za ostale podržane obračune knjiži stavke obračuna, a zatvaranje se obavlja knjiženjem izvoda. Vi pregledate rezultat; ispravno knjiženje ne zahteva dodatni unos ni potvrđivanje.',
                              'video': {'file': 'knjizenje-plate.mp4',
                                        'poster': 'nalog-za-knjizenje.jpg',
                                        'caption': 'Pregled obračuna plate u nalogu. Video prikazuje stariju '
                                                   'verziju programa.'}},
 'spiri-kumulativno-placanje': {'how': 'U pregledu e-faktura označite obaveze i izaberite „Pripremi za '
                                       'SPIRI“. Program preuzima podatke sa faktura i priprema jedan XML '
                                       'dokument, koji nakon pregleda učitavate u SPIRI za dalju obradu '
                                       'plaćanja.',
                             'media': [{'file': 'demo-spiri-priprema.png', 'alt': 'Tri označene e-fakture ukupne vrednosti 104.000 dinara i opcija Pripremi za SPIRI', 'width': 2880, 'height': 2200, 'caption': 'Izbor više e-faktura za pripremu SPIRI plaćanja. Demonstracioni podaci. Izgled zavisi od verzije.'}]},
 'rucni-unos-spiri-placanja': {'how': 'Otvorite sačuvani šablon i ažurirajte podatke za aktuelnu isplatu. '
                                      'Budžet+ priprema dokument koji učitavate u SPIRI za dalju obradu '
                                      'plaćanja. Podatke za novo plaćanje možete sačuvati kao šablon za '
                                      'sledeći put.',
                             'media': [{'file': 'demo-spiri-sablon.png', 'alt': 'Plaćanje održavanja opreme od 12.000 dinara popunjeno iz sačuvanog šablona', 'width': 2368, 'height': 1062, 'caption': 'Sačuvani šablon popunjava podatke redovne obaveze; pre pripreme plaćanja proverite iznos, datume i poziv na broj. Demonstracioni podaci. Izgled zavisi od verzije.'}]},
 'oris-izvoz-za-skole': {'how': 'Izaberite mesec i godinu, a Budžet+ priprema dokument sa mesečnim promenama '
                                'iz postojećih knjiženja. Preuzeti dokument učitajte na ORIS portal i '
                                'pregledajte rezultat.',
                             'media': [{'file': 'demo-oris-priprema.png', 'alt': 'Izbor septembra 2026. i dugme za preuzimanje dokumenta za ORIS', 'width': 944, 'height': 750, 'caption': 'Izbor meseca i godine za pripremu ORIS dokumenta. Demonstracioni podaci. Izgled zavisi od verzije.', 'compact': True}]},
 'obrazac-5-ispfi': {'how': 'Izaberite period i podatke izveštaja, a program priprema Obrazac 5 iz '
                            'postojećih knjiženja. Preuzmite JSON dokument i učitajte ga u ISPFI, gde '
                            'pregledate rezultat.',
                       'media': [{'file': 'uputstvo-obrazac-5.png',
                                  'alt': 'Izbor perioda i podataka izveštaja sa dugmetom Preuzmi Obrazac 5',
                                  'width': 672,
                                  'height': 599,
                                  'caption': 'Priprema Obrasca 5 za ISPFI. Demonstracioni podaci. Izgled zavisi od verzije.'}]},
 'izvrsenje-budzeta-skola': {'how': 'Učitajte Excel plan preuzet iz IFISUP-a i izaberite period za pregled. '
                                    'Budžet+ prikazuje plan i realizaciju iz evidentiranih podataka, uz '
                                    'odstupanja i grafikone koji olakšavaju praćenje budžeta.',
                             'media': [{'file': 'demo-grafikoni.png',
                                        'alt': 'Grafikoni plana, troškova i prihoda po ekonomskoj '
                                               'klasifikaciji',
                                        'width': 1280,
                                        'height': 1033,
                                        'caption': 'Plan i realizacija budžeta u Budžet+ programu. Demonstracioni podaci. Izgled zavisi od verzije.'}, {'file': 'demo-izvrsenje-tabela.png', 'alt': 'Izveštaj izvršenja budžeta sa planom od 6 miliona dinara, realizacijom od 4,2 miliona i procentom izvršenja od 70 odsto', 'width': 1556, 'height': 850, 'caption': 'Primer izveštaja: plan, realizacija i procenat izvršenja po ekonomskoj klasifikaciji. Demonstracioni podaci. Izgled zavisi od verzije.'}]},
 'osnovna-sredstva-skola': {'how': 'Učitajte jednu XML e-fakturu, rasporedite stavke, proverite vrstu '
                                   'sredstva i unesite stopu amortizacije. Pregledajte pripremljeni nalog i '
                                   'potvrdite — knjiženje i evidencija osnovnih sredstava čuvaju se '
                                   'zajedno.',
                            'media': [{'file': 'demo-sredstva-raspored.png', 'alt': 'Raspored stavke Računar za nastavu i izbor vrste sredstva i stope amortizacije', 'width': 1024, 'height': 1820, 'caption': 'Korak 1: raspored stavki e-fakture i provera podataka osnovnog sredstva. Demonstracioni podaci. Izgled zavisi od verzije.', 'compact': True},
                                       {'file': 'demo-sredstva-nalog.png', 'alt': 'Pregled sredstva vrednog 72.000 dinara i pripremljenih stavki naloga pre potvrde', 'width': 1024, 'height': 1512, 'caption': 'Korak 2: pregled naloga pre zajedničkog čuvanja knjiženja i evidencije osnovnih sredstava. Demonstracioni podaci. Izgled zavisi od verzije.', 'compact': True},
                                       {'file': 'uputstvo-osnovna-sredstva.png',
                                       'alt': 'Evidencija osnovnih sredstava sa inventarskim brojem, lokacijom, nabavnom i trenutnom vrednošću',
                                       'width': 1728,
                                       'height': 618,
                                       'caption': 'Pregled evidencije osnovnih sredstava. Demonstracioni podaci. Izgled zavisi od verzije.'}]},
 'uplate-ucenika': {'how': 'Povežite učenike sa aktivnošću i zaduženjima, pa učitajte uplate iz popunjenog '
                           'Excel šablona. Program daje pregled zaduženja, uplata i preostalog iznosa po '
                           'učeniku, odeljenju ili aktivnosti.'},
 'zatvaranje-poslovne-godine': {'how': 'Pokrenite obračun amortizacije, zatvaranje rashoda i prihoda i '
                                       'prenos salda u narednu godinu. Program priprema završne naloge i '
                                       'prenos, a vi pregledate rezultat, status naloga i početna stanja.',
                                'media': [{'file': 'demo-zatvaranje-godine.png',
                                           'alt': 'Opciona priprema amortizacije i dva koraka: zatvaranje rashoda i prihoda i otvaranje naredne godine',
                                           'width': 768,
                                           'height': 803,
                                           'caption': 'Priprema amortizacije, zatvaranje rashoda i prihoda i otvaranje naredne godine. Demonstracioni podaci. Izgled zavisi od verzije.'}]}}
