#!/usr/bin/env python3
"""Independent Schreier/F_2 certificate for the characteristic S4 envelope.
No enumeration of its 442368 elements, and no simple-group theorem for S4.
"""
from itertools import product,permutations
from math import gcd
from pathlib import Path
import json
from finite_groups import permutation_group,orbit_pair_classes

G=permutation_group(4); K=permutation_group(3)
reps,which=orbit_pair_classes(G); rr3,ww3=orbit_pair_classes(K)
assert len(reps)==9 and len(rr3)==3
xbase,ybase=reps[0]
automorphisms=[h for a,b in which for h in [G.map_from_generators(xbase,ybase,a,b)] if h is not None]
assert len(automorphisms)==24
assert set(automorphisms)=={tuple(c) for c in G.conj}
parts=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
qp=[]
for p in G.elements:
    image=[]
    for part in parts:
        pp=tuple(sorted(tuple(sorted(p[i] for i in edge)) for edge in part))
        image.append(parts.index(pp))
    qp.append(K.index[tuple(image)])
assert all(qp[G.mul(a,b)]==K.mul(qp[a],qp[b]) for a,b in product(range(24),repeat=2))
vv=[G.index[p] for p in [(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)]]
ve={v:i for i,v in enumerate(vv)}
assert all(ve[G.mul(vv[a],vv[b])]==a^b for a,b in product(range(4),repeat=2))
x=tuple(a for a,b in reps);y=tuple(b for a,b in reps);ei=(G.e,)*9
mul=lambda a,b:tuple(G.mul(s,t) for s,t in zip(a,b))
inv=lambda a:tuple(G.inv[s] for s in a)
pr=lambda a:tuple(qp[s] for s in a)
kmul=lambda a,b:tuple(K.mul(s,t) for s,t in zip(a,b))
kinv=lambda a:tuple(K.inv[s] for s in a)
encode=lambda a:sum(ve[s]<<(2*i) for i,s in enumerate(a))
decode=lambda n:tuple(vv[(n>>(2*i))&3] for i in range(9))
conj=lambda h,a:mul(mul(inv(h),a),h)

qx,qy=pr(x),pr(y);qe=(K.e,)*9
sections={qe:ei};todo=[qe]
for q in todo:
 for qg,g in [(qx,x),(qy,y)]:
  r=kmul(q,qg)
  if r not in sections:sections[r]=mul(sections[q],g);todo.append(r)
assert len(todo)==108

def basis(vs):
 b={}
 for v in vs:
  while v:
   k=v.bit_length()-1
   if k in b:v^=b[k]
   else:b[k]=v;break
 return [b[k] for k in sorted(b,reverse=True)]
def red(v,bs):
 for b in bs:
  if v&(1<<(b.bit_length()-1)):v^=b
 return v
sch=[]
for q in todo:
 for qg,g in [(qx,x),(qy,y)]:
  r=kmul(q,qg)
  h=mul(mul(sections[q],g),inv(sections[r]))
  assert pr(h)==qe
  sch.append(encode(h))
bb=basis(sch);assert len(bb)==12
assert all(red(encode(conj(g,decode(v))),bb)==0 for g in (x,y) for v in bb)
# Simultaneous fixed vectors modulo V0. The kernel has dim12, so invariants dim0.
cols=[]
for i in range(18):
 w=decode(1<<i); cx=red(encode(conj(x,w))^(1<<i),bb);cy=red(encode(conj(y,w))^(1<<i),bb)
 cols.append(cx|(cy<<18))
rank_fixed=len(basis(cols));assert 18-rank_fixed-len(bb)==0
# Odd subgroup A = C3^3 acts with no fixed vectors on W.
A=[q for q in todo if all(K.orders[a]%2 for a in q)]
assert len(A)==27
acol=[]
for i in range(18):
 bits=0
 for j,q in enumerate(A):bits|=(encode(conj(sections[q],decode(1<<i)))^(1<<i))<<(18*j)
 acol.append(bits)
assert len(basis(acol))==18
# S(S4) by independent exhaustive permutations within color classes.
theta=tuple(which[(b,a)] for a,b in reps)
delta=tuple(which[(G.inv[G.mul(a,b)],b)] for a,b in reps)
colors=[(G.classes[a],G.classes[b]) for a,b in reps]
blocks={}
for i,c in enumerate(colors):blocks.setdefault(c,[]).append(i)
accepted=[];candidate_count=0
for choices in product(*(list(permutations(v)) for v in blocks.values())):
 p=list(range(9))
 for domain,targets in zip(blocks.values(),choices):
  for i,j in zip(domain,targets):p[i]=j
 candidate_count+=1
 if all(p[g[i]]==g[p[i]] for g in (theta,delta) for i in range(9)):accepted.append(p)
