"""Exact finite-field checks; no external dependencies; not an OCR program.

Fields: F5, and F9=F3[i]/(i^2+1). Matrices are projective normalized.
The computations check a counterexample and a bad-characteristic refinement,
not all claims in the manuscript.
"""
import itertools,json
from pathlib import Path
from datetime import datetime,timezone

class Field:
 def __init__(self,p,quadratic=False):self.p=p;self.q=p*p if quadratic else p;self.quadratic=quadratic
 def add(self,a,b):
  p=self.p
  return ((a%p+b%p)%p)+p*((a//p+b//p)%p) if self.quadratic else (a+b)%p
 def neg(self,a):
  p=self.p
  return (-a%p)+p*(-(a//p)%p) if self.quadratic else (-a)%p
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):
  p=self.p
  if not self.quadratic:return a*b%p
  x,y=a%p,a//p;u,v=b%p,b//p
  return (x*u-y*v)%p+p*((x*v+y*u)%p)
 def inv(self,a):
  assert a
  return next(b for b in range(1,self.q) if self.mul(a,b)==1)
 def div(self,a,b):return self.mul(a,self.inv(b))
 def display(self,a):
  if a is None:return 'infinity'
  if not self.quadratic:return str(a)
  return f'{a%self.p}+{a//self.p}i'

def inspect(F,i):
 f=F.mul;add=F.add;sub=F.sub;neg=F.neg
 def norm(m):
  c=next(x for x in m if x);return tuple(F.div(x,c) for x in m)
 def prod(m,n):
  a,b,c,d=m;e,h,j,k=n
  return norm((add(f(a,e),f(b,j)),add(f(a,h),f(b,k)),add(f(c,e),f(d,j)),add(f(c,h),f(d,k))))
 def inv(m):
  a,b,c,d=m;return norm((d,neg(b),neg(c),a))
 def action(m,x):
  a,b,c,d=m
  top,bottom=(a,c) if x is None else (add(f(a,x),b),add(f(c,x),d))
  return F.div(top,bottom) if bottom else None
 mats=sorted({norm(m) for m in itertools.product(range(F.q),repeat=4) if sub(f(m[0],m[3]),f(m[1],m[2]))})
 one=norm((1,0,0,1));u=norm((neg(1),0,0,1));v=norm((0,1,1,0))
 V=frozenset((one,u,v,prod(u,v)))
 points=list(range(F.q))+[None]
 fixes=lambda m:frozenset(x for x in points if action(m,x)==x)
 fixed_union=lambda H:frozenset().union(*(fixes(g) for g in H if g!=one))
 S=fixed_union(V)
 assert S==frozenset((0,None,1,neg(1),i,neg(i))) and len(S)==6
 conjugate=lambda H,g:frozenset(prod(prod(g,h),inv(g)) for h in H)
 N=[g for g in mats if conjugate(V,g)==V]
 central=[g for g in mats if all(prod(g,h)==prod(h,g) for h in V)]
 autS=[g for g in mats if {action(g,x) for x in S}==S]
 conj={conjugate(V,g) for g in mats}
 same=[H for H in conj if fixed_union(H)==S]
 pairs=frozenset(fixes(g) for g in V if g!=one)
 faces=frozenset(frozenset(t) for t in itertools.product(*[tuple(p) for p in pairs]))
 facepairs=frozenset(frozenset((face,S-face)) for face in faces)
 def actset(g,T):return frozenset(action(g,x) for x in T)
 def actpair(g,Q):return frozenset(actset(g,t) for t in Q)
 assert len(faces)==8 and len(facepairs)==4
 assert len(N)==24 and len(central)==4
 perms={tuple(next(j for j,t in enumerate(facepairs) if t==actpair(g,Q)) for Q in facepairs) for g in N}
 assert len(perms)==24
 face=next(iter(faces));fp=next(Q for Q in facepairs if face in Q)
 fs=[g for g in N if actset(g,face)==face];fps=[g for g in N if actpair(g,fp)==fp]
 assert len(fs)==3 and len(fps)==6
 ram=fixed_union(N)
 ram_orbits=[];unused=set(ram)
 while unused:
  x=next(iter(unused));orb={action(g,x) for g in N};assert orb<=ram
  unused-=orb
  stab=[g for g in N if action(g,x)==x]
  ram_orbits.append({'orbit_size':len(orb),'stabilizer_size':len(stab)})
 trans=norm((1,1,0,1));Vt=conjugate(V,trans)
 result={
 'field':f'F{F.q}', 'pgl2_order':len(mats),
 'V':[list(m) for m in sorted(V)], 'fixed_set':[F.display(x) for x in points if x in S],
 'normalizer_order':len(N),'centralizer_order':len(central),
 'normalizer_faithful_on_four_face_pairs':len(perms)==24,
 'face_stabilizer_order':len(fs),'antipodal_face_pair_stabilizer_order':len(fps),
 'setwise_stabilizer_of_six_points_order':len(autS),
 'conjugate_V_with_same_six_points':len(same),
 'fixed_point_orbits_within_P1_of_field':sorted(ram_orbits,key=lambda z:z['orbit_size']),
 'all_geometric_fixed_points_in_this_field':all(len(fixes(g))==(1 if add(f(sub(g[0],g[3]),sub(g[0],g[3])),f(4%F.p,f(g[1],g[2])))==0 else 2) for g in N if g!=one),
 'translation_conjugate':{'matrix':list(trans),'V_prime':[list(m) for m in sorted(Vt)],'V_prime_differs':Vt!=V,'same_fixed_set':fixed_union(Vt)==S}}
 if F.q==5:
  assert len(mats)==120 and len(autS)==120 and len(same)==5
  assert Vt!=V and fixed_union(Vt)==S
 if F.q==9:
  assert len(autS)==24 and len(same)==1
  assert sorted((a['orbit_size'],a['stabilizer_size']) for a in ram_orbits)==[(4,6),(6,4)]
 return result

if __name__=='__main__':
 out={'checked_at_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'), 'checks':[inspect(Field(5),2),inspect(Field(3,True),3)]}
 p=Path(__file__).with_name('finite_octahedron_certificate.json');p.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
