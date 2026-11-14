\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[a4paper,margin=27mm,headheight=14pt]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools}
\usepackage{array,booktabs,longtable,tabularx,enumitem,graphicx}
\usepackage{xcolor,microtype}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,
 urlcolor=blue!45!black,pdftitle={LM7: The Fermat tower in the metabelian approximation},
 pdfauthor={GPT-6 Astra, OpenAI, ChatGPT Pro mode}}
\urlstyle{same}
\setlength{\parindent}{1.3em}
\setlength{\parskip}{.22em}
\setlength{\emergencystretch}{2em}
\setlength{\LTpre}{.6em}
\setlength{\LTpost}{.6em}
\setlist{nosep}
\setcounter{secnumdepth}{0}
\setcounter{tocdepth}{1}
\allowdisplaybreaks[2]
\newenvironment{statement}[3]{%
 \par\addvspace{1.1em}\phantomsection\label{st:#1}%
 \noindent\textbf{#1. #3}\quad\textsf{\small[#2]}\par\nobreak\smallskip\ignorespaces
}{\par\smallskip}
\newcommand{\statementref}[1]{\hyperref[st:#1]{#1}}
\newcommand{\Sha}{\mathop{\mathrm{Sh}}}
\begin{document}
\input{../sections/E_quartic_compact_cups.tex}
\bibliographystyle{plain}
\bibliography{E113_refs}
\end{document}
