#!/usr/bin/env python3
"""Mechanical LaTeX compilation only; never edits manuscript pages or records.

Usage: python scripts/verify_latex.py [SCAN ...]
With no scan arguments, compile all saved page fragments. The generated format,
wrappers and logs remain outside the deliverable tree, in ../tex_mechanical_qa.
No OCR, source-image access, context access, audit logging, freezing or upload.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import os, subprocess, json, hashlib, re, sys, shutil

ROOT = Path(__file__).resolve().parent.parent
QA = ROOT.parent / 'tex_mechanical_qa'
QA.mkdir(exist_ok=True)
ENV = os.environ.copy()
# Some installations have the packages but lack a usable ls-R database.
# The fallback removes the database-only (!!) search requirement for this run.
if not shutil.which('pdftex') or not shutil.which('kpsewhich'):
    raise SystemExit('pdftex and kpsewhich are required; no sources were changed.')
lookup = subprocess.run(['kpsewhich', 'tikz-cd.sty'], capture_output=True, text=True)
if not lookup.stdout.strip():
    trees = ['/usr/share/texlive/texmf-dist', '/usr/share/texmf', '/etc/texmf']
    trees = [tree for tree in trees if Path(tree).is_dir()]
    if not trees:
        raise SystemExit('No usable installed TeX tree was found.')
    ENV['TEXMF'] = '{' + ','.join(trees) + '}'
ENV['TEXMFVAR'] = str(QA / 'texmf-var')
ENV['TEXMFCONFIG'] = str(QA / 'texmf-config')
for key in ['TEXMFVAR', 'TEXMFCONFIG']:
    Path(ENV[key]).mkdir(exist_ok=True)
if not (QA / 'qa_pdflatex.fmt').exists():
    build = subprocess.run(
        ['pdftex', '-ini', '-etex', '-no-shell-escape',
         '-interaction=nonstopmode', '-halt-on-error',
         '-jobname=qa_pdflatex', 'pdflatex.ini'],
        cwd=QA, env=ENV, capture_output=True, text=True, timeout=60)
    (QA / 'format_build.stdout').write_text(build.stdout + '\n' + build.stderr)
    if build.returncode != 0:
        raise SystemExit('Temporary format build failed; see format_build.stdout.')

PREAMBLE = r'''\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,tikz-cd,graphicx}
\usetikzlibrary{arrows.meta,decorations.pathmorphing,decorations.markings,decorations.pathreplacing,calc,positioning,shapes.geometric}
\newcommand{\cotefile}[1]{\par Cote #1\par}
\newcommand{\scanpage}[1]{\clearpage\typeout{SCAN #1}\noindent Scan #1\par}
\newcommand{\mspage}[1]{#1}
\newcommand{\deleted}[1]{#1}
\newcommand{\inserted}[1]{#1}
\newcommand{\margin}[1]{#1}
% Preserve the grouping of underlined mathematical expressions and exponents.
\newcommand{\uline}[1]{\ifmmode\underline{#1}\else#1\fi}
\newcommand{\uuline}[1]{\ifmmode\underline{\underline{#1}}\else#1\fi}
\newcommand{\unsure}[1]{#1}
\newcommand{\illegible}[1]{[#1]}
\renewcommand{\figure}[1]{#1}
% A transparent syntax-checking wrapper, not a diplomatic rendering design.
% Retokenization permits raw & even in diagrams nested in another marker.
\long\def\diagram#1{\begingroup\endlinechar=-1\relax\scantokens{#1}\endgroup}
\begin{document}
'''


def check(path):
    scan = int(re.search(r'scan([0-9]+)', path.name).group(1))
    work = QA / 'runs' / f'scan{scan}'
    work.mkdir(parents=True, exist_ok=True)
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    wrapper = work / 'wrapper.tex'
    wrapper.write_text(PREAMBLE + '\\input{' + str(path) + '}\n\\end{document}\n')
    command = ['pdftex', '-fmt=' + str(QA / 'qa_pdflatex'),
               '-draftmode', '-no-shell-escape', '-interaction=nonstopmode',
               '-file-line-error', '-halt-on-error', 'wrapper.tex']
    result = subprocess.run(command, cwd=work, env=ENV,
                            capture_output=True, text=True, timeout=90)
    output = result.stdout + '\n' + result.stderr
    (work / 'compiler.stdout').write_text(output)
    errors = []
    for line in output.replace('.\ntex:', '.tex:').splitlines():
        if re.search(r'\.(?:tex|sty|def):[0-9]+:', line) or line.startswith('!'):
            errors.append(line)
    warnings = [re.sub(r'\s+', ' ', value).strip() for value in
                re.findall(r'LaTeX Warning: Command.*?(?:\n\n|$)', output, re.S)]
    missing = re.findall(r'Missing character:[^\n]*', output)
    after = hashlib.sha256(path.read_bytes()).hexdigest()
    report = dict(scan=scan, file=str(path), exit_code=result.returncode,
                  errors=errors, command_warnings=warnings,
                  missing_glyphs=missing, source_sha256=before,
                  source_changed_during_check=before != after,
                  compiler_log=str(work / 'wrapper.log'))
    (work / 'result.json').write_text(json.dumps(report, indent=2) + '\n')
    return report


scans = {int(value) for value in sys.argv[1:]}
paths = [path for path in sorted((ROOT / 'pages').glob('*.tex'))
         if not scans or int(re.search(r'scan([0-9]+)', path.name).group(1)) in scans]
started = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
results = []
with ThreadPoolExecutor(max_workers=4) as pool:
    jobs = [pool.submit(check, path) for path in paths]
    for job in as_completed(jobs):
        result = job.result()
        results.append(result)
        print(json.dumps({'scan': result['scan'], 'exit_code': result['exit_code'],
                          'command_warning_count': len(result['command_warnings']),
                          'missing_glyph_count': len(result['missing_glyphs']),
                          'errors': result['errors']}), flush=True)
results.sort(key=lambda result: result['scan'])
summary = dict(started=started, checked=len(results),
               passed=sum(result['exit_code'] == 0 for result in results),
               failed=[result['scan'] for result in results if result['exit_code'] != 0],
               changed_during_check=[result['scan'] for result in results
                                     if result['source_changed_during_check']],
               warning_scans=[result['scan'] for result in results
                               if result['command_warnings'] or result['missing_glyphs']])
report_name = 'report.json' if not scans else 'report_' + '_'.join(map(str, sorted(scans))) + '.json'
(QA / report_name).write_text(json.dumps(dict(summary=summary, results=results), indent=2) + '\n')
print(json.dumps(summary))
sys.exit(1 if summary['failed'] or summary['changed_during_check'] else 0)
