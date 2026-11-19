#!/usr/bin/env python3
"""Generate a mechanical C-to-final comparison and C-doubt audit worksheet.

No manuscript reading or content judgment is performed. Character alignment
only proposes the corresponding final span; every changed span requires human
or visual-reader review. Without --report-prefix, only aggregate counts and
workflow gaps are printed. --report-prefix PATH writes PATH.json,
PATH_unsure.tsv, PATH.diff, and PATH.md. No page or record is ever modified.
The TSV is the canonical place for ink_disposition, crop_links, reviewed_by,
reviewed_utc and review_note annotations. Those fields survive regeneration
when the stable occurrence id and exact source token still match.
If a reviewed candidate span subsequently changes, alignment_recheck_required
is set to yes without changing the reviewer's fields. The reviewer may clear
that flag after checking the new alignment.

Examples:
  python out/scripts/audit_source_c.py --scan 2 --report-prefix out/audit/C_scan002
  python out/scripts/audit_source_c.py --report-prefix out/audit/C_all
"""
from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = ROOT / "out"
DEFAULT_WITNESSES = ROOT / "source/SP31_CW_156-3_witnesses"


def mask_comments(tex: str) -> str:
    """Mask TeX comments but preserve character positions and line breaks."""
    chars = list(tex)
    i = 0
    while i < len(chars):
        if chars[i] == "\\":
            # A TeX control symbol consumes the next character, including %.
            if i + 1 < len(chars) and not chars[i + 1].isalpha():
                i += 2
            else:
                i += 1
        elif chars[i] == "%":
            while i < len(chars) and chars[i] != "\n":
                chars[i] = " "
                i += 1
        else:
            i += 1
    return "".join(chars)


def macro_occurrences(tex: str, macro: str = "unsure") -> list[dict]:
    masked = mask_comments(tex)
    result = []
    i = 0
    while i < len(masked):
        if masked[i] != "\\":
            i += 1
            continue
        match = re.match(r"\\([A-Za-z@]+)", masked[i:])
        if not match:
            i += 2
            continue
        start = i
        i += len(match.group(0))
        if match.group(1) != macro:
            continue
        j = i
        while j < len(masked) and masked[j].isspace():
            j += 1
        if j == len(masked) or masked[j] != "{":
            continue
        arg_start = j + 1
        depth = 1
        j += 1
        while j < len(masked) and depth:
            if masked[j] == "\\" and j + 1 < len(masked) and not masked[j + 1].isalpha():
                j += 2
                continue
            if masked[j] == "{":
                depth += 1
            elif masked[j] == "}":
                depth -= 1
            j += 1
        if depth:
            result.append({"start": start, "end": len(tex), "argument": tex[arg_start:],
                           "line": tex.count("\n", 0, start) + 1, "malformed": True})
        else:
            result.append({"start": start, "end": j, "argument": tex[arg_start:j - 1],
                           "line": tex.count("\n", 0, start) + 1, "malformed": False})
        # Continue after the command itself, so nested macros are enumerated too.
    return result


def aligned_span(start: int, end: int, opcodes: list[tuple]) -> tuple[int, int, bool]:
    for tag, i1, i2, j1, _ in opcodes:
        if tag == "equal" and i1 <= start and end <= i2:
            return j1 + start - i1, j1 + end - i1, True
    spans = []
    for tag, i1, i2, j1, j2 in opcodes:
        if i1 == i2:
            if start <= i1 < end:
                spans.append((j1, j2))
        elif max(start, i1) < min(end, i2):
            if tag == "equal":
                spans.append((j1 + max(start, i1) - i1, j1 + min(end, i2) - i1))
            else:
                spans.append((j1, j2))
    if spans:
        return min(s[0] for s in spans), max(s[1] for s in spans), False
    return 0, 0, False


