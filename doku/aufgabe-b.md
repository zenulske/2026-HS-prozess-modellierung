# Aufgabe B – Überarbeitung des fachlichen BPMN-Ist-Modells auf Basis von Feedback

> Woche b, zweite Präsentation. Baut auf `aufgabe-a.md` auf; alle bisherigen Anforderungen gelten weiter.
> Stand der Aufgabenstellung: zuletzt geändert am 5. November 2026.

## Kurzüberblick

| Punkt | Inhalt |
|---|---|
| Kernfrage | Wie wurde das Feedback fachlich geprüft und genutzt, um BPMN-Ist-Modell, Prozessbeschreibung und Dokumentation zu verbessern? |
| Feedbackquellen | 1) Rückmeldungen aus der ersten Präsentation, 2) BPMN-Ist-Evaluationsassistent |
| Weiterhin gültig | Abgegrenzter Kernprozess, mind. zwei Rollen/Organisationseinheiten, mind. 40 Aktivitäten, Ereignisse und Gateways (ohne Verbindungen, Pools, Lanes) |
| Präsentation | ca. 12 Minuten, verbindlich, inkl. Vorstellung der Assistentennutzung |
| Gegenstand | Weiterhin der **Ist-Prozess**: Modellierungskorrekturen von Änderungen am betrieblichen Ablauf unterscheiden |
| Abgabe | Moodle, .zip nach Gruppennummer (z. B. `KK6-4.zip`) |

---

## 1. Erneute Vorstellung des Kernprozesses

Bewusst kurz halten, der Schwerpunkt liegt auf der Weiterentwicklung.

- Name und Ziel des Kernprozesses
- Einordnung in die Prozesslandkarte
- beteiligte Rollen oder Organisationseinheiten
- wesentliche Prozessschritte und zentrale Entscheidungen
- relevantes Prozessergebnis

## 2. Feedback mit dem BPMN-Ist-Evaluationsassistenten einholen

Das bestehende Ist-Modell vom Assistenten prüfen lassen und festhalten, **welche Modellfassung** geprüft wurde.

### Bereitzustellende Dateien (derselben Modellfassung)

- BPMN-Modell als `.bpmn`-Datei
- gut lesbarer Export als PNG, SVG oder PDF
- optional: textuelle Prozessbeschreibung und weitere Unterlagen zur Klärung der Modellaussage

Ein Bild- oder PDF-Export allein ermöglicht nur eine eingeschränkte Prüfung.

### Prüfdimensionen

| Dimension | Leitfrage |
|---|---|
| Syntax | Sind BPMN-Elemente zulässig verwendet und verbunden? |
| Semantik | Ist die Bedeutung der modellierten Abläufe, Entscheidungen, Ereignisse und Nachrichten stimmig? |
| Pragmatik | Ist das Modell für die fachliche Zielgruppe verständlich und lesbar? |

### Umgang mit den Rückmeldungen

- Rückmeldungen selbst prüfen.
- Unterscheiden zwischen **belegten Fehlern**, **offenen Rückfragen** und **Darstellungsempfehlungen**.
- Relevante Rückfragen klären und begründet entscheiden, welche Hinweise umgesetzt werden.

### Grenzen des Assistenten

- bewertet keine betrieblichen Eigenschaften (Effizienz, Wartezeiten, Doppelarbeit)
- prüft nicht, ob der reale Prozess vollständig und wirklichkeitsgetreu erfasst ist
- erstellt oder verändert keine Modelle
- fachliche Verantwortung und Überarbeitung liegen bei der Gruppe

### Zu sichern und dokumentieren

- verwendeter Evaluationsbericht
- geprüfte Modellfassung
- wesentliche Entscheidungen zum Feedback (kann in der bestehenden Prozessdokumentation erfolgen)

### Vorgehen: Assistent in ein Sprachmodell einbinden

Der Assistent ist ein Paket mit Anweisungen, Prüfregeln und Hilfsdateien. Er wird in einer Sprachmodell-Umgebung genutzt, die Dateien und Bilder lesen kann.

1. **Neuen Chat öffnen** – eigener Chat für die Gruppe, damit keine anderen Aufgaben oder Modelle die Prüfung beeinflussen.
2. **Assistentenpaket bereitstellen** – Paket hochladen. Falls ZIP nicht verarbeitet wird: entpacken und Dateien über die Datei- oder Projektfunktion bereitstellen. Ordnerstruktur und Dateinamen erhalten.
3. **Assistenten starten** mit folgender Anweisung:

   > Im bereitgestellten Paket befindet sich der BPMN-Ist-Evaluationsassistent. Lies START_PROMPT.md und die darin genannten Pflichtdateien vollständig. Verwende diese Anweisungen und Prüfgrundlagen für die anschließende Evaluation unseres fachlichen BPMN-Ist-Modells. Benenne ausdrücklich, wenn du eine benötigte Datei nicht lesen kannst.

