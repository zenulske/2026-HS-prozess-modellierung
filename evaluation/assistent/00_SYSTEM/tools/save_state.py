"""BPMN storage derivation 0.1.0: local references, not model generation."""
from __future__ import annotations

import argparse
import base64
import copy
import importlib.util
import os
from pathlib import Path, PurePosixPath
import re
import secrets
import sys

from neutral_io import (SaveError, WriterLock, apply_patch, ensure_safe_hierarchy,
                        ensure_within, json_bytes, parse_json_bytes, read_file,
                        result, sha256, write_temp_replace)

VERSION = "0.1.0"
HEX = re.compile(r"^[0-9a-fA-F]{64}$")
WORK = "03_ARBEITSSTAND/"
OUTPUTS = (WORK + "arbeitsstand.json", "04_UEBERGABE/berichtsausgabe.md",
           "04_UEBERGABE/HANDOFF.md")
PENDING = WORK + ".speicherentwurf.json"
RECEIPT = WORK + ".storage-receipt.json"
JOURNAL = WORK + ".storage-transaction.json"


def fail(code, message, path=""):
    raise SaveError(code, message, path)


def local_path(root, name):
    if (not isinstance(name, str) or not name or "\\" in name or ":" in name
            or name.startswith("/") or any(p in {"", ".", ".."} for p in name.split("/"))):
        fail("INVALID_PATH", "Use a normalized project-relative POSIX path.", str(name))
    path = root.joinpath(*PurePosixPath(name).parts)
    ensure_within(root, path, name)
    return path


