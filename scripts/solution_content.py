"""Concise product benefits and real visuals. Sources: docs/content-review.md."""

DETAILS = {'program-za-racunovodstvo-skola': {'how': 'Izaberite dokument i pokrenite knjiženje — program preuzima '
                                           'podatke i priprema stavke u nalogu. Jednom evidentirane podatke '
                                           'koristite kroz glavnu knjigu, kartice, preglede i izveštaje, bez '
                                           'ponovnog prepisivanja.',
                                    'media': [{'file': 'demo-nalog.png',
                                               'alt': 'Nalog sa stavkama, ukupnim dugovnim i potražnim '
                                                      'prometom i saldom',
                                               'width': 1760,
                                               'height': 557,
                                               'caption': 'Nalog sa stavkama u Budžet+ programu. Demonstracioni podaci. Izgled zavisi od verzije.'}]},
 'knjizenje-e-faktura-za-skole': {'how': 'Preuzmite e-fakture iz SEF-a direktno u Budžet+, označite fakture '
                                         'i izaberite nalog. Program preuzima podatke, povezuje ili kreira '
                                         'partnera i automatski knjiži odabrane fakture; vi pregledate '
                                         'rezultat.',
                                  'media': [{'file': 'uputstvo-e-fakture.png',
                                             'alt': 'Pregled e-faktura sa odabranim nalogom, statusom Nije knjiženo i dugmetom Proknjiži',
                                             'width': 2040,
                                             'height': 1502,
                                             'caption': 'Pregled e-faktura i knjiženje iz programa. Demonstracioni podaci. Izgled zavisi od verzije.'}],
                                  'workflow_link': {'slug': 'osnovna-sredstva-skola',
                                                    'label': 'Od e-fakture do knjiženja i evidencije '
                                                             'osnovnih sredstava',
                                                    'text': 'Za nabavku osnovnih sredstava možete zajedno '
                                                            'sačuvati knjiženje i evidenciju sredstava.'},
                                  'advance': {'title': 'Konačna faktura i zatvaranje avansa',
                                              'text': 'Program obuhvata i zatvaranje avansa. Kategoriju '
                                                      'birate samo kada program zatraži izbor, uz dostupan '
                                                      'pregled salda avansa na datum naloga.',
                                              'slug': 'spiri-izvodi-skole',
                                              'label': 'Kako se knjiži isplata avansa iz izvoda'}},
 'spiri-izvodi-skole': {'how': 'Dodajte SPIRI izvod u JSON formatu u izabrani nalog i pokrenite knjiženje. '
                               'Budžet+ automatski knjiži stavke prema podacima izvoda i pravilima '
                               'knjiženja, a vi pregledate rezultat.',
                        'advance': {'title': 'Automatsko knjiženje isplata avansa',
                                    'text': 'Isplate avansa knjiže se iz izvoda. Kategoriju birate samo kada '
                                            'program zatraži izbor, bez unosa brojeva konta i iznosa '
                                            'raspodele.',
                                    'slug': 'knjizenje-e-faktura-za-skole',
                                    'label': 'Konačna faktura i zatvaranje avansa'}},
 'iskra-obracuni-knjizenje': {'how': 'U izabranom nalogu učitajte podržani Excel obračun plata ili bolovanja '
                                     'iz ISKRA sistema i pokrenite knjiženje. Program proverava dokument i '
                                     'automatski knjiži stavke, bez prepisivanja obračuna; vi pregledate '
                                     'rezultat.',
                              'video': {'file': 'knjizenje-plate.mp4',
                                        'poster': 'nalog-za-knjizenje.jpg',
                                        'caption': 'Pregled obračuna plate u nalogu. Video prikazuje stariju '
                                                   'verziju programa.'}},
 'spiri-kumulativno-placanje': {'how': 'U pregledu e-faktura označite obaveze i izaberite „Pripremi za '
                                       'SPIRI“. Program preuzima podatke sa faktura i priprema jedan XML '
                                       'dokument, koji nakon pregleda učitavate u SPIRI za dalju obradu '
                                       'plaćanja.'},
 'rucni-unos-spiri-placanja': {'how': 'Otvorite sačuvani šablon i ažurirajte podatke za aktuelnu isplatu. '
                                      'Budžet+ priprema dokument koji učitavate u SPIRI za dalju obradu '
                                      'plaćanja. Podatke za novo plaćanje možete sačuvati kao šablon za '
                                      'sledeći put.'},
 'oris-izvoz-za-skole': {'how': 'Izaberite mesec i godinu, a Budžet+ priprema dokument sa mesečnim promenama '
                                'iz postojećih knjiženja. Preuzeti dokument učitajte na ORIS portal i '
                                'pregledajte rezultat.'},
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
                                        'caption': 'Plan i realizacija budžeta u Budžet+ programu. Demonstracioni podaci. Izgled zavisi od verzije.'}]},
 'osnovna-sredstva-skola': {'how': 'Učitajte jednu XML e-fakturu, rasporedite stavke, proverite vrstu '
                                   'sredstva i unesite stopu amortizacije. Pregledajte pripremljeni nalog i '
                                   'potvrdite — knjiženje i evidencija osnovnih sredstava čuvaju se '
                                   'zajedno.',
                            'media': [{'file': 'uputstvo-osnovna-sredstva.png',
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
