# Optionale Vorschau für fachliche Ist-Evaluation

Nur bereitgestellte zulässige Daten lesen. Kein Rendererzwang für eine
Teilprüfung. check-input (Alias check-course) prüft nur Eingangslesbarkeit,
keine operativen Kursregeln.

## Vorschau aus der gespeicherten Datei

Der mitgelieferte unveränderte bpmn-js-Viewer 18.3.1 liest BPMN samt DI.
Der gemeinsame Aufruf nutzt bereits vorhandenes Node.js, Playwright und sharp
sowie einen vorhandenen Chromium-Browser. Nichts automatisch installieren oder
herunterladen. Vorhandene Laufzeitübersicht zuerst verwenden. `--packages` ist
der tatsächlich gefundene node_modules-Ordner. Browser als `--channel msedge`,
`--channel chrome` oder vorhandene Datei über `--browser ABS_BROWSER` wählen.
Ohne Browseroption verwendet Playwright seinen bereits installierten Chromium.

```text
node ABS_PAKET/00_SYSTEM/tools/render_bpmn.cjs --input ABS_MODELL.bpmn --output ABS_NEUER_VORSCHAUORDNER --packages ABS_NODE_MODULES --channel msedge --environment UMGEBUNG --approved-environment UMGEBUNG
```

Bei mehreren BPMNDiagram-Einträgen zusätzlich `--diagram-id ID` angeben und
weitere benötigte Diagramme separat rendern. Kein stiller Vollständigkeitsanspruch.
Der neue Ausgabeordner enthält SVG, PNG und Herkunftsprotokoll mit Quellhash,
Diagramm-ID, Renderer-/Browserversion, Importwarnungen und Bildhashes.
Die BPMN-Datei bleibt unverändert. Nach jeder XML-/DI-Änderung neu rendern.
Nur nach Rückleseabgleich dieser Hashes Modell und Vorschau zusammen verlinken.

Die Vorschau tatsächlich ansehen, bevor die Lesbarkeit oder Darstellung
bewertet wird. Die Eingangs-BPMN bleibt unverändert. Keine Erzeugungsrunden,
Modellkorrekturen oder nativen Ausführbarkeitsprüfungen.

Fehlen Voraussetzungen, `RENDERER_UNAVAILABLE` konkret nennen, visuelle Prüfung
offen lassen und Export derselben Datei aus dem Zielwerkzeug verwenden.
Keine eigenen BPMN-Zeichner, unabhängig festgelegten Bildkoordinaten oder eigenen
SVG-Rasterizer als Ersatz. Windows, Intel-Mac und Apple-Silicon-Mac sind Zielgruppen;
vorhandene Browser-/Node-Bibliotheken müssen zur tatsächlichen Architektur passen.
Mac-Ausführung ist bisher nicht praktisch nachgewiesen.

## Herkunft

Wiederverwendung des lokalen Vorprüfwegs aus OPS-008, nun ohne fallspezifische
Koordinaten oder Rückschreiben der XML. bpmn-js wird unverändert mit Lizenz und
Hash unter `renderer/` geliefert. Das bpmn.io-Wasserzeichen im Viewer bleibt
sichtbar; Standardexport durch dessen saveSVG-API. Playwright/sharp und Browser
werden aus der vorhandenen Umgebung verwendet und sind nicht im Paket enthalten.
