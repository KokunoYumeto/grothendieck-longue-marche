#!/usr/bin/env python3
"""Order-24 arithmetic quotient and exact local polynomial certificates."""
from D_finite import generated,mul
from collections import Counter
from sympy import symbols,Poly,discriminant
import json
n=4
r=(0,1,3,1);s=(0,1,3,0);tau=(3,0,0,1);I=(1,0,0,1)
K=generated([(3,2,0,3),(3,0,2,3)],n)
G=generated([r,s,tau],n)
assert len(K)==4 and len(G)==96
iv=lambda g:(g[3]*pow((g[0]*g[3]-g[1]*g[2])%4,-1,4)%4,
 -g[1]*pow((g[0]*g[3]-g[1]*g[2])%4,-1,4)%4,
 -g[2]*pow((g[0]*g[3]-g[1]*g[2])%4,-1,4)%4,
 g[0]*pow((g[0]*g[3]-g[1]*g[2])%4,-1,4)%4)
assert all(mul(mul(g,k,n),iv(g),n) in K for g in G for k in K)
cosets={};reps=[]
for g in sorted(G):
 if g not in cosets:
  idx=len(reps);reps.append(g)
  for k in K:cosets[mul(g,k,n)]=idx
assert len(reps)==24
assert cosets[mul(mul(tau,r,n),tau,n)]==cosets[r]
assert cosets[mul(mul(tau,s,n),tau,n)]==cosets[iv(s)]
identity=cosets[I]
orders=[]
for i,g in enumerate(reps):
 a=I
 for j in range(1,25):
  a=mul(a,g,n)
  if cosets[a]==identity:orders.append(j);break
x=symbols('x')
f=x**3-2;g=x**4-3
def eisenstein(f,p):
 c=[int(a) for a in Poly(f,x).all_coeffs()]
 return c[0]%p!=0 and all(a%p==0 for a in c[1:]) and c[-1]%(p*p)!=0
certificates=[
 {'field':'Q2(cuberoot2)','polynomial':str(f),'p':2,'Eisenstein':eisenstein(f,2)},
 {'field':'Q3(cuberoot2)','polynomial':str(f.subs(x,x-1).expand()),'p':3,'Eisenstein':eisenstein(f.subs(x,x-1).expand(),3)},
 {'field':'Q2(fourthroot3)','polynomial':str(g.subs(x,x+1).expand()),'p':2,'Eisenstein':eisenstein(g.subs(x,x+1).expand(),2)},
 {'field':'Q3(fourthroot3)','polynomial':str(g),'p':3,'Eisenstein':eisenstein(g,3)}]
assert all(c['Eisenstein'] for c in certificates)
print(json.dumps(dict(GL2_mod4=len(G),normal_V4=len(K),
 arithmetic_quotient_order=len(reps),
 arithmetic_quotient_order_distribution=dict(Counter(orders)),
 tau_fixes_rho=True,tau_inverts_sigma=True,
 cubic_discriminant=int(discriminant(f,x)),quartic_discriminant=int(discriminant(g,x)),
 local_eisenstein_certificates=certificates,
 local_quadratic_square_classes={'at2':'sqrt(-3) unramified since -3=5 mod8','at3':'i unramified since -1 is nonsquare mod3'},
 local_invariants_derived_in_D16={'K_over_Q':{'2':{'e':12,'f':2,'g':1},'3':{'e':12,'f':2,'g':1}},
 'K_over_Qi':{'2':{'e':6,'f':2,'g':1},'3':{'e':12,'f':1,'g':1}}}),indent=2))
