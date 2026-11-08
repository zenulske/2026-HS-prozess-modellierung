# Evaluation und optionale Speicherung

Die fachliche Evaluation beginnt mit vorhandenen Uploads und folgt
ARBEITSWEISE.md. Kein lokaler Speicher- oder Pythonzwang. Ohne geeignete
Umgebung Bericht im Gespräch ausgeben, Grenzen nennen und dort fortsetzen.

## Lokale Speicherung

Nur bei gewünschter lokaler Sicherung und tatsächlichem Zugriff. Vorher
tools/LOKALER_START.md und tools/INTEGRATION.md lesen. Vertrauenswürdiges Schema
output_schema.json und Hook bpmn_contract.py verwenden. Neue Kennung:
m1_bpmn_ist_evaluation/0.3.0. Keine automatische Migration oder Überschreibung
alter Modellierungsstände. Neuen Fallordner benutzen; alte Dateien erhalten.

Neutrale probe über python -I -S tools/run_local.py; danach bei tatsächlich
gültiger Umgebungsfreigabe status. environment/approved-environment sind deren
Dokumentation, kein Ersatz. Keine Abhängigkeiten automatisch installieren.
Fehlende CPython-3.12-Laufzeit verhindert nur lokale Speicherung.

1. Unveränderte Eingänge und Belegkopien unter
   03_ARBEITSSTAND/modelle/<Fassung>/ ablegen; frühere Fassungen erhalten.
   Hier dürfen auch freiwillige Kontextbelege liegen. Keine Modelle ändern.
2. Schema-konformen Evaluationsstand mit Kontext, Quellen, Modellzuordnung,
   issues, checks und continuation erstellen. issues enthalten dimension
   (syntax/semantics/pragmatics), rule_kind und rule_reference. checks erfassen die
   Abdeckung mit kind syntax/semantics/pragmatics; visual und input_integrity sind
   getrennte Hilfsprüfungen. status ist not_checked/partial/checked/not_assessable,
   kein Qualitätsurteil. Geprüfte Dimensionen mit Mängeln bleiben checked; Befunde
   stehen in issues. Ein Teilstand darf offene Dimensionen enthalten; im Bericht
   alle drei mit ihrer tatsächlichen Abdeckung ausweisen. Kein source_alignment. Hashes auf tatsächliche Bytes
   beziehen. Quellenartefakte werden ebenso gegen Änderungen abgesichert.
3. Schema und bpmn_contract.validate prüfen, dann inspect_models als getrennte
   Lese-/Zuordnungsprüfung verwenden. Deren Befunde sind Prüfgrenzen, keine
   fachlichen Mängel. Defekte BPMN darf als Eingangsbeleg gespeichert werden;
   checks/limitations müssen die tatsächlichen Grenzen benennen.
4. Bildzuordnung nur nach tatsächlichem Inhaltsvergleich bestätigen.
   Fehlt XML/Bild oder ist die Zuordnung unklar: Prüfgrenze dokumentieren.
   Keine Sichtprüfung aus Hash oder Rendererfolg ableiten.
5. Bericht und Handoff als Markdown-Stagingdateien schreiben. prepare mit
   aktuellem Basishash; gegebenenfalls patch. Schema/Hook prüfen den Kandidaten.
   Relative Dokumentlinks mit check-links unter dem späteren Zielpfad prüfen:
   --document 03_ARBEITSSTAND/.speichern/bericht.md
   --base-document 04_UEBERGABE/berichtsausgabe.md (analog für HANDOFF.md).
6. commit mit aktuellem Kandidatenhash. Nur saved:true ist Speichererfolg.
   Danach status, Rücklesen und Links der gespeicherten Ausgaben prüfen.
   Bei Fehlern keine Journale löschen, keine alten Prüfungen als aktuell ausgeben.

Der neutrale Kern prüft Schema, Hook, Artefakthashes und Speicherbeziehungen.
Er erzwingt keine vollständige fachliche oder visuelle Evaluation. inspect_models
ist eine getrennte Python-API, kein CLI-Befehl. Es wird keine technische
Ausführbarkeit oder vollständige OMG-Konformität geprüft. Chat-Evaluationen
ohne lokale Sicherung benötigen keinen künstlichen JSON-Arbeitsstand.
