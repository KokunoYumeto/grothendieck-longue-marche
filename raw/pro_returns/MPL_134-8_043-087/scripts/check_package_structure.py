#!/usr/bin/env python3
"""Check package metadata and TeX structure, without reading images or context.

This check does not decide whether the inventory covers every visible mark.
It checks file/scan correspondence, inventory schema, record presence, macro
names, and completion/audit log coverage. It never writes to live sources.
"""
import argparse
from collections import Counter
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PREFIX = 'MPL_134-8_043-087'
EXPECTED = set(range(43, 88)) - {60}
FIELDS = ['cote', 'scan', 'sheet_kind', 'element', 'kind', 'position', 'first_words_or_objects', 'transcribed']
KINDS = {'text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion'}
SHEET_KINDS = {'text', 'reused_typed', 'cancelled_draft', 'cover'}
TASK_MACROS = set('cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible'.split())
STANDARD_COMMANDS = set('''
Delta Downarrow Gamma Lambda Longleftarrow Longleftrightarrow Longrightarrow
Phi Rightarrow Theta Uparrow Updownarrow Vert alpha amalg bar begin beta big
bigl bigotimes bigr bigwedge boxed boxtimes bullet cdot cdots check circ delta
displaystyle end eta exists flat forall frac geq hfill hookrightarrow hspace
in infty int joinrel kappa lambda langle left leq lhook lim linewidth
longleftarrow longleftrightarrow longmapsto longrightarrow mapsto mathbb
mathbf mathbin mathcal mathrm mid multicolumn ne ni noindent operatorname
oplus otimes overbrace overline overset par phantom pi prime prod psi qquad
quad rangle resizebox right rightrightarrows rotatebox rule scriptsize sharp
sim simeq small subset subseteq substack text textcircled textsuperscript
texttt textwidth times ttfamily underbrace underline underset varepsilon
varinjlim varphi varprojlim vdots vee vert vphantom widehat widetilde wr
xhookrightarrow xi xleftarrow xrightarrow fbox begingroup endgroup setlength
arraycolsep tabcolsep
'''.split())
TIKZ_COMMANDS = {'arrow', 'draw', 'fill', 'foreach', 'node', 'tikzcdmatrixname'}
LOOP_VARIABLES = {'x', 'y'}
FORBIDDEN = set('input include includegraphics documentclass usepackage newcommand renewcommand providecommand def edef gdef xdef let DeclareRobustCommand'.split())


def control_words(text):
    """Lex control words, consuming doubled backslashes as one row separator."""
    i = 0
    while i < len(text):
        if text[i] == '%':
            j = text.find('\n', i)
            i = len(text) if j < 0 else j + 1
        elif text[i] == '\\':
            start = i + 1
            if start < len(text) and text[start].isascii() and text[start].isalpha():
                i = start + 1
                while i < len(text) and text[i].isascii() and text[i].isalpha():
                    i += 1
                yield text[start:i]
            else:
                i += 2
        else:
            i += 1


def grouped_macro_bodies(text, macro):
    for match in re.finditer(r'\\' + macro + r'\s*\{', text):
        depth, i = 1, match.end()
        while i < len(text) and depth:
            if text[i] == '\\':
                i += 2
                continue
            if text[i] == '%':
                end = text.find('\n', i)
                i = len(text) if end < 0 else end + 1
                continue
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
            i += 1
        if depth:
            yield text.count('\n', 0, match.start()) + 1, None
        else:
            yield text.count('\n', 0, match.start()) + 1, text[match.end():i-1]


