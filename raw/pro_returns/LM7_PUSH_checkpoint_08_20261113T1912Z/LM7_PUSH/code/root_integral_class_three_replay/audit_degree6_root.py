#!/usr/bin/env python3
"""Sequential root replay of the complete degree-six Ferrari certificates.

Original agent stdout is retained; each replay has a separate output file.
Input programs are hashed before and after the run.  The independent model
check precedes the complete kernel, lift, generation and whole-plane audits.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
PROGRAMS = (
    "de_ferrari_degree6_model_audit",
    "de_ferrari_degree6_kernel",
    "de_ferrari_degree6_lift",
    "de_ferrari_degree6_generation",
    "de_ferrari_degree6_wholeplanes",
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    protected = [HERE / (s + ".out") for s in PROGRAMS]
    protected += [HERE / (s + ".py") for s in PROGRAMS]
    before = {p.name: sha256(p) for p in protected}
    results = []
    started = time.time()
    for stem in PROGRAMS:
        output = HERE / (stem + "_root_check.out")
        assert not output.exists(), "Preserve every prior root replay"
        begin = time.time()
        with output.open("x") as stream:
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
    after = {p.name: sha256(p) for p in protected}
    result = {"programs": results,
              "all_passed": len(results) == len(PROGRAMS)
                            and all(r["exit_code"] == 0 for r in results),
              "original_programs_and_stdout_unchanged": before == after,
              "protected_artifact_sha256": before,
              "elapsed_seconds": round(time.time() - started, 3)}
    (HERE / "audit_degree6_root.json").write_text(json.dumps(result, indent=2) + "\n")
    assert before == after, "An original program or stdout changed during replay"
    assert result["all_passed"], "A degree-six certificate failed"
    print("ROOT_DEGREE6_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
