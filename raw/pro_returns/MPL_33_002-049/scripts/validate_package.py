#!/usr/bin/env python3
"""Read-only structural checks. This does not assess manuscript readings."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

PREFIX = "MPL_33_002-049"
SCANS = tuple(range(2, 50))
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
           "first_words_or_objects", "transcribed"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEETS = {"text", "reused_typed", "cancelled_draft", "cover"}


def uncomment(text: str) -> str:
    """Remove TeX comments, respecting escaped percent signs."""
    out = []
    i = 0
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            out.append(text[i:i + 2])
            i += 2
        elif text[i] == "%":
            j = text.find("\n", i)
            i = len(text) if j < 0 else j
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def brace_errors(text: str) -> list[str]:
    stack = []
    errors = []
    i = 0
    line = 1
    while i < len(text):
        char = text[i]
        if char == "\\" and i + 1 < len(text):
            i += 2
            continue
        if char == "\n":
            line += 1
        elif char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at line {line}")
        i += 1
    errors.extend(f"unclosed opening brace at line {n}" for n in stack)
    return errors


def validate(root: Path, final: bool = False) -> dict:
    errors = []
    warnings = []
    counts = {"page_files": 0, "inventory_rows": 0, "inventory_scans": 0,
              "done_scans": 0, "audited_scans": 0, "verified_hashes": 0}
    expected = {n: root / "pages" / f"{PREFIX}_33_scan{n:03}.tex" for n in SCANS}
    found = {n: p for n, p in expected.items() if p.is_file()}
    counts["page_files"] = len(found)
    missing = sorted(set(SCANS) - set(found))
    if missing:
        (errors if final else warnings).append("Missing page files: " + ", ".join(f"{n:03}" for n in missing))
    extra = sorted(p.name for p in (root / "pages").glob("*.tex") if p not in expected.values())
    if extra:
        errors.append("Unexpected page files: " + ", ".join(extra))

    texts = {}
    for n, path in found.items():
        try:
            raw = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        texts[n] = raw
        clean = uncomment(raw)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if [int(v) for v in markers] != [n]:
            errors.append(f"{path.name}: expected exactly one scanpage{{{n}}}; found {markers}")
        if re.search(r"\\(?:documentclass|usepackage)\b|\\begin\s*\{document\}", clean):
            errors.append(f"{path.name}: must be a LaTeX fragment without preamble/document wrapper")
        if re.search(r"\\includegraphics\b", clean):
            errors.append(f"{path.name}: embedded scan/image is not permitted in the transcription")
        errors.extend(f"{path.name}: {e}" for e in brace_errors(clean))
        envs = []
        for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
            action, env = match.groups()
            if action == "begin":
                envs.append(env)
            elif not envs or envs.pop() != env:
                errors.append(f"{path.name}: unmatched end of environment {env}")
        if envs:
            errors.append(f"{path.name}: unclosed environments {envs}")

    combined = root / f"{PREFIX}_transcription.tex"
    if combined.is_file():
        whole = combined.read_text(encoding="utf-8")
        clean = uncomment(whole)
        cotes = re.findall(r"\\cotefile\s*\{\s*([^{}]+)\s*\}", clean)
        if cotes != ["33"]:
            errors.append(f"Combined transcription must contain exactly one cotefile{{33}}; found {cotes}")
        if not clean.lstrip().startswith("\\cotefile{33}"):
            errors.append("Combined transcription must start with cotefile{33}")
        concat = "".join(texts[n] for n in sorted(texts))
        # Support either the first page owning the cote marker or one prefix in the combined file.
        variants = {concat, "\\cotefile{33}\n" + concat, "\\cotefile{33}\n\n" + concat}
        if whole not in variants:
            errors.append("Combined transcription is not the exact ordered concatenation of page files (with optional cotefile prefix)")
        markers = [int(v) for v in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)]
        if markers != sorted(found):
            errors.append(f"Combined scan markers differ from ordered page files: {markers}")
    elif final:
        errors.append("Combined transcription is missing")

    inventory = root / f"{PREFIX}_inventory.csv"
    inventory_scans = set()
    if inventory.is_file():
        with inventory.open(encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames != COLUMNS:
                errors.append(f"Inventory columns must be {COLUMNS}; found {reader.fieldnames}")
            seen = set()
            for line, row in enumerate(reader, start=2):
                counts["inventory_rows"] += 1
                label = f"Inventory line {line}"
                try:
                    scan = int(row.get("scan", ""))
                    inventory_scans.add(scan)
                    if scan not in SCANS:
                        errors.append(f"{label}: unexpected scan {scan}")
                except (ValueError, TypeError):
                    errors.append(f"{label}: invalid scan")
                    continue
                if row.get("cote") != "33":
                    errors.append(f"{label}: cote must be 33")
                if row.get("sheet_kind") not in SHEETS:
                    errors.append(f"{label}: invalid sheet_kind {row.get('sheet_kind')!r}")
                if row.get("kind") not in KINDS:
                    errors.append(f"{label}: invalid kind {row.get('kind')!r}")
                if row.get("transcribed") != "yes":
                    errors.append(f"{label}: transcribed is not yes")
                identity = (scan, row.get("element"))
                if identity in seen:
                    errors.append(f"{label}: duplicate scan/element {identity}")
                seen.add(identity)
                if not row.get("element") or not row.get("position"):
                    errors.append(f"{label}: element and position must be nonempty")
                if None in row:
                    errors.append(f"{label}: extra CSV cells")
        counts["inventory_scans"] = len(inventory_scans)
        if set(found) - inventory_scans:
            errors.append(f"Page files without inventory: {sorted(set(found) - inventory_scans)}")
        if inventory_scans - set(found):
            errors.append(f"Inventory scans without page files: {sorted(inventory_scans - set(found))}")
    elif final or found:
        errors.append("Inventory is missing")

    log = root / "progress.log"
    if log.is_file():
        lines = log.read_text(encoding="utf-8").splitlines()
        done = {}
        audited = {}
        freeze_lines = []
        context_lines = []
        hashes = {}
        for i, line in enumerate(lines):
            m = re.search(r"\b33 scan (\d+) done\b", line)
            if m:
                done[int(m.group(1))] = i
            m = re.search(r"\bscan (\d+) audited\b", line)
            if m:
                audited[int(m.group(1))] = i
            if line.startswith("transcription frozen "):
                freeze_lines.append(i)
            if line.startswith("context opened "):
                context_lines.append(i)
            digest = re.search(r"\b[0-9a-fA-F]{64}\b", line)
            filename = re.search(r"(?:pages/)?MPL_33_002-049_(?:33_scan\d{3}|transcription)\.tex", line)
            if digest and filename:
                name = filename.group(0)
                if "_33_scan" in name and not name.startswith("pages/"):
                    name = "pages/" + name
                hashes[name] = (digest.group(0).lower(), i)
        counts["done_scans"] = len(done)
        counts["audited_scans"] = len(audited)
        if not lines or not re.fullmatch(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?: UTC|Z|\+00:00)", lines[0]):
            errors.append("First progress.log line must be the starting UTC timestamp")
        if set(found) - set(done):
            errors.append(f"Page files without done log: {sorted(set(found) - set(done))}")
        if final:
            if set(SCANS) - set(audited):
                errors.append(f"Scans without audit log: {sorted(set(SCANS) - set(audited))}")
            if len(freeze_lines) != 1:
                errors.append(f"Expected one transcription frozen line; found {len(freeze_lines)}")
            freeze = freeze_lines[0] if freeze_lines else -1
            for n in SCANS:
                if n in done and n in audited and audited[n] <= done[n]:
                    errors.append(f"Scan {n:03}: audit does not follow done log")
                if n in audited and freeze >= 0 and audited[n] >= freeze:
                    errors.append(f"Scan {n:03}: audit is not before freezing")
            if len(context_lines) != 1 or (freeze >= 0 and context_lines[0] <= freeze):
                errors.append("Expected one context opened line after transcription frozen")
            targets = [*expected.values(), combined]
            for path in targets:
                rel = path.relative_to(root).as_posix()
                if rel not in hashes:
                    errors.append(f"Missing frozen SHA-256 for {rel}")
                elif path.is_file():
                    digest, at = hashes[rel]
                    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                        errors.append(f"Frozen SHA-256 mismatch: {rel}")
                    else:
                        counts["verified_hashes"] += 1
                    if freeze >= 0 and at > freeze:
                        warnings.append(f"Hash record for {rel} occurs after freeze marker; ensure it records the pre-context state")
            if not any(re.search(r"hashes.*unchanged|unchanged.*hashes", line, re.I) for line in lines[freeze + 1:]):
                errors.append("No post-freeze confirmation that hashes are unchanged")
    elif final or found:
        errors.append("progress.log is missing")

    if final:
        for suffix in ("doubts.md", "notes.md"):
            path = root / f"{PREFIX}_{suffix}"
            if not path.is_file() or not path.read_text(encoding="utf-8").strip():
                errors.append(f"Missing or empty {path.name}")
    return {"ok": not errors, "mode": "final" if final else "partial", "counts": counts,
            "errors": errors, "warnings": warnings,
            "scope": "Structural checks only; no claim about accuracy or completeness against scan images."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--final", action="store_true", help="Require all 48 scans, audits, freeze hashes, and notes")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate(args.root.resolve(), args.final)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("PASS" if result["ok"] else "FAIL", f"({result['mode']})")
        for key, value in result["counts"].items():
            print(f"{key}: {value}")
        for level in ("errors", "warnings"):
            for item in result[level]:
                print(f"{level[:-1].upper()}: {item}")
        print(result["scope"])
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