def check(inventory, require_audits=False):
    errors, pages = [], []
    files = sorted((ROOT / 'pages').glob('*.tex'))
    found = set()
    total_commands = Counter()
    cote_occurrences = []
    for path in files:
        match = re.fullmatch(PREFIX + r'_134-8_scan(\d{3})\.tex', path.name)
        if not match:
            errors.append({'file': path.name, 'issue': 'Unexpected page filename'})
            continue
        scan = int(match.group(1))
        found.add(scan)
        source_bytes = path.read_bytes()
        text = source_bytes.decode('utf-8')
        commands = Counter(control_words(text))
        total_commands.update(commands)
        headers = re.findall(r'\\scanpage\{(\d+)\}', text)
        if headers != [str(scan)]:
            errors.append({'scan': scan, 'issue': 'scanpage header mismatch', 'values': headers})
        for cote in re.findall(r'\\cotefile\{([^}]+)\}', text):
            cote_occurrences.append({'scan': scan, 'cote': cote})
        forbidden = sorted(set(commands) & FORBIDDEN)
        unknown = sorted(set(commands) - TASK_MACROS - STANDARD_COMMANDS - TIKZ_COMMANDS - LOOP_VARIABLES)
        if forbidden:
            errors.append({'scan': scan, 'issue': 'Forbidden fragment command', 'commands': forbidden})
        if unknown:
            errors.append({'scan': scan, 'issue': 'Command outside reviewed structural allowlist', 'commands': unknown})
        local_variables = sorted(set(commands) & LOOP_VARIABLES)
        if local_variables and r'\foreach' not in text:
            errors.append({'scan': scan, 'issue': 'Local TikZ variable without a foreach declaration', 'commands': local_variables})
        for line, body in grouped_macro_bodies(text, 'diagram'):
            if body is None:
                errors.append({'scan': scan, 'line': line, 'issue': 'Unclosed diagram macro group'})
            elif not any(env in body for env in (r'\begin{tikzcd}', r'\begin{array}')):
                issue = 'tabular inside diagram requires an array' if r'\begin{tabular}' in body else 'diagram contains neither tikzcd nor array'
                errors.append({'scan': scan, 'line': line, 'issue': issue})
        for line, body in grouped_macro_bodies(text, 'figure'):
            if body is None or r'\begin{tikzpicture}' not in body:
                errors.append({'scan': scan, 'line': line, 'issue': 'figure lacks a complete tikzpicture body'})
        pages.append({'scan': scan, 'file': 'pages/' + path.name,
                      'sha256': hashlib.sha256(source_bytes).hexdigest(),
                      'task_macro_counts': {k: commands[k] for k in sorted(TASK_MACROS) if commands[k]},
                      'local_tikz_variables': local_variables})
    if found != EXPECTED:
        errors.append({'issue': 'Page-set mismatch', 'missing': sorted(EXPECTED - found), 'extra': sorted(found - EXPECTED)})
    if cote_occurrences != [{'scan': 43, 'cote': '134-8'}]:
        errors.append({'issue': 'Cote-header mismatch', 'values': cote_occurrences})
    if files and not files[0].read_text().startswith('\\cotefile{134-8}\n\\scanpage{43}'):
        errors.append({'issue': 'First fragment does not begin with the required cote and scan headers'})

    with inventory.open(newline='') as source:
        reader = csv.DictReader(source)
        rows = list(reader)
        fields = reader.fieldnames
    if fields != FIELDS:
        errors.append({'issue': 'Inventory header mismatch', 'fields': fields})
    row_scans = set()
    ids = Counter()
    kinds = Counter()
    counts = Counter()
    sheets = {}
    for n, row in enumerate(rows, 2):
        try:
            scan = int(row['scan'])
        except (ValueError, KeyError):
            errors.append({'inventory_line': n, 'issue': 'Invalid scan field'})
            continue
        row_scans.add(scan)
        counts[scan] += 1
        ids[(row['cote'], row['element'])] += 1
        kinds[row['kind']] += 1
        sheets.setdefault(scan, set()).add(row['sheet_kind'])
        if row['cote'] != '134-8' or row['transcribed'] != 'yes':
            errors.append({'inventory_line': n, 'issue': 'Invalid cote or transcribed status', 'row': row})
        if row['sheet_kind'] not in SHEET_KINDS:
            errors.append({'inventory_line': n, 'issue': 'Invalid sheet kind', 'value': row['sheet_kind']})
        for field in ('element', 'position', 'first_words_or_objects'):
            if not row[field]:
                errors.append({'inventory_line': n, 'issue': 'Empty inventory field', 'field': field})
    if row_scans != EXPECTED:
        errors.append({'issue': 'Inventory scan-set mismatch', 'missing': sorted(EXPECTED - row_scans), 'extra': sorted(row_scans - EXPECTED)})
    duplicates = [{'cote': cote, 'element': element, 'count': count}
                  for (cote, element), count in ids.items() if count != 1]
    if duplicates:
        errors.append({'issue': 'Duplicate inventory element identifiers', 'values': duplicates})
    for scan, values in sheets.items():
        if len(values) != 1:
            errors.append({'scan': scan, 'issue': 'Inconsistent sheet kinds', 'values': sorted(values)})
    invalid_kinds = {kind: count for kind, count in sorted(kinds.items()) if kind not in KINDS}
    if invalid_kinds:
        errors.append({'issue': 'Inventory kinds outside required seven-value set', 'values': invalid_kinds})

    record_summary = []
    for scan in sorted(EXPECTED):
        record = ROOT / 'records' / f'scan{scan:03d}_inventory.json'
        if not record.exists():
            errors.append({'scan': scan, 'issue': 'Missing per-scan inventory record'})
            continue
        data = json.loads(record.read_text())
        if data.get('scan') != scan:
            errors.append({'scan': scan, 'issue': 'Per-scan record header mismatch'})
        record_summary.append({'scan': scan, 'original_record_elements': len(data.get('elements', [])),
                               'current_inventory_rows': counts[scan]})

    progress = (ROOT / 'progress.log').read_text()
    done = Counter(int(x) for x in re.findall(r'^134-8 scan (\d{3}) done ', progress, re.M))
    audited = Counter(int(x) for x in re.findall(r'^scan (\d{3}) audited ', progress, re.M))
    if set(done) != EXPECTED:
        errors.append({'issue': 'Done-log coverage mismatch', 'missing': sorted(EXPECTED - set(done)), 'extra': sorted(set(done) - EXPECTED)})
    if require_audits and not EXPECTED.issubset(audited):
        errors.append({'issue': 'Audit-log coverage incomplete', 'missing': sorted(EXPECTED - set(audited))})
    return {'checked_utc': dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'scope': 'Structural metadata and TeX control-word check only; no scan image/context reading; no source edits',
            'expected_scan_count': 44, 'page_count': len(files), 'inventory_file': str(inventory),
            'inventory_row_count': len(rows), 'inventory_kind_counts': dict(sorted(kinds.items())),
            'all_inventory_rows_yes': all(row.get('transcribed') == 'yes' for row in rows),
            'done_scan_count': len(done), 'audited_scan_count_so_far': len(audited),
            'require_audits': require_audits,
            'permitted_task_macros_used': sorted(set(total_commands) & TASK_MACROS),
            'standard_or_tikz_control_words_used': sorted(set(total_commands) - TASK_MACROS),
            'pages': pages, 'per_scan_inventory_counts': record_summary,
            'errors': errors, 'pass': not errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inventory', type=Path, default=ROOT / (PREFIX + '_inventory.csv'))
    parser.add_argument('--report', type=Path, default=ROOT / 'records' / 'package_structure_report.json')
    parser.add_argument('--require-audits', action='store_true')
    args = parser.parse_args()
    report = check(args.inventory, args.require_audits)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print('Pages:', report['page_count'], 'Inventory rows:', report['inventory_row_count'],
          'Done scans:', report['done_scan_count'], 'Audited so far:', report['audited_scan_count_so_far'])
    print('PASS' if report['pass'] else 'REVIEW REQUIRED')
    for issue in report['errors']:
        print(json.dumps(issue, ensure_ascii=False))
    print('Report:', args.report)
    return int(not report['pass'])


if __name__ == '__main__':
    raise SystemExit(main())
