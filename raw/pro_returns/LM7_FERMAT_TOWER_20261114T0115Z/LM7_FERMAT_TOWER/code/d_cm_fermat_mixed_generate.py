#!/usr/bin/env python3
"""An actual extra-CM automorphism on the joint Fermat12 homology quotient.

The input base and all linear-obstruction certificates are regenerated on import.
The final witness is checked as a literal B-word in all 6912 edge coordinates.
Generation is checked on all 1153 free-kernel basis elements at both 2 and 3.
"""
from pathlib import Path
from collections import deque
import json,time
import numpy as np
import d_cm_fermat_mixed_linear as m

OUT=Path(__file__).resolve().parent;started=time.time()
n=m.rank;size=m.size;C=m.C;nc=m.nc
D=m.D;hs=m.hs;hr=m.hr;ht=m.ht
rec=next(r for r in D['candidate_conjugators']
         if r['A_Q']==[1,0,0,1] and r['beta_Q']==[3,4,8,3])
base=next(v for v in rec['lifts'] if v['A']==0 and v['beta']==408)
A=base['A'];beta=base['beta'];ss=base['s_image'];rr=base['r_image']
assert (ss,rr)==(hs,hr)
PA=m.path(A);PB=m.path(beta);Pt=m.Pt
E=PB-m.act(PB,hs)
assert np.array_equal(C@E[nc],E)
Ms=m.Ms;Mt=m.act(C,ht)[nc]
F=np.concatenate([np.eye(n,dtype=np.int16)-Ms,Ms-Mt],axis=1)%2
rhs=E[nc]%2

