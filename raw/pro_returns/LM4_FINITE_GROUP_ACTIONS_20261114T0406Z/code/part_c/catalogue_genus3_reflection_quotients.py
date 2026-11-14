#!/usr/bin/env python3
"""Genus-three mixed actions whose positive quotient is a sphere and whose
induced involution on that sphere has a fixed circle.
Uses the attributed complete Aut(H)-normalized KNS genus-three vectors.
All equivalence generators are induced by homeomorphisms of the quotient
mirror disc: colored interior braids and colored boundary dihedral maps.
"""
from pathlib import Path
from itertools import product,permutations
from collections import Counter,deque
from fractions import Fraction
import json,csv,sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'root'
if not (ROOT/'catalogue_higher_genus.py').exists():ROOT=HERE.parents[1]/'root'
sys.path.insert(0,str(ROOT))
from catalogue_higher_genus import Group,braid,braid_generators

def ordered(G,v,orders,target):
 v=tuple(v);orders=tuple(orders)
 for i,m in enumerate(target):
  j=next(j for j in range(i,len(orders)) if orders[j]==m)
  for k in range(j-1,i-1,-1):v,orders=braid(G,v,orders,k,1)
 assert orders==tuple(target)
 return v

def types(ms):
 counts=Counter(ms);keys=sorted(counts)
 out=[]
 for ns in product(*(range(counts[m]//2+1) for m in keys)):
  interior=tuple(m for m,n in zip(keys,ns) for _ in range(n))
  boundary=tuple(m for m,n in zip(keys,ns) for _ in range(counts[m]-2*n))
  words=set(permutations(boundary))
  cyc=set()
  for w in words:
   if not w:q=()
   else:q=min(z[s:]+z[:s] for z in (w,tuple(reversed(w))) for s in range(len(w)))
   cyc.add(q)
  out.extend((c,interior) for c in sorted(cyc))
 return out

def hom(G,gens,images):
 seen={G.one:G.one};todo=[G.one]
 for x in todo:
  for a,b in zip(gens,images):
   y=G.mul[x][a];v=G.mul[seen[x]][b]
   if y in seen:
    if seen[y]!=v:return None
   else:seen[y]=v;todo.append(y)
 assert len(seen)==G.n
 if len(set(seen.values()))!=G.n:return None
 return tuple(seen[x] for x in range(G.n))

def decode(G,v,k,l):
 z=tuple(v[:k]);u=tuple(v[k:k+l]);vv=tuple(G.inv[x] for x in reversed(v[k+l:]))
 x=tuple(G.inv[a] for a in reversed(u))
 return z,u,vv,x

def reflect(G,v,k,l):
 z,u,vv,x=decode(G,v,k,l)
 p=G.one;images=[]
 for a in z:
  images.append(G.conj(p,G.inv[a]));p=G.mul[p][a]
 images+=list(vv)+[G.inv[a] for a in reversed(u)]
 a=hom(G,v,images)
 if a is not None:
  assert all(a[a[j]]==j for j in range(G.n))
  assert G.prod(v)==G.one
 return a

def encode(G,z,x,a):
 u=tuple(G.inv[q] for q in reversed(x))
 vv=tuple(a[q] for q in u)
 ans=tuple(z)+u+tuple(G.inv[q] for q in reversed(vv))
 assert G.prod(ans)==G.one
 return ans

def rotate(G,z,x,a):
 if not z:return z,x,a
 e=G.inv[G.prod(x)];first=z[0]
 zz=z[1:]+(G.conj(e,first),)
 aa=tuple(G.conj(G.inv[first],a[j]) for j in range(G.n))
 return zz,x,aa

def reverse(G,z,x,a):
 p=G.prod(z)
 return tuple(G.inv[q] for q in reversed(z)),tuple(G.inv[q] for q in reversed(x)),tuple(G.conj(G.inv[p],a[j]) for j in range(G.n))

def hyperelliptic(G,v,ms):
 for z in range(G.n):
  if G.orders[z]!=2 or any(G.mul[z][h]!=G.mul[h][z] for h in range(G.n)):continue
  count=sum(G.n//m for x,m in zip(v,ms) if z in G.powers[x])
  if count==8:return z
 return None

def neighbours(G,v,c,n):
 k,l=len(c),len(n);a=reflect(G,v,k,l);assert a is not None
 z,u,vv,x=decode(G,v,k,l)
 for word in braid_generators(n):
  xx=x;dd=n
  for i,s in word:xx,dd=braid(G,xx,dd,i,s)
  assert dd==n
  yield encode(G,z,xx,a)
 if k:
  zz,xx,aa=z,x,a
  for s in range(1,k+1):
   zz,xx,aa=rotate(G,zz,xx,aa)
   if c[s%k:]+c[:s%k]==c:yield encode(G,zz,xx,aa)
 else:
  # Relative-boundary braid generators already generate the unoriented disc.
  pass
 zz,xx,aa=reverse(G,z,x,a)
 # Restore the chosen sorted order of the interior cone points by a fixed braid.
 xx=ordered(G,xx,tuple(reversed(n)),n)
 if k:
  cc=tuple(reversed(c))
  for s in range(k):
   if cc==c:yield encode(G,zz,xx,aa)
   zz,xx,aa=rotate(G,zz,xx,aa);cc=cc[1:]+cc[:1]
 else:yield encode(G,zz,xx,aa)

def main():
 actions=json.loads((ROOT/'research_data/actions-genus3.json').read_text())['actions']
 rows=[];certs=[]
 for action_id,action in enumerate(actions,1):
  if action['gamma']!=0:continue
  G=Group([tuple(x-1 for x in p) for p in action['autgreps'][0]])
  reps=[G.ids_of(v) for v in action['autgreps']]
  ms=tuple(action['bd']);assert all(G.prod(v)==G.one for v in reps)
  for c,n in types(ms):
   k,l=len(c),len(n);target=c+tuple(reversed(n))+n
   converted=[ordered(G,v,ms,target) for v in reps]
   keys={G.tuple_key(v):i for i,v in enumerate(converted)}
   assert len(keys)==len(reps)
   valid={i for i,v in enumerate(converted) if reflect(G,v,k,l) is not None}
   remaining=set(valid);orbits=[]
   while remaining:
    first=min(remaining);orbit={first};todo=[first]
    for i in todo:
     for w in neighbours(G,converted[i],c,n):
      assert tuple(G.orders[q] for q in w)==target
      j=keys[G.tuple_key(w)]
      assert j in valid,(action_id,c,n,i,j)
      if j not in orbit:orbit.add(j);todo.append(j)
    assert orbit<=remaining
    remaining-=orbit;orbits.append(sorted(orbit))
   for orbit in orbits:
    v=converted[orbit[0]];a=reflect(G,v,k,l);z,u,vv,x=decode(G,v,k,l)
    hz=hyperelliptic(G,v,target)
    cid=f'G3R_{len(rows)+1:03}'
    row={'class_id':cid,'positive_action':f'O3.{action_id}','order':2*G.n,
      'positive_group_order':G.n,'positive_group_code':action['group']['code'],
      'corner_orders':','.join(map(str,c)),'interior_cones':','.join(map(str,n)),
      'contains_hyperelliptic':hz is not None,'AutH_kernel_orbit':','.join(map(str,orbit)),
      'representative_AutH_vector':orbit[0]}
    rows.append(row)
    certs.append({'class_id':cid,'positive_action':action_id,'corner_orders':c,'cone_orders':n,
      'positive_elements':G.el,'positive_one':G.one,'positive_vector':v,
      'positive_generators_interior':x,'positive_generators_corners':z,
      'reflection_automorphism':a,'hyperelliptic_element':hz,'kernel_orbit':orbit,
      'kernel_orbit_keys':[G.tuple_key(converted[j]) for j in orbit]})
   print('O3.'+str(action_id),'disc',c,n,'valid',len(valid),'orbits',len(orbits),flush=True)
 summary={'scope':'positive quotient sphere; induced negative quotient involution has a fixed circle',
  'classes':len(rows),'containing_hyperelliptic':sum(r['contains_hyperelliptic'] for r in rows),
  'without_hyperelliptic':sum(not r['contains_hyperelliptic'] for r in rows),
  'by_order':dict(sorted(Counter(r['order'] for r in rows).items()))}
 assert summary['containing_hyperelliptic']==57,summary
 with (HERE/'type_3_0_reflection_quotient_catalogue.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 (HERE/'type_3_0_reflection_quotient_certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
 (HERE/'catalogue_genus3_reflection_quotients_output.json').write_text(json.dumps(summary,indent=2)+'\n')
 print('FINAL',json.dumps(summary),flush=True)
if __name__=='__main__':main()
