#!/usr/bin/env python3
"""Optional compilation QA. Never rewrites or assembles transcription files.

The generated wrapper, PDF, and TeX logs live outside the deliverable tree.
Editorial wrappers are deliberately transparent in this syntax-check harness;
the generated PDF is not a diplomatic edition or requested deliverable.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

PACKAGE = "MPL_67_002-052"
ROOT = Path(__file__).resolve().parent.parent
SCANS = tuple(n for n in range(2, 53) if n not in {15, 22, 23, 47, 52})

PREAMBLE = r"""\documentclass[a4paper,11pt]{article}
\usepackage[margin=22mm]{geometry}
\usepackage{iftex}
\ifPDFTeX
  \usepackage[T1]{fontenc}
  \usepackage[utf8]{inputenc}
\else
  \usepackage{fontspec}
  \setmainfont{Noto Serif CJK JP}
  \setsansfont{Noto Sans CJK JP}
  \setmonofont{Noto Sans Mono CJK JP}
\fi
\usepackage{amsmath,amssymb,mathtools}
\ifPDFTeX\else
  \usepackage{unicode-math}
  \setmathfont{Latin Modern Math}
\fi
\usepackage{tikz,tikz-cd}
\usetikzlibrary{arrows.meta,calc,decorations.pathreplacing,decorations.markings,positioning,shapes.geometric}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5\baselineskip}
\setlength{\emergencystretch}{3em}
\newcommand{\cotefile}[1]{\par\noindent\textbf{Cote #1}\par}
\newcommand{\scanpage}[1]{\clearpage\noindent\textbf{Scan #1}\par}
\newcommand{\mspage}[1]{\par\noindent\textbf{MS #1}\par}
% Zero-argument transparent wrappers leave the following braced group in the
% input stream. In particular, tikz-cd can assign its ampersand catcode before
% matrix contents are tokenized. Arrays retain ordinary ampersands.
\makeatletter
\newcommand{\diagram}{\ifmmode\expandafter\diagram@math\else\expandafter\diagram@text\fi}
\def\diagram@math{}
\def\diagram@text{\begingroup\afterassignment\diagram@start\let\diagram@token=}
\def\diagram@start{$\bgroup\aftergroup\diagram@stop}
\def\diagram@stop{$\endgroup}
\makeatother
\renewcommand{\figure}{}
\newcommand{\deleted}{}
\newcommand{\inserted}{}
\newcommand{\margin}{}
\newcommand{\unsure}{}
\newcommand{\uline}{}
\newcommand{\uuline}{}
\newcommand{\illegible}[1]{\mbox{[illegible: #1]}}
\tracinglostchars=3
\begin{document}
"""


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runtime_environment(output: Path) -> dict[str, str]:
    """Use installed TeX resources without depending on missing ls-R indexes."""
    env = os.environ.copy()
    lookup = subprocess.run(["kpsewhich", "--var-value=TEXMF"],
                            capture_output=True, text=True, check=False)
    texmf = lookup.stdout.strip().replace("!!", "")
    if texmf:
        env["TEXMF"] = "{" + str(output / "texmf-var") + "," + texmf + "}"
    env["TEXMFVAR"] = str(output / "texmf-var")
    env["TEXMFCONFIG"] = str(output / "texmf-config")
    env["TEXMFCACHE"] = str(output / "texmf-cache")
    env["TEXFORMATS"] = str(output / "formats") + ":"
    env["max_print_line"] = "10000"
    return env


def ensure_format(engine: str, output: Path, env: dict[str, str]) -> None:
    lookup = subprocess.run(["kpsewhich", engine + ".fmt"], env=env,
                            capture_output=True, text=True, check=False)
    if lookup.stdout.strip():
        return
    formats = output / "formats"
    formats.mkdir(exist_ok=True)
    executable = {"xelatex": "xetex", "pdflatex": "pdftex", "lualatex": "luahbtex"}[engine]
    command = [executable, "-ini", "-etex", "-jobname=" + engine,
               "-progname=" + engine, "-interaction=nonstopmode", "-halt-on-error",
               "-output-directory", str(formats), engine + ".ini"]
    with (output / "format_stdout.log").open("wb") as stream:
        result = subprocess.run(command, env=env, cwd=output, stdout=stream,
                                stderr=subprocess.STDOUT, timeout=180, check=False)
    if result.returncode or not (formats / (engine + ".fmt")).is_file():
        raise RuntimeError("TeX format bootstrap failed; inspect the isolated format_stdout.log")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--engine", choices=("xelatex", "lualatex", "pdflatex"), default="xelatex")
    parser.add_argument("--combined", action="store_true", help="Use the existing combined file")
    parser.add_argument("--scan", type=int, action="append", help="Limit QA to selected existing scans")
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--no-pdf", action="store_true", help="Run XeTeX syntax/glyph checks without the PDF driver")
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output_dir or root.parent / f"{PACKAGE}_latex_qa").resolve()
    if output == root or root in output.parents:
        parser.error("QA output directory must be outside the deliverable tree")
    if args.combined and args.scan:
        parser.error("--combined and --scan cannot be used together")
    if args.no_pdf and args.engine != "xelatex":
        parser.error("--no-pdf is supported by this harness with xelatex only")
    if args.scan and any(n not in SCANS for n in args.scan):
        parser.error("--scan contains a scan outside the required package")
    if args.combined:
        sources = [root / f"{PACKAGE}_transcription.tex"]
    else:
        selected = set(args.scan) if args.scan else set(SCANS)
        sources = [root / "pages" / f"{PACKAGE}_67_scan{n:03d}.tex"
                   for n in SCANS if n in selected]
        if not args.scan:
            sources = [path for path in sources if path.is_file()]
    if not sources or any(not path.is_file() for path in sources):
        parser.error("No source files, or a requested source is missing")
    if any(any(char in str(path) for char in "{}\n\r") for path in sources):
        parser.error("Unsupported characters in a source path")
    before = {str(path): digest(path) for path in sources}
    output.mkdir(parents=True, exist_ok=True)
    wrapper = output / "transcription_qa.tex"
    wrapper.write_text(PREAMBLE + "\n".join(
        r"\input{\detokenize{" + str(path) + "}}" for path in sources
    ) + "\n\\end{document}\n", encoding="utf-8")
    report = {
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "engine": args.engine,
        "source_file_count": len(sources),
        "source_hashes": before,
        "wrapper": str(wrapper),
        "editorial_wrappers_transparent": True,
        "prepared_only": args.prepare_only,
        "pdf_generation_requested": not args.no_pdf,
    }
    status = 0
    if not args.prepare_only:
        engine = shutil.which(args.engine)
        if not engine:
            parser.error(f"{args.engine} is unavailable")
        env = runtime_environment(output)
        ensure_format(args.engine, output, env)
        command = [engine, "-no-shell-escape", "-halt-on-error", "-file-line-error",
                   "-interaction=nonstopmode", "-output-directory", str(output), str(wrapper)]
        if args.no_pdf:
            command.insert(1, "-no-pdf")
        with (output / "compiler_stdout.log").open("wb") as stream:
            result = subprocess.run(command, env=env, cwd=output, stdout=stream,
                                    stderr=subprocess.STDOUT, timeout=180, check=False)
        status = result.returncode
        report["compiler_returncode"] = status
        report["pdf_exists"] = (output / "transcription_qa.pdf").is_file()
        log = (output / "compiler_stdout.log").read_text(encoding="utf-8", errors="replace")
        # Report error locations and engine diagnoses without manuscript snippets.
        report["diagnostics"] = [
            {"file": match.group(1), "line": int(match.group(2)), "diagnosis": match.group(3)}
            for match in re.finditer(r"^([^\n]+\.tex):(\d+): ([^\n]+)$", log, re.MULTILINE)
        ]
        report["overfull_box_count"] = log.count("Overfull ")
        report["underfull_box_count"] = log.count("Underfull ")
        report["missing_character_diagnostics"] = re.findall(r"^Missing character:.*$", log, re.MULTILINE)
        report["font_warning_count"] = log.count("LaTeX Font Warning:")
        report["driver_diagnostics"] = re.findall(r"(?:xdvipdfmx:[^\n]+|^Error \d+[^\n]+)", log, re.MULTILINE)
    unchanged = all(path.is_file() and digest(path) == before[str(path)] for path in sources)
    report["source_files_unchanged"] = unchanged
    if not unchanged:
        status = 2
    (output / "qa_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
