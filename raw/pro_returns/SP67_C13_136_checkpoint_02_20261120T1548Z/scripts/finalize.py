#!/usr/bin/env python3
"""Gate, freeze, verify and package the completed diplomatic transcription.

This helper does not read scans or witness passages, does not rebuild reports,
does not schedule/create checkpoints, and does not upload anything.

Before running it, the sole reader must finish all 25 pages and second readings,
migrate additional doubts, finalize the reports, and apply report enrichment.

Read-only readiness check:
    python scripts/finalize.py --check

Authorized finalization, when all work is complete:
    python scripts/finalize.py

The default output is the sibling SP67_C13_136.zip. Existing ZIPs are never
overwritten. A retry can reuse an existing freeze only if every recorded page
and combined-transcription hash is unchanged.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import tempfile
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True

from enrich_reports import macro_checks
from validate_package import PAGE_NAMES, PREFIX, SCANS, package_file_allowed, validate


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
FROZEN_FILES = tuple(f"pages/{name}" for name in PAGE_NAMES) + (f"{PREFIX}_transcription.tex",)


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def require_complete_stream(root):
    expected = set(PAGE_NAMES)
    actual = {path.name for path in (root / "pages").glob("*.tex")}
    if actual != expected:
        raise ValueError(f"Page set is not exactly ORDER: missing={sorted(expected - actual)}, extra={sorted(actual - expected)}")
    progress = (root / "progress.log").read_text(encoding="utf-8")
    for state in ("done", "audited"):
        values = [int(value) for value in re.findall(r"(?m)^scan\s+(\d+)\s+" + state + r"\b", progress)]
        if len(values) != 25 or Counter(values) != Counter(SCANS):
            raise ValueError(f"Required exactly 25 {state} entries, one for every ORDER page; found {len(values)} entries")
        if state == "done" and values != list(SCANS):
            raise ValueError("The 25 done entries are not in ORDER")
    return progress


def require_validation(root, source, *, pre_freeze, archive=None):
    args = argparse.Namespace(output_root=root, source_texts_root=source,
                              partial=False, pre_freeze=pre_freeze, zip=archive)
    checks = validate(args)
    for warning in checks.warnings:
        print("WARNING:", warning)
    if checks.errors:
        raise ValueError("Strict validation failed:\n" + "\n".join(checks.errors))
    return checks


def require_supported_macros(root, source):
    issues = []
    macro_checks(root, source, issues)
    if issues:
        raise ValueError("Macro validation requires review:\n" + "\n".join(message for _, message in issues))


def frozen_hashes(progress):
    markers = list(re.finditer(r"(?m)^transcription frozen\b.*$", progress))
    if not markers:
        return None
    if len(markers) != 1:
        raise ValueError("Multiple freeze markers require manual review; no new freeze will be written")
    hashes = {}
    for line in progress[markers[0].end():].splitlines():
        match = re.fullmatch(r"sha256\s+(\S+)\s+([0-9a-fA-F]{64})\s*", line)
        if match:
            name, value = match.group(1), match.group(2).lower()
        else:
            match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(\S+)\s*", line)
            if not match:
                continue
            value, name = match.group(1).lower(), match.group(2)
        if name not in FROZEN_FILES:
            continue
        if name in hashes and hashes[name] != value:
            raise ValueError(f"Conflicting frozen hashes for {name}")
        hashes[name] = value
    if set(hashes) != set(FROZEN_FILES):
        raise ValueError("Existing freeze does not contain every required page and combined hash")
    return hashes


def verify_frozen(root, hashes):
    changed = [name for name in FROZEN_FILES if digest(root / name) != hashes[name]]
    if changed:
        raise ValueError(f"Frozen transcription changed: {changed}; no package created")


def append_progress(root, lines):
    with (root / "progress.log").open("a", encoding="utf-8") as stream:
        stream.write("\n".join(lines) + "\n")


def package_paths(root):
    return [path for path in sorted(root.rglob("*"))
            if path.is_file() and package_file_allowed(path.relative_to(root).as_posix())]


def build_final_zip(root, source, destination, hashes):
    paths = package_paths(root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # This is the last transcription operation before archive creation.
    verify_frozen(root, hashes)
    append_progress(root, [f"frozen hashes unchanged {utc_now()}; verified all {len(FROZEN_FILES)} files immediately before final ZIP creation"])
    descriptor, temporary_name = tempfile.mkstemp(prefix="SP67_C13_136_build_", suffix=".zip", dir=destination.parent)
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in paths:
                archive.write(path, path.relative_to(root).as_posix())
        with zipfile.ZipFile(temporary) as archive:
            for name in FROZEN_FILES:
                if hashlib.sha256(archive.read(name)).hexdigest() != hashes[name]:
                    raise ValueError(f"Packaged bytes disagree with the frozen hash: {name}")
        require_validation(root, source, pre_freeze=False, archive=temporary)
        # Same-directory hard-link installation is atomic and refuses to replace
        # a file that appeared at the destination after the initial check.
        os.link(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--source-texts-root", type=Path)
    parser.add_argument("--output", type=Path, help="final ZIP destination; basename must be SP67_C13_136.zip")
    parser.add_argument("--check", action="store_true", help="read-only strict readiness check; never freeze or package")
    args = parser.parse_args()
    root = args.output_root.resolve()
    source = (args.source_texts_root or root.parent.parent / "source/SP67_C13_136_texts").resolve()
    destination = (args.output or root.parent / f"{PREFIX}.zip").resolve()
    if destination.name != f"{PREFIX}.zip":
        parser.error(f"final filename must be {PREFIX}.zip")
    if root == destination or root in destination.parents:
        parser.error("put the final ZIP outside the output tree")
    if not source.is_dir() or not (source / "MARKS.tsv").is_file() or not (source / "PREAMBLE.tex").is_file():
        parser.error("source metadata directory must contain MARKS.tsv and PREAMBLE.tex")
    try:
        progress = require_complete_stream(root)
        hashes = frozen_hashes(progress)
        require_validation(root, source, pre_freeze=hashes is None)
        require_supported_macros(root, source)
        if hashes is not None:
            verify_frozen(root, hashes)
        if args.check:
            print("Strict readiness checks passed; no files were modified.")
            return 0
        if destination.exists():
            raise FileExistsError(f"Final ZIP already exists; refusing to overwrite: {destination}")
        if hashes is None:
            hashes = {name: digest(root / name) for name in FROZEN_FILES}
            append_progress(root, [f"transcription frozen {utc_now()}"] +
                            [f"sha256 {name} {hashes[name]}" for name in FROZEN_FILES])
        build_final_zip(root, source, destination, hashes)
        print(f"Final ZIP created: {destination}")
        print(f"Frozen hashes verified for {len(FROZEN_FILES)} transcription files; strict archive validation passed.")
        return 0
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"Finalization stopped: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
