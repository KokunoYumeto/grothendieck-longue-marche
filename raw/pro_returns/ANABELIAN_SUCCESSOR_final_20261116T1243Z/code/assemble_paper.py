"""Assemble current audited contributions, renumber claims, and write register.

The originals stay in their owner directories.  Re-running this file never
overwrites an agent contribution.  It builds one self-contained TeX source.
"""
import re,csv,json
from pathlib import Path
W=Path(__file__).resolve().parents[1]
FILES=['sections/A_foundations.tex','agent_criteria/criteria_section.tex',
       'agent_geometric/geometric_section.tex','sections/A_computations.tex',
       'sections/A_structure.tex','agent_F/F_section.tex']
parts=[(p,(W/p).read_text()) for p in FILES]
claims=[];mapping={};counts={'A':0,'F':0};scopes={};labelowners={}
for path,txt in parts:
    for match in re.finditer(r'\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}(.*?)\\end\{claim\}',txt,re.S):
        old,status,body=match.groups();part='F' if old.startswith('FF') else 'A'
        counts[part]+=1;new=f'{part}.{counts[part]}';mapping[old]=new
        claims.append((old,new,status,body,path))
        next_start=txt.find(r'\begin{claim}',match.end())
        scopes[old]=txt[match.start():next_start if next_start>=0 else len(txt)]
        for lab in re.findall(r'\\label\{([^}]+)\}',scopes[old]):labelowners[lab]=old
internal_claim_pattern=re.compile(r'(?<![A-Za-z0-9_])(AR|AC|AG|FF)\.?(\d+)(?![A-Za-z0-9_])')
def internal_claim_id(match):
    return match.group(1)+'.'+match.group(2)
def renumber(s):
    # Both AG.39 and AG39 occur in prose and display tags.  Underscore
    # boundaries preserve original program and audit filenames verbatim.
    return internal_claim_pattern.sub(lambda m:mapping.get(internal_claim_id(m),m.group()),s)
