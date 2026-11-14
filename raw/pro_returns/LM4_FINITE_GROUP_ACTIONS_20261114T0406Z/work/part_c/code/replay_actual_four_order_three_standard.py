#!/usr/bin/env python3
"""Replay the frozen four-kappa program without changing any input byte."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / "work/part_c/four_order_three_standard_peer_replay"
SOURCE = ROOT / "work/part_d_attack/code/actual_four_order_three_standard.py"
META = ROOT / "work/part_d_attack/actual_four_order_three_elements_and_cusp_comparison_result.json"
EXPECTED_PROGRAM = "8aa61eef553c18b74fd78491d1f2c3c124660237e63a7d8209c03b5a8693d7c5"
EXPECTED_META = "c1c043d263c17c78528df0db18fef9c6e57f0c47c438053345d427a2d667b00b"
EXPECTED_OUTPUT = "10af2c129561226b60ee444abf5dc5270428686fbf3bdb8d0ce36912cbdf8497"


def bind(path):
    value = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(value).hexdigest(), "bytes": len(value)}


def verify_routes(metadata_path, groups):
    metadata = json.loads(metadata_path.read_text())
    result = []
    for group in groups:
        for entry in metadata[group]:
            actual = bind(ROOT / entry["path"])
            assert actual["sha256"] == entry["sha256"], entry["path"]
            assert actual["bytes"] == entry["bytes"], entry["path"]
            result.append({"metadata": str(metadata_path.relative_to(ROOT)),
                           "group": group, **actual})
    return result


assert bind(SOURCE)["sha256"] == EXPECTED_PROGRAM
assert bind(META)["sha256"] == EXPECTED_META
direct = verify_routes(META, ("files", "mathematical_dependencies", "primary_copies"))
prior_meta = ROOT / "work/part_d_attack/actual_order_three_defect_and_canonical_candidate_result.json"
prior = verify_routes(prior_meta, ("files", "dependencies", "source_comparison_only"))
assert len(direct) == 22
assert len(prior) == 20
all_routes = direct + prior
all_files = {entry["path"]: entry for entry in all_routes}
all_files[str(META.relative_to(ROOT))] = bind(META)
assert not DEST.exists(), "Preserve existing replays; choose a fresh destination."
DEST.mkdir()
copied = DEST / SOURCE.name
shutil.copyfile(SOURCE, copied)
assert copied.read_bytes() == SOURCE.read_bytes()
started = time.monotonic()
completed = subprocess.run([sys.executable, str(copied)], cwd=DEST,
                           capture_output=True, check=False)
elapsed = time.monotonic() - started
(DEST / "stdout.txt").write_bytes(completed.stdout)
(DEST / "stderr.txt").write_bytes(completed.stderr)
output = DEST / "actual_four_order_three_standard_output.json"
original_output = SOURCE.with_name("actual_four_order_three_standard_output.json")
original_stdout = SOURCE.with_name("actual_four_order_three_standard_stdout.txt")
assert completed.returncode == 0
assert not completed.stderr
assert output.read_bytes() == original_output.read_bytes() == original_stdout.read_bytes() == completed.stdout
assert bind(output)["sha256"] == EXPECTED_OUTPUT
assert bind(copied)["sha256"] == bind(SOURCE)["sha256"] == EXPECTED_PROGRAM
data = json.loads(output.read_text())
assert data["status"] == "PASS"
assert data["assertion_count"] == len(data["checks"]) == 22
assert all(row["passed"] for row in data["checks"])
assert len({row["name"] for row in data["checks"]}) == 22
assert data["actual_finite_image_order"] == 1080
assert len(data["rows"]) == 4
assert [row["epsilon_in_M_over_F"] for row in data["rows"]] == [1, -1, -1, 1]
assert [row["sigma_in_M_abelianization"] for row in data["rows"]] == [1, -1, 1, -1]
assert [row["original_standard_nu"] for row in data["rows"]] == [1, -1, 1, -1]
assert [row["original_cusp_word_is_identity_in_this_image"] for row in data["rows"]] == [False, False, True, True]
assert all(row["finite_image_order"] == 1080 for row in data["rows"])
assert data["rows"][0]["cusp_defect_image"]["PSL2_F5_matrix"] == [0, 2, 2, 4]
assert data["rows"][1]["cusp_defect_image"]["PSL2_F5_matrix"] == [1, 3, 3, 0]
for entry in all_files.values():
    current = bind(ROOT / entry["path"])
    assert current["sha256"] == entry["sha256"], entry["path"]
    assert current["bytes"] == entry["bytes"], entry["path"]
record = {
    "status": "PASS",
    "scope": "Unchanged self-contained program; original standard h=1,t=tau,w=x only.",
    "runner": bind(Path(__file__)),
    "metadata": bind(META),
    "command": [sys.executable, str(copied.relative_to(ROOT))],
    "cwd": str(DEST.relative_to(ROOT)),
    "exit_code": completed.returncode,
    "elapsed_seconds": elapsed,
    "external_program_inputs": [],
    "program": bind(SOURCE),
    "copied_program": bind(copied),
    "source_and_copy_whole_bytes_equal": True,
    "output": bind(output),
    "stdout": bind(DEST / "stdout.txt"),
    "stderr": bind(DEST / "stderr.txt"),
    "original_output": bind(original_output),
    "original_stdout": bind(original_stdout),
    "all_four_output_and_stdout_files_whole_bytes_equal": True,
    "output_transport": "Identity on all bytes; no path, value, order or serialization change.",
    "inverse_output_transport": "Identity on all bytes.",
    "named_checks": 22,
    "actual_standard_image_order": 1080,
    "standard_rows": data["rows"],
    "direct_author_binding_routes_count": len(direct),
    "direct_author_binding_routes": direct,
    "prior_author_binding_routes_count": len(prior),
    "prior_author_binding_routes": prior,
    "unique_frozen_files_including_current_metadata_count": len(all_files),
    "all_frozen_bindings_unchanged_after_replay": True,
    "remaining_actual_target": "No assertion of full H3 generation, full-unit nu0, an original cusp zero, or original T nonemptiness."
}
(DEST / "comparison.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "comparison": bind(DEST / "comparison.json"),
                  "elapsed_seconds": elapsed, "named_checks": 22,
                  "standard_image_order": 1080, "direct_routes": len(direct),
                  "prior_routes": len(prior), "unique_frozen_files": len(all_files)}, indent=2))
