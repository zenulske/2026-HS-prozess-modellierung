# Prüfprotokoll r2 – BPMN-Ist-Evaluationsassistent

## Vorgehen

1. Im **selben Chat wie r1** weiterarbeiten (dort ist das Assistentenpaket bereits geladen). Die Aufgabenstellung sieht das so vor: eine überarbeitete Fassung eindeutig kennzeichnen und die zugehörigen Dateien hochladen.
2. Folgende Dateien hochladen:
   - `prozesse/v2/KK6-4_VeloWerkZuerich_ReparaturService_BPMN_v2.bpmn`
   - `prozesse/v2/KK6-4_VeloWerkZuerich_ReparaturService_BPMN_v2.png`
   - `doku/feedbackuebersicht.md` (zur Klärung der beabsichtigten Änderungen)
   - `doku/prozessdoku-aenderungen-v2.md` bzw. die überarbeitete Prozessdokumentation v2
3. Prüfauftrag eingeben:

> Hier ist die überarbeitete Fassung v2 unseres fachlichen BPMN-Ist-Modells. Sie ersetzt v1 vollständig; bitte prüfe ausschliesslich die neu hochgeladenen Dateien. Evaluiere v2 anhand der Prüfgrundlagen des Assistenten. Prüfe Syntax, Semantik und Pragmatik. Gib einen Bericht mit belegten Befunden, Darstellungshinweisen, offenen Fragen und der tatsächlichen Prüfabdeckung aus. Gib zusätzlich für jeden Befund B1–B11 aus deinem Bericht r1 an, ob er in v2 behoben, teilweise behoben oder weiterhin vorhanden ist. Die beigefügte Feedbackübersicht und die Dokumentationsänderungen dienen zur Klärung unserer beabsichtigten Modellaussage.

4. Bericht als `evaluationsbericht_r2.md` in diesem Ordner speichern und unten eintragen.

## Angaben

| Feld | Angabe |
|---|---|
| Geprüfte Modellfassung | v2 (Überarbeitung von K4-A-3.0 auf Basis von Präsentationsfeedback und r1) |
| Bereitgestellte Dateien | v2 .bpmn (77 Elemente, 1 Ansicht), v2 PNG, v2 SVG (nur Herkunft geprüft), feedbackuebersicht.md, prozessdoku-aenderungen-v2.md |
| Sprachmodell-Umgebung | claude.ai |
| Modellbezeichnung | Opus 5.5 |
| Prüfdatum | 08.11.26 |
| Bericht | `evaluationsbericht_r2.md` (für Abgabe: `KK6-4_VeloWerkZuerich_ReparaturService_Assistentenbericht_r2.pdf`) |
| Vom Assistenten gemeldete nicht lesbare Dateien | keine gemeldet |
| Gesamturteil | Kein BPMN-Regelverstoss; keine offene Rückfrage; 2 neue Darstellungshinweise |
| Prüfgrenzen | Keine XSD-/OMG-Vollkonformität; SVG nicht separat angesehen; vollständige Prozessdokumentation v2 lag nicht vor (nur Änderungsliste) |

## Nachverfolgung r1

| Befund r1 | Unsere Entscheidung | Ergebnis laut r2 |
|---|---|---|
| B1 | Umgesetzt | behoben |
| B2 | Umgesetzt | behoben |
| B3 | Umgesetzt (mit B2) | behoben |
| B4 | Umgesetzt (Präzisierung) | behoben |
| B5 | Umgesetzt | behoben |
| B6 | Umgesetzt (= F3) | behoben |
| B7 | Umgesetzt | behoben (kleine Restüberlagerung bei M15, siehe R2-02) |
| B8 | Teilweise (Legende) | behoben (Namen an den Nachrichtenflüssen im Modell; Eintrag in der Feedbackübersicht anpassen) |
| B9 | Umgesetzt | behoben |
| B10 | Teilweise (Merge vor A33/A34) | teilweise behoben (G03 führt weiterhin zusammen und verzweigt; die dokumentierte Konvention passt nicht zu G06/G07/G10/G16 und G20) |
| B11 | Nicht umgesetzt (begründet) | weiterhin vorhanden, bewusste und nachvollziehbare Konvention, kein weiterer Befund |

## Neue Befunde r2

| Nr. | Dimension | Art (Fehler / Rückfrage / Darstellung) | Befund | Entscheidung |
|---|---|---|---|---|
| R2-01 | Pragmatik | Darstellung / mittel, belegt | In SP2 stehen die Beschriftungen „Ja“ (G05), „Nein“ (G04) und „Ja“ (G09) weit weg von ihrem Gateway an der Lane-Grenze neben G21; „Ja“ (G05) wird von der Linie G20 → G21 durchgestrichen | |
| R2-02 | Pragmatik | Darstellung / niedrig, belegt | Wörter werden ohne Bindestrich mitten im Wort umbrochen (M13, M08, M05, G06, G08, G02); die Linie von M15 berührt die eigene Beschriftung, die Linie von M08 kreuzt die Beschriftung von E06 | |
