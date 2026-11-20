#!/usr/bin/env python3
"""Read-only structural validation of SP62_CW_162-1+162-6 deliverables.

This program checks syntax, schemas, membership, and hashes only.  It does not
recognize images, judge readings, compare witnesses, compile TeX, or modify any
file.  A successful result is not a claim of palaeographical correctness.

Usage:
    python scripts/validate_package.py OUT_DIRECTORY
    python scripts/validate_package.py OUT_DIRECTORY --zip FINAL_ZIP --format json

Exit status is 0 when all structural checks pass, 1 for validation failures,
and 2 for command-line errors.  Reports are printed to stdout only.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath


PREFIX = "SP62_CW_162-1+162-6"
PAGES = [
    ("H162-01", "162-1", scan) for scan in range(5, 11)
] + [
    ("H162-02", "162-6", scan) for scan in range(2, 7)
]
PAGE_NAMES = [f"{folder}_{cote}_scan{scan:03d}.tex" for folder, cote, scan in PAGES]
REQUIRED = [
    f"pages/{name}" for name in PAGE_NAMES
] + [
    f"{PREFIX}_transcription.tex",
    f"{PREFIX}_changes.md",
    f"{PREFIX}_collation.tsv",
    f"{PREFIX}_doubts.md",
    f"{PREFIX}_inventory.csv",
    f"{PREFIX}_notes.md",
    f"{PREFIX}_sheet_feedback.md",
    f"{PREFIX}_hand_log.md",
    "progress.log",
    "CHECK_EVENTS.tsv",
]
COLLATION_FIELDS = [
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H",
    "confidence",
]
INVENTORY_FIELDS = [
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission",
    "text not on the page",
    "deletion state (struck given live or live given struck)",
    "insertion or placement", "abbreviation expanded or spelling modernised",
    r"readable ink left as \ill{}", "drawing or diagram", "other",
}
INVENTORY_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion",
    "deletion",
}
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list",
    "cancelled_draft", "cover",
}
CONFIDENCES = {"high", "medium", "low"}
IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".bmp", ".webp",
    ".svg", ".ico", ".heic", ".avif", ".jp2", ".ppm", ".pgm", ".pbm",
    ".pdf",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def strip_comments(text: str) -> str:
    """Remove unescaped TeX comments while retaining newlines and line numbers."""
    return re.sub(r"(?<!\\)((?:\\\\)*)%[^\n]*", r"\1", text)


def tex_checks(text: str, name: str) -> list[str]:
    """Check braces, $/$$/\\[...\\]/\\(...\\), and environment nesting."""
    clean = strip_comments(text)
    errors: list[str] = []
    braces: list[int] = []
    envs: list[tuple[str, int]] = []
    # This is delimiter balancing, not TeX mode inference.  Text boxes, p-type
    # table columns, and TikZ nodes can re-enter math inside an outer formula.
    # A stack therefore permits nested delimiters without claiming to verify
    # whether the intervening macro actually changes TeX's mode.
    math: list[tuple[str, int]] = []
    i = 0
    line = 1
    while i < len(clean):
        char = clean[i]
        if char == "\n":
            line += 1
            i += 1
            continue
        if char == "\\":
            match = re.match(r"\\(begin|end)\s*\{([^{}]+)\}", clean[i:])
            if match:
                command, env = match.groups()
                if command == "begin":
                    envs.append((env, line))
                elif not envs:
                    errors.append(f"{name}:{line}: unmatched \\end{{{env}}}")
                elif envs[-1][0] != env:
                    errors.append(
                        f"{name}:{line}: \\end{{{env}}} mismatches "
                        f"\\begin{{{envs[-1][0]}}} on line {envs[-1][1]}"
                    )
                else:
                    envs.pop()
                i += len(match.group())
                continue
            token = clean[i:i + 2]
            if token in (r"\[", r"\("):
                math.append((token, line))
            elif token in (r"\]", r"\)"):
                wanted = r"\[" if token == r"\]" else r"\("
                if not math or math[-1][0] != wanted:
                    errors.append(f"{name}:{line}: unmatched math delimiter {token}")
                else:
                    math.pop()
            # TeX control symbols consume their next character, including
            # escaped braces, escaped dollars, and the second slash of \\.
            if i + 1 < len(clean) and not clean[i + 1].isalpha():
                i += 2
            else:
                command = re.match(r"\\[A-Za-z]+", clean[i:])
                i += len(command.group()) if command else 1
            continue
        if char == "{":
            braces.append(line)
        elif char == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"{name}:{line}: unmatched closing brace")
        elif char == "$":
            token = "$$" if clean[i:i + 2] == "$$" else "$"
            if math and math[-1][0] == token:
                math.pop()
            else:
                math.append((token, line))
            i += len(token)
            continue
        i += 1
    for opening in braces:
        errors.append(f"{name}:{opening}: unclosed opening brace")
    for env, opening in envs:
        errors.append(f"{name}:{opening}: unclosed environment {env}")
    for delimiter, opening in math:
        errors.append(f"{name}:{opening}: unclosed math delimiter {delimiter}")
    return errors


def load_table(path: Path, delimiter: str, required: list[str], errors: list[str]):
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream, delimiter=delimiter)
            if reader.fieldnames != required:
                errors.append(
                    f"{path.name}: header {reader.fieldnames!r}; expected {required!r}"
                )
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{path.name}: cannot read table: {exc}")
        return []
    for number, row in enumerate(rows, 2):
        if None in row or any(value is None for value in row.values()):
            errors.append(f"{path.name}:{number}: malformed column count")
    return rows


def disallowed_member(name: str) -> str | None:
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or "\\" in name:
        return "unsafe member path"
    if path.suffix.lower() in IMAGE_EXTENSIONS:
        return "image or PDF included"
    if path.suffix.lower() == ".zip":
        return "nested ZIP/checkpoint/source archive included"
    for part in path.parts:
        lower = part.lower()
        if lower in {"source", "upload", "scans", "witnesses", "context", "hua", "codex"}:
            return "source-attachment directory included"
        if lower.endswith(("_scans", "_witnesses", "_context")):
            return "source-attachment directory included"
    if path.name == "PROMPT.md" or path.name.startswith("PROMPT("):
        return "attached prompt included"
    return None


def validate(root: Path, archive: Path | None) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    hashes: dict[str, str] = {}
    counts: dict[str, object] = {}
    for relative in REQUIRED:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"empty required file: {relative}")
    actual_pages = {path.name for path in (root / "pages").glob("*.tex")}
    extra_pages = sorted(actual_pages - set(PAGE_NAMES))
    if extra_pages:
        errors.append(f"unexpected page files: {extra_pages}")
    page_texts: list[str] = []
    for name, (_, cote, scan) in zip(PAGE_NAMES, PAGES):
        path = root / "pages" / name
        if not path.is_file():
            continue
        try:
            data = path.read_bytes()
            text = data.decode("utf-8-sig")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{name}: cannot read UTF-8: {exc}")
            continue
        hashes[f"pages/{name}"] = sha256(data)
        page_texts.append(text)
        errors.extend(tex_checks(text, name))
        clean = strip_comments(text)
        scans = re.findall(r"\\scanpage\s*\{([^{}]+)\}", clean)
        if scans != [str(scan)]:
            errors.append(f"{name}: scan markers {scans!r}; expected {[str(scan)]!r}")
        cotes = re.findall(r"\\cotefile\s*\{([^{}]+)\}", clean)
        if any(value != cote for value in cotes):
            errors.append(f"{name}: wrong cote marker {cotes!r}")
    combined_path = root / f"{PREFIX}_transcription.tex"
    if combined_path.is_file():
        try:
            data = combined_path.read_bytes()
            combined = data.decode("utf-8-sig")
            hashes[combined_path.name] = sha256(data)
            errors.extend(tex_checks(combined, combined_path.name))
            clean = strip_comments(combined)
            if re.search(r"\\(?:documentclass|usepackage)\b|\\begin\{document\}", clean):
                errors.append("combined transcription contains a preamble/document wrapper")
            expected_markers = []
            prior_cote = None
            for _, cote, scan in PAGES:
                if cote != prior_cote:
                    expected_markers.append(("cotefile", cote))
                    prior_cote = cote
                expected_markers.append(("scanpage", str(scan)))
            markers = re.findall(r"\\(cotefile|scanpage)\s*\{([^{}]+)\}", clean)
            if markers != expected_markers:
                errors.append(f"combined cote/scan order is {markers!r}; expected {expected_markers!r}")
            # Cote headers may be supplied by the assembler instead of the
            # individual page files. Their exact order was checked above.
            # Remove only those headers, comments, and whitespace for this
            # content-equivalence check.
            def canonical(value: str) -> str:
                value = strip_comments(value)
                value = re.sub(r"\\cotefile\s*\{[^{}]+\}", "", value)
                return re.sub(r"\s+", "", value)
            if len(page_texts) == 11 and canonical(combined) != canonical("\n".join(page_texts)):
                errors.append("combined fragment differs from concatenated page files")
            counts["macros_in_page_files"] = {
                macro: sum(len(re.findall(r"\\" + macro + r"\s*\{", text)) for text in page_texts)
                for macro in ("unsure", "illegible", "deleted", "inserted", "margin", "diagram", "figure")
            }
        except (OSError, UnicodeError) as exc:
            errors.append(f"combined transcription cannot be read: {exc}")
    collation = load_table(root / f"{PREFIX}_collation.tsv", "\t", COLLATION_FIELDS, errors)
    valid_pairs = {(folder, str(scan)) for folder, _, scan in PAGES}
    for number, row in enumerate(collation, 2):
        if row.get("kind") not in COLLATION_KINDS:
            errors.append(f"collation:{number}: invalid kind {row.get('kind')!r}")
        if row.get("confidence") not in CONFIDENCES:
            errors.append(f"collation:{number}: invalid confidence {row.get('confidence')!r}")
        try:
            scan = int(row.get("our_scan", ""))
            if int(row.get("their_page", "")) != scan - 1:
                errors.append(f"collation:{number}: their_page is not our_scan - 1")
            if (row.get("folder"), str(scan)) not in valid_pairs:
                errors.append(f"collation:{number}: unrequested folder/scan")
        except (ValueError, TypeError):
            errors.append(f"collation:{number}: noninteger page/scan")
        if not (row.get("marked_in_H") or "").strip():
            errors.append(f"collation:{number}: empty marked_in_H")
    inventory = load_table(root / f"{PREFIX}_inventory.csv", ",", INVENTORY_FIELDS, errors)
    for number, row in enumerate(inventory, 2):
        if row.get("transcribed") != "yes":
            errors.append(f"inventory:{number}: transcribed is not yes")
        if row.get("kind") not in INVENTORY_KINDS:
            errors.append(f"inventory:{number}: invalid kind {row.get('kind')!r}")
        if row.get("sheet_kind") not in SHEET_KINDS:
            errors.append(f"inventory:{number}: invalid sheet_kind {row.get('sheet_kind')!r}")
    events = root / "CHECK_EVENTS.tsv"
    if events.is_file():
        try:
            with events.open(encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream, delimiter="\t")
                fields = reader.fieldnames or []
                aliases = {
                    "statement id": {"statement_id", "statement id", "statement"},
                    "date": {"date", "date_utc", "timestamp", "timestamp_utc"},
                    "who": {"who", "reader", "agent", "model_effort_run"},
                    "type": {"type", "event_type", "check_type"},
                    "outcome": {"outcome", "result"},
                }
                normalized = {field.lower().strip() for field in fields}
                for concept, acceptable in aliases.items():
                    if not normalized.intersection(acceptable):
                        if concept == "who" and {"model", "effort", "run"}.issubset(normalized):
                            continue
                        errors.append(f"CHECK_EVENTS.tsv: missing {concept} column")
                event_rows = list(reader)
                counts["check_events"] = len(event_rows)
                for number, row in enumerate(event_rows, 2):
                    if None in row or any(value is None for value in row.values()):
                        errors.append(f"CHECK_EVENTS.tsv:{number}: malformed column count")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"CHECK_EVENTS.tsv: cannot read: {exc}")
    counts["page_files"] = len(page_texts)
    counts["collation_rows"] = len(collation)
    counts["inventory_rows"] = len(inventory)
    counts["collation_by_kind"] = dict(Counter(row.get("kind", "") for row in collation))
    counts["collation_by_confidence"] = dict(Counter(row.get("confidence", "") for row in collation))
    for path in root.rglob("*"):
        if path.is_file():
            relative = path.relative_to(root).as_posix()
            reason = disallowed_member(relative)
            if reason:
                errors.append(f"output directory: {reason}: {relative}")
    if archive:
        try:
            with zipfile.ZipFile(archive) as package:
                members = [item for item in package.infolist() if not item.is_dir()]
                names = [item.filename for item in members]
                duplicates = [name for name, count in Counter(names).items() if count > 1]
                if duplicates:
                    errors.append(f"ZIP duplicate members: {duplicates!r}")
                prefix = ""
                if names and not any(name in REQUIRED for name in names):
                    roots = {name.split("/", 1)[0] for name in names}
                    if len(roots) == 1 and all("/" in name for name in names):
                        prefix = next(iter(roots)) + "/"
                logical = {name[len(prefix):]: name for name in names}
                for relative in REQUIRED:
                    if relative not in logical:
                        errors.append(f"ZIP missing required file: {relative}")
                for item in members:
                    reason = disallowed_member(item.filename)
                    if reason:
                        errors.append(f"ZIP: {reason}: {item.filename}")
                        continue
                    relative = item.filename[len(prefix):]
                    local = root / relative
                    if not local.is_file():
                        errors.append(f"ZIP member has no matching output file: {relative}")
                    elif sha256(package.read(item)) != sha256(local.read_bytes()):
                        errors.append(f"ZIP bytes differ from output file: {relative}")
                bad_member = package.testzip()
                if bad_member:
                    errors.append(f"ZIP CRC failure: {bad_member}")
                counts["zip_members"] = len(members)
                counts["zip_bytes"] = archive.stat().st_size
        except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
            errors.append(f"cannot validate ZIP: {exc}")
    return {
        "status": "PASS" if not errors else "FAIL",
        "scope": "Mechanical structure only; no manuscript reading or textual judgment.",
        "output_directory": str(root),
        "archive": str(archive) if archive else None,
        "counts": counts,
        "sha256": hashes,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--zip", dest="archive", type=Path)
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args()
    report = validate(args.output_directory.resolve(), args.archive.resolve() if args.archive else None)
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Structural validation: {report['status']}")
        print(report["scope"])
        print("Counts: " + json.dumps(report["counts"], ensure_ascii=False, sort_keys=True))
        for error in report["errors"]:
            print("ERROR: " + error)
        for warning in report["warnings"]:
            print("WARNING: " + warning)
        print("SHA-256 (transcription files):")
        for name, digest in report["sha256"].items():
            print(f"{digest}  {name}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
