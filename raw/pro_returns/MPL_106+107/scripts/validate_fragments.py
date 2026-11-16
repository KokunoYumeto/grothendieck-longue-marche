from pathlib import Path
import subprocess, json, re
ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT.parent/'validation'
TMP.mkdir(exist_ok=True)
PRE=r"""\documentclass{article}
\usepackage[paperwidth=80cm,paperheight=120cm,margin=1cm]{geometry}
\usepackage{fontspec,amsmath,amssymb,graphicx,xcolor,tikz-cd}
\usetikzlibrary{shapes.geometric,arrows.meta}
\newcommand{\cotefile}[1]{\par\textbf{Cote #1}\par}
\newcommand{\scanpage}[1]{\par\textbf{Scan #1}\par}
\newcommand{\mspage}[1]{\ifmmode\text{#1}\else#1\fi}
\newcommand{\deleted}[1]{{#1}}
\newcommand{\inserted}[1]{{#1}}
\newcommand{\margin}[1]{{#1}}
\newcommand{\uline}[1]{{#1}}
\newcommand{\uuline}[1]{{#1}}
\newcommand{\unsure}[1]{{#1}}
\newcommand{\illegible}[1]{{#1}}
\newcommand{\diagram}[1]{\ifmmode#1\else\par\noindent\ensuremath{#1}\par\fi}
\renewcommand{\figure}[1]{\ifmmode\text{#1}\else\par\noindent#1\par\fi}
\begin{document}
\small
"""
results=[]
for page in sorted((ROOT/'pages').glob('*.tex')):
    tex=PRE+page.read_text()+'\n\\end{document}\n'
    (TMP/'qa.tex').write_text(tex)
    p=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','qa.tex'],cwd=TMP,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    errs='\n'.join(p.stdout.splitlines()[-18:]) if p.returncode else ''
    results.append(dict(page=page.name,passed=p.returncode==0,details=errs))
    print(page.name,'PASS' if p.returncode==0 else errs,flush=True)
(ROOT/'records/latex_validation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print('PASSED',sum(r['passed'] for r in results),'/',len(results))
