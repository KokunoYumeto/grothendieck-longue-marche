"""Independent exact recheck of LM6 A.54 and A.55 point-count certificates.
No supplied program is read or imported. Elliptic law and subgroup cosets are explicit.
"""
import json
from pathlib import Path
from sympy import isprime

def run(q,n,zeta3,zetan,P0,v0,parameters,kummer):
 assert isprime(q)
 def add(P,Q):
  if P is None:return Q
  if Q is None:return P
  x,y=P;u,v=Q
  if x==u:
   if (y+v)%q==0:return None
   m=(3*x*x)*pow(2*y,-1,q)%q
  else:m=(v-y)*pow(u-x,-1,q)%q
  a=(m*m-x-u)%q
  return (a,(m*(x-a)-y)%q)
 def times(k,P):
  if k<0:return times(-k,None if P is None else(P[0],-P[1]%q))
  R=None
  while k:
   if k&1:R=add(R,P)
   P=add(P,P);k//=2
  return R
 squares={}
 for y in range(q):squares.setdefault(y*y%q,[]).append(y)
 E=[None]+[(x,y) for x in range(q) for y in squares.get((x*x*x+16)%q,[])]
 assert len(E)==(3*n)**2
 assert all(times(3*n,P) is None for P in E)
 assert sum(times(n,P) is None for P in E)==n*n
 assert times(n,P0) is None and times(n//5,P0) is not None
 assert pow(zeta3,3,q)==1 and zeta3!=1
 assert pow(zetan,n,q)==1 and pow(zetan,n//5,q)!=1
 log={pow(zetan,k,q):k for k in range(n)}
 cubes={}
 for w in range(q):cubes.setdefault(pow(w,3,q),[]).append(w)
 J={a:{(times(k*a,P0),(k*v0[0]%n,k*v0[1]%n)) for k in range(n)} for a in parameters}
 def T(v):a,b=v;return((b-a)%n,-a%n)
 def orbitpoint(P):
  return [None]*3 if P is None else[((pow(zeta3,i,q)*P[0])%q,P[1]) for i in range(3)]
 counts={a:0 for a in parameters};fibres={a:[] for a in parameters};eligible=0;root_checks=0
 for t in range(2,q):
  ws1=cubes.get(t*(t-1)%q,[]);ws2=cubes.get(t*pow(t-1,-1,q)%q,[])
  if not ws1 or not ws2:continue
  eligible+=1;local=None
  for w1 in ws1:
   for w2 in ws2:
    Q=(4*w1%q,(8*t-4)%q)
    assert (Q[1]**2-Q[0]**3-16)%q==0
    d=times(kummer,Q)
    rr=(w2*zeta3*zeta3-zeta3)*pow(w2-1,-1,q)%q
    vv=(log[pow(rr,(q-1)//n,q)],log[pow((-1-rr)%q,(q-1)//n,q)])
    vo=[vv,T(vv),T(T(vv))]
    here={a:n**3*sum((u,v) in J[a] for u in orbitpoint(d) for v in vo) for a in parameters}
    if local is None:local=here
    assert here==local
    root_checks+=1
  for a,c in local.items():
   counts[a]+=c
   if c:fibres[a].append([t,c])
 return {'q':q,'n':n,'elliptic_points':len(E),'rational_n_torsion':n*n,'exponent_verified':3*n,'eligible_base_values':eligible,'root_pair_checks':root_checks,'counts':counts,'nonzero_fibres':fibres}

r5=run(211,5,14,55,(103,117),(3,1),[1,4],3)
r25=run(5701,25,75,303,(25,2322),(0,23),[1,6,11,16,21],-3)
assert r5['counts']=={1:250,4:0}
assert r25['counts']=={1:15625,6:0,11:0,16:0,21:15625}
out={'LM6_A54':r5,'LM6_A55':r25}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
