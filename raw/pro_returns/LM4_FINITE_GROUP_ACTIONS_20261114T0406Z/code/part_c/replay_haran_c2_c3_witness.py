#!/usr/bin/env python3
"""Isolated byte-identical replay of the frozen Haran finite witness."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / "work/part_c/haran_c2_c3_peer_replay"
SOURCE = ROOT / "work/part_d_attack/code/haran_c2_c3_marked_subgroup_witness.py"
META = ROOT / "work/part_d_attack/haran_c2_c3_actual_map_comparison_result.json"
PROGRAM_SHA = "5b84d0a79f60e5533aa8673906da23f4e03aaf3e4877d788323b8f6b5a2779c6"
META_SHA = "fcac5535d5ba53ae9c67a4d09823c7c2970124466da6160abe6dbdb336d1d39d"
OUTPUT_SHA = "612e55e5d4ed6e37bc97e18b5dbe530b81a7cd5a14d34c66d08830bc6c46a57f"


def bind(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


assert bind(SOURCE)["sha256"] == PROGRAM_SHA
assert bind(META)["sha256"] == META_SHA
metadata = json.loads(META.read_text())
routes = []
for group in ("files", "mathematical_dependencies", "primary_source_copies"):
    for entry in metadata[group]:
        actual = bind(ROOT / entry["path"])
        assert actual["sha256"] == entry["sha256"]
        assert actual["bytes"] == entry["bytes"]
        routes.append({"group": group, **actual})
assert len(routes) == 11
assert not DEST.exists()
DEST.mkdir()
copied = DEST / SOURCE.name
shutil.copyfile(SOURCE, copied)
assert copied.read_bytes() == SOURCE.read_bytes()
started = time.monotonic()
done = subprocess.run([sys.executable, str(copied)], cwd=DEST,
                      capture_output=True, check=False)
elapsed = time.monotonic() - started
(DEST / "stdout.txt").write_bytes(done.stdout)
(DEST / "stderr.txt").write_bytes(done.stderr)
output = DEST / "haran_c2_c3_marked_subgroup_witness_output.json"
original_output = SOURCE.with_name(output.name)
original_stdout = SOURCE.with_name("haran_c2_c3_marked_subgroup_witness_stdout.txt")
assert done.returncode == 0 and not done.stderr
assert output.read_bytes() == done.stdout == original_output.read_bytes() == original_stdout.read_bytes()
assert bind(output)["sha256"] == OUTPUT_SHA
data = json.loads(output.read_text())
assert data["status"] == "PASS"
assert data["named_check_count"] == len(data["checks"]) == 11
assert all(check["status"] == "PASS" for check in data["checks"])
assert len({check["name"] for check in data["checks"]}) == 11
assert data["S3_conjugator_pair_cases"] == 36
assert data["proper_image_order"] == 6
assert data["proper_image_fixed_point"] == 3
assert data["tau_image"] == [2, 1, 3, 4]
assert data["xi_image"] == [3, 2, 4, 1]
assert data["r_image"] == [2, 3, 4, 1]
assert data["conjugate_image"] == [2, 4, 3, 1]
assert data["J_star_inversion_defect_image"] == [3, 4, 1, 2]
for entry in routes:
    assert bind(ROOT / entry["path"])["sha256"] == entry["sha256"]
assert bind(META)["sha256"] == META_SHA
assert bind(copied)["sha256"] == bind(SOURCE)["sha256"] == PROGRAM_SHA
record = {
    "status": "PASS",
    "scope": "Exact S4 and S3 maps only; no finite values assigned to a nonstandard original h,j,H3.",
    "runner": bind(Path(__file__)),
    "metadata": bind(META),
    "command": [sys.executable, str(copied.relative_to(ROOT))],
    "cwd": str(DEST.relative_to(ROOT)),
    "elapsed_seconds": elapsed,
    "exit_code": done.returncode,
    "external_computational_inputs": [],
    "program": bind(SOURCE),
    "copied_program": bind(copied),
    "program_copy_whole_bytes_identical": True,
    "output": bind(output),
    "stdout": bind(DEST / "stdout.txt"),
    "stderr": bind(DEST / "stderr.txt"),
    "original_output": bind(original_output),
    "original_stdout": bind(original_stdout),
    "all_four_output_and_stdout_files_whole_bytes_identical": True,
    "forward_output_transport": "Identity on all bytes.",
    "inverse_output_transport": "Identity on all bytes.",
    "named_checks": 11,
    "S3_conjugator_pairs": 36,
    "S4_image_order": 24,
    "proper_image_order": 6,
    "proper_image_fixed_point": 3,
    "standard_J_inversion_defect": [3, 4, 1, 2],
    "author_routes_verified": routes,
    "all_author_routes_unchanged_after_replay": True,
    "retained_unresolved": "No identification of Hstar or H1 with original H3, and no new full image, unit or original cusp conclusion."
}
comparison = DEST / "comparison.json"
comparison.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "comparison": bind(comparison),
                  "named_checks": 11, "S3_pairs": 36}, indent=2))
