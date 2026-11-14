#!/usr/bin/env python3
"""Assemble the current research checkpoint without changing statement semantics."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'deliverable'
OUT.mkdir(exist_ok=True)
ID='LM6_POINTS_AS_SECTIONS'
preamble=r'''\documentclass[11pt,oneside]{article}
\usepackage[margin=25mm,headheight=15pt]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage{booktabs,longtable,array,enumitem}
\usepackage{xcolor,xurl,hyperref,fancyhdr,microtype}
\hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,
pdftitle={Points as sections: incomplete research return},
pdfauthor={GPT-6 Astra (OpenAI, ChatGPT Pro mode)}}
\setlength{\emergencystretch}{2em}
\setlength{\parskip}{3pt}
\setlength{\parindent}{1.2em}
\setlist{itemsep=2pt,topsep=4pt}
\allowdisplaybreaks
\newcommand{\Sha}{\operatorname{Sha}}
\newcommand{\Q}{\mathbb Q}
\newcommand{\Z}{\mathbb Z}
\newcommand{\R}{\mathbb R}
\newcommand{\C}{\mathbb C}
\newcommand{\F}{\mathbb F}
\DeclareMathOperator{\Aut}{Aut}
\DeclareMathOperator{\Out}{Out}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Gal}{Gal}
\DeclareMathOperator{\Spec}{Spec}
\DeclareMathOperator{\Pic}{Pic}
\DeclareMathOperator{\Jac}{Jac}
\DeclareMathOperator{\GL}{GL}
\DeclareMathOperator{\SL}{SL}
\DeclareMathOperator{\im}{im}
\DeclareMathOperator{\coker}{coker}
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\tr}{tr}
\DeclareMathOperator{\End}{End}
\DeclareMathOperator{\Inn}{Inn}
\DeclareMathOperator{\Sect}{Sect}
\newcommand{\enquote}[1]{\textquotedblleft#1\textquotedblright}
\newcounter{statementanchor}
\makeatletter
\newenvironment{statement}[3]{%
 \refstepcounter{statementanchor}\def\@currentlabel{#1}%
 \par\addvspace{9pt}\noindent
 \textbf{#1. #2. #3.}\par\nobreak\noindent\ignorespaces
}{\par\addvspace{5pt}}
\makeatother
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small Points as sections}
\fancyhead[R]{\small Research return --- INCOMPLETE}
\fancyfoot[C]{\thepage}
\begin{document}
\begin{center}
{\LARGE\bfseries Points as sections}\\[4pt]
{\large The anabelian texts of 1981 and 1983, real structures,\\
Mordell, and the Fermat tower}\\[7pt]
AI-produced by GPT-6 Astra\\
OpenAI, ChatGPT Pro mode\\[4pt]
14 November 2026 \qquad \textbf{INCOMPLETE research return}
\end{center}
\noindent
We give proofs, explicit comparison maps, counterexamples, and
independently executed finite certificates for the requested manuscript
passages. The unresolved statements remain numbered, with the precise
obstruction and the attempted approaches. We claim no priority.
Results using the supplied unrefereed local section theorem are
identified as deductions from that stipulated input.

\smallskip
\noindent\textbf{Notation and manuscript concordance.}
Symbols are fixed locally when a source uses the same letter differently.
The following table governs the arithmetic curve comparisons.
\begin{center}\small
\begin{tabular}{@{}p{.17\textwidth}p{.39\textwidth}p{.36\textwidth}@{}}
\toprule
Our notation & Mathematical object & Manuscript notation and introduction\\
\midrule
$G_K,\Gamma$ & Absolute Galois group, with profinite topology &
$\Gamma$; \S5, scans 21--24; cote 149, scans 43--48\\
$U=X\setminus S$ & Smooth hyperbolic curve and its proper completion &
$U,X,S$; \S6, scans 25--31\\
$E_U,\Pi_U$ & Arithmetic fundamental group &
$\mathcal E,E$; \S7, scans 43--54; cote 149, scan 44\\
$\pi,\Delta_U$ & Geometric fundamental group &
$\pi,\Pi_{U/K}$; same passages\\
$I_c,L_c,D_c$ & Cusp inertia and arithmetic decomposition &
$L_i,\mathcal E_i,N(L_i)$; scans 28--35, 69, 75--80\\
$T,\chi,\Gamma^\circ$ & $\widehat{\mathbb Z}(1)$, cyclotomic character, its kernel &
$T,\chi,\Gamma^\circ$; cote 149, scans 45, 54--56\\
$\operatorname{Sec}(U/K)$ & Continuous sections modulo geometric conjugacy &
Classes of splittings; scans 61--65, 75--79\\
\bottomrule
\end{tabular}
\end{center}
\noindent
A field embedding and a base-point path are specified wherever they
change a genuine homomorphism. A quotient map always specifies the
induced map of section classes. All closures are taken in the named
profinite or prime-adic topology.
For a multiplicative group, the Kummer completion means
$\varprojlim_n K^*/K^{*n}$ with its inverse-limit topology.
For a number field this group need not be compact.
Every finite quotient of $K^*$ has an exponent $n$ and therefore
factors through $K^*/K^{*n}$; these maps give the comparison
from the Kummer completion to the completion over all finite
quotients. It is injective, because finite quotients separate
every nonzero class in $K^*/K^{*n}$, and it has dense image,
because its image contains $K^*$.
\newpage
\tableofcontents
\newpage
'''
parts=[]
records=[]
counterA=0
envnames='proposition|theorem|lemma|corollary|remark|definition'
for name in ['A','B','C','C_extra','D','D_tail','E','E_density','E_extra','E_symmetry','E_integral_symmetry','E_symmetry_refinement','E_cover_comparison','E_explicit_kernel','E_no_boundary_cubic','E_mu6_three_parameters','E_remaining_kernel','E_full_metabelian','E_pronilpotent_families','E_five_metabelian','E_ross_edge','E_kummer_values','E_integral_detector','E_integral_path_comparison','F']:
    p=ROOT/'sections'/f'{name}.tex'
    if not p.exists():continue
    txt=p.read_text()
    snapshot=ROOT/'assembly_snapshot'/'sections'
    snapshot.mkdir(parents=True,exist_ok=True)
    (snapshot/p.name).write_text(txt)
    if name!='A':
        txt=re.sub(r'\\begin\{remark\}\[(?![A-F]\.\d+)([^\n]*?)\](.*?)\\end\{remark\}',
                   lambda m:r'\paragraph{'+m.group(1)+'}'+m.group(2),txt,flags=re.S)
    if name=='A':
        txt=r'\section{The anabelian conjectures and their exact groupoid form}'+'\n'+txt
    pat=re.compile(r'\\begin\{('+envnames+r')\}\[([^\n]*?)\]')
    def conv(m):
        global counterA
        env,title=m.groups()
        idmatch=re.match(r'([A-F]\.\d+)\s*---\s*(.*)',title)
        if idmatch: ident,rest=idmatch.groups()
        elif name=='A':
            counterA+=1;ident=f'A.{counterA}';rest=title
        else:raise RuntimeError(('unidentified theorem',name,title))
        status=next((s for s in ['Open','Refuted','Proved','Known'] if s.lower() in rest.split(':')[0].lower()),'Proved')
        heading=rest.split(':',1)[-1].strip() if ':' in rest else rest
        return r'\begin{statement}{'+ident+'}{'+status+'}{'+heading+'}\n'+r'\label{st:'+ident+'}'
    txt=pat.sub(conv,txt)
    txt=re.sub(r'\\end\{('+envnames+r')\}',r'\\end{statement}',txt)
    needle=r'\begin{statement}'
    pos=0
    while True:
        k=txt.find(needle,pos)
        if k<0:break
        at=k+len(needle); vals=[]
        for _ in range(3):
            assert txt[at]=='{',(name,txt[at:at+60])
            dep=1;j=at+1
            while dep:
                if txt[j]=='{' and (j==0 or txt[j-1]!='\\'):dep+=1
                if txt[j]=='}' and (j==0 or txt[j-1]!='\\'):dep-=1
                j+=1
            vals.append(txt[at+1:j-1]);at=j
        end=txt.find(r'\end{statement}',at)
        labels=re.findall(r'\\label\{([^}]+)\}',txt[at:end])
        anchor='st:'+vals[0]
        if anchor not in labels:
            inserted='\n'+r'\label{'+anchor+'}'+'\n'
            txt=txt[:at]+inserted+txt[at:]
            labels=[anchor]+labels
        records.append({'id':vals[0],'status':vals[1],'title':vals[2],
                        'labels':labels,'source_file':str(p.relative_to(ROOT))})
        pos=at
    parts.append('% ---- '+name+' ----\n'+txt)
(OUT/f'{ID}_paper.tex').write_text(preamble+'\n'.join(parts)+r'''
\clearpage
\bibliographystyle{plain}
\bibliography{LM6_POINTS_AS_SECTIONS_references}
\end{document}
''')
bibs=[]
for n in ['A_refs.bib','B_refs.bib','C_extra_refs.bib','F_references.bib','Root_refs.bib','E_density_refs.bib','E_ross_ramified_refs.bib']:
    p=ROOT/n
    if p.exists():bibs.append(p.read_text())
(OUT/f'{ID}_references.bib').write_text('\n\n'.join(bibs))
(ROOT/'statement_index.json').write_text(json.dumps(records,indent=2))
print(json.dumps({'statements':len(records),'output':str(OUT)},indent=2))

