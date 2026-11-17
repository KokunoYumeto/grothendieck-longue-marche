#!/usr/bin/env python3
"""Mechanically validate the MPL_83_178-222 transcription package.

This program does not assess readings, mathematical correctness, completeness
against images, or the fidelity of drawings.  It never opens scans or context
sources.  It reads only page fragments, the combined fragment, and the inventory.
Use --partial while the page sequence is still being written.

The lightweight LaTeX check understands comments and escaped characters, but
does not expand macros.  Literal/verbatim environments are outside its scope.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


STEM = "MPL_83_178-222"
EXPECTED = tuple(n for n in range(178, 223) if n not in {182, 206})
HEADERS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
PAGE_NAME = re.compile(rf"{re.escape(STEM)}_83_scan(\d{{3}})\.tex\Z")
COMMAND = re.compile(r"\\([A-Za-z@]+|[^\n])")
SCANPAGE = re.compile(r"\\scanpage\s*\{\s*(\d+)\s*\}")
COTEFILE = re.compile(r"\\cotefile\s*\{\s*(\d+)\s*\}")
IMAGE_COMMANDS = {
    "includegraphics", "epsfig", "psfig", "pgfimage", "includepdf", "includesvg",
}
PREAMBLE_COMMANDS = {
    "documentclass", "documentstyle", "usepackage", "RequirePackage",
    "newcommand", "renewcommand", "providecommand", "DeclareRobustCommand",
    "newenvironment", "renewenvironment", "DeclareMathOperator",
    "def", "gdef", "edef", "xdef",
}
# A deliberately narrow warning list, not an attempted list of all LaTeX macros.
SUSPECT_STATE_COMMANDS = {
    "unclear", "illeg", "struckout", "strikethrough", "strikeout", "sout",
    "added", "addition", "marginal", "marginnote", "sourcepage",
    "archivepage", "manuscriptpage",
}
EDITORIAL_ARGUMENT_COMMANDS = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
    "uline", "uuline", "diagram", "figure", "unsure", "illegible",
}


@dataclass
class Issue:
    level: str
    path: str
    message: str
    line: int | None = None


class Validator:
    def __init__(self, root: Path, partial: bool = False):
        self.root = root
        self.partial = partial
        self.issues: list[Issue] = []
        self.checks = 0
        self.page_sources: dict[int, str] = {}

    def issue(self, level: str, path: Path, message: str, line: int | None = None):
        try:
            label = str(path.relative_to(self.root))
        except ValueError:
            label = str(path)
        self.issues.append(Issue(level, label, message, line))

    def check(self, condition: bool, path: Path, message: str, line: int | None = None):
        self.checks += 1
        if not condition:
            self.issue("error", path, message, line)

    def read_text(self, path: Path) -> str | None:
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.issue("error", path, f"Cannot read UTF-8 text: {exc}")
            return None

    def validate_tex(self, path: Path, source: str) -> str:
        clean = remove_comments(source)
        starts = [0] + [m.end() for m in re.finditer("\n", clean)]

        def line_at(offset: int) -> int:
            return bisect.bisect_right(starts, offset)

        braces: list[int] = []
        environments: list[tuple[str, int]] = []
        offset = 0
        while offset < len(clean):
            char = clean[offset]
            if char == "\\":
                match = COMMAND.match(clean, offset)
                if match is None:
                    self.issue("warning", path, "Trailing or isolated backslash.", line_at(offset))
                    offset += 1
                    continue
                name = match.group(1)
                if name in EDITORIAL_ARGUMENT_COMMANDS:
                    following = match.end()
                    while following < len(clean) and clean[following].isspace():
                        following += 1
                    self.check(
                        following < len(clean) and clean[following] == "{", path,
                        f"Editorial macro \\{name} requires a braced argument.",
                        line_at(offset),
                    )
                if name in IMAGE_COMMANDS:
                    self.issue("error", path, f"Embedded image command \\{name} is forbidden.", line_at(offset))
                if name in PREAMBLE_COMMANDS:
                    self.issue("error", path, f"Preamble or macro-definition command \\{name} in fragment.", line_at(offset))
                if name in SUSPECT_STATE_COMMANDS:
                    self.issue("warning", path, f"Review \\{name}: it may be an unsupported state-marking macro.", line_at(offset))
                if name in {"verb", "Verbatim", "lstinline"}:
                    self.issue("warning", path, "Literal/verbatim content is outside this parser's scope.", line_at(offset))
                if name in {"begin", "end"}:
                    arg = re.match(r"\s*\{([^{}]*)\}", clean[match.end():])
                    if arg is None:
                        self.issue("error", path, f"\\{name} has no simple braced environment name.", line_at(offset))
                    else:
                        env = arg.group(1).strip()
                        if env == "document":
                            self.issue("error", path, "Document environment is forbidden in a fragment.", line_at(offset))
                        if env in {"verbatim", "Verbatim", "lstlisting", "minted"}:
                            self.issue("warning", path, "Literal/verbatim environment is outside this parser's scope.", line_at(offset))
                        if name == "begin":
                            environments.append((env, offset))
                        elif not environments:
                            self.issue("error", path, f"Unmatched \\end{{{env}}}.", line_at(offset))
                        else:
                            opening, where = environments.pop()
                            self.check(
                                opening == env, path,
                                f"\\end{{{env}}} mismatches \\begin{{{opening}}} from line {line_at(where)}.",
                                line_at(offset),
                            )
                offset = match.end()
                continue
            if char == "{":
                braces.append(offset)
            elif char == "}":
                if braces:
                    braces.pop()
                else:
                    self.issue("error", path, "Unmatched closing brace.", line_at(offset))
            offset += 1
        self.checks += 2
        for where in braces:
            self.issue("error", path, "Unclosed opening brace.", line_at(where))
        for env, where in environments:
            self.issue("error", path, f"Unclosed \\begin{{{env}}}.", line_at(where))
        return clean

    def validate_pages(self):
        folder = self.root / "pages"
        self.check(folder.is_dir(), folder, "Missing pages directory.")
        if not folder.is_dir():
            return
        for path in sorted(folder.glob("*.tex")):
            match = PAGE_NAME.fullmatch(path.name)
            self.check(match is not None, path, "Unexpected page-fragment filename.")
            if match is None:
                continue
            scan = int(match.group(1))
            self.check(scan in EXPECTED, path, f"Unexpected scan {scan}; blank scans 182 and 206 are excluded.")
            if scan not in EXPECTED:
                continue
            source = self.read_text(path)
            if source is None:
                continue
            self.page_sources[scan] = source
            clean = self.validate_tex(path, source)
            names = [m.group(1) for m in COMMAND.finditer(clean)]
            values = [int(m.group(1)) for m in SCANPAGE.finditer(clean)]
            self.check(names.count("scanpage") == 1, path, "Page fragment must contain exactly one \\scanpage command.")
            self.check(values == [scan], path, f"Expected the sole page marker \\scanpage{{{scan}}}; found {values}.")
        missing = sorted(set(EXPECTED) - self.page_sources.keys())
        if missing:
            message = "Missing page fragments: " + ", ".join(map(str, missing))
            if self.partial:
                self.issue("warning", folder, message + " (allowed by --partial).")
            else:
                self.issue("error", folder, message)
        self.checks += 1

    def validate_inventory(self):
        path = self.root / f"{STEM}_inventory.csv"
        if not path.is_file():
            if self.partial and not self.page_sources:
                self.issue("warning", path, "Inventory not yet present (allowed because there are no page fragments).")
            else:
                self.issue("error", path, "Missing inventory.")
            return
        try:
            with path.open(encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream)
                self.check(reader.fieldnames == HEADERS, path, f"Inventory header must be exactly {HEADERS}.", 1)
                if reader.fieldnames != HEADERS:
                    return
                seen_elements: set[tuple[str, str, str]] = set()
                covered: set[int] = set()
                for row in reader:
                    line = reader.line_num
                    self.check(None not in row, path, "Inventory row has more fields than the header.", line)
                    for key in HEADERS:
                        self.check(bool((row.get(key) or "").strip()), path, f"Empty inventory field: {key}.", line)
                    self.check(row["cote"] == "83", path, "Inventory cote must be 83.", line)
                    scan_text = (row["scan"] or "").strip()
                    scan = int(scan_text) if scan_text.isdecimal() else -1
                    self.check(scan in EXPECTED, path, f"Unexpected inventory scan {scan_text!r}.", line)
                    self.check(scan in self.page_sources, path, f"Inventory scan {scan_text!r} has no successfully read page file.", line)
                    covered.add(scan)
                    self.check(row["sheet_kind"] in SHEET_KINDS, path, f"Invalid sheet_kind {row['sheet_kind']!r}.", line)
                    self.check(row["kind"] in ELEMENT_KINDS, path, f"Invalid element kind {row['kind']!r}.", line)
                    self.check(row["transcribed"] == "yes", path, "Every inventory row must have transcribed=yes.", line)
                    key = (row["cote"], row["scan"], row["element"])
                    self.check(key not in seen_elements, path, f"Duplicate element identifier {key!r}.", line)
                    seen_elements.add(key)
                for scan in sorted(self.page_sources):
                    self.check(scan in covered, path, f"Scan {scan} has no inventory elements.")
        except (OSError, UnicodeError, csv.Error) as exc:
            self.issue("error", path, f"Cannot read CSV inventory: {exc}")

    def validate_combined(self):
        path = self.root / f"{STEM}_transcription.tex"
        if not path.is_file():
            self.issue("warning" if self.partial else "error", path,
                       "Combined transcription not present" + (" (allowed by --partial)." if self.partial else "."))
            return
        source = self.read_text(path)
        if source is None:
            return
        clean = self.validate_tex(path, source)
        self.check(re.match(r"\s*\\cotefile\s*\{\s*83\s*\}", clean) is not None,
                   path, "Combined fragment must start with \\cotefile{83}, ignoring whitespace/comments.")
        cote_values = [int(m.group(1)) for m in COTEFILE.finditer(clean)]
        self.check(cote_values == [83], path, f"Expected exactly one \\cotefile{{83}}; found {cote_values}.")
        values = [int(m.group(1)) for m in SCANPAGE.finditer(clean)]
        expected = sorted(self.page_sources) if self.partial else list(EXPECTED)
        self.check(values == expected, path, f"Combined scan sequence must be {expected}; found {values}.")
        parts = [self.page_sources[n].strip() for n in sorted(self.page_sources)]
        if parts:
            first_clean = remove_comments(parts[0])
            if re.match(r"\s*\\cotefile\s*\{\s*83\s*\}", first_clean) is None:
                parts.insert(0, r"\cotefile{83}")
            # Only whitespace at page boundaries is flexible; page content is exact.
            pattern = r"\s*" + r"\s*".join(re.escape(part) for part in parts) + r"\s*"
            self.check(re.fullmatch(pattern, source) is not None, path,
                       "Combined source differs from the ordered page fragments (only boundary whitespace may differ).")

    def run(self) -> dict:
        if not self.root.is_dir():
            self.issue("error", self.root, "Package directory does not exist.")
        else:
            self.validate_pages()
            self.validate_inventory()
            self.validate_combined()
        errors = sum(issue.level == "error" for issue in self.issues)
        warnings = sum(issue.level == "warning" for issue in self.issues)
        return {
            "ok": errors == 0,
            "partial": self.partial,
            "package": str(self.root),
            "pages_read": len(self.page_sources),
            "expected_pages": len(EXPECTED),
            "checks": self.checks,
            "errors": errors,
            "warnings": warnings,
            "issues": [asdict(issue) for issue in self.issues],
        }


def remove_comments(source: str) -> str:
    """Blank unescaped % comments, preserving offsets, line breaks, and escapes."""
    result = list(source)
    offset = 0
    while offset < len(source):
        if source[offset] == "\\":
            # A control symbol such as \\%, \\{, or \\\\ consumes its next byte.
            offset += 2
        elif source[offset] == "%":
            while offset < len(source) and source[offset] != "\n":
                result[offset] = " "
                offset += 1
        else:
            offset += 1
    return "".join(result)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="Package directory (default: parent of this script's directory).")
    parser.add_argument("--partial", action="store_true", help="Allow page fragments and the combined fragment not yet written.")
    parser.add_argument("--json", action="store_true", help="Print a JSON report instead of text.")
    args = parser.parse_args()
    result = Validator(args.package.resolve(), partial=args.partial).run()
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        status = "PASS" if result["ok"] else "FAIL"
        print(f"{status}: {result['pages_read']}/{result['expected_pages']} pages; "
              f"{result['checks']} checks; {result['errors']} errors; {result['warnings']} warnings.")
        for issue in result["issues"]:
            location = issue["path"] + (f":{issue['line']}" if issue["line"] else "")
            print(f"{issue['level'].upper()}: {location}: {issue['message']}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
