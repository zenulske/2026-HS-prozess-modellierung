# Änderungen an der Prozessdokumentation für v2

> Vorlage für die Überarbeitung der Prozessdokumentation K4 (bisher K4-A-3.0). Die Textbausteine ersetzen die genannten Stellen, damit Beschreibung und Modell v2 konsistent sind. Fassungsangabe überall auf „v2“ ändern.

## AN3 Fristen (F4)

**Neu:** Die Antwortfrist ist der Zeitraum ab Versand eines Vorschlags an die Kundschaft, innerhalb dessen VeloWerk deren Entscheid erwartet. Sie wird in Arbeitstagen gerechnet: 5 Arbeitstage für die Freigabe des Vorschlags (A07), 3 Arbeitstage für den Lieferentscheid (A12) und 2 Arbeitstage für den Zusatzentscheid (A18), weil das E-Bike dann bereits teilweise zerlegt einen Werkstattplatz belegt. Läuft die Frist ab (E03, E05, E08), wird der Empfang unterbrochen und der Auftrag über den Abbruchweg mit dokumentiertem Grund abgeschlossen. Späte Antworten setzen den Abbruchweg nicht automatisch fort. Dauerhafte Nichtlieferung und Nichtabholung sind nicht vollständig ausgearbeitet.

## AN4 Teile und Schnittstelle K2 (B2)

**Ergänzen:** Eine Meldung zu Abbruch und Restteilen (M15) erhält K2 nur, wenn im Auftrag zuvor Teile bei K2 angefordert wurden (G17). Wurde K4.2 übersprungen oder waren keine Ersatzteile nötig, entfällt die Meldung.

**Schnittstellenabschnitt K2 anpassen:** „… bei Abbruch meldet es Restteile (M15), sofern zuvor Teile angefordert wurden.“

## AN5 Zusatz und Rückgabe (B5)

**Ersetzen:** „Die Rückgabe folgt einem abgestimmten sicheren Vorgehen“ → „Die Kundschaft wird über Abbruch und Rückgabe informiert (A29); ein nicht sicheres E-Bike erhält keine Fahrfreigabe.“

## AN6 Nacharbeit (B4)

**Neu:** Jede Nacharbeit endet mit erneuter Prüfung. Nacharbeit dient ausschliesslich dem bereits vereinbarten Ergebnis und liegt damit im freigegebenen Umfang. G12 fragt deshalb nur, ob Nacharbeit im freigegebenen Umfang möglich ist. Ist das nicht der Fall, weil das Ergebnis nur mit zusätzlichem, nicht freigegebenem Aufwand erreichbar wäre oder fachlich nicht erreichbar ist, wird die Reparaturgrenze dokumentiert (A22). Eine feste Zahl von Wiederholungen wird nicht angenommen.

## Ablauf K4.1 (B10)

**Ergänzen:** Technische Unmöglichkeit, Ablehnung und Fristablauf werden über G19 zusammengeführt und führen zu A33.

## Ablauf K4.2 (B10)

**Ergänzen:** Ablehnung oder Fristablauf beim Zusatzentscheid werden zuerst über G20 zusammengeführt. G21 bündelt danach alle Abbruchwege von K4.2 vor A34.

## Ablauf K4.3 (B2, B3, B4, B5)

**Ersetzen ab „A22 und frühere Abbrüche …“:** A22 und frühere Abbrüche führen zu A28. Ist-Zustand und Nutzungshinweise bilden die Grundlage für die Rückgabe: A29 teilt Abbruch und Rückgabe der Kundschaft mit, A30 gibt das E-Bike mit Status zurück, A31 meldet die tatsächlich erbrachten Leistungen an S4. G17 prüft, ob Teile bei K2 angefordert wurden; nur dann meldet A35 Abbruch und Restteile an K2. Nach G18 schliesst A32 den Auftrag mit Grund, E24 beendet SP3 unvollständig. G15 unterscheidet danach E11 und E13.

## Modellierungsentscheidungen

**Ersetzen bzw. ergänzen:**

- Die BPMN-Datei enthält eine einzige Ansicht (Gesamtmodell). PNG und SVG sind direkt aus dieser Datei exportiert, damit Bild und .bpmn dieselbe Fassung zeigen (B7). Die früheren separaten Detailansichten entfallen; Detailausschnitte für Folien werden aus dem Gesamtexport geschnitten.
- Textanmerkungen beschreiben das Ergebnis jedes Unterprozesses in Klartext statt in ID-Kurzschrift (B6, F3).
- Zusammenführungskonvention: Abbruchwege werden vor dem Festhalten des Abbruchgrunds (A33, A34) mit XOR-Gateways gebündelt (B10). Übrige Zusammenführungen mit zwei Wegen bleiben direkt am Task.
- Die physische Übergabe des E-Bikes wird nicht als Nachrichtenfluss dargestellt, weil Nachrichtenflüsse im Modell konsequent für Informationen stehen; sie ist im Tasknamen von A25 und A30 ausgedrückt (B11, bewusst nicht umgesetzt).
- Timer sind mit Fristwerten beschriftet (F4).

## Umfang

**Ersetzen:** Fachlicher Stand ist v2. Das XML enthält 77 eindeutige Elemente: 35 Tasks, drei Unterprozesse, 18 Ereignisse und 21 Gateways. Konservativ verbleiben 59: 35 Tasks, sieben Ereignisse und 17 Gateways. Rahmen, neun interne Start-/Endereignisse, beide Links und G13–G16 sind dabei ausgeschlossen. Pools, Lanes, Flüsse und Anmerkungen zählen nicht.
