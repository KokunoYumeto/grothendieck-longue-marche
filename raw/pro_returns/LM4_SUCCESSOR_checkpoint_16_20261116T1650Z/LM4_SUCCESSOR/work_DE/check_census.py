"""Exact finite verification for LM4_SUCCESSOR E.30--E.36.
No floating-point group or orbit calculation is used.
Run with Python 3; standard library only.
"""
from itertools import permutations
from collections import Counter
from pathlib import Path
import json,csv

n=5
I=tuple(range(n))
S=list(permutations(I))
def mul(p,q): return tuple(p[q[i]] for i in I)
def cyc(*cs):
 p=list(I)
 for c in cs:
  for a,b in zip(c,c[1:]+c[:1]): p[a-1]=b-1
 return tuple(p)
def gen(gs):
 H={I}; todo=[I]
 while todo:
  a=todo.pop()
  for g in gs:
   b=mul(a,g)
   if b not in H: H.add(b);todo.append(b)
 return frozenset(H)
def smul(a,b): return mul(a[0],b[0]),a[1]*b[1]
def sgen(gs):
 H={(I,1)};todo=[(I,1)]
 while todo:
  a=todo.pop()
  for g in gs:
   b=smul(a,g)
   if b not in H:H.add(b);todo.append(b)
 return frozenset(H)
def order(a):
 b=(I,1)
 for k in range(1,241):
  b=smul(b,a)
  if b==(I,1):return k
 raise AssertionError

def cosets(H):
 return frozenset(frozenset(mul(g,h) for h in H) for g in S)
def num_orbits(X,act):
 rem=set(X); counts=[]
 while rem:
  x=next(iter(rem)); orb={act(g,x) for g in S}; rem-=orb;counts.append(len(orb))
 return sorted(counts)

C2=gen([cyc((1,2),(3,4))])
C4=gen([cyc((1,3,2,4))])
D3=gen([cyc((1,2,3)),cyc((1,2),(4,5))])
D5=gen([cyc((1,2,3,4,5)),cyc((2,5),(3,4))])
assert [len(H) for H in (C2,C4,D3,D5)]==[2,4,6,10]
vertex_specs=[('I10',D5),('I6',D3),('I4',C4),('II2',C2),('II2prime',C2),('II1',gen([])),('III2',C2),('III1',gen([])),('III2prime',C2)]
vertices={k:cosets(H) for k,H in vertex_specs}
vc={k:len(v) for k,v in vertices.items()}
vo={k:num_orbits(v,lambda g,c:frozenset(mul(g,h) for h in c)) for k,v in vertices.items()}
assert all(len(o)==1 for o in vo.values())
assert sum(vc.values())==542

# Arrow-family sizes and degrees as read from the diagram.  The size-360
# family has a free S5 source, hence consists of three free S5 orbits.
arrow_specs=[
 ('f_B_s','I6','I4',60,1),
 ('f_Q_a','II2prime','I4',120,1),
 ('tau_pi_s','II2','II2prime',60,1),
 ('tau_r_0','II1','II1',120,1),
 ('gamma_pi_s','II2','I10',60,1),
 ('gamma_pi_s_1','II2prime','I6',60,1),
 ('gamma_r_0','II1','I6',120,1),
 ('tau_pi_rho','III2','III1',120,1),
 ('gamma_pi_rho','III2','II2',120,1),
 ('tau_r_1','III1','III2prime',120,1),
 ('gamma_r_1','III1','II2prime',120,1),
 ('gamma_r_1prime','III1','II1',360,3),
 ('gamma_r_2','III1','II2',120,1),
 ('gamma_r_21','III2prime','I4',60,1)]
