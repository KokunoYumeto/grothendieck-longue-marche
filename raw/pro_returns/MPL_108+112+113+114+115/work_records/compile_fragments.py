#!/usr/bin/env python3
"""Build a local LaTeX syntax harness and compile page fragments read-only.

This is a syntax check, not a manuscript or typographic accuracy review. The
environment lacks ulem, so its underlining macros use a documented identity
fallback. No transcription source is copied, modified, or normalized.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import re
import subprocess

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
WORK = BASE / "latex_check"

def tex_environment():
    env = os.environ.copy()
    dist = "/usr/share/texlive/texmf-dist"
    other = "/usr/share/texmf"
    env.update({
        "TEXINPUTS": f".:{dist}/tex/latex/base//:{dist}/tex//:{other}/tex//:",
        "TFMFONTS": f"{dist}/fonts/tfm//:{other}/fonts/tfm//:",
        "TEXFORMATS": str(WORK) + "//:",
        "TEXMFVAR": str(WORK / "texmf-var"),
        "TEXMFCONFIG": str(WORK / "texmf-config"),
        "TEXMFCACHE": str(WORK / "texmf-var"),
        "TEXFONTMAPS": f"{dist}/fonts/map//:{other}/fonts/map//:",
        "T1FONTS": f"{dist}/fonts/type1//:{other}/fonts/type1//:",
        "VFFONTS": f"{dist}/fonts/vf//:{other}/fonts/vf//:",
        "ENCFONTS": f"{dist}/fonts/enc//:{other}/fonts/enc//:",
        "MFINPUTS": f"{dist}/metafont//:{dist}/fonts/source//:{other}/fonts/source//:",
    })
    return env

def ensure_format():
    WORK.mkdir(exist_ok=True)
    for name in ("texmf-var", "texmf-config", "compiled"):
        (WORK / name).mkdir(exist_ok=True)
    if (WORK / "pdflatex.fmt").is_file():
        return
    run = subprocess.run(["pdflatex", "-ini", "-etex", "-interaction=nonstopmode",
                          "-halt-on-error", "-jobname=pdflatex", "-progname=pdflatex",
                          "pdflatex.ini"], cwd=WORK, env=tex_environment(),
                         capture_output=True, text=True, timeout=60)
    (WORK / "format_build_output.txt").write_text(run.stdout + "\n" + run.stderr)
    if run.returncode:
        raise RuntimeError("local LaTeX format build failed; see format_build_output.txt")

def compile_one(source: Path | None):
    label = source.stem if source else "smoke"
    target = WORK / "compiled" / label
    target.mkdir(exist_ok=True)
    harness = target / "harness.tex"
    body = ("Test $A\\to B$.\\begin{tikzcd}A\\arrow[r]&B\\end{tikzcd}"
            if source is None else "\\input{" + str(source) + "}")
    harness.write_text("\\input{" + str(WORK / "harness_preamble.tex") + "}\n"
                       "\\begin{document}\n" + body + "\n\\end{document}\n")
    run = subprocess.run(["pdflatex", "-draftmode", "-interaction=nonstopmode",
                          "-file-line-error", "-halt-on-error", "harness.tex"],
                         cwd=target, env=tex_environment(),
                         capture_output=True, text=True, timeout=60)
    output = run.stdout + "\n" + run.stderr
    (target / "compiler_output.txt").write_text(output)
    errors = []
    lines = output.splitlines()
    for i,line in enumerate(lines):
        if (re.search(r"\.tex:\d+:|^!|LaTeX Error:|Package .* Error:|Undefined control sequence", line)
                or "Fatal error occurred" in line):
            errors.append("\n".join(lines[i:i+3]))
    if run.returncode and not errors:
        errors = lines[-12:]
    return {"source": str(source.relative_to(ROOT)) if source else "smoke",
            "ok": run.returncode == 0, "returncode": run.returncode,
            "errors": errors, "log": str((target / "harness.log").relative_to(ROOT))}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page", action="append", type=Path,
                        help="one or more root-relative page files; default: all forty")
    parser.add_argument("--jobs", type=int, default=4)
    args = parser.parse_args()
    ensure_format()
    smoke = compile_one(None)
    if not smoke["ok"]:
        print(json.dumps({"environment_error":smoke},indent=2))
        return 2
    sources = ([p if p.is_absolute() else ROOT/p for p in args.page]
               if args.page else sorted((ROOT/"pages").glob("*.tex")))
    with ThreadPoolExecutor(max_workers=max(1,min(8,args.jobs))) as pool:
        results = list(pool.map(compile_one,sources))
    report = {"scope":"Compilation syntax only; not manuscript or typography review.",
              "engine":"pdflatex (locally built format, explicit package search paths)",
              "ulem":"not installed; identity fallback in harness only",
              "passed":sum(r["ok"] for r in results),"total":len(results),
              "results":results}
    (BASE/"latex_compile_report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({key:value for key,value in report.items() if key!="results"},indent=2))
    for row in results:
        if not row["ok"]:
            print(json.dumps(row,indent=2,ensure_ascii=False))
    return 0 if report["passed"]==report["total"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
