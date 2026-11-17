#!/usr/bin/env python3
"""Verify the frozen sources, record final status, and build the delivery ZIP.

This script never rewrites a page or the combined transcription. It deliberately
excludes attached sources, inspection images, rendered PDFs, and bytecode.
Run from any directory after all research records have been completed.
"""
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import json
import re
import zipfile

from validate_package import Validator

ROOT = Path(__file__).resolve().parent.parent
STEM = "MPL_83_178-222"
EXPECTED = [n for n in range(178, 223) if n not in (182, 206)]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    frozen = json.loads((ROOT / "records/frozen_hashes.json").read_text())
    observed = {name: sha(ROOT / name) for name in frozen["files"]}
    assert len(observed) == 44
    assert observed == frozen["files"], "A frozen transcription file changed."
    validation = Validator(ROOT).run()
    assert validation["ok"] and validation["errors"] == 0
    assert validation["warnings"] == 0
    (ROOT / "records/final_mechanical_validation.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=False) + "\n")

    notes = (ROOT / f"{STEM}_notes.md").read_text()
    note_ids = re.findall(r"^### ([QEARCXTP]\d\d) —", notes, re.M)
    note_ids += re.findall(r"^\| (S\d\d) \|", notes, re.M)
    assert len(note_ids) == len(set(note_ids)) == 111
    assert (ROOT / "records/context_search_ledger.json").is_file()
    assert notes.count("```") % 2 == 0
    assert all(line.count("$") % 2 == 0 for line in notes.splitlines())
    for filename in (f"{STEM}_notes.md", f"{STEM}_doubts.md"):
        table_width = None
        for line in (ROOT / filename).read_text().splitlines():
            if line.startswith("|"):
                width = len(re.findall(r"(?<!\\)\|", line))
                if table_width is None:
                    table_width = width
                assert width == table_width, f"Malformed Markdown table in {filename}"
            else:
                table_width = None

    log_path = ROOT / "progress.log"
    log = log_path.read_text()
    done = [int(x) for x in re.findall(r"^83 scan (\d+) done ", log, re.M)]
    audits = [int(x) for x in re.findall(r"^scan (\d+) audited ", log, re.M)]
    assert done == EXPECTED
    assert audits == EXPECTED
    assert log.index("transcription frozen ") < log.index("context opened ")

    rows = list(csv.DictReader((ROOT / f"{STEM}_inventory.csv").open()))
    assert len(rows) == 1025 and all(row["transcribed"] == "yes" for row in rows)
    text = (ROOT / f"{STEM}_transcription.tex").read_text()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    report = {
        "verified_utc": now,
        "frozen_at_utc": frozen["frozen_at_utc"],
        "frozen_sources_unchanged": True,
        "frozen_file_count": len(observed),
        "observed_sha256": observed,
        "scan_count": len(EXPECTED),
        "scan_numbers": EXPECTED,
        "completion_entries": len(done),
        "second_visual_audit_entries": len(audits),
        "inventory_rows": len(rows),
        "inventory_all_transcribed": True,
        "uncertainty_macro_occurrences": text.count("\\unsure{"),
        "illegible_macro_occurrences": text.count("\\illegible{"),
        "research_note_count": len(note_ids),
        "research_note_ids": note_ids,
        "mechanical_checks": validation["checks"],
        "mechanical_errors": validation["errors"],
        "mechanical_warnings": validation["warnings"],
        "scope": "Mechanical completeness and unchanged hashes; image-reading quality is documented separately."
    }
    (ROOT / "records/final_verification.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    with log_path.open("a") as out:
        out.write(f"research notes complete {now}; 111 indexed items; context comparisons and independent calculations reviewed\n")
        out.write(f"final mechanical validation {now}; 43 pages; 1025 inventory rows all yes; {validation['checks']} checks; 0 errors; 0 warnings\n")
        out.write(f"transcription hashes unchanged {now}; all 44 SHA-256 values match the freeze at {frozen['frozen_at_utc']}\n")
        out.write(f"final delivery ZIP prepared {now}; attached scans and context sources excluded\n")

    included = sorted(p for p in ROOT.rglob("*") if p.is_file()
                      and "__pycache__" not in p.parts
                      and p.suffix not in {".pyc", ".pyo", ".pdf", ".jpg", ".jpeg", ".png", ".zip"})
    assert not any(part in {"upload", "scans", "context", "inspection"}
                   for p in included for part in p.relative_to(ROOT).parts)
    archive = ROOT.parent / f"{STEM}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in included:
            z.write(p, p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert len(z.namelist()) == len(included)
        for name, expected in frozen["files"].items():
            assert hashlib.sha256(z.read(name)).hexdigest() == expected
    print(json.dumps({
        "archive": str(archive), "bytes": archive.stat().st_size,
        "entries": len(included), "sha256": sha(archive),
        "frozen_sources_unchanged": True, "research_note_count": len(note_ids),
        "mechanical_validation": "passed"
    }, indent=2))


if __name__ == "__main__":
    main()
