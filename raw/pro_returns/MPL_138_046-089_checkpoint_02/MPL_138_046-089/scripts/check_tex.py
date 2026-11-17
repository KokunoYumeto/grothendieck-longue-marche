"""Compile the raw combined fragment with a disposable macro harness.

The harness is an engineering check, not a replacement edition or facsimile.
It is intentionally kept outside the final package's transcription files.
"""
from pathlib import Path
import os, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
QA=ROOT.parent/'tex-validation'
QA.mkdir(exist_ok=True)
env=os.environ.copy()
env['TEXMF']='{'+str(QA/'texmf')+',/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}'
env['TEXMFVAR']=str(QA/'var')
env['TEXMFCONFIG']=str(QA/'config')
env['TEXFORMATS']=str(QA)+'//:'
for p in [QA/'var',QA/'config',QA/'texmf']:p.mkdir(exist_ok=True)

def run(args,log):
    p=subprocess.run(args,cwd=QA,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (QA/log).write_text(p.stdout)
    print(log, 'exit',p.returncode)
    print('\n'.join(p.stdout.splitlines()[-30:]))
    return p.returncode

if not (QA/'pdflatex.fmt').exists():
    r=run(['pdftex','-ini','-etex','-jobname=pdflatex','-progname=pdflatex','-interaction=nonstopmode',r'\pdfoutput=1 \input latex.ltx'],'format-build.txt')
    if r:sys.exit(r)

harness=r'''\documentclass[10pt]{article}
\pdfmapfile{=cm.map}
\pdfmapfile{+cmextra.map}
\pdfmapfile{+symbols.map}
\pdfmapfile{+euler.map}
\pdfmapfile{+latxfont.map}
\pdfmapfile{+lm.map}
\usepackage[a3paper,landscape,margin=18mm]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,tikz-cd,xcolor}
\usetikzlibrary{arrows.meta,decorations.pathreplacing,positioning,shapes.geometric}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\newcommand{\cotefile}[1]{\section*{Cote #1}}
\newcommand{\scanpage}[1]{\clearpage\section*{Scan #1}}
\newcommand{\mspage}[1]{\par Manuscript page #1\par}
\long\def\deleted#1{{\color{red!60!black}#1}}
\long\def\inserted#1{{\color{blue!60!black}#1}}
\long\def\margin#1{\par\noindent\textsc{Margin:} #1\par}
\long\def\unsure#1{{\color{orange!70!black}#1}}
\newcommand{\illegible}[1]{\textnormal{[illegible: #1 words]}}
\newcommand{\uline}[1]{\underline{#1}}
\newcommand{\uuline}[1]{\underline{\underline{#1}}}
\long\def\diagram#1{\par\begingroup\centering#1\par\endgroup}
\long\def\figure#1{#1}
\begin{document}
\input{FRAGMENT}
\end{document}
'''.replace('FRAGMENT',str(ROOT/'MPL_138_046-089_transcription.tex'))
(QA/'validation.tex').write_text(harness)
sys.exit(run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error','validation.tex'],'compile-output.txt'))
