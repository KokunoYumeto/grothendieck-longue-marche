"""Check required record coverage and file consistency; never read/recognize ink.

Run with --final only after the blind readings and freeze have been completed.
This is a structural audit, not a mathematical or visual verification.
"""
from pathlib import Path
import csv
import json
import re
import sys
import hashlib

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parents[1]
SCANS = [21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34,
         35, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47]
KINDS = {'misread word', 'misread symbol or index', 'omission',
         'text not on the page',
         'deletion state (struck given live or live given struck)',
         'insertion or placement', 'abbreviation expanded or spelling modernised',
         'readable ink left as \\ill{}', 'drawing or diagram', 'other'}
SHEET_KINDS = {'text', 'reused_typed', 'typescript', 'letter', 'list',
               'cancelled_draft', 'cover'}
ELEMENT_KINDS = {'text', 'display', 'diagram', 'drawing', 'margin note',
                 'insertion', 'deletion'}
CHECK_TYPES = {'targeted proof check', 'independent re-proof',
               'computation or formal certificate', 'used and rechecked in this run',
               'carried as background without fault found'}
ERRORS = []


def require(value, message):
    if not value:
        ERRORS.append(message)


def tsv(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main():
    final = '--final' in sys.argv
    reviews = {}
    for path in sorted((OUT / 'reviews').glob('148_scan*.json')):
        obj = json.loads(path.read_text())
        if obj.get('approved'):
            reviews[int(obj['scan'])] = obj
    require(set(reviews) <= set(SCANS), 'Unexpected approved scan')
    if final:
        require(set(reviews) == set(SCANS), 'All24 first readings required')

    with (ROOT / 'source/SP82_C13_148_texts/MARKS.tsv').open() as f:
        marks = list(csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE))
    expected = [r['id'] for r in marks if int(r['scan']) in reviews]
    decisions = tsv(OUT / 'decisions.tsv')
    require([r['id'] for r in decisions] == expected,
            'Decisions must cover source marks once, in source order')
    for row in decisions:
        require(row['decision'] in {'first', 'alternative', 'other', 'undecided'},
                f"Invalid decision {row['id']}")
        require(row['confidence'] in {'high', 'medium', 'low'},
                f"Invalid confidence {row['id']}")

    for scan, obj in reviews.items():
        path = OUT / 'pages' / f'148_scan{scan:03d}.tex'
        require(path.exists(), f'Missing page{scan:03d}')
        if not path.exists():
            continue
        text = path.read_text()
        require(re.findall(r'\\scanpage\{([0-9]+)\}', text) == [str(scan)],
                f'Page marker mismatch{scan:03d}')
        require(not any(ord(c) < 32 and c not in '\n\r\t' for c in text),
                f'Control character in page{scan:03d}')
        require(not re.search(r'\\(?:documentclass|usepackage|begin\{document)', text),
                f'Unexpected preamble in page{scan:03d}')
        for row in obj.get('changes', []) + obj.get('decisions', []):
            crop = row.get('crop')
            if crop and crop != 'page':
                require((OUT / crop).is_file(),
                        f'Missing evidence {scan:03d}: {crop}')
                require(len(row.get('box', [])) == 4,
                        f'Missing evidence coordinates{scan:03d}: {crop}')
        boxes = obj.get('second_boxes', [])
        require(len({r['box'] for r in boxes}) == len(boxes),
                f'Duplicate second box ids{scan:03d}')
        for box in boxes:
            require(box['x0'] < box['x1'] and box['y0'] < box['y1'],
                    f'Invalid second box{scan:03d}: {box["box"]}')
            require('reading' in box, f'Missing first reading{scan:03d}')
        if final:
            stem = OUT / 'second' / f'148_scan{scan:03d}'
            for suffix in ('_boxes.tsv', '_first.tsv', '_second.tsv', '_comparison.tsv',
                           '_token_differences.tsv', '_adjudication.tsv', '_adjudications.json'):
                require(Path(str(stem) + suffix).is_file(),
                        f'Missing blind-reading file {stem.name}{suffix}')
            if all(Path(str(stem) + suffix).is_file()
                   for suffix in ('_boxes.tsv', '_first.tsv', '_second.tsv', '_comparison.tsv')):
                expected_ids = {r['box'] for r in boxes}
                for suffix in ('_boxes.tsv', '_first.tsv', '_second.tsv', '_comparison.tsv'):
                    rows = tsv(Path(str(stem) + suffix))
                    require(len(rows) == len(expected_ids)
                            and {r['box'] for r in rows} == expected_ids,
                            f'Blind-reading coverage mismatch {stem.name}{suffix}')
                if Path(str(stem)+'_adjudication.tsv').is_file():
                    rows=tsv(Path(str(stem)+'_adjudication.tsv'))
                    require(len(rows)==len(expected_ids) and {r['box'] for r in rows}==expected_ids,
                            f'Adjudication coverage mismatch {stem.name}')
                    changed=sum(r['changed']=='yes' for r in rows)
                    comparison=tsv(Path(str(stem)+'_comparison.tsv'))
                    different={r['box'] for r in comparison if r['different']=='yes'}
                    audit=obj.get('second_audit',{})
                    require(audit.get('boxes')==len(expected_ids) and audit.get('differences')==len(different)
                            and audit.get('changed')==changed, f'Audit totals mismatch {stem.name}')
                    jp=Path(str(stem)+'_adjudications.json')
                    if jp.is_file():
                        entries=json.loads(jp.read_text())
                        require({r['box'] for r in entries}==different and
                                all(r.get('viewed_by_main') is True for r in entries),
                                f'Unadjudicated or unviewed difference {stem.name}')

    combined = (OUT / 'SP82_C13_148_transcription.tex').read_text()
    require([int(v) for v in re.findall(r'\\scanpage\{([0-9]+)\}', combined)]
            == [n for n in SCANS if n in reviews], 'Combined page order mismatch')
    expected_combined = '\\cotefile{148}\n\n' + '\n\n'.join(
        (OUT / 'pages' / f'148_scan{n:03d}.tex').read_text().rstrip()
        for n in SCANS if n in reviews) + '\n'
    require(combined == expected_combined, 'Combined fragment differs from pages')

    for row in tsv(OUT / 'SP82_C13_148_collation.tsv'):
        require(row['kind'] in KINDS, f'Invalid collation kind: {row["kind"]}')
        require(int(row['our_scan']) not in (22, 29), 'H row on an H-absent page')
        require(int(row['their_page']) + 1 == int(row['our_scan']), 'H page offset')
    with (OUT / 'SP82_C13_148_inventory.csv').open(newline='') as f:
        inventory = list(csv.DictReader(f))
    for row in inventory:
        require(row['sheet_kind'] in SHEET_KINDS,
                f'Invalid sheet kind{row["scan"]}: {row["sheet_kind"]}')
        require(row['kind'] in ELEMENT_KINDS,
                f'Invalid inventory kind{row["scan"]}: {row["kind"]}')
        require(row['transcribed'] == 'yes', f'Untranscribed inventory{row["scan"]}')
    for row in tsv(OUT / 'CHECK_EVENTS.tsv'):
        require(row['type'] in CHECK_TYPES or row['type'].startswith('refuted'),
                f'Invalid check-event type: {row["type"]}')

    progress = (OUT / 'progress.log').read_text()
    for scan in reviews:
        require(bool(re.search(rf'^scan {scan:03d} done ', progress, re.M)),
                f'Missing done log{scan:03d}')
        if final:
            require(bool(re.search(rf'^scan {scan:03d} audited ', progress, re.M)),
                    f'Missing audited log{scan:03d}')
    if final:
        require('transcription frozen ' in progress, 'Missing freeze log')
        require('frozen hashes verified unchanged ' in progress, 'Missing final frozen-hash verification')
        require((OUT / 'legibility.md').is_file(), 'Missing completed legibility assessment')
        first_hashes=json.loads((OUT/'second/first_reading_hashes.json').read_text())
        require(len(first_hashes)==24, 'Need24 original first-reading hashes')
        for name,sha in first_hashes.items():
            require(hashlib.sha256((OUT/'second'/name).read_bytes()).hexdigest()==sha,
                    f'Original first reading changed: {name}')
        for name,sha in json.loads((OUT/'transcription_hashes.json').read_text()).items():
            require(hashlib.sha256((OUT/name).read_bytes()).hexdigest()==sha,
                    f'Frozen transcription changed: {name}')
    print(json.dumps({'approved_pages': len(reviews), 'decisions': len(decisions),
                      'inventory_elements': len(inventory), 'final_mode': final,
                      'errors': ERRORS}, ensure_ascii=False, indent=2))
    return 1 if ERRORS else 0


if __name__ == '__main__':
    raise SystemExit(main())
