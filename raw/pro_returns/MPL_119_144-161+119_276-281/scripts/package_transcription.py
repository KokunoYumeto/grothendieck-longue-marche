#!/usr/bin/env python3
"""Mechanical packaging checks; this program never certifies visual accuracy.

Run from any directory. It does not perform OCR, inspect images, or open context.
The directory above this script's scripts/ directory is the deliverable root.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path


PACKAGE = "MPL_119_144-161+119_276-281"
COTE = "119"
SCANS = (144, 145, 146, *range(148, 154), *range(155, 162), *range(276, 282))
HEADERS = (
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
CHECK_EVENT_HEADERS = ("statement_id", "date", "who", "type", "outcome")
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
TIME_FORMAT = "%Y-%m-%d %H:%M:%S UTC"
FROZEN_RE = re.compile(r"^transcription frozen (.+)$", re.MULTILINE)
HASH_RE = re.compile(r"^sha256 ([0-9a-f]{64}) (.+)$", re.MULTILINE)
CHECKPOINT_RE = re.compile(r"^checkpoint (\d+) saved (.+)$", re.MULTILINE)
CONTEXT_RE = re.compile(r"^context opened (.+)$", re.MULTILINE)
EXCLUDED_DIRS = {"upload", "uploads", "input", "inputs", "scans", "context", "__pycache__", ".git", "build", "tex_build"}
EXCLUDED_SUFFIXES = {".zip", ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".pyc", ".pyo"}


def now() -> str:
    return datetime.now(timezone.utc).strftime(TIME_FORMAT)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def page_path(root: Path, scan: int) -> Path:
    return root / "pages" / f"{PACKAGE}_{COTE}_scan{scan:03d}.tex"


def combined_path(root: Path) -> Path:
    return root / f"{PACKAGE}_transcription.tex"


def read_log(root: Path) -> str:
    return (root / "progress.log").read_text(encoding="utf-8")


def append_log(root: Path, lines: list[str]) -> None:
    log = root / "progress.log"
    prior = log.read_bytes() if log.exists() else b""
    with log.open("a", encoding="utf-8", newline="\n") as stream:
        if prior and not prior.endswith(b"\n"):
            stream.write("\n")
        stream.write("\n".join(lines) + "\n")


def concatenated(root: Path) -> str:
    # A blank line separates pages. Page-file bytes themselves are not changed.
    return "\n".join(page_path(root, s).read_text(encoding="utf-8").rstrip("\n") + "\n" for s in SCANS)


def brace_errors(source: str) -> list[str]:
    """Balance unescaped braces, skipping ordinary TeX comments and \\verb.

    This is deliberately only a mechanical check, not a complete TeX parser.
    An odd run of preceding backslashes escapes a percent sign or brace.
    """
    errors: list[str] = []
    opened: list[tuple[int, int]] = []
    for line_no, line in enumerate(source.splitlines(), 1):
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == "\\":
                if line.startswith("\\verb", i):
                    j = i + 5
                    if j < len(line) and line[j] == "*":
                        j += 1
                    if j < len(line) and not line[j].isalpha() and not line[j].isspace():
                        end = line.find(line[j], j + 1)
                        if end == -1:
                            errors.append(f"line {line_no}: unterminated \\verb")
                            break
                        i = end + 1
                        continue
                # Skip one escaped non-letter, including \\, \%, \{, and \}.
                if i + 1 < len(line) and not line[i + 1].isalpha():
                    i += 2
                    continue
                i += 1
                continue
            if ch == "%":
                break
            if ch == "{":
                opened.append((line_no, i + 1))
            elif ch == "}":
                if opened:
                    opened.pop()
                else:
                    errors.append(f"line {line_no}, column {i + 1}: unmatched closing brace")
            i += 1
    errors.extend(f"line {line}, column {col}: unmatched opening brace" for line, col in opened)
    return errors


def tex_controls(source: str):
    """Yield control tokens and offsets, skipping comments and verbatim spans.

    A double backslash is one control-symbol token, so a following word is
    not mistakenly reported as a command. This is a lexical pass, not TeX
    expansion or mathematical/content interpretation.
    """
    i = 0
    length = len(source)
    while i < length:
        if source[i] == "%":
            newline = source.find("\n", i)
            i = length if newline == -1 else newline + 1
            continue
        if source[i] != "\\":
            i += 1
            continue
        start = i
        i += 1
        if i == length:
            yield "", start, i
            break
        if source[i].isascii() and (source[i].isalpha() or source[i] == "@"):
            first = i
            while i < length and source[i].isascii() and (source[i].isalpha() or source[i] == "@"):
                i += 1
            command = source[first:i]
        else:
            command = source[i]
            i += 1
        if command == "verb":
            if i < length and source[i] == "*":
                i += 1
            if i < length and source[i] not in "\r\n":
                end = source.find(source[i], i + 1)
                newline = source.find("\n", i)
                if end != -1 and (newline == -1 or end < newline):
                    i = end + 1
                    continue
        yield command, start, i


def environment_errors(source: str) -> list[str]:
    """Balance literal begin/end environments and check nesting order.

    Macro-generated names and verbatim environments are outside this small
    parser's scope. The manuscript fragments use literal environment names.
    Inline \\verb spans and ordinary comments are ignored by tex_controls.
    """
    errors: list[str] = []
    stack: list[tuple[str, int]] = []
    for command, start, end in tex_controls(source):
        if command not in {"begin", "end"}:
            continue
        # Whitespace and complete ordinary comment lines may precede the name.
        match = re.match(r"(?:\s|%[^\n]*(?:\n|$))*\{([A-Za-z@*][A-Za-z0-9@*.-]*)\}", source[end:])
        line = source.count("\n", 0, start) + 1
        if match is None:
            errors.append(f"line {line}: cannot mechanically read literal environment name after \\{command}")
            continue
        name = match.group(1)
        if command == "begin":
            stack.append((name, line))
        elif not stack:
            errors.append(f"line {line}: unmatched \\end{{{name}}}")
        else:
            opened, opening_line = stack.pop()
            if name != opened:
                errors.append(f"line {line}: \\end{{{name}}} mismatches \\begin{{{opened}}} on line {opening_line}")
    errors.extend(f"line {line}: unclosed \\begin{{{name}}}" for name, line in stack)
    return errors


def validate(root: Path, require_combined: bool = True, partial: bool = False) -> list[str]:
    errors: list[str] = []
    expected = {page_path(root, s).name for s in SCANS}
    actual = {p.name for p in (root / "pages").glob("*.tex")}
    if not partial:
        errors.extend(f"missing page: {name}" for name in sorted(expected - actual))
    errors.extend(f"unexpected page: {name}" for name in sorted(actual - expected))
    present_scans: set[int] = set()
    for scan in SCANS:
        path = page_path(root, scan)
        if not path.exists():
            continue
        present_scans.add(scan)
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        if not source.strip():
            errors.append(f"{path.name}: empty page")
        markers = re.findall(r"\\scanpage\{(\d+)\}", source)
        if markers != [str(scan)]:
            errors.append(f"{path.name}: scanpage markers are {markers!r}")
        for issue in brace_errors(source):
            errors.append(f"{path.name}: {issue}")
        for issue in environment_errors(source):
            errors.append(f"{path.name}: {issue}")

    inventory = root / f"{PACKAGE}_inventory.csv"
    covered: set[int] = set()
    seen_elements: set[tuple[int, str]] = set()
    if not inventory.exists():
        errors.append("missing inventory")
    else:
        with inventory.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if tuple(reader.fieldnames or ()) != HEADERS:
                errors.append(f"inventory columns differ: {reader.fieldnames!r}")
            else:
                for line_no, row in enumerate(reader, 2):
                    label = f"inventory row {line_no}"
                    if None in row or any(value is None for value in row.values()):
                        errors.append(f"{label}: malformed column count")
                        continue
                    if row["cote"] != COTE:
                        errors.append(f"{label}: unexpected cote")
                    try:
                        scan = int(row["scan"])
                    except ValueError:
                        errors.append(f"{label}: invalid scan number")
                        continue
                    if scan not in SCANS:
                        errors.append(f"{label}: scan outside expected set")
                    else:
                        covered.add(scan)
                    if row["sheet_kind"] not in SHEET_KINDS:
                        errors.append(f"{label}: invalid sheet_kind {row['sheet_kind']!r}")
                    if row["kind"] not in KINDS:
                        errors.append(f"{label}: invalid kind {row['kind']!r}")
                    if row["transcribed"] != "yes":
                        errors.append(f"{label}: transcribed must be exactly yes")
                    if not row["element"].strip():
                        errors.append(f"{label}: empty element id")
                    key = (scan, row["element"])
                    if key in seen_elements:
                        errors.append(f"{label}: duplicate element id on scan {scan}")
                    seen_elements.add(key)
        needed = present_scans if partial else set(SCANS)
        errors.extend(f"inventory has no rows for scan {scan}" for scan in sorted(needed - covered))
        errors.extend(f"inventory has rows but page file missing for scan {scan}" for scan in sorted(covered - present_scans))

    combined = combined_path(root)
    if require_combined and not partial:
        if not combined.exists():
            errors.append("missing combined transcription")
        elif expected <= actual:
            if combined.read_text(encoding="utf-8") != concatenated(root):
                errors.append("combined transcription differs from prescribed page concatenation")
            else:
                for issue in brace_errors(combined.read_text(encoding="utf-8")):
                    errors.append(f"combined transcription: {issue}")
                for issue in environment_errors(combined.read_text(encoding="utf-8")):
                    errors.append(f"combined transcription: {issue}")
    return errors


def require_clean(errors: list[str]) -> None:
    if errors:
        raise ValueError("\n".join(errors))


def completion_log_errors(log: str, latest_time: datetime | None = None) -> list[str]:
    """Check recorded event order only; this does not establish visual work."""
    errors: list[str] = []
    if not log.splitlines():
        return ["empty progress.log"]
    try:
        start = datetime.strptime(log.splitlines()[0], TIME_FORMAT)
    except ValueError:
        return ["progress.log must begin with an exact UTC timestamp"]
    done = []
    audited = []
    timed_events = []
    for scan in SCANS:
        for kind, pattern, collection in (
            ("completion", rf"^{COTE} scan {scan:03d} done (.+)$", done),
            ("second-reading audit", rf"^scan {scan:03d} audited (.+)$", audited),
        ):
            matches = list(re.finditer(pattern, log, re.MULTILINE))
            if not matches:
                errors.append(f"missing {kind} log for scan {scan}")
                continue
            match = matches[-1]
            try:
                event_time = datetime.strptime(match.group(1), TIME_FORMAT)
                if event_time < start:
                    errors.append(f"{kind} time precedes start for scan {scan}")
                if latest_time is not None and event_time > latest_time:
                    errors.append(f"{kind} time follows freeze for scan {scan}")
                timed_events.append((match.start(), event_time))
            except ValueError:
                errors.append(f"invalid {kind} UTC time for scan {scan}")
            collection.append(match)
    if done and audited and min(m.start() for m in audited) < max(m.start() for m in done):
        errors.append("second-reading audit records must follow completion of all pages")
    ordered_times = [value for _, value in sorted(timed_events)]
    if any(later < earlier for earlier, later in zip(ordered_times, ordered_times[1:])):
        errors.append("completion/audit UTC timestamps are not chronological in log order")
    return errors


def assemble(root: Path) -> None:
    if FROZEN_RE.search(read_log(root)):
        raise ValueError("transcription is frozen; assembly refused")
    require_clean(validate(root, require_combined=False))
    combined_path(root).write_text(concatenated(root), encoding="utf-8", newline="\n")
    print("Combined transcription assembled; page files unchanged.")


def freeze(root: Path) -> None:
    log = read_log(root)
    if FROZEN_RE.search(log):
        raise ValueError("freeze already recorded; use verify-frozen")
    if CONTEXT_RE.search(log):
        raise ValueError("context opened already recorded; cannot establish pre-context freeze")
    if HASH_RE.search(log):
        raise ValueError("pre-existing hash records without a freeze need review before retry")
    require_clean(validate(root))
    require_clean(completion_log_errors(log))
    paths = [page_path(root, scan) for scan in SCANS] + [combined_path(root)]
    records = [f"sha256 {sha256(path)} {path.relative_to(root).as_posix()}" for path in paths]
    records.append(f"transcription frozen {now()}")
    append_log(root, records)
    print(f"Frozen hashes recorded for {len(paths)} files. Visual audits are asserted by the log, not performed by this program.")


def verify_frozen(root: Path, record: bool = False) -> None:
    log = read_log(root)
    freezes = list(FROZEN_RE.finditer(log))
    if len(freezes) != 1:
        raise ValueError("expected exactly one freeze record")
    frozen = freezes[0]
    frozen_time = datetime.strptime(frozen.group(1), TIME_FORMAT)
    records = list(HASH_RE.finditer(log))
    expected = [page_path(root, s).relative_to(root).as_posix() for s in SCANS]
    expected.append(combined_path(root).name)
    if [m.group(2) for m in records] != expected:
        raise ValueError("frozen hashes must list the 22 pages in scan order, then the combined transcription")
    if any(m.start() > frozen.start() for m in records):
        raise ValueError("all transcription hashes must precede the freeze record")
    require_clean(completion_log_errors(log[:records[0].start()], latest_time=frozen_time))
    contexts = list(CONTEXT_RE.finditer(log))
    if len(contexts) > 1:
        raise ValueError("more than one context-opening record")
    for context in contexts:
        if context.start() < frozen.end():
            raise ValueError("context opening must follow the transcription freeze")
        if datetime.strptime(context.group(1), TIME_FORMAT) < frozen_time:
            raise ValueError("context-opening timestamp precedes freeze timestamp")
    for match in records:
        digest, relative = match.groups()
        path = root / relative
        if not path.is_file() or sha256(path) != digest:
            raise ValueError(f"frozen hash mismatch: {relative}")
    if record:
        append_log(root, [f"frozen hashes unchanged {now()} (22 page files and combined transcription)"])
    print("All 23 frozen hashes are unchanged; no transcription files were edited.")


def archive_paths(root: Path) -> list[Path]:
    paths: list[Path] = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if path.suffix.lower() in EXCLUDED_SUFFIXES:
            continue
        if path.is_symlink():
            raise ValueError(f"refusing symlink in deliverables: {rel}")
        if path.is_file():
            paths.append(path)
    return paths


def write_zip(root: Path, destination: Path, log_additions: list[str] | None = None) -> None:
    if destination.exists():
        raise ValueError(f"refusing to overwrite ZIP: {destination}")
    files = archive_paths(root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive mode also protects against a race after the exists check.
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(root).as_posix()
            if relative == "progress.log" and log_additions:
                log_copy = read_log(root).rstrip("\n") + "\n" + "\n".join(log_additions) + "\n"
                archive.writestr(relative, log_copy)
            else:
                archive.write(path, relative)
    print(f"Created {destination} ({len(files)} files; supplied sources and previous ZIPs excluded).")


def checkpoint(root: Path, output_dir: Path | None) -> None:
    log = read_log(root)
    start = datetime.strptime(log.splitlines()[0], TIME_FORMAT).replace(tzinfo=timezone.utc)
    previous = CHECKPOINT_RE.findall(log)
    number = max((int(n) for n, _ in previous), default=0) + 1
    due = start + timedelta(hours=number)
    current = datetime.now(timezone.utc)
    if current < due:
        raise ValueError(f"checkpoint {number:02d} is not due until {due.strftime(TIME_FORMAT)}")
    if previous:
        last = datetime.strptime(previous[-1][1], TIME_FORMAT).replace(tzinfo=timezone.utc)
        if current - last < timedelta(minutes=59):
            raise ValueError("an hourly checkpoint was saved less than 59 minutes ago")
    directory = output_dir or root.parent
    destination = directory / f"{PACKAGE}_checkpoint_{number:02d}.zip"
    if destination.exists():
        raise ValueError(f"refusing to overwrite ZIP: {destination}")
    # This documents local packaging only. Root must independently confirm persistence.
    records = [f"checkpoint {number:02d} saved {now()}"]
    # Include the success record in the archive, but append it to the live log
    # only after local ZIP creation succeeds. Library persistence is separate.
    write_zip(root, destination, log_additions=records)
    append_log(root, records)


def check_events_errors(root: Path) -> list[str]:
    errors: list[str] = []
    path = root / "CHECK_EVENTS.tsv"
    if not path.is_file():
        return ["missing CHECK_EVENTS.tsv"]
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if tuple(reader.fieldnames or ()) != CHECK_EVENT_HEADERS:
            return [f"CHECK_EVENTS.tsv columns differ: {reader.fieldnames!r}"]
        count = 0
        for line_no, row in enumerate(reader, 2):
            count += 1
            if None in row or any(value is None for value in row.values()):
                errors.append(f"CHECK_EVENTS.tsv row {line_no}: malformed column count")
            elif any(not value.strip() for value in row.values()):
                errors.append(f"CHECK_EVENTS.tsv row {line_no}: empty required field")
        if not count:
            errors.append("CHECK_EVENTS.tsv has no events; research-note statement use/checks must be accounted for")
    return errors


def final_zip(root: Path, output_dir: Path | None) -> None:
    require_clean(validate(root))
    required = [f"{PACKAGE}_doubts.md", f"{PACKAGE}_notes.md", "CHECK_EVENTS.tsv", "progress.log"]
    for filename in required:
        path = root / filename
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            raise ValueError(f"missing or empty final deliverable: {filename}")
    require_clean(check_events_errors(root))
    if len(CONTEXT_RE.findall(read_log(root))) != 1:
        raise ValueError("final packaging requires the single post-freeze context-opening record")
    destination = (output_dir or root.parent) / f"{PACKAGE}.zip"
    if destination.exists():
        raise ValueError(f"refusing to overwrite ZIP: {destination}")
    # The final archive must contain the required statement that hashes remain
    # unchanged. This happens only when the user runs final-zip, not on import.
    verify_frozen(root, record=True)
    write_zip(root, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("validate", help="mechanical checks only; does not certify transcription completeness")
    check.add_argument("--partial", action="store_true", help="check only present pages; do not require combined file")
    sub.add_parser("assemble", help="assemble combined file before freeze")
    sub.add_parser("freeze", help="record hashes after all done/audited log entries exist")
    verify = sub.add_parser("verify-frozen", help="verify immutable transcription files")
    verify.add_argument("--record", action="store_true", help="append successful verification to progress.log")
    for name in ("checkpoint", "final-zip"):
        command = sub.add_parser(name)
        command.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "validate":
            require_clean(validate(root, partial=args.partial))
            print("Mechanical validation passed. Visual completeness and accuracy are not assessed.")
        elif args.command == "assemble":
            assemble(root)
        elif args.command == "freeze":
            freeze(root)
        elif args.command == "verify-frozen":
            verify_frozen(root, record=args.record)
        elif args.command == "checkpoint":
            checkpoint(root, args.output_dir)
        elif args.command == "final-zip":
            final_zip(root, args.output_dir)
    except (OSError, ValueError, UnicodeError, csv.Error, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
