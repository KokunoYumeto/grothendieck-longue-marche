#!/usr/bin/env python3
"""Check package structure only; does not assess or change any reading.

Run after the transcription package has been assembled. A frozen manifest,
when present, must be either {"relative/path": "sha256", ...} or
{"files": {"relative/path": "sha256", ...}, ...}.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
import re
import sys
from pathlib import Path


STEM = "MPL_154_077-126"
SCANS = tuple(n for n in range(77, 127) if n != 99)
COLUMNS = (
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
MACRO_KINDS = {
    "figure": "drawing", "diagram": "diagram", "margin": "margin note",
    "inserted": "insertion", "deleted": "deletion", "displayed math": "display",
}
DISPLAY_ENVIRONMENTS = {
    b"displaymath", b"equation", b"equation*", b"align", b"align*",
    b"alignat", b"alignat*", b"flalign", b"flalign*", b"gather", b"gather*",
    b"multline", b"multline*", b"eqnarray", b"eqnarray*", b"xalignat",
    b"xalignat*", b"xxalignat", b"xxalignat*",
}


def structural_tex(data: bytes) -> bytes:
    """Remove literal-code regions and comments without interpreting prose."""
    data = re.sub(
        rb"\\begin\s*\{(verbatim\*?|Verbatim|lstlisting|minted)\}.*?"
        rb"\\end\s*\{\1\}", b"", data, flags=re.DOTALL,
    )
    data = re.sub(rb"\\verb\*?([^A-Za-z\s])(.*?)\1", b"", data)
    lines: list[bytes] = []
    for line in data.splitlines(keepends=True):
        for pos, char in enumerate(line):
            if char != 37:  # percent sign
                continue
            preceding = pos - 1
            while preceding >= 0 and line[preceding] == 92:
                preceding -= 1
            if (pos - preceding - 1) % 2 == 0:
                line = line[:pos] + (b"\n" if line.endswith(b"\n") else b"")
                break
        lines.append(line)
    return b"".join(lines)


def count_structural_macros(data: bytes) -> Counter[str]:
    """Count only control tokens and display delimiters, never textual claims."""
    data = structural_tex(data)
    counts: Counter[str] = Counter()
    position = 0
    dollar_display_open = False
    while position < len(data):
        char = data[position]
        if char == 92:  # backslash
            token = re.match(rb"\\([A-Za-z@]+|.)", data[position:], flags=re.DOTALL)
            if token is None:
                position += 1
                continue
            name = token.group(1)
            position += token.end()
            if name in (b"figure", b"diagram", b"margin", b"inserted", b"deleted"):
                counts[name.decode("ascii")] += 1
            elif name == b"[":
                counts["displayed math"] += 1
            elif name == b"begin":
                environment = re.match(rb"\s*\{([^{}]+)\}", data[position:])
                if environment is not None and environment.group(1) in DISPLAY_ENVIRONMENTS:
                    counts["displayed math"] += 1
            continue
        if data[position:position + 2] == b"$$":
            if not dollar_display_open:
                counts["displayed math"] += 1
            dollar_display_open = not dollar_display_open
            position += 2
            continue
        position += 1
    return counts


def check_package(
    root: Path, *, require_frozen: bool = False,
    warnings: list[str] | None = None,
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    facts: list[str] = []
    if warnings is None:
        warnings = []
    required = (
        f"{STEM}_transcription.tex", f"{STEM}_doubts.md",
        f"{STEM}_inventory.csv", f"{STEM}_notes.md", "progress.log",
    )
    for name in required:
        path = root / name
        if not path.is_file():
            errors.append(f"Missing deliverable: {name}")
        elif path.stat().st_size == 0:
            errors.append(f"Empty deliverable: {name}")

    expected_names = {f"{STEM}_154_scan{n:03d}.tex" for n in SCANS}
    page_dir = root / "pages"
    actual_names = {p.name for p in page_dir.glob("*.tex")}
    for name in sorted(expected_names - actual_names):
        errors.append(f"Missing page: pages/{name}")
    for name in sorted(actual_names - expected_names):
        errors.append(f"Unexpected page: pages/{name}")

    page_bytes: list[bytes] = []
    macro_counts: dict[int, Counter[str]] = {}
    for scan in SCANS:
        path = page_dir / f"{STEM}_154_scan{scan:03d}.tex"
        if not path.is_file():
            continue
        data = path.read_bytes()
        page_bytes.append(data)
        macro_counts[scan] = count_structural_macros(data)
        structure = structural_tex(data)
        markers = re.findall(rb"\\scanpage\s*\{\s*(\d+)\s*\}", structure)
        if tuple(map(int, markers)) != (scan,):
            errors.append(f"Wrong or repeated scan marker: pages/{path.name}")
        if re.search(rb"\\(?:documentclass|begin\s*\{document\})", structure):
            errors.append(f"Page contains a document preamble/body wrapper: {path.name}")

    combined = root / f"{STEM}_transcription.tex"
    if combined.is_file() and len(page_bytes) == len(SCANS):
        combined_bytes = combined.read_bytes()
        if combined_bytes != b"".join(page_bytes):
            errors.append("Combined transcription is not the exact ordered concatenation of page files")
        combined_structure = structural_tex(combined_bytes)
        if not re.match(
            rb"\s*\\cotefile\s*\{\s*154\s*\}\s*\\scanpage\s*\{\s*0*77\s*\}",
            combined_structure,
        ):
            errors.append("Combined transcription does not begin with cotefile 154 and scanpage 77")
        all_markers = re.findall(rb"\\scanpage\s*\{\s*(\d+)\s*\}", combined_structure)
        if tuple(map(int, all_markers)) != SCANS:
            errors.append("Combined scan markers are not the expected 49 scans in order")
        facts.append(f"Page files checked: {len(page_bytes)}")

    inventory = root / f"{STEM}_inventory.csv"
    if inventory.is_file():
        try:
            with inventory.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                if tuple(reader.fieldnames or ()) != COLUMNS:
                    errors.append(f"Inventory columns differ from {','.join(COLUMNS)}")
                rows = list(reader)
            seen_scans: set[int] = set()
            seen_elements: set[tuple[str, str, str]] = set()
            kinds_by_scan: dict[int, Counter[str]] = defaultdict(Counter)
            sheet_kinds_by_scan: dict[int, set[str]] = defaultdict(set)
            for line, row in enumerate(rows, 2):
                if None in row:
                    errors.append(f"Inventory line {line}: extra CSV fields")
                if row.get("cote") != "154":
                    errors.append(f"Inventory line {line}: cote is not 154")
                scan = None
                try:
                    scan = int(row.get("scan", ""))
                    seen_scans.add(scan)
                    if scan not in SCANS:
                        errors.append(f"Inventory line {line}: unexpected scan {scan}")
                except (ValueError, TypeError):
                    errors.append(f"Inventory line {line}: invalid scan")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    errors.append(f"Inventory line {line}: invalid sheet_kind")
                if row.get("kind") not in ELEMENT_KINDS:
                    errors.append(f"Inventory line {line}: invalid element kind")
                if scan in SCANS:
                    kinds_by_scan[scan][row.get("kind", "")] += 1
                    sheet_kinds_by_scan[scan].add(row.get("sheet_kind", ""))
                if row.get("transcribed") != "yes":
                    errors.append(f"Inventory line {line}: transcribed is not yes")
                for field in ("element", "position", "first_words_or_objects"):
                    if not (row.get(field) or "").strip():
                        errors.append(f"Inventory line {line}: empty {field}")
                # Normalize numeric scan identifiers so 77 and 077 cannot
                # disguise repeated identifiers within the same scan.
                scan_key = str(scan) if scan is not None else row.get("scan", "")
                key = (row.get("cote", ""), scan_key, row.get("element", ""))
                if key in seen_elements:
                    errors.append(f"Inventory line {line}: repeated element identifier {key}")
                seen_elements.add(key)
            for scan in sorted(set(SCANS) - seen_scans):
                errors.append(f"Inventory has no rows for scan {scan:03d}")
            for scan, sheet_kinds in sorted(sheet_kinds_by_scan.items()):
                if len(sheet_kinds) > 1:
                    errors.append(
                        f"Inventory scan {scan:03d}: inconsistent sheet_kind values "
                        + ", ".join(sorted(str(kind) for kind in sheet_kinds))
                    )
            for scan, macros in sorted(macro_counts.items()):
                for macro, kind in MACRO_KINDS.items():
                    occurrences = macros[macro]
                    row_count = kinds_by_scan[scan][kind]
                    label = macro if macro == "displayed math" else "\\" + macro
                    if occurrences and not row_count:
                        warnings.append(
                            f"Scan {scan:03d}: {label} is present ({occurrences} occurrence(s)), "
                            f"but inventory kind '{kind}' is absent"
                        )
                    elif row_count and not occurrences:
                        warnings.append(
                            f"Scan {scan:03d}: inventory kind '{kind}' is present ({row_count} row(s)), "
                            f"but {label} was not detected"
                        )
            facts.append(f"Inventory rows checked: {len(rows)}")
            facts.append(
                "Macro/inventory checks compare presence by scan only; no count equality is required"
            )
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"Cannot parse inventory: {exc}")

    manifest = root / "records" / "frozen_hashes.json"
    if manifest.is_file():
        try:
            value = json.loads(manifest.read_text(encoding="utf-8"))
            hashes = value.get("files", value) if isinstance(value, dict) else None
            if not isinstance(hashes, dict):
                raise ValueError("manifest must be a mapping, optionally under the key 'files'")
            required_hash_paths = {f"pages/{name}" for name in expected_names}
            required_hash_paths.add(f"{STEM}_transcription.tex")
            for name in sorted(required_hash_paths - hashes.keys()):
                errors.append(f"Frozen manifest lacks {name}")
            checked = 0
            for name, digest in hashes.items():
                if not isinstance(name, str) or not isinstance(digest, str):
                    errors.append("Frozen manifest contains a non-string path or digest")
                    continue
                if not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
                    errors.append(f"Invalid SHA-256 digest for {name}")
                    continue
                path = (root / name).resolve()
                if not path.is_relative_to(root.resolve()):
                    errors.append(f"Frozen manifest path escapes package: {name}")
                    continue
                if not path.is_file():
                    errors.append(f"Frozen file is missing: {name}")
                    continue
                observed = hashlib.sha256(path.read_bytes()).hexdigest()
                if observed != digest.lower():
                    errors.append(f"Frozen SHA-256 mismatch: {name}")
                checked += 1
            facts.append(f"Frozen SHA-256 entries checked: {checked}")
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"Cannot verify frozen manifest: {exc}")
    else:
        if require_frozen:
            errors.append("Final verification requires records/frozen_hashes.json; manifest is absent")
        else:
            facts.append("No frozen-hash manifest present; hash verification not performed")

    return errors, facts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--require-frozen", action="store_true",
        help="Require a complete, matching frozen-hash manifest for final verification",
    )
    args = parser.parse_args()
    warnings: list[str] = []
    errors, facts = check_package(args.root, require_frozen=args.require_frozen, warnings=warnings)
    for fact in facts:
        print(fact)
    for warning in warnings:
        print(f"WARNING: {warning}")
    if warnings:
        print(f"Advisory macro/inventory warnings: {len(warnings)}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Structural validation failed: {len(errors)} issue(s)", file=sys.stderr)
        return 1
    print("Structural validation passed. This check does not certify the readings or inventory completeness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
