#!/usr/bin/env python3
"""Isolate and replay the unchanged F33 literal-word certificate checker."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
AUTHOR = ROOT / "work/part_a/code"
DEST = ROOT / "work/part_c/f33_peer_replay"
NAME = "affine_nonproduct_sign_pair_independent_audit"
PROGRAM = AUTHOR / f"{NAME}.py"
OUTPUT = AUTHOR / f"{NAME}_output.json"
STDOUT = AUTHOR / f"{NAME}_stdout.txt"


def bind(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


assert bind(PROGRAM)["sha256"] == "ce73e213189a8c63ca72d2c43c71d3caaac6cd7061736d598050bb1076cead0b"
assert bind(OUTPUT)["sha256"] == "07b92a66895988a539ba886a260883325f6fd1862b3ed499c22ac2a2d552c3bf"
assert bind(STDOUT)["sha256"] == "bd4166ce8b078185afe93a62a00057189c7a8a10ee8779b06953fa60632278e7"
expected = json.loads(OUTPUT.read_text())
assert len(expected["input_bindings"]) == 8
assert not DEST.exists()
DEST.mkdir()
copied = DEST / PROGRAM.name
shutil.copyfile(PROGRAM, copied)
input_copies = []
for entry in expected["input_bindings"]:
    original = AUTHOR / entry["path"]
    before = bind(original)
    assert before["sha256"] == entry["sha256"] and before["bytes"] == entry["bytes"]
    target = DEST / entry["path"]
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(original, target)
    assert original.read_bytes() == target.read_bytes()
    input_copies.append({"relative_input": entry["path"],
                         "original": before, "copy": bind(target),
                         "complete_bytes_identical": True})
assert PROGRAM.read_bytes() == copied.read_bytes()
started = time.monotonic()
done = subprocess.run([sys.executable, str(copied)], cwd=DEST,
                      capture_output=True, check=False)
elapsed = time.monotonic() - started
(DEST / "stdout.txt").write_bytes(done.stdout)
(DEST / "stderr.txt").write_bytes(done.stderr)
new_output = DEST / OUTPUT.name
assert done.returncode == 0 and done.stderr == b""
assert done.stdout == STDOUT.read_bytes()
assert new_output.read_bytes() == OUTPUT.read_bytes()
actual = json.loads(new_output.read_text())
assert actual == expected
assert actual["check_count"] == 252309
assert actual["literal_sources"] == 19 and actual["original_source_rows"] == 64
assert [row["certified_rank"] for row in actual["charts"]] == [13, 13, 13, 13]
assert [row["single_pivots"] for row in actual["charts"]] == [13, 11, 13, 13]
assert actual["charts"][1]["terminal_block_rows"] == [35, 51]
for item in input_copies:
    assert bind(ROOT / item["original"]["path"]) == item["original"]
    assert bind(ROOT / item["copy"]["path"]) == item["copy"]
assert bind(PROGRAM)["sha256"] == bind(copied)["sha256"]
record = {
    "status": "PASS", "date": "2026-11-14",
    "runner": bind(Path(__file__)),
    "command": [sys.executable, str(copied.relative_to(ROOT))],
    "cwd": str(DEST.relative_to(ROOT)), "elapsed_seconds": elapsed,
    "exit_code": done.returncode,
    "checker_original": bind(PROGRAM), "checker_copy": bind(copied),
    "input_copies": input_copies,
    "author_output": bind(OUTPUT), "output": bind(new_output),
    "author_stdout": bind(STDOUT), "stdout": bind(DEST / "stdout.txt"),
    "stderr": bind(DEST / "stderr.txt"),
    "raw_output_whole_bytes_identical": True,
    "raw_stdout_whole_bytes_identical": True,
    "output_rewriting_required": False,
    "checks": 252309, "literal_negative_sources": 19,
    "original_source_rows": 64, "chart_ranks": [13, 13, 13, 13],
    "single_pivots": [13, 11, 13, 13], "terminal_block_rows": [35, 51],
    "all_frozen_inputs_unchanged": True,
    "scope": "Original literal F23 negative braids, their eight seeds and eleven actions; all64 source rows and four Laurent certificates. The separate proof/domain audit handles all-field units and the odd-characteristic paired inverse."
}
(DEST / "comparison.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "checks": 252309,
                  "comparison": bind(DEST / "comparison.json")}, indent=2))
