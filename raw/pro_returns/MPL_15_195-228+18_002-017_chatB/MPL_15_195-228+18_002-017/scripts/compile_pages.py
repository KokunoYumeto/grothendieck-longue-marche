#!/usr/bin/env python3
"""Compile saved transcription fragments with neutral, temporary macro wrappers.

This is a mechanical syntax/environment check, not a transcription audit or a
publication rendering. Required editorial macros retain their arguments without
styling. Page files and the combined fragment are never modified. All TeX input
copies, wrappers, formats, PDFs, and engine logs go to a scratch directory outside
the deliverable package; only a concise JSON report is saved in records/.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
from validate_package import EXPECTED, PREFIX, mask_tex, page_name


WRAPPER = r"""\documentclass[10pt]{article}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage[a4paper,margin=20mm]{geometry}
\usepackage{amsmath,amssymb,graphicx}
\usepackage{tikz,tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathreplacing,decorations.pathmorphing,calc,shapes.geometric}
\newcommand{\cotefile}[1]{}
\newcommand{\scanpage}[1]{}
\newcommand{\mspage}[1]{}
% These empty commands leave the following brace group to TeX. They do not
% pre-tokenize matrix ampersands as a conventional #1 identity macro would.
\newcommand{\deleted}{}
\newcommand{\inserted}{}
\newcommand{\margin}{}
\newcommand{\uline}{}
\newcommand{\uuline}{}
\newcommand{\diagram}{}
\renewcommand{\figure}{}
\newcommand{\unsure}{}
\newcommand{\illegible}[1]{[illegible #1]}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\begin{document}
\input{fragment.tex}
\end{document}
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def find_tex(name: str, environment: dict) -> str | None:
    result = subprocess.run(["kpsewhich", name], capture_output=True, text=True,
                            env=environment, timeout=20)
    return result.stdout.strip() if result.returncode == 0 else None


def prepare_engine(work: Path) -> tuple[dict, dict]:
    """Keep format/cache setup local, including installs lacking a TeX database."""
    if not shutil.which("xelatex") or not shutil.which("kpsewhich"):
        raise RuntimeError("xelatex and kpsewhich must be installed")
    environment = os.environ.copy()
    for variable, subdirectory in [
        ("TEXMFVAR", "texmf-var"), ("TEXMFCONFIG", "texmf-config"),
        ("TEXMFCACHE", "texmf-cache"),
    ]:
        target = work / subdirectory
        target.mkdir(parents=True, exist_ok=True)
        environment[variable] = str(target)
    formats = work / "formats"
    formats.mkdir(parents=True, exist_ok=True)
    environment["TEXFORMATS"] = str(formats) + "//:"
    fallback_used = False
    if not find_tex("article.cls", environment):
        roots = [str(work / "texmf-var")]
        for candidate in ["/usr/share/texmf", "/usr/local/share/texmf",
                          "/usr/share/texlive/texmf-dist", "/etc/texmf"]:
            if Path(candidate).is_dir():
                roots.append(candidate)
        environment["TEXMF"] = "{" + ",".join(roots) + "}"
        fallback_used = True
    packages = {}
    for name in ["article.cls", "fontspec.sty", "geometry.sty", "amsmath.sty",
                 "amssymb.sty", "graphicx.sty", "tikz.sty", "tikz-cd.sty"]:
        packages[name] = find_tex(name, environment)
        if not packages[name]:
            raise RuntimeError(f"Required TeX file unavailable: {name}")
    format_path = find_tex("xelatex.fmt", environment)
    format_built = False
    if not format_path:
        result = subprocess.run(
            ["xelatex", "-ini", "-etex", "-interaction=nonstopmode", "-halt-on-error",
             "-no-shell-escape", "-jobname=xelatex", "xelatex.ini"],
            cwd=formats, env=environment, capture_output=True, text=True, timeout=60,
        )
        (work / "format_build_output.txt").write_text(result.stdout + result.stderr, encoding="utf-8")
        if result.returncode:
            raise RuntimeError("XeLaTeX format preparation failed; inspect scratch format_build_output.txt")
        format_path = find_tex("xelatex.fmt", environment)
        if not format_path:
            raise RuntimeError("XeLaTeX format was built but cannot be resolved")
        format_built = True
    (work / "wrapper_template.tex").write_text(WRAPPER, encoding="utf-8")
    return environment, {
        "engine": "xelatex", "format": format_path, "format_built": format_built,
        "filesystem_search_fallback": fallback_used, "packages": packages,
        "wrapper_template": str(work / "wrapper_template.tex"),
        "wrapper_policy": "Editorial wrappers retain arguments without styling; page/cote markers are omitted.",
    }


def diagnostics(output: str) -> list[dict]:
    found = []
    lines = output.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^(.*?\.tex):(\d+):\s*(.*)$", line)
        if match:
            found.append({"tex_file": match.group(1), "tex_line": int(match.group(2)),
                          "message": match.group(3).strip(),
                          "context": "\n".join(lines[index + 1:index + 5]).strip()[:600]})
        elif line.startswith("!"):
            found.append({"message": line[1:].strip(),
                          "context": "\n".join(lines[index + 1:index + 5]).strip()[:600]})
    return found


def compile_one(root: Path, work: Path, environment: dict, key: tuple[int, int], timeout: int) -> dict:
    cote, scan = key
    source = root / "pages" / page_name(cote, scan)
    data = source.read_bytes()
    text = data.decode("utf-8")
    destination = work / f"cote{cote}_scan{scan:03d}"
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "fragment.tex").write_bytes(data)
    (destination / "wrapper.tex").write_text(WRAPPER, encoding="utf-8")
    started = time.monotonic()
    timed_out = False
    try:
        result = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
             "-no-shell-escape", "wrapper.tex"], cwd=destination, env=environment,
            text=True, errors="replace", capture_output=True, timeout=timeout,
        )
        output = result.stdout + result.stderr
        code = result.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        stdout = exc.stdout.decode("utf-8", errors="replace") if isinstance(exc.stdout, bytes) else exc.stdout or ""
        stderr = exc.stderr.decode("utf-8", errors="replace") if isinstance(exc.stderr, bytes) else exc.stderr or ""
        output = stdout + stderr
        code = None
    (destination / "engine_output.txt").write_text(output, encoding="utf-8")
    current_hash = digest(source.read_bytes())
    original_hash = digest(data)
    masked = mask_tex(text)
    return {
        "cote": cote, "scan": scan, "file": str(source.relative_to(root)),
        "source_sha256": original_hash,
        "source_changed_during_compile": current_hash != original_hash,
        "exit_code": code, "timed_out": timed_out,
        "syntax_compile_passed": code == 0 and not timed_out,
        "seconds": round(time.monotonic() - started, 3),
        "diagnostics": diagnostics(output),
        "missing_character_messages": [line.strip() for line in output.splitlines()
                                       if line.startswith("Missing character:")],
        "overfull_box_count": output.count("Overfull \\hbox") + output.count("Overfull \\vbox"),
        "underfull_box_count": output.count("Underfull \\hbox") + output.count("Underfull \\vbox"),
        "commands": sorted(set(re.findall(r"\\([A-Za-z]+)", masked))),
        "environments": sorted(set(re.findall(r"\\begin\s*\{([^}]+)\}", masked))),
        "scratch_directory": str(destination),
    }


