"""Check local Markdown links relative to each document; no writes."""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import unquote

LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
WINDOWS_ABSOLUTE = re.compile(r"^[A-Za-z]:[/\\]")


def check_document(project, document, base_document=None):
    from neutral_io import ensure_within, read_file, SaveError
    from save_state import local_path

    doc = local_path(project, document)
    final_doc = local_path(project, base_document or document)
    raw = read_file(doc, document, required=True)
    text = raw.decode("utf-8")
    findings = []
    checked = []
    for match in LINK.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        target = unquote(target.split("#", 1)[0])
        if not target or target.startswith("#"):
            continue
        if target.startswith(('/', '\\')) or WINDOWS_ABSOLUTE.match(target):
            findings.append(dict(code="DOCUMENT_LINK_ABSOLUTE", document=document,
                                 target=target,
                                 message="Lokaler Dokumentlink muss relativ zum Dokumentverzeichnis sein."))
            continue
        if SCHEME.match(target):
            continue
        candidate = (final_doc.parent.joinpath(*PurePosixPath(target).parts)).resolve()
        try:
            ensure_within(project, candidate, target)
            read_file(candidate, target, required=True)
            checked.append(dict(content_document=document,
                                document=base_document or document, target=target,
                                resolved=candidate.relative_to(project).as_posix()))
        except (SaveError, OSError) as exc:
            findings.append(dict(code="DOCUMENT_LINK_MISSING", document=document,
                                 target=target, message=str(exc)))
    return checked, findings


def main(argv):
    from neutral_io import ensure_safe_hierarchy, SaveError
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--document", action="append", required=True)
    parser.add_argument("--base-document", action="append",
                        help="Final document location used as link base; repeat with --document.")
    parser.add_argument("--environment")
    parser.add_argument("--approved-environment")
    args = parser.parse_args(argv)
    try:
        if not args.environment or args.environment != args.approved_environment:
            raise ValueError("PRIVACY_REQUIRED: tatsächliche menschliche Umgebungsfreigabe erforderlich.")
        root = args.project.absolute()
        ensure_safe_hierarchy(root)
        bases = args.base_document or args.document
        if len(bases) != len(args.document):
            raise ValueError("Each --document needs exactly one --base-document.")
        checked, findings = [], []
        for document, base_document in zip(args.document, bases):
            good, bad = check_document(root, document, base_document)
            checked.extend(good)
            findings.extend(bad)
        result = dict(ok=not findings,
                      scope="Lokale Markdown-Links relativ zum jeweiligen Dokumentverzeichnis.",
                      checked=checked, findings=findings)
    except SaveError as exc:
        result = dict(ok=False, error=dict(code=exc.code, path=exc.path,
                                           message=exc.message),
                      checked=[], findings=[])
    except (ValueError, OSError, UnicodeError) as exc:
        result = dict(ok=False, error=dict(code="LINK_CHECK_FAILED", path="",
                                           message=str(exc)),
                      checked=[], findings=[])
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main(None))
