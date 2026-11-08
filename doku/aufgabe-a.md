# Aufgabe A – Modellierung eines Kernprozesses mit BPMN 2.0

> Woche a, erste Präsentation. Gruppenaufgabe. Grundlage: die zuvor erstellte Prozesslandkarte (siehe `unternehmen.md`).
> Folgeaufgabe: `aufgabe-b.md` (Überarbeitung auf Basis von Feedback).
> Stand der Aufgabenstellung: zuletzt geändert am 22. Oktober 2026.

## Kurzüberblick

| Punkt | Inhalt |
|---|---|
| Ziel | Einen Kernprozess aus der Prozesslandkarte analysieren, textuell beschreiben und als fachliches BPMN-2.0-Modell darstellen |
| Umfang Modell | Mindestens 40 modellierte Elemente (Aktivitäten, Ereignisse, Gateways); Sequenzflüsse, Pools und Lanes zählen nicht |
| Präsentation | ca. 8 Minuten, Zeit strikt einhalten |
| Abgabe | Moodle, als .zip (z. B. `KK1-1.zip`), hochgeladen von einer Person |
| Tool | Adonis oder anderes Tool, Hauptsache konforme BPMN-2.0-Notation |

---

## 1. Auswahl des Kernprozesses

Einen Kernprozess aus der bestehenden Prozesslandkarte wählen, der sich für eine detaillierte Modellierung eignet.

Der Prozess sollte:

- für die Wertschöpfung des Unternehmens relevant sein,
- einen klar erkennbaren Anfang und ein nachvollziehbares Ende besitzen,
- mehrere Aktivitäten bzw. Bearbeitungsschritte umfassen,
- mindestens zwei beteiligte Rollen oder Organisationseinheiten einbeziehen,
- ausreichend komplex für eine fachlich sinnvolle BPMN-Modellierung sein.

**Gefordert:** kurze Begründung der Wahl.

## 2. Textuelle Prozessbeschreibung

Beschreibung so formulieren, dass auch eine Person ohne Vorwissen den grundlegenden Ablauf nachvollziehen kann. Sie ist die fachliche Grundlage für das BPMN-Modell.

Mindestens enthalten:

- Name und Ziel des Prozesses
- auslösendes Ereignis bzw. Prozessstart
- erwartetes Prozessergebnis
- beteiligte Rollen, Abteilungen oder externe Akteure
- wesentliche Prozessschritte
- wichtige Entscheidungen oder Verzweigungen

## 3. Herausforderungen des Prozesses

Wesentliche Herausforderungen bei der Durchführung beschreiben, nicht nur aufzählen: jeweils erläutern, **warum** sie relevant sind und **welche Auswirkungen** sie haben können.

Mögliche Herausforderungen:

- Medienbrüche
- Wartezeiten
- unklare Verantwortlichkeiten
- Abstimmungsprobleme zwischen Rollen oder Abteilungen
- Fehleranfälligkeit
- Informationsverluste
- Engpässe
- manuelle Tätigkeiten
- Abhängigkeiten von externen Akteuren
- Sonderfälle und Ausnahmen

## 4. Erstellung des BPMN-2.0-Prozessmodells

Fachliches Modell auf sinnvoller Abstraktionsebene; Ziel ist eine verständliche Darstellung des fachlichen Ablaufs, keine technische Implementierung.

### Pflichtbestandteile

- ein eindeutiges Startereignis
- mindestens ein Endereignis
- die wesentlichen Aktivitäten bzw. Tasks
- die relevanten Rollen oder Organisationseinheiten
- geeignete Pools und/oder Lanes
- die notwendigen Sequenzflüsse
- relevante Entscheidungen und Verzweigungen mit geeigneten Gateways
- ggf. Nachrichtenflüsse, wenn unterschiedliche Prozessbeteiligte kommunizieren

### Mindestumfang

- **Mindestens 40 modellierte Elemente**
- Zählen: Aktivitäten, Ereignisse, Gateways
- Zählen nicht: Sequenzflüsse und andere verbindende Elemente, Pools, Lanes
- Die Zahl ist eine Orientierung; entscheidend ist eine fachlich korrekte, vollständige und nachvollziehbare Darstellung.

### Qualitätskriterien

