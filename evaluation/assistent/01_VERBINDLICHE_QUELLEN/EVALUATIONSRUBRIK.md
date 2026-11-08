# Evaluationsrubrik – fachliche BPMN-Modellqualität

| Dimension | Leitfrage | Prüfaspekte |
|---|---|---|
| Syntax | Werden BPMN-Elemente zulässig verwendet und verbunden? | Flussarten und Grenzen, Anschlüsse, Ereignispositionen, zulässige Elementkombinationen |
| Semantik | Ist die Modellaussage unter der BPMN-Bedeutung stimmig? | Gateway-Art, Alternativen und Synchronisation, Ereignis- und Nachrichtenbedeutung, Rollen-/Teilnehmerbedeutung, Wiederholungen und Fallbezug |
| Pragmatik | Ist das Modell für die fachliche Zielgruppe verständlich? | Bezeichnungen, Begriffe, Zuständigkeiten, Linienführung, Lesbarkeit, Grenzen und fachliche Detailtiefe |

Jede Dimension vollständig berücksichtigen; tatsächlich gelesenen Umfang nennen.
Abdeckung je Dimension: geprüft / teilweise geprüft / nicht geprüft / nicht beurteilbar.
Dies beschreibt keine Fehlerfreiheit. Nicht beurteilbare Aspekte mit fehlender
Grundlage benennen; nur teilweise Prüfung nicht als vollständige Abdeckung ausgeben.
Visuelle Prüfung und Eingangsdiagnostik sind Hilfsprüfungen, keine weiteren Dimensionen.

## Befundarten und Massstab

- Belegter Fehler: konkreter Verstoss gegen eine BPMN-Regel, semantischer Widerspruch
  oder belegte pragmatische Mehrdeutigkeit/Unlesbarkeit.
- Rückfrage: beabsichtigte Bedeutung unklar; keine Regelverletzung unterstellen.
- Darstellungshinweis: begründete Modellierungsempfehlung mit Verständnisgewinn.
- Nicht beurteilbar: fehlende oder unlesbare Grundlage verhindert die Aussage.

Jeder Befund nennt Dimension, sichtbare Fundstelle, Regel/Kriterium, Beleg, Auswirkung,
Modellierungshinweis und Sicherheit. Regelart ausdrücklich unterscheiden:
BPMN-Regel / Verständlichkeitskriterium / Modellierungsempfehlung / Klärungsbedarf.
Eine Empfehlung oder offene Frage ist kein belegter Fehler. Beim BPMN-Regelbezug
konkrete Regel erläutern; externe Normstelle nur nennen, wenn tatsächlich nachgelesen.
Keine Quellenstellen erfinden. Priorität: hoch = zentrale Modellaussage betroffen;
mittel = relevante Teilstelle; niedrig = lokale Klarheit. Sicherheit: belegt / begründet / offen.
Fehler ausschliesslich bei Sicherheit belegt und vorhandenem Beleg ausweisen.
Positiv geprüfte Stellen knapp nennen. Keine Note oder pauschale Freigabe.

## Grenzen und Beispiele

- Sequenzfluss zwischen Pools: Syntax prüfen und konkrete Verbindung belegen.
- Parallelverzweigung und nicht passende Zusammenführung: semantische Wirkung
  anhand erreichbarer Pfade erklären; kein pauschales Gateway-Paarungsverbot.
- Unklare Tätigkeitsnamen: Pragmatik, Empfehlung begründen; Objekt/Verb ist keine Syntaxpflicht.
- Doppelerfassung oder lange Wartezeit: keine Bewertung dieser betrieblichen Eigenschaft.
  Nur ihre BPMN-Darstellung kann Gegenstand eines Befunds sein.
- Abweichende Prozessbeschreibung: beabsichtigte Modellaussage klären; kein eigener
  Quellenabgleich und kein Fehler allein wegen einer betrieblichen Abweichung.
- Fehlende technische Ausführungsattribute oder Zusatzunterlagen: kein Qualitätsabzug.
