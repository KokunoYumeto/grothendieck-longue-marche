#!/usr/bin/env python3
"""Complete genus-three mixed actions with a Klein-bottle quotient.
All oriented index-two extensions of C2,C3,C4,V4; all smooth generating
monodromies; exact complete source automorphisms; all section data.
Standard library only. See B.41 and Gromadzki--Szepietowski Lemma3.3.
"""
from itertools import product,permutations
from collections import Counter,deque
from fractions import Fraction
from pathlib import Path
import json,csv
OUT=Path(__file__).resolve().parent

def pmul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def pinv(a):
 v=[0]*len(a)
 for i,x in enumerate(a):v[x]=i
 return tuple(v)
class Group:
 def __init__(self,gens):
  identity=tuple(range(len(gens[0])));seen={identity};todo=[identity]
  for a in todo:
   for b in gens:
    c=pmul(a,b)
    if c not in seen:seen.add(c);todo.append(c)
  self.el=sorted(seen);self.n=len(self.el);self.ids={g:i for i,g in enumerate(self.el)}
  self.one=self.ids[identity]
  self.mul=[[self.ids[pmul(a,b)] for b in self.el] for a in self.el]
  self.inv=[self.ids[pinv(a)] for a in self.el]
  self.powers=[];self.orders=[]
  for a in range(self.n):
   ps=[self.one];x=a
   while x!=self.one:ps.append(x);x=self.mul[x][a]
   self.powers.append(ps);self.orders.append(len(ps))
 def prod(self,seq):
  x=self.one
  for a in seq:x=self.mul[x][a]
  return x
 def conj(self,a,b):return self.prod([a,b,self.inv[a]])
 def subgroup(self,gens):
  seen={self.one};todo=[self.one]
  for x in todo:
   for a in gens:
    y=self.mul[x][a]
    if y not in seen:seen.add(y);todo.append(y)
  return frozenset(seen)
 def cosets(self,h):
  left=set(range(self.n));out=[]
  while left:
   x=min(left);c=frozenset(self.mul[x][a] for a in h);left-=c;out.append((x,c))
  return out
 def name(self):
  n=self.n;orders=Counter(self.orders);ab=all(self.mul[x][y]==self.mul[y][x] for x in range(n) for y in range(n))
  if max(self.orders)==n:return f'C{n}'
  if ab:return 'V4' if n==4 else 'C4_x_C2' if max(self.orders)==4 else 'C2^3'
  if n==6:return 'S3'
  if n==8:return 'D8' if orders[2]==5 else 'Q8'
  raise AssertionError((n,orders))

def automorphisms(g,orientation=None):
 other=[x for x in range(g.n) if x!=g.one];out=[]
 for image in permutations(other):
  v=[None]*g.n;v[g.one]=g.one
  for x,y in zip(other,image):v[x]=y
  if any(g.orders[x]!=g.orders[v[x]] for x in other):continue
  if orientation is not None and any(orientation[x]!=orientation[v[x]] for x in other):continue
  if all(v[g.mul[x][y]]==g.mul[v[x]][v[y]] for x in range(g.n) for y in range(g.n)):out.append(tuple(v))
 return out