def page_argument(value: str) -> tuple[int, int]:
    try:
        cote, scan = value.split(":")
        key = int(cote), int(scan)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use COTE:SCAN, for example 15:195 or 18:006") from exc
    if key not in EXPECTED:
        raise argparse.ArgumentTypeError("Page is outside this package")
    return key


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--work", type=Path, help="Scratch directory outside the deliverable root.")
    parser.add_argument("--page", type=page_argument, action="append", dest="pages",
                        help="Compile one specified page; repeat for several. Default: all saved pages.")
    parser.add_argument("--jobs", type=int, default=4, help="Independent compiler processes, default 4.")
    parser.add_argument("--timeout", type=int, default=45, help="Per-page compiler timeout in seconds.")
    parser.add_argument("--report", type=Path, help="JSON report path; default records/latex_check_report.json.")
    args = parser.parse_args()
    root = args.root.resolve()
    work = (args.work or root.parent / "latex_check").resolve()
    if work == root or root in work.parents:
        parser.error("--work must be outside the deliverable root")
    work.mkdir(parents=True, exist_ok=True)
    report_path = args.report or root / "records" / "latex_check_report.json"
    keys = ([key for key in EXPECTED if key in set(args.pages)] if args.pages
            else [key for key in EXPECTED if (root / "pages" / page_name(*key)).is_file()])
    started = utc_now()
    try:
        environment, preparation = prepare_engine(work)
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
            futures = [pool.submit(compile_one, root, work, environment, key, args.timeout) for key in keys]
            pages = [future.result() for future in futures]
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as exc:
        report = {"scope": "Mechanical compile check", "started_utc": started,
                  "finished_utc": utc_now(), "setup_or_execution_error": str(exc),
                  "scratch_directory": str(work), "page_files_modified": False}
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 2
    failures = [page for page in pages if not page["syntax_compile_passed"]]
    changed = [page["file"] for page in pages if page["source_changed_during_compile"]]
    report = {
        "package": PREFIX, "started_utc": started, "finished_utc": utc_now(),
        "scope": "Mechanical syntax/environment compilation only; no visual, textual, or mathematical audit.",
        "preparation": preparation, "page_count": len(pages),
        "passed_count": len(pages) - len(failures), "failed_count": len(failures),
        "source_files_changed_during_compile": changed,
        "all_compiled_snapshots_passed": not failures and bool(pages),
        "page_files_modified_by_checker": False, "pages": pages,
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {
        "report": str(report_path), "page_count": len(pages),
        "passed_count": report["passed_count"], "failed_count": report["failed_count"],
        "source_files_changed_during_compile": changed,
        "failures": [{"file": page["file"], "diagnostics": page["diagnostics"],
                      "timed_out": page["timed_out"]} for page in failures],
        "missing_character_pages": [page["file"] for page in pages if page["missing_character_messages"]],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if failures or changed or not pages else 0


if __name__ == "__main__":
    raise SystemExit(main())
