# Feedbackübersicht und Entscheidungen (Aufgabe B)

> Geprüfte Fassung: v1 = K4-A-3.0, Abgabestand 03.11.2026. Zielfassung: v2.
> Quellen: Präsentationsrunde 1 (F1–F4, siehe `feedback-praesentation1.md`) und Evaluationsassistent r1 (B1–B11, siehe `evaluation/r1/`).
> Gegenstand bleibt der Ist-Prozess: Alle Änderungen sind Korrekturen bzw. Präzisierungen der Modellierung und Dokumentation, keine Änderungen am betrieblichen Ablauf.

## Übersicht

| Nr. | Feedbackquelle und Fundstelle | Rückmeldung | Fachliche Prüfung und Entscheidung | Änderung und betroffenes Artefakt |
|---|---|---|---|---|
| F1 | Präsentationsrunde 1 | Präsentation zu wenig übersichtlich | **Umgesetzt.** Berechtigt: Viele ID-Kürzel und ein ganzes Modell auf einer Folie erschwerten das Folgen. | Folien: klare Gliederung, lesbare Modellausschnitte, Klartext statt Kürzel im Vortrag |
| F2 | Präsentationsrunde 1 | Nur K4 gezeigt, Einordnung fehlte | **Umgesetzt.** Berechtigt: Ohne Prozesslandkarte waren Schnittstellen (K1, K2, S4) nicht nachvollziehbar. | Folien: Prozesslandkarte zu Beginn, K4 markiert, Schnittstellen benannt |
| F3 | Präsentationsrunde 1 | Annotationen im Modell unklar | **Umgesetzt** (siehe B6). Inhalt wird gebraucht, Formulierung war unverständlich. | Modell: Annotationen in Klartext; Doku: Modellierungsentscheidungen angepasst |
| F4 | Präsentationsrunde 1 | „Antwortfrist“ nicht definiert | **Umgesetzt.** Berechtigt: „fallbezogen vereinbart“ wirkte wie eine Lücke. Für das fiktive Unternehmen wird eine plausible Annahme festgelegt. Der Assistent beurteilt dies ausdrücklich nicht. | Doku: Definition und Werte in AN3 (A07: 5, A12: 3, A18: 2 Arbeitstage – **in Gruppe bestätigen**); Modell: Timer E03/E05/E08 mit Wert beschriften |
| B1 | Assistent r1, SP1 G01 / SP2 G08 | Nein-Flüsse kreuzen Ja-Fluss vor A04/A16, Beschriftung weit weg | **Umgesetzt.** Im PNG nachvollzogen, Befund belegt. | Modell: Nein-Flüsse ohne Kreuzung führen, Beschriftung am Gateway-Ausgang |
| B2 | Assistent r1, SP3 A32 → M15 | M15 auch gesendet, wenn K2 nie beteiligt war | **Umgesetzt.** Restteilemeldung ist nur sinnvoll, wenn K2 Teile bereitgestellt oder reserviert hat. | Modell: XOR „Teile bei K2 angefordert?“ vor der Meldung; Doku: Schnittstelle K2 und AN4 präzisieren |
| B3 | Assistent r1, SP3 A32 | A32 einziger Sender ohne Send-Task | **Umgesetzt** (mit B2). | Modell: neuer Send-Task „Abbruch und Restteile an K2 melden“, A32 sendet nicht mehr selbst |
| B4 | Assistent r1, SP3 G12 | Unklar, welche Freigabe gemeint ist; zwei Kriterien | **Umgesetzt durch Präzisierung.** Nacharbeit dient dem bereits vereinbarten Ergebnis; darüber hinaus führt der Weg zur Reparaturgrenze. Keine neue Kundeninteraktion. | Modell: G12 „Nacharbeit im freigegebenen Umfang möglich?“; Doku: AN6 anpassen |
| B5 | Assistent r1, SP3 A29 | „Abstimmen“ passt nicht zu reinem Senden | **Umgesetzt.** | Modell: A29 „Abbruch und Rückgabe mitteilen“; Doku: AN5 Formulierung anpassen |
| B6 | Assistent r1, T01–T03 | Annotationen in ID-Kurzschrift | **Umgesetzt** (= F3). Assistent bestätigt: inhaltlich nötig. | Modell: Annotationen als Klartext zum Ergebnisstatus |
| B7 | Assistent r1, Gesamtansicht .bpmn | Layout der .bpmn weicht vom PNG ab, M14/M15 überlagern G15 | **Umgesetzt.** Wichtig für die Abgabe: Bild und .bpmn müssen dieselbe Fassung zeigen. | Modell: Gesamtansicht entwirren; PNG/PDF direkt aus dem Werkzeug exportieren |
| B8 | Assistent r1, Gesamtansicht | Nachrichtenflüsse nur M01–M15 | **Teilweise umgesetzt.** Namen im Gesamtbild würden es überladen. | Folien/PDF: Legende M01–M15 |
| B9 | Assistent r1, SP3 G14/G11 | Zwei „Nein“-Beschriftungen mehrdeutig | **Umgesetzt.** Belegt. | Modell: Beschriftungen an den jeweiligen Gateway-Ausgang |
| B10 | Assistent r1, Zusammenführungen | Uneinheitlich, A34 mit 4 Eingängen | **Teilweise umgesetzt.** Konvention: Zusammenführungsgateway ab drei eingehenden Flüssen. | Modell: Merge-Gateways vor A33 und A34 |
| B11 | Assistent r1, SP3 A25/A30 | Physische Übergabe nicht als Nachrichtenfluss sichtbar | **Nicht umgesetzt.** Nachrichtenflüsse stehen im Modell konsequent für Informationen; die physische Übergabe ist im Tasknamen ausgedrückt. | keine Änderung, Begründung in Doku |

