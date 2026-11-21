"""Seal all 25 first readings and neutral box lists before blind reading starts."""
from pathlib import Path
import csv, datetime, hashlib, json

ROOT = Path(__file__).resolve().parents[1]
order = (ROOT/'page_order.txt').read_text().splitlines()
assert len(order) == 25
destination = ROOT/'second'/'first_reading_hashes.tsv'
assert not destination.exists(), 'First-reading seal is immutable.'
rows = []
for page in order:
    d = json.loads((ROOT/'records'/f'{page}.json').read_text())
    assert d.get('root_reviewed') and (ROOT/'pages'/f'{page}.tex').exists()
    assert not (ROOT/'second'/f'{page}_second.tsv').exists(), 'Blind reading started before all first readings were sealed.'
    for suffix in ['boxes', 'first']:
        path = ROOT/'second'/f'{page}_{suffix}.tsv'
        rows.append({'page':page, 'path':str(path.relative_to(ROOT)), 'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
with destination.open('w', newline='') as f:
    out = csv.DictWriter(f, fieldnames=['page','path','sha256'], delimiter='\t'); out.writeheader(); out.writerows(rows)
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f: f.write(f'All 25 first readings and neutral box lists sealed {now}; blind second reading may begin.\n')
print('Sealed 50 files for 25 pages.')
