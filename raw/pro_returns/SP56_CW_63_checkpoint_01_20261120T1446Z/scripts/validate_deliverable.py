#!/usr/bin/env python3
"""Validate the *structure* of the SP56_CW_63 deliverable, using stdlib only.

Usage:
    python validate_deliverable.py OUTPUT_DIR
    python validate_deliverable.py OUTPUT_DIR --zip FINAL.zip --format text

This program does not interpret a transcription, consult source material, run
other scripts, compile TeX, or extract an archive.  It writes its report only to
stdout.  Exit status is 0 for passing checks, 1 for a failed check, and 2 for an
argument error.  A ZIP check is optional and is only run when --zip is supplied.

The combined-file convention is deliberately byte-exact:
    b"\\cotefile{63}\\n" + b"".join(ordered_page_bytes)

Page order is the EXPECTED_SCANS sequence below; the scan for each page file is
obtained from its one literal \\scanpage{NUMBER} command.  The inventory header is
CSV; the collation and event headers are TSV.  Header order is significant.

Allowed optional documentation consists of README.md, PREAMBLE.tex,
SP56_CW_63_audit.md, scripts/**/*.py, records/**/*.json, and root-level reports
whose name starts with validation or SP56_CW_63_validation and ends in .json,
.txt, .md, .tsv, or .log.  Matching is case-sensitive except for report names.
The optional PREAMBLE.tex macro-only policy requires a separate human check.
"""

from __future__ import annotations

import argparse
import bisect
import collections
import csv
import io
import json
import re
import stat
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


EXPECTED_SCANS = (
    53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64,
    78, 80, 81, 83, 84, 85, 87, 88, 89, 90, 91, 92, 93, 94,
)
COMBINED = "SP56_CW_63_transcription.tex"
INVENTORY = "SP56_CW_63_inventory.csv"
COLLATION = "SP56_CW_63_collation.tsv"
EVENTS = "CHECK_EVENTS.tsv"
REQUIRED_FILES = (
    COMBINED,
    "SP56_CW_63_changes.md",
    COLLATION,
    "SP56_CW_63_doubts.md",
    INVENTORY,
    "SP56_CW_63_notes.md",
    "SP56_CW_63_sheet_feedback.md",
    "SP56_CW_63_hand_log.md",
    "progress.log",
    EVENTS,
)
OPTIONAL_FILES = {"SP56_CW_63_audit.md", "README.md", "PREAMBLE.tex"}
INVENTORY_COLUMNS = (
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
COLLATION_COLUMNS = (
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H",
    "confidence",
)
EVENT_COLUMNS = ("statement_id", "date", "who", "type", "outcome")
REPORT_NAME_RE = re.compile(
    r"(?:SP56_CW_63_)?validation[A-Za-z0-9_.-]*\.(?:json|txt|md|tsv|log)\Z",
    re.IGNORECASE,
)
FORBIDDEN_ARCHIVE_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".gif", ".webp",
    ".bmp", ".pdf", ".jp2", ".j2k", ".heic", ".heif", ".svg",
    ".avif", ".ico", ".psd", ".eps", ".zip", ".7z", ".rar",
    ".tar", ".gz", ".bz2", ".xz", ".zst",
}
LIMITATIONS = [
    "Structural checks only: source scans, witness readings, transcription "
    "accuracy, paleography, omissions, line mappings, and editorial judgments "
    "are not assessed.",
    "No TeX compilation or macro expansion is performed. TeX checks assume "
    "ordinary backslash escapes and percent comments with unchanged catcodes; "
    "verbatim regions, conditional TeX, and macro-generated delimiters are "
    "not interpreted.",
    "CHECK_EVENTS.tsv values are checked for the specified header, rectangular "
    "rows, and nonempty fields; the reported events are not independently "
    "verified and date or outcome meanings are not judged.",
    "ZIP checks establish allowed paths and byte agreement with output files; "
    "they cannot identify source material renamed or encoded within an "
    "otherwise allowed file.",
    "The optional PREAMBLE.tex macro-definitions-only policy is not evaluated.",
]


@dataclass(frozen=True)
class Token:
    kind: str
    value: str
    offset: int
    end: int


