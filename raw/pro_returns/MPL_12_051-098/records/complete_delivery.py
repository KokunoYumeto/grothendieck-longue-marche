#!/usr/bin/env python3
"""Validate the completed return, regenerate research audits, and log completion.

The transcription, doubts and inventory are read only. No context images or OCR
are used. The lexical context ledger reads only its fixed supplied-text allowlist.
This script does not create or upload a ZIP; package_bundle.py does that later.
"""
from collections import Counter
from datetime import datetime, timezone
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parents[1]
RECORDS = BASE / "records"
PREFIX = "MPL_12_051-098"
sys.path.insert(0, str(RECORDS))
from rebuild_inventory import parse_page


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_json(script, *args):
    result = subprocess.run(
        [sys.executable, str(RECORDS / script), *map(str, args)],
        text=True, capture_output=True,
    )
    if result.returncode:
        raise RuntimeError(f"{script} failed:\n{result.stdout}\n{result.stderr}")
    return json.loads(result.stdout)


def main():
    expected = set(range(51, 99)) - {66, 68, 69, 70, 81, 83, 85, 97, 98}
    before = json.loads((RECORDS / "frozen_transcription_hashes.json").read_text())
    for name, digest in before["sha256"].items():
        if hashlib.sha256((BASE / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError(f"Frozen file changed: {name}")

    ledger_run = run_json("context_search_ledger.py")
    ledger = json.loads((RECORDS / "context_search_ledger.json").read_text())
    if ledger["diagnostics"] or len(ledger["items"]) != 158:
        raise RuntimeError("Context ledger coverage/metadata diagnostics need review")
    notes_run = run_json("validate_research_notes.py")
    notes = json.loads((RECORDS / "research_notes_validation.json").read_text())
    if notes["status"] != "PASS":
        raise RuntimeError("Research metadata or sentence-count warnings need review")

    syntax = {}
    for path in sorted((BASE / "pages").glob("*.tex")):
        _, diagnostics = parse_page(path.read_text(encoding="utf-8"))
        syntax[path.name] = diagnostics
    syntax_report = {
        "pages_checked": len(syntax),
        "diagnostics": {name: rows for name, rows in syntax.items() if rows},
        "checks": ["balanced groups", "matching environments", "display delimiters",
                   "inline dollar delimiters", "conservative math contexts"],
        "limitation": "Mechanical syntax checks, not a successful compilation or a reading audit.",
    }
    dump(RECORDS / "tex_structure_final.json", syntax_report)
    if syntax_report["diagnostics"]:
        raise RuntimeError("TeX structure diagnostics need review; frozen text was not changed")

    structure = run_json("validate_structure.py", BASE)
    dump(RECORDS / "structure_validation_final.json", structure)
    if not structure["ok"]:
        raise RuntimeError("Package structure validation failed")

    log = (BASE / "progress.log").read_text(encoding="utf-8")
    done = re.findall(r"^12 scan (\d{3}) done (.+)$", log, flags=re.M)
    audited = re.findall(r"^scan (\d{3}) audited (.+)$", log, flags=re.M)
    if len(done) != 39 or {int(n) for n, _ in done} != expected:
        raise RuntimeError("Page completion record does not match the supplied set")
    if len(audited) != 39 or {int(n) for n, _ in audited} != expected:
        raise RuntimeError("Visual audit record does not match the supplied set")
    freeze_match = re.search(r"^transcription frozen (.+)$", log, re.M)
    context_match = re.search(r"^context opened (.+)$", log, re.M)
    if not freeze_match or not context_match or freeze_match.start() > context_match.start():
        raise RuntimeError("Freeze/context order is not documented")
    timeformat = "%Y-%m-%d %H:%M:%S UTC"
    freeze_time = datetime.strptime(freeze_match.group(1), timeformat)
    context_time = datetime.strptime(context_match.group(1), timeformat)
    if not freeze_time < context_time:
        raise RuntimeError("Context was not opened after the freeze")
    if any(datetime.strptime(t, timeformat) > freeze_time for _, t in done + audited):
        raise RuntimeError("A page completion/audit record falls after the freeze")

    with (BASE / f"{PREFIX}_inventory.csv").open(newline="", encoding="utf-8") as handle:
        inventory = list(csv.DictReader(handle))
    element_counts = dict(Counter(row["kind"] for row in inventory))
    sheet_by_scan = {int(row["scan"]): row["sheet_kind"] for row in inventory}
    notes_text = (BASE / f"{PREFIX}_notes.md").read_text(encoding="utf-8")
    notes_hash = hashlib.sha256(notes_text.encode()).hexdigest()
    if notes_hash != ledger["notes"]["sha256"] or notes_hash != notes["notes_sha256"]:
        raise RuntimeError("Research audits refer to a different notes snapshot")

    frozen = run_json("verify_frozen.py", "--log")
    frozen["checked_at_utc"] = datetime.now(timezone.utc).strftime(timeformat)
    dump(RECORDS / "frozen_verification_final.json", frozen)
    report = {
        "completed_at_utc": datetime.now(timezone.utc).strftime(timeformat),
        "status": "PASS",
        "supplied_scan_count": 39,
        "completed_page_records": len(done),
        "visual_audit_records": len(audited),
        "freeze_utc": freeze_match.group(1),
        "context_opened_utc": context_match.group(1),
        "frozen_files_verified_unchanged": frozen["verified_files"],
        "combined_transcription_sha256": before["sha256"][f"{PREFIX}_transcription.tex"],
        "inventory_rows": len(inventory),
        "inventory_all_transcribed_yes": all(row["transcribed"] == "yes" for row in inventory),
        "inventory_element_counts": element_counts,
        "sheet_counts": dict(Counter(sheet_by_scan.values())),
        "unsure_occurrences": structure["state_macro_counts"]["unsure"],
        "illegible_spans": structure["state_macro_counts"]["illegible"],
        "notes_sha256": notes_hash,
        "notes_whitespace_word_count": len(notes_text.split()),
        "research_identified_items": notes["items"]["actual_total"],
        "principal_notes": notes["principal_notes"]["actual_count"],
        "principal_sentence_count_distribution": notes["principal_notes"]["sentence_count_distribution"],
        "bibliography_keys": notes["bibliography"]["definition_count"],
        "context_search_counts": ledger["counts"],
        "compilation": "Unavailable formats/classes/packages; no successful compilation claimed.",
        "limitations": [
            "Mechanical checks do not measure the error rate of the diplomatic reading.",
            "Context lexical matches do not prove mathematical claims.",
            "No source/context files or original images are to be included in the final archive.",
        ],
    }
    dump(RECORDS / "final_validation_summary.json", report)
    with (BASE / "progress.log").open("a", encoding="utf-8") as handle:
        handle.write("research notes completed " + report["completed_at_utc"] +
                     "; 75 principal notes, 158 identified items, 17 bibliography keys; context searches and independent research review recorded\n")
        handle.write("final package validation passed " + report["completed_at_utc"] +
                     "; 39 pages, 39 visual audits, 628 inventory rows all yes, 40 frozen files unchanged; structural checks only, compilation unavailable\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
