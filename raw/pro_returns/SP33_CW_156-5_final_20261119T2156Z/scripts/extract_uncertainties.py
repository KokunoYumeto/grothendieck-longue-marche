#!/usr/bin/env python3
"""Extract every braced \\unsure and \\illegible occurrence from TeX pages.

The extractor never interprets or settles a reading. It preserves each macro's
exact argument in TSV, including nested macros and literal newlines. Markdown
is a human-readable appendix. Comments and \\verb literals are ignored.

Run synthetic checks without opening any page:
  python extract_uncertainties.py --self-test

Run on page files:
  python extract_uncertainties.py --pages-dir out/pages \
      --tsv out/uncertainties.tsv --markdown out/uncertainties_appendix.md

An exact repeated (macro, argument) pair within one page is flagged as a
duplicate, but every occurrence remains in both outputs. Nested uncertainty
macros are also retained and flagged as overlapping spans, with parent and
child IDs. Repetition does not itself mean an editorial error.
"""
from __future__ import annotations

import argparse
import bisect
import csv
import html
import re
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path


MACROS = {"unsure", "illegible"}
FIELDS = [
    "occurrence_id", "file", "scan", "line", "column", "end_line", "end_column",
    "macro", "argument", "duplicate_of", "parent_id", "child_ids", "overlap_ids", "flags",
]


class ParseError(ValueError):
    """A target macro or verbatim literal could not be parsed completely."""


@dataclass
class Occurrence:
    occurrence_id: str
    file: str
    scan: str
    line: int
    column: int
    end_line: int
    end_column: int
    macro: str
    argument: str
    start: int
    end: int
    duplicate_of: str = ""
    parent_id: str = ""
    child_ids: list[str] = field(default_factory=list)
    overlap_ids: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)

    def row(self) -> dict[str, object]:
        return {
            name: ";".join(value) if isinstance(value, list) else value
            for name in FIELDS
            for value in [getattr(self, name)]
        }


def command_at(text: str, start: int) -> tuple[str, int]:
    """Return a TeX control word/symbol and the index immediately after it."""
    assert text[start] == "\\"
    if start + 1 == len(text):
        return "", len(text)
    end = start + 1
    if text[end].isascii() and (text[end].isalpha() or text[end] == "@"):
        while end < len(text) and text[end].isascii() and (text[end].isalpha() or text[end] == "@"):
            end += 1
        return text[start + 1:end], end
    return text[end], end + 1


def mask_noncode(source: str) -> str:
    """Mask comments and inline verbatim while preserving offsets/newlines."""
    chars = list(source)
    i = 0
    while i < len(source):
        if source[i] == "%":
            end = source.find("\n", i)
            if end < 0:
                end = len(source)
            chars[i:end] = " " * (end - i)
            i = end
        elif source[i] == "\\":
            command, end = command_at(source, i)
            if command != "verb":
                i = end
                continue
            if end < len(source) and source[end] == "*":
                end += 1
            if end == len(source) or source[end] in "\r\n":
                raise ParseError(f"Unterminated verbatim literal at character {i}")
            delimiter = source[end]
            closing = source.find(delimiter, end + 1)
            next_newline = source.find("\n", end + 1)
            if closing < 0 or (next_newline >= 0 and next_newline < closing):
                raise ParseError(f"Unterminated verbatim literal at character {i}")
            chars[i:closing + 1] = " " * (closing + 1 - i)
            i = closing + 1
        else:
            i += 1
    return "".join(chars)


def closing_brace(masked: str, opening: int) -> int:
    assert masked[opening] == "{"
    depth = 1
    i = opening + 1
    while i < len(masked):
        if masked[i] == "\\":
            _, i = command_at(masked, i)
            continue
        if masked[i] == "{":
            depth += 1
        elif masked[i] == "}":
            depth -= 1
            if not depth:
                return i
        i += 1
    raise ParseError(f"Unclosed argument beginning at character {opening}")


