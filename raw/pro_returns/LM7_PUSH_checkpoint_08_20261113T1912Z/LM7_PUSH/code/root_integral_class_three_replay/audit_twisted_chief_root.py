#!/usr/bin/env python3
"""Independent protected replay of the D.30 class algebra and exact maps."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPLAY = HERE / "root_d30_replay"
PROGRAMS = ("a_peripheral_s5_twist", "a_peripheral_s5_maps")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    REPLAY.mkdir(exist_ok=False)
    protected = [p for p in HERE.iterdir() if p.is_file() and
                 (p.name.startswith("a_peripheral_s5_") or
                  p.name == "a_peripheral_count.py")]
    before = {p.name: digest(p) for p in protected}
    for name in (*PROGRAMS, "a_peripheral_count"):
        shutil.copy2(HERE / (name + ".py"), REPLAY / (name + ".py"))
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
               "json_byte_identical": (HERE / (stem + ".json")).read_bytes() ==
                                      (REPLAY / (stem + ".json")).read_bytes(),
               "stdout_byte_identical": (HERE / (stem + ".out")).read_bytes() ==
                                        output.read_bytes(),
               "replay_json_sha256": digest(REPLAY / (stem + ".json")),
               "replay_output_sha256": digest(output)}
        rows.append(row)
        print(json.dumps(row), flush=True)
        if run.returncode:
            break
    result = {"programs": rows,
              "all_passed": len(rows) == len(PROGRAMS) and all(
                  r["exit_code"] == 0 and r["json_byte_identical"] for r in rows),
              "original_artifacts_unchanged": all(
                  digest(HERE / name) == value for name, value in before.items()),
              "protected_sha256": before,
              "elapsed_seconds": round(time.time() - begin, 3)}
    HERE.joinpath("audit_twisted_chief_root.json").write_text(json.dumps(result, indent=2)+"\n")
    assert result["original_artifacts_unchanged"] and result["all_passed"]
    print("ROOT_TWISTED_A5_CHIEF_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
