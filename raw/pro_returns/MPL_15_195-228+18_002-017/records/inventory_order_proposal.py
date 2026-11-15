#!/usr/bin/env python3
"""Propose only an inventory permutation; never alter canonical files.

Every automatic row is matched exactly to a final frozen TeX macro. Explicit
source-block anchors connect it to the existing manual inventory. Manual rows
retain their relative order and every CSV field retains its original value.
No scan images are opened and no physical position is inferred from formulae.

Run from any directory. Outputs are confined to this script's records folder:
  inventory_order_proposal.csv
  inventory_pagination_suggestions.csv
  inventory_order_report.md
"""
from __future__ import annotations

from collections import Counter, defaultdict, deque
import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
RECORDS = Path(__file__).resolve().parent
ROOT = RECORDS.parent
PREFIX = ROOT.name
spec = importlib.util.spec_from_file_location("mechanical_read_only", RECORDS / "finalize_mechanical.py")
mechanical = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mechanical
spec.loader.exec_module(mechanical)

# Only source blocks containing an automatic row need an anchor. The fields are
# manual element ID, first/last source lines, placement (after/before), and status.
# S = containing source block; B = source boundary only (review physical place);
# W = wrapper crossing more than one manual block; P = whole-page cancellation.
# The anchors do not purport to recover the complete page's physical geometry.
A = {
 (15,195): [(1,3,3),(2,5,7),(6,15,15),(7,17,19),(8,21,23)],
 (15,197): [(2,4,6)],
 (15,199): [(3,5,8),(4,10,10),(7,19,19),(10,25,25)],
 (15,201): [(1,2,4),(3,7,11)],
 (15,203): [(1,2,2),(6,14,17),(7,19,19),(9,23,24)],
 (15,205): [(2,4,4),(3,6,6),(6,13,13)],
 (15,207): [(1,2,2),(2,4,4),(3,6,6),(4,8,10),(7,16,16)],
 (15,209): [(1,2,2),(2,4,19)],
 (15,211): [(1,3,4),(2,7,15),(3,17,22),(5,24,30)],
 (15,213): [(4,10,14),(6,21,25),(9,32,37)],
 (15,215): [(1,3,5),(8,7,7),(4,14,26),(6,28,32),(1001,34,34),(7,35,37)],
 (15,217): [(1,3,8),(2,10,16),(4,20,24)],
 (15,219): [(1,3,3),(2,5,10),(3,12,15),(4,16,22),(7,29,35),(8,37,40),(9,42,48),(10,50,53),(11,55,56)],
 (15,221): [(1,3,4),(6,19,23),(8,27,29),(9,31,35)],
 (15,223): [(1,2,3),(3,6,6),(5,10,10),(6,11,11),(7,12,12),(9,17,17)],
 (15,225): [(1,2,2,"before","B"),(1,3,3),(3,4,8),(4,9,14),(5,15,15),(6,16,16)],
 (15,227): [(1,2,2,"before","B"),(1,3,3),(2,3,3),(3,5,5)],
 (18,5): [(1,2,2),(4,8,8),(5,10,12),(6,14,14),(7,16,16),(8,18,18),(9,20,20),(12,26,26)],
 (18,6): [(2,12,12),(5,21,22),(10,34,38),(11,39,39),(13,43,43)],
 (18,7): [(2,10,10),(3,11,16),(4,17,17)],
 (18,9): [(2,4,5)],
 (18,11): [(6,18,23),(6,24,24,"after","B"),(1000,25,28,"after","W"),
           (1001,29,31,"after","B"),(9,37,38),(11,41,44),
           (13,49,49,"before","B"),(13,50,56),(14,57,59),(15,63,63,"after","B")],
 (18,12): [(1,2,24,"before","P"),(2,5,5),(4,9,9),(5,11,11),(8,18,18),(10,25,26,"after","B")],
 (18,13): [(4,8,10),(5,12,14)],
 (18,15): [(2,4,6),(4,10,17),(5,19,19),(6,20,20)],
 (18,17): [(1,2,2,"before","B"),(2,4,4),(3,5,8),(9,21,24)],
}

