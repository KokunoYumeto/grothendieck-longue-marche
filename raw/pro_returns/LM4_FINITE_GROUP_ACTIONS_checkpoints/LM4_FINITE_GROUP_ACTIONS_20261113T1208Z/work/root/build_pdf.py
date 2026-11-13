#!/usr/bin/env python3
"""Build with LuaLaTeX, retaining logs and using writable local TeX caches."""
from pathlib import Path
import os,sys,subprocess,json,re,hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverable'
WORK=ROOT/'work'/'tex_cache'
WORK.mkdir(exist_ok=True)
env=os.environ.copy()
# This container has the distribution files but no global ls-R database.
# Omit the kpathsea !! flag so the installed trees are searched directly.
env['TEXMF']='{'+','.join([str(WORK/'texmf'),str(WORK/'var'),'/usr/share/texlive/texmf-dist','/usr/share/texmf','/etc/texmf'])+'}'
env['TEXMFVAR']=str(WORK/'var')
env['TEXMFCONFIG']=str(WORK/'config')
env['TEXMFCACHE']=str(WORK/'cache')
for k in ['TEXMFVAR','TEXMFCONFIG','TEXMFCACHE']:Path(env[k]).mkdir(exist_ok=True)
local_web=WORK/'texmf'/'web2c'
local_web.mkdir(parents=True,exist_ok=True)
(local_web/'fmtutil.cnf').write_text('lualatex luahbtex language.dat,language.dat.lua lualatex.ini\n')
local_hyph=WORK/'texmf'/'tex'/'generic'/'config'
local_hyph.mkdir(parents=True,exist_ok=True)
(local_hyph/'language.dat').write_text('english hyphen.tex\n')
fontmap=WORK/'texmf'/'fonts'/'map'/'pdftex'/'updmap'
fontmap.mkdir(parents=True,exist_ok=True)
maps=[Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map')]
for name in ['cm','cmextra','latxfont','symbols','euler','cyrillic']:
 maps.append(Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts')/(name+'.map'))
maps.extend(Path('/usr/share/texlive/texmf-dist/fonts/map').rglob('rsfs.map'))
(fontmap/'pdftex.map').write_text('\n'.join(p.read_text() for p in maps))
name='LM4_FINITE_GROUP_ACTIONS_paper'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
source_hashes={p.name:sha(p) for p in
               [OUT/(name+'.tex'), OUT/'LM4_FINITE_GROUP_ACTIONS_references.bib']}
stages=[['lualatex','-interaction=nonstopmode','-halt-on-error',name+'.tex']]
if '--full' in sys.argv:
 stages.extend([['bibtex',name],stages[0],stages[0]])
results=[]
for i,cmd in enumerate(stages):
 fn=OUT/f'build_stage_{i+1}_stdout.txt'
 with fn.open('w') as f:
  proc=subprocess.run(cmd,cwd=OUT,env=env,stdout=f,stderr=subprocess.STDOUT)
 results.append({'command':cmd,'exit_code':proc.returncode,'log':fn.name})
 print(json.dumps(results[-1]),flush=True)
 if proc.returncode:
  print('\n'.join(fn.read_text(errors='replace').splitlines()[-45:]),flush=True)
  break
(OUT/'build_commands.json').write_text(json.dumps(results,indent=2)+'\n')
success=all(r['exit_code']==0 for r in results) and len(results)==len(stages)
record={'success':success,'stage_count':len(results),'source_sha256':source_hashes,
        'pdf_sha256':sha(OUT/(name+'.pdf')) if success else None}
(OUT/'build_artifact.json').write_text(json.dumps(record,indent=2)+'\n')
sys.exit(results[-1]['exit_code'])
