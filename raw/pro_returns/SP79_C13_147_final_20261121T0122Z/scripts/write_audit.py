"""Store explicit main-reader decisions without retyping committed readings.

Input is JSON on stdin with scan, second_reader, decisions and optional notes.
Each decision supplies box, crop, ink, changed, token_resolutions, and either
use_first=true or an explicit final string. No reading is inferred here.
Existing boxes cannot be overwritten; approval is a separate operation.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
payload = json.load(sys.stdin)
n = int(payload['scan'])
stem = f'147_scan{n:03d}'
comparison = json.loads((ROOT / 'second' / f'{stem}_comparison.json').read_text())
items = {x['box']: x for x in comparison['items']}
path = ROOT / 'second' / f'{stem}_adjudication.json'
result = json.loads(path.read_text()) if path.exists() else {
    'second_reader': payload['second_reader'], 'decisions': [], 'notes': []}
assert result['second_reader'] == payload['second_reader']
existing = {x['box'] for x in result['decisions']}
for supplied in payload['decisions']:
    d = dict(supplied)
    assert d['box'] not in existing, 'Do not overwrite an existing decision'
    item = items[d['box']]
    if d.pop('use_first', False):
        assert 'final' not in d
        d['final'] = item['first']
    assert isinstance(d['changed'], bool)
    assert d['final'] and d['ink'] and (ROOT / d['crop']).exists()
    covered = [i for group in d['token_resolutions'] for i in group['operations']]
    assert sorted(covered) == list(range(len(item['token_differences'])))
    assert all(g['decision'] and g['ink'] for g in d['token_resolutions'])
    d['first'] = item['first']
    d['second'] = item['second']
    result['decisions'].append(d)
    existing.add(d['box'])
result['notes'].extend(payload.get('notes', []))
path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(f'Stored {len(result["decisions"])}/{len(items)} differing-box decisions for {stem}')
