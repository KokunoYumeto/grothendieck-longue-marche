"""Textual coverage aid, not image recognition or a reading decision.

Report transcription macro contents not found verbatim, with punctuation and
wrappers removed, in the written first readings of the neutral image boxes.
The resulting candidates require human/visual assessment: paraphrased box
readings and overlapping source lines can create false positives.
"""
from pathlib import Path
import csv
import re

OUT = Path(__file__).resolve().parents[1]


def arguments(text, name):
    for match in re.finditer(r"\\" + name + r"\s*\{", text):
        level, end = 1, match.end()
        start = end
        while end < len(text) and level:
            if text[end] == "{" and text[end - 1] != "\\":
                level += 1
            elif text[end] == "}" and text[end - 1] != "\\":
                level -= 1
            end += 1
        yield match.start(), text[start:end - 1]


def norm(text):
    text = re.sub(r"\\(?:handwritten|mathrm|mathit|text|uline|uuline|underline|overline|inserted|deleted|unsure|margin)\b", "", text)
    return re.sub(r"[\s{}$]", "", text)


rows = []
for page in sorted((OUT / "pages").glob("*.tex")):
    first = OUT / "second" / f"{page.stem}_first.tsv"
    if not first.exists():
        continue
    boxes = list(csv.DictReader(first.open(), delimiter="\t"))
    text = page.read_text()
    for kind in ["inserted", "deleted", "margin", "mspage"]:
        for position, value in arguments(text, kind):
            needle = norm(value)
            matches = [b["box"] for b in boxes if needle and needle in norm(b["reading"])]
            rows.append({"page": page.stem, "kind": kind, "source_line": text.count("\n", 0, position) + 1,
                         "reading": value, "exact_text_box_matches": ";".join(matches),
                         "status": "text matched" if matches else "manual coverage review"})
with (OUT / "work/box_coverage_candidates.tsv").open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]) if rows else [], delimiter="\t")
    writer.writeheader()
    writer.writerows(rows)
for row in rows:
    if row["status"] == "manual coverage review":
        print(row["page"], row["kind"], row["source_line"], row["reading"][:180])
print(f"{len(rows)} macro occurrences; {sum(r['status'] == 'manual coverage review' for r in rows)} textual coverage candidates.")
