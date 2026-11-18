#!/usr/bin/env python3
"""Compile one transcription fragment without editing it.

Usage:
    python work/compile_check.py
    python work/compile_check.py pages/MPL_29_049-094_29_scan049.tex

Requires xelatex, amsmath, amssymb, mathrsfs and tikz-cd. If the engine's
format is absent, it is initialized in the temporary output directory. This temporary
wrapper is a syntax check, not part of the diplomatic transcription. It colors
deletions instead of striking them so arbitrary nested content compiles safely.
The output and full log are retained only when --output-dir is supplied.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=18mm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,mathtools,mathrsfs}
\usepackage{xcolor}
\usepackage{tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,decorations.pathreplacing,positioning,calc,matrix}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\DeclareRobustCommand{\cotefile}[1]{\par\bigskip\textbf{Cote #1}\par}
\DeclareRobustCommand{\scanpage}[1]{\par\bigskip\textbf{Scan #1}\par}
\DeclareRobustCommand{\mspage}[1]{\par\textit{Manuscript page #1}\par}
\makeatletter
\newcommand{\mpl@colored}[1]{\@ifnextchar\bgroup{\bgroup\color{#1}\let\mplDiscard=}{\mpl@coloredsingle{#1}}}
\newcommand{\mpl@coloredsingle}[2]{{\color{#1}#2}}
\DeclareRobustCommand{\deleted}{\mpl@colored{gray}}
\DeclareRobustCommand{\inserted}{\mpl@colored{blue!65!black}}
\DeclareRobustCommand{\uline}[1]{\underline{#1}}
\DeclareRobustCommand{\uuline}[1]{\underline{\underline{#1}}}
\DeclareRobustCommand{\margin}{\par\bgroup\small\aftergroup\par\let\mplDiscard=}
\DeclareRobustCommand{\unsure}{\mpl@colored{orange!65!black}}
\makeatother
\DeclareRobustCommand{\illegible}[1]{\ifmmode\text{[illegible: #1]}\else[illegible: #1]\fi}
% Do not collect the body as an argument: tikz-cd needs to set the catcode of
% matrix separators before its body is tokenized. Consume only the opening
% brace, using a simple group which the caller's closing brace will close.
\DeclareRobustCommand{\diagram}{\par\bgroup\centering\aftergroup\par\let\mplDiscard=}
\renewcommand{\figure}{\par\bgroup\centering\aftergroup\par\let\mplDiscard=}
\begin{document}
"""


def compile_fragment(fragment: Path, dest: Path, engine: str) -> int:
    dest.mkdir(parents=True, exist_ok=True)
    content = fragment.read_text(encoding="utf-8")
    wrapper = dest / "transcription-check.tex"
    wrapper.write_text(PREAMBLE + content + "\n\\end{document}\n", encoding="utf-8")
    format_option = []
    format_name = Path(engine).name
    format_probe = subprocess.run(["kpsewhich", format_name + ".fmt"],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if format_probe.returncode:
        format_path = dest / (format_name + ".fmt")
        if not format_path.is_file():
            initialize = [engine, "-ini", "-etex", "-interaction=nonstopmode", "-halt-on-error",
                          "-jobname=" + format_name, "-output-directory", str(dest),
                          format_name + ".ini"]
            init = subprocess.run(initialize, cwd=dest, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT, text=True, timeout=180)
            (dest / "format-initialization.txt").write_text(init.stdout, encoding="utf-8")
            if init.returncode or not format_path.is_file():
                print("Could not initialize the local TeX format:")
                print("\n".join(init.stdout.splitlines()[-30:]))
                return init.returncode or 1
        format_option = ["-fmt=" + str(format_path)]
    command = [engine, *format_option, "-interaction=nonstopmode", "-halt-on-error", "-no-shell-escape",
               "-output-directory", str(dest), str(wrapper)]
    run = subprocess.run(command, cwd=dest, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, timeout=180)
    (dest / "compiler-stdout.txt").write_text(run.stdout, encoding="utf-8")
    if run.returncode:
        lines = run.stdout.splitlines()
        first = next((i for i, line in enumerate(lines) if line.startswith("!")), max(0, len(lines) - 30))
        print("\n".join(lines[max(0, first - 3): first + 24]))
        print(f"Compilation failed for {fragment.name}")
    else:
        warnings = [s for s in run.stdout.splitlines()
                    if "Warning" in s or "Overfull" in s or "Missing character" in s]
        print(f"Compilation succeeded for {fragment.name}")
        if warnings:
            print("\n".join(warnings))
    return run.returncode


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fragment", nargs="?", type=Path,
                        default=root / "MPL_29_049-094_transcription.tex")
    parser.add_argument("--engine", default="xelatex")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    fragment = args.fragment.resolve()
    if not fragment.is_file():
        parser.error(f"fragment does not exist: {fragment}")
    engine = shutil.which(args.engine)
    if not engine:
        parser.error(f"engine unavailable: {args.engine}")
    if args.output_dir:
        return compile_fragment(fragment, args.output_dir.resolve(), engine)
    with tempfile.TemporaryDirectory(prefix="mpl29-latex-") as temporary:
        return compile_fragment(fragment, Path(temporary), engine)


if __name__ == "__main__":
    sys.exit(main())
