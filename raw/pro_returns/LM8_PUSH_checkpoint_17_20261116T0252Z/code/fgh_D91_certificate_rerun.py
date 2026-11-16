#!/usr/bin/env python3
"""Independent read-only replay of the complete D91 literal certificate."""
from pathlib import Path
import hashlib
import json
import runpy

root = Path(__file__).resolve().parents[1]
source = root / "notes/de_sha_cusp_complete_certificate.py"
original = json.loads(source.with_suffix(".json").read_text())
actual = runpy.run_path(str(source), run_name="fgh_D91")["run"]()
actual["source_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
# Elapsed time is provenance of the author's run, not a mathematical output.
assert {k: v for k, v in original.items() if k != "elapsed_seconds"} == actual
result = {
    "status": "PASS",
    "all_mathematical_and_source_fields_equal": True,
    "elapsed_seconds_excluded_from_comparison": original["elapsed_seconds"],
    "source_sha256": actual["source_sha256"],
    "original_json_sha256": hashlib.sha256(source.with_suffix(".json").read_bytes()).hexdigest(),
    "literal_middle_cases": len(actual["middle_rows"]),
    "literal_target_cases": len(actual["target_rows"]),
    "independent_result": actual,
}
(root / "notes/fgh_D91_certificate_rerun.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "independent_result"}, indent=2))
