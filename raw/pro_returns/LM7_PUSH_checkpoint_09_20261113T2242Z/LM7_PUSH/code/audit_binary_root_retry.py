#!/usr/bin/env python3
"""Retained retry after the first replay omitted its de_source input directory.

The first run stopped on FileNotFoundError before the lower-degree test ran.
Its code, stdout, result, and copied inputs remain unchanged.  This retry
adds the missing source inputs and writes separately named replay outputs.
"""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import time
from audit_binary_root import HERE, DEST, PROGRAMS, digest


def main():
    before = json.loads((DEST / "original_input_manifest.json").read_text())
    assert all(digest(HERE / name) == value for name, value in before.items())
    assert not (DEST / "de_source").exists()
    shutil.copytree(HERE / "de_source", DEST / "de_source")
    source_inputs = {str(p.relative_to(HERE)): digest(p)
                     for p in (HERE / "de_source").rglob("*") if p.is_file()}
    rows = []
    started = time.time()
    for stem in PROGRAMS:
        begin = time.time()
        output = DEST / (stem + "_root_retry.out")
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
    unchanged = all(digest(HERE / name) == value for name, value in before.items())
    unchanged &= all(digest(HERE / name) == value for name, value in source_inputs.items())
    result = {"programs": rows,
              "all_passed": len(rows) == len(PROGRAMS)
                            and all(r["exit_code"] == 0 for r in rows),
              "original_artifacts_unchanged": unchanged,
              "protected_artifact_sha256": before,
              "additional_source_input_sha256": source_inputs,
              "elapsed_seconds": round(time.time() - started, 3),
              "previous_attempt": "audit_binary_root.json: missing copied de_source input; retained"}
    HERE.joinpath("audit_binary_root_retry.json").write_text(
        json.dumps(result, indent=2) + "\n")
    assert unchanged, "An original artifact changed during replay"
    assert result["all_passed"], "An E.24 certificate failed"
    print("ROOT_BINARY_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