STATUS = {
 "S": "containing source block",
 "B": "source boundary only; physical position unverified",
 "W": "one margin wrapper covers manual 1000 and 1001; placed after 1000",
 "P": "whole-page cancellation wrapper; placed before first manual block",
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def md(value):
    return str(value).replace("|", "\\|").replace("\n", " ")

def identity(row):
    return tuple(row[f] for f in mechanical.FIELDS)

def line_offsets(text):
    starts = [0]
    starts.extend(m.end() for m in re.finditer("\n", text))
    if starts[-1] != len(text):
        starts.append(len(text))
    return starts

def anchors(pair, text):
    starts = line_offsets(text)
    result = []
    for item in A.get(pair, []):
        element, first, last = item[:3]
        side, status = item[3:] if len(item) == 5 else ("after", "S")
        start, end = starts[first-1], starts[last]
        # One physical TeX line contains two separate manual text blocks.
        if pair == (15,227) and first == 3:
            split = text.index("Plus généralement", start, end)
            if element == 1:
                end = split
            else:
                start = split
        # Precisely delimit the live first paragraph on this shared source line.
        if pair == (15,225) and first == 3:
            end = text.index("Mais que se passe-t-il", start, end)
        if pair == (15,227) and first == 5:
            end = text.index("Kif kif", start, end)
        if pair == (15,219) and element == 4:
            start = text.index("Soit ", start, starts[first])
        result.append(dict(element=f"{element:03d}", start=start, end=end,
                           first=first, last=last, side=side, status=status))
    return result

def main():
    source = ROOT / f"{PREFIX}_inventory.csv"
    input_bytes = source.read_bytes()
    input_hash = hashlib.sha256(input_bytes).hexdigest()
    reader = csv.DictReader(io.StringIO(input_bytes.decode("utf-8"), newline=""))
    if reader.fieldnames != mechanical.FIELDS:
        raise RuntimeError("Unexpected inventory columns")
    rows = list(reader)
    pages = defaultdict(list)
    for row in rows:
        pages[(int(row["cote"]), int(row["scan"]))].append(row)
    if list(pages) != list(mechanical.EXPECTED):
        raise RuntimeError("Unexpected inventory page ordering")
    frozen = json.loads((RECORDS / "frozen_manifest.json").read_text())["sha256"]
    for relative, expected in frozen.items():
        if digest(ROOT / relative) != expected:
            raise RuntimeError(f"Frozen input mismatch: {relative}")
    proposal = []
    audit = []
    duplicates = []
    ambiguous = []
    unmatched = []
    page_counts = []
    missing_page_numbers = []
    sheet_issues = []
    picture_counts = []
    for pair, page_rows in pages.items():
        cote, scan = pair
        path = ROOT / "pages" / mechanical.page_name(cote, scan)
        text = path.read_text()
        _, macros = mechanical.scan_macros(text, path.name)
        auto_macros = [m for m in macros if m.name in mechanical.AUTO_KINDS]
        index = defaultdict(deque)
        for macro in auto_macros:
            key = (mechanical.AUTO_KINDS[macro.name], f"TeX line {macro.line}",
                   mechanical.compact(macro.argument)[:350])
            index[key].append(macro)
        duplicates.extend((pair, key, len(items)) for key, items in index.items() if len(items) > 1)
        manual = [r for r in page_rows if r["kind"] in mechanical.MANUAL_KINDS]
        auto = [r for r in page_rows if r["kind"] not in mechanical.MANUAL_KINDS]
        if len(auto) != len(auto_macros):
            raise RuntimeError(f"Automatic row count mismatch: {pair}")
        source_anchors = anchors(pair, text)
        manual_ids = {r["element"] for r in manual}
        if any(a["element"] not in manual_ids for a in source_anchors):
            raise RuntimeError(f"Anchor refers to missing manual ID: {pair}")
        slots = defaultdict(list)
        unplaced = []
        for row in auto:
            key = (row["kind"], row["position"], row["first_words_or_objects"])
            if not index[key]:
                raise RuntimeError(f"No exact macro match for {pair} element {row['element']}")
            macro = index[key].popleft()
            candidates = [a for a in source_anchors
                          if a["start"] <= macro.offset and macro.closing < a["end"]
                          and (a["status"] != "P" or macro.line == a["first"])]
            if len(candidates) != 1:
                note = (pair, row["element"], macro.line, macro.column,
                        [a["element"] for a in candidates])
                (ambiguous if candidates else unmatched).append(note)
                unplaced.append(row)
                audit.append((pair, row, macro, None))
                continue
            anchor = candidates[0]
            slots[(anchor["element"], anchor["side"])].append((macro.offset, row))
            audit.append((pair, row, macro, anchor))
        if any(index.values()):
            raise RuntimeError(f"Unmatched source macros remain on {pair}")
        page_proposal = []
        for row in manual:
            for side in ("before", "after"):
                if side == "after":
                    page_proposal.append(row)
                page_proposal.extend(r for _, r in sorted(slots[(row["element"], side)], key=lambda x:x[0]))
        page_proposal.extend(unplaced)
        proposal.extend(page_proposal)
        page_counts.append((pair, len(manual), len(auto), sum(a is not None and a["status"] != "S"
                           for p,r,m,a in audit if p == pair)))
        if [identity(r) for r in manual] != [identity(r) for r in page_proposal if r["kind"] in mechanical.MANUAL_KINDS]:
            raise RuntimeError(f"Manual ordering changed on {pair}")
        kinds = {r["sheet_kind"] for r in page_rows}
        original = json.loads((RECORDS / f"{cote}_{scan:03d}_inventory.json").read_text())
        original_kinds = {str(r[2]) for r in original}
        if len(kinds) != 1 or kinds != original_kinds:
            sheet_issues.append((pair, sorted(kinds), sorted(original_kinds)))
        # These are coverage signals, not image-based conclusions.
        for number in re.finditer(r"\\mspage\{([^{}]*)\}", text):
            value = number.group(1)
            dedicated = [r for r in manual if r["first_words_or_objects"].strip() == value]
            if not dedicated:
                line = text.count("\n", 0, number.start()) + 1
                missing_page_numbers.append((pair, line, value, next(iter(kinds))))
        for macro_name, row_kind in (("diagram", "diagram"),("figure", "drawing")):
            macro_count = len(re.findall(r"\\" + macro_name + r"\s*\{", mechanical.lexical_mask(text)))
            row_count = sum(r["kind"] == row_kind for r in manual)
            if macro_count != row_count:
                picture_counts.append((pair, macro_name, macro_count, row_kind, row_count))
    if Counter(map(identity, rows)) != Counter(map(identity, proposal)):
        raise RuntimeError("The proposal does not preserve the complete row multiset")
    if source.read_bytes() != input_bytes:
        raise RuntimeError("Canonical inventory changed during proposal generation")
    for relative, expected in frozen.items():
        if digest(ROOT / relative) != expected:
            raise RuntimeError(f"Frozen input changed during generation: {relative}")
    csv_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(csv_buffer, fieldnames=mechanical.FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(proposal)
    csv_data = csv_buffer.getvalue().encode("utf-8")
    (RECORDS / "inventory_order_proposal.csv").write_bytes(csv_data)
    # Suggestions are a separate file; they do not enter the 694-row permutation.
    additions = []
    next_ids = {p:max(int(r['element']) for r in rs)+1 for p,rs in pages.items()}
    for pair,line,value,sheet_kind in missing_page_numbers:
        element = f"{next_ids[pair]:03d}"
        next_ids[pair] += 1
        additions.append(dict(cote=str(pair[0]), scan=str(pair[1]), sheet_kind=sheet_kind,
                              element=element, kind="text",
                              position=f"pagination; TeX line {line} (physical position for review)",
                              first_words_or_objects=value, transcribed="yes"))
    additions_buffer = io.StringIO(newline="")
    additions_writer = csv.DictWriter(additions_buffer, fieldnames=mechanical.FIELDS, lineterminator="\n")
    additions_writer.writeheader()
    additions_writer.writerows(additions)
    (RECORDS / "inventory_pagination_suggestions.csv").write_text(additions_buffer.getvalue())
    report = [
        "# Inventory ordering proposal — mechanical audit only", "",
        "The canonical inventory and all frozen page/combined TeX files are unchanged. This report accompanies a proposed permutation, not a replacement canonical inventory or a certification of physical reading order.", "",
        "## Inputs and invariant checks", "",
        f"- Input: `{source.name}`; SHA-256 `{input_hash}`.",
        f"- Proposal: `records/inventory_order_proposal.csv`; SHA-256 `{hashlib.sha256(csv_data).hexdigest()}`.",
        f"- Rows: {len(rows)} = {sum(r['kind'] in mechanical.MANUAL_KINDS for r in rows)} manual + {len(audit)} generated.",
        "- Every original CSV field, including element ID, classification, position and excerpt, is retained exactly as a parsed field value; the complete row multiset is equal. No rows are added or removed.",
        "- `records/inventory_pagination_suggestions.csv` is a separate ten-row suggestion file, excluded from that equality/permutation. It uses existing sheet kinds, fresh per-page IDs above all retained IDs, and exact frozen pagination values; the position fields deliberately identify source lines and leave physical placement for primary-reader review.",
        "- All manual rows retain their relative order within each page. Page order and column order are unchanged.",
        f"- All {len(audit)} generated rows match final macros exactly by kind, source line and compacted 350-character excerpt; source character offsets and columns disambiguate occurrences.",
        f"- Unmatched source-block anchors: {len(unmatched)}. Ambiguous source-block anchors: {len(ambiguous)}. Duplicate exact macro keys: {len(duplicates)}.",
        f"- All {len(frozen)} files listed in `records/frozen_manifest.json` match the frozen SHA-256 values before and after this operation.",
        "", "## Ordering rule and limits", "",
        "The finalizer (`records/finalize_mechanical.py`, `make_outputs`) intentionally appends generated rows after every page's manual rows. The proposal instead matches each generated row to its source macro and associates it with an explicitly delimited source passage corresponding to a retained manual row. Insertions, deletions and marginal wrappers follow that parent row in source occurrence order; nested macros therefore retain the parser's outer-before-inner order. Two text blocks on 15/227 share a TeX line and are separated by the literal phrase `Plus généralement`; equivalent literal boundaries delimit shared-line passages on 15/225, 15/219 and 15/227. No formula semantics, inferred reading, numerical element ID ordering or global TeX-line sort determines placement.", "",
        "An enclosing macro can cover an already inventoried drawing without making that drawing's late-added manual row the parent of the enclosing insertion. Thus the insertion containing the ellipse on 15/215 stays beside manual 001, and the insertion containing the ellipse on 15/217 stays beside manual 004. The late-added figure rows themselves remain in their existing manual positions. Every association is recorded below, with the exact macro start line and column.", "",
        "Free-standing margins that have no uniquely containing manual row are placed at an explicitly marked source boundary. Such placement is a document-order convention for review, not evidence of their physical height on the sheet. The margin on 18/11 lines 25–28 wraps both manual 1000 and 1001 and is placed after 1000. The deletion beginning 18/12 line 2 spans the cancelled page's ten manual blocks and is placed before the first, rather than treated as a deletion contained in that first sentence. No unresolved anchor is silently guessed; an unmatched or ambiguous row would remain at the page tail and be listed below.", "",
        "## Remaining manual-order issues", "",
        "Preserving manual order is essential to this proposal's scope, but it prevents a claim that the entire CSV now obeys strict physical top-to-bottom order. The following conflicts or ambiguities are visible in the existing position labels and source correspondence alone; they require the primary reader's judgment, and no original scan was opened for this audit.", "",
        "| Page | Retained manual rows | Review issue |",
        "| --- | --- | --- |",
        "| 15/197 | 003, then 999 | Bottom page number precedes an added left-margin stroke; the stroke's vertical extent is not specified. |",
        "| 15/203 | 010, then 999 | Bottom page number precedes an added bottom-left stroke; relative height remains unspecified. |",
        "| 15/211 | 009, then 999 | The bottom-left page number precedes the far-left long vertical line (source line 5). The spanning line has no unique vertical rank. |",
        "| 15/215 | 007, 008, 009, 1000, 1001 | Manual 007 is bottom text, 008 is left upper-margin bars, 009 is bottom pagination, and 1000 is an upper insertion ellipse. These retained labels do not form a strict vertical order. |",
        "| 15/217 | 006, then 1000 | Bottom page number precedes the ellipse inside the lower insertion (source line 21); relative height should be checked by the primary reader. |",
        "| 18/11 | 018, then 1000, 1001 | Bottom-right consequence equations precede two added upper-right diagrams. Their generated wrappers/notes remain beside these retained diagram rows in the proposal, so that portion also stays late. |",
        "| 18/16 | 011, then 012 | Bottom equation (32) precedes marks described as left of (30)–(31). This page has no generated rows, so its order is untouched. |",
        "", "## Sheet classification and element coverage", "",
        f"Canonical/per-page-record `sheet_kind` inconsistencies: {len(sheet_issues)}. Every page has a single allowed classification matching its saved manual record. This verifies metadata agreement only; it does not independently establish whether a sheet is reused typescript, a cover, or another physical class.", "",
        f"All prescribed generated macro classes are covered exactly once. Dedicated pagination rows appear absent for {len(missing_page_numbers)} `\\mspage` markers on {len(set(p for p,l,v,k in missing_page_numbers))} pages. These page numbers are present in the frozen transcription; the issue is inventory granularity/coverage. The proposal deliberately adds nothing.", "",
        "| Page | Page TeX line | Frozen pagination marker | Existing sheet_kind | Suggested new ID |",
        "| --- | --- | --- | --- | --- |",
    ]
    report.extend(f"| {p[0]}/{p[1]} | {line} | `\\mspage{{{md(value)}}}` | `{kind}` | {addition['element']} |"
                  for (p,line,value,kind),addition in zip(missing_page_numbers,additions))
    report.extend([
        "", "On 15/211 line 24, the live underlined heading `\\uline{\\deleted{\\unsure{de X}} \\unsure{car $p$}}` has no obvious separate manual heading row. Its deletion has generated row 1010, which is associated in the proposal with manual 005 (`Pts banaux; Pts à valeurs dans Z_l ou Q_l`). That broader row may have been intended to cover the heading; this is a possible granularity gap, not an asserted missing transcription.", "",
        "The counts of explicit `\\diagram`/`\\figure` wrappers and manual `diagram`/`drawing` rows were also compared. Count differences, if any, are signals for review, since a compound drawing or inline object may be represented differently at the two levels.", "",
        "| Page | TeX wrapper | Wrapper count | Manual kind | Row count |",
        "| --- | --- | --- | --- | --- |",
    ])
    report.extend(f"| {p[0]}/{p[1]} | `{macro}` | {mc} | `{kind}` | {rc} |" for p,macro,mc,kind,rc in picture_counts)
    if not picture_counts:
        report.append("| All 49 pages | diagram / figure | — | diagram / drawing | Counts agree per page |")
    report.extend(["", "## Source-boundary and wrapper cases requiring review", "",
                   "| Page | Generated element | Macro start | Placement | Reason |",
                   "| --- | --- | --- | --- | --- |"])
    for pair,row,macro,anchor in audit:
        if anchor is not None and anchor["status"] != "S":
            report.append(f"| {pair[0]}/{pair[1]} | {row['element']} ({row['kind']}) | {macro.line}:{macro.column} | {anchor['side']} manual {anchor['element']} | {STATUS[anchor['status']]} |")
    report.extend(["", "## Unmatched, ambiguous and duplicate-key anchors", "",
                   f"Unmatched: `{md(unmatched)}`.", "", f"Ambiguous: `{md(ambiguous)}`.", "",
                   f"Duplicate exact keys (resolved only by source occurrence order): `{md(duplicates)}`.", "",
                   "## Page counts", "",
                   "| Page | Manual rows | Generated rows | Boundary/wrapper review rows |",
                   "| --- | --- | --- | --- |"])
    report.extend(f"| {p[0]}/{p[1]} | {m} | {a} | {review} |" for p,m,a,review in page_counts)
    report.extend(["", "## Complete generated-row anchor ledger", "",
                   "Source references are to individual `pages/MPL_15_195-228+18_002-017_C_scanNNN.tex` files. Line:column identifies the opening backslash of the exact macro. IDs are preserved, so the proposed sequence need not be numerically ascending.", "",
                   "| Page | Generated ID | Kind | Macro line:column | Parent manual ID | Parent excerpt | Placement/status |",
                   "| --- | --- | --- | --- | --- | --- | --- |"])
    for pair,row,macro,anchor in audit:
        if anchor is None:
            parent_id, excerpt, placement = "—", "—", "Unresolved; retained at tail"
        else:
            parent_id = anchor["element"]
            parent = next(r for r in pages[pair] if r["element"] == parent_id)
            excerpt = parent["first_words_or_objects"][:100]
            placement = anchor["side"] + "; " + STATUS[anchor["status"]]
        report.append(f"| {pair[0]}/{pair[1]} | {row['element']} | {row['kind']} | {macro.line}:{macro.column} | {parent_id} | {md(excerpt)} | {placement} |")
    report.extend(["", "## Reproduction", "",
                   "Run `python records/inventory_order_proposal.py`. The helper validates all frozen hashes and all exact macro matches before writing only the proposal CSV, separate pagination-suggestion CSV and this report. It never invokes the finalizer's write path, never changes canonical CSV, pages, combined TeX, original per-page records or notes, and disables bytecode cache writes. Root should review the flagged cases before deciding whether to adopt any permutation or suggested additions.", ""])
    (RECORDS / "inventory_order_report.md").write_text("\n".join(report))
    print(json.dumps(dict(rows=len(rows), generated_rows=len(audit), unmatched=len(unmatched),
                          ambiguous=len(ambiguous), duplicate_keys=len(duplicates),
                          boundary_wrapper_rows=sum(a is not None and a['status'] != 'S' for p,r,m,a in audit),
                          pagination_markers_without_rows=len(missing_page_numbers),
                          sheet_kind_issues=sheet_issues, picture_count_differences=picture_counts,
                          input_sha256=input_hash, proposal_sha256=hashlib.sha256(csv_data).hexdigest()), indent=2))

if __name__ == "__main__":
    main()
