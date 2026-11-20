#!/usr/bin/env python3
"""Create a new, verified final ZIP; never overwrite or upload an archive.

Requires work/final_validation.json with ok=true and a valid immutable
transcription freeze. OUT contents are stored directly at the archive root.
The manifest is written before the ZIP and includes every member's SHA-256
except its own self-referential hash. The archive SHA-256 is printed afterward.

Excluded: symlinks, ZIP files, __pycache__, source-input directories, known
witness/context-input filenames, original scan/half filenames, and raster
inputs outside evidence-crop locations. Every exclusion is recorded.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Importing the adjacent helper must not create cache artifacts in OUT.
sys.dont_write_bytecode = True

from freeze_transcription import (
    COMBINED_NAME,
    FREEZE_RELATIVE,
    IDENTIFIER,
    IntegrityError,
    read_json,
    regular_artifact,
    sha256_file,
    utc_now,
    verify_frozen,
)


MANIFEST_RELATIVE = "work/final_package_manifest.json"
VALIDATION_RELATIVE = "work/final_validation.json"
REQUIRED_TOP_LEVEL = {
    COMBINED_NAME,
    IDENTIFIER + "_changes.md",
    IDENTIFIER + "_collation.tsv",
    IDENTIFIER + "_inventory.csv",
    IDENTIFIER + "_doubts.md",
    IDENTIFIER + "_notes.md",
    IDENTIFIER + "_sheet_feedback.md",
    IDENTIFIER + "_hand_log.md",
    "CHECK_EVENTS.tsv",
    "progress.log",
    "PREAMBLE.tex",
}
INPUT_DIRECTORY_NAMES = {
    "packets", "scans", "scan_images", "original_scans", "witnesses",
    "witness", "inputs", "input", "context", "contexts", "context_inputs",
    "codex", "hua", "source_inputs", "source", "sources", "raw", "originals",
}
CONTEXT_INPUT_NAMES = {
    "c.tex", "h.tex", "errors.md", "conventions.md",
    "prior_questions.md", "meta.json", "differences.tsv",
}
RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp", ".bmp", ".gif"}
DOCUMENT_INPUT_SUFFIXES = {".pdf", ".djvu", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"}


def scan_image_name(name: str) -> bool:
    # Original packet images end at scanNNN or scanNNN_a/scanNNN_b.
    # Derived evidence names have an additional crop/box identifier.
    import re
    return bool(re.fullmatch(
        r".*scan[0-9]+(?:_[ab])?\.(?:png|jpe?g|tiff?|webp|bmp|gif)",
        name, flags=re.IGNORECASE,
    ))


def exclusion_reason(path: Path, relative: Path, *, directory: bool = False) -> str | None:
    if path.is_symlink():
        return "symlink"
    lowered = [part.casefold() for part in relative.parts]
    if "__pycache__" in lowered:
        return "__pycache__"
    directory_parts = lowered if directory else lowered[:-1]
    if any(part in INPUT_DIRECTORY_NAMES for part in directory_parts):
        return "source/witness/context input directory"
    if directory:
        return None
    name = path.name.casefold()
    suffix = path.suffix.casefold()
    if suffix == ".zip":
        return "ZIP archive"
    if suffix in {".pyc", ".pyo"}:
        return "Python bytecode"
    if name in CONTEXT_INPUT_NAMES:
        return "known witness or context-input filename"
    if scan_image_name(name):
        return "original scan or full-resolution half"
    if suffix in DOCUMENT_INPUT_SUFFIXES:
        return "source/document input format outside the requested deliverables"
    if suffix in RASTER_SUFFIXES:
        evidence_location = (
            bool(lowered) and lowered[0] in {"crops", "second"}
        ) or any(part in {"crops", "evidence_crops"} for part in lowered[:-1])
        if not evidence_location:
            return "raster input outside evidence-crop locations"
    return None


def stable_file_record(out: Path, relative: str) -> dict[str, Any]:
    path = regular_artifact(out, relative, nonempty=False)
    before = path.stat()
    digest = sha256_file(path)
    after = path.stat()
    before_key = (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
    after_key = (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
    if before_key != after_key:
        raise IntegrityError(f"File changed while preparing package manifest: {relative}")
    return {"path": relative, "size": after.st_size, "sha256": digest}


def collect_members(out: Path) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    members: list[dict[str, Any]] = []
    excluded: list[dict[str, str]] = []
    for current, directories, filenames in os.walk(out, followlinks=False):
        current_path = Path(current)
        kept: list[str] = []
        for name in sorted(directories):
            path = current_path / name
            relative = path.relative_to(out)
            reason = exclusion_reason(path, relative, directory=True)
            if reason:
                excluded.append({"path": relative.as_posix() + "/", "reason": reason})
            else:
                kept.append(name)
        directories[:] = kept
        for name in sorted(filenames):
            path = current_path / name
            relative = path.relative_to(out)
            relative_text = relative.as_posix()
            if relative_text == MANIFEST_RELATIVE:
                if path.is_symlink():
                    raise IntegrityError("The package manifest path is a symlink")
                # Replaced by the newly generated manifest and included separately.
                continue
            reason = exclusion_reason(path, relative)
            if reason:
                excluded.append({"path": relative_text, "reason": reason})
                continue
            if not path.is_file():
                excluded.append({"path": relative_text, "reason": "not a regular file"})
                continue
            members.append(stable_file_record(out, relative_text))
    members.sort(key=lambda member: member["path"])
    excluded.sort(key=lambda member: member["path"])
    paths = [member["path"] for member in members]
    if len(paths) != len(set(paths)):
        raise IntegrityError("Package member paths are not unique")
    absent = REQUIRED_TOP_LEVEL - set(paths)
    if absent:
        raise IntegrityError(f"Required deliverables are missing or excluded: {sorted(absent)}")
    return members, excluded


def write_manifest(out: Path, manifest: dict[str, Any]) -> None:
    target = out / MANIFEST_RELATIVE
    if target.is_symlink():
        raise IntegrityError("Refusing to replace a symlink at the package manifest path")
    target.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=".final_package_manifest.", suffix=".tmp", dir=target.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(manifest, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
    finally:
        if temporary.exists():
            temporary.unlink()


def write_member(archive: zipfile.ZipFile, out: Path, member: dict[str, Any],
                 timestamp: tuple[int, int, int, int, int, int]) -> None:
    relative = member["path"]
    source = regular_artifact(out, relative, nonempty=False)
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(source, flags)
    digest = hashlib.sha256()
    size = 0
    with os.fdopen(descriptor, "rb") as handle:
        source_stat = os.fstat(handle.fileno())
        if not stat.S_ISREG(source_stat.st_mode):
            raise IntegrityError(f"ZIP member is no longer a regular file: {relative}")
        info = zipfile.ZipInfo(relative, date_time=timestamp)
        info.create_system = 3
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = (stat.S_IFREG | stat.S_IMODE(source_stat.st_mode)) << 16
        with archive.open(info, mode="w", force_zip64=True) as destination:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                destination.write(chunk)
                digest.update(chunk)
                size += len(chunk)
    if size != member["size"] or digest.hexdigest() != member["sha256"]:
        raise IntegrityError(f"File changed after the package manifest snapshot: {relative}")


def new_zip(out: Path, destination: Path, members: list[dict[str, Any]]) -> None:
    created = False
    identity: tuple[int, int] | None = None
    now = datetime.now(timezone.utc)
    timestamp = (now.year, now.month, now.day, now.hour, now.minute, now.second)
    try:
        with zipfile.ZipFile(
            destination, mode="x", compression=zipfile.ZIP_DEFLATED,
            compresslevel=6, allowZip64=True,
        ) as archive:
            created = True
            saved_stat = destination.stat()
            identity = (saved_stat.st_dev, saved_stat.st_ino)
            for member in members:
                write_member(archive, out, member, timestamp)
        with zipfile.ZipFile(destination, mode="r") as archive:
            expected_names = [member["path"] for member in members]
            actual_names = archive.namelist()
            if actual_names != expected_names or len(actual_names) != len(set(actual_names)):
                raise IntegrityError("ZIP member list differs from the manifest snapshot")
            bad_member = archive.testzip()
            if bad_member is not None:
                raise IntegrityError(f"ZIP CRC test failed: {bad_member}")
            for info in archive.infolist():
                if stat.S_ISLNK(info.external_attr >> 16):
                    raise IntegrityError(f"ZIP unexpectedly contains a symlink: {info.filename}")
        final_verification = verify_frozen(out, append_log=False)
        if not final_verification["ok"]:
            raise IntegrityError(
                "Transcription changed during packaging: "
                + "; ".join(final_verification["errors"])
            )
    except Exception:
        # Remove only the incomplete/failed archive this call exclusively created.
        if created and identity is not None:
            try:
                current = destination.stat()
                if (current.st_dev, current.st_ino) == identity and not destination.is_symlink():
                    destination.unlink()
            except OSError:
                pass
        raise


def package(out: Path) -> dict[str, Any]:
    out = out.resolve()
    destination = out.parent / (IDENTIFIER + ".zip")
    if destination.exists() or destination.is_symlink():
        raise IntegrityError(f"Output already exists and will not be overwritten: {destination}")
    validation = read_json(out, VALIDATION_RELATIVE)
    if not isinstance(validation, dict) or validation.get("ok") is not True:
        raise IntegrityError(f"{VALIDATION_RELATIVE} must have ok=true")
    if validation.get("errors"):
        raise IntegrityError("Validation claims success but still contains errors")
    validation_sha = sha256_file(regular_artifact(out, VALIDATION_RELATIVE))
    verification = verify_frozen(out, append_log=True)
    if not verification["ok"]:
        raise IntegrityError("Frozen transcription verification failed: " + "; ".join(verification["errors"]))
    freeze_sha = sha256_file(regular_artifact(out, FREEZE_RELATIVE))
    members, excluded = collect_members(out)
    by_path = {member["path"]: member for member in members}
    for relative, digest in verification["hashes"].items():
        if relative not in by_path or by_path[relative]["sha256"] != digest:
            raise IntegrityError(f"Frozen transcription changed before the ZIP snapshot: {relative}")
    for relative, digest in (
        (VALIDATION_RELATIVE, validation_sha),
        (FREEZE_RELATIVE, freeze_sha),
    ):
        if relative not in by_path or by_path[relative]["sha256"] != digest:
            raise IntegrityError(f"Required integrity record changed before packaging: {relative}")
    manifest_members = members + [{
        "path": MANIFEST_RELATIVE,
        "sha256": None,
        "self_hash_omitted": True,
    }]
    manifest_members.sort(key=lambda member: member["path"])
    manifest = {
        "schema_version": 1,
        "identifier": IDENTIFIER,
        "created_utc": utc_now(),
        "archive_path": str(destination),
        "archive_root": "contents of OUT, without an enclosing out directory",
        "hash_algorithm": "sha256",
        "member_count": len(manifest_members),
        "members": manifest_members,
        "validation": {"path": VALIDATION_RELATIVE, "sha256": validation_sha},
        "freeze": {"path": FREEZE_RELATIVE, "sha256": freeze_sha},
        "excluded": excluded,
        "notes": [
            "This manifest was written before archive creation.",
            "Its own member hash is omitted to avoid self-reference.",
            "The completed archive SHA-256 is printed after the CRC test; it is not embedded here.",
            "No symlinks, ZIPs, caches, scans, witnesses or known context inputs are included.",
            "Derived evidence crops, page fragments, scripts and work documentation are included.",
        ],
    }
    write_manifest(out, manifest)
    members.append(stable_file_record(out, MANIFEST_RELATIVE))
    members.sort(key=lambda member: member["path"])
    new_zip(out, destination, members)
    result = {
        "path": str(destination),
        "size": destination.stat().st_size,
        "sha256": sha256_file(destination),
        "filecount": len(members),
        "crc_test": "passed",
        "manifest": str(out / MANIFEST_RELATIVE),
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out", type=Path, default=Path(__file__).resolve().parents[1],
        help="Final output directory; defaults to the directory containing scripts/.",
    )
    args = parser.parse_args()
    try:
        result = package(args.out)
    except (IntegrityError, OSError, ValueError, zipfile.BadZipFile, RuntimeError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
