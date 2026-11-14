#!/usr/bin/env python3
"""Replay the complete order-three test and exponent-four boundary refinement.

The earlier root batch owns the shared isolated replay directory until its
completion certificate exists.  This batch then checks every static Python
dependency and protects all original programs, outputs and certificates.
"""
from pathlib import Path
import ast
import hashlib
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPLAY = HERE / "root_e24_binary_replay"
PROGRAMS = (
    "de_ferrari_three_conjugacy",
    "de_ferrari_three_torsion",
    "de_ferrari_three_torsion_words",
    "bc_fermat_class_two_four",
    "bc_fermat_class_two_four_kernel",
    "bc_fermat_class_two_four_fibres",
    "bc_fermat_class_two_four_central",
    "bc_fermat_class_two_crt",
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dependencies():
    seen, pending = set(), list(PROGRAMS)
    while pending:
        name = pending.pop()
        path = HERE / (name + ".py")
        if name in seen or not path.exists():
            continue
        seen.add(name)
        for node in ast.walk(ast.parse(path.read_text())):
            modules = []
            if isinstance(node, ast.Import):
                modules = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules = [node.module]
            pending.extend(m for m in modules if (HERE / (m + ".py")).exists())
    return sorted(seen - set(PROGRAMS))


def main():
    prior = HERE / "audit_new_refinements_root.json"
    print("Waiting for exclusive access to the isolated replay directory.", flush=True)
    while not prior.exists():
        time.sleep(5)
    cert = json.loads(prior.read_text())
    assert cert["all_passed"] and cert["original_artifacts_unchanged"]
    protected = [p for p in HERE.iterdir() if p.is_file() and
                 any(p.name.startswith(stem) for stem in PROGRAMS)]
    before = {p.name: digest(p) for p in protected}
    reused = {}
    for stem in dependencies():
        source, target = HERE / (stem + ".py"), REPLAY / (stem + ".py")
        if not target.exists():
            shutil.copy2(source, target)
        assert source.read_bytes() == target.read_bytes(), stem
        reused[source.name] = digest(source)
    for stem in PROGRAMS:
        target = REPLAY / (stem + ".py")
        assert not target.exists(), target
        shutil.copy2(HERE / target.name, target)
    rows = []
    begin = time.time()
    for stem in PROGRAMS:
        start = time.time()
        output = REPLAY / (stem + "_root_check.out")
        with output.open("x") as stream:
            run = subprocess.run([sys.executable, "-u", str(REPLAY / (stem + ".py"))],
                                 cwd=REPLAY, stdout=stream, stderr=subprocess.STDOUT)
        row = {"program": stem + ".py", "exit_code": run.returncode,
               "elapsed_seconds": round(time.time() - start, 3),
               "replay_output": str(output.relative_to(HERE)),
               "program_sha256": digest(REPLAY / (stem + ".py")),
               "output_sha256": digest(output)}
        rows.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode:
            break
    result = {"programs": rows,
              "all_passed": len(rows) == len(PROGRAMS)
                            and all(r["exit_code"] == 0 for r in rows),
              "original_artifacts_unchanged": all(
                  digest(HERE / name) == value for name, value in before.items()),
              "protected_sha256": before, "reused_dependency_sha256": reused,
              "elapsed_seconds": round(time.time() - begin, 3)}
    HERE.joinpath("audit_torsion_class_four_root.json").write_text(json.dumps(result, indent=2)+"\n")
    assert result["original_artifacts_unchanged"] and result["all_passed"]
    print("ROOT_ORDER_THREE_TORSION_AND_EXPONENT_FOUR_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
