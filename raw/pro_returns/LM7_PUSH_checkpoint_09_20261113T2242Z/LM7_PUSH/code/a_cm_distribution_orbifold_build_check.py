#!/usr/bin/env python3
"""Isolated TeX syntax/layout-log check; never touches the active main build."""
from pathlib import Path
import json,os,subprocess

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'research/E68_build_check'
OUT.mkdir(exist_ok=True)
preamble=(ROOT/'LM7_PUSH_paper.tex').read_text().split('\\begin{document}',1)[0]
(OUT/'check.tex').write_text(preamble+'\\begin{document}\n'+
    '\\input{sections/E_distribution_orbifold_agent.tex}\n\\end{document}\n')
env=os.environ.copy()
env.update({'TEXMF':'{'+str(OUT/'texmf-var')+',/usr/share/texmf,/usr/share/texlive/texmf-dist}',
            'TEXMFVAR':str(OUT/'texmf-var'),'TEXMFCONFIG':str(OUT/'texmf-config'),
            'TEXMFCACHE':str(OUT/'texmf-var'),'TEXFORMATS':str(ROOT/'build'),
            'TEXINPUTS':str(ROOT)+':'+str(ROOT/'build')+':'})
for key in ('TEXMFVAR','TEXMFCONFIG','TEXMFCACHE'):Path(env[key]).mkdir(exist_ok=True)
commands=[]
for i in (1,2):
    argv=['lualatex','-fmt=lm7lualatex','-interaction=nonstopmode','-halt-on-error',
          '-output-directory='+str(OUT),str(OUT/'check.tex')]
    run=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True,text=True)
    (OUT/f'pass{i}.out').write_text(run.stdout+run.stderr)
    commands.append({'pass':i,'argv':argv,'exit_code':run.returncode})
    (OUT/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
    if run.returncode:raise SystemExit(run.returncode)
log=(OUT/'check.log').read_text()
warnings=[line for line in log.splitlines() if 'Overfull' in line or 'Warning' in line]
print(json.dumps({'status':'PASS_TEX_COMPILE','warnings':warnings},indent=2))
