"""All field powers in AC40 are necessary: exact 256-vector model.
This is a finite module example, not a claimed curve realization.
"""
from itertools import product
import json
G=list(product(range(3),repeat=2));zero=(0,0,0,0)
weights=[(1,1),(1,2),(1,0),(0,1)]
def mul(a,b):
 z=0
 for i in range(2):
  if b>>i&1:z^=a<<i
 return z^7 if z&4 else z
omega=[1,2,3]
def act(g,v):
 return tuple(mul(omega[(a*g[0]+b*g[1])%3],x)
 for (a,b),x in zip(weights,v))
def F(v):return(v[0],mul(v[1],v[1]),mul(2,v[3]),v[2])
def Fr(v,r):
 for _ in range(r):v=F(v)
 return v
def phi(g):return g[::-1]
def norm(H,v):
 z=[0]*4
 for g in H:
  for i,x in enumerate(act(g,v)):z[i]^=x
 return tuple(z)
lines={frozenset(((a*i)%3,(b*i)%3) for i in range(3))
 for a,b in G if(a,b)!=(0,0)}
subgroups=[frozenset({(0,0)})]+sorted(lines,key=lambda H:sorted(H))+[frozenset(G)]
V=list(product(range(4),repeat=4))
assert all(F(act(g,v))==act(phi(g),F(v)) for g in G for v in V)
assert all(Fr(v,6)==v for v in V)
fixed=[v for v in V if F(v)==v]
regular=[v for v in fixed if sum(act(g,v)==v for g in G)==1]
all_norm_regular=[v for v in fixed if all(
 {g for g in G if act(g,norm(H,v))==norm(H,v)}==set(H) for H in subgroups)]
rows=[]
for r in range(1,7):
 stable=[H for H in subgroups if frozenset(phi(g) if r%2 else g for g in H)==H]
 dims={H:sum(Fr(v,r)==v and all(act(g,v)==v for g in H) for v in V).bit_length()-1
 for H in stable}
 failures=[]
 for H in stable:
  for K in stable:
   if H<K and len(K)//len(H)==3 and dims[H]==dims[K]:
    failures.append(dict(H=sorted(H),K=sorted(K),fixed_dimension=dims[H]))
 rows.append(dict(power=r,invariant_dimensions=[
  dict(subgroup=sorted(H),dimension=dims[H]) for H in stable],failed_strict_tests=failures))
assert len(fixed)==8 and len(regular)==3 and not all_norm_regular
assert not rows[0]['failed_strict_tests']
assert len(rows[1]['failed_strict_tests'])==2
assert not rows[2]['failed_strict_tests']
assert len(rows[3]['failed_strict_tests'])==2
assert not rows[4]['failed_strict_tests'] and not rows[5]['failed_strict_tests']
out=dict(group='C3 squared',coefficient_field='F2',vector_count=len(V),
 field_encoding='F4=F2[omega]/(omega^2+omega+1), omega=2',
 character_weights=weights,F='(zplus,zminus,x,y) maps to(zplus,zminus^2,omega*y,x)',
 deck_automorphism='swap the two C3 coordinates',
 Frobenius_order=6,F_fixed_vector_count=len(fixed),
 F_fixed_free_G_vector_count=len(regular),
 F_fixed_all_normal_projection_regular_count=len(all_norm_regular),
 base_field_all_stable_relative_tests_fail=True,
 all_power_results=rows,
 limitation='Abstract finite module; no geometric realization claimed.')
print(json.dumps(out,indent=2))
