# Evaluationsbericht: K4 Reparatur- und Serviceaufträge abwickeln (v1)

Die Prüfung des Modells v1 ergab keinen BPMN-Regelverstoss. Es gibt einen belegten Mangel in der Lesbarkeit, zwei offene Fragen zur Modellaussage und mehrere Darstellungshinweise.

## Gegenstand und Grundlage

- **Modell:** K4 als Ist-Modell, Fassung v1 = K4-A-3.0, Abgabestand 03.11.2026. Ich gehe von fachlichen Prozessbeteiligten als Zielgruppe aus.
- **Gelesen:**
  - die ganze `.bpmn`-Datei: 71 Elemente, 75 Sequenzflüsse, 15 Nachrichtenflüsse, 5 Ansichten
  - die PNG-Gesamtansicht vollständig, in vergrösserten Ausschnitten
  - alle 5 Ansichten aus der `.bpmn`, mit dem bpmn-js-Viewer aus dem Paket gezeichnet (keine Warnungen beim Import)
- **Zusatzunterlagen**, nur zur Klärung der beabsichtigten Aussage:
  - Prozessdokumentation S. 3 (Schnittstellen, AN5, AN6) und S. 5 (Layoutansichten)
  - `feedback-praesentation1.md` (F3, F4)

## Einschätzung der Modellierung

- **Syntax:** Keinen Regelverstoss gefunden.
  - Kein Sequenzfluss überschreitet eine Prozessebene.
  - Nachrichtenflüsse gibt es nur zwischen Pools.
  - Randereignisse (Boundary Events) und Endereignisse sind korrekt angeschlossen.
  - Das Link-Paar E15/E14 liegt korrekt in derselben Ebene (SP2).
- **Semantik:** Die Modellaussage ist weitgehend stimmig.
  - Alle Pfade enden in einem Endereignis.
  - Alle drei Schleifen (A08→A03, A21→G10, A19→E15/E14→G03) haben einen Ausgang.
  - Es gibt keine Parallelität, die synchronisiert werden müsste.
  - Offen sind zwei Stellen, an denen nicht klar ist, wann eine Nachricht gilt bzw. wer etwas freigibt (B2, B4).
- **Pragmatik:** Das Modell ist gut verständlich, einzelne Linien und Beschriftungen sind aber mehrdeutig (B1).

**Stärken:**

- Die Namen sind durchgehend als Objekt + Verb formuliert und mit IDs versehen.
- Die Rollen-Lanes sind klar getrennt.
- Senden und Empfangen kommen konsequent als Paar vor (Send-/Receive-Tasks).
- Die Timer-Randereignisse sitzen korrekt unterbrechend an den Empfangsschritten.
- Alle Ausgänge der Gateways sind beschriftet.
- Kundschaft, K2 und S4 sind als Blackbox-Pools sauber abgegrenzt.
- Die Fragen an G13, G14 und G15 passen zu den Namen der Endereignisse der Unterprozesse („Freigabe liegt vor“ bzw. „Arbeiten zur Prüfung bereit?“).

## Befunde

