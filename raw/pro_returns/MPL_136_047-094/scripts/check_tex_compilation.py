#!/usr/bin/env python3
"""Compile immutable temporary snapshots, never the live transcription files.

Usage: python scripts/check_tex_compilation.py PACKAGE_DIRECTORY OUTPUT_DIRECTORY

The wrapper gives editorial macros transparent validation-only definitions;
it is not a proposed edition or a visual rendering specification. Each page
is compiled independently, so one failure cannot corrupt later diagnostics.
The output directory must be outside the package directory and must not exist.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import hashlib
import os
import re
import shutil
import subprocess
from pathlib import Path


PREAMBLE = r"""\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage[a4paper,margin=18mm]{geometry}
\usepackage{amsmath,amssymb,mathtools,mathrsfs}
\usepackage{tikz-cd}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.markings,patterns,shapes.geometric}
\newcommand{\cotefile}[1]{\par\noindent Cote #1\par}
\newcommand{\scanpage}[1]{\par\noindent Scan #1\par}
\newcommand{\mspage}[1]{\par\noindent #1\par}
% No-argument transparent definitions leave the following group to be read
% naturally. This avoids pre-tokenizing TikZ matrix ampersands in macro arguments.
\def\deleted{}
\def\inserted{}
\def\margin{}
\def\uline{}
\def\uuline{}
\def\diagram{}
\def\figure{}
\def\unsure{}
\long\def\illegible#1{\ifmmode\text{[illegible #1]}\else[illegible #1]\fi}
\begin{document}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--texmf-runtime", type=Path, help="Use an isolated TeX runtime with a prebuilt format and direct distribution searches")
    parser.add_argument("--scans", type=int, nargs="+", help="Check only these scan numbers, for a targeted rerun after repairs")
    args = parser.parse_args()
    root = args.directory.resolve()
    output = args.output.resolve()
    if output == root or root in output.parents:
        parser.error("Output must be outside the deliverable package")
    engine = shutil.which("xelatex") or shutil.which("lualatex")
    if engine is None:
        parser.error("No Unicode-capable TeX engine found")
    output.mkdir(parents=True, exist_ok=False)
    environment = os.environ.copy()
    if args.texmf_runtime:
        runtime = args.texmf_runtime.resolve()
        environment.update(
            TEXMF="{" + str(runtime / "texmf-var") + "," + str(runtime / "texmf-config") + ",/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}",
            TEXMFVAR=str(runtime / "texmf-var"), TEXMFCONFIG=str(runtime / "texmf-config"),
            TEXMFHOME=str(runtime / "texmf-home"), TEXFORMATS=str(runtime / "texmf-var/web2c/xetex") + "//",
        )
    snapshots = output / "pages"
    snapshots.mkdir()
    originals = sorted((root / "pages").glob("MPL_136_047-094_136_scan*.tex"))
    if args.scans:
        requested = set(args.scans)
        originals = [path for path in originals
                     if int(re.search(r"scan(\d+)\.tex$", path.name).group(1)) in requested]
        present = {int(re.search(r"scan(\d+)\.tex$", path.name).group(1)) for path in originals}
        if present != requested:
            parser.error("Requested scan files are missing: " + str(sorted(requested - present)))
    manifest = {}
    for original in originals:
        data = original.read_bytes()
        (snapshots / original.name).write_bytes(data)
        manifest[original.name] = hashlib.sha256(data).hexdigest()
    (output / "sources.sha256").write_text("".join(f"{digest}  pages/{name}\n" for name, digest in manifest.items()))
    (output / "validation_preamble.tex").write_text(PREAMBLE, encoding="utf-8")
    (output / "run.txt").write_text(
        datetime.datetime.now(datetime.timezone.utc).isoformat() + "\nEngine: " + engine +
        "\nTransparent editorial macro definitions; syntax check only.\n", encoding="utf-8")

    def compile_one(original: Path) -> tuple[str, int, str]:
        name = original.stem + "_wrapper"
        wrapper = output / (name + ".tex")
        wrapper.write_text(PREAMBLE + "\\input{pages/" + original.name + "}\n\\end{document}\n", encoding="utf-8")
        command = [engine, "-interaction=nonstopmode", "-file-line-error", "-halt-on-error", "-no-shell-escape", wrapper.name]
        if Path(engine).name == "xelatex":
            command.insert(1, "-no-pdf")
        try:
            result = subprocess.run(command, cwd=output, env=environment, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True, timeout=90)
            code, transcript = result.returncode, result.stdout
        except subprocess.TimeoutExpired as error:
            code, transcript = 124, str(error)
        (output / (name + ".stdout.txt")).write_text(transcript, encoding="utf-8")
        return original.name, code, transcript

    failures = []
    report_lines = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(compile_one, originals))
    for name, code, transcript in results:
        if code == 0:
            report_lines.append("PASS " + name)
            continue
        failures.append(name)
        report_lines.append(f"FAIL {name} (exit {code})")
        lines = transcript.splitlines()
        positions = [i for i, line in enumerate(lines)
                     if re.search(r"(?:\.tex:\d+:|^!|^l\.\d+)", line)]
        if positions:
            included = set()
            for index in positions:
                for selected in range(max(0, index - 1), min(len(lines), index + 5)):
                    if selected not in included:
                        report_lines.append("  " + lines[selected])
                        included.add(selected)
        else:
            report_lines.extend("  " + line for line in lines[-12:])
    changed = [path.name for path in originals
               if hashlib.sha256(path.read_bytes()).hexdigest() != manifest[path.name]]
    report_lines.append(f"RESULT: {len(results) - len(failures)}/{len(results)} page snapshots compiled; {len(failures)} failed.")
    report_lines.append("Live pages changed since snapshot: " + (", ".join(changed) if changed else "none"))
    report = "\n".join(report_lines) + "\n"
    (output / "compile_report.txt").write_text(report, encoding="utf-8")
    print(report)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
