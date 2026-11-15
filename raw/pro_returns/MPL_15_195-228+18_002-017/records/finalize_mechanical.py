#!/usr/bin/env python3
"""Assemble final derived files from the 49 primary-reader page fragments.

No manuscript interpretation, OCR, image access, context access, audit claim,
or freezing is performed. Page files, original inventory JSON records, the
main doubts document, and progress.log are never modified.

Default mode validates and reports planned outputs without writing anything.
Use --write only after the primary reader has completed the page readings and
corrections, before recording the transcription as frozen or opening context.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from dataclasses import dataclass
import hashlib
import io
import json
import os
from pathlib import Path
import re
import sys
import tempfile


PREFIX = "MPL_15_195-228+18_002-017"
EXPECTED = tuple([(15, n) for n in range(195, 229)] +
                 [(18, n) for n in range(2, 18) if n != 8])
FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
MANUAL_KINDS = {"text", "display", "diagram", "drawing"}
AUTO_KINDS = {"deleted": "deletion", "inserted": "insertion", "margin": "margin note"}
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
TARGETS = set(AUTO_KINDS) | {"unsure", "illegible", "cotefile", "scanpage"}


class MechanicalError(Exception):
    pass


@dataclass(frozen=True)
class Macro:
    name: str
    offset: int
    opening: int
    closing: int
    line: int
    column: int
    argument: str


def control_end(text: str, offset: int) -> int:
    """Return the end of one TeX control word or escaped control symbol."""
    index = offset + 1
    if index == len(text):
        return index
    if text[index].isalpha() or text[index] == "@":
        while index < len(text) and (text[index].isalpha() or text[index] == "@"):
            index += 1
        return index
    return index + 1


def lexical_mask(text: str) -> str:
    """Mask comments and verbatim bodies without changing character offsets."""
    result = list(text)

    def blank(start, end):
        for pos in range(start, end):
            if result[pos] not in "\r\n":
                result[pos] = " "

    index = 0
    while index < len(text):
        if text[index] == "%":
            end = text.find("\n", index)
            if end < 0:
                end = len(text)
            blank(index, end)
            index = end
            continue
        if text[index] != "\\":
            index += 1
            continue
        end = control_end(text, index)
        command = text[index + 1:end]
        if command == "verb":
            delimiter_pos = end + (end < len(text) and text[end] == "*")
            if delimiter_pos >= len(text) or text[delimiter_pos].isspace():
                raise MechanicalError("Malformed \\verb command")
            closing = text.find(text[delimiter_pos], delimiter_pos + 1)
            if closing < 0 or "\n" in text[delimiter_pos:closing]:
                raise MechanicalError("Unclosed \\verb command")
            blank(index, closing + 1)
            index = closing + 1
            continue
        if command == "begin":
            environment = re.match(r"\s*\{(verbatim\*?|Verbatim)\}", text[end:])
            if environment:
                name = environment.group(1)
                finish_token = "\\end{" + name + "}"
                body_start = end + environment.end()
                finish = text.find(finish_token, body_start)
                if finish < 0:
                    raise MechanicalError(f"Unclosed {name} environment")
                blank(index, finish + len(finish_token))
                index = finish + len(finish_token)
                continue
        index = end
    return "".join(result)


def balanced_groups(mask: str, filename: str) -> None:
    stack = []
    index = 0
    while index < len(mask):
        char = mask[index]
        if char == "\\":
            index = control_end(mask, index)
            continue
        if char == "{":
            stack.append(index)
        elif char == "}":
            if not stack:
                line = mask.count("\n", 0, index) + 1
                raise MechanicalError(f"{filename}: unmatched closing brace on TeX line {line}")
            stack.pop()
        index += 1
    if stack:
        lines = [mask.count("\n", 0, index) + 1 for index in stack]
        raise MechanicalError(f"{filename}: unmatched opening brace(s) on TeX line(s) {lines}")


def closing_brace(mask: str, opening: int) -> int:
    depth = 1
    index = opening + 1
    while index < len(mask):
        char = mask[index]
        if char == "\\":
            index = control_end(mask, index)
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    raise MechanicalError("Unclosed macro argument")


def scan_macros(text: str, filename: str) -> tuple[str, list[Macro]]:
    mask = lexical_mask(text)
    balanced_groups(mask, filename)
    found = []
    index = 0
    while index < len(mask):
        if mask[index] != "\\":
            index += 1
            continue
        end = control_end(mask, index)
        name = mask[index + 1:end]
        if name in TARGETS:
            opening = end
            while opening < len(mask) and mask[opening].isspace():
                opening += 1
            if opening >= len(mask) or mask[opening] != "{":
                line = mask.count("\n", 0, index) + 1
                raise MechanicalError(f"{filename}: \\{name} lacks a braced argument on TeX line {line}")
            closing = closing_brace(mask, opening)
            found.append(Macro(
                name=name, offset=index, opening=opening, closing=closing,
                line=mask.count("\n", 0, index) + 1,
                column=index - mask.rfind("\n", 0, index),
                argument=text[opening + 1:closing],
            ))
        # Continue through arguments, so nested target macros are also recorded.
        index = end
    return mask, found


def split_alternatives(argument: str) -> list[str]:
    r"""Split literal | only at brace depth zero, excluding escaped \|."""
    mask = lexical_mask(argument)
    depth = 0
    cuts = []
    index = 0
    while index < len(mask):
        char = mask[index]
        if char == "\\":
            index = control_end(mask, index)
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "|" and depth == 0:
            cuts.append(index)
        index += 1
    starts = [0] + [pos + 1 for pos in cuts]
    ends = cuts + [len(argument)]
    # Original arguments remain available separately in JSON. The parsed
    # reading fields omit comments/verbatim bodies consistently with the mask.
    return [mask[start:end].strip() for start, end in zip(starts, ends)]


def compact(value: str) -> str:
    return " ".join(value.split())


def md_code(value: str) -> str:
    value = compact(value).replace("|", "\\|")
    if not value:
        return "—"
    runs = re.findall(r"`+", value)
    fence = "`" * (max(map(len, runs), default=0) + 1)
    return fence + " " + value + " " + fence


def page_name(cote: int, scan: int) -> str:
    return f"{PREFIX}_{cote}_scan{scan:03d}.tex"


def read_inventory(path: Path, cote: int, scan: int):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise MechanicalError(f"Cannot read inventory record {path.name}: {exc}") from exc
    if not isinstance(data, list) or not data:
        raise MechanicalError(f"{path.name}: expected nonempty list of eight-field inventory rows")
    converted = []
    for index, row in enumerate(data, start=1):
        if not isinstance(row, list) or len(row) != len(FIELDS):
            raise MechanicalError(f"{path.name}: row {index} is not an eight-field list")
        try:
            pair = int(row[0]), int(row[1])
        except (TypeError, ValueError) as exc:
            raise MechanicalError(f"{path.name}: invalid cote/scan in row {index}") from exc
        if pair != (cote, scan):
            raise MechanicalError(f"{path.name}: row {index} refers to a different page")
        if row[2] not in SHEET_KINDS:
            raise MechanicalError(f"{path.name}: unknown sheet_kind in row {index}")
        if row[4] not in MANUAL_KINDS | set(AUTO_KINDS.values()):
            raise MechanicalError(f"{path.name}: unknown element kind in row {index}")
        if row[7] != "yes":
            raise MechanicalError(f"{path.name}: row {index} does not say transcribed=yes")
        converted.append(list(row))
    sheet_kinds = {row[2] for row in converted}
    if len(sheet_kinds) != 1:
        raise MechanicalError(f"{path.name}: inconsistent sheet_kind values")
    manual = [row for row in converted if row[4] in MANUAL_KINDS]
    identifiers = [str(row[3]) for row in manual]
    if len(set(identifiers)) != len(identifiers):
        raise MechanicalError(f"{path.name}: duplicate manual element identifiers")
    if any(not identifier.isdigit() for identifier in identifiers):
        raise MechanicalError(f"{path.name}: manual element identifiers must be numeric")
    old_auto_counts = Counter(row[4] for row in converted if row[4] not in MANUAL_KINDS)
    return manual, next(iter(sheet_kinds)), old_auto_counts


def make_outputs(root: Path):
    expected_names = {page_name(c, n) for c, n in EXPECTED}
    actual_names = {p.name for p in (root / "pages").glob("*.tex")}
    missing = expected_names - actual_names
    extra = actual_names - expected_names
    if missing or extra:
        raise MechanicalError("Exactly 49 page fragments are required. " +
                              f"Missing: {sorted(missing)}; extra: {sorted(extra)}")
    pieces = []
    inventory = []
    doubts = []
    page_reports = []
    input_hashes = {}
    for cote, scan in EXPECTED:
        name = page_name(cote, scan)
        path = root / "pages" / name
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
        except (OSError, UnicodeError) as exc:
            raise MechanicalError(f"Cannot read {name}: {exc}") from exc
        if raw.startswith(b"\xef\xbb\xbf"):
            raise MechanicalError(f"{name}: UTF-8 BOM is not allowed inside the combined fragment")
        pieces.append(raw)
        input_hashes["pages/" + name] = hashlib.sha256(raw).hexdigest()
        mask, macros = scan_macros(text, name)
        actual_markers = []
        for macro in macros:
            if macro.name in {"cotefile", "scanpage"}:
                value = lexical_mask(macro.argument).strip()
                if not value.isdigit():
                    raise MechanicalError(f"{name}: nonnumeric {macro.name} argument")
                actual_markers.append((macro.name, int(value)))
        target_markers = ([] if (cote, scan) not in {(15, 195), (18, 2)}
                          else [("cotefile", cote)]) + [("scanpage", scan)]
        if actual_markers != target_markers:
            raise MechanicalError(f"{name}: page/cote markers differ from required sequence {target_markers}")
        record_path = root / "records" / f"{cote}_{scan:03d}_inventory.json"
        manual, sheet_kind, old_auto_counts = read_inventory(record_path, cote, scan)
        # Preserve every field of each manual text/display/diagram/drawing row.
        inventory.extend(manual)
        next_id = max((int(row[3]) for row in manual), default=0) + 1
        new_auto_counts = Counter()
        page_doubt_counts = Counter()
        for macro in macros:
            if macro.name in AUTO_KINDS:
                kind = AUTO_KINDS[macro.name]
                inventory.append([
                    cote, scan, sheet_kind, f"{next_id:03d}", kind,
                    f"TeX line {macro.line}", compact(macro.argument)[:350], "yes",
                ])
                next_id += 1
                new_auto_counts[kind] += 1
            elif macro.name in {"unsure", "illegible"}:
                parts = split_alternatives(macro.argument)
                reading = parts[0]
                alternatives = parts[1:]
                if macro.name == "illegible":
                    reading = "\\illegible{" + lexical_mask(macro.argument).strip() + "}"
                    alternatives = []
                doubts.append({
                    "file": name, "cote": cote, "scan": scan,
                    "line": macro.line, "column": macro.column,
                    "offset": macro.offset, "macro": macro.name,
                    "argument_raw": macro.argument,
                    "reading": reading, "alternatives": alternatives,
                    "confidence": "medium" if macro.name == "unsure" else "low",
                })
                page_doubt_counts[macro.name] += 1
        page_reports.append({
            "cote": cote, "scan": scan, "manual_rows_preserved": len(manual),
            "old_auto_rows": dict(old_auto_counts),
            "new_auto_rows": dict(new_auto_counts),
            "doubts": dict(page_doubt_counts),
        })
    combined = b"".join(pieces)
    # Ensure concatenation did not join a trailing TeX comment to the next page.
    _, all_macros = scan_macros(combined.decode("utf-8"), "combined transcription")
    combined_markers = [(m.name, int(lexical_mask(m.argument).strip()))
                        for m in all_macros if m.name in {"cotefile", "scanpage"}]
    required_markers = []
    for cote, scan in EXPECTED:
        if (cote, scan) in {(15, 195), (18, 2)}:
            required_markers.append(("cotefile", cote))
        required_markers.append(("scanpage", scan))
    if combined_markers != required_markers:
        raise MechanicalError("Exact byte concatenation changes the required page-marker sequence")
    csv_buffer = io.StringIO(newline="")
    writer = csv.writer(csv_buffer, lineterminator="\n")
    writer.writerow(FIELDS)
    writer.writerows(inventory)
    table = [
        "# Doubt rows regenerated from the final page macros", "",
        "Mechanical extraction only. Confidence is assigned by macro: medium for `\\unsure`, low for `\\illegible`. "
        "TeX line numbers refer to individual page files. The notation table and abbreviation prose in the main doubts file are untouched. "
        "Exact raw arguments and character offsets are retained in `final_doubt_rows.jsonl`.", "",
        "| File | Cote | Scan | TeX line | Macro | Reading | Alternatives | Confidence |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in doubts:
        alternatives = "; ".join(md_code(value) for value in row["alternatives"]) or "—"
        table.append("| " + " | ".join([
            md_code(row["file"]), str(row["cote"]), f"{row['scan']:03d}", str(row["line"]),
            md_code("\\" + row["macro"]), md_code(row["reading"]), alternatives, row["confidence"],
        ]) + " |")
    table.extend(["", f"Total extracted doubt macros: {len(doubts)}.", ""])
    report = {
        "scope": "mechanical assembly only; no visual audit or freezing performed",
        "pages": len(pieces), "inventory_rows": len(inventory), "doubt_rows": len(doubts),
        "combined_sha256": hashlib.sha256(combined).hexdigest(),
        "input_page_sha256": input_hashes,
        "manual_inventory_rows": sum(p["manual_rows_preserved"] for p in page_reports),
        "auto_inventory_rows": sum(sum(p["new_auto_rows"].values()) for p in page_reports),
        "page_reports": page_reports,
        "ordering_note": "Original manual-row order and identifiers are preserved; regenerated auto rows follow each page's manual rows in TeX occurrence order.",
        "main_doubts_document_modified": False,
        "page_files_modified": False,
        "progress_log_modified": False,
    }
    outputs = {
        f"{PREFIX}_transcription.tex": combined,
        f"{PREFIX}_inventory.csv": csv_buffer.getvalue().encode("utf-8"),
        "records/final_doubt_rows.jsonl": "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in doubts).encode("utf-8"),
        "records/final_doubt_table.md": "\n".join(table).encode("utf-8"),
        "records/finalization_report.json": (json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    }
    return outputs, report


def write_outputs(root: Path, outputs, report):
    log = (root / "progress.log").read_text(encoding="utf-8") if (root / "progress.log").exists() else ""
    if re.search(r"^\s*(?:transcription frozen|context opened)\b", log, flags=re.I | re.M):
        raise MechanicalError("Refusing to write after a transcription-frozen or context-opened event")
    staged = []
    try:
        for relative, data in outputs.items():
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            descriptor, name = tempfile.mkstemp(prefix=".mechanical_", dir=target.parent)
            temporary = Path(name)
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
            staged.append((temporary, target))
        for relative, digest in report["input_page_sha256"].items():
            if hashlib.sha256((root / relative).read_bytes()).hexdigest() != digest:
                raise MechanicalError(f"Input page changed during assembly: {relative}")
        for temporary, target in staged:
            os.replace(temporary, target)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true", help="write the five derived outputs, before freeze/context only")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        outputs, report = make_outputs(root)
        if args.write:
            write_outputs(root, outputs, report)
        print(json.dumps({
            "mode": "written" if args.write else "dry-run; no files written",
            "pages": report["pages"], "inventory_rows": report["inventory_rows"],
            "manual_rows_preserved": report["manual_inventory_rows"],
            "auto_rows_regenerated": report["auto_inventory_rows"],
            "doubt_rows": report["doubt_rows"],
            "combined_sha256": report["combined_sha256"],
            "outputs": [str(root / relative) for relative in outputs],
            "scope": report["scope"],
        }, ensure_ascii=False, indent=2))
    except (MechanicalError, OSError) as exc:
        print(f"Mechanical finalization failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
