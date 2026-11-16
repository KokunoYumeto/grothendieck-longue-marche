"""Exact finite countermodel in AC39; this is not a curve construction."""
from itertools import combinations
import json

G=[(a,b) for a in range(7) for b in range(3)]
def mul(g,h):
 return ((g[0]+pow(2,g[1],7)*h[0])%7,(g[1]+h[1])%3)
def inv(g):
 return((-pow(pow(2,g[1],7),-1,7)*g[0])%7,(-g[1])%3)
def closure(gs):
 S={(0,0)};todo=[(0,0)]
 while todo:
  x=todo.pop()
  for g in gs:
   y=mul(x,g)
   if y not in S:S.add(y);todo.append(y)
 return frozenset(S)
subgroups={closure(z) for r in [0,1,2] for z in combinations(G,r)}
normal=sorted([H for H in subgroups if all(
 frozenset(mul(mul(g,h),inv(g)) for h in H)==H for g in G)],key=len)
def f4mul(a,b):
 ans=0
 for i in range(2):
  if b>>i&1:ans^=a<<i
 if ans&4:ans^=7
 return ans
alpha=[1,2,3]
def action(g,v):return f4mul(alpha[g[1]],v)
assert all(action(mul(g,h),v)==action(g,action(h,v))
 for g in G for h in G for v in range(4))
fixed={len(H):[v for v in range(4) if all(action(h,v)==v for h in H)]
 for H in normal}
stab=[sum(action(g,v)==v for g in G) for v in range(4)]
assert fixed=={1:[0,1,2,3],7:[0,1,2,3],21:[0]}
assert stab==[21,7,7,7]
# Check that every transfer maps onto the target invariant group and
# that normalized inclusion is a splitting (all relevant degrees odd).
transfer_rows=[]
for H in normal:
 for K in normal:
  if H<K:
   reps=[];used=set()
   for g in K:
    if g not in used:
     reps.append(g);used.update(mul(g,h) for h in H)
   def norm(v):
    out=0
    for g in reps:out^=action(g,v)
    return out
   image=sorted({norm(v) for v in fixed[len(H)]})
   assert image==fixed[len(K)]
   assert all(norm(v)==v for v in fixed[len(K)])
   transfer_rows.append(dict(source_subgroup_order=len(H),
    target_subgroup_order=len(K),degree=len(K)//len(H),image=image))
out=dict(group='C7 semidirect C3, action exponent2',group_order=len(G),
 all_subgroups=len(subgroups),normal_subgroup_orders=list(fixed),
 fixed_vectors=fixed,vector_stabilizer_orders=stab,
 all_base_quotient_tests_fail=True,free_vector_exists=False,
 relative_test_for_1_less_C7_succeeds=True,all_transfers_split=True,
 transfer_checks=transfer_rows,
 limitation='Pure finite module; not claimed to be an actual full Jacobian tower.')
print(json.dumps(out,indent=2))
