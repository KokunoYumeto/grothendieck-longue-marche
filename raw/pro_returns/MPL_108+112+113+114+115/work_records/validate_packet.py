#!/usr/bin/env python3
"""Check packet structure and frozen bytes; do not assess manuscript readings.

Run: python work_records/validate_packet.py [--root DELIVERABLE] [--hashes FILE]

The combined fragment must be the exact byte concatenation of the forty page
files in the prescribed order (no separator is inserted by this validator).
Optional frozen manifests may use sha256sum text or a JSON object mapping
root-relative filenames to SHA-256 digests. A JSON {"files": {...}} or
{"sha256": {...}} wrapper is also accepted. If supplied/present, the manifest
must cover all forty pages and the combined transcription. This utility never
writes, normalizes, or corrects any transcription, inventory, or hash file.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path

PREFIX = "MPL_108+112+113+114+115"
RANGES = ((108, 2, 6), (112, 2, 5), (113, 2, 13), (114, 2, 6), (115, 2, 15))
EXPECTED = [(c, n) for c, first, last in RANGES for n in range(first, last + 1)]
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
           "first_words_or_objects", "transcribed"]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note",
                 "insertion", "deletion"}


def strip_tex_comments(text: str) -> str:
    """Drop unescaped percent comments, preserving line counts and escaped %.

    An odd number of immediately preceding backslashes escapes a percent;
    an even number leaves it as the start of a comment.
    """
    output = []
    for line in text.splitlines(keepends=True):
        backslashes = 0
        for index, character in enumerate(line):
            if character == "%" and backslashes % 2 == 0:
                output.append(line[:index] + ("\n" if line.endswith("\n") else ""))
                break
            backslashes = backslashes + 1 if character == "\\" else 0
        else:
            output.append(line)
    return "".join(output)


def brace_errors(text: str) -> list[str]:
    """Check unescaped grouping braces after comments have been removed."""
    stack: list[int] = []
    issues = []
    line = 1
    backslashes = 0
    for character in strip_tex_comments(text):
        escaped = backslashes % 2 == 1
        if character == "{" and not escaped:
            stack.append(line)
        elif character == "}" and not escaped:
            if stack:
                stack.pop()
            else:
                issues.append(f"unmatched closing brace at line {line}")
        if character == "\n":
            line += 1
        backslashes = backslashes + 1 if character == "\\" else 0
    issues.extend(f"unclosed opening brace at line {n}" for n in stack)
    return issues


def page_name(cote: int, scan: int) -> str:
    return f"pages/{PREFIX}_{cote}_scan{scan:03d}.tex"


def load_manifest(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json" or text.lstrip().startswith("{"):
        data = json.loads(text)
        if isinstance(data, dict) and isinstance(data.get("files"), dict):
            data = data["files"]
        elif isinstance(data, dict) and isinstance(data.get("sha256"), dict):
            data = data["sha256"]
        if not isinstance(data, dict):
            raise ValueError("JSON manifest must contain a filename-to-digest object")
        result = {}
        for name, value in data.items():
            if isinstance(value, dict):
                value = value.get("sha256")
            if not isinstance(name, str) or not isinstance(value, str):
                raise ValueError("manifest entries need string filenames and SHA-256 digests")
            result[name] = value
    else:
        result = {}
        for n, line in enumerate(text.splitlines(), 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            match = re.fullmatch(r"([0-9a-fA-F]{64})[ \t]+\*?(.+?)\s*", line)
            if not match:
                raise ValueError(f"invalid sha256sum manifest line {n}")
            digest, name = match.groups()
            if name in result:
                raise ValueError(f"duplicate manifest filename: {name}")
            result[name] = digest
    for name, digest in result.items():
        if not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
            raise ValueError(f"invalid SHA-256 digest for {name}")
    return result


def validate(root: Path, explicit_manifest: Path | None = None) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    expected_names = [page_name(c, n) for c, n in EXPECTED]
    actual_names = sorted(str(p.relative_to(root)) for p in (root / "pages").glob("*.tex"))
    missing = sorted(set(expected_names) - set(actual_names))
    extra = sorted(set(actual_names) - set(expected_names))
    errors.extend(f"missing page file: {name}" for name in missing)
    errors.extend(f"unexpected page file: {name}" for name in extra)
    page_bytes = []
    for cote, scan in EXPECTED:
        name = page_name(cote, scan)
        path = root / name
        if not path.is_file():
            continue
        raw = path.read_bytes()
        page_bytes.append(raw)
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{name}: invalid UTF-8: {exc}")
            continue
        clean = strip_tex_comments(text)
        scan_markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if scan_markers != [str(scan)]:
            errors.append(f"{name}: expected exactly one scanpage{{{scan}}}, got {scan_markers}")
        cote_markers = re.findall(r"\\cotefile\s*\{\s*(\d+)\s*\}", clean)
        expected_cote = [str(cote)] if scan == 2 else []
        if cote_markers != expected_cote:
            errors.append(f"{name}: expected cote markers {expected_cote}, got {cote_markers}")
        first_markers = (rf"\s*\\cotefile\s*\{{\s*{cote}\s*\}}\s*"
                         if scan == 2 else r"\s*")
        first_markers += rf"\\scanpage\s*\{{\s*{scan}\s*\}}"
        if not re.match(first_markers, clean):
            errors.append(f"{name}: page does not begin with its required markers")
        if re.search(r"\\(?:documentclass|begin\s*\{document\}|end\s*\{document\})", clean):
            errors.append(f"{name}: fragment contains a document wrapper")
        errors.extend(f"{name}: {issue}" for issue in brace_errors(text))
    combined_name = f"{PREFIX}_transcription.tex"
    combined = root / combined_name
    if not combined.is_file():
        errors.append(f"missing combined transcription: {combined_name}")
    elif not missing and combined.read_bytes() != b"".join(page_bytes):
        errors.append("combined transcription differs from exact ordered page-byte concatenation")
    inventory_path = root / f"{PREFIX}_inventory.csv"
    inventory_rows = 0
    seen_pages: set[tuple[int, int]] = set()
    if not inventory_path.is_file():
        errors.append(f"missing inventory: {inventory_path.name}")
    else:
        try:
            reader = csv.DictReader(io.StringIO(inventory_path.read_text(encoding="utf-8-sig")))
            if reader.fieldnames != COLUMNS:
                errors.append(f"inventory columns differ: {reader.fieldnames}")
            seen_elements = set()
            last_rank = -1
            page_rank = {pair: index for index, pair in enumerate(EXPECTED)}
            for line, row in enumerate(reader, 2):
                inventory_rows += 1
                if None in row or any(value is None for value in row.values()):
                    errors.append(f"inventory line {line}: wrong number of columns")
                    continue
                try:
                    pair = (int(row.get("cote", "")), int(row.get("scan", "")))
                except ValueError:
                    errors.append(f"inventory line {line}: invalid cote/scan")
                    continue
                if pair not in page_rank:
                    errors.append(f"inventory line {line}: unexpected cote/scan {pair}")
                else:
                    seen_pages.add(pair)
                    rank = page_rank[pair]
                    if rank < last_rank:
                        errors.append(f"inventory line {line}: page rows out of prescribed order")
                    last_rank = max(last_rank, rank)
                if row.get("transcribed") != "yes":
                    errors.append(f"inventory line {line}: transcribed is not yes")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    errors.append(f"inventory line {line}: invalid sheet_kind")
                if row.get("kind") not in ELEMENT_KINDS:
                    errors.append(f"inventory line {line}: invalid element kind")
                element = row.get("element", "")
                if not element:
                    errors.append(f"inventory line {line}: empty element identifier")
                key = (pair, element)
                if key in seen_elements:
                    errors.append(f"inventory line {line}: duplicate page/element identifier")
                seen_elements.add(key)
            for pair in EXPECTED:
                if pair not in seen_pages:
                    errors.append(f"inventory has no elements for cote {pair[0]}, scan {pair[1]:03d}")
        except (UnicodeDecodeError, csv.Error) as exc:
            errors.append(f"inventory parse error: {exc}")
    manifests = []
    if explicit_manifest:
        manifests = [explicit_manifest if explicit_manifest.is_absolute() else root / explicit_manifest]
    else:
        for directory in (root, root / "work_records"):
            for basename in ("frozen_sha256.json", "frozen_sha256.txt", "freeze_hashes.sha256",
                             "freeze_hashes.json", "SHA256SUMS"):
                candidate = directory / basename
                if candidate.is_file():
                    manifests.append(candidate)
    verified_hashes = 0
    if not manifests:
        warnings.append("no frozen hash manifest found; byte immutability was not checked")
    for manifest in manifests:
        try:
            hashes = load_manifest(manifest)
            normalized = {}
            for name, digest in hashes.items():
                path = Path(name)
                path = path if path.is_absolute() else root / path
                try:
                    relative = str(path.resolve().relative_to(root.resolve()))
                except ValueError:
                    errors.append(f"manifest path lies outside packet root: {name}")
                    continue
                normalized[relative] = digest
                if not path.is_file():
                    errors.append(f"frozen file is missing: {relative}")
                elif hashlib.sha256(path.read_bytes()).hexdigest().lower() != digest.lower():
                    errors.append(f"frozen SHA-256 has changed: {relative}")
                else:
                    verified_hashes += 1
            for name in expected_names + [combined_name]:
                if name not in normalized:
                    errors.append(f"frozen manifest does not cover: {name}")
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"cannot use frozen manifest {manifest.name}: {exc}")
    for basename in (f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md", "progress.log"):
        if not (root / basename).is_file():
            errors.append(f"missing required deliverable: {basename}")
    return {"ok": not errors, "expected_pages": len(EXPECTED),
            "found_page_files": len(actual_names), "inventory_rows": inventory_rows,
            "inventory_pages": len(seen_pages), "verified_hashes": verified_hashes,
            "errors": errors, "warnings": warnings,
            "scope": "Structural checks only; no assessment of readings, omissions, or mathematical correctness."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--hashes", type=Path)
    args = parser.parse_args()
    result = validate(args.root, args.hashes)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
