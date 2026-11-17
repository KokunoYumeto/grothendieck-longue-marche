#!/usr/bin/env python3
"""Extract every explicit unsure/illegible invocation without interpreting it.

This read-only source pass preserves the exact original occurrence and argument,
including nested macros and physical newlines. It recognizes normal TeX control
words/control symbols, ignores comments and verbatim text, and balances only
unescaped grouping braces. Nested doubt invocations receive separate rows.

Positions are 1-based physical line/column numbers; start/end offsets are
0-based Unicode-character offsets, with the end exclusive. SHA-256 identifies
the exact input bytes. The script changes no page, inventory, doubts, or log
file. Its sole output is the specified derived CSV, which should be refreshed
after auditing. This is not a TeX expansion engine: catcode changes or generated
macro names are outside its scope and are reported when found.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path


PACKAGE = "MPL_136_282-327"
SCANS = tuple(n for n in range(282, 328) if n != 319)
DOUBTS = {"unsure", "illegible"}
VERBATIM_ENVIRONMENTS = {"verbatim", "verbatim*", "Verbatim", "BVerbatim",
                         "LVerbatim", "lstlisting", "minted"}
UNSUPPORTED_COMMANDS = {"catcode", "makeatletter", "makeatother", "csname",
                        "endcsname", "scantokens", "obeylines", "obeyspaces"}
COLUMNS = (
    "cote", "scan", "filename", "source_sha256", "occurrence_id", "macro",
    "line_start", "column_start", "line_end", "column_end", "start_offset",
    "end_offset", "raw_occurrence", "raw_argument", "balanced",
    "enclosing_doubt_id", "diagnostic",
)


def command_at(text: str, start: int) -> tuple[str, int]:
    """Return a control token's name and exclusive end; start must be a slash."""
    match = re.match(r"\\([A-Za-z@]+|[\s\S])", text[start:])
    return (match.group(1), start + len(match.group())) if match else ("", start + 1)


def skip_comment(text: str, start: int) -> int:
    newline = text.find("\n", start)
    return len(text) if newline < 0 else newline + 1


def skip_space_and_comments(text: str, start: int) -> int:
    while start < len(text):
        if text[start].isspace():
            start += 1
        elif text[start] == "%":
            start = skip_comment(text, start)
        else:
            break
    return start


def verb_end(text: str, after_command: int) -> int:
    pos = after_command
    if pos < len(text) and text[pos] == "*":
        pos += 1
    if pos >= len(text) or text[pos] in "\r\n":
        return pos
    delimiter = text[pos]
    end = text.find(delimiter, pos + 1)
    return len(text) if end < 0 else end + 1


def group_end(text: str, opening: int) -> int | None:
    """Return the position after the matching closing brace, without expansion."""
    if opening >= len(text) or text[opening] != "{":
        return None
    depth = 1
    pos = opening + 1
    while pos < len(text):
        char = text[pos]
        if char == "%":
            pos = skip_comment(text, pos)
            continue
        if char == "\\":
            command, end = command_at(text, pos)
            pos = verb_end(text, end) if command in {"verb", "Verb"} else end
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return pos + 1
        pos += 1
    return None


def extract(text: str) -> tuple[list[dict], list[str]]:
    rows: list[dict] = []
    diagnostics: list[str] = []
    line_starts = [0] + [match.end() for match in re.finditer("\n", text)]

    def location(offset: int) -> tuple[int, int]:
        line = bisect.bisect_right(line_starts, offset)
        return line, offset - line_starts[line - 1] + 1

    pos = 0
    while pos < len(text):
        if text[pos] == "%":
            pos = skip_comment(text, pos)
            continue
        if text[pos] != "\\":
            pos += 1
            continue
        start = pos
        command, after_command = command_at(text, pos)
        if command in {"verb", "Verb"}:
            pos = verb_end(text, after_command)
            continue
        if command in UNSUPPORTED_COMMANDS:
            line, column = location(start)
            diagnostics.append(f"line {line}, column {column}: expansion/catcode command \\{command}")
        if command == "begin":
            opening = skip_space_and_comments(text, after_command)
            end = group_end(text, opening)
            if end is not None:
                environment = text[opening + 1:end - 1].strip()
                if environment in VERBATIM_ENVIRONMENTS:
                    closing = re.search(r"\\end\s*\{" + re.escape(environment) + r"\}", text[end:])
                    if closing is None:
                        diagnostics.append(f"line {location(start)[0]}: unterminated verbatim environment")
                        break
                    pos = end + closing.end()
                    continue
        if command in DOUBTS:
            opening = skip_space_and_comments(text, after_command)
            end = group_end(text, opening)
            issue = ""
            if opening >= len(text) or text[opening] != "{":
                issue = "missing braced argument"
                end = after_command
                argument = ""
            elif end is None:
                issue = "unbalanced argument; occurrence extends to EOF"
                end = len(text)
                argument = text[opening + 1:]
            else:
                argument = text[opening + 1:end - 1]
            line_start, column_start = location(start)
            line_end, column_end = location(max(start, end - 1))
            rows.append({
                "macro": command, "line_start": line_start, "column_start": column_start,
                "line_end": line_end, "column_end": column_end,
                "start_offset": start, "end_offset": end,
                "raw_occurrence": text[start:end], "raw_argument": argument,
                "balanced": "no" if issue else "yes", "diagnostic": issue,
            })
        # Do not jump over the argument: a nested doubt must get its own row.
        pos = after_command
    return rows, diagnostics


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path,
                        help="default: records/inline_doubts.csv")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output or root / "records" / "inline_doubts.csv"
    rows: list[dict] = []
    problems: list[str] = []
    page_count = 0
    for scan in SCANS:
        relative = Path("pages") / f"{PACKAGE}_136_scan{scan}.tex"
        path = root / relative
        if not path.is_file():
            problems.append(f"scan {scan}: missing page file")
            continue
        data = path.read_bytes()
        source = data.decode("utf-8")
        digest = hashlib.sha256(data).hexdigest()
        occurrences, warnings = extract(source)
        problems.extend(f"scan {scan}: {warning}" for warning in warnings)
        for index, row in enumerate(occurrences, 1):
            row.update({"cote": "136", "scan": scan, "filename": relative.as_posix(),
                        "source_sha256": digest, "occurrence_id": f"136-{scan}-{index:04d}"})
            containers = [previous for previous in occurrences[:index - 1]
                          if previous["start_offset"] < row["start_offset"]
                          and previous["end_offset"] >= row["end_offset"]]
            row["enclosing_doubt_id"] = containers[-1]["occurrence_id"] if containers else ""
            if row["diagnostic"]:
                problems.append(f"scan {scan} line {row['line_start']}: {row['diagnostic']}")
        rows.extend(occurrences)
        page_count += 1
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    counts = Counter(row["macro"] for row in rows)
    nested = sum(bool(row["enclosing_doubt_id"]) for row in rows)
    print(f"Extracted {len(rows)} occurrences across {page_count} pages to {output}")
    print(f"unsure={counts['unsure']}; illegible={counts['illegible']}; nested doubt occurrences={nested}")
    print(f"Malformed occurrences or unsupported lexical contexts: {len(problems)}")
    for problem in problems:
        print(f"WARNING: {problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
