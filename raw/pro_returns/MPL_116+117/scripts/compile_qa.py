#!/usr/bin/env python3
"""Compile the manuscript fragments for structural QA without editing them.

The wrapper macros are deliberately transparent in both text and math mode.
This harness is not a deliverable edition or a diplomatic rendering; it only
checks that the source can be parsed by LaTeX/TikZ. No OCR is performed.

Usage: python compile_qa.py WORK_DIRECTORY [--engine xelatex]
Compiler output and a content-suppressed error report go under working/qa.
"""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

PAGES = [(116, n) for n in (*range(2, 9), 10, 11)] + [(117, n) for n in range(2, 27)]
PREAMBLE = r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=20mm]{geometry}
\usepackage{fontspec}
\setmainfont{lmroman10-regular.otf}[Path=/usr/share/texmf/fonts/opentype/public/lm/,BoldFont=lmroman10-bold.otf,ItalicFont=lmroman10-italic.otf,BoldItalicFont=lmroman10-bolditalic.otf]
\usepackage{amsmath,amssymb,mathtools}
\usepackage{tikz,tikz-cd}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,decorations.markings,patterns,positioning,calc,shapes.geometric}
\IfFileExists{ulem.sty}{\usepackage[normalem]{ulem}}{}
\providecommand{\uline}[1]{#1}
\providecommand{\uuline}[1]{#1}
\usepackage{textcomp}
\usepackage{xcolor}
\usepackage{graphicx}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\newcommand{\cotefile}[1]{\par\section*{Cote #1}}
\newcommand{\scanpage}[1]{\par\subsection*{Scan #1}}
\newcommand{\mspage}[1]{\par\textit{Manuscript page #1}\par}
\long\def\deleted#1{#1}
\long\def\inserted#1{#1}
\long\def\margin#1{#1}
\long\def\unsure#1{#1}
\long\def\illegible#1{[\text{illegible: #1}]}
\tikzcdset{ampersand replacement=\&}
\ExplSyntaxOn
\NewDocumentCommand{\diagram}{+m}{
  \tl_set:Nn \l_tmpa_tl {#1}
  \tl_if_in:NnT \l_tmpa_tl {\begin{tikzcd}}
    {\tl_replace_all:Nnn \l_tmpa_tl {&} {\&}}
  \tl_use:N \l_tmpa_tl
}
\ExplSyntaxOff
\long\def\figure#1{#1}
\begin{document}
'''


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('work_directory', type=Path)
    parser.add_argument('--engine', default='xelatex', choices=['lualatex','xelatex','pdflatex'])
    parser.add_argument('--timeout', type=int, default=180)
    args=parser.parse_args()
    root=args.work_directory.resolve()
    qa=root/'working'/'qa'
    qa.mkdir(parents=True, exist_ok=True)
    compiler=shutil.which(args.engine)
    if not compiler:
        print(f'Compiler unavailable: {args.engine}')
        return 2
    files=[root/'pages'/f'MPL_116+117_{c}_scan{n:03d}.tex' for c,n in PAGES]
    missing=[str(p) for p in files if not p.is_file()]
    if missing:
        print('Missing expected page files:\n'+'\n'.join(missing))
        return 2
    preamble=PREAMBLE
    if args.engine=='pdflatex':
        preamble=re.sub(r'\\usepackage\{fontspec\}\n\\setmainfont[^\n]*',
                        lambda _: '\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{lmodern}',
                        preamble)
    env=os.environ.copy()
    texvar=qa/'texmf-var'
    formats=qa/'formats'
    texconfig=qa/'texmf-config'
    for directory in (texvar, formats, texconfig):
        directory.mkdir(exist_ok=True)
    # The container has the TeX distribution but lacks its ls-R database and
    # prebuilt formats. Direct recursive lookup and local format files avoid
    # touching any system directory.
    env['TEXMF']='{'+str(texvar)+',/usr/share/texmf,/usr/share/texlive/texmf-dist}'
    env['TEXMFVAR']=str(texvar)
    env['TEXMFCONFIG']=str(texconfig)
    env['TEXMFCACHE']=str(texvar)
    env['TEXFORMATS']=str(formats)+'//:'
    env['max_print_line']='1000'
    lookup=subprocess.run(['kpsewhich',args.engine+'.fmt'],env=env,text=True,capture_output=True)
    if not lookup.stdout.strip():
        build=subprocess.run([compiler,'-ini','-etex','-interaction=nonstopmode','-no-shell-escape',
                              '-jobname='+args.engine,'-progname='+args.engine,
                              '-output-directory',str(formats),args.engine+'.ini'],
                              env=env,cwd=str(formats),text=True,stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,timeout=args.timeout)
        (qa/'format_build.log').write_text(build.stdout,encoding='utf-8')
        if build.returncode:
            print('Local TeX format generation failed; see working/qa/format_build.log.')
            return 2
    # The task's fixed filenames contain no TeX-special path characters other
    # than '+'. detokenize also protects any space in the work-directory path.
    content=preamble+'\n'.join(
        f'\\typeout{{QA-PAGE {p.name}}}\n\\input{{\\detokenize{{{p}}}}}\n\\clearpage'
        for p in files
    )+'\n\\end{document}\n'
    harness=qa/'structural_qa.tex'
    harness.write_text(content,encoding='utf-8')
    cmd=[compiler,'-interaction=nonstopmode','-file-line-error','-no-shell-escape',
         '-output-directory',str(qa),str(harness)]
    try:
        result=subprocess.run(cmd,cwd=str(root),env=env,text=True,stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,timeout=args.timeout)
        raw=result.stdout
        status=result.returncode
    except subprocess.TimeoutExpired as exc:
        raw=exc.stdout or ''
        if isinstance(raw,bytes): raw=raw.decode('utf-8','replace')
        status=124
    (qa/'compiler_stdout.log').write_text(raw,encoding='utf-8')
    # Deliberately suppress source excerpts from the model-facing report.
    # They remain in the compiler log for the transcriber if needed.
    errors=[]
    current='unknown input'
    for line in raw.splitlines():
        if line.startswith('QA-PAGE '):
            current=line[len('QA-PAGE '):].strip()
        if re.search(r'\.tex:\d+:',line):
            errors.append(line.strip())
        elif line.startswith('! '):
            errors.append(f'{current}: {line.strip()}')
        elif 'Fatal error occurred' in line or 'Emergency stop' in line:
            errors.append(f'{current}: {line.strip()}')
    report=[f'Engine: {args.engine}',f'Exit status: {status}',
            f'Input files: {len(files)}',f'Compiler error entries: {len(errors)}']
    report.extend(errors)
    if status==0:
        report.append('PASS: compiler completed. This is a structural check only.')
    elif not errors:
        report.append('Compiler failed without a standard file-line diagnostic; inspect compiler_stdout.log locally.')
    report_text='\n'.join(report)+'\n'
    (qa/'structural_errors.txt').write_text(report_text,encoding='utf-8')
    print(report_text,end='')
    return 0 if status==0 else 1

if __name__=='__main__':
    sys.exit(main())
