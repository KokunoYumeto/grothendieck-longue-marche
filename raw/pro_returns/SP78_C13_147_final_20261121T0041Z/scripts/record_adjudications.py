#!/usr/bin/env python3
"""Copy explicit main-reader decisions into the auditable comparison record.

This helper does not inspect images, select readings, alter pages, or infer a
decision. Every differing box must have a manually supplied visual decision.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sys

root = Path(__file__).resolve().parents[1]
scan = int(sys.argv[1])
page = f'147_scan{scan:03}'
decisions_path = Path(sys.argv[2])
decisions = json.loads(decisions_path.read_text())
comparison = json.loads((root/'second'/f'{page}_comparison.json').read_text())
assert set(decisions) == {r['box'] for r in comparison}, 'Missing or extra visual decisions'
output = []
for row in comparison:
    box = row['box']
    d = decisions[box]
    assert d.get('root_viewed') is True, box
    assert isinstance(d.get('changed'), bool), box
    assert d.get('evidence'), box
    final = d.get('final', row['first'])
    if d['changed']:
        assert final != row['first'], 'A changed box requires its new reading'
    else:
        assert final == row['first'], 'An unchanged box must retain its first reading'
    crop = d.get('crop', f'{page}_second_{box}.png')
    assert (root/'crops'/crop).is_file(), crop
    output.append({**row, 'final':final, 'crop':crop,
        'evidence':d['evidence'], 'root_viewed':True,
        'changed':d['changed'],
        'adjudicated_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')})
target = root/'second'/f'{page}_adjudications.json'
assert not target.exists(), 'Do not silently replace an adjudication record'
target.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'scan':scan, 'decided_boxes':len(output),
    'changed_boxes':sum(r['changed'] for r in output)}))
