"""Materialize the main reader's explicit crop decisions; never infer readings.

Input on stdin is JSON with page and box_reviews. Each review supplies box,
decision, ink, changed, and either final or choose='first'/'second'. Choosing
an existing reading is an explicit human/model decision made after image
inspection. This helper does not alter the transcription or witness records.
"""
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]
data = json.load(sys.stdin)
page = data['page']
comparison = json.loads((ROOT/'second'/f'{page}_comparison.json').read_text())
by_box = {x['box']: x for x in comparison}
reviews = []
for supplied in data['box_reviews']:
    item = dict(supplied)
    box = item['box']
    assert box in by_box
    if 'choose' in item:
        choice = item.pop('choose')
        assert choice in ('first', 'second') and 'final' not in item
        item['final'] = by_box[box][choice]
    assert isinstance(item['final'], str) and item['ink']
    assert isinstance(item['changed'], bool)
    assert item['decision'] in ('keep', 'correct', 'mark doubt', 'formatting')
    reviews.append(item)
assert len({x['box'] for x in reviews}) == len(reviews)
assert {x['box'] for x in comparison if x['different']} <= {x['box'] for x in reviews}
path = ROOT/'second'/f'{page}_review.json'
assert not path.exists(), 'An existing review must be revised explicitly'
path.write_text(json.dumps({'box_reviews': reviews}, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'page': page, 'reviewed_boxes': len(reviews)}))
