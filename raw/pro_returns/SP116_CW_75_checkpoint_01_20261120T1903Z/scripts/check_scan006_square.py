"""Finite certificate for the two orientation conditions on scan006.

No image/text recognition. Vertices and edges are adjacent when distinct and
incident to a common edge/vertex respectively, as in the contour discussion.
"""
from itertools import permutations
from pathlib import Path
import json

edges = {frozenset((i, (i+1)%4)) for i in range(4)}
rows = []
for p in permutations(range(4)):
    image = lambda e: frozenset(p[v] for v in e)
    if {image(e) for e in edges} != edges:
        continue
    vertex_condition = all(frozenset((v,p[v])) in edges for v in range(4))
    edge_condition = all(image(e) != e and bool(image(e)&e) for e in edges)
    rows.append(dict(permutation=list(p),condition_1=vertex_condition,
                     condition_2=edge_condition))
assert len(rows)==8
assert any(r['condition_1'] and not r['condition_2'] for r in rows)
assert any(r['condition_2'] and not r['condition_1'] for r in rows)
assert sum(r['condition_1'] and r['condition_2'] for r in rows)==2
out = {'statement_id':'scan006-orientation-conditions',
       'refined_statement_id':'scan006-square-both-conditions',
       'assumption':'Adjacency of distinct vertices/edges in the square C4.',
       'automorphisms':rows,
       'condition_1_count':sum(r['condition_1'] for r in rows),
       'condition_2_count':sum(r['condition_2'] for r in rows),
       'both_count':sum(r['condition_1'] and r['condition_2'] for r in rows)}
path=Path(__file__).resolve().parents[1]/'records/scan006_square_certificate.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
