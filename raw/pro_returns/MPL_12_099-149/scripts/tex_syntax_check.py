#!/usr/bin/env python3
"""Optional one-pass TeX syntax check, with a dependency-only probe mode.

Never edits the fragment, installs packages, fetches files, freezes a result,
or opens the source archives. Missing dependencies stop the run before the
fragment is opened by TeX. This is not a diplomatic rendering specification.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ENGINES = ("xelatex", "lualatex", "pdflatex")
BASE_DEPENDENCIES = ("article.cls", "amsmath.sty", "amssymb.sty", "tikz.sty", "tikz-cd.sty")

PREAMBLE = r"""\documentclass[11pt]{article}
% Generated temporary wrapper. The supplied fragment remains unchanged.
% This wrapper checks syntax; its annotation styling is deliberately neutral.
__ENCODING_PACKAGES__
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{tikz-cd}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathmorphing,decorations.pathreplacing}
\IfFileExists{mathrsfs.sty}{\usepackage{mathrsfs}}{}
\IfFileExists{bm.sty}{\usepackage{bm}}{}
\DeclareRobustCommand{\cotefile}[1]{\par\bigskip\noindent Cote #1\par}
\DeclareRobustCommand{\scanpage}[1]{\par\bigskip\noindent Scan #1\par}
\DeclareRobustCommand{\mspage}[1]{\par\noindent Manuscript page #1\par}
% Identity wrappers accept their actual arguments in either text or math mode.
% Nothing inside a deletion, insertion, margin note, doubt or underline is lost.
\long\def\deleted#1{#1}
\long\def\inserted#1{#1}
\long\def\margin#1{#1}
\long\def\uline#1{#1}
\long\def\uuline#1{#1}
\long\def\unsure#1{#1}
\DeclareRobustCommand{\illegible}[1]{%
  \ifmmode\text{[illegible: #1]}\else[illegible: #1]\fi}
% An array needs math mode. tikzcd also works within this display wrapper.
% Nested diagram arguments already in math mode are passed through directly.
\long\def\diagram#1{\ifmmode#1\else\[#1\]\fi}
% The user-defined figure macro intentionally replaces LaTeX's float opener.
% Its actual TikZ argument is passed through without introducing a float.
\long\def\figure#1{#1}
\begin{document}
\input{\detokenize{__FRAGMENT_PATH__}}
\end{document}
"""


def probe(requested_engine: str | None) -> dict:
    engines = {name: shutil.which(name) for name in ENGINES}
    engine = requested_engine or next((name for name in ENGINES if engines[name]), None)
    lookup = shutil.which("kpsewhich")
    dependencies = list(BASE_DEPENDENCIES)
    dependencies += ["inputenc.sty", "fontenc.sty"] if engine == "pdflatex" else ["fontspec.sty"]
    packages = {}
    for name in dependencies:
        if lookup:
            result = subprocess.run([lookup, name], capture_output=True, text=True, timeout=15)
            packages[name] = result.stdout.strip() if result.returncode == 0 else None
        else:
            packages[name] = None
    missing = [name for name, value in packages.items() if not value]
    available = bool(engine and engines.get(engine) and lookup and not missing)
    return {
        "available": available,
        "selected_engine": engine,
        "engine_paths": engines,
        "kpsewhich": lookup,
        "package_paths": packages,
        "missing_packages": missing,
        "installed_or_downloaded_anything": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", action="store_true", help="check executables/packages only; never inspect a fragment")
    parser.add_argument("--engine", choices=ENGINES)
    parser.add_argument("--fragment", type=Path,
                        default=Path(__file__).resolve().parent.parent / "MPL_12_099-149_transcription.tex")
    parser.add_argument("--output-directory", type=Path, help="scratch output directory, outside the deliverable bundle")
    args = parser.parse_args()
    try:
        status = probe(args.engine)
    except (OSError, subprocess.TimeoutExpired) as error:
        print(json.dumps({"compiled": False, "probe_failed": type(error).__name__}))
        return 2
    if args.probe or not status["available"]:
        print(json.dumps({"compiled": False, "probe_only": args.probe, "tooling": status}, indent=2))
        return 0 if status["available"] else 2

    # Reach this point only after every mandatory dependency was located.
    fragment = args.fragment.resolve()
    if not fragment.is_file():
        print(json.dumps({"compiled": False, "error": "Fragment path is not a regular file"}))
        return 2
    if any(char in str(fragment) for char in "{}%#\\\n\r"):
        print(json.dumps({"compiled": False, "error": "Fragment path contains unsupported TeX filename characters"}))
        return 2
    bundle = Path(__file__).resolve().parent.parent
    if args.output_directory:
        output = args.output_directory.resolve()
        if output == bundle or bundle in output.parents:
            print(json.dumps({"compiled": False, "error": "Use an output directory outside the deliverable bundle"}))
            return 2
        output.mkdir(parents=True, exist_ok=True)
    else:
        output = Path(tempfile.mkdtemp(prefix="mpl_tex_syntax_", dir=bundle.parent))
    wrapper = output / "syntax_wrapper.tex"
    if wrapper.exists():
        print(json.dumps({"compiled": False, "error": "Wrapper already exists; choose a fresh output directory"}))
        return 2
    encoding = (r"\usepackage[utf8]{inputenc}" + "\n" + r"\usepackage[T1]{fontenc}") if status["selected_engine"] == "pdflatex" else r"\usepackage{fontspec}"
    wrapper.write_text(PREAMBLE.replace("__ENCODING_PACKAGES__", encoding).replace("__FRAGMENT_PATH__", str(fragment)), encoding="utf-8")
    executable = status["engine_paths"][status["selected_engine"]]
    command = [executable, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error",
               "-file-line-error", "-output-directory", str(output), str(wrapper)]
    try:
        result = subprocess.run(command, cwd=output, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        print(json.dumps({"compiled": False, "error": "TeX run exceeded 180 seconds", "output_directory": str(output)}))
        return 1
    (output / "compiler_output.txt").write_text(result.stdout + result.stderr, encoding="utf-8")
    # Do not echo manuscript excerpts from compiler diagnostics to stdout.
    print(json.dumps({
        "compiled": True,
        "syntax_passed": result.returncode == 0,
        "exit_code": result.returncode,
        "engine": status["selected_engine"],
        "output_directory": str(output),
        "compiler_output": str(output / "compiler_output.txt"),
        "tex_log": str(output / "syntax_wrapper.log"),
        "fragment_modified": False,
        "scope": "One-pass syntax check under neutral editorial-macro definitions; no fidelity certification",
    }, indent=2))
    return 0 if result.returncode == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
