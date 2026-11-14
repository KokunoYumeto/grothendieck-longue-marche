#!/usr/bin/env python3
"""Exact D9(K) image in the rank385 exponent-four relative homology quotient."""
from pathlib import Path
from collections import deque
from itertools import product
import json,time
import numpy as np

OUT=Path(__file__).resolve().parent;OLD=OUT if (OUT/'d_cm_fermat_joint_base.json').is_file() else next(p/'LM7_FERMAT_TOWER'/'code' for p in OUT.parents if (p/'LM7_FERMAT_TOWER'/'code'/'d_cm_fermat_joint_base.json').is_file())
started=time.time();D=json.loads((OLD/'d_cm_fermat_joint_base.json').read_text())
Q=[tuple(q) for q in D['Q']];ix={q:i for i,q in enumerate(Q)}
LM=np.array(D['Q_linear_matrices'],dtype=np.int16);I=(1,0,0,1);qi=ix[I]
def canon(a):return min(tuple(a),tuple(-int(x)%12 for x in a))
def qm(a,b):return canon(((a[0]*b[0]+a[1]*b[2])%12,(a[0]*b[1]+a[1]*b[3])%12,(a[2]*b[0]+a[3]*b[2])%12,(a[2]*b[1]+a[3]*b[3])%12))
qt=np.array([[ix[qm(a,b)] for b in Q] for a in Q],dtype=np.int16)
qinv=np.array([ix[canon((q[3],-q[1]%12,-q[2]%12,q[0]))] for q in Q],dtype=np.int16)
states=[];lookup={};projection=[]
for q,a,b in D['states']:
 z=(q,a%4,b%4)
 if z not in lookup:lookup[z]=len(states);states.append(z)
 projection.append(lookup[z])
states=np.array(states,dtype=np.int16);projection=np.array(projection,dtype=np.int32)
size=len(states);assert size==2304
hs=projection[D['s']];hr=projection[D['r']];ht=projection[D['t']]
grid=np.full((576,16),-1,dtype=np.int32)
for h,(q,a,b) in enumerate(states):grid[q,int(a)+4*int(b)]=h
def mul(a,b):
 q,u,v=states[a];qq,x,y=states[b];M=LM[q]
 return int(grid[qt[q,qq],int((u+M[0,0]*x+M[0,1]*y)%4)+4*int((v+M[1,0]*x+M[1,1]*y)%4)])
inverse=[]
for q,u,v in states:
 qq=qinv[q];M=LM[qq]
 inverse.append(int(grid[qq,int((-M[0,0]*u-M[0,1]*v)%4)+4*int((-M[1,0]*u-M[1,1]*v)%4)]))
inverse=np.array(inverse,dtype=np.int32);perms={}
def perm(h):
 if h not in perms:
  q,u,v=states[h];M=LM[q]
  aa=(u+states[:,1]*M[0,0]+states[:,2]*M[0,1])%4
  bb=(v+states[:,1]*M[1,0]+states[:,2]*M[1,1])%4
  perms[h]=grid[qt[q,states[:,0]],aa+4*bb]
 return perms[h]
def act(v,h):return v[perm(int(inverse[h]))]
rs=np.array([mul(h,hs) for h in range(size)],dtype=np.int32)
rr=np.array([mul(h,hr) for h in range(size)],dtype=np.int32);rr2=rr[rr]
v2=[(0,min(h,int(rs[h]))) for h in range(size)]
v3=[(1,min(h,int(rr[h]),int(rr2[h]))) for h in range(size)]
vertices=sorted(set(v2)|set(v3));vi={v:i for i,v in enumerate(vertices)}
adj=[[] for v in vertices]
for h in range(size):
 a,b=vi[v2[h]],vi[v3[h]];adj[a].append((b,h,1));adj[b].append((a,h,-1))
root=vi[v2[0]];paths={root:[]};queue=deque([root]);tree=set()
while queue:
 a=queue.popleft()
 for b,h,sgn in adj[a]:
  if b not in paths:paths[b]=paths[a]+[(h,sgn)];tree.add(h);queue.append(b)
nc=[h for h in range(size) if h not in tree];d=len(nc);assert d==385
C=np.zeros((size,d),dtype=np.int16)
for j,h in enumerate(nc):
 for e,sgn in paths[vi[v2[h]]]+[(h,1)]+[(e,-sgn) for e,sgn in paths[vi[v3[h]]]]:C[e,j]+=sgn
assert np.array_equal(C[nc],np.eye(d,dtype=np.int16))
def model(w):
 h=0;v=np.zeros(size,dtype=np.int32)
 for a in w:
  if a==0:h=int(rs[h])
  else:
   z=int(rr[h] if a==1 else rr2[h]);v[h]+=1;v[z]-=1;h=z
 return h,v%4
def mm(a,b):return mul(a[0],b[0]),(a[1]+act(b[1],a[0]))%4
def ii(a):
 h=int(inverse[a[0]]);return h,(-act(a[1],h))%4
def cm(a,b):return mm(mm(mm(a,b),ii(a)),ii(b))
def powelt(a,n):
 z=(0,np.zeros(size,dtype=np.int16))
 while n:
  if n&1:z=mm(z,a)
  a=mm(a,a);n//=2
 return z
Kwords=json.loads((OLD/'d_cm_rank4_refine.json').read_text())['K_basis_words']
K=[model(w) for w in Kwords];kg=[q for q,v in K]
A0={0};todo=[0]
for q in todo:
 for h in kg:
  z=mul(q,h)
  if z not in A0:A0.add(z);todo.append(z)
