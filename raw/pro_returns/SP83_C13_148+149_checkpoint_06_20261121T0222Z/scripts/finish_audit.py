"""Record a completed, visually adjudicated independent reading.

This script does not decide readings or edit transcription text. The main reader
must first update the accepted page and its witness records, and supply an
adjudication row for every box whose token sequences differ.
"""
from pathlib import Path
import csv, hashlib, json, re, sys
csv.field_size_limit(16 * 1024 * 1024)
from datetime import datetime, timezone

OUT = Path(__file__).resolve().parents[1]
page, second_reader = sys.argv[1:3]
record_path = OUT / 'records' / f'{page}.json'
record = json.loads(record_path.read_text())
if record['reader'] == second_reader:
    raise ValueError('The second reader must differ from the first reader')
if record.get('audit'):
    raise ValueError('This page already has a completed audit')

def tokens(text):
    return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]', text)

comparison = json.loads((OUT / 'second' / f'{page}_comparison.json').read_text())
differences = {row['box']: row for row in comparison if not row['same_tokens']}
with (OUT / 'second' / f'{page}_adjudication.tsv').open() as stream:
    adjudications = list(csv.DictReader(stream, delimiter='\t'))
if len({row['box'] for row in adjudications}) != len(adjudications):
    raise ValueError('Duplicate adjudication box')
if {row['box'] for row in adjudications} != set(differences):
    raise ValueError('Adjudications must cover exactly every differing box')

changed = 0
audit_changes = []
for row in adjudications:
    comparison_row = differences[row['box']]
    if row['first'] != comparison_row['first'] or row['second'] != comparison_row['second']:
        raise ValueError('Adjudication does not preserve both original readings')
    if row.get('main_reader_reviewed') != 'yes':
        raise ValueError('Main reader has not confirmed visual review')
    crop = row['crop']
    if not (OUT / crop).is_file():
        raise ValueError('Missing adjudication crop: ' + crop)
    if not row['evidence'].strip():
        raise ValueError('Missing visual decision evidence')
    is_changed = tokens(row['first']) != tokens(row['final'])
    if row['changed'] != ('yes' if is_changed else 'no'):
        raise ValueError('Changed flag does not match token comparison')
    changed += is_changed
    audit_changes.append({
        'box': row['box'], 'first': row['first'], 'second': row['second'],
        'final': row['final'], 'evidence': row['evidence'] + '; ' + crop,
        'changed': is_changed,
    })

now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
second_path = OUT / 'second' / f'{page}_second.tsv'
record['main_reader_crops'] = sorted(set(record.get('main_reader_crops', [])) | {row['crop'] for row in adjudications})
record['audit_changes'] = audit_changes
record['audit'] = {
    'reader': second_reader, 'boxes': len(comparison),
    'differences': len(differences), 'changed': changed, 'completed_at': now,
    'second_reading_sha256': hashlib.sha256(second_path.read_bytes()).hexdigest(),
    'comparison': f'second/{page}_comparison.json',
    'adjudication': f'second/{page}_adjudication.tsv',
}
record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
with (OUT / 'progress.log').open('a') as stream:
    stream.write(f"scan {int(page.split('_scan')[1]):03} audited {now}: "
                 f"{len(comparison)} boxes read, {len(differences)} differences, "
                 f"{changed} changed; cote {page.split('_')[0]}; "
                 f"independent reader {second_reader}\n")
print(json.dumps(record['audit'], ensure_ascii=False))
