#!/usr/bin/env python3
"""Mechanical checks only: this script never opens scans or contextual sources.

Run from any directory:
    python records/check_mechanical.py [--final] [--compile]

The optional wrapper deliberately renders editorial macros transparently. It
checks LaTeX syntax, not the fidelity or visual presentation of the transcription.
No page, inventory, doubts, or progress file is modified.
"""
from __future__ import annotations

import argparse
import csv
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [95, 96, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108,
            109, 110, 111, 112, 117, 118, 124, 126, 129, 130, 131, 132,
            133, 135, 137, 138, 139, 140]
PREFIX = 'MPL_29_095-140'
FIELDS = ['cote', 'scan', 'sheet_kind', 'element', 'kind', 'position',
          'first_words_or_objects', 'transcribed']
KINDS = {'text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion'}
SHEETS = {'text', 'typed', 'reused_typed', 'cancelled_draft', 'cover'}


def visible_tex(source: str) -> str:
    """Remove TeX comments while preserving newlines and source offsets."""
    output = []
    for line in source.splitlines(keepends=True):
        cut = len(line)
        for i, char in enumerate(line):
            if char != '%':
                continue
            nslash = 0
            j = i - 1
            while j >= 0 and line[j] == '\\':
                nslash += 1
                j -= 1
            if nslash % 2 == 0:
                cut = i
                break
        output.append(line[:cut] + ''.join('\n' if c == '\n' else ' ' for c in line[cut:]))
    return ''.join(output)


def lexical_issues(source: str) -> list[str]:
    text = visible_tex(source)
    issues = []
    stack = []
    # Consume TeX control sequences first; escaped braces are not grouping tokens.
    for token in re.finditer(r'\\(?:[A-Za-z@]+|[^\n])|[{}]', text):
        char = token.group()
        line = text.count('\n', 0, token.start()) + 1
        if char == '{':
            stack.append(line)
        elif char == '}':
            if stack:
                stack.pop()
            else:
                issues.append(f'line {line}: unmatched closing brace')
    for line in stack:
        issues.append(f'line {line}: unclosed opening brace')
    envs = []
    for token in re.finditer(r'\\(begin|end)\s*\{([^{}]+)\}', text):
        line = text.count('\n', 0, token.start()) + 1
        action, name = token.groups()
        if action == 'begin':
            envs.append((name, line))
        elif not envs or envs[-1][0] != name:
            issues.append(f'line {line}: unmatched end of environment {name}')
        else:
            envs.pop()
    for name, line in envs:
        issues.append(f'line {line}: unclosed environment {name}')
    for match in re.finditer(r'\\(includegraphics|includepdf|input|include|documentclass|usepackage|newcommand|renewcommand)\b', text):
        line = text.count('\n', 0, match.start()) + 1
        issues.append(f'line {line}: forbidden external inclusion or preamble command {match.group()}')
    for match in re.finditer(r'\b(?:TODO|TBD|PLACEHOLDER)\b|\[\s*\.\.\.\s*\]', text, re.I):
        line = text.count('\n', 0, match.start()) + 1
        issues.append(f'line {line}: possible editorial placeholder {match.group()!r}; inspect manually')
    return issues


