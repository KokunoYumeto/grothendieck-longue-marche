#!/usr/bin/env python3
"""Compile individual transcription fragments for syntax, without editing them.

Uses the already installed local TeX tree. Its database-only lookup is replaced
by a process-local filesystem lookup; no package installation or network access
is performed. Generated formats, wrappers, logs and auxiliary files remain in
the scratch work directory, outside the deliverable folder. No combined
transcription is produced, and pdfTeX draft mode suppresses PDF output.

Editorial wrappers are deliberately transparent. In particular, ulem is not
available locally, so this checks source/TikZ syntax, not final underlining,
deletion appearance, page layout, or diplomatic accuracy.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import os
from pathlib import Path
import re
import subprocess


PREAMBLE = r"""\documentclass{article}
\usepackage{amsmath,amssymb,graphicx,tikz-cd}
\IfFileExists{mathrsfs.sty}{\usepackage{mathrsfs}}{}
\usetikzlibrary{arrows,arrows.meta,calc,decorations.markings,decorations.pathreplacing,patterns,positioning,quotes,shapes.geometric}
\setlength{\textwidth}{180mm}
\setlength{\textheight}{250mm}
\setlength{\oddsidemargin}{-10mm}
\setlength{\topmargin}{-20mm}
\long\def\cotefile#1{\par\noindent Cote #1\par}
\long\def\scanpage#1{\par\noindent Scan #1\par}
\long\def\mspage#1{\par\noindent #1\par}
% Do not pre-tokenize TikZ-CD ampersands by collecting wrapper arguments.
\let\deleted\relax
\let\inserted\relax
\let\margin\relax
\let\uline\relax
\let\uuline\relax
\let\unsure\relax
\long\def\illegible#1{\textnormal{[illegible: #1]}}
\def\diagram{\ifmmode\let\diagramend\relax\else\[\let\diagramend\]\fi
  \afterassignment\diagramstart\let\diagrambegin=}
\def\diagramstart{\bgroup\aftergroup\diagramend}
\let\figure\relax
\begin{document}
"""


def command(args: list[str], cwd: Path, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, env=env, text=True, capture_output=True,
                          errors="replace", timeout=120)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, required=True)
    parser.add_argument("--scans", type=int, nargs="+", help="recheck only these scan numbers")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--work", type=Path,
                        default=Path(__file__).resolve().parent.parent.parent / "latex_syntax_work")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    work = args.work.resolve()
    work.mkdir(exist_ok=True, parents=True)
    env = os.environ.copy()
    env.update({"TEXMF": "/usr/share/texlive/texmf-dist",
                "TEXMFDBS": "/usr/share/texlive/texmf-dist",
                "TEXMFVAR": str(work / "texmf-var"),
                "TEXFORMATS": str(work) + "//:"})
    if not (work / "pdflatex.fmt").is_file():
        made = command(["pdftex", "-ini", "-etex", "-jobname=pdflatex", "-progname=pdflatex",
                        "-interaction=nonstopmode", "pdflatex.ini"], work, env)
        (work / "format_generation_stdout.txt").write_text(made.stdout + made.stderr)
        if made.returncode:
            raise RuntimeError("Private format generation failed; see scratch format log")
    results: list[str] = [
        "Individual-page syntax compilation",
        "UTC: " + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "Local packages only; transparent editorial wrappers; no ulem; no page edits; no combined transcription.",
        "Draft-mode pdfTeX checks TeX/amsmath/TikZ processing but does not certify typography or manuscript readings.",
        "",
    ]
    successes: list[int] = []
    failures: list[int] = []
    for page in sorted((root / "pages").glob("MPL_136_328-376_136_scan*.tex")):
        match = re.fullmatch(r"MPL_136_328-376_136_scan(\d{3})\.tex", page.name)
        if not match or int(match.group(1)) > args.through:
            continue
        scan = int(match.group(1))
        if args.scans is not None and scan not in args.scans:
            continue
        page_work = work / f"scan{scan}"
        page_work.mkdir(exist_ok=True)
        wrapper = page_work / "syntax_wrapper.tex"
        wrapper.write_text(PREAMBLE + "\\input{" + str(page) + "}\n\\end{document}\n")
        run = command(["pdftex", "-fmt=pdflatex", "-progname=pdflatex", "-draftmode",
                       "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
                       "-file-line-error", str(wrapper)], page_work, env)
        output = run.stdout + run.stderr
        (page_work / "compiler_stdout.txt").write_text(output)
        if run.returncode == 0:
            successes.append(scan)
            results.append(f"PASS scan {scan}")
        else:
            failures.append(scan)
            results.append(f"FAIL scan {scan}; compiler exit {run.returncode}")
            lines = output.splitlines()
            starts = [i for i, line in enumerate(lines)
                      if re.search(r"\.tex:\d+:|^! |^!$|Error:|Emergency stop", line)]
            if starts:
                start = starts[0]
                results.extend(lines[max(0, start - 1):min(len(lines), start + 18)])
            else:
                results.extend(lines[-20:])
            results.append("")
        print(f"scan {scan}: {'PASS' if run.returncode == 0 else 'FAIL'}", flush=True)
    results.extend(["", f"Passed: {len(successes)}; failed: {len(failures)}.",
                    "Passed scans: " + ", ".join(map(str, successes)),
                    "Failed scans: " + ", ".join(map(str, failures))])
    report = args.report or root / "records" / f"compile_328-{args.through}.txt"
    report.write_text("\n".join(results) + "\n")
    print(str(report), flush=True)
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
