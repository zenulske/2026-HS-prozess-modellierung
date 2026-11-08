"""One isolated offline entry point for storage and trusted source validation."""
import json
from pathlib import Path
import sys


def error(code, message):
    print(json.dumps({"ok": False, "saved": False, "outputs_consistent": False,
                      "prior_checks_applicable": False,
                      "errors": [{"code": code, "path": "", "message": message}]}))
    return 2


def main():
    # Require flags before importing any adjacent or third-party module.
    if not (sys.flags.isolated and sys.flags.no_site):
        return error("ISOLATION_REQUIRED", "Use Python -I -S 00_SYSTEM/tools/run_local.py ...")
    sys.dont_write_bytecode = True
    here = Path(__file__).resolve().parent
    sys.path.insert(0, str(here))
    from local_runtime import activate, RuntimeUnavailable
    try:
        runtime = activate()
    except RuntimeUnavailable as exc:
        return error(exc.code, str(exc))
    if len(sys.argv) > 1 and sys.argv[1] in {"check-input", "check-course"}:
        from check_course import main as check
        return check(sys.argv[2:])
    if len(sys.argv) > 1 and sys.argv[1] == "check-links":
        from check_links import main as check
        return check(sys.argv[2:])
    if len(sys.argv) > 1 and sys.argv[1] == "runtime":
        print(json.dumps({"ok": True, **runtime}))
        return 0
    import save_state
    return save_state.main()


if __name__ == "__main__":
    sys.exit(main())
