"""Replay the exact LM7 D.32/D.45 obstruction certificates in isolation.

This copies the supplied code and textual inputs to work/c_obstruction_replay
so that the supplied background is never modified.  It evaluates the literal
long words again, recomputes all relevant central and lower-centralizer columns,
and saves new stdout and JSON certificates under deliverable/code/c_*.
Earlier masks specify the recorded input actions; their construction is not
silently reclassified as a fresh search or a proof of other tower stages.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--part", choices=("d32", "d45", "all"), default="all")
parser.add_argument("--regenerate-inputs", action="store_true",
                    help="regenerate the JSON data omitted from the supplied attachment")
args = parser.parse_args()
root = Path(__file__).resolve().parents[2]
source = root / "background/LM7_return/code"
replay = root / "work/c_obstruction_replay"
output = root / "deliverable/code"
replay.mkdir(parents=True, exist_ok=True)
manifest = {}
for path in sorted(source.iterdir()):
    if path.is_file():
        shutil.copy2(path, replay / path.name)
        manifest[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
(output / "c_obstruction_input_hashes.json").write_text(json.dumps(manifest, indent=2) + "\n")

jobs = []
if args.regenerate_inputs:
    jobs += [("d_cm_quadratic_search", []), ("d_cm_rank4_joint", []),
             ("d_cm_rank4_degree7", []), ("d_cm_degree8_seed", [])]
    if args.part in ("d45", "all"):
        jobs += [("d_cm_degree8_common", []), ("d_cm_degree8_high", []),
                 ("d_cm_degree8_joint", []), ("d_cm_rank4_structure", []),
                 ("d_cm_solvable_even_boundary", ["--source-code", str(replay)]),
                 ("d_cm_fermat_joint_base", [])]
        # This is part of the definition of the recorded D.39 action.  Its
        # derivation in the larger homology tower is not asserted as rerun.
        gauge_text = (source / "d_cm_fermat_homology_seed.out").read_text()
        gauge = int(re.search(r'"finite_gauge_exponent"\s*:\s*(-?\d+)', gauge_text).group(1))
        assert gauge == -438
        (replay / "d_cm_fermat_homology_seed.json").write_text(
            json.dumps({"summary": {"finite_gauge_exponent": gauge},
                        "scope": "Recorded input gauge, read from the supplied .out; not a rerun of its upstream homology search."}) + "\n")
if args.part in ("d45", "all"):
    jobs += [
        ("d_cm_rank2_boundary_test", ["--source-code", str(replay)]),
        ("d_cm_rank2_degree9", []),
        ("d_cm_rank2_centralizers", []),
        ("d_cm_rank2_multiplier_transport", ["--rank2-code", str(replay)]),
    ]
if args.part in ("d32", "all"):
    if not args.regenerate_inputs:
        jobs += [("d_cm_degree8_seed", [])]
    jobs += [("d_cm_degree8_centralizer", [])]
summaries = {}
started = time.monotonic()
for name, arguments in jobs:
    print("Recomputing", name, flush=True)
    log = output / ("c_replay_" + name + ".out")
    with log.open("w") as stream:
        process = subprocess.run(
            [sys.executable, str(replay / (name + ".py")), *arguments],
            cwd=replay, stdout=stream, stderr=subprocess.STDOUT, check=False,
        )
    if process.returncode:
        raise RuntimeError(f"{name} failed; see {log}")
    certificate = json.loads((replay / (name + ".json")).read_text())
    summaries[name] = certificate.get("summary", certificate)
    shutil.copy2(replay / (name + ".json"), output / ("c_replay_" + name + ".json"))
    print("Passed", name, flush=True)

if args.part in ("d45", "all"):
    rank2 = summaries["d_cm_rank2_centralizers"]["results"]
    assert rank2[0]["graph"] == "sphere"
    assert rank2[0]["full_same_action_correction_rank"] == 47
    assert not rank2[0]["same_lower_action_has_a_degree9_lift"]
    assert rank2[0]["annihilator_checked_on_all_central_and_centralizer_columns"]
    assert rank2[1]["same_lower_action_has_a_degree9_lift"]
if args.part in ("d32", "all"):
    rank4 = summaries["d_cm_degree8_centralizer"]
    assert rank4["rank_after_all_lower_s_centralizer_defects"] == 7777
    assert not rank4["recorded_T2_action_has_torsion_conjugate_peripheral_lift_to_T3"]
    assert rank4["annihilating_functional_verified"]
    # The centralizer program recomputes this as a dependency.
    shutil.copy2(replay / "d_cm_degree8_linear.json", output / "c_replay_d_cm_degree8_linear.json")

record = {"part": args.part, "elapsed_seconds": round(time.monotonic() - started, 3),
          "recomputed": list(summaries), "summaries": summaries,
          "scope": "Literal recorded actions and their complete same-action peripheral central-layer obstructions; earlier construction masks remain the specified inputs."}
(output / ("c_obstruction_replay_" + args.part + ".json")).write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({key: record[key] for key in ("part", "elapsed_seconds", "recomputed", "scope")}, indent=2), flush=True)
