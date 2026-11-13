#!/usr/bin/env python3
"""Root replay of E.25--E.26 with original certificates kept unchanged."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPLAY = HERE / "root_e24_binary_replay"
PROGRAMS = ("bc_distribution_quartic", "bc_cm_fermat_factorization")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    previous = json.loads((HERE / "audit_binary_root_retry.json").read_text())
    assert previous["all_passed"] and previous["original_artifacts_unchanged"]
    dependencies = previous["protected_artifact_sha256"]
    assert all(digest(HERE / name) == sha for name, sha in dependencies.items())
    protected = [HERE / "bc_cm_literal_words.json"]
    protected += [p for p in HERE.iterdir() if p.is_file() and (
        p.name == "bc_distribution_quartic.py" or
        p.name.startswith("bc_distribution_quartic_2_3_4_6_12.") or
        p.name.startswith("bc_cm_fermat_factorization."))]
    before = {p.name: digest(p) for p in protected}
    for name in ("bc_distribution_quartic.py", "bc_cm_fermat_factorization.py",
                 "bc_cm_literal_words.json"):
        assert not (REPLAY / name).exists()
        shutil.copy2(HERE / name, REPLAY / name)
    rows = []
    started = time.time()
    for stem in PROGRAMS:
        begin = time.time()
        output = REPLAY / (stem + "_root_check.out")
        with output.open("x") as stream:
            run = subprocess.run([sys.executable, "-u", str(REPLAY / (stem + ".py"))],
                                 cwd=REPLAY, stdout=stream, stderr=subprocess.STDOUT)
        row = {"program": stem + ".py", "output": str(output.relative_to(HERE)),
               "exit_code": run.returncode,
               "elapsed_seconds": round(time.time() - begin, 3),
               "program_sha256": digest(REPLAY / (stem + ".py")),
               "output_sha256": digest(output)}
        rows.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode:
            break
    unchanged = all(digest(HERE / name) == value for name, value in before.items())
    result = {"programs": rows,
              "all_passed": len(rows) == len(PROGRAMS)
                            and all(r["exit_code"] == 0 for r in rows),
              "original_artifacts_unchanged": unchanged,
              "protected_artifact_sha256": before,
              "dependency_manifest": "root_e24_binary_replay/original_input_manifest.json",
              "elapsed_seconds": round(time.time() - started, 3)}
    HERE.joinpath("audit_geometry_cm_root.json").write_text(
        json.dumps(result, indent=2) + "\n")
    assert unchanged, "An original certificate changed during replay"
    assert result["all_passed"], "An E.25 or E.26 certificate failed"
    print("ROOT_GEOMETRY_CM_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
