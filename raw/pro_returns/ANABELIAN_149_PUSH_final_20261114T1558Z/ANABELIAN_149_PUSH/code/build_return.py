#!/usr/bin/env python3
"""Reproduce the stabilized LuaLaTeX/BibTeX manuscript build."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
BUILD.mkdir(exist_ok=True)
NAME = "ANABELIAN_149_PUSH_paper"
env = os.environ.copy()
latex_options = []
# This execution image keeps its initialized format outside the TeX search tree.
# An ordinary complete TeX Live installation uses its standard format instead.
local_format = ROOT.parent / "tmp/F_build/lualatex.fmt"
if local_format.exists():
    from F_prepare_lualatex import environment
    env = environment(local_format.parent)
    latex_options = ["--fmt=" + str(local_format)]

def latex(number):
    log = BUILD / f"lualatex-pass{number}.log"
    with log.open("w") as out:
        subprocess.run(["lualatex", *latex_options, "-interaction=nonstopmode", "-halt-on-error",
                        NAME + ".tex"], cwd=ROOT, env=env, stdout=out,
                       stderr=subprocess.STDOUT, check=True)

latex(1)
with (BUILD / "bibtex.log").open("w") as out:
    subprocess.run(["bibtex", NAME], cwd=ROOT, env=env, stdout=out,
                   stderr=subprocess.STDOUT, check=True)
for number in (2, 3, 4):
    latex(number)
shutil.copyfile(ROOT / (NAME + ".log"), BUILD / "lualatex-final.log")
log = (BUILD / "lualatex-final.log").read_text()
warnings = [line for line in log.splitlines() if "Warning" in line]
overflows = [float(x) for x in re.findall(
    r"Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)", log)]
result = {"pdf_sha256": hashlib.sha256((ROOT / (NAME + ".pdf")).read_bytes()).hexdigest(),
          "warnings": warnings, "overfull_boxes": overflows,
          "passes": 4, "bibtex_runs": 1}
(ROOT / "code/build_return_output.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
if warnings or any(x > 2 for x in overflows):
    raise SystemExit("Build requires a warning or overflow repair before delivery")