def mask_comments(source: str) -> str:
    """Replace ordinary TeX comments with spaces, preserving all offsets.

    A backslash consumes the following control symbol or control word.  This
    correctly distinguishes escaped percent from percent after a double
    backslash without treating every preceding backslash as an escape.
    """
    chars = list(source)
    i = 0
    while i < len(source):
        if source[i] == "\\":
            i += 1
            if i < len(source) and (source[i].isascii() and source[i].isalpha()):
                while i < len(source) and (
                    source[i].isascii() and source[i].isalpha()
                ):
                    i += 1
            elif i < len(source):
                i += 1
        elif source[i] == "%":
            while i < len(source) and source[i] not in "\r\n":
                chars[i] = " "
                i += 1
        else:
            i += 1
    return "".join(chars)


def tex_tokens(masked: str) -> Iterable[Token]:
    i = 0
    while i < len(masked):
        start = i
        char = masked[i]
        if char == "\\":
            i += 1
            if i == len(masked):
                yield Token("trailing_escape", "", start, i)
            elif masked[i].isascii() and masked[i].isalpha():
                word_start = i
                while i < len(masked) and (
                    masked[i].isascii() and masked[i].isalpha()
                ):
                    i += 1
                yield Token("command", masked[word_start:i], start, i)
            else:
                i += 1
                yield Token("command", masked[i - 1], start, i)
        elif char in "{}":
            i += 1
            yield Token("brace", char, start, i)
        elif char == "$":
            i += 1
            if i < len(masked) and masked[i] == "$":
                i += 1
            yield Token("math", masked[start:i], start, i)
        else:
            i += 1


def literal_group(masked: str, offset: int) -> str | None:
    """Read a simple, literal brace argument without executing TeX."""
    match = re.match(r"\s*\{([^{}]*)\}", masked[offset:])
    return match.group(1).strip() if match else None


def inspect_tex(source: str) -> dict[str, Any]:
    """Return structural diagnostics only; never return source line contents."""
    masked = mask_comments(source)
    tokens = list(tex_tokens(masked))
    newlines = [i for i, char in enumerate(source) if char == "\n"]
    errors: list[str] = []
    braces: list[int] = []
    environments: list[tuple[str, int]] = []
    math: tuple[str, int] | None = None
    scan_markers: list[int | None] = []
    cote_markers: list[str | None] = []
    counts: collections.Counter[str] = collections.Counter()

    def location(offset: int) -> str:
        index = bisect.bisect_left(newlines, offset)
        previous_newline = newlines[index - 1] if index else -1
        return f"line {index + 1}, column {offset - previous_newline}"

    def math_open(kind: str, token: Token) -> None:
        nonlocal math
        if math is not None:
            errors.append(
                f"Nested math opener {kind!r} at {location(token.offset)}; "
                f"{math[0]!r} opened at {location(math[1])} is still open."
            )
        else:
            math = (kind, token.offset)

    def math_close(kind: str, token: Token) -> None:
        nonlocal math
        if math is None:
            errors.append(f"Math closer {kind!r} without an opener at {location(token.offset)}.")
        elif math[0] != kind:
            errors.append(
                f"Mismatched math closer {kind!r} at {location(token.offset)}; "
                f"open delimiter is {math[0]!r} at {location(math[1])}."
            )
        else:
            math = None

    for token in tokens:
        if token.kind == "trailing_escape":
            errors.append(f"Trailing backslash at {location(token.offset)}.")
        elif token.kind == "brace":
            counts["unescaped_brace_tokens"] += 1
            if token.value == "{":
                braces.append(token.offset)
            elif braces:
                braces.pop()
            else:
                errors.append(f"Unmatched closing brace at {location(token.offset)}.")
        elif token.kind == "math":
            counts["dollar_tokens" if token.value == "$" else "double_dollar_tokens"] += 1
            if math is None:
                math = (token.value, token.offset)
            elif math[0] == token.value:
                math = None
            else:
                errors.append(
                    f"Dollar delimiter {token.value!r} within {math[0]!r} math "
                    f"at {location(token.offset)}."
                )
        elif token.kind == "command":
            command = token.value
            if command == "[":
                counts["display_bracket_openers"] += 1
                math_open("\\[...\\]", token)
            elif command == "]":
                counts["display_bracket_closers"] += 1
                math_close("\\[...\\]", token)
            elif command == "(":
                counts["inline_parenthesis_openers"] += 1
                math_open("\\(...\\)", token)
            elif command == ")":
                counts["inline_parenthesis_closers"] += 1
                math_close("\\(...\\)", token)
            elif command in {"begin", "end"}:
                environment = literal_group(masked, token.end)
                if not environment or "\\" in environment:
                    errors.append(
                        f"\\{command} has no simple literal environment name "
                        f"at {location(token.offset)}."
                    )
                elif command == "begin":
                    environments.append((environment, token.offset))
                    counts["environment_openers"] += 1
                elif not environments:
                    errors.append(
                        f"Environment end {environment!r} without a begin "
                        f"at {location(token.offset)}."
                    )
                else:
                    expected, opened_at = environments.pop()
                    counts["environment_closers"] += 1
                    if environment != expected:
                        errors.append(
                            f"Environment nesting mismatch at {location(token.offset)}: "
                            f"end {environment!r}, expected {expected!r} opened "
                            f"at {location(opened_at)}."
                        )
            elif command == "scanpage":
                argument = literal_group(masked, token.end)
                if argument is None or not re.fullmatch(r"[0-9]+", argument):
                    scan_markers.append(None)
                    errors.append(
                        f"\\scanpage has no literal nonnegative integer argument "
                        f"at {location(token.offset)}."
                    )
                else:
                    scan_markers.append(int(argument))
            elif command == "cotefile":
                cote_markers.append(literal_group(masked, token.end))

    for offset in braces:
        errors.append(f"Unclosed opening brace at {location(offset)}.")
    for environment, offset in environments:
        errors.append(f"Unclosed environment {environment!r} at {location(offset)}.")
    if math is not None:
        errors.append(f"Unclosed math delimiter {math[0]!r} at {location(math[1])}.")
    return {
        "errors": errors,
        "scan_markers": scan_markers,
        "cote_markers": cote_markers,
        "token_counts": dict(sorted(counts.items())),
    }


