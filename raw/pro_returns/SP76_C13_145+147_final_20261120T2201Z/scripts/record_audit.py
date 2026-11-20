"""Record explicit main-reader decisions supplied on stdin; never choose readings."""
from pathlib import Path
import csv, json, sys

W = Path(__file__).resolve().parents[1]
page = sys.argv[1]
with (W/'second'/f'{page}_comparison.tsv').open() as f:
    comparison = list(csv.DictReader(f, delimiter='\t'))
cm = {r['box']: r for r in comparison}
out = W/'second'/f'{page}_adjudications.tsv'
rows = {}
if out.exists():
    with out.open() as f:
        rows = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
decisions = json.load(sys.stdin)
viewed = (W/'reports/root_viewed_crops.txt').read_text().splitlines()
for d in decisions:
    box = d['box']
    assert cm[box]['exact_token_match'] == 'no'
    assert d['changed'] in ('yes', 'no')
    assert d['confidence'] in ('high', 'medium', 'low') and d['evidence']
    if d.pop('use_first', False):
        assert d['changed'] == 'no'
        d['final_reading'] = cm[box]['first_reading']
    assert d['final_reading']
    d['crop'] = f'crops/{page}_second_{box}.png'
    assert (W/d['crop']).is_file()
    rows[box] = d
    viewed.append(Path(d['crop']).name)
fields = ['box', 'changed', 'evidence', 'final_reading', 'confidence', 'crop']
with out.open('w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    wr.writeheader()
    wr.writerows(rows[r['box']] for r in comparison if r['box'] in rows)
(W/'reports/root_viewed_crops.txt').write_text('\n'.join(dict.fromkeys(viewed))+'\n')
print(page, len(rows), 'explicit root decisions recorded')
