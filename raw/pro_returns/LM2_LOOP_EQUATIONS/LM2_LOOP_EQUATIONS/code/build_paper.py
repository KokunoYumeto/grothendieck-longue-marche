#!/usr/bin/env python3
"""Build the LuaLaTeX paper and run bibliography/cross-reference passes.

Normal installation: python3 code/build_paper.py
Minimal Debian tree with an absent filename database/format:
    python3 code/build_paper.py --local-tex-tree
The latter builds only a workspace-local format; it changes no system files.
"""
from pathlib import Path
import argparse
import os
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = 'LM2_LOOP_EQUATIONS_paper'

def run(command, destination, env, cwd=ROOT):
    with destination.open('w') as out:
        result = subprocess.run(command, cwd=cwd, env=env, stdout=out,
                                stderr=subprocess.STDOUT)
    if result.returncode:
        print(destination.read_text()[-6000:])
        raise SystemExit(result.returncode)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--local-tex-tree', action='store_true')
    args = parser.parse_args()
    env = os.environ.copy()
    logs = ROOT/'code'/'build_logs'
    logs.mkdir(exist_ok=True)
    if args.local_tex_tree:
        build = ROOT/'.build'
        fmt = build/'formats'; fmt.mkdir(parents=True, exist_ok=True)
        env.update(TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf}',
                   TEXFORMATS=str(fmt)+':', TEXMFVAR=str(build/'texvar'),
                   TEXMFCACHE=str(build/'texcache'))
        if not (fmt/'lualatex.fmt').exists():
            run(['luahbtex','--ini','--jobname=lualatex','--progname=lualatex',
                 '-interaction=nonstopmode','-halt-on-error','lualatex.ini'],
                logs/'format_build.out',env,fmt)
    command=['lualatex','-interaction=nonstopmode','-halt-on-error',NAME+'.tex']
    run(command,logs/'lualatex_pass1.out',env)
    run(['bibtex',NAME],logs/'bibtex.out',env)
    run(command,logs/'lualatex_pass2.out',env)
    run(command,logs/'lualatex_pass3.out',env)
    log=(ROOT/(NAME+'.log')).read_text(errors='replace')
    defects=[s for s in log.splitlines() if
             'undefined' in s.lower() and ('Citation' in s or 'Reference' in s or 'citations' in s)]
    assert not defects, defects
    assert not re.search(r'^! ',log,re.M), 'TeX error in final log'
    assert 'Missing character:' not in log, 'Missing glyph in final log'
    print('LuaLaTeX PDF:',ROOT/(NAME+'.pdf'))
    print('Final log: no TeX errors, undefined citations/references, or missing glyphs.')
    print('Overfull boxes:',log.count('Overfull \\hbox')+log.count('Overfull \\vbox'))
    print('Build logs:',logs)

if __name__=='__main__':
    main()
