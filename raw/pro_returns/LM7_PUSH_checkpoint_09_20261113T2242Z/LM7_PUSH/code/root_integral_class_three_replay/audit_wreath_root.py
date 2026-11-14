#!/usr/bin/env python3
"""Independent replay of the complete A5 wreath-lifting constants."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPLAY = HERE / "root_e24_binary_replay"
STEM = "a_peripheral_a5_wreath"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    original = [HERE / (STEM + extension) for extension in (".py", ".out", ".json")]
    before = {p.name: digest(p) for p in original}
    dependency = "a_peripheral_count.py"
    if not (REPLAY / dependency).exists():
        shutil.copy2(HERE / dependency, REPLAY / dependency)
    assert (REPLAY / dependency).read_bytes() == (HERE / dependency).read_bytes()
    target = REPLAY / (STEM + ".py")
    assert not target.exists()
    shutil.copy2(HERE / target.name, target)
    output = REPLAY / (STEM + "_root_check.out")
    start = time.time()
    with output.open("x") as stream:
        run = subprocess.run([sys.executable, "-u", str(target)], cwd=REPLAY,
                             stdout=stream, stderr=subprocess.STDOUT)
    result = {"exit_code": run.returncode,
              "elapsed_seconds": round(time.time() - start, 3),
              "original_artifacts_unchanged": all(
                  digest(HERE / name) == value for name, value in before.items()),
              "protected_sha256": before,
              "certificate_byte_identical": (REPLAY / (STEM + ".json")).read_bytes()
                                            == (HERE / (STEM + ".json")).read_bytes(),
              "replay_output": str(output.relative_to(HERE)),
              "replay_output_sha256": digest(output)}
    HERE.joinpath("audit_wreath_root.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2), flush=True)
    assert run.returncode == 0 and result["original_artifacts_unchanged"]
    assert result["certificate_byte_identical"]
    print("ROOT_A5_WREATH_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
