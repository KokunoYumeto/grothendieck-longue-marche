#!/usr/bin/env python3
"""Isolated, syntax-only checks of current fragment snapshots; never edits them."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
import shutil
import subprocess

PREAMBLE = r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{tikz,tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,patterns,calc,shapes.geometric}
% Editorial wrappers are deliberately visually neutral for syntax checking.
\long\def\cotefile#1{\par\noindent Cote #1\par}
\long\def\scanpage#1{\clearpage\noindent Scan #1\par}
\long\def\mspage#1{\par\noindent Manuscript page #1\par}
% Do not pre-tokenize an argument that may contain a TikZ matrix: its
% ampersands must receive the catcode selected by the matrix environment.
\def\deleted{}
\def\inserted{}
\def\margin{}
\def\uline{}
\def\uuline{}
\def\unsure{}
\long\def\illegible#1{\ifmmode\text{[illegible: #1]}\else[illegible: #1]\fi}
\def\diagram{}
\def\figure{}
\begin{document}
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--temporary-dir', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    temporary = (args.temporary_dir or root.parent/'tex_validation').resolve()
    if temporary == root or root in temporary.parents:
        raise ValueError('Temporary wrapper directory must be outside the deliverable tree')
    temporary.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env['TEXMF'] = '{'+str(temporary)+',/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}'
    # Local files must precede every package search. Never recursively search
    # sibling page directories, which all contain a fragment.tex/check.tex.
    env['TEXINPUTS'] = '.:'+str(temporary)+':'
    env['max_print_line'] = '1000'
    env['TEXMFVAR'] = str(temporary/'texmf-var')
    env['TEXMFCONFIG'] = str(temporary/'texmf-config')
    env['TEXFORMATS'] = str(temporary)+'//:'
    (temporary/'language.dat').write_text('english hyphen.tex\n')
    if not (temporary/'pdflatex.fmt').exists():
        r = subprocess.run(
            ['pdftex','-ini','-etex','-interaction=nonstopmode','-halt-on-error',
             '-jobname=pdflatex','-output-directory='+str(temporary),'pdflatex.ini'],
            cwd=temporary,env=env,capture_output=True,text=True,
        )
        (temporary/'format_build.stdout.txt').write_text(r.stdout+r.stderr)
        if r.returncode:
            raise RuntimeError('Local format build failed: '+str(temporary/'format_build.stdout.txt'))
    sources = sorted((root/'pages').glob('*.tex'))
    snapshots = []
    for source in sources:
        target_dir = temporary/source.stem
        target_dir.mkdir(exist_ok=True)
        snapshot = target_dir/'fragment.tex'
        content = source.read_bytes()
        snapshot.write_bytes(content)
        wrapper = target_dir/'check.tex'
        wrapper.write_text(PREAMBLE+'\\input{'+str(snapshot)+'}\n\\end{document}\n',encoding='utf-8')
        snapshots.append((source, target_dir, hashlib.sha256(content).hexdigest()))

    def check(item):
        source,target_dir,digest = item
        r = subprocess.run(
            ['pdftex','-fmt=pdflatex','-draftmode','-interaction=nonstopmode',
             '-halt-on-error','-file-line-error',str(target_dir/'check.tex')],
            cwd=target_dir,env=env,capture_output=True,text=True,
        )
        output = r.stdout+r.stderr
        (target_dir/'compile.stdout.txt').write_text(output,encoding='utf-8')
        errors = []
        lines = output.splitlines()
        for i,line in enumerate(lines):
            if line.startswith('!') or ('fragment.tex:' in line and (': ' in line)):
                errors.append('\n'.join(lines[max(0,i-1):min(len(lines),i+7)]))
        return {
            'page':source.name,'sha256':digest,'returncode':r.returncode,
            'source_unchanged_since_snapshot':hashlib.sha256(source.read_bytes()).hexdigest()==digest,
            'errors':errors,'log':str(target_dir/'compile.stdout.txt'),
            'output_tail_if_unclassified_error':output[-2000:] if r.returncode and not errors else '',
        }
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(check,snapshots))
    report = {
        'checked_at':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'engine':'pdfTeX 1.40.26; isolated local LaTeX format; draft mode',
        'scope':'Syntax only, visually neutral editorial macros; no visual audit or completeness claim.',
        'pages_checked':len(results),'pages_passed':sum(r['returncode']==0 for r in results),
        'results':results,
    }
    report_path = root/'records'/'latex_syntax_report.json'
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))
    for result in results:
        if result['returncode']:
            print(json.dumps(result,ensure_ascii=False,indent=2))
    print('Report:',report_path)


if __name__ == '__main__':
    main()
