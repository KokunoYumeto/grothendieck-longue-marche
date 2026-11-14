#!/usr/bin/env python3
"""Compile the paper with LuaLaTeX and BibTeX; retain actual logs and overflow counts."""
from pathlib import Path
import subprocess,os,re,json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'deliverable' if (ROOT/'deliverable').exists() else ROOT
PAPER='LM6_POINTS_AS_SECTIONS_paper'
scratch=ROOT.parent
env=os.environ.copy()
runtime=ROOT/'texruntime'
engine=['lualatex']
if (runtime/'lualatex.fmt').exists():
    env['TEXMF']='{'+','.join([str(runtime/'texmf'),'/usr/share/texmf',
        '/usr/share/texlive/texmf-dist','/etc/texmf'])+'}'
    # LuaTeX's normal restricted-output rules accept a cache below the working directory.
    env['TEXMFCACHE']=str((runtime/'cache').relative_to(scratch))
    env['TEXFONTMAPS']=str(runtime)+':'
    engine+=['--fmt='+str(runtime/'lualatex.fmt')]
def latex(name):
    with (OUT/name).open('w') as f:
        p=subprocess.run(engine+['-interaction=nonstopmode','-halt-on-error',
            '-output-directory='+str(OUT),str(OUT/(PAPER+'.tex'))],
            cwd=scratch,env=env,stdout=f,stderr=subprocess.STDOUT)
    if p.returncode: raise RuntimeError('LuaLaTeX failed; see '+str(OUT/name))
if (OUT/(PAPER+'.aux')).exists():
    with (OUT/'bibtex_initial.txt').open('w') as f:
        subprocess.run(['bibtex',PAPER],cwd=OUT,env=env,stdout=f,stderr=subprocess.STDOUT)
latex('build_pass1.txt')
with (OUT/'bibtex_output.txt').open('w') as f:
    p=subprocess.run(['bibtex',PAPER],cwd=OUT,env=env,stdout=f,stderr=subprocess.STDOUT)
if p.returncode:raise RuntimeError('BibTeX failed; see bibtex_output.txt')
latex('build_pass2.txt')
latex('build_pass3.txt')
log=(OUT/(PAPER+'.log')).read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
missing=re.findall(r'Missing character:.*',log)
undefined=re.findall(r'LaTeX Warning: (?:Reference|Citation).*?undefined.*',log)
out={'engine':'LuaLaTeX (LuaHBTeX)','overfull_total':len(over),
    'overfull_over_2pt':sum(x>2 for x in over),'overfull_sizes_pt':over,
    'missing_characters':missing,'undefined_references_or_citations':undefined,
    'pdf':str(OUT/(PAPER+'.pdf'))}
(OUT/'typesetting_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))

