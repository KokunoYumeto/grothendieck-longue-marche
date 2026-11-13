#!/usr/bin/env python3
"""Fresh isolated replay of the unchanged initial wrapper; no recovered output."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
ap=argparse.ArgumentParser()
ap.add_argument("--gp",required=True)
args=ap.parse_args()
gp=Path(args.gp).resolve()
source=HERE/"e106_initial_prime_driver.py"
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
with tempfile.TemporaryDirectory(prefix="e106_history_replay_") as td:
    stage=Path(td)
    target=stage/"research_e106"
    (target/"code").mkdir(parents=True)
    (target/"inputs").mkdir()
    for path in (ROOT/"inputs").glob("*.bin"):
        shutil.copyfile(path,target/"inputs"/path.name)
    shutil.copyfile(ROOT/"code/e_next_prime_maps.gp",
                    target/"code/e_next_prime_maps.gp")
    executable=stage/"research_e52/vendor/pari-2.19.0/gp"
    executable.parent.mkdir(parents=True)
    executable.symlink_to(gp)
    copied=stage/source.name
    shutil.copyfile(source,copied)
    assert sha(copied)==sha(source)
    proc=subprocess.run(["python",str(copied)],cwd=stage,
                        stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                        text=True)
    (HERE/"e106_initial_prime_driver.out").write_text(proc.stdout)
    arithmetic=target/"code/e_next_prime_maps.out"
    stream=arithmetic.read_text()
    (HERE/"e106_initial_prime_driver_replay_arithmetic.out").write_text(stream)
    assert proc.returncode==0 and proc.stdout.startswith("0 ")
    assert '"type":"completion","status":"PASS"' in stream
    assert "***   at top-level" not in stream and "***   user error" not in stream
    original=HERE/"e106_initial_prime_driver_arithmetic.out"
    assert stream==original.read_text()
    record={
      "status":"PASS",
      "provenance":"Fresh isolated replay of the unchanged wrapper; not recovered original stdout.",
      "wrapper_sha256":sha(source),
      "wrapper_exit_code":proc.returncode,
      "complete_wrapper_stdout":"e106_initial_prime_driver.out",
      "complete_GP_arithmetic_stdout":"e106_initial_prime_driver_replay_arithmetic.out",
      "arithmetic_stream_equals_previously_retained":True,
      "wrapper_stdout_sha256":sha(HERE/"e106_initial_prime_driver.out"),
      "arithmetic_stdout_sha256":sha(HERE/"e106_initial_prime_driver_replay_arithmetic.out")
    }
    (HERE/"e106_history_replay.json").write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps(record,indent=2))