def compile_pages(pages: list[Path]) -> tuple[bool, list[str]]:
    engine = shutil.which('pdflatex') or shutil.which('lualatex')
    if not engine:
        return False, ['No local LaTeX engine; compilation was not attempted.']
    # No ulem dependency: transparent editorial macros avoid changing content.
    wrapper = r'''\documentclass{article}
\ifdefined\pdfmapfile
\pdfmapfile{+cm.map}
\pdfmapfile{+cmextra.map}
\pdfmapfile{+euler.map}
\pdfmapfile{+symbols.map}
\pdfmapfile{+latxfont.map}
\pdfmapfile{+lm.map}
\fi
\usepackage{lmodern}
\usepackage[paperwidth=32cm,paperheight=45cm,margin=2cm]{geometry}
\usepackage{amsmath,amssymb,tikz-cd}
\usetikzlibrary{arrows.meta,shapes.geometric}
\setlength{\parindent}{0pt}
\long\def\cotefile#1{\par Cote #1\par}
\long\def\scanpage#1{\clearpage\section*{Scan #1}}
\long\def\mspage#1{\par Manuscript page #1\par}
\long\def\deleted#1{#1}
\long\def\inserted#1{#1}
\long\def\unsure#1{#1}
\long\def\illegible#1{[illegible: #1]}
\long\def\uline#1{#1}
\long\def\uuline#1{#1}
\long\def\margin#1{\par\begingroup\small #1\par\endgroup}
\long\def\diagram#1{\par\begingroup\expandafter\scantokens\expandafter{\detokenize{#1}}\endgroup\par}
\long\def\figure#1{\par\noindent #1\par}
\begin{document}
'''
    wrapper += '\n'.join(r'\input{' + str(p) + '}' for p in pages)
    wrapper += '\n\\end{document}\n'
    with tempfile.TemporaryDirectory(prefix='mpl29-tex-') as directory:
        env = os.environ.copy()
        format_name = Path(engine).name
        lookup = subprocess.run(['kpsewhich', format_name + '.fmt'], capture_output=True, text=True)
        format_report = []
        if not lookup.stdout.strip():
            # This runtime has the TeX sources but no prebuilt formats. Build one
            # wholly inside this temporary directory; no system configuration or
            # persistent TeX cache is changed, and no network is used.
            if format_name != 'pdflatex' or not shutil.which('pdftex'):
                return False, [f'{format_name} format unavailable; temporary compilation not attempted.']
            (Path(directory) / 'language.dat').write_text('english hyphen.tex\n', encoding='utf-8')
            env['TEXINPUTS'] = directory + ':' + env.get('TEXINPUTS', '')
            env['TEXFORMATS'] = directory + ':' + env.get('TEXFORMATS', '')
            built = subprocess.run(['pdftex', '-ini', '-etex', '-jobname=pdflatex',
                                    '-progname=pdflatex', '-no-shell-escape',
                                    '-interaction=nonstopmode', 'pdflatex.ini'],
                                   cwd=directory, env=env, capture_output=True,
                                   text=True, timeout=30)
            if built.returncode or not (Path(directory) / 'pdflatex.fmt').exists():
                return False, ['Temporary format build failed.'] + (built.stdout + built.stderr).splitlines()[-12:]
            format_report.append('Built a temporary local pdflatex format from installed sources (no installation).')
        target = Path(directory) / 'qa_wrapper.tex'
        target.write_text(wrapper, encoding='utf-8')
        completed = subprocess.run([engine, '-no-shell-escape', '-interaction=nonstopmode',
                                    '-halt-on-error', '-file-line-error', target.name],
                                   cwd=directory, env=env, capture_output=True, text=True, timeout=120)
        output = completed.stdout + completed.stderr
        # Keep diagnostic lines, not manuscript content or the verbose engine log.
        lines = output.splitlines()
        diagnostic_indices = set()
        for i, line in enumerate(lines):
            if re.search(r'(Error|Undefined control sequence|^!|\.tex:\d+:)', line):
                diagnostic_indices.update(range(max(0, i - 1), min(len(lines), i + 5)))
        errors = [lines[i] for i in sorted(diagnostic_indices)]
        if completed.returncode and not errors:
            errors = lines[-12:]
        overfull = sum('Overfull ' in line for line in lines)
        report = format_report + [f'{Path(engine).name}: exit {completed.returncode}; {overfull} overfull-box warnings in the temporary syntax wrapper.']
        report.extend(errors)
        return completed.returncode == 0, report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--final', action='store_true', help='Require all 31 expected pages and final audit records.')
    parser.add_argument('--compile', action='store_true', help='Compile a temporary transparent-macro wrapper.')
    args = parser.parse_args()
    errors = []
    pages = sorted((ROOT / 'pages').glob(f'{PREFIX}_29_scan*.tex'))
    scans = []
    sources = []
    for page in pages:
        match = re.fullmatch(rf'{PREFIX}_29_scan(\d{{3}})\.tex', page.name)
        if not match:
            errors.append(f'Unexpected page filename: {page.name}')
            continue
        scan = int(match.group(1))
        scans.append(scan)
        source = page.read_text(encoding='utf-8')
        sources.append(source)
        errors.extend(f'{page.name}: {issue}' for issue in lexical_issues(source))
        ids = re.findall(r'\\scanpage\s*\{(\d+)\}', visible_tex(source))
        if ids != [str(scan)]:
            errors.append(f'{page.name}: scanpage declarations {ids}, expected [{scan}]')
        cote = re.findall(r'\\cotefile\s*\{([^{}]+)\}', visible_tex(source))
        if cote != (['29'] if scan == EXPECTED[0] else []):
            errors.append(f'{page.name}: unexpected cotefile declarations {cote}')
    unexpected = set(scans) - set(EXPECTED)
    if unexpected:
        errors.append(f'Unexpected scans: {sorted(unexpected)}')
    if args.final and scans != EXPECTED:
        errors.append(f'Final page set incomplete: missing {sorted(set(EXPECTED)-set(scans))}')
    inventory = ROOT / f'{PREFIX}_inventory.csv'
    rows = []
    with inventory.open(newline='', encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            errors.append(f'Inventory columns differ from required schema: {reader.fieldnames}')
        rows = list(reader)
    counts = {scan: 0 for scan in scans}
    elements = set()
    for n, row in enumerate(rows, 2):
        try:
            scan = int(row['scan'])
        except (ValueError, KeyError):
            errors.append(f'Inventory row {n}: invalid scan')
            continue
        counts[scan] = counts.get(scan, 0) + 1
        if row.get('cote') != '29' or row.get('transcribed') != 'yes':
            errors.append(f'Inventory row {n}: wrong cote or not marked yes')
        if row.get('sheet_kind') not in SHEETS or row.get('kind') not in KINDS:
            errors.append(f'Inventory row {n}: unknown sheet or element kind')
        if any(not row.get(field) for field in ['element', 'position', 'first_words_or_objects']):
            errors.append(f'Inventory row {n}: required field empty')
        if row.get('element') in elements:
            errors.append(f'Inventory row {n}: duplicate element identifier')
        elements.add(row.get('element'))
    for scan in scans:
        if not counts.get(scan):
            errors.append(f'Scan {scan}: no inventory rows')
    for scan in set(counts) - set(scans):
        errors.append(f'Inventory has scan {scan} without a saved page file')
    progress = (ROOT / 'progress.log').read_text(encoding='utf-8')
    done = [int(n) for n in re.findall(r'^29 scan (\d+) done ', progress, re.M)]
    if sorted(done) != scans:
        errors.append('Progress done entries differ from saved page set (or contain duplicates).')
    if args.final:
        audited = {int(n) for n in re.findall(r'^scan (\d+) audited ', progress, re.M)}
        if audited != set(EXPECTED):
            errors.append(f'Final audit entries incomplete: {sorted(set(EXPECTED)-audited)}')
        if 'transcription frozen ' not in progress:
            errors.append('No transcription-frozen entry in progress.log.')
        combined_path = ROOT / f'{PREFIX}_transcription.tex'
        if not combined_path.exists():
            errors.append('Combined transcription file is missing.')
        else:
            combined = combined_path.read_text(encoding='utf-8')
            errors.extend(f'{combined_path.name}: {issue}' for issue in lexical_issues(combined))
            offset = 0
            for page, source in zip(pages, sources):
                found = combined.find(source.strip(), offset)
                if found < 0:
                    errors.append(f'Combined transcription lacks the exact current text of {page.name} in order.')
                else:
                    offset = found + len(source.strip())
    print(f'Mechanical snapshot: {len(scans)}/31 pages; {len(rows)} inventory elements; {len(done)} done entries.')
    for error in errors:
        print('ISSUE:', error)
    compile_ok = True
    if args.compile:
        compile_ok, report = compile_pages(pages)
        for line in report:
            print('COMPILE:', line)
    if not errors:
        print('PASS: structural checks for the current snapshot.')
    print('Scope: mechanical verification only; no scan reading or mathematical checking.')
    return int(bool(errors) or not compile_ok)


if __name__ == '__main__':
    raise SystemExit(main())
