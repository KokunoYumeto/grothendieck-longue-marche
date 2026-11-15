#!/usr/bin/env python3
"""Mechanically compile a fresh snapshot of all page fragments, read-only.

No image/context reading or interpretation is performed. TeX output is temporary.
The editorial macros pass their contents through without semantic alteration.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

PREFIX = "MPL_33_098-146"
PREAMBLE = r"""\documentclass{article}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage{amsmath,amssymb,mathtools,mathrsfs,bm}
\usepackage{graphicx}
\usepackage{tikz,tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,decorations.markings,calc,patterns,positioning}
\paperwidth=17in
\paperheight=22in
\textwidth=15in
\textheight=20in
\oddsidemargin=0pt
\evensidemargin=0pt
\topmargin=-30pt
\errorcontextlines=8
\long\def\cotefile#1{\par\noindent Cote #1\par}
\long\def\scanpage#1{\clearpage\noindent Scan #1\par}
\long\def\mspage#1{#1}
% Do not pre-tokenize the brace contents: TikZ matrices require their own
% active-ampersand catcode setup while reading cells from the input stream.
\let\deleted\relax
\let\inserted\relax
\let\margin\relax
\let\uline\relax
\let\uuline\relax
\let\diagram\relax
\let\figure\relax
\let\unsure\relax
\long\def\illegible#1{\ifmmode\text{[illegible #1]}\else[illegible #1]\fi}
\begin{document}
"""


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def run_engine(source: Path, temp: Path, env: dict[str, str]) -> dict:
    result = subprocess.run(
        ["xelatex", "-fmt=" + str(temp / "xelatex.fmt"), "-interaction=nonstopmode",
         "-halt-on-error", "-file-line-error", "-no-shell-escape", source.name],
        cwd=source.parent, env=env, capture_output=True, text=True, timeout=90,
    )
    stdout = result.stdout + result.stderr
    source.with_suffix(".stdout.txt").write_text(stdout, encoding="utf-8")
    error_lines = []
    for line in stdout.splitlines():
        match = re.match(r"(.+?\.tex):(\d+):\s*(.*)", line)
        if match:
            error_lines.append({"compiler_file": match.group(1), "compiler_line": int(match.group(2)),
                                "message": match.group(3)})
    return {"returncode": result.returncode, "errors": error_lines,
            "stdout_path": str(source.with_suffix(".stdout.txt")),
            "log_path": str(source.with_suffix(".log"))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--temp", type=Path,
                        default=Path("/workspace/scratch/ef44ae13eff0/MPL_33_098-146_compile_tmp"))
    parser.add_argument("--isolate", action="store_true",
                        help="if joined compilation fails, also compile every page separately")
    args = parser.parse_args()
    base, temp = args.work.resolve(), args.temp.resolve()
    temp.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    # The image contains TeX package files but no ls-R database or prebuilt
    # formats. Remove the database-only !! search convention for this process.
    env["TEXMF"] = "{/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}"
    env["TEXMFVAR"] = str(temp / "texmf-var")
    env["TEXMFCONFIG"] = str(temp / "texmf-config")
    env["max_print_line"] = "1000"
    if not (temp / "xelatex.fmt").exists():
        result = subprocess.run(
            ["xelatex", "-ini", "-etex", "-interaction=nonstopmode", "-halt-on-error",
             "-jobname=xelatex", "xelatex.ini"], cwd=temp, env=env,
            capture_output=True, text=True, timeout=90)
        (temp / "format-build.stdout.txt").write_text(result.stdout + result.stderr, encoding="utf-8")
        if result.returncode:
            print("ENVIRONMENT ERROR: could not build temporary XeLaTeX format; see", temp / "format-build.stdout.txt")
            return 2

    pages = []
    source_map: dict[int, dict] = {}
    joined_lines: list[str] = []
    for scan in range(98, 147):
        path = base / "pages" / f"{PREFIX}_33_scan{scan:03}.tex"
        data = path.read_bytes()
        text = data.decode("utf-8")
        pages.append({"scan": scan, "path": path, "text": text,
                      "sha256": hashlib.sha256(data).hexdigest()})
        for index, line in enumerate(text.splitlines(), 1):
            source_map[len(joined_lines) + 1] = {"file": str(path.relative_to(base)), "line": index}
            joined_lines.append(line)
        joined_lines.append("")
    (temp / "joined.tex").write_text("\n".join(joined_lines) + "\n", encoding="utf-8")
    (temp / "source_map.json").write_text(json.dumps(source_map, indent=2) + "\n", encoding="utf-8")
    harness = temp / "harness.tex"
    harness.write_text(PREAMBLE + "\\input{joined.tex}\n\\end{document}\n", encoding="utf-8")
    report = {"time_utc": utc(), "engine": "XeLaTeX", "snapshot_pages": len(pages),
              "paleographic_review": False, "editorial_macros": "pass-through (both uncertainty alternatives retained)",
              "temporary_directory": str(temp),
              "page_sha256": {str(p["path"].relative_to(base)): p["sha256"] for p in pages}}
    combined = run_engine(harness, temp, env)
    for error in combined["errors"]:
        if Path(error["compiler_file"]).name == "joined.tex":
            error.update(source_map.get(error["compiler_line"], {}))
    report["joined_compile"] = combined

    isolated = []
    if args.isolate and combined["returncode"]:
        def compile_page(page: dict) -> dict:
            directory = temp / f"scan{page['scan']:03}"
            directory.mkdir(exist_ok=True)
            (directory / "page.tex").write_text(page["text"], encoding="utf-8")
            source = directory / "harness.tex"
            source.write_text(PREAMBLE + "\\input{page.tex}\n\\end{document}\n", encoding="utf-8")
            result = run_engine(source, temp, env)
            result["scan"] = page["scan"]
            result["source_file"] = str(page["path"].relative_to(base))
            for error in result["errors"]:
                if Path(error["compiler_file"]).name == "page.tex":
                    error.update({"file": result["source_file"], "line": error["compiler_line"]})
            return result
        with ThreadPoolExecutor(max_workers=4) as executor:
            isolated = list(executor.map(compile_page, pages))
        report["isolated_compiles"] = isolated

    report["source_files_unchanged_during_check"] = all(
        hashlib.sha256(page["path"].read_bytes()).hexdigest() == page["sha256"] for page in pages)
    record_path = base / "records" / "latex_compile_validation.json"
    record_path.parent.mkdir(exist_ok=True)
    record_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("Joined compilation return code:", combined["returncode"])
    for error in combined["errors"]:
        print("JOINED:", error.get("file", error["compiler_file"]),
              "line", error.get("line", error["compiler_line"]), error["message"])
    if isolated:
        failed = [item for item in isolated if item["returncode"]]
        print(f"Isolated page compiles: {len(isolated)-len(failed)}/{len(isolated)} successful")
        for item in failed:
            if not item["errors"]:
                print("FAILED WITHOUT PARSED TEX LOCATION:", item["source_file"], item["stdout_path"])
            for error in item["errors"]:
                print("PAGE:", error.get("file", error["compiler_file"]),
                      "line", error.get("line", error["compiler_line"]), error["message"])
    print("Original page files unchanged during check:", report["source_files_unchanged_during_check"])
    print("Mechanical validation record:", record_path)
    print("This compilation does not establish transcription accuracy or editorial rendering quality.")
    return 1 if combined["returncode"] else 0


if __name__ == "__main__":
    sys.exit(main())
