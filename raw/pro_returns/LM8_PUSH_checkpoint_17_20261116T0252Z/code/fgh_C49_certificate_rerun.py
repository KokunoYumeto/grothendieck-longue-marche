#!/usr/bin/env python3
"""Read-only independent replay of the owner's exact C49 certificate."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root / "code/pbc_cm_frames_24_60.py"
namespace = {"__name__": "fgh_C49_independent_replay", "__file__": str(source)}
exec(compile(source.read_text(), str(source), "exec"), namespace)
result = {
    "status": "PASS",
    "levels": [namespace["run_level"](24), namespace["run_level"](60)],
    "local_norm_lift_checks": namespace["norm_lift_checks"](),
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "scope": "Exact finite certificate for a structural actual-image proof. Galois/full-group liftability is not inferred merely from finite solutions.",
}
owner = json.loads(source.with_suffix(".json").read_text())
assert json.loads(json.dumps(result)) == owner
destination = root / "notes/fgh_C49_certificate_rerun.json"
destination.write_text(json.dumps(result, indent=2) + "\n")
assert destination.read_bytes() == source.with_suffix(".json").read_bytes()
print(json.dumps({"status": "PASS", "whole_json_byte_equal": True,
                  "source_sha256": result["source_sha256"],
                  "result_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
                  "levels": [{k: row[k] for k in ("level", "signed_pure_order", "signed_pure_derived_order", "paired_CM_order", "framed_image_order", "arithmetic_kernel_order")}
                             for row in result["levels"]]}, indent=2))
