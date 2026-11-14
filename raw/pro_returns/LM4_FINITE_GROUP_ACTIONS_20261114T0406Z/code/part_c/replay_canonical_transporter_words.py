#!/usr/bin/env python3
"""Isolated unchanged replay of the actual canonical-transporter checker."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / "work/part_c/canonical_transporter_peer_replay"
SOURCE = ROOT / "work/part_d_attack/code/actual_canonical_transporter_words.py"
META = ROOT / "work/part_d_attack/actual_canonical_transporter_and_cusp_membership_result.json"
PROGRAM_SHA = "ee354569eedce861e104647f9a190af227ff3e28a133d417b853b2f6bdaf4c33"
META_SHA = "62c400ad942308fb77906084f4cbfbe70a9f9f42fbd5b3fff042a65076bfa08a"
OUTPUT_SHA = "65806b2bd6cf34312ced05a162472182e3f44bdf3012ab062076925b7fc010a9"


def bind(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data), "lines": len(data.splitlines())}


def bindings(value, route=""):
    if isinstance(value, dict):
        if "path" in value and "sha256" in value:
            yield route, value
        for key, item in value.items():
            yield from bindings(item, f"{route}/{key}")
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from bindings(item, f"{route}/{i}")


assert bind(SOURCE)["sha256"] == PROGRAM_SHA
assert bind(META)["sha256"] == META_SHA
author = json.loads(META.read_text())
routes = []
for route, entry in bindings(author):
    actual = bind(ROOT / entry["path"])
    for key in ("sha256", "bytes", "lines"):
        if key in entry:
            assert actual[key] == entry[key], (route, key)
    routes.append({"route": route, **actual})
assert len(routes) == 12
assert author["verification"]["program_external_inputs"] == []

# Retain the already accepted predecessor's entire explicitly bound closure.
# These are source bindings, not additional inputs imported by this checker.
prior_meta = ROOT / "work/part_d_attack/actual_four_order_three_elements_and_cusp_comparison_result.json"
prior_routes = []
for route, entry in bindings(json.loads(prior_meta.read_text())):
    actual = bind(ROOT / entry["path"])
    for key in ("sha256", "bytes", "lines"):
        if key in entry:
            assert actual[key] == entry[key], (route, key)
    prior_routes.append({"route": route, **actual})

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
output = DEST / "actual_canonical_transporter_words_output.json"
original_output = SOURCE.with_name(output.name)
original_stdout = SOURCE.with_name("actual_canonical_transporter_words_stdout.txt")
assert done.returncode == 0 and done.stderr == b""
assert output.read_bytes() == done.stdout == original_output.read_bytes() == original_stdout.read_bytes()
assert bind(output)["sha256"] == OUTPUT_SHA
data = json.loads(output.read_text())
assert data["status"] == "PASS"
assert data["named_check_count"] == len(data["checks"]) == 20
assert all(check["status"] == "PASS" for check in data["checks"])
assert len({check["name"] for check in data["checks"]}) == 20
assert data["universal_odd_exponent_cases"] == 17
assert len(data["integral_branch_cases"]) == 19
assert data["standard_input"] == {
    "h": "1", "a": "1", "L": "1", "k": 0, "nu0": 1,
    "kappa_plus": "xi", "A": "x", "B": "1", "T_parameters": [-1, 1]}
for row in data["integral_branch_cases"]:
    k = row["k"]
    assert row["branch"] == ("A" if k % 2 else "B")
    assert row["z_exponent"] == (-(k + 1) // 2 if k % 2 else -k // 2)
for entry in routes + prior_routes:
    actual = bind(ROOT / entry["path"])
    assert all(actual[key] == entry[key] for key in ("sha256", "bytes", "lines"))
assert bind(META)["sha256"] == META_SHA
assert bind(copied)["sha256"] == PROGRAM_SHA

record = {
    "status": "PASS", "date": "2026-11-14",
    "scope": "Universal word identities and the original standard h=1; formal letters are not new original inputs.",
    "runner": bind(Path(__file__)), "author_metadata": bind(META),
    "command": [sys.executable, str(copied.relative_to(ROOT))],
    "cwd": str(DEST.relative_to(ROOT)), "elapsed_seconds": elapsed,
    "exit_code": done.returncode, "external_computational_inputs": [],
    "program": bind(SOURCE), "copied_program": bind(copied),
    "program_copy_whole_bytes_identical": True,
    "author_output": bind(original_output), "author_stdout": bind(original_stdout),
    "replay_output": bind(output), "replay_stdout": bind(DEST / "stdout.txt"),
    "replay_stderr": bind(DEST / "stderr.txt"),
    "whole_output_raw_byte_identity": True,
    "output_path_or_schema_rewrite_used": False,
    "named_checks": 20, "universal_odd_exponent_cases": 17,
    "integral_branch_cases": 19,
    "author_routes_verified_before_and_after": routes,
    "predecessor_metadata": bind(prior_meta),
    "predecessor_routes_verified_before_and_after": prior_routes,
    "all_frozen_inputs_unchanged": True
}
(DEST / "comparison.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "named_checks": 20,
                  "universal_odd_exponent_cases": 17, "integral_branch_cases": 19,
                  "direct_binding_routes": len(routes),
                  "predecessor_binding_routes": len(prior_routes),
                  "comparison": bind(DEST / "comparison.json")}, indent=2))
