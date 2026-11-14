#!/usr/bin/env python3
"""Actual arithmetic moving exterior module via all40 character-pair blocks.

The module is the actual rank649 graph homology over the order3888 base.
All projections, deck actions, coinvariants and compact norms are retained.
"""
from pathlib import Path
from itertools import product
import json,time
OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_affine_base.json').read_text())
H=json.loads((OUT/'d_arithmetic_affine_homology.json').read_text())
G=json.loads((OUT/'d_arithmetic_rank9_geometry.json').read_text())
rho=649
HS=[int(x,16) for x in H['homology_s_columns']]
HR=[int(x,16) for x in H['homology_r_columns']]
HA=[[int(x,16) for x in cols] for cols in H['homology_translation_columns']]
EA=[int(x,16) for x in H['A_norm_columns']]
Omega=[int(x,16) for x in H['pairing_columns_mod2']]
def combine(cols,v):
 out=0
 while v:
  b=v&-v;out^=cols[b.bit_length()-1];v^=b
 return out
def solver(cols):
 bas={};null=[];ind=[]
 for j,col in enumerate(cols):
  v=col;w=1<<j
  while v:
   p=v.bit_length()-1
   if p not in bas:bas[p]=(v,w);ind.append(j);break
   a,b=bas[p];v^=a;w^=b
  if not v:null.append(w)
 def solve(v):
  out=0
  for p in sorted(bas,reverse=True):
   if v>>p&1:a,b=bas[p];v^=a;out^=b
  assert not v
  return out
 return solve,len(bas),null,ind
def rank(cols):return solver(cols)[1]
AC={(0,0,0,0):[1<<j for j in range(rho)]}
def amat(a):
 a=tuple(a)
 if a not in AC:
  j=next(i for i,x in enumerate(a) if x);b=list(a);b[j]-=1
  AC[a]=[combine(HA[j],v) for v in amat(b)]
 return AC[a]
def norm(v,Hgens):
 for a in Hgens:
  A=amat(a);w=combine(A,v);v^=w^combine(A,w)
 return v
def normalized(v):
 a=next(x for x in v if x);return tuple(x*pow(a,-1,3)%3 for x in v)
lines=sorted({normalized(v) for v in product(range(3),repeat=4) if any(v)})
assert len(lines)==40
blocks=[];projectors=[];block_solvers=[];C3=[]
for ell in lines:
 p=next(i for i,x in enumerate(ell) if x)
 kernels=[]
 for j in range(4):
  if j!=p:
   a=[0]*4;a[j]=1;a[p]=-ell[j]*pow(ell[p],-1,3)%3;kernels.append(tuple(a))
 a=[0]*4;a[p]=pow(ell[p],-1,3);J=amat(a)
 candidates=[norm(1<<j,kernels)^EA[j] for j in range(rho)]
 assert rank(candidates)==16
 paired=[];bs={}
 def insert(v):
  while v:
   q=v.bit_length()-1
   if q not in bs:bs[q]=v;return True
   v^=bs[q]
  return False
 for v in candidates:
  if insert(v):
   w=combine(J,v);assert insert(w)
   assert combine(J,w)==v^w
   paired.extend([v,w])
 assert len(paired)==16
 solve,rr,_,_=solver(paired);assert rr==16
 coords=[solve(v) for v in candidates]
 assert all(combine(paired,coords[j])==candidates[j] for j in range(rho))
 blocks.append(paired);projectors.append(coords);block_solvers.append(solve);C3.append(J)
assert rank([v for p in blocks for v in p])==640

