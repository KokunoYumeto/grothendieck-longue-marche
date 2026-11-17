#!/usr/bin/env python3
"""Exact finite centralizer stabilization for B=C2*C3 over q12.

Q=PSL2(Z/12), N=ker(B->Q), R=B/(N' N^3). N is the free
rank97 subgroup represented by its literal Bass--Serre covering graph.
Every Q-residue centralizing r is checked by its actual affine lifting
obstruction in H1(N,F3). No profinite centralizer theorem is invoked.
"""
import test_fivepoint_cm_level as T
import numpy as np,json
from pathlib import Path
from collections import deque
Q=T.BQ;nt=len(Q);table=T.btable;inverses=np.array(T.binverses,dtype=np.int16)
qs,qr=T.bs,T.br
which2,reps2,_=T.bcases[2];which3,reps3,_=T.bcases[3]
n2=len(reps2);n3=len(reps3)
endpoints=np.array([(which2[q],n2+which3[q]) for q in Q],dtype=np.int16)
assert endpoints.shape==(576,2) and n2+n3==480
adj=[[] for _ in range(n2+n3)]
for e,(u,v) in enumerate(endpoints):adj[u].append((int(v),e,1));adj[v].append((int(u),e,-1))
root=which2[Q[0]];paths=np.zeros((480,576),dtype=np.int16);seen={root};queue=deque([root]);tree=set()
while queue:
 u=queue.popleft()
 for v,e,sg in adj[u]:
  if v in seen:continue
  seen.add(v);queue.append(v);tree.add(e);paths[v]=paths[u];paths[v,e]+=sg
assert len(seen)==480 and len(tree)==479
chords=[e for e in range(576) if e not in tree]
cycles=[]
for e in chords:
 u,v=endpoints[e];z=paths[u]-paths[v];z[e]+=1;cycles.append(z)
cycles=np.array(cycles,dtype=np.int16);assert cycles.shape==(97,576)
assert np.array_equal(cycles[:,chords],np.eye(97,dtype=np.int16))
boundary=np.zeros((576,480),dtype=np.int16)
for e,(u,v) in enumerate(endpoints):boundary[e,u]=-1;boundary[e,v]=1
assert not np.any(cycles@boundary)
# Positive Cayley words in the literal factors s,r for all Q residues.
words={0:()};order=[0]
for q in order:
 for j,g in enumerate((qs,qr),1):
  h=int(table[q,g])
  if h not in words:words[h]=words[q]+(j,);order.append(h)
assert len(words)==576

def path(w):
 q=0;v=np.zeros(576,dtype=np.int16)
 for j in w:
  g=qs if abs(j)==1 else qr
  if j<0:g=int(inverses[g])
  h=int(table[q,g])
  if abs(j)==2:v[q]+=1;v[h]-=1
  q=h
 return q,v
# Defining relators have zero graph paths (including all translations).
for w in ((1,1),(2,2,2)):
 q,v=path(w);assert q==0 and not np.any(v)
A=cycles[:,table[inverses[qr],np.array(chords)]]%3
assert np.array_equal(A@A@A%3,np.eye(97,dtype=np.int16))
K=(A-np.eye(97,dtype=np.int16))%3
basis,projection=T.row_space_projection(K,3)
central=[q for q in range(576) if table[q,qr]==table[qr,q]]
records=[]
for q in central:
 w=(2,)+words[q]+(-2,)+T.inverse(words[q])
 end,v=path(w);assert end==0 and not np.any(v@boundary)
 c=v[chords]%3;obs=c@projection%3
 records.append({'residue':q,'matrix_mod12_projective':list(Q[q]),'lift_word':list(words[q]),
                 'obstruction':obs.tolist(),'lifts_to_centralizer':not np.any(obs)})
allowed=[r['residue'] for r in records if r['lifts_to_centralizer']]
actual=sorted([0,qr,int(table[qr,qr])]);assert sorted(allowed)==actual
print('PASS modular finite centralizer: Q order576; free kernel rank97',flush=True)
print('rank(r-1) over F3:',len(basis),'fixed dimension',97-len(basis),flush=True)
for rec in records:print(rec,flush=True)
print('PASS all',len(central),'commuting Q residues; allowed exactly <r>:',allowed,flush=True)
out={'Q_order':576,'N_rank':97,'R_order':'576*3^97','rank_r_minus_1':len(basis),
     'centralizer_kernel_dimension':97-len(basis),'centralizer_base_residues':len(central),
     'centralizer_allowed_residues':allowed,'records':records,
     'signed_refinement_order':'1152*3^97','signed_centralizer_image':'<UL0 mod12> of order6'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),cycles=cycles,chords=np.array(chords),
                   endpoints=endpoints,table=table,inverses=inverses,action_r=A,
                   obstruction_projection=projection)
