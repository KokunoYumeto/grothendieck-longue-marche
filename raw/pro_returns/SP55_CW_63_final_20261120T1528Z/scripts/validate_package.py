#!/usr/bin/env python3
"""Mechanical checks for SP55_CW_63; no OCR, image reading, or TeX compilation.

Usage: python validate_package.py DELIVERABLE_DIRECTORY [--zip FINAL_ZIP]
The JSON report is written to stdout only. Exit 0 means these structural checks
passed; it makes no claim about the accuracy or completeness of an ink reading.

Recommended progress hash record (other conventional hash orders also work):
    sha256 <64 hex characters> pages/H63-03_63_scan021.tex
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath


PREFIX = "SP55_CW_63"
SCANS = tuple(range(21, 35)) + tuple(range(41, 53))
H_TEXT = {21, 22, 27, 30, 32, 33, 34}


def folder(scan: int) -> str:
    if scan <= 24:
        return "H63-03"
    if scan <= 34:
        return "H63-04"
    if scan <= 48:
        return "H63-05"
    return "H63-06"


PAGES = [f"pages/{folder(s)}_63_scan{s:03d}.tex" for s in SCANS]
REQUIRED = [
    f"{PREFIX}_transcription.tex",
    f"{PREFIX}_changes.md",
    f"{PREFIX}_collation.tsv",
    f"{PREFIX}_doubts.md",
    f"{PREFIX}_inventory.csv",
    f"{PREFIX}_notes.md",
    "progress.log",
    f"{PREFIX}_sheet_feedback.md",
    f"{PREFIX}_hand_log.md",
    "CHECK_EVENTS.tsv",
] + PAGES
INVENTORY_COLUMNS = [
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
COLLATION_COLUMNS = [
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H",
    "confidence",
]
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover",
}
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state (struck given live or live given struck)", "insertion or placement",
    "abbreviation expanded or spelling modernised", r"readable ink left as \ill{}",
    "drawing or diagram", "other",
}
CONFIDENCES = {"high", "medium", "low"}
ERROR_SHEET_CATEGORIES = (
    "Symbols and indices",
    "Words",
    "Omissions",
    "Drawings and diagrams",
    "Readable ink left as illegible",
    "Insertions put in the wrong place",
    "Struck text",
    "Abbreviations expanded, spelling modernised",
    "Text that is not on the page",
    "Other",
)
REFUTED_CHECK_TYPES = {
    "refuted, with the refined statement’s id",
    "refuted, with the refined statement's id",
}
CHECK_TYPES = {
    "targeted proof check", "independent re-proof", "computation or formal certificate",
    "used and rechecked in this run", "carried as background without fault found",
} | REFUTED_CHECK_TYPES
IMAGE_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".bmp", ".webp", ".svg", ".avif",
}


def uncomment(text: str) -> str:
    """Remove TeX comments, preserving escaped percent signs."""
    out = []
    for line in text.splitlines():
        for i, char in enumerate(line):
            if char != "%":
                continue
            slashes = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                slashes += 1
                j -= 1
            if slashes % 2 == 0:
                line = line[:i]
                break
        out.append(line)
    return "\n".join(out)


def brace_issues(text: str) -> list[dict]:
    """Heuristic only: comments and escaped literal braces are ignored."""
    text = uncomment(text)
    stack = []
    issues = []
    line = 1
    for i, char in enumerate(text):
        if char == "\n":
            line += 1
        if char not in "{}":
            continue
        slashes = 0
        j = i - 1
        while j >= 0 and text[j] == "\\":
            slashes += 1
            j -= 1
        if slashes % 2:
            continue
        if char == "{":
            stack.append(line)
        elif stack:
            stack.pop()
        else:
            issues.append({"line": line, "problem": "unmatched closing brace"})
    issues.extend({"line": n, "problem": "unmatched opening brace"} for n in stack)
    return issues


def as_int(value):
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        return None


def label_key(value: str) -> str:
    """Normalize typography in Markdown labels, not enum values in data files."""
    value = re.sub(r"^\s*\d+[.)]\s*", "", value)
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def markdown_tables(text: str):
    """Read conventional pipe tables used by the editorial reporting script."""
    blocks = []
    block = []
    for line_number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in re.split(r"(?<!\\)\|", stripped[1:-1])]
            block.append((line_number, cells))
        elif block:
            blocks.append(block)
            block = []
    if block:
        blocks.append(block)
    for block in blocks:
        if len(block) < 2:
            continue
        if not all(re.fullmatch(r":?-+:?", cell.replace(" ", "")) for cell in block[1][1]):
            continue
        yield block[0][1], block[2:]


def markdown_sections(text: str):
    headings = list(re.finditer(r"(?m)^#{1,6}[ \t]+([^\n]+)\n?", text))
    for i, match in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        yield match.group(1).strip(), text[match.end():end].strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--zip", dest="zip_path", type=Path)
    args = parser.parse_args()
    root = args.directory.resolve()
    checks = []
    facts = {}

    def check(name, passed, detail=None):
        record = {"check": name, "passed": bool(passed)}
        if detail is not None:
            record["detail"] = detail
        checks.append(record)

    def load_text(relative):
        path = root / relative
        if not path.is_file():
            return None
        try:
            return path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            check(f"readable UTF-8: {relative}", False, str(exc))
            return None

    def load_table(relative, delimiter, columns=None):
        text = load_text(relative)
        if text is None:
            return [], []
        try:
            import io
            reader = csv.DictReader(io.StringIO(text), delimiter=delimiter)
            rows = list(reader)
            headers = reader.fieldnames or []
        except csv.Error as exc:
            check(f"parse table: {relative}", False, str(exc))
            return [], []
        if columns is not None:
            check(f"exact columns: {relative}", headers == columns, {"actual": headers})
        malformed = [i + 2 for i, row in enumerate(rows)
                     if None in row or any(value is None for value in row.values())]
        check(f"complete rows: {relative}", not malformed, malformed)
        return headers, rows

    missing = [name for name in REQUIRED if not (root / name).is_file()]
    empty = [name for name in REQUIRED if (root / name).is_file() and (root / name).stat().st_size == 0]
    check("all required files present", not missing, missing)
    check("all required files nonempty", not empty, empty)
    actual_pages = sorted(p.relative_to(root).as_posix() for p in (root / "pages").glob("*.tex"))
    check("exact 26 page filenames", actual_pages == sorted(PAGES), {
        "missing": sorted(set(PAGES) - set(actual_pages)),
        "extra": sorted(set(actual_pages) - set(PAGES)),
        "count": len(actual_pages),
    })
    page_texts = {name: load_text(name) for name in PAGES}
    for scan, name in zip(SCANS, PAGES):
        text = page_texts[name]
        if text is None:
            continue
        marks = [int(s) for s in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", uncomment(text))]
        check(f"page scan marker: {name}", marks == [scan], marks)
        cotemarks = re.findall(r"\\cotefile\s*\{\s*([^}]+?)\s*\}", uncomment(text))
        expected_cotes = ["63"] if scan == SCANS[0] else []
        check(f"page cote marker: {name}", cotemarks == expected_cotes,
              {"expected": expected_cotes, "actual": cotemarks})

    combined_name = f"{PREFIX}_transcription.tex"
    combined = load_text(combined_name)
    if combined is not None:
        marks = [int(s) for s in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", uncomment(combined))]
        check("combined page order", marks == list(SCANS), marks)
        cotemarks = re.findall(r"\\cotefile\s*\{\s*([^}]+?)\s*\}", uncomment(combined))
        check("combined has exactly one cote marker", cotemarks == ["63"], cotemarks)
        forbidden = re.findall(r"\\(?:documentclass|usepackage)\b|\\(?:begin|end)\s*\{document\}", uncomment(combined))
        check("combined is a fragment without preamble", not forbidden, forbidden)
        if all(text is not None for text in page_texts.values()):
            position = 0
            errors = []
            gaps = []
            for name in PAGES:
                text = page_texts[name].strip()
                found = combined.find(text, position)
                if found < 0:
                    errors.append(name)
                else:
                    gaps.append(combined[position:found])
                    position = found + len(text)
            gaps.append(combined[position:])
            substantive_gaps = [g for g in gaps if uncomment(g).strip()]
            check("combined includes each page verbatim in order", not errors, errors)
            check("combined has no added substantive text", not substantive_gaps,
                  {"unmatched_gap_count": len(substantive_gaps)})
    for name, text in [*page_texts.items(), (combined_name, combined)]:
        if text is not None:
            issues = brace_issues(text)
            check(f"brace balance heuristic: {name}", not issues, issues)

    _, inventory = load_table(f"{PREFIX}_inventory.csv", ",", INVENTORY_COLUMNS)
    inv_scans = {as_int(row.get("scan")) for row in inventory}
    check("inventory covers exactly the 26 scans", inv_scans == set(SCANS), {
        "missing": sorted(set(SCANS) - inv_scans),
        "unexpected": sorted(str(s) for s in inv_scans - set(SCANS)),
    })
    check("inventory transcribed=yes for every row", bool(inventory) and all(row.get("transcribed") == "yes" for row in inventory))
    check("inventory element kinds", all(row.get("kind") in ELEMENT_KINDS for row in inventory),
          sorted({str(row.get("kind")) for row in inventory if row.get("kind") not in ELEMENT_KINDS}))
    check("inventory sheet kinds", all(row.get("sheet_kind") in SHEET_KINDS for row in inventory),
          sorted({str(row.get("sheet_kind")) for row in inventory if row.get("sheet_kind") not in SHEET_KINDS}))
    facts["inventory_rows"] = len(inventory)
    facts["inventory_rows_by_scan"] = {str(s): sum(as_int(r.get("scan")) == s for r in inventory) for s in SCANS}

    _, collation = load_table(f"{PREFIX}_collation.tsv", "\t", COLLATION_COLUMNS)
    no_h = [i + 2 for i, row in enumerate(collation) if as_int(row.get("our_scan")) not in H_TEXT]
    check("collation only includes pages with H text", not no_h, no_h)
    mapping_errors = []
    for i, row in enumerate(collation):
        scan = as_int(row.get("our_scan"))
        if scan not in SCANS or row.get("folder") != folder(scan) or as_int(row.get("their_page")) != scan - 1:
            mapping_errors.append(i + 2)
    check("collation page mapping", not mapping_errors, mapping_errors)
    check("collation kinds", all(row.get("kind") in COLLATION_KINDS for row in collation),
          sorted({str(row.get("kind")) for row in collation if row.get("kind") not in COLLATION_KINDS}))
    check("collation confidences", all(row.get("confidence") in CONFIDENCES for row in collation),
          sorted({str(row.get("confidence")) for row in collation if row.get("confidence") not in CONFIDENCES}))
    facts["collation_rows"] = len(collation)

    # Heading and table checks are mechanical conventions, not a judgement of
    # whether the prose actually provides the requested assessment.
    doubts = load_text(f"{PREFIX}_doubts.md")
    if doubts is not None:
        sections = list(markdown_sections(doubts))
        abbreviation_sections = [(heading, body) for heading, body in sections if "abbrevi" in heading.casefold()]
        legibility_sections = [(heading, body) for heading, body in sections
                               if "legib" in heading.casefold() or "readability" in heading.casefold()]
        check("doubts includes a nonempty abbreviations section", any(body for _, body in abbreviation_sections),
              {"matching_headings": [heading for heading, _ in abbreviation_sections]})
        check("doubts includes a nonempty legibility section", any(body for _, body in legibility_sections),
              {"matching_headings": [heading for heading, _ in legibility_sections]})
    for relative, content in ((f"{PREFIX}_doubts.md", doubts),
                              (f"{PREFIX}_changes.md", load_text(f"{PREFIX}_changes.md"))):
        if content is None:
            continue
        invalid = []
        confidence_tables = 0
        for headers, table_rows in markdown_tables(content):
            indexes = [i for i, header in enumerate(headers) if label_key(header) == "confidence"]
            if not indexes:
                continue
            confidence_tables += 1
            for line_number, cells in table_rows:
                for index in indexes:
                    confidence = cells[index].strip("`* ") if index < len(cells) else None
                    if confidence not in CONFIDENCES:
                        invalid.append({"line": line_number, "value": confidence})
        check(f"Markdown confidence enums: {relative}", not invalid, invalid)
        if relative.endswith("_doubts.md"):
            check("remaining-doubts confidence table present", confidence_tables > 0)

    feedback = load_text(f"{PREFIX}_sheet_feedback.md")
    if feedback is not None:
        keys = {label_key(category): category for category in ERROR_SHEET_CATEGORIES}
        # These two harmless title variants retain the same error-sheet category.
        keys["insertions put in wrong place"] = "Insertions put in the wrong place"
        keys["text not on the page"] = "Text that is not on the page"
        observed = {}
        malformed_counts = []
        duplicates = []
        for headers, table_rows in markdown_tables(feedback):
            count_columns = [i for i, header in enumerate(headers)
                             if label_key(header) in {"places", "count", "total", "number of places"}]
            count_index = count_columns[0] if count_columns else 1
            for line_number, cells in table_rows:
                if not cells:
                    continue
                canonical = keys.get(label_key(cells[0]))
                if canonical is None:
                    continue
                value = cells[count_index].strip("`* ") if count_index < len(cells) else ""
                if not re.fullmatch(r"\d+", value):
                    malformed_counts.append({"line": line_number, "category": canonical, "value": value})
                if canonical in observed:
                    duplicates.append(canonical)
                observed[canonical] = int(value) if re.fullmatch(r"\d+", value) else None
        check("feedback lists all ten error-sheet categories", set(observed) == set(ERROR_SHEET_CATEGORIES),
              {"missing": [name for name in ERROR_SHEET_CATEGORIES if name not in observed]})
        check("feedback counts are nonnegative integers", not malformed_counts, malformed_counts)
        check("feedback categories have one count each", not duplicates, duplicates)
        facts["error_sheet_counts"] = observed

    event_headers, events = load_table("CHECK_EVENTS.tsv", "\t")
    norm = {re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_"): name for name in event_headers}
    # The prompt names concepts rather than prescribing exact header spelling.
    required_events = {"statement_id", "date", "type", "outcome"}
    who_ok = "who" in norm or {"model", "effort", "run"} <= set(norm)
    check("check-events required concepts", required_events <= set(norm) and who_ok, event_headers)
    if "type" in norm:
        unexpected_types = sorted({str(row.get(norm["type"])) for row in events
                                   if row.get(norm["type"]) not in CHECK_TYPES})
        check("check-events type vocabulary", not unexpected_types, unexpected_types)
    facts["check_event_rows"] = len(events)

    progress = load_text("progress.log")
    if progress is not None:
        first_line = progress.splitlines()[0] if progress.splitlines() else ""
        check("progress first line carries UTC start", bool(re.search(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}.*(?:UTC|Z|\+00:00)", first_line)), first_line)
        for phase in ("done", "audited"):
            entries = re.findall(rf"(?m)^scan\s+(\d+)\s+{phase}\s+(.+)$", progress)
            seen = {int(scan) for scan, _ in entries}
            check(f"progress {phase} for every scan", set(SCANS) <= seen,
                  {"missing": sorted(set(SCANS) - seen), "entry_count": len(entries)})
            malformed_times = [scan for scan, stamp in entries if not re.search(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}.*(?:UTC|Z|\+00:00)", stamp)]
            check(f"progress {phase} timestamps", not malformed_times, malformed_times)
        check("transcription frozen marker", bool(re.search(r"(?m)^transcription frozen\s+", progress)))
        hashes = {}
        for line in progress.splitlines():
            match = re.search(r"\b([0-9a-fA-F]{64})\b", line)
            if not match:
                continue
            for name in PAGES + [combined_name]:
                if name in line or Path(name).name in line:
                    hashes.setdefault(name, set()).add(match.group(1).lower())
        needed_hashes = PAGES + [combined_name]
        check("frozen hashes cover all pages and combined", all(name in hashes for name in needed_hashes),
              [name for name in needed_hashes if name not in hashes])
        mismatches = []
        for name in needed_hashes:
            path = root / name
            if name in hashes and path.is_file():
                current = hashlib.sha256(path.read_bytes()).hexdigest()
                if hashes[name] != {current}:
                    mismatches.append({"file": name, "recorded": sorted(hashes[name]), "current": current})
        check("all recorded frozen hashes equal current bytes", not mismatches, mismatches)
        check("end verification states hashes unchanged", bool(re.search(r"(?:hashes.*unchanged|unchanged.*hashes)", progress, re.I)))

    def forbidden_member(name):
        parts = PurePosixPath(name).parts
        suffix = PurePosixPath(name).suffix.lower()
        if suffix in IMAGE_SUFFIXES:
            return "image"
        if suffix == ".pdf":
            return "PDF (not a requested deliverable)"
        if any(part.lower() in {"input", "upload", "codex", "hua"} or "_scans" in part.lower() or "_witnesses" in part.lower() for part in parts):
            return "input scan/witness tree"
        if re.search(r"checkpoint.*\.zip$", name, re.I):
            return "nested checkpoint ZIP"
        if suffix == ".zip":
            return "nested ZIP"
        return None

    exclusions = [{"file": p.relative_to(root).as_posix(), "reason": reason}
                  for p in root.rglob("*") if p.is_file()
                  if (reason := forbidden_member(p.relative_to(root).as_posix()))]
    check("deliverable directory excludes scans, witnesses, images and nested ZIPs", not exclusions, exclusions)
    if args.zip_path:
        try:
            with zipfile.ZipFile(args.zip_path) as archive:
                names = archive.namelist()
                unsafe = [name for name in names if name.startswith("/") or ".." in PurePosixPath(name).parts]
                excluded = [{"file": name, "reason": reason} for name in names
                            if (reason := forbidden_member(name))]
                check("ZIP paths are safe", not unsafe, unsafe)
                check("ZIP excludes images, witnesses and nested ZIPs", not excluded, excluded)
                check("ZIP CRC integrity", archive.testzip() is None)
                # Accept either a flat archive or a single containing directory.
                files = [name for name in names if not name.endswith("/")]
                prefixes = [""] + sorted({name.split("/", 1)[0] + "/" for name in files if "/" in name})
                prefix = next((p for p in prefixes if all(p + name in names for name in REQUIRED)), None)
                check("ZIP contains all required deliverables", prefix is not None)
                if prefix is not None:
                    mismatch = [name for name in REQUIRED
                                if (root / name).is_file() and archive.read(prefix + name) != (root / name).read_bytes()]
                    check("ZIP deliverables match current directory bytes", not mismatch, mismatch)
                facts["zip_file_count"] = len(files)
        except (OSError, zipfile.BadZipFile) as exc:
            check("ZIP readable", False, str(exc))

    failed = [entry for entry in checks if not entry["passed"]]
    report = {
        "directory": str(root),
        "scope": "Mechanical structure only; not an assessment of transcription or image reading accuracy.",
        "passed": not failed,
        "check_count": len(checks),
        "failed_count": len(failed),
        "facts": facts,
        "checks": checks,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