def extensions(h):
 autos=automorphisms(h);valid=set()
 for a in autos:
  for A in range(h.n):
   if a[A]==A and all(a[a[x]]==h.conj(A,x) for x in range(h.n)):valid.add((a,A))
 left=set(valid);out=[]
 while left:
  first=min(left);orb={first};todo=[first]
  for a,A in todo:
   neighbors=[]
   for k in range(h.n):neighbors.append((tuple(h.conj(k,a[x]) for x in range(h.n)),h.prod([k,a[k],A])))
   for b in autos:
    bi=[0]*h.n
    for i,j in enumerate(b):bi[j]=i
    neighbors.append((tuple(b[a[bi[x]]] for x in range(h.n)),b[A]))
   for st in neighbors:
    assert st in valid
    if st not in orb:orb.add(st);todo.append(st)
  left-=orb;a,A=first;N=h.n
  def gm(v,w):
   x,i=v%N,v//N;y,j=w%N,w//N
   z=h.mul[x][a[y] if i else y]
   if i and j:z=h.mul[z][A]
   return z+N*(i^j)
  assert all(gm(gm(x,y),z)==gm(x,gm(y,z)) for x,y,z in product(range(2*N),repeat=3))
  g=Group([tuple(gm(v,w) for w in range(2*N)) for v in range(2*N)])
  orientation=tuple(1 if p[h.one]<N else -1 for p in g.el)
  assert all(orientation[g.mul[x][y]]==orientation[x]*orientation[y] for x in range(g.n) for y in range(g.n))
  out.append((g,orientation,{'alpha':a,'negative_square':A,'extension_parameter_orbit':sorted(orb)}))
 return out

def pair_orbits(g,orientation,m):
 positive=[i for i in range(g.n) if orientation[i]==1];negative=[i for i in range(g.n) if orientation[i]==-1]
 def cone(y,z):return g.inv[g.prod([y,z,g.inv[y],z])]
 valid={(y,z) for y,z in product(negative,positive) if g.orders[cone(y,z)]==m and len(g.subgroup([y,z]))==g.n}
 aut=automorphisms(g,orientation);left=set(valid);orbs=[]
 while left:
  first=min(left);orb={first};todo=[first]
  for y,z in todo:
   neighbors=[(g.mul[y][z],z),(g.inv[y],z),(y,g.inv[z])]+[(a[y],a[z]) for a in aut]
   for st in neighbors:
    assert st in valid
    if st not in orb:orb.add(st);todo.append(st)
  left-=orb;orbs.append(sorted(orb))
 return orbs,cone

def section_data(g,orientation,cones,orders):
 points=[]
 for j,(x,m) in enumerate(zip(cones,orders)):
  assert g.orders[x]==m and orientation[x]==1
  h=frozenset(g.powers[x])
  for rep,c in g.cosets(h):
   stab=frozenset(g.conj(rep,a) for a in h)
   rotation=g.conj(rep,x)
   mus={a:str(Fraction(orientation[rep]*k,m)%1) for k,a in enumerate(g.powers[rotation])}
   for k,a in enumerate(g.powers[rotation]):
    v=Fraction(mus[a]);assert v.denominator==g.orders[a]
    assert v==(orientation[rep]*Fraction(k,m))%1
   points.append({'point_id':len(points),'cone':j,'coset_elements':sorted(c),
    'stabilizer_elements':sorted(stab),'local_generator':rotation,'mu':mus})
 # All local orders here are prime, so each critical point has exactly one
 # nontrivial local subgroup and hence one maximal partial section.
 assert all(m in (2,3) for m in orders)
 records=[]
 for p in points:
  i=p['point_id'];records.append({'section_id':i,'image_elements':p['stabilizer_elements'],'kind':'point',
   'fixed_point':i,'centralizer':'1','mu':p['mu'],'maximal':True,
   'strict_extensions':[],'maximal_overgroups':[i],'Gamma_stabilizer':p['stabilizer_elements']})
 orbits=[[p['point_id'] for p in points if p['cone']==j] for j in range(len(cones))]
 keys={(p['cone'],frozenset(p['coset_elements'])):p['point_id'] for p in points}
 actions=[[keys[(p['cone'],frozenset(g.mul[a][b] for b in p['coset_elements']))] for p in points] for a in range(g.n)]
 assert all(sorted(v)==list(range(len(points))) for v in actions)
 return {'full_splitting_classes':0,'nontrivial_partial_splitting_classes':len(points),
  'maximal_partial_classes_Phi':len(points),'Gamma_orbits_on_Phi':len(cones),
  'oval_section_classes':0,'line_section_classes':0}, {'points':points,'sections':records,'Phi_orbits':orbits,'Gamma_action_on_points':actions}

