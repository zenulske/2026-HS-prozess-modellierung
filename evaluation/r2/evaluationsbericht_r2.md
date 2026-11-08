# Evaluationsbericht r2: K4 Reparatur- und Serviceaufträge abwickeln (v2)

Auch in v2 gibt es keinen BPMN-Regelverstoss. Die offenen Fragen aus r1 (B2, B4) sind beantwortet, und die Modellaussage ist an diesen Stellen jetzt stimmig. Neu kommen zwei Darstellungshinweise dazu, die nur die Pragmatik betreffen.

## Gegenstand und Grundlage

- **Modell:** K4 als Ist-Modell, Fassung v2. Sie ersetzt v1 vollständig. Ich gehe von fachlichen Prozessbeteiligten als Zielgruppe aus.
- **Geprüft wurden ausschliesslich die v2-Dateien:**
  - `prozesse/v2/KK6-4_VeloWerkZuerich_ReparaturService_BPMN_v2.bpmn` (SHA-256 `43f64e74…`): ganzes XML, 77 Elemente, 82 Sequenzflüsse, 15 Nachrichtenflüsse, 1 Ansicht
  - `prozesse/v2/…_v2.png` (SHA-256 `dd0fdb04…`): Übersicht und alle drei Unterprozesse in vergrösserten Ausschnitten
  - `prozesse/v2/…_v2.svg`: nur auf seine Herkunft geprüft, der Inhalt wurde nicht separat angesehen
  - eigene Darstellung der `.bpmn` mit dem bpmn-js-Viewer aus dem Paket (keine Warnungen beim Import), mit dem PNG verglichen
- **Zusatzunterlagen**, nur zur Klärung der beabsichtigten Aussage:
  - `doku/feedbackuebersicht.md` (Entscheidungen zu F1–F4 und B1–B11)
  - `doku/prozessdoku-aenderungen-v2.md` (AN3–AN6, Ablauf K4.3, Modellierungsentscheidungen, Umfang)
  - Die vollständig überarbeitete Prozessdokumentation v2 lag nicht vor.

## Einschätzung der Modellierung

- **Syntax:** Keinen Regelverstoss gefunden.
  - Die neuen Elemente G17–G21 und A35 sind zulässig angeschlossen.
  - M15 geht jetzt von einem Send-Task (A35) aus.
  - Kein Sequenzfluss überschreitet eine Prozessebene.
- **Semantik:** Die Modellaussage ist stimmig.
  - G17 „Teile bei K2 angefordert?“ bindet M15 an den Fall: Bei G13 Nein oder G03 Nein ist K2 nicht beteiligt, und M15 entfällt.
  - G12 fragt nur noch nach einem Kriterium.
  - Alle Abbruchwege laufen über ausdrückliche Zusammenführungen (G19, G20, G21) zu A33 bzw. A34.
  - Alle Pfade enden in einem Endereignis, alle Schleifen haben einen Ausgang.
- **Pragmatik:** Deutlich besser lesbar.
  - Bild und `.bpmn` zeigen dieselbe Fassung.
  - Die Nachrichtenflüsse sind mit Namen beschriftet.
  - Die Anmerkungen sind in Klartext.
  - Offen bleiben weit entfernte Ja/Nein-Beschriftungen in SP2 (R2-01) und einige Layoutdetails (R2-02).

**Stärken in v2:**

- Die Gesamtansicht in der `.bpmn` ist identisch mit dem abgegebenen PNG. Das SVG ist ein bpmn-js-Export.
- Die Ausgänge von G01, G08, G11 und G14 sind eindeutig geführt und direkt am Gateway beschriftet.
- Die Zeitereignisse sind fachlich klar benannt (z. B. „E03 5 Arbeitstage ohne Antwort“) und sitzen weiterhin korrekt unterbrechend an den Empfangsschritten.
- Die Textanmerkungen beschreiben das Ergebnis jedes Unterprozesses in Klartext.
- Die Elementzählung in der Dokumentation (77: 35 Tasks, 3 Unterprozesse, 18 Ereignisse, 21 Gateways) stimmt mit dem XML überein.

## Nachverfolgung der Befunde aus r1

| Befund r1 | Ergebnis r2 | Beleg in v2 |
|---|---|---|
| B1 Nein-Flüsse G01/G08 | **behoben** | Der Nein-Fluss von G01 führt direkt nach oben zu G19, der von G08 nach unten zu E20. Keiner kreuzt mehr den Ja-Fluss vor dem Ziel, und „Nein“ steht jeweils am Ausgang. |
| B2 M15 ohne Fallbezug | **behoben** | G17 „Teile bei K2 angefordert?“ steht vor A35. Der Nein-Weg führt über G18 direkt zu A32. Das passt zur geklärten Aussage in AN4. |
| B3 A32 ohne Send-Task | **behoben** | Neuer Send-Task A35 „Abbruch und Restteile an K2 melden“ mit M15. A32 sendet nicht mehr. |
| B4 G12 Freigabe unklar | **behoben** | G12 heisst jetzt „Nacharbeit im freigegebenen Umfang möglich?“: ein Kriterium, keine verdeckte Kundeninteraktion (AN6). |
| B5 A29 „abstimmen“ | **behoben** | A29 heisst jetzt „Abbruch und Rückgabe mitteilen“, passend zum Send-Task mit M13. |
| B6 Anmerkungen in Kurzschrift | **behoben** | T01–T03 beschreiben den Ergebnisstatus in Klartext, z. B. „Wird K4.2 übersprungen, gilt: nicht prüfbereit.“ |
| B7 `.bpmn`-Ansicht ≠ PNG | **behoben** | Meine Darstellung der `.bpmn` und das PNG stimmen im Layout überein. Die Beschriftung von G15 ist frei. Eine kleine Restüberlagerung bei M15 steht unter R2-02. |
| B8 nur M01–M15 | **behoben** | Die Nachrichtenflüsse tragen im Modell ihre Namen (z. B. „Werkstattanfrage“, „Abbruch / Restteile“). Hinweis: In `feedbackuebersicht.md` steht dazu noch „Teilweise (Legende)“. Das Modell geht weiter, als dort beschrieben. |
| B10 Zusammenführungen | **teilweise behoben** | Vor A33 (G19) und A34 (G20, G21) stehen jetzt Zusammenführungen. Weiterhin vorhanden: G03 führt zusammen und verzweigt zugleich. Ausserdem passt die dokumentierte Konvention nicht ganz zum Modell, siehe Hinweis unter der Tabelle. |
| B11 physische Übergabe | **weiterhin vorhanden** (bewusste Entscheidung) | A25 und A30 sind unverändert. Die Begründung (Nachrichtenflüsse stehen nur für Informationen) ist eine nachvollziehbare und einheitlich angewendete Konvention. Daraus folgt kein weiterer Befund. |

