#!/usr/bin/env python3
"""Exploratory exact primitive-character Frobenius polynomials for D_lambda.
D_lambda: y^4=s(s-1)^2, z^5=s-lambda, lambda=(1+2i)/5.
W=yz satisfies W^20=s^5(s-1)^10(s-lambda)^4.
Not a registered theorem or CM conclusion.
"""
from pathlib import Path
import json
import sympy as s
z=s.symbols('z');Phi=s.cyclotomic_poly(20,z)
def red(a):return s.Poly(s.rem(s.expand(a),Phi,z),z,domain=s.QQ).as_expr()
def trace_character(q,degree):
 g=s.primitive_root(q);i=pow(g,(q-1)//4,q);lam=(1+2*i)*pow(5,-1,q)%q
 logs={pow(g,j,q):j%20 for j in range(q-1)}
 ns=next(a for a in range(2,q) if pow(a,(q-1)//2,q)==q-1)
 counts=[0]*20
 if degree==1:
  for a in range(q):
   ff=pow(a,5,q)*pow(a-1,10,q)*pow(a-lam,4,q)%q
   if ff:counts[logs[ff]]+=1
 else:
  for a in range(q):
   for b in range(q):
    b2=ns*b*b%q
    n0=(a*a-b2)%q;n1=((a-1)**2-b2)%q;nl=((a-lam)**2-b2)%q
    ff=pow(n0,5,q)*pow(n1,10,q)*pow(nl,4,q)%q
    if ff:counts[logs[ff]]+=1
 a=red(-sum(n*z**j for j,n in enumerate(counts)))
 return a,dict(q=q,degree=degree,primitive_root=int(g),i=i,lambda_residue=lam,quadratic_nonsquare=ns,character_counts=counts)
rows=[]
for q in (41,61,101,181):
 a,m1=trace_character(q,1);a2,m2=trace_character(q,2)
 d=red((a*a-a2)/2);disc=red(a*a-4*d)
 assert all(c.q==1 for c in s.Poly(d,z).all_coeffs())
 # Norm of the discriminant is retained only as a necessary square test.
 norm=s.resultant(Phi,disc,z)
 row=dict(q=q,trace=str(a),trace_square_Frob=str(a2),determinant=str(d),discriminant=str(disc),discriminant_norm=str(norm),count_data=[m1,m2])
 rows.append(row)
 print(json.dumps({k:v for k,v in row.items() if k!='count_data'},sort_keys=True),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'exploratory exact character sums; geometric identification and non-CM proof pending','cyclotomic_polynomial':str(Phi),'rows':rows},indent=2)+'\n')
print('Exact character sums complete.',flush=True)
