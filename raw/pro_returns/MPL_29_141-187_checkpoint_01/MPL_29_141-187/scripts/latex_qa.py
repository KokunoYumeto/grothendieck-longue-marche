#!/usr/bin/env python3
"""Prepare a separate QA wrapper, optionally compile it, without editing sources.

This is a syntax/layout aid, not a diplomatic rendering specification or an
accuracy check.  It never reads images, archives, context, or page fragments in
Python.  The requested combined fragment is read only by TeX when --compile is
explicitly supplied.  No package installation and no shell escape are used.

Textual deletions/insertions/marginal notes use visible colored boundary labels,
which safely accept paragraphs, displayed mathematics, and complete diagrams.
In math mode deletions use cancel, while insertions/marginal notes use color.
The final transcription fragment remains untouched.  If ulem is unavailable,
underlining falls back to native LaTeX underline; that fallback cannot wrap
underlined text across lines.  This limitation is only in the QA rendering.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys


PREAMBLE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=18mm]{geometry}
__FONT_SETUP__
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage{xcolor,graphicx,cancel}
\usepackage{tikz,tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,decorations.markings,
  calc,positioning,patterns,fit,bending,shapes.geometric}
\IfFileExists{ulem.sty}{%
  \usepackage[normalem]{ulem}%
}{%
  \newcommand{\uline}[1]{\underline{#1}}%
  \newcommand{\uuline}[1]{\underline{\underline{#1}}}%
}
\definecolor{qaDeleted}{RGB}{150,35,35}
\definecolor{qaInserted}{RGB}{0,105,65}
\definecolor{qaMargin}{RGB}{100,45,140}
\definecolor{qaDoubt}{RGB}{155,90,0}
\setlength{\parindent}{1em}
\setlength{\parskip}{5pt}
\setlength{\emergencystretch}{2em}
\overfullrule=3pt
\allowdisplaybreaks

% These macros deliberately accept long (multi-paragraph) arguments.
% Color/boundaries are QA conventions, not additions to the source fragment.
\newcommand{\qaCote}{29}
\NewDocumentCommand{\cotefile}{m}{\gdef\qaCote{#1}}
\NewDocumentCommand{\scanpage}{m}{%
  \clearpage\section*{Cote \qaCote\quad Scan #1}%
  \markboth{Cote \qaCote}{Scan #1}%
}
\NewDocumentCommand{\mspage}{+m}{%
  \par\noindent\textit{Manuscript page: #1}\par
}
\NewDocumentCommand{\deleted}{+m}{%
  \begingroup\color{qaDeleted}%
  \ifmmode\cancel{#1}%
  \else\textsuperscript{[deleted]}#1\textsuperscript{[/deleted]}\fi
  \endgroup
}
\NewDocumentCommand{\inserted}{+m}{%
  \begingroup\color{qaInserted}%
  \ifmmode #1%
  \else\textsuperscript{[inserted]}#1\textsuperscript{[/inserted]}\fi
  \endgroup
}
\NewDocumentCommand{\margin}{+m}{%
  \begingroup\color{qaMargin}%
  \ifmmode #1%
  \else\textsuperscript{[margin]}#1\textsuperscript{[/margin]}\fi
  \endgroup
}
\NewDocumentCommand{\unsure}{+m}{%
  \begingroup\color{qaDoubt}%
  \ifmmode {#1}^{\scriptscriptstyle ?}%
  \else #1\textsuperscript{?}\fi
  \endgroup
}
\NewDocumentCommand{\illegible}{m}{%
  \ifmmode\text{[illegible: #1]}\else[illegible: #1]\fi
}
\NewDocumentCommand{\diagram}{+m}{%
  \par\begingroup\centering #1\par\endgroup
}
% The user's drawing macro occupies the standard figure environment's name.
% Figure environments must not be used in this QA wrapper.
\RenewDocumentCommand{\figure}{+m}{%
  \par\begingroup\centering #1\par\endgroup
}

\begin{document}
\input{\detokenize{__INPUT_PATH__}}
\end{document}
"""


def tex_path(path: Path) -> str:
    value = path.resolve().as_posix()
    # These characters cannot be safely handled by this simple detokenize form.
    # The task's supplied paths do not contain them.
    if any(char in value for char in "{}%\n\r"):
        raise ValueError("Source path contains a character unsupported by the QA wrapper.")
    return value


def main() -> int:
    package = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "fragment", nargs="?", type=Path,
        default=package / "MPL_29_141-187_transcription.tex",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=package.parent / "latex_qa",
        help="Separate scratch directory for the wrapper and compiler products.",
    )
    parser.add_argument("--engine", choices=["lualatex", "xelatex", "pdflatex"], default="lualatex")
    parser.add_argument("--compile", action="store_true", help="Explicitly authorize reading the fragment through TeX and compiling it.")
    parser.add_argument("--passes", type=int, choices=[1, 2], default=1)
    parser.add_argument("--timeout", type=int, default=60, help="Seconds allowed per compiler pass.")
    args = parser.parse_args()
    if args.timeout < 1:
        parser.error("--timeout must be positive")
    engine = shutil.which(args.engine)
    if engine is None:
        print(f"TeX engine unavailable: {args.engine}; no installation attempted.", file=sys.stderr)
        return 2
    source = args.fragment.resolve()
    if not source.is_file():
        print(f"Combined fragment does not exist: {source}", file=sys.stderr)
        return 2
    out = args.output_dir.resolve()
    if out == package or package in out.parents:
        print("QA output directory must be outside the deliverable package.", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    font_setup = (
        r"\usepackage[T1]{fontenc}" + "\n"
        + r"\usepackage[utf8]{inputenc}" + "\n" + r"\usepackage{lmodern}"
        if args.engine == "pdflatex"
        else r"\usepackage{fontspec}" + "\n" + r"\setmainfont{Latin Modern Roman}"
    )
    try:
        wrapper_text = PREAMBLE.replace("__FONT_SETUP__", font_setup).replace("__INPUT_PATH__", tex_path(source))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    wrapper = out / "qa_transcription.tex"
    wrapper.write_text(wrapper_text, encoding="utf-8")
    print(f"Prepared QA wrapper: {wrapper}", flush=True)
    print("Revision colors/labels are QA conventions; source files remain unchanged.", flush=True)
    if not args.compile:
        print("Not compiled. Re-run with --compile when source inspection is authorized.")
        return 0
    command = [
        engine, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
        "-file-line-error", f"-output-directory={out}", str(wrapper),
    ]
    for number in range(1, args.passes + 1):
        print(f"Compiler pass {number}/{args.passes}", flush=True)
        try:
            process = subprocess.run(command, cwd=source.parent, timeout=args.timeout, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            print(f"Compilation did not finish: {exc}", file=sys.stderr)
            return 2
        if process.returncode:
            print(f"Compilation failed; inspect {out / 'qa_transcription.log'}", file=sys.stderr)
            return process.returncode
    print(f"Compiled QA PDF: {out / 'qa_transcription.pdf'}")
    print("A successful compilation does not validate readings, completeness, or mathematics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