arrow_rows=[]
for name,src,tgt,size,no in arrow_specs:
 assert size%vc[src]==0 and size%vc[tgt]==0
 H=C2 if size//no==60 else gen([])
 A={(i,c) for i in range(no) for c in cosets(H)}
 orb=num_orbits(A,lambda g,a:(a[0],frozenset(mul(g,h) for h in a[1])))
 assert len(A)==size and len(orb)==no
 arrow_rows.append(dict(name=name,source=src,target=tgt,size=size,source_degree=size//vc[src],target_degree=size//vc[tgt],orbits=no,orbit_sizes=orb))
assert sum(a['size'] for a in arrow_rows)==1620
assert sum(a['orbits'] for a in arrow_rows)==16

r2=cyc((1,2),(3,4));r3=cyc((1,2,3));r4=cyc((1,2,3,4));r5=cyc((1,2,3,4,5))
s3=cyc((1,2),(4,5));s5=cyc((2,5),(3,4))
positive=[('1',[]),('C2',[(r2,1)]),('C3',[(r3,1)]),('C4',[(r4,1)]),('C5',[(r5,1)]),('D3',[(r3,1),(s3,1)]),('D5',[(r5,1),(s5,1)])]
negative=[
 ('reflection_5',[(I,-1)]),
 ('reflection_3',[(cyc((1,2)),-1)]),
 ('reflection_1',[(r2,-1)]),
 ('V4_real_5_1',[(r2,1),(I,-1)]),
 ('V4_real_3_3',[(r2,1),(cyc((1,2)),-1)]),
 ('V4_real_1_1',[(r2,1),(cyc((1,3),(2,4)),-1)]),
 ('C6_mixed',[(cyc((1,2,3),(4,5)),-1)]),
 ('D3_mixed',[(r3,1),(cyc((1,2)),-1)]),
 ('D4_mixed',[(r4,1),(cyc((2,4)),-1)]),
 ('C10_mixed',[(r5,-1)]),
 ('D5_mixed',[(r5,1),(s5,-1)]),
 ('D3_times_C2',[(r3,1),(s3,1),(cyc((4,5)),-1)]),
 ('D5_times_C2',[(r5,1),(s5,1),(I,-1)])]
rows=[]
canonical_subgroups=set()
for name,gs in positive+negative:
 H=sgen(gs)
 def conjugate_by(g,h):
  inv=tuple(g.index(i) for i in I)
  return mul(mul(g,h[0]),inv),h[1]
 canon=min(tuple(sorted(conjugate_by(g,h) for h in H)) for g in S)
 assert canon not in canonical_subgroups, (name, 'duplicate S5-conjugacy class')
 canonical_subgroups.add(canon)
 neg=[g for g in H if g[1]==-1]
 rows.append(dict(name=name,order=len(H),positive_order=len(H)-len(neg),negative_orders=sorted(set(order(g) for g in neg)),negative_involution_fixed_marks=sorted(sum(p[i]==i for i in I) for p,e in neg if order((p,e))==2)))
assert len(rows)==20
assert sum(not r['negative_orders'] for r in rows)==7
assert order((cyc((1,2,3),(4,5)),-1))==6
assert order((r5,-1))==10

# Cyclotomic semilinear transformations sigma(z)=zeta_n/conjugate(z).
# In matrix notation (M,eps), composition is (M*conj^eps(N),eps+delta).
# Every even iterate is z -> zeta_n^(2k) z; every odd iterate is
# z -> zeta_n^(2k+1)/conjugate(z). For odd n>=3, exactly 2n is first identity.
for m in (3,5):
 exps=[(k% m,k%2) for k in range(1,2*m+1)]
 first=next(k for k,(e,anti) in enumerate(exps,1) if e==0 and anti==0)
 assert first==2*m
 print(f'anti-Mobius sigma_{m}: exact order {first}; sigma^2= zeta_{m}^2*z; no fixedpoint because |z|^2=zeta_{m} is impossible')

out=Path(__file__).parent
(out/'census_computation.json').write_text(json.dumps(dict(vertices=vc,vertex_orbits=vo,arrows=arrow_rows,finite_actions=rows),indent=2))
with (out/'census_finite_actions.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
with (out/'census_arrow_families.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(arrow_rows[0]));w.writeheader();w.writerows(arrow_rows)
print('vertex sizes',vc,'total',sum(vc.values()),'orbits',len(vo))
print('arrow-family sizes',[a['size'] for a in arrow_rows],'total',sum(a['size'] for a in arrow_rows),'named families',len(arrow_rows),'S5 orbits',sum(a['orbits'] for a in arrow_rows))
print('finite-action models:',len(rows),'positive 7, mixed 13; all pairwise nonconjugate under S5')
for r in rows: print(r)
print('PASS: exact finite computations completed')
