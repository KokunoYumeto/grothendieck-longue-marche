#!/usr/bin/env python3
"""Isolated unchanged-program replay of the frozen D order-three calculation."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / "work/part_c/order_three_defects_peer_replay"
SOURCE = ROOT / "work/part_d_attack/code/actual_order_three_defects.py"
EXPECTED_PROGRAM = "ca6b10f52c3be47e6835d8fec7ea45faf63f62474338d86df54496661806e5eb"
EXPECTED_OUTPUT = "634910286efa79d802c6c08efa0f131b987b9ea2f329bccb0e0b22927fe6a5d4"
META = ROOT / "work/part_d_attack/actual_order_three_defect_and_canonical_candidate_result.json"
EXPECTED_META = "b5c422c5570c93f8ce4c795412a8426d9c7d3edd88e5465984ccd3b8fd087923"

def bind(path):
    value = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(value).hexdigest(),
            "bytes": len(value)}

assert bind(SOURCE)["sha256"] == EXPECTED_PROGRAM
assert bind(META)["sha256"] == EXPECTED_META
metadata = json.loads(META.read_text())
bindings = []
for group in ("files", "dependencies", "source_comparison_only"):
    for entry in metadata[group]:
        actual = bind(ROOT / entry["path"])
        assert actual["sha256"] == entry["sha256"], entry["path"]
        assert actual["bytes"] == entry["bytes"], entry["path"]
        bindings.append({"group": group, **actual})
assert not DEST.exists(), "Preserve every existing replay; use a fresh destination."
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
output = DEST / "actual_order_three_defects_output.json"
original_output = ROOT / "work/part_d_attack/code/actual_order_three_defects_output.json"
original_stdout = ROOT / "work/part_d_attack/code/actual_order_three_defects_stdout.txt"
assert completed.returncode == 0
assert not completed.stderr
assert output.read_bytes() == original_output.read_bytes() == original_stdout.read_bytes() == completed.stdout
assert bind(output)["sha256"] == EXPECTED_OUTPUT
assert bind(copied)["sha256"] == bind(SOURCE)["sha256"] == EXPECTED_PROGRAM
data = json.loads(output.read_text())
assert data["status"] == "PASS"
assert data["assertion_count"] == len(data["checks"]) == 24
assert all(row["passed"] for row in data["checks"])
assert data["c_word_count"] == 161
assert data["defect_case_count"] == 644
assert data["finite_nonzero_separations_by_prime"] == {"3": 598, "5": 44}
assert data["simultaneous_solutions_in_corpus"] == [
    {"nu": -1, "epsilon": 1, "c": "y"},
    {"nu": 1, "epsilon": -1, "c": "x^-1"}]
for entry in bindings:
    assert bind(ROOT / entry["path"])["sha256"] == entry["sha256"]
record = {
    "status": "PASS",
    "scope": "Unchanged frozen program, actual original standard h=1, g=x^-1, w=x, nu=-1,+1 only.",
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
    "output_transport": "Identity on all bytes; no path, value, order, or serialization change.",
    "inverse_output_transport": "Identity on all bytes.",
    "named_checks": 24,
    "free_word_count": 161,
    "defect_cases": 644,
    "finite_nonzero_separations": 642,
    "finite_nonzero_separations_by_prime": data["finite_nonzero_separations_by_prime"],
    "simultaneous_solutions_in_corpus": data["simultaneous_solutions_in_corpus"],
    "all_20_author_file_and_dependency_bindings": bindings,
    "all_bindings_unchanged_after_replay": True,
    "remaining_actual_target": "Neither full-unit m nor W=1 nor nonemptiness of original T is proved."
}
(DEST / "comparison.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "comparison": bind(DEST / "comparison.json"),
                  "elapsed_seconds": elapsed, "named_checks": 24, "cases": 644,
                  "finite_separations": 642}, indent=2))