def extract(source: str, filename: str = "synthetic.tex", id_prefix: str = "U") -> list[Occurrence]:
    """Return all occurrences, including nested ones, in source order."""
    masked = mask_noncode(source)
    line_starts = [0] + [m.end() for m in re.finditer("\n", source)]

    def position(offset: int) -> tuple[int, int]:
        index = bisect.bisect_right(line_starts, offset) - 1
        return index + 1, offset - line_starts[index] + 1

    match = re.search(r"scan(\d+)", filename)
    scan = str(int(match.group(1))) if match else ""
    result: list[Occurrence] = []
    i = 0
    while i < len(masked):
        if masked[i] != "\\":
            i += 1
            continue
        command, after_command = command_at(masked, i)
        if command not in MACROS:
            i = after_command
            continue
        opening = after_command
        while opening < len(masked) and masked[opening].isspace():
            opening += 1
        if opening == len(masked) or masked[opening] != "{":
            ln, col = position(i)
            raise ParseError(f"{filename}:{ln}:{col}: \\{command} has no braced argument")
        try:
            closing = closing_brace(masked, opening)
        except ParseError as exc:
            ln, col = position(i)
            raise ParseError(f"{filename}:{ln}:{col}: {exc}") from exc
        ln, col = position(i)
        end_ln, end_col = position(closing)
        result.append(Occurrence(
            occurrence_id=f"{id_prefix}{len(result) + 1:04d}", file=filename, scan=scan,
            line=ln, column=col, end_line=end_ln, end_column=end_col,
            macro="\\" + command, argument=source[opening + 1:closing],
            start=i, end=closing + 1,
        ))
        # Continue inside the argument to retain, rather than swallow, any nested macro.
        i = opening + 1

    first_seen: dict[tuple[str, str], str] = {}
    stack: list[Occurrence] = []
    for item in result:
        key = (item.macro, item.argument)
        if key in first_seen:
            item.duplicate_of = first_seen[key]
            item.flags.append("duplicate_argument")
        else:
            first_seen[key] = item.occurrence_id
        while stack and stack[-1].end <= item.start:
            stack.pop()
        if stack:
            if item.end > stack[-1].end:
                # Balanced braced arguments cannot cross. This guards the parser invariant.
                raise ParseError(f"{filename}: crossing uncertainty spans at {item.occurrence_id}")
            item.parent_id = stack[-1].occurrence_id
            stack[-1].child_ids.append(item.occurrence_id)
            item.flags.append("nested_uncertainty")
            for ancestor in stack:
                item.overlap_ids.append(ancestor.occurrence_id)
                ancestor.overlap_ids.append(item.occurrence_id)
                if "contains_uncertainty" not in ancestor.flags:
                    ancestor.flags.append("contains_uncertainty")
        stack.append(item)
    return result


