# Prüfnachweis – 0.3.0-candidate

Stand: 5. November 2026. Auftrag: Syntax, Semantik und Pragmatik fachlicher
BPMN-Ist-Modelle. Keine Bewertung betrieblicher Eigenschaften oder Realitätstreue.

## Nachweisstatus

39 Tests bestanden mit `py -3.13 -m unittest discover -s tests -v` auf Windows.
Geprüft: drei Dimensionen und Pflichtfelder, Ausschluss betrieblicher Dimensionen
und des alten Quellenabgleichs, Trennung von Empfehlung/Klärung und Fehler,
Prüfabdeckung unabhängig von Befunden, Versionswechsel, Beleg-/Modellreferenzen,
Bild-/XML-Grenzen, Hashschutz, tatsächlicher prepare/commit/status-Speicherablauf,
unveränderter neutraler Kern sowie Paketbau mit ZIP-/Dateihashes und Dokumentlinks.
Der Test verwendet CPython 3.13 und vorhandenes jsonschema, nicht den ausgelieferten
isolierten CPython-3.12-Einstieg.

Sechs synthetische fachliche Durchgänge wurden vom bearbeitenden Assistenten
durchgeführt und mit Eingabe, Kurzantwort und Grenzen in
tests/FACHLICHE_DURCHSICHT_030.md dokumentiert. Dies ist keine unabhängige Abnahme.
20 Dialog-Abnahmefälle stehen in tests/FACHLICHE_PRUEFFAELLE.md; deren separate
praktische Ausführung mit vollständigen Modellen bleibt offen. Historische
Nachweise gelten nicht als Nachweis der neuen Bewertungsstruktur.

## Grenzen

Keine neue native ADONIS-/Camunda-/Mac-Prüfung, kein neuer Renderer-Test und kein
isolierter CPython-3.12-Erststart. Entwicklungstests mit vorhandenem CPython 3.13
und jsonschema ersetzen diesen optionalen Speicherstart nicht. Die Evaluation im
Gespräch benötigt diese Laufzeit nicht. Technische Tests prüfen keine allgemeine
fachliche Fehlererkennungsqualität und keine vollständige BPMN-Normkonformität.
