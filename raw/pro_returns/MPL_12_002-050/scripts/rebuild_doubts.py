#!/usr/bin/env python3
"""Refresh only the doubt-register section from the existing page TeX files.

Run explicitly, after making any intended page corrections:
    python3 work/scripts/rebuild_doubts.py --root work

This script does not alter page files, progress.log, the notation table,
abbreviations, or legibility prose. It cannot verify readings against images.
The balanced-brace parser below reuses the macros() algorithm in save_page.py;
it is copied rather than imported because that script writes files at import.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import os
from pathlib import Path
import re
import sys


PREFIX = "MPL_12_002-050"
NO_ALTERNATIVE = "Unresolved ink; no secure alternative"
ILLEGIBLE_ALTERNATIVE = "crossed or physically indistinct ink"
CONFIDENCES = {"high", "medium", "low"}
HEADER = "| Cote | Scan | Approximate line or position | Reading | Alternative(s) | Confidence |"
RULE = "|---|---|---|---|---|---|"


def _escaped(text: str, pos: int) -> bool:
    count = 0
    pos -= 1
    while pos >= 0 and text[pos] == "\\":
        count += 1
        pos -= 1
    return count % 2 == 1


def _mask_comments(text: str) -> str:
    """Preserve offsets and line numbers while excluding TeX comments."""
    chars = list(text)
    cursor = 0
    while cursor < len(text):
        if text[cursor] == "%" and not _escaped(text, cursor):
            end = text.find("\n", cursor)
            if end < 0:
                end = len(text)
            for i in range(cursor, end):
                if chars[i] != "\r":
                    chars[i] = " "
            cursor = end
        else:
            cursor += 1
    return "".join(chars)


def macros(text: str, name: str):
    """Balanced-argument extraction adapted from save_page.py's macros().

    Retains that helper's argument/line interface. Escape parity is checked,
    and finditer also permits a nested doubt macro to have its own entry.
    """
    clean = _mask_comments(text)
    pattern = re.compile(r"\\" + re.escape(name) + r"\s*\{")
    for match in pattern.finditer(clean):
        if _escaped(clean, match.start()):
            continue
        argument = match.end()
        cursor, depth = argument, 1
        while cursor < len(clean) and depth:
            if clean[cursor] == "{" and not _escaped(clean, cursor):
                depth += 1
            elif clean[cursor] == "}" and not _escaped(clean, cursor):
                depth -= 1
            cursor += 1
        line = clean.count("\n", 0, argument) + 1
        if depth:
            raise ValueError(f"unclosed \\{name} argument at transcription line {line}")
        yield clean[argument:cursor - 1], line, match.start()


def _table_cells(line: str) -> list[str]:
    """Read old rows, allowing literal pipes inside backtick code spans."""
    cells, current = [], []
    fence = 0
    cursor = 0
    while cursor < len(line):
        ch = line[cursor]
        if ch == "`":
            end = cursor + 1
            while end < len(line) and line[end] == "`":
                end += 1
            run = end - cursor
            if not fence:
                fence = run
            elif run == fence:
                fence = 0
            current.append(line[cursor:end])
            cursor = end
            continue
        # GFM table escapes are accepted even inside a code span. Checking the
        # immediately preceding slash also handles a literal TeX backslash-pipe.
        if ch == "|" and not fence and (cursor == 0 or line[cursor - 1] != "\\"):
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
        cursor += 1
    cells.append("".join(current).strip())
    if cells and not cells[0]:
        cells.pop(0)
    if cells and not cells[-1]:
        cells.pop()
    return cells


def _plain_cell(cell: str) -> str:
    cell = cell.strip()
    match = re.fullmatch(r"(`+)(.*)\1", cell, flags=re.DOTALL)
    return match.group(2).strip() if match else cell


def _relaxed(value: str) -> str:
    # New table rows escape pipes. Keep an exact key as well so legacy TeX \|
    # is never assumed to be a Markdown escape when an exact match is present.
    return " ".join(value.replace("\\|", "|").split())


def _prior_confidences(section: str):
    exact = defaultdict(list)
    relaxed = defaultdict(list)
    for line in section.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = _table_cells(line)
        if len(cells) != 6:
            continue
        try:
            cote, scan = int(cells[0]), int(cells[1])
        except ValueError:
            continue
        confidence = _plain_cell(cells[5]).lower()
        if cote != 12 or confidence not in CONFIDENCES:
            continue
        reading, alternatives = _plain_cell(cells[3]), _plain_cell(cells[4])
        exact[(scan, reading, alternatives)].append(confidence)
        relaxed[(scan, _relaxed(reading), _relaxed(alternatives))].append(confidence)
    return exact, relaxed


def _section_bounds(document: str) -> tuple[int, int]:
    heading = re.search(r"(?m)^(#{1,6})[ \t]+Doubt register[ \t]*\r?$", document)
    if not heading:
        raise ValueError("doubts file has no 'Doubt register' heading")
    depth = len(heading.group(1))
    start = heading.end()
    if document.startswith("\r\n", start):
        start += 2
    elif document.startswith("\n", start):
        start += 1
    next_heading = re.search(rf"(?m)^#{{1,{depth}}}[ \t]+", document[start:])
    if not next_heading:
        raise ValueError("no following section found; refusing to risk other doubts-file content")
    return start, start + next_heading.start()


def _code_cell(value: str) -> str:
    value = " ".join(value.split()).replace("|", "\\|")
    longest = max((len(m.group()) for m in re.finditer(r"`+", value)), default=0)
    fence = "`" * (longest + 1)
    padding = " " if value.startswith("`") or value.endswith("`") else ""
    return f"{fence}{padding}{value}{padding}{fence}"


def rebuild(document: str, pages: list[tuple[int, str]]) -> tuple[str, int, int]:
    """Return an updated document, number of entries, and preserved confidences."""
    start, end = _section_bounds(document)
    exact, relaxed = _prior_confidences(document[start:end])
    used = defaultdict(int)
    rows = []
    preserved = 0
    for scan, text in sorted(pages):
        entries = []
        for argument, line, offset in macros(text, "unsure"):
            parts = argument.split("|", 1)
            entries.append((offset, line, parts[0], parts[1] if len(parts) > 1
                            else NO_ALTERNATIVE, "medium"))
        for argument, line, offset in macros(text, "illegible"):
            entries.append((offset, line, f"unreadable, estimated {argument} word(s)",
                            ILLEGIBLE_ALTERNATIVE, "low"))
        for _, line, reading, alternatives, default in sorted(entries):
            key = (scan, reading, alternatives)
            confidence_values = exact.get(key)
            if not confidence_values:
                confidence_values = relaxed.get((scan, _relaxed(reading), _relaxed(alternatives)))
            if confidence_values:
                # Preserve occurrence order for repeated keys. If there are
                # additional identical occurrences, reuse the last known value.
                confidence = confidence_values[min(used[key], len(confidence_values) - 1)]
                used[key] += 1
                preserved += 1
            else:
                confidence = default
            rows.append(f"| 12 | {scan:03d} | transcription line {line} | "
                        f"{_code_cell(reading)} | {_code_cell(alternatives)} | {confidence} |")
    newline = "\r\n" if "\r\n" in document else "\n"
    replacement = newline + newline.join([HEADER, RULE, *rows]) + newline * 2
    return document[:start] + replacement + document[end:], len(rows), preserved


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    destination = root / f"{PREFIX}_doubts.md"
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    try:
        document = destination.read_bytes().decode("utf-8")
        pattern = re.compile(rf"{re.escape(PREFIX)}_12_scan(\d{{3}})\.tex\Z")
        pages = []
        for path in (root / "pages").glob(f"{PREFIX}_12_scan*.tex"):
            match = pattern.fullmatch(path.name)
            if match:
                pages.append((int(match.group(1)), path.read_bytes().decode("utf-8")))
        if not pages:
            raise ValueError("no page files found; doubts file was not changed")
        updated, count, preserved = rebuild(document, pages)
        temporary.write_bytes(updated.encode("utf-8"))
        os.replace(temporary, destination)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Doubt-register rebuild failed: {exc}", file=sys.stderr)
        return 1
    print(f"Rebuilt {count} doubt entries from {len(pages)} page files; "
          f"preserved {preserved} matching prior confidence values.")
    print("Only the doubt-register body changed. Notation, abbreviations, and legibility "
          "sections are retained; reading accuracy still requires visual verification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
