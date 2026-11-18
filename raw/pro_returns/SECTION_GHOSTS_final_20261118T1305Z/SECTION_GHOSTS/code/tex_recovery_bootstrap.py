#!/usr/bin/env python3
"""Run the restored manuscript build with isolated TeX lookup/cache repair."""
from pathlib import Path
import hashlib, json, os, subprocess, sys, zipfile
ROOT=Path(__file__).resolve().parents[1]
DEPS=ROOT.parent/'tex_deps'
DEPS.mkdir(exist_ok=True)
RESOURCES=ROOT/'code/tex_runtime_sources'
manifest=json.loads((RESOURCES/'manifest.json').read_text())
for name, record in manifest.items():
    archive=RESOURCES/name
    if hashlib.sha256(archive.read_bytes()).hexdigest()!=record['sha256']:
        raise RuntimeError('Dependency archive hash mismatch: '+name)
    with zipfile.ZipFile(archive) as package:
        for member in package.infolist():
            target=(DEPS/member.filename).resolve()
            if target!=DEPS.resolve() and DEPS.resolve() not in target.parents:
                raise RuntimeError('Invalid dependency archive path: '+member.filename)
        package.extractall(DEPS)
print('Verified and unpacked four retained upstream Lua dependency archives.',flush=True)
for sub in ('cache','var','config','fonts/map/pdftex'):
    (DEPS/sub).mkdir(parents=True,exist_ok=True)
# System macro trees are present, but the system ls-R databases are absent.
# Remove database-only (!!) lookup without writing to the system installation.
env=os.environ.copy()
env['TEXMF']='{'+str(DEPS)+',/usr/share/texmf,/usr/share/texlive/texmf-dist}'
env['TEXINPUTS']='.:'+str(DEPS)+'//:'
env['LUAINPUTS']=str(DEPS)+'//:'
env['TEXMFCACHE']=str(DEPS/'cache')
env['TEXMFVAR']=str(DEPS/'var')
env['TEXMFCONFIG']=str(DEPS/'config')
# TeX's existing paranoid output policy permits absolute cache writes only
# under this job-specific allowed output root. It remains enabled.
env['TEXMFOUTPUT']=str(DEPS)
# Official distributions retain these documented docstrip-derived entry files.
for package, source, generated in [('lualibs','lualibs.dtx','lualibs.lua'),
                                  ('luatexbase','luatexbase.ins','luatexbase.sty')]:
    if not (DEPS/package/generated).exists():
        command=['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error',
                 r'\input plain \input '+source]
        result=subprocess.run(command,cwd=DEPS/package,env=env,text=True,
                              stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (DEPS/(package+'_docstrip.out')).write_text(result.stdout)
        if result.returncode:
            print(result.stdout[-10000:]);sys.exit(result.returncode)
# Recreate the minimal normal PDF font map from the installed upstream maps.
map_sources=[
'/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/cm.map',
'/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/cmextra.map',
'/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/symbols.map',
'/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/euler.map',
'/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/latxfont.map',
'/usr/share/texlive/texmf-dist/fonts/map/dvips/rsfs/rsfs.map',
'/usr/share/texmf/fonts/map/dvips/lm/lm.map']
entries={}
for source in map_sources:
    for line in Path(source).read_text().splitlines():
        if line.strip() and not line.lstrip().startswith(('%','#')):
            entries.setdefault(line.split()[0],line)
(DEPS/'fonts/map/pdftex/pdftex.map').write_text('\n'.join(entries.values())+'\n')
(ROOT/'build').mkdir(exist_ok=True)
if not (ROOT/'build/lualatex.fmt').exists():
    cmd=['luahbtex','--ini','--jobname=lualatex','--progname=lualatex',
         '--interaction=nonstopmode','--halt-on-error','--output-directory=build','lualatex.ini']
    result=subprocess.run(cmd,cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (DEPS/'format_bootstrap.out').write_text(result.stdout)
    if result.returncode:
        print(result.stdout[-10000:]);sys.exit(result.returncode)
with (DEPS/'final_build_summary.out').open('w') as output:
    result=subprocess.run([sys.executable,str(ROOT/'code/build.py')],cwd=ROOT,env=env,text=True,
                          stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output.write(result.stdout)
print(result.stdout)
sys.exit(result.returncode)
