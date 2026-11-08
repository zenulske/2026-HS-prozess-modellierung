"""Narrow neutral helpers extracted from System 0.5.1-pilot, commit 70b3eb4.
No system-specific validation or model generation. See INTEGRATION.md.
"""
from __future__ import annotations
import copy
import hashlib
import json
import os
import secrets
import stat
from pathlib import Path
from typing import Any, Iterable

class SaveError(Exception):
    def __init__(self, code: str, message: str, path: str = "") -> None:
        super().__init__(message)
        self.code, self.message, self.path = code, message, path

class RequestError(SaveError):
    pass

def error_obj(error: SaveError | tuple[str, str, str]) -> dict[str, str]:
    if isinstance(error, SaveError):
        return {"path": error.path, "code": error.code, "message": error.message}
    path, code, message = error
    return {"path": path, "code": code, "message": message}

def result(ok: bool, errors: Iterable[SaveError | tuple[str, str, str]], **extra: Any) -> dict[str, Any]:
    payload = {"ok": ok, "errors": [error_obj(e) for e in errors], **extra}
    if not ok:
        payload.setdefault("saved", False)
    return payload

def strict_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate JSON member")
        value[key] = item
    return value

def reject_constant(_: str) -> Any:
    raise ValueError("non-finite JSON number")

def parse_json_bytes(data: bytes, path: str) -> Any:
    try:
        text = data.decode("utf-8")
        return json.loads(text, object_pairs_hook=strict_pairs, parse_constant=reject_constant)
    except UnicodeDecodeError as exc:
        raise SaveError("INVALID_UTF8", "JSON is not valid UTF-8.", path) from exc
    except ValueError as exc:
        if "duplicate JSON member" in str(exc):
            raise SaveError("DUPLICATE_KEY", "JSON contains a duplicate member.", path) from exc
        raise SaveError("INVALID_JSON", "JSON is not valid.", path) from exc

def json_bytes(value: Any) -> bytes:
    try:
        return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise SaveError("INVALID_JSON", "Value cannot be serialized as strict JSON.") from exc

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def is_reparse_point(path: Path) -> bool:
    try:
        info = os.lstat(path)
    except OSError:
        return False
    if stat.S_ISLNK(info.st_mode):
        return True
    if os.name == "nt":
        try:
            if getattr(path, "is_junction", lambda: False)():
                return True
        except OSError:
            return True
        if getattr(info, "st_reparse_tag", None) in {0xA0000003, 0xA000000C}:
            return True
    return False

def ensure_safe_hierarchy(directory: Path, pointer: str = "/project") -> None:
    if not directory.is_absolute() or not directory.is_dir():
        raise SaveError("INVALID_PROJECT", "Project must be an existing absolute directory.", pointer)
    current = Path(directory.anchor)
    for part in directory.parts[1:]:
        current /= part
        if is_reparse_point(current):
            raise SaveError("UNSAFE_PATH", "Path hierarchy contains a link or junction.", pointer)

def ensure_within(project: Path, target: Path, pointer: str) -> None:
    try:
        relative = target.relative_to(project)
    except ValueError as exc:
        raise RequestError("PATH_OUTSIDE_PROJECT", "Path is outside the project.", pointer) from exc
    if any(part in {".", ".."} for part in relative.parts):
        raise RequestError("INVALID_PATH", "Path must use a normalized project-internal location.", pointer)
    current = project
    for part in relative.parts:
        current /= part
        if is_reparse_point(current):
            raise RequestError("UNSAFE_PATH", "Path hierarchy contains a link or junction.", pointer)

def read_file(path: Path, pointer: str, *, required: bool = True) -> bytes | None:
    if is_reparse_point(path):
        raise SaveError("UNSAFE_PATH", "Target path is a link or junction.", pointer)
    try:
        return path.read_bytes()
    except FileNotFoundError:
        if required:
            raise SaveError("MISSING_FILE", "Required file is missing.", pointer)
        return None
    except OSError as exc:
        raise SaveError("IO_ERROR", "File cannot be read.", pointer) from exc

def write_temp_replace(path: Path, data: bytes) -> None:
    if is_reparse_point(path) or not path.parent.is_dir() or is_reparse_point(path.parent):
        raise SaveError("UNSAFE_PATH", "Target cannot be safely written.")
    temp = path.parent / f".{path.name}.{os.getpid()}.{secrets.token_hex(8)}.tmp"
    fd: int | None = None
    try:
        fd = os.open(temp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "wb") as handle:
            fd = None
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        if is_reparse_point(path) or is_reparse_point(temp):
            raise SaveError("UNSAFE_PATH", "Target became unsafe during write.")
        os.replace(temp, path)
    except SaveError:
        raise
    except OSError as exc:
        raise SaveError("IO_ERROR", "File cannot be safely replaced.") from exc
    finally:
        if fd is not None:
            try:
                os.close(fd)
            except OSError:
                pass
        try:
            if temp.exists() and not is_reparse_point(temp):
                temp.unlink()
        except OSError:
            pass

