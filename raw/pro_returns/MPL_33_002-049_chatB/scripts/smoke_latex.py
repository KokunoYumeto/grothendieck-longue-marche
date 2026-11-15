#!/usr/bin/env python3
"""Compile the manuscript fragments with neutral editorial macro definitions.

This is a syntax smoke test only. It neither reads source images nor edits any
page, the combined fragment, inventory, or progress log. Its rendering is not
an edition and does not reproduce deletion/uncertainty styling.
"""
from __future__ import annotations
import hashlib
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "records" / "latex_smoke"
PAGES = sorted((ROOT / "pages").glob("MPL_33_002-049_33_scan*.tex"))


def hashes():
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in PAGES}


def main():
    engine = shutil.which("xelatex")
    if not engine:
        raise SystemExit("No Unicode LaTeX engine found.")
    OUT.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.update(TEXMF="{/usr/share/texmf,/usr/share/texlive/texmf-dist}",
               TEXINPUTS=".:/usr/share/texmf/tex//:/usr/share/texlive/texmf-dist/tex//:",
               TFMFONTS="/usr/share/texmf/fonts/tfm//:/usr/share/texlive/texmf-dist/fonts/tfm//:",
               OPENTYPEFONTS="/usr/share/texmf/fonts/opentype//:/usr/share/texlive/texmf-dist/fonts/opentype//:",
               TEXFORMATS=str(OUT) + ":")
    if not (OUT / "xelatex.fmt").exists():
        fmt = subprocess.run([engine, "-ini", "-etex", "-interaction=nonstopmode",
                              "-jobname=xelatex", "-progname=xelatex", "xelatex.ini"],
                             cwd=OUT, env=env, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True, timeout=120)
        (OUT / "format_build_output.txt").write_text(fmt.stdout, encoding="utf-8")
        if fmt.returncode:
            raise SystemExit("Local XeLaTeX format build failed; see format_build_output.txt")
    before = hashes()
    macros = ("cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
              "uline", "uuline", "diagram", "figure", "unsure", "illegible")
    preamble = r"""\documentclass{article}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,mathtools,mathrsfs,graphicx,xcolor}
\usepackage{tikz-cd}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathmorphing}
\setlength{\textwidth}{170mm}
\setlength{\textheight}{250mm}
\setlength{\oddsidemargin}{-5mm}
\setlength{\topmargin}{-20mm}
\setlength{\headheight}{0pt}
\setlength{\headsep}{0pt}
\pagestyle{empty}
"""
    # No-argument transparent definitions leave each braced body as a group.
    # Unlike #1 identity macros, they do not pre-tokenize TikZ matrix ampersands
    # before TikZ can establish their catcodes. They accept text/math/paragraphs.
    preamble += "\n".join("\\def\\" + name + "{}" for name in macros)
    body = "\n\\begin{document}\n"
    body += "\n".join("\\input{" + str(p.relative_to(ROOT)).replace("\\", "/") + "}\n\\clearpage" for p in PAGES)
    body += "\n\\end{document}\n"
    wrapper = OUT / "smoke.tex"
    wrapper.write_text(preamble + body, encoding="utf-8")
    started = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run([engine, "-no-pdf", "-interaction=nonstopmode", "-file-line-error",
                           "-output-directory=" + str(OUT), str(wrapper)],
                          cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          text=True, timeout=240)
    (OUT / "compiler_output.txt").write_text(proc.stdout, encoding="utf-8")
    after = hashes()
    changed = [name for name in before if before[name] != after.get(name)]
    meta = {"started_utc": started, "engine": engine, "exit_code": proc.returncode,
            "page_count": len(PAGES), "changed_during_test": changed,
            "sha256_before": before, "sha256_after": after}
    (OUT / "run_metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Engine: {engine}; exit: {proc.returncode}; pages: {len(PAGES)}")
    print(f"Compiler output: {OUT / 'compiler_output.txt'}")
    print(f"Changed during test: {changed}")
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
