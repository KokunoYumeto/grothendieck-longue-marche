"""Serialize explicit, manually adjudicated choices; never select a reading.

Root supplies work/PAGE_audit_choices.json after viewing the relevant crops.
Each choice names a box, choice (first/second/literal), evidence, confidence,
and changed (a semantic/source-reading change, not TeX serialization alone).
For literal choices supply final. This script does not edit page text or the
witness-change registry. Those edits must already have been made by root.
"""
from pathlib import Path
from datetime import datetime, timezone
import json, sys

root = Path(__file__).resolve().parents[1]
page = sys.argv[1]
choices = json.loads((root / 'work' / (page + '_audit_choices.json')).read_text())
comparison = json.loads((root / 'second' / (page + '_comparison.json')).read_text())
diffs = {d['box']: d for d in comparison['differences']}
assert {d['box'] for d in choices['choices']} == set(diffs)
assert len(choices['choices']) == len(diffs)
decisions = []
for item in choices['choices']:
    d = diffs[item['box']]
    assert item['choice'] in ('first', 'second', 'literal')
    assert isinstance(item['changed'], bool) and item['evidence'].strip()
    final = item['final'] if item['choice'] == 'literal' else d[item['choice']]
    crop = item.get('crop', page + '_second_' + item['box'] + '.png')
    decisions.append(dict(box=item['box'], first=d['first'], second=d['second'],
                          final=final, changed=item['changed'],
                          evidence=item['evidence'], crop=crop,
                          confidence=item['confidence']))
out = dict(reader=choices['reader'], adjudications=decisions,
           serialized_at=datetime.now(timezone.utc).isoformat())
(root / 'work' / (page + '_audit_decisions.json')).write_text(
    json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(page=page, adjudications=len(decisions),
                     changed=sum(d['changed'] for d in decisions))))
