#!/usr/bin/env python3
"""Build a structural inventory from the existing diplomatic TeX fragments.

This is only an inventory aid: it cannot detect material absent from a
transcription and cannot establish visual completeness or reading accuracy.
The operator must compare its rows with each scan. It never opens source images
or the context archive and never changes page files or progress.log.

Import inventory_rows(text, scan, sheet_kind="text"), or run:
    python3 work/scripts/inventory_from_tex.py --root work

The command rebuilds MPL_12_002-050_inventory.csv in scan order, retaining each
scan's sheet_kind from the existing CSV. New scans default to "text".
"""

from __future__ import annotations

import argparse
import bisect
import csv
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PREFIX = "MPL_12_002-050"
FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
SPECIAL = {"inserted": "insertion", "deleted": "deletion",
           "margin": "margin note", "diagram": "diagram", "figure": "drawing"}
METADATA = {"cotefile", "scanpage"}
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
COMMAND = re.compile(r"\\([A-Za-z@]+)")


@dataclass(frozen=True)
class Span:
    start: int
    end: int
    kind: str
    depth: int = 0


def _escaped(text: str, pos: int) -> bool:
    count = 0
    pos -= 1
    while pos >= 0 and text[pos] == "\\":
        count += 1
        pos -= 1
    return count % 2 == 1


def _without_comments(text: str) -> str:
    """Blank comment text, preserving every offset and newline."""
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


def _argument_end(text: str, start: int) -> int:
    """Return the exclusive end of a balanced argument starting with '{'."""
    depth = 0
    for cursor in range(start, len(text)):
        ch = text[cursor]
        if ch in "{}" and not _escaped(text, cursor):
            depth += 1 if ch == "{" else -1
            if depth == 0:
                return cursor + 1
    line = text.count("\n", 0, start) + 1
    raise ValueError(f"unclosed macro argument at transcription line {line}")


def _scan(text: str) -> tuple[str, list[Span], list[Span], list[int]]:
    """Find all special macros/displays and classify display nesting.

    All offsets refer to the original text. Braces inside nested macro
    arguments keep their displays from splitting an enclosing text block.
    """
    clean = _without_comments(text)
    chars = list(clean)
    special: list[Span] = []
    displays: list[Span] = []
    display_stack: list[tuple[int, int]] = []
    depths = [0] * (len(clean) + 1)
    depth = 0
    for cursor, ch in enumerate(clean):
        depths[cursor] = depth
        if ch == "\\" and not _escaped(clean, cursor):
            match = COMMAND.match(clean, cursor)
            if match and match.group(1) in SPECIAL.keys() | METADATA:
                name = match.group(1)
                arg = match.end()
                while arg < len(clean) and clean[arg].isspace():
                    arg += 1
                if arg >= len(clean) or clean[arg] != "{":
                    line = clean.count("\n", 0, cursor) + 1
                    raise ValueError(f"\\{name} has no braced argument at line {line}")
                end = _argument_end(clean, arg)
                if name in SPECIAL:
                    special.append(Span(cursor, end, SPECIAL[name], depth))
                else:
                    for i in range(cursor, end):
                        if chars[i] not in "\r\n":
                            chars[i] = " "
            if clean.startswith("\\[", cursor):
                display_stack.append((cursor, depth))
            elif clean.startswith("\\]", cursor):
                if not display_stack:
                    line = clean.count("\n", 0, cursor) + 1
                    raise ValueError(f"unmatched \\] at transcription line {line}")
                start, opening_depth = display_stack.pop()
                displays.append(Span(start, cursor + 2, "display", opening_depth))
        elif ch in "{}" and not _escaped(clean, cursor):
            depth += 1 if ch == "{" else -1
            if depth < 0:
                line = clean.count("\n", 0, cursor) + 1
                raise ValueError(f"unmatched closing brace at transcription line {line}")
    depths[len(clean)] = depth
    if display_stack:
        line = clean.count("\n", 0, display_stack[-1][0]) + 1
        raise ValueError(f"unclosed \\[ at transcription line {line}")
    if depth:
        raise ValueError("unclosed unescaped brace in transcription")
    return "".join(chars), special, sorted(displays, key=lambda span: span.start), depths


def _trim(text: str, start: int, end: int) -> tuple[int, int]:
    while start < end and text[start].isspace():
        start += 1
    while end > start and text[end - 1].isspace():
        end -= 1
    return start, end


def _special_only(text: str, start: int, end: int, special: list[Span]) -> bool:
    """Whether the block consists solely of standalone special macros."""
    cursor = start
    for span in sorted(special, key=lambda item: (item.start, -item.end)):
        if span.start < cursor or span.end > end:
            continue
        if text[cursor:span.start].strip():
            return False
        cursor = span.end
    return cursor > start and not text[cursor:end].strip()


