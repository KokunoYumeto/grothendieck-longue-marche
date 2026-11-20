#!/usr/bin/env python3
"""Freeze or verify the final transcription; never replace an existing freeze.

Usage:
    python freeze_transcription.py freeze
    python freeze_transcription.py verify

All source/report reads occur only when a command or exported function runs.
The freeze covers the fifteen page fragments and the combined transcription.
Both commands require the fifteen corresponding second-reading audit files.
Verification appends its explicit result to progress.log and never rewrites
work/frozen_transcription.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any


IDENTIFIER = "SP117_CW_97+123+162-1"
EXPECTED_PAGES = 15
COMBINED_NAME = IDENTIFIER + "_transcription.tex"
FREEZE_RELATIVE = "work/frozen_transcription.json"
ORDER_RELATIVE = "work/page_order.json"


class IntegrityError(RuntimeError):
    """A required artifact is absent, unsafe, inconsistent, or changed."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def regular_artifact(out: Path, relative: str | Path, *, nonempty: bool = True) -> Path:
    """Resolve a regular artifact without following any symlink below OUT."""
    relative = Path(relative)
    if relative.is_absolute() or ".." in relative.parts:
        raise IntegrityError(f"Artifact path must stay relative to OUT: {relative}")
    cursor = out
    for component in relative.parts:
        cursor = cursor / component
        if cursor.is_symlink():
            raise IntegrityError(f"Symlink is not an eligible artifact: {cursor}")
    if not cursor.is_file():
        raise IntegrityError(f"Required regular file is missing: {cursor}")
    if nonempty and cursor.stat().st_size == 0:
        raise IntegrityError(f"Required file is empty: {cursor}")
    return cursor


def read_json(out: Path, relative: str | Path) -> Any:
    path = regular_artifact(out, relative)
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise IntegrityError(f"Cannot read JSON {path}: {exc}") from exc


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_page_order(out: Path) -> list[str]:
    raw = read_json(out, ORDER_RELATIVE)
    entries = raw.get("pages") if isinstance(raw, dict) else raw
    if not isinstance(entries, list) or len(entries) != EXPECTED_PAGES:
        raise IntegrityError(f"{ORDER_RELATIVE} must contain exactly {EXPECTED_PAGES} pages")
    pages: list[str] = []
    for number, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            raise IntegrityError(f"page_order entry {number} must be an object")
        value = entry.get("codex_file")
        if not isinstance(value, str) or not value.strip():
            raise IntegrityError(f"page_order entry {number} lacks codex_file")
        stem = PurePosixPath(value.replace("\\", "/")).stem
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.+-]*", stem):
            raise IntegrityError(f"Invalid codex_file stem in page_order entry {number}")
        if stem in pages:
            raise IntegrityError(f"Duplicate page in page_order: {stem}")
        pages.append(stem)
    return pages


def require_second_audits(out: Path, pages: list[str]) -> list[str]:
    relatives: list[str] = []
    for page in pages:
        relative = f"second/{page}_audit.json"
        audit = read_json(out, relative)
        if not isinstance(audit, dict) or audit.get("page") != page:
            raise IntegrityError(f"{relative} must be an audit object for {page}")
        readers = [audit.get("first_reader"), audit.get("second_reader")]
        if any(not isinstance(reader, str) or not reader.strip() for reader in readers):
            raise IntegrityError(f"{relative} lacks both reader identifiers")
        if readers[0].strip().casefold() == readers[1].strip().casefold():
            raise IntegrityError(f"{relative} must name different first and second readers")
        for field in ("boxes", "differences", "changed"):
            value = audit.get(field)
            if type(value) is not int or value < 0:
                raise IntegrityError(f"{relative}: {field} must be a nonnegative integer")
        if audit["boxes"] == 0:
            raise IntegrityError(f"{relative} has no audited boxes")
        if not audit["changed"] <= audit["differences"] <= audit["boxes"]:
            raise IntegrityError(f"{relative} has inconsistent audit counts")
        audited = audit.get("audited_utc")
        if not isinstance(audited, str) or not audited.strip():
            raise IntegrityError(f"{relative} lacks audited_utc")
        relatives.append(relative)
    if len(relatives) != EXPECTED_PAGES:
        raise IntegrityError("All fifteen second-reading audit files are required")
    return relatives


def transcription_paths(pages: list[str]) -> list[str]:
    return [f"pages/{page}.tex" for page in pages] + [COMBINED_NAME]


def transcription_hashes(out: Path, pages: list[str]) -> dict[str, str]:
    return {
        relative: sha256_file(regular_artifact(out, relative))
        for relative in transcription_paths(pages)
    }


