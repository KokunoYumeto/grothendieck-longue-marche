#!/usr/bin/env python3
"""Mechanically parse page fragments in temporary LaTeX wrappers.

Never changes a transcription file. Wrappers, TeX logs and generated PDFs go
outside the deliverable directory. State/underline macros are identity macros:
this tests LaTeX syntax, not the appearance or correctness of the transcription.
Only sanitized diagnostics (file, line and error) are reported, not source prose.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import os
import re
import shutil
import subprocess
import sys


PREAMBLE = r"""\documentclass{article}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,mathrsfs}
\usepackage{tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,calc,positioning,patterns}
\newcommand{\cotefile}[1]{\par\noindent Cote~#1\par}
\newcommand{\scanpage}[1]{\par\noindent Scan~#1\par}
\newcommand{\mspage}[1]{\par\noindent Manuscript~#1\par}
% Leave each following brace group in the input stream, without collecting it
% as a macro argument. This lets TikZ set matrix-ampersand catcodes itself.
\newcommand{\deleted}{}
\newcommand{\inserted}{}
\newcommand{\margin}{}
\newcommand{\uline}{}
\newcommand{\uuline}{}
% Both arrays and tikz-cd are permitted diagram bodies. Supply display math;
% rescan so TikZ can give ampersands their expected matrix catcode.
\newcommand{\diagram}[1]{\[\scantokens{#1}\]}
\renewcommand{\figure}{}
\newcommand{\unsure}{}
\newcommand{\illegible}[1]{\mbox{[#1]}}
\begin{document}
"""


def compile_one(page: Path, output_root: Path, engine: str, format_path: Path | None) -> tuple[str, bool, list[str]]:
    output_dir = output_root / page.stem
    output_dir.mkdir(parents=True, exist_ok=True)
    wrapper = output_dir / "parse.tex"
    wrapper.write_text(PREAMBLE + "\\input{" + page.as_posix() + "}\n\\end{document}\n", encoding="utf-8")
    command = [engine, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
               "-file-line-error", "-output-directory", str(output_dir)]
    if Path(engine).name == "xelatex":
        # Parsing needs no PDF driver; avoid unrelated xdvipdfmx/font failures.
        command.append("-no-pdf")
    if format_path is not None:
        command.append("-fmt=" + str(format_path.resolve()))
    command.append(str(wrapper))
    environment = os.environ.copy()
    environment["max_print_line"] = "1000"
    completed = subprocess.run(command, cwd=output_dir, capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=60, env=environment)
    (output_dir / "engine.stdout.txt").write_text(completed.stdout + completed.stderr, encoding="utf-8")
    diagnostics = []
    # TeX's file-line-error format includes only the error message on its first
    # line; subsequent l.N/source-context lines are deliberately not returned.
    for line in (completed.stdout + completed.stderr).splitlines():
        match = re.match(r"^(.+?\.(?:tex|sty|cls)):(\d+):\s*(.*)$", line)
        if match:
            diagnostics.append(f"{match.group(1)}:{match.group(2)}: {match.group(3)}")
        elif line.startswith("! "):
            diagnostics.append(line)
    if completed.returncode and not diagnostics:
        diagnostics.append(f"Engine exit {completed.returncode}; consult scratch log {output_dir / 'parse.log'}")
    return page.name, completed.returncode == 0, diagnostics


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--scratch", type=Path, required=True,
                        help="temporary output directory outside the deliverable folder")
    parser.add_argument("--through", type=int, help="only inspect filenames at or below this scan number")
    parser.add_argument("--engine", choices=("lualatex", "xelatex"), default="lualatex")
    parser.add_argument("--format", type=Path, help="explicit scratch-built engine format file")
    parser.add_argument("--jobs", type=int, default=4)
    args = parser.parse_args()
    root = args.root.resolve()
    scratch = args.scratch.resolve()
    if scratch == root or root in scratch.parents:
        parser.error("--scratch must be outside the deliverable folder")
    engine = shutil.which(args.engine)
    if engine is None:
        parser.error(f"{args.engine} is unavailable")
    pages = []
    for page in sorted((root / "pages").glob("MPL_93_047-091_93_scan*.tex")):
        match = re.fullmatch(r"MPL_93_047-091_93_scan(\d{3})\.tex", page.name)
        if match and (args.through is None or int(match.group(1)) <= args.through):
            pages.append(page)
    if not pages:
        parser.error("no matching saved page fragments")
    scratch.mkdir(parents=True, exist_ok=True)
    print(f"Engine: {engine}; saved page fragments: {len(pages)}")
    print("State/underline macros are identity definitions; this is syntax QA only.")
    with ThreadPoolExecutor(max_workers=max(1, min(args.jobs, 4))) as pool:
        results = list(pool.map(lambda page: compile_one(page, scratch, engine, args.format), pages))
    failures = 0
    report = []
    for name, passed, diagnostics in results:
        report.append(("PASS " if passed else "FAIL ") + name)
        failures += not passed
        report.extend("  " + line for line in diagnostics)
    report.append(f"Passed {len(results) - failures}/{len(results)} page fragments; failures: {failures}.")
    (scratch / "syntax-report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
