#!/usr/bin/env python3
"""Compile saved fragments in an isolated, temporary XeLaTeX harness.

Sources are copied as compiler input and never edited.  The program does not
inspect images, open context material, or evaluate manuscript readings.  Custom
editorial macros are transparent wrappers: this is a syntax check, not a
typographic or diplomatic rendering check.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


PREFIX = "MPL_43_094-142"
PACKAGES = [
    "fontspec", "amsmath", "amssymb", "mathtools", "mathrsfs", "tikz-cd",
    "bm", "array", "xcolor", "cancel",
]
PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[no-math]{fontspec}
\usepackage{amsmath,amssymb,mathtools,mathrsfs,tikz-cd,bm,array,xcolor,cancel}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathmorphing,decorations.markings,decorations.pathreplacing,patterns,fit,shapes.geometric}
\errorcontextlines=12
\tracinglostchars=3
\setlength{\textwidth}{170mm}
\setlength{\textheight}{245mm}
\setlength{\oddsidemargin}{-5mm}
\setlength{\topmargin}{-15mm}
\long\def\cotefile#1{\typeout{MPL-COTE:#1}}
\long\def\scanpage#1{\par\clearpage\typeout{MPL-SCAN:#1 SOURCE-LINE:\the\inputlineno}}
\long\def\mspage#1{{#1}}
\long\def\deleted#1{{#1}}
\long\def\inserted#1{{#1}}
\long\def\margin#1{{#1}}
\long\def\uline#1{{#1}}
\long\def\uuline#1{{#1}}
% The declared diagram macro accepts both tikz-cd and a bare array table.
% Supply math mode locally for a bare array, while preserving an array that
% already occurs inside explicit math delimiters.
\let\MPLoriginalarray\array
\let\MPLoriginalendarray\endarray
\def\MPLdiagramarray{\ifmmode\def\MPLarraycloser{}\else\(\def\MPLarraycloser{\)}\fi\MPLoriginalarray}
\def\MPLdiagramendarray{\MPLoriginalendarray\MPLarraycloser}
\long\def\diagram#1{{\let\array\MPLdiagramarray\let\endarray\MPLdiagramendarray#1}}
\long\def\figure#1{{#1}}
\long\def\unsure#1{{#1}}
\long\def\illegible#1{\ifmmode\text{[illegible #1]}\else[illegible #1]\fi}
% Captured editorial arguments must retain an active ampersand for TikZ
% matrices.  Outside a TikZ matrix its meaning is the ordinary alignment tab.
% This also permits array/tabular bodies inside the same editorial macros.
\let\MPLalignmenttab=&
\catcode`\&=13
\let&\MPLalignmenttab
\begin{document}
"""
PREFLIGHT = r"""\scanpage{000}
Synthetic compiler fixture. \[x\xrightarrow{a}y\]
\deleted{\diagram{\begin{tikzcd} A \arrow[r,"\unsure{a|b}"] \arrow[d] & B \arrow[d] \\ C \arrow[r] & D \end{tikzcd}}}
\diagram{$\begin{array}{cc} a & b \\ c & d \end{array}$}
\diagram{\begin{array}{cc} a & b \\ c & d \end{array}}
\figure{\begin{tikzpicture}\draw[->] (0,0) -- (1,1);\end{tikzpicture}}
"""


def run(command: list[str], directory: Path, environment: dict[str, str], stem: str) -> dict:
    try:
        process = subprocess.run(
            command, cwd=directory, env=environment, capture_output=True,
            text=True, errors="replace", timeout=60,
        )
        stdout, stderr, code = process.stdout, process.stderr, process.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", "replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", "replace")
        code = 124
        stderr += "\nCompiler process exceeded its 60-second limit.\n"
    (directory / (stem + ".stdout.txt")).write_text(stdout, encoding="utf-8")
    (directory / (stem + ".stderr.txt")).write_text(stderr, encoding="utf-8")
    return {"exit_code": code, "stdout": stdout, "stderr": stderr}


