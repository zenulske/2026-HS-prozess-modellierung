# Optionaler lokaler Speicherstart – Evaluation 0.3.0

Nur optionale Speicheraktionen laufen über diesen Einstieg.
Die fachliche Evaluation benötigt diese Laufzeit nicht.
Der neutrale Speichercode bleibt unverändert; seine Anleitung ist auf den
folgenden isolierten Einstieg angepasst. Parameter und Fehlerbehandlung
bleiben gültig; Original- und angepasster Dokumenthash sind festgehalten.

## Aufruf

Vorhandenes Python ermitteln (gegebenenfalls über die Laufzeitübersicht des
KI-Werkzeugs); keinen persönlichen Pfad fest eintragen und nichts installieren.
Bei einem ungeeigneten ersten Treffer (etwa 3.14) die vorhandene Laufzeitübersicht
und weitere bekannte Interpreter prüfen; nicht sofort die Umgebung insgesamt
als unbrauchbar melden. Version und Prozessarchitektur abfragen, passenden
CPython-3.12-Interpreter wählen, keine rekursive Suche durch eigene Unterlagen.
`python` bezeichnet nachfolgend diesen tatsächlich gefundenen Interpreter.

```text
python -I -S 00_SYSTEM/tools/run_local.py probe --project ABS_FALLORDNER
python -I -S 00_SYSTEM/tools/run_local.py status --project ABS_FALLORDNER --environment UMGEBUNG --approved-environment UMGEBUNG
python -I -S 00_SYSTEM/tools/run_local.py prepare --project ABS_FALLORDNER --request-file 03_ARBEITSSTAND/.speichern/prepare.json --environment UMGEBUNG --approved-environment UMGEBUNG
python -I -S 00_SYSTEM/tools/run_local.py check-links --project ABS_FALLORDNER --document 03_ARBEITSSTAND/.speichern/bericht.md --base-document 04_UEBERGABE/berichtsausgabe.md --document 03_ARBEITSSTAND/.speichern/handoff.md --base-document 04_UEBERGABE/HANDOFF.md --environment UMGEBUNG --approved-environment UMGEBUNG
python -I -S 00_SYSTEM/tools/run_local.py check-links --project ABS_FALLORDNER --document 04_UEBERGABE/berichtsausgabe.md --document 04_UEBERGABE/HANDOFF.md --environment UMGEBUNG --approved-environment UMGEBUNG
```

patch/commit analog. Absolute Werkzeugpfade verwenden, falls das aktuelle
Arbeitsverzeichnis nicht der Paketordner ist. `-I -S` sind verpflichtend:
keine Umgebungs-Pythonpfade, Benutzerbibliotheken oder site-Startskripte laden.
Der Einstieg lädt ausschliesslich die mitgelieferten geprüften Abhängigkeiten.
Keine Änderung an globaler Laufzeit, keine Entpackung oder Installation beim
Start und kein Netzabruf. Fehlende/beschädigte Bibliotheken führen zum Abbruch,
auch wenn zufällig anderswo eine Bibliothek vorhanden ist.

Erst probe; keine eigenen Unterlagen oder Arbeitsstände lesen, bevor gültige
menschliche Datenschutzfreigabe vorliegt. Gleiche CLI-Umgebungswerte sind nur
deren Dokumentation. Die bisherigen Datenschutzregeln gelten vollständig.

## Kompatibilität und Nachweisgrenzen

Standard-CPython 3.12 mit GIL wird benötigt. Python selbst ist nicht enthalten.

| Umgebung | Bereitstellung | Nachweis |
|---|---|---|
| Windows x86-64, CPython 3.12 | Mitgelieferter nativer Satz | Lokaler Reparaturtest mit 3.12.14; unabhängiger Erststart noch ausstehend |
| macOS Intel x86-64, CPython 3.12 | Passender Wheel-Satz vorbereitet | Nicht auf macOS ausgeführt; kein Funktionsnachweis |
| macOS Apple Silicon arm64, CPython 3.12 | Passender Wheel-Satz vorbereitet | Nicht auf macOS ausgeführt; kein Funktionsnachweis |
| Andere Python-Versionen, Architekturen oder Betriebssysteme | In diesem Pilotpaket nicht bereitgestellt | Nicht geprüft; kontrollierter Abbruch, nicht automatisch installieren |

Björn hat Windows und Macs verschiedener Generationen als Zielgruppe bestätigt:
Intel und Apple Silicon sind beide zu berücksichtigen. Beide Mac-Sätze sind
enthalten; ihre native Prüfung bleibt vor einer entsprechenden Freigabe offen.
Windows-Prüfungen sind ausdrücklich keine macOS-Nachweise. Auf jedem Mac beim
Erststart die tatsächlich vorhandene Python-Version und Prozessarchitektur
feststellen. Bei unpassender Umgebung die konkrete Kombination Björn melden;
keine Installation und keine Behauptung, Mac-Nutzung sei generell ausgeschlossen.
Die Bereitstellung setzt derzeit CPython 3.12 voraus; dessen Verfügbarkeit auf
den studentischen Macs ist noch nicht belegt.

## Herkunft und Lizenzen

`../vendor/LOCK.json` enthält exakte Versionen, PyPI-Quelladressen, SHA-256,
Anforderungen und Lizenzpfade. Alle unveränderten Wheels enthalten METADATA,
WHEEL, RECORD und die originalen Lizenztexte; der native Satz ist zusätzlich
bereits entpackt. Die Wheels sind ZIP-Archive. Keine Entwickler-Tempbibliothek
ist Grundlage oder Voraussetzung der Lieferung.

| Bibliothek | Version | Lizenz laut Distribution |
|---|---|---|
| jsonschema | 4.26.0 | MIT |
| attrs | 25.4.0 | MIT |
| jsonschema-specifications | 2025.9.1 | MIT |
| referencing | 0.37.0 | MIT |
| rpds-py | 0.30.0 | MIT |
| typing-extensions | 4.15.0 | PSF-2.0 |
| rfc3339-validator | 0.1.4 | MIT |
| six | 1.17.0 | MIT |

Die direkten und transitiven Pflichtabhängigkeiten sind vollständig fixiert.
rfc3339-validator und six ergänzen die in den vorhandenen Importschemas
verwendete date-time-Prüfung; weitere Format-Extras werden nicht benötigt.
Massgeblich sind die mitgelieferten vollständigen Lizenztexte mit Copyright-
Hinweisen. Das Hashmanifest erkennt fehlende/abweichende Paketdateien, ist aber
keine digitale Signatur gegen einen vollständigen Austausch des Pakets.
