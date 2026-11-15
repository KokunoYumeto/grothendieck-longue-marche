#!/usr/bin/env python3
"""Compile a temporary snapshot for syntax only, without changing source files.

The allowed editorial macros are transparent here. This is deliberately not a
presentation renderer: it accepts paragraph/display arguments without imposing
boxes, and it does not assess readings or visual fidelity. Draft mode suppresses
PDF generation; all intermediate TeX files remain outside the deliverable.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,mathrsfs,mathtools}
\usepackage{tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,positioning,calc}
\setlength{\textwidth}{17cm}
\setlength{\textheight}{25cm}
\setlength{\oddsidemargin}{-0.5cm}
\setlength{\topmargin}{-1.5cm}
\newcommand{\cotefile}[1]{}
\newcommand{\scanpage}[1]{\clearpage\typeout{MPL-SCAN:#1}}
\newcommand{\mspage}[1]{}
\newcommand{\deleted}[1]{#1}
\newcommand{\inserted}[1]{#1}
\newcommand{\margin}[1]{#1}
\newcommand{\uline}[1]{#1}
\newcommand{\uuline}[1]{#1}
% Retokenization lets tikzcd activate &, including within \deleted{...}.
\newcommand{\diagram}[1]{\begingroup\scantokens{#1}\endgroup}
\renewcommand{\figure}[1]{#1}
\newcommand{\unsure}[1]{#1}
\newcommand{\illegible}[1]{\ensuremath{?}}
\begin{document}
"""


def run(command: list[str], cwd: Path, env: dict[str, str], timeout: int) -> subprocess.CompletedProcess:
    return subprocess.run(command, cwd=cwd, env=env, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=timeout)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package_directory", type=Path)
    parser.add_argument("--temporary-parent", type=Path, default=Path(tempfile.gettempdir()))
    parser.add_argument("--report", type=Path, help="write a concise JSON report here; never stores source text")
    args = parser.parse_args()
    root = args.package_directory.resolve()
    args.temporary_parent.mkdir(parents=True, exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix="mpl-syntax-", dir=args.temporary_parent))
    snapshot = temp / "pages"
    snapshot.mkdir()
    captured = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    files = sorted((root / "pages").glob("MPL_60_036-070_60_scan*.tex"))
    for source in files:
        shutil.copyfile(source, snapshot / source.name)
    wrapper = PREAMBLE + "\n".join(r"\input{pages/" + path.name + "}" for path in files) + "\n\\end{document}\n"
    (temp / "syntax.tex").write_text(wrapper, encoding="utf-8")

    env = os.environ.copy()
    # These trees exist in the supplied environment, but its ls-R databases may
    # be absent. Explicitly omit !! so Kpathsea can search the installed files.
    env["TEXMF"] = "{" + str(temp / "texmf-var") + ",/etc/texmf,/var/lib/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
    env["TEXMFVAR"] = str(temp / "texmf-var")
    env["TEXMFCONFIG"] = str(temp / "texmf-config")
    env["TEXFORMATS"] = str(temp) + ":"
    env["TEXMFOUTPUT"] = str(temp)
    for directory in [temp / "texmf-var", temp / "texmf-config"]:
        directory.mkdir()
    result = {"snapshot_utc": captured, "temporary_directory": str(temp),
              "page_count": len(files), "source_files_modified": False,
              "purpose": "LaTeX syntax only; editorial macros are transparent",
              "compiler_mode": "pdfLaTeX -draftmode -halt-on-error; no PDF generated",
              "format_build_status": None, "compile_status": None,
              "error_lines": [], "scan_markers_reached": [],
              "limitations": ["Sources may change after the temporary snapshot.",
                              "This does not certify readings, layout fidelity, or source completeness.",
                              "Overfull and underfull boxes are not reading errors."]}
    try:
        build = run(["pdflatex", "-ini", "-etex", "-jobname=pdflatex",
                     "-interaction=nonstopmode", "-halt-on-error", "pdflatex.ini"], temp, env, 180)
        (temp / "format-build-output.txt").write_text(build.stdout, encoding="utf-8")
        result["format_build_status"] = build.returncode
        if build.returncode:
            result["error_lines"] = [line for line in build.stdout.splitlines() if line.startswith("!") or "Error" in line][-12:]
        else:
            compiled = run(["pdflatex", "-draftmode", "-fmt=" + str(temp / "pdflatex.fmt"),
                            "-interaction=nonstopmode", "-halt-on-error",
                            "-file-line-error", "-no-shell-escape", "syntax.tex"], temp, env, 180)
            (temp / "compile-output.txt").write_text(compiled.stdout, encoding="utf-8")
            result["compile_status"] = compiled.returncode
            result["scan_markers_reached"] = re.findall(r"MPL-SCAN:(\d+)", compiled.stdout)
            lines = compiled.stdout.splitlines()
            result["error_lines"] = [line for line in lines if
                                     re.search(r"\.tex:\d+:|^!|Fatal error|Undefined control sequence", line)][-15:]
            result["output_page_count"] = next((int(m.group(1)) for m in [re.search(r"Output written on .*\((\d+) pages?", compiled.stdout)] if m), None)
    except (OSError, subprocess.TimeoutExpired) as exc:
        result["error_lines"] = [str(exc)]
    result["syntax_pass"] = result["compile_status"] == 0
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 0 if result["syntax_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
