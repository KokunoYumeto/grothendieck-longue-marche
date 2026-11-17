#!/usr/bin/env python3
"""Invoke XeLaTeX using only this task's private TeX search configuration."""
import json
import os
import subprocess
import sys
from pathlib import Path

runtime = Path(__file__).resolve().parent / "tex_runtime"
environment = os.environ.copy()
environment.update(json.loads((runtime / "environment.json").read_text()))
command = ["xelatex", "-fmt=" + str(runtime / "xelatex.fmt"),
           "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
           *sys.argv[1:]]
raise SystemExit(subprocess.call(command, env=environment))
