#!/usr/bin/env python3
"""Root replay of the coupled perfect-kernel and pro-five certificate in D.27."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPLAY = HERE / "root_e24_binary_replay"
PROGRAMS = ("a_peripheral_coupled",)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    protected = [p for p in HERE.iterdir() if p.is_file()
                 and any(p.stem == s for s in PROGRAMS)]
    protected += [HERE / "a_peripheral_cycle.py", HERE / "a_peripheral_cycle_a8.json"]
    before = {p.name: digest(p) for p in protected}
    for name in ("a_peripheral_cycle.py", "a_peripheral_cycle_a8.json"):
        assert not (REPLAY / name).exists()
        shutil.copy2(HERE / name, REPLAY / name)
    for stem in PROGRAMS:
        assert not (REPLAY / (stem+".py")).exists()
        shutil.copy2(HERE / (stem+".py"), REPLAY / (stem+".py"))
    rows = []
    started = time.time()
    for stem in PROGRAMS:
        begin = time.time()
        output = REPLAY / (stem+"_root_check.out")
        with output.open("x") as stream:
            run = subprocess.run([sys.executable, "-u", str(REPLAY / (stem+".py"))],
                                 cwd=REPLAY, stdout=stream, stderr=subprocess.STDOUT)
        row = {"program": stem+".py", "output": str(output.relative_to(HERE)),
               "exit_code": run.returncode,
               "elapsed_seconds": round(time.time()-begin, 3),
               "program_sha256": digest(REPLAY / (stem+".py")),
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
              "elapsed_seconds": round(time.time()-started, 3)}
    HERE.joinpath("audit_coupled_root.json").write_text(json.dumps(result, indent=2)+"\n")
    assert unchanged and result["all_passed"]
    print("ROOT_COUPLED_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
