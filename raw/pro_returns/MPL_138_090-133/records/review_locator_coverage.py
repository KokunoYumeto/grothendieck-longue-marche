#!/usr/bin/env python3
"""Generate mechanical grouping and doubt-locator reports without editing sources."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import json
import re
import validate_package as v

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "MPL_138_090-133"
MAPPING = {"deleted": "deletion", "inserted": "insertion", "margin": "margin note", "figure": "drawing", "diagram": "diagram"}


def norm(text):
    # This normalization is only a candidate-discovery aid, not a reading equivalence.
    return re.sub(r"\s+", " ", re.sub(r"\\+", r"\\", text)).strip()


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    inventory = list(csv.DictReader((ROOT / f"{PREFIX}_inventory.csv").open(newline="")))
    rows_by_scan = defaultdict(list)
    kinds = defaultdict(Counter)
    for row in inventory:
        scan = int(row["scan"])
        rows_by_scan[scan].append(row)
        kinds[scan][row["kind"]] += 1
    page_text, all_macros, hashes = {}, {}, {}
    for path in sorted((ROOT / "pages").glob(f"{PREFIX}_138_scan[0-9][0-9][0-9].tex")):
        scan = int(re.search(r"scan(\d+)", path.name).group(1))
        raw = path.read_text()
        clean = v.uncomment(raw)
        page_text[scan] = raw
        hashes[scan] = hashlib.sha256(path.read_bytes()).hexdigest()
        items, ordinal = [], Counter()
        for match in re.finditer(r"\\(deleted|inserted|margin|figure|diagram|unsure|illegible)(?![A-Za-z])\s*", clean):
            if v.escaped(clean, match.start()):
                continue
            macro = match.group(1)
            ordinal[macro] += 1
            start = match.end()
            while start < len(clean) and clean[start].isspace():
                start += 1
            body, end = v.argument_at(clean, start)
            if body is None:
                raise ValueError(f"Unclosed {macro} in scan {scan}.")
            exact = raw[start + 1:end - 1] if clean[start] == "{" else raw[start:end]
            items.append({"macro": macro, "ordinal": ordinal[macro], "line": v.line_at(raw, match.start()), "start": match.start(), "end": end, "body": exact})
        all_macros[scan] = items
    grouping_cases = []
    for scan in sorted(page_text):
        items, raw = all_macros[scan], page_text[scan]
        display_spans, display_start = [], None
        for delim in re.finditer(r"\\\[|\\\]", v.uncomment(raw)):
            if v.escaped(raw, delim.start()):
                continue
            if delim.group() == r"\[":
                display_start = delim.start()
            elif display_start is not None:
                display_spans.append((display_start, delim.end()))
                display_start = None
        for macro, kind in MAPPING.items():
            group = [x for x in items if x["macro"] == macro]
            if len(group) <= kinds[scan][kind]:
                continue
            case = {"scan": scan, "macro": macro, "kind": kind, "macro_count": len(group), "row_count": kinds[scan][kind], "source_sha256": hashes[scan], "existing_same_kind_rows": [r for r in rows_by_scan[scan] if r["kind"] == kind], "occurrences": []}
            for item in group:
                parents = sorted([p for p in items if p["macro"] in MAPPING and p["start"] < item["start"] and p["end"] >= item["end"]], key=lambda p: p["end"] - p["start"])
                # A literal paragraph is used only as a source container; its physical placement is not inferred.
                bounds = {0, len(raw)}
                for gap in re.finditer(r"\n\s*\n|\\par(?![A-Za-z])", raw):
                    bounds.update((gap.start(), gap.end()))
                for a, b in display_spans:
                    bounds.update((a, b))
                left = max(x for x in bounds if x <= item["start"])
                right = min(x for x in bounds if x >= item["end"])
                container = raw[left:right]
                enclosing_spans = [(p["start"], p["end"]) for p in parents] + [(a, b) for a, b in display_spans if a <= item["start"] and b >= item["end"]]
                if enclosing_spans:
                    a, b = min(enclosing_spans, key=lambda pair: pair[1] - pair[0])
                    container = raw[a:b]
                candidates = []
                body_norm, container_norm = norm(item["body"]), norm(container)
                for row in rows_by_scan[scan]:
                    caption = norm(row["first_words_or_objects"])
                    reasons = []
                    if body_norm and body_norm == caption:
                        reasons.append("exact body/caption after whitespace-and-backslash normalization")
                    elif len(body_norm) >= 8 and body_norm in caption:
                        reasons.append("normalized macro body appears in caption")
                    if len(caption) >= 8 and caption in container_norm:
                        reasons.append("normalized caption appears in enclosing source block")
                    if reasons:
                        candidates.append({"element": row["element"], "kind": row["kind"], "reasons": reasons})
                case["occurrences"].append({"ordinal": item["ordinal"], "tex_line": item["line"], "body": item["body"], "enclosing_apparatus": [{"macro": p["macro"], "ordinal": p["ordinal"], "tex_line": p["line"]} for p in parents], "candidate_inventory_relationships": candidates})
            grouping_cases.append(case)
    md = f"# Exact apparatus locations and candidate inventory groupings\n\nSnapshot: {now}\n\n"
    md += ("This is a mechanical source report, not a visual inventory audit. It lists every macro occurrence in page/kind combinations where macro counts exceed corresponding row counts. Candidate relationships use literal substring comparison after collapsing whitespace and repeated backslashes; they are not accepted matches. Parent apparatus relationships are derived from TeX nesting only. No rows or transcription text were changed.\n\n")
    for case in grouping_cases:
        md += f"## Scan {case['scan']}: {case['macro']} — {case['macro_count']} macros / {case['row_count']} {case['kind']} rows\n\n"
        md += "### Existing rows of this kind\n\n| Element | Position | Caption |\n|---|---|---|\n"
        for row in case["existing_same_kind_rows"]:
            md += f"| {cell(row['element'])} | {cell(row['position'])} | {cell(row['first_words_or_objects'])} |\n"
        for item in case["occurrences"]:
            md += f"\n### Macro occurrence {item['ordinal']}, TeX line {item['tex_line']}\n\n```tex\n{item['body']}\n```\n\n"
            md += "Enclosing apparatus: " + (", ".join(f"{p['macro']} occurrence {p['ordinal']} at line {p['tex_line']}" for p in item["enclosing_apparatus"]) or "none") + ".\n\n"
            md += "Candidate inventory relationships: " + ("; ".join(f"{p['element']} ({p['kind']}): {', '.join(p['reasons'])}" for p in item["candidate_inventory_relationships"]) or "no literal match found") + ".\n"
    (ROOT / "records/apparatus_grouping_review.md").write_text(md)
    (ROOT / "records/apparatus_grouping_review.json").write_text(json.dumps({"time": now, "cases": grouping_cases}, ensure_ascii=False, indent=2) + "\n")

    # Parse only the current authored Reading doubts table, not notation or abbreviations.
    doubts_text = (ROOT / f"{PREFIX}_doubts.md").read_text()
    section = doubts_text.split("## Reading doubts", 1)[1].split("\n## ", 1)[0]
    doubt_rows = []
    malformed = []
    for line in section.splitlines():
        if not line.startswith("| 138 |"):
            continue
        fields = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(fields) != 6:
            malformed.append(line)
            continue
        doubt_rows.append({"scan": int(fields[1]), "approximate_line": fields[2], "reading": fields[3], "alternatives": fields[4], "confidence": fields[5]})
    uncertain = []
    for scan, items in all_macros.items():
        for item in items:
            if item["macro"] not in {"unsure", "illegible"}:
                continue
            same_page = [row for row in doubt_rows if row["scan"] == scan]
            body = norm(item["body"]).strip("$`")
            alternatives = [norm(x).strip("$`") for x in item["body"].split("|")]
            exact = [row for row in same_page if norm(row["reading"]).strip("$`") in [body, *alternatives]]
            uncertain.append({"scan": scan, "macro": item["macro"], "ordinal": item["ordinal"], "tex_line": item["line"], "exact_body": item["body"], "same_page_authored_rows": len(same_page), "exact_reading_cell_candidates": exact})
    by_scan = []
    for scan in sorted(page_text):
        u = [x for x in uncertain if x["scan"] == scan]
        by_scan.append({"scan": scan, "unsure": sum(x["macro"] == "unsure" for x in u), "illegible": sum(x["macro"] == "illegible" for x in u), "authored_doubt_rows": sum(x["scan"] == scan for x in doubt_rows), "exact_reading_cell_candidates": sum(bool(x["exact_reading_cell_candidates"]) for x in u)})
    summary = {"time": now, "source_uncertainty_macros": len(uncertain), "unsure": sum(x["macro"] == "unsure" for x in uncertain), "illegible": sum(x["macro"] == "illegible" for x in uncertain), "authored_doubt_rows": len(doubt_rows), "exact_reading_cell_candidates": sum(bool(x["exact_reading_cell_candidates"]) for x in uncertain), "authored_rows_explicitly_using_tex_line_locators": sum(bool(re.search(r"TeX\s+line", x["approximate_line"], re.I)) for x in doubt_rows), "malformed_authored_rows": malformed, "per_scan": by_scan}
    index_path = ROOT / "records/uncertainty_locator_index.json"
    supplement_status = None
    if "<!-- BEGIN EXHAUSTIVE_UNCERTAINTY_LOCATORS -->" in doubts_text and index_path.exists():
        index = json.loads(index_path.read_text())
        expected_index = {(x["scan"], x["macro"], x["ordinal"]): x for x in uncertain}
        recorded_index = {(x["scan"], x["macro"], x["occurrence"]): x for x in index["entries"]}
        mismatches = []
        for key in expected_index.keys() & recorded_index.keys():
            current, recorded = expected_index[key], recorded_index[key]
            if current["tex_line"] != recorded["tex_line"] or current["exact_body"] != recorded["exact_argument"]:
                mismatches.append(key)
        supplement_status = {"recorded_entries": len(index["entries"]), "missing_keys": sorted(expected_index.keys() - recorded_index.keys()), "extra_keys": sorted(recorded_index.keys() - expected_index.keys()), "body_or_line_mismatches": mismatches, "current_occurrence_coverage_exact": expected_index.keys() == recorded_index.keys() and not mismatches and len(recorded_index) == len(index["entries"])}
        summary["existing_supplement_verification"] = supplement_status
    dm = f"# Mechanical doubts locator coverage review\n\nSnapshot: {now}\n\n"
    dm += f"The page files contain {summary['source_uncertainty_macros']} uncertainty macros: {summary['unsure']} unsure and {summary['illegible']} illegible. The current authored Reading doubts table has {len(doubt_rows)} rows. {summary['exact_reading_cell_candidates']} macro occurrences have an exact same-page reading-cell candidate after whitespace/backslash normalization and removal of outer math/code delimiters. This is a candidate text match, not confirmation that the occurrence is covered.\n\n"
    dm += ("The authored rows use approximate manuscript positions, frequently grouping several symbols or occurrences. Those positions cannot be safely equated with TeX source line numbers. Consequently the current table cannot be mechanically certified as an exhaustive occurrence locator, nor can a nonmatching row be declared an omitted doubt merely from this comparison. No confidence was inferred or changed.\n\n")
    dm += "| Scan | unsure | illegible | Authored rows | Exact reading-cell candidates |\n|---|---:|---:|---:|---:|\n"
    for row in by_scan:
        dm += f"| {row['scan']} | {row['unsure']} | {row['illegible']} | {row['authored_doubt_rows']} | {row['exact_reading_cell_candidates']} |\n"
    if supplement_status is not None:
        dm += "\n## Current exhaustive supplement\n\nThe primary reader has run the supplementary-table script. The current read-only verification is:\n\n```json\n" + json.dumps(supplement_status, ensure_ascii=False, indent=2) + "\n```\n"
    dm += ("\n## Supplementary-table method\n\n"
           "After the transcription is frozen, append a separate exhaustive macro locator table while preserving the existing notation table, authored readings, alternatives, confidence judgments, and abbreviations. Use one row per source macro occurrence, including nested or deleted uncertainties and unbraced single-token arguments. Columns should identify cote, scan, TeX line, macro kind, ordinal, and exact macro body; manuscript line positions must not be invented. Keep alternatives in the same order as the source body and retain illegible word counts as counts rather than proposed readings.\n\n"
           "The supplement should state that it is a mechanical locator index, not an additional reading or independent check. Do not assign new confidence ratings from the presence of unsure; link to authored confidence rows only when a unique exact relationship is established. Preserve exact raw strings in a TSV or JSON record alongside any Markdown escaping needed for pipes, backticks, and line breaks. Hash the frozen source files used, count every occurrence, and assert that the supplement has exactly the same occurrence keys.\n\n"
           "This read-only review does not append the supplementary table or change the doubts file; any existing supplement is checked separately above.\n")
    (ROOT / "records/doubts_locator_coverage_review.md").write_text(dm)
    (ROOT / "records/doubts_locator_coverage_review.json").write_text(json.dumps({**summary, "occurrences": uncertain}, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"time": now, "grouping_cases": len(grouping_cases), **{k: summary[k] for k in ["source_uncertainty_macros", "unsure", "illegible", "authored_doubt_rows", "exact_reading_cell_candidates", "authored_rows_explicitly_using_tex_line_locators"]}}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
