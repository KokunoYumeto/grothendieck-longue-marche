"""Exact second-digit certificate for A:third-derived-second-digit.

This uses no imported probe: it directly enumerates all base points,
all cubic-root choices, and membership in the two fixed order25 groups.
The geometric and arithmetic identifications are proved in A.54--A.55.
"""
from pathlib import Path
from math import isqrt,gcd
import json
q,n=5701,25
assert all(q%d for d in range(2,isqrt(q)+1))
z,mu=75,303
assert pow(z,3,q)==1 and z!=1
assert pow(mu,25,q)==1 and pow(mu,5,q)!=1
sq={}
for y in range(q):sq.setdefault(y*y%q,[]).append(y)
points=[None]+[(x,y) for x in range(q) for y in sq.get((x*x*x+16)%q,[])]
def add(P,Q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and (y+v)%q==0:return None
 m=((v-y)*pow(u-x,-1,q) if x!=u else 3*x*x*pow(2*y,-1,q))%q
 a=(m*m-x-u)%q
 return a,(m*(x-a)-y)%q
def mul(a,P):
 R=None
 while a:
  if a&1:R=add(R,P)
  P=add(P,P);a>>=1
 return R
assert len(points)==5625 and all(mul(75,P) is None for P in points)
E25={P for P in points if mul(25,P) is None}
assert len(E25)==625
pi=[(a,b) for a in range(-100,101) for b in range(-100,101)
    if 2*a-b==77 and a*a-a*b+b*b==q]
assert pi==[(1,-75),(76,75)]
P0,v0=(25,2322),(0,23)
assert P0 in E25 and mul(5,P0) is not None

def C(P):return None if P is None else (z*P[0]%q,P[1])
def T(v):return (v[1]-v[0])%n,-v[0]%n
def scale(a,v):return tuple(a*x%n for x in v)
subgroups={s:{(mul(a,mul(s,P0)),scale(a,v0)) for a in range(n)}
           for s in (1,6,11,16,21)}
assert all(len(J)==25 for J in subgroups.values())
for slope,J in subgroups.items():
 for unit in (a for a in range(25) if gcd(a,25)==1):
  assert {(mul(b,mul(unit*slope,P0)),scale(b,scale(unit,v0)))
          for b in range(25)}==J
def fixed(P,v,J):
 total=0
 for i in range(3):
  w=v
  for j in range(3):
   if (P,w) in J:total+=15625
   w=T(w)
  P=C(P)
 return total
logs={pow(mu,a,q):a for a in range(n)}
cubes={}
for w in range(q):cubes.setdefault(pow(w,3,q),[]).append(w)
rows=[];nontrivial_cubic=0
for t in range(2,q):
 a,b=t*(t-1)%q,t*pow(t-1,-1,q)%q
 if a not in cubes or b not in cubes:
  nontrivial_cubic+=1;continue
 vals=[]
 for w1 in cubes[a]:
  Q=(4*w1%q,(8*t-4)%q)
  P=mul(72,Q) # delta25(Q)=-3Q up to a common C3 rotation.
  assert P in E25
  for w2 in cubes[b]:
   r=(w2*z*z-z)*pow(w2-1,-1,q)%q
   v=(logs[pow(r,228,q)],logs[pow((-1-r)%q,228,q)])
   vals.append(tuple(fixed(P,v,J) for J in subgroups.values()))
 assert len(vals)==9 and len(set(vals))==1
 rows.append(dict(t=t,counts=dict(zip(subgroups,vals[0]))))
totals={s:sum(r['counts'][s] for r in rows) for s in subgroups}
assert totals=={1:15625,6:0,11:0,16:0,21:15625}
contributions={s:[(r['t'],r['counts'][s]) for r in rows if r['counts'][s]]
               for s in subgroups}
assert contributions[1]==[(8,15625)] and contributions[21]==[(4104,15625)]
out=dict(status='all exact checks passed',q=q,n=n,zeta3=z,zeta25=mu,
         E_order=5625,E25_size=625,E_exponent=75,pi_options=pi,
         P0=P0,v0=v0,group_order=3515625,subgroup_order=25,cover_degree=140625,
         base_point_count=q-2,trivial_cubic_fibres=len(rows),
         nontrivial_cubic_fibres=nontrivial_cubic,root_choices_checked=9*len(rows),
         subgroup_generator_choices_checked=100,
         slope_counts=totals,contributions=contributions,all_trivial_cubic_rows=rows)
Path(__file__).with_name('third_derived_25_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_trivial_cubic_rows'},indent=2))