n=16;offset=[i*(2*n-i-1)//2 for i in range(n)]
pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
def wedge(a,b):
 out=0
 for i in range(n):
  row=(b if a>>i&1 else 0)^(a if b>>i&1 else 0)
  out|=(row>>(i+1))<<offset[i]
 return out
def wa(v,cols):
 out=0
 while v:
  b=v&-v;i,j=pairs[b.bit_length()-1];out^=wedge(cols[i],cols[j]);v^=b
 return out
IB=[wedge(1<<(2*i),1<<(2*i+1)) for i in range(8)]
for i in range(8):
 for j in range(i+1,8):
  u,v=1<<(2*i),1<<(2*i+1);a,b=1<<(2*j),1<<(2*j+1)
  IB.append(wedge(u,a)^wedge(u,b)^wedge(v,b))
for i in range(8):
 for j in range(i+1,8):
  u,v=1<<(2*i),1<<(2*i+1);a,b=1<<(2*j),1<<(2*j+1)
  IB.append(wedge(u,b)^wedge(v,a))
isco,ir,_,_=solver(IB);assert ir==64
JC=[]
for i in range(8):JC.extend([1<<(2*i+1),(1<<(2*i))^(1<<(2*i+1))])
assert all(wa(v,JC)==v for v in IB)
S4=tuple(map(tuple,D['quotient_s_columns']));R4=tuple(map(tuple,D['quotient_r_columns']))
def mv(A,v):return tuple(sum(v[j]*A[j][i] for j in range(4))%3 for i in range(4))
def mm(A,B):return tuple(mv(A,c) for c in B)
Rinv=mm(R4,R4)
lix={v:i for i,v in enumerate(lines)}
actions={};block_actions={}
for name,HM,inv4 in [('s',HS,S4),('r',HR,Rinv)]:
 cols=[];records=[]
 for bi,ell in enumerate(lines):
  target=normalized(tuple(sum(ell[i]*c[i] for i in range(4))%3 for c in inv4));bj=lix[target]
  local=[block_solvers[bj](combine(HM,v)) for v in blocks[bi]]
  assert rank(local)==16
  for j,v in enumerate(blocks[bi]):assert combine(blocks[bj],local[j])==combine(HM,v)
  exterior=[isco(wa(v,local)) for v in IB]
  assert rank(exterior)==64
  cols.extend(v<<(64*bj) for v in exterior)
  records.append({'target_block':bj,'homology_columns':local,'exterior_columns':exterior})
 actions[name]=cols;block_actions[name]=records
assert all(combine(actions['s'],v)==1<<j for j,v in enumerate(actions['s']))
assert all(combine(actions['r'],combine(actions['r'],v))==1<<j for j,v in enumerate(actions['r']))

dim=2560;rel={}
for M0 in actions.values():
 for j,v in enumerate(M0):
  v^=1<<j
  while v:
   p=v.bit_length()-1
   if p not in rel:rel[p]=v;break
   v^=rel[p]
free=[j for j in range(dim) if j not in rel];d=len(free)
def quotient(v):
 for p in sorted(rel,reverse=True):
  if v>>p&1:v^=rel[p]
 return sum(((v>>p)&1)<<i for i,p in enumerate(free))
qcols=[quotient(1<<j) for j in range(dim)]
assert rank(qcols)==d
assert all(quotient(v^(1<<j))==0 for M0 in actions.values() for j,v in enumerate(M0))
dual=[sum(1<<j for j,c in enumerate(qcols) if c>>i&1) for i in range(d)]
# The compactification map in every actual character block is the quotient
# by the radical of its restricted integral ribbon pairing.
compact=[]
for p in blocks:
 local=[sum(1<<i for i,u in enumerate(p) if (u&combine(Omega,v)).bit_count()%2)
        for v in p]
 assert rank(local)==8
 compact.append([wa(v,local) for v in IB])
 assert rank(compact[-1])==16
def compact_map(v):
 out=0
 for bi in range(40):
  piece=(v>>(64*bi))&((1<<64)-1)
  out|=combine(compact[bi],piece)<<(120*bi)
 return out
def normQ(v):
 out=0
 for word in G['all48_marked_words']:
  w=v
  # Left action of a product applies its last letter first.
  for token in reversed(word):w=combine(actions['s' if token==0 else 'r'],w)
  out^=w
 return out
norms=[];cnorms=[]
for p in free:
 v=normQ(1<<p)
 assert combine(actions['s'],v)==v and combine(actions['r'],v)==v
 norms.append(v);cnorms.append(compact_map(v))
nr=rank(norms);cr=rank(cnorms)
summary={
 'scope':'Actual arithmetic order3888 module and actual compact norm.',
 'homology_dimension':rho,'moving_homology_dimension':640,
 'character_pair_blocks':40,'each_character_pair_homology_dimension':16,
 'each_character_pair_compact_dimension':8,
 'each_invariant_exterior_block_dimension':64,
 'invariant_exterior_dimension':dim,
 'actual_coinvariant_dimension':d,'actual_relation_rank':len(rel),
 'full_group_norm_rank':nr,'compact_group_norm_rank':cr,
 'Tate_minus_one_dimension':d-nr,
 'compact_norm_kernel_dimension':d-cr,
 'all40_projection_and_s_r_maps_checked':True,
 'all_coinvariant_relations_and_norm_invariances_checked':True,
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'all40_character_pairs':[list(v) for v in lines],
 'all40_homology_bases':[[hex(v) for v in p] for p in blocks],
 'all40_projector_coordinate_columns':projectors,
 'universal64_invariant_exterior_basis':[hex(v) for v in IB],
 'block_s_action':block_actions['s'],'block_r_action':block_actions['r'],
 'coinvariant_representative_indices':free,
 'coinvariant_dual_functionals':[hex(v) for v in dual],
 'coinvariant_columns':[hex(v) for v in qcols],
 'all40_compact_exterior_columns':[[hex(v) for v in c] for c in compact],
 'full_norm_representative_images':[hex(v) for v in norms],
 'compact_norm_representative_images':[hex(v) for v in cnorms]}
(OUT/'d_arithmetic_invariant_module.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
