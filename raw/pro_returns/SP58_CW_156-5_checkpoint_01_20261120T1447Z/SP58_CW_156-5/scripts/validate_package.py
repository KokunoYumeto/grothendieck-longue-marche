#!/usr/bin/env python3
"""Mechanically validate the SP58_CW_156-5 transcription package.

This checker does not interpret readings, compare witnesses, open images, or run
TeX.  It checks filenames, exact assembly, lexical structure, table schemas,
controlled categories, inventory coverage, and forbidden packaged artifacts.

Usage:
    python scripts/validate_package.py
    python scripts/validate_package.py --partial
    python scripts/validate_package.py /path/to/SP58_CW_156-5

JSON is written to stdout.  Exit status is 0 when no errors are found, otherwise
1.  Partial mode tolerates missing deliverables and unfinished scan coverage;
it still validates every file and table row that is present.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import io
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PREFIX = "SP58_CW_156-5"
SCANS = tuple(range(34, 50))
EXPECTED_PAGES = {
    scan: f"J156-5-{'05' if scan <= 41 else '06'}_156-5_scan{scan:03d}.tex"
    for scan in SCANS
}
COMBINED_NAME = f"{PREFIX}_transcription.tex"
COLLATION_NAME = f"{PREFIX}_collation.tsv"
INVENTORY_NAME = f"{PREFIX}_inventory.csv"
REQUIRED_FILES = (
    f"{PREFIX}_changes.md",
    COLLATION_NAME,
    f"{PREFIX}_doubts.md",
    INVENTORY_NAME,
    f"{PREFIX}_notes.md",
    "progress.log",
    f"{PREFIX}_sheet_feedback.md",
    f"{PREFIX}_hand_log.md",
    "CHECK_EVENTS.tsv",
)
COLLATION_HEADERS = (
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind",
    "marked_in_H", "confidence",
)
INVENTORY_HEADERS = (
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
SHEET_KINDS = frozenset({
    "text", "reused_typed", "typescript", "letter", "list",
    "cancelled_draft", "cover",
})
INVENTORY_KINDS = frozenset({
    "text", "display", "diagram", "drawing", "margin note",
    "insertion", "deletion",
})
COLLATION_KINDS = frozenset({
    "misread word",
    "misread symbol or index",
    "omission",
    "text not on the page",
    "deletion state (struck given live or live given struck)",
    "insertion or placement",
    "abbreviation expanded or spelling modernised",
    "readable ink left as \\ill{}",
    "drawing or diagram",
    "other",
})
CONFIDENCES = frozenset({"high", "medium", "low"})
MACROS = ("unsure", "illegible", "deleted", "ill", "del")
IMAGE_SUFFIXES = frozenset({
    ".png", ".jpg", ".jpeg", ".jpe", ".jfif", ".tif", ".tiff",
    ".bmp", ".gif", ".webp", ".avif", ".heic", ".heif", ".jp2",
    ".j2k", ".svg", ".ico", ".ppm", ".pgm", ".pbm", ".pnm",
    ".dng", ".cr2", ".nef", ".arw",
})
VERBATIM_ENVIRONMENTS = frozenset({
    "verbatim", "verbatim*", "Verbatim", "BVerbatim", "LVerbatim",
    "lstlisting", "minted", "comment",
})
ENVIRONMENT_ARGUMENT = re.compile(r"\s*\{([A-Za-z0-9@*_.:-]+)\}")
SCAN_ARGUMENT = re.compile(r"\{([0-9]+)\}")
PAGE_FILE_PATTERN = re.compile(r".*_scan[0-9]+\.tex\Z", re.IGNORECASE)
SCAN_VALUE_PATTERN = re.compile(r"(?:scan)?([0-9]+)\Z", re.IGNORECASE)


def lexical_check(source: str) -> dict:
    """Check literal delimiters, ignoring TeX comments and verbatim content.

    This is deliberately a lexer, not a TeX interpreter: macro expansion,
    conditionals, catcode changes, semantic mathematics, and typesetting are
    outside its scope.  Escaped braces, dollars and percent signs are handled.
    """
    newline_offsets = [match.start() for match in re.finditer("\n", source)]
    braces = []
    environments = []
    math = []
    markers = []
    counts = Counter({name: 0 for name in MACROS})
    issues = []
    cotefile_count = 0

    def location(offset: int) -> dict:
        line_index = bisect.bisect_left(newline_offsets, offset)
        previous_newline = newline_offsets[line_index - 1] if line_index else -1
        return {"line": line_index + 1, "column": offset - previous_newline}

    def issue(code: str, offset: int, message: str) -> None:
        issues.append({"code": code, "message": message, **location(offset)})

    def open_math(token: str, offset: int) -> None:
        if math:
            issue("nested_math_delimiter", offset,
                  f"Opened {token!r} before closing {math[-1][0]!r}.")
        math.append((token, offset))

    def close_math(expected: str, token: str, offset: int) -> None:
        if not math:
            issue("unexpected_math_close", offset,
                  f"Closing delimiter {token!r} has no opener.")
        elif math[-1][0] != expected:
            issue("mismatched_math_delimiter", offset,
                  f"Closing delimiter {token!r} does not match {math[-1][0]!r}.")
        else:
            math.pop()

    i = 0
    length = len(source)
    while i < length:
        char = source[i]
        if char == "%":
            newline = source.find("\n", i)
            i = length if newline < 0 else newline
            continue
        if char == "\\":
            start = i
            i += 1
            if i == length:
                issue("trailing_backslash", start,
                      "A final backslash has no control word or symbol.")
                break
            if source[i].isalpha() or source[i] == "@":
                end = i + 1
                while end < length and (source[end].isalpha() or source[end] == "@"):
                    end += 1
                name = source[i:end]
                i = end
                if name in counts:
                    counts[name] += 1
                if name == "cotefile":
                    cotefile_count += 1
                if name == "scanpage":
                    argument = SCAN_ARGUMENT.match(source, i)
                    if argument is None:
                        issue("malformed_scan_marker", start,
                              "Expected the literal form \\scanpage{integer}.")
                    else:
                        markers.append({"scan": int(argument.group(1)),
                                        **location(start)})
                if name == "verb":
                    if i < length and source[i] == "*":
                        i += 1
                    if i >= length or source[i].isspace():
                        issue("malformed_verb", start,
                              "A verb command needs a non-whitespace delimiter.")
                        continue
                    delimiter = source[i]
                    close = source.find(delimiter, i + 1)
                    newline = source.find("\n", i + 1)
                    if close < 0 or (newline >= 0 and newline < close):
                        issue("unclosed_verb", start,
                              "A verb command is not closed on the same line.")
                        i = length if newline < 0 else newline
                    else:
                        i = close + 1
                    continue
                if name in {"begin", "end"}:
                    argument = ENVIRONMENT_ARGUMENT.match(source, i)
                    if argument is None:
                        issue("malformed_environment", start,
                              f"The {name} command lacks a simple braced environment name.")
                        continue
                    environment = argument.group(1)
                    i = argument.end()
                    if name == "begin":
                        if environment in VERBATIM_ENVIRONMENTS:
                            terminator = re.compile(
                                r"\\end\s*\{" + re.escape(environment) + r"\}"
                            ).search(source, i)
                            if terminator is None:
                                issue("unclosed_environment", start,
                                      f"Environment {environment!r} is not closed.")
                                i = length
                            else:
                                i = terminator.end()
                        else:
                            environments.append((environment, start))
                    elif not environments:
                        issue("unexpected_environment_end", start,
                              f"Environment {environment!r} ends without a begin.")
                    elif environments[-1][0] != environment:
                        issue("mismatched_environment", start,
                              f"Environment {environment!r} ends while "
                              f"{environments[-1][0]!r} remains open.")
                    else:
                        environments.pop()
                continue
            symbol = source[i]
            i += 1
            if symbol in {"(", "["}:
                open_math("\\" + symbol, start)
            elif symbol == ")":
                close_math("\\(", "\\)", start)
            elif symbol == "]":
                close_math("\\[", "\\]", start)
            continue
        if char == "{":
            braces.append(i)
        elif char == "}":
            if braces:
                braces.pop()
            else:
                issue("unexpected_closing_brace", i,
                      "A closing brace has no matching opening brace.")
        elif char == "$":
            token = "$$" if source.startswith("$$", i) else "$"
            if math and math[-1][0] == token:
                math.pop()
            elif math:
                issue("mismatched_math_delimiter", i,
                      f"Dollar delimiter {token!r} occurs while {math[-1][0]!r} is open.")
            else:
                math.append((token, i))
            i += len(token)
            continue
        i += 1

    for offset in braces:
        issue("unclosed_brace", offset, "An opening brace has no closing brace.")
    for environment, offset in environments:
        issue("unclosed_environment", offset,
              f"Environment {environment!r} is not closed.")
    for token, offset in math:
        issue("unclosed_math_delimiter", offset,
              f"Math delimiter {token!r} is not closed.")
    return {
        "issues": sorted(issues, key=lambda entry: (entry["line"], entry["column"])),
        "scan_markers": markers,
        "macro_counts": dict(counts),
        "cotefile_count": cotefile_count,
    }


def is_cotefile_header(prefix: str) -> bool:
    """Accept whitespace surrounding exactly one balanced cotefile macro."""
    match = re.match(r"\s*\\cotefile\s*\{", prefix)
    if match is None:
        return False
    depth = 1
    i = match.end()
    while i < len(prefix):
        if prefix[i] == "\\":
            i += 2
            continue
        if prefix[i] == "{":
            depth += 1
        elif prefix[i] == "}":
            depth -= 1
            if depth == 0:
                return prefix[i + 1:].strip() == ""
        elif prefix[i] == "%":
            return False
        i += 1
    return False


class Validator:
    def __init__(self, root: Path, partial: bool) -> None:
        self.root = root
        self.partial = partial
        self.errors = []
        self.warnings = []
        self.pages = []
        self.page_data = {}
        self.page_lexical = {}
        self.inventory_scans = set()
        self.table_rows = {}
        self.combined_data = None
        self.combined_lexical = None
        self.combined_exact = None
        self.cotefile_header_added = False

    def relative(self, path: Path) -> str:
        try:
            return path.relative_to(self.root).as_posix()
        except ValueError:
            return str(path)

    def add(self, code: str, path: Path, message: str,
            warning: bool = False, **details) -> None:
        target = self.warnings if warning else self.errors
        target.append({"code": code, "file": self.relative(path),
                       "message": message, **details})

    def read(self, path: Path, *, required: bool = True):
        if not path.is_file():
            if required:
                self.add("missing_file", path, "Required file is missing.",
                         warning=self.partial)
            return None
        try:
            data = path.read_bytes()
        except OSError as error:
            self.add("unreadable_file", path, str(error))
            return None
        if not data.strip():
            self.add("empty_file", path, "Required file is empty.")
        return data

    def decode(self, path: Path, data: bytes, *, table: bool = False):
        try:
            return data.decode("utf-8-sig" if table else "utf-8")
        except UnicodeDecodeError as error:
            self.add("invalid_utf8", path,
                     f"File is not valid UTF-8 at byte {error.start}.")
            return None

    def check_tex(self, path: Path, data: bytes):
        source = self.decode(path, data)
        if source is None:
            return None
        result = lexical_check(source)
        for issue in result["issues"]:
            self.add(issue["code"], path, issue["message"],
                     line=issue["line"], column=issue["column"])
        return result

    def check_pages(self) -> None:
        directory = self.root / "pages"
        for scan, name in EXPECTED_PAGES.items():
            path = directory / name
            data = self.read(path)
            if data is None:
                self.pages.append({"scan": scan, "file": self.relative(path),
                                   "present": False})
                continue
            self.page_data[scan] = data
            lexical = self.check_tex(path, data)
            entry = {"scan": scan, "file": self.relative(path),
                     "present": True, "bytes": len(data)}
            if lexical is not None:
                self.page_lexical[scan] = lexical
                found = [marker["scan"] for marker in lexical["scan_markers"]]
                entry.update({"scan_markers": found,
                              "macro_counts": lexical["macro_counts"],
                              "lexical_error_count": len(lexical["issues"])})
                if found != [scan]:
                    self.add("page_scan_markers", path,
                             f"Expected exactly one \\scanpage{{{scan}}} marker.",
                             found=found)
            self.pages.append(entry)
        if directory.is_dir():
            names = set(EXPECTED_PAGES.values())
            for path in sorted(directory.rglob("*")):
                if path.is_file() and PAGE_FILE_PATTERN.fullmatch(path.name):
                    if path.parent != directory or path.name not in names:
                        self.add("unexpected_page_file", path,
                                 "Page filename or location is outside the expected 16-file set.")

    def check_combined(self) -> None:
        path = self.root / COMBINED_NAME
        data = self.read(path)
        if data is None:
            return
        self.combined_data = data
        self.combined_lexical = self.check_tex(path, data)
        if self.combined_lexical is not None:
            found = [marker["scan"]
                     for marker in self.combined_lexical["scan_markers"]]
            if not self.partial or len(self.page_data) == len(SCANS):
                if found != list(SCANS):
                    self.add("combined_scan_markers", path,
                             "Combined markers must occur exactly once in order from 34 through 49.",
                             found=found)
            elif found != sorted(set(found)) or any(scan not in SCANS for scan in found):
                self.add("combined_scan_markers", path,
                         "Present combined markers must be distinct, increasing, and within 34–49.",
                         found=found)
        if len(self.page_data) != len(SCANS):
            self.add("assembly_check_skipped", path,
                     "Exact assembly cannot be checked until all 16 page files are present.",
                     warning=True)
            return
        expected = b"".join(self.page_data[scan] for scan in SCANS)
        self.combined_exact = data == expected
        if not self.combined_exact and expected and data.endswith(expected):
            first_page = self.page_lexical.get(SCANS[0])
            prefix = data[:-len(expected)]
            try:
                header = prefix.decode("utf-8")
            except UnicodeDecodeError:
                header = ""
            if first_page is not None and first_page["cotefile_count"] == 0:
                if is_cotefile_header(header):
                    self.combined_exact = True
                    self.cotefile_header_added = True
        if not self.combined_exact:
            limit = min(len(data), len(expected))
            mismatch = next((i for i in range(limit) if data[i] != expected[i]), limit)
            self.add("combined_not_exact_concatenation", path,
                     "Combined bytes differ from the ordered page concatenation; only a leading "
                     "cotefile header absent from page 34 is permitted.",
                     first_difference_byte=mismatch,
                     combined_bytes=len(data), page_bytes=len(expected))

    def read_table(self, path: Path, headers: tuple, delimiter: str):
        data = self.read(path, required=False)
        if data is None:
            return None
        source = self.decode(path, data, table=True)
        if source is None:
            return None
        rows = []
        try:
            reader = csv.reader(io.StringIO(source, newline=""),
                                delimiter=delimiter, strict=True)
            actual_headers = next(reader, [])
            if actual_headers != list(headers):
                self.add("table_headers", path,
                         "Table headers do not match the required names and order.",
                         expected=list(headers), found=actual_headers)
                return None
            for row in reader:
                line = reader.line_num
                if not row or all(not value.strip() for value in row):
                    continue
                if len(row) != len(headers):
                    self.add("table_row_width", path,
                             f"Expected {len(headers)} columns; found {len(row)}.", line=line)
                    continue
                rows.append((line, dict(zip(headers, row))))
        except csv.Error as error:
            self.add("invalid_delimited_table", path, str(error))
            return None
        self.table_rows[path.name] = len(rows)
        return rows

    def category(self, path: Path, line: int, row: dict,
                 field: str, allowed: frozenset) -> None:
        value = row[field].strip()
        if value not in allowed:
            self.add("invalid_category", path,
                     f"Column {field!r} has an unrecognized category.",
                     line=line, field=field, found=value, allowed=sorted(allowed))

    def scan_value(self, path: Path, line: int, value: str, field: str):
        match = SCAN_VALUE_PATTERN.fullmatch(value.strip())
        if match is None or int(match.group(1)) not in SCANS:
            self.add("invalid_scan_value", path,
                     f"Column {field!r} must identify a scan from 34 through 49.",
                     line=line, field=field)
            return None
        return int(match.group(1))

    def check_tables(self) -> None:
        inventory_path = self.root / INVENTORY_NAME
        rows = self.read_table(inventory_path, INVENTORY_HEADERS, ",")
        if rows is not None:
            for line, row in rows:
                scan = self.scan_value(inventory_path, line, row["scan"], "scan")
                if scan is not None:
                    self.inventory_scans.add(scan)
                self.category(inventory_path, line, row, "sheet_kind", SHEET_KINDS)
                self.category(inventory_path, line, row, "kind", INVENTORY_KINDS)
                self.category(inventory_path, line, row, "transcribed", frozenset({"yes"}))
            missing = sorted(set(SCANS) - self.inventory_scans)
            if missing:
                self.add("inventory_missing_scans", inventory_path,
                         "Inventory lacks entries for expected scans.",
                         warning=self.partial, missing=missing)
        collation_path = self.root / COLLATION_NAME
        rows = self.read_table(collation_path, COLLATION_HEADERS, "\t")
        if rows is not None:
            for line, row in rows:
                self.scan_value(collation_path, line, row["our_scan"], "our_scan")
                self.category(collation_path, line, row, "kind", COLLATION_KINDS)
                self.category(collation_path, line, row, "confidence", CONFIDENCES)
                self.category(collation_path, line, row, "marked_in_H",
                              frozenset({"yes", "no"}))

    def check_required_files(self) -> None:
        for name in REQUIRED_FILES:
            self.read(self.root / name)

    def check_forbidden_artifacts(self) -> None:
        try:
            paths = sorted(self.root.rglob("*"))
        except OSError as error:
            self.add("package_walk_failed", self.root, str(error))
            return
        for path in paths:
            if not path.is_file():
                continue
            suffix = path.suffix.lower()
            if suffix in IMAGE_SUFFIXES:
                self.add("packaged_image", path,
                         "Image artifacts must not be included in the deliverable directory.")
            elif suffix == ".zip":
                self.add("nested_zip", path,
                         "ZIP archives, including prior checkpoints, must not be nested in the package.")

    def run(self) -> dict:
        if not self.root.is_dir():
            self.add("missing_directory", self.root, "Package directory does not exist.")
        else:
            self.check_pages()
            self.check_combined()
            self.check_required_files()
            self.check_tables()
            self.check_forbidden_artifacts()
        totals = Counter({name: 0 for name in MACROS})
        for result in self.page_lexical.values():
            totals.update(result["macro_counts"])
        combined_counts = (
            self.combined_lexical["macro_counts"]
            if self.combined_lexical is not None else None
        )
        return {
            "package": PREFIX,
            "directory": str(self.root),
            "checked_at_utc": datetime.now(timezone.utc).isoformat(),
            "mode": "partial" if self.partial else "complete",
            "ok": not self.errors,
            "scope": "Mechanical checks only; no reading judgments or TeX compilation.",
            "summary": {
                "expected_page_count": len(SCANS),
                "present_page_count": len(self.page_data),
                "combined_exact_concatenation": self.combined_exact,
                "permitted_cotefile_header_added": self.cotefile_header_added,
                "inventory_scans": sorted(self.inventory_scans),
                "table_data_rows": self.table_rows,
                "error_count": len(self.errors),
                "warning_count": len(self.warnings),
            },
            "macro_counts": {
                "page_totals": dict(totals),
                "combined": combined_counts,
                "note": "Literal control-word counts; ill and del are reported separately as aliases.",
            },
            "pages": self.pages,
            "errors": self.errors,
            "warnings": self.warnings,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent.parent,
                        help="package root; defaults to this script's parent directory")
    parser.add_argument("--partial", action="store_true",
                        help="tolerate missing files and incomplete inventory coverage")
    args = parser.parse_args()
    report = Validator(args.directory.expanduser().resolve(), args.partial).run()
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