def workflow_gaps(out: Path, scans: list[int]) -> list[str]:
    gaps = []
    log_path = out / "progress.log"
    if not log_path.exists():
        return ["progress.log is missing"]
    log = log_path.read_text(encoding="utf-8")
    first = log.splitlines()[0] if log.splitlines() else ""
    if not re.fullmatch(r"\d{4}-\d\d-\d\d[ T]\d\d:\d\d:\d\d(?: UTC|Z|\+00:00)", first):
        gaps.append("progress.log first line is not a recognized UTC timestamp")
    for scan in scans:
        for phase in ("done", "audited"):
            if not re.search(rf"(?m)^scan {scan:03d} {phase} .+$", log):
                gaps.append(f"scan {scan:03d}: missing {phase} record")
    if "transcription frozen " not in log:
        gaps.append("transcription freeze not yet recorded")
    if "context opened " in log:
        if "transcription frozen " not in log or log.index("context opened ") < log.index("transcription frozen "):
            gaps.append("ERROR: context opening is not preceded by recorded freeze")
    return gaps


def apply_review_coverage(report: dict) -> None:
    """Accept complete occurrence evidence without changing any ink judgment."""
    required=['ink_disposition','crop_links','reviewed_by','review_note']
    by_scan={}
    for row in report['unsure_occurrences']:
        complete=all(str(row.get(k) or '').strip() for k in required) and row.get('alignment_recheck_required')!='yes'
        by_scan.setdefault(int(row['scan']),[]).append(complete)
    complete_scans={scan for scan,states in by_scan.items() if states and all(states)}
    gaps=[]
    for gap in report['workflow_gaps']:
        match=re.match(r'^scan (\d+): \d+ source C unsure occurrences, \d+ recorded decisions;',gap)
        if match and int(match.group(1)) in complete_scans:continue
        gaps.append(gap)
    report['workflow_gaps']=gaps
    report['summary']['workflow_gap_count']=len(gaps)
    report['summary']['root_evidence_complete_occurrences']=sum(sum(states) for states in by_scan.values())
    report['summary']['root_evidence_complete_pages']=len(complete_scans)
    for page in report['pages']:
        page['complete_root_occurrence_evidence']=page['scan'] in complete_scans


