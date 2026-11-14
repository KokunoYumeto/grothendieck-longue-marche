#!/usr/bin/env python3
"""Retain the exact D33 G6 conjugators in the Fermat12 mixed homology cover."""
from pathlib import Path
from collections import deque
import json,time
import numpy as np
import d_cm_fermat_mixed_generate as g

started=time.time();OUT=Path(__file__).resolve().parent
OLD=OUT if (OUT/'d_cm_elliptic_pair.json').exists() else OUT.parent.parent/'LM7_FERMAT_TOWER'/'code'
m=g.m;n=g.n;C=g.C;nc=g.nc;size=g.size;D=m.D
Q=m.Q;qt=m.qt;qi=m.qi;qs=int(m.states[m.hs,0]);qr=int(m.states[m.hr,0])
qright_s=qt[:,qs];qright_r=qt[:,qr];qright_r2=qright_r[qright_r]
v2=[(0,min(i,int(qright_s[i]))) for i in range(576)]
v3=[(1,min(i,int(qright_r[i]),int(qright_r2[i]))) for i in range(576)]
vertices=sorted(set(v2)|set(v3));vi={v:i for i,v in enumerate(vertices)}
adj=[[] for v in vertices]
for i in range(576):
 a,b=vi[v2[i]],vi[v3[i]];adj[a].append((b,i,1));adj[b].append((a,i,-1))
paths={vi[v2[qi]]:[]};queue=deque(paths);tree=set()
while queue:
 a=queue.popleft()
 for b,e,sgn in adj[a]:
  if b not in paths:paths[b]=paths[a]+[(e,sgn)];tree.add(e);queue.append(b)
qchords=[i for i in range(576) if i not in tree]
assert len(qchords)==97
CQ=np.zeros((576,97),dtype=np.int16)
for j,e in enumerate(qchords):
 for i,sgn in paths[vi[v2[e]]]+[(e,1)]+[(i,-sgn) for i,sgn in paths[vi[v3[e]]]]:CQ[i,j]+=sgn
assert np.array_equal(CQ[qchords],np.eye(97,dtype=np.int16))
def qact(v,q):return v[qt[int(m.qinv[q])]]
qP={qi:np.zeros(576,dtype=np.int16)};qreps={qi:[]};queue=deque([qi])
pr=np.zeros(576,dtype=np.int16);pr[qi]=1;pr[qr]=-1
while queue:
 a=queue.popleft()
 for letter,h,ph in [(0,qs,np.zeros(576,dtype=np.int16)),(1,qr,pr)]:
  b=int(qt[a,h])
  if b not in qP:qP[b]=qP[a]+qact(ph,a);qreps[b]=qreps[a]+[letter];queue.append(b)
assert len(qP)==576
projectedC=np.zeros((576,n),dtype=np.int16)
np.add.at(projectedC,m.states[:,0],C)
S=projectedC[qchords]
assert np.array_equal(CQ@S,projectedC)
assert g.rank2(S)==95

J=json.loads((OLD/'d_cm_quadratic_search.json').read_text())['witness']
fixed=json.loads((OLD/'d_cm_class2_two.json').read_text())['s_centralizer_basis']
def maskvec(mask):return np.array([(mask>>i)&1 for i in range(97)],dtype=np.int16)
b=maskvec(int(J['homology_beta_cycles'],16));a=maskvec(int(J['homology_A_cycles'],16))
right=int(J['beta_right_s_centralizer_coefficients'],16);rightmask=0
for j,v in enumerate(fixed):
 if (right>>j)&1:rightmask^=int(v,16)
qb=m.ix[(3,4,8,3)]
targetA2=CQ@a
targetB2=qP[qb]+CQ@b+qact(CQ@maskvec(rightmask),qb)
# All D29--D33 corrections are in Phi(N); these are therefore the exact G2
# conjugators of the independently audited D33 representative.
assert not np.any((targetB2-qact(targetB2,qs)+qact(targetA2-qact(targetA2,qr),qs))%2)
oldrow=next(r for r in json.loads((OLD/'d_cm_shadow.json').read_text())['pairs']
            if r['A']==[1,0,0,1] and r['beta']==[9,8,4,9])
