# Einordnung 0.3.0

Nur optionale lokale Speicherung. Fachlicher Gegenstand: Syntax, Semantik und
Pragmatik; keine betriebliche Realitätstreue- oder Vollständigkeitsprüfung.
Das Schema sichert Struktur und Zuordnung, es bewertet keine Freitextaussagen. Der neue Fachvertrag gilt; historische
OPS-Bezüge beschreiben die Herkunft des neutralen Kerns. Quellenbelege liegen
für Hashsicherung ebenfalls unter modelle/<Fassung>/. Kein Fremdprofilimport,
keine Modellerzeugung oder Ausführbarkeitsprüfung. Fachliche Evaluation ohne
diese Laufzeit fortsetzen.

# Begrenzte BPMN-Speicherableitung 0.1.0

Neutraler Speicherbaustein für OPS-008. Der Code bleibt bei 0.1.0;
diese Anleitung ist für den Paketstart 0.1.1 angepasst. Verbindlicher Einstieg
und Kompatibilitätsmatrix: LOKALER_START.md. Python 3.12.14/jsonschema 4.26.0
ist die geprüfte Windows-Kombination. Kein Node-Adapter. Keine Installation
durch den Adapter, kein Netzbedarf und keine privaten Runtimepfade im Ergebnis.

## Herkunft und Umfang

Architekturreferenz: System v0.5.1-pilot, Commit
`70b3eb453479cb8e15c27f92a59b35760204b3b7`.
`neutral_io.py` übernimmt daraus gezielt striktes JSON, SHA-256, Pfad-/
Linkprüfung, WriterLock, einzelne atomare Dateiersetzung und begrenztes
JSON-Patch. `save_state.py` leitet den bestehenden Kandidaten-/Basishash- und
Revisionsablauf ab, ergänzt Artefaktprüfung und Abbruchjournal. Keine 22 Fragen,
System-IDs oder BPMN-Modellerzeugung. Publizierte Quellpakete bleiben unverändert.

## Einbindung und vertrauenswürdiger Fachvertrag

OPS-008 übernimmt `save_state.py`, `neutral_io.py` und `requirements.txt` nach
`00_SYSTEM/tools/`. Daneben liefert OPS-008 **bpmn_contract.py** und unter
`00_SYSTEM/schemas/output_schema.json` das echte Fachschema. Die synthetischen
Fixtures in tests/bpmn_storage sind kein auslieferbarer Fachvertrag.

Schema: Draft 2020-12, nur dokumentinterne #/$ref und #/$dynamicRef.
Externe Referenzen werden vor Validierung abgelehnt. Hook/Schema sind geprüfter
Paketcode; niemals einen aus eigenen Unterlagen gelieferten Hook ausführen.
Der Hook muss rein prüfen/projizieren, ohne Dateien zu schreiben oder externe
Programme/Netzwerk aufzurufen. Die Python-API ist keine Sandbox für Fremdcode.

Abgestimmt mit OPS-008 am 12.09.:

```python
CONTRACT_ID = "m1_bpmn_ist_evaluation/0.3.0"
def validate(state):
    # [] oder [{"code": "...", "path": "/...", "message": "..."}]
    ...
def artifact_refs(state):
    # Alle aktuellen Referenzen, nicht nur das erste Bild:
    # [{"artifact_id": "...", "path": "03_ARBEITSSTAND/modelle/r1/modell.bpmn",
    #   "sha256": "64 hexadezimale Zeichen"}]
    ...
```

Fachhook verantwortet vollständiges Register, unveränderliche Dateifassungen,
XML-/Rollenbezüge, Modellrevision und Bildherkunft. Der Kern verlangt nur ein
State-Objekt mit nichtleerem unveränderlichem `case_ref` und positiver `revision`.
Revision wird bei prepare/patch auf 1 bzw. vorherige +1 gesetzt. Alle anderen
Felder gehören OPS-008. Unterschiedliche Fachverträge erhalten andere CONTRACT_IDs;
Schema-/Hookänderungen nicht heimlich unter gleichem Vertragsstand austauschen.

