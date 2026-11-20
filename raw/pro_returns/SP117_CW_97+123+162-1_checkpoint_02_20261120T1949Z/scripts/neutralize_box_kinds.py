"""Keep blind box labels categorical; preserve selection reasons separately."""
from pathlib import Path
import csv
import json

OUT = Path(__file__).resolve().parents[1]
records = []


def neutral(kind):
    lower = kind.lower()
    if "diagram" in lower:
        return "diagram"
    if "formula" in lower or "display" in lower or "mathematical" in lower:
        return "formula"
    if "margin" in lower:
        return "margin note"
    if "number" in lower or "numeral" in lower:
        return "number"
    if "drawing" in lower or "rule" in lower or "bracket" in lower:
        return "drawing"
    if "insertion" in lower and "deletion" in lower:
        return "revision"
    if "insertion" in lower:
        return "insertion"
    if "deletion" in lower or "overtyping" in lower or "struck" in lower or "cancel" in lower:
        return "revision"
    if "punctuation" in lower or "quotation" in lower:
        return "punctuation"
    return "text"


for report in sorted((OUT / "work").glob("*_decided.json")):
    data = json.loads(report.read_text())
    page = data["page"]
    rows = []
    for box in data["boxes"]:
        original = box["kind"]
        label = neutral(original)
        records.append({"page": page, "box": box["box"], "selection_description": original,
                        "blind_kind": label})
        rows.append({**box, "kind": label})
    with (OUT / "second" / f"{page}_boxes.tsv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["box", "kind", "x0", "y0", "x1", "y1"], delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
(OUT / "work/box_selection_reasons.json").write_text(json.dumps(records, ensure_ascii=False, indent=2))
print(f"Neutralized {len(records)} box category labels; source readings were not changed.")