def main():
 positive={'C2':Group([(1,0)]),'C3':Group([(1,2,0)]),'C4':Group([(1,2,3,0)]),
           'V4':Group([tuple(i^1 for i in range(4)),tuple(i^2 for i in range(4))])}
 source={'C2':'O3.3','C3':'O3.5','C4':'O3.7','V4':'O3.8'}
 expected_extensions={'C2':2,'C3':2,'C4':4,'V4':3}
 rows=[];details=[];all_attempts=[]
 for hname,h in positive.items():
  exts=extensions(h);assert len(exts)==expected_extensions[hname]
  for ei,(g,ori,edata) in enumerate(exts,1):
   if hname=='C2':
    a=next(x for x in range(g.n) if ori[x]==1 and x!=g.one)
    negatives=[x for x in range(g.n) if ori[x]==-1]
    valid={(d1,d2) for d1,d2 in product(negatives,repeat=2)
           if g.prod([d1,d1,a,d2,d2,a])==g.one and len(g.subgroup([a,d1,d2]))==g.n}
    assert len(valid)==4
    first=min(valid);seen={first};todo=[first]
    for d1,d2 in todo:
     for st in ((g.mul[d1][a],d2),(d1,g.mul[d2][a]),(d2,d1)):
      assert st in valid
      if st not in seen:seen.add(st);todo.append(st)
    assert seen==valid
    orbs=[sorted(seen)];cone=lambda d1,d2:a;ms=[2,2]
   else:
    m=3 if hname=='C3' else 2;orbs,cone=pair_orbits(g,ori,m);ms=[m]
   all_attempts.append({'positive_group':hname,'extension_group':g.name(),'extension_id':ei,
    'oriented_extension_data':edata,'valid_monodromy_orbits':orbs})
   for orb in orbs:
    v=orb[0];xs=[cone(*v)]*len(ms)
    chi=-sum((1-Fraction(1,m) for m in ms),Fraction())
    assert g.n*chi==-4
    cid=f'G3Klein_{len(rows)+1:02}';summary,data=section_data(g,ori,xs,ms)
    row={'class_id':cid,'type':'(3,0)','positive_source':source[hname],'positive_group':hname,
     'group':g.name(),'order':g.n,'positive_order':h.n,'cone_orders':str(ms),**summary}
    data.update({'class_id':cid,'positive_source':source[hname],'group':g.name(),
     'group_elements':[{'id':i,'permutation':p,'orientation':ori[i],'order':g.orders[i]} for i,p in enumerate(g.el)],
     'multiplication':g.mul,'monodromy_generators':({'d1':v[0],'d2':v[1],'x1':xs[0],'x2':xs[1]} if hname=='C2' else {'y':v[0],'z':v[1],'x':xs[0]}),
     'monodromy_orbit':orb,'quotient_euler_characteristic':str(chi),'cover_euler_characteristic':str(g.n*chi),
     'oriented_extension_data':edata})
    rows.append(row);details.append(data)
 assert len(rows)==6
 assert Counter(r['positive_source'] for r in rows)=={'O3.3':2,'O3.5':1,'O3.7':2,'O3.8':1}
 with (OUT/'type_3_0_klein_quotient_catalogue.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (OUT/'type_3_0_klein_quotient_sections.json').write_text(json.dumps({'catalogue':details,'all_oriented_extension_attempts':all_attempts},indent=2)+'\n')
 summary={'mixed_klein_quotient_classes':len(rows),'by_positive_source':dict(Counter(r['positive_source'] for r in rows)),
          'groups':[r['group'] for r in rows],'all_oriented_extension_counts':expected_extensions}
 (OUT/'catalogue_genus3_klein_output.json').write_text(json.dumps(summary,indent=2)+'\n')
 print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
