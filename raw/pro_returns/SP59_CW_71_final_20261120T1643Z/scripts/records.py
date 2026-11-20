#!/usr/bin/env python3
"""Mechanical record keeping for SP59_CW_71.

No OCR, image reading, mathematical decisions, or TeX compilation is performed.
All readings and descriptions are supplied explicitly by the sole page reader.
The TSV/CSV/Markdown records are authoritative; build() regenerates summaries.
Run `python output/scripts/records.py build` or `... validate` from any directory.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
PREFIX = "SP59_CW_71"
FOLDERS = {
    **{n: "J71-01" for n in (7, 8, 9, 10)},
    **{n: "J71-02" for n in (11, 12, 13, 14, 15, 17, 19)},
    **{n: "J71-03" for n in (21, 22, 23, 24, 25, 26, 27)},
    **{n: "J71-04" for n in (28, 29, 30, 31, 32, 33, 34)},
}
H_STATUS = {n: ("nothing" if n in (9, 15, 26) else "desc" if n in (24, 28) else "text") for n in FOLDERS}
CHANGE_FIELDS = ["id", "place", "C", "H", "final", "scan_shows", "confidence", "diff_C", "diff_H", "kind", "error_kind", "marked_H", "consequential", "S_id"]
INVENTORY_FIELDS = ["scan", "sheet_kind", "hand", "element", "kind", "position", "first_words_or_objects", "transcribed"]
DOUBT_FIELDS = ["place", "reading", "alternatives", "confidence", "status"]
HAND_FIELDS = ["habit", "occurrences", "scope", "misreadings"]
NOTATION_FIELDS = ["sign", "form", "scans", "remarks"]
ABBREVIATION_FIELDS = ["abbreviation", "expansion", "scans", "remarks"]
CHECK_FIELDS = ["statement_id", "date", "who", "type", "outcome"]
COLLATION_FIELDS = ["folder", "their_page", "our_scan", "line", "their_reading", "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H", "confidence"]
KINDS = {"misread word", "misread symbol or index", "omission", "text not on the page", "deletion state (struck given live or live given struck)", "insertion or placement", "abbreviation expanded or spelling modernised", "readable ink left as \\ill{}", "drawing or diagram", "other"}
CHECK_TYPES = {"targeted proof check", "independent re-proof", "computation or formal certificate", "used and rechecked in this run", "carried as background without fault found"}
ERROR_CATEGORIES = ["Symbols and indices", "Words", "Omissions", "Drawings and diagrams", "Readable ink left as illegible", "Insertions put in the wrong place", "Struck text", "Abbreviations expanded, spelling modernised", "Text that is not on the page", "Other"]


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def as_bool(value):
    return value is True or str(value).strip().lower() in {"1", "true", "yes", "y"}


def cell(value):
    return str(value if value is not None else "").replace("|", "\\|").replace("\r\n", "\n").replace("\n", "<br>")


def table(headers, rows):
    lines = ["| " + " | ".join(map(cell, headers)) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines.extend("| " + " | ".join(map(cell, row)) + " |" for row in rows)
    return "\n".join(lines) + "\n"


def write_text(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(str(value).rstrip() + "\n", encoding="utf-8")


def write_rows(path, fields, rows, delimiter="\t"):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=delimiter, extrasaction="raise", lineterminator="\n")
        writer.writeheader()
        for source in rows:
            row = {key: source.get(key, "") for key in fields}
            for key, value in row.items():
                if isinstance(value, bool):
                    row[key] = "yes" if value else "no"
                elif value is None:
                    row[key] = ""
            writer.writerow(row)


def read_rows(path, delimiter="\t"):
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=delimiter))


def extra(name):
    p = OUT / name
    return p.read_text(encoding="utf-8").strip() if p.exists() else ""


def page_name(scan):
    scan = int(scan)
    if scan not in FOLDERS:
        raise ValueError(f"Scan {scan} is not in the 25-page task")
    return f"{FOLDERS[scan]}_71_scan{scan:03d}.tex"


def record_dir(scan):
    return OUT / "records" / f"scan{int(scan):03d}"


def log_event(message):
    progress = OUT / "progress.log"
    if not progress.exists() or not progress.read_text(encoding="utf-8").strip():
        raise RuntimeError("Root must initialize progress.log with the actual starting UTC time before recording a page")
    with progress.open("a", encoding="utf-8") as f:
        f.write(message + "\n")


def record_page(scan, tex, changes, inventory, notes, doubts=None, hand=None,
                notation=None, abbreviations=None, checks=None, unresolved=None,
                audit=None):
    """Save one reader-decided page and regenerate current deliverables.

    `tex` and `notes` are literal strings. List entries are dictionaries with
    field names given by the constants above. A missing flag means false.
    Calling this again replaces that page's records; it does not merge them.
    Unresolved may be a Markdown string or a list of strings. No assertion of
    page completion is made until all records and the combined files are saved.
    """
    scan = int(scan)
    filename = page_name(scan)
    progress = OUT / "progress.log"
    if not progress.exists() or not progress.read_text(encoding="utf-8").strip():
        raise RuntimeError("Initialize progress.log before record_page()")
    if not isinstance(tex, str) or not tex.strip():
        raise ValueError("tex must be the complete nonempty page transcription")
    if not re.search(r"\\scanpage\s*\{\s*" + str(scan) + r"\s*\}", tex):
        raise ValueError(f"Page text must contain \\scanpage{{{scan}}}")
    d = record_dir(scan)
    d.mkdir(parents=True, exist_ok=True)
    cooked_changes = []
    for i, source in enumerate(changes, 1):
        row = dict(source)
        row.setdefault("id", f"71-{scan:03d}-{i:03d}")
        row.setdefault("confidence", "medium")
        row.setdefault("diff_C", False)
        row.setdefault("diff_H", False)
        row.setdefault("kind", "other")
        row.setdefault("error_kind", "Other")
        row.setdefault("marked_H", "no")
        row.setdefault("consequential", "")
        row.setdefault("S_id", "")
        if as_bool(row["diff_H"]) and H_STATUS[scan] != "text":
            raise ValueError(f"H has {H_STATUS[scan]} for scan {scan}; no H collation rows are allowed")
        cooked_changes.append(row)
    cooked_inventory = []
    for i, source in enumerate(inventory, 1):
        row = dict(source)
        row["scan"] = scan
        row.setdefault("sheet_kind", "text")
        row.setdefault("hand", "his hand")
        row.setdefault("element", f"{scan:03d}-{i:02d}")
        row.setdefault("transcribed", "yes")
        cooked_inventory.append(row)
    cooked_checks = []
    for source in checks or []:
        row = dict(source)
        row.setdefault("date", datetime.now(timezone.utc).date().isoformat())
        row.setdefault("who", "GPT-6 Astra Pro; effort not exposed; SP59_CW_71 second pass")
        cooked_checks.append(row)
    cooked_notation = []
    for source in notation or []:
        row = dict(source)
        row.setdefault("scans", str(scan))
        cooked_notation.append(row)
    cooked_hand = []
    for source in hand or []:
        row = dict(source)
        row.setdefault("occurrences", str(scan))
        cooked_hand.append(row)
    cooked_abbr = []
    for source in abbreviations or []:
        row = dict(source)
        if "abbreviation" not in row:
            row["abbreviation"] = row.get("short", row.get("form", ""))
        if "expansion" not in row:
            row["expansion"] = row.get("full", row.get("meaning", ""))
        row.setdefault("scans", str(scan))
        cooked_abbr.append(row)
    write_text(OUT / "pages" / filename, tex)
    write_rows(d / "changes.tsv", CHANGE_FIELDS, cooked_changes)
    write_rows(d / "inventory.csv", INVENTORY_FIELDS, cooked_inventory, delimiter=",")
    write_text(d / "notes.md", notes)
    write_rows(d / "doubts.tsv", DOUBT_FIELDS, doubts or [])
    write_rows(d / "hand.tsv", HAND_FIELDS, cooked_hand)
    write_rows(d / "notation.tsv", NOTATION_FIELDS, cooked_notation)
    write_rows(d / "abbreviations.tsv", ABBREVIATION_FIELDS, cooked_abbr)
    write_rows(d / "checks.tsv", CHECK_FIELDS, cooked_checks)
    if isinstance(unresolved, str):
        unresolved_text = unresolved
    else:
        unresolved_text = "\n".join(f"- {item}" for item in unresolved or [])
    write_text(d / "unresolved.md", unresolved_text or "None recorded.")
    if audit is not None:
        write_text(d / "audit.md", audit)
    build()
    log_event(f"scan {scan:03d} done {utc_now()}")
    return OUT / "pages" / filename


def record_audit(scan, audit):
    """Record an actually completed second reading; does not modify readings."""
    scan = int(scan)
    if not (OUT / "pages" / page_name(scan)).exists():
        raise ValueError("Cannot audit an unwritten page")
    write_text(record_dir(scan) / "audit.md", audit)
    build()
    log_event(f"scan {scan:03d} audited {utc_now()}")


def load_records():
    result = []
    for scan in sorted(FOLDERS):
        d = record_dir(scan)
        page = OUT / "pages" / page_name(scan)
        if not d.is_dir() and not page.exists():
            continue
        if not d.is_dir() or not page.exists():
            raise RuntimeError(f"Incomplete page/record pair for scan {scan}")
        r = {"scan": scan, "dir": d, "page": page, "changes": read_rows(d / "changes.tsv"), "inventory": read_rows(d / "inventory.csv", ",")}
        for key in ("doubts", "hand", "notation", "abbreviations", "checks"):
            r[key] = read_rows(d / f"{key}.tsv")
        for key in ("notes", "unresolved", "audit"):
            p = d / f"{key}.md"
            r[key] = p.read_text(encoding="utf-8").strip() if p.exists() else ""
        result.append(r)
    return result


def resolved_status(status):
    s = status.strip().lower()
    if s.startswith(("unresolved", "remaining", "retained", "kept", "open")):
        return False
    # These witness-qualified statuses explicitly record the reader's resolved
    # decision. Route them without changing the saved status or the reading.
    return (s.startswith(("resolved", "confirmed", "cleared", "certainty", "removed", "settled"))
            or re.match(r"^c doubts? resolved\b", s) is not None)


def error_category(value):
    s = str(value).strip()
    match = re.match(r"^(10|[1-9])(?:[. :\-]|$)", s)
    if match:
        return ERROR_CATEGORIES[int(match.group(1)) - 1]
    aliases = {
        "symbol": 0, "indices": 0, "word": 1, "omission": 2,
        "drawing": 3, "diagram": 3, "illegible": 4, "readable ink": 4,
        "insertion": 5, "placement": 5, "struck": 6, "deletion": 6,
        "abbreviation": 7, "spelling": 7, "not on the page": 8,
        "invented": 8, "other": 9,
    }
    for name in ERROR_CATEGORIES:
        if s.lower() == name.lower():
            return name
    for name, i in aliases.items():
        if name in s.lower():
            return ERROR_CATEGORIES[i]
    return "Other"


def build():
    """Regenerate current deliverables from saved records; no completion claims."""
    OUT.mkdir(parents=True, exist_ok=True)
    records = load_records()
    tex_parts = ["\\cotefile{71}"]
    all_changes, inventory, checks, h_rows = [], [], [], []
    for r in records:
        body = re.sub(r"\\cotefile\s*\{71\}\s*", "", r["page"].read_text(encoding="utf-8")).strip()
        tex_parts.append(body)
        inventory.extend(r["inventory"])
        checks.extend(r["checks"])
        for change in r["changes"]:
            all_changes.append((r["scan"], change))
            if as_bool(change["diff_H"]) and H_STATUS[r["scan"]] == "text":
                h_rows.append(dict(zip(COLLATION_FIELDS, [FOLDERS[r["scan"]], r["scan"] - 1, r["scan"], change["place"], change["H"], change["C"], change["final"], change["scan_shows"], change["kind"], change["marked_H"], change["confidence"]])))
    write_text(OUT / f"{PREFIX}_transcription.tex", "\n\n".join(tex_parts))
    write_rows(OUT / f"{PREFIX}_inventory.csv", INVENTORY_FIELDS, inventory, ",")
    write_rows(OUT / f"{PREFIX}_collation.tsv", COLLATION_FIELDS, h_rows)
    write_rows(OUT / "CHECK_EVENTS.tsv", CHECK_FIELDS, checks)

    counts, consequential = [], []
    totals = Counter()
    for r in records:
        c = Counter()
        for row in r["changes"]:
            dc, dh = as_bool(row["diff_C"]), as_bool(row["diff_H"])
            c["C"] += dc
            c["H"] += dh
            if dc or dh:
                c["places"] += 1
                c[row["confidence"].lower()] += 1
            if row["consequential"].strip() and row["consequential"].lower() not in {"no", "false", "0"}:
                detail = row["consequential"]
                if detail.lower() in {"yes", "true", "1"}:
                    detail = f"{row['place']}: {row['final']}"
                consequential.append(f"- Scan {r['scan']:03d}, {row['id']}: {detail}")
        totals.update(c)
        counts.append([f"{r['scan']:03d}", c["C"], c["H"], c["places"], c["high"], c["medium"], c["low"]])
    counts.append(["Total", totals["C"], totals["H"], totals["places"], totals["high"], totals["medium"], totals["low"]])
    change_md = [f"# {PREFIX}: changes and decisions", "Counts refer to recorded reading differences. A place differing from both witnesses is counted once in each witness column and once in the distinct-place/confidence columns. Certainty-only decisions are listed in the doubts file. Witness-S decisions with no changed reading are retained below but do not increase the difference counts.", "## Counts", table(["Scan", "Against C", "Against H", "Distinct changed places", "High", "Medium", "Low"], counts), "## Consequential corrections", "\n".join(consequential) or "None recorded so far."]
    for r in records:
        change_md += [f"## Scan {r['scan']:03d}", f"Witness H coverage: {H_STATUS[r['scan']]} (their page {r['scan'] - 1})."]
        rows = []
        for ch in r["changes"]:
            evidence = ch["scan_shows"]
            if ch["S_id"]:
                evidence += f" [Witness S: {ch['S_id']}]"
            rows.append([ch["id"], ch["place"], ch["C"], ch["H"], ch["final"], evidence, ch["confidence"], "/".join(x for x, yes in (("C", as_bool(ch["diff_C"])), ("H", as_bool(ch["diff_H"]))) if yes) or "decision only"])
        change_md.append(table(["ID", "Place", "C", "H", "Final", "What the scan shows", "Confidence", "Differs from"], rows) if rows else "No reading differences recorded.")
        change_md += ["### Still unresolved", r["unresolved"] or "None recorded."]
    if extra("CHANGES_EXTRA.md"):
        change_md += ["## Additional decisions", extra("CHANGES_EXTRA.md")]
    write_text(OUT / f"{PREFIX}_changes.md", "\n\n".join(change_md))

    notation, remaining, resolved, abbreviations, hand = [], [], [], [], []
    for r in records:
        notation.extend([[v["sign"], v["form"], v["scans"], v["remarks"]] for v in r["notation"]])
        abbreviations.extend([[v["abbreviation"], v["expansion"], v["scans"], v["remarks"]] for v in r["abbreviations"]])
        hand.extend([[v["habit"], v["occurrences"], v["scope"], v["misreadings"]] for v in r["hand"]])
        for v in r["doubts"]:
            row = [f"{r['scan']:03d}", v["place"], v["reading"], v["alternatives"], v["confidence"], v["status"]]
            (resolved if resolved_status(v["status"]) else remaining).append(row)
    doubt_md = [f"# {PREFIX}: notation and doubts", "## Notation table", table(["Sign", "Written form / reading", "Scans", "Remarks"], notation), "## Remaining doubts", table(["Scan", "Place", "Reading", "Alternatives", "Confidence", "Status"], remaining) if remaining else "None recorded so far.", "## Resolved or confirmed certainty decisions", table(["Scan", "Place", "Reading", "Alternatives", "Confidence", "Decision"], resolved) if resolved else "None recorded so far.", "## Abbreviations", "Expansions are interpretive aids confined to this list; they do not replace the manuscript abbreviations in the transcription.", table(["Abbreviation", "Proposed expansion", "Scans", "Remarks"], abbreviations), "## Legibility and comparison of witnesses", extra("LEGIBILITY.md") or "The reader's final assessment has not yet been entered."]
    if extra("DOUBTS_EXTRA.md"):
        doubt_md += ["## Further notes", extra("DOUBTS_EXTRA.md")]
    write_text(OUT / f"{PREFIX}_doubts.md", "\n\n".join(doubt_md))

    notes = [f"# {PREFIX}: notes while reading", "These notes concern only the supplied pages. A transcription observation is not a proof check; actual mathematical check events are recorded separately in CHECK_EVENTS.tsv."]
    for r in records:
        notes += [f"## Scan {r['scan']:03d}", r["notes"] or "No note entered."]
    if extra("NOTES_EXTRA.md"):
        notes += ["## Cross-page notes", extra("NOTES_EXTRA.md")]
    write_text(OUT / f"{PREFIX}_notes.md", "\n\n".join(notes))

    hand_md = [f"# {PREFIX}: hand log", "Each entry is the reader's observation of a recurring form. Scope and exceptions are stated explicitly; a habit never substitutes for viewing an occurrence.", table(["Habit / notation", "Pages and occurrences", "Scope / exceptions", "Witness misreadings"], hand)]
    if extra("HAND_LOG_EXTRA.md"):
        hand_md += ["## Cross-page reconciliation", extra("HAND_LOG_EXTRA.md")]
    write_text(OUT / f"{PREFIX}_hand_log.md", "\n\n".join(hand_md))

    feedback_counts = Counter()
    feedback_places = {name: [] for name in ERROR_CATEGORIES}
    for scan, ch in all_changes:
        if as_bool(ch["diff_C"]) or as_bool(ch["diff_H"]):
            kind = error_category(ch["error_kind"])
            feedback_counts[kind] += 1
            feedback_places[kind].append(f"{scan:03d}/{ch['id']}")
    feedback = [f"# {PREFIX}: error-sheet feedback", "Counts use each changed place's primary recorded error category. A place differing from both C and H is counted once. Certainty-only decisions and unchanged witness-S confirmations are excluded.", table(["Error-sheet kind", "Places", "References"], [[f"{i}. {name}", feedback_counts[name], "; ".join(feedback_places[name])] for i, name in enumerate(ERROR_CATEGORIES, 1)]), "## Recurring errors not named in the sheet", extra("FEEDBACK_EXTRA.md") or "No additional recurring category has yet been recorded."]
    write_text(OUT / f"{PREFIX}_sheet_feedback.md", "\n\n".join(feedback))

    audits = [f"# {PREFIX}: second-reading record"]
    for r in records:
        if r["audit"]:
            audits += [f"## Scan {r['scan']:03d}", r["audit"]]
    write_text(OUT / f"{PREFIX}_audit.md", "\n\n".join(audits))
    return {"pages": len(records), "against_C": totals["C"], "against_H": totals["H"], "changed_places": totals["places"], "remaining_doubt_rows": len(remaining), "check_events": len(checks)}


def brace_balance(text):
    """Coarse lexical balance; comments and escaped braces are ignored."""
    depth = 0
    for line_no, line in enumerate(text.splitlines(), 1):
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == "\\":
                i += 2
                continue
            if ch == "%":
                break
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth < 0:
                    return False, f"unexpected closing brace on line {line_no}"
            i += 1
    return depth == 0, "balanced" if depth == 0 else f"net brace depth {depth}"


def validate(require_complete=False):
    records = load_records()
    errors, warnings = [], []
    scans = [r["scan"] for r in records]
    if require_complete and scans != sorted(FOLDERS):
        errors.append(f"Missing scans: {sorted(set(FOLDERS) - set(scans))}")
    expected_files = [f"{PREFIX}_{suffix}" for suffix in ("transcription.tex", "changes.md", "collation.tsv", "doubts.md", "inventory.csv", "notes.md", "sheet_feedback.md", "hand_log.md")] + ["CHECK_EVENTS.tsv", "progress.log"]
    for name in expected_files:
        if not (OUT / name).is_file():
            errors.append(f"Missing deliverable: {name}")
    schemas = [(OUT / f"{PREFIX}_collation.tsv", COLLATION_FIELDS, "\t"), (OUT / f"{PREFIX}_inventory.csv", INVENTORY_FIELDS, ","), (OUT / "CHECK_EVENTS.tsv", CHECK_FIELDS, "\t")]
    seen_ids = set()
    for r in records:
        scan = r["scan"]
        body = r["page"].read_text(encoding="utf-8")
        ok, detail = brace_balance(body)
        if not ok:
            errors.append(f"Scan {scan}: {detail}")
        if not re.search(r"\\scanpage\s*\{\s*" + str(scan) + r"\s*\}", body):
            errors.append(f"Scan {scan}: missing or incorrect scanpage marker")
        if not r["inventory"]:
            errors.append(f"Scan {scan}: empty inventory")
        for inv in r["inventory"]:
            if inv.get("transcribed", "").lower() != "yes":
                errors.append(f"Scan {scan}: inventory element {inv['element']} not transcribed=yes")
        for ch in r["changes"]:
            if ch["id"] in seen_ids:
                errors.append(f"Duplicate change ID: {ch['id']}")
            seen_ids.add(ch["id"])
            if ch["confidence"] not in {"high", "medium", "low"}:
                errors.append(f"{ch['id']}: invalid confidence {ch['confidence']!r}")
            if as_bool(ch["diff_H"]) and H_STATUS[scan] != "text":
                errors.append(f"{ch['id']}: H row where H has no text")
            if as_bool(ch["diff_H"]) and ch["kind"] not in KINDS:
                errors.append(f"{ch['id']}: invalid H collation kind {ch['kind']!r}")
            if not ch["scan_shows"].strip():
                warnings.append(f"{ch['id']}: no ink-evidence text")
        for event in r["checks"]:
            if event["type"] not in CHECK_TYPES and not event["type"].startswith("refuted"):
                warnings.append(f"{event['statement_id']}: nonstandard check-event type {event['type']!r}")
        if require_complete and not r["audit"]:
            warnings.append(f"Scan {scan}: no saved second-reading narrative")
        d = r["dir"]
        schemas += [(d / "changes.tsv", CHANGE_FIELDS, "\t"), (d / "inventory.csv", INVENTORY_FIELDS, ","), (d / "doubts.tsv", DOUBT_FIELDS, "\t"), (d / "hand.tsv", HAND_FIELDS, "\t"), (d / "notation.tsv", NOTATION_FIELDS, "\t"), (d / "abbreviations.tsv", ABBREVIATION_FIELDS, "\t"), (d / "checks.tsv", CHECK_FIELDS, "\t")]
    for path, expected, delimiter in schemas:
        if not path.exists():
            errors.append(f"Missing record: {path.relative_to(OUT)}")
            continue
        with path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            if reader.fieldnames != expected:
                errors.append(f"Incorrect schema: {path.relative_to(OUT)}")
            for n, row in enumerate(reader, 2):
                if None in row or any(v is None for v in row.values()):
                    errors.append(f"Malformed row {n}: {path.relative_to(OUT)}")
    combined = OUT / f"{PREFIX}_transcription.tex"
    if combined.exists():
        body = combined.read_text(encoding="utf-8")
        if len(re.findall(r"\\cotefile\s*\{71\}", body)) != 1:
            errors.append("Combined transcription must contain cotefile{71} exactly once")
        found = [int(n) for n in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", body)]
        if found != scans:
            errors.append(f"Combined scan markers {found} differ from saved page order {scans}")
        ok, detail = brace_balance(body)
        if not ok:
            errors.append(f"Combined transcription: {detail}")
    for p in OUT.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif", ".tiff", ".json"}:
            errors.append(f"Forbidden image/JSON in output tree: {p.relative_to(OUT)}")
    return {"pages": len(records), "errors": errors, "warnings": warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "validate"])
    parser.add_argument("--complete", action="store_true", help="Require all 25 pages")
    args = parser.parse_args()
    if args.command == "build":
        for key, value in build().items():
            print(f"{key}: {value}")
    else:
        result = validate(args.complete)
        print(f"pages: {result['pages']}")
        for key in ("errors", "warnings"):
            print(f"{key}: {len(result[key])}")
            for message in result[key]:
                print(f"  {message}")
        if result["errors"]:
            sys.exit(1)


if __name__ == "__main__":
    main()
