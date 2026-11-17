#!/usr/bin/env python3
"""Explicit assembly, freeze, and later verification of the transcription.

No action occurs without a required mode flag. This program never changes a
page file, never reads images or context, and never claims to perform a visual
audit. Root must finish visual audits, notation review, and doubts before using
--freeze --notation-reviewed. Freeze checks the existing audit records, writes
the combined fragment and SHA-256 manifest, then appends all hashes followed by
the UTC freeze record. It does not open context. --verify is read-only;
--verify-and-log additionally appends a successful final verification record.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


PACKAGE = "MPL_136_282-327"
SCANS = tuple(n for n in range(282, 328) if n != 319)
PAGE_NAMES = tuple(f"pages/{PACKAGE}_136_scan{scan}.tex" for scan in SCANS)
COMBINED = f"{PACKAGE}_transcription.tex"
MANIFEST = "frozen_hashes.sha256"


def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(message: str) -> None:
    raise RuntimeError(message)


def atomic_write(path: Path, data: bytes) -> None:
    temporary = path.with_name(path.name + f".{os.getpid()}.tmp")
    try:
        with temporary.open("xb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def uncomment(text: str) -> str:
    lines = []
    for line in text.splitlines(keepends=True):
        for match in re.finditer("%", line):
            before = line[:match.start()]
            slashes = len(before) - len(before.rstrip("\\"))
            if slashes % 2 == 0:
                line = before + "\n"
                break
        lines.append(line)
    return "".join(lines)


def read_pages(root: Path) -> dict[str, bytes]:
    paths = {path.name for path in (root / "pages").glob("*.tex")}
    expected_names = {Path(name).name for name in PAGE_NAMES}
    if paths != expected_names:
        fail(f"Page filename mismatch; missing={sorted(expected_names-paths)}; extra={sorted(paths-expected_names)}")
    pages = {name: (root / name).read_bytes() for name in PAGE_NAMES}
    for scan, (name, data) in zip(SCANS, pages.items()):
        text = uncomment(data.decode("utf-8"))
        markers = re.findall(r"\\scanpage\s*\{(\d+)\}", text)
        if markers != [str(scan)]:
            fail(f"Wrong scan marker in {name}")
        if scan != SCANS[0] and re.search(r"\\cotefile\b", text):
            fail(f"Unexpected extra cote marker in {name}")
    return pages


def assembled(pages: dict[str, bytes]) -> bytes:
    data = b"\n".join(pages.values())
    first = uncomment(next(iter(pages.values())).decode("utf-8"))
    cotefiles = re.findall(r"\\cotefile\s*\{([^{}]+)\}", first)
    if not cotefiles:
        data = b"\\cotefile{136}\n" + data
    elif cotefiles != ["136"] or not re.match(r"\s*\\cotefile\s*\{136\}", first):
        fail("First page has an invalid or misplaced cotefile marker")
    return data if data.endswith(b"\n") else data + b"\n"


def verify(root: Path) -> dict[str, str]:
    path = root / MANIFEST
    entries: dict[str, str] = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            fail(f"Invalid manifest line {number}")
        hash_value, name = match.groups()
        if name in entries:
            fail(f"Duplicate manifest entry {name}")
        entries[name] = hash_value
    expected = set(PAGE_NAMES) | {COMBINED}
    if set(entries) != expected:
        fail("Manifest does not contain exactly the 45 page files and combined fragment")
    for name, hash_value in entries.items():
        if digest((root / name).read_bytes()) != hash_value:
            fail(f"Frozen file changed: {name}")
    return entries


def append_log(path: Path, text: str) -> None:
    existing = path.read_bytes()
    addition = ("" if not existing or existing.endswith(b"\n") else "\n") + text
    with path.open("ab") as stream:
        stream.write(addition.encode("utf-8"))
        stream.flush()
        os.fsync(stream.fileno())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--assemble-only", action="store_true")
    mode.add_argument("--freeze", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--verify-and-log", action="store_true")
    parser.add_argument("--notation-reviewed", action="store_true",
                        help="required for freeze: caller confirms completed notation review")
    args = parser.parse_args()
    root = args.root.resolve()
    log_path = root / "progress.log"
    log = log_path.read_text(encoding="utf-8")
    frozen = bool(re.search(r"(?m)^transcription frozen\b", log))
    if args.verify or args.verify_and_log:
        if not frozen:
            fail("No existing freeze record; verification does not create one")
        entries = verify(root)
        if args.verify_and_log:
            append_log(log_path, f"frozen hashes unchanged {stamp()}\n")
        print(f"Verified unchanged SHA-256 values for {len(entries)} transcription files.")
        return 0
    if frozen:
        fail("Transcription already frozen; only verification modes are allowed")
    if re.search(r"(?m)^context opened\b", log):
        fail("Context has already been opened; assembly/freeze is refused")
    if (root / MANIFEST).exists():
        fail("A manifest already exists without a freeze record; inspect the interrupted freeze manually")
    if args.freeze and not args.notation_reviewed:
        fail("Freeze requires --notation-reviewed after root completes that review")
    validation = subprocess.run(
        [sys.executable, str(root / "scripts/validate_package.py"), str(root)],
        capture_output=True, text=True)
    if validation.returncode != 0:
        fail("Mechanical validation failed:\n" + validation.stdout + validation.stderr)
    pages = read_pages(root)
    combined = assembled(pages)
    if args.freeze:
        completed = [int(n) for n in re.findall(r"(?m)^136 scan (\d+) done\b", log)]
        audited = [int(n) for n in re.findall(r"(?m)^scan (\d+) audited\b", log)]
        if completed != list(SCANS) or audited != list(SCANS):
            fail("Freeze requires exactly one ordered done and audited record per page")
        doubts = root / f"{PACKAGE}_doubts.md"
        if not doubts.is_file() or doubts.stat().st_size == 0:
            fail("The nonempty doubts/notation file must exist before freeze")
    # Confirm no page changed while the snapshot and validation were prepared.
    for name, data in pages.items():
        if (root / name).read_bytes() != data:
            fail(f"Concurrent page change detected: {name}; nothing has been frozen")
    atomic_write(root / COMBINED, combined)
    if args.assemble_only:
        print(f"Assembled {len(pages)} pages into {root / COMBINED}; no freeze recorded.")
        return 0
    hashes = {name: digest(data) for name, data in pages.items()}
    hashes[COMBINED] = digest(combined)
    manifest = "".join(f"{value}  {name}\n" for name, value in hashes.items())
    atomic_write(root / MANIFEST, manifest.encode("utf-8"))
    # Reverify all bytes immediately before committing the log marker.
    verify(root)
    if log_path.read_text(encoding="utf-8") != log:
        fail("Progress log changed concurrently; manifest exists but freeze was not recorded")
    hash_records = "".join(f"sha256 {value} {name}\n" for name, value in hashes.items())
    append_log(log_path, hash_records + f"transcription frozen {stamp()}\n")
    print(f"Frozen {len(hashes)} files; context remains unopened by this script.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