def affine2(F,rhs):
 packed=np.packbits(F,axis=1,bitorder='little');basis={}
 for row,b in zip(packed,rhs):
  v=int.from_bytes(row.tobytes(),'little');b=int(b)
  while v:
   k=v.bit_length()-1
   if k not in basis:basis[k]=(v,b);break
   w,c=basis[k];v^=w;b^=c
  if not v:assert b==0
 piv=sorted(basis);free=[j for j in range(F.shape[1]) if j not in basis]
 freemask=sum(1<<j for j in free)
 def solve(rng):
  v=int.from_bytes(rng.bytes((F.shape[1]+7)//8),'little')&freemask
  for k in piv:
   w,b=basis[k]
   if ((w&v).bit_count()&1)^b:v^=1<<k
  return np.array([(v>>j)&1 for j in range(F.shape[1])],dtype=np.int16)
 return solve,len(piv),len(free)

solve,correction_rank,affine_dimension=affine2(F,rhs)
assert correction_rank==1152 and affine_dimension==1154
print('affine correction rank',correction_rank,'dimension',affine_dimension,flush=True)

def rank2(A):
 basis={}
 for row in np.packbits(A%2,axis=1,bitorder='little'):
  v=int.from_bytes(row.tobytes(),'little')
  while v:
   k=v.bit_length()-1
   if k not in basis:basis[k]=v;break
   v^=basis[k]
 return len(basis)

# For the chosen base action alpha_H is the identity.  Transport of the image
# of one oriented edge gives the exact induced map of the Bass--Serre graph.
indices=np.empty((n,size),dtype=np.int32)
st=m.states[nc]
for h in range(size):
 q,u,v=m.states[int(m.inverse[h])];M=m.LM[q]
 aa=(u+st[:,1]*M[0,0]+st[:,2]*M[0,1])%12
 bb=(v+st[:,1]*M[1,0]+st[:,2]*M[1,1])%12
 indices[:,h]=m.grid[m.qt[q,st[:,0]],aa+12*bb]
assert np.all(indices>=0)
cols=[(np.array([e for e,v in col],dtype=np.int32),
        np.array([v for e,v in col],dtype=np.int16))
       for col in D['integral_cycle_columns']]
def kernel_matrix(edge,p):
 transported=edge[indices]%p
 T=np.empty((n,n),dtype=np.int16)
 for j,(edges,values) in enumerate(cols):T[:,j]=transported[:,edges]@values%p
 return T

rng=np.random.default_rng(37012026)
trials=[];chosen=None
edge0=PA-PB;edge0[A]+=1
for trial in range(1,513):
 z=solve(rng);b2=z[:n];a2=z[n:]
 assert not np.any((F@z-rhs)%2)
 edge=(edge0+C@(a2-b2))%2
 T2=kernel_matrix(edge,2);rankT=rank2(T2)
 trials.append(rankT)
 print('trial',trial,'kernel rank',rankT,flush=True)
 if rankT==n:chosen=(b2.copy(),a2.copy(),T2.copy());break
assert chosen is not None,'No generating solution found in the explicit search.'
b2,a2,T2=chosen

# At 3, the coprime order-two centralizer correction is explicit: E is
# anti-invariant, and b3=E gives (1-s)b3=-E over F3.  A stays the identity.
a3=np.zeros(n,dtype=np.int16);b3=E[nc]%3
assert not np.any((PB+C@b3-m.act(PB+C@b3,hs))%3)
edge3=(edge0+C@(a3-b3))%3
T3=kernel_matrix(edge3,3)
assert np.array_equal(T3,np.eye(n,dtype=np.int16))

# The one integral pair below represents both prime-wise corrections.
a6=(3*a2+4*a3)%6;b6=(3*b2+4*b3)%6
PA6=PA+C@a6;PB6=PB+C@b6
defect=PB6-m.act(PB6,hs)+m.act(PA6-m.act(PA6,hr)+m.act(m.path(hr),A),hs)-Pt
assert not np.any(defect%6)

# Rebuild the graph tree and convert every fundamental cycle to a literal
# free-product word; 0=s, 1=r, 2=r^{-1}.  Every word is checked integrally.
rs=np.array(D['right_s'],dtype=np.int32);rright=np.array(D['right_r'],dtype=np.int32)
rright2=rright[rright]
v2=[(0,min(h,int(rs[h]))) for h in range(size)]
v3=[(1,min(h,int(rright[h]),int(rright2[h]))) for h in range(size)]
vertices=sorted(set(v2)|set(v3));vi={v:i for i,v in enumerate(vertices)}
adj=[[] for v in vertices]
for h in range(size):
 aa=vi[v2[h]];bb=vi[v3[h]];adj[aa].append((bb,h,1));adj[bb].append((aa,h,-1))
root=vi[v2[0]];paths={root:[]};queue=deque([root]);tree=set()
while queue:
 aa=queue.popleft()
 for bb,h,sign in adj[aa]:
  if bb not in paths:paths[bb]=paths[aa]+[(h,sign)];tree.add(h);queue.append(bb)
assert [h for h in range(size) if h not in tree]==nc.tolist()

def model(word):
 h=0;P=np.zeros(size,dtype=np.int32)
 for letter in word:
  if letter==0:h=int(rs[h])
  else:
   k=int(rright[h] if letter==1 else rright2[h]);P[h]+=1;P[k]-=1;h=k
 return h,P
def inverse_word(word):return [0 if a==0 else 3-a for a in reversed(word)]
def base_word(h):
 w=[]
 while h:
  h,a=m.parent[h];w.append(a)
 return list(reversed(w))

basiswords=[]
for j,h in enumerate(nc):
 walk=paths[vi[v2[h]]]+[(int(h),1)]+[(e,-sgn) for e,sgn in reversed(paths[vi[v3[h]]])]
 w=[];g=0
 for e,sign in walk:
  if sign==1:
   if g!=e:assert rs[g]==e;w.append(0)
  else:
   if g!=e:
    if rright[g]==e:w.append(1)
    else:assert rright2[g]==e;w.append(2)
  g=e
 if g:assert g==hs;w.append(0)
 q,P=model(w);assert q==0 and np.array_equal(P,C[:,j])
 basiswords.append(w)
def correction_word(coeff):
 w=[]
 for c,bw in zip(coeff,basiswords):
  c=int(c)
  if c>3:c-=6
  block=bw if c>=0 else inverse_word(bw)
  for j in range(abs(c)):w.extend(block)
 return w
Aw=correction_word(a6)+base_word(A)
Bw=correction_word(b6)+base_word(beta)
assert model(Aw)[0]==A and not np.any((model(Aw)[1]-PA6)%6)
assert model(Bw)[0]==beta and not np.any((model(Bw)[1]-PB6)%6)
cuspword=Bw+[0]+inverse_word(Bw)+Aw+[1]+inverse_word(Aw)+[2,0]
q,P=model(cuspword);assert q==0 and not np.any(P%6)
print('literal cusp identity checked',len(cuspword),'letters',size,'edge coordinates',flush=True)

# Independent generator-substitution evaluation of every free-kernel word.
genwords=[Bw+[0]+inverse_word(Bw),Aw+[1]+inverse_word(Aw)]
gen=[model(w) for w in genwords]
assert [g for g,p in gen]==[hs,hr]
gen.append((int(m.inverse[hr]),-m.act(gen[1][1],int(m.inverse[hr]))))
Tcheck=np.empty((n,n),dtype=np.int16)
for j,w in enumerate(basiswords):
 h=0;P=np.zeros(size,dtype=np.int32)
 for a in w:
  q,v=gen[a];P+=m.act(v,h);h=m.mul(h,q)
 assert h==0
 Tcheck[:,j]=P[nc]%6
assert np.array_equal(Tcheck%2,T2)
assert np.array_equal(Tcheck%3,T3)
print('all',n,'kernel basis images checked; ranks',n,n,flush=True)

# The cusp acquires precisely the expected 2- and 3-homology orders.
P24=np.zeros(size,dtype=np.int32);h=0
for j in range(24):P24+=m.act(Pt,h);h=m.mul(h,ht)
assert h==0 and np.any(P24%2) and np.any(P24%3)
summary={'base_order':size,'free_kernel_rank':n,'A_Q':rec['A_Q'],
 'beta_Q':rec['beta_Q'],'A_H':A,'beta_H':beta,
 'base_action':'identity','extra_CM_coset':True,'multiplier':1,
 'correction_rank_mod2':correction_rank,'affine_dimension_mod2':affine_dimension,
 'first_generating_trial':len(trials),'generation_ranks_mod2_trials':trials,
 'kernel_generation_ranks':{'2':n,'3':n},
 'mod3_action':'identity, with explicit coprime centralizer correction',
 'cusp_orders':{'H':24,'J2':48,'J3':72,'J6':144},
 'quotient_order':'6912 * 6^1153',
 'A_word_length':len(Aw),'beta_word_length':len(Bw),
 'literal_cusp_word_length':len(cuspword),'all_edge_cusp_check':True,
 'all_basis_words_integrally_verified':True,
 'all_basis_images_independently_checked':True,
 'scope':'Actual automorphism of B/[L,L]L^6; full profinite lifting is not inferred.',
 'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,'a_mod6':a6.tolist(),'beta_correction_mod6':b6.tolist(),
 'A_word':Aw,'beta_word':Bw,'basis_words':basiswords}
(OUT/'d_cm_fermat_mixed_generate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
