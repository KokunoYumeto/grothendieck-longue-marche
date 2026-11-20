"""Make a blind reader's fresh crops from only the scan and neutral box list.

No witness, first reading, page text, record, or notes are opened here.
The reader still has to view and transcribe every resulting image.
"""
from pathlib import Path
import csv
import json
import subprocess
import sys

work = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1])
with (work / "second" / f"147_scan{scan:03d}_boxes.tsv").open() as source:
    boxes = list(csv.DictReader(source, delimiter="\t"))
for box in boxes:
    suffix = box["box"].split("-")[-1]
    name = "audit_" + suffix
    target = work / "crops" / f"147_scan{scan:03d}_{name}.jpg"
    if target.exists():
        raise SystemExit(f"Refusing to replace existing blind crop: {target}")
    subprocess.run(
        [sys.executable, str(work / "scripts" / "crop.py"), str(scan), name]
        + [box[key] for key in ("x0", "y0", "x1", "y1")],
        check=True,
        capture_output=True,
        text=True,
    )
    print(json.dumps({"box": box["box"], "crop": str(target)}))
