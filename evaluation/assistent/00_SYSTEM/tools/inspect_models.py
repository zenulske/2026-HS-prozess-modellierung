"""Read-only input diagnostics; these are evaluation limits, not domain errors."""
import hashlib
import xml.etree.ElementTree as ET
from save_state import local_path
from neutral_io import SaveError, read_file

BPMN = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
DI = "{http://www.omg.org/spec/BPMN/20100524/DI}"


def inspect_models(root, state):
    """After schema/hook checks. Diagnostics never repair or reject source content."""
    findings = []
    artifacts = {a["artifact_id"]: a for a in state["artifacts"]}

    def add(code, path, message):
        findings.append(dict(code=code, path=path, message=message,
                             category="evaluation_limit"))

    for model in state["models"]:
        aid = model["bpmn_artifact_id"]
        if aid is None:
            add("NO_XML", model["model_id"], "Nur Export: XML-Zuordnung und Elementtypen begrenzt prüfbar.")
            continue
        artifact = artifacts[aid]
        path = artifact["path"]
        try:
            raw = read_file(local_path(root, path), path, required=True)
            if hashlib.sha256(raw).hexdigest() != artifact["sha256"]:
                add("INPUT_CHANGED", path, "Andere Fassung: frühere Prüfung nicht übernehmen.")
                continue
            if b"<!DOCTYPE" in raw.upper() or b"<!ENTITY" in raw.upper():
                add("XML_DECLARATION", path, "DTD/Entity-Deklarationen werden nicht verarbeitet.")
                continue
            xml = ET.fromstring(raw)
            if xml.tag != BPMN + "definitions":
                add("BPMN_ROOT", path, "Kein lesbarer BPMN-Eingang; vorhandenen Export verwenden.")
                continue
            elements = [e for e in xml.iter() if e.get("id")]
            by_id = {e.get("id"): e for e in elements}
            if len(elements) != len(by_id):
                add("AMBIGUOUS_ID", path, "Elementzuordnung über IDs nicht eindeutig.")
            if not xml.findall(DI + "BPMNDiagram"):
                add("NO_PREVIEW_DI", path, "Vorschau aus XML nicht verfügbar; keine fachliche Abwertung.")
            for e in elements:
                if e.tag.startswith(BPMN):
                    for attr in ("sourceRef", "targetRef", "processRef", "attachedToRef"):
                        if e.get(attr) and e.get(attr) not in by_id:
                            add("UNRESOLVED_REFERENCE", path, f"Anschluss bei {e.get('id')} nicht zuordenbar.")
            for issue in state["issues"]:
                if issue["model_id"] == model["model_id"] and any(i not in by_id for i in issue["element_ids"]):
                    add("ISSUE_LOCATION", path, "Befund-ID nicht vorhanden; sichtbare Fundstelle abgleichen.")
        except (SaveError, OSError, ET.ParseError, ValueError) as exc:
            add("INPUT_READ", path, str(exc))
    return findings
