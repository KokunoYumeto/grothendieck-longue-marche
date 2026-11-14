#!/usr/bin/env python3
"""Peer replay of the frozen actual-transporter finite quotient producer."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
AUTHOR = ROOT / "work/part_d_attack"
OUT = ROOT / "work/part_c/actual_transporter_independent_replay"
OUT.mkdir(parents=True, exist_ok=True)

EXPECTED = {
    "actual_transporter_single_parameter_reduction.txt": "7ba862392788a46b4fa92563ae0c5cea293897fd8d39ac9d27a17e2ab6826b49",
    "actual_transporter_single_parameter_reduction_result.json": "cc281bb8abf4e351971891dc881106143449491d81abef5ce33d10cde632d4bf",
    "code/actual_transporter_reduction.py": "a0507439a6132be28aca56fb4c4d5d7316fb2fa103c8c181664acbcb970c3c2b",
    "code/actual_transporter_reduction_output.json": "43f8ceef3d62899e624a99b3699fcc17256c9dae49f8599d6c45a43c5b52b92d",
    "code/actual_transporter_reduction_stdout.txt": "43f8ceef3d62899e624a99b3699fcc17256c9dae49f8599d6c45a43c5b52b92d",
}

def binding(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}

before = {name: binding(AUTHOR / name) for name in EXPECTED}
assert all(before[name]["sha256"] == digest for name, digest in EXPECTED.items())
meta = json.loads((AUTHOR / "actual_transporter_single_parameter_reduction_result.json").read_text())
dependencies = []
for row in meta["files"] + meta["dependency_bindings"]:
    observed = binding(ROOT / row["path"])
    assert observed["sha256"] == row["sha256"] and observed["bytes"] == row["bytes"]
    dependencies.append(observed)

script = OUT / "actual_transporter_reduction.py"
shutil.copyfile(AUTHOR / "code/actual_transporter_reduction.py", script)
assert script.read_bytes() == (AUTHOR / "code/actual_transporter_reduction.py").read_bytes()
run = subprocess.run([sys.executable, str(script)], cwd=OUT, capture_output=True, check=False)
(OUT / "replay_stdout.txt").write_bytes(run.stdout)
(OUT / "replay_stderr.txt").write_bytes(run.stderr)
assert run.returncode == 0 and not run.stderr
generated = OUT / "actual_transporter_reduction_output.json"
expected_output = (AUTHOR / "code/actual_transporter_reduction_output.json").read_bytes()
assert generated.read_bytes() == run.stdout == expected_output
assert run.stdout == (AUTHOR / "code/actual_transporter_reduction_stdout.txt").read_bytes()
data = json.loads(run.stdout)
assert data["status"] == "PASS" and data["assertion_count"] == 24
assert len(data["checks"]) == 24 and all(row["passed"] for row in data["checks"])
assert len(data["base_rows"]) == 16 and len(data["refined_rows"]) == 32
assert all(row["B_conjugator_count_in_A5_times_C2_squared"] in (0, 20)
           for row in data["base_rows"])
assert all(not row["B_nonempty"] or
           row["solution_coset_count"] * row["solutions_per_base_coset"] == 40960
           for row in data["refined_rows"])

after = {name: binding(AUTHOR / name) for name in EXPECTED}
assert after == before
for row in dependencies:
    assert binding(ROOT / row["path"]) == row

record = {
    "status": "PASS",
    "reviewer": "/root/c89_review_and_general_c",
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "method": "Unchanged self-contained producer copied to an isolated peer directory and executed without importing or modifying the original file.",
    "exit_code": run.returncode,
    "named_assertions": data["assertion_count"],
    "base_unit_rows": len(data["base_rows"]),
    "refined_unit_rows": len(data["refined_rows"]),
    "retained_refined_conjugator_witnesses": sum(len(row["one_chain_per_solution_coset"]) for row in data["refined_rows"]),
    "output_and_stdout_raw_bytes_equal_to_both_frozen_outputs": True,
    "path_transport_applied": False,
    "all_frozen_files_and_dependencies_unchanged": True,
    "frozen_files": list(before.values()),
    "metadata_file_and_dependency_bindings": dependencies,
    "replay_files": [binding(script), binding(generated), binding(OUT / "replay_stdout.txt"), binding(OUT / "replay_stderr.txt")],
    "checks": data["checks"],
    "base_B_unit_residues": data["base_B_unit_residues"],
    "base_T_unit_residues": data["base_T_unit_residues"],
    "refined_B_unit_residues": data["refined_B_unit_residues"],
    "refined_T_unit_residues": data["refined_T_unit_residues"],
}
(OUT / "comparison.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": record["status"], "assertions": record["named_assertions"],
                  "witnesses": record["retained_refined_conjugator_witnesses"],
                  "comparison": binding(OUT / "comparison.json")}, indent=2))