def regular_file(path: Path) -> bool:
    try:
        return path.is_file() and not path.is_symlink()
    except OSError:
        return False


def add_check(
    checks: list[dict[str, Any]], name: str, errors: list[str], **details: Any
) -> None:
    checks.append({"name": name, "status": "fail" if errors else "pass", "errors": errors, **details})


def check_required(output_dir: Path, checks: list[dict[str, Any]]) -> None:
    errors = []
    for name in REQUIRED_FILES:
        path = output_dir / name
        if not regular_file(path):
            errors.append(f"Required regular file missing or is a symlink: {name}")
        else:
            try:
                if path.stat().st_size == 0:
                    errors.append(f"Required file is empty: {name}")
            except OSError as exc:
                errors.append(f"Cannot stat {name}: {exc}")
    pages_dir = output_dir / "pages"
    if not pages_dir.is_dir() or pages_dir.is_symlink():
        errors.append("Required regular directory missing or is a symlink: pages/")
    add_check(checks, "required_deliverables", errors, required_files=list(REQUIRED_FILES), required_directory="pages/")


def check_pages(output_dir: Path, checks: list[dict[str, Any]]) -> dict[int, tuple[Path, bytes]]:
    pages_dir = output_dir / "pages"
    errors: list[str] = []
    page_details: list[dict[str, Any]] = []
    by_scan: dict[int, tuple[Path, bytes]] = {}
    if not pages_dir.is_dir() or pages_dir.is_symlink():
        add_check(checks, "page_tex_structure", ["pages/ is unavailable as a regular directory."])
        return by_scan
    try:
        entries = sorted(pages_dir.iterdir(), key=lambda path: path.name)
    except OSError as exc:
        add_check(checks, "page_tex_structure", [f"Cannot list pages/: {exc}"])
        return by_scan
    page_files = []
    for path in entries:
        if not regular_file(path) or path.suffix != ".tex":
            errors.append(f"Unexpected non-page entry in pages/: {path.name}")
        else:
            page_files.append(path)
    if len(page_files) != len(EXPECTED_SCANS):
        errors.append(f"Expected {len(EXPECTED_SCANS)} page .tex files; found {len(page_files)}.")
    for path in page_files:
        relative = path.relative_to(output_dir).as_posix()
        try:
            data = path.read_bytes()
            source = data.decode("utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {relative} as UTF-8: {exc}")
            continue
        analysis = inspect_tex(source)
        page_errors = list(analysis["errors"])
        markers = analysis["scan_markers"]
        if len(markers) != 1:
            page_errors.append(f"Expected exactly one \\scanpage command; found {len(markers)}.")
        elif markers[0] is not None:
            scan = markers[0]
            if scan not in EXPECTED_SCANS:
                page_errors.append(f"Unexpected scan marker: {scan}.")
            elif scan in by_scan:
                page_errors.append(f"Duplicate scan marker: {scan}.")
            else:
                by_scan[scan] = (path, data)
        if analysis["cote_markers"]:
            page_errors.append("Page files must not contain a \\cotefile command.")
        errors.extend(f"{relative}: {error}" for error in page_errors)
        page_details.append({
            "file": relative,
            "scan_markers": markers,
            "bytes": len(data),
            "token_counts": analysis["token_counts"],
            "status": "fail" if page_errors else "pass",
        })
    missing = sorted(set(EXPECTED_SCANS) - set(by_scan))
    if missing:
        errors.append(f"Missing expected scan markers: {missing}.")
    add_check(
        checks, "page_tex_structure", errors,
        expected_scan_order=list(EXPECTED_SCANS), pages=page_details,
    )
    return by_scan


