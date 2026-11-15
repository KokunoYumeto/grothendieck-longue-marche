"""Build a temporary wrapper to check fragment syntax, not manuscript layout."""
from pathlib import Path

root = Path(__file__).resolve().parent
qa = root.parent / "qa"
qa.mkdir(exist_ok=True)
header = r"""\documentclass[11pt]{article}
\usepackage[a3paper,margin=22mm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\long\def\uline#1{{#1}}
\long\def\uuline#1{{#1}}
\usepackage{tikz-cd}
\newcommand{\cotefile}[1]{\section*{Cote #1}}
\newcommand{\scanpage}[1]{\clearpage\section*{Scan #1}}
\newcommand{\mspage}[1]{#1}
\long\def\deleted#1{{#1}}
\long\def\inserted#1{{#1}}
\long\def\unsure#1{{#1}}
\newcommand{\illegible}[1]{[unreadable: #1 words]}
\long\def\margin#1{\ifmmode\text{#1}\else{#1}\fi}
\long\def\diagram#1{\ifmmode\vcenter{\hbox{#1}}\else\begin{center}#1\end{center}\fi}
\long\def\figure#1{\ifmmode\hbox{#1}\else{#1}\fi}
\begin{document}
"""
(qa / "validation.tex").write_text(header + "\\input{" + str(root / "MPL_136_189-234_transcription.tex") + "}\n\\end{document}\n")
print(qa / "validation.tex")
