"""Exact actual finite-group and marked-cover data, not a fixed-group theorem."""
from itertools import product
from pathlib import Path
import json
G=list(product(range(16),range(4)))
one=(0,0)
def rot(v,k):
 k%=4
 return ((v<<k)|(v>>(4-k)))&15 if k else v
def mul(g,h):return (g[0]^rot(h[0],g[1]),(g[1]+h[1])%4)
def inv(g):return (rot(g[0],-g[1]),(-g[1])%4)
def comm(g,h):return mul(mul(mul(g,h),inv(g)),inv(h))
def closure(S):
 C={one};todo=[one]
 while todo:
  g=todo.pop()
  for h in S:
   z=mul(g,h)
   if z not in C:C.add(z);todo.append(z)
 return C
def order(g):
 z=one
 for n in range(1,65):
  z=mul(z,g)
  if z==one:return n
 raise AssertionError

def perm(g):
 v,k=g
 return tuple(2*((i+k)%4)+(eps^((v>>((i+k)%4))&1)) for i in range(4) for eps in range(2))
def compose(f,g):return tuple(f[g[i]] for i in range(8))
def cycles(s):
 U=set(range(8));ans=[]
 while U:
  i=min(U);c=[]
  while i in U:c.append(i);U.remove(i);i=s[i]
  ans.append(c)
 return ans

a=(1,0);b=(0,1);c=comm(a,b)
assert closure([a,b])==set(G)
assert all(compose(perm(g),perm(h))==perm(mul(g,h)) for g in G for h in G)
assert len({perm(g) for g in G})==64
D=closure([comm(g,h) for g in G for h in G]);assert D=={(v,0) for v in range(16) if v.bit_count()%2==0}
assert len(D)==8 and {order(g) for g in D}=={1,2}
Z=[g for g in G if all(mul(g,h)==mul(h,g) for h in G)];assert Z==[(0,0),(15,0)]
I=closure([c]);assert c==(3,0) and len(I)==2
conjugates={frozenset(mul(mul(g,h),inv(g)) for h in I) for g in G};assert len(conjugates)==4
normal_closure=closure([h for J in conjugates for h in J]);assert normal_closure==D
N=[g for g in G if frozenset(mul(mul(g,h),inv(g)) for h in I)==frozenset(I)];assert len(N)==16
Phi=closure(list(D)+[mul(g,g) for g in G]);assert len(Phi)==16 and I<=Phi
A={(v,0) for v in range(16)};H={g for g in G if perm(g)[0]==0};assert len(H)==8 and H<A
assert H=={(v,0) for v in range(16) if not(v&1)}
marked_cycles=cycles(perm(c));assert sorted(map(len,marked_cycles))==[1,1,1,1,2,2]
branch=[]
for i in range(4):
 ci=mul(mul((0,i),c),(0,-i%4))
 branch.append({'kernel_index':i,'inertia_mask':ci[0],'double_cover_ramified':bool(ci[0]&1),'cusps_above':1 if ci[0]&1 else 2})
assert [r['kernel_index'] for r in branch if r['double_cover_ramified']]==[0,3]
assert sum(r['cusps_above'] for r in branch)==6
full_genus=1+(64-64//len(I))//2
intermediate_genus=1+(8-len(marked_cycles))//2
assert full_genus==17 and intermediate_genus==2
result={'status':'PASS','scope':'Exact group and marked-cover certificate only; no fixed-subgroup conclusion.','group':'(C2)^4 semidirect C4, regular cyclic shift','order':64,'generators':[a,b],'commutator':c,'derived_order':8,'derived_exponent':2,'derived_is_cyclic':False,'center':Z,'maximum_element_order':max(map(order,G)),'inertia_order':2,'inertia_normal':False,'inertia_conjugates':len(conjugates),'normalizer_order':len(N),'frattini_order':len(Phi),'full_genus':full_genus,'full_cusps':32,'natural_degree':8,'natural_genus':intermediate_genus,'natural_cusps':len(marked_cycles),'natural_inertia_cycles':marked_cycles,'elliptic_intermediate_degree':4,'double_cover_degree':2,'branch_data':branch,'permutation_composition_pairs_checked':4096}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