assert accepted==[list(range(9))]
# Construct explicit nontrivial coordinatewise normalizer representative.
# Align each projected pair with one of the three standard S3 pairs.
align=[];types=[]
for a,b in reps:
 t=ww3[(qp[a],qp[b])];types.append(t)
 aa,bb3=rr3[t]
 c=next(h for h in range(K.n) if K.conj[h][aa]==qp[a] and K.conj[h][bb3]==qp[b])
 align.append(c)
assert sorted(types.count(t) for t in range(3))==[3,3,3]
r=next(h for h in range(K.n) if K.orders[h]==2)
nproj=tuple(K.conj[c][r if t==0 else K.e] for c,t in zip(align,types))
assert nproj not in sections
n0=tuple(qp.index(a) for a in nproj)
comp=[];bs=bb[:]
for i in range(18):
 if red(1<<i,bs):comp.append(1<<i);bs=basis(bs+[1<<i])
assert len(comp)==6
members=lambda h:pr(h) in sections and red(encode(mul(h,inv(sections[pr(h)]))),bb)==0
normals=[]
for coeff in product((0,1),repeat=6):
 v=0
 for c,b in zip(coeff,comp):
  if c:v^=b
 n=mul(n0,decode(v))
 if all(members(conj(n,g)) for g in (x,y)):normals.append(n)
assert len(normals)==1
n=normals[0]
# Exact conjugacy test inside H using quotient and the F2 kernel.
def solve_span(vectors,target):
 b={}
 for j,v in enumerate(vectors):
  c=1<<j
  while v:
   k=v.bit_length()-1
   if k in b:v^=b[k][0];c^=b[k][1]
   else:b[k]=(v,c);break
 c=0;v=target
 while v:
  k=v.bit_length()-1
  if k not in b:return None
  w,d=b[k];v^=w;c^=d
 return c

def conjugate_in_H(a,target):
 qa,qt=pr(a),pr(target)
 for q in todo:
  if kmul(kmul(kinv(q),qa),q)!=qt:continue
  a0=conj(sections[q],a)
  v=mul(target,inv(a0))
  assert pr(v)==qe
  image=[encode(mul(decode(b),conj(inv(a0),decode(b)))) for b in bb]
  solution=solve_span(image,encode(v))
  if solution is not None:
   w=0
   for i,b in enumerate(bb):
    if solution&(1<<i):w^=b
   h=mul(sections[q],decode(w))
   assert members(h) and conj(h,a)==target
   return h
 return None
units=[k for k in range(12) if gcd(k,12)==1]
allowed=[]
for k in units:
 if all(conjugate_in_H(tuple(G.power(a,k) for a in g),conj(n,g)) for g in (x,y)):allowed.append(k)
# The finite normalizer quotient C2 is normal in Out(H), so theta/delta centralize it.
assert allowed
out={'group':'S4','automorphism_group_order':len(automorphisms),'generating_pairs':len(which),'inner_pair_classes':len(reps),
 'pair_representatives':[[G.elements[a],G.elements[b]] for a,b in reps],
 'theta':theta,'delta':delta,'color_blocks':list(blocks.values()),'color_preserving_candidate_count':candidate_count,'S_of_S4_order':len(accepted),
 'projected_envelope_order':len(todo),'projected_pair_type_multiplicities':[types.count(t) for t in range(3)],
 'kernel_dimension':len(bb),'kernel_F2_basis':bb,'envelope_order':len(todo)*(1<<len(bb)),
 'W_dimension':18,'quotient_dimension':6,'quotient_fixed_constraint_rank':rank_fixed,
 'quotient_invariants_dimension':0,'quotient_invariants_order':1,'fixed_constraint_columns':cols,
 'odd_subgroup_order':len(A),'W_odd_subgroup_invariants_dimension':0,
 'normalizer_quotient_upper_bound':2,'normalizer_quotient_order':2,
 'nontrivial_normalizer_coordinates':[G.elements[a] for a in n],
 'nontrivial_class_allowed_power_exponents_mod12':allowed,
 'H_conjugators_for_multiplier_one':[[G.elements[a] for a in conjugate_in_H(g,conj(n,g))] for g in (x,y)],
 'GT_S4_order':2,'GT1_S4_order':2 if 1 in allowed else 1,
 'Galois_outer_image_order':2,'arithmetic_justification':'S3 quotient and explicit Q(sqrt3) constant field; see B.s4.1'}
path=Path(__file__).resolve().parent
(path/'arithmetic_s4.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
