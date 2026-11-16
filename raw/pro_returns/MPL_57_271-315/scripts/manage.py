#!/usr/bin/env python3
"""Mechanical record keeping only: no OCR, interpretation, or audit claims.

save accepts JSON on stdin (or --input). Only the human/primary reader may
decide that a page is complete or append an actual audited entry to the log.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "MPL_57_271-315"
EXPECTED = [n for n in range(271, 316) if n not in (278, 293)]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position", "first_words_or_objects", "transcribed"]
STATE_MACROS = {"cotefile", "scanpage", "mspage", "deleted", "inserted", "margin", "uline", "uuline", "diagram", "figure", "unsure", "illegible"}
FORBIDDEN_MACROS = {"documentclass", "usepackage", "includegraphics", "input", "include", "newcommand", "renewcommand", "providecommand", "def", "gdef", "edef", "xdef", "let"}
FROZEN = ROOT / "records" / "frozen_hashes.json"


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def pagepath(scan):
    return ROOT / "pages" / f"{PREFIX}_57_scan{scan:03d}.tex"


def recordpath(scan):
    return ROOT / "records" / f"scan{scan:03d}.json"


def combinedpath():
    return ROOT / f"{PREFIX}_transcription.tex"


def appendlog(line):
    with (ROOT / "progress.log").open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def atomic_write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(value, encoding="utf-8")
    temporary.replace(path)


def unfrozen():
    if FROZEN.exists() or "transcription frozen " in (ROOT / "progress.log").read_text(encoding="utf-8"):
        raise ValueError("Transcription is frozen; page changes and rebuilding are prohibited.")


def uncomment(tex):
    """Remove TeX comments while preserving newlines and escaped percent signs."""
    out = []
    i = 0
    while i < len(tex):
        if tex[i] == "\\" and i + 1 < len(tex):
            out.append(tex[i:i+2])
            i += 2
        elif tex[i] == "%":
            stop = tex.find("\n", i)
            i = len(tex) if stop == -1 else stop
        else:
            out.append(tex[i])
            i += 1
    return "".join(out)


def tex_errors(tex, scan):
    clean = uncomment(tex)
    errors = []
    stack = []
    i = 0
    line = 1
    while i < len(clean):
        char = clean[i]
        if char == "\\" and i + 1 < len(clean):
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
    errors.extend(f"unclosed brace from line {number}" for number in stack)
    scans = re.findall(r"\\scanpage\s*\{([^{}]*)\}", clean)
    if scans != [str(scan)]:
        errors.append(f"expected exactly \\scanpage{{{scan}}}; found {scans!r}")
    cotes = re.findall(r"\\cotefile\s*\{([^{}]*)\}", clean)
    if cotes != (["57"] if scan == EXPECTED[0] else []):
        errors.append("\\cotefile{57} must occur only at the start of the first page")
    start = rf"\s*\\cotefile\s*\{{57\}}\s*\\scanpage\s*\{{{scan}\}}" if scan == EXPECTED[0] else rf"\s*\\scanpage\s*\{{{scan}\}}"
    if not re.match(start, clean):
        errors.append("page does not begin with its required cote/scan marker(s)")
    for match in re.finditer(r"\\([A-Za-z@]+)", clean):
        name = match.group(1)
        if name in FORBIDDEN_MACROS:
            errors.append(f"forbidden fragment command \\{name}")
        if name in STATE_MACROS:
            tail = clean[match.end():].lstrip()
            if not tail.startswith("{"):
                errors.append(f"\\{name} needs a braced argument")
            if name == "illegible" and not re.match(r"\{[1-9][0-9]*\}", tail):
                errors.append("\\illegible requires a positive word count")
    envs = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]*)\}", clean):
        action, env = match.groups()
        if env == "document":
            errors.append("document environment is forbidden in a fragment")
        if action == "begin":
            envs.append(env)
        elif not envs or envs.pop() != env:
            errors.append(f"unmatched \\end{{{env}}}")
    errors.extend(f"unclosed environment {env}" for env in envs)
    return errors


def inventory_rows(record):
    if record.get("sheet_kind") not in SHEET_KINDS:
        raise ValueError(f"Invalid sheet_kind for scan {record.get('scan')}")
    inventory = record.get("inventory")
    if not isinstance(inventory, list) or not inventory:
        raise ValueError("inventory must be a nonempty list")
    rows = []
    seen = set()
    for item in inventory:
        if not isinstance(item, dict):
            raise ValueError("Each inventory item must be an object")
        for key in ("element", "kind", "position", "first_words_or_objects"):
            if key not in item:
                raise ValueError(f"Inventory item is missing {key}")
        key = str(item["element"])
        if not key or key in seen:
            raise ValueError(f"Empty or duplicate inventory element: {key!r}")
        seen.add(key)
        if item["kind"] not in KINDS:
            raise ValueError(f"Invalid inventory kind: {item['kind']!r}")
        if item.get("transcribed", "yes") != "yes":
            raise ValueError("A saved completed page must have transcribed=yes throughout")
        rows.append(dict(cote="57", scan=str(record["scan"]), sheet_kind=record["sheet_kind"],
                         element=key, kind=item["kind"], position=item["position"],
                         first_words_or_objects=item["first_words_or_objects"], transcribed="yes"))
    return rows


def load_records():
    return {n: json.loads(recordpath(n).read_text(encoding="utf-8")) for n in EXPECTED if recordpath(n).exists()}


def derived(records):
    fragments = []
    rows = []
    for scan in sorted(records):
        record = records[scan]
        fragments.append(record["tex"].rstrip("\n") + "\n")
        rows.extend(inventory_rows(record))
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return "\n".join(fragments), buffer.getvalue()


def save(args):
    unfrozen()
    source = Path(args.input).read_text(encoding="utf-8") if args.input else sys.stdin.read()
    record = json.loads(source)
    if not isinstance(record, dict):
        raise ValueError("JSON input must be an object")
    scan = int(record["scan"])
    if scan not in EXPECTED:
        raise ValueError(f"Unexpected scan {scan}")
    record["scan"] = scan
    record["cote"] = "57"
    if not isinstance(record.get("tex"), str) or not record["tex"]:
        raise ValueError("tex must be a nonempty string")
    errors = tex_errors(record["tex"], scan)
    if errors:
        raise ValueError("; ".join(errors))
    inventory_rows(record)
    records = load_records()
    existed = scan in records
    missing = [n for n in EXPECTED if n not in records]
    if not existed and missing and scan != missing[0]:
        raise ValueError(f"One-stream order requires scan {missing[0]} next, not {scan}")
    record.setdefault("doubts", [])
    record.setdefault("observations", [])
    record["saved_at"] = now()
    records[scan] = record
    combined, inventory = derived(records)
    atomic_write(pagepath(scan), record["tex"])
    atomic_write(recordpath(scan), json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    atomic_write(combinedpath(), combined)
    atomic_write(ROOT / f"{PREFIX}_inventory.csv", inventory)
    appendlog(f"57 scan {scan:03d} {'revised' if existed else 'done'} {now()}")
    print(json.dumps({"scan": scan, "page": str(pagepath(scan)), "pages_saved": len(records),
                      "inventory_elements": len(record["inventory"]), "status": "revised" if existed else "done"}))


def validate(partial=False):
    errors = []
    records = load_records()
    present = {n for n in EXPECTED if pagepath(n).exists()}
    missing = [n for n in EXPECTED if n not in present]
    if missing and not partial:
        errors.append(f"Missing pages: {missing}")
    if set(records) != present:
        errors.append(f"Page/record mismatch: pages={sorted(present)}, records={sorted(records)}")
    expected_names = {pagepath(n).name for n in EXPECTED}
    unexpected = [p.name for p in (ROOT / "pages").glob("*.tex") if p.name not in expected_names]
    if unexpected:
        errors.append(f"Unexpected page files: {unexpected}")
    for scan in sorted(present):
        tex = pagepath(scan).read_text(encoding="utf-8")
        errors.extend(f"scan {scan}: {item}" for item in tex_errors(tex, scan))
        if scan in records and tex != records[scan]["tex"]:
            errors.append(f"scan {scan}: page differs from saved record; resave before freezing")
    try:
        combined, inventory = derived(records)
        for path, expected in [(combinedpath(), combined), (ROOT / f"{PREFIX}_inventory.csv", inventory)]:
            if records and (not path.exists() or path.read_text(encoding="utf-8") != expected):
                errors.append(f"Derived file is absent or stale: {path.name}")
    except (ValueError, KeyError, TypeError) as exc:
        errors.append(str(exc))
    return {"ok": not errors, "pages": len(present), "expected_pages": len(EXPECTED),
            "missing": missing, "errors": errors,
            "scope": "Mechanical checks only; no claim about visual completeness or correctness."}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def freeze(args):
    unfrozen()
    result = validate()
    if not result["ok"]:
        raise ValueError("Cannot freeze: " + "; ".join(result["errors"]))
    progress = (ROOT / "progress.log").read_text(encoding="utf-8")
    audited = {int(n) for n in re.findall(r"^scan ([0-9]+) audited .+$", progress, re.M)}
    unaudited = [n for n in EXPECTED if n not in audited]
    if unaudited:
        raise ValueError(f"Root must finish and log its visual audits first: {unaudited}")
    paths = [pagepath(n) for n in EXPECTED] + [combinedpath()]
    hashes = {str(path.relative_to(ROOT)): sha256(path) for path in paths}
    timestamp = now()
    atomic_write(FROZEN, json.dumps({"frozen_at": timestamp, "sha256": hashes}, indent=2) + "\n")
    for name, digest in hashes.items():
        appendlog(f"sha256 {digest} {name}")
    appendlog("transcription frozen " + timestamp)
    print(json.dumps({"status": "frozen", "files": len(hashes), "time": timestamp}))


def verify(args):
    if not FROZEN.exists():
        raise ValueError("No frozen hash record exists")
    frozen = json.loads(FROZEN.read_text(encoding="utf-8"))
    changed = [name for name, digest in frozen["sha256"].items()
               if not (ROOT / name).exists() or sha256(ROOT / name) != digest]
    if changed:
        raise ValueError(f"Frozen transcription changed or is missing: {changed}")
    appendlog("frozen transcription hashes unchanged " + now())
    print(json.dumps({"status": "unchanged", "files": len(frozen["sha256"])}))


def archive(args):
    if args.final:
        result = validate()
        if not result["ok"]:
            raise ValueError("Cannot package final: " + "; ".join(result["errors"]))
        for name in [f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md", "progress.log"]:
            if not (ROOT / name).is_file():
                raise ValueError(f"Missing final deliverable: {name}")
        if not FROZEN.exists():
            raise ValueError("Freeze and verify the transcription before final packaging")
        verify(args)
        filename = f"{PREFIX}.zip"
    else:
        if args.checkpoint < 1:
            raise ValueError("Checkpoint number must be positive")
        filename = f"{PREFIX}_checkpoint_{args.checkpoint:02d}.zip"
    destination = Path(args.output).resolve() if args.output else ROOT.parent / filename
    if destination.name != filename:
        raise ValueError(f"Required archive filename is {filename}")
    if destination.exists():
        raise ValueError(f"Refusing to overwrite existing archive: {destination}")
    excluded_dirs = {"scans", "upload", "sources", "context", "__pycache__", ".git"}
    files = [path for path in ROOT.rglob("*") if path.is_file()
             and not any(part in excluded_dirs for part in path.relative_to(ROOT).parts)
             and path.suffix.lower() not in {".zip", ".pyc"} and not path.name.endswith(".tmp")]
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in sorted(files):
            bundle.write(path, path.relative_to(ROOT).as_posix())
    print(json.dumps({"archive": str(destination), "files": len(files), "bytes": destination.stat().st_size,
                      "sha256": sha256(destination), "uploaded": False}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("save", help="Save one completed page from JSON stdin, in scan order")
    p.add_argument("--input", help="Read the JSON object from this file instead")
    commands.add_parser("freeze", help="Hash all pages after root has logged every visual audit")
    commands.add_parser("verify", help="Check frozen files and append the result to progress.log")
    p = commands.add_parser("validate", help="Mechanical structural checks only")
    p.add_argument("--partial", action="store_true", help="Do not require all 43 pages yet")
    p = commands.add_parser("archive", help="Create a ZIP locally; never uploads or claims durability")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--final", action="store_true")
    group.add_argument("--checkpoint", type=int, metavar="NN", help="Caller must enforce the hourly schedule")
    p.add_argument("--output", help="Optional full output path; prescribed filename is enforced")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            result = validate(args.partial)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0 if result["ok"] else 1
        {"save": save, "freeze": freeze, "verify": verify, "archive": archive}[args.command](args)
        return 0
    except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
