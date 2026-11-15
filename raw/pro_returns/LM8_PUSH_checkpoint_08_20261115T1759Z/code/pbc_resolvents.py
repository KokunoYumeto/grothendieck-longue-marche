#!/usr/bin/env python3
"""Exact subgroup/coset certificates and the explicit degree-five resolvents.
No supplied finite-group module is imported.
"""
import json
from pathlib import Path
from itertools import product
import sympy as sp

def run(p,bmat):
 def norm(a):
  a=tuple(v%p for v in a);z=next(v for v in a if v);iz=pow(z,-1,p)
  return tuple(v*iz%p for v in a)
 def det(a):return (a[0]*a[3]-a[1]*a[2])%p
 def mul(a,b):
  return norm((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
 def inv(a):return norm((a[3],-a[1],-a[2],a[0]))
 one=norm((1,0,0,1));S=norm((0,-1,1,0));R=norm((0,-1,1,-1));B=norm(bmat)
 def closure(gs):
  out={one};todo=[one]
  while todo:
   a=todo.pop()
   for g in gs:
    b=mul(a,g)
    if b not in out:out.add(b);todo.append(b)
  return out
 G=closure([S,R]);H=closure([S,B]);allpg={norm(a) for a in product(range(p),repeat=4) if det(a)}
 assert len(G)==p*(p*p-1)//2 and len(allpg)==p*(p*p-1)
 assert H<=G and len(H)==(p*p-1)//2
 def order(a):
  b=one
  for n in range(1,len(G)+1):
   b=mul(b,a)
   if b==one:return n
  raise AssertionError
 assert order(S)==2 and order(B)==3 and order(mul(S,B))=={5:3,7:4,11:5}[p]
 cosets=[];which={}
 for g in sorted(G):
  if g in which:continue
  c={mul(g,h) for h in H};i=len(cosets);cosets.append(c)
  for a in c:which[a]=i
 assert len(cosets)==p
 reps=[min(c) for c in cosets]
 def cycles(g):
  perm=[which[mul(g,r)] for r in reps];seen=set();lens=[]
  for i in range(p):
   if i in seen:continue
   j=i;n=0
   while j not in seen:seen.add(j);n+=1;j=perm[j]
   lens.append(n)
  return sorted(lens)
 def cj(g,h):return mul(mul(g,h),inv(g))
 normal=[g for g in allpg if {cj(g,h) for h in H}==H]
 sc=cycles(S);rc=cycles(R);tc=cycles(mul(S,R))
 e2=sc.count(1);e3=rc.count(1);cusps=len(tc)
 genus=1+sp.Rational(p,12)-sp.Rational(e2,4)-sp.Rational(e3,3)-sp.Rational(cusps,2)
 assert (e2,e3,cusps,genus)=={5:(1,2,1,0),7:(3,1,1,0),11:(3,2,1,0)}[p]
 out=dict(p=p,G_order=len(G),H_order=len(H),H_generators=[S,B],generator_orders=[2,3,order(mul(S,B))],
          index=len(cosets),S_cycles=sc,R_cycles=rc,SR_cycles=tc,e2=e2,e3=e3,cusps=cusps,genus=int(genus),
          PGL_normalizer_order=len(normal),PSL_normalizer_order=sum(g in G for g in normal))
 if p==5:
  three={h for h in H if order(h)==3};classes=[]
  while three:
   h=min(three);c={cj(g,h) for g in H};classes.append(c);three-=c
  assert sorted(map(len,classes))==[4,4]
  table=[]
  for lam in range(1,15):
   if sp.gcd(lam,15)!=1:continue
   legendre=1 if pow(lam%5,2,5)==1 else -1
   n=next(g for g in normal if (1 if pow(det(g),2,5)==1 else -1)==legendre)
   h=min(classes[0]);hh=h if lam%3==1 else inv(h)
   target=cj(n,hh);flip=int(target not in classes[0])
   expected=legendre*(1 if lam%3==1 else -1)
   assert flip==int(expected==-1)
   odd_lam=lam if lam%2 else lam+15
   assert int(sp.kronecker_symbol(-15,odd_lam))==expected
   table.append(dict(lambda_mod15=lam,swaps_order3_factors=bool(flip),kronecker_minus15=expected))
  out['factor_permutation_table']=table
 return out

out={'finite_actions':[run(5,(4,2,1,2)),run(7,(2,4,1,6)),run(11,(3,4,1,9))]}
t=sp.symbols('t');j=27*t**3*(9*t*t+15*t+40)
assert sp.expand(j-1728-27*(t-1)*(3*t*t+4*t+8)**2)==0
assert sp.factor(sp.diff(j,t))==405*t*t*(3*t*t+4*t+8)
bp=(-5+3*sp.sqrt(-15))/6;bm=(-5-3*sp.sqrt(-15))/6
assert sp.simplify(j.subs(t,bp))==0 and sp.simplify(j.subs(t,bm))==0
res=[]
for b in [bp,bm]:
 r=1728*(t-b)/(1-b)
 assert sp.simplify(r.subs(t,b))==0 and sp.simplify(r.subs(t,1))==1728
 res.append(str(r))
out['degree5_polynomial']=str(j)
out['degree5_factorization_1728']=str(27*(t-1)*(3*t*t+4*t+8)**2)
out['order3_points']=[str(bp),str(bm)]
out['order2_point']=1;out['cusp']='infinity';out['resolvent_coordinates']=res
out['all_assertions_passed']=True
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
