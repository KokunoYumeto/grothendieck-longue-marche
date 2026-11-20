"""Validate completion records and file structure; never infer image readings."""
from pathlib import Path
import csv, json, re

OUT = Path(__file__).resolve().parents[1]
NAME = 'SP57_CW_97+123+162-1+162-6'
order = json.loads((OUT / 'page_order.json').read_text())
assert len(order) == 26
expected = {m['stem'] + '.tex' for m in order}
actual = {p.name for p in (OUT / 'pages').glob('*.tex')}
assert actual == expected, (expected - actual, actual - expected)
kinds = {'misread word', 'misread symbol or index', 'omission', 'text not on the page',
         'deletion state (struck given live or live given struck)', 'insertion or placement',
         'abbreviation expanded or spelling modernised', 'readable ink left as \\ill{}',
         'drawing or diagram', 'other'}
counts = {'pages': 0, 'independent_reports': 0, 'decision_loci': 0, 'H_rows': 0, 'inventory': 0}
for meta in order:
    stem = meta['stem']
    page = OUT / 'pages' / (stem + '.tex')
    record = json.loads((OUT / 'decisions' / (stem + '.json')).read_text())
    assert '\\scanpage{' + meta['our_scan'] + '}' in page.read_text()
    for reader in ('R1', 'R2', 'R3'):
        folder = OUT / 'readers' / stem / reader
        report = json.loads((folder / 'report.json').read_text())
        assert (folder / 'reading.tex').read_text().strip()
        assert report.get('viewed') and report.get('inventory')
        counts['independent_reports'] += 1
    assert record.get('notes') and record.get('brief')
    for difference in record['differences']:
        assert difference['confidence'] in ('high', 'medium', 'low')
        assert difference['crop'] and (OUT / difference['crop']).exists()
        assert difference.get('readers'), (stem, difference['id'])
        if difference.get('h_changed'):
            assert difference['kind'] in kinds, difference
            assert difference['marked_in_H'] in ('yes', 'no')
            counts['H_rows'] += 1
        counts['decision_loci'] += 1
    for item in record['inventory']:
        assert item['transcribed'] in ('yes', True), (stem, item)
        assert item['kind'] in ('text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion')
        assert item['sheet_kind'] in ('text', 'reused_typed', 'typescript', 'letter', 'list', 'cancelled_draft', 'cover'), (stem, item)
        counts['inventory'] += 1
    counts['pages'] += 1
with (OUT / (NAME + '_collation.tsv')).open() as f:
    rows = list(csv.DictReader(f, delimiter='\t'))
assert len(rows) == counts['H_rows']
with (OUT / (NAME + '_inventory.csv')).open() as f:
    rows = list(csv.DictReader(f))
assert len(rows) == counts['inventory'] and all(r['transcribed'] == 'yes' for r in rows)
done = re.findall(r'^scan \d+ done ', (OUT / 'progress.log').read_text(), flags=re.M)
assert len(done) == 26, len(done)
syntax = json.loads((OUT / 'syntax_check.json').read_text())
assert len(syntax) == 26 and all(not r['errors'] for r in syntax)
with (OUT / 'CHECK_EVENTS.tsv').open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
event_types = {'targeted proof check', 'independent re-proof', 'computation or formal certificate',
               'used and rechecked in this run', 'carried as background without fault found',
               "refuted, with the refined statement's id"}
for event in events:
    assert set(event) == {'statement_id', 'date', 'who', 'type', 'outcome'}, event
    assert all(event.values()) and event['type'] in event_types, event
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC', event['date']), event
    if event['type'].startswith('refuted'):
        assert re.search(r'Refined statement \d{2,3}-\d{3}-[A-Za-z0-9-]+', event['outcome']), event
counts['check_events'] = len(events)
assert (OUT / 'decisions/legibility.md').read_text().strip()
(OUT / 'completion_validation.json').write_text(json.dumps({'status': 'passed', **counts}, indent=2) + '\n')
print(json.dumps({'status': 'passed', **counts}))
