#!/usr/bin/env python3
"""Sequential root rerun of the corrected degree-five certificates.

Each child has its own retained stdout/stderr file.  The failed initial
certificates and their explicitly labelled reproduction are never touched.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
PROGRAMS = (
    "de_ferrari_degree5_kernel",
    "de_ferrari_degree5_lift",
    "de_ferrari_degree5_control",
    "de_ferrari_degree5_generation",
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    protected = sorted(HERE.glob("de_ferrari_degree5_*failed_initial*"))
    before = {p.name: sha256(p) for p in protected if p.is_file()}
    results = []
    started = time.time()
    for stem in PROGRAMS:
        output = HERE / (stem + "_root_check.out")
        begin = time.time()
        with output.open("w") as stream:
            run = subprocess.run([sys.executable, "-u", str(HERE / (stem + ".py"))],
                                 cwd=HERE, stdout=stream, stderr=subprocess.STDOUT)
        row = {"program": stem + ".py", "output": output.name,
               "exit_code": run.returncode,
               "elapsed_seconds": round(time.time() - begin, 3),
               "program_sha256": sha256(HERE / (stem + ".py")),
               "output_sha256": sha256(output)}
        results.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode:
            break
    after = {p.name: sha256(p) for p in protected if p.is_file()}
    result = {"programs": results,
              "all_passed": len(results) == len(PROGRAMS)
                            and all(r["exit_code"] == 0 for r in results),
              "failed_initial_artifacts_unchanged": before == after,
              "protected_artifact_sha256": before,
              "elapsed_seconds": round(time.time() - started, 3)}
    (HERE / "audit_degree5_root.json").write_text(json.dumps(result, indent=2) + "\n")
    assert before == after, "A retained failed-initial artifact changed"
    assert result["all_passed"], "A corrected degree-five certificate failed"
    print("ROOT_DEGREE5_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
