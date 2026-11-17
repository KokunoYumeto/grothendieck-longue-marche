#!/usr/bin/env python3
"""Compile a transcription fragment without changing it.

Creates a XeLaTeX wrapper, a local format if needed, and all build output under
--output (default: compilation_support/render).  TeX shell escape is disabled.
Editorial macros are illustrative validation renderings, not a final edition:
deletions, insertions, doubts, and margins use colors; simple underlines are used
when ulem is unavailable.  The source fragment itself is always input unchanged.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys


SUPPORT = Path(__file__).resolve().parent

PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=18mm]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{xcolor}
\usepackage{tikz,tikz-cd}
\usetikzlibrary{arrows.meta,calc,decorations.markings,positioning,shapes.geometric}
% ulem is not installed in this runtime; these simple underlines do not wrap.
\newcommand{\uline}[1]{\underline{#1}}
\newcommand{\uuline}[1]{\underline{\underline{#1}}}
\allowdisplaybreaks
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\setlength{\emergencystretch}{3em}
\newif\ifMPLfirstscan
\MPLfirstscantrue
\newcommand{\cotefile}[1]{\gdef\MPLcote{#1}}
\def\MPLcote{83}
\newcommand{\scanpage}[1]{%
  \ifMPLfirstscan\MPLfirstscanfalse\else\clearpage\fi
  {\large\bfseries Cote \MPLcote\quad Scan #1}\par\medskip
}
\newcommand{\mspage}[1]{{\bfseries #1}}
% Read colored groups as a stream, so a nested tikzcd can set ampersand catcodes.
\def\MPLcolored#1{\bgroup\color{#1}\let\MPLdiscard=}
\newcommand{\deleted}{\MPLcolored{red!60!black}}
\newcommand{\inserted}{\MPLcolored{blue!60!black}}
\newcommand{\margin}{\MPLcolored{teal!65!black}}
\newcommand{\unsure}{\MPLcolored{orange!65!black}}
\newcommand{\illegible}[1]{{\color{red!70!black}[illegible: #1]}}
% Keep the following brace group, without scanning it as a macro argument.
\newcommand{\diagram}{}
\renewcommand{\figure}{}
\begin{document}
% The runtime has no generated font maps; use Latin Modern's math encoding.
\special{pdf:mapfile +lm-math.map}
"""


def environment() -> tuple[dict[str, str], Path]:
    fmt = SUPPORT / "texmf-var" / "web2c" / "xetex"
    fmt.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    # The installed tree has usable packages but no working ls-R databases.
    # Avoid the system configuration's database-only (!!) search prefixes.
    env.update({
        "TEXMF": "{/usr/share/texmf,/usr/share/texlive/texmf-dist}",
        "TEXMFVAR": str(SUPPORT / "texmf-var"),
        "TEXMFCONFIG": str(SUPPORT / "texmf-config"),
        "TEXMFCACHE": str(SUPPORT / "texmf-cache"),
        "TEXFORMATS": str(fmt) + "//:",
        "VARTEXFONTS": str(SUPPORT / "texmf-var" / "fonts"),
        "MKTEXPK": "0", "MKTEXTFM": "0", "MKTEXFMT": "0",
    })
    return env, fmt


def run_logged(command: list[str], cwd: Path, env: dict[str, str], log: Path, timeout: int) -> int:
    try:
        result = subprocess.run(command, cwd=cwd, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                check=False, timeout=timeout)
        output = result.stdout
        status = result.returncode
    except subprocess.TimeoutExpired as exc:
        partial = exc.stdout or ""
        output = partial.decode("utf-8", errors="replace") if isinstance(partial, bytes) else partial
        output += f"\nBUILD TIMEOUT after {timeout} seconds.\n"
        status = 124
    log.write_text(output, encoding="utf-8")
    if status:
        print(output[-6000:])
    return status


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fragment", type=Path)
    parser.add_argument("--output", type=Path, default=SUPPORT / "render")
    parser.add_argument("--passes", type=int, choices=[1, 2], default=1)
    parser.add_argument("--timeout", type=int, default=60, help="Timeout in seconds for each TeX process.")
    args = parser.parse_args()
    fragment = args.fragment.resolve()
    if not fragment.is_file():
        parser.error("Fragment file does not exist.")
    if any(char in str(fragment) for char in "%{}\n\r\\"):
        parser.error("Fragment path contains a character unsupported by this wrapper.")
    engine = shutil.which("xelatex")
    if engine is None:
        parser.error("XeLaTeX is not installed.")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    env, fmt = environment()
    if not (fmt / "xelatex.fmt").is_file():
        command = [engine, "-ini", "-etex", "-no-shell-escape", "-interaction=nonstopmode",
                   "-halt-on-error", "-file-line-error", "-jobname=xelatex", "-progname=xelatex", "xelatex.ini"]
        status = run_logged(command, fmt, env, SUPPORT / "format-build.stdout.log", args.timeout)
        if status:
            print("Local XeLaTeX format build failed.")
            return status
    wrapper = output / "transcription_validation.tex"
    wrapper.write_text(PREAMBLE + "\\input{\\detokenize{" + fragment.as_posix() + "}}\n\\end{document}\n",
                       encoding="utf-8")
    command = [engine, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
               "-file-line-error", "-synctex=0", wrapper.name]
    for number in range(1, args.passes + 1):
        log = output / f"compile-pass-{number}.stdout.log"
        status = run_logged(command, output, env, log, args.timeout)
        print(f"Pass {number}: exit {status}; log {log}")
        if status:
            return status
    pdf = output / "transcription_validation.pdf"
    print(f"PDF: {pdf}" if pdf.is_file() else "No PDF was produced.")
    print("The input fragment was not modified. Editorial styling is for validation only.")
    return 0 if pdf.is_file() else 1


if __name__ == "__main__":
    sys.exit(main())
