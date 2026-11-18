#!/usr/bin/env python3
"""Build a disposable LaTeX harness; compile only with explicit --compile.

The manuscript fragment is referenced with \\input, never rewritten.
The rendering apparatus is editorial and does not belong in the transcription.
"""
import argparse
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

DEFAULT_ROOT = Path('/workspace/scratch/22f602b123f8/MPL_64_116-157_work')
PREAMBLE = r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{tikz,tikz-cd}
\usetikzlibrary{arrows.meta,calc,decorations.pathmorphing,positioning}
\usepackage{xcolor,cancel}
\usepackage[margin=22mm]{geometry}
\IfFileExists{ulem.sty}{\usepackage[normalem]{ulem}}{}
\providecommand{\uline}[1]{\ifmmode\underline{#1}\else
  \leavevmode\hbox{$\underline{\hbox{#1}}$}\fi}
\providecommand{\uuline}[1]{\ifmmode\underline{\underline{#1}}\else
  \leavevmode\hbox{$\underline{\underline{\hbox{#1}}}$}\fi}
\definecolor{doubtink}{RGB}{150,85,0}
\definecolor{deleteink}{RGB}{160,25,35}
\definecolor{insertink}{RGB}{20,80,170}
\definecolor{marginink}{RGB}{30,105,85}
\newsavebox{\deletedbox}
\providecommand{\sout}[1]{\sbox{\deletedbox}{#1}%
  \rlap{\raisebox{.5ex}{\rule{\wd\deletedbox}{.35pt}}}\usebox{\deletedbox}}
\newcommand{\currentcote}{64}
\newcommand{\cotefile}[1]{\gdef\currentcote{#1}}
\newif\iffirstscan\firstscantrue
\newcommand{\scanpage}[1]{\iffirstscan\firstscanfalse\else\clearpage\fi
  \noindent{\Large\bfseries Cote \currentcote\quad Scan #1}\par\medskip}
\newcommand{\mspage}[1]{\noindent\textit{Manuscript page: #1}\par\smallskip}
\newcommand{\deleted}[1]{\ifmmode{\color{deleteink}\cancel{#1}}\else
  {\color{deleteink}\textsf{[deleted:}\enspace #1\enspace\textsf{]}}\fi}
\newcommand{\inserted}[1]{\ifmmode{\color{insertink}{#1}^{\scriptscriptstyle+}}\else
  {\color{insertink}\textsuperscript{+}#1}\fi}
\newcommand{\unsure}[1]{\ifmmode{\color{doubtink}{#1}^{\scriptscriptstyle?}}\else
  {\color{doubtink}#1\textsuperscript{?}}\fi}
\newcommand{\illegible}[1]{{\color{doubtink}\textit{[#1 word(s) illegible]}}}
\newcommand{\margin}[1]{\par\smallskip\noindent
  {\color{marginink}\textsf{[margin]}\enspace #1}\par\smallskip}
\def\qaalignmenttab{&}
\begingroup\catcode`\&=\active
\gdef\qaactivateampersand{\catcode`\&=\active\let&\qaalignmenttab}
\endgroup
\newcommand{\diagram}{\begingroup\qaactivateampersand\qadiagram}
\newcommand{\qadiagram}[1]{\ifmmode #1\else\[#1\]\fi\endgroup}
\renewcommand{\figure}[1]{\par\begingroup\centering #1\par\endgroup}
\setlength{\parindent}{1em}
\setlength{\parskip}{.35em}
\setlength{\emergencystretch}{2em}
\begin{document}
'''

def lookup_environment():
    """Search installed files directly despite missing ls-R; no global mutation."""
    env = os.environ.copy()
    assets = Path(env.get('MPL_TEX_ASSETS',str(DEFAULT_ROOT.parent/'MPL_64_116-157_qa'/'tex-assets')))
    env['TEXMFDBS'] = '/usr/share/texlive/texmf-dist:/usr/share/texmf'
    env['TEXINPUTS'] = (f'.:{assets / "tex"}//:/usr/share/texlive/texmf-dist/tex/latex//:'
                        '/usr/share/texlive/texmf-dist/tex/generic//:'
                        '/usr/share/texmf/tex//:')
    env['TEXFORMATS'] = str(assets/'formats')+':'+env.get('TEXFORMATS','')
    env['TEXFONTMAPS'] = (str(assets/'maps')+'//:/usr/share/texlive/texmf-dist/fonts/map//:'
                          '/usr/share/texmf/fonts/map//:')
    env['ENCFONTS'] = ('/usr/share/texlive/texmf-dist/fonts/enc//:'
                       '/usr/share/texmf/fonts/enc//:')
    env['TEXMFVAR'] = str(assets/'var')
    env['TEXMFCONFIG'] = str(assets/'config')
    env['TEXMFCACHE'] = str(assets/'cache')
    for variable, subdir in [('TFMFONTS','tfm'),('VFFONTS','vf'),
                             ('T1FONTS','type1'),('TTFONTS','truetype'),
                             ('OPENTYPEFONTS','opentype')]:
        env[variable] = (f'/usr/share/texlive/texmf-dist/fonts/{subdir}//:'
                         f'/usr/share/texmf/fonts/{subdir}//:')
    return env

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=DEFAULT_ROOT)
    parser.add_argument('--source', type=Path, help='fragment to input; default combined transcription')
    parser.add_argument('--output-dir', type=Path, help='temporary build directory; must be outside package root')
    parser.add_argument('--engine', choices=['pdflatex','xelatex','lualatex'], default='pdflatex')
    parser.add_argument('--compile', action='store_true', help='explicitly authorize compilation in temporary directory')
    parser.add_argument('--probe-only', action='store_true', help='only report binaries/package availability; create nothing')
    args = parser.parse_args()
    env = lookup_environment()
    for executable in ['pdflatex','xelatex','lualatex','latexmk','kpsewhich']:
        print(f'{executable}: {shutil.which(executable) or "MISSING"}')
    if shutil.which('kpsewhich'):
        for name in ['article.cls','amsmath.sty','amssymb.sty','mathtools.sty',
                     'tikz.sty','tikz-cd.sty','xcolor.sty','geometry.sty',
                     'cancel.sty','ulem.sty','french.ldf',args.engine+'.fmt']:
            result = subprocess.run(['kpsewhich',name],env=env,text=True,capture_output=True)
            print(f'{name}: {result.stdout.strip() or "MISSING under fallback lookup"}')
    if args.probe_only:
        return 0
    root = args.root.resolve()
    source = (args.source or root/'MPL_64_116-157_transcription.tex').resolve()
    if not source.is_file():
        parser.error(f'fragment does not exist: {source}')
    if any(char in str(source) for char in '{}%#\n\r'):
        parser.error('source path contains characters unsafe in a TeX input filename')
    build = (args.output_dir.resolve() if args.output_dir else
             Path(tempfile.mkdtemp(prefix='MPL_64_116-157_latex_',dir=root.parent)))
    if build.is_relative_to(root):
        parser.error('build directory must remain outside the deliverable root')
    build.mkdir(parents=True,exist_ok=True)
    main_file = build/'main.tex'
    main_file.write_text(PREAMBLE+'\\input{'+source.as_posix()+'}\n\\end{document}\n',encoding='utf-8')
    (build/'HARNESS_ASSUMPTIONS.txt').write_text(
        'Editorial rendering harness, not part of the diplomatic text.\n'
        'Uses pdfLaTeX-compatible UTF-8 input and T1 text fonts by default.\n'
        'No French babel: French language package is unavailable.\n'
        'ulem when available; otherwise boxed text/math underline fallbacks.\n'
        'Fallback underlines cannot wrap; text deletions use red editorial brackets and can span paragraphs.\n'
        'Math deletion uses cancel; inserted and doubtful text has visible markers.\n'
        'Margin notes print in reading order with a colored editorial label.\n'
        'Each scan begins on a fresh rendered page; this need not match manuscript pagination.\n'
        'figure macro is repurposed for the required TikZ drawing wrapper.\n'
        'diagram reads active ampersands for TikZ; ordinary arrays also supported.\n'
        'Do not nest an entire diagram inside another capturing macro; mark individual objects instead.\n'
        'TEXMFDBS/TEXINPUTS and font lookup paths are process-local fallbacks.\n'
        'Local format/map assets may be selected with MPL_TEX_ASSETS; no setup is run automatically.\n',
        encoding='utf-8')
    print(f'Harness: {main_file}')
    print(f'Source: {source}')
    if not args.compile:
        print('Prepared only; compilation was not requested.')
        return 0
    original_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    command = [args.engine,'-no-shell-escape','-interaction=nonstopmode',
               '-halt-on-error','-file-line-error',f'-output-directory={build}',str(main_file)]
    result = subprocess.run(command,cwd=build,env=env,text=True,capture_output=True)
    (build/'compile.stdout.txt').write_text(result.stdout,encoding='utf-8')
    (build/'compile.stderr.txt').write_text(result.stderr,encoding='utf-8')
    unchanged = original_hash == hashlib.sha256(source.read_bytes()).hexdigest()
    print(f'Compiler exit: {result.returncode}; source unchanged: {unchanged}')
    print(f'Log: {build / "main.log"}')
    if result.returncode:
        print(result.stdout[-6000:])
        print(result.stderr[-2000:])
    return result.returncode if unchanged else 2

if __name__ == '__main__':
    raise SystemExit(main())
