#!/usr/bin/env python3
"""Exact real-action check for the full-metabelian families in E.33.

The cubic calculation builds the integral boundary quotient by the diagonal sum,
adds the compact orientation-reversing action, and forms its exterior square.
Larger ranks are recorded from the proved eigenspace formula.
"""
from pathlib import Path
import json
import sympy as s

n=3
g=(n-1)*(n-2)//2
m=3*n
# Three real cusps, then three conjugate pairs; c reverses inertia.
perm=[0,1,2,4,3,6,5,8,7]
C=s.zeros(m)
for j,k in enumerate(perm):C[k,j]=-1
# The boundary module is Z_3^m / <sum e_i>.  Use the images of
# e_0,...,e_{m-2}; pi(v)_i=v_i-v_{m-1} is the quotient map.
B=s.zeros(m,m-1)
for i in range(m-1):B[i,i]=1
pi=s.eye(m-1).row_join(-s.ones(m-1,1))
CB=pi*C*B
assert pi*C==CB*pi
assert pi*s.ones(m,1)==s.zeros(m-1,1)
CV=s.diag(1,-1,CB)
assert CV*CV==s.eye(n*n+1)
pairs=[(i,j) for i in range(CV.rows) for j in range(i+1,CV.rows)]
CW=s.zeros(len(pairs))
for a,(i,j) in enumerate(pairs):
    for b,(k,l) in enumerate(pairs):
        CW[a,b]=CV[i,k]*CV[j,l]-CV[i,l]*CV[j,k]
assert CW*CW==s.eye(len(pairs))
plus=CV.rows-(CV-s.eye(CV.rows)).rank()
minus=CV.rows-(CV+s.eye(CV.rows)).rank()
wminus=CW.rows-(CW+s.eye(CW.rows)).rank()
assert (plus,minus,wminus)==(4,6,24)
out={
    'claim':'E.33 real-action rank; not an evaluation of the arithmetic cocycles',
    'cubic_boundary_permutation':perm,
    'cubic_integral_V_matrix':[[int(v) for v in row] for row in CV.tolist()],
    'cubic_exterior_square_dimension':len(pairs),
    'cubic_plus_rank':plus,'cubic_minus_rank':minus,
    'cubic_exterior_minus_rank':wminus,
    'higher_formula_values':[
        {'n':3**r,'V_plus':((3**r)**2-1)//2,
         'V_minus':((3**r)**2+3)//2,
         'family_rank':(((3**r)**2-1)*((3**r)**2+3))//4}
        for r in range(1,5)]
}
dest=Path(__file__).with_name('metabelian_family_rank_output.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