def lookup(name: str, environment: dict[str, str]) -> str | None:
    process = subprocess.run(["kpsewhich", name], env=environment, capture_output=True, text=True)
    return process.stdout.strip() if process.returncode == 0 else None


def compiler_diagnostics(result: dict, log_path: Path) -> dict:
    output = result["stdout"]
    log = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else output
    errors = []
    scans = []
    scan = None
    marker_line = None
    lines = output.splitlines()
    for index, line in enumerate(lines):
        marker = re.search(r"MPL-SCAN:(\d+) SOURCE-LINE:(\d+)", line)
        if marker:
            scan, marker_line = int(marker.group(1)), int(marker.group(2))
            scans.append(scan)
        located = re.match(r"(.+\.tex):(\d+):\s*(.+)", line)
        if located:
            filename, lineno, message = located.groups()
            errors.append({
                "scan": scan, "compiler_file": filename,
                "compiler_line": int(lineno), "scan_marker_line": marker_line,
                "message": message,
                "compiler_context": "\n".join(lines[index + 1:index + 9]),
            })
        elif line.startswith("!"):
            errors.append({
                "scan": scan, "message": line.lstrip("! "),
                "compiler_context": "\n".join(lines[index + 1:index + 9]),
            })
    if result["exit_code"] and not errors:
        errors.append({"scan": scan, "message": "Compiler did not complete.", "compiler_context": (output + result["stderr"])[-3000:]})
    missing_glyphs = sorted(set(re.findall(r"^Missing character: .+$", log, re.MULTILINE)))
    missing_glyph_locations = []
    current_scan = None
    for number, line in enumerate(log.splitlines(), 1):
        marker = re.search(r"MPL-SCAN:(\d+) SOURCE-LINE:(\d+)", line)
        if marker:
            current_scan = int(marker.group(1))
        if line.startswith("Missing character:"):
            missing_glyph_locations.append({"scan": current_scan, "log_line": number, "message": line})
    return {
        "passed": result["exit_code"] == 0,
        "exit_code": result["exit_code"],
        "scans_reached": scans,
        "errors": errors,
        "missing_glyphs": missing_glyphs,
        "missing_glyph_locations": missing_glyph_locations,
        "overfull_box_warnings": len(re.findall(r"Overfull \\[hv]box", log)),
        "underfull_box_warnings": len(re.findall(r"Underfull \\[hv]box", log)),
        "log_path": str(log_path),
    }


def compile_input(source: Path, directory: Path, environment: dict[str, str], engine: str) -> dict:
    directory.mkdir(parents=True, exist_ok=True)
    wrapper = directory / "harness.tex"
    wrapper.write_text(
        PREAMBLE + "\\input{\\detokenize{" + source.as_posix() + "}}\n\\end{document}\n",
        encoding="utf-8",
    )
    result = run([
        engine, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
        "-no-shell-escape", "harness.tex",
    ], directory, environment, "compiler")
    return compiler_diagnostics(result, directory / "harness.log")


