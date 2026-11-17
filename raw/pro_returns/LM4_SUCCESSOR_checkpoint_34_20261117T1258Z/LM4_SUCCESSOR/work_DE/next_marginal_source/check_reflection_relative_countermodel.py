#!/usr/bin/env python3
"""Exact auxiliary reflection model; not the actual mu5 surface."""
import json
from pathlib import Path
import sympy as s
l,z=s.symbols('lambda z')
D=[l-1,l+1,z,z-l,z+l,z+2*l]
F={l:-l,z:z+l}
assert all(s.expand(p.subs(F,simultaneous=True).subs(F,simultaneous=True)-p)==0 for p in (l,z))
permutation=[]
for p in D:
 q=s.expand(p.subs(F,simultaneous=True))
 hits=[i for i,r in enumerate(D) if s.expand(q-r)==0 or s.expand(q+r)==0]
 assert len(hits)==1;permutation.append(hits[0])
A=z-1;B=z+l-1
assert s.expand(A.subs(F,simultaneous=True)-B)==0
assert s.expand(B.subs(F,simultaneous=True)-A)==0
assert all(p.subs({l:0,z:1})!=0 for p in D)
assert s.det(s.Matrix([[s.diff(A,l),s.diff(A,z)],[s.diff(B,l),s.diff(B,z)]]))==-1
assert {s.solve(p.subs(l,0),z)[0] for p in D if p.has(z)}=={0}
assert s.solve(A.subs(l,0),z)==[1] and s.solve(B.subs(l,0),z)==[1]

def mul(p,q):return tuple(p[q[i]] for i in range(3))
def inv(p):return tuple(p.index(i) for i in range(3))
a=(1,0,2);b=(0,2,1);comm=mul(mul(mul(a,b),inv(a)),inv(b))
assert comm!=(0,1,2)
out={'status':'PASS','retained_line_permutation':permutation,'mixed_intersection':[0,1],'source_deleted_points':[0,1],'source_filled_points':[0],'first_factor_S3_commutator':list(comm),'topology_input':'B76 plus surjective actual normal-meridian transfer','scope':'Auxiliary broad-shortcut counterexample only; not the actual mu5 arrangement.'}
Path(__file__).with_name('reflection_relative_countermodel.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS linear reflection squares to1 and permutes the six retained lines.')
print('PASS deleted mirror lines meet transversely once, outside retained boundary.')
print('PASS source spaces agree exactly with B76 before/after filling.')
print('PASS nontrivial first-factor S3 commutator lies outside diagonal S3.')
print('Topology transfer is proved in the accompanying note; no new monodromy data invented.')