b3old=np.zeros(97,dtype=np.int16)
for j,v in oldrow['mod3_beta_cycles'].items():b3old[int(j)]=v
assert oldrow['mod3_A_cycles']=={}
targetB3=qP[qb]+CQ@b3old
assert not np.any((targetB3-qact(targetB3,qs))%3)

Z=np.zeros_like(S)
constraints=np.concatenate([np.concatenate([S,Z],axis=1),np.concatenate([Z,S],axis=1)],axis=0)
def projection(P):
 q=np.zeros(576,dtype=np.int32);np.add.at(q,m.states[:,0],P);return q
base_records=[];selected=None
for base in g.rec['lifts']:
 A=base['A'];beta=base['beta']
 ss=base['s_image'];rr=base['r_image']
 PA=m.path(A);PB=m.path(beta)
 E=PB-m.act(PB,ss)+m.act(PA-m.act(PA,rr)+m.act(m.path(m.hr),A),ss)-m.Pt
 Mss=m.act(C,ss)[nc]
 Fbase=np.concatenate([np.eye(n,dtype=np.int16)-Mss,Mss-g.Mt],axis=1)
 F=np.concatenate([Fbase,constraints],axis=0)%2
 rhs=np.concatenate([E[nc],(targetB2-projection(PB))[qchords],(targetA2-projection(PA))[qchords]])%2
 try:solver,rr,dd=g.affine2(F,rhs)
 except AssertionError:
  base_records.append({'A_H':A,'beta_H':beta,'exact_G2_conjugators_possible':False});continue
 base_records.append({'A_H':A,'beta_H':beta,'exact_G2_conjugators_possible':True,'rank':rr,'dimension':dd})
 if selected is None:selected=(base,solver,rr,dd,rhs,Fbase,F)
print('exact G2-compatible base choices',json.dumps(base_records),flush=True)
assert selected is not None
base,solver,crank,dim,rhs,Fbase,F=selected
A=base['A'];beta=base['beta'];PA=m.path(A);PB=m.path(beta)
ss=base['s_image'];rr=base['r_image']
# Transport by the actual (possibly nonidentity) affine base automorphism.
coc={tuple(map(int,k.split(','))):v for k,v in base['linear_S3_cocycle'].items()}
alpha=[]
for q,u,v in m.states:
 du,dv=coc[tuple(m.LM[q].ravel())]
 alpha.append(int(m.grid[q,int((u+du)%12)+12*int((v+dv)%12)]))
assert len(set(alpha))==size
st=m.states[nc]
for h in range(size):
 q,u,v=m.states[int(m.inverse[alpha[h]])];M=m.LM[q]
 aa=(u+st[:,1]*M[0,0]+st[:,2]*M[0,1])%12
 bb=(v+st[:,1]*M[1,0]+st[:,2]*M[1,1])%12
 g.indices[:,h]=m.grid[m.qt[q,st[:,0]],aa+12*bb]
rng=np.random.default_rng(37033026);ranks=[]
edge0=PA-PB;edge0[A]+=1
for trial in range(1,257):
 z=solver(rng);assert not np.any((F@z-rhs)%2)
 b2,a2=z[:n],z[n:]
 edge=(edge0+C@(a2-b2))%2;T2=g.kernel_matrix(edge,2)
 r=g.rank2(T2);ranks.append(r);print('compatible trial',trial,'kernel rank',r,flush=True)
 if r==n:break
assert ranks[-1]==n

