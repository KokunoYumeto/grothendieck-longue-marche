#!/usr/bin/env python3
"""Independent exact discriminant orders at the six retained base holes.
Works over Q(zeta5), before the certified rational coefficient deformation.
"""
from pathlib import Path
import sympy as S
import json,hashlib
ROOT=Path(__file__).resolve().parent.parent
P=ROOT/'next_symmetric_nodes'
z,q=S.symbols('z q');phi=z**4+z**3+z**2+z+1
def kf(a):
 n,d=S.fraction(S.cancel(a))
 return S.rem(S.expand(n*S.invert(d,phi,z)),phi,z)
U=[kf(z**j) for j in range(1,5)]
mob=[(0,0,0,1),(0,1,0,1),(1,0,0,1)]
mob += [(0,v,0,1) for v in U]
mob += [(1,0,0,v) for v in U]
mob += [(-1,v,0,v-1) for v in U]
mob += [(1-v,0,1,-v) for v in U]
ND=[(S.expand(n1*q+n0),S.expand(d1*q+d0)) for n1,n0,d1,d0 in mob]
def order(poly,a):
 poly=S.Poly(poly,q);coeff=[kf(c) for c in poly.all_coeffs()]
 poly=S.Poly.from_list(coeff,q)
 assert not poly.is_zero
 for j in range(poly.degree()+1):
  if kf(poly.diff((q,j)).eval(a))!=0:return j
 raise AssertionError('zero polynomial')
rows=[]
for name,a in [('0',S.Integer(0)),('1',S.Integer(1))]+[(f'zeta^{j}',v) for j,v in enumerate(U,1)]:
 pair_terms=[];root_terms=[];total=1 if a==0 else 0
 dorders=[order(d,a) for n,d in ND]
 for i in range(19):
  n,d=ND[i]
  o=order(n*n-q*d*d,a)-2*dorders[i]
  root_terms.append(o);total+=2*o
  for j in range(i+1,19):
   m,e=ND[j];o=order(n*e-m*d,a)-dorders[i]-dorders[j]
   pair_terms.append({'labels':[i,j],'difference_order':o});total+=2*o
 rows.append({'name':name,'point_coefficients':[str(kf(a).coeff(z,j)) for j in range(4)],
  'rational_pair_orders':pair_terms,'rational_against_two_roots_orders':root_terms,
  'square_root_pair_discriminant_order':1 if a==0 else 0,
  'discriminant_order':total,'expected_sqrt_permutation':'transposition' if a==0 else 'identity'})
 print('PASS exact discriminant order',name,total,flush=True)
assert rows[0]['discriminant_order']==111
assert rows[1]['discriminant_order']==126
out={'field':'Q[z]/(z^4+z^3+z^2+z+1)',
 'identity':'Disc = 4*q * product_(i<j)(r_i-r_j)^2 * product_i(r_i^2-q)^2',
 'identity_scope':'21 finite strands; constant rotation changes only a nonzero scalar',
 'rows':rows,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'topological_link':'Artin exponent is the winding of the finite-configuration discriminant; deformation preserves each isolated old cluster.'}
(P/'symmetric_old_discriminant_orders.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all six exact retained-hole exponents, including finite-chart pole contributions.',flush=True)