def check_combined(
    output_dir: Path, pages: dict[int, tuple[Path, bytes]], checks: list[dict[str, Any]]
) -> None:
    errors = []
    path = output_dir / COMBINED
    if not regular_file(path):
        add_check(checks, "combined_tex", [f"{COMBINED} is unavailable as a regular file."])
        return
    try:
        actual = path.read_bytes()
        analysis = inspect_tex(actual.decode("utf-8"))
    except (OSError, UnicodeError) as exc:
        add_check(checks, "combined_tex", [f"Cannot read {COMBINED} as UTF-8: {exc}"])
        return
    if analysis["cote_markers"] != ["63"]:
        errors.append("Combined file must contain exactly one literal \\cotefile{63} command.")
    if analysis["scan_markers"] != list(EXPECTED_SCANS):
        errors.append("Combined scanpage markers do not match the exact expected scan order.")
    expected_bytes = None
    if set(pages) == set(EXPECTED_SCANS):
        expected = b"\\cotefile{63}\n" + b"".join(pages[scan][1] for scan in EXPECTED_SCANS)
        expected_bytes = len(expected)
        if actual != expected:
            errors.append(
                "Combined bytes differ from b'\\\\cotefile{63}\\n' followed by "
                "the exact page-file bytes in expected scan order (no added separators)."
            )
    else:
        errors.append("Exact combined comparison could not run because an expected page is missing.")
    if analysis["errors"]:
        errors.extend(f"Combined TeX: {error}" for error in analysis["errors"])
    add_check(
        checks, "combined_tex", errors, actual_bytes=len(actual), expected_bytes=expected_bytes,
        convention="b'\\\\cotefile{63}\\n' + b''.join(ordered_page_bytes)",
    )


def read_table(
    output_dir: Path, filename: str, delimiter: str, columns: tuple[str, ...]
) -> tuple[list[str], list[tuple[int, list[str]]]]:
    errors: list[str] = []
    rows: list[tuple[int, list[str]]] = []
    path = output_dir / filename
    if not regular_file(path):
        return [f"{filename} is unavailable as a regular file."], rows
    try:
        # A UTF-8 BOM does not become part of the first column name.
        source = path.read_bytes().decode("utf-8-sig")
        reader = csv.reader(io.StringIO(source, newline=""), delimiter=delimiter, strict=True)
        header = next(reader, None)
        if header != list(columns):
            errors.append(f"{filename}: header differs from the exact required ordered columns.")
        for row in reader:
            if not row:
                continue
            line_number = reader.line_num
            if len(row) != len(columns):
                errors.append(
                    f"{filename}: row ending at physical line {line_number} has "
                    f"{len(row)} fields; expected {len(columns)}."
                )
            else:
                rows.append((line_number, row))
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"Cannot parse {filename}: {exc}")
    return errors, rows


