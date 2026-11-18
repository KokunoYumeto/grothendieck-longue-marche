#!/usr/bin/env python3
"""Compile with LuaLaTeX and BibTeX; retain the full command transcript."""
from pathlib import Path
import os, subprocess, sys, shutil, re
ROOT=Path(__file__).resolve().parents[1]
build=ROOT/'build'
build.mkdir(exist_ok=True)
env=os.environ.copy()
deps=ROOT.parent/'tex_deps'
if deps.exists():
    env['TEXINPUTS']='.:'+str(deps)+'//:'+env.get('TEXINPUTS','')
    env['LUAINPUTS']=str(deps)+'//:'+env.get('LUAINPUTS','')
cmd=['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=build']
if (build/'lualatex.fmt').exists():
    cmd+=['-fmt=build/lualatex.fmt']
cmd+=['SECTION_GHOSTS_paper.tex']
commands=[cmd,['bibtex','build/SECTION_GHOSTS_paper'],cmd,cmd]
# Regenerate an existing bibliography before the first pass so a previously
# malformed .bbl cannot prevent the corrected .bib from being read.
auxpath=build/'SECTION_GHOSTS_paper.aux'
if auxpath.exists():
    # A failed author-year pass can leave this generated mode switch behind.
    # Remove it before regenerating the bibliography; an actually invalid
    # bibliography will still report its own error on the new pass.
    auxpath.write_text('\n'.join(line for line in auxpath.read_text().splitlines()
                                 if '\\NAT@force@numbers' not in line)+'\n')
if auxpath.exists() and all(token in auxpath.read_text() for token in ('\\bibdata','\\bibstyle')):
    commands.insert(0,['bibtex','build/SECTION_GHOSTS_paper'])
logpath=ROOT/'code/build.out'
with logpath.open('w') as log:
    for command in commands:
        print('RUN', ' '.join(command),flush=True)
        log.write('RUN '+' '.join(command)+'\n')
        p=subprocess.run(command,cwd=ROOT,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        log.write(p.stdout)
        log.flush()
        if p.returncode:
            print(p.stdout[-10000:])
            print('BUILD FAILED:',p.returncode)
            sys.exit(p.returncode)
    shutil.copy2(build/'SECTION_GHOSTS_paper.pdf',ROOT/'SECTION_GHOSTS_paper.pdf')
    texlog=(build/'SECTION_GHOSTS_paper.log').read_text()
    boxes=re.findall(r'Overfull \\[hv]box \(([\d.]+)pt',texlog)
    print('overfull boxes:',len(boxes))
    print('overfull boxes exceeding 2pt:',sum(float(x)>2 for x in boxes))
    print('largest overfull box:',max(map(float,boxes),default=0))
    print('unresolved references:',len(re.findall(r'(?:Citation|Reference).*undefined',texlog)))
    print('PDF written:',ROOT/'SECTION_GHOSTS_paper.pdf')
