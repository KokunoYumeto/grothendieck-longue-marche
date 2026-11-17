#!/usr/bin/env python3
"""Compile independent page snapshots with neutral definitions of state macros.

This is a syntax check only. It does not reproduce the intended editorial
appearance, and it cannot assess readings or visual completeness. Inputs are
copied into a separate scratch directory; page files are never modified.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


PACKAGE = "MPL_136_282-327"
PREAMBLE = r"""\documentclass[a4paper,10pt]{article}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,mathrsfs,graphicx}
\usepackage{tikz-cd}
\usetikzlibrary{arrows.meta,decorations.markings,patterns,calc,positioning}
\newcommand{\cotefile}[1]{\par\noindent Cote #1\par}
\newcommand{\scanpage}[1]{\par\noindent Scan #1\par}
\newcommand{\mspage}[1]{\par\noindent #1\par}
\newcommand{\deleted}[1]{#1}
\newcommand{\inserted}[1]{#1}
\newcommand{\margin}[1]{#1}
\newcommand{\uline}[1]{#1}
\newcommand{\uuline}[1]{#1}
\newcommand{\diagram}[1]{#1}
\renewcommand{\figure}[1]{#1}
\newcommand{\unsure}[1]{#1}
\newcommand{\illegible}[1]{\ifmmode\text{[illegible #1]}\else[illegible #1]\fi}
\begin{document}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--scratch", type=Path,
                        default=Path(__file__).resolve().parent.parent.parent / "tex_syntax_checks")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    root = args.root.resolve()
    scratch = args.scratch.resolve()
    engine = shutil.which("xelatex")
    if not engine:
        raise SystemExit("xelatex is unavailable")
    required = ("xelatex.fmt", "fontspec.sty", "amsmath.sty", "amssymb.sty",
                "mathrsfs.sty", "graphicx.sty", "tikz-cd.sty")
    unavailable = []
    for resource in required:
        lookup = subprocess.run(["kpsewhich", resource], capture_output=True, text=True)
        if lookup.returncode != 0 or not lookup.stdout.strip():
            unavailable.append(resource)
    if unavailable:
        destination = root / "records" / "tex_compile_environment.txt"
        destination.parent.mkdir(parents=True, exist_ok=True)
        message = ("No page could be compiled: the TeX binary is present but required "
                   "runtime files are absent.\nMissing: " + ", ".join(unavailable) +
                   "\nThese are environment failures, not page syntax findings.\n")
        destination.write_text(message, encoding="utf-8")
        print(message, end="")
        return 2
    sources = sorted((root / "pages").glob(f"{PACKAGE}_136_scan*.tex"))

    def one(source: Path) -> dict[str, str | int]:
        scan = int(re.search(r"scan(\d+)\.tex$", source.name).group(1))
        run = scratch / str(scan)
        run.mkdir(parents=True, exist_ok=True)
        data = source.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        snapshot = run / source.name
        snapshot.write_bytes(data)
        harness = run / "harness.tex"
        harness.write_text(PREAMBLE + r"\input{" + source.name + "}\n" +
                           r"\end{document}" + "\n", encoding="utf-8")
        try:
            result = subprocess.run(
                [engine, "-no-shell-escape", "-interaction=nonstopmode", "-file-line-error",
                 "-halt-on-error", "harness.tex"], cwd=run, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True, timeout=60)
            (run / "console.txt").write_text(result.stdout, encoding="utf-8")
            lines = result.stdout.splitlines()
            errors = [line for line in lines if
                      re.search(r"(?:\.tex:\d+:|^!).*", line)]
            first = errors[0] if errors else ("" if result.returncode == 0 else lines[-1])
            return {"scan": scan, "source_sha256": digest,
                    "exit_code": result.returncode, "first_error": first,
                    "scratch_directory": str(run)}
        except subprocess.TimeoutExpired:
            return {"scan": scan, "source_sha256": digest, "exit_code": 124,
                    "first_error": "compile timeout (60 seconds)",
                    "scratch_directory": str(run)}

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        rows = list(pool.map(one, sources))
    destination = root / "records" / "tex_compile_summary.csv"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=(
            "scan", "source_sha256", "exit_code", "first_error", "scratch_directory"))
        writer.writeheader()
        writer.writerows(rows)
    failures = [row for row in rows if row["exit_code"] != 0]
    print(f"Compiled {len(rows)} independent snapshots; failures: {len(failures)}")
    for row in failures:
        print(f"scan {row['scan']}: {row['first_error']}")
    print(f"Summary: {destination}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
