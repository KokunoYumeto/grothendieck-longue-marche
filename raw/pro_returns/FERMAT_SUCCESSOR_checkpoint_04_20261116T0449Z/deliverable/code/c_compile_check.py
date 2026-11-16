"""Compile a temporary standalone Part C wrapper to check mathematical TeX."""
from pathlib import Path
import re
import subprocess

base=Path(__file__).resolve().parents[2]
work=base/"work"
preamble=(base/"deliverable/FERMAT_SUCCESSOR_paper.tex").read_text().split("\\title",1)[0]
wrapper=preamble+r"""
\begin{document}
\section{Part C verification wrapper}
\input{../deliverable/sections/C_main.tex}
\bibliographystyle{plainnat}
\bibliography{c_references}
\end{document}
"""
(work/"c_check.tex").write_text(wrapper)
commands=[
    ["lualatex","-interaction=nonstopmode","-halt-on-error","c_check.tex"],
    ["bibtex","c_check"],
    ["lualatex","-interaction=nonstopmode","-halt-on-error","c_check.tex"],
    ["lualatex","-interaction=nonstopmode","-halt-on-error","c_check.tex"],
]
for command in commands:
    r=subprocess.run(command,cwd=work,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(command[0], "exit", r.returncode)
    if r.returncode:
        print(r.stdout[-9000:])
        raise SystemExit(r.returncode)
log=(work/"c_check.log").read_text()
boxes=re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)",log)
print("Overfull hboxes:",len(boxes))
print("Largest horizontal overflow:",max(map(float,boxes),default=0))
print("Overflows above 2pt:",sum(float(x)>2 for x in boxes))
print("Undefined references/citations:",len(re.findall(r"(?:Citation|Reference).*undefined",log)))
print("PDF wrapper:",work/"c_check.pdf")
