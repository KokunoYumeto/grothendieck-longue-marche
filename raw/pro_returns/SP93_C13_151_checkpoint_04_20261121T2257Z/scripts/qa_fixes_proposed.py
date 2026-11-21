"""Proposed encoding/metadata fixes, prepared by blind_a; NOT yet applied.

Default: report the proposed changes without writing anything.
With --apply: write the narrowly identified files, then rebuild aggregates.
No source images, witness readings, frozen first/second TSVs, or box lists are
modified. No TeX compilation, OCR, or image-reading adjudication is performed.
Scan020's uncertain deletion-state wrapper is deliberately excluded.
"""
from pathlib import Path
import argparse
import json
import re
import subprocess
import sys

WORK = Path(__file__).resolve().parents[1]


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected one exact old snippet, found {count}")
    return text.replace(old, new, 1)


def change_note(report, old, new, label):
    hits = [i for i, note in enumerate(report['notes']) if old in note]
    if len(hits) != 1:
        raise ValueError(f"{label}: expected one matching note, found {len(hits)}")
    i = hits[0]
    report['notes'][i] = replace_once(report['notes'][i], old, new, label)


def group_end(text, opening):
    """Find a TeX group's end, ignoring escaped brace control symbols."""
    depth, i = 1, opening + 1
    while i < len(text):
        if text[i] == '\\':
            token = re.match(r'\\(?:[A-Za-z]+|.)', text[i:], re.S)
            if token:
                i += len(token.group())
                continue
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError('Unclosed TeX group in proposed cancellation edit')


def remove_local_deleted(text):
    """Remove only rendering wrappers; retain every glyph and unsure wrapper."""
    token = r'\deleted{'
    while token in text:
        start = text.index(token)
        opening = start + len(token) - 1
        closing = group_end(text, opening)
        text = text[:start] + text[opening + 1:closing] + text[closing + 1:]
    return text


def update_json(scan, report):
    if scan == 17:
        change_note(report,
            'The group-ens. annotation earlier is a real underbrace annotation attached to E_n* only.',
            'The group-ens. annotation earlier is a flat underbar annotation attached to E_n* only.',
            '017 notes: group annotation')
        change_note(report,
            'in the separate boxed factorization;',
            'in the separate factorization with only a left boundary stroke;',
            '017 notes: bottom factorization')
        by_id = {row['id']: row for row in report['changes']}
        row = by_id['C017-28']
        row['evidence'] = replace_once(row['evidence'],
            'sits above its boxed factorization.',
            'sits above its factorization with only a left boundary stroke.',
            'C017-28 evidence')
        for ident in ['C017-32', 'C017-39']:
            row = by_id[ident]
            row['place'] = replace_once(row['place'],
                'bottom boxed factorization', 'bottom factorization', ident + ' place')
    elif scan == 18:
        change_note(report,
            'Ordinary under-bracket annotations are represented with the established underbrace transcription convention.',
            'The two under-bracket annotations are represented by their observed flat drawn courses, as revised in the independent audit.',
            '018 notes: bracket encoding')
        change_note(report,
            'The final deleted wrapper implements that state but is not counted as a change against H.',
            'The final traced global X implements that state, without an outer deleted wrapper, and is not counted as a change against H.',
            '018 notes: cancellation encoding')
    elif scan == 19:
        # Accepted audit B001 already added the stop after K to the page.
        doubts = [d for d in report['doubts'] if d['place'] == 'First sketch, both épi arrowheads']
        if len(doubts) != 1:
            raise ValueError('019: first-sketch doubt entry is not unique')
        doubts[0]['reading'] = replace_once(doubts[0]['reading'],
            r'\&K\&{}', r'\&K.\&{}', '019 first-sketch doubt reading')

        # These excerpts belong to the single globally cancelled central region.
        # The separate marginal p/* cancellation (M0806) is intentionally untouched.
        ids = {'019-C41', '019-C44', '019-C45', '019-C46',
               '019-C47', '019-C48', '019-C49'}
        found = set()
        for row in report['changes']:
            if row['id'] in ids:
                found.add(row['id'])
                row['final'] = remove_local_deleted(row['final'])
        if found != ids:
            raise ValueError(f'019: missing targeted change records {ids - found}')
        prefixes = ('Cancelled upper E-to-E sketch,', 'Cancelled E square,', 'Cancelled X square,')
        for doubt in report['doubts']:
            if doubt['place'].startswith(prefixes):
                doubt['reading'] = remove_local_deleted(doubt['reading'])
        for adjudication in report.get('second_adjudications', []):
            if adjudication['box'] in {'B018', 'B019', 'B020', 'B021'}:
                # Historical first/second fields are immutable and left intact.
                adjudication['final'] = remove_local_deleted(adjudication['final'])
        report['notes'].append(
            'Encoding-only QA: the cancelled state of the lower-right central diagrams is conveyed by the existing shared TikZ cancellation courses. '
            'Their text/math labels retain all glyphs and local doubts without additional linewise deleted strikeouts. '
            'The first-sketch doubt excerpt also includes the stop after K already accepted in audit B001.')
    return report


def proposed_changes():
    staged = {}
    for scan in [17, 18, 19]:
        for folder in ['reports', 'reviews']:
            path = WORK / folder / f'151_scan{scan:03d}.json'
            report = json.loads(path.read_text())
            staged[path] = json.dumps(update_json(scan, report), ensure_ascii=False, indent=2) + '\n'

    marker = r'\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm]'
    closing = r'\end{tikzpicture}}'
    for folder in ['reports', 'pages']:
        path = WORK / folder / '151_scan019.tex'
        text = path.read_text()
        if text.count(marker) != 1:
            raise ValueError(f'{path}: central diagram marker not unique')
        start = text.index(marker)
        end = text.index(closing, start) + len(closing)
        region = text[start:end]
        if '% Cancellation strokes lie over the central diagrams' not in region:
            raise ValueError(f'{path}: expected shared cancellation paths absent')
        if r'\deleted{' not in region:
            raise ValueError(f'{path}: targeted local wrappers already absent')
        staged[path] = text[:start] + remove_local_deleted(region) + text[end:]
    return staged


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    staged = proposed_changes()  # Validate every target before any writes.
    print(json.dumps({'apply': args.apply,
                      'files': [str(p.relative_to(WORK)) for p in staged],
                      'frozen_files_modified': False,
                      'scan020_excluded': True}, indent=2))
    if not args.apply:
        return
    for path, text in staged.items():
        path.write_text(text)
    subprocess.run([sys.executable, str(WORK / 'scripts/assemble.py')], check=True)


if __name__ == '__main__':
    main()