4. **Zugriff kontrollieren** – auf Meldungen zu fehlenden oder unlesbaren Dateien achten und diese nachreichen. Die Startdatei allein enthält nicht alle Prüfgrundlagen.
5. **Modell hochladen und Prüfung beauftragen** – `.bpmn` und lesbaren Export derselben Fassung bereitstellen, z. B.:

   > Evaluiere unser hochgeladenes fachliches BPMN-Ist-Modell anhand der Prüfgrundlagen des Assistenten. Prüfe Syntax, Semantik und Pragmatik. Gib einen Bericht mit belegten Befunden, Darstellungshinweisen, offenen Fragen und der tatsächlichen Prüfabdeckung aus. Die beigefügte Prozessbeschreibung dient zur Klärung unserer beabsichtigten Modellaussage.

   Den letzten Satz nur verwenden, wenn eine Prozessbeschreibung beigefügt ist.

6. **Feedback bearbeiten** – Rückfragen beantworten, Hinweise fachlich prüfen, Artefakte selbst überarbeiten. Eine erneut geprüfte Fassung eindeutig kennzeichnen und die zugehörigen Dateien hochladen.

Eine lokale Installation von Python oder den Hilfsprogrammen ist nicht nötig. Kann die Umgebung keine Vorschau aus der BPMN-Datei erzeugen, einen lesbaren Export bereitstellen.

**Dokumentieren:** Sprachmodell-Umgebung, Modellbezeichnung (soweit angezeigt), Prüfdatum, geprüfte Fassung des BPMN-Modells.

## 3. Überarbeitete Prozessbeschreibung und Dokumentation

Deutlich machen:

- welche Rückmeldungen für die Überarbeitung relevant waren
- welche Inhalte präzisiert, ergänzt oder entfernt wurden
- ob Rollen, Prozessschritte oder Entscheidungen klarer beschrieben wurden
- ob Annahmen oder Prozessgrenzen präzisiert werden mussten
- warum die Änderungen vorgenommen wurden

Bei Änderungen am Modell selbst prüfen, welche Anpassungen an den begleitenden Unterlagen nötig sind. Beschreibung und Modell müssen konsistent bleiben. Den vollständigen Konsistenzabgleich verantwortet die Gruppe.

## 4. Überarbeitetes BPMN-2.0-Ist-Modell

Auf die Stellen konzentrieren, die aufgrund von Präsentations- oder Assistentenfeedback geändert wurden, zum Beispiel:

- Korrekturen an Verwendung oder Verbindung von BPMN-Elementen
- Anpassungen an Gateways, Verzweigungen oder Zusammenführungen
- präzisere Darstellung von Ereignissen und Nachrichtenflüssen
- klarere Darstellung von Pools, Lanes und Zuständigkeiten
- verständlichere und einheitlichere Bezeichnungen
- übersichtlichere Linienführung und lesbarere Modellausschnitte

Jeweils erläutern: welches Problem vorlag und wie die Überarbeitung Korrektheit oder Verständlichkeit verbessert.

Gegenstand bleibt der **bestehende Ist-Prozess**. Änderungen am betrieblichen Ablauf sind von Korrekturen der Modellierung zu unterscheiden. Das gesamte Modell muss nicht erneut erklärt werden.

## 5. Umgang mit identifizierten Herausforderungen

Herausforderungen aus der ersten Präsentation erneut aufgreifen und zeigen:

- ob sich die Einschätzung durch Feedback oder weitere Analyse verändert hat
- ob Herausforderungen ergänzt, präzisiert oder anders eingeordnet wurden
- ob daraus Anpassungen an Beschreibung oder BPMN-Darstellung entstanden sind

Beispiele: Wartezeiten, Medienbrüche, unklare Zuständigkeiten, Informationsverluste, Engpässe, Ausnahmefälle.

Die betriebliche Einschätzung erfolgt durch die Gruppe; der Assistent prüft nur die BPMN-Darstellung.

## 6. Integration und kritische Reflexion des Feedbacks

Zentraler Bestandteil der Präsentation. Beide Feedbackquellen berücksichtigen.

Leitfragen:

- Welche wesentlichen Rückmeldungen gab es aus beiden Quellen?
- Welche waren besonders hilfreich?
- Wie wurde ihre fachliche Berechtigung geprüft?
- Welche Änderungen wurden abgeleitet?
- Welche Artefakte waren betroffen?
- Welche Hinweise wurden bewusst nicht umgesetzt und warum?
- Welche Fragen oder Prüfgrenzen sind offen geblieben?

