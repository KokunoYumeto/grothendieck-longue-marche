#!/usr/bin/env python3
"""Count explicit doubt macros mechanically; never infer a confidence or reading.

The output is a snapshot and should be refreshed after the final visual audits.
It does not establish that every uncertain reading was marked.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


PACKAGE = "MPL_136_282-327"


def remove_comments(text: str) -> str:
    result = []
    for line in text.splitlines(keepends=True):
        for pos, char in enumerate(line):
            if char != "%":
                continue
            slash_count = 0
            cursor = pos - 1
            while cursor >= 0 and line[cursor] == "\\":
                slash_count += 1
                cursor -= 1
            if slash_count % 2 == 0:
                line = line[:pos] + "\n"
                break
        result.append(line)
    return "".join(result)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path,
                        help="default: records/mechanical_doubt_counts.csv")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output or root / "records" / "mechanical_doubt_counts.csv"
    rows = []
    for scan in (n for n in range(282, 328) if n != 319):
        path = root / "pages" / f"{PACKAGE}_136_scan{scan}.tex"
        if not path.exists():
            continue
        text = remove_comments(path.read_text(encoding="utf-8"))
        unsure = len(re.findall(r"\\unsure\s*\{", text))
        illegible = len(re.findall(r"\\illegible\s*\{", text))
        numbers = re.findall(r"\\illegible\s*\{\s*(\d+)\s*\}", text)
        words = sum(map(int, numbers))
        rows.append({"cote": "136", "scan": scan, "unsure_count": unsure,
                     "illegible_count": illegible, "illegible_word_estimate": words,
                     "nonnumeric_illegible_arguments": illegible - len(numbers)})
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=(
            "cote", "scan", "unsure_count", "illegible_count",
            "illegible_word_estimate", "nonnumeric_illegible_arguments"))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} page counts: {output}")
    print(f"unsure: {sum(row['unsure_count'] for row in rows)}")
    print(f"illegible: {sum(row['illegible_count'] for row in rows)}")
    print(f"illegible word estimate: {sum(row['illegible_word_estimate'] for row in rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
