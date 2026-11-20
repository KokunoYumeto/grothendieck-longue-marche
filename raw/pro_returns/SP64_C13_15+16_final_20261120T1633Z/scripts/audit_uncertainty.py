#!/usr/bin/env python3
"""Extract uncertainty macros and exact-context comparisons for the primary reader.

Example:
  python scripts/audit_uncertainty.py \
    --c-pages /path/to/source/pages --final-pages /path/to/work/pages \
    --output /path/to/scratch/uncertainty_audit.tsv

The output path is required and must lie outside the input/deliverable trees.
No source or deliverable is modified. Existing output requires --overwrite.
Use --page 16/004 (repeatable) to restrict extraction; otherwise all 25 expected
page pairs are considered. Missing or malformed inputs remain visible as rows.

The lexer handles nested braces, escaped control symbols, comments, \\verb,
and the named verbatim environments. It includes macros inside \\deleted{}.
For \\unsure{a|b|c}, the first candidate is the exact text before the first
unescaped top-level |. A single candidate is the complete raw argument.
No whitespace, Unicode, or line-ending conversion is applied to the inputs.

C-to-final comparisons require a unique pair of exact surrounding anchors.
The TSV records those anchors, offsets, raw spans, and both input SHA256 values.
Comparison labels describe those string equalities and positions. Reading
significance is left to the primary reader. Repeated/changed context remains
unclassified. Macro expansion, catcode changes, and constructed command names
are outside this lexer; it does not execute TeX, OCR, or mathematical checks.

Offsets are zero-based Unicode-code-point offsets, with exclusive end offsets.
Lines/columns are one-based. TSV quoting preserves embedded tabs and newlines;
read this file with a TSV/CSV parser rather than splitting physical lines.
Exit 0: audit written; 1: configuration/publication failure; 2: audit written
with file or lexical issues. Unclassified comparisons alone do not cause 2.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import os
import re
import sys
import tempfile
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path


ORDER = tuple(
    [("15", str(number)) for number in (180, 183, 184, 185, 187, 189, 190, 191, 192, 193, 194)]
    + [("16", f"{number:03d}") for number in range(3, 17)]
)
LETTERS = frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@")
UNCERTAINTY_COMMANDS = {"unsure", "illegible"}
FIELDS = (
    "record_type", "cote", "scan", "side", "file", "occurrence", "macro",
    "parse_status", "start", "end", "line", "column", "inside_deleted",
    "raw_macro", "raw_argument", "first_candidate", "candidate_count",
    "context_before", "context_after", "comparison_status", "final_start",
    "final_end", "final_span", "final_macro_ordinals",
    "C_anchor_rows_containing_final_macro", "left_anchor", "right_anchor",
    "left_anchor_is_page_prefix", "right_anchor_is_page_suffix", "anchor_size",
    "C_sha256", "final_sha256", "detail",
)


@dataclass
class Token:
    kind: str
    value: str
    start: int
    end: int
    depth: int = 0


@dataclass
class Occurrence:
    ordinal: int
    name: str
    start: int
    end: int
    status: str
    raw: str
    argument: str
    first: str
    candidate_count: int
    inside_deleted: bool = False


@dataclass
class Page:
    path: Path
    text: str
    digest: str
    occurrences: list[Occurrence]
    issues: list[tuple[str, int]] = field(default_factory=list)
    line_starts: list[int] = field(default_factory=list)


def newline_position(text: str, start: int) -> int:
    positions = [value for value in (text.find("\r", start), text.find("\n", start)) if value != -1]
    return min(positions) if positions else len(text)


def skip_tex_space(text: str, start: int) -> int:
    position = start
    while position < len(text):
        if text[position].isspace():
            position += 1
        elif text[position] == "%":
            position = newline_position(text, position + 1)
        else:
            break
    return position


def lex(text: str) -> tuple[list[Token], list[tuple[str, int]]]:
    tokens: list[Token] = []
    issues: list[tuple[str, int]] = []
    position = 0
    while position < len(text):
        character = text[position]
        if character == "%":
            position = newline_position(text, position + 1)
            continue
        if character == "\\":
            start = position
            position += 1
            word_start = position
            while position < len(text) and text[position] in LETTERS:
                position += 1
            if position == word_start:
                position = min(position + 1, len(text))
                continue
            command = text[word_start:position]
            tokens.append(Token("command", command, start, position))
            if command == "verb":
                if position < len(text) and text[position] == "*":
                    position += 1
                end_of_line = newline_position(text, position)
                closing = text.find(text[position], position + 1, end_of_line) if position < end_of_line else -1
                if closing == -1:
                    issues.append(("unclosed_verb", start))
                    position = end_of_line
                else:
                    position = closing + 1
            elif command == "begin":
                match = re.match(r"\s*\{(verbatim\*?|Verbatim|lstlisting|minted)\}", text[position:])
                if match:
                    closing_marker = "\\end{" + match.group(1) + "}"
                    closing = text.find(closing_marker, position + match.end())
                    if closing == -1:
                        issues.append(("unclosed_verbatim_environment", start))
                        position = len(text)
                    else:
                        position = closing + len(closing_marker)
            continue
        if character in "{}|":
            tokens.append(Token({"{": "open", "}": "close", "|": "separator"}[character], character, position, position + 1))
        position += 1
    return tokens, issues


def parse_page(path: Path) -> Page:
    payload = path.read_bytes()
    text = payload.decode("utf-8")
    tokens, issues = lex(text)
    stack: list[Token] = []
    closing_for: dict[int, int] = {}
    opening_tokens: dict[int, Token] = {}
    for token in tokens:
        token.depth = len(stack)
        if token.kind == "open":
            opening_tokens[token.start] = token
            stack.append(token)
        elif token.kind == "close":
            if stack:
                opening = stack.pop()
                closing_for[opening.start] = token.start
            else:
                issues.append(("unmatched_close_brace", token.start))
    issues.extend(("unmatched_open_brace", token.start) for token in stack)

    def argument_bounds(token: Token) -> tuple[int | None, int | None]:
        opening = skip_tex_space(text, token.end)
        if opening >= len(text) or text[opening] != "{" or opening not in opening_tokens:
            return None, None
        return opening, closing_for.get(opening)

    deletion_spans = []
    for token in tokens:
        if token.kind == "command" and token.value == "deleted":
            opening, closing = argument_bounds(token)
            if opening is not None:
                deletion_spans.append((opening, closing if closing is not None else len(text)))

    occurrences = []
    for token in tokens:
        if token.kind != "command" or token.value not in UNCERTAINTY_COMMANDS:
            continue
        opening, closing = argument_bounds(token)
        if opening is None:
            status, end, argument, first, candidate_count = "missing_braced_argument", token.end, "", "", 0
            issues.append(("uncertainty_missing_braced_argument", token.start))
        else:
            status = "balanced" if closing is not None else "unclosed_argument"
            argument_end = closing if closing is not None else len(text)
            end = argument_end + 1 if closing is not None else len(text)
            argument = text[opening + 1:argument_end]
            separators = [
                item.start for item in tokens
                if item.kind == "separator" and opening < item.start < argument_end
                and item.depth == opening_tokens[opening].depth + 1
            ] if token.value == "unsure" else []
            first = text[opening + 1:separators[0]] if separators else argument
            candidate_count = len(separators) + 1
        occurrence = Occurrence(
            ordinal=len(occurrences) + 1, name=token.value, start=token.start, end=end,
            status=status, raw=text[token.start:end], argument=argument,
            first=first, candidate_count=candidate_count,
            inside_deleted=any(left < token.start < right for left, right in deletion_spans),
        )
        occurrences.append(occurrence)
    starts = [0] + [match.end() for match in re.finditer(r"\r\n|\r|\n", text)]
    return Page(path, text, hashlib.sha256(payload).hexdigest(), occurrences, sorted(issues, key=lambda item: item[1]), starts)


def all_positions(text: str, needle: str) -> list[int]:
    positions = []
    position = text.find(needle)
    while position != -1:
        positions.append(position)
        position = text.find(needle, position + 1)
    return positions


def match_anchors(source: Page, occurrence: Occurrence, final: Page, args) -> dict:
    sizes = sorted(
        {args.anchor_chars, args.minimum_anchor}
        | {size for size in (64, 48, 32, 24, 16) if args.minimum_anchor <= size <= args.anchor_chars},
        reverse=True,
    )
    evidence = {}
    for size in sizes:
        left_start = max(0, occurrence.start - size)
        right_end = min(len(source.text), occurrence.end + size)
        left = source.text[left_start:occurrence.start]
        right = source.text[occurrence.end:right_end]
        at_prefix, at_suffix = left_start == 0, right_end == len(source.text)
        left_positions = ([0] if final.text.startswith(left) else []) if at_prefix else all_positions(final.text, left)
        right_positions = ([len(final.text) - len(right)] if final.text.endswith(right) else []) if at_suffix else all_positions(final.text, right)
        evidence = {
            "left_anchor": left, "right_anchor": right,
            "left_anchor_is_page_prefix": "yes" if at_prefix else "no",
            "right_anchor_is_page_suffix": "yes" if at_suffix else "no",
            "anchor_size": size,
        }
        chosen = None
        for left_position in left_positions:
            target_start = left_position + len(left)
            first_right = bisect.bisect_left(right_positions, target_start)
            last_right = bisect.bisect_right(right_positions, target_start + args.max_target_span)
            count = last_right - first_right
            if count > 1 or (count == 1 and chosen is not None):
                return {**evidence, "comparison_status": "ambiguous_exact_anchors"}
            if count == 1:
                chosen = target_start, right_positions[first_right]
        if chosen is not None:
            return {
                **evidence, "comparison_status": "unique_exact_anchors",
                "final_start": chosen[0], "final_end": chosen[1],
                "final_span": final.text[chosen[0]:chosen[1]],
            }
    return {**evidence, "comparison_status": "no_exact_anchor_pair"}


def classify_span(occurrence: Occurrence, matched: dict, final: Page) -> str:
    span = matched["final_span"]
    if span == occurrence.raw:
        return "exact_macro_retained"
    if span == occurrence.first:
        return "exact_first_reading_retained_as_span" if occurrence.name == "unsure" else "exact_illegible_argument_retained_as_span"
    for candidate in final.occurrences:
        if candidate.start == matched["final_start"] and candidate.end == matched["final_end"] and candidate.status == "balanced":
            if candidate.argument == occurrence.first:
                return "exact_first_reading_retained_as_macro_argument" if occurrence.name == "unsure" else "exact_illegible_argument_retained_as_macro_argument"
            if occurrence.name == "unsure" and candidate.name == "unsure":
                return "exact_first_reading_retained_as_final_first_candidate" if candidate.first == occurrence.first else "final_first_candidate_differs"
    return "anchored_span_empty" if span == "" else "anchored_span_differs"


def blank_row(cote: str, scan: str, side: str, c_page: Page | None, final: Page | None) -> dict:
    row = dict.fromkeys(FIELDS, "")
    row.update(cote=cote, scan=scan, side=side, C_sha256=c_page.digest if c_page else "", final_sha256=final.digest if final else "")
    return row


def position_fields(page: Page, start: int, end: int, context: int) -> dict:
    line_index = bisect.bisect_right(page.line_starts, start) - 1
    return {
        "start": start, "end": end, "line": line_index + 1,
        "column": start - page.line_starts[line_index] + 1,
        "context_before": page.text[max(0, start - context):start],
        "context_after": page.text[end:end + context],
    }


def occurrence_row(cote: str, scan: str, side: str, page: Page, occurrence: Occurrence, c_page: Page | None, final: Page | None, context: int) -> dict:
    row = blank_row(cote, scan, side, c_page, final)
    row.update(
        record_type="uncertainty_occurrence", file=str(page.path), occurrence=occurrence.ordinal,
        macro=occurrence.name, parse_status=occurrence.status,
        inside_deleted="yes" if occurrence.inside_deleted else "no",
        raw_macro=occurrence.raw, raw_argument=occurrence.argument,
        first_candidate=occurrence.first, candidate_count=occurrence.candidate_count,
    )
    row.update(position_fields(page, occurrence.start, occurrence.end, context))
    return row


def audit_pair(cote: str, scan: str, args) -> tuple[list[dict], int]:
    filename = f"{cote}_scan{scan}.tex"
    pages: dict[str, Page | None] = {}
    load_issues = []
    for side, directory in (("C", args.c_pages), ("final", args.final_pages)):
        path = directory / filename
        try:
            pages[side] = parse_page(path)
        except (OSError, UnicodeError) as exc:
            pages[side] = None
            load_issues.append((side, path, type(exc).__name__))
    c_page, final = pages["C"], pages["final"]
    rows = []
    issue_count = len(load_issues)
    for side, path, issue in load_issues:
        row = blank_row(cote, scan, side, c_page, final)
        row.update(record_type="file_issue", file=str(path), parse_status="unavailable", detail=issue)
        rows.append(row)
    contained_by: dict[int, list[int]] = {}
    if c_page is not None:
        for occurrence in c_page.occurrences:
            row = occurrence_row(cote, scan, "C", c_page, occurrence, c_page, final, args.context_chars)
            if occurrence.status != "balanced":
                row["comparison_status"] = "source_macro_unparsed"
            elif final is None:
                row["comparison_status"] = "final_page_unavailable"
            else:
                matched = match_anchors(c_page, occurrence, final, args)
                row.update(matched)
                if matched["comparison_status"] == "unique_exact_anchors":
                    row["comparison_status"] = classify_span(occurrence, matched, final)
                    contained = [item.ordinal for item in final.occurrences if matched["final_start"] <= item.start and item.end <= matched["final_end"]]
                    row["final_macro_ordinals"] = ";".join(map(str, contained))
                    for ordinal in contained:
                        contained_by.setdefault(ordinal, []).append(occurrence.ordinal)
            rows.append(row)
    if final is not None:
        for occurrence in final.occurrences:
            row = occurrence_row(cote, scan, "final", final, occurrence, c_page, final, args.context_chars)
            row["comparison_status"] = "final_occurrence"
            row["C_anchor_rows_containing_final_macro"] = ";".join(map(str, contained_by.get(occurrence.ordinal, [])))
            rows.append(row)
    for side, page in pages.items():
        if page is None:
            continue
        for issue, offset in page.issues:
            row = blank_row(cote, scan, side, c_page, final)
            row.update(record_type="lexical_issue", file=str(page.path), parse_status=issue, detail=issue)
            row.update(position_fields(page, offset, min(offset + 1, len(page.text)), args.context_chars))
            rows.append(row)
            issue_count += 1
    return rows, issue_count


def is_within(path: Path, directory: Path) -> bool:
    try:
        path.relative_to(directory)
        return True
    except ValueError:
        return False


def write_tsv(output: Path, rows: list[dict], overwrite: bool) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="", dir=output.parent,
            prefix=f".{output.name}.", suffix=".tmp", delete=False,
        ) as handle:
            temporary = Path(handle.name)
            writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        if overwrite:
            os.replace(temporary, output)
        else:
            os.link(temporary, output)
            temporary.unlink()
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--c-pages", type=Path, required=True)
    parser.add_argument("--final-pages", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="Scratch TSV outside the source and deliverable trees")
    parser.add_argument("--page", action="append", default=[], help="Restrict to a specified cote/scan; repeatable")
    parser.add_argument("--context-chars", type=int, default=120)
    parser.add_argument("--anchor-chars", type=int, default=80)
    parser.add_argument("--minimum-anchor", type=int, default=16)
    parser.add_argument("--max-target-span", type=int, default=8192)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)
    if args.context_chars < 0 or args.max_target_span < 0 or not 1 <= args.minimum_anchor <= args.anchor_chars:
        parser.error("Require context-chars/max-target-span >= 0 and 1 <= minimum-anchor <= anchor-chars")
    requested = set(args.page)
    allowed = {f"{cote}/{scan}" for cote, scan in ORDER}
    if requested - allowed:
        parser.error("Every --page must be one of the 25 specified cote/scan identifiers")
    args.c_pages = args.c_pages.expanduser().resolve()
    args.final_pages = args.final_pages.expanduser().resolve()
    raw_output = args.output.expanduser()
    if raw_output.is_symlink():
        parser.error("The output path must not be a symlink")
    output = raw_output.resolve()
    protected = {Path(__file__).resolve().parents[1]}
    for directory in (args.c_pages, args.final_pages):
        protected.add(directory.parent if directory.name == "pages" else directory)
    if any(is_within(output, directory) for directory in protected):
        parser.error("The output must be outside the source and deliverable trees")
    if output.exists() and (not args.overwrite or not output.is_file()):
        parser.error("The output already exists; a regular scratch file can be replaced with --overwrite")
    rows = []
    issues = 0
    considered = 0
    try:
        for cote, scan in ORDER:
            if requested and f"{cote}/{scan}" not in requested:
                continue
            pair_rows, pair_issues = audit_pair(cote, scan, args)
            rows.extend(pair_rows)
            issues += pair_issues
            considered += 1
        write_tsv(output, rows, args.overwrite)
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print(f"Audit failed: {type(exc).__name__}; no input file was modified.", file=sys.stderr)
        return 1
    counts = Counter(row["comparison_status"] for row in rows if row["side"] == "C" and row["record_type"] == "uncertainty_occurrence")
    print(f"Wrote: {output}")
    print(f"Page pairs considered: {considered}; TSV records: {len(rows)}; file/lexical issues: {issues}")
    for status, count in sorted(counts.items()):
        print(f"{status}: {count}")
    print("Comparisons retain exact text and anchor evidence; the primary reader determines reading significance.")
    return 2 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
