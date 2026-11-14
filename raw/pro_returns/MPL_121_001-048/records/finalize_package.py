#!/usr/bin/env python3
"""Verify the frozen deliverables and create the final, complete ZIP.

This script reads all transcription files without modifying them. It writes
only the final validation/archive records and an appended progress entry.
"""

from __future__ import annotations

import csv
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile

from create_checkpoint import include_path


ROOT = Path(__file__).resolve().parents[1]
NAME = "MPL_121_001-048"
SCANS = [n for n in range(1, 49) if n not in {3, 25, 29, 38, 40}]
FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    expected_pages = [f"pages/{NAME}_121_scan{n:03d}.tex" for n in SCANS]
    actual_pages = sorted(p.relative_to(ROOT).as_posix()
                          for p in (ROOT / "pages").glob("*.tex"))
    require(actual_pages == expected_pages, "Page file set/order mismatch")
    combined_name = f"{NAME}_transcription.tex"
    combined = (ROOT / combined_name).read_text()
    manifest = json.loads((ROOT / "records/frozen_sha256.json").read_text())
    require(set(manifest["files"]) == set(expected_pages + [combined_name]),
            "Frozen manifest must contain exactly the 44 transcription files")
    checks = {name: digest(ROOT / name) == sha
              for name, sha in manifest["files"].items()}
    require(all(checks.values()), "A frozen transcription hash changed")
    require(combined == "\n".join((ROOT / name).read_text().rstrip() + "\n"
                                 for name in expected_pages),
            "Combined fragment differs from ordered page files")
    require(combined.startswith("\\cotefile{121}\n\\scanpage{1}"),
            "Unexpected initial cote/scan markers")
    require([int(n) for n in re.findall(r"\\scanpage\{(\d+)\}", combined)] == SCANS,
            "Combined scan-marker order mismatch")
    require(not re.search(r"\\(?:documentclass|includegraphics|input|include)\b", combined),
            "Unexpected preamble or external inclusion in transcription")

    with (ROOT / f"{NAME}_inventory.csv").open(newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames == FIELDS, "Inventory column mismatch")
        inventory = list(reader)
    require(len(inventory) == 825, "Inventory row count mismatch")
    require(all(r["transcribed"] == "yes" and r["cote"] == "121"
                for r in inventory), "Incomplete inventory row")
    require(sorted({int(r["scan"]) for r in inventory}) == SCANS,
            "Inventory scan coverage mismatch")
    require(all(r["kind"] in {"text", "display", "diagram", "drawing", "margin note",
                               "insertion", "deletion"} for r in inventory),
            "Unexpected inventory element kind")

    progress_path = ROOT / "progress.log"
    progress = progress_path.read_text()
    lines = progress.splitlines()
    require(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC", lines[0])),
            "Progress log lacks initial UTC timestamp")
    done = [(i, int(m.group(1))) for i, line in enumerate(lines)
            if (m := re.match(r"121 scan (\d{3}) done ", line))]
    audits = [(i, int(m.group(1))) for i, line in enumerate(lines)
              if (m := re.match(r"scan (\d{3}) audited ", line))]
    require([n for _, n in done] == SCANS, "Initial-reading log mismatch")
    require([n for _, n in audits] == SCANS, "Second-reading log mismatch")
    freeze = next(i for i, line in enumerate(lines) if line.startswith("transcription frozen "))
    context = next(i for i, line in enumerate(lines) if line.startswith("context opened "))
    require(max(i for i, _ in audits) < freeze < context,
            "Audit/freeze/context order mismatch")
    require("notation cross-check completed" in "\n".join(lines[:freeze]),
            "Notation check missing before freeze")
    require(all(f"SHA-256 {sha} {name}" in lines[:freeze]
                for name, sha in manifest["files"].items()),
            "Frozen hashes missing from progress log")

    compile_results = json.loads((ROOT / "records/latex_validation/compile_results.json").read_text())
    require(compile_results["passed"] == compile_results["total"] == 43,
            "Recorded syntax check did not pass all pages")
    require(all(row["returncode"] == 0 and digest(ROOT / row["file"]) == row["sha256"]
                for row in compile_results["pages"]),
            "Syntax-check records no longer match delivered files")
    structural = json.loads((ROOT / "records/latex_validation/integrity_results.json").read_text())
    require(not structural["issues"], "Earlier structural validation reported issues")

    notes_path = ROOT / f"{NAME}_notes.md"
    notes = notes_path.read_text()
    n_ids = re.findall(r"^### (N\d{2}) —", notes, re.M)
    q_ids = re.findall(r"^#### (Q\d+\.\d+) —", notes, re.M)
    expected_n = {f"N{n:02d}" for n in range(1, 86)}
    expected_q = {f"Q{q}.{n}" for q, count in [(1, 6), (2, 8), (3, 9), (4, 7)]
                  for n in range(1, count + 1)}
    require(len(n_ids) == 85 and set(n_ids) == expected_n, "Current-page note IDs mismatch")
    require(len(q_ids) == 30 and set(q_ids) == expected_q, "Question-note IDs mismatch")
    sections = re.findall(r"^#{3,4} (N\d{2}|Q\d+\.\d+) —[^\n]*\n(.*?)(?=^#{2,4} |\Z)",
                          notes, re.M | re.S)
    require(len(sections) == 115, "Could not parse all research entries")
    required_metadata = ["**Kind:**", "**Anchor:**", "**Context:**",
                         "**Relationship:**", "**Register:**"]
    metadata_issues = {identifier: [field for field in required_metadata if field not in body]
                       for identifier, body in sections
                       if any(field not in body for field in required_metadata)}
    require(not metadata_issues, f"Research metadata missing: {metadata_issues}")
    for heading in ["## Steps the manuscript itself marks as unverified",
                    "## Title sheets, internal headings, and page counts",
                    "## Sources and precise locators"]:
        require(heading in notes, f"Missing standing/source section: {heading}")
    require(notes.count(r"\(") == notes.count(r"\)") and
            notes.count(r"\[") == notes.count(r"\]"), "Unbalanced note math delimiters")
    require(not re.search(r"\bTODO\b|\bTBD\b|INSERT HERE|PLACEHOLDER|undergoing a targeted",
                          notes, re.I), "Unfinished assembly placeholder")
    for filename, expected in [("context_search_audit.json", expected_n),
                               ("question_context_search_audit.json", expected_q)]:
        data = json.loads((ROOT / "records/research" / filename).read_text())
        identifiers = {row.get("note", row.get("id")) for row in data}
        require(identifiers == expected, f"Context-search coverage mismatch: {filename}")

    required_files = [combined_name, f"{NAME}_doubts.md", f"{NAME}_inventory.csv",
                      f"{NAME}_notes.md", "progress.log", "README.md"]
    require(all((ROOT / name).is_file() for name in required_files), "Missing deliverable")
    verification = {
        "verified_utc": utc,
        "result": "passed",
        "frozen_utc": manifest["frozen_utc"],
        "frozen_transcription_files_checked": len(checks),
        "all_frozen_hashes_unchanged": all(checks.values()),
        "combined_sha256": digest(ROOT / combined_name),
        "retained_scans": SCANS,
        "initial_reading_entries": len(done),
        "second_visual_audit_entries": len(audits),
        "audits_then_freeze_then_context": True,
        "inventory_rows": len(inventory),
        "inventory_all_transcribed_yes": True,
        "recorded_syntax_passes_matching_current_files": 43,
        "syntax_scope": "See records/latex_validation/README.md: transparent wrappers; no ulem.sty",
        "current_page_research_items": len(n_ids),
        "question_research_items": len(q_ids),
        "research_required_metadata_present": True,
        "context_search_records_complete": True,
        "research_notes_bytes": notes_path.stat().st_size,
        "research_notes_sha256": digest(notes_path),
        "frozen_file_checks": checks,
    }
    write_json(ROOT / "records/final_validation.json", verification)
    with progress_path.open("a") as handle:
        handle.write(f"frozen transcription hashes unchanged {utc}; all 43 page files and combined fragment verified against freeze manifest\n")
        handle.write(f"final package validated {utc}; 43 retained scans; 825 inventory rows all yes; 115 research items; final_validation.json passed\n")

    def package_files() -> list[Path]:
        found = []
        for path in sorted(ROOT.rglob("*")):
            relative = path.relative_to(ROOT)
            if not include_path(relative):
                continue
            require(not path.is_symlink(), f"Unexpected symbolic link: {relative}")
            if path.is_file():
                require(path.suffix.lower() in {"", ".tex", ".csv", ".md", ".log", ".json", ".py"},
                        f"Unexpected source/binary attachment: {relative}")
                found.append(path)
        return found

    archive_manifest = ROOT / "records/final_archive_manifest.json"
    members = [p for p in package_files() if p != archive_manifest]
    write_json(archive_manifest, {
        "created_utc": utc,
        "archive_name": f"{NAME}.zip",
        "manifest_scope": "All archive files except this self-referential manifest",
        "source_attachments_and_images_excluded": True,
        "files": {p.relative_to(ROOT).as_posix(): {"bytes": p.stat().st_size, "sha256": digest(p)}
                  for p in members},
    })
    members = package_files()
    output = ROOT.parent / f"{NAME}.zip"
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{NAME}_final_", suffix=".tmp", dir=ROOT.parent)
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with ZipFile(temporary, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            for path in members:
                archive.write(path, arcname=path.relative_to(ROOT).as_posix())
        with ZipFile(temporary) as archive:
            require(archive.testzip() is None, "ZIP CRC validation failed")
            require(archive.namelist() == [p.relative_to(ROOT).as_posix() for p in members],
                    "ZIP membership mismatch")
            for path in members:
                require(hashlib.sha256(archive.read(path.relative_to(ROOT).as_posix())).hexdigest() == digest(path),
                        f"Archived bytes differ: {path.name}")
        os.replace(temporary, output)
    finally:
        temporary.unlink(missing_ok=True)
    print(json.dumps({"result": "passed", "zip": str(output), "files": len(members),
                      "bytes": output.stat().st_size, "sha256": digest(output),
                      "frozen_files_unchanged": 44, "inventory_rows": 825,
                      "research_items": 115}, indent=2))


if __name__ == "__main__":
    main()
