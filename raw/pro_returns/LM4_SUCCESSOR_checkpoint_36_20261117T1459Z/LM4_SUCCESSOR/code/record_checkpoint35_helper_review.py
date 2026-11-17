"""Bind root's completed entire-source audit of the five35 helper adaptations."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
manifest = root / "records/checkpoint35_helper_source_adaptation.json"
rows = json.loads(manifest.read_text())["copies"]
assert len(rows) == 5
for row in rows:
    for kind in ("source", "target"):
        raw = (root / row[kind]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row[kind + "_sha256"]
    compile((root / row["target"]).read_text(), row["target"], "exec")
record = {
    "recorded_at": datetime.now(timezone.utc).isoformat(),
    "reviewer": "/root", "status": "PASS_ENTIRE_SOURCE_AND_ADAPTATION_REVIEW",
    "source_scope": "All five complete35 sources read,867lines; entire adaptation diff read, including a bounded re-read of the initially truncated middle. No truncated output counted as complete.",
    "copies": rows,
    "diff_sha256": hashlib.sha256((root / "records/checkpoint35_helper_source_adaptation.diff").read_bytes()).hexdigest(),
    "checks": [
        "Exact parent34 identity529409669bytes and28dbe8b3...;10387parent entries+152653inherited rows=163040.",
        "Previously observed actual verifier sessions and chunks, not inferred process success.",
        "All immutable parent paths/bytes and historical key identities remain covered; mutable retention records must still equal archived34 before commit.",
        "Closed35 induction never trusts the workspace retention table; complete parent map and exact composition checked.",
        "Native system-tar restoration verifies all original paths and bytes, with actual64MiB properties for all three35 streams.",
        "Estimator measures complete prospective35 streams; original mainPDF subtraction requires its exact old bytes in the measured document TAR, its changed new payload separately counted, and disjointness from migrated data. Every header and5MB allowance retained."
    ],
    "helpers_executed_by_this_review": False,
    "creates_zip": False,
    "retention_published": False,
    "packager_installation": "Separate actual-gain gate, not asserted by this record."
}
target = root / "records/checkpoint35_root_helper_review.json"
with target.open("x") as stream:
    json.dump(record, stream, indent=2)
    stream.write("\n")
print(json.dumps({"path": str(target.relative_to(root)),
                  "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}, indent=2))
