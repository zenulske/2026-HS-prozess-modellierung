"""Offline, hash-checked vendor loading for the trusted package entry point."""
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys
import sysconfig


class RuntimeUnavailable(Exception):
    def __init__(self, code, message):
        self.code = code
        super().__init__(message)


def activate():
    if not (sys.flags.isolated and sys.flags.no_site):
        raise RuntimeUnavailable("ISOLATION_REQUIRED", "Start with Python -I -S; no external libraries are used.")
    if (sys.implementation.name != "cpython" or sys.version_info[:2] != (3, 12)
            or sysconfig.get_config_var("Py_GIL_DISABLED")):
        raise RuntimeUnavailable("UNSUPPORTED_RUNTIME", "This candidate requires standard CPython 3.12; no installation performed.")
    machine = platform.machine().lower()
    target = {("Windows", "amd64"): "win_amd64", ("Windows", "x86_64"): "win_amd64",
              ("Darwin", "x86_64"): "macosx_10_12_x86_64",
              ("Darwin", "arm64"): "macosx_11_0_arm64"}.get((platform.system(), machine))
    root = Path(__file__).resolve().parent.parent / "vendor"
    try:
        lock = json.loads((root / "LOCK.json").read_text(encoding="utf-8"))
        if lock["lock_version"] != 1 or not target or not any(e["target"] == target for e in lock["entries"]):
            raise RuntimeUnavailable("UNSUPPORTED_RUNTIME", "No bundled validator for this operating system/architecture.")
        entries = [e for e in lock["entries"] if e["target"] in ("common", target)]
        if {e["name"]: e["version"] for e in entries} != lock["pins"]:
            raise RuntimeUnavailable("VENDOR_INVALID", "Incomplete dependency manifest.")
        for entry in entries:
            for item in [entry] + entry["extracted"]:
                path = root / item["path"]
                if (not path.resolve().is_relative_to(root.resolve()) or path.is_symlink()
                        or hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]):
                    raise RuntimeUnavailable("VENDOR_INVALID", "Bundled dependency missing or modified: " + item["path"])
        # Native code must be extracted at build time; pure wheels are zip-imported.
        paths = [str(root / "native" / target)] + [str(root / e["path"]) for e in entries if e["target"] == "common"]
        sys.path[:0] = paths
        for entry in entries:
            if importlib.metadata.version(entry["name"]) != entry["version"]:
                raise RuntimeUnavailable("VENDOR_INVALID", "Bundled distribution version mismatch.")
        from jsonschema import Draft202012Validator, FormatChecker
        checker = FormatChecker()
        if "date-time" not in checker.checkers or checker.conforms("not-a-date", "date-time"):
            raise RuntimeUnavailable("VENDOR_INVALID", "Required date-time validator unavailable.")
        Draft202012Validator.check_schema({"type": "object"})
        return {"target": target, "python": platform.python_version(), "jsonschema": lock["pins"]["jsonschema"],
                "vendor_verified": True}
    except RuntimeUnavailable:
        raise
    except (OSError, ImportError, ValueError, KeyError, TypeError) as exc:
        raise RuntimeUnavailable("VENDOR_INVALID", "Bundled validator cannot be loaded; restore the complete package. Nothing installed.") from exc
