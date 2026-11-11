#!/usr/bin/env python3
"""Build the self-contained paper with LuaLaTeX; keep temporary files separate.

On a normal TeX Live installation this runs LuaLaTeX directly.  The supplied
execution environment has the TeX source/font trees but omits format files,
filename databases, and LuaOTFload.  In that environment only, this script builds
a local format using the document's Type 1 Latin Modern fonts.  Its local copy
of the kernel disables only the unavailable OpenType startup loader.  The
document itself is an ordinary, portable LuaLaTeX source.
"""
from pathlib import Path
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ID = "LM3b_TEICHMULLER_PUSH"
BUILD = ROOT / "_build"
BUILD.mkdir(exist_ok=True)
env = os.environ.copy()

def lookup(name):
    return subprocess.run(["kpsewhich",name],env=env,text=True,
                          capture_output=True,check=False).stdout.strip()

fallback = not lookup("article.cls")
if fallback:
    env["TEXMF"]="{"+str(BUILD)+",/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}"
    env["TEXMFVAR"]=str(BUILD/"var")
    env["TEXMFCONFIG"]=str(BUILD/"config")
    env["TEXMFCACHE"]=str(BUILD/"cache")
    env["TEXFORMATS"]=str(BUILD)+":"
    fmt=BUILD/"lualatex.fmt"
    if not fmt.exists():
        kernel=Path(lookup("latex.ltx")).read_text()
        if not lookup("luaotfload-main.lua"):
            start=kernel.index(r"\everyjob\expandafter{%",kernel.index('require("ltluatex")'))
            end=kernel.index("\n\\fi",start)
            kernel=kernel[:start]+(
                "\\everyjob\\expandafter{\\the\\everyjob\n"
                "\\def\\encodingdefault{OT1}\\let\\f@encoding\\encodingdefault}\n"
            )+kernel[end:]
        (BUILD/"lm3b-latex.ltx").write_text(kernel)
        ini=Path(lookup("lualatex.ini")).read_text()
        ini=ini.replace(r"\input latex.ltx",r"\input lm3b-latex.ltx")
        (BUILD/"lm3b-lualatex.ini").write_text(ini)
        with (BUILD/"format_build.out").open("w") as out:
            subprocess.run([
                "luahbtex","--ini","--jobname=lualatex","--progname=lualatex",
                "-interaction=nonstopmode","-halt-on-error",
                "lm3b-lualatex.ini"],cwd=BUILD,env=env,stdout=out,
                stderr=subprocess.STDOUT,check=True)

for n in range(1,4):
    with (BUILD/f"pass_{n}.out").open("w") as out:
        process=subprocess.run([
            "lualatex","-interaction=nonstopmode","-halt-on-error",
            "-file-line-error","-output-directory="+str(BUILD),
            ID+"_paper.tex"],cwd=ROOT,env=env,stdout=out,
            stderr=subprocess.STDOUT,check=False)
    if process.returncode:
        lines=(BUILD/f"pass_{n}.out").read_text(errors="replace").splitlines()
        print("\n".join(lines[-55:]))
        sys.exit(process.returncode)
    print("LuaLaTeX pass",n,"completed",flush=True)
    log=(BUILD/(ID+"_paper.log")).read_text(errors="replace")
    if n>=2 and not re.search(r"Rerun|rerun|changed",log):
        break
shutil.copyfile(BUILD/(ID+"_paper.pdf"),ROOT/(ID+"_paper.pdf"))
warnings=[x for x in log.splitlines()
          if re.search(r"Overfull|Missing character|Warning:|undefined",x)]
result={
    "engine":"LuaHBTeX / LuaLaTeX",
    "local_type1_format_fallback":fallback,
    "passes":n,
    "pdf_bytes":(ROOT/(ID+"_paper.pdf")).stat().st_size,
    "warnings":warnings,
}
(ROOT/"audit"/"build_summary.json").write_text(json.dumps(result,indent=2))
shutil.copyfile(BUILD/(ID+"_paper.log"),ROOT/"audit"/"lualatex.log")
print(json.dumps(result,indent=2))
