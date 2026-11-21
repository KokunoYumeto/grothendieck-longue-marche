"""Record an eligible one-page blind assignment after the first-reading seal."""
from pathlib import Path
import csv, sys, datetime, json
W=Path(__file__).resolve().parents[1]
page,reader=sys.argv[1:3]
assert (W/'second/first_reading_hashes.tsv').exists()
assert reader in {'reader_a','reader_b','reader_c'}
p=W/'reader_assignments.tsv'
rows=list(csv.DictReader(p.open(),delimiter='\t'))
entry=next(r for r in rows if r['page']==page)
assert not entry['second_reader'], 'Assignment already exists.'
assert reader!=entry['first_reader'], 'Reader has already read this page.'
if page=='150_scan087':assert reader=='reader_c', 'reader_a has also seen witness material for087.'
assert not (W/'second'/f'{page}_second.tsv').exists()
entry['second_reader']=reader
with p.open('w',newline='') as out:
    writer=csv.DictWriter(out,fieldnames=['page','first_reader','second_reader'],delimiter='\t')
    writer.writeheader();writer.writerows(rows)
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (W/'progress.log').open('a') as out:out.write(f'Blind reading assigned {stamp}: {page} {reader}.\n')
print(f'{page} assigned to {reader}.')
