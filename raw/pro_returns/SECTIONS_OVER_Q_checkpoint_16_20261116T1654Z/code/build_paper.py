#!/usr/bin/env python3
"""Rebuild the manuscript with LuaLaTeX and record its actual diagnostics.

Run from any directory. A normal TeX Live installation needs no configuration.
The optional ../runtime directory is a session-local TeX runtime; it is not a
mathematical input and is not required on a complete TeX Live installation.
"""
from pathlib import Path
import json
import os
import re
import subprocess
import sys

WORK = Path(__file__).resolve().parents[1]
BASE = "SECTIONS_OVER_Q_paper"
env = os.environ.copy()
runtime = WORK.parent / "runtime"
if (runtime / "texmf").exists():
    env["TEXMFHOME"] = str(runtime / "texmf")
    env["TEXMFCACHE"] = str(runtime / "cache")
    env["TEXMFVAR"] = str(runtime / "cache")
    env["TEXFORMATS"] = str(runtime / "agent_builds") + os.pathsep

commands = [
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", BASE + ".tex"],
    ["bibtex", BASE],
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", BASE + ".tex"],
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", BASE + ".tex"],
]
if "--one-pass" in sys.argv:
    commands = commands[:1]
outpath = WORK / "code" / "build_paper_output.txt"
with outpath.open("w") as out:
    for command in commands:
        proc = subprocess.run(command, cwd=WORK, env=env, text=True, capture_output=True)
        out.write("COMMAND: " + " ".join(command) + "\n")
        out.write(proc.stdout)
        out.write(proc.stderr)
        out.flush()
        if proc.returncode:
            print(proc.stdout[-6500:])
            raise SystemExit(f"Build failed ({proc.returncode}); see {outpath}")
    log = (WORK / (BASE + ".log")).read_text()
    overfull = [float(x) for x in re.findall(r"Overfull \\hbox \(([0-9.]+)pt too wide\)", log)]
    v_overfull = [float(x) for x in re.findall(r"Overfull \\vbox \(([0-9.]+)pt too high\)", log)]
    result = {
        "engine": "LuaLaTeX",
        "overfull_hboxes": len(overfull),
        "overfull_hboxes_above_2pt": sum(x > 2 for x in overfull),
        "maximum_hbox_pt": max(overfull, default=0),
        "overfull_vboxes": len(v_overfull),
        "overfull_vboxes_above_2pt": sum(x > 2 for x in v_overfull),
        "maximum_vbox_pt": max(v_overfull, default=0),
        "undefined_references": "There were undefined references" in log,
        "undefined_citations": "Citation" in log and "undefined" in log,
    }
    out.write(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    (WORK / "notes" / "typesetting_current.json").write_text(json.dumps(result, indent=2) + "\n")
