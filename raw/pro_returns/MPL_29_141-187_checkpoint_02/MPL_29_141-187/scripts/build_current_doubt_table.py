#!/usr/bin/env python3
"""Build a Markdown table solely from the current balanced doubt-macro index.

No images or context materials are read. Confidence is copied only for exact
same-scan matches in the supplied manual rows; otherwise it defaults to low.
Historical manual alternatives are never introduced into the current table.
"""

from __future__ import annotations

import csv
import html
import json
from collections import Counter, defaultdict
from pathlib import Path

from index_doubt_macros import control_sequence_end, comment_end


ROOT = Path(__file__).resolve().parents[1]


def split_alternatives(content: str) -> tuple[str, list[str]]:
    """Split unescaped top-level pipes, preserving all text in each portion."""
    depth = 0
    start = 0
    parts = []
    position = 0
    while position < len(content):
        char = content[position]
        if char == "\\":
            position = control_sequence_end(content, position)
            continue
        if char == "%":
            position = comment_end(content, position)
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "|" and depth == 0:
            parts.append(content[start:position])
            start = position + 1
        position += 1
    parts.append(content[start:])
    return parts[0], parts[1:]


def code_cell(value: str) -> str:
    """Use escaped HTML code spans so TeX and table delimiters remain literal."""
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    escaped = html.escape(value, quote=False).replace("|", "&#124;")
    return "<code>" + escaped.replace("\n", "</code><br><code>") + "</code>"


def main() -> None:
    with (ROOT / "doubt_macro_index.tsv").open(encoding="utf-8", newline="") as handle:
        current = list(csv.DictReader(handle, delimiter="\t"))
    manual = defaultdict(set)
    with (ROOT / "doubts_rows.tsv").open(encoding="utf-8", newline="") as handle:
        for row in csv.reader(handle, delimiter="\t"):
            if len(row) == 6 and row[5] in {"low", "medium", "high"}:
                manual[(row[1], row[3].strip())].add(row[5])

    lines = [
        "# Current doubt-macro table",
        "",
        "This table reflects the macros in the **current page fragments**. "
        "The historical working file `doubts_rows.tsv` contains superseded readings; "
        "those historical readings and alternatives are not added here.",
        "",
        "Every locator is a one-based **physical TeX source line, not a manuscript "
        "line**. For scan NNN, the source is "
        "`pages/MPL_29_141-187_29_scanNNN.tex`. Each macro occurrence has its own row, "
        "including repeated occurrences on one source line and nested doubt macros.",
        "",
        "Confidence defaults conservatively to **low**; this is a mechanical "
        "default, not an independent visual assessment. A supplied confidence "
        "is carried only when the same scan has an exact matching current reading "
        "in `doubts_rows.tsv`. Alternatives shown here come only from unescaped "
        "top-level `|` separators in the current macro. The TSV index preserves "
        "each full argument exactly; the table displays source newlines as line breaks.",
        "",
        "| File / cote | Scan | Approximate locator | Reading | Alternatives | Confidence |",
        "|---|---:|---|---|---|---|",
    ]
    counts = Counter()
    confidences = Counter()
    per_scan = Counter()
    supplied = 0
    conflicts = []
    empty_alternatives = []
    illegible = []
    for occurrence, row in enumerate(current, 1):
        scan = row["scan"]
        macro = row["macro"]
        exact = row["exact_content"]
        reading, alternatives = split_alternatives(exact) if macro == "unsure" else (exact, [])
        matching = set(manual.get((scan, exact.strip()), set()))
        matching.update(manual.get((scan, reading.strip()), set()))
        confidence = "low"
        if len(matching) == 1:
            confidence = next(iter(matching))
            supplied += 1
        elif len(matching) > 1:
            conflicts.append({"scan": int(scan), "tex_source_line": int(row["tex_source_line"]),
                              "supplied_confidences": sorted(matching)})
        if macro == "illegible":
            reading_cell = code_cell("\\illegible{" + exact + "}")
            alternatives_cell = "No reading proposed; the macro encodes an unreadable-word count."
            illegible.append({"scan": int(scan), "tex_source_line": int(row["tex_source_line"]),
                              "exact_content": exact})
        else:
            reading_cell = code_cell(reading)
            alternatives_cell = "<br>".join(code_cell(part) for part in alternatives) if alternatives else "—"
        if any(not part.strip() for part in alternatives):
            empty_alternatives.append({"scan": int(scan), "tex_source_line": int(row["tex_source_line"])})
        locator = f"TeX source line {row['tex_source_line']} (occurrence {occurrence})"
        lines.append(f"| 29.pdf / 29 | {scan} | {locator} | {reading_cell} | {alternatives_cell} | {confidence} |")
        counts[macro] += 1
        confidences[confidence] += 1
        per_scan[int(scan)] += 1
    (ROOT / "doubts_current_table.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"occurrences": len(current),
                      "scans_with_doubt_macros": len(per_scan),
                      "per_scan_occurrences": dict(sorted(per_scan.items())),
                      "macro_counts": dict(sorted(counts.items())),
                      "confidence_counts": dict(sorted(confidences.items())),
                      "exact_supplied_confidence_matches": supplied,
                      "conflicting_supplied_confidences": conflicts,
                      "empty_alternatives": empty_alternatives,
                      "illegible_macros": illegible}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
