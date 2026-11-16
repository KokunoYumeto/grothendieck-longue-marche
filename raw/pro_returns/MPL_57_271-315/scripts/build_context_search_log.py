#!/usr/bin/env python3
"""Build the item-level post-freeze context-search record.

Reads only the final research notes, five allowlisted context text files, and
already extracted printed Oda page_*.txt files. It does not open source images,
run OCR, change the transcription, or perform external lookups.

Run from any directory; defaults follow this script's package location:
    python MPL_57_271-315/scripts/build_context_search_log.py
Use --workspace and --oda-dir if the supplied context/extraction is elsewhere.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import unicodedata


PREFIX_COUNTS = {
    "F": 3, "J": 7, "P": 11, "E": 10, "D": 9, "C": 10,
    "I": 5, "R": 6, "S": 40, "T": 8, "G": 8,
}
SOURCE_ORDER = ("CR", "RS", "CT", "CN", "CD", "Oda")
CANDIDATE_LIMITS = {"CR": 2, "RS": 3, "CT": 4, "CN": 4, "CD": 2, "Oda": 3}
CONTEXT_FILES = {
    "CR": "context/README.md",
    "RS": "context/notes/RESULTS_STATE.md",
    "CT": "context/MPL_16+47+54+44_transcription.tex",
    "CN": "context/MPL_16+47+54+44_notes.md",
    "CD": "context/MPL_16+47+54+44_doubts.md",
}
SOURCE_STATUS = {
    "CR": "Supplied package scope and research instructions.",
    "RS": "Mixed-status register; a lexical hit does not change an entry's stated status.",
    "CT": "Supplied earlier transcription; not second-passed, a provisional witness.",
    "CN": "Supplied earlier research notes; unreviewed claims and bibliographic leads.",
    "CD": "Supplied earlier doubts; reported reading uncertainties, not newly inspected images.",
    "Oda": "Supplied extraction of the printed primary paper; keyword hits alone are not verification.",
}


def normalized(text):
    return unicodedata.normalize("NFC", text).casefold()


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_name(path, workspace):
    try:
        return str(path.resolve().relative_to(workspace.resolve()))
    except ValueError:
        return str(path.resolve())


def short_heading(title):
    """Keep exact item labels where present; otherwise retain the heading."""
    match = re.match(r"(\d+:\d+:\d+|[A-Z]\d{1,2})(?:\.|\s|$)", title)
    return match.group(1) if match else "§ " + title


def parse_items(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    items, current, all_search_lines = [], None, []
    for number, line in enumerate(lines, 1):
        heading = re.match(r"^###\s+([A-Z]\d{2})\s+—\s+(.+?)\s*$", line)
        if heading:
            current = {"id": heading[1], "kind": "heading", "title": heading[2],
                       "notes_line": number, "search_lines": [], "terms": []}
            items.append(current)
            continue
        if re.match(r"^#{1,3}\s", line):
            current = None
        search = re.match(r"^\*\*Search:\*\*\s*(.*?)\s*$", line)
        if search:
            all_search_lines.append(number)
            if current is None:
                raise ValueError(f"Orphan Search field at notes line {number}")
            current["search_lines"].append(number)
            current["terms"].extend(term.strip() for term in search[1].split("|"))
        row = re.match(r"^\|\s*([STG]\d{2})\b", line)
        if row:
            cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
            if len(cells) != 4:
                raise ValueError(f"Expected 4 cells for {row[1]}, got {len(cells)}")
            items.append({"id": row[1], "kind": "table", "title": cells[0],
                          "notes_line": number, "search_lines": [number],
                          "terms": [term.strip() for term in cells[-1].split(";")]})

    expected = {f"{prefix}{number:02d}" for prefix, count in PREFIX_COUNTS.items()
                for number in range(1, count + 1)}
    counts = Counter(item["id"] for item in items)
    missing = sorted(expected - set(counts))
    extra = sorted(set(counts) - expected)
    duplicates = sorted(key for key, value in counts.items() if value != 1)
    invalid_search = [item["id"] for item in items
                      if len(item["search_lines"]) != 1 or not item["terms"]
                      or any(not term for term in item["terms"])]
    heading_count = sum(item["kind"] == "heading" for item in items)
    table_count = len(items) - heading_count
    validation = {
        "expected_items": 117, "parsed_items": len(items),
        "heading_items": heading_count, "heading_search_fields": len(all_search_lines),
        "table_items": table_count, "prefix_counts": dict(Counter(i["id"][0] for i in items)),
        "missing_ids": missing, "unexpected_ids": extra,
        "duplicate_ids": duplicates, "invalid_search_entries": invalid_search,
    }
    if missing or extra or duplicates or invalid_search or heading_count != 61 or table_count != 56:
        raise ValueError("Search coverage failed: " + json.dumps(validation, ensure_ascii=False))
    return items, validation


class Corpus:
    def __init__(self, workspace):
        self.workspace = workspace
        self.lines = []
        self.units = {}
        self.files = []

    def add_file(self, key, path, pdf_page=None):
        lines = path.read_text(encoding="utf-8").splitlines()
        relative = relative_name(path, self.workspace)
        self.files.append({"source": key, "path": relative, "sha256": sha256(path),
                           "line_count": len(lines)})
        heading, anchor, cote, scan = "Document opening", 1, None, None
        for number, text in enumerate(lines, 1):
            locator = heading
            if key == "CT":
                match = re.search(r"\\cotefile\{([^}]+)\}", text)
                if match:
                    cote, scan, anchor = match[1], None, number
                match = re.search(r"\\scanpage\{([^}]+)\}", text)
                if match:
                    scan, anchor = match[1], number
                locator = f"{cote}:{scan}" if scan else f"cote {cote}, opening"
                heading = locator
            elif key == "Oda":
                locator = (f"printed p.{pdf_page + 61} / PDF {pdf_page}"
                           if pdf_page >= 2 else "NUMDAM cover / PDF 1")
                heading, anchor = locator, 1
            else:
                match = re.match(r"^#{1,6}\s+(.+?)\s*$", text)
                if match:
                    heading, anchor = match[1], number
                locator = short_heading(heading) if key == "CN" else "§ " + heading
                if key == "RS":
                    entry = re.match(r"^- \*\*(.+?)\*\*", text)
                    if entry:
                        locator, anchor = entry[1], number
                elif key == "CD":
                    table = re.match(r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|", text)
                    bullet = re.match(r"^- Cote (\d+), scan (\d+):", text)
                    if table or bullet:
                        match = table or bullet
                        locator = f"{match[1]}:{match[2]} ({heading})"
                        anchor = number
            unit_key = (key, relative, locator)
            if unit_key not in self.units:
                self.units[unit_key] = {"source": key, "path": relative, "locator": locator,
                                        "heading": heading, "anchor_line": anchor}
            self.lines.append({"source": key, "text": normalized(text),
                               "line": number, "unit": unit_key})


def search_items(items, corpus):
    cache = {}
    for item in items:
        for term in item["terms"]:
            key = normalized(term)
            if key not in cache:
                matches = [index for index, record in enumerate(corpus.lines) if key in record["text"]]
                by_source = Counter(corpus.lines[index]["source"] for index in matches)
                cache[key] = {"matches": matches, "counts": {s: by_source[s] for s in SOURCE_ORDER}}

    results = []
    for item in items:
        queries, union = [], set()
        units = defaultdict(lambda: {"terms": set(), "lines": set(), "weight": 0.0})
        for term in item["terms"]:
            found = cache[normalized(term)]
            queries.append({"term": term, "matching_lines": len(found["matches"]),
                            "by_source": found["counts"]})
            union.update(found["matches"])
            seen_units = set()
            for index in found["matches"]:
                record = corpus.lines[index]
                unit = units[record["unit"]]
                unit["terms"].add(term)
                unit["lines"].add(index)
                if record["unit"] not in seen_units:
                    unit["weight"] += 1.0 / (1 + len(found["matches"]))
                    seen_units.add(record["unit"])
        union_counts = Counter(corpus.lines[index]["source"] for index in union)
        candidates, available = [], {}
        for source in SOURCE_ORDER:
            keys = [key for key in units if key[0] == source]
            available[source] = len(keys)
            keys.sort(key=lambda key: (-len(units[key]["terms"]), -units[key]["weight"],
                                       corpus.units[key]["path"], corpus.units[key]["anchor_line"]))
            for key in keys[:CANDIDATE_LIMITS[source]]:
                unit = units[key]
                descriptor = corpus.units[key]
                candidates.append({"source": source, "path": descriptor["path"],
                                   "locator": descriptor["locator"], "heading": descriptor["heading"],
                                   "first_hit_line": min(corpus.lines[i]["line"] for i in unit["lines"]),
                                   "matching_lines": len(unit["lines"]),
                                   "terms": [q for q in item["terms"] if q in unit["terms"]]})
        results.append({**item, "queries": queries,
                        "unique_matching_lines": {s: union_counts[s] for s in SOURCE_ORDER},
                        "candidate_units_available": available, "candidate_locators": candidates,
                        "zero_hit_terms": [query["term"] for query in queries if not query["matching_lines"]]})
    return results, len(cache)


def compact(text, limit=75):
    return text if len(text) <= limit else text[:limit - 1] + "…"


def markdown_code(text):
    return "`" + text.replace("`", "'") + "`"


def make_markdown(payload):
    validation = payload["validation"]
    output = [
        "# Item-level context search log",
        "",
        "**Search hits are candidate retrieval locations, not proof, source validation, or a change in evidentiary status.** Earlier CT/CN/CD contents remain supplied, unreviewed claims/readings. No source image was opened and no OCR or external lookup was performed by this script.",
        "",
        f"Coverage: **{validation['parsed_items']} / {validation['expected_items']} items** — "
        f"{validation['heading_items']} heading items with Search fields and {validation['table_items']} table items "
        "(S01–S40, T01–T08, G01–G08). Missing, duplicate, unexpected, or empty entries: **none**.",
        "",
        f"Search specification: {payload['term_occurrences']} item-term searches, "
        f"{payload['distinct_terms']} distinct normalized terms. Matching is case-insensitive NFC-normalized **literal substring matching per source line**. No regex, stemming, accent removal, TeX normalization, OCR correction, or joining across line breaks is performed. Counts are matching lines, not word occurrences; source totals are unions of lines and are not the sum of query counts. Single-letter and short terms can be very broad. Zero hits do not establish conceptual absence.",
        "",
        "Corpus keys: CR = context/README.md; RS = context/notes/RESULTS_STATE.md; CT = earlier transcription TEX; CN = earlier notes; CD = earlier doubts; Oda = the 74 supplied printed-source page_*.txt extracts. Oda printed page = PDF/extract index + 61 for indices 2–74; index 1 is the NUMDAM cover. Extraction errors and mathematical formatting can cause missed literal matches.",
        "",
        "Per item, query counts are followed by union counts for CR/RS/CT/CN/CD/Oda. Candidate locators are ranked within each corpus by number of distinct matched terms, then summed inverse global hit frequency, then source order. At most CR 2, RS 3, CT 4, CN 4, CD 2, and Oda 3 locations are shown. These are compact samples, not an exhaustive concordance or necessarily the strongest mathematical comparators. The JSON records corpus-specific query counts, source hashes, and the number of candidate units before truncation; it contains no source-text dumps.",
        "",
        "Reproduce with `python MPL_57_271-315/scripts/build_context_search_log.py` in the supplied workspace. The script rereads the latest main notes and fails if the expected 117-ID coverage or a Search entry is missing. Paths can be set with `--workspace`, `--notes`, `--oda-dir`, and `--output-dir`. It requires the existing context texts and existing printed Oda extracts and does not regenerate them. It writes only this log and its companion JSON.",
        "",
        f"Generated UTC: {payload['generated_utc']}. Main-notes SHA-256: `{payload['notes']['sha256']}`. "
        f"ID/query signature: `{payload['notes']['search_signature_sha256']}`. Rerun after final prose edits if an exact whole-file hash is required; the ID/query signature isolates search coverage from prose-only changes.",
        "",
    ]
    previous_prefix = None
    for item in payload["items"]:
        if item["id"][0] != previous_prefix:
            previous_prefix = item["id"][0]
            output.extend([f"## {previous_prefix} items", ""])
        output.extend([f"### {item['id']} — {compact(item['title'], 105)}", ""])
        output.append("- **Queries → matching lines:** " + "; ".join(
            f"{markdown_code(query['term'])} → {query['matching_lines']}" for query in item["queries"]) + ".")
        output.append("- **Union by corpus:** " + "; ".join(
            f"{source} {item['unique_matching_lines'][source]}" for source in SOURCE_ORDER) + ".")
        locations = []
        for source in SOURCE_ORDER:
            matches = [hit for hit in item["candidate_locators"] if hit["source"] == source]
            if matches:
                group = "; ".join(f"{compact(hit['locator'])} (L{hit['first_hit_line']})" for hit in matches)
                total = item["candidate_units_available"][source]
                suffix = f" [{len(matches)}/{total} units]" if total > len(matches) else ""
                locations.append(f"**{source}:** {group}{suffix}")
        output.append("- **Candidate locators:** " + (" · ".join(locations) if locations else "none") + ".")
        if item["zero_hit_terms"]:
            output.append("- **Literal zero-hit terms:** " + "; ".join(map(markdown_code, item["zero_hit_terms"])) + ".")
        output.append("")
    output.extend([
        "## Coverage and source inventory", "",
        "| Prefix | Expected | Recorded |", "|---|---:|---:|",
    ])
    for prefix, count in PREFIX_COUNTS.items():
        output.append(f"| {prefix} | {count} | {validation['prefix_counts'].get(prefix, 0)} |")
    output.extend(["", f"All-zero-hit items: {', '.join(payload['all_zero_hit_items']) or 'none'}. "
                   f"Zero-hit item-term entries: {payload['zero_hit_item_terms']}. "
                   "These are search outcomes, not missing search records.", ""])
    for source in SOURCE_ORDER:
        files = [file for file in payload["source_files"] if file["source"] == source]
        output.append(f"- {source}: {len(files)} file(s), {sum(f['line_count'] for f in files)} lines. " + SOURCE_STATUS[source])
    output.extend(["", "The companion JSON retains every parsed ID exactly once, exact terms, notes-line provenance, "
                   "per-term/per-corpus counts, limited candidate locators, and hashes of the allowlisted source files.", ""])
    return "\n".join(output)


def main():
    package = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=package.parent)
    parser.add_argument("--notes", type=Path, default=package / "MPL_57_271-315_notes.md")
    parser.add_argument("--oda-dir", type=Path)
    parser.add_argument("--output-dir", type=Path, default=package / "records")
    args = parser.parse_args()
    oda_dir = args.oda_dir or args.workspace / "tmp/pdfs/oda_support"
    notes_before = sha256(args.notes)
    items, validation = parse_items(args.notes)
    corpus = Corpus(args.workspace)
    for key, relative in CONTEXT_FILES.items():
        corpus.add_file(key, args.workspace / relative)
    pages = sorted(oda_dir.glob("page_[0-9][0-9][0-9].txt"))
    if [int(page.stem.split("_")[-1]) for page in pages] != list(range(1, 75)):
        raise ValueError("Expected the 74 supplied printed Oda page_001.txt–page_074.txt extracts")
    for page in pages:
        corpus.add_file("Oda", page, int(page.stem.split("_")[-1]))
    results, distinct_terms = search_items(items, corpus)
    if sha256(args.notes) != notes_before:
        raise RuntimeError("Main notes changed while search ran; rerun to obtain a consistent snapshot")
    signature = json.dumps([{ "id": item["id"], "terms": item["terms"] } for item in items],
                           ensure_ascii=False, separators=(",", ":"))
    payload = {
        "schema_version": 1,
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "candidate_only": True,
        "matching": "NFC casefold literal substring, independently within each supplied source line",
        "count_unit": "matching source lines; item source totals are unions, not summed query totals",
        "candidate_limits": CANDIDATE_LIMITS,
        "candidate_ranking": "distinct matched terms descending; summed inverse global line frequency descending; source path/anchor order",
        "notes": {"path": relative_name(args.notes, args.workspace), "sha256": notes_before,
                  "search_signature_sha256": hashlib.sha256(signature.encode()).hexdigest()},
        "validation": validation,
        "source_status": SOURCE_STATUS,
        "source_files": corpus.files,
        "oda_pagination": "PDF/extract 1 is NUMDAM cover; printed page = extract index + 61 for 2–74",
        "term_occurrences": sum(len(item["terms"]) for item in items),
        "distinct_terms": distinct_terms,
        "zero_hit_item_terms": sum(len(item["zero_hit_terms"]) for item in results),
        "all_zero_hit_items": [item["id"] for item in results if not any(item["unique_matching_lines"].values())],
        "items": results,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "context_search_log.json"
    markdown_path = args.output_dir / "context_search_log.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    markdown_path.write_text(make_markdown(payload), encoding="utf-8")
    print(json.dumps({"items": len(items), "headings": validation["heading_items"],
                      "table_rows": validation["table_items"], "item_terms": payload["term_occurrences"],
                      "distinct_terms": distinct_terms, "coverage_gaps": validation["missing_ids"],
                      "zero_hit_item_terms": payload["zero_hit_item_terms"],
                      "all_zero_hit_items": payload["all_zero_hit_items"],
                      "outputs": [str(markdown_path), str(json_path)]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
