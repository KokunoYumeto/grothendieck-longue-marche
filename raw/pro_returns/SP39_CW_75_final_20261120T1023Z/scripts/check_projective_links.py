#!/usr/bin/env python3
"""Explicit finite permutation morphisms for two links printed on scan 032."""
from itertools import product,permutations
from pathlib import Path
from datetime import datetime,timezone
import json

def pc(p,q):return tuple(p[q[i]] for i in range(len(p)))
def pi(p):return tuple(p.index(i) for i in range(len(p)))
def power(p,n):
 r=tuple(range(len(p)))
 for _ in range(n):r=pc(r,p)
 return r
def even(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0
def cyc(p):
 seen=set();out=[]
 for i in range(len(p)):
  if i in seen:continue
  c=[];j=i
  while j not in seen:seen.add(j);c.append(j+1);j=p[j]
  if len(c)>1:out.append('('+' '.join(map(str,c))+')')
 return ''.join(out) or 'id'

class Field:
 def __init__(self,q):self.q=q
 def add(self,a,b):return a^b if self.q==4 else (a+b)%5
 def neg(self,a):return a if self.q==4 else (-a)%5
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):
  if self.q==5:return a*b%5
  r=0
  while b:
   if b&1:r^=a
   b>>=1;a<<=1
   if a&4:a^=7
  return r
 def inv(self,a):return next(b for b in range(1,self.q) if self.mul(a,b)==1)
 def det(self,m):a,b,c,d=m;return self.sub(self.mul(a,d),self.mul(b,c))
 def norm(self,m):
  k=self.inv(next(x for x in m if x));return tuple(self.mul(k,x) for x in m)
 def mm(self,m,n):
  a,b,c,d=m;e,f,g,h=n
  return (self.add(self.mul(a,e),self.mul(b,g)),self.add(self.mul(a,f),self.mul(b,h)),self.add(self.mul(c,e),self.mul(d,g)),self.add(self.mul(c,f),self.mul(d,h)))
 def action(self,m):
  a,b,c,d=m;out=[]
  for t in [None,*range(self.q)]:
   u,v=(a,c) if t is None else (self.add(self.mul(a,t),b),self.add(self.mul(c,t),d))
   out.append(0 if v==0 else self.mul(u,self.inv(v))+1)
  return tuple(out)

F4=Field(4);F5=Field(5)
SL4={m for m in product(range(4),repeat=4) if F4.det(m)==1}
P4={F4.norm(m) for m in product(range(4),repeat=4) if F4.det(m)}
P5={F5.norm(m) for m in product(range(5),repeat=4) if F5.det(m)}
a4={m:F4.action(m) for m in SL4}
assert len(SL4)==len(P4)==len(set(a4.values()))==60
A5=set(filter(even,permutations(range(5))))
assert set(a4.values())==A5=={F4.action(m) for m in P4}
assert all(a4[F4.mm(m,n)]==pc(a4[m],a4[n]) for m in SL4 for n in SL4)
p5={m:F5.action(m) for m in P5};assert len(p5)==len(set(p5.values()))==120
assert all(p5[F5.norm(F5.mm(m,n))]==pc(p5[m],p5[n]) for m in P5 for n in P5)

S5=set(permutations(range(5)));identity=tuple(range(5))
subgroups=sorted({tuple(sorted(power(g,k) for k in range(5))) for g in S5 if g!=identity and power(g,5)==identity})
assert len(subgroups)==6
sid={H:i for i,H in enumerate(subgroups)}
rho={g:tuple(sid[tuple(sorted(pc(pc(g,h),pi(g)) for h in H))] for H in subgroups) for g in S5}
assert len(set(rho.values()))==120
assert all(rho[pc(g,h)]==pc(rho[g],rho[h]) for g in S5 for h in S5)
target=set(p5.values())
generators=[(1,0,2,3,4),(1,2,3,4,0)]
u=None
for candidate in permutations(range(6)):
 inv=pi(candidate)
 if all(pc(pc(candidate,rho[g]),inv) in target for g in generators):
  if {pc(pc(candidate,r),inv) for r in rho.values()}==target:
   u=candidate;break
assert u is not None
rho_inverse={r:g for g,r in rho.items()}
phi={m:rho_inverse[pc(pc(pi(u),p5[m]),u)] for m in P5}
assert set(phi.values())==S5
assert all(phi[F5.norm(F5.mm(m,n))]==pc(phi[m],phi[n]) for m in P5 for n in P5)
out={
 'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
 'field_models':{'F4':'0,1,a,a+1 encoded 0,1,2,3; a^2+a+1=0; bitwise polynomial arithmetic','F5':'residue classes 0,1,2,3,4'},
 'projective_point_order':{'F4':['infinity','0','1','a','a+1'],'F5':['infinity','0','1','2','3','4']},
 'matrix_convention':'row-major [a,b,c,d]; t maps to (at+b)/(ct+d). Projective representatives are scaled so the first nonzero entry is 1.',
 'sizes':{'SL2_F4':len(SL4),'PGL2_F4':len(P4),'PGL2_F5':len(P5),'cyclic_order5_subgroups_of_S5':len(subgroups)},
 'SL2_F4_to_A5':[{'matrix':m,'permutation':[x+1 for x in a4[m]],'cycles':cyc(a4[m])} for m in sorted(SL4)],
 'six_subgroups':[[[x+1 for x in g] for g in H] for H in subgroups],
 'subgroup_to_projective_point_index_zero_based':u,
 'PGL2_F5_to_S5':[{'matrix':m,'permutation':[x+1 for x in phi[m]],'cycles':cyc(phi[m])} for m in sorted(P5)],
 'verification':'All 3600 products for SL2(F4), all 14400 projective products for PGL2(F5), and all 14400 products in the S5 conjugation action were verified entrywise. The explicit maps are bijective onto A5 and S5, respectively.',
 'scope':'These are concrete permutation-model checks of the Sl/GP links using SL2 and PGL2. The SO(3) links and the icosahedral dictionaries are not checked here.'}
path=Path(__file__).resolve().parents[1]/'decisions/scan032_projective_check.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['utc','sizes','subgroup_to_projective_point_index_zero_based','verification','scope']}))