## Änderungsliste für v2

### BPMN-Modell

- [ ] B1: Nein-Fluss G01 → A33 und G08 → E20 ohne Kreuzung, Beschriftung am Gateway
- [ ] B2/B3: XOR „Teile bei K2 angefordert?“ + Send-Task „Abbruch und Restteile an K2 melden“ (M15), A32 als normaler Task ohne Nachricht
- [ ] B4: G12 umbenennen in „Nacharbeit im freigegebenen Umfang möglich?“
- [ ] B5: A29 umbenennen in „Abbruch und Rückgabe mitteilen“
- [ ] B6/F3: Annotationen T01–T03 in Klartext
- [ ] B9: „Nein“-Beschriftungen an G14 und G11 korrekt platzieren
- [ ] B10: Merge-Gateways vor A33 und A34
- [ ] F4: Timer E03/E05/E08 mit Fristwert beschriften
- [ ] B7: Gesamtansicht in der .bpmn entwirren, danach PNG und PDF aus derselben Datei exportieren
- [ ] Neue Elemente IDs vergeben, Elementzählung aktualisieren

### Prozessdokumentation

- [ ] AN3: Definition Antwortfrist und Werte (F4)
- [ ] AN4 und Schnittstelle K2: Restteilemeldung nur bei vorheriger Beteiligung von K2 (B2)
- [ ] AN5: „abgestimmtes Vorgehen“ an „mitteilen“ anpassen (B5)
- [ ] AN6: G12 neu formuliert (B4)
- [ ] Ablaufbeschreibung K4.3: neue Elemente und Namen
- [ ] Modellierungsentscheidungen: Annotationen, Merge-Konvention (B10), Verzicht B11
- [ ] Elementzahl und Fassungsangabe (v2) aktualisieren

### Präsentation

- [ ] Prozesslandkarte mit markiertem K4 (F2)
- [ ] Legende Nachrichtenflüsse (B8)
- [ ] Vorher-Nachher-Ausschnitte: B1, B2/B3, B6, F4
- [ ] Prüfgrenzen nennen: F4 nicht vom Assistenten beurteilt, SP2/SP3-Detailseiten nur in der Übersicht geprüft
