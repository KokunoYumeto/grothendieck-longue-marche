"""Syntax check with a scratch XeLaTeX format and neutral state macros."""
from pathlib import Path
from datetime import datetime, timezone
import os
import subprocess
import sys

root = Path(__file__).resolve().parent
qa = root.parent / "qa"
env = os.environ.copy()
env.update(TEXMFCNF="/usr/share/texlive/texmf-dist/web2c", TEXMF="{/usr/share/texmf,/usr/share/texlive/texmf-dist}")
cmd = ["xelatex", "-no-pdf", f"-fmt={qa / 'xelatex.fmt'}", "-interaction=nonstopmode", "-halt-on-error", f"-output-directory={qa}", str(qa / "validation.tex")]
run = subprocess.run(cmd, cwd=root.parent, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
(qa / "compile.stdout").write_text(run.stdout)
tail = "\n".join(run.stdout.splitlines()[-18:])
with (root / "compile_check.log").open("a") as f:
    f.write(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC") + f" exit={run.returncode}\n" + tail + "\n\n")
print(tail)
sys.exit(run.returncode)
