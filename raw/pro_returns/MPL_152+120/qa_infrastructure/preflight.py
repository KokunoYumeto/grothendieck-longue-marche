#!/usr/bin/env python3
"""Nonsemantic checks, assembly, and hashing for the 38-page transcription.

No command modifies page files, the inventory, doubts, notes, or progress.log.
Diagnostics contain filenames, positions, counts, and structural status only.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re
import sys


PREFIX = "MPL_152+120"
COTE_COUNTS = ((152, 13), (120, 25))
PAGES = tuple((cote, scan, f"{PREFIX}_{cote}_scan{scan:03d}.tex")
              for cote, count in COTE_COUNTS for scan in range(1, count + 1))
COMBINED = f"{PREFIX}_transcription.tex"
INVENTORY = f"{PREFIX}_inventory.csv"
MANIFEST = "qa_infrastructure/transcription.sha256"
COLUMNS = ("cote", "scan", "sheet_kind", "element", "kind", "position",
           "first_words_or_objects", "transcribed")
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
COUNTED_MACROS = ("unsure", "illegible", "deleted", "inserted", "margin",
                  "uline", "uuline", "diagram", "figure")
EXPECTED_PATHS = tuple("pages/" + name for _, _, name in PAGES) + (COMBINED,)
CONTROL_WORD = re.compile(r"[A-Za-z@]+")
SIMPLE_ARGUMENT = re.compile(r"\s*\{\s*([^{}]*?)\s*\}")


def without_comments(source: str) -> str:
    """Replace TeX comments with spaces, preserving offsets and newlines."""
    result: list[str] = []
    index = 0
    while index < len(source):
        char = source[index]
        if char == "\\":
            match = CONTROL_WORD.match(source, index + 1)
            end = match.end() if match else min(index + 2, len(source))
            if match and match.group() == "verb":
                if end < len(source) and source[end] == "*":
                    end += 1
                if end < len(source) and source[end] != "\n":
                    stop = source.find(source[end], end + 1)
                    end = stop + 1 if stop >= 0 else len(source)
            result.append(source[index:end])
            index = end
        elif char == "%":
            stop = source.find("\n", index)
            if stop < 0:
                stop = len(source)
            result.append(" " * (stop - index))
            index = stop
        else:
            result.append(char)
            index += 1
    return "".join(result)


def inspect_tex(source: str) -> dict:
    """Lexical checks only; this function does not interpret manuscript prose."""
    clean = without_comments(source)
    braces: list[int] = []
    environments: list[tuple[str, int]] = []
    errors: list[str] = []
    markers: list[tuple[str, str | None, int]] = []
    counts = Counter({name: 0 for name in COUNTED_MACROS})
    illegible_word_estimate = 0
    index = 0
    while index < len(clean):
        char = clean[index]
        line = clean.count("\n", 0, index) + 1
        if char == "\\":
            match = CONTROL_WORD.match(clean, index + 1)
            if not match:
                index = min(index + 2, len(clean))
                continue
            command = match.group()
            index = match.end()
            if command == "verb":
                if index < len(clean) and clean[index] == "*":
                    index += 1
                if index >= len(clean) or clean[index] == "\n":
                    errors.append(f"Malformed verb delimiter at line {line}")
                else:
                    stop = clean.find(clean[index], index + 1)
                    if stop < 0:
                        errors.append(f"Unclosed verb delimiter at line {line}")
                        index = len(clean)
                    else:
                        index = stop + 1
                continue
            if command in COUNTED_MACROS:
                counts[command] += 1
            if command in {"cotefile", "scanpage", "begin", "end", "illegible"}:
                argument_match = SIMPLE_ARGUMENT.match(clean, index)
                argument = argument_match.group(1).strip() if argument_match else None
                if command in {"cotefile", "scanpage"}:
                    markers.append((command, argument, line))
                elif command == "illegible":
                    if argument is not None and argument.isdigit():
                        illegible_word_estimate += int(argument)
                elif command == "begin":
                    if not argument:
                        errors.append(f"Malformed environment start at line {line}")
                    else:
                        environments.append((argument, line))
                elif command == "end":
                    if not argument:
                        errors.append(f"Malformed environment end at line {line}")
                    elif not environments:
                        errors.append(f"Environment end without start at line {line}")
                    else:
                        opened, open_line = environments.pop()
                        if opened != argument:
                            errors.append(f"Environment-end mismatch at line {line}; start at line {open_line}")
            continue
        if char == "{":
            braces.append(line)
        elif char == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"Closing brace without opening brace at line {line}")
        index += 1
    for line in braces:
        errors.append(f"Unclosed brace opened at line {line}")
    for _, line in environments:
        errors.append(f"Unclosed environment opened at line {line}")
    return {"errors": errors, "markers": markers, "macro_counts": dict(counts),
            "illegible_word_estimate": illegible_word_estimate, "clean": clean}


def expected_marker_sequence() -> list[tuple[str, int]]:
    result = []
    for cote, count in COTE_COUNTS:
        result.append(("cotefile", cote))
        result.extend(("scanpage", scan) for scan in range(1, count + 1))
    return result


def numeric_markers(markers: list[tuple[str, str | None, int]]) -> list[tuple[str, int | None]]:
    return [(command, int(value) if value is not None and value.isdigit() else None)
            for command, value, _ in markers]


def combined_bytes(root: Path) -> bytes:
    # Preserve every source byte. Exactly one LF separates consecutive files.
    return b"\n".join((root / "pages" / name).read_bytes() for _, _, name in PAGES)


def inspect_inventory(root: Path) -> dict:
    path = root / INVENTORY
    result = {"rows": 0, "page_counts": {}, "errors": []}
    errors = result["errors"]
    if not path.is_file():
        errors.append("Inventory file is missing")
        return result
    expected_pages = {(cote, scan) for cote, scan, _ in PAGES}
    rank = {(cote, scan): index for index, (cote, scan, _) in enumerate(PAGES)}
    ids = set()
    counts = Counter()
    sheet_kinds = defaultdict(set)
    previous_rank = -1
    try:
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            if tuple(reader.fieldnames or ()) != COLUMNS:
                errors.append("Inventory columns differ from the eight required columns or their order")
                return result
            for row_index, row in enumerate(reader, start=2):
                result["rows"] += 1
                label = f"Inventory record {row_index}"
                if None in row or any(row.get(column) is None for column in COLUMNS):
                    errors.append(label + ": field count differs from header")
                    continue
                for column in COLUMNS:
                    if not row[column].strip():
                        errors.append(label + f": empty {column} field")
                if row["transcribed"].strip() != "yes":
                    errors.append(label + ": transcribed is not yes")
                if row["sheet_kind"].strip() not in SHEET_KINDS:
                    errors.append(label + ": unrecognized sheet_kind")
                if row["kind"].strip() not in ELEMENT_KINDS:
                    errors.append(label + ": unrecognized element kind")
                try:
                    page = (int(row["cote"]), int(row["scan"]))
                except ValueError:
                    errors.append(label + ": cote or scan is not an integer")
                    continue
                if page not in expected_pages:
                    errors.append(label + ": page is outside the expected 38-page sequence")
                    continue
                counts[page] += 1
                sheet_kinds[page].add(row["sheet_kind"].strip())
                identity = (page, row["element"].strip())
                if identity in ids:
                    errors.append(label + ": duplicate (cote, scan, element) identifier")
                ids.add(identity)
                if rank[page] < previous_rank:
                    errors.append(label + ": page order moves backwards")
                previous_rank = max(previous_rank, rank[page])
    except (OSError, UnicodeError, csv.Error) as error:
        errors.append(f"Inventory read failed ({type(error).__name__})")
    for cote, scan, _ in PAGES:
        page = (cote, scan)
        if not counts[page]:
            errors.append(f"Inventory has no rows for cote {cote} scan {scan:03d}")
        if len(sheet_kinds[page]) > 1:
            errors.append(f"Inventory has multiple sheet_kind values for cote {cote} scan {scan:03d}")
        result["page_counts"][f"{cote}:{scan:03d}"] = counts[page]
    return result


def inspect_package(root: Path, *, require_combined: bool = False,
                    inspect_existing_combined: bool = True) -> dict:
    result = {"status": "pass", "expected_pages": len(PAGES), "pages": [],
              "macro_totals": {name: 0 for name in COUNTED_MACROS},
              "illegible_word_estimate": 0, "errors": []}
    errors = result["errors"]
    page_dir = root / "pages"
    found = {path.name for path in page_dir.glob("*.tex") if path.is_file()}
    expected = {name for _, _, name in PAGES}
    result["found_page_files"] = len(found)
    for name in sorted(expected - found):
        errors.append("Missing page file: " + name)
    for name in sorted(found - expected):
        errors.append("Unexpected page file: " + name)
    for cote, scan, name in PAGES:
        path = page_dir / name
        if not path.is_file():
            continue
        try:
            data = path.read_bytes()
            text = data.decode("utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{name}: read failed ({type(error).__name__})")
            continue
        page = inspect_tex(text)
        errors.extend(name + ": " + issue for issue in page["errors"])
        expected_markers = ([("cotefile", cote)] if scan == 1 else []) + [("scanpage", scan)]
        if numeric_markers(page["markers"]) != expected_markers:
            errors.append(name + ": cote/scan markers or their order differ from the expected page markers")
        opening = (rf"\s*\\cotefile\s*\{{\s*{cote}\s*\}}" if scan == 1 else "")
        opening += rf"\s*\\scanpage\s*\{{\s*0*{scan}\s*\}}"
        if not re.match(opening, page["clean"]):
            errors.append(name + ": expected page marker is not at the start of the uncommented fragment")
        for macro, count in page["macro_counts"].items():
            result["macro_totals"][macro] += count
        result["illegible_word_estimate"] += page["illegible_word_estimate"]
        result["pages"].append({"cote": cote, "scan": scan, "file": name,
                                 "bytes": len(data), "macro_counts": page["macro_counts"],
                                 "illegible_word_estimate": page["illegible_word_estimate"]})
    result["inventory"] = inspect_inventory(root)
    errors.extend(result["inventory"]["errors"])
    combined = root / COMBINED
    if inspect_existing_combined and combined.is_file():
        try:
            data = combined.read_bytes()
            checked = inspect_tex(data.decode("utf-8"))
            errors.extend(COMBINED + ": " + issue for issue in checked["errors"])
            if numeric_markers(checked["markers"]) != expected_marker_sequence():
                errors.append(COMBINED + ": cote/scan sequence differs from the required order")
            if expected <= found and data != combined_bytes(root):
                errors.append(COMBINED + ": bytes differ from the ordered page concatenation with one LF separator")
            result["combined"] = {"present": True, "bytes": len(data)}
        except (OSError, UnicodeError) as error:
            errors.append(COMBINED + f": read failed ({type(error).__name__})")
    else:
        result["combined"] = {"present": combined.is_file(), "checked": False}
        if require_combined:
            errors.append("Combined transcription is missing")
    if errors:
        result["status"] = "fail"
    return result


def write_new_or_same(path: Path, data: bytes, *, replace: bool = False) -> str:
    if path.exists():
        if path.read_bytes() == data:
            return "unchanged"
        if not replace:
            raise ValueError("Refusing to replace a different existing output; choose a new output or explicitly use --replace")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return "written"


def guard_auxiliary_output(root: Path, output: Path) -> None:
    resolved = output.resolve()
    pages = (root / "pages").resolve()
    protected = {root / COMBINED, root / INVENTORY, root / "progress.log",
                 root / f"{PREFIX}_doubts.md", root / f"{PREFIX}_notes.md"}
    if resolved == pages or pages in resolved.parents or resolved in {path.resolve() for path in protected}:
        raise ValueError("Auxiliary output cannot replace a page or a required deliverable")


def manifest_bytes(root: Path) -> bytes:
    return "".join(hashlib.sha256((root / name).read_bytes()).hexdigest() + "  " + name + "\n"
                   for name in EXPECTED_PATHS).encode("ascii")


def verify_manifest(root: Path, path: Path) -> dict:
    errors = []
    entries = []
    try:
        for line_number, line in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
            match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
            if not match:
                errors.append(f"Manifest line {line_number}: malformed SHA-256 record")
            else:
                entries.append((match.group(1), match.group(2)))
    except (OSError, UnicodeError) as error:
        errors.append(f"Manifest read failed ({type(error).__name__})")
    if tuple(name for _, name in entries) != EXPECTED_PATHS:
        errors.append("Manifest entries differ from the required 38 pages followed by the combined file")
    for digest, name in entries:
        # Read only the exact known paths, regardless of manifest contents.
        if name not in EXPECTED_PATHS:
            continue
        path = root / name
        if not path.is_file():
            errors.append("Manifest target is missing: " + name)
        elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append("SHA-256 mismatch: " + name)
    return {"status": "fail" if errors else "pass", "manifest_entries": len(entries),
            "expected_entries": len(EXPECTED_PATHS), "errors": errors}


def main() -> int:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    common.add_argument("--report", type=Path, help="Optional structural JSON report; no manuscript prose")
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", parents=[common], help="Read-only structural preflight")
    check.add_argument("--require-combined", action="store_true")
    build = commands.add_parser("build", parents=[common], help="Create the combined fragment in exact order")
    build.add_argument("--replace", action="store_true", help="Explicitly replace an earlier combined output; use only before freeze")
    manifest = commands.add_parser("manifest", parents=[common], help="Write 39 SHA-256 records after successful preflight")
    manifest.add_argument("--manifest", type=Path)
    verify = commands.add_parser("verify", parents=[common], help="Verify all 39 records without modifying anything")
    verify.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "verify":
            result = verify_manifest(root, args.manifest or root / MANIFEST)
        else:
            result = inspect_package(root,
                                     require_combined=(args.command == "manifest" or
                                                       getattr(args, "require_combined", False)),
                                     inspect_existing_combined=args.command != "build")
            if result["status"] == "pass" and args.command == "build":
                result["build"] = write_new_or_same(root / COMBINED, combined_bytes(root), replace=args.replace)
                result["output"] = str(root / COMBINED)
            elif result["status"] == "pass" and args.command == "manifest":
                output = args.manifest or root / MANIFEST
                guard_auxiliary_output(root, output)
                result["manifest"] = write_new_or_same(output, manifest_bytes(root))
                result["manifest_entries"] = len(EXPECTED_PATHS)
                result["output"] = str(output)
    except (OSError, ValueError) as error:
        result = {"status": "fail", "errors": [f"{type(error).__name__}: {error}"]}
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        try:
            guard_auxiliary_output(root, args.report)
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(rendered, encoding="utf-8")
        except (OSError, ValueError) as error:
            result["status"] = "fail"
            result.setdefault("errors", []).append(f"Report output failed ({type(error).__name__}): {error}")
            rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    sys.stdout.write(rendered)
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
