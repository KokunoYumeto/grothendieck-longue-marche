#!/usr/bin/env python3
"""Root replay of E.24 in a copied, fully retained certificate directory.

All original programs, certificates, and stdout files remain byte-identical.
The copied code directory records every new certificate and stdout from this
audit.  There are no symbolic links to mutable original outputs.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
DEST = HERE / "root_e24_binary_replay"
PROGRAMS = (
    "de_ferrari_two_model",
    "de_ferrari_two_lower",
    "de_ferrari_two_module",
    "de_ferrari_two_lift",
    "de_ferrari_two_generation",
    "de_ferrari_two_collection_audit",
    "de_ferrari_two_joint_control",
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert not DEST.exists(), "Retain earlier replays under their existing names"
    DEST.mkdir()
    inputs = sorted(p for p in HERE.iterdir()
                    if p.is_file() and p.name.startswith("de_")
                    and p.suffix in (".py", ".json", ".npz", ".csv"))
    protected = inputs + [HERE / (s + ".out") for s in PROGRAMS]
    before = {p.name: digest(p) for p in protected}
    for path in inputs:
        shutil.copy2(path, DEST / path.name)
    (DEST / "original_input_manifest.json").write_text(
        json.dumps(before, indent=2) + "\n")
    rows = []
    started = time.time()
    for stem in PROGRAMS:
        begin = time.time()
        output = DEST / (stem + "_root_check.out")
        with output.open("x") as stream:
            run = subprocess.run([sys.executable, "-u", str(DEST / (stem + ".py"))],
                                 cwd=DEST, stdout=stream, stderr=subprocess.STDOUT)
        row = {"program": stem + ".py", "output": str(output.relative_to(HERE)),
               "exit_code": run.returncode,
               "elapsed_seconds": round(time.time() - begin, 3),
               "program_sha256": digest(DEST / (stem + ".py")),
               "output_sha256": digest(output)}
        rows.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode:
            break
    after = {p.name: digest(p) for p in protected}
    result = {"programs": rows,
              "all_passed": len(rows) == len(PROGRAMS)
                            and all(r["exit_code"] == 0 for r in rows),
              "original_artifacts_unchanged": before == after,
              "protected_artifact_sha256": before,
              "elapsed_seconds": round(time.time() - started, 3)}
    HERE.joinpath("audit_binary_root.json").write_text(
        json.dumps(result, indent=2) + "\n")
    assert before == after, "An original artifact changed during replay"
    assert result["all_passed"], "An E.24 certificate failed"
    print("ROOT_BINARY_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