def _blocks(text: str, start: int, end: int, depths: list[int],
            special: list[Span]) -> list[Span]:
    """Contiguous nonblank root lines in an interval outside root displays."""
    blocks = []
    block_start = start
    cursor = start
    while cursor < end:
        newline = text.find("\n", cursor, end)
        line_end = end if newline < 0 else newline + 1
        # A blank line inside a macro is part of that macro, not a root break.
        if not text[cursor:line_end].strip() and depths[cursor] == 0:
            left, right = _trim(text, block_start, cursor)
            if left < right and not _special_only(text, left, right, special):
                blocks.append(Span(left, right, "text"))
            block_start = line_end
        cursor = line_end
    left, right = _trim(text, block_start, end)
    if left < right and not _special_only(text, left, right, special):
        blocks.append(Span(left, right, "text"))
    return blocks


def inventory_rows(text: str, scan: int, sheet_kind: str = "text") -> list[dict[str, str]]:
    """Return ordered inventory rows for one page, without reading any files.

    Every paragraph/root text block and every \\[...\\] display gets a row.
    Every inserted/deleted/margin/diagram/figure macro, including nested ones,
    gets its own row. Standalone special macros do not also produce a redundant
    root-text row. Metadata commands and TeX comments are excluded; mspage is
    deliberately retained as text. Excerpts retain TeX spelling and macros,
    with whitespace collapsed and length limited to 180 characters.

    'transcribed=yes' identifies represented TeX spans; it is not an independent
    claim that the manuscript's visual contents have all been represented.
    """
    scan = int(scan)
    if sheet_kind not in SHEET_KINDS:
        raise ValueError(f"unsupported sheet_kind: {sheet_kind!r}")
    clean, special, displays, depths = _scan(text)
    spans = special + displays
    # Ignore displays nested in macro arguments when cutting root text blocks.
    # Outermost display ranges also protect against an accidental nested pair.
    root_displays = []
    covered_to = -1
    for span in displays:
        if span.depth == 0 and span.start >= covered_to:
            root_displays.append(span)
            covered_to = span.end
    cursor = 0
    for span in root_displays:
        spans.extend(_blocks(clean, cursor, span.start, depths, special))
        cursor = span.end
    spans.extend(_blocks(clean, cursor, len(clean), depths, special))
    starts = [0] + [match.end() for match in re.finditer("\n", text)]
    rows = []
    priority = {"text": 0, "display": 1, "margin note": 2,
                "diagram": 2, "drawing": 2, "insertion": 2, "deletion": 2}
    for number, span in enumerate(sorted(spans, key=lambda item:
                                        (item.start, priority[item.kind], -item.end)), 1):
        first_line = bisect.bisect_right(starts, span.start)
        last_line = bisect.bisect_right(starts, max(span.start, span.end - 1))
        position = f"transcription line {first_line}"
        if last_line != first_line:
            position += f"-{last_line}"
        excerpt = " ".join(clean[span.start:span.end].split())[:180]
        rows.append({"cote": "12", "scan": f"{scan:03d}",
                     "sheet_kind": sheet_kind, "element": f"{number:03d}",
                     "kind": span.kind, "position": position,
                     "first_words_or_objects": excerpt, "transcribed": "yes"})
    return rows


def _existing_kinds(path: Path) -> dict[int, str]:
    if not path.exists():
        return {}
    kinds = {}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not {"scan", "sheet_kind"} <= set(reader.fieldnames):
            raise ValueError("existing inventory has no scan/sheet_kind columns")
        for lineno, row in enumerate(reader, 2):
            scan = int(row["scan"])
            kind = row["sheet_kind"].strip()
            if kind not in SHEET_KINDS:
                raise ValueError(f"existing inventory line {lineno}: invalid sheet_kind {kind!r}")
            if scan in kinds and kinds[scan] != kind:
                raise ValueError(f"existing inventory: inconsistent sheet_kind for scan {scan}")
            kinds[scan] = kind
    return kinds


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="deliverable directory; default is this script's work/ parent")
    args = parser.parse_args()
    root = args.root.resolve()
    destination = root / f"{PREFIX}_inventory.csv"
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    try:
        kinds = _existing_kinds(destination)
        pattern = re.compile(rf"{re.escape(PREFIX)}_12_scan(\d{{3}})\.tex\Z")
        paths = []
        for path in (root / "pages").glob(f"{PREFIX}_12_scan*.tex"):
            match = pattern.fullmatch(path.name)
            if match:
                paths.append((int(match.group(1)), path))
        if not paths:
            raise ValueError("no page files found; existing inventory was not changed")
        rows = []
        for scan, path in sorted(paths):
            try:
                rows.extend(inventory_rows(path.read_text(encoding="utf-8"), scan,
                                           kinds.get(scan, "text")))
            except ValueError as exc:
                raise ValueError(f"{path.name}: {exc}") from exc
        with temporary.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temporary, destination)
    except (OSError, UnicodeError, ValueError, csv.Error, TypeError) as exc:
        print(f"Inventory rebuild failed: {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {len(rows)} structural inventory rows for {len(paths)} pages: {destination}")
    print("This is an aid derived from the TeX. Verify every page's coverage visually against "
          "its scan; no visual completeness or reading-accuracy check was performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
