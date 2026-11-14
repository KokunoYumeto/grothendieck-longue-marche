from catalogue_spheres import orbifolds
from itertools import product,permutations
from collections import Counter

def expanded(o,p):
 cs,ks,es,a=p
 if not o.corner_orders:
  return [(1,1,'mirror_branch')]*sum(es)
 ans=[]
 # r0 edge0 has corner0 at its start and lastcorner at its end;
 # standard r0,r1,... sequence traverses corner0,edge1,corner1,...,edge0.
 for j,n in enumerate(o.corner_orders):
  ans.append((n,ks[j],'old_corner'))
  ans += [(1,1,'mirror_branch')]*es[(j+1)%len(es)]
 return ans

def character_orbits(o,p):
 cs,ks,es,a=p
 if o.kind=='sphere':
  colors=list(zip(o.cone_orders,cs)); chars=[]
  for bits in product(range(2),repeat=len(cs)):
   if any((m*b-d)%2 for m,b,d in zip(o.cone_orders,bits,cs)):continue
   if (sum(bits)-a)%2:continue
   chars.append(bits)
  perms=[q for q in permutations(range(len(cs))) if all(colors[i]==colors[q[i]] for i in range(len(cs)))]
  orbits={min(tuple(b[q[i]] for i in range(len(cs))) for q in perms) for b in chars}
  return sorted(orbits), {'chars':chars,'perms':perms,'colors':colors}
 if o.kind=='RP2':
  chars=[]
  for bits in product(range(2),repeat=len(cs)+1):
   x=bits[1:]
   if any((m*b-d)%2 for m,b,d in zip(o.cone_orders,x,cs)):continue
   if (sum(x)-a)%2:continue
   chars.append(bits)
  assert not chars,(o.name,p,chars)
  return [],{'chars':[]}
 colors=expanded(o,p); l=len(colors);nr=max(1,l);chars=[]
 for bits in product(range(2),repeat=len(cs)+nr):
  x=bits[:len(cs)];rs=bits[len(cs):]
  if any((m*b-d)%2 for m,b,d in zip(o.cone_orders,x,cs)):continue
  if any((m*(rs[j]+rs[(j+1)%nr])-d)%2 for j,(m,d,_) in enumerate(colors)):continue
  chars.append(bits)
 perms=[]
 if l:
  for sign in (1,-1):
   for s in range(l):
    cornerperm=[(s+j)%l if sign==1 else (s-j-1)%l for j in range(l)]
    if all(colors[j]==colors[cornerperm[j]] for j in range(l)):
     perms.append(tuple((s+sign*j)%l for j in range(l)))
 else:perms=[(0,)]
 orbits={min(b[:len(cs)]+tuple(b[len(cs)+q[j]] for j in range(nr)) for q in perms) for b in chars}
 return sorted(orbits),{'chars':chars,'perms':perms,'colors':colors}

if __name__=='__main__':
 cases=[(o,p) for o in orbifolds() for p in o.patterns(6)]
 cases.sort(key=lambda z:(z[0].order,z[0].name,z[1]))
 count=Counter();rows=[]
 for j,(o,p) in enumerate(cases,1):
  chars,data=character_orbits(o,p)
  positive=o.kind=='sphere'
  count['full']+=1;count['complements']+=len(chars)
  if positive:count['positive_full']+=1;count['positive_complements']+=len(chars)
  rows.append((j,o.name,p,len(chars),chars))
 print(count)
 for row in rows:print(row)
