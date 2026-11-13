#!/usr/bin/env python3
"""Replay the actual word preimages and complete ternary fibre lattices."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
REPLAY = HERE / "root_e24_binary_replay"
STEM = "bc_cm_fermat_kernel_words"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    protected = [HERE / (STEM + extension) for extension in (".py", ".out", ".json")]
    before = {p.name: digest(p) for p in protected}
    for filename in ("de_fermat_schreier.py", "de_ferrari_degree6_lift.py"):
        assert (HERE / filename).read_bytes() == (REPLAY / filename).read_bytes()
    target = REPLAY / (STEM + ".py")
    assert not target.exists()
    shutil.copy2(HERE / target.name, target)
    output = REPLAY / (STEM + "_root_check.out")
    begin = time.time()
    with output.open("x") as stream:
        run = subprocess.run([sys.executable, "-u", str(target)], cwd=REPLAY,
                             stdout=stream, stderr=subprocess.STDOUT)
    result = {"exit_code": run.returncode,
              "elapsed_seconds": round(time.time() - begin, 3),
              "original_artifacts_unchanged": all(
                  digest(HERE / name) == value for name, value in before.items()),
              "protected_sha256": before,
              "certificate_byte_identical": (HERE / (STEM + ".json")).read_bytes()
                                            == (REPLAY / (STEM + ".json")).read_bytes(),
              "replay_output": str(output.relative_to(HERE)),
              "replay_output_sha256": digest(output)}
    HERE.joinpath("audit_boundary_words_root.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2), flush=True)
    assert run.returncode == 0 and result["original_artifacts_unchanged"]
    assert result["certificate_byte_identical"]
    print("ROOT_COMPLETE_BOUNDARY_WORDS_AUDIT_PASS", flush=True)


if __name__ == "__main__":
    main()
