#!/usr/bin/env python3
"""Run an archived GAP check in its original relative-path layout.

The research scripts use Read("work/centralizer_code/...") and related
paths. This runner reconstructs that layout in a temporary directory,
uses the recorded local GAP runtime or an installed GAP, and preserves
the transcript and generated certificates under notes/reproduced/.
"""
from pathlib import Path
import argparse
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("script", help="Archived GAP script basename")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    script = CODE / Path(args.script).name
    if not script.is_file() or script.suffix != ".g":
        parser.error("Choose a .g file present in code/.")
    runtime = ROOT.parent / ".gapruntime/root"
    binary = runtime / "usr/lib/x86_64-linux-gnu/gap/gap"
    env = os.environ.copy()
    if binary.is_file():
        libraries = str(runtime / "usr/lib/x86_64-linux-gnu")
        old = env.get("LD_LIBRARY_PATH", "")
        env["LD_LIBRARY_PATH"] = libraries + (":" + old if old else "")
        command = [str(binary), "-q", "-b", "-l",
                   str(runtime / "usr/share/gap")]
    else:
        installed = shutil.which("gap")
        if not installed:
            parser.error("Run python3 code/bootstrap_runtimes.py gap first, or install GAP.")
        command = [installed, "-q", "-b"]
    destination = (args.output_dir or ROOT / "notes/reproduced" / script.stem).resolve()
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="gt_tower_gap_") as temporary:
        staging = Path(temporary)
        staged_code = staging / "archived_code"
        shutil.copytree(CODE, staged_code)
        work = staging / "work"
        work.mkdir()
        for group in ("centralizer_code", "tower_code", "ghost_code"):
            (work / group).symlink_to(staged_code, target_is_directory=True)
        fragments = ROOT / "notes/source_fragments"
        for source in fragments.iterdir():
            if source.is_file():
                shutil.copy2(source, work / source.name)
        background = ROOT.parent / "background"
        if background.is_dir():
            (staging / "background").symlink_to(background, target_is_directory=True)
        before = {p.name: p.read_bytes() for p in staged_code.iterdir() if p.is_file()}
        transcript = destination / (script.stem + ".out")
        with transcript.open("wb") as output:
            result = subprocess.run(command + [str(staged_code / script.name)],
                                    cwd=staging, env=env, stdout=output,
                                    stderr=subprocess.STDOUT)
        changed = []
        for produced in staged_code.iterdir():
            if produced.is_file() and before.get(produced.name) != produced.read_bytes():
                shutil.copy2(produced, destination / produced.name)
                changed.append(produced.name)
        text = transcript.read_text(errors="replace")
        # GAP may enter a break loop and eventually exit with status zero.
        errors = [line for line in text.splitlines()
                  if line.startswith(("Error,", "Syntax error:"))]
        print("Transcript:", transcript)
        print("Changed or generated certificates:", changed)
        print("Process exit:", result.returncode, "; GAP errors:", len(errors))
        if result.returncode or errors:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
