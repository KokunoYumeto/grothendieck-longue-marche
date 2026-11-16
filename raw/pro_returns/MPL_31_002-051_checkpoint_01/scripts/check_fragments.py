#!/usr/bin/env python3
"""Compile existing fragments without editing them or examining their meanings.

This temporary syntax wrapper uses pass-through state macros. It checks parsing,
not the final appearance of underlining, deletion, uncertainty, or marginalia.

The package directory defaults to the parent of scripts/. Compilation products
stay outside it, in an existing sibling _latex_check directory or a temporary
cache. --cache-dir chooses another external cache. --rebuild-format regenerates
the local format using the installed pdfLaTeX engine and TeX resource tree.
Required resources: article, fontenc, inputenc, AMS math/fonts, mathrsfs, TikZ,
tikz-cd, and geometry. --texmf-root supplies a TeX tree explicitly when needed.
"""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile

WORK = Path(__file__).resolve().parents[1]
PREFIX = "MPL_31_002-051_31_scan"
PREAMBLE = r"""\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,mathrsfs,tikz-cd}
\usepackage[margin=10mm,paperwidth=420mm,paperheight=594mm]{geometry}
\usetikzlibrary{arrows.meta,calc,decorations.pathmorphing,shapes.geometric}
\errorcontextlines=3
\hbadness=10000
\vbadness=10000
\hfuzz=1000pt
\vfuzz=1000pt
% Long pass-through definitions preserve nested math, text, and paragraphs.
\long\def\cotefile#1{#1}
\long\def\scanpage#1{\par #1\par}
\long\def\mspage#1{#1}
\long\def\deleted#1{#1}
\long\def\inserted#1{#1}
\long\def\margin#1{#1}
\long\def\uline#1{#1}
\long\def\uuline#1{#1}
\long\def\diagram#1{\begingroup\scantokens{#1}\endgroup}
\long\def\figure#1{#1}
\long\def\unsure#1{#1}
\long\def\illegible#1{\ifmmode\mbox{[illegible #1]}\else[illegible #1]\fi}
\begin{document}
"""


def environment(check, texmf_root):
    env = os.environ.copy()
    env.update(TEXMFVAR=str(check / "texmf-var"),
               TEXMFCONFIG=str(check / "texmf-config"),
               TEXMFCACHE=str(check / "texmf-cache"),
               max_print_line="10000")
    kpse = shutil.which("kpsewhich")
    if not kpse:
        raise RuntimeError("kpsewhich is required to locate the installed TeX resources")

    def locate(name):
        run = subprocess.run([kpse, name], env=env, capture_output=True, text=True, timeout=15)
        return run.stdout.strip()

    if texmf_root:
        env["TEXMF"] = str(texmf_root.resolve())
    elif not locate("article.cls"):
        # Some installed trees have no usable ls-R database. Searching the
        # reported tree without database-only !! restores normal lookup.
        dist = locate("--var-value=TEXMFDIST")
        if dist and Path(dist).is_dir():
            env["TEXMF"] = dist
    resources = {name: locate(name) for name in (
        "pdflatex.ini", "article.cls", "fontenc.sty", "inputenc.sty",
        "amsmath.sty", "amssymb.sty", "mathrsfs.sty", "tikz.sty",
        "tikz-cd.sty", "geometry.sty")}
    missing = [name for name, path in resources.items() if not path]
    if missing:
        raise RuntimeError("Required TeX resources are unavailable: " + ", ".join(missing))
    return env, resources


def ensure_format(check, env, engine, rebuild):
    directory = check / "formats"
    directory.mkdir(exist_ok=True)
    fmt = directory / "pdflatex.fmt"
    if rebuild and fmt.exists():
        fmt.unlink()
    if not fmt.is_file():
        result = subprocess.run(
            [engine, "-ini", "-etex", "-interaction=nonstopmode", "-halt-on-error",
             "-jobname=pdflatex", "-progname=pdflatex", "pdflatex.ini"],
            cwd=directory, env=env, capture_output=True, text=True, timeout=60)
        (check / "format-build.log").write_text(result.stdout + result.stderr, encoding="utf-8")
        if result.returncode:
            raise RuntimeError("Local format build failed; see format-build.log")
    return fmt


