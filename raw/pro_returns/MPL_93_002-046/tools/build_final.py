#!/usr/bin/env python3
"""Build the final cumulative text/code ZIP after validation and frozen-hash checks."""
from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import re
import shutil
import subprocess
import sys
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "MPL_93_002-046"
TARGET = ROOT.parent / (PREFIX + ".zip")
STAMP = "%Y-%m-%d %H:%M:%S UTC"
EXCLUDED_DIRS = {
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".git", "node_modules", "inspection", "scans", "upload", "uploads",
    "attachments", "context", "context_sources", "external_research_sources",
}
EXCLUDED_NAMES = {"library_file_transfer.py"}
ALLOWED_SUFFIXES = {".tex", ".md", ".csv", ".json", ".log", ".py", ".txt", ".sh"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    if TARGET.exists():
        raise SystemExit("Refusing to overwrite an existing final archive.")
    validation = subprocess.run(
        [sys.executable, str(ROOT / "tools/validate_package.py")],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    context = subprocess.run(
        [sys.executable, str(ROOT / "tools/build_research_records.py")],
        check=True, capture_output=True, text=True,
    ).stdout.strip()

    frozen = json.loads((ROOT / "frozen_sha256.json").read_text())
    assert len(frozen) == 43
    for name, expected in frozen.items():
        assert digest((ROOT / name).read_bytes()) == expected, name
    notes_bytes = (ROOT / f"{PREFIX}_notes.md").read_bytes()
    notes = notes_bytes.decode()
    note_ids = re.findall(r"^### ([EOAPC]\d{2}) — ", notes, re.M)
    assert len(note_ids) == len(set(note_ids)) == 82
    assert "<!--" not in notes, "Unfinished notes placeholder"

    with (ROOT / f"{PREFIX}_inventory.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 693 and all(r["transcribed"] == "yes" for r in rows)
    scans = sorted({int(r["scan"]) for r in rows})
    assert scans == [n for n in range(3, 47) if n not in (26, 35)]
    kinds = {}
    for row in rows:
        kinds.setdefault(int(row["scan"]), set()).add(row["sheet_kind"])
    assert all(len(k) == 1 for k in kinds.values())
    counts = {kind: sum(next(iter(k)) == kind for k in kinds.values())
              for kind in ("reused_typed", "typed", "text", "cover")}
    assert counts == {"reused_typed": 24, "typed": 9, "text": 7, "cover": 2}
    with (ROOT / "doubt_records.csv").open(newline="") as stream:
        assert sum(1 for _ in csv.DictReader(stream)) == 124

    log_path = ROOT / "progress.log"
    original_log = log_path.read_bytes()
    log_text = original_log.decode()
    assert len(re.findall(r"^93 scan \d{3} done ", log_text, re.M)) == 42
    assert len(re.findall(r"^scan \d{3} audited ", log_text, re.M)) == 42
    assert log_text.index("transcription frozen ") < log_text.index("context opened ")

    # Preserve the session's page-writing scripts without executing them.
    copies = ROOT / "tools/session_scripts"
    copies.mkdir(exist_ok=True)
    for pattern in ("*.py", "*.sh"):
        for source in sorted(ROOT.parent.glob(pattern)):
            if source.is_file() and not source.is_symlink():
                shutil.copy2(source, copies / source.name)

    now = datetime.now(timezone.utc).strftime(STAMP)
    report = f"""# Final validation report

Validation time: {now}

## Coverage and state

| Check | Result |
|---|---|
| Expected retained scan set | 42 pages; exact match |
| Page-completion log records | 42 |
| Second image-audit log records | 42 |
| Combined transcription | Exact ordered byte concatenation |
| Inventory | 693 rows; all transcribed=yes |
| Sheet classifications | 24 reused_typed; 9 typed; 7 text; 2 cover |
| Doubt register | 124 entries |
| Research notes | 82 unique labelled items |
| Research-note context searches | Refreshed by the per-note builder |
| Frozen SHA-256 values | All 43 unchanged |
| Context timing | Opened only after the recorded freeze |

Research-notes SHA-256: {digest(notes_bytes)}

## Mechanical validator

{validation}

## Per-note context validator

{context.splitlines()[0]}

## Limits and independent review

The mechanical validator does not verify paleography or mathematical truth.
All images were read by the primary transcriber before the freeze; no additional
reading is claimed by these tests. The research-note integrity and targeted
mathematical reviews are documented in research/final_notes_review.md and the
source-verification registers. Full TeX compilation was unavailable because
format/package data were missing; no rendered typesetting proof is claimed.

The archive builder additionally verifies ZIP integrity, every packaged file
against package_contents_sha256.txt, and all frozen page/combined hashes inside
the archive before reporting success.
"""
    (ROOT / "final_validation_report.md").write_text(report)
    extra = (
        f"research notes completed {now}: 82 labelled items; 33 typed/printed sheets inventoried\n"
        f"research context comparisons verified {now}: two supplied context files; per-note search record complete\n"
        f"final mechanical validation PASS {now}: 42 pages; 693 inventory elements; 124 doubt entries\n"
        f"transcription hashes unchanged {now}: all 42 page files and combined transcription match frozen SHA-256\n"
        f"final archive created {now}: {PREFIX}.zip\n"
    ).encode()
    log_path.write_bytes(original_log.rstrip(b"\n") + b"\n" + extra)

    try:
        files = []
        for path in sorted(ROOT.rglob("*")):
            rel = path.relative_to(ROOT)
            if not path.is_file() or path.is_symlink():
                continue
            if any(part in EXCLUDED_DIRS for part in rel.parts):
                continue
            if path.name in EXCLUDED_NAMES or path.suffix.lower() not in ALLOWED_SUFFIXES:
                continue
            if path.name == "package_contents_sha256.txt":
                continue
            files.append((rel.as_posix(), path))
        manifest = "".join(f"{digest(path.read_bytes())}  {name}\n"
                           for name, path in files)
        manifest_path = ROOT / "package_contents_sha256.txt"
        manifest_path.write_text(manifest)
        files.append((manifest_path.name, manifest_path))

        with ZipFile(TARGET, "x", ZIP_DEFLATED, compresslevel=9) as archive:
            for name, path in files:
                archive.write(path, name)
        with ZipFile(TARGET) as archive:
            assert archive.testzip() is None
            assert len(archive.namelist()) == len(files)
            for name, path in files:
                assert archive.read(name) == path.read_bytes(), name
            for name, expected in frozen.items():
                assert digest(archive.read(name)) == expected, name
            assert len([n for n in archive.namelist() if n.startswith("pages/")]) == 42
    except Exception:
        TARGET.unlink(missing_ok=True)
        log_path.write_bytes(original_log)
        raise

    print(json.dumps({
        "file": str(TARGET), "bytes": TARGET.stat().st_size,
        "sha256": digest(TARGET.read_bytes()), "files": len(files),
        "pages": 42, "inventory_rows": 693, "doubt_rows": 124,
        "research_notes": 82, "frozen_hashes_unchanged": 43,
        "created_utc": now,
    }, indent=2))


if __name__ == "__main__":
    main()
