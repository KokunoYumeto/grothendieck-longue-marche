#!/usr/bin/env python3
"""Write mechanical macro-to-inventory coverage cues; never change task source records."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

PREFIX = "MPL_72_035-081"
KINDS = {
    "figure": "drawing",
    "diagram": "diagram",
    "margin": "margin note",
    "inserted": "insertion",
    "deleted": "deletion",
}


def skip_space_comments(text, pos):
    while pos < len(text):
        if text[pos].isspace():
            pos += 1
        elif text[pos] == "%":
            end = text.find("\n", pos)
            pos = end + 1 if end >= 0 else len(text)
        else:
            break
    return pos


def control_end(text, pos):
    match = re.match(r"\\[A-Za-z@]+|\\.", text[pos:], re.DOTALL)
    return pos + len(match[0]) if match else pos + 1


def argument_span(text, pos):
    pos = skip_space_comments(text, pos)
    if pos >= len(text):
        return pos, pos, False
    if text[pos] != "{":
        end = control_end(text, pos) if text[pos] == "\\" else pos + 1
        return pos, end, False
    start = pos + 1
    depth = 1
    pos += 1
    while pos < len(text):
        char = text[pos]
        if char == "%":
            end = text.find("\n", pos)
            pos = end + 1 if end >= 0 else len(text)
            continue
        if char == "\\":
            pos = control_end(text, pos)
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return start, pos, True
        pos += 1
    return start, len(text), True


def macro_calls(text):
    calls = []
    i = 0
    while i < len(text):
        if text[i] == "%":
            end = text.find("\n", i)
            i = end + 1 if end >= 0 else len(text)
            continue
        if text[i] != "\\":
            i += 1
            continue
        end = control_end(text, i)
        name = text[i + 1:end]
        if name == "verb":
            pos = end + (end < len(text) and text[end] == "*")
            stop = text.find(text[pos], pos + 1) if pos < len(text) else -1
            i = stop + 1 if stop >= 0 else len(text)
            continue
        if name in KINDS:
            start_arg, end_arg, braced = argument_span(text, end)
            calls.append({
                "macro": name,
                "position": i,
                "line": text[:i].count("\n") + 1,
                "argument_start": start_arg,
                "argument_end": end_arg,
                "argument": text[start_arg:end_arg],
                "braced": braced,
            })
        i = end
    return calls


def build_report(root, output_dir, prefix_chars):
    inventory_path = root / f"{PREFIX}_inventory.csv"
    inventory_bytes = inventory_path.read_bytes()
    inventory = list(csv.DictReader(io.StringIO(inventory_bytes.decode("utf-8-sig"), newline="")))
    inventory_counts = defaultdict(Counter)
    for row in inventory:
        inventory_counts[int(row["scan"])][row["kind"]] += 1
    per_scan = {}
    details = []
    hashes = {}
    for path in sorted((root / "pages").glob(f"{PREFIX}_72_scan*.tex")):
        scan = int(path.stem[-3:])
        raw = path.read_bytes()
        hashes[scan] = hashlib.sha256(raw).hexdigest()
        calls = macro_calls(raw.decode("utf-8"))
        counts = Counter(call["macro"] for call in calls)
        per_scan[scan] = counts
        occurrence_counts = Counter()
        parents = []
        for call in calls:
            name = call["macro"]
            occurrence_counts[name] += 1
            identifier = f"{scan:03d}.{name}.{occurrence_counts[name]:03d}"
            while parents and call["position"] >= parents[-1]["argument_end"]:
                parents.pop()
            parent_identifier = parents[-1]["identifier"] if parents else ""
            argument = call["argument"]
            details.append({
                "cote": "72",
                "scan": f"{scan:03d}",
                "tex_line": call["line"],
                "call_id": identifier,
                "macro": name,
                "inventory_kind": KINDS[name],
                "macro_calls_on_scan": counts[name],
                "inventory_kind_rows_on_scan": inventory_counts[scan][KINDS[name]],
                "enclosing_marked_call": parent_identifier,
                "braced_argument": "yes" if call["braced"] else "no",
                "argument_characters": len(argument),
                "prefix_truncated": "yes" if len(argument) > prefix_chars else "no",
                "argument_prefix": argument[:prefix_chars],
            })
            parents.append({**call, "identifier": identifier})
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "macro_inventory_coverage.csv"
    columns = [
        "cote", "scan", "tex_line", "call_id", "macro", "inventory_kind",
        "macro_calls_on_scan", "inventory_kind_rows_on_scan", "enclosing_marked_call",
        "braced_argument", "argument_characters", "prefix_truncated", "argument_prefix",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(details)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# Macro-to-inventory coverage cues",
        "",
        f"Snapshot generated: {now}.",
        "",
        f"This report covers {len(per_scan)} saved page fragments and {len(inventory)} inventory rows. "
        f"The companion CSV contains {len(details)} marked macro calls, including nested calls. "
        "It reads source text only; no manuscript image or context was accessed.",
        "",
        "Each CSV row supplies the scan, exact source line at the macro token, a stable-in-this-snapshot call identifier, "
        "the enclosing marked call, a raw argument prefix, and the corresponding inventory-kind count. "
        f"Prefixes preserve source whitespace and contain the first {prefix_chars} Unicode characters of the argument; "
        "multiline prefixes occupy properly quoted CSV fields. The truncation flag records omitted suffixes. "
        "Line positions are exact for the hashed snapshot and become approximate after edits.",
        "",
        "The figures compare macro calls with inventory rows; equality alone does not establish complete coverage. "
        "An inventory row may describe a larger block containing several nested changes, and a figure may be classified "
        "under another kind. Differences identify places for the primary transcriber's element-by-element reconciliation. "
        "The report neither labels an element complete nor changes inventory entries.",
        "",
        "## Counts for every saved scan",
        "",
        "Each entry is **macro calls / inventory rows of the corresponding kind**.",
        "",
        "| Scan | Figure / drawing | Diagram / diagram | Margin / margin note | Inserted / insertion | Deleted / deletion |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for scan, counts in sorted(per_scan.items()):
        fields = [f"{counts[name]} / {inventory_counts[scan][kind]}" for name, kind in KINDS.items()]
        lines.append("| " + f"{scan:03d}" + " | " + " | ".join(fields) + " |")
    total_calls = Counter()
    total_rows = Counter()
    for values in per_scan.values():
        total_calls.update(values)
    for values in inventory_counts.values():
        total_rows.update(values)
    lines.append("| **Total** | " + " | ".join(f"**{total_calls[name]} / {total_rows[kind]}**" for name, kind in KINDS.items()) + " |")
    lines.extend([
        "",
        "## Differences to reconcile",
        "",
        "| Scan | Macro | Calls | Inventory kind | Rows |",
        "|---|---|---:|---|---:|",
    ])
    differences = []
    for scan, counts in sorted(per_scan.items()):
        for name, kind in KINDS.items():
            if counts[name] != inventory_counts[scan][kind]:
                differences.append((scan, name, counts[name], kind, inventory_counts[scan][kind]))
                lines.append(f"| {scan:03d} | `{name}` | {counts[name]} | {kind} | {inventory_counts[scan][kind]} |")
    if not differences:
        lines.append("| — | No count differences | — | — | — |")
    lines.extend([
        "",
        "## Refreshing the report",
        "",
        "```sh",
        "python scripts/inventory_coverage.py",
        "```",
        "",
        "Only `scripts/macro_inventory_coverage.md` and `scripts/macro_inventory_coverage.csv` are overwritten by the "
        "default invocation. Page files, the inventory, progress records, and audit records are read-only inputs.",
        "",
        "## Source hashes for this report",
        "",
        "These identify the inspected versions and make no transcription-freeze claim.",
        "",
        "| Source | SHA-256 |",
        "|---|---|",
        f"| Inventory CSV | `{hashlib.sha256(inventory_bytes).hexdigest()}` |",
    ])
    for scan, digest in sorted(hashes.items()):
        lines.append(f"| Scan {scan:03d} | `{digest}` |")
    md_path = output_dir / "macro_inventory_coverage.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"markdown": str(md_path), "csv": str(csv_path), "scans": len(per_scan), "macro_calls": len(details), "count_differences": len(differences)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--prefix-chars", type=int, default=100)
    args = parser.parse_args()
    if args.prefix_chars < 1:
        parser.error("prefix character count must be positive")
    import json
    print(json.dumps(build_report(args.root.resolve(), args.output_dir.resolve(), args.prefix_chars), indent=2))


if __name__ == "__main__":
    main()
