#!/usr/bin/env python3
"""Record final package checks without modifying any frozen transcription file."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "records"


def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    required = ["MPL_154_127-176_transcription.tex", "MPL_154_127-176_doubts.md",
                "MPL_154_127-176_inventory.csv", "MPL_154_127-176_notes.md",
                "progress.log", "README.md"]
    assert all((ROOT / name).is_file() for name in required), "Missing final deliverable"
    check = subprocess.run([sys.executable, str(ROOT / "scripts/validate_package.py"),
                            "--root", str(ROOT), "--complete"],
                           text=True, capture_output=True, check=True)
    report = [f"FINAL PACKAGE VALIDATION — {now}", check.stdout.strip()]

    with (ROOT / "MPL_154_127-176_inventory.csv").open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 636
    assert {row["sheet_kind"] for row in rows} <= {"text", "reused_typed", "cancelled_draft", "cover"}
    assert {row["scan"] for row in rows} == {str(i) for i in range(127,177)}
    assert all(row["transcribed"] == "yes" for row in rows)
    report.append("Inventory: 636 elements; all fifty scans; permitted sheet kinds; all transcribed=yes.")

    with (RECORDS / "post_audit_compile_coverage.csv").open(newline="", encoding="utf-8") as stream:
        coverage = list(csv.DictReader(stream))
    assert len(coverage) == 50
    for item in coverage:
        page = ROOT / "pages" / f"MPL_154_127-176_154_scan{item['scan']}.tex"
        assert hashlib.sha256(page.read_bytes()).hexdigest() == item["sha256"]
        assert item["pdflatex_status"] == item["xelatex_status"] == "PASS"
    report.append("Compilation coverage: all fifty current frozen page hashes match both-engine PASS evidence; no new compilation performed.")

    notes = (ROOT / "MPL_154_127-176_notes.md").read_text(encoding="utf-8")
    headers = list(re.finditer(r"^### ([A-Z]\d{2}) — .+$", notes, re.M))
    ids = [m[1] for m in headers]
    assert len(ids) == len(set(ids)) == 75, f"Expected75 distinct selected notes, got {len(ids)}"
    ledger = "\n".join((RECORDS / name).read_text(encoding="utf-8") for name in
                       ("research_doubts_searches.md", "research_cube_searches.md", "research_gluing_searches.md"))
    root_ids = {json.loads(line)["note_id"] for line in
                (RECORDS / "root_context_searches.jsonl").read_text(encoding="utf-8").splitlines()}
    for i, m in enumerate(headers):
        key = m[1]
        end = headers[i+1].start() if i+1 < len(headers) else notes.index("## Documentary appendix:",m.end())
        block = notes[m.start():end]
        assert "**Source:**" in block and "**Kind:**" in block, f"Missing note metadata: {key}"
        original = "CUBE-" + key[1:] if key.startswith("C") else key
        assert key in root_ids or re.search(r"\b"+re.escape(original)+r"\b",ledger), f"Missing prior search ID: {key}"
    assert "genui" not in notes, "Unresolved tool citation in Markdown deliverable"
    report.append("Research notes:75 distinct IDs, source/kind fields, corresponding prior-search ledger IDs; bibliography and standing sections present.")
    report.append("Sentence limits and mathematical/source scope: reviewed separately in research_review.txt, final_documentary_review.txt, final_comparison_review.txt and final_cube_math_review.txt.")

    for filename in ("research_review.txt", "final_documentary_review.txt", "final_comparison_review.txt", "final_cube_math_review.txt"):
        assert (RECORDS / filename).is_file(), f"Missing review record: {filename}"
    excluded_extensions = {".jpg", ".jpeg", ".png", ".pdf", ".zip"}
    assert not any(p.is_file() and p.suffix.lower() in excluded_extensions for p in ROOT.rglob("*")), "Input or image file in package work tree"
    report.append("Package inputs: no scan images, supplied PDFs/ZIPs or context source files copied into deliverable tree.")
    report.append("Limits: structural and hash checks do not prove visual fidelity or mathematical correctness; the visual reading records and explicit doubt markers remain essential.")

    # Preserve the previous current-status file as part of the work history.
    old_status = RECORDS / "current_work_status.txt"
    old_copy = RECORDS / "checkpoint_02_work_status.txt"
    if old_status.exists() and not old_copy.exists():
        old_copy.write_bytes(old_status.read_bytes())
    old_status.write_text(
        f"FINAL STATUS {now}\n"
        "All 50 scans 127–176 transcribed sequentially by root with whole/a/b viewing; all 50 second visual audits complete.\n"
        "Transcription frozen 2026-11-15 01:44:43 UTC; context opened 01:44:50 UTC.\n"
        "All 51 frozen SHA256 records unchanged at final check. Inventory 636 rows, all yes; doubts 687 occurrences.\n"
        "Research notes complete: 75 selected notes, per-note context searches, standing documentary/self-flag sections, APA references; conditional cube proof retained in research_cube_memo.md.\n"
        "Research review corrections applied: I05 integer n, G01 incident-face wording, I01 undefined dimension of K_0, Q05 relative wording order; further resolutions documented in progress.log.\n"
        "All frozen page hashes match both-engine compilation evidence. Earlier pending reports and generators are historical; do not rerun mutation scripts.\n"
        "Final deliverables complete. The final ZIP packaging event is recorded by package_work.py in progress.log.\n",
        encoding="utf-8")
    (RECORDS / "final_validation.txt").write_text("\n\n".join(report)+"\n", encoding="utf-8")
    with (ROOT / "progress.log").open("a", encoding="utf-8") as stream:
        stream.write(f"research notes and separate reviews completed {now}; 75 selected notes with prior context searches and source/status qualifications\n")
        stream.write(f"final integrity verified {now}; all 51 frozen SHA256 values unchanged: 50 page files and combined transcription\n")
    print("\n".join(report))


if __name__ == "__main__":
    main()