def make_report(out: Path, witnesses: Path, selected: list[int] | None, completed_only: bool = False) -> dict:
    with (witnesses / "page_map.tsv").open(encoding="utf-8", newline="") as f:
        page_map = {int(r["our_scan"]): r for r in csv.DictReader(f, delimiter="\t")}
    scans = sorted(selected if selected else page_map)
    if completed_only:
        scans = [s for s in scans if (out / "pages" / Path(page_map[s]["codex_file"]).name).exists()]
    report = {"caution": "Mechanical alignment is a review aid, not a reading decision or proof check.",
              "pages": [], "unsure_occurrences": [], "workflow_gaps": workflow_gaps(out, scans)}
    changes_path = out / "SP31_CW_156-3_changes.md"
    changes = changes_path.read_text(encoding="utf-8") if changes_path.exists() else ""
    for scan in scans:
        mapping = page_map[scan]
        filename = Path(mapping["codex_file"]).name
        source = (witnesses / mapping["codex_file"]).read_text(encoding="utf-8")
        source_marks = macro_occurrences(source)
        target_path = out / "pages" / filename
        record_path = out / "records" / f"{scan:03d}.json"
        record = json.loads(record_path.read_text(encoding="utf-8")) if record_path.exists() else {}
        decisions = record.get("decisions", [])
        page = {"scan": scan, "filename": filename, "source_unsure_count": len(source_marks),
                "manual_decision_count": len(decisions), "final_exists": target_path.exists(),
                "change_log_section_present": bool(re.search(rf"(?m)^### Scan {scan:03d}\b", changes)),
                "manual_decision_count_matches_source": len(decisions) == len(source_marks)}
        if not page["manual_decision_count_matches_source"]:
            report["workflow_gaps"].append(f"scan {scan:03d}: {len(source_marks)} source C unsure occurrences, {len(decisions)} recorded decisions; verify mapping manually")
        if not page["change_log_section_present"]:
            report["workflow_gaps"].append(f"scan {scan:03d}: changes-log section missing")
        target = target_path.read_text(encoding="utf-8") if target_path.exists() else ""
        target_marks = macro_occurrences(target)
        page["final_unsure_count"] = len(target_marks)
        page["byte_identical"] = target_path.exists() and (witnesses / mapping["codex_file"]).read_bytes() == target_path.read_bytes()
        page["diff"] = "".join(difflib.unified_diff(source.splitlines(keepends=True), target.splitlines(keepends=True),
                                                    fromfile="C/" + filename, tofile="consolidated/" + filename))
        opcodes = difflib.SequenceMatcher(None, source, target, autojunk=False).get_opcodes()
        page["changed_alignment_blocks"] = sum(op[0] != "equal" for op in opcodes)
        for index, mark in enumerate(source_marks, 1):
            j1, j2, exact = aligned_span(mark["start"], mark["end"], opcodes)
            candidates = [x for x in target_marks if (max(j1, x["start"]) < min(j2, x["end"]))
                          or (j1 == j2 and x["start"] <= j1 < x["end"])]
            if not target_path.exists():
                state = "final page missing"
            elif exact:
                state = "same unsure token in equal alignment"
            elif candidates:
                state = "unsure token(s) overlap changed alignment; inspect"
            else:
                state = "no unsure token in aligned span; inspect replacement"
            category = ("final-missing" if not target_path.exists() else "unchanged" if exact else
                        "changed-ambiguous" if candidates else "resolved-to-unmarked (candidate)" if target[j1:j2].strip() else
                        "empty-aligned-span (review)")
            row = {"occurrence_id": f"C-{scan:03d}-U{index:03d}", "scan": scan, "source_occurrence": index, "source_line": mark["line"],
                   "source_token": source[mark["start"]:mark["end"]],
                   "source_context": source[max(0,mark["start"]-100):min(len(source),mark["end"]+100)],
                   "source_argument": mark["argument"], "mechanical_state": state,
                   "mechanical_category": category,
                   "classification_scope": "TeX tokens only; no ink resolution or confidence inferred",
                   "final_line": target.count("\n", 0, j1) + 1 if target_path.exists() else "",
                   "final_aligned_text": target[j1:j2],
                   "final_unsure_arguments": " || ".join(x["argument"] for x in candidates),
                   "final_context": target[max(0, j1 - 100):min(len(target), j2 + 100)],
                   "recorded_decision_same_ordinal": decisions[index - 1] if len(decisions)==len(source_marks) else "NOT MAPPED: decision and occurrence counts differ; grouped decisions require explicit mapping",
                   "source_malformed": mark["malformed"], "ink_disposition": "", "crop_links": "",
                   "reviewed_by": "", "reviewed_utc": "", "review_note": "", "alignment_recheck_required": ""}
            report["unsure_occurrences"].append(row)
        report["pages"].append(page)
    report["summary"] = {"pages_examined_mechanically": len(scans), "final_pages_present": sum(p["final_exists"] for p in report["pages"]),
                         "source_c_unsure_occurrences": len(report["unsure_occurrences"]),
                         "mechanical_states": dict(Counter(r["mechanical_state"] for r in report["unsure_occurrences"])),
                         "workflow_gap_count": len(report["workflow_gaps"])}
    canonical_ledger=out/'audit/source_C_unsure.tsv'
    if canonical_ledger.exists():
        with canonical_ledger.open(encoding='utf-8',newline='') as f:
            previous={r.get('occurrence_id',''):r for r in csv.DictReader(f,delimiter='\t')}
        for row in report['unsure_occurrences']:
            old=previous.get(row['occurrence_id'])
            if old and old.get('source_token')==row['source_token']:
                for key in ['ink_disposition','crop_links','reviewed_by','reviewed_utc','review_note','alignment_recheck_required']:
                    row[key]=old.get(key,'')
    apply_review_coverage(report)
    return report