def check_inventory(output_dir: Path, checks: list[dict[str, Any]]) -> None:
    errors, rows = read_table(output_dir, INVENTORY, ",", INVENTORY_COLUMNS)
    coverage: collections.Counter[int] = collections.Counter()
    for line_number, row in rows:
        value = row[0].strip()
        if not re.fullmatch(r"[0-9]+", value):
            errors.append(f"{INVENTORY}: scan is not a literal integer at physical line {line_number}.")
        else:
            scan = int(value)
            coverage[scan] += 1
            if scan not in EXPECTED_SCANS:
                errors.append(f"{INVENTORY}: unexpected scan {scan} at physical line {line_number}.")
        if row[7].strip() != "yes":
            errors.append(f"{INVENTORY}: transcribed is not 'yes' at physical line {line_number}.")
    missing = sorted(set(EXPECTED_SCANS) - set(coverage))
    if missing:
        errors.append(f"{INVENTORY}: no inventory row for expected scans {missing}.")
    add_check(
        checks, "inventory_csv", errors, expected_columns=list(INVENTORY_COLUMNS),
        rows=len(rows), rows_per_scan={str(scan): coverage[scan] for scan in sorted(coverage)},
    )


def check_collation(output_dir: Path, checks: list[dict[str, Any]]) -> None:
    errors, rows = read_table(output_dir, COLLATION, "\t", COLLATION_COLUMNS)
    add_check(checks, "collation_tsv", errors, expected_columns=list(COLLATION_COLUMNS), rows=len(rows))


def check_events(output_dir: Path, checks: list[dict[str, Any]]) -> None:
    errors, rows = read_table(output_dir, EVENTS, "\t", EVENT_COLUMNS)
    if not rows:
        errors.append(f"{EVENTS}: expected at least one structured event row.")
    for line_number, row in rows:
        empty_fields = [name for name, value in zip(EVENT_COLUMNS, row) if not value.strip()]
        if empty_fields:
            errors.append(
                f"{EVENTS}: empty fields at physical line {line_number}: {', '.join(empty_fields)}."
            )
    add_check(checks, "check_events_tsv", errors, expected_columns=list(EVENT_COLUMNS), rows=len(rows))


def allowed_file(relative: PurePosixPath) -> bool:
    parts = relative.parts
    if not parts or any(part in {".", ".."} for part in parts) or relative.is_absolute():
        return False
    if relative.suffix.lower() in FORBIDDEN_ARCHIVE_SUFFIXES:
        return False
    if len(parts) == 1:
        return relative.name in REQUIRED_FILES or relative.name in OPTIONAL_FILES or bool(REPORT_NAME_RE.fullmatch(relative.name))
    if len(parts) == 2 and parts[0] == "pages" and relative.suffix == ".tex":
        return True
    if parts[0] == "scripts" and relative.suffix == ".py":
        return True
    if parts[0] == "records" and relative.suffix == ".json":
        return True
    return False


def allowed_directory(relative: PurePosixPath) -> bool:
    return relative.as_posix() == "pages" or bool(relative.parts and relative.parts[0] in {"scripts", "records"})


def collect_intended_files(output_dir: Path) -> tuple[list[str], dict[str, Path]]:
    errors: list[str] = []
    intended: dict[str, Path] = {}
    if not output_dir.is_dir():
        return ["Output directory is unavailable."], intended
    try:
        root_entries = list(output_dir.iterdir())
        candidates = [path for path in root_entries if path.is_file() or path.is_symlink()]
        for dirname in ("pages", "scripts", "records"):
            directory = output_dir / dirname
            if directory.is_symlink():
                errors.append(f"Allowed output directory is a symlink: {dirname}/")
            elif directory.is_dir():
                for path in directory.rglob("*"):
                    if path.is_symlink():
                        errors.append(f"Symlink within output documentation: {path.relative_to(output_dir).as_posix()}")
                    elif path.is_file():
                        candidates.append(path)
        for path in candidates:
            relative = PurePosixPath(path.relative_to(output_dir).as_posix())
            if allowed_file(relative):
                if path.is_symlink():
                    errors.append(f"Allowed output file is a symlink: {relative.as_posix()}")
                else:
                    intended[relative.as_posix()] = path
    except OSError as exc:
        errors.append(f"Cannot enumerate allowed output files: {exc}")
    return errors, intended


def same_bytes(left: Any, right: Any) -> bool:
    while True:
        left_chunk = left.read(1024 * 1024)
        right_chunk = right.read(1024 * 1024)
        if left_chunk != right_chunk:
            return False
        if not left_chunk:
            return True


