#!/usr/bin/env python3
"""Build with LuaLaTeX, retaining all logs and the overflow audit.

A normal TeX Live installation uses lualatex directly. This workspace
initially lacked generated formats and font maps; a local, unmodified
Debian texlive-luatex package provides the documented fallback.
"""
from pathlib import Path
from datetime import datetime,timezone
import os,re,subprocess,json,shutil
ROOT=Path(__file__).resolve().parents[1]
runtime=ROOT.parent/'tex_runtime'
env=os.environ.copy()
if (runtime/'lualatex.fmt').exists():
    trees=[runtime/'root/usr/share/texlive/texmf-dist',
           runtime/'root/usr/share/texmf',Path('/usr/share/texlive/texmf-dist'),
           Path('/usr/share/texmf')]
    env.update(TEXMF='{'+','.join(map(str,trees))+'}',
               TEXMFVAR=str(runtime/'cache'),TEXMFCACHE=str(runtime/'cache'))
    latex=['luahbtex','--fmt='+str(runtime/'lualatex.fmt'),'--progname=lualatex']
else:latex=['lualatex']
logroot=ROOT/'build_logs';logroot.mkdir(exist_ok=True)
logs=logroot/datetime.now(timezone.utc).strftime('build_%Y%m%dT%H%M%SZ')
logs.mkdir(exist_ok=False)
def run(args,name):
    with (logs/name).open('w') as f:
        r=subprocess.run(args,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
    if r.returncode:raise RuntimeError('Build failed: '+name)
run(['python',str(ROOT/'code/build_registers.py')],'registers.stdout')
aux = ROOT/'EXIT_TOWER_paper.aux'
if aux.exists() and '\\bibdata' in aux.read_text(errors='replace'):
    # Refresh a previously generated bibliography before TeX reads it;
    # this also permits repairs to malformed text in a prior .bbl.
    run(['bibtex','EXIT_TOWER_paper'],'bibtex_prepass.stdout')
run(latex+['-interaction=nonstopmode','-halt-on-error','EXIT_TOWER_paper.tex'],
    'lualatex_1.stdout')
run(['bibtex','EXIT_TOWER_paper'],'bibtex.stdout')
for n in [2,3]:
    run(latex+['-interaction=nonstopmode','-halt-on-error','EXIT_TOWER_paper.tex'],
        f'lualatex_{n}.stdout')
log=(ROOT/'EXIT_TOWER_paper.log').read_text(errors='replace')
overflow=[float(x) for x in re.findall(r'Overfull \\hbox \(([\d.]+)pt',log)]
data={'engine':latex,'overfull_total':len(overflow),
      'overfull_over_2pt':sum(x>2 for x in overflow),
      'overfull_widths_pt':overflow,
      'undefined':re.findall(r'.*(?:undefined|multiply defined).*',log),
      'missing_characters':re.findall(r'.*Missing character.*',log)}
(logs/'audit.json').write_text(json.dumps(data,indent=2)+'\n')
(logroot/'audit.json').write_text(json.dumps(data,indent=2)+'\n')
shutil.copy2(ROOT/'EXIT_TOWER_paper.log',logs/'latest.log')
print(json.dumps(data,indent=2))