def write_tsv(path: Path, items: list[Occurrence]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(item.row() for item in items)


def code(value: str) -> str:
    """HTML code spans keep TeX literal; entity-encode table separators."""
    escaped = html.escape(value).replace("|", "&#124;").replace("\r", "&#13;")
    return "<code>" + escaped.replace("\n", "</code><br><code>") + "</code>"


def write_markdown(path: Path, items: list[Occurrence]) -> None:
    lines = [
        "## Exhaustive in-place uncertainty register",
        "",
        "This appendix lists every `\\unsure{…}` and `\\illegible{…}` occurrence "
        "in the page files, in filename and source order. The TSV preserves the "
        "exact arguments, including whitespace and newlines; this table renders "
        "them for reading. Line and column numbers are one-based.",
        "",
        "Repeated exact arguments within a page are retained and marked "
        "`duplicate_argument`; this flag does not itself imply an error. Nested "
        "uncertainty macros are listed separately, with their parent and every "
        "overlapping occurrence identified. Ordinary nested TeX macros, such as "
        "`\\ensuremath`, are not uncertainty overlaps.",
        "",
        f"**Occurrences: {len(items)}** "
        f"({sum(i.macro == r'\unsure' for i in items)} `\\unsure`; "
        f"{sum(i.macro == r'\illegible' for i in items)} `\\illegible`).",
        "",
        "| ID | Scan | File and line:column | Macro | Exact argument (rendered) | Flags / relationships |",
        "|---|---:|---|---|---|---|",
    ]
    for item in items:
        details = list(item.flags)
        if item.duplicate_of:
            details.append("duplicate of " + item.duplicate_of)
        if item.parent_id:
            details.append("parent " + item.parent_id)
        if item.child_ids:
            details.append("children " + ", ".join(item.child_ids))
        if item.overlap_ids:
            details.append("overlaps " + ", ".join(item.overlap_ids))
        location = f"{item.file}:{item.line}:{item.column}"
        lines.append(
            f"| {item.occurrence_id} | {item.scan} | {code(location)} | "
            f"{code(item.macro)} | {code(item.argument)} | "
            f"{html.escape('; '.join(details)).replace('|', '&#124;')} |"
        )
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def self_test() -> None:
    source = (
        "% \\unsure{comment}\n"
        "plain \\unsure{\\ensuremath{=}|m}, \\illegible{2}.\n"
        "\\unsure{a|\\unsure{b}} and \\unsure{b}\n"
        "\\verb|\\unsure{literal}| \\verb*+\\illegible{literal}+\n"
        "\\\\unsure{escaped control symbol} \\unsurefoo{not target}\n"
        "\\unsure % skipped brace } and macro \\unsure{comment}\n"
        "{multiline\n\\{x\\} \\text{y}}\n"
        "\\unsure{a % } comment\n b}\\unsure{\\%}"
    )
    items = extract(source, "J156-5-01_156-5_scan002.tex", "S002-U")
    assert [x.argument for x in items] == [
        r"\ensuremath{=}|m", "2", r"a|\unsure{b}", "b", "b",
        "multiline\n\\{x\\} \\text{y}", "a % } comment\n b", r"\%",
    ]
    assert items[0].line == 2 and items[0].column == 7
    assert not items[0].overlap_ids  # ensuremath is ordinary nesting, not uncertainty.
    assert items[2].child_ids == [items[3].occurrence_id]
    assert items[3].parent_id == items[2].occurrence_id
    assert items[2].overlap_ids == [items[3].occurrence_id]
    assert items[3].overlap_ids == [items[2].occurrence_id]
    assert items[4].duplicate_of == items[3].occurrence_id
    assert "duplicate_argument" in items[4].flags
    assert items[5].line == 6 and items[5].end_line == 8
    assert all(x.scan == "2" for x in items)
    deep = extract(r"\unsure{x\unsure{y\illegible{1}}}")
    assert len(deep) == 3
    assert deep[2].parent_id == deep[1].occurrence_id
    assert deep[2].overlap_ids == [deep[0].occurrence_id, deep[1].occurrence_id]
    assert deep[0].overlap_ids == [deep[1].occurrence_id, deep[2].occurrence_id]
    for bad in (r"\unsure{x", r"\unsure x", r"\verb|unterminated"):
        try:
            extract(bad)
        except ParseError:
            pass
        else:
            raise AssertionError("Malformed input accepted: " + bad)
    with tempfile.TemporaryDirectory(prefix="uncertainty-parser-synthetic-") as temp:
        tsv = Path(temp) / "synthetic.tsv"
        markdown = Path(temp) / "synthetic.md"
        write_tsv(tsv, items)
        write_markdown(markdown, items)
        with tsv.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream, delimiter="\t"))
        assert [r["argument"] for r in rows] == [x.argument for x in items]
        assert "&#124;" in markdown.read_text(encoding="utf-8")
        assert "overlaps" in markdown.read_text(encoding="utf-8")
    print("Synthetic extraction, exact-argument TSV round-trip, duplicate, overlap, and error checks passed.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    default_out = Path(__file__).resolve().parents[1]
    parser.add_argument("--pages-dir", type=Path, default=default_out / "pages")
    parser.add_argument("--tsv", type=Path, default=default_out / "SP33_CW_156-5_uncertainties.tsv")
    parser.add_argument("--markdown", type=Path, default=default_out / "SP33_CW_156-5_uncertainties_appendix.md")
    parser.add_argument("--self-test", action="store_true", help="Run synthetic tests only; do not read page files")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    paths = sorted(args.pages_dir.glob("*.tex"), key=lambda p: p.name)
    if not paths:
        parser.error(f"No .tex files found in {args.pages_dir}")
    input_paths = {p.resolve() for p in paths}
    if args.tsv.resolve() == args.markdown.resolve():
        parser.error("TSV and Markdown output paths must differ")
    if args.tsv.resolve() in input_paths or args.markdown.resolve() in input_paths:
        parser.error("An output path would overwrite an input page")
    all_items: list[Occurrence] = []
    for file_index, path in enumerate(paths, 1):
        # Explicit newline='' retains the source argument's exact line endings.
        with path.open(encoding="utf-8", newline="") as stream:
            source = stream.read()
        match = re.search(r"scan(\d+)", path.name)
        prefix = f"S{int(match.group(1)):03d}-U" if match else f"F{file_index:03d}-U"
        try:
            all_items.extend(extract(source, path.name, prefix))
        except ParseError as exc:
            print(str(exc), file=sys.stderr)
            return 2
    if len({x.occurrence_id for x in all_items}) != len(all_items):
        print("Duplicate occurrence IDs; page filenames contain repeated scan numbers.", file=sys.stderr)
        return 2
    write_tsv(args.tsv, all_items)
    write_markdown(args.markdown, all_items)
    print(f"Extracted {len(all_items)} uncertainty occurrences from {len(paths)} page files.")
    print(f"Exact repeated arguments: {sum(bool(x.duplicate_of) for x in all_items)}")
    print(f"Nested uncertainty occurrences: {sum(bool(x.parent_id) for x in all_items)}")
    print(f"TSV: {args.tsv}")
    print(f"Markdown: {args.markdown}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
