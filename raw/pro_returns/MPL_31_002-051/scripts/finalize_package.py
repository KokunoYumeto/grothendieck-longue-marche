#!/usr/bin/env python3
"""Verify frozen deliverables, record completion, and assemble one ZIP.

This script never writes a transcription fragment. It reads existing generated
records and invokes the read-only final validator; no supplied image or original
context file is read.
"""
from __future__ import annotations
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

PREFIX = "MPL_31_002-051"
SCANS = [n for n in range(2, 52) if n not in {34, 40, 41, 46}]


def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root.parent / f"{PREFIX}.zip").resolve()
    if output.exists():
        raise SystemExit(f"Output already exists: {output}")
    if output.is_relative_to(root):
        raise SystemExit("The output ZIP must be outside the package directory.")
    records = root / "records"
    frozen = load(records / "frozen_sha256.json")
    expected_paths = {f"pages/{PREFIX}_31_scan{n:03d}.tex" for n in SCANS}
    expected_paths.add(f"{PREFIX}_transcription.tex")
    assert set(frozen["files"]) == expected_paths

    def verify_frozen():
        mismatches = [name for name, digest in frozen["files"].items() if sha(root / name) != digest]
        assert not mismatches, mismatches
        return len(frozen["files"])

    assert verify_frozen() == 47
    syntax = load(records / "latex_syntax_check.json")
    assert syntax["compiled"] == syntax["passed"] == 46
    assert not syntax["source_changes_during_run"]
    assert all(digest == frozen["files"]["pages/" + name]
               for name, digest in syntax["source_hashes_at_end"].items())
    assert len(syntax["source_hashes_at_end"]) == 46

    items = load(records / "research_items.json")["items"]
    searches = load(records / "context_searches.json")
    registry = load(records / "results_state_coverage.json")["entries"]
    research_review = load(records / "research_structure_check.json")
    assert research_review["status"] == "passed"
    reviewed_files = [
        "records/research_items.json",
        "records/context_searches.json",
        "records/results_state_coverage.json",
        "records/primary_sources.json",
        f"{PREFIX}_notes.md",
    ]
    assert all(sha(root / name) == research_review["file_hashes_after"][name]
               for name in reviewed_files), "Research structure report needs refreshing."
    ids = [item["id"] for item in items]
    assert len(ids) == len(set(ids)) == 101
    assert sum(i.startswith("N") for i in ids) == 94
    assert sum(i.startswith("T") for i in ids) == 7
    assert {q["item"] for q in searches["note_searches"]} == set(ids)
    assert len(searches["note_searches"]) == 101
    assert len(searches["register_coverage_searches"]) == len(registry) == 26
    search_records = []
    for query in searches["note_searches"]:
        search_records.append(query["object_search"])
        search_records.extend(query["id_searches"])
    search_records.extend(query["search"] for query in searches["register_coverage_searches"])
    assert len(search_records) == 255
    assert all(q["return_code"] in {0, 1} for q in search_records)
    own_ideas = [i for i in items if i.get("confidence") is not None]
    assert len(own_ideas) == 16 and all(i.get("reason") for i in own_ideas)
    with (root / f"{PREFIX}_inventory.csv").open(encoding="utf-8-sig", newline="") as handle:
        inventory = list(csv.DictReader(handle))
    assert len(inventory) == 1177 and all(row["transcribed"] == "yes" for row in inventory)
    doubt_macros = sum(len(re.findall(r"\\(?:unsure|illegible)\b",
                                     (root / f"pages/{PREFIX}_31_scan{n:03d}.tex").read_text(encoding="utf-8")))
                       for n in SCANS)
    assert doubt_macros == 449

    with (root / "progress.log").open("a", encoding="utf-8") as log:
        log.write(f"final transcription hashes verified unchanged {utc()} files=47/47\n")
    run = subprocess.run(
        [sys.executable, str(root / "scripts/validate_package.py"), str(root), "--phase", "final"],
        text=True, capture_output=True, check=False
    )
    if run.returncode:
        raise RuntimeError(run.stdout + run.stderr)
    validation = json.loads(run.stdout)
    assert validation["status"] == "passed", validation["issues"]
    assert verify_frozen() == 47
    validation["final_dossier_checks"] = {
        "retained_scans": 46,
        "inventory_rows": 1177,
        "all_inventory_rows_transcribed_yes": True,
        "doubt_macros": 449,
        "research_items": 101,
        "substantive_items": 94,
        "title_and_count_items": 7,
        "own_idea_items_with_confidence_and_reason": 16,
        "per_item_context_queries": 101,
        "selected_register_entries_with_dispositions": 26,
        "individual_rg_executions_recorded": 255,
        "compiled_frozen_page_files": 46,
        "compiled_page_hashes_match_frozen_files": True,
        "frozen_files_verified": 47,
        "research_structure_report_matches_final_research_files": True,
    }
    write_json(records / "final_validation.json", validation)
    completed = utc()
    (records / "work_state.md").write_text(
        "# Completed work state\n\n"
        "All 46 retained scans have completed the sequential direct reading and "
        "the second visual audit. Every whole image and both supplied halves were "
        "examined by the primary reader; no manuscript OCR or delegation of manuscript "
        "or supplied-context reading was used.\n\n"
        "The 47 transcription files were frozen at 2026-11-16 23:40:30 UTC. "
        "Context opened at 23:40:37 UTC. Every frozen SHA-256 remains unchanged. "
        "The combined file, 46 page fragments, 449-entry doubts register and 1,177-row "
        "inventory are complete. All inventory rows are marked yes.\n\n"
        "Research is complete: 94 substantive items and seven title/count items, "
        "101 per-item context searches, 255 recorded rg executions, 26 register-entry "
        "dispositions, and 15 primary-source entries. The 16 own-idea items have "
        "confidence and reasons. The supplied context's truncated excerpts and "
        "attributed statuses remain explicit in the notes.\n\n"
        "The final read-only validator passed. The 46 successful syntax compilations "
        "are tied to the frozen page hashes. The final research-structure report "
        "matches the delivered research files. No requested work remains pending.\n\n"
        "Hourly checkpoints 01 and 02 were saved at 2026-11-16 22:42:34 UTC and "
        "23:42:33 UTC. This final package was completed before the next hourly "
        "checkpoint was due. Supplied source archives, images and original context "
        "files are omitted from the deliverable; generated work records and scripts "
        "are retained.\n\n"
        f"Completed UTC: {completed}\n",
        encoding="utf-8"
    )
    with (root / "progress.log").open("a", encoding="utf-8") as log:
        log.write(f"final package validation passed {completed} pages=46 inventory_yes=1177 "
                  "doubts=449 research_items=101 per_item_context_queries=101 registry_entries=26\n")
        log.write(f"final transcription hash check unchanged {utc()} page_files=46 combined=1 "
                  "matched_frozen_SHA256=47/47\n")
        log.write(f"deliverables completed {utc()}; final ZIP assembly started\n")

    manifest_path = records / "package_manifest.json"
    files = sorted(p for p in root.rglob("*")
                   if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
                   and p != manifest_path)
    assert not any(p.suffix.lower() in {".jpg", ".jpeg", ".png", ".pdf", ".zip"} for p in files)
    manifest = {
        "created_utc": utc(),
        "archive": output.name,
        "scope": "All delivered files except this manifest itself.",
        "excluded": ["__pycache__ directories", "*.pyc", "supplied source archives and original inputs"],
        "files": [{"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size,
                   "sha256": sha(p)} for p in files],
    }
    write_json(manifest_path, manifest)
    files.append(manifest_path)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(files):
            archive.write(path, path.relative_to(root).as_posix())
    with zipfile.ZipFile(output, "r") as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(files)
        for item in manifest["files"]:
            data = archive.read(item["path"])
            assert len(data) == item["bytes"]
            assert hashlib.sha256(data).hexdigest() == item["sha256"]
        for name, digest in frozen["files"].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest
    assert verify_frozen() == 47
    print(json.dumps({
        "status": "passed", "zip": str(output), "bytes": output.stat().st_size,
        "sha256": sha(output), "files": len(files), "zip_crc": "passed",
        "manifest_hashes": "all matched", "frozen_hashes_in_zip": "47/47 unchanged",
        "completed_utc": utc()
    }, indent=2))


if __name__ == "__main__":
    main()
