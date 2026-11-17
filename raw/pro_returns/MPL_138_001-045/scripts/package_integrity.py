#!/usr/bin/env python3
"""Byte-integrity and archive-membership checks; no manuscript text is displayed."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import stat
import zipfile
from pathlib import Path, PurePosixPath

PREFIX = "MPL_138_001-045"
SCANS = tuple(n for n in range(1, 46) if n != 24)
FROZEN_PATHS = tuple(f"pages/{PREFIX}_138_scan{n:03}.tex" for n in SCANS) + (f"{PREFIX}_transcription.tex",)
ROOT_FILES = frozenset({
    f"{PREFIX}_transcription.tex", f"{PREFIX}_doubts.md", f"{PREFIX}_inventory.csv",
    f"{PREFIX}_notes.md", "progress.log",
})
BLOCKED_PARTS = frozenset({
    "__pycache__", ".git", ".pytest_cache", ".mypy_cache", ".ruff_cache", "node_modules",
    "upload", "uploads", "input", "inputs", "scans", "context", "sources", "cache",
})
ANCILLARY_SUFFIXES = {
    "records": {".md", ".log", ".sha256", ".csv", ".json", ".txt"},
    "scripts": {".py", ".sh", ".tex", ".md", ".txt"},
}


def file_digest(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read_frozen_manifest(root: Path) -> tuple[dict[str, str], list[str]]:
    errors = []
    entries = {}
    manifest = root / "records" / "frozen.sha256"
    try:
        lines = manifest.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return {}, [f"Frozen manifest cannot be read ({type(exc).__name__})."]
    for number, line in enumerate(lines, 1):
        match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
        if not match:
            errors.append(f"Frozen manifest line {number}: invalid SHA-256 record.")
            continue
        digest, name = match.groups()
        if name not in FROZEN_PATHS:
            errors.append(f"Frozen manifest line {number}: unexpected path.")
            continue
        if name in entries:
            errors.append(f"Frozen manifest line {number}: duplicate path.")
        entries[name] = digest.lower()
    if len(lines) != 45 or tuple(entries) != FROZEN_PATHS:
        errors.append("Frozen manifest must list exactly the 44 ordered pages followed by the combined transcription.")
    return entries, errors


def frozen_checks(root: Path, progress: str | None = None) -> dict:
    entries, errors = read_frozen_manifest(root)
    if progress is None:
        try:
            progress = (root / "progress.log").read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Progress log cannot be read ({type(exc).__name__}).")
            progress = ""
    lines = progress.splitlines()
    freezes = [n for n, line in enumerate(lines) if line.startswith("transcription frozen ")]
    if len(freezes) != 1:
        errors.append("Progress log must contain exactly one transcription frozen record.")
    frozen_index = freezes[0] if freezes else len(lines)
    log_hashes = {}
    log_records = 0
    for number, line in enumerate(lines[:frozen_index], 1):
        if not line.startswith("SHA-256 "):
            continue
        log_records += 1
        match = re.fullmatch(r"SHA-256\s+([0-9a-fA-F]{64})\s+(.+)", line)
        if not match:
            errors.append(f"Progress log line {number}: invalid frozen SHA-256 record.")
            continue
        digest, name = match.groups()
        if name in log_hashes:
            errors.append(f"Progress log line {number}: duplicate frozen SHA-256 path.")
        log_hashes[name] = digest.lower()
    if log_records != 45 or tuple(log_hashes) != FROZEN_PATHS:
        errors.append("Progress log must contain the same 45 ordered SHA-256 records before the freeze.")
    if log_hashes != entries:
        errors.append("Frozen manifest and progress-log SHA-256 records disagree.")

    verified = 0
    for name in FROZEN_PATHS:
        path = root / name
        if path.is_symlink():
            errors.append(f"Frozen file is a symlink: {name}.")
            continue
        try:
            actual = file_digest(path)
        except OSError as exc:
            errors.append(f"Frozen file cannot be hashed: {name} ({type(exc).__name__}).")
            continue
        if entries.get(name) != actual:
            errors.append(f"Frozen SHA-256 mismatch: {name}.")
        else:
            verified += 1
    return {"ok": not errors, "manifest_entries": len(entries), "progress_hash_entries": log_records,
            "frozen_hashes_verified": verified, "errors": errors}


def eligible_name(name: str) -> bool:
    path = PurePosixPath(name)
    if path.is_absolute() or "\\" in name or str(path) != name or ".." in path.parts:
        return False
    if any(part.casefold() in BLOCKED_PARTS or part.startswith(".") for part in path.parts):
        return False
    if name in ROOT_FILES or name in FROZEN_PATHS:
        return True
    return (
        len(path.parts) >= 2
        and path.parts[0] in ANCILLARY_SUFFIXES
        and path.suffix.lower() in ANCILLARY_SUFFIXES[path.parts[0]]
    )


def package_members(root: Path) -> tuple[list[str], list[str]]:
    included, excluded = [], []
    for path in sorted(root.rglob("*")):
        if not path.is_file() and not path.is_symlink():
            continue
        name = path.relative_to(root).as_posix()
        unsafe_link = path.is_symlink() or any(parent.is_symlink() for parent in path.parents if parent != root)
        if eligible_name(name) and not unsafe_link:
            included.append(name)
        else:
            excluded.append(name)
    return sorted(included), sorted(excluded)


def zip_checks(root: Path, archive_path: Path) -> dict:
    errors = []
    expected, excluded = package_members(root)
    frozen, manifest_errors = read_frozen_manifest(root)
    errors.extend(manifest_errors)
    verified = 0
    frozen_verified = 0
    try:
        with zipfile.ZipFile(archive_path, "r") as archive:
            members = archive.infolist()
            names = [member.filename for member in members]
            if len(names) != len(set(names)):
                errors.append("ZIP contains duplicate member names.")
            if sorted(names) != expected:
                errors.append("ZIP membership differs from the complete allowlisted work tree.")
            required = ROOT_FILES | frozenset(FROZEN_PATHS) | {"records/frozen.sha256"}
            if not required.issubset(names):
                errors.append("ZIP is missing one or more required deliverables or the frozen manifest.")
            for member in members:
                name = member.filename
                if not eligible_name(name) or stat.S_ISLNK(member.external_attr >> 16):
                    errors.append(f"ZIP contains a forbidden member: {name}.")
                    continue
                path = root / name
                if name not in expected or not path.is_file() or member.file_size != path.stat().st_size:
                    errors.append(f"ZIP size/path mismatch: {name}.")
                    continue
                with archive.open(member) as stream:
                    digest = hashlib.file_digest(stream, "sha256").hexdigest()
                if digest != file_digest(path):
                    errors.append(f"ZIP bytes differ from the work tree: {name}.")
                else:
                    verified += 1
                if name in frozen:
                    if digest != frozen[name]:
                        errors.append(f"ZIP frozen SHA-256 mismatch: {name}.")
                    else:
                        frozen_verified += 1
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        errors.append(f"ZIP verification failed ({type(exc).__name__}).")
    return {"ok": not errors, "zip_members_verified": verified,
            "zip_frozen_hashes_verified": frozen_verified, "excluded_work_files": excluded, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--zip", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    report = {"frozen": frozen_checks(root)}
    included, excluded = package_members(root)
    report["package_members"] = len(included)
    report["excluded_work_files"] = excluded
    report["notes_present_and_nonempty"] = (root / f"{PREFIX}_notes.md").is_file() and (root / f"{PREFIX}_notes.md").stat().st_size > 0
    if args.zip:
        report["zip"] = zip_checks(root, args.zip.resolve())
    print(json.dumps(report, indent=2))
    return 0 if report["frozen"]["ok"] and (not args.zip or report["zip"]["ok"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
