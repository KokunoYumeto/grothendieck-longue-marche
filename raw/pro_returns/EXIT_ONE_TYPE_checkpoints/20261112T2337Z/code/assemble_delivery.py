#!/usr/bin/env python3
"""Assemble registers and bibliography; verify every numbered result is indexed.

This is a delivery consistency check, not a mathematical proof checker.
Run from any directory. Re-run after the final LuaLaTeX pass to record numbers.
"""
from pathlib import Path
import csv
import json
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ['criterion', 'examples', 'cusp', 'compactifications', 'boundary', 'levels']
RESULT_FIELDS = [
    'id', 'statement', 'status', 'where_proved', 'depends_on',
    'manuscript_passages (section; folio; scan)',
    'depends_on_doubtful_reading (scan, alternatives)', 'notes',
]
READING_FIELDS = ['package', 'scan', r'the \unsure or \illegible place',
                  'what the mathematics supports', 'how strongly']


def read_rows(path):
    with path.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def bib_entries(text):
    pattern = re.compile(r'@(\w+)\s*\{\s*([^\s,]+)\s*,')
    pos = 0
    while match := pattern.search(text, pos):
        depth = 1
        cursor = match.end()
        while cursor < len(text) and depth:
            if text[cursor] == '{':
                depth += 1
            elif text[cursor] == '}':
                depth -= 1
            cursor += 1
        if depth:
            raise ValueError(f'Unbalanced bibliography entry {match.group(2)}')
        yield match.group(2), text[match.start():cursor]
        pos = cursor


def main():
    missing_sections = [s for s in SECTIONS if not (ROOT/'sections'/f'{s}.tex').exists()]
    if missing_sections:
        raise RuntimeError(f'Missing complete sections: {missing_sections}')
    section_text = {s: (ROOT/'sections'/f'{s}.tex').read_text() for s in SECTIONS}
    alltex = '\n'.join(section_text.values())
    numbered = []
    environments = 'theorem|proposition|lemma|corollary|counterexample|example|conjecture'
    for section, text in section_text.items():
        for match in re.finditer(r'\\begin\{('+environments+r')\}(.*?)\\end\{\1\}', text, re.S):
            labels = re.findall(r'\\label\{([^}]+)\}', match.group(2))
            labels = [label for label in labels if label.startswith('P')]
            if len(labels) != 1:
                raise ValueError(f'{section}: numbered {match.group(1)} has {labels}')
            numbered.append((labels[0], section, match.group(1)))
    labels = [entry[0] for entry in numbered]
    duplicates = [key for key, count in Counter(labels).items() if count != 1]
    if duplicates:
        raise ValueError(f'Duplicate statement labels: {duplicates}')

    rows = {}
    for path in sorted((ROOT/'notes').glob('*_results.csv')):
        for raw in read_rows(path):
            ident = raw.get('id') or raw.get('label')
            if not ident:
                raise ValueError(f'Missing result id in {path}')
            if ident in rows:
                raise ValueError(f'Duplicate register id {ident}')
            row = {field: raw.get(field, '') for field in RESULT_FIELDS}
            row['id'] = ident
            row[RESULT_FIELDS[5]] = raw.get(RESULT_FIELDS[5], raw.get('manuscript_passages', ''))
            row[RESULT_FIELDS[6]] = raw.get(RESULT_FIELDS[6], raw.get('depends_on_doubtful_reading', ''))
            rows[ident] = row
    if set(rows) != set(labels):
        raise ValueError({'missing_rows': sorted(set(labels)-set(rows)),
                          'extra_rows': sorted(set(rows)-set(labels))})
    aux_path = ROOT/'EXIT_ONE_TYPE_paper.aux'
    aux = aux_path.read_text() if aux_path.exists() else ''
    numbers = dict(re.findall(r'\\newlabel\{(P[^}]+)\}\{\{([^}]+)\}', aux))
    for ident, section, env in numbered:
        row = rows[ident]
        number = numbers.get(ident)
        row['where_proved'] = ((env.title()+' '+number+'; ') if number else '') + f'sections/{section}.tex; label {ident}'
        if row['status'] not in {'Proved', 'Refuted', 'Known', 'Open'}:
            raise ValueError(f'Unsupported status {row["status"]} for {ident}')
    with (ROOT/'EXIT_ONE_TYPE_results.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, RESULT_FIELDS)
        writer.writeheader()
        writer.writerows(rows[ident] for ident in labels)

    readings = []
    for path in sorted((ROOT/'notes').glob('*_readings.csv')):
        for raw in read_rows(path):
            keys = list(raw)
            if all(field in raw for field in READING_FIELDS):
                row = {field: raw[field] for field in READING_FIELDS}
            elif {'source', 'scan', 'passage', 'doubtful_reading', 'effect', 'status'} <= set(raw):
                package = raw['source']
                if package.isdigit():
                    package = 'MPL_'+package
                place = '; '.join(piece for piece in [
                    'folio '+raw['folio'] if raw.get('folio') else '',
                    raw['passage'], 'doubtful: '+raw['doubtful_reading'],
                    'alternatives: '+raw['alternatives'] if raw.get('alternatives') else '',
                ] if piece)
                support = '; '.join(piece for piece in [raw.get('adopted', ''), raw['effect'],
                    'results: '+raw['labels'] if raw.get('labels') else ''] if piece)
                row = dict(zip(READING_FIELDS, [package, raw['scan'], place, support, raw['status']]))
            elif len(keys) == 5:
                row = dict(zip(READING_FIELDS, (raw[key] for key in keys)))
            else:
                raise ValueError(f'Unexpected readings schema in {path}: {keys}')
            readings.append(row)
    with (ROOT/'EXIT_ONE_TYPE_readings.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, READING_FIELDS)
        writer.writeheader()
        writer.writerows(readings)

    entries = {}
    duplicate_bib = []
    for path in sorted((ROOT/'notes').glob('*_references.bib')):
        for key, entry in bib_entries(path.read_text()):
            if key in entries:
                duplicate_bib.append({'key': key, 'additional_source': path.name})
                continue
            entries[key] = entry
    cited = set()
    for match in re.finditer(r'\\(?:cite[tp]?|citeauthor|citeyearpar|citeyear)(?:\[[^\]]*\]){0,2}\{([^}]+)\}', alltex):
        cited.update(key.strip() for key in match.group(1).split(','))
    missing_citations = cited-set(entries)
    if missing_citations:
        raise ValueError(f'Missing bibliography keys: {sorted(missing_citations)}')
    with (ROOT/'EXIT_ONE_TYPE_references.bib').open('w') as f:
        f.write('% Verified reference register. Per-source verification notes are retained.\n\n')
        f.write('\n\n'.join(entries[key] for key in sorted(entries))+'\n')
    status_counts = Counter(row['status'] for row in rows.values())
    report = {
        'role': 'Metadata, reference, and numbering consistency; not proof verification',
        'numbered_statements': len(labels), 'result_rows': len(rows),
        'status_counts': dict(status_counts), 'reading_rows': len(readings),
        'bibliography_entries': len(entries), 'cited_keys': len(cited),
        'unresolved_number_labels': [label for label in labels if label not in numbers],
        'deduplicated_bibliography_entries': duplicate_bib,
        'numbered_results': [{'id': ident, 'number': numbers.get(ident), 'environment': env,
                             'section_file': section+'.tex'} for ident, section, env in numbered],
        'open_results': [ident for ident in labels if rows[ident]['status']=='Open'],
    }
    (ROOT/'code/assembly_output.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'numbered_results'}, indent=2))


if __name__ == '__main__':
    main()