header=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\pdfextension mapfile{+lm.map}
\pdfextension mapfile{+cm.map}
\pdfextension mapfile{+symbols.map}
\pdfextension mapfile{+euler.map}
\pdfextension mapfile{+rsfs.map}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage{booktabs,longtable,array,enumitem,microtype,xurl}
\usepackage[numbers,sort&compress]{natbib}
\usepackage[unicode,colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\hypersetup{pdftitle={ANABELIAN SUCCESSOR: point sections and reconstruction from etale topoi},
pdfauthor={GPT-6 Astra (OpenAI, ChatGPT Pro mode)},
pdfsubject={Incomplete research return, 16 November 2026}}
\makeatletter
\newcommand{\claimspace}{\par\if@nobreak\else\begingroup
  \@tempdima=5\baselineskip
  \vskip\z@\@plus\@tempdima\penalty-100
  \vskip\z@\@plus-\@tempdima
  \vskip\@tempdima\penalty10000\vskip-\@tempdima
\endgroup\fi}
\newenvironment{claim}[2]{\claimspace\medskip\phantomsection\def\@currentlabel{#1}\noindent\textbf{#1.}\quad\textsc{#2}\par\nobreak\smallskip\nobreak}{\par\medskip}
\makeatother
\newcommand{\F}{\mathbf F}
\newcommand{\Z}{\mathbf Z}
\newcommand{\Q}{\mathbf Q}
\newcommand{\C}{\mathbf C}
\newcommand{\Gal}{\operatorname{Gal}}
\newcommand{\Spec}{\operatorname{Spec}}
\newcommand{\Hom}{\operatorname{Hom}}
\newcommand{\Aut}{\operatorname{Aut}}
\newcommand{\im}{\operatorname{im}}
\newcommand{\Pic}{\operatorname{Pic}}
\newcommand{\et}{\mathrm{\acute et}}
\newcommand{\pp}{p'}
\newcommand{\rank}{\operatorname{rank}}
\newcommand{\coker}{\operatorname{coker}}
\newcommand{\Tr}{\operatorname{Tr}}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{0.2em}
\title{ANABELIAN\_SUCCESSOR\\Point sections in characteristic $p$\\and reconstruction from \'etale topoi}
\author{AI-produced by GPT-6 Astra\\(OpenAI, ChatGPT Pro mode)}
\date{16 November 2026}
\begin{document}
\maketitle
\begin{abstract}
\textbf{INCOMPLETE research return.}
We prove injectivity of the point-section map for every smooth proper
curve of genus at least two over every finite field, retaining the full
arithmetic quotient and the whole geometric prime-to-$p$ group.
The proof combines fixed-prime cuspidal configuration exactness,
diagonal boundary transport, and a point-recognition and Kummer
evaluation argument. It also proves the corresponding injectivity for
hyperbolic curves over fields finitely generated over $\mathbf F_p$.
We prove the rational relative-class-number criterion, its exact character
formula, its reduction to prime cyclic covers, and a controlled comparison
for nonconstant deck groups. We compute all base-field prime-character
tests for genus-two curves over fields of sizes $4,8,16$, give rational
witnesses for every original pointed genus-two pair over $\mathbf F_4$,
and compute every base-field odd-prime character test on pointed plane
quartics over $\mathbf F_3$ and $\mathbf F_5$. We determine all-extension least primes in
the explicitly certified cases. We audit the geometric
criteria, the exceptional-set formulation, and the norm module. An explicit
supersingular genus-two pencil refutes universal existence of nontrivial
odd cyclic covers with primitive two-rank zero; allowing the identity
cover leaves a separate positive-two-rank question. A cyclic-cover
Kodaira fibration and strong approximation also prove that the full
prime-to-$p$ configuration fiber map is not injective for any prime $p$,
ruling out that sufficient route without producing a collision. In the
topos problem we refute two broad formulations, prove a normal-extension
reconstruction theorem, prove reconstruction for subfields of
$\overline{\mathbf Q}_p$ of finite transcendence degree with bounded
$p$-primary ramification, prove reconstruction for finite extensions of the
fixed finite-class nilpotent extensions of the strict henselization of
$\mathbf Q$ at $p$ and for their subfields, and distinguish
precise model descent from a
bare pro-category assertion. The separate cover-existence, full-census,
abstract norm-module, and field-classification requests remain explicitly
open where they have not been settled. No claim of priority or human
authorship is made.
\end{abstract}
\tableofcontents
\section{Part A. Point sections over finite fields}
'''
body=[]
for path,txt in parts:
    if path.startswith('agent_F/'):
        txt=txt.replace(r'\section{Schemes, relative topoi, and the proposed field criteria}',r"\section{Part F. Reconstruction from \'etale topoi}",1)
    body.append('% Source: '+path+'\n'+renumber(txt))
(W/'ANABELIAN_SUCCESSOR_paper.tex').write_text(header+'\n'.join(body)+'\n\\bibliographystyle{plainnat}\n\\bibliography{ANABELIAN_SUCCESSOR_references}\n\\end{document}\n')
bibfiles=['notes/root_references.bib','agent_criteria/criteria_refs.bib','agent_geometric/geometric_references.bib','agent_F/F_references.bib']
bibs=[]
for path in bibfiles:
    if (W/path).exists():bibs.append('% Source: '+path+'\n'+(W/path).read_text())
(W/'ANABELIAN_SUCCESSOR_references.bib').write_text('\n'.join(bibs))
# Per-claim task mapping is kept explicit rather than inferred from prose.
answers={
'AR.1':'A1; L7; R1','AR.2':'A1','AR.3':'A1','AR.4':'A4','AR.5':'A4; R6','AR.6':'A4',
'AR.7':'A4','AR.15':'A4; R6','AR.16':'A3; A4; L2','AR.8':'A8; L9','AR.9':'A8; L7; L9','AR.10':'A9',
'AR.11':'A10(a); L11','AR.12':'A10(b); L11','AR.13':'A10(c,d); L11','AR.14':'A10(c); L11','AR.17':'A1; A7; L10','AR.18':'A1; A3; A10; L11','AR.19':'A1; A7; L10','AR.20':'A1; A7',
'AC.1':'A2; L0; R1; R2','AC.2':'A2; L1','AC.3':'A3; A7; L1',
'AC.4':'A2; L2','AC.5':'A2; L2','AC.6':'A2; L2','AC.7':'A3; L3',
'AC.8':'A3; L3','AC.9':'A2; A3; L2; L3','AC.10':'A3; L2; R7',
'AC.11':'A2; L4','AC.12':'A3; L3','AC.13':'A2; L1; R8','AC.14':'A3; L3',
'AC.15':'A4; R6','AC.16':'A4; A10(c)','AC.17':'A4; A10(c)',
'AC.18':'A2; L0; L1','AC.19':'A2; A3; L1','AC.20':'A3; A7',
'AC.21':'A3; A4','AC.22':'A3; A4; L2','AC.23':'A3; L2','AC.24':'A3; A5',
'AC.25':'A3; A4','AC.26':'A3; A4','AC.27':'A2; A3; A4; L2',
'AC.28':'A3; A4','AC.29':'A3; A4','AC.30':'A3; A4','AC.31':'A3; A6; L1; L8','AC.32':'A3; L3','AC.33':'A3; L2; L3','AC.34':'A1; A3; A5; L5','AC.35':'A3; L2','AC.36':'A1; A7; L10','AC.37':'A1; A7; L10','AC.38':'A3; A6; L1; L8','AC.39':'A1; A3; A10; L11','AC.40':'A1; A3; A10; L11','AC.41':'A3; A6; L1; L8','AC.42':'A1; A7','AC.43':'A1; A7','AC.44':'A6; L8','AC.45':'A10; L11',
'AG.1':'A5; L5','AG.2':'A5; L6','AG.3':'A6; L8','AG.4':'A6; L8',
'AG.5':'A7; L10','AG.6':'A7; A10; L10; L11','AG.7':'A7; L10',
'AG.8':'A5; R4','AG.9':'A5; A6','AG.10':'A5; A6; L8',
'AG.11':'A6; L8','AG.12':'A6; L8','AG.13':'A5; L5','AG.14':'A5; L6',
'AG.15':'A6; L8','AG.16':'A6; L8','AG.17':'A2; A7; L1',
'AG.18':'A6; L8','AG.19':'A2; A7; L1; A10(b)','AG.20':'A3; A5; A7','AG.21':'A6; L8','AG.22':'A3; A6; L3','AG.23':'A4; L2','AG.24':'A4','AG.25':'A4','AG.26':'A4','AG.27':'A6; L8','AG.28':'A1; A7; L10','AG.29':'A1; A4; A7; L10','AG.30':'A1; A5; L5; L6','AG.31':'A1; A10; L11','AG.32':'A6; L8','AG.33':'A6; L8','AG.34':'A6; L8','AG.35':'A1; A7','AG.36':'A1; A7','AG.37':'A6; L8','AG.38':'A6; L8','AG.39':'A1; A8; L9','AG.40':'A1; A8; L9','AG.41':'A1; A8; L9','AG.42':'A1; A5; A8; L5; L9',
'FF.1':'F1(i)','FF.2':'F1(i)','FF.3':'F1(ii)','FF.4':'F1(ii)','FF.5':'F2',
'FF.6':'F3(a)','FF.7':'F3(b)','FF.8':'F1(iii); F3(c); F6',
'FF.9':'F3; F5','FF.10':'F3; F5','FF.11':'F3; F5','FF.12':'F5; R9',
'FF.13':'F1(iii); F6','FF.14':'F3(c)','FF.15':'F6','FF.16':'F4',
'FF.17':'F4','FF.18':'F3(a); F4','FF.19':'F3; F5; R9',
'FF.20':'F3(a); F4','FF.21':'F3; F5; R9','FF.22':'F3; F4; R9',
'FF.23':'F3; F4','FF.24':'F3; F4; F5','FF.25':'F3; F4; F5','FF.26':'F3; F4; F5','FF.27':'F3; F4; F5',
'FF.28':'F3; F4; F5','FF.29':'F3; F4; F5','FF.30':'F3; F4; F5','FF.31':'F3(a); F4','FF.32':'F3(a); F4; F5',
'FF.33':'F3; F4; F5','FF.34':'F3; F4; F5','FF.35':'F3; F4; F5','FF.36':'F3; F4; F5','FF.37':'F3; F4; F5','FF.38':'F3; F4; F5','FF.39':'F3(a); F4; F5','FF.40':'F3(a); F4; F5','FF.41':'F3(a); F4; F5','FF.42':'F3(a); F4; F5','FF.43':'F3(a); F4; F5','FF.44':'F3(a); F4; F5','FF.45':'F3(a); F4; F5','FF.46':'F3(a); F4; F5','FF.47':'F3(a); F4; F5','FF.48':'F3(a); F4; F5','FF.49':'F3(a); F4; F5','FF.50':'F3(a); F4; F5'}
headercsv=['id','statement','status','where_proved','depends_on','answers (item or lead)',
 'manuscript_passages (cote; scan)','depends_on_doubtful_reading (scan, alternatives)','notes']
# A reference to a later consequence is not a premise. Prefer the owners'
# explicit proof-input records, and audit the main proof chain separately.
owner_dependencies={}
for owner_register in ['agent_criteria/criteria_results.csv','agent_F/F_results.csv']:
    for row in csv.DictReader((W/owner_register).open()):
        if row['depends_on'].strip()!='see proof':
            owner_dependencies[row['id']]=row['depends_on']
dependency_overrides={
 'AR.1':{'AC.1'}, 'AR.2':{'AR.3'},
 'AR.3':{'AG.40','AG.41','AG.42'},
 'AG.24':{'AG.23'}, 'AG.25':{'AG.24'},
 'AG.26':{'AG.23','AG.24','AG.25'},
 'AG.39':set(), 'AG.40':{'AG.39'}, 'AG.41':set(),
 'AG.42':{'AG.40','AG.41'},
 'AC.45':{'AR.3','AR.11','AG.38'},
}
def dependency_ids(s):
    result={internal_claim_id(m) for m in internal_claim_pattern.finditer(s)}
    for prefix,first,last in re.findall(r'(AR|AC|AG|FF)\.(\d+)\s*--\s*(\d+)',s):
        result.update(f'{prefix}.{n}' for n in range(int(first),int(last)+1))
    return result
with (W/'ANABELIAN_SUCCESSOR_results.csv').open('w',newline='') as f:
    wr=csv.writer(f);wr.writerow(headercsv)
    for old,new,status,txt,path in claims:
        clean=re.sub(r'\\label\{[^}]*\}','',renumber(txt)).strip()
        context=scopes[old]
        depids={internal_claim_id(m) for m in internal_claim_pattern.finditer(context)}
        depids.update(labelowners[lab] for lab in re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',context) if lab in labelowners)
        depids.discard(old)
        dependency_note='Proof-scope references.'
        if old in owner_dependencies:
            depids=dependency_ids(owner_dependencies[old])
            dependency_note='Explicit owner proof inputs: '+renumber(owner_dependencies[old])+'.'
        if old in dependency_overrides:
            depids=dependency_overrides[old]
            dependency_note+=' Internal premises independently audited; forward consequences are excluded.'
        deps=sorted({mapping.get(d,d) for d in depids})
        cites=sorted(set(k.strip() for block in re.findall(r'\\cite[a-z]*\*?(?:\[[^]]*\])*\{([^}]+)\}',context) for k in block.split(',')))
        normalized_status=re.match(r'(Proved|Refuted|Known|Open)',status,re.I).group(1).capitalize()
        passage='149; 35–36' if new.startswith('A') else '149; 52'
        if old=='AR.10':passage='149; 22, 36'
        if old in ['FF.8','FF.13','FF.15']:passage='149; 6–8, 52'
        wr.writerow([new,clean,normalized_status,f'ANABELIAN_SUCCESSOR_paper.tex; source {path}',
                     '; '.join(deps),answers.get(old,''),passage,'No conclusion depends on choosing an uncertain word',
                     f'Working identifier {old}. '+status+' '+dependency_note+(' External citations: '+', '.join(cites) if cites else '')])
(W/'notes/statement_map.json').write_text(json.dumps(mapping,indent=2)+'\n')
print(json.dumps({'claims':counts,'mapping':mapping,'bibliographies':bibfiles},indent=2))
