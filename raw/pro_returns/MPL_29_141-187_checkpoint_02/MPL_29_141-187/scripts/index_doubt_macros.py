#!/usr/bin/env python3
"""Index literal doubt macros in page fragments without interpreting their text.

The TSV column ``tex_source_line`` is the one-based physical line in the
corresponding .tex file. It is NOT a manuscript line number. ``exact_content``
preserves the characters inside the macro's balanced outer braces, including
any newlines, nested commands, and comments. Standard CSV quoting is used with
tab delimiters so multiline arguments remain single TSV fields.

This is a structural index only: no scan inspection, transcription judgment,
reading audit, or mathematical check is performed.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import json
from collections import Counter
from pathlib import Path


TARGET_MACROS = frozenset({"unsure", "illegible"})
PREFIX = "MPL_29_141-187"


def control_sequence_end(text: str, position: int) -> int:
    """Return the end of a control sequence starting with a backslash."""
    end = position + 1
    if end == len(text):
        return end
    if text[end].isalpha():
        while end < len(text) and text[end].isalpha():
            end += 1
        return end
    return end + 1


def comment_end(text: str, position: int) -> int:
    end = text.find("\n", position)
    return len(text) if end < 0 else end + 1


def argument_start(text: str, position: int) -> int:
    """Skip whitespace and TeX comments between a command and its argument."""
    while position < len(text):
        if text[position].isspace():
            position += 1
        elif text[position] == "%":
            position = comment_end(text, position)
        else:
            break
    return position


def balanced_group_end(text: str, opening: int) -> int | None:
    """Find a matching brace, ignoring escaped braces and comment contents."""
    depth = 0
    position = opening
    while position < len(text):
        character = text[position]
        if character == "\\":
            position = control_sequence_end(text, position)
            continue
        if character == "%":
            position = comment_end(text, position)
            continue
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return position
        position += 1
    return None


def index_fragment(text: str) -> tuple[list[tuple[int, str, str]], list[dict]]:
    """Return (source line, macro name, exact argument) rows plus errors."""
    line_starts = [0]
    line_starts.extend(i + 1 for i, character in enumerate(text) if character == "\n")
    rows: list[tuple[int, str, str]] = []
    errors: list[dict] = []
    position = 0
    while position < len(text):
        character = text[position]
        if character == "%":
            position = comment_end(text, position)
            continue
        if character != "\\":
            position += 1
            continue
        end = control_sequence_end(text, position)
        macro = text[position + 1:end]
        if macro in TARGET_MACROS:
            line = bisect.bisect_right(line_starts, position)
            opening = argument_start(text, end)
            if opening == len(text) or text[opening] != "{":
                errors.append({"tex_source_line": line, "macro": macro,
                               "error": "Expected a braced argument"})
            else:
                closing = balanced_group_end(text, opening)
                if closing is None:
                    errors.append({"tex_source_line": line, "macro": macro,
                                   "error": "Unclosed braced argument"})
                else:
                    rows.append((line, macro, text[opening + 1:closing]))
        # Continue scanning inside arguments so nested target macros also have
        # their own rows; do not advance directly to a closing brace.
        position = end
    return rows, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output or root / "doubt_macro_index.tsv"
    rows: list[tuple[int, int, str, str]] = []
    errors: list[dict] = []
    pages_read = 0
    for scan in range(141, 188):
        page = root / "pages" / f"{PREFIX}_29_scan{scan:03d}.tex"
        if not page.is_file():
            errors.append({"scan": scan, "file": page.name, "error": "Missing page fragment"})
            continue
        fragment_rows, fragment_errors = index_fragment(page.read_text(encoding="utf-8"))
        pages_read += 1
        rows.extend((scan, *row) for row in fragment_rows)
        errors.extend({"scan": scan, "file": page.name, **error} for error in fragment_errors)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["scan", "tex_source_line", "macro", "exact_content"])
        writer.writerows(rows)
    counts = Counter(row[2] for row in rows)
    print(json.dumps({"pages_indexed": pages_read,
                      "rows": len(rows),
                      "macro_counts": dict(sorted(counts.items())),
                      "line_number_type": "one-based physical TeX source line, not manuscript line",
                      "parser_errors": errors}, ensure_ascii=False, indent=2))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
