#!/usr/bin/env python3
"""Build, explicitly freeze, or verify the exact 39-page transcription.

From the deliverable root:
    python records/manage_transcription.py . --build
    python records/manage_transcription.py . --freeze
    python records/manage_transcription.py . --verify
    python records/manage_transcription.py . --check

With no mode flag, --check is used. Build writes only the combined TeX file.
Freeze writes a new SHA-256 manifest and appends 40 ordered digest lines followed
by the exact freeze line to progress.log.
Verify appends an unchanged-hashes log line only after all checks succeed.
Check is read-only. Existing manifests prohibit rebuilding or refreezing.
No page file is modified by any mode.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile


PREFIX = "MPL_11_002-042"
SCANS = tuple(range(3, 33)) + tuple(range(34, 43))
COMBINED = f"{PREFIX}_transcription.tex"
MANIFEST = "records/frozen_sha256.json"
LOG = "progress.log"
SCHEMA = "MPL-transcription-sha256-v1"
STAMP = r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} UTC"
DONE = re.compile(r"11 scan ([0-9]{3}) done (" + STAMP + r")")
AUDITED = re.compile(r"scan ([0-9]{3}) audited (" + STAMP + r")")


class StructuralError(Exception):
    pass


def expected_page_paths():
    return [f"pages/{PREFIX}_11_scan{scan:03d}.tex" for scan in SCANS]


def hash_log_lines(hashes):
    return [
        f"sha256 {relative} {hashes[relative]}"
        for relative in expected_page_paths() + [COMBINED]
    ]


def checked_path(root, relative):
    path = root / relative
    try:
        path.resolve().relative_to(root)
    except ValueError as exc:
        raise StructuralError(f"Path leaves the deliverable root: {relative}") from exc
    return path


def read_bytes(root, relative):
    try:
        return checked_path(root, relative).read_bytes()
    except OSError as exc:
        raise StructuralError(f"Cannot read {relative}: {exc}") from exc


def page_snapshot(root):
    expected = expected_page_paths()
    present = {
        path.relative_to(root).as_posix()
        for path in (root / "pages").glob(f"{PREFIX}_11_scan*.tex")
    }
    missing = sorted(set(expected) - present)
    extra = sorted(present - set(expected))
    problems = []
    if missing:
        problems.append("Missing page fragments: " + ", ".join(missing))
    if extra:
        problems.append("Unexpected page fragments: " + ", ".join(extra))
    if problems:
        raise StructuralError("\n".join(problems))
    return {relative: read_bytes(root, relative) for relative in expected}


def check_snapshot_unchanged(root, snapshot):
    changed = [
        relative for relative, original in snapshot.items()
        if read_bytes(root, relative) != original
    ]
    if changed:
        raise StructuralError("Files changed during this operation: " + ", ".join(changed))


def snapshot_with_combined(root):
    snapshot = page_snapshot(root)
    combined = read_bytes(root, COMBINED)
    if combined != b"".join(snapshot.values()):
        raise StructuralError(
            f"{COMBINED} does not equal the exact ordered concatenation of the 39 pages."
        )
    snapshot[COMBINED] = combined
    return snapshot


def prerequisite_log(root):
    raw = read_bytes(root, LOG)
    try:
        lines = raw.decode("utf-8").splitlines()
    except UnicodeError as exc:
        raise StructuralError(f"{LOG} is not valid UTF-8: {exc}") from exc
    done = set()
    audited = set()
    for line in lines:
        for pattern, found in ((DONE, done), (AUDITED, audited)):
            match = pattern.fullmatch(line)
            if not match:
                continue
            try:
                datetime.strptime(match.group(2), "%Y-%m-%d %H:%M:%S UTC")
            except ValueError as exc:
                raise StructuralError(f"Invalid timestamp on a {pattern.pattern[:8]!r} log record.") from exc
            scan = int(match.group(1))
            if scan in SCANS:
                found.add(scan)
    problems = []
    for label, found in (("page-done", done), ("audited", audited)):
        missing = sorted(set(SCANS) - found)
        if missing:
            problems.append(
                f"Missing {label} log lines for scans: "
                + ", ".join(f"{scan:03d}" for scan in missing)
            )
    if problems:
        raise StructuralError("Freeze prerequisites are incomplete.\n" + "\n".join(problems))
    return raw, lines


def assert_unfrozen(root):
    if (root / MANIFEST).exists():
        raise StructuralError(
            f"{MANIFEST} already exists. Rebuilding and refreezing are disabled; use --verify."
        )


def build(root):
    assert_unfrozen(root)
    snapshot = page_snapshot(root)
    payload = b"".join(snapshot.values())
    target = checked_path(root, COMBINED)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", prefix=".transcription-build-", suffix=".tmp",
            dir=root, delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        check_snapshot_unchanged(root, snapshot)
        assert_unfrozen(root)
        os.replace(temporary, target)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    print(f"BUILT: {COMBINED}; exact concatenation of 39 pages, {len(payload)} bytes.")
    print("No log or SHA-256 manifest was written.")


def freeze(root):
    assert_unfrozen(root)
    progress, _ = prerequisite_log(root)
    snapshot = snapshot_with_combined(root)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    freeze_line = f"transcription frozen {stamp}"
    payload = {
        "schema": SCHEMA,
        "cote": PREFIX,
        "frozen_at": stamp,
        "ordered_scans": list(SCANS),
        "progress_log": LOG,
        "freeze_log_line": freeze_line,
        "files": {
            relative: hashlib.sha256(data).hexdigest()
            for relative, data in snapshot.items()
        },
    }
    encoded = (json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    check_snapshot_unchanged(root, snapshot)
    if read_bytes(root, LOG) != progress:
        raise StructuralError(f"{LOG} changed during the freeze check; retry after writes finish.")
    manifest_path = checked_path(root, MANIFEST)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with manifest_path.open("xb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise StructuralError(f"{MANIFEST} already exists; no freeze log was appended.") from exc
    separator = b"" if not progress or progress.endswith(b"\n") else b"\n"
    freeze_block = "\n".join(hash_log_lines(payload["files"]) + [freeze_line]) + "\n"
    try:
        with checked_path(root, LOG).open("ab") as handle:
            handle.write(separator + freeze_block.encode("utf-8"))
            handle.flush()
            os.fsync(handle.fileno())
    except OSError as exc:
        raise StructuralError(
            f"{MANIFEST} was created, but the freeze log append failed: {exc}. "
            "The freeze record is incomplete; --verify will report the missing log line."
        ) from exc
    print("FROZEN: 39 page hashes and the combined transcription hash.")
    print(f"Manifest: {MANIFEST}")
    print(f"Appended to {LOG}: 40 ordered SHA-256 lines, followed by {freeze_line}")


def verify(root, append_log=False):
    try:
        payload = json.loads(read_bytes(root, MANIFEST).decode("utf-8"))
    except (UnicodeError, ValueError) as exc:
        raise StructuralError(f"Cannot parse {MANIFEST}: {exc}") from exc
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise StructuralError(f"{MANIFEST} has an unsupported schema.")
    if payload.get("cote") != PREFIX or payload.get("ordered_scans") != list(SCANS):
        raise StructuralError("Manifest cote or page order differs from the required deliverable.")
    frozen_at = payload.get("frozen_at")
    if not isinstance(frozen_at, str) or not re.fullmatch(STAMP, frozen_at):
        raise StructuralError("Manifest frozen_at must have the exact UTC timestamp format.")
    try:
        datetime.strptime(frozen_at, "%Y-%m-%d %H:%M:%S UTC")
    except ValueError as exc:
        raise StructuralError("Manifest frozen_at is not a valid UTC calendar timestamp.") from exc
    hashes = payload.get("files")
    expected = set(expected_page_paths() + [COMBINED])
    if not isinstance(hashes, dict) or set(hashes) != expected:
        raise StructuralError("Manifest must contain exactly the expected 39 page paths and combined path.")
    for relative, digest in hashes.items():
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
            raise StructuralError(f"Invalid SHA-256 digest in manifest for {relative}.")
    snapshot = snapshot_with_combined(root)
    changed = [
        relative for relative, data in snapshot.items()
        if hashlib.sha256(data).hexdigest() != hashes[relative].lower()
    ]
    if changed:
        raise StructuralError("Frozen content changed: " + ", ".join(changed))
    progress, lines = prerequisite_log(root)
    expected_line = f"transcription frozen {frozen_at}"
    if (
        payload.get("progress_log") != LOG
        or payload.get("freeze_log_line") != expected_line
        or not re.fullmatch(r"transcription frozen " + STAMP, expected_line)
        or expected_line not in lines
    ):
        raise StructuralError("The manifest's exact freeze log line is missing or inconsistent.")
    expected_hash_lines = hash_log_lines(hashes)
    matching_freeze_positions = [index for index, line in enumerate(lines) if line == expected_line]
    if not any(
        index >= len(expected_hash_lines)
        and lines[index - len(expected_hash_lines):index] == expected_hash_lines
        for index in matching_freeze_positions
    ):
        raise StructuralError(
            "The matching freeze line must immediately follow the exact ordered 40-line SHA-256 block."
        )
    check_snapshot_unchanged(root, snapshot)
    if append_log:
        if read_bytes(root, LOG) != progress:
            raise StructuralError(f"{LOG} changed during verification; retry after writes finish.")
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        verification_line = f"all page and combined hashes unchanged {stamp}"
        separator = b"" if not progress or progress.endswith(b"\n") else b"\n"
        with checked_path(root, LOG).open("ab") as handle:
            handle.write(separator + verification_line.encode("utf-8") + b"\n")
            handle.flush()
            os.fsync(handle.fileno())
    print("VERIFIED: all 40 SHA-256 digests match the frozen manifest.")
    print("The combined transcription equals the exact ordered page concatenation.")
    print("All 39 page-done lines, all 39 audited lines, and the exact ordered hash/freeze block are present.")
    if append_log:
        print(f"Appended to {LOG}: {verification_line}")
    else:
        print("Read-only check: no files were modified.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Deliverable root directory")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--build", action="store_true", help="Write exact combined TeX; do not freeze or log")
    modes.add_argument("--freeze", action="store_true", help="Require all done/audited lines; write manifest and freeze log")
    modes.add_argument("--verify", action="store_true", help="Verify unchanged hashes and append a UTC success log line")
    modes.add_argument("--check", action="store_true", help="Read-only verification (default)")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"Deliverable root is not a directory: {root}")
    try:
        if args.build:
            build(root)
        elif args.freeze:
            freeze(root)
        else:
            verify(root, append_log=args.verify)
    except (StructuralError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
