"""Higher-digit discovery test; structural proof is separate."""
from pathlib import Path
from collections import Counter
from math import gcd,isqrt
import json
q,n=5701,25
assert all(q%d for d in range(2,isqrt(q)+1))
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
assert len(points)==5625
assert all(mul(75,P) is None for P in points)
E25=[P for P in points if mul(25,P) is None]
assert len(E25)==625
z=next(a for a in range(2,q) if pow(a,3,q)==1)
mu=next(a for a in range(2,q) if pow(a,25,q)==1 and pow(a,5,q)!=1)
logs={pow(mu,a,q):a for a in range(25)}
def C(P):return None if P is None else (P[0]*z%q,P[1])
def T(v):return ((v[1]-v[0])%25,-v[0]%25)
def scale(a,v):return tuple(a*x%25 for x in v)
def enc(P,v):return ((-1,-1) if P is None else P)+v
units=[a for a in range(25) if gcd(a,25)==1]
mult={(a,P):mul(a,P) for a in units for P in E25}
def key(P,v):
 out=[]
 for a in units:
  R=mult[a,P]
  for i in range(3):
   w=scale(a,v)
   for j in range(3):
    out.append(enc(R,w));w=T(w)
   R=C(R)
 return min(out)
cubes={}
for w in range(q):cubes.setdefault(pow(w,3,q),w)
rows=[];counts=Counter()
for t in range(2,q):
 c1=t*(t-1)%q;c2=t*pow(t-1,-1,q)%q
 if c1 not in cubes or c2 not in cubes:continue
 w1,w2=cubes[c1],cubes[c2]
 Q=4*w1%q,(8*t-4)%q
 P=mul(72,Q) # -3Q, since 75Q=0
 assert P in E25
 r=(w2*z*z-z)*pow(w2-1,-1,q)%q
 v=logs[pow(r,(q-1)//25,q)],logs[pow((-1-r)%q,(q-1)//25,q)]
 primitive=mul(5,P) is not None and any(x%5 for x in v)
 k=key(P,v) if primitive else None
 if primitive:counts[k]+=1
 rows.append(dict(t=t,P=P,v=v,key=k))
for k,count in counts.items():
 P,v=k[:2],k[2:]
 orbit=[]
 for a in (1,6,11,16,21):orbit.append(counts[key(mul(a,P),v)])
 if len(set(orbit))>1:
  selected=k;break
else:raise AssertionError('no higher-digit obstruction found')
P0,v0=selected[:2],selected[2:]
def subgroup(a):return {(mul(b,mul(a,P0)),scale(b,v0)) for b in range(25)}
def fixed(P,v,J):
 total=0
 for i in range(3):
  w=v
  for j in range(3):
   if (P,w) in J:total+=15625
   w=T(w)
  P=C(P)
 return total
slope_counts={};contributing={}
for a in (1,6,11,16,21):
 J=subgroup(a)
 fs=[(row['t'],fixed(row['P'],row['v'],J)) for row in rows]
 slope_counts[a]=sum(b for t,b in fs)
 contributing[a]=[(t,b) for t,b in fs if b]
assert len(set(slope_counts.values()))>1
out=dict(q=q,n=n,E_order=len(points),E25_size=len(E25),zeta3=z,zeta25=mu,
         P0=P0,v0=v0,primitive_orbit_counts=orbit,
         slope_counts=slope_counts,contributing=contributing,rows=rows)
Path(__file__).with_name('third_derived_25_probe_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
