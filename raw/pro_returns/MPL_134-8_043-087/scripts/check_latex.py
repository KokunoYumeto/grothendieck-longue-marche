#!/usr/bin/env python3
"""Compile manuscript page fragments individually without modifying them.

Run from any directory. Results and generated TeX/PDF/cache files stay under
the sibling scratch folder texqa-cache. Only the small JSON report is retained
under records. No scan image or context archive is ever opened by this tool.
The optional positional arguments are three-digit scan numbers. With no
arguments all current page fragments are checked. A missing TeX format is
generated in the isolated QA cache from the installed TeX Live sources.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
QA = ROOT.parent / 'texqa-cache'
PREAMBLE = ROOT / 'scripts' / 'latex_qa_preamble.tex'


def env_for_tex():
    env = dict(os.environ)
    # The installed package tree is complete, but the image may lack ls-R.
    # Omit TeX's !! database-only prefix so kpathsea can use the actual files.
    env['TEXMF'] = '{/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}'
    env['TEXMFVAR'] = str(QA / 'texmf-var')
    env['TEXMFCONFIG'] = str(QA / 'texmf-config')
    env['TEXMFHOME'] = str(QA / 'texmf-home')
    env['TEXFORMATS'] = str(QA / 'formats') + ':'
    return env


def ensure_format(env):
    target = QA / 'formats'
    target.mkdir(parents=True, exist_ok=True)
    if (target / 'pdflatex.fmt').exists():
        return
    command = ['pdftex', '-ini', '-etex', '-interaction=nonstopmode',
               '-halt-on-error', '-jobname=pdflatex', '-progname=pdflatex',
               '-output-directory=' + str(target), 'pdflatex.ini']
    run = subprocess.run(command, cwd=target, env=env, text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         timeout=120)
    (target / 'format-build.txt').write_text(run.stdout)
    if run.returncode:
        raise RuntimeError('TeX format generation failed; see ' +
                           str(target / 'format-build.txt'))


def structural_checks(path):
    text = path.read_text()
    # Strip comments without changing line numbers; escaped percent is text.
    text = re.sub(r'(?<!\\)%[^\n]*', '', text)
    issues = []
    braces = []
    envs = []
    for line, row in enumerate(text.splitlines(), 1):
        for match in re.finditer(r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}|(?<!\\)[{}]', row):
            start, end = match.group(1), match.group(2)
            if start:
                envs.append((start, line))
            elif end:
                if not envs or envs[-1][0] != end:
                    issues.append({'line': line, 'issue': 'environment end mismatch: ' + end})
                else:
                    envs.pop()
            elif match.group() == '{':
                braces.append(line)
            elif braces:
                braces.pop()
            else:
                issues.append({'line': line, 'issue': 'unmatched closing brace'})
    issues.extend({'line': line, 'issue': 'unclosed brace'} for line in braces)
    issues.extend({'line': line, 'issue': 'unclosed environment: ' + name} for name, line in envs)
    return issues


def compile_page(path, env):
    scan_match = re.search(r'scan(\d+)\.tex$', path.name)
    scan = scan_match.group(1) if scan_match else 'combined'
    output = QA / path.parent.name / ('scan' + scan)
    output.mkdir(parents=True, exist_ok=True)
    source_bytes = path.read_bytes()
    snapshot = output / path.name
    snapshot.write_bytes(source_bytes)
    wrapper = output / ('qa_scan' + scan + '.tex')
    wrapper.write_text(PREAMBLE.read_text() + '\n\\input{' + snapshot.as_posix() + '}\n\\end{document}\n')
    command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
               '-file-line-error', '-output-directory=' + str(output), str(wrapper)]
    run = subprocess.run(command, cwd=ROOT, env=env, text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         timeout=60 if scan_match else 180)
    (output / 'compiler-output.txt').write_text(run.stdout)
    result = {'scan': scan, 'file': ('pages/' if scan_match else '') + path.name,
              'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
              'returncode': run.returncode, 'structural': structural_checks(snapshot),
              'log': str(output / 'compiler-output.txt'),
              'errors': [], 'warnings': []}
    for line in run.stdout.splitlines():
        if re.search(r':\d+:|^! |^l\.\d+', line):
            result['errors'].append(line)
        elif any(s in line for s in ('Warning:', 'Overfull', 'Underfull', 'Missing character')):
            result['warnings'].append(line)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('scans', nargs='*')
    parser.add_argument('--source-dir', type=Path, default=ROOT / 'pages')
    parser.add_argument('--fragment', type=Path, help='Compile this one fragment, e.g. the combined transcription.')
    parser.add_argument('--report', type=Path, default=ROOT / 'records' / 'latex_qa_report.json')
    args = parser.parse_args()
    QA.mkdir(parents=True, exist_ok=True)
    paths = [args.fragment.resolve()] if args.fragment else sorted(args.source_dir.glob('*.tex'))
    if args.scans:
        wanted = {str(int(x)).zfill(3) for x in args.scans}
        paths = [p for p in paths if re.search(r'scan(\d+)\.tex$', p.name).group(1) in wanted]
    env = env_for_tex()
    ensure_format(env)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(lambda p: compile_page(p, env), paths))
    report = {'checked_utc': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
              'scope': 'TeX syntax only; no image or context reading',
              'source_dir': str(args.fragment or args.source_dir), 'pages': results}
    report_path = args.report
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    for result in results:
        print(result['scan'], 'PASS' if result['returncode'] == 0 and not result['structural'] else 'FAIL')
        for issue in result['errors'][:6]:
            print('  ' + issue)
        for issue in result['structural']:
            print('  line', issue['line'], issue['issue'])
    print('Report:', report_path)
    return int(any(x['returncode'] or x['structural'] for x in results))


if __name__ == '__main__':
    sys.exit(main())