Referenzen haben genau artifact_id/path/sha256. IDs und Pfade sind eindeutig;
Pfade relativ mit `/`, unter `03_ARBEITSSTAND/modelle/<Revision>/...`, ohne
Ausbruch oder symbolische Links/Junctions. Hashes prüfen tatsächliche Bytes.
Mehrere Modelle/Bilder sowie leere Listen sind technisch möglich; der Fachhook
entscheidet, ob der konkrete bildlose Teilstand zulässig ist. Eine referenzierte
fehlende Datei wird niemals übersprungen. Der Kern schreibt keine Artefakte.
Quellenregister unter 02_EIGENE_UNTERLAGEN ist ausdrücklich nicht dieser Prüfumfang.

## Aufrufe und Datenschutz

Vorhandene lokale Fallordner 03_ARBEITSSTAND und 04_UEBERGABE voraussetzen.
Starter ermittelt tatsächliche Laufzeit; keine automatische Installation.
Alle CLI-Aktionen über den isolierten gemeinsamen Einstieg ausführen.

```text
python -I -S 00_SYSTEM/tools/run_local.py probe --project ABS_FALLORDNER
python -I -S 00_SYSTEM/tools/run_local.py status --project ABS_FALLORDNER --environment UMGEBUNG --approved-environment UMGEBUNG
python -I -S 00_SYSTEM/tools/run_local.py prepare --project ABS_FALLORDNER --request-file 03_ARBEITSSTAND/.speichern/prepare.json --environment UMGEBUNG --approved-environment UMGEBUNG
```

patch/commit analog mit eigener Request-Datei. Alle Request- und darin benannten
Markdownpfade relativ zum Fallordner; keine Inhalte in der Befehlszeile.
`probe` liest nur vertrauenswürdigen Vertrag und neutrale Testdateien, keine
Requests, Arbeitsstände oder eigenen Unterlagen. Vor allen anderen Aktionen
verlangt die CLI gleiche nichtleere environment/approved-environment-Werte.
Dies ist eine explizite Zusicherung des Starters, keine selbst ermittelte
Datenschutzfreigabe. Starter muss vorher menschliche, umgebungsbezogene Freigabe
prüfen; nicht blind die beiden Werte füllen. Bestehende gültige Freigabe darf
weitergelten, Umgebungswechsel erneut beurteilen. Vorher auch kein Word-Import.

Nur für interne Integration im Prozess: mit `-I -S` starten, den vertrauenswürdigen
Paket-Werkzeugordner in sys.path aufnehmen und zuerst `local_runtime.activate()`
erfolgreich ausführen. Erst danach `Store(root, trusted_schema_path, trusted_hook_path)`
und ausschliesslich `run(action, request_file, environment=..., approved_environment=...)`.
Interne Methoden umgehen Gates/Lock und sind keine öffentliche Aufrufschnittstelle.

Initialer prepare-Request:

```json
{
  "base_sha256": null,
  "state": {"case_ref": "FALL", "revision": 1},
  "report_file": "03_ARBEITSSTAND/.speichern/bericht.md",
  "handoff_file": "03_ARBEITSSTAND/.speichern/handoff.md"
}
```

State hier absichtlich nur neutraler Ausschnitt, kein gültiges BPMN-Beispiel.
Fortsetzung: statt state eine `ops`-Liste mit add/replace/remove/test gegen
State-Pfade, dazu tatsächlicher base_sha256 aus status. Initialer Vollstate
bei vorhandener Revision wird abgelehnt. Markdown muss nichtleer sein.

Kandidat in `03_ARBEITSSTAND/.speicherentwurf.json`:
storage_version, contract_id, base_sha256, base_outputs (Hashes von JSON,
Bericht, Handoff und technischer Receipt), state, report_markdown,
handoff_markdown, artifact_refs. prepare ist kein gespeicherter Abschluss.
Ungültiger State wird vor Kandidatenerstellung zurückgewiesen.

patch: `{ "candidate_sha256": "...", "ops": [...] }`, nur `/state/...`,
`/report_markdown` oder `/handoff_markdown`. Aktualisierte Kandidatenhashes
verwenden. commit: `{ "candidate_sha256": "..." }`.
Eine neue Vorbereitung überschreibt keinen offenen Kandidaten.

