#!/usr/bin/env python3
"""Consolidate actual actor logs, preserving their times and declared scope."""
import csv
from pathlib import Path
base=Path(__file__).resolve().parents[1]
rec=base/'records'
cols=['statement_id','date','who','type','outcome']
root=rec/'check_events_root.tsv'
if not root.exists():root.write_bytes((base/'CHECK_EVENTS.tsv').read_bytes())
rows=[]; seen=set()
for p in sorted(rec.glob('check_events_*.tsv')):
    with p.open(newline='') as f:
        reader=csv.DictReader(f,delimiter='\t')
        if reader.fieldnames!=cols:raise SystemExit(f'Unexpected header: {p}')
        for row in reader:
            if not all(row[k] for k in cols):raise SystemExit(f'Incomplete row in {p}')
            key=tuple(row[c] for c in cols)
            if key not in seen:rows.append(row);seen.add(key)
rows.sort(key=lambda r:(r['date'],r['who'],r['statement_id']))
with (base/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
print(f'{len(rows)} actual research check/use events consolidated from actor records')