def check_zip(output_dir: Path, archive: Path, checks: list[dict[str, Any]]) -> None:
    errors, intended = collect_intended_files(output_dir)
    file_names: list[str] = []
    compared = 0
    if not regular_file(archive):
        errors.append("Requested ZIP is unavailable as a regular file.")
        add_check(checks, "zip_archive", errors, archive=str(archive))
        return
    try:
        with zipfile.ZipFile(archive) as zipped:
            entries = zipped.infolist()
            duplicates = sorted(name for name, count in collections.Counter(item.filename for item in entries).items() if count > 1)
            if duplicates:
                errors.append(f"Duplicate ZIP member names: {duplicates}.")
            for info in entries:
                name = info.filename
                candidate = name[:-1] if info.is_dir() else name
                components = candidate.split("/")
                if (
                    not candidate or "\\" in candidate or candidate.startswith("/")
                    or any(part in {"", ".", ".."} for part in components)
                    or ":" in components[0]
                ):
                    errors.append(f"Unsafe or noncanonical ZIP path: {name!r}.")
                    continue
                relative = PurePosixPath(candidate)
                mode = info.external_attr >> 16
                if stat.S_ISLNK(mode):
                    errors.append(f"ZIP symlink is not allowed: {name}.")
                    continue
                if info.is_dir():
                    if not allowed_directory(relative):
                        errors.append(f"Unexpected ZIP directory: {name}.")
                    continue
                file_names.append(name)
                if not allowed_file(relative):
                    errors.append(f"ZIP contains a file outside the output allowlist: {name}.")
                    continue
                path = intended.get(name)
                if path is None:
                    errors.append(f"ZIP member has no matching allowed output file: {name}.")
                    continue
                if info.flag_bits & 1:
                    errors.append(f"Encrypted ZIP member cannot be checked: {name}.")
                    continue
                if path.stat().st_size != info.file_size:
                    errors.append(f"ZIP member size differs from output file: {name}.")
                    continue
                with zipped.open(info) as zip_stream, path.open("rb") as disk_stream:
                    if not same_bytes(zip_stream, disk_stream):
                        errors.append(f"ZIP member bytes differ from output file: {name}.")
                    else:
                        compared += 1
            missing = sorted(set(intended) - set(file_names))
            if missing:
                errors.append(f"Allowed output files missing from ZIP: {missing}.")
    except (OSError, RuntimeError, ValueError, zipfile.BadZipFile, NotImplementedError) as exc:
        errors.append(f"Cannot fully validate ZIP: {exc}")
    add_check(
        checks, "zip_archive", errors, archive=str(archive), file_members=len(file_names),
        intended_files=len(intended), byte_identical_members=compared,
        allowed_optional_files=sorted(OPTIONAL_FILES),
        allowed_optional_patterns=[
            "scripts/**/*.py", "records/**/*.json",
            "validation*.{json,txt,md,tsv,log}",
            "SP56_CW_63_validation*.{json,txt,md,tsv,log}",
        ],
    )


def validate(output_dir: Path, archive: Path | None = None) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    check_required(output_dir, checks)
    pages = check_pages(output_dir, checks)
    check_combined(output_dir, pages, checks)
    check_inventory(output_dir, checks)
    check_collation(output_dir, checks)
    check_events(output_dir, checks)
    if archive is not None:
        check_zip(output_dir, archive, checks)
    else:
        checks.append({
            "name": "zip_archive", "status": "not_requested", "errors": [],
            "reason": "No --zip path supplied; no archive was inspected.",
        })
    return {
        "validator": "SP56_CW_63 structural validator",
        "output_directory": str(output_dir),
        "passed": all(check["status"] in {"pass", "not_requested"} for check in checks),
        "scope": "Formatting, file membership, and declared table structure only.",
        "checks": checks,
        "limitations": LIMITATIONS,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output_dir", type=Path, help="Directory containing the required deliverables and pages/.")
    parser.add_argument("--zip", dest="archive", type=Path, help="Optional final ZIP; paths inside must be relative to output_dir.")
    parser.add_argument("--format", choices=("json", "text"), default="json", help="stdout report format (default: json).")
    args = parser.parse_args()
    output_dir = args.output_dir.expanduser().absolute()
    archive = args.archive.expanduser().absolute() if args.archive is not None else None
    report = validate(output_dir, archive)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("PASS" if report["passed"] else "FAIL")
        print(f"Output: {report['output_directory']}")
        for check in report["checks"]:
            print(f"[{check['status']}] {check['name']}")
            for error in check["errors"]:
                print(f"  - {error}")
            if "reason" in check:
                print(f"  {check['reason']}")
        print("Limitations:")
        for limitation in report["limitations"]:
            print(f"  - {limitation}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
