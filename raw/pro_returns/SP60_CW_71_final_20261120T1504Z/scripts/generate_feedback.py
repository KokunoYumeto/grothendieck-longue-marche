#!/usr/bin/env python3
"""Regenerate sheet feedback from recorded metadata, without reading source scans.

This script does not decide readings or modify pages, decisions, or doubts.
The manually named issue families below refer to the primary reader's existing
place/scan_shows records. Counts always come from the current decision table.
Run after the last edit to decisions.tsv or doubt_records.tsv.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


PREFIX = "SP60_CW_71"
CATEGORIES = [
    ("1. Symbols and indices", "misread symbol or index"),
    ("2. Words", "misread word"),
    ("3. Omissions", "omission"),
    ("4. Drawings and diagrams", "drawing or diagram"),
    ("5. Readable ink left as illegible", r"readable ink left as \ill{}"),
    ("6. Insertions put in the wrong place", "insertion or placement"),
    ("7. Struck text / deletion state", "deletion state (struck given live or live given struck)"),
    ("8. Abbreviations expanded or spelling modernised", "abbreviation expanded or spelling modernised"),
    ("9. Text that is not on the page", "text not on the page"),
    ("10. Other", "other"),
]

# These are whole source-block gaps, identified from the recorded place sizes
# and source-coverage descriptions, not from a fresh reading of witness H.
COVERAGE_IDS = (
    {f"038-H{i:02}" for i in range(1, 9)}
    | {f"047-HB{i:02}" for i in range(1, 8)}
    | {f"048-HB{i:02}" for i in range(1, 8)}
)

# Descriptions summarize only the saved place/scan_shows metadata. All are
# cross-cutting issue families; they must not be added to the category totals.
ISSUES = [
    (
        "Small tails, stems, raised marks, and overwritten numerals",
        ["042-C1", "042-C2", "043-C2", "045-C02", "047-H01"],
        "The records distinguish a descending tail, projecting crossbar, raised mark, or retraced stem; several decisions remain explicitly uncertain.",
        "Already covered by symbols and indices; keep the distinction between a visible mark and an expected formula.",
    ),
    (
        "Cancellation state and the reading underneath are separate decisions",
        ["039-C1", "039-C2", "044-C07", "047-H03", "048-C02"],
        "The records separately identify overstriking or deletion and the surviving word ending, letter shape, or case.",
        "Already covered by struck text and words/symbols; a resolved deletion state need not resolve the cancelled reading.",
    ),
    (
        "Flat accent strokes and uncertain accent absence",
        ["040-C1", "040-C2", "040-C3", "047-C02"],
        "The records describe near-horizontal accent marks or the absence of a securely visible circumflex, with alternatives retained.",
        "Already covered by spelling and normalization; preserve shape uncertainty instead of silently choosing the conventional accent.",
    ),
    (
        "Repeated cramped letter junctions",
        ["044-C02", "044-C03"],
        "Two occurrences are recorded as having the same extra undotted minim at a cramped junction.",
        "Already covered by words and the hand log; the two locations remain separate change places.",
    ),
    (
        "Faint, slanted marginal annotations recovered only in part",
        ["047-H02", "047-H03", "048-C05", "048-H01", "048-H02", "048-H03", "048-H05"],
        "The records document rotated crops and distinguish recoverable strokes from unresolved endings or alternative readings.",
        "Already covered by readable ink left illegible; these are partial recoveries, not claims of complete certainty.",
    ),
    (
        "Long adjoining strokes can resemble punctuation",
        ["043-C4", "048-C03"],
        "One record retains uncertainty about a long final curved mark; another records no separate punctuation where letter, attachment, and following-word strokes meet.",
        "A useful subtype of symbol/other or text-not-on-page decisions; decide a punctuation mark separately from an adjacent connector.",
    ),
]

REFINEMENTS = [
    (
        "Rules surrounding folios and references",
        ["038-H13", "043-C1", "044-C01", "044-C04", "045-C01", "047-C01", "048-C01"],
        "Parallel rules above and below a folio or reference are recorded as omitted marks. This is a recurring completeness issue even where the numeral itself was already present.",
    ),
    (
        "Detached points retained without an assigned mathematical meaning",
        ["043-C3", "044-C05", "044-C08"],
        "The records retain small detached or raised points, including a point at a word's line division, without forcing a conventional mathematical interpretation. The feedback concerns each mark's presence, not its meaning.",
    ),
    (
        "Connected annotation enclosures, notches, and side strokes",
        ["047-C03", "047-C04", "048-C04", "048-C06"],
        "The records identify a continuous enclosure, insertion notch, lower connecting rule, or long side mark. These refine the existing drawing/placement categories: a connector need not be emphasis or cancellation.",
    ),
]


def load(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def canonical_kind(value: str) -> str:
    value = value.replace("`", "").strip()
    while "\\\\" in value:
        value = value.replace("\\\\", "\\")
    return value


def md(value: object) -> str:
    return str(value).replace("|", "&#124;").replace("\n", "<br>")


def table(headers: list[str], rows: list[list[object]]) -> str:
    return (
        "| " + " | ".join(headers) + " |\n"
        + "|" + "|".join("---" for _ in headers) + "|\n"
        + "".join("| " + " | ".join(md(value) for value in row) + " |\n" for row in rows)
    )


def identifiers(rows: list[dict[str, str]]) -> str:
    ordered = sorted(rows, key=lambda row: (int(row["scan"]), row["id"]))
    return ", ".join("`" + row["id"] + "`" for row in ordered) or "None"


def family_rows(families: list[tuple], by_id: dict[str, dict[str, str]], with_scope: bool) -> list[list[object]]:
    result = []
    for family in families:
        title, ids, description, *scope = family
        present = [by_id[identifier] for identifier in ids if identifier in by_id]
        if len(present) < 2:
            continue
        row = [title, identifiers(present), description]
        if with_scope:
            row.append(scope[0])
        result.append(row)
    return result


def generate(output: Path) -> Path:
    decisions_path = output / "decisions.tsv"
    decisions = load(decisions_path)
    if not decisions_path.is_file():
        raise SystemExit("decisions.tsv is required")
    duplicate_ids = [key for key, count in Counter((r["scan"], r["id"]) for r in decisions).items() if count > 1]
    if duplicate_ids:
        raise SystemExit(f"Resolve duplicate decision IDs before generating feedback: {duplicate_ids}")
    changes = [r for r in decisions if r["against_C"] == "yes" or r["against_H"] == "yes"]
    allowed = {kind for _, kind in CATEGORIES}
    unknown = sorted({canonical_kind(r["kind"]) for r in changes} - allowed)
    if unknown:
        raise SystemExit(f"Unrecognized primary categories: {unknown}")
    by_id = {r["id"]: r for r in changes}
    counts = []
    for title, kind in CATEGORIES:
        selected = [r for r in changes if canonical_kind(r["kind"]) == kind]
        c = sum(r["against_C"] == "yes" for r in selected)
        h = sum(r["against_H"] == "yes" for r in selected)
        overlap = sum(r["against_C"] == "yes" and r["against_H"] == "yes" for r in selected)
        counts.append([title, c, h, overlap, len(selected)])
    totals = [sum(row[index] for row in counts) for index in range(1, 5)]
    counts.append(["Total", *totals])
    h_rows = [r for r in changes if r["against_H"] == "yes"]
    coverage = [r for r in h_rows if r["id"] in COVERAGE_IDS and canonical_kind(r["kind"]) == "omission"]
    local_omissions = [r for r in h_rows if canonical_kind(r["kind"]) == "omission" and r not in coverage]
    recoveries = [r for r in h_rows if canonical_kind(r["kind"]) == r"readable ink left as \ill{}"]
    other_h = [r for r in h_rows if r not in coverage and r not in local_omissions and r not in recoveries]
    confidence = Counter(r["confidence"] for r in changes)
    retained = [r for r in decisions if r not in changes]
    doubt_rows = load(output / "doubt_records.tsv")
    doubt_status = Counter(r["status"] for r in doubt_rows)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    source_hash = hashlib.sha256(decisions_path.read_bytes()).hexdigest()
    lines = [
        "# SP60_CW_71 — Feedback on the error sheet\n\n",
        f"Generated from the recorded decisions on {now}. This is a mechanical account of the primary reader's saved decisions, not an additional reading of the scans or witnesses. Regenerate it after any decision or doubt-status update.\n\n",
        "## Read H's omission count as a coverage measure\n\n",
        f"**Of {len(h_rows)} discrepancy rows against H, {len(coverage)} represent broad source-block coverage gaps and {len(local_omissions)} are local or additional omissions. These must not be presented as {len(coverage) + len(local_omissions)} attempted readings that H got wrong.** The remaining H rows comprise {len(recoveries)} partial recoveries from illegibility placeholders and {len(other_h)} other recorded differences.\n\n",
        "The source-block group records places where H's editorial descriptions or short source locators do not supply the full source text. Local omissions concern such things as marginal marks, folio rules, trailing marks, or side strokes. A description in an editorial note does not supply a diplomatic transcription of the described source. No H discrepancy rows are counted for scans 39–46, where H has only description or no source text.\n\n",
        "This is not an error-rate comparison between the witnesses: their coverage differs, and a recorded place can range from one mark to several omitted lines. The source-block classification below follows the saved place/coverage records; it does not come from a fresh examination of H.\n\n",
        "## Counts for all ten error-sheet categories\n\n",
        "Each changed decision place has one **primary category**. The same row counts once against each witness it differs from, once in overlap if it differs from both, and once in distinct places. Thus distinct = C + H − overlap. Counts include changes that remain explicitly uncertain; they are recorded differences, not uniformly certain corrections.\n\n",
        table(["Error-sheet category", "Against C", "Against H", "Overlap", "Distinct places"], counts),
        "\nThe primary category belongs to the place, not separately to each witness's cause of error. If C and H differ for different reasons at one place, both witness columns inherit the stored category; the table does not silently invent separate per-witness diagnoses. For example, `048-C05` is stored under recovered illegibility, while its scan record also discusses a compressed versus expanded form. Its witness-specific causes must be read in the changes log.\n\n",
        f"Confidence of the {len(changes)} changed-place records: high {confidence['high']}, medium {confidence['medium']}, low {confidence['low']}.\n\n",
        "## Retentions and certainty are separate ledgers\n\n",
        f"There are {len(retained)} decision rows with neither witness-change flag set; they document retained readings or crop decisions and contribute zero to the discrepancy table. The doubt ledger contains {doubt_status['resolved']} resolved certainty entries, {doubt_status['remaining']} remaining entries, and {doubt_status['retained']} explicitly retained-doubt entries. These ledgers may refer to the same places and must not be added together. A certainty change without a changed reading does not enter the discrepancy counts.\n\n",
        "## H coverage and recovery breakdown\n\n",
    ]
    h_breakdown = []
    for scan in sorted({int(r["scan"]) for r in h_rows}):
        groups = [coverage, local_omissions, recoveries, other_h]
        values = [sum(int(r["scan"]) == scan for r in group) for group in groups]
        h_breakdown.append([scan, *values, sum(values)])
    h_breakdown.append(["Total", len(coverage), len(local_omissions), len(recoveries), len(other_h), len(h_rows)])
    lines.append(table(["Scan", "Broad source-block gaps", "Local/additional omissions", "Partial illegibility recoveries", "Other differences", "All H rows"], h_breakdown))
    lines += [
        "\nBroad source-block coverage IDs: " + identifiers(coverage) + ".\n\n",
        "Local/additional omission IDs: " + identifiers(local_omissions) + ".\n\n",
        "Partial recovery IDs: " + identifiers(recoveries) + ".\n\n",
        "Other H difference IDs: " + identifiers(other_h) + ".\n\n",
        "## Recurring issues already covered by the sheet\n\n",
        "These families are supported by the saved `place` and `scan_shows` records. They cut across primary categories and are not extra rows to add to the totals. Wording such as 'favors' or 'uncertain' in an underlying record remains in force.\n\n",
        table(["Recurring issue", "Decision IDs", "What the saved records document", "Use in the next run"], family_rows(ISSUES, by_id, True)),
        "\n## Specific refinements for the next error sheet\n\n",
        "The metadata establish no new mutually exclusive error class beyond the ten categories. They do support the following recurring subtypes, which the broad sheet does not name individually. H's partial-quotation coverage is an additional comparison issue, addressed prominently above; it should remain distinct from misreading attempted source text.\n\n",
        table(["Refinement", "Decision IDs", "Recorded issue"], family_rows(REFINEMENTS, by_id, False)),
        "\n## Bookkeeping limits and regeneration\n\n",
        "The totals count unique decision IDs. Identical normalized scan/place labels are checked below, but differently worded labels can still refer to the same physical place; only the primary reader can settle that. A zero category means no changed place currently carries that primary classification, not that the associated feature was absent from the manuscript.\n\n",
    ]
    place_groups = defaultdict(list)
    for row in changes:
        key = (row["scan"], " ".join(row["place"].casefold().split()))
        place_groups[key].append(row["id"])
    repeated = [(scan, ids) for (scan, _), ids in place_groups.items() if len(ids) > 1]
    if repeated:
        lines.append("Repeated exact scan/place labels requiring count review:\n\n")
        lines.extend(f"- Scan {scan}: {', '.join(ids)}.\n" for scan, ids in repeated)
    else:
        lines.append("No duplicate decision IDs or repeated exact normalized scan/place labels occur in the changed-place ledger.\n")
    lines += [
        "\nRegenerate only this feedback file with `python3 scripts/generate_feedback.py .` from the package directory. The script reads metadata tables and writes this file; it does not alter page files, decision records, doubt records, or the combined transcription. Its named issue families are summaries of already recorded evidence and are not new manuscript judgments.\n\n",
        f"Decision-table SHA-256 at generation: `{source_hash}`.\n",
    ]
    destination = output / f"{PREFIX}_sheet_feedback.md"
    destination.write_text("".join(lines), encoding="utf-8")
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_directory", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    destination = generate(args.output_directory.resolve())
    print(destination)


if __name__ == "__main__":
    main()
