# Feedback aus der ersten Präsentation (Aufgabe A)

> Feedbackquelle 1 für Aufgabe B. Mündliche Rückmeldungen nach der ersten Präsentation, nachträglich von der Gruppe festgehalten.
> Feedbackquelle 2 (Evaluationsassistent) wird separat dokumentiert.

## Kontext

| Feld | Angabe |
|---|---|
| Gruppe | KK6-4 |
| Unternehmen | VeloWerk Zürich AG |
| Gezeigter Kernprozess | K4 Reparatur- und Serviceaufträge abwickeln |
| Präsentierte Modellfassung | v1 = K4-A-3.0, Abgabestand 03.11.2026 |
| Datum der Präsentation | <!-- ergänzen --> |

## Rückmeldungen

### F1 – Präsentation war zu wenig übersichtlich

- **Betrifft:** Präsentation (Folien, Aufbau)
- **Rückmeldung:** Der Präsentation hat es an Übersichtlichkeit gefehlt.
- **Offene Punkte zur Prüfung:**
  - Woran lag es konkret: Folienaufbau, Reihenfolge, zu viel Inhalt pro Folie, Lesbarkeit des Modells?
  - War das BPMN-Modell auf den Folien gross genug bzw. in lesbaren Ausschnitten gezeigt?

### F2 – Nur Kernprozess K4 gezeigt, das hat verwirrt

- **Betrifft:** Präsentation, Einordnung in die Prozesslandkarte
- **Rückmeldung:** Es wurde nur der Kernprozess K4 gezeigt, was beim Publikum zu Verwirrung geführt hat.
- **Offene Punkte zur Prüfung:**
  - Fehlte die Einordnung von K4 in die Prozesslandkarte (welche anderen Kern-, Management- und Supportprozesse es gibt)?
  - War unklar, warum gerade K4 gewählt wurde?
  - Waren Schnittstellen zu anderen Prozessen (z. B. Übergaben von oder an K1–K3) nicht erkennbar?

### F3 – Annotationen im Modell waren der Gruppe selbst unklar

- **Betrifft:** BPMN-Modell (Pragmatik), ggf. Prozessbeschreibung
- **Rückmeldung:** Im Modell wurden Textannotationen verwendet, deren Bedeutung bzw. Zweck die Gruppe selbst nicht erklären konnte.
- **Stand v1:** Laut Prozessdokumentation stehen „Ergebnisangaben als BPMN-Textanmerkungen im Modell“.
- **Offene Punkte zur Prüfung:**
  - Welche Annotationen sind im Modell enthalten und was sollten sie jeweils aussagen?
  - Tragen sie fachliche Information, die sonst fehlt, oder sind sie überflüssig?
  - Gehört die Information eher in die Prozessbeschreibung, in die Annahmen oder in die Benennung eines Elements?

### F4 – Begriff „Antwortfrist“ ist nicht definiert

- **Betrifft:** Prozessbeschreibung, Annahmen, ggf. BPMN-Modell (Zeitereignis)
- **Rückmeldung:** Es muss definiert werden, was mit „Antwortfrist“ genau gemeint ist und wie lange sie dauert (z. B. Anzahl Tage).
- **Stand v1 (AN3):** Antwortfristen für A07, A12 und A18 werden „fallbezogen vereinbart“; die Timer sind symbolisch und enthalten bewusst keine Zeitwerte. Fristablauf (E03, E05, E08) führt zum Abbruchweg.
- **Betroffene Stellen:**

  | Warteschritt | Worauf wird gewartet | Timer bei Ablauf |
  |---|---|---|
  | A07 | Kundenentscheid zu Vorschlag (Umfang, Kosten, Terminrahmen) | E03 |
  | A12 | Kundenentscheid zur Lieferoption bei fehlenden Teilen | E05 |
  | A18 | Kundenentscheid zum Zusatzvorschlag | E08 |

- **Offene Punkte zur Prüfung:**
  - Wer muss innerhalb der Frist antworten, und wem (Kundschaft an VeloWerk oder umgekehrt)?
  - Worauf bezieht sich die Antwort (z. B. Freigabe eines Kostenvoranschlags, Rückmeldung zu einer Reklamation)?
  - Wie lange ist die Frist (Kalender- oder Arbeitstage)?
  - Was passiert im Prozess, wenn die Frist abläuft?
  - Ist die Frist im Modell als Zeitereignis dargestellt, und stimmt die Darstellung mit der Definition überein?

## Feedbackübersicht für Aufgabe B

> Wird nach der fachlichen Prüfung ausgefüllt. Hinweis: Gegenstand bleibt der Ist-Prozess. Eine Definition der Antwortfrist präzisiert eine Annahme; sie ändert nicht den betrieblichen Ablauf.

| Nr. | Feedbackquelle und Fundstelle | Rückmeldung | Fachliche Prüfung und Entscheidung | Änderung und betroffenes Artefakt |
|---|---|---|---|---|
| F1 | Präsentationsrunde 1 | Präsentation zu wenig übersichtlich | | |
| F2 | Präsentationsrunde 1 | Nur K4 gezeigt, Einordnung fehlte, verwirrend | | |
| F3 | Präsentationsrunde 1 | Annotationen im Modell, Bedeutung der Gruppe selbst unklar | | |
| F4 | Präsentationsrunde 1 | „Antwortfrist“ nicht definiert (Bedeutung, Dauer) | | |
