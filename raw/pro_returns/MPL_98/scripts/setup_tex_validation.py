#!/usr/bin/env python3
"""Prepare a local pdfLaTeX syntax-check runtime from installed TeX resources.

No downloads, package installations, manuscript reads, or system changes.
The generated format, font map, logs, JSON environment, and independent smoke
test stay under the explicitly selected --runtime directory.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess


MAPS = ["cm.map", "cmextra.map", "symbols.map", "latxfont.map", "euler.map",
        "cyrillic.map", "lm.map"]
SMOKE = r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern,amsmath,amssymb,xcolor,tikz-cd,geometry}
\IfFileExists{ulem.sty}{\usepackage[normalem]{ulem}}{}
\providecommand{\uline}[1]{\underline{#1}}
\providecommand{\uuline}[1]{\underline{\underline{#1}}}
\def\diagram{\par\bgroup\centering\aftergroup\par\let\mplwrapperopen=}
\def\inserted{\bgroup\color{blue!70!black}\let\mplwrapperopen=}
\usetikzlibrary{arrows.meta,calc,decorations.pathmorphing,positioning}
\begin{document}
Independent syntax smoke test: \uline{français}, \uuline{mathématiques}.
\[\mathcal{T}^!_3\otimes\mathfrak{S}_2\longrightarrow\bigwedge^3 M\]
\inserted{\diagram{\begin{tikzcd}
A\arrow[r,"f"]\arrow[d,"g"']&B\arrow[d,"h"]\\
C\arrow[r,"k"']&D
\end{tikzcd}}}
\begin{tikzpicture}
\draw[->] (0,0) .. controls (1,1) and (2,-1) .. (3,0);
\end{tikzpicture}
\end{document}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--tex-tree", type=Path, action="append",
                        help="repeat for each installed TeX tree; defaults to the two observed system trees")
    args = parser.parse_args()
    runtime = args.runtime.resolve()
    runtime.mkdir(parents=True, exist_ok=True)
    trees = args.tex_tree or [Path("/usr/share/texlive/texmf-dist"), Path("/usr/share/texmf")]
    trees = [path.resolve() for path in trees if path.is_dir()]
    if not trees:
        parser.error("no installed TeX resource tree found")
    for command in ("pdftex", "pdflatex", "kpsewhich"):
        if not shutil.which(command):
            parser.error(f"required executable unavailable: {command}")
    # Default Debian paths here use !! (database-only) lookup while the mounted
    # resource trees have no ls-R databases. Per-process recursive lookup fixes
    # discovery without modifying /usr/share or any user's global settings.
    overrides = {
        "TEXMF": "{" + ",".join(str(path) for path in trees) + "}",
        "TEXMFVAR": str(runtime / "var"),
        "TEXMFCONFIG": str(runtime / "config"),
        "TEXFORMATS": str(runtime) + "//:",
        "TEXFONTMAPS": str(runtime) + "//:",
    }
    environment = dict(os.environ, **overrides)
    environment_file = runtime / "tex_environment.json"
    environment_file.write_text(json.dumps(overrides, indent=2) + "\n", encoding="utf-8")

    def locate(name: str) -> Path:
        run = subprocess.run(["kpsewhich", name], env=environment,
                             capture_output=True, text=True, timeout=15)
        if run.returncode or not run.stdout.strip():
            raise RuntimeError(f"installed TeX resource not found: {name}")
        return Path(run.stdout.strip())

    def run_tex(arguments: list[str], log_name: str) -> int:
        run = subprocess.run(arguments, env=environment, cwd=runtime,
                             capture_output=True, text=True, timeout=120)
        (runtime / log_name).write_text(run.stdout + run.stderr, encoding="utf-8")
        return run.returncode

    resources = {name: str(locate(name)) for name in MAPS}
    # These are installed font maps, not manuscript sources. Runtime outputs are
    # disposable and should remain outside the user deliverable/checkpoint tree.
    (runtime / "pdftex.map").write_text(
        "\n".join(Path(path).read_text(encoding="utf-8") for path in resources.values()),
        encoding="utf-8")
    format_code = run_tex(["pdftex", "-ini", "-etex", "-no-shell-escape",
                           "-interaction=nonstopmode", "-halt-on-error",
                           "-jobname=pdflatex", "-progname=pdflatex", "pdflatex.ini"],
                          "format_stdout.txt")
    report = {"setup": "local-only; no downloads or system mutations",
              "runtime": str(runtime), "environment": str(environment_file),
              "font_map_sources": resources, "format_exit_code": format_code,
              "limitations": [
                  "The absent language.dat makes format generation use the installed default hyphen.tex; this is a syntax-check runtime, not final French typography.",
                  "If ulem.sty is absent, smoke and validation harnesses use simple non-wrapping standard underline definitions.",
                  "Successful smoke compilation establishes package/runtime availability, not manuscript correctness."]}
    if format_code == 0:
        (runtime / "smoke.tex").write_text(SMOKE, encoding="utf-8")
        smoke_code = run_tex(["pdflatex", "-no-shell-escape", "-interaction=nonstopmode",
                              "-halt-on-error", "smoke.tex"], "smoke_stdout.txt")
        report["smoke_exit_code"] = smoke_code
        report["smoke_pdf"] = str(runtime / "smoke.pdf") if smoke_code == 0 else None
    else:
        report["smoke_exit_code"] = None
    (runtime / "setup_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if format_code == 0 and report["smoke_exit_code"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