def append_progress(out: Path, lines: list[str]) -> None:
    path = regular_artifact(out, "progress.log", nonempty=False)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write("\n" + "\n".join(lines) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def exclusive_json(path: Path, data: dict[str, Any]) -> None:
    """Create a new manifest exclusively; never replace a prior freeze."""
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    descriptor = os.open(path, flags, 0o644)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
    except Exception:
        # This function created the path with O_EXCL; a prior freeze was never opened.
        try:
            path.unlink()
        except OSError:
            pass
        raise


def freeze(out: Path) -> dict[str, Any]:
    out = out.resolve()
    destination = out / FREEZE_RELATIVE
    if destination.exists() or destination.is_symlink():
        raise IntegrityError(
            f"Freeze already exists: {destination}. Use verify; this command will not update it."
        )
    pages = load_page_order(out)
    audits = require_second_audits(out, pages)
    regular_artifact(out, "progress.log", nonempty=False)
    hashes = transcription_hashes(out, pages)
    frozen_utc = utc_now()
    manifest = {
        "schema_version": 1,
        "identifier": IDENTIFIER,
        "frozen_utc": frozen_utc,
        "pages": pages,
        "audits": audits,
        "hash_algorithm": "sha256",
        "hashes": hashes,
    }
    try:
        exclusive_json(destination, manifest)
    except FileExistsError as exc:
        raise IntegrityError(f"Freeze appeared concurrently and was not overwritten: {destination}") from exc
    append_progress(
        out,
        [f"transcription frozen {frozen_utc}"]
        + [f"sha256 {digest}  {relative}" for relative, digest in hashes.items()],
    )
    return {
        "ok": True,
        "operation": "freeze",
        "frozen_utc": frozen_utc,
        "manifest": str(destination),
        "files": len(hashes),
        "hashes": hashes,
    }


def verify_frozen(out: Path, *, append_log: bool = True) -> dict[str, Any]:
    """Compare against the immutable freeze; optionally append a verification event.

The packaging script uses append_log=False only for a final race check after
its progress.log snapshot has already been archived.
"""
    out = out.resolve()
    errors: list[str] = []
    pages: list[str] = []
    stored: Any = None
    actual: dict[str, str] = {}
    try:
        pages = load_page_order(out)
        require_second_audits(out, pages)
    except (IntegrityError, OSError) as exc:
        errors.append(str(exc))
    try:
        stored = read_json(out, FREEZE_RELATIVE)
    except (IntegrityError, OSError) as exc:
        errors.append(str(exc))
    if not isinstance(stored, dict):
        errors.append("Frozen transcription manifest must be an object")
        stored = {}
    if stored.get("schema_version") != 1:
        errors.append("Unrecognized frozen transcription manifest schema_version")
    if stored.get("identifier") != IDENTIFIER:
        errors.append("Frozen transcription manifest identifier is incorrect")
    if stored.get("hash_algorithm") != "sha256":
        errors.append("Frozen transcription manifest must use sha256")
    if not isinstance(stored.get("frozen_utc"), str) or not stored.get("frozen_utc", "").strip():
        errors.append("Frozen transcription manifest lacks frozen_utc")
    expected = stored.get("hashes")
    if not isinstance(expected, dict):
        errors.append("Frozen transcription hashes must be an object")
        expected = {}
    if pages:
        if stored.get("pages") != pages:
            errors.append("Page order differs from the frozen page order")
        wanted = set(transcription_paths(pages))
        if set(expected) != wanted:
            errors.append(
                "Frozen hash member set is incorrect: "
                f"missing={sorted(wanted-set(expected))}, extra={sorted(set(expected)-wanted)}"
            )
        wanted_audits = [f"second/{page}_audit.json" for page in pages]
        if stored.get("audits") != wanted_audits:
            errors.append("Frozen audit-file list differs from the required fifteen audits")
        for relative in transcription_paths(pages):
            saved = expected.get(relative)
            if not isinstance(saved, str) or not re.fullmatch(r"[0-9a-f]{64}", saved):
                errors.append(f"{relative}: stored SHA-256 is missing or invalid")
            try:
                digest = sha256_file(regular_artifact(out, relative))
                actual[relative] = digest
                if saved != digest:
                    errors.append(f"{relative}: SHA-256 changed; frozen={saved}, current={digest}")
            except (IntegrityError, OSError) as exc:
                errors.append(str(exc))
    verified_utc = utc_now()
    if append_log:
        status = "OK" if not errors else "FAILED"
        lines = [f"transcription freeze verification {status} {verified_utc}"]
        if errors:
            lines.extend("verification error: " + error for error in errors)
        else:
            lines.append(f"verified unchanged: {len(actual)} SHA-256 hashes")
        try:
            append_progress(out, lines)
        except (IntegrityError, OSError) as exc:
            errors.append(f"Could not append verification outcome to progress.log: {exc}")
    return {
        "ok": not errors,
        "operation": "verify",
        "verified_utc": verified_utc,
        "manifest": str(out / FREEZE_RELATIVE),
        "files": len(actual),
        "hashes": actual,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("freeze", "verify"))
    parser.add_argument(
        "--out", type=Path, default=Path(__file__).resolve().parents[1],
        help="Final output directory; defaults to the directory containing scripts/.",
    )
    args = parser.parse_args()
    try:
        result = freeze(args.out) if args.operation == "freeze" else verify_frozen(args.out)
    except (IntegrityError, OSError, ValueError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
