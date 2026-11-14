#!/usr/bin/env python3
"""Compile every fragment in a disposable syntax-check wrapper (no OCR).

The wrapper deliberately uses simple editorial macros; it is not a facsimile
edition or a replacement for the diplomatic fragment and its doubt apparatus.
"""
from pathlib import Path
import re, subprocess, tempfile, json
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
PREAMBLE=r'''\documentclass{article}
\usepackage[paperwidth=55cm,paperheight=65cm,margin=2cm]{geometry}
\usepackage{amsmath,amssymb,tikz-cd,cancel,xcolor}
\usetikzlibrary{arrows.meta,shapes.geometric}
\usepackage[utf8]{inputenc}
\newcommand{\cotefile}[1]{\par\textbf{Cote #1}\par}
\newcommand{\scanpage}[1]{\par\textbf{Scan #1}\par}
\newcommand{\mspage}[1]{\par\textit{#1}\par}
\newcommand{\deleted}[1]{{\color{gray}#1}}
\newcommand{\inserted}[1]{{\color{blue}#1}}
\newcommand{\margin}[1]{\par #1\par}
\newcommand{\uline}[1]{\ifmmode\underline{#1}\else\underline{\hbox{#1}}\fi}
\newcommand{\uuline}[1]{\uline{#1}}
\newcommand{\diagram}[1]{\par\noindent\(\displaystyle #1\)\par}
\renewcommand{\figure}[1]{\par\noindent #1\par}
\long\def\firstreading#1|#2\ENDREAD{#1}
\newcommand{\unsure}[1]{\firstreading#1|\ENDREAD}
\newcommand{\illegible}[1]{[\textit{#1 unreadable words}]}
\begin{document}
'''

def main():
 results=[]
 with tempfile.TemporaryDirectory(prefix='mpl-tex-') as tmp:
  tmp=Path(tmp)
  for p in sorted((ROOT/'pages').glob('*.tex')):
   f=tmp/(p.stem+'.tex');f.write_text(PREAMBLE+p.read_text()+'\n\\end{document}\n')
   run=subprocess.run(['pdflatex','-output-format=dvi','-halt-on-error','-interaction=nonstopmode','-output-directory',str(tmp),str(f)],capture_output=True,text=True)
   errors=[]
   if run.returncode:
    ls=run.stdout.splitlines()
    for i,line in enumerate(ls):
     if line.startswith('!'):errors.append('\n'.join(ls[max(0,i-1):i+9]))
   results.append({'file':p.name,'passed':run.returncode==0,'errors':errors})
   print(p.name, 'PASS' if run.returncode==0 else 'FAIL',flush=True)
   if errors:print('\n'.join(errors),flush=True)
 report={'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'purpose':'per-page LaTeX syntax check; simplified editorial macros; not a visual fidelity test','results':results}
 (ROOT/'tex_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print('TOTAL',len(results),'PASS',sum(x['passed'] for x in results),'FAIL',sum(not x['passed'] for x in results))

if __name__=='__main__':main()
