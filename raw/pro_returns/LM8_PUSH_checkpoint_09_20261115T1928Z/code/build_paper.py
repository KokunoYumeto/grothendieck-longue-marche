#!/usr/bin/env python3
"""LuaLaTeX build using the locally installed, hash-checked TeX runtime."""
import os,pathlib,subprocess,sys
PAPER=pathlib.Path(__file__).resolve().parents[1]
RT=PAPER.parent/'tex-runtime'
BUILD=PAPER/'build';BUILD.mkdir(exist_ok=True)
env=os.environ.copy()
for key,child in [('TEXMFROOT',''),('TEXMFDIST','texmf-dist'),('TEXMFVAR','var'),('TEXMFCONFIG','config'),('TEXMFCACHE','cache'),('TEXMFHOME','home')]:
    env[key]=str(RT/child)
    if child in ['var','config','cache','home']:(RT/child).mkdir(exist_ok=True)
(BUILD/'tex-cache').mkdir(exist_ok=True)
env['TEXMFCACHE']='build/tex-cache'
env['TEXMF']=str(RT/'texmf-dist')
env['TEXMFCNF']=str(RT/'texmf-dist/web2c')
env['TEXFORMATS']=str(RT/'var/web2c')+'//'
env['BIBINPUTS']=str(PAPER)+os.pathsep
env['BSTINPUTS']=str(RT/'texmf-dist/bibtex/bst')+'//'+os.pathsep
env['PATH']=str(RT/'bin/x86_64-linux')+os.pathsep+env.get('PATH','')
engine=RT/'bin/x86_64-linux/luahbtex'
fontmap=RT/'texmf-dist/fonts/map/pdftex/updmap/pdftex.map'
fontmap.parent.mkdir(parents=True,exist_ok=True)
maps=list((RT/'texmf-dist/fonts/map/dvips/amsfonts').glob('*.map'))
maps.append(RT/'texmf-dist/fonts/map/dvips/lm/lm.map')
maplines={}
for source in maps:
    for line in source.read_text().splitlines():
        if line.strip() and not line.lstrip().startswith('%'):
            maplines.setdefault(line.split()[0],line)
fontmap.write_text('\n'.join(maplines.values())+'\n')
fmt=RT/'var/web2c/lualatex.fmt';fmt.parent.mkdir(parents=True,exist_ok=True)
with (BUILD/'build_console.out').open('w') as log:
    def run(args,cwd=PAPER):
        print('RUN',args,flush=True)
        p=subprocess.run([str(a) for a in args],cwd=cwd,env=env,stdout=log,stderr=subprocess.STDOUT)
        log.flush()
        if p.returncode: raise SystemExit(p.returncode)
    if not fmt.exists():
        run([engine,'--ini','--interaction=nonstopmode','--halt-on-error','--jobname=lualatex','lualatex.ini'],fmt.parent)
    for n in range(4):
        run([engine,'--fmt=lualatex','--interaction=nonstopmode','--halt-on-error','--output-directory='+str(BUILD),'LM8_PUSH_paper.tex'])
        if n==0:run(['/usr/bin/bibtex','LM8_PUSH_paper'],BUILD)
    import shutil
    shutil.copy2(BUILD/'LM8_PUSH_paper.pdf',PAPER/'LM8_PUSH_paper.pdf')
print('PDF',PAPER/'LM8_PUSH_paper.pdf')
