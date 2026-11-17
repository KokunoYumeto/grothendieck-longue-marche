#!/usr/bin/env python3
"""Freeze or verify a transcription after the human visual audit.

The freeze action only trusts audit entries already recorded by the reader.
It does not perform an audit, read images, open the context, or change pages.
Nothing is executed when this module is imported.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile

PREFIX = "MPL_93_221-236+161-5"
PAGES = [("93", number) for number in range(221, 237)] + [
    ("161-5", number) for number in range(3, 30)
]
PAGE_PATHS = [f"pages/{PREFIX}_{cote}_scan{number:03d}.tex" for cote, number in PAGES]
COMBINED_PATH = f"{PREFIX}_transcription.tex"
MANIFEST_PATH = "records/frozen_hashes.json"
UTC_FORMAT = "%Y-%m-%d %H:%M:%S UTC"
AUDIT_ENTRY = re.compile(
    r"^[ \t]*(?:(?:cote[ \t]+)?(?P<cote>93|161-5)[ \t]+)?"
    r"scan[ \t]+(?P<scan>\d{1,3})[ \t]+audited[ \t]+"
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC)"
    r"(?:[ \t].*)?$",
    re.MULTILINE,
)


class FreezeError(Exception):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime(UTC_FORMAT)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_progress(work: Path) -> str:
    path = work / "progress.log"
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise FreezeError(f"Cannot read progress.log: {exc}") from exc


def append_log(work: Path, entries: list[str]) -> None:
    path = work / "progress.log"
    old = path.read_bytes()
    separator = b"" if not old or old.endswith(b"\n") else b"\n"
    with path.open("ab") as handle:
        handle.write(separator + ("\n".join(entries) + "\n").encode("utf-8"))
        handle.flush()
        os.fsync(handle.fileno())


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".freeze-", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def assert_all_audited(progress: str) -> None:
    expected_by_scan = {number: cote for cote, number in PAGES}
    audited: set[tuple[str, int]] = set()
    for match in AUDIT_ENTRY.finditer(progress):
        number = int(match.group("scan"))
        if number not in expected_by_scan:
            continue
        cote = match.group("cote") or expected_by_scan[number]
        if cote != expected_by_scan[number]:
            raise FreezeError(f"Audit entry pairs scan {number:03d} with wrong cote {cote}")
        try:
            datetime.strptime(match.group("timestamp"), UTC_FORMAT)
        except ValueError as exc:
            raise FreezeError(f"Invalid UTC audit timestamp for {cote} scan {number:03d}") from exc
        audited.add((cote, number))
    missing = [f"{cote} scan {number:03d}" for cote, number in PAGES if (cote, number) not in audited]
    if missing:
        raise FreezeError("Missing valid UTC audit entries: " + ", ".join(missing))


def freeze(work: Path) -> dict[str, object]:
    progress = read_progress(work)
    if re.search(r"^[ \t]*context opened\b", progress, re.MULTILINE | re.IGNORECASE):
        raise FreezeError("Context has already been marked opened; freezing or rebuilding is forbidden")
    if re.search(r"^[ \t]*transcription frozen\b", progress, re.MULTILINE | re.IGNORECASE):
        raise FreezeError("Transcription is already marked frozen; use verify")
    manifest_path = work / MANIFEST_PATH
    if manifest_path.exists():
        raise FreezeError("Frozen manifest already exists; use verify")
    assert_all_audited(progress)
    actual_pages = {path.relative_to(work).as_posix() for path in (work / "pages").glob("*.tex")}
    expected_pages = set(PAGE_PATHS)
    if actual_pages != expected_pages:
        raise FreezeError(
            f"Wrong page-file set; missing={sorted(expected_pages - actual_pages)}, "
            f"extra={sorted(actual_pages - expected_pages)}"
        )
    contents = []
    hashes = {}
    for relative in PAGE_PATHS:
        data = (work / relative).read_bytes()
        if not data.strip():
            raise FreezeError(f"Empty page file: {relative}")
        contents.append(data)
        hashes[relative] = sha256(data)
    # Page bytes are retained unchanged. One newline separates successive
    # files, preventing an end-of-file comment from swallowing the next page.
    combined = b"\n".join(contents)
    if not combined.endswith(b"\n"):
        combined += b"\n"
    if not re.match(rb"\s*\\cotefile\s*\{93\}\s*\\scanpage\s*\{221\}", combined):
        raise FreezeError("First page does not start with cotefile{93} and scanpage{221}")
    hashes[COMBINED_PATH] = sha256(combined)
    stamp = utc_now()
    manifest = {
        "schema_version": 1,
        "frozen_at": stamp,
        "algorithm": "sha256",
        "audited_pages": len(PAGES),
        "hashes": hashes,
    }
    atomic_write(work / COMBINED_PATH, combined)
    atomic_write(manifest_path, (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    append_log(work, [f"SHA-256 {relative} {digest}" for relative, digest in hashes.items()] + [f"transcription frozen {stamp}"])
    return {"action": "freeze", "utc": stamp, "pages": len(PAGES), "hashes": len(hashes), "manifest": MANIFEST_PATH}


def verify(work: Path) -> dict[str, object]:
    progress = read_progress(work)
    if not re.search(r"^[ \t]*transcription frozen\b", progress, re.MULTILINE | re.IGNORECASE):
        raise FreezeError("Progress log contains no transcription frozen entry")
    try:
        manifest = json.loads((work / MANIFEST_PATH).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise FreezeError(f"Cannot read frozen manifest: {exc}") from exc
    hashes = manifest.get("hashes") if isinstance(manifest, dict) else None
    expected = set(PAGE_PATHS + [COMBINED_PATH])
    if not isinstance(hashes, dict) or set(hashes) != expected:
        raise FreezeError("Frozen manifest must contain exactly all 43 page paths and the combined transcription")
    changed = []
    for relative in PAGE_PATHS + [COMBINED_PATH]:
        digest = hashes[relative]
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise FreezeError(f"Invalid SHA-256 in manifest for {relative}")
        try:
            current = sha256((work / relative).read_bytes())
        except OSError:
            current = None
        if current != digest:
            changed.append(relative)
    stamp = utc_now()
    if changed:
        append_log(work, [f"frozen hash verification failed {stamp}"] + [f"changed or missing: {relative}" for relative in changed])
        raise FreezeError("Frozen hashes changed or files missing: " + ", ".join(changed))
    append_log(work, [f"frozen hashes unchanged (43 page files and combined transcription; 44 SHA-256 checks) {stamp}"])
    return {"action": "verify", "utc": stamp, "unchanged": True, "hashes": len(hashes)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("freeze", "verify"))
    parser.add_argument("--workdir", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    work = args.workdir.resolve()
    try:
        result = freeze(work) if args.action == "freeze" else verify(work)
    except (FreezeError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
