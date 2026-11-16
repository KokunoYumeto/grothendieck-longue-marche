"""Exact common residual-seed gate on the two coupling modules and six B-cores.
No finite GT assignments are enumerated. Written by GPT-6 Astra, 2026-11-16.
"""
from pathlib import Path
from itertools import product,permutations
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parents[1];FIVE=HERE.parent/'agent_five'
def m2(a,b):return tuple((a[2*i]*b[j]+a[2*i+1]*b[2+j])%3 for i in range(2)for j in range(2))
def i2(a):
 d=(a[0]*a[3]-a[1]*a[2])%3
 return(d*a[3]%3,-d*a[1]%3,-d*a[2]%3,d*a[0]%3)
def act(g,v):
 out=[0]*16
 for j in range(4):
  k=g[j];out[4*k:4*k+4]=m2(m2(g[4+4*j:8+4*j],v[4*j:4*j+4]),i2(g[20+4*j:24+4*j]))
 return tuple(out)
def basis(rows):
 piv={}
 for vv in rows:
  v=list(vv)
  for j,w in sorted(piv.items()):
   z=v[j]
   if z:v=[(a-z*b)%3 for a,b in zip(v,w)]
  nz=[j for j,a in enumerate(v)if a]
  if nz:
   j=nz[0];z=v[j];piv[j]=tuple(z*a%3 for a in v)
 return sorted(piv.items())
def coord(v,bs):
 v=list(v);out=[]
 for j,w in bs:
  z=v[j];out.append(z);v=[(a-z*b)%3 for a,b in zip(v,w)]
 assert not any(v)
 return out
def inv(M):
 n=len(M);r=np.concatenate((M.copy(),np.eye(n,dtype=np.int64)),axis=1)
 for j in range(n):
  k=j+int(np.flatnonzero(r[j:,j])[0]);r[[j,k]]=r[[k,j]]
  r[j]=r[j]*r[j,j]%3
  for k in range(n):
   if k!=j:r[k]=(r[k]-r[k,j]*r[j])%3
 return r[:,n:]
matrix_pairs=[];records=[]
for file in('ferrari_harmonic16_module.npz','ferrari_harmonic16_second_module.npz'):
 D=np.load(FIVE/file);bs=basis(D['kernel_basis']);assert len(bs)==4
 pair=[]
 for q in D['generator_bases']:
  q=tuple(map(int,q));cols=[coord(act(q,w),bs)for j,w in bs]
  pair.append(np.array(cols,dtype=np.int64).T)
 z=inv(pair[0]@pair[1]%3);triple=pair+[z]
 for perm in permutations(range(3)):matrix_pairs.append((triple[perm[0]],triple[perm[1]]))
 records.append({'module':file,'x_matrix':pair[0].tolist(),'y_matrix':pair[1].tolist()})
matrix_pairs.append((np.array([[1,2],[0,1]],dtype=np.int64),np.array([[1,0],[1,1]],dtype=np.int64)))
images=[[],[]];target=[];offset=0
for k,(a,b)in enumerate(matrix_pairs):
 n=len(a);vectors=[v for v in product(range(3),repeat=n)if any(v)];idx={v:i for i,v in enumerate(vectors)}
 for j,M in enumerate((a,b)):
  images[j].extend(offset+idx[tuple(map(int,np.array(v)@M%3))]for v in vectors)
 if k==len(matrix_pairs)-1:
  target.extend(offset+idx[tuple(-x%3 for x in v)]for v in vectors)
 else:target.extend(offset+i for i in range(len(vectors)))
 offset+=len(vectors)
gens=[Permutation(v)for v in images];goal=Permutation(target);G=PermutationGroup(gens)
print('degree',offset,'computing actual common image',flush=True)
t0=time.time();orderG=int(G.order());print('image order',orderG,'seconds',time.time()-t0,flush=True)
D1=G.derived_subgroup();orderD1=int(D1.order());print('first derived order',orderD1,flush=True)
D2=D1.derived_subgroup();orderD2=int(D2.order());print('second derived order',orderD2,flush=True)
contained=bool(D2.contains(goal));print('common identity-module / negative-compact element in second derived:',contained,flush=True)
def e3(o):
 o=int(o);three=1
 while o%3==0:three*=3;o//=3
 return 0 if three==1 else o*pow(o,-1,three)
def comm(g,h):return g*h*g**-1*h**-1
trip=(gens[0],gens[1],(gens[0]*gens[1])**-1)
core_gens=[];core_records=[]
for pp in permutations(range(3)):
 u,v=trip[pp[0]],trip[pp[1]];z=(u*v)**-1
 uu,vv,zz=u**e3(u.order()),v**e3(v.order()),z**e3(z.order())
 seed=comm(comm(uu,vv),comm(vv,zz))
 if seed not in core_gens:
  core_gens.append(seed);core_records.append({'peripheral_pair':list(pp[:2]),'conjugating_word':[]})
S=PermutationGroup(core_gens);S.schreier_sims();j=0
ambient=[(1,gens[0]),(2,gens[1]),(-1,gens[0]**-1),(-2,gens[1]**-1)]
while j<len(core_gens):
 g=core_gens[j];record=core_records[j];j+=1
 for letter,h in ambient:
  value=h*g*h**-1
  if not S.contains(value):
   core_gens.append(value)
   core_records.append({'peripheral_pair':record['peripheral_pair'],
                        'conjugating_word':[letter]+record['conjugating_word']})
   S=PermutationGroup(core_gens);S.schreier_sims()
   print('orbifold-core normal closure generators',len(core_gens),'order',int(S.order()),flush=True)
normal_contains=bool(S.contains(goal));print('goal in actual orbifold-core seed normal closure:',normal_contains,flush=True)
source_product=[]
if normal_contains:
 raw_word=S.generator_product(goal,original=True)
 lookup={g:i+1 for i,g in enumerate(core_gens)}
 lookup.update({g**-1:-(i+1)for i,g in enumerate(core_gens)if g**-1 not in lookup})
 source_product=[lookup[g]for g in reversed(raw_word)]
 test=Permutation(list(range(offset)))
 for j in source_product:test=test*(core_gens[abs(j)-1]if j>0 else core_gens[abs(j)-1]**-1)
 assert test==goal and len(source_product)%2==1
 print('explicit common seed product length',len(source_product),flush=True)
out={'permutation_degree':offset,'module_data':records,'actual_common_image_order':orderG,
     'first_derived_order':orderD1,'second_derived_order':orderD2,
     'identity_on_all_twelve_core_modules_and_negative_compact_in_second_derived':contained,
     'orbifold_core_seed_normal_closure_order':int(S.order()),
     'goal_in_orbifold_core_seed_normal_closure':normal_contains,
     'core_generators':core_records,'explicit_common_seed_product':source_product,
     'word_convention':'Generator j is h A_e3(u,v) h^-1, with h the listed word in x,y; u,v selected from x,y,(xy)^-1. Multiply signed generator indices left to right. This is an actual profinite word in the full orbifold core and F second derived.',
     'scope':'Exact simultaneous source-derived/core image and explicit controlled seed. No GT lift or complete rank129 nilpotent-image conclusion is inferred without checking all remaining blocks.'}
(HERE/'records'/'rank129_common_residual_seed.json').write_text(json.dumps(out,indent=2)+'\n')