class WriterLock:
    def __init__(self, path: Path) -> None:
        self.path, self.owned = path, False

    def __enter__(self) -> "WriterLock":
        if is_reparse_point(self.path):
            raise SaveError("UNSAFE_PATH", "Lock path is unsafe.", "/lock")
        try:
            fd = os.open(self.path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "w", encoding="ascii", newline="\n") as handle:
                handle.write("save-state-lock\n")
                handle.flush()
                os.fsync(handle.fileno())
            self.owned = True
            return self
        except FileExistsError as exc:
            raise SaveError("LOCKED", "Another save operation holds the writer lock.", "/lock") from exc
        except OSError as exc:
            raise SaveError("LOCK_ERROR", "Writer lock cannot be acquired.", "/lock") from exc

    def __exit__(self, *_: Any) -> None:
        if self.owned:
            try:
                if not is_reparse_point(self.path):
                    self.path.unlink(missing_ok=True)
            except OSError:
                pass

def pointer_tokens(pointer: Any, path: str) -> list[str]:
    if not isinstance(pointer, str) or (pointer and not pointer.startswith("/")):
        raise RequestError("INVALID_POINTER", "JSON Pointer is invalid.", path)
    if pointer == "":
        return []
    output: list[str] = []
    for raw in pointer[1:].split("/"):
        import re
        if re.search(r"~(?![01])", raw):
            raise RequestError("INVALID_POINTER", "JSON Pointer escape is invalid.", path)
        token = raw.replace("~1", "/").replace("~0", "~")
        if token in {"__proto__", "constructor", "prototype"}:
            raise RequestError("FORBIDDEN_KEY", "Prototype-related member names are forbidden.", path)
        output.append(token)
    return output

def array_index(token: str, length: int, *, allow_end: bool = False, allow_dash: bool = False) -> int | str:
    if allow_dash and token == "-":
        return token
    if not token.isdigit() or (len(token) > 1 and token[0] == "0"):
        raise RequestError("INVALID_POINTER", "Array index is invalid.")
    index = int(token)
    if index > length or (not allow_end and index >= length):
        raise RequestError("MISSING_TARGET", "Patch target does not exist.")
    return index

def deep_equal(left: Any, right: Any) -> bool:
    if isinstance(left, bool) or isinstance(right, bool):
        return type(left) is type(right) and left == right
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return left == right
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(deep_equal(left[key], right[key]) for key in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(deep_equal(a, b) for a, b in zip(left, right))
    return left == right

def resolve_parent(document: Any, tokens: list[str], operation_path: str) -> tuple[Any, str]:
    if not tokens:
        raise RequestError("ROOT_REPLACEMENT", "Root replacement is not allowed.", operation_path)
    current = document
    for token in tokens[:-1]:
        if isinstance(current, dict) and token in current:
            current = current[token]
        elif isinstance(current, list):
            current = current[array_index(token, len(current))]
        else:
            raise RequestError("MISSING_TARGET", "Patch target does not exist.", operation_path)
    return current, tokens[-1]

def patch_one(document: Any, operation: Any, operation_path: str, allowed: str) -> Any:
    if not isinstance(operation, dict) or set(operation) - {"op", "path", "value"}:
        raise RequestError("INVALID_OPERATION", "Patch operation is invalid.", operation_path)
    op, pointer = operation.get("op"), operation.get("path")
    if op not in {"add", "replace", "remove", "test"} or not isinstance(pointer, str):
        raise RequestError("INVALID_OPERATION", "Patch operation is invalid.", operation_path)
    if op in {"add", "replace", "test"} and "value" not in operation:
        raise RequestError("INVALID_OPERATION", "Patch operation requires a value.", operation_path)
    if op == "remove" and "value" in operation:
        raise RequestError("INVALID_OPERATION", "Remove operation cannot contain a value.", operation_path)
    tokens = pointer_tokens(pointer, operation_path + "/path")
    if allowed == "state" and not pointer.startswith("/"):
        raise RequestError("FORBIDDEN_PATH", "Patch path is outside the state.", operation_path + "/path")
    if allowed == "envelope" and not (pointer.startswith("/state/") or pointer in {"/report_markdown", "/handoff_markdown"}):
        raise RequestError("FORBIDDEN_PATH", "Patch path is outside the candidate payload.", operation_path + "/path")
    parent, token = resolve_parent(document, tokens, operation_path + "/path")
    value = copy.deepcopy(operation.get("value"))
    if isinstance(parent, dict):
        exists = token in parent
        if op == "test":
            if not exists or not deep_equal(parent[token], value):
                raise RequestError("TEST_FAILED", "Patch test failed.", operation_path + "/path")
        elif op == "add" or (op == "replace" and exists):
            parent[token] = value
        elif op == "remove" and exists:
            del parent[token]
        else:
            raise RequestError("MISSING_TARGET", "Patch target does not exist.", operation_path + "/path")
        return document
    if isinstance(parent, list):
        if op == "add":
            index = array_index(token, len(parent), allow_end=True, allow_dash=True)
            parent.append(value) if index == "-" else parent.insert(index, value)
        else:
            index = array_index(token, len(parent))
            if op == "test" and not deep_equal(parent[index], value):
                raise RequestError("TEST_FAILED", "Patch test failed.", operation_path + "/path")
            elif op == "replace":
                parent[index] = value
            elif op == "remove":
                parent.pop(index)
        return document
    raise RequestError("MISSING_TARGET", "Patch target does not exist.", operation_path + "/path")

def apply_patch(document: Any, operations: Any, allowed: str) -> Any:
    if not isinstance(operations, list):
        raise RequestError("INVALID_OPERATION", "ops must be an array.", "/ops")
    clone = copy.deepcopy(document)
    for index, operation in enumerate(operations):
        try:
            clone = patch_one(clone, operation, f"/ops/{index}", allowed)
        except RequestError as exc:
            if not exc.path:
                exc.path = f"/ops/{index}/path"
            raise
    return clone