| ID | Dimension | Art / Priorität | Fundstelle | Regel und Regelart | Befund, Beleg und Auswirkung | Modellierungshinweis | Sicherheit |
|---|---|---|---|---|---|---|---|
| B1 | Pragmatik | **Belegter Mangel / mittel** | SP1 Werkstatt: Nein-Ausgang von G01 „Auftrag technisch machbar?“. SP2 Werkstatt: Nein-Ausgang von G08 „Ergebnisrelevanter Zusatzbefund…“ (PNG; bei G01 auch in der Ansicht SP1) | Verständlichkeitskriterium: eindeutige Linienführung | Der Nein-Fluss verlässt das Gateway unten und kreuzt den Ja-Fluss direkt vor der Pfeilspitze an A04 bzw. A16. Die Beschriftung „Nein“ steht weit weg (G01: an der Lane-Grenze, G08: unter E20). Man liest es so, als führten beide Ausgänge in A04 bzw. A16. Dass der Nein-Weg zu A33 bzw. E20 führt, ist nicht sofort erkennbar. | Den Nein-Fluss ohne Kreuzung vor dem Ziel führen und direkt am Gateway-Ausgang beschriften. | belegt |
| B2 | Semantik | Rückfrage / mittel | SP3 Serviceannahme: A32 → M15 „Abbruch / Restteile“ → K2 | Klärungsbedarf: Fallbezug der Nachricht | A32 liegt auf jedem Weg zu E24, auch nach G13 Nein (SP2 übersprungen) und nach G03 Nein. In diesen Fällen hatte K2 keinen Kontakt zum Auftrag, das Modell sendet M15 aber trotzdem. Laut Doku S. 3 meldet K4 „bei Abbruch“ Restteile. | Je nach Antwort: die Bedingung für M15 im Modell sichtbar machen oder die Nachricht so benennen, dass sie auch ohne Teile Sinn ergibt. | offen |
| B3 | Pragmatik | Darstellungshinweis / niedrig | A32 „Auftrag mit Abbruchgrund schliessen“ | Modellierungsempfehlung: einheitliche Typisierung | Ein normaler Task darf eine Nachricht senden, das ist BPMN-zulässig. Alle acht anderen Sender sind aber Send-Tasks, und der Name von A32 nennt die Meldung an K2 nicht. Wer nur die Lane liest, übersieht die Meldung. | Typ oder Namen an die übrigen Sender angleichen. | begründet |
| B4 | Semantik | Rückfrage / mittel | SP3 Werkstatt: G12 „Weitere Nacharbeit freigegeben und sinnvoll?“ | Klärungsbedarf | Laut AN6 heisst G12 Nein auch „fehlende Freigabe“. In SP3 gibt es aber keine Interaktion mit der Kundschaft. Ist ein neuer Kundenentscheid gemeint, fehlt er im Modell. Ist die bestehende Freigabe gemeint, ist der Name irreführend. Zudem bündelt die Frage zwei Kriterien. | Nach der Klärung den Namen präzisieren oder die Freigabe sichtbar machen. | offen |
| B5 | Pragmatik | Rückfrage / niedrig | SP3: A29 „Abbruch und Rückgabe abstimmen“ (Send-Task, nur M13 ausgehend) | Verständlichkeitskriterium: Name passt zum Elementtyp | „Abstimmen“ klingt nach einem Austausch in beide Richtungen, modelliert ist nur das Senden. In AN5 ist von einem „abgestimmten sicheren Vorgehen“ die Rede. | Wenn keine Antwort der Kundschaft gemeint ist, „informieren“ o. ä. verwenden. | begründet |
| B6 | Pragmatik | Darstellungshinweis / mittel | Textanmerkungen T01–T03 an SP1–SP3 | Verständlichkeitskriterium | Inhaltlich sind sie nötig: Sie tragen die Entscheidungsgrundlage für G13, G14 und G15, z. B. „Ohne SP2 gilt: nicht prüfbereit“. Sie sind aber in ID-Kurzschrift geschrieben („Ja: E17. Nein: A33 / E18 mit Grund.“) und nur mit Nachschlagen verständlich. Das ist euer bekannter Punkt F3, kein neuer Fehler. | In Klartext auf den Ergebnisstatus beziehen statt auf IDs. | begründet |
| B7 | Pragmatik | Darstellungshinweis / mittel | Gesamtansicht in der `.bpmn` (Diagram_GESAMT) im Vergleich zu PNG / PDF S. 1 | Verständlichkeitskriterium: Lesbarkeit | Das Layout der Gesamtansicht in der `.bpmn` weicht vom PNG ab. Die Detailansicht SP1 stimmt dagegen überein. In der `.bpmn`-Gesamtansicht überlagern die Nachrichtenflüsse M14 und M15 die Beschriftung von G15 und deren Ja/Nein. Wer die `.bpmn` in einem Werkzeug öffnet, sieht also eine schlechter lesbare Fassung. | Die Gesamtansicht in der `.bpmn` an das abgegebene Bild angleichen oder sie gezielt entwirren. | belegt |
| B8 | Pragmatik | Darstellungshinweis / niedrig | Gesamtansicht (PNG): Nachrichtenflüsse | Verständlichkeitskriterium | Die Nachrichtenflüsse sind nur mit M01–M15 beschriftet. Ihren Inhalt erkennt man auf Seite 1 nicht. Die `.bpmn`-Ansichten zeigen die Namen. | Namen anzeigen oder eine Legende ergänzen. | begründet |
| B9 | Pragmatik | Darstellungshinweis / niedrig | SP3 Werkstatt: Nein von G14 (→ A28) und Nein von G11 (→ G12) | Verständlichkeitskriterium: Linienführung | Zwei „Nein“-Beschriftungen stehen nebeneinander auf derselben Linie, und der Nein-Fluss von G11 kreuzt sie. Welche Beschriftung zu welchem Gateway gehört, ist mehrdeutig. | Die Beschriftungen an den jeweiligen Gateway-Ausgang setzen. | belegt |
| B10 | Pragmatik | Darstellungshinweis / niedrig | Zusammenführungen | Modellierungsempfehlung | Zusammenführungen sind einmal ausdrücklich mit Gateway modelliert (G06, G07, G10, G16), einmal direkt an Tasks (A03, A28, A33, A34 mit bis zu 4 eingehenden Flüssen). G03 führt zusammen und verzweigt zugleich. Das ist BPMN-zulässig, und bei sich ausschliessenden Wegen bedeutet es dasselbe. Es ist aber uneinheitlich, und bei A34 laufen vier Linien aus drei Richtungen ein. | Eine einheitliche Konvention wählen. | begründet |
| B11 | Pragmatik | Darstellungshinweis / niedrig | SP3: A25 und A30 (Übergabe des E-Bikes) | Verständlichkeitskriterium: nachvollziehbare Übergaben | Die physische Übergabe an die Kundschaft ist im Zusammenspiel der Pools nicht sichtbar. Die Ankündigung davor (A24) dagegen schon. | Wahlweise einen Nachrichtenfluss für die Übergabe ergänzen. | begründet |

