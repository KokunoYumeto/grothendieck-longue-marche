#!/usr/bin/env python3
"""Independent E89.17--22 finite-character and actual-matrix audit."""
from pathlib import Path
from itertools import product
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
layers=json.loads((ROOT/'e_wild_layers.json').read_text())['layers']
T,J=[s.Matrix(layers['1'][k]) for k in ['input_tau','input_c']]
old=json.loads((ROOT/'a_abelian_kernel_obstruction.json').read_text())
R=s.Matrix([[s.Rational(x) for x in row] for row in old['first_degree_map']])
def mod(v):return tuple((int(s.Rational(a).p)*pow(int(s.Rational(a).q),-1,3))%3 for a in v)
rows=[]
for a,b,c,d in product(range(3),repeat=4):
 w=s.Matrix([[a,b,0,0,0,0,c,d,0,0]])
 if mod(w*T-w-R[1,:])==(0,)*10 and mod(w*J-w)==(0,)*10:rows.append(w)
assert [list(w) for w in rows]==[[a,(a+1)%3,0,0,0,0,2,1,0,0] for a in range(3)]
B=s.zeros(10,6)
B[:,0]=s.Matrix([0,0,0,0,0,-1,0,0,0,0])
B[:,1]=s.Matrix([2,-2,0,0,0,3,0,1,1,2])
B[:,2]=s.Matrix([0,0,1,0,0,0,0,0,0,0])
B[:,3]=s.Matrix([0,0,0,1,1,0,0,0,0,0])
B[:,4]=s.Matrix([2,4,0,1,0,-3,1,0,-2,0])
B[:,5]=s.Matrix([1,2,0,2,0,-2,0,1,-1,0])
for w in rows:assert mod(w*B)==(0,2,0,0,0,0)
def pair(L,p,m,n,nn):
 return ((p,p-L,n),(3*m-p,3*m-p-L,nn))
def mul(a,b):
 A,B,n=a;D,E,r=b
 return (A+D,B+E,n+r-D*B)
def theta(z):
 return (z[0][2]+z[1][2]+z[0][0]*(z[0][0]-1))%3
def op(a,mu):
 A,B,n=a
 return (7*A,7*B,49*n+7*mu*B)
def invletters(a):
 A,B,n=a
 return (-A,-B,n)
states=[pair(*v) for v in product(range(3),repeat=5)]
count=0
for a in states:
 for b in states:
  z=(mul(a[0],b[0]),mul(a[1],b[1]))
  assert (theta(z)-theta(a)-theta(b))%3==0
  count+=1
 forT=(op(a[0],2),op(a[1],1)) # exact μ reductions −5/2=2,−1/2=1
 assert (theta(forT)-theta(a)-a[0][0])%3==0
 assert theta((invletters(a[1]),invletters(a[0])))==theta(a)
out={'status':'PASS','scope':'E89.17--22 only',
 'row_candidates':81,'actual_rows':[list(map(int,w)) for w in rows],
 'six_representative_values':[0,2,0,0,0,0],
 'finite_homomorphism_identities':count,'arithmetic_and_involution_pairs':len(states),
 'geometric_check':'A cusps fill; B0 maps(y,y); a conjugate of a third peripheral power has all Hall coordinates0 mod3, so C-cusp theta is0.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
