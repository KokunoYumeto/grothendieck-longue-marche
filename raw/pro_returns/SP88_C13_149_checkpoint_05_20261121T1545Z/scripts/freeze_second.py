"""Seal a completed image-only reading before comparing it with the first."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1])
stem = f"149_scan{scan:03d}"
second = ROOT / "second"
reading = second / f"{stem}_second.tsv"
observations = second / f"{stem}_second_observations.json"
with (second / f"{stem}_boxes.tsv").open() as handle:
    expected = [row["box"] for row in csv.DictReader(handle, delimiter="\t")]
with reading.open() as handle:
    rows = list(csv.DictReader(handle, delimiter="\t"))
if [row["box"] for row in rows] != expected or any(not row["reading"].strip() for row in rows):
    raise SystemExit("The independent reading must contain every box, in order.")
json.loads(observations.read_text())
manifest_path = second / "SECOND_READINGS_SHA256.json"
manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
if stem in manifest:
    raise SystemExit("This independent reading has already been sealed.")
manifest[stem] = {
    "sealed_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    "files": [
        {"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        for path in (reading, observations)
    ],
}
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"scan": scan, "sealed_boxes": len(rows)}))
