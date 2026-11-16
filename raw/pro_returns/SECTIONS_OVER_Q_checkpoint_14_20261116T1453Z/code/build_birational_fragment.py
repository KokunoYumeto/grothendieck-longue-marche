#!/usr/bin/env python3
"""Compile the isolated B/D fragments without modifying the root manuscript."""
from pathlib import Path
import os
import re
import subprocess

WORK = Path(__file__).resolve().parents[1]
BUILD = WORK / "code" / "birational_fragment_build"
BUILD.mkdir(exist_ok=True)
build_env = os.environ.copy()
build_env["TEXFORMATS"] = "/workspace/scratch/677df891cc45/tex_runtime:"
build_env["TEXMFHOME"] = "/workspace/scratch/677df891cc45/tex_runtime/root/usr/share/texlive/texmf-dist"
build_env["TEXMFCACHE"] = "cache"
(BUILD / "cache").mkdir(exist_ok=True)
preamble = (WORK / "SECTIONS_OVER_Q_paper.tex").read_text().split(r"\begin{document}")[0]
tex = preamble + r"""
\begin{document}
\section{Birational and valuative results}
\input{../../sections/birational_agent.tex}
\section{Local rings}
\input{../../sections/local_rings_agent.tex}
\section{Full class-two comparison}
\input{../../sections/class2_lift_agent.tex}
\bibliographystyle{alpha}
\bibliography{../../notes/birational_references}
\end{document}
"""
(BUILD / "birational_fragment_test.tex").write_text(tex)
commands = [
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "birational_fragment_test.tex"],
    ["bibtex", "birational_fragment_test"],
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "birational_fragment_test.tex"],
    ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "birational_fragment_test.tex"],
]
with (WORK / "code" / "birational_fragment_build_output.txt").open("w") as output:
    for command in commands:
        result = subprocess.run(command, cwd=BUILD, env=build_env, text=True, capture_output=True)
        output.write("COMMAND: " + " ".join(command) + "\n")
        output.write(result.stdout + result.stderr)
        if result.returncode:
            raise SystemExit(f"Build failed: {' '.join(command)}; see build output")
    log = (BUILD / "birational_fragment_test.log").read_text()
    overfull = [float(x) for x in re.findall(r"Overfull \\hbox \(([0-9.]+)pt too wide\)", log)]
    summary = (
        f"Overfull boxes: {len(overfull)}; above 2pt: {sum(x > 2 for x in overfull)}; "
        f"maximum: {max(overfull, default=0)}pt\n"
    )
    output.write(summary)
    print(summary.strip())