assert len(A0)==128
assert all(np.array_equal(LM[states[h,0]],np.eye(2,dtype=np.int16)) for h in A0)
for h in A0:assert mul(mul(h,h),mul(h,h))==0
for a,b in product(A0,repeat=2):
 z=mul(mul(mul(a,b),int(inverse[a])),int(inverse[b]))
 assert mul(z,z)==0 and all(mul(z,h)==mul(h,z) for h in kg)
M=[act(C,q)[nc]%4 for q in kg]
eye=np.eye(d,dtype=np.int16)

def module_basis(vectors):
 """Exact generators and membership over Z/4, with invariant type C4^a C2^b."""
 A=np.array(vectors,dtype=np.int16).reshape((-1,d))%4
 r=0;piv=[]
 for j in range(d):
  hits=np.flatnonzero(A[r:,j]%2)
  if not len(hits):continue
  k=r+int(hits[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*int(A[r,j])%4
  factors=A[:,j].copy();factors[r]=0;A=(A-factors[:,None]*A[r])%4
  piv.append(j);r+=1
  if r==len(A):break
 assert not np.any(A[r:]%2)
 B=(A[r:]//2).astype(np.uint8);s=0;piv2=[]
 for j in range(d):
  hits=np.flatnonzero(B[s:,j])
  if not len(hits):continue
  k=s+int(hits[0]);B[[s,k]]=B[[k,s]]
  factors=B[:,j].copy();factors[s]=0;B^=factors[:,None]*B[s]
  piv2.append(j);s+=1
  if s==len(B):break
 assert all(j not in piv for j in piv2)
 units=A[:r].copy();evens=2*B[:s].astype(np.int16)
 basis=np.concatenate([units,evens],axis=0)
 def reduce(v):
  v=np.array(v,dtype=np.int16).copy()%4
  for p,w in zip(piv,units):v=(v-int(v[p])*w)%4
  for p,w in zip(piv2,evens):
   if v[p]%2:return v
   v=(v-(int(v[p])//2)*w)%4
  return v
 def contains(v):return not np.any(reduce(v))
 return {'basis':basis,'C4_rank':r,'C2_rank':s,'log2_order':2*r+s,
         'unit_pivots':piv,'even_pivots':piv2,'contains':contains,'reduce':reduce}

triples=[]
for i in range(4):
 for j in range(i+1,4):
  for k in range(4):
   q,v=cm(cm(K[i],K[j]),K[k]);assert q==0 and not np.any((C@v[nc]-v)%4)
   triples.append(v[nc])
U=module_basis(triples);history=[]
while True:
 history.append([U['C4_rank'],U['C2_rank']])
 vectors=[v for v in U['basis']]
 for a in M:vectors.extend((a@U['basis'].T%4).T)
 W=module_basis(vectors)
 if W['log2_order']==U['log2_order']:
  U=W;break
 U=W
assert all(U['contains'](a@v%4) for a in M for v in U['basis'])
gamma={3:U};data=[]
for degree in range(3,10):
 if degree>3:
  prev=gamma[degree-1]['basis'];vectors=[]
  for a in M:vectors.extend(((a-eye)@prev.T%4).T)
  gamma[degree]=module_basis(vectors)
 V=gamma[degree]
 assert all(V['contains'](a@v%4) for a in M for v in V['basis'])
 data.append({'degree':degree,'C4_rank':V['C4_rank'],'C2_rank':V['C2_rank'],'log2_order':V['log2_order']})
 print('gamma',degree,'type',V['C4_rank'],V['C2_rank'],flush=True)
W=module_basis(list(gamma[9]['basis'])+list(2*gamma[5]['basis']%4))
assert all(W['contains'](a@v%4) for a in M for v in W['basis'])
for h in [hs,hr]:
 MM=act(C,h)[nc]%4
 assert all(W['contains'](MM@v%4) for v in W['basis'])
summary={'H4_order':size,'L4_rank':d,'K_over_L4_order':len(A0),
 'K_over_L4_class_at_most2_and_exponent4_checked':True,
 'gamma3_normal_closure_type_history':history,'gamma_types':data,
 'D9_image_C4_rank':W['C4_rank'],'D9_image_C2_rank':W['C2_rank'],
 'D9_image_log2_order':W['log2_order'],
 'common_coefficient_quotient_C4_rank':d-W['C4_rank']-W['C2_rank'],
 'common_coefficient_quotient_C2_rank':W['C2_rank'],
 'common_quotient_order':'2304 * 2^'+str(2*d-W['log2_order']),
 'formula':'image D9(K) = gamma9(K-image) + 2 gamma5(K-image) = I^6 U + 2 I^2 U',
 'all_module_stability_checks':True,
 'scope':'Exact common quotient with B/D9(K), not an asserted intersection-image formula for gamma3N intersect D9K.',
 'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,'states':states.tolist(),'H12_to_H4':projection.tolist(),
 'cycle_chords':nc,'cycle_columns':[[[int(e),int(C[e,j])] for e in np.flatnonzero(C[:,j])] for j in range(d)],
 'K_base_elements':kg,'K_action_matrices':[a.tolist() for a in M],
 'gamma3_generators':[v.tolist() for v in U['basis']],
 'D9_generators':[v.tolist() for v in W['basis']],
 'D9_unit_pivots':W['unit_pivots'],'D9_even_pivots':W['even_pivots']}
(OUT/'d_cm_fermat_degree8_module.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