def affine3(A,b):
 A=np.column_stack([A%3,b%3]);r=0;piv=[];nrows,ncols=A.shape
 for j in range(ncols-1):
  hits=np.flatnonzero(A[r:,j])
  if not len(hits):continue
  k=r+int(hits[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*int(A[r,j])%3
  f=A[r+1:,j].copy();A[r+1:]=(A[r+1:]-f[:,None]*A[r])%3
  piv.append(j);r+=1
  if r==nrows:break
 assert not np.any(A[r:,-1])
 free=[j for j in range(ncols-1) if j not in piv]
 def solve(rng):
  x=np.zeros(ncols-1,dtype=np.int16);x[free]=rng.integers(0,3,len(free),dtype=np.int16)
  for k in range(r-1,-1,-1):x[piv[k]]=(int(A[k,-1])-int(A[k,:-1]@x))%3
  return x
 return solve,r,len(free)
def rank3(A):
 A=A.copy()%3;r=0
 for j in range(A.shape[1]):
  hits=np.flatnonzero(A[r:,j])
  if not len(hits):continue
  k=r+int(hits[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*int(A[r,j])%3
  fac=A[r+1:,j].copy();A[r+1:]=(A[r+1:]-fac[:,None]*A[r])%3;r+=1
  if r==A.shape[0]:break
 return r
E=PB-m.act(PB,ss)+m.act(PA-m.act(PA,rr)+m.act(m.path(m.hr),A),ss)-m.Pt
F3=np.concatenate([Fbase,constraints],axis=0)%3
rhs3=np.concatenate([-E[nc],(targetB3-projection(PB))[qchords],(-projection(PA))[qchords]])%3
solver3,crank3,dim3=affine3(F3,rhs3)
ranks3=[]
for trial3 in range(1,129):
 z=solver3(rng);b3,a3=z[:n],z[n:];assert not np.any((F3@z-rhs3)%3)
 T3=g.kernel_matrix((edge0+C@(a3-b3))%3,3);rk=rank3(T3);ranks3.append(rk)
 print('compatible mod3 trial',trial3,'kernel rank',rk,flush=True)
 if rk==n:break
assert ranks3[-1]==n

a6=(3*a2+4*a3)%6;b6=(3*b2+4*b3)%6
PA6=PA+C@a6;PB6=PB+C@b6
assert not np.any((projection(PA6)-targetA2)%2)
assert not np.any((projection(PB6)-targetB2)%2)
assert not np.any(projection(PA6)%3)
assert not np.any((projection(PB6)-targetB3)%3)
Aw=g.correction_word(a6)+g.base_word(A);Bw=g.correction_word(b6)+g.base_word(beta)
cusp=Bw+[0]+g.inverse_word(Bw)+Aw+[1]+g.inverse_word(Aw)+[2,0]
q,P=g.model(cusp);assert q==0 and not np.any(P%6)
gen=[g.model(Bw+[0]+g.inverse_word(Bw)),g.model(Aw+[1]+g.inverse_word(Aw))]
assert [q for q,P in gen]==[ss,rr]
gen.append((int(m.inverse[rr]),-m.act(gen[1][1],int(m.inverse[rr]))))
check=np.zeros((n,n),dtype=np.int16)
for j,w in enumerate(g.basiswords):
 q=0;P=np.zeros(size,dtype=np.int32)
 for letter in w:
  h,v=gen[letter];P+=m.act(v,q);q=m.mul(q,h)
 assert q==0;check[:,j]=P[nc]%6
assert np.array_equal(check%2,T2) and np.array_equal(check%3,T3)

summary={'base_order':size,'free_kernel_rank':n,'A_H':A,'beta_H':beta,
 'extra_CM_coset':True,'multiplier':1,'exact_D33_G6_conjugators_retained':True,
 'mod2_correction_rank':crank,'mod2_affine_dimension':dim,
 'mod3_correction_rank':crank3,'mod3_affine_dimension':dim3,
 'generation_ranks_mod2_trials':ranks,'generation_ranks_mod3_trials':ranks3,
 'kernel_generation_ranks':{'2':n,'3':n},
 'literal_cusp_word_length':len(cusp),'all_6912_coordinates_checked':True,
 'all_1153_basis_images_independently_checked':True,
 'scope':'Actual J6 automorphism retaining the exact G6 conjugators of D33. Agreement on the larger D33 quotient is not asserted.',
 'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,'base_choice_tests':base_records,
 'a_mod6':a6.tolist(),'beta_correction_mod6':b6.tolist(),
 'A_word':Aw,'beta_word':Bw,
 'target_A_G2_path':targetA2.tolist(),'target_beta_G2_path':targetB2.tolist(),
 'target_beta_G3_path':targetB3.tolist()}
(OUT/'d_cm_fermat_mixed_compatible.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