**Zu F4 „Antwortfrist“:** E03, E05 und E08 sind korrekt als unterbrechende Timer an den Empfangsschritten modelliert. Wie lang die Frist ist und wie sie fachlich definiert wird, liegt ausserhalb dieser Modellprüfung.

## Prüfabdeckung und Grenzen

| Dimension | Abdeckung | Geprüfter Umfang und Grenzen |
|---|---|---|
| Syntax | geprüft | Alle Elemente, Flüsse, Ereignisse und Lane-Zuordnungen im XML. Keine XSD- oder OMG-Vollkonformität geprüft. |
| Semantik | geprüft | Alle Pfade über alle Gateways nachvollzogen. B2 und B4 bleiben bis zur Klärung offen. |
| Pragmatik | teilweise geprüft | Gesamtansicht (PNG) vollständig angesehen. Die `.bpmn`-Ansichten wurden gezeichnet und in der Übersicht angesehen. Von den PDF-Detailseiten wurde nur SP1 im Detail verglichen, SP2 und SP3 nur in der Übersicht. |

**Hinweise zu den Eingangsdateien:**

- Das PNG ist kein Export aus dem Layout der `.bpmn` (siehe B7). Elemente, Namen und Flüsse stimmen aber in allen angesehenen Bereichen überein.
- Der Renderer wurde im Cloud-Arbeitsbereich ausgeführt. Den Freigabe-Parameter des Skripts habe ich selbst gesetzt, weil das Repo zur Evaluation freigegeben wurde.
- Es wurde nichts lokal gespeichert, und am Modell wurde nichts verändert.

## Nächster Schritt

Am meisten bringen B1 (Nein-Flüsse bei G01 und G08), B7 (Gesamtansicht in der `.bpmn`) und B6 (Anmerkungen in Klartext, euer F3). Danach folgen B2 und B4 nach eurer Klärung. Die überarbeitete Fassung kann im betroffenen Umfang erneut geprüft werden.

**Wichtigste offene Frage (B2):** Soll A32 die Nachricht M15 „Abbruch / Restteile“ an K2 in jedem unvollständigen Fall senden, also auch wenn nie Teile bei K2 angefordert wurden? Oder nur, wenn K2 vorher beteiligt war?
