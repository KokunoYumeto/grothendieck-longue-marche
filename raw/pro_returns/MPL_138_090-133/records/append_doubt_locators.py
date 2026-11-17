#!/usr/bin/env python3
"""Append/replace the authorized exhaustive doubt-locator supplement.

This script does not change page TeX, authored doubt rows, notation, or confidence
judgments. Unmatched occurrences receive low confidence by the primary reader's
explicit conservative assessment. It does not freeze the transcription or read
the research context. Run only when the primary reader is ready.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import io
import json
import re
import validate_package as v

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "MPL_138_090-133"
BEGIN = "<!-- BEGIN EXHAUSTIVE_UNCERTAINTY_LOCATORS -->"
END = "<!-- END EXHAUSTIVE_UNCERTAINTY_LOCATORS -->"


def split_markdown_row(line):
    cells, start = [], 0
    for i, char in enumerate(line):
        if char == "|" and not v.escaped(line, i):
            cells.append(line[start:i].strip())
            start = i + 1
    cells.append(line[start:].strip())
    if cells and cells[0] == "":
        cells.pop(0)
    if cells and cells[-1] == "":
        cells.pop()
    return [cell.replace(r"\|", "|") for cell in cells]


def authored_readings(text):
    active, rows, warnings = False, [], []
    for number, line in enumerate(text.splitlines(), 1):
        if line.strip() == "## Reading doubts":
            active = True
            continue
        if active and line.startswith("## "):
            break
        if not active or not re.match(r"\|\s*138\s*\|", line):
            continue
        cells = split_markdown_row(line)
        if len(cells) != 6 or not cells[1].isdigit():
            warnings.append({"markdown_line": number, "reason": "Authored row not mechanically parseable; retained unchanged."})
            continue
        rows.append({"scan": int(cells[1]), "approximate_line": cells[2], "reading": cells[3], "alternatives": cells[4], "confidence": cells[5], "markdown_line": number})
    return rows, warnings


def split_alternatives(body):
    depth = 0
    for i, char in enumerate(body):
        if v.escaped(body, i):
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "|" and depth == 0:
            return body[:i], body[i + 1:]
    return body, ""


def code_cell(value):
    # JSON encoding preserves spaces, line breaks, backslashes, and quotation marks.
    encoded = json.dumps(value, ensure_ascii=False)
    runs = re.findall(r"`+", encoded)
    delimiter = "`" * (max((len(x) for x in runs), default=0) + 1)
    return delimiter + encoded.replace("|", r"\|") + delimiter


def main():
    doubts_path = ROOT / f"{PREFIX}_doubts.md"
    original = doubts_path.read_text()
    if original.count(BEGIN) != original.count(END) or original.count(BEGIN) > 1:
        raise SystemExit("Supplement markers are inconsistent; authored file was not changed.")
    authored, warnings = authored_readings(original)
    entries, source_hashes, source_bytes = [], {}, {}
    expected = [90, 91, *range(93, 134)]
    for scan in expected:
        relative = f"pages/{PREFIX}_138_scan{scan:03d}.tex"
        path = ROOT / relative
        data = path.read_bytes()
        raw, clean = data.decode("utf-8"), v.uncomment(data.decode("utf-8"))
        source_bytes[relative] = data
        source_hashes[relative] = hashlib.sha256(data).hexdigest()
        ordinals = Counter()
        for match in re.finditer(r"\\(unsure|illegible)(?![A-Za-z])\s*", clean):
            if v.escaped(clean, match.start()):
                continue
            macro = match.group(1)
            ordinals[macro] += 1
            start = match.end()
            while start < len(clean) and clean[start].isspace():
                start += 1
            body, end = v.argument_at(clean, start)
            if body is None:
                raise ValueError(f"Missing {macro} argument in scan {scan}.")
            exact = raw[start + 1:end - 1] if clean[start] == "{" else raw[start:end]
            first, alternatives = split_alternatives(exact) if macro == "unsure" else ("", "")
            matches = [row for row in authored if row["scan"] == scan and row["reading"].strip() == first.strip()] if macro == "unsure" else []
            match_row = matches[0] if len(matches) == 1 and matches[0]["confidence"] in {"high", "medium", "low"} else None
            confidence = match_row["confidence"] if match_row else "low"
            entries.append({
                "cote": "138", "scan": scan, "source_path": relative,
                "tex_line": v.line_at(raw, match.start()), "macro": macro,
                "occurrence": ordinals[macro],
                "occurrence_id": f"138/{scan:03d}/{macro}/{ordinals[macro]:03d}",
                "first_reading": first, "alternatives": alternatives,
                "confidence": confidence,
                "confidence_basis": "unique exact same-page authored reading-cell match" if match_row else "primary reader's conservative low default",
                "authored_markdown_line": match_row["markdown_line"] if match_row else None,
                "exact_argument": exact, "exact_macro_source": raw[match.start():end],
                "source_tex_sha256": source_hashes[relative],
            })
    assert len({entry["occurrence_id"] for entry in entries}) == len(entries)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    counts = Counter(entry["macro"] for entry in entries)
    text = BEGIN + "\n\n## Exhaustive uncertainty macro locators\n\n"
    text += (f"Generated from the current page fragments at {now}. This mechanical index contains {len(entries)} source occurrences "
             f"({counts['unsure']} `\\unsure` and {counts['illegible']} `\\illegible`). It supplements the authored doubts above; it does not replace them or add an independent reading.\n\n")
    text += ("Locations are **local TeX source line numbers**, not guesses at manuscript line numbers. Occurrence numbers restart for each macro kind on each scan. Nested uncertainties, uncertainties in deleted material, and unbraced single-token arguments are included. First readings and alternatives retain source order; a top-level vertical bar is the alternative separator. For illegible material, the first-reading and alternatives cells are empty because no reading is supplied; the exact argument preserves the word-count estimate.\n\n")
    text += ("Confidence is **low by the primary reader's explicit conservative assessment**, except where exactly one same-page authored reading cell matches the first reading after trimming cell-edge whitespace; that row's existing high/medium/low rating is retained. No linguistic, mathematical, spelling, or notation equivalence is inferred for matching.\n\n")
    text += ("Text cells below are JSON strings, so source backslashes, quotation marks, whitespace, and line breaks are represented reversibly. Markdown table escaping does not change the source argument. The exact raw arguments and full macro source are also preserved in `records/uncertainty_locator_index.json` and `records/uncertainty_locator_index.tsv`, with source SHA-256 values and confidence provenance.\n\n")
    text += "| Cote | Scan | TeX line | Occurrence # | Macro | First reading | Alternatives | Confidence | Exact argument (JSON) |\n|---|---:|---:|---:|---|---|---|---|---|\n"
    for entry in entries:
        text += f"| 138 | {entry['scan']} | {entry['tex_line']} | {entry['occurrence']} | `{entry['macro']}` | {code_cell(entry['first_reading'])} | {code_cell(entry['alternatives'])} | {entry['confidence']} | {code_cell(entry['exact_argument'])} |\n"
    text += "\n" + END + "\n"
    if BEGIN in original:
        before = original[:original.index(BEGIN)]
        after = original[original.index(END) + len(END):]
        if after.startswith("\n"):
            after = after[1:]
        result = before + text + after
    else:
        result = original + ("" if original.endswith("\n") else "\n") + "\n" + text
    for relative, data in source_bytes.items():
        if (ROOT / relative).read_bytes() != data:
            raise RuntimeError(f"Source changed during extraction: {relative}; doubts file was not changed.")
    if doubts_path.read_text() != original:
        raise RuntimeError("Authored doubts changed during extraction; no write performed.")
    index = {"generated_utc": now, "purpose": "Exhaustive mechanical source-locator supplement authorized by the primary reader; not an independent visual or mathematical check.", "source_hashes": source_hashes, "occurrence_count": len(entries), "macro_counts": dict(counts), "authored_parse_warnings": warnings, "entries": entries}
    (ROOT / "records/uncertainty_locator_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    columns = list(entries[0]) if entries else []
    with (ROOT / "records/uncertainty_locator_index.tsv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter="\t")
        writer.writeheader()
        writer.writerows(entries)
    doubts_path.write_text(result)
    print(json.dumps({"time": now, "source_occurrences": len(entries), "macro_counts": dict(counts), "unique_authored_confidence_matches": sum(entry["authored_markdown_line"] is not None for entry in entries), "low_default_occurrences": sum(entry["authored_markdown_line"] is None for entry in entries), "authored_parse_warnings": warnings, "source_files_changed": False}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
