#!/usr/bin/env python3
"""Compile snapshot copies of page fragments for syntax checks, without editing originals."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[a3paper,margin=15mm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,mathrsfs}
\usepackage{tikz,tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathreplacing,calc,positioning,patterns,shapes.geometric}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\newcommand{\cotefile}[1]{\par Cote #1\par}
\newcommand{\scanpage}[1]{\par Scan #1\par}
\newcommand{\mspage}[1]{\par Manuscript #1\par}
\newcommand{\deleted}{}
\newcommand{\inserted}{}
\newcommand{\margin}{}
\def\diagram{\afterassignment\diagramopen\let\diagrambrace=}
\def\diagramopen{\begingroup\futurelet\diagramfirst\diagramchoose}
\newif\ifdiagramwrap
\def\diagramchoose{\diagramwraptrue\ifmmode\diagramwrapfalse\fi\ifx\diagramfirst$\diagramwrapfalse\fi\ifx\diagramfirst\[\diagramwrapfalse\fi\ifx\diagramfirst\(\diagramwrapfalse\fi\ifdiagramwrap\[\def\diagramclose{\]\endgroup}\else\def\diagramclose{\endgroup}\fi\bgroup\aftergroup\diagramclose}
\renewcommand{\figure}{}
\newcommand{\unsure}{}
\newcommand{\illegible}[1]{\text{[unreadable #1]}}
\newcommand{\uline}{}
\newcommand{\uuline}{}
\begin{document}
"""

def run_one(source, dest, engine, env):
    dest.mkdir(parents=True, exist_ok=True)
    (dest / 'tex_cache').mkdir(exist_ok=True)
    original = source.read_bytes()
    copied = dest / 'fragment.tex'
    copied.write_bytes(original)
    harness = dest / 'check.tex'
    harness.write_text(PREAMBLE + '\\input{fragment.tex}\n\\end{document}\n', encoding='utf-8')
    command = [engine, '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error',
               '-file-line-error', 'check.tex']
    try:
        proc = subprocess.run(command, cwd=dest, env=env, capture_output=True, text=True,
                              encoding='utf-8', errors='replace', timeout=45)
        output = proc.stdout + proc.stderr
        (dest/'console.log').write_text(output, encoding='utf-8')
        lines = output.splitlines()
        # Keep error context without dumping complete manuscript passages.
        indices = [i for i,l in enumerate(lines) if 'Error:' in l or l.startswith('!') or
                   re.match(r'^\./(?:fragment|check)\.tex:\d+:',l)]
        snippets=[]
        for i in indices:
            snippets.append('\n'.join(lines[max(0,i):min(len(lines),i+9)]))
        return {'page': source.name, 'sha256': hashlib.sha256(original).hexdigest(),
                'exit_code': proc.returncode, 'errors': snippets,
                'console': str(dest/'console.log'),
                'same_as_source_after_compile': source.read_bytes()==original}
    except subprocess.TimeoutExpired:
        return {'page':source.name,'sha256':hashlib.sha256(original).hexdigest(),
                'exit_code':'timeout','errors':['Compilation exceeded 45 seconds'],
                'same_as_source_after_compile':source.read_bytes()==original}

def run_combined(sources, dest, engine, env):
    dest.mkdir(parents=True, exist_ok=True)
    (dest/'tex_cache').mkdir(exist_ok=True)
    hashes=[]
    lines=[PREAMBLE]
    for source in sources:
        data=source.read_bytes()
        (dest/source.name).write_bytes(data)
        hashes.append({'page':source.name,'sha256':hashlib.sha256(data).hexdigest()})
        lines.append('\\input{'+source.name+'}\\clearpage\n')
    lines.append('\\end{document}\n')
    (dest/'check.tex').write_text(''.join(lines),encoding='utf-8')
    try:
        proc=subprocess.run([engine,'-no-shell-escape','-interaction=nonstopmode',
                             '-halt-on-error','-file-line-error','check.tex'],
                            cwd=dest,env=env,capture_output=True,text=True,
                            encoding='utf-8',errors='replace',timeout=180)
        output=proc.stdout+proc.stderr
        (dest/'console.log').write_text(output,encoding='utf-8')
        textlines=output.splitlines()
        indices=[i for i,l in enumerate(textlines) if 'Error:' in l or l.startswith('!') or
                 re.match(r'^\./[^:]+\.tex:\d+:',l)]
        errors=['\n'.join(textlines[i:min(len(textlines),i+9)]) for i in indices]
        result={'checked_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
                'pages':len(sources),'exit_code':proc.returncode,'errors':errors,
                'console':str(dest/'console.log'),'source_hashes':hashes,
                'source_files_unchanged':all(hashlib.sha256(p.read_bytes()).hexdigest()==h['sha256'] for p,h in zip(sources,hashes)),
                'limitations':'Mechanical compilation only; no scan comparison. Editorial annotations are identity wrappers; diagram bodies are read without pre-tokenizing ampersands.'}
        (dest/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        return result
    except subprocess.TimeoutExpired:
        return {'pages':len(sources),'exit_code':'timeout','errors':['Combined compilation exceeded 180 seconds'],'source_hashes':hashes}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--build', type=Path, required=True)
    p.add_argument('--engine', default='xelatex')
    p.add_argument('--scans', nargs='*', type=int)
    p.add_argument('--workers', type=int, default=3)
    p.add_argument('--env-json', type=Path)
    p.add_argument('--combined', action='store_true')
    args=p.parse_args()
    engine=shutil.which(args.engine)
    if engine is None: raise SystemExit('TeX engine not available: '+args.engine)
    pages=sorted((args.root/'pages').glob('*.tex'))
    if args.scans:
        pages=[f for f in pages if int(re.search(r'scan(\d+)',f.name).group(1)) in args.scans]
    build=args.build.resolve();build.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy()
    if args.env_json:
        env.update(json.loads(args.env_json.read_text()))
        for key,subdir in [('TEXMFVAR','var'),('TEXMFCONFIG','config')]:
            local=build/subdir;local.mkdir(exist_ok=True)
            env[key]=str(local)
        env['TEXMFCACHE']='tex_cache'
        env['LUAOTFLOAD_CACHE']='tex_cache'
    if args.combined:
        print(json.dumps(run_combined(pages,build/'all_saved',engine,env),ensure_ascii=False,indent=2))
        return
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures=[pool.submit(run_one,f,build/f.stem,engine,env) for f in pages]
        results=[f.result() for f in futures]
    report={'checked_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'engine':engine,'pages':len(results),'passed':sum(r['exit_code']==0 for r in results),
            'limitations':'Syntax only. Editorial wrappers are identity macros; no scan comparison or reading review.',
            'results':results}
    (build/'results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
