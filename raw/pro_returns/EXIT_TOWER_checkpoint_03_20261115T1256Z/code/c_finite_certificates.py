#!/usr/bin/env python3
"""Finite checks used in the filling witness and the raw-face counterexample."""
from itertools import permutations
from pathlib import Path
import json
import sympy as s

P=list(permutations(range(3)));e=(0,1,2)
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def inv(a):return tuple(a.index(i) for i in range(3))
def closure(S):
 out={e}|set(S)
 while True:
  new=out|{mul(a,b) for a in out for b in out}
  if new==out:return out
  out=new
comm=closure(mul(mul(mul(a,b),inv(a)),inv(b)) for a in P for b in P)
assert len(comm)==3
assert all(mul(mul(a,a),a)==e for a in comm)
assert all(mul(mul(a,b),inv(a)) in comm for a in P for b in comm)
# Boundary of the triangular one-dimensional circle; no 2-cell is filled.
d1=s.Matrix([[-1,0,1],[1,-1,0],[0,1,-1]])
assert d1.rank()==2
data={'S3_order':len(P),'commutator_order':len(comm),
      'abelianization_order':len(P)//len(comm),
      'nonidentity_commutator':next(a for a in comm if a!=e),
      'circle_H0_rank':3-d1.rank(),'circle_H1_rank':3-d1.rank(),
      'point_H0_rank':1,'point_H1_rank':0,
      'two_edge_permutations':2,'flag_preserving_permutations':1}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
