#!/usr/bin/env python3
"""Enumerate diplomatic doubt macros without interpreting their readings.

Only page .tex files are read. The output is a review table; the transcription
and main doubts document are never modified.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
import html
from pathlib import Path
import re
import sys


PREFIX = "MPL_14_002-044"
LOW_CONFIDENCE_SCANS = {3, 13, 15, 30, 32, 41}
PAGE_PATTERN = re.compile(rf"{PREFIX}_(\d+)_scan(\d{{3}})\.tex")
COMMAND_PATTERN = re.compile(r"\\([A-Za-z]+|.)", re.DOTALL)
DOUBT_COMMANDS = {"unsure", "illegible"}


def skip_comment(text: str, index: int) -> int:
    newline = text.find("\n", index)
    return len(text) if newline < 0 else newline + 1


def skip_space_and_comments(text: str, index: int) -> int:
    while index < len(text):
        if text[index].isspace():
            index += 1
        elif text[index] == "%":
            index = skip_comment(text, index)
        else:
            break
    return index


def balanced_argument_end(text: str, opening: int) -> int:
    """Return the closing-brace index, respecting escaped braces and comments."""
    if text[opening] != "{":
        raise ValueError("Argument does not begin with an opening brace")
    depth = 1
    index = opening + 1
    while index < len(text):
        char = text[index]
        if char == "%":
            index = skip_comment(text, index)
            continue
        if char == "\\":
            command = COMMAND_PATTERN.match(text, index)
            index = command.end() if command else index + 1
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    raise ValueError("Unbalanced doubt-macro argument")


def split_top_level_alternatives(argument: str) -> list[str]:
    """Split unescaped | tokens only at brace depth zero, retaining whitespace."""
    result = []
    start = 0
    index = 0
    depth = 0
    while index < len(argument):
        char = argument[index]
        if char == "%":
            index = skip_comment(argument, index)
            continue
        if char == "\\":
            command = COMMAND_PATTERN.match(argument, index)
            index = command.end() if command else index + 1
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "|" and depth == 0:
            result.append(argument[start:index])
            start = index + 1
        index += 1
    result.append(argument[start:])
    return result


def occurrences(text: str) -> list[dict]:
    """Find every command occurrence, including nested doubt macros."""
    found = []
    errors = []
    index = 0
    while index < len(text):
        char = text[index]
        if char == "%":
            index = skip_comment(text, index)
            continue
        if char != "\\":
            index += 1
            continue
        match = COMMAND_PATTERN.match(text, index)
        if match is None:
            index += 1
            continue
        command = match.group(1)
        if command in DOUBT_COMMANDS:
            line = text.count("\n", 0, index) + 1
            column = index - text.rfind("\n", 0, index)
            opening = skip_space_and_comments(text, match.end())
            try:
                if opening >= len(text) or text[opening] != "{":
                    raise ValueError("Doubt macro has no braced argument")
                closing = balanced_argument_end(text, opening)
                argument = text[opening + 1:closing]
                pieces = split_top_level_alternatives(argument) if command == "unsure" else [argument]
                found.append({
                    "command": command,
                    "line": line,
                    "column": column,
                    "reading": pieces[0] if command == "unsure" else text[index:closing + 1],
                    "alternatives": pieces[1:] if command == "unsure" else [],
                })
            except ValueError as error:
                errors.append(f"line {line}, column {column}: {error}")
        # Continue inside the argument so nested occurrences are also counted.
        index = match.end()
    if errors:
        raise ValueError("\n".join(errors))
    return found


def code_cell(text: str) -> str:
    # HTML entities protect literal pipes from Markdown's table delimiter parser.
    # Line endings become visible breaks; all source characters are otherwise kept.
    encoded = html.escape(text, quote=False).replace("|", "&#124;")
    encoded = encoded.replace("\r\n", "<br>").replace("\r", "<br>").replace("\n", "<br>")
    return f"<code>{encoded}</code>"


def render(root: Path) -> tuple[str, int, int]:
    page_files = sorted((root / "pages").glob(f"{PREFIX}_*_scan*.tex"))
    if not page_files:
        raise ValueError("No page files found")
    table_rows = []
    counts = Counter()
    page_counts = []
    for path in page_files:
        match = PAGE_PATTERN.fullmatch(path.name)
        if match is None:
            raise ValueError(f"Unexpected page filename: {path.name}")
        cote, scan_text = match.groups()
        scan = int(scan_text)
        try:
            page_occurrences = occurrences(path.read_bytes().decode("utf-8"))
        except ValueError as error:
            raise ValueError(f"{path.name}: {error}") from error
        local_counts = Counter(item["command"] for item in page_occurrences)
        counts.update(local_counts)
        page_counts.append((scan_text, local_counts["unsure"], local_counts["illegible"]))
        for item in page_occurrences:
            location = f"line {item['line']}, column {item['column']} ({code_cell(chr(92) + item['command'])})"
            alternatives = "<br>".join(code_cell(value) for value in item["alternatives"]) or "—"
            confidence = "low" if scan in LOW_CONFIDENCE_SCANS else "medium"
            table_rows.append(
                f"| {cote} | {scan_text} | {location} | {code_cell(item['reading'])} | {alternatives} | {confidence} |"
            )
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    header = (
        "# Mechanical enumeration of doubt occurrences\n\n"
        f"Generated {timestamp} from {len(page_files)} page files.\n\n"
        "Every balanced `\\unsure{...}` and `\\illegible{...}` occurrence is listed, including nested occurrences. "
        "Locations are one-based lines and columns in the page's LaTeX source, not manuscript line numbers. "
        "The page filename is `pages/MPL_14_002-044_14_scanNNN.tex`, where NNN is the scan column.\n\n"
        "The confidence values are mechanical review defaults supplied for this table: **low** on scans "
        "003, 013, 015, 030, 032, and 041; **medium** on the other pages. They have not been assessed occurrence by occurrence. "
        "No manuscript reading is inferred or revised by this enumeration.\n\n"
        "Alternatives are split only at unescaped literal `|` tokens at brace depth zero within an `\\unsure` argument. "
        "Pipes inside nested braces, escaped pipes, and pipes in TeX comments do not split the argument. "
        "The `\\illegible` macro is retained with its original count. HTML encoding protects literal characters in Markdown table cells.\n\n"
        f"Totals: **{counts['unsure']}** unsure occurrences and **{counts['illegible']}** illegible occurrences "
        f"(**{sum(counts.values())}** rows).\n\n"
        "| Cote | Scan | TeX source location | Reading | Alternatives | Confidence |\n"
        "|---|---|---|---|---|---|\n"
    )
    footer = (
        "\n\n## Counts by scan\n\n"
        "| Scan | Unsure | Illegible |\n|---|---:|---:|\n"
        + "\n".join(f"| {scan} | {unsure} | {illegible} |" for scan, unsure, illegible in page_counts)
        + "\n"
    )
    return header + "\n".join(table_rows) + footer, len(page_files), sum(counts.values())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Defaults to records/doubt_occurrences.md under root")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve() if args.output else root / "records" / "doubt_occurrences.md"
    try:
        rendered, pages, count = render(root)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8", newline="")
    except (OSError, UnicodeError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print(f"Enumerated {count} doubt occurrences from {pages} page files: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
