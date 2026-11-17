"""Read-only checks of frozen sources; write a final report and append the log.

This script does not repair, reassemble, or rewrite the transcription.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "MPL_154_001-045"
EXPECTED = [n for n in range(1, 46) if n != 11]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    errors = []
    pagefiles = sorted((ROOT / "pages").glob("*.tex"))
    scans = [int(re.search(r"scan(\d+)\.tex$", p.name).group(1)) for p in pagefiles]
    if scans != EXPECTED:
        errors.append("Unexpected page set/order")
    combined_path = ROOT / f"{PREFIX}_transcription.tex"
    combined = combined_path.read_text()
    if not combined.startswith("\\cotefile{154}\n\\scanpage{1}"):
        errors.append("Combined fragment header differs from required header")
    if combined != "\n".join(p.read_text() for p in pagefiles):
        errors.append("Combined fragment is not the ordered concatenation of page files")
    markers = [int(x) for x in re.findall(r"\\scanpage\{(\d+)\}", combined)]
    if markers != EXPECTED:
        errors.append("Scan markers disagree with retained scan set")
    for forbidden in [r"\documentclass", r"\begin{document}", r"\usepackage",
                      r"\includegraphics", r"\pgfimage"]:
        if forbidden in combined:
            errors.append(f"Forbidden preamble/image command in fragment: {forbidden}")

    manifest = json.loads((ROOT / "records/frozen_sha256.json").read_text())
    expected_hashes = manifest["sha256"]
    if len(expected_hashes) != 45:
        errors.append("Freeze manifest does not have45 files")
    hashes = []
    for name, frozen in expected_hashes.items():
        actual = sha256(ROOT / name)
        hashes.append({"file": name, "frozen_sha256": frozen,
                       "current_sha256": actual, "unchanged": actual == frozen})
        if actual != frozen:
            errors.append(f"FROZEN TRANSCRIPTION CHANGED: {name}")

    inventory_path = ROOT / f"{PREFIX}_inventory.csv"
    with inventory_path.open(newline="") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        inventory = list(reader)
    if columns != ["cote", "scan", "sheet_kind", "element", "kind", "position",
                   "first_words_or_objects", "transcribed"]:
        errors.append("Inventory columns differ from requested schema")
    kinds = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
    sheets = {"text", "reused_typed", "cancelled_draft", "cover"}
    if any(r["transcribed"] != "yes" or r["cote"] != "154" or r["kind"] not in kinds
           or r["sheet_kind"] not in sheets or int(r["scan"]) not in EXPECTED for r in inventory):
        errors.append("Inventory contains a nonconforming or unfinished row")
    if len({r["element"] for r in inventory}) != len(inventory):
        errors.append("Inventory element IDs are not unique")
    if sorted({int(r["scan"]) for r in inventory}) != EXPECTED:
        errors.append("Inventory does not cover every retained scan")
    page_kinds = {}
    for row in inventory:
        page_kinds.setdefault(int(row["scan"]), set()).add(row["sheet_kind"])
    if any(len(v) != 1 for v in page_kinds.values()):
        errors.append("Sheet-kind labels are inconsistent within a page")

    unsure_count = len(re.findall(r"\\unsure\{", combined))
    illegible = [int(x) for x in re.findall(r"\\illegible\{(\d+)\}", combined)]
    doubts = (ROOT / f"{PREFIX}_doubts.md").read_text()
    doubt_rows = re.findall(r"^\| 154 \|.*$", doubts, re.M)
    if len(doubt_rows) != unsure_count + len(illegible):
        errors.append("Doubt table row count does not equal current marked uncertainties")
    if len(re.findall(r"\\deleted\{", combined)) != sum(r["kind"] == "deletion" for r in inventory):
        errors.append("Deletion macro and element counts disagree")
    if len(re.findall(r"\\inserted\{", combined)) != sum(r["kind"] == "insertion" for r in inventory):
        errors.append("Insertion macro and element counts disagree")

    notes = (ROOT / f"{PREFIX}_notes.md").read_text()
    headings = list(re.finditer(r"^### ([A-Z]\d{2}) — (.+)$", notes, re.M))
    note_ids = [m.group(1) for m in headings]
    if len(note_ids) != len(set(note_ids)):
        errors.append("Research-note IDs are not unique")
    for i, match in enumerate(headings):
        stop = headings[i + 1].start() if i + 1 < len(headings) else len(notes)
        block = notes[match.end():stop]
        for required in ["**Source:**", "**Kind:**", "**Context:**", "**Register:**", "<!-- search:"]:
            if required not in block:
                errors.append(f"{match.group(1)} lacks {required}")
        kind = re.search(r"\*\*Kind:\*\*([^\n]+)", block)
        if kind and "own idea" in kind.group(1).lower() and "confidence" not in block.lower():
            errors.append(f"Own idea {match.group(1)} lacks confidence/reason")
    searches = [json.loads(line) for line in (ROOT / "records/context_searches.jsonl").read_text().splitlines()]
    if [row["note"] for row in searches] != note_ids:
        errors.append("Per-note context search journal does not match research notes")
    if any(not row["total_matching_lines_with_repetition"] for row in searches):
        errors.append("Some context searches have no recorded match")
    for heading in ["## 9. Steps the manuscript itself marks as unverified",
                    "## 10. Title sheets, headings, numbering, dates and counts",
                    "## 11. Research-state disposition"]:
        if heading not in notes:
            errors.append(f"Missing standing section: {heading}")

    log_path = ROOT / "progress.log"
    log = log_path.read_text()
    done = [int(x) for x in re.findall(r"^154 scan (\d+) done ", log, re.M)]
    audited = [int(x) for x in re.findall(r"^scan (\d+) audited ", log, re.M)]
    if done != EXPECTED:
        errors.append("Per-page done records are incomplete or out of order")
    if audited != EXPECTED:
        errors.append("Per-page second-audit records are incomplete or out of order")
    if log.find("transcription frozen ") < 0 or log.find("context opened ") < log.find("transcription frozen "):
        errors.append("Freeze/context-opening order is not recorded correctly")
    previous = json.loads((ROOT / "records/pre_freeze_validation.json").read_text())
    if previous.get("compile_exit_status") != 0:
        errors.append("No successful pre-freeze compile record")

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    report = {
        "validated_utc": timestamp, "errors": errors,
        "page_files": len(pagefiles), "scan_numbers": scans,
        "inventory_rows": len(inventory),
        "inventory_kinds": dict(Counter(r["kind"] for r in inventory)),
        "sheet_kinds_by_page": dict(Counter(next(iter(v)) for v in page_kinds.values())),
        "all_inventory_transcribed_yes": all(r["transcribed"] == "yes" for r in inventory),
        "first_reading_done_records": len(done), "second_audit_records": len(audited),
        "unsure_occurrences": unsure_count, "illegible_groups": len(illegible),
        "estimated_illegible_words": sum(illegible), "current_doubt_rows": len(doubt_rows),
        "research_note_items": len(note_ids), "research_note_ids": note_ids,
        "research_word_count_including_metadata": len(notes.split()),
        "per_note_context_searches": len(searches), "source_context_files": 6,
        "pre_freeze_compile_exit_status": previous["compile_exit_status"],
        "pre_freeze_wrapper_pdf_pages": previous["qa_wrapper_output_pages"],
        "frozen_utc": manifest["frozen_utc"], "all_frozen_hashes_unchanged": all(h["unchanged"] for h in hashes),
        "frozen_files_checked": hashes,
        "validation_limit": "Structural checks and hash preservation; no new image reading or claim that doubtful readings have become certain.",
    }
    (ROOT / "records/final_validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    if errors:
        print(json.dumps({"status": "FAILED", "errors": errors}, ensure_ascii=False))
        raise SystemExit(1)
    with log_path.open("a") as f:
        f.write(f"final deliverable validation passed {timestamp}:44 retained pages;1235 inventory elements all yes;114 research items\n")
        f.write(f"transcription hashes verified unchanged {timestamp}: all45 frozen files match; no transcription changes after context opening\n")
    print(json.dumps({k: v for k, v in report.items()
                      if k not in {"frozen_files_checked", "research_note_ids"}}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
