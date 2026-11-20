"""Compare written blind readings with first readings, preserving all tokens.

This does no image recognition and makes no reading decisions.
"""
from pathlib import Path
import csv
import difflib
import json
import re
import sys

OUT = Path(__file__).resolve().parents[1]
page = sys.argv[1]
TOKEN = re.compile(r"\\[A-Za-z]+|\\.|[^\W\d_]+|\d+|[^\s]", re.UNICODE)


def read_tsv(suffix):
    path = OUT / "second" / f"{page}_{suffix}.tsv"
    with path.open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    ids = [row["box"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError(f"Duplicate box in {path}")
    return rows


boxes = read_tsv("boxes")
first = {row["box"]: row["reading"] for row in read_tsv("first")}
second = {row["box"]: row["reading"] for row in read_tsv("second")}
expected = {row["box"] for row in boxes}
if set(first) != expected or set(second) != expected:
    raise ValueError({"expected": sorted(expected), "first": sorted(first), "second": sorted(second)})

comparisons = []
differences = []
for box in boxes:
    key = box["box"]
    a, b = TOKEN.findall(first[key]), TOKEN.findall(second[key])
    opcodes = [
        {"operation": tag, "first": a[i:j], "second": b[k:l]}
        for tag, i, j, k, l in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
        if tag != "equal"
    ]
    comparisons.append({"box": key, "equal_tokens": "no" if opcodes else "yes", "first": first[key], "second": second[key], "token_differences": json.dumps(opcodes, ensure_ascii=False)})
    if opcodes:
        differences.append({**box, "first": first[key], "second": second[key], "token_differences": opcodes})

with (OUT / "second" / f"{page}_comparison.tsv").open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=["box", "equal_tokens", "first", "second", "token_differences"], delimiter="\t")
    writer.writeheader()
    writer.writerows(comparisons)
(OUT / "second" / f"{page}_differences.json").write_text(json.dumps(differences, ensure_ascii=False, indent=2))
print(json.dumps({"page": page, "boxes": len(boxes), "differences": len(differences)}, ensure_ascii=False))
