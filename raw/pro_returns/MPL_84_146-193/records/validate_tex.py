"""Compile copies of the page fragments; never edit transcription files.

This is a syntax/TikZ check only.  The state macros are deliberately rendered
without editorial styling, and no image files or contextual sources are read.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PREAMBLE = r"""\documentclass{article}
\usepackage[paperwidth=50cm,paperheight=70cm,margin=1cm]{geometry}
\usepackage{amsmath,amssymb,array,graphicx,tikz-cd,xcolor}
\usetikzlibrary{calc,fit,shapes.geometric,arrows.meta}
\tikzset{ampersand replacement=\&}
\newcommand{\cotefile}[1]{\par Cote #1\par}
\newcommand{\scanpage}[1]{\par Scan #1\par}
\newcommand{\mspage}[1]{\par Page #1\par}
\newcommand{\deleted}[1]{#1}
\newcommand{\inserted}[1]{#1}
\newcommand{\margin}[1]{#1}
\newcommand{\uline}[1]{\underline{#1}}
\newcommand{\uuline}[1]{\underline{\underline{#1}}}
\newcommand{\unsure}[1]{#1}
\newcommand{\illegible}[1]{[#1 unreadable words]}
\renewcommand{\figure}[1]{#1}
\ExplSyntaxOn
\NewDocumentCommand \diagram { +m }
 {
  \tl_set:Nx \l_tmpa_tl { \tl_to_str:n {#1} }
  \regex_match:nVTF { \A\s*\\begin\s*\{array\} } \l_tmpa_tl
   { \[ #1 \] }
   {
    \regex_match:nVTF { \\begin\s*\{tikzcd\} } \l_tmpa_tl
     {
      \tl_set:Nn \l_tmpa_tl {#1}
      \tl_replace_all:Nnn \l_tmpa_tl { & } { \& }
      \tl_use:N \l_tmpa_tl
     }
     { #1 }
   }
 }
\ExplSyntaxOff
\begin{document}
"""


def main():
    engine = shutil.which('pdflatex')
    if not engine:
        raise SystemExit('No pdfLaTeX engine is available.')
    temp = Path(tempfile.mkdtemp(prefix='mpl84-tex-validation-'))
    tex_env = os.environ.copy()
    # The supplied runtime has installed TeX packages but an incomplete ls-R
    # database.  Use direct filesystem lookup only in these subprocesses.
    tex_env['TEXMF'] = '{/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf,/var/lib/texmf}'
    tex_env['TEXFORMATS'] = str(temp) + os.pathsep
    fmt = subprocess.run(
        ['pdftex', '-ini', '-etex', '-interaction=nonstopmode', '-halt-on-error',
         '-jobname=pdflatex', '-progname=pdflatex', 'pdflatex.ini'],
        cwd=temp, env=tex_env, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, text=True, timeout=60)
    (temp / 'format_build_stdout.txt').write_text(fmt.stdout, encoding='utf-8')
    if fmt.returncode:
        raise SystemExit('Local format build failed:\n' + fmt.stdout[-4000:])
    snapshots = []
    for page in sorted((ROOT / 'pages').glob('*.tex')):
        raw = page.read_bytes()
        run_dir = temp / page.stem
        run_dir.mkdir()
        (run_dir / page.name).write_bytes(raw)
        wrapper = PREAMBLE + '\\input{' + page.name + '}\n\\end{document}\n'
        (run_dir / 'wrapper.tex').write_text(wrapper, encoding='utf-8')
        snapshots.append((page, run_dir, hashlib.sha256(raw).hexdigest()))

    def compile_page(item):
        page, run_dir, digest = item
        proc = subprocess.run(
            [engine, '-draftmode', '-interaction=nonstopmode', '-halt-on-error',
             '-file-line-error', 'wrapper.tex'],
            cwd=run_dir, env=tex_env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, timeout=60)
        output = proc.stdout
        (run_dir / 'stdout.txt').write_text(output, encoding='utf-8')
        diagnostics = []
        lines = output.splitlines()
        if proc.returncode:
            for index, line in enumerate(lines):
                if (line.startswith('./') and ':' in line) or line.startswith('!'):
                    diagnostics.append('\n'.join(lines[index:index + 9]))
            if not diagnostics:
                diagnostics = ['\n'.join(lines[-25:])]
        return {'file': str(page.relative_to(ROOT)), 'sha256': digest,
                'returncode': proc.returncode, 'diagnostics': diagnostics,
                'temporary_run_directory': str(run_dir)}

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(compile_page, snapshots))
    report = {'utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
              'engine': engine, 'purpose': 'Syntax and TikZ compilation only; no visual or semantic validation.',
              'harness_notes': 'State macros have identity-style definitions; diagram wrappers put raw arrays in math mode and replace alignment ampersands with the tikz-cd ampersand-replacement command. A temporary local pdfLaTeX format and subprocess-only TEXMF override accommodate the runtime installation.',
              'snapshot_root': str(temp), 'pages': results}
    dest = ROOT / 'records' / 'tex_validation.json'
    dest.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    failed = [r for r in results if r['returncode']]
    print(f'Compiled {len(results)} copied fragments: {len(results)-len(failed)} passed, {len(failed)} failed.')
    for item in failed:
        print(item['file'])
        print('\n'.join(item['diagnostics']))
    print('Report:', dest)


if __name__ == '__main__':
    main()
