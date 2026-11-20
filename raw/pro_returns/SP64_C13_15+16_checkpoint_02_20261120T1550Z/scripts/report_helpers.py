#!/usr/bin/env python3
"""Regenerate structural reports from the primary reader's recorded tables.

This module reads the recorded tables and progress log only. It does not open
page files, scans, witnesses, or the combined transcription. It reproduces
recorded readings in reports without selecting or revising any reading.

Usage: python scripts/report_helpers.py WORK_DIR

The CLI regenerates doubts.md, refreshes the managed count section of
sheet_feedback.md, and refreshes the managed crop register in changes.md.
workflow.rebuild() also calls these functions. No ZIP is created here.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import tempfile
from collections import Counter
from pathlib import Path


PREFIX = "SP64_C13_15+16"
ORDER = tuple(
    [("15", str(number)) for number in (180, 183, 184, 185, 187, 189, 190, 191, 192, 193, 194)]
    + [("16", f"{number:03d}") for number in range(3, 17)]
)
SCHEMAS = {
    "notation.tsv": ("notation", "written_form", "scans"),
    "remaining_doubts.tsv": ("scan", "line", "reading", "alternatives", "confidence"),
    "abbreviations.tsv": ("form", "expansion", "scans"),
    "certainty_only.tsv": ("scan", "line", "old_mark", "reading", "evidence", "confidence"),
    "decisions.tsv": ("id", "cote", "scan", "decision", "reading", "what the ink shows", "crop", "confidence"),
    "changes_records.tsv": (
        "cote", "scan", "place", "C", "H", "final", "scan_shows", "confidence",
        "kind", "against_C", "against_H", "crop", "consequential",
    ),
}
OPTIONAL_TABLES = {"certainty_only.tsv"}
CROP_START = "<!-- BEGIN GENERATED CROP REGISTER -->"
CROP_END = "<!-- END GENERATED CROP REGISTER -->"
COUNTS_START = "<!-- BEGIN GENERATED CHANGE COUNTS -->"
COUNTS_END = "<!-- END GENERATED CHANGE COUNTS -->"
DOUBTS_START = "<!-- BEGIN GENERATED DOUBTS REGISTERS -->"
DOUBTS_END = "<!-- END GENERATED DOUBTS REGISTERS -->"
LEGIBILITY_HEADING = "## Final legibility observations"
LEGIBILITY_START = "<!-- BEGIN FINAL LEGIBILITY OBSERVATIONS -->"
LEGIBILITY_END = "<!-- END FINAL LEGIBILITY OBSERVATIONS -->"
OBSERVATION_HEADING = "## Final legibility and pattern observations"
OBSERVATION_START = "<!-- BEGIN FINAL LEGIBILITY AND PATTERN OBSERVATIONS -->"
OBSERVATION_END = "<!-- END FINAL LEGIBILITY AND PATTERN OBSERVATIONS -->"
CROP_PATTERN = re.compile(
    r"^crop (?P<cote>[0-9]+)/(?P<scan>[0-9]{3}) "
    r"(?P<box>\([^\r\n]*?\)) (?P<label>.*?) rotation (?P<rotation>[^\r\n]+)$"
)


def read_table(work: Path, name: str) -> list[dict[str, str]]:
    with (work / name).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t", strict=True)
        if tuple(reader.fieldnames or ()) != SCHEMAS[name]:
            raise ValueError(f"{name}: unexpected header or header order")
        rows = []
        for number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"{name}: inconsistent field count at logical row {number}")
            rows.append(row)
        return rows


def atomic_write(path: Path, text: str) -> None:
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="", dir=path.parent,
            prefix=f".{path.name}.", suffix=".tmp", delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def mdcell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def table(columns: tuple[tuple[str, str], ...], rows: list[dict[str, str]]) -> list[str]:
    lines = [
        "| " + " | ".join(label for label, _ in columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    lines.extend("| " + " | ".join(mdcell(row[key]) for _, key in columns) + " |" for row in rows)
    return lines


def render_doubts(tables: dict[str, list[dict[str, str]]]) -> str:
    lines = [
        "# Doubts, notation, and abbreviations", "",
        "## Notation register", "", "Source: `notation.tsv`.", "",
    ]
    if tables["notation.tsv"]:
        lines += table((("Notation", "notation"), ("Written form", "written_form"), ("Scans", "scans")), tables["notation.tsv"])
    else:
        lines += ["No notation rows are currently recorded."]
    lines += [
        "",
        "## Remaining doubts", "",
        "Source: `remaining_doubts.tsv`.", "",
    ]
    doubts = tables["remaining_doubts.tsv"]
    if doubts:
        lines += table((
            ("Cote / scan", "scan"), ("Line / place", "line"), ("Reading", "reading"),
            ("Alternatives", "alternatives"), ("Confidence", "confidence"),
        ), doubts)
    else:
        lines += ["No rows are currently recorded in the remaining-doubts register."]
    decision_columns = (
        ("Mark ID", "id"), ("Cote", "cote"), ("Scan", "scan"), ("Reading", "reading"),
        ("What the ink shows", "what the ink shows"), ("Crop", "crop"), ("Confidence", "confidence"),
    )
    undecided = [row for row in tables["decisions.tsv"] if row["decision"] == "undecided"]
    lines += ["", "## Marked decisions still undecided", "", "Source: `decisions.tsv`, with `decision == undecided`.", ""]
    if undecided:
        lines += table(decision_columns, undecided)
    else:
        lines += ["No current decision rows have the value `undecided`."]
    first = [row for row in tables["decisions.tsv"] if row["decision"] == "first"]
    lines += [
        "", "## Resolved C uncertainty: first reading retained", "",
        "Source: `decisions.tsv`, with `decision == first`. Each listed reading "
        "selects the first reading of C's doubt mark. These rows document resolution "
        "of C's marked uncertainty and do not independently add a substantive "
        "reading-difference count. The values `alternative` and `other` record "
        "other reading choices in `decisions.tsv`.", "",
    ]
    if first:
        lines += table(decision_columns, first)
    else:
        lines += ["No current decision rows have the value `first`."]
    extra_certainty = tables.get("certainty_only.tsv", [])
    if extra_certainty:
        lines += [
            "", "## Certainty-only resolutions outside MARKS.tsv", "",
            "Source: `certainty_only.tsv`. These entries document resolutions "
            "of recorded uncertainty outside `MARKS.tsv`, including struck-text "
            "uncertainty. They do not independently add a substantive "
            "reading-difference count.", "",
        ]
        lines += table((
            ("Cote / scan", "scan"), ("Line / place", "line"), ("Old uncertainty mark", "old_mark"),
            ("Reading", "reading"), ("Evidence", "evidence"), ("Confidence", "confidence"),
        ), extra_certainty)
    lines += ["", "## Abbreviation register", "", "Source: `abbreviations.tsv`.", ""]
    if tables["abbreviations.tsv"]:
        lines += table((("Form", "form"), ("Expansion", "expansion"), ("Scans", "scans")), tables["abbreviations.tsv"])
    else:
        lines += ["No abbreviation rows are currently recorded."]
    return "\n".join(lines) + "\n"


def render_counts(work: Path, rows: list[dict[str, str]]) -> str:
    counts = {"C": Counter(), "H": Counter(), "union": Counter()}
    by_scan = {key: Counter() for key in ORDER}
    kinds = []
    both = 0
    for number, row in enumerate(rows, start=2):
        if row["against_C"] not in ("yes", "no") or row["against_H"] not in ("yes", "no"):
            raise ValueError(f"changes_records.tsv: comparison flag is not yes/no at logical row {number}")
        if not row["kind"]:
            raise ValueError(f"changes_records.tsv: empty error kind at logical row {number}")
        key = row["cote"], row["scan"]
        if key not in by_scan:
            raise ValueError(f"changes_records.tsv: unexpected cote/scan at logical row {number}")
        kind = row["kind"]
        if kind not in kinds:
            kinds.append(kind)
        against_c = row["against_C"] == "yes"
        against_h = row["against_H"] == "yes"
        both += int(against_c and against_h)
        for label, counted in (("C", against_c), ("H", against_h), ("union", against_c or against_h)):
            counts[label][kind] += int(counted)
            by_scan[key][label] += int(counted)
    totals = {label: sum(values.values()) for label, values in counts.items()}
    lines = [
        COUNTS_START, "## Recorded reading-change counts", "",
        "Source: `changes_records.tsv`. A row contributes to the C count when "
        "`against_C` is `yes`, to the H count when `against_H` is `yes`, and once "
        "to the union when either flag is `yes`. A row affecting both witnesses "
        "therefore contributes one to each witness count and one to the union. "
        "Error-kind labels are taken directly from the recorded `kind` field. "
        "Crop-log entries and certainty-only decision entries add no counts here.", "",
        f"Recorded change rows: **{len(rows)}**. Against C: **{totals['C']}**. "
        f"Against H: **{totals['H']}**. Union: **{totals['union']}**. "
        f"Against both: **{both}**. Rows with neither comparison flag set: "
        f"**{len(rows) - totals['union']}**.", "",
        "### Counts by recorded error kind", "",
        "| Error kind | Against C | Against H | Union |",
        "|---|---:|---:|---:|",
    ]
    for kind in kinds:
        lines += [f"| {mdcell(kind)} | {counts['C'][kind]} | {counts['H'][kind]} | {counts['union'][kind]} |"]
    lines += [f"| **Total** | **{totals['C']}** | **{totals['H']}** | **{totals['union']}** |", ""]
    lines += [
        "### Counts by scan", "",
        "Page-file presence is reported from filenames. Counts reflect the current "
        "register, including while the page set is incomplete.", "",
        "| Cote / scan | Page file present | Against C | Against H | Union |",
        "|---|---|---:|---:|---:|",
    ]
    for key in ORDER:
        cote, scan = key
        present = "yes" if (work / "pages" / f"{cote}_scan{scan}.tex").is_file() else "no"
        values = by_scan[key]
        lines += [f"| {cote}/{scan} | {present} | {values['C']} | {values['H']} | {values['union']} |"]
    lines += [f"| **Total** | | **{totals['C']}** | **{totals['H']}** | **{totals['union']}** |", COUNTS_END]
    return "\n".join(lines)


def replace_managed(existing: str, block: str, start: str, end: str) -> str | None:
    starts, ends = existing.count(start), existing.count(end)
    if not starts and not ends:
        return None
    if starts != 1 or ends != 1:
        raise ValueError("Managed report markers are incomplete or duplicated; existing prose was left unchanged")
    left, right = existing.index(start), existing.index(end)
    if right < left:
        raise ValueError("Managed report markers are out of order; existing prose was left unchanged")
    return existing[:left] + block + existing[right + len(end):]


def legacy_doubts_prose(existing: str) -> str:
    """Retain reader prose when adopting a report written before managed markers."""
    owned_headings = {
        "## Notation register", "## Remaining doubts", "## Marked decisions still undecided",
        "## Resolved C uncertainty: first reading retained",
        "## Certainty-only resolutions outside MARKS.tsv", "## Abbreviation register",
    }
    template = render_doubts({name: [] for name in SCHEMAS})
    generated_lines = set(template.splitlines()) | {
        "These tables reproduce the current registers in source-row order. The registers may grow while the reading proceeds.",
        "Source: `certainty_only.tsv`. These entries document resolutions of recorded uncertainty outside `MARKS.tsv`, including struck-text uncertainty. They do not independently add a substantive reading-difference count.",
    }
    kept = []
    in_owned_section = False
    skipped_title = False
    for line in existing.splitlines(keepends=True):
        bare = line.rstrip("\r\n")
        if not skipped_title and bare.startswith("# "):
            skipped_title = True
            continue
        if bare.startswith("## "):
            in_owned_section = bare in owned_headings
            if in_owned_section:
                continue
        if bare == "":
            kept.append(line)
        elif in_owned_section and (bare.startswith("| ") or bare in generated_lines):
            continue
        elif bare not in generated_lines:
            kept.append(line)
    result = "".join(kept).strip("\r\n")
    return result + "\n" if result else ""


def render_doubts_document(work: Path, tables: dict[str, list[dict[str, str]]]) -> str:
    generated = render_doubts(tables)
    title, _, body = generated.partition("\n")
    block = DOUBTS_START + "\n" + body.lstrip("\n") + DOUBTS_END
    path = work / f"{PREFIX}_doubts.md"
    existing = path.read_text(encoding="utf-8") if path.is_file() else ""
    updated = replace_managed(existing, block, DOUBTS_START, DOUBTS_END)
    if updated is None:
        preserved = legacy_doubts_prose(existing)
        updated = title + "\n\n" + block + "\n" + ("\n" + preserved if preserved else "")
    if not re.search(r"(?m)^" + re.escape(LEGIBILITY_HEADING) + r"[ \t]*$", updated):
        updated += "\n\n" + "\n".join((
            LEGIBILITY_HEADING, "", LEGIBILITY_START,
            "_Primary reader: add the final legibility assessment here._",
            LEGIBILITY_END, "",
        ))
    return updated


def render_sheet_feedback(work: Path, rows: list[dict[str, str]]) -> str:
    path = work / f"{PREFIX}_sheet_feedback.md"
    existing = path.read_text(encoding="utf-8") if path.is_file() else ""
    block = render_counts(work, rows)
    updated = replace_managed(existing, block, COUNTS_START, COUNTS_END)
    if updated is None:
        title = re.match(r"\A(?:\ufeff)?# [^\n]*(?:\n|$)", existing)
        if title:
            updated = existing[:title.end()] + "\n" + block + "\n\n" + existing[title.end():]
        else:
            updated = "# Sheet feedback\n\n" + block + "\n\n" + existing
    if not re.search(r"(?m)^" + re.escape(OBSERVATION_HEADING) + r"[ \t]*$", updated):
        separator = "\n\n" if updated.endswith("\n") else "\n\n\n"
        updated += separator + "\n".join((
            OBSERVATION_HEADING, "", OBSERVATION_START,
            "_Primary reader: add the final legibility assessment and recurring-pattern observations here._",
            OBSERVATION_END, "",
        ))
    return updated


def crop_register_markdown(work: Path) -> str:
    progress = work / "progress.log"
    grouped: dict[tuple[str, str], list[dict[str, str]]] = {}
    if progress.is_file():
        for number, line in enumerate(progress.read_text(encoding="utf-8-sig").splitlines(), start=1):
            if not line.startswith("crop "):
                continue
            match = CROP_PATTERN.fullmatch(line)
            if match is None:
                raise ValueError(f"progress.log: crop entry at line {number} has an unrecognized format")
            row = match.groupdict()
            row["log_line"] = str(number)
            grouped.setdefault((row["cote"], row["scan"]), []).append(row)
    lines = [
        CROP_START, "## Per-scan crop register", "",
        "Source: crop entries in `progress.log`. Every logged box is listed in log "
        "order within its scan, including diagnostic crops and crops showing "
        "neighbouring fragments. These entries document image review and add no "
        "substantive reading-change counts.", "",
    ]
    if not progress.is_file():
        lines += ["The progress log is unavailable; crop coverage has not been established.", ""]
    elif not grouped:
        lines += ["No crop entries are currently recorded in the progress log.", ""]
    keys = [key for key in ORDER if key in grouped] + [key for key in grouped if key not in ORDER]
    for cote, scan in keys:
        lines += [f"### Cote {cote}, scan {scan}", ""]
        lines += table((
            ("Log line", "log_line"), ("Crop label", "label"),
            ("Box (x0, y0, x1, y1)", "box"), ("Rotation", "rotation"),
        ), grouped[(cote, scan)])
        lines += [""]
    lines += [CROP_END]
    return "\n".join(lines)


def refresh_crop_register(work: Path) -> None:
    path = work / f"{PREFIX}_changes.md"
    existing = path.read_text(encoding="utf-8") if path.is_file() else "# Changes and visual evidence\n"
    block = crop_register_markdown(work)
    updated = replace_managed(existing, block, CROP_START, CROP_END)
    if updated is None:
        updated = existing + ("" if existing.endswith("\n") else "\n") + "\n" + block + "\n"
    atomic_write(path, updated)


def rebuild_reports(work: Path) -> None:
    work = Path(work)
    tables = {
        name: ([] if name in OPTIONAL_TABLES and not (work / name).is_file() else read_table(work, name))
        for name in SCHEMAS
    }
    doubts = render_doubts_document(work, tables)
    feedback = render_sheet_feedback(work, tables["changes_records.tsv"])
    atomic_write(work / f"{PREFIX}_doubts.md", doubts)
    atomic_write(work / f"{PREFIX}_sheet_feedback.md", feedback)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("work_dir", type=Path)
    args = parser.parse_args(argv)
    work = args.work_dir.expanduser().resolve()
    if not work.is_dir():
        parser.error("work_dir is unavailable or is not a directory")
    try:
        rebuild_reports(work)
        refresh_crop_register(work)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        parser.exit(1, f"Report generation failed: {exc}\n")
    print("Refreshed doubts.md, sheet_feedback.md counts, and changes.md crop register.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
