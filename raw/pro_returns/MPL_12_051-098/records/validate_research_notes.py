#!/usr/bin/env python3
"""Read-only structural validation of the completed research notes.

The only output is a JSON report in this script's records directory.  This
validator never edits the notes, manuscript fragments, doubts, or inventory.
Sentence counts and reason cues are mechanical aids, not semantic proof checks.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys


RECORDS = Path(__file__).resolve().parent
DEFAULT_NOTES = RECORDS.parent / "MPL_12_051-098_notes.md"
EXPECTED = {"Q": 11, "N": 64, "B": 4, "SF": 32, "W": 9, "C": 5, "T": 9, "RQ": 24}
FIELDS = ("Kind", "Witness", "Context search", "Context", "RS")
ITEM_RE = re.compile(r"^(?:### |\| )((?:RQ|SF|Q|N|B|W|C|T)\d{2,3})\b")
PRINCIPAL_RE = re.compile(r"^### ((?:Q\d{2}|N\d{3}))\b")
FIELD_RE = re.compile(r"\*\*(Kind|Witness|Context search|Context|RS):\*\*\s*")
BIB_KEY = r"[A-Z][A-Z0-9]*(?:[-/][A-Z0-9]+)*"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def table_cells(line: str) -> list[str]:
    """Split on every unescaped pipe, as a Markdown table parser does.

    LaTeX delimiters do not protect raw pipes from table parsing.  Counting
    backslashes also avoids accepting an even number as an escaping prefix.
    """
    cells, current = [], []
    backslashes = 0
    for char in line.strip():
        if char == "|" and backslashes % 2 == 0:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        backslashes = backslashes + 1 if char == "\\" else 0
    cells.append("".join(current).strip())
    if cells and cells[0] == "":
        cells.pop(0)
    if cells and cells[-1] == "":
        cells.pop()
    return cells


def remove_math(text: str) -> str:
    def display(match: re.Match[str]) -> str:
        inner = match.group(0)[2:-2].rstrip()
        punctuation = inner[-1] if inner and inner[-1] in ".!?" else ""
        return " MATHEXPR" + punctuation + " "

    text = re.sub(r"\\\[.*?\\\]", display, text, flags=re.S)
    text = re.sub(r"\\\(.*?\\\)", " MATHEXPR ", text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", " MATHEXPR ", text, flags=re.S)
    return text


def body_only(block: list[str]) -> str:
    """Exclude heading, metadata paragraphs, table cells, and code blocks."""
    kept = []
    metadata_paragraph = False
    in_fence = False
    for line in block:
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if FIELD_RE.search(line):
            metadata_paragraph = True
            continue
        if not stripped:
            metadata_paragraph = False
            kept.append("")
            continue
        if metadata_paragraph or stripped.startswith(("|", "#")):
            continue
        kept.append(line)
    return "\n".join(kept).strip()


def sentence_segments(body: str) -> list[str]:
    """Heuristic prose count; report outliers for human review, not failure."""
    text = remove_math(body)
    text = re.sub(r"\[([^]\n]+)\]\([^\n)]*\)", r"\1", text)
    text = re.sub(r"\[[^]\n]*\]", " CITATION ", text)
    text = re.sub(r"https?://\S+", " URL ", text)
    text = text.replace("**", "").replace("`", "")
    for abbreviation in ("e.g.", "i.e.", "etc.", "cf.", "pp.", "p.", "no.", "nos.", "vs."):
        text = re.sub(re.escape(abbreviation), abbreviation.replace(".", "∯"), text, flags=re.I)
    text = re.sub(r"(?<=\d)\.(?=\d)", "∯", text)
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    # Pull closing punctuation into the preceding sentence without letting it
    # hide a boundary; abbreviations and decimal points were protected above.
    pieces = re.split(r"(?<=[.!?])(?:[\"”’')\]]*)\s+", text)
    return [piece.replace("∯", ".").strip() for piece in pieces if piece.strip()]


def bibliography_checks(lines: list[str]) -> dict:
    definitions = []
    definition_lines = set()
    definition_re = re.compile(r"^\|\s*\*\*\[(" + BIB_KEY + r")\]\*\*\s*\|")
    for number, line in enumerate(lines, 1):
        match = definition_re.match(line)
        if match:
            definitions.append({"key": match.group(1), "line": number})
            definition_lines.add(number)
    known = {entry["key"] for entry in definitions}
    uses = []
    for number, original_line in enumerate(lines, 1):
        if number in definition_lines:
            continue
        line = remove_math(original_line)
        for bracket in re.finditer(r"(?<!\\)\[([^]\n]+)\](?!\s*\()", line):
            for clause in bracket.group(1).split(";"):
                match = re.match(r"\s*(" + BIB_KEY + r")(?=\s*(?:,|$))", clause)
                if match:
                    uses.append({"key": match.group(1), "line": number, "citation": bracket.group(0)})
    used = {entry["key"] for entry in uses}
    counts = Counter(entry["key"] for entry in definitions)
    return {
        "definitions": definitions,
        "definition_count": len(definitions),
        "uses": uses,
        "undefined_keys": sorted(used - known),
        "duplicate_definitions": sorted(key for key, count in counts.items() if count > 1),
        "uncited_defined_keys": sorted(known - used),
        "scope": "Checks bracketed reference keys, not bibliographic accuracy or whether a source proves a claim.",
    }


def validate(notes_path: Path) -> dict:
    before = notes_path.read_bytes()
    text = before.decode("utf-8")
    lines = text.splitlines()
    errors, warnings = [], []
    defined = []
    for number, line in enumerate(lines, 1):
        match = ITEM_RE.match(line)
        if match:
            defined.append({"id": match.group(1), "line": number})
    actual_ids = [entry["id"] for entry in defined]
    expected_ids = {
        f"{family}{number:0{3 if family == 'N' else 2}d}"
        for family, count in EXPECTED.items()
        for number in range(1, count + 1)
    }
    family_counts = Counter(re.match(r"[A-Z]+", ident).group(0) for ident in actual_ids)
    duplicates = [ident for ident, count in Counter(actual_ids).items() if count > 1]
    missing = sorted(expected_ids - set(actual_ids))
    unexpected = sorted(set(actual_ids) - expected_ids)
    if len(actual_ids) != 158 or dict(family_counts) != EXPECTED or duplicates or missing or unexpected:
        errors.append({"check": "item_families", "message": "Expected exactly the 158 specified unique items.", "missing": missing, "unexpected": unexpected, "duplicates": duplicates})

    principals = []
    for index, line in enumerate(lines):
        match = PRINCIPAL_RE.match(line)
        if not match:
            continue
        end = index + 1
        while end < len(lines) and not re.match(r"^#{1,3}\s", lines[end]):
            end += 1
        block = lines[index + 1:end]
        joined = "\n".join(block)
        fields = {}
        metadata_parts = FIELD_RE.split(joined)
        for offset in range(1, len(metadata_parts), 2):
            name = metadata_parts[offset]
            value = metadata_parts[offset + 1].split("\n\n", 1)[0].strip()
            fields.setdefault(name, []).append(value)
        missing_fields = [field for field in FIELDS if field not in fields or not all(fields[field])]
        duplicate_fields = [field for field, values in fields.items() if len(values) != 1]
        if missing_fields or duplicate_fields:
            errors.append({"check": "principal_metadata", "item": match.group(1), "missing_or_empty": missing_fields, "duplicates": duplicate_fields})
        body = body_only(block)
        sentences = sentence_segments(body)
        own_idea = any("own idea" in kind.lower() for kind in fields.get("Kind", []))
        confidence = re.search(r"\bConfidence\s*:\s*([^\n*]+)", body, re.I) if own_idea else None
        # Reasons can precede the confidence sentence: e.g. an explicit exact
        # sequence, two matrices, or an incidence-complex calculation.
        reason_patterns = (
            r"\bbecause\b", r"\bsince\b", r"\bby (?:the |direct |these |explicit )",
            r"\bfrom (?:the |these |an? |their |its |his |her |two |explicit )",
            r"\bfollows? from\b", r"\blong exact sequence\b", r"\bcalculation\b",
        )
        reason_evidence = []
        if own_idea:
            for pattern in reason_patterns:
                for found in re.finditer(pattern, body, re.I):
                    reason_evidence.append(body[max(0, found.start() - 30):min(len(body), found.end() + 130)].replace("\n", " "))
            if not confidence:
                errors.append({"check": "own_idea_confidence", "item": match.group(1), "message": "No explicit Confidence: qualification in the note body."})
            if not reason_evidence:
                warnings.append({"check": "own_idea_reason", "item": match.group(1), "message": "No recognizable explanatory cue; manually check the stated reason."})
        if not 1 <= len(sentences) <= 4:
            warnings.append({"check": "body_sentence_count", "item": match.group(1), "count": len(sentences), "message": "Heuristic count outside 1–4; inspect body and segmentation manually."})
        principals.append({
            "id": match.group(1), "line_start": index + 1, "line_end": end,
            "metadata_complete": not missing_fields and not duplicate_fields,
            "metadata": {field: values[0] for field, values in fields.items()},
            "own_idea": own_idea,
            "confidence": confidence.group(1).strip() if confidence else None,
            "reason_cue_examples": list(dict.fromkeys(reason_evidence))[:3],
            "body_sentence_count_heuristic": len(sentences),
            "body_sentence_count_within_1_to_4": 1 <= len(sentences) <= 4,
            "body_sentence_segments_for_manual_review": sentences,
        })
    if len(principals) != 75:
        errors.append({"check": "principal_count", "actual": len(principals), "expected": 75})

    tables = []
    index = 0
    while index < len(lines):
        if not lines[index].lstrip().startswith("|"):
            index += 1
            continue
        start = index
        rows = []
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            rows.append({"line": index + 1, "cells": table_cells(lines[index])})
            index += 1
        width = len(rows[0]["cells"])
        mismatches = [{"line": row["line"], "actual": len(row["cells"]), "expected": width} for row in rows if len(row["cells"]) != width]
        delimiter_ok = len(rows) > 1 and all(re.fullmatch(r":?-{3,}:?", cell) for cell in rows[1]["cells"])
        if mismatches or not delimiter_ok:
            errors.append({"check": "markdown_table", "line_start": start + 1, "width_mismatches": mismatches, "valid_delimiter_row": delimiter_ok})
        tables.append({"line_start": start + 1, "line_end": index, "columns": width, "rows_including_header_and_delimiter": len(rows), "valid_delimiter_row": delimiter_ok, "width_mismatches": mismatches})

    bibliography = bibliography_checks(lines)
    if bibliography["undefined_keys"] or bibliography["duplicate_definitions"]:
        errors.append({"check": "bibliography_keys", "undefined": bibliography["undefined_keys"], "duplicate_definitions": bibliography["duplicate_definitions"]})
    pending = [{"line": number, "text": line} for number, line in enumerate(lines, 1) if re.search(r"\bPENDING\b", line, re.I)]
    if pending:
        errors.append({"check": "no_pending", "occurrences": pending})
    unchanged = digest(before) == digest(notes_path.read_bytes())
    if not unchanged:
        errors.append({"check": "notes_unchanged_during_validation", "message": "Input changed concurrently; rerun for a single current snapshot."})
    return {
        "validator": "validate_research_notes.py", "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "notes_path": str(notes_path.resolve()), "notes_sha256": digest(before),
        "notes_line_count": len(lines), "notes_unchanged_during_validation": unchanged,
        "status": "FAIL" if errors else "PASS_WITH_WARNINGS" if warnings else "PASS",
        "errors": errors, "warnings": warnings,
        "items": {"expected_total": 158, "actual_total": len(defined), "expected_family_counts": EXPECTED, "actual_family_counts": dict(family_counts), "definitions": defined, "missing": missing, "unexpected": unexpected, "duplicates": duplicates},
        "principal_notes": {"expected_count": 75, "actual_count": len(principals), "metadata_complete_count": sum(item["metadata_complete"] for item in principals), "own_idea_count": sum(item["own_idea"] for item in principals), "sentence_count_distribution": dict(sorted(Counter(item["body_sentence_count_heuristic"] for item in principals).items())), "items": principals},
        "markdown_tables": tables, "bibliography": bibliography,
        "pending_occurrences": pending,
        "limits": [
            "This is read-only with respect to the notes and all frozen/input artifacts; it writes only the JSON report.",
            "Sentence counts exclude metadata paragraphs, all table cells, headings, and code; mathematical displays are placeholders with final sentence punctuation retained.",
            "Sentence segmentation, own-idea reason cues, and citation-key recognition are heuristic and do not replace manual semantic review.",
            "This validates reference-key definitions, not publication metadata, quotations, hypotheses, or the correctness of mathematical claims.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--output", type=Path, default=RECORDS / "research_notes_validation.json")
    args = parser.parse_args()
    if args.output.resolve().parent != RECORDS or args.output.resolve() == args.notes.resolve():
        parser.error("The output must be a separate report file in this script's records directory.")
    report = validate(args.notes)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "items": report["items"]["actual_total"], "principal_notes": report["principal_notes"]["actual_count"], "metadata_complete": report["principal_notes"]["metadata_complete_count"], "bibliography_keys": report["bibliography"]["definition_count"], "tables": len(report["markdown_tables"]), "errors": report["errors"], "warnings": report["warnings"], "notes_sha256": report["notes_sha256"], "report": str(args.output.resolve())}, ensure_ascii=False, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
