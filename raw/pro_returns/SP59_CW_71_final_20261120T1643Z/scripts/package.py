#!/usr/bin/env python3
"""Validate and package the reader's SP59_CW_71 deliverables.

This script never reads source scans or witnesses and performs no OCR or TeX
compilation. It creates no scheduled task and never uploads to Library. Root
controls checkpoint timing and performs durable saving after each archive.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import records

OUT = records.OUT
PREFIX = records.PREFIX
DEFAULT_DESTINATION = OUT.parent / "delivery"
MANIFEST_NAME = "MANIFEST.tsv"
FROZEN_NAME = "TRANSCRIPTION_SHA256.tsv"
HISTORY_NAME = "ARCHIVE_HISTORY.tsv"
EXCLUDED_DIRS = {"__pycache__", ".git", ".pytest_cache", "source", "upload", "support", "scans", "witnesses", "crops", "delivery", "archives"}
EXCLUDED_SUFFIXES = {".zip", ".tar", ".gz", ".tgz", ".7z", ".rar", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif", ".tiff", ".bmp", ".svg", ".pdf", ".json", ".jsonl", ".pyc", ".pyo", ".tmp", ".part"}
EXCLUDED_BASENAMES = {"PROMPT.md", "PREAMBLE.tex", ".DS_Store"}
MANIFEST_FIELDS = ["path", "bytes", "sha256"]
FROZEN_FIELDS = ["path", "bytes", "sha256", "frozen_utc"]
HISTORY_FIELDS = ["archive_name", "kind", "capture_utc"]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def serialize_tsv(fields, rows):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n", delimiter="\t")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def include_path(path):
    relative = path.relative_to(OUT)
    if path.is_symlink():
        return False
    if any(part in EXCLUDED_DIRS or part.startswith(".") for part in relative.parts[:-1]):
        return False
    if path.name in EXCLUDED_BASENAMES or path.name.startswith("."):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    return path.is_file()


def included_paths():
    return sorted((p for p in OUT.rglob("*") if include_path(p)), key=lambda p: p.relative_to(OUT).as_posix())


def transcription_paths():
    pages = [OUT / "pages" / records.page_name(n) for n in sorted(records.FOLDERS)]
    return pages + [OUT / f"{PREFIX}_transcription.tex"]


def progress_scans(verb):
    path = OUT / "progress.log"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    return {int(n) for n in re.findall(r"^scan (\d{3}) " + re.escape(verb) + r" \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC$", text, re.MULTILINE)}


def validate(complete=False, require_audits=False):
    """Read-only structural verification of current output; no ink judgment."""
    result = records.validate(require_complete=complete)
    errors = list(result["errors"])
    warnings = list(result["warnings"])
    saved = records.load_records()
    # Ensure the combined fragment contains the actual current page bytes,
    # modulo the documented single cotefile marker and surrounding whitespace.
    combined = OUT / f"{PREFIX}_transcription.tex"
    if combined.exists():
        parts = ["\\cotefile{71}"]
        for page in saved:
            body = page["page"].read_text(encoding="utf-8")
            parts.append(re.sub(r"\\cotefile\s*\{71\}\s*", "", body).strip())
        expected = "\n\n".join(parts).rstrip() + "\n"
        if combined.read_text(encoding="utf-8") != expected:
            errors.append("Combined transcription is stale or differs from the saved page fragments; rebuild before freezing")
    expected_page_names = {records.page_name(n) for n in records.FOLDERS}
    extra_pages = sorted(p.name for p in (OUT / "pages").glob("*.tex") if p.name not in expected_page_names)
    if extra_pages:
        errors.append("Unexpected page fragments: " + ", ".join(extra_pages))
    if require_audits:
        expected_scans = set(records.FOLDERS)
        for verb in ("done", "audited"):
            missing = expected_scans - progress_scans(verb)
            if missing:
                errors.append(f"Missing actual '{verb}' progress events: " + ", ".join(f"{n:03d}" for n in sorted(missing)))
        for page in saved:
            if not page["audit"].strip():
                errors.append(f"Scan {page['scan']:03d} has no saved second-reading record")
    return {"pages": result["pages"], "errors": errors, "warnings": warnings}


def require_valid(complete=False, require_audits=False):
    result = validate(complete, require_audits)
    if result["errors"]:
        raise RuntimeError("Structural validation failed:\n" + "\n".join("- " + e for e in result["errors"]))
    return result


def freeze():
    """Freeze exactly 25 page files and the combined fragment after all audits.

    An existing freeze is never replaced. If it exists and remains valid, the
    function returns that fact without adding another freeze event.
    """
    require_valid(complete=True, require_audits=True)
    target = OUT / FROZEN_NAME
    if target.exists():
        count = verify_frozen(log=False)
        return {"status": "already frozen and unchanged", "files": count}
    timestamp = records.utc_now()
    rows = []
    for path in transcription_paths():
        data = path.read_bytes()
        rows.append({"path": path.relative_to(OUT).as_posix(), "bytes": len(data), "sha256": digest(data), "frozen_utc": timestamp})
    # Exclusive creation prevents an earlier frozen hash list being replaced.
    with target.open("xb") as f:
        f.write(serialize_tsv(FROZEN_FIELDS, rows))
    records.log_event(f"transcription frozen {timestamp}")
    for row in rows:
        records.log_event(f"sha256 {row['sha256']} {row['path']}")
    return {"status": "frozen", "files": len(rows), "utc": timestamp}


def verify_frozen(log=True):
    """Verify frozen bytes; append an unchanged event only after success."""
    manifest = OUT / FROZEN_NAME
    if not manifest.is_file():
        raise RuntimeError("The transcription has not been frozen; run freeze after all audits")
    with manifest.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        if reader.fieldnames != FROZEN_FIELDS:
            raise RuntimeError("Unexpected frozen-hash schema")
        rows = list(reader)
    expected = {p.relative_to(OUT).as_posix() for p in transcription_paths()}
    found = [r["path"] for r in rows]
    if len(found) != len(set(found)) or set(found) != expected:
        raise RuntimeError("Frozen hash list must contain exactly the 25 page files and combined transcription")
    failures = []
    for row in rows:
        path = OUT / row["path"]
        if not path.is_file():
            failures.append(f"missing {row['path']}")
            continue
        data = path.read_bytes()
        if str(len(data)) != row["bytes"] or digest(data) != row["sha256"]:
            failures.append(f"changed {row['path']}")
    if failures:
        raise RuntimeError("Frozen transcription no longer matches:\n" + "\n".join(failures))
    if log:
        records.log_event(f"transcription hashes unchanged {records.utc_now()} ({len(rows)} files)")
    return len(rows)


def update_history(archive_name, kind, timestamp):
    path = OUT / HISTORY_NAME
    rows = []
    if path.exists():
        with path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter="\t")
            if reader.fieldnames != HISTORY_FIELDS:
                raise RuntimeError("Unexpected archive-history schema")
            rows = list(reader)
    if any(row["archive_name"] == archive_name for row in rows):
        raise RuntimeError(f"Archive name already appears in capture history: {archive_name}")
    rows.append({"archive_name": archive_name, "kind": kind, "capture_utc": timestamp})
    path.write_bytes(serialize_tsv(HISTORY_FIELDS, rows))


def capture_manifest():
    """Capture allowed output files into memory and generate their manifest.

    The ZIP will use these captured bytes, not reread live files. MANIFEST.tsv
    describes every other included file; its own digest is necessarily omitted.
    """
    explanation = (
        "# Archive manifest\n\n"
        "MANIFEST.tsv lists each archived file's relative path, exact byte count, "
        "and SHA-256. The manifest itself is included in the ZIP but omitted from "
        "its own rows to avoid a circular hash. ZIP entries are written from the "
        "same captured bytes used to calculate the hashes.\n\n"
        "ARCHIVE_HISTORY.tsv records capture names and UTC times. Earlier ZIPs "
        "are never embedded. It does not assert that a capture was durably saved; "
        "the primary reader verifies saving separately.\n\n"
        "Source attachments, scans, crops, images, PDF files, old archives, JSON "
        "records, bytecode, caches, and hidden metadata are excluded. The archive "
        "contains the current deliverables, their tabular/Markdown records, and "
        "the scripts and documentation needed to continue from the supplied "
        "attachments.\n"
    )
    (OUT / "MANIFEST_README.md").write_text(explanation, encoding="utf-8")
    payload = {}
    for path in included_paths():
        relative = path.relative_to(OUT).as_posix()
        if relative == MANIFEST_NAME:
            continue
        payload[relative] = path.read_bytes()
    rows = [{"path": name, "bytes": len(data), "sha256": digest(data)} for name, data in sorted(payload.items())]
    manifest = serialize_tsv(MANIFEST_FIELDS, rows)
    (OUT / MANIFEST_NAME).write_bytes(manifest)
    payload[MANIFEST_NAME] = manifest
    return payload


def verify_archive(path):
    """Check ZIP paths, CRCs, and every manifest hash without extracting."""
    with ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise RuntimeError("Archive contains duplicate names")
        if any(n.startswith("/") or ".." in Path(n).parts for n in names):
            raise RuntimeError("Archive contains an unsafe entry path")
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"ZIP CRC failure: {bad}")
        with archive.open(MANIFEST_NAME) as f:
            text = io.TextIOWrapper(f, encoding="utf-8", newline="")
            reader = csv.DictReader(text, delimiter="\t")
            if reader.fieldnames != MANIFEST_FIELDS:
                raise RuntimeError("Archive manifest has unexpected columns")
            rows = list(reader)
        named = [r["path"] for r in rows]
        if len(named) != len(set(named)) or set(named) != set(names) - {MANIFEST_NAME}:
            raise RuntimeError("Archive entries do not match the manifest")
        for row in rows:
            data = archive.read(row["path"])
            if str(len(data)) != row["bytes"] or digest(data) != row["sha256"]:
                raise RuntimeError(f"Archive digest mismatch: {row['path']}")
    return len(names)


def package(kind, number=None, destination=None):
    """Create one new archive; never overwrite, rename, delete, or nest old ZIPs."""
    if kind == "checkpoint":
        if number is None or number < 1:
            raise ValueError("A positive checkpoint number is required")
        archive_name = f"{PREFIX}_checkpoint_{number:02d}.zip"
    elif kind == "final":
        archive_name = f"{PREFIX}.zip"
    else:
        raise ValueError("kind must be checkpoint or final")
    destination = Path(destination).resolve() if destination else DEFAULT_DESTINATION
    if destination == OUT or OUT in destination.parents:
        raise ValueError("Place archives outside the output tree")
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / archive_name
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite existing archive: {target}")
    if kind == "checkpoint":
        # The primary reader invokes this only when a 45-minute checkpoint is due.
        records.build()
        require_valid()
        if (OUT / FROZEN_NAME).exists():
            verify_frozen(log=False)
    else:
        # Rebuilding after freeze is deliberately unnecessary: validate current
        # assembled bytes and verify the frozen bytes before taking the snapshot.
        require_valid(complete=True, require_audits=True)
        verify_frozen(log=True)
    timestamp = records.utc_now()
    update_history(archive_name, kind, timestamp)
    records.log_event(f"{kind} archive capture started {timestamp} {archive_name}")
    payload = capture_manifest()
    # Exclusive mode guarantees that an older checkpoint cannot be overwritten.
    with ZipFile(target, "x", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            archive.writestr(name, data)
    count = verify_archive(target)
    return {"path": str(target), "files": count, "bytes": target.stat().st_size, "sha256": digest(target.read_bytes()), "capture_utc": timestamp}


def print_result(result):
    for key, value in result.items():
        if isinstance(value, list):
            print(f"{key}: {len(value)}")
            for item in value:
                print(f"  {item}")
        else:
            print(f"{key}: {value}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    checker = commands.add_parser("validate", help="Read-only integrity checks")
    checker.add_argument("--complete", action="store_true")
    checker.add_argument("--audits", action="store_true")
    commands.add_parser("manifest", help="Capture and write a file manifest without creating a ZIP")
    commands.add_parser("freeze", help="Freeze transcription hashes after all 25 audits")
    commands.add_parser("verify", help="Verify frozen hashes and append an unchanged event")
    checkpoint = commands.add_parser("checkpoint", help="Create the checkpoint due under root's 45-minute schedule")
    checkpoint.add_argument("--number", type=int, required=True)
    checkpoint.add_argument("--destination", type=Path)
    final = commands.add_parser("final", help="Create final ZIP after all audits and freeze")
    final.add_argument("--destination", type=Path)
    archive_check = commands.add_parser("verify-archive", help="Verify an existing ZIP against its embedded manifest")
    archive_check.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "validate":
            result = validate(args.complete, args.audits)
            print_result(result)
            if result["errors"]:
                return 1
        elif args.command == "manifest":
            payload = capture_manifest()
            print_result({"manifest": str(OUT / MANIFEST_NAME), "included_files": len(payload)})
        elif args.command == "freeze":
            print_result(freeze())
        elif args.command == "verify":
            print_result({"status": "all frozen transcription hashes unchanged", "files": verify_frozen()})
        elif args.command == "checkpoint":
            print_result(package("checkpoint", args.number, args.destination))
        elif args.command == "final":
            print_result(package("final", destination=args.destination))
        elif args.command == "verify-archive":
            print_result({"status": "archive manifest verified", "files": verify_archive(args.path)})
    except (ValueError, RuntimeError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
