"""Save explicit crop adjudications in batches without making reading decisions.

Usage: append_root_decisions.py PAGE < a JSON list of decisions
Decisions must be the next prefix of nonidentical comparison boxes. The final
write_adjudications.py check still requires complete coverage.
"""
from pathlib import Path
import json
import sys

W = Path(__file__).resolve().parents[1]
page = sys.argv[1]
base = W / 'second'
comparison = json.loads((base / f'{page}_comparison.json').read_text())
expected = [x['box'] for x in comparison if not x['token_equal']]
path = base / f'{page}_root_decisions.json'
current = json.loads(path.read_text()) if path.exists() else []
new = json.load(sys.stdin)
combined = current + new
if [x['box'] for x in combined] != expected[:len(combined)]:
    raise ValueError('Decisions are duplicated, out of order, or not a comparison prefix')
for row in new:
    if row.get('decision') not in ('retain', 'revise'):
        raise ValueError('An explicit retain/revise decision is required')
    if not row.get('evidence') or not row.get('outcome'):
        raise ValueError('Visual evidence and outcome are required')
    if row['decision'] == 'revise' and 'final' not in row:
        raise ValueError('Revised source reading is required')
path.write_text(json.dumps(combined, ensure_ascii=False, indent=2) + '\n')
print(page, len(combined), '/', len(expected), 'main-reader decisions saved')