def write_reports(prefix: Path, report: dict) -> None:
    prefix.parent.mkdir(parents=True, exist_ok=True)
    rows = report["unsure_occurrences"]
    ledger_path=Path(str(prefix) + "_unsure.tsv")
    if ledger_path.exists():
        with ledger_path.open(encoding="utf-8", newline="") as f:
            previous={r.get("occurrence_id", ""):r for r in csv.DictReader(f,delimiter="\t")}
        for row in rows:
            old=previous.get(row["occurrence_id"])
            if old and old.get("source_token")==row["source_token"]:
                for key in ["ink_disposition","crop_links","reviewed_by","reviewed_utc","review_note"]:
                    row[key]=old.get(key,"")
                row["alignment_recheck_required"]=old.get("alignment_recheck_required","")
                if any(old.get(key,"").strip() for key in ["ink_disposition","reviewed_by","reviewed_utc"]):
                    if any(old.get(key,"")!=row.get(key,"") for key in ["final_aligned_text","final_unsure_arguments","mechanical_category"]):
                        row["alignment_recheck_required"]="yes"
    report["summary"]["ink_dispositions_filled"]=sum(bool(r.get("ink_disposition")) for r in rows)
    report["summary"]["alignment_rechecks_flagged"]=sum(r.get("alignment_recheck_required")=="yes" for r in rows)
    apply_review_coverage(report)
    Path(str(prefix) + ".json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = ["occurrence_id", "scan", "source_occurrence", "source_line", "source_token", "source_context", "source_argument",
              "mechanical_category", "mechanical_state", "classification_scope", "final_line", "final_aligned_text",
              "final_unsure_arguments", "final_context", "recorded_decision_same_ordinal", "source_malformed",
              "ink_disposition", "crop_links", "reviewed_by", "reviewed_utc", "review_note", "alignment_recheck_required"]
    with Path(str(prefix) + "_unsure.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    Path(str(prefix) + ".diff").write_text("\n".join(p["diff"] for p in report["pages"]), encoding="utf-8")
    lines = ["# Source C mechanical audit worksheet", "", report["caution"], "",
             "Grouped decisions are not assigned to individual occurrences by ordinal. A candidate unmarked alignment is not an ink-resolution judgment. Add ink dispositions and crop links to the TSV; those review fields survive regeneration.",
             "", "## Summary", "", "```json", json.dumps(report["summary"], ensure_ascii=False, indent=2), "```",
             "", "## Workflow gaps", ""]
    lines.extend("- " + gap for gap in report["workflow_gaps"])
    if not report["workflow_gaps"]:
        lines.append("None detected mechanically.")
    lines += ["", "## Source C doubts", ""]
    for row in rows:
        lines += [f"### {row['occurrence_id']} (C line {row['source_line']})", "",
                  f"Mechanical state: **{row['mechanical_state']}**. Final aligned line: {row['final_line'] or 'missing'}.", "",
                  "Source C token:", "", "```tex", row["source_token"], "```", "",
                  "Source C context:", "", "```tex", row["source_context"], "```", "",
                  "Aligned final span:", "", "```tex", row["final_aligned_text"], "```", "",
                  "Final context (up to 100 characters either side):", "", "```tex", row["final_context"], "```", "",
                  "Recorded decision at the same ordinal: " + (row["recorded_decision_same_ordinal"] or "NONE"), "",
                  "Ink disposition: " + (row["ink_disposition"] or "PENDING"), "",
                  "Crop links: " + (row["crop_links"] or "PENDING"), "",
                  "Alignment requires recheck: " + (row["alignment_recheck_required"] or "no flag"), "",
                  "Review note: " + row["review_note"], ""]
    Path(str(prefix) + ".md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--witnesses", type=Path, default=DEFAULT_WITNESSES)
    parser.add_argument("--scan", type=int, action="append", choices=range(2, 26))
    parser.add_argument("--completed-only", action="store_true", help="Limit to existing consolidated page files.")
    parser.add_argument("--report-prefix", type=Path)
    args = parser.parse_args()
    report = make_report(args.out.resolve(), args.witnesses.resolve(), args.scan, args.completed_only)
    if args.report_prefix:
        write_reports(args.report_prefix, report)
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    for gap in report["workflow_gaps"]:
        print("GAP: " + gap)
    if args.report_prefix:
        print("Reports written with prefix: " + str(args.report_prefix))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
