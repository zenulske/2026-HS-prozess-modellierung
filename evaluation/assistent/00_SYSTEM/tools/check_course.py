"""Legacy command name: read-only evaluation input check, no operative course rules."""
import argparse
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

BPMN = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"


def check_bytes(raw):
    if b"<!DOCTYPE" in raw.upper() or b"<!ENTITY" in raw.upper():
        raise ValueError("DTD/Entity-Deklarationen werden nicht verarbeitet.")
    xml = ET.fromstring(raw)
    if xml.tag != BPMN + "definitions":
        raise ValueError("Keine BPMN-definitions.")
    return dict(ok=True, source_sha256=hashlib.sha256(raw).hexdigest(),
                scope="Nur Eingangslesbarkeit; keine fachliche Bewertung oder Ausführbarkeitsprüfung.",
                findings=[])


def main(argv):
    from neutral_io import ensure_safe_hierarchy, read_file, SaveError
    from save_state import local_path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--environment")
    parser.add_argument("--approved-environment")
    args = parser.parse_args(argv)
    try:
        if not args.environment or args.environment != args.approved_environment:
            raise ValueError("PRIVACY_REQUIRED: tatsächliche Umgebungsfreigabe erforderlich.")
        root = args.project.absolute()
        ensure_safe_hierarchy(root)
        result = check_bytes(read_file(local_path(root, args.source), args.source, required=True))
    except (ValueError, OSError, ET.ParseError, SaveError) as exc:
        result = dict(ok=False, category="evaluation_limit", error=str(exc))
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["ok"] else 2
