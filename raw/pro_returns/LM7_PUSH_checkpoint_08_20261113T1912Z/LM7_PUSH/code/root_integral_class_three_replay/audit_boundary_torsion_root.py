#!/usr/bin/env python3
"""Independent replay of literal boundary fibres and the torsion test.

All mutations occur in the retained root replay directory.  The seven
new programs are copied once; their original code and certificates are
hashed before and after the replay.  Earlier audited dependencies are
checked byte for byte before they are reused.
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
    "de_ferrari_two_family_words",
    "bc_cm_fermat_odd_boundary",
    "bc_twoadic_ferrari_comparison",
    "bc_cm_fermat_kernel_boundary",
    "de_ferrari_two_conjugacy",
    "de_ferrari_two_torsion",
    "de_ferrari_two_torsion_words",
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dependencies():
    found, pending = set(), list(PROGRAMS)
    while pending:
        name = pending.pop()
        path = HERE / (name + ".py")
        if name in found or not path.exists():
            continue
        found.add(name)
        for node in ast.walk(ast.parse(path.read_text())):
            modules = []
            if isinstance(node, ast.Import):
                modules = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules = [node.module]
            pending.extend(m for m in modules if (HERE / (m + ".py")).exists())
    return sorted(found - set(PROGRAMS))


def main():
    protected = [p for p in HERE.iterdir() if p.is_file()
                 and any(p.stem == s or p.stem.startswith(s + "_")
                         for s in PROGRAMS)]
    before = {p.name: digest(p) for p in protected}
    reused = {}
    for stem in dependencies():
        source, target = HERE / (stem + ".py"), REPLAY / (stem + ".py")
        assert source.read_bytes() == target.read_bytes(), stem
        reused[source.name] = digest(source)
    for stem in PROGRAMS:
        target = REPLAY / (stem + ".py")
        assert not target.exists(), target
        shutil.copy2(HERE / (stem + ".py"), target)
    rows = []
    started = time.time()
    for stem in PROGRAMS:
        begin = time.time()
        output = REPLAY / (stem + "_root_check.out")
        with output.open("x") as stream:
            run = subprocess.run(
                [sys.executable, "-u", str(REPLAY / (stem + ".py"))],
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
              "reused_dependency_sha256": reused,
              "elapsed_seconds": round(time.time() - started, 3)}
    HERE.joinpath("audit_boundary_torsion_root.json").write_text(
        json.dumps(result, indent=2) + "\n")
    assert unchanged and result["all_passed"]
    print("ROOT_BOUNDARY_TORSION_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