- BPMN-Elemente fachlich korrekt eingesetzt
- Prozessfluss eindeutig nachvollziehbar
- Aktivitäten verständlich und nach dem Muster **Verb + Objekt** benannt
- Entscheidungen und alternative Pfade logisch dargestellt
- Rollen und Verantwortlichkeiten eindeutig erkennbar
- Modell nicht unnötig komplex
- grafische Darstellung übersichtlich und gut lesbar

### Tool

Adonis oder ein anderes Modellierungstool. Das finale Modell muss in konformer BPMN-2.0-Notation vorliegen.

## 5. Konsistenz zwischen Beschreibung und Modell

Textuelle Beschreibung und BPMN-Modell müssen inhaltlich übereinstimmen: Prozessschritte, Rollen, Entscheidungen und wesentliche Abläufe aus dem Text müssen im Modell erkennbar sein.

Werden während der Modellierung Annahmen ergänzt oder der Ablauf angepasst, muss die Dokumentation entsprechend aktualisiert werden.

## 6. Präsentation

Gruppenpräsentation, **ca. 8 Minuten**, die Einhaltung der Zeit ist sehr wichtig.

Mindestinhalte:

- kurze Einordnung des Kernprozesses in die bestehende Prozesslandkarte
- Ziel und Bedeutung des Prozesses für das Unternehmen
- beteiligte Rollen und wesentliche Prozessschritte
- Vorstellung und Erläuterung des BPMN-2.0-Modells
- zentrale Entscheidungen, Varianten oder Besonderheiten im Prozess
- identifizierte Herausforderungen
- kurze Reflexion der wichtigsten Modellierungsentscheidungen

Beim Modell auf die besonders relevanten Stellen konzentrieren; nicht jedes Element erklären.

## 7. Abgabe über Moodle

### Vier Bestandteile pro Gruppe

- [ ] BPMN-2.0-Modell als Bilddatei (.png oder .jpg)
- [ ] BPMN-2.0-Modell als .bpmn-Datei
- [ ] textuelle Prozessdokumentation
- [ ] Präsentationsfolien

Das Modell gut lesbar einreichen (z. B. PDF oder Bilddatei), wenn möglich zusätzlich im nativen Format des Modellierungstools.

### Dateinamen

Schema: `Gruppennummer_Unternehmensname_Kernprozess_Dokument`

Beispiel: `Gruppe03_MusterAG_Auftragsabwicklung_BPMN.pdf`

### Archiv

Alle Dateien gebündelt als .zip, hochgeladen von einer Person der Gruppe.

Schema: `Gruppennummer.zip`, Beispiel: `KK1-1.zip`

## 8. Bewertungskriterien

- Der gewählte Prozess ist tatsächlich ein Kernprozess des Unternehmens.
- Die textuelle Beschreibung ist verständlich und vollständig.
- BPMN 2.0 ist fachlich korrekt angewendet.
- Der Ablauf ist logisch und nachvollziehbar modelliert.
- Rollen und Verantwortlichkeiten sind eindeutig dargestellt.
- Modell und Dokumentation sind konsistent.
- Relevante Herausforderungen sind sinnvoll identifiziert und erläutert.
- Die Modellierung hat eine angemessene Detailtiefe.
- Die Darstellung ist übersichtlich und professionell.
- Wesentliche Modellierungsentscheidungen können begründet werden.

**Fiktiver Prozess:** Annahmen sind erlaubt, müssen aber plausibel, transparent und in sich konsistent sein.

## 9. Rolle als Zuhörende: konstruktives Feedback

Bei den Präsentationen anderer Gruppen mündliches Feedback geben, zu gelungenen Aspekten und konkreten Verbesserungspotenzialen. Ein Handout mit Beobachtungskriterien steht zur Verfügung.

Worauf achten:

- Werden Ziel und Ablauf des Prozesses verständlich?
- Ist der Kernprozess sinnvoll abgegrenzt?
- Sind Rollen und Verantwortlichkeiten nachvollziehbar?
- Sind die BPMN-Elemente passend eingesetzt?
- Sind Entscheidungen und alternative Pfade verständlich modelliert?
- Passen Modell und Beschreibung zusammen?
- Wurden relevante Herausforderungen erkannt?
- Ist das Modell insgesamt verständlich und übersichtlich?
