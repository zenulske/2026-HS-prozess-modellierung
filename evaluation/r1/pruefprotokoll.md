# Prüfprotokoll r1 – BPMN-Ist-Evaluationsassistent

| Feld | Angabe |
|---|---|
| Geprüfte Modellfassung | v1 – K4-A-3.0, Abgabestand 03.11.2026 |
| Bereitgestellte Dateien | .bpmn (71 Elemente, 5 Ansichten), PNG-Gesamtansicht, Prozessdokumentation (S. 3, S. 5), feedback-praesentation1.md |
| Sprachmodell-Umgebung | claude.ai|
| Modellbezeichnung | Opus 5.5 |
| Prüfdatum | 08.11.26 |
| Bericht | `evaluationsbericht_r1.md` (für Abgabe umbenennen: `KK6-4_VeloWerkZuerich_ReparaturService_Assistentenbericht_r1.pdf`) |
| Vom Assistenten gemeldete nicht lesbare Dateien | keine gemeldet |
| Gesamturteil | Kein BPMN-Regelverstoss; 1 belegter Mangel (Lesbarkeit), 2 offene Fragen, mehrere Darstellungshinweise |
| Prüfgrenzen | Keine XSD-/OMG-Vollkonformität; PDF-Detailseiten SP2 und SP3 nur in der Übersicht verglichen |

## Befunde (Kurzfassung)

| Nr. | Dimension | Art (Fehler / Rückfrage / Darstellung) | Befund | Entscheidung |
|---|---|---|---|---|
| B1 | Pragmatik | Belegter Mangel / mittel | Nein-Flüsse von G01 und G08 kreuzen den Ja-Fluss vor A04 bzw. A16, Beschriftung weit entfernt || Umgesetzt |
| B2 | Semantik | Rückfrage / mittel | A32 sendet M15 „Abbruch / Restteile“ an K2 auch, wenn K2 nie beteiligt war (G13 Nein, G03 Nein) || Umgesetzt |
| B3 | Pragmatik | Darstellung / niedrig | A32 ist als einziger Sender kein Send-Task, Name nennt Meldung an K2 nicht || Umgesetzt (mit B2) |
| B4 | Semantik | Rückfrage / mittel | G12 „freigegeben und sinnvoll?“: unklar, welche Freigabe gemeint ist; bündelt zwei Kriterien || Umgesetzt (Präzisierung) |
| B5 | Pragmatik | Rückfrage / niedrig | A29 „abstimmen“ klingt nach Austausch, modelliert ist nur Senden || Umgesetzt |
| B6 | Pragmatik | Darstellung / mittel | Annotationen T01–T03 in ID-Kurzschrift (= F3) || Umgesetzt (= F3) |
| B7 | Pragmatik | Darstellung / mittel, belegt | Gesamtansicht in .bpmn weicht vom PNG ab; M14/M15 überlagern G15 || Umgesetzt |
| B8 | Pragmatik | Darstellung / niedrig | Nachrichtenflüsse in Gesamtansicht nur mit M01–M15 beschriftet || Teilweise (Legende) |
| B9 | Pragmatik | Darstellung / niedrig, belegt | Zwei „Nein“-Beschriftungen an G14/G11 mehrdeutig || Umgesetzt |
| B10 | Pragmatik | Darstellung / niedrig | Zusammenführungen uneinheitlich (Gateway vs. direkt an Task, A34 mit 4 Eingängen) || Teilweise (Merge ab 3 Eingängen) |
| B11 | Pragmatik | Darstellung / niedrig | Physische Übergabe (A25, A30) im Pool-Zusammenspiel nicht sichtbar || Nicht umgesetzt (begründet) |

Begründungen: siehe `doku/feedbackuebersicht.md`.