def compile_page(path, fmt, check, env, engine):
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    scan = int(re.search(r"scan(\d+)", path.name)[1])
    out = check / f"scan{scan:03d}"
    out.mkdir(exist_ok=True)
    wrapper = out / "check.tex"
    wrapper.write_text(PREAMBLE + "\\input{\\detokenize{" + str(path) + "}}\n\\end{document}\n", encoding="utf-8")
    cmd = [engine, "-fmt=" + str(fmt), "-no-shell-escape", "-draftmode",
           "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "check.tex"]
    try:
        run = subprocess.run(cmd, cwd=out, env=env, capture_output=True,
                             text=True, errors="replace", timeout=45)
        output, code = run.stdout + run.stderr, run.returncode
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or b"").decode(errors="replace") + (exc.stderr or b"").decode(errors="replace")
        output += "\nCompilation timed out after 45 seconds.\n"
        code = 124
    (out / "compiler-output.txt").write_text(output, encoding="utf-8")
    errors = []
    for line in output.splitlines():
        match = re.match(r"^(.+\.(?:tex|sty|cls)):(\d+):\s*(.*)$", line)
        if match:
            errors.append({"file": match[1], "line": int(match[2]), "message": match[3]})
        elif line.startswith("!"):
            errors.append({"message": line})
    after = hashlib.sha256(path.read_bytes()).hexdigest()
    return {"file": str(path), "scan": scan, "exit_code": code,
            "sha256_before": before, "sha256_after": after, "source_stable": before == after,
            "errors": errors, "compiler_output": str(out / "compiler-output.txt")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scans", nargs="*", type=int)
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--root", type=Path, default=WORK, help="Directory containing pages/; defaults to this package.")
    parser.add_argument("--cache-dir", type=Path, help="External directory for compiler products and logs.")
    parser.add_argument("--texmf-root", type=Path, help="Optional installed TeX resource tree.")
    parser.add_argument("--rebuild-format", action="store_true", help="Regenerate the temporary pdfLaTeX format.")
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be positive")
    root = args.root.resolve()
    existing = root.parent / "_latex_check"
    check = (args.cache_dir or (existing if existing.is_dir() else
             Path(tempfile.gettempdir()) / ("MPL_31_002-051_latex_" + hashlib.sha256(str(root).encode()).hexdigest()[:12]))).resolve()
    if check == root or root in check.parents:
        parser.error("--cache-dir must be outside the deliverable package")
    check.mkdir(parents=True, exist_ok=True)
    engine = shutil.which("pdflatex")
    if not engine:
        parser.error("pdflatex is unavailable; install a TeX distribution before running this checker")
    paths = sorted((root / "pages").glob(PREFIX + "*.tex"))
    if args.scans:
        paths = [p for p in paths if int(re.search(r"scan(\d+)", p.name)[1]) in args.scans]
        absent = sorted(set(args.scans) - {int(re.search(r"scan(\d+)", p.name)[1]) for p in paths})
        if absent:
            parser.error("Requested page files are absent: " + ", ".join(f"{n:03d}" for n in absent))
    if not paths:
        parser.error("No page fragments were found")
    env, resources = environment(check, args.texmf_root)
    fmt = ensure_format(check, env, engine, args.rebuild_format)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda p: compile_page(p.resolve(), fmt, check, env, engine), paths))
    report = {"purpose": "Temporary mechanical LaTeX syntax check; no visual or reading certification.",
              "engine": engine, "format": str(fmt), "root": str(root),
              "cache": str(check), "resources": resources,
              "results": results, "compiled": len(results),
              "passed": sum(r["exit_code"] == 0 and r["source_stable"] for r in results)}
    (check / "latest-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["passed"] == report["compiled"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
