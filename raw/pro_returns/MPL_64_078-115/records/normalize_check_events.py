#!/usr/bin/env python3
"""Normalize category spelling and split distinct background statements; no new checks."""
import csv
from pathlib import Path
rec=Path(__file__).resolve().parent
cols=['statement_id','date','who','type','outcome']
root_splits={
 'LM4 D.12; EXIT_TOWER E.24; LM4_SUCCESSOR B.38':['LM4 D.12','EXIT_TOWER E.24','LM4_SUCCESSOR B.38'],
 'LM7_PUSH E.3; LM6 A.22':['LM7_PUSH E.3','LM6 A.22']
}
lit_splits={
 'Antieau-Meier2020/4.5-and4.6':[
  ('Antieau-Meier2020/4.5','RC03: used the standard presentation as the nearest literature comparison after reading the primary presentation proof; not independently re-proved as a stack theorem, and no novelty inference.'),
  ('Antieau-Meier2020/4.6','RC03: used the coarse-moduli corollary to distinguish the coarse parameter from the pinned problem; source read, no independent proof or novelty inference.')],
 'Katz1972/2.0.2.2-2.3.1.1':[
  ('Katz1972/2.0.2.2','RC01: used the primary indexed passage on relative derivations as a comparison framework; no proof of the full article or manuscript identification claimed.'),
  ('Katz1972/2.1','RC01 and RC13: used the primary indexed Cartier framework as background; the coefficient calculation is separately proved in RC13, and the full article is not re-proved.'),
  ('Katz1972/2.3.1.1','RC01: used the primary indexed Gauss-Manin/conjugate-filtration comparison to distinguish a connection from a fibre derivation; no historical identification inferred.')]
}
allowed={'targeted proof check','independent re-proof','computation or formal certificate',
         'used and rechecked in this run','carried as background without fault found','refuted'}
for path in rec.glob('check_events_*.tsv'):
    with path.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    out=[]
    for row in rows:
        if row['type'].startswith('refuted'):
            row['type']='refuted'
            if not ('-R' in row['outcome']):raise RuntimeError(f'Missing refined statement ID: {row}')
        if row['type'] not in allowed:raise RuntimeError(f'Unknown event type: {row}')
        ident=row['statement_id']
        if ident in root_splits:
            for sid in root_splits[ident]:out.append({**row,'statement_id':sid})
        elif ident in lit_splits:
            for sid,description in lit_splits[ident]:out.append({**row,'statement_id':sid,'outcome':description})
        else:out.append(row)
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(out)
print('Actor categories normalized; distinct background statements separated; no event times invented')
