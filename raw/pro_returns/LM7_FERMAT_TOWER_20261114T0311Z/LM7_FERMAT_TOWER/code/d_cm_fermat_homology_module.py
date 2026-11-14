#!/usr/bin/env python3
"""Exact D9(K) image in the rank385 exponent-eight relative homology quotient."""
from pathlib import Path
from collections import deque
from itertools import product
import json,time
import numpy as np
MOD=8

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
 return h,v%MOD
def mm(a,b):return mul(a[0],b[0]),(a[1]+act(b[1],a[0]))%MOD
def ii(a):
 h=int(inverse[a[0]]);return h,(-act(a[1],h))%MOD
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
M=[act(C,q)[nc]%MOD for q in kg]
eye=np.eye(d,dtype=np.int16)

def module_basis(vectors):
 """Exact row generators and membership for a submodule of (Z/8)^d."""
 A=np.array(vectors,dtype=np.int32).reshape((-1,d))%MOD
 r=0;piv=[];scales=[];counts=[0,0,0]
 for power in range(3):
  scale=2**power
  assert not np.any(A[r:]%scale)
  for j in range(d):
   hits=np.flatnonzero((A[r:,j]//scale)%2)
   if not len(hits):continue
   k=r+int(hits[0]);A[[r,k]]=A[[k,r]]
   inv=pow(int(A[r,j]//scale),-1,MOD)
   A[r]=A[r]*inv%MOD
   assert A[r,j]==scale
   factors=A[r+1:,j]//scale
   A[r+1:]=(A[r+1:]-factors[:,None]*A[r])%MOD
   piv.append(j);scales.append(scale);counts[power]+=1;r+=1
   if r==len(A):break
  if r==len(A):break
 assert not np.any(A[r:])
 basis=A[:r].copy()
 def reduce(v):
  v=np.array(v,dtype=np.int32).copy()%MOD
  for p,scale,row in zip(piv,scales,basis):
   if int(v[p])%scale:return v
   v=(v-(int(v[p])//scale)*row)%MOD
  return v
 def contains(v):return not np.any(reduce(v))
 assert all(contains(v) for v in vectors)
 return {'basis':basis,'C8_rank':counts[0],'C4_rank':counts[1],
         'C2_rank':counts[2],'log2_order':3*counts[0]+2*counts[1]+counts[2],
         'pivots':piv,'scales':scales,'contains':contains,'reduce':reduce}

def run():
 triples=[]
 for i in range(4):
  for j in range(i+1,4):
   for k in range(4):
    q,v=cm(cm(K[i],K[j]),K[k])
    assert q==0 and not np.any((C@v[nc]-v)%MOD)
    triples.append(v[nc])
 U=module_basis(triples);history=[]
 while True:
  history.append([U['C8_rank'],U['C4_rank'],U['C2_rank']])
  vectors=list(U['basis'])
  for a in M:vectors.extend((a@U['basis'].T%MOD).T)
  new=module_basis(vectors)
  if new['log2_order']==U['log2_order']:
   U=new;break
  U=new
 assert all(U['contains'](a@v%MOD) for a in M for v in U['basis'])
 gamma={3:U};data=[]
 for degree in range(3,10):
  if degree>3:
   prev=gamma[degree-1]['basis'];vectors=[]
   for a in M:vectors.extend(((a-eye)@prev.T%MOD).T)
   gamma[degree]=module_basis(vectors)
  V=gamma[degree]
  assert all(V['contains'](a@v%MOD) for a in M for v in V['basis'])
  row={'degree':degree,'C8_rank':V['C8_rank'],'C4_rank':V['C4_rank'],
       'C2_rank':V['C2_rank'],'log2_order':V['log2_order']}
  data.append(row);print('gamma',row,flush=True)
 
 # Actual lifts of every element in the class-two exponent-four base A0.
 identity=(0,np.zeros(size,dtype=np.int32))
 lifts={0:identity};queue=deque([0])
 while queue:
  h=queue.popleft()
  for a in K:
   z=mm(lifts[h],a)
   if z[0] not in lifts:lifts[z[0]]=z;queue.append(z[0])
 assert set(lifts)==A0
 actions={}
 def action_matrix(h):
  if h not in actions:actions[h]=act(C,h)[nc].astype(np.int32)%MOD
  return actions[h]
 def cycles(g):
  assert g[0]==0
  v=g[1][nc]%MOD
  assert not np.any((C@v-g[1])%MOD)
  return v
 
 # All sixteenth powers.  For g=v*h, the power is N16(h)v+h^16.
 # The base order is 1,2,4.  Only order4 contributes a nonzero norm
 # modulo8, namely 4(1+h+h^2+h^3) on the full coefficient module.
 powers16=[]
 base_orders={}
 for h,gh in lifts.items():
  hh=h;order=1
  while hh:
   hh=mul(hh,h);order+=1
  assert order in (1,2,4)
  base_orders[h]=order;powers16.append(cycles(powelt(gh,16)))
  if order==4:
   A=action_matrix(h);A2=A@A%MOD;A3=A2@A%MOD
   powers16.extend((4*(eye+A+A2+A3)%MOD).T)
 P16=module_basis(powers16)
 assert all(P16['contains'](a@v%MOD) for a in M for v in P16['basis'])
 
 # Compute the entire derived subgroup, including its intersection with V.
 # The derived base has order2.  Normal conjugates by all base lifts plus
 # conjugation by arbitrary V generate it exactly.
 commutators=[cm(K[i],K[j]) for i in range(4) for j in range(i+1,4)]
 derived_bases={0}
 todo=[0]
 for h in todo:
  for g in commutators:
   z=mul(h,g[0])
   if z not in derived_bases:derived_bases.add(z);todo.append(z)
 assert len(derived_bases)==2
 c0=next(g for g in commutators if g[0]!=0);hc=c0[0]
 assert derived_bases=={0,hc}
 Hvectors=[cycles(powelt(c0,2))]
 for lift in lifts.values():
  for g in commutators:
   z=mm(mm(lift,g),ii(lift))
   assert z[0] in (0,hc)
   if z[0]:z=mm(z,ii(c0))
   Hvectors.append(cycles(z))
 Mc=action_matrix(hc)
 Hvectors.extend((eye-Mc).T)
 Hmodule=module_basis(Hvectors)
 assert all(Hmodule['contains'](a@v%MOD) for a in M for v in Hmodule['basis'])
 for a in K:
  z=mm(mm(a,c0),ii(a));z=mm(z,ii(c0))
  assert Hmodule['contains'](cycles(z))
 assert all(Hmodule['contains'](Mc@v%MOD) for v in Hmodule['basis'])
 
 # For c=v*c0 in the derived coset, c^8=4(1+hc)v+c0^8.
 # Elements in the identity derived coset are coefficient vectors and
 # have eighth power zero.  This exhausts every element of gamma2(G).
 derived8=[cycles(powelt(c0,8))]
 derived8.extend((4*(eye+Mc)@Hmodule['basis'].T%MOD).T)
 P28=module_basis(derived8)
 assert all(P28['contains'](a@v%MOD) for a in M for v in P28['basis'])
 
 # The complete Zassenhaus product at9, including both genuine power terms.
 vectors=list(gamma[9]['basis'])+list(2*gamma[5]['basis']%MOD)
 vectors+=list(4*U['basis']%MOD)+list(P16['basis'])+list(P28['basis'])
 W=module_basis(vectors)
 assert all(W['contains'](a@v%MOD) for a in M for v in W['basis'])
 for h in (hs,hr):
  A=action_matrix(h)
  assert all(W['contains'](A@v%MOD) for v in W['basis'])
 W4old=json.loads((OLD/'d_cm_fermat_degree8_module.json').read_text())
 oldgens=np.array(W4old['D9_generators'],dtype=np.int32)
 def basis4(vectors):
  # Embed the Z/4 module as twice its vectors in Z/8.
  return module_basis(2*np.array(vectors,dtype=np.int32)%MOD)
 red4=basis4(W['basis']%4);old4=basis4(oldgens)
 assert red4['log2_order']==old4['log2_order']
 assert all(old4['contains'](2*v%MOD) for v in W['basis'])
 assert all(red4['contains'](2*v%MOD) for v in oldgens)
 def brief(A):
  return {k:A[k] for k in ('C8_rank','C4_rank','C2_rank','log2_order')}
 summary={'H4_order':size,'L4_rank':d,'K_over_L4_order':len(A0),
  'gamma3_normal_closure_history':history,'gamma_types':data,
  'G_sixteenth_powers':brief(P16),'derived_coefficient_subgroup':brief(Hmodule),
  'derived_eighth_powers':brief(P28),'D9_image':brief(W),
  'common_coefficient_quotient':{'C8_rank':d-len(W['basis']),
    'C4_rank':W['C2_rank'],'C2_rank':W['C4_rank'],
    'log2_order':3*d-W['log2_order']},
  'common_quotient_order':'2304 * 2^'+str(3*d-W['log2_order']),
  'kernel_to_previous_common_log2_order':3*d-W['log2_order']-403,
  'reduction_to_previous_D9_image_checked':True,
  'all_base_lifts_and_full_s_r_stability_checked':True,
  'exact_formula':'G^16 + gamma2(G)^8 + 4 gamma3(G) + 2 gamma5(G) + gamma9(G)',
  'scope':'Exact exponent-eight common quotient. No cusp lift or generation is yet asserted.',
  'elapsed_seconds':round(time.time()-started,3)}
 certificate={'summary':summary,'states':states.tolist(),'H12_to_H4':projection.tolist(),
  'cycle_chords':nc,'cycle_columns':[[[int(e),int(C[e,j])] for e in np.flatnonzero(C[:,j])] for j in range(d)],
  'K_base_elements':kg,'K_action_matrices':[a.tolist() for a in M],
  'D9_generators':W['basis'].tolist(),'D9_pivots':W['pivots'],'D9_scales':W['scales'],
  'G_sixteenth_power_generators':P16['basis'].tolist(),
  'derived_eighth_power_generators':P28['basis'].tolist(),
  'derived_coefficient_generators':Hmodule['basis'].tolist()}
 (OUT/'d_cm_fermat_homology_module.json').write_text(json.dumps(certificate,indent=2)+'\n')
 print(json.dumps(summary,indent=2),flush=True)
 return W

if __name__ == "__main__":
 W=run()
else:
 saved_module=json.loads((OUT/"d_cm_fermat_homology_module.json").read_text())
 W=module_basis(saved_module["D9_generators"])
 assert W["log2_order"]==745
