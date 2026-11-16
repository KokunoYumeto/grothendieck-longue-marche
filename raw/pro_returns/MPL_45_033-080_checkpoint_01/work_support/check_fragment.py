#!/usr/bin/env python3
"""Compile one TeX body fragment for syntax only; never edit its contents.

Uses a local XeLaTeX format and bypasses the missing system filename database.
Annotation macros are identity wrappers, so this is not a visual edition proof.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage{amsmath,amssymb}
\usepackage{tikz-cd}
\usepackage[margin=20mm]{geometry}
\pagestyle{empty}
\long\def\cotefile#1{}
\long\def\scanpage#1{}
\long\def\mspage#1{}
\long\def\deleted#1{#1}
\long\def\inserted#1{#1}
\long\def\margin#1{#1}
\long\def\uline#1{#1}
\long\def\uuline#1{#1}
% Do not collect diagram bodies as arguments: tikz-cd changes & catcodes.
\let\diagram\relax
\let\figure\relax
\long\def\unsure#1{#1}
\long\def\illegible#1{#1}
\begin{document}
"""

def run(command, cwd, env, logfile):
    result = subprocess.run(command, cwd=cwd, env=env, capture_output=True, text=True)
    output = result.stdout + "\n" + result.stderr
    logfile.write_text(output, encoding="utf-8")
    return result, output

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fragment", type=Path)
    parser.add_argument("--work-dir", type=Path, default=Path(__file__).resolve().parent / "texqa")
    args = parser.parse_args()
    source = args.fragment.resolve()
    if not source.is_file():
        parser.error("fragment must name an existing regular file")
    if any(c in str(source) for c in "{}\n\r"):
        parser.error("fragment path must not contain braces or line breaks")
    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ,
               TEXMF="{/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}",
               TEXMFVAR=str(work), TEXMFCONFIG=str(work), TEXMFOUTPUT=str(work))
    format_path = work / "xelatex.fmt"
    if not format_path.is_file():
        result, output = run(
            ["xetex", "-ini", "-etex", "-interaction=nonstopmode", "-halt-on-error",
             "-jobname=xelatex", "-progname=xelatex", "xelatex.ini"],
            work, env, work / "format-build.txt")
        if result.returncode:
            print(output[-12000:])
            return result.returncode
    env["TEXFORMATS"] = str(work) + "//:"
    jobname = source.stem + "_syntax"
    wrapper = work / (jobname + ".tex")
    if wrapper == source:
        parser.error("source and generated wrapper must have different paths")
    wrapper.write_text(
        PREAMBLE + "\\input{\\detokenize{" + str(source) + "}}\n\\end{document}\n",
        encoding="utf-8")
    result, output = run(
        ["xetex", "-fmt=" + str(format_path), "-progname=xelatex", "-no-shell-escape",
         "-no-pdf", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
         "-jobname=" + jobname, str(wrapper)],
        work, env, work / (jobname + ".stdout.txt"))
    print(json.dumps({"fragment": str(source), "exit_code": result.returncode,
                      "log": str(work / (jobname + ".log")),
                      "stdout": str(work / (jobname + ".stdout.txt")),
                      "mode": "syntax_only_identity_annotations"}))
    if result.returncode:
        print(output[-12000:])
    return result.returncode

if __name__ == "__main__":
    raise SystemExit(main())

