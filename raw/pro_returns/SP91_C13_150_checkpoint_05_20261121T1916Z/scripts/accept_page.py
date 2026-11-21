"""Promote a return only after the main reader has completed its visual review.

The main visual review file is written by the main reader from actual inspections.
This helper performs file bookkeeping; it does not decide any reading.
"""
from pathlib import Path
import json
import shutil
import sys
import build_outputs

root = Path(__file__).resolve().parents[1]
scan = sys.argv[1].zfill(3)
record_path = root / 'records' / f'150_scan{scan}.json'
page_path = root / 'pages' / f'150_scan{scan}.tex'
review_path = root / 'records' / f'main_visual_review_{scan}.txt'
if record_path.exists() or page_path.exists():
    raise RuntimeError('An accepted page already exists; review amendments explicitly.')
record = json.loads((root / 'reader_returns' / f'150_scan{scan}.json').read_text())
assert record['scan'] == scan
assert review_path.read_text().strip(), 'Missing main visual review'
assert record['coverage']['whole_image_viewed']
assert record['coverage']['all_tokens_read']
assert record['coverage']['all_C_insertions_deletions_checked']
assert set(record['coverage']['halves_viewed']) == {'top', 'bottom'}
assert all(row['transcribed'] == 'yes' for row in record['inventory'])
assert len({b['box'] for b in record['audit_boxes']}) == len(record['audit_boxes'])
record['main_reviewed'] = True
record['main_review'] = review_path.read_text()
record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
shutil.copyfile(root / 'reader_returns' / f'150_scan{scan}.tex', page_path)
build_outputs.finalize(scan)
state_path = root / 'records' / 'workflow_state.json'
state = json.loads(state_path.read_text())
state['accepted'] = [s for s in build_outputs.ORDER if (root / 'records' / f'150_scan{s}.json').exists()]
state['notes'] = 'See main_visual_review files for actual root inspections. Dispatch only after acceptance.'
state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
