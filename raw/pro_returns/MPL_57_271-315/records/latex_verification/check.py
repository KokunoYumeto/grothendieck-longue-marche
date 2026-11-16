"""Compile manuscript fragments mechanically without changing their source."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import os, subprocess, json, hashlib, re, sys

QA=Path(__file__).resolve().parent
ROOT=QA.parent/'MPL_57_271-315'
ENV=os.environ.copy()
ENV['TEXMF']='{/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}'
ENV['TEXMFVAR']=str(QA/'texmf-var')
ENV['TEXMFCONFIG']=str(QA/'texmf-config')
PREAMBLE=r'''\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,tikz-cd,graphicx}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,decorations.markings,decorations.pathreplacing,calc,positioning,shapes.geometric}
\newcommand{\cotefile}[1]{\par Cote #1\par}
\newcommand{\scanpage}[1]{\clearpage\typeout{SCAN #1}\noindent Scan #1\par}
\newcommand{\mspage}[1]{#1}
\newcommand{\deleted}[1]{#1}
\newcommand{\inserted}[1]{#1}
\newcommand{\margin}[1]{#1}
\newcommand{\uline}[1]{#1}
\newcommand{\uuline}[1]{#1}
\newcommand{\unsure}[1]{#1}
\newcommand{\illegible}[1]{[#1]}
\renewcommand{\figure}[1]{#1}
% Retokenize diagram bodies so plain & works even inside another marker.
\long\def\diagram#1{\begingroup\endlinechar=-1\relax\scantokens{#1}\endgroup}
\begin{document}
'''

def check(path):
    scan=int(re.search(r'scan([0-9]+)',path.name).group(1))
    work=QA/'runs'/f'scan{scan}'
    work.mkdir(parents=True,exist_ok=True)
    source_hash=hashlib.sha256(path.read_bytes()).hexdigest()
    wrapper=work/'wrapper.tex'
    wrapper.write_text(PREAMBLE+'\\input{'+str(path)+'}\n\\end{document}\n')
    command=['pdftex','-fmt='+str(QA/'qa_pdflatex'),'-draftmode','-no-shell-escape',
             '-interaction=nonstopmode','-file-line-error','-halt-on-error','wrapper.tex']
    result=subprocess.run(command,cwd=work,env=ENV,capture_output=True,text=True,timeout=90)
    output=result.stdout+'\n'+result.stderr
    (work/'compiler.stdout').write_text(output)
    errors=[]
    for line in output.replace('.\ntex:', '.tex:').splitlines():
        if re.search(r'\.(?:tex|sty|def):[0-9]+:',line) or line.startswith('!'):
            errors.append(line)
    after=hashlib.sha256(path.read_bytes()).hexdigest()
    return dict(scan=scan,file=str(path),exit_code=result.returncode,errors=errors,
                source_sha256=source_hash,source_changed_during_check=source_hash!=after,
                compiler_log=str(work/'wrapper.log'))

scans={int(s) for s in sys.argv[1:]}
paths=[p for p in sorted((ROOT/'pages').glob('*.tex'))
       if not scans or int(re.search(r'scan([0-9]+)',p.name).group(1)) in scans]
results=[]
with ThreadPoolExecutor(max_workers=4) as pool:
    jobs=[pool.submit(check,p) for p in paths]
    for job in as_completed(jobs):
        result=job.result()
        results.append(result)
        print(json.dumps(result,ensure_ascii=False),flush=True)
results.sort(key=lambda r:r['scan'])
(QA/'report.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checked':len(results),'passed':sum(r['exit_code']==0 for r in results),
                  'failed':[r['scan'] for r in results if r['exit_code']!=0],
                  'changed_during_check':[r['scan'] for r in results if r['source_changed_during_check']]}))
