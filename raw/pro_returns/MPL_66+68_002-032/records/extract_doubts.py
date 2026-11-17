#!/usr/bin/env python3
"""Extract doubt macros mechanically, without judging or changing readings.

Reads only the 30 expected page files. Never reads scans or context. Nested
braces and nested doubt macros are retained; escaped braces and TeX comments
are handled lexically. Alternatives are split only at an unescaped vertical
bar at argument brace depth zero. That is a mechanical convention, not a
claim that every such bar necessarily denotes an alternative reading.

Usage:
    python work/records/extract_doubts.py work
    python work/records/extract_doubts.py work --output /absolute/report.json

The only written file is the requested JSON report. Page files are read-only.
"""

from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

PREFIX = "MPL_66+68_002-032"
SCANS = tuple(range(2, 23)) + tuple(range(24, 33))
CONTROL = re.compile(r"\\(?:[A-Za-z@]+|.)", re.DOTALL)


def mask_comments(text: str) -> str:
    """Preserve offsets/newlines while masking unescaped percent comments."""
    result = list(text)
    index = 0
    while index < len(text):
        if text[index] == "\\":
            token = CONTROL.match(text, index)
            index = token.end() if token else index + 1
        elif text[index] == "%":
            end = text.find("\n", index)
            end = len(text) if end < 0 else end
            result[index:end] = " " * (end - index)
            index = end
        else:
            index += 1
    return "".join(result)


def close_brace(masked: str, opening: int) -> int | None:
    depth = 1
    index = opening + 1
    while index < len(masked):
        char = masked[index]
        if char == "\\":
            token = CONTROL.match(masked, index)
            index = token.end() if token else index + 1
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def split_alternatives(original: str, masked: str) -> list[str]:
    boundaries = [-1]
    index = 0
    depth = 0
    while index < len(masked):
        char = masked[index]
        if char == "\\":
            token = CONTROL.match(masked, index)
            index = token.end() if token else index + 1
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "|" and depth == 0:
            boundaries.append(index)
        index += 1
    boundaries.append(len(original))
    return [original[left + 1:right] for left, right in zip(boundaries, boundaries[1:])]


def extract(path: Path, scan: int) -> tuple[list[dict], list[dict], str]:
    text = path.read_text(encoding="utf-8")
    masked = mask_comments(text)
    starts = [0] + [match.end() for match in re.finditer("\n", text)]
    lines = text.splitlines()
    occurrences: list[dict] = []
    issues: list[dict] = []
    index = 0
    while index < len(masked):
        if masked[index] != "\\":
            index += 1
            continue
        token = CONTROL.match(masked, index)
        if token is None:
            index += 1
            continue
        macro = token.group(0)
        offset = index
        index = token.end()
        if macro not in (r"\unsure", r"\illegible"):
            continue
        line_number = bisect_right(starts, offset)
        opening = token.end()
        while opening < len(masked) and masked[opening].isspace():
            opening += 1
        if opening >= len(masked) or masked[opening] != "{":
            issues.append({"page_filename": path.name, "scan": scan,
                           "tex_line": line_number, "macro": macro,
                           "issue": "Missing braced argument"})
            continue
        closing = close_brace(masked, opening)
        if closing is None:
            issues.append({"page_filename": path.name, "scan": scan,
                           "tex_line": line_number, "macro": macro,
                           "issue": "Unbalanced braced argument"})
            continue
        argument = text[opening + 1:closing]
        parts = split_alternatives(argument, masked[opening + 1:closing])
        if macro == r"\illegible":
            reading, alternatives = argument, []
        else:
            reading, alternatives = parts[0], parts[1:]
        occurrence = {
            "page_filename": path.name,
            "cote": 68,
            "scan": scan,
            "tex_line": line_number,
            "tex_end_line": bisect_right(starts, closing),
            "macro": macro,
            "reading": reading,
            "alternatives": alternatives,
            "raw_argument": argument,
            "exact_macro_tex": text[offset:closing + 1],
            "surrounding_line": lines[line_number - 1] if line_number <= len(lines) else "",
            "start_offset": offset,
            "end_offset_exclusive": closing + 1,
        }
        if macro == r"\illegible":
            if re.fullmatch(r"\s*\d+\s*", argument):
                occurrence["estimated_words"] = int(argument)
            else:
                issues.append({"page_filename": path.name, "scan": scan,
                               "tex_line": line_number, "macro": macro,
                               "issue": "Illegible argument is not an unsigned integer"})
        if not argument.strip():
            issues.append({"page_filename": path.name, "scan": scan,
                           "tex_line": line_number, "macro": macro,
                           "issue": "Empty doubt argument"})
        occurrences.append(occurrence)
        # Continue after the command name, not the argument, so any nested
        # doubt macro is independently represented in the output.
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return occurrences, issues, digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("work_dir", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.work_dir.resolve()
    output = args.output.resolve() if args.output else root / "records/doubt_occurrences.json"
    expected = [root / "pages" / f"{PREFIX}_68_scan{scan:03}.tex" for scan in SCANS]
    if output in [path.resolve() for path in expected]:
        parser.error("Output must not overwrite a page file")
    occurrences: list[dict] = []
    issues: list[dict] = []
    source_hashes: dict[str, str] = {}
    for scan, path in zip(SCANS, expected):
        try:
            found, page_issues, digest = extract(path, scan)
        except (OSError, UnicodeError) as exc:
            issues.append({"page_filename": path.name, "scan": scan,
                           "issue": f"Page could not be read: {exc}"})
            continue
        occurrences.extend(found)
        issues.extend(page_issues)
        source_hashes[path.name] = digest
    macro_counts = Counter(item["macro"] for item in occurrences)
    page_counts = Counter(item["scan"] for item in occurrences)
    report = {
        "scope": "Mechanical extraction only. No judgment, confidence assignment, correction, OCR, or context access.",
        "alternative_split_rule": "Unescaped vertical bars at argument brace depth zero; nested-brace bars are retained.",
        "line_number_rule": "One-based line numbers in the exact UTF-8 page file; surrounding_line excludes the newline.",
        "offset_rule": "Zero-based Python Unicode character offsets; end_offset_exclusive is exclusive.",
        "summary": {
            "pages_read": len(source_hashes),
            "pages_with_doubts": len(page_counts),
            "occurrences": len(occurrences),
            "macro_counts": dict(sorted(macro_counts.items())),
            "per_scan_counts": {f"{scan:03}": page_counts[scan] for scan in SCANS},
            "structural_issues": len(issues),
        },
        "source_sha256": source_hashes,
        "structural_issues": issues,
        "occurrences": occurrences,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Doubt extraction: pages={len(source_hashes)}, occurrences={len(occurrences)}, structural_issues={len(issues)}")
    print(", ".join(f"{macro}={count}" for macro, count in sorted(macro_counts.items())))
    print(f"Report: {output}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