Ergebnisse sind JSON; Exitcode 0 bei ok:true, sonst 2. Bei Fehlern saved:false,
outputs_consistent:false, prior_checks_applicable:false, konkreter code/path.
Erfolg liefert je Aktion current_sha256, candidate_sha256 und revision.
status zeigt offenen Kandidaten getrennt. Bei Fehlern soweit lesbar zusätzlich
observed_current_sha256/observed_revision: nur beobachtet, nicht als gültig bestätigt.
prior_checks_applicable bezeichnet ausschliesslich technische Dateianwendbarkeit,
nicht menschliche/fachliche Prüfung oder visuelle Gleichheit.

## Erneute Prüfung und Abbruchgrenzen

Bei prepare/patch werden Basis und neue Referenzen geprüft. commit prüft sie
frisch vor Veröffentlichung, erneut vor jedem Dateiersetzen und nach Rücklesen.
status prüft aktuellen Stand sowie offenen Kandidaten. Geänderte/fehlende
Artefakte oder auch nur veränderter Handoff-Inhalt verhindern konsistenten Erfolg.
Der bisherige reine Headervergleich ist durch vollständige Ausgabedateihashes
in `.storage-receipt.json` ergänzt. Ein alter JSON-Hash allein genügt nicht.

Fortgeschrieben werden Bericht, Handoff, Receipt und **zuletzt** arbeitsstand.json.
Modell-/Bilddateien bleiben externe, vorher erzeugte versionierte Dateien.
Vor Veröffentlichung wird ein Journal mit alten Dateibytes (Base64) und
geplanten Hashes exklusiv erzeugt; dauerhafte Kopie unter
`03_ARBEITSSTAND/.storage-history/<Transaktions-ID>.json`.
Dieses interne Backup enthält Fallinhalte: gleiche Datenschutz-/Ablageregeln,
nicht ungeprüft veröffentlichen. Keine automatische Löschung alter Backups.

Bei abgefangenem Fehler oder hartem Prozessabbruch kann ein gemischter
Bericht/Handoff/Receipt-Stand bestehen. Vorherige Revision bleibt im Journal/
Backup erhalten; bis zum letzten Austausch auch in arbeitsstand.json.
Ein existierendes `.storage-transaction.json` bedeutet RECOVERY_REQUIRED,
keine Erfolgsmeldung und keine automatische Weiterveröffentlichung.
Nach hartem Abbruch kann zusätzlich `.save.lock` zurückbleiben.

Wiederherstellung ist bewusst nicht automatisiert: beteiligte Schreiber stoppen,
Journal/History und vorhandene Dateien sichern, aktuelle Bytes mit geplanten
Hashes und Backup abgleichen. Entweder den vollständig nachgewiesenen neuen
Stand übernehmen oder den vorherigen Stand aus dem Backup in einer separaten
Prüfkopie herstellen. Fremdänderungen nicht überschreiben. Journal/Lock erst
nach belegtem Ende des Schreibers und abgeschlossener Klärung gezielt entfernen.
Adapter bietet keinen pauschalen Reset-/Force-Schalter. Fehlende/geänderte
Artefakte zunächst aus gesicherten Originalen klären; keine neuen Hashes zum
blossen Verbergen einer Abweichung eintragen.

Der kooperative WriterLock sperrt keine externen Editoren. Zwischen letzter
Hashprüfung und Dateizugriff bleibt ein unvermeidbares Zeitfenster; kein Schutz
gegen böswillige gleichzeitige Manipulation oder Hardwareverlust. Keine
vollatomare Mehrdatei-Transaktion, keine getestete automatische Recovery,
keine Netz-/Cloud-/macOS-/Linux-Garantie. Mehrdatei-Abbruchtests injizieren Fehler,
sie simulieren keinen realen Stromausfall. Versionierte alte Artefakte werden
nicht durch diesen Kern überschrieben, aber auch nicht gegen fremdes Löschen geschützt.

## Nachweise und Integrationsgrenze

Synthetische Tests: `tests/bpmn_storage/test_storage.py` mit ausschliesslich
synthetischem Schema/Hook. Echte OPS-008-Fachintegration bleibt erforderlich.
BPMN-XML/DI, veraltete Bildinhalte trotz passendem Dateihash, Quellenimport und
ADONIS/Camunda sind keine Aussagen dieses neutralen Testlaufs.
Historische System-Befunde F-001/E-001 bleiben separat offen.
