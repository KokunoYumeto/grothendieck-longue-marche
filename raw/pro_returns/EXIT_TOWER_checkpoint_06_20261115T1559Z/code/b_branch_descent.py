#!/usr/bin/env python3
"""Exact finite permutations and rational maps for the E.44 V4 descent.
This checks algebraic identities and finite label choices; the group/topology
proof is in E.44, not inferred from these computations.
"""
import itertools,json
from pathlib import Path
import sympy as s
P=Path(__file__).resolve().parent

def compose(p,q): return tuple(p[q[i]] for i in range(len(p)))
def perm(n,cycles):
 p=list(range(n))
 for c in cycles:
  for i,j in zip(c,c[1:]+c[:1]):p[i]=j
 return tuple(p)
e=tuple(range(10))
a=perm(10,[[2,3],[4,5],[6,7],[8,9]])
b=perm(10,[[0,1],[4,5],[6,8],[7,9]])
c=compose(a,b);H=[e,a,b,c]
assert all(compose(h,k)==compose(k,h) for h in H for k in H)
fixed=[[i for i in range(10) if h[i]==i] for h in H[1:]]
assert fixed==[[0,1],[2,3],[4,5]]
central=[]
for flips in itertools.product([0,1],repeat=3):
 for h in H:
  p=list(e)
  for j,f in enumerate(flips):
   if f:p[2*j],p[2*j+1]=p[2*j+1],p[2*j]
  for i in range(6,10):p[i]=h[i]
  p=tuple(p)
  assert all(compose(p,k)==compose(k,p) for k in H)
  central.append(p)
assert len(set(central))==32
O_b={6,8};O_a={6,7}
N_b_perm=[p for p in central if {p[i] for i in O_b}==O_b]
N_a_perm=[p for p in central if {p[i] for i in O_a}==O_a]
assert set(H)&set(N_b_perm)=={e,b}
assert set(H)&set(N_a_perm)=={e,a}
Pflip=perm(10,[[4,5]])
assert all(Pflip[i]==i for i in [0,1,2,3,6,7,8,9])
V4={tuple(range(4)),perm(4,[[0,1],[2,3]]),perm(4,[[0,2],[1,3]]),perm(4,[[0,3],[1,2]])}
C4={tuple(range(4)),perm(4,[[0,1]]),perm(4,[[2,3]]),perm(4,[[0,1],[2,3]])}
D8={p for p in itertools.permutations(range(4)) if {frozenset(p[i] for i in [0,1]),frozenset(p[i] for i in [2,3])}=={frozenset([0,1]),frozenset([2,3])}}
assert len(D8)==8 and len(C4&V4)==2
assert {compose(p,q) for p in C4 for q in V4}==D8
z=s.symbols('z');t=s.symbols('t');u=(z*z+1)**2/(4*z*z)
lam=((z*z-1)/(z*z+1))**2
ell_b=z*z;ell_a=((z-1)/(z+1))**2
inv=lambda x:(x+1)**2/(4*x)
S=lambda x:x/(x-1)
checks={
 'generic_crossratio':s.factor(lam-(1-1/u)),
 'q_b_coordinate':s.factor(inv(ell_b)-u),
 'q_a_coordinate':s.factor(inv(ell_a)-S(u)),
 'cusp_swap_order_two':s.factor(S(S(u))-u),
 'pole_swap_trivial':s.factor(((t+1)**2/(4*t)).subs(t,1/t)-(t+1)**2/(4*t)),
 'normalizer_T':s.factor(u.subs(z,(z-1)/(z+1))-S(u)),
}
assert all(v==0 for v in checks.values())
# Fixed-pair discriminants of the canonical V4 on {0,1,infinity,lambda}.
l=s.symbols('lambda');x=s.symbols('x')
polys=[x*x-l,x*x-2*x+l,x*x-2*l*x+l]
discs=[s.factor(s.discriminant(p,x)) for p in polys]
assert all(s.expand(q-r)==0 for q,r in zip(discs,[4*l,4-4*l,4*l*(l-1)]))
monodromy=[[1,0,1],[0,1,1]]
even={tuple((i*monodromy[0][k]+j*monodromy[1][k])%2 for k in range(3)) for i,j in itertools.product([0,1],repeat=2)}
assert len(even)==4 and all(sum(v)%2==0 for v in even)
result={
 'status':'executed; all exact checks passed',
 'H_permutations':[list(h) for h in H], 'fixed_pairs':fixed,
 'permutation_centralizer_order':len(central),
 'choice_stabilizer_orders_in_permutation_centralizer':[len(N_a_perm),len(N_b_perm)],
 'choice_intersections_with_H':{'a':[list(e),list(a)],'b':[list(e),list(b)]},
 'target_orders':{'colored':len(C4),'D8':len(D8),'normal_V4':len(V4),'intersection':len(C4&V4)},
 'forgotten_chirality_swap':list(Pflip),
 'coordinate_identities':{k:str(v) for k,v in checks.items()},
 'fixed_pair_discriminants':[str(q) for q in discs],
 'pure_fourpoint_fixed_pair_monodromy':monodromy,
 'pure_chirality_classes':2,
 'normalizer_permutation_image_order':len(even)*4,
 'orbifold_q_b':{'source':'F(v,d)','target':'<v,d | (v*d)^2=1>','images':{'v':'v','d':'d'},'kernel':'closed normal closure of (v*d)^2','surjective':True},
 'scope':'Finite labels and rational identities only. Geometrization, centralizer topology and naturality are proved separately in E.44.'
}
(P/'b_branch_descent.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
