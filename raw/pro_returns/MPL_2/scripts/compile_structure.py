#!/usr/bin/env python3
"""Temporary LaTeX syntax smoke check; never edits source or reads images/context.

Editorial wrapper macros have deliberately neutral definitions. This checks
structural typesettability, not appearance or fidelity. Outputs stay in /tmp.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


PREAMBLE = r"""\documentclass{article}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{tikz-cd}
\usetikzlibrary{shapes.geometric,decorations.pathmorphing,decorations.pathreplacing,decorations.markings,arrows.meta}
\setlength{\textwidth}{18cm}
\setlength{\textheight}{24cm}
\setlength{\oddsidemargin}{-1cm}
\newcommand{\cotefile}[1]{}
\newcommand{\scanpage}[1]{\typeout{MPLCHECK SCAN #1}}
\newcommand{\mspage}[1]{}
\newcommand{\illegible}[1]{[illegible #1]}
\let\deleted\relax
\let\inserted\relax
\let\margin\relax
\let\uline\relax
\let\uuline\relax
\let\unsure\relax
\let\diagram\relax
\let\figure\relax
\begin{document}
"""

MIXED_WRAPPER_DEFINITIONS = r"""\ExplSyntaxOn
\cs_new_protected:Npn \mpl_mixed_wrapper:n #1
 {\mode_if_math:TF
   {\tl_if_in:nnTF {#1} {$} {\text{#1}} {#1}}
   {#1}}
\cs_set_eq:NN \uuline \mpl_mixed_wrapper:n
\cs_set_eq:NN \inserted \mpl_mixed_wrapper:n
\ExplSyntaxOff
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--temp", type=Path, help="Reuse an existing temporary harness directory")
    parser.add_argument("--scans", nargs="*", type=int, help="Optional subset of scan numbers")
    parser.add_argument("--mixed-wrapper-boxes", action="store_true",
                        help="Box dollar-delimited mixed text/math in uuline/inserted when already in math mode")
    args = parser.parse_args()
    temporary = args.temp or Path(tempfile.mkdtemp(prefix="mpl2_tex_structure_"))
    temporary.mkdir(parents=True, exist_ok=True)
    tex_env = os.environ.copy()
    # Packages are installed, but this environment lacks their filename DB and
    # dumped formats. Omitting !! enables normal recursive disk lookup.
    tex_env["TEXMF"] = "{/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}"
    tex_env["TEXMFVAR"] = str(temporary / "var")
    tex_env["TEXMFCONFIG"] = str(temporary / "config")
    tex_env["TEXFORMATS"] = str(temporary) + "//:"
    if not (temporary / "xelatex.fmt").exists():
        build = subprocess.run(
            ["xetex", "-ini", "-etex", "-jobname=xelatex", "-interaction=nonstopmode", "xelatex.ini"],
            cwd=temporary, env=tex_env, capture_output=True, text=True, timeout=60)
        if build.returncode or not (temporary / "xelatex.fmt").exists():
            print(json.dumps({"ok": False, "stage": "format setup", "temporary": str(temporary),
                              "diagnostic": (build.stdout + build.stderr)[-5000:]}, indent=2))
            return 2

    source_paths = sorted((args.root / "pages").glob("MPL_2_2_scan*.tex"))
    if args.scans:
        source_paths = [p for p in source_paths if int(p.stem[-3:]) in args.scans]

    def check_page(path: Path) -> dict:
        source_bytes = path.read_bytes()
        source = source_bytes.decode("utf-8")
        work = temporary / path.stem
        work.mkdir(exist_ok=True)
        # A separate input preserves the original source line numbers.
        (work / "source.tex").write_text(source, encoding="utf-8")
        preamble = PREAMBLE
        if args.mixed_wrapper_boxes:
            preamble = preamble.replace(r"\begin{document}", MIXED_WRAPPER_DEFINITIONS + r"\begin{document}")
        (work / "check.tex").write_text(preamble + r"\input{source.tex}" + "\n"
                                        + r"\end{document}" + "\n", encoding="utf-8")
        process = subprocess.run(
            ["xelatex", "-no-pdf", "-no-shell-escape", "-file-line-error", "-halt-on-error",
             "-interaction=nonstopmode", "check.tex"],
            cwd=work, env=tex_env, capture_output=True, text=True, timeout=60)
        output = process.stdout + process.stderr
        diagnostics = []
        lines = output.splitlines()
        for i, line in enumerate(lines):
            if re.match(r"(?:\./)?(?:source|check)\.tex:\d+:|^!", line):
                diagnostics.append("\n".join(lines[i:i + 7]))
        if process.returncode and not diagnostics:
            diagnostics.append("\n".join(lines[-15:]))
        return {"scan": int(path.stem[-3:]), "exit_code": process.returncode,
                "snapshot_sha256": hashlib.sha256(source_bytes).hexdigest(),
                "source_changed_during_check": path.read_bytes() != source_bytes,
                "diagnostics": diagnostics}

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(check_page, source_paths))
    report = {"ok": all(r["exit_code"] == 0 for r in results),
              "temporary": str(temporary), "pages_checked": len(results),
              "mixed_wrapper_boxes": args.mixed_wrapper_boxes,
              "pages_passed": sum(r["exit_code"] == 0 for r in results), "results": results,
              "scope": "Neutral-wrapper structural compilation only; no image or context access."}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
