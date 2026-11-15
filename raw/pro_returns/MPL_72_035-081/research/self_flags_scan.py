#!/usr/bin/env python3
"""Read frozen TeX; enumerate literal question marks and their encoded scopes."""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


NOTES = {
    (35, 1): ("F01", "N035.1", "conic uniqueness"),
    (43, 1): ("F02", "N043.2", "local nonidentity section"),
    (46, 1): ("F03", "N046.2", "last diagonal coefficient"),
    (47, 1): ("F04", "N047.1", "determinant expansion"),
    (48, 1): ("F05", "N048.2", "centre pairing"),
    (63, 1): ("F06", "N063.3", "cancelled orthogonality attempt"),
    (67, 1): ("F07", "N067.1", "cancelled cofactor identity"),
    (67, 2): ("F08", "N067.1", "cancelled rank-one composition"),
    (75, 1): ("F09", "N075.3", "implication among orthogonality conditions"),
    (80, 1): ("F10", "IS05; N080–081", "distinctness of the two flags"),
}


def question_positions(text: str):
    """Track braces and the actual deleted/unsure macros without interpreting math."""
    scopes: list[str | None] = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "%":
            end = text.find("\n", i)
            i = len(text) if end < 0 else end + 1
            continue
        if ch == "\\":
            match = re.match(r"\\([A-Za-z]+)", text[i:])
            if match:
                command = match.group(1)
                i += len(match.group(0))
                if command in {"deleted", "unsure"}:
                    after_space = i
                    while after_space < len(text) and text[after_space].isspace():
                        after_space += 1
                    if after_space < len(text) and text[after_space] == "{":
                        scopes.append(command)
                        i = after_space + 1
            else:
                # Escaped braces, math delimiters, and line-break commands.
                i += 2
            continue
        if ch == "{":
            scopes.append(None)
        elif ch == "}":
            if scopes:
                scopes.pop()
        elif ch == "?":
            yield i, "unsure" in scopes, "deleted" in scopes
        i += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--work",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
    )
    args = parser.parse_args()
    pages = sorted((args.work / "pages").glob("MPL_72_035-081_72_scan*.tex"))
    assert len(pages) == 47, f"Expected 47 frozen page files, got {len(pages)}"
    rows = []
    digests = {}
    for path in pages:
        scan = int(re.search(r"scan(\d+)\.tex$", path.name).group(1))
        raw = path.read_bytes()
        source = raw.decode("utf-8")
        digests[path.name] = hashlib.sha256(raw).hexdigest()
        starts = [0] + [m.end() for m in re.finditer("\n", source)]
        lines = source.splitlines()
        positions = list(question_positions(source))
        assert len(positions) == source.count("?"), (
            f"Unexpected literal question mark in an excluded TeX scope: {path.name}"
        )
        for within_scan, (offset, unsure, cancelled) in enumerate(positions, 1):
            flag, note, subject = NOTES[(scan, within_scan)]
            line_index = bisect.bisect_right(starts, offset) - 1
            rows.append({
                "flag": flag,
                "scan": f"{scan:03d}",
                "occurrence_in_scan": within_scan,
                "source_file": path.name,
                "line": line_index + 1,
                "column": offset - starts[line_index] + 1,
                "inside_unsure": unsure,
                "inside_deleted": cancelled,
                "research_note": note,
                "subject": subject,
                "exact_source_line": lines[line_index],
            })
    assert len(rows) == len(NOTES) == 10
    output = args.work / "research"
    with (output / "self_flags_occurrences.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "command": "python3 research/self_flags_scan.py",
        "source_page_count": len(pages),
        "literal_question_mark_count": len(rows),
        "scans_with_question_marks": dict(sorted(Counter(row["scan"] for row in rows).items())),
        "inside_unsure_count": sum(row["inside_unsure"] for row in rows),
        "inside_deleted_count": sum(row["inside_deleted"] for row in rows),
        "notes": "Counts concern frozen TeX encoding; uncertainty and cancellation are retained.",
        "source_sha256": digests,
    }
    (output / "self_flags_counts.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in summary.items() if k != "source_sha256"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