def snapshot(path: Path, target: Path) -> dict:
    data = path.read_bytes()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return {"source": str(path), "snapshot": str(target), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--work-dir", type=Path, help="New compiler work directory, outside the deliverable; otherwise use a new temporary directory.")
    parser.add_argument("--report", type=Path, help="Also save the JSON report here.")
    parser.add_argument("--combined-only", action="store_true", help="Do not isolate failures by compiling each saved page separately.")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if args.work_dir is None:
        work = Path(tempfile.mkdtemp(prefix="mpl-tex-check-"))
    else:
        work = args.work_dir.resolve()
        if work == root or root in work.parents:
            parser.error("Compiler output must be outside the deliverable directory.")
        work.mkdir(parents=True, exist_ok=False)
    report = {
        "checked_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "root": str(root), "work_directory": str(work), "ok": False,
        "limitations": [
            "This checks TeX execution and syntax, not handwriting readings or visual completeness.",
            "Editorial macros retain their contents without editorial decoration in this temporary harness.",
            "Layout warnings reflect the temporary harness; its PDF is not a deliverable.",
            "Each input is a snapshot; later source changes are outside this run.",
        ],
    }

    def finish(code: int) -> int:
        serialized = json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        (work / "report.json").write_text(serialized, encoding="utf-8")
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(serialized, encoding="utf-8")
        print(serialized, end="")
        return code

    engine = shutil.which("xelatex")
    if engine is None or shutil.which("kpsewhich") is None or shutil.which("xetex") is None:
        report["environment_error"] = "XeLaTeX, XeTeX, and kpsewhich must be installed."
        return finish(2)
    report["engine"] = engine
    environment = os.environ.copy()
    environment.update({
        "TEXMFVAR": str(work / "texmf-var"),
        "TEXMFCONFIG": str(work / "texmf-config"),
        "TEXMFCACHE": str(work / "texmf-var"),
        "VARTEXFONTS": str(work / "texfonts"),
        "TEXFORMATS": str(work / "formats") + "//:",
        "max_print_line": "1000", "error_line": "254", "half_error_line": "238",
    })
    adjustments = []
    if lookup("article.cls", environment) is None:
        configured = subprocess.run(["kpsewhich", "--var-value=TEXMF"], env=environment, capture_output=True, text=True)
        if configured.returncode == 0 and configured.stdout.strip():
            environment["TEXMF"] = configured.stdout.strip().replace("!!", "")
            adjustments.append("Allowed direct directory lookup in the installed TeX trees because their filename databases were absent.")
    report["environment_adjustments"] = adjustments
    packages = {package: lookup(package + ".sty", environment) for package in PACKAGES}
    report["packages"] = packages
    missing = [name for name, location in packages.items() if location is None]
    if missing:
        report["environment_error"] = "Required harness packages are unavailable: " + ", ".join(missing)
        return finish(2)
    if lookup("xelatex.fmt", environment) is None:
        formats = work / "formats"
        formats.mkdir()
        built = run([
            shutil.which("xetex"), "-ini", "-etex", "-jobname=xelatex",
            "-interaction=nonstopmode", "-halt-on-error", "-no-shell-escape", "xelatex.ini",
        ], formats, environment, "format")
        if built["exit_code"]:
            report["environment_error"] = "The local XeLaTeX format could not be generated."
            report["format_diagnostics"] = compiler_diagnostics(built, formats / "xelatex.log")
            return finish(2)
        adjustments.append("Generated the missing XeLaTeX format inside the temporary work directory.")
    preflight_source = work / "synthetic_preflight.tex"
    preflight_source.write_text(PREFLIGHT, encoding="utf-8")
    preflight = compile_input(preflight_source, work / "preflight", environment, engine)
    report["preflight"] = preflight
    if not preflight["passed"]:
        report["environment_error"] = "The synthetic harness preflight failed; no manuscript compiler diagnosis is claimed."
        return finish(2)
    combined = root / (PREFIX + "_transcription.tex")
    if not combined.is_file():
        report["input_error"] = "The combined transcription does not yet exist."
        return finish(2)
    inputs = work / "inputs"
    report["combined_snapshot"] = snapshot(combined, inputs / combined.name)
    page_paths = sorted((root / "pages").glob(PREFIX + "_43_scan[0-9][0-9][0-9].tex"))
    page_snapshots = [snapshot(path, inputs / "pages" / path.name) for path in page_paths]
    report["page_snapshots"] = page_snapshots
    report["combined"] = compile_input(inputs / combined.name, work / "combined", environment, engine)
    report["isolated_page_failures"] = []
    if not report["combined"]["passed"] and not args.combined_only:
        passed = []
        for item in page_snapshots:
            path = Path(item["snapshot"])
            result = compile_input(path, work / "isolated" / path.stem, environment, engine)
            result["page_file"] = path.name
            if result["passed"]:
                passed.append(path.name)
            else:
                report["isolated_page_failures"].append(result)
        report["isolated_pages_passed"] = passed
    report["ok"] = report["combined"]["passed"]
    return finish(0 if report["ok"] else 1)


if __name__ == "__main__":
    sys.exit(main())