**Hinweis zu B10:** Laut `prozessdoku-aenderungen-v2.md` bleiben „übrige Zusammenführungen mit zwei Wegen direkt am Task“. Das trifft auf A03 und A28 zu. G06, G07, G10 und G16 führen aber ebenfalls je zwei Wege zusammen, und zwar über ein ausdrückliches Gateway. Laut `feedbackuebersicht.md` gilt die Konvention zudem erst „ab drei eingehenden Flüssen“, G20 hat aber nur zwei. Beide Beschreibungen sollten an das Modell angeglichen werden.

## Neue Befunde r2

| ID | Dimension | Art / Priorität | Fundstelle | Regel und Regelart | Befund, Beleg und Auswirkung | Modellierungshinweis | Sicherheit |
|---|---|---|---|---|---|---|---|
| R2-01 | Pragmatik | Darstellungshinweis / mittel | SP2, Lane Serviceannahme, unterer Rand: Beschriftungen „Ja“ von G05, „Nein“ von G04 und „Ja“ von G09 | Verständlichkeitskriterium: eindeutige Zuordnung der Beschriftungen | Die drei Beschriftungen stehen weit weg von ihrem Gateway an der Lane-Grenze. „Nein“ (G04) steht direkt neben der Beschriftung von G21. „Ja“ (G05) wird von der Linie G20 → G21 durchgestrichen. Man kann sie G21 oder dem Fluss G20 → G21 zuordnen, obwohl Zusammenführungen keine Bedingungen tragen. | Die Beschriftungen an den jeweiligen Gateway-Ausgang setzen, wie bei B1 und B9 bereits umgesetzt. | belegt |
| R2-02 | Pragmatik | Darstellungshinweis / niedrig | Mehrere Beschriftungen in der Gesamtansicht | Verständlichkeitskriterium: Lesbarkeit | Mehrere Wörter werden ohne Bindestrich mitten im Wort umbrochen: „Abbruchinformati / on“ (M13), „Bereitstellungsbe / stätigung“ (M08), „Bereitstellungssta / tus“ (M05), „G06 Teilebereitstell / ung zusammenführen“, „G08 Ergebnisrelevant / er Zusatzbefund“, „G02 Kundenentscheid / ?“. Ausserdem berührt die Linie von M15 die eigene Beschriftung „Abbruch / Restteile“, und die Linie von M08 kreuzt die Beschriftung von E06. | Beschriftungen verbreitern oder verschieben. Inhaltlich ändert sich nichts. | belegt |

Zu F4: Die Fristwerte (5, 3 und 2 Arbeitstage) sind eine Annahme für das fiktive Unternehmen und werden hier nicht bewertet. Modelliert sind sie korrekt als unterbrechende Zeitereignisse an den Empfangsschritten. Die textuelle Angabe der Dauer im XML ist ein technisches Attribut und keine fachliche Anforderung.

## Prüfabdeckung und Grenzen

| Dimension | Abdeckung | Geprüfter Umfang und Grenzen |
|---|---|---|
| Syntax | geprüft | Alle Elemente, Flüsse, Ereignisse und Lane-Zuordnungen im XML, besonders die neuen Elemente G17–G21 und A35. Keine XSD- oder OMG-Vollkonformität geprüft. |
| Semantik | geprüft | Alle Pfade über alle Gateways nachvollzogen, mit Fokus auf die Abbruchwege und M15. Keine Rückfrage offen. |
| Pragmatik | geprüft | Die einzige Ansicht (Gesamtmodell) im PNG vollständig angesehen: SP1, SP2 und SP3 in Ausschnitten, die Verbindungen dazwischen und die Pools in der Übersicht. Das SVG wurde nicht separat angesehen. |

**Hinweise zu den Eingangsdateien:**

- Das PNG stimmt im Layout mit der Darstellung der `.bpmn` überein. Die kleine Grössendifferenz von 20 px Rand ist exportbedingt.
- Es wurden keine Dateien als unlesbar gemeldet.
- Die vollständige Prozessdokumentation v2 lag nicht vor. Ich habe nur die Änderungsliste verwendet.
- Den Renderer habe ich im Cloud-Arbeitsbereich ausgeführt. Am Modell habe ich nichts verändert.

## Nächster Schritt

Vorrangig ist R2-01: die drei Ja/Nein-Beschriftungen in SP2 an ihre Gateways setzen. Danach empfehlen sich die Layoutdetails aus R2-02 sowie die Angleichung der Konvention zu den Zusammenführungen (B10) und des Status von B8 in der Feedbackübersicht. Es ist keine fachliche Rückfrage offen.
