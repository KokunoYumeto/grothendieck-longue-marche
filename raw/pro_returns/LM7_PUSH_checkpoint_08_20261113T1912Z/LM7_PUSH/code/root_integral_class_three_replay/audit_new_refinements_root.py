#!/usr/bin/env python3
"""Replay the odd-base chief theorem, class-two boundary, and A5 Ferrari.

New programs execute sequentially in the existing isolated root directory.
Every reused Python dependency is checked against its current original.
Original code, outputs and certificates are hash-protected throughout.
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
    "a_peripheral_a5_invariance",
    "bc_fermat_class_two",
    "bc_fermat_class_two_kernel",
    "bc_fermat_class_two_fibres",
    "bc_fermat_class_two_obstruction",
    "bc_fermat_class_two_integral_kernel",
    "de_ferrari_a5_model",
    "de_ferrari_a5_components",
    "de_ferrari_a5_source",
    "de_ferrari_a5_source_compress",
    "de_ferrari_a5_corrections",
    "de_ferrari_a5_compare",
    "de_ferrari_a5_solvable",
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
    protected = [p for p in HERE.iterdir() if p.is_file() and
                 (p.stem in PROGRAMS or p.name.startswith("de_ferrari_a5_")
                  or p.name.startswith("a_peripheral_a5_invariance"))]
    before = {p.name: digest(p) for p in protected}
    reused = {}
    for stem in dependencies() + ["a_peripheral_count"]:
        source, target = HERE / (stem + ".py"), REPLAY / (stem + ".py")
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
    HERE.joinpath("audit_new_refinements_root.json").write_text(json.dumps(result, indent=2)+"\n")
    assert result["original_artifacts_unchanged"] and result["all_passed"]
    print("ROOT_ODD_CHIEF_CLASS_TWO_AND_A5_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