def load_contract(schema_path, hook_path):
    # Both files are trusted package inputs, never supplied by student requests.
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise SaveError("MISSING_DEPENDENCY", "Python jsonschema is unavailable; nothing installed.") from exc
    schema = parse_json_bytes(schema_path.read_bytes(), "/schema")

    def no_remote(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {"$ref", "$dynamicRef"} and (not isinstance(child, str) or not child.startswith("#")):
                    fail("SCHEMA_ERROR", "Only document-local schema references are supported.")
                no_remote(child)
        elif isinstance(value, list):
            for child in value:
                no_remote(child)
    no_remote(schema)
    try:
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        spec = importlib.util.spec_from_file_location("trusted_bpmn_contract", hook_path)
        hook = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(hook)
        if not isinstance(hook.CONTRACT_ID, str) or not hook.CONTRACT_ID:
            fail("CONTRACT_ERROR", "Missing versioned CONTRACT_ID.")
        if not callable(hook.validate) or not callable(hook.artifact_refs):
            fail("CONTRACT_ERROR", "Required contract functions missing.")
        return validator, hook
    except SaveError:
        raise
    except Exception as exc:
        raise SaveError("CONTRACT_ERROR", "Trusted schema/hook could not be loaded.") from exc


class Store:
    def __init__(self, root, schema_path, hook_path):
        self.root = Path(root).absolute()
        ensure_safe_hierarchy(self.root)
        for name in ("03_ARBEITSSTAND", "04_UEBERGABE"):
            path = local_path(self.root, name)
            if not path.is_dir():
                fail("MISSING_DIRECTORY", "Required directory missing.", name)
        self.schema_path, self.hook_path = Path(schema_path), Path(hook_path)
        self.validator = self.hook = None

    def data(self, name, required=False):
        return read_file(local_path(self.root, name), name, required=required)

    def write(self, name, data):
        write_temp_replace(local_path(self.root, name), data)
        if self.data(name, True) != data:
            fail("READBACK_FAILED", "Written bytes differ on readback.", name)

    def create(self, name, data):
        # Exclusive creation: a foreign candidate/journal is never replaced.
        with local_path(self.root, name).open("xb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        if self.data(name, True) != data:
            fail("READBACK_FAILED", "Created file differs on readback.", name)

    def hashes(self):
        return {name: (sha256(data) if (data := self.data(name)) is not None else None)
                for name in (*OUTPUTS, RECEIPT)}

    def check_refs(self, refs):
        if not isinstance(refs, list):
            fail("CONTRACT_ERROR", "artifact_refs must return an array.")
        ids, paths = set(), set()
        for ref in refs:
            if not isinstance(ref, dict) or set(ref) != {"artifact_id", "path", "sha256"}:
                fail("CONTRACT_ERROR", "Reference requires artifact_id, path, sha256.")
            ident, name, expected = ref["artifact_id"], ref["path"], ref["sha256"]
            if not isinstance(ident, str) or not ident or ident in ids:
                fail("ARTIFACT_ID", "Artifact IDs must be nonempty and unique.")
            path = local_path(self.root, name)
            if not name.startswith(WORK + "modelle/") or len(name.split("/")) < 4 or name.casefold() in paths:
                fail("ARTIFACT_PATH", "Unique versioned model paths required.", name)
            if not isinstance(expected, str) or not HEX.fullmatch(expected):
                fail("ARTIFACT_HASH", "Expected SHA-256 must have 64 hex digits.", name)
            actual = read_file(path, name)
            if sha256(actual) != expected.lower():
                fail("ARTIFACT_CHANGED", "Artifact hash differs; prior checks do not apply.", name)
            ids.add(ident)
            paths.add(name.casefold())
        return refs

    def validate(self, state):
        if not isinstance(state, dict) or not isinstance(state.get("case_ref"), str) or not state["case_ref"]:
            fail("INVALID_STATE", "State must have a nonempty case_ref.")
        if type(state.get("revision")) is not int or state["revision"] < 1:
            fail("INVALID_STATE", "Positive integer revision required.")
        try:
            errors = list(self.validator.iter_errors(state))
            if errors:
                fail("SCHEMA_INVALID", "State violates the trusted schema.", "/state")
            frozen = json_bytes(state)
            errors = self.hook.validate(copy.deepcopy(state))
            if not isinstance(errors, list):
                fail("CONTRACT_ERROR", "validate must return an error array.")
            if errors:
                error = errors[0]
                if not isinstance(error, dict) or not all(isinstance(error.get(k), str) for k in ("code", "path", "message")):
                    fail("CONTRACT_ERROR", "Domain errors require string code/path/message.")
                fail(error["code"], error["message"], error["path"])
            refs = self.hook.artifact_refs(copy.deepcopy(state))
            if frozen != json_bytes(state):
                fail("CONTRACT_ERROR", "Contract must not mutate state.")
        except SaveError:
            raise
        except Exception as exc:
            raise SaveError("CONTRACT_ERROR", "Domain validation failed closed.") from exc
        return self.check_refs(refs)

    def current(self):
        raw = self.data(OUTPUTS[0])
        return raw, parse_json_bytes(raw, "/current") if raw is not None else None

    def inspect_current(self):
        if self.data(JOURNAL) is not None:
            fail("RECOVERY_REQUIRED", "Interrupted publication: preserve journal/history and reconcile manually.", JOURNAL)
        raw, state = self.current()
        if state is None:
            if any(self.data(name) is not None for name in (*OUTPUTS[1:], RECEIPT)):
                fail("FOREIGN_OUTPUT", "Outputs exist without an owned state; will not overwrite.")
            return raw, state
        self.validate(state)
        receipt = parse_json_bytes(self.data(RECEIPT, True), "/receipt")
        if receipt.get("contract_id") != self.hook.CONTRACT_ID or receipt.get("storage_version") != VERSION:
            fail("CONTRACT_MISMATCH", "Receipt contract/version mismatch.")
        expected = receipt.get("files")
        if not isinstance(expected, dict) or set(expected) != set(OUTPUTS):
            fail("OUTPUT_INCONSISTENT", "Receipt file inventory invalid.")
        for name in OUTPUTS:
            data = self.data(name, True)
            if sha256(data) != expected[name]:
                fail("OUTPUT_INCONSISTENT", "Owned output changed or incomplete.", name)
        return raw, state

    def pending(self, expected=None):
        raw = self.data(PENDING, True)
        if expected != sha256(raw):
            fail("CANDIDATE_MISMATCH", "Candidate hash differs.")
        env = parse_json_bytes(raw, "/candidate")
        if env.get("storage_version") != VERSION or env.get("contract_id") != self.hook.CONTRACT_ID:
            fail("CONTRACT_MISMATCH", "Candidate contract/version mismatch.")
        return raw, env

    def baseline(self, env):
        hashes = self.hashes()
        if hashes[OUTPUTS[0]] != env["base_sha256"]:
            fail("BASE_MISMATCH", "State baseline changed; no overwrite.")
        if hashes != env["base_outputs"]:
            fail("OUTPUT_CHANGED", "Baseline outputs changed; no overwrite.")
        return self.inspect_current()[1]

    def candidate_state(self, state, previous):
        if not isinstance(state, dict):
            fail("INVALID_STATE", "State must be an object.")
        if previous is not None and state.get("case_ref") != previous["case_ref"]:
            fail("IMMUTABLE_CASE", "case_ref cannot change.")
        state["revision"] = previous["revision"] + 1 if previous else 1
        return self.validate(state)

    def markdown(self, name):
        path = local_path(self.root, name)
        if not name.startswith(WORK + ".speichern/") or path.suffix != ".md":
            fail("INVALID_PATH", "Markdown inputs must be under 03_ARBEITSSTAND/.speichern/.", name)
        text = self.data(name, True).decode("utf-8")
        if not text.strip():
            fail("EMPTY_MARKDOWN", "Markdown must be nonempty.", name)
        return text

    def probe(self):
        # No existing requests, states, artifacts or student data are read here.
        for directory in ("03_ARBEITSSTAND", "04_UEBERGABE"):
            path = local_path(self.root, directory + "/.probe-" + secrets.token_hex(12))
            owned = False
            try:
                with path.open("xb") as stream:
                    owned = True
                    stream.write(b"neutral-probe\n")
                    stream.flush()
                    os.fsync(stream.fileno())
                if path.read_bytes() != b"neutral-probe\n":
                    fail("PROBE_FAILED", "Probe readback differs.")
            finally:
                if owned:
                    path.unlink(missing_ok=True)
        return result(True, [], access_verified=True, validator="jsonschema", storage_version=VERSION)

    def status(self):
        raw, state = self.inspect_current()
        pending = self.data(PENDING)
        if pending is not None:
            _, env = self.pending(sha256(pending))
            self.baseline(env)
            if self.validate(env["state"]) != env["artifact_refs"]:
                fail("MANIFEST_CHANGED", "Candidate reference extraction differs.")
        return result(True, [], current_sha256=sha256(raw) if raw else None,
                      revision=state["revision"] if state else None,
                      candidate_sha256=sha256(pending) if pending else None,
                      outputs_consistent=state is not None,
                      prior_checks_applicable=state is not None)

    def prepare(self, request):
        if "base_sha256" not in request:
            fail("INVALID_REQUEST", "Explicit base_sha256 required, null for initial state.")
        if self.data(PENDING) is not None:
            fail("PENDING_EXISTS", "Existing candidate must be handled explicitly.")
        base = self.hashes()
        if request.get("base_sha256") != base[OUTPUTS[0]]:
            fail("BASE_MISMATCH", "State baseline differs.")
        _, previous = self.inspect_current()
        if (previous is None and ("state" not in request or "ops" in request)) or (
                previous is not None and ("ops" not in request or "state" in request)):
            fail("INVALID_REQUEST", "Initial state or continuation ops required exclusively.")
        state = copy.deepcopy(request["state"]) if previous is None else apply_patch(previous, request["ops"], "state")
        refs = self.candidate_state(state, previous)
        env = dict(storage_version=VERSION, contract_id=self.hook.CONTRACT_ID,
                   base_sha256=base[OUTPUTS[0]], base_outputs=base, state=state,
                   report_markdown=self.markdown(request["report_file"]),
                   handoff_markdown=self.markdown(request["handoff_file"]), artifact_refs=refs)
        self.baseline(env)
        data = json_bytes(env)
        self.create(PENDING, data)
        return result(True, [], saved=False, candidate_sha256=sha256(data), revision=state["revision"])

    def patch(self, request):
        pending_raw, env = self.pending(request.get("candidate_sha256"))
        previous = self.baseline(env)
        env = apply_patch(env, request.get("ops"), "envelope")
        env["artifact_refs"] = self.candidate_state(env["state"], previous)
        for key in ("report_markdown", "handoff_markdown"):
            if not isinstance(env[key], str) or not env[key].strip():
                fail("EMPTY_MARKDOWN", "Candidate Markdown must be nonempty.")
        self.baseline(env)
        data = json_bytes(env)
        if self.data(PENDING, True) != pending_raw:
            fail("CANDIDATE_MISMATCH", "Candidate changed during patch; no overwrite.")
        self.write(PENDING, data)
        return result(True, [], saved=False, candidate_sha256=sha256(data), revision=env["state"]["revision"])

    def commit(self, request):
        pending_raw, env = self.pending(request.get("candidate_sha256"))
        previous = self.baseline(env)
        if env["state"].get("revision") != (previous["revision"] + 1 if previous else 1):
            fail("REVISION_MISMATCH", "Candidate revision does not follow baseline.")
        refs = self.validate(env["state"])
        if refs != env["artifact_refs"]:
            fail("MANIFEST_CHANGED", "Candidate reference extraction differs.")
        state = json_bytes(env["state"])
        head = f'<!-- arbeitsstand-sha256: {sha256(state)}; revision: {env["state"]["revision"]} -->\n\n'
        new = {OUTPUTS[0]: state}
        for name, key in zip(OUTPUTS[1:], ("report_markdown", "handoff_markdown")):
            if not isinstance(env[key], str) or not env[key].strip():
                fail("EMPTY_MARKDOWN", "Candidate Markdown must be nonempty.")
            new[name] = (head + env[key]).encode("utf-8")
        new[RECEIPT] = json_bytes(dict(storage_version=VERSION, contract_id=self.hook.CONTRACT_ID,
                                       files={name: sha256(data) for name, data in new.items()}))
        old = {name: self.data(name) for name in new}
        journal = json_bytes(dict(storage_version=VERSION, candidate_sha256=sha256(pending_raw),
            previous={name: base64.b64encode(data).decode("ascii") if data is not None else None
                      for name, data in old.items()}, planned={name: sha256(data) for name, data in new.items()}))
        self.baseline(env)
        self.check_refs(refs)  # Fresh B-01 check immediately before publication.
        history = local_path(self.root, WORK + ".storage-history")
        history.mkdir(exist_ok=True)
        backup = local_path(self.root, WORK + ".storage-history/" + secrets.token_hex(16) + ".json")
        with backup.open("xb") as stream:
            stream.write(journal)
            stream.flush()
            os.fsync(stream.fileno())
        if backup.read_bytes() != journal:
            fail("READBACK_FAILED", "Recovery backup differs on readback.")
        self.create(JOURNAL, journal)
        # State is published LAST. No automatic rollback over potentially foreign edits.
        for name in (*OUTPUTS[1:], RECEIPT, OUTPUTS[0]):
            self.check_refs(refs)
            if self.data(name) != old[name] or self.data(PENDING, True) != pending_raw:
                fail("OUTPUT_CHANGED", "File changed during publication; recovery required.", name)
            self.write(name, new[name])
        for name, data in new.items():
            if self.data(name, True) != data:
                fail("READBACK_FAILED", "Publication readback failed; recovery required.", name)
        self.check_refs(refs)
        if self.data(PENDING, True) != pending_raw:
            fail("CANDIDATE_MISMATCH", "Candidate changed during publication.")
        local_path(self.root, PENDING).unlink()
        local_path(self.root, JOURNAL).unlink()
        return result(True, [], saved=True, current_sha256=sha256(state),
                      revision=env["state"]["revision"], outputs_consistent=True,
                      prior_checks_applicable=True)

    def run(self, action, request_file=None, *, approved_environment=None, environment=None):
        try:
            if action != "probe" and (not environment or approved_environment != environment):
                fail("PRIVACY_REQUIRED", "Confirm valid approval for this environment before reading contents.")
            self.validator, self.hook = load_contract(self.schema_path, self.hook_path)
            if action == "probe":
                return self.probe()
            with WriterLock(local_path(self.root, WORK + ".save.lock")):
                if action == "status":
                    return self.status()
                if action not in {"prepare", "patch", "commit"}:
                    fail("INVALID_ACTION", "Unsupported action.")
                request = parse_json_bytes(self.data(request_file, True), "/request")
                if not isinstance(request, dict):
                    fail("INVALID_REQUEST", "Request must be an object.")
                return getattr(self, action)(request)
        except SaveError as exc:
            output = result(False, [exc], outputs_consistent=False, prior_checks_applicable=False)
            if action == "status" and environment and approved_environment == environment:
                # Observed metadata only: never call this a valid or checked revision.
                try:
                    raw, state = self.current()
                    pending = self.data(PENDING)
                    output.update(observed_current_sha256=sha256(raw) if raw else None,
                                  observed_revision=state.get("revision") if isinstance(state, dict) else None,
                                  observed_candidate_sha256=sha256(pending) if pending else None,
                                  recovery_required=self.data(JOURNAL) is not None)
                except Exception:
                    output["observed_metadata_unavailable"] = True
            return output
        except (OSError, UnicodeError) as exc:
            return result(False, [SaveError("IO_ERROR", "Local I/O failed; inspect status and recovery journal.")],
                          outputs_consistent=False, prior_checks_applicable=False)
        except Exception:
            return result(False, [SaveError("CONTRACT_ERROR", "Invalid request or contract; operation failed closed.")],
                          outputs_consistent=False, prior_checks_applicable=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["probe", "status", "prepare", "patch", "commit"])
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--request-file", help="Project-relative request path")
    parser.add_argument("--environment")
    parser.add_argument("--approved-environment")
    args = parser.parse_args()
    try:
        here = Path(__file__).resolve().parent
        store = Store(args.project, here.parent / "schemas/output_schema.json", here / "bpmn_contract.py")
        output = store.run(args.action, args.request_file, environment=args.environment,
                           approved_environment=args.approved_environment)
    except (SaveError, OSError) as exc:
        output = result(False, [exc if isinstance(exc, SaveError) else SaveError("IO_ERROR", "Project unavailable.")])
    print(json_bytes(output).decode("utf-8"), end="")
    return 0 if output["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