Nicht jeder Hinweis muss präsentiert werden; die relevantesten aus beiden Quellen auswählen. Aussagen des Assistenten nicht ungeprüft übernehmen; auch eine begründete Ablehnung zeigt fachliche Auseinandersetzung.

### Vorlage: Feedbackübersicht

| Feedbackquelle und Fundstelle | Rückmeldung | Fachliche Prüfung und Entscheidung | Änderung und betroffenes Artefakt |
|---|---|---|---|
| Präsentationsrunde / Assistent | Kurze Zusammenfassung | Umgesetzt, teilweise umgesetzt oder nicht umgesetzt, mit Begründung | Konkrete Anpassung bzw. begründeter Verzicht |
| | | | |

## 7. Vorher-Nachher-Vergleich

Zentrale Änderungen nachvollziehbar machen, z. B. durch:

- Gegenüberstellung ursprünglicher und überarbeiteter Modellausschnitte
- eine präzisierte Stelle der Prozessbeschreibung
- eine Änderung gleichzeitig in Modell und Dokumentation

Abfolge: **Feedback → fachliche Prüfung → Entscheidung → Änderung → Ergebnis**

Lesbare Ausschnitte verwenden, Fassungen eindeutig kennzeichnen und konkret erklären, wodurch die neue Darstellung korrekter, eindeutiger oder verständlicher ist.

## 8. Präsentationsdauer

**Ca. 12 Minuten, verbindlich.** Die Vorstellung der Assistentennutzung gehört in diese Zeit; eine ausführliche Vorführung ist nicht nötig. Schwerpunkt: Weiterentwicklung und Begründung der Entscheidungen.

## 9. Erwartung an die zweite Präsentation

Am Ende soll erkennbar sein:

- wie sich Prozessbeschreibung, Dokumentation und Ist-Modell weiterentwickelt haben
- welches Feedback aus welcher Quelle ausschlaggebend war
- wie das Assistentenfeedback fachlich geprüft wurde
- warum Hinweise umgesetzt oder bewusst nicht umgesetzt wurden
- welche Herausforderungen präzisiert wurden
- welche Fragen offen bleiben und welche Erkenntnisse gewonnen wurden

Entscheidend ist die Qualität der Überarbeitung und Begründungen, nicht die Anzahl der Änderungen oder Befunde.

## 10. Abgabe über Moodle

### Bestandteile

- [ ] Überarbeitetes BPMN-2.0-Ist-Modell als Bild- oder PDF-Datei
- [ ] Überarbeitetes BPMN-2.0-Ist-Modell als `.bpmn`-Datei
- [ ] Überarbeitete textuelle Prozessdokumentation
- [ ] Präsentationsfolien
- [ ] Evaluationsbericht des Assistenten (PDF oder Textdatei)
- [ ] Angaben zum Bericht: Sprachmodell-Umgebung, Modellbezeichnung (soweit angezeigt), Prüfdatum, geprüfte Modellfassung
- [ ] Dokumentation der Feedbackverarbeitung inkl. Vorher-Nachher-Vergleich (kann in Dokumentation oder Folien integriert sein)

Ein vollständiger Chatverlauf ist nicht erforderlich. Die Abgabe der ersten Präsentation muss nicht erneut eingereicht werden.

### Dokumentation der Feedbackverarbeitung

Für jede wesentliche Rückmeldung:

- Quelle
- fachliche Prüfung
- umgesetzt, teilweise umgesetzt oder nicht umgesetzt
- Begründung
- daraus entstandene Änderungen und betroffene Artefakte

### Dateinamen

Schema: `Gruppennummer_Unternehmensname_Kernprozess_Dokument_Fassung`

Für diese Gruppe (Kernprozess noch einsetzen):

- `KK6-4_VeloWerkZuerich_<Kernprozess>_BPMN_final.bpmn`
- `KK6-4_VeloWerkZuerich_<Kernprozess>_BPMN_final.pdf`
- `KK6-4_VeloWerkZuerich_<Kernprozess>_Dokumentation_final.pdf`
- `KK6-4_VeloWerkZuerich_<Kernprozess>_Praesentation2.pdf`
- `KK6-4_VeloWerkZuerich_<Kernprozess>_Assistentenbericht_r1.pdf`

Die vom Assistenten geprüfte Fassung und die finale Abgabefassung eindeutig unterscheiden, falls sie abweichen.

### Gebündelte Abgabe

- Alle Dateien als ZIP, benannt nach der Gruppennummer: `KK6-4.zip`
- Hochladen innerhalb der Frist im Moodle-Abgabebereich; laut Aufgabenstellung laden alle Gruppenmitglieder die Abgabe hoch.
- Prüfen, dass alle Dateien geöffnet werden können und alle bewertungsrelevanten Inhalte enthalten sind. Bewertet werden nur die eingereichten Artefakte.
