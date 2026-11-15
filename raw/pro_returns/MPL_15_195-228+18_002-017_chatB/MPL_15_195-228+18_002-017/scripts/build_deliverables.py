#!/usr/bin/env python3
"""Assemble saved page files and a doubts table, with optional reader review.

Only the responsible reader should execute this against the package. This
script reads saved LaTeX pages, records/expected_pages.json, and
records/notation.md. It never opens source scans, archives, or context files;
never edits a page file; and never edits progress.log. It makes no assessment
of manuscript accuracy, completeness, or legibility.

By default, assemble all page files currently present in the prescribed order.
Use --require-complete to require all 49 page files before writing outputs.
Use --doubt-review-file to apply a complete, exactly matched reader review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

from validate_package import EXPECTED, PREFIX, mask_tex, page_name


DEFAULT_LEGIBILITY_NOTE = """This note is provisional and must be replaced by the responsible reader's
assessment after visual review. The assembler has made no assessment of the
manuscript's legibility, the reliability of particular passages, or the accuracy
of any reading. The confidence labels in the extracted table are mechanical
defaults: `medium` for a single reading in `\\unsure`, and `low` for explicit
alternatives or `\\illegible`. They remain subject to the reader's review.
"""

REVIEWED_LEGIBILITY_NOTE = """The table records the reader's reviewed confidence labels and source locations.
The assembler has made no assessment of manuscript legibility and has not altered
the readings in the page fragments.
"""


def paragraph_number(text: str, offset: int) -> int:
    """Count nonempty TeX-source blocks separated by blank source lines.

    Page markers, comments, and display code participate in this count. This
    count intentionally makes no assertion about manuscript paragraphing.
    """
    if offset < 0 or offset > len(text):
        raise ValueError("Offset outside the source text")
    paragraph = 0
    inside = False
    position = 0
    for line in text.splitlines(keepends=True):
        if line.strip():
            if not inside:
                paragraph += 1
            inside = True
        else:
            inside = False
        if position <= offset < position + len(line):
            return paragraph
        position += len(line)
    return paragraph


def split_alternatives(raw: str, masked: str) -> list[str]:
    """Split unescaped top-level pipe characters, retaining nested braces.

    Escaped pipes and pipes within a braced subexpression remain in their
    original reading. The source convention supplies the meaning of the
    top-level delimiter; no mathematical interpretation is attempted.
    """
    if len(raw) != len(masked):
        raise ValueError("Mask and source offsets differ")
    level = 0
    begin = 0
    parts = []
    for index, char in enumerate(masked):
        if char == "{":
            level += 1
        elif char == "}":
            level -= 1
        elif char == "|" and level == 0:
            parts.append(raw[begin:index].strip())
            begin = index + 1
    parts.append(raw[begin:].strip())
    return parts


def extract_doubts(text: str) -> list[dict]:
    """Extract every balanced doubt macro, including nested occurrences."""
    masked = mask_tex(text)
    rows = []
    for found in re.finditer(r"\\(?P<macro>unsure|illegible)\s*\{", masked):
        begin = found.end()
        end = begin
        level = 1
        while end < len(masked):
            char = masked[end]
            if char == "{":
                level += 1
            elif char == "}":
                level -= 1
                if level == 0:
                    break
            end += 1
        line = text.count("\n", 0, found.start()) + 1
        if level:
            raise ValueError(f"Unclosed \\{found.group('macro')} argument at TeX line {line}")
        macro = found.group("macro")
        raw = text[begin:end]
        parts = split_alternatives(raw, masked[begin:end]) if macro == "unsure" else [raw]
        reading = parts[0] if macro == "unsure" else "\\illegible{" + raw + "}"
        rows.append({
            "macro": macro,
            "tex_line": line,
            "tex_paragraph": paragraph_number(text, found.start()),
            "offset": found.start(),
            "argument": raw,
            "reading": reading,
            "alternatives": parts[1:],
            "confidence": "low" if macro == "illegible" or len(parts) > 1 else "medium",
        })
    return rows


def apply_doubt_review(rows: list[dict], review_path: Path) -> tuple[list[dict], dict]:
    """Require a complete one-to-one reader review before any output write.

    Offsets are the zero-based character offsets returned by extract_doubts.
    No reading, alternative, source page, or manuscript interpretation changes.
    """
    review_path = review_path.resolve()
    review_bytes = review_path.read_bytes()
    review = json.loads(review_bytes.decode("utf-8"))
    if not isinstance(review, dict):
        raise ValueError("Doubt review must be a JSON object")
    for field in ("reviewed_by", "reviewed_utc"):
        if not isinstance(review.get(field), str) or not review[field].strip():
            raise ValueError(f"Doubt review requires a nonempty string {field}")
    if not isinstance(review.get("rows"), list):
        raise ValueError("Doubt review requires a rows array")
    expected = {}
    for row in rows:
        position = (row["cote"], row["scan"], row["offset"])
        if position in expected:
            raise ValueError(f"Duplicate extracted doubt position: {position}")
        expected[position] = row
    supplied = {}
    for index, record in enumerate(review["rows"]):
        if not isinstance(record, dict):
            raise ValueError(f"Doubt review rows[{index}] must be an object")
        for field in ("cote", "scan", "offset"):
            if type(record.get(field)) is not int:
                raise ValueError(f"Doubt review rows[{index}].{field} must be an integer")
        if record["offset"] < 0:
            raise ValueError(f"Doubt review rows[{index}].offset must be nonnegative")
        if not isinstance(record.get("argument"), str):
            raise ValueError(f"Doubt review rows[{index}].argument must be a string")
        if record.get("confidence") not in ("low", "medium", "high"):
            raise ValueError(f"Doubt review rows[{index}].confidence must be low, medium, or high")
        if not isinstance(record.get("source_location"), str) or not record["source_location"].strip():
            raise ValueError(f"Doubt review rows[{index}].source_location must be a nonempty string")
        position = (record["cote"], record["scan"], record["offset"])
        if position in supplied:
            raise ValueError(f"Duplicate doubt review position: {position}")
        supplied[position] = record
    missing = [position for position in expected if position not in supplied]
    extra = [position for position in supplied if position not in expected]
    if missing or extra:
        raise ValueError(
            "Doubt review coverage mismatch: "
            f"{len(missing)} extracted doubt(s) have no review; "
            f"{len(extra)} review row(s) have no extracted doubt. "
            f"First missing positions: {missing[:10]}; first extra positions: {extra[:10]}"
        )
    reviewed_rows = []
    for row in rows:
        position = (row["cote"], row["scan"], row["offset"])
        record = supplied[position]
        if record["argument"] != row["argument"]:
            raise ValueError(f"Doubt review exact argument mismatch at cote, scan, offset {position}")
        reviewed_rows.append({**row, "confidence": record["confidence"],
                              "source_location": record["source_location"]})
    provenance = {
        "file": str(review_path),
        "sha256": hashlib.sha256(review_bytes).hexdigest(),
        "reviewed_by": review["reviewed_by"],
        "reviewed_utc": review["reviewed_utc"],
        "reviewed_row_count": len(reviewed_rows),
        "coverage": "complete one-to-one match",
        "matched_fields": ["cote", "scan", "offset", "argument"],
        "offset_convention": "Zero-based character offset in the UTF-8-decoded page fragment.",
    }
    return reviewed_rows, provenance


def inline_code(value: str) -> str:
    """Render literal readings without letting a pipe split a table cell.

    Use ordinary code spans when possible. A reading containing a pipe uses
    encoded inline HTML code, avoiding ambiguous Markdown backslash counting.
    """
    value = value.replace("\r\n", "\n").replace("\r", "\n").replace("\n", " ")
    if "|" in value:
        encoded = "".join(char if char.isalnum() or char == " " else f"&#{ord(char)};" for char in value)
        return "<code>" + encoded + "</code>"
    runs = re.findall(r"`+", value)
    delimiter = "`" * (max((len(run) for run in runs), default=0) + 1)
    # Code spans collapse source newlines. Render their locations explicitly
    # as a literal space; the original source remains in the page fragment.
    if value.startswith("`") or value.endswith("`"):
        value = " " + value + " "
    return delimiter + value + delimiter


def table_cell(value: str) -> str:
    """Escape pipes even within code spans, as required by Markdown tables."""
    return value.replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def render_doubts(notation: str, rows: list[dict], legibility_note: str,
                  review_provenance: dict | None = None) -> str:
    top = notation + ("" if notation.endswith("\n") else "\n")
    content = [top, "\n## Reading doubts\n\n"]
    if review_provenance is not None:
        content.append(
            "Source locations and confidence labels follow the reader's recorded review. "
            "Each location also includes the corresponding physical TeX source line. "
            "Every explicit doubt macro has been matched to exactly one review entry by "
            "cote, scan, character offset, and exact argument.\n\n"
        )
        location_header = "Source location and TeX line"
    else:
        content.append(
            "Locations below refer explicitly to the saved **TeX source**: paragraphs are "
            "nonempty source blocks separated by blank lines, and lines are physical source "
            "lines. These are approximate locators, not manuscript line or paragraph numbers. "
            "Each row comes from an explicit doubt macro; the table does not establish that "
            "all uncertain manuscript readings have been marked.\n\n"
            "Confidence labels are provisional mechanical defaults pending the responsible "
            "reader's review. A single `\\unsure` reading receives `medium`; explicit "
            "alternatives and `\\illegible` receive `low`.\n\n"
        )
        location_header = "Approximate location in TeX source"
    headers = ["File", "Cote", "Scan", location_header, "Macro",
               "Reading", "Alternatives", "Confidence"]
    content.append("| " + " | ".join(headers) + " |\n")
    content.append("| " + " | ".join(["---"] * len(headers)) + " |\n")
    for row in rows:
        alternatives = "; ".join(inline_code(part) for part in row["alternatives"]) or "—"
        location = (f"{row['source_location']}; TeX line {row['tex_line']}"
                    if review_provenance is not None
                    else f"TeX paragraph {row['tex_paragraph']}; TeX line {row['tex_line']}")
        values = [
            inline_code(row["file"]), str(row["cote"]), str(row["scan"]),
            location,
            inline_code("\\" + row["macro"]), inline_code(row["reading"]),
            alternatives, row["confidence"],
        ]
        content.append("| " + " | ".join(table_cell(value) for value in values) + " |\n")
    if not rows:
        content.append("\nNo doubt macros were found in the currently saved page files.\n")
    if review_provenance is not None:
        content.append("\n## Legibility note\n\n")
    else:
        content.append("\n## Legibility note (provisional)\n\n")
        content.append("<!-- Replace this provisional note after the responsible reader's visual review. -->\n")
    content.append(legibility_note.rstrip() + "\n")
    return "".join(content)


def atomic_write(path: Path, data: bytes) -> None:
    """Replace an output only after its complete bytes have been written."""
    descriptor, temporary_name = tempfile.mkstemp(prefix="." + path.name + ".", suffix=".tmp", dir=path.parent)
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def assemble(root: Path, require_complete: bool, legibility_note: str,
             doubt_review_file: Path | None = None) -> dict:
    root = root.resolve()
    manifest_path = root / "records" / "expected_pages.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected = [(int(item["cote"]), int(item["scan"])) for item in manifest]
    if expected != EXPECTED:
        raise ValueError("records/expected_pages.json differs from the prescribed 49-page order")
    notation = (root / "records" / "notation.md").read_text(encoding="utf-8")
    if not notation.strip():
        raise ValueError("records/notation.md is empty")
    page_bytes = []
    rows = []
    present = []
    missing = []
    for cote, scan in expected:
        relative = "pages/" + page_name(cote, scan)
        path = root / relative
        if not path.is_file():
            missing.append({"cote": cote, "scan": scan, "file": relative})
            continue
        data = path.read_bytes()
        text = data.decode("utf-8")
        extracted = extract_doubts(text)
        for row in extracted:
            row.update({"cote": cote, "scan": scan, "file": relative})
        rows.extend(extracted)
        page_bytes.append(data)
        present.append({"cote": cote, "scan": scan, "file": relative,
                        "bytes": len(data), "doubt_count": len(extracted)})
    if require_complete and missing:
        raise ValueError(f"Cannot assemble final deliverables: {len(missing)} page files are missing")
    if not present:
        raise ValueError("No saved page files found; no output files were changed")
    review_provenance = None
    if doubt_review_file is not None:
        rows, review_provenance = apply_doubt_review(rows, doubt_review_file)
        if legibility_note == DEFAULT_LEGIBILITY_NOTE:
            legibility_note = REVIEWED_LEGIBILITY_NOTE
    combined = b"".join(page_bytes)
    doubts = render_doubts(notation, rows, legibility_note, review_provenance).encode("utf-8")
    combined_path = root / f"{PREFIX}_transcription.tex"
    doubts_path = root / f"{PREFIX}_doubts.md"
    atomic_write(combined_path, combined)
    atomic_write(doubts_path, doubts)
    report = {
        "package": PREFIX,
        "root": str(root),
        "scope": "Mechanical assembly and macro extraction; no assessment of manuscript accuracy or legibility.",
        "present_page_count": len(present),
        "expected_page_count": len(expected),
        "missing_pages": missing,
        "pages": present,
        "doubt_rows": len(rows),
        "doubt_macro_counts": dict(Counter(row["macro"] for row in rows)),
        "outputs": [
            {"file": str(combined_path), "bytes": len(combined),
             "sha256": hashlib.sha256(combined).hexdigest()},
            {"file": str(doubts_path), "bytes": len(doubts),
             "sha256": hashlib.sha256(doubts).hexdigest()},
        ],
        "page_files_modified": False,
        "progress_log_modified": False,
    }
    confidence_key = "reviewed_confidence_counts" if review_provenance is not None else "provisional_confidence_counts"
    report[confidence_key] = dict(Counter(row["confidence"] for row in rows))
    if review_provenance is not None:
        report["doubt_review"] = review_provenance
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="Package directory (default: this script's parent package).")
    parser.add_argument("--require-complete", action="store_true",
                        help="Require all 49 page files before writing either assembled output.")
    parser.add_argument("--legibility-note-file", type=Path,
                        help="Optional reader-written UTF-8 text to replace the provisional legibility note.")
    parser.add_argument("--doubt-review-file", type=Path,
                        help="JSON reader review with complete one-to-one coverage by cote, scan, offset, and exact argument.")
    parser.add_argument("--compact", action="store_true", help="Emit JSON without indentation.")
    args = parser.parse_args()
    try:
        note = (args.legibility_note_file.read_text(encoding="utf-8")
                if args.legibility_note_file else DEFAULT_LEGIBILITY_NOTE)
        report = assemble(args.root, args.require_complete, note, args.doubt_review_file)
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        json.dump({"error": str(exc), "outputs_may_be_partial": isinstance(exc, OSError)},
                  sys.stderr, ensure_ascii=False, indent=2)
        sys.stderr.write("\n")
        return 1
    json.dump(report, sys.stdout, ensure_ascii=False, indent=None if args.compact else 2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
