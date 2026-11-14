#!/usr/bin/env python3
"""Solve the actual mixed quotient cusp equations with the exact D33 T3 images."""
from pathlib import Path
import json,time
import numpy as np
import d_cm_fermat_degree8_image as V

OUT=Path(__file__).resolve().parent;R=V.R;OLD=R.OLD;started=time.time()
D=R.D;states=np.array(D['states'],dtype=np.int16);size=len(states);d=len(D['cycle_chords'])
assert size==6912 and d==1153
nc=np.array(D['cycle_chords'],dtype=np.int32);qt=R.qt;LM=R.LM
hs,hr,ht=(D[k] for k in ['s','r','t']);grid=np.full((576,144),-1,dtype=np.int32)
for h,(q,a,b) in enumerate(states):grid[q,int(a)+12*int(b)]=h
def mul(a,b):
 q,u,v=states[a];qq,x,y=states[b];M=LM[q]
 return int(grid[qt[q,qq],int((u+M[0,0]*x+M[0,1]*y)%12)+12*int((v+M[1,0]*x+M[1,1]*y)%12)])
inverse=[]
for q,u,v in states:
 qq=R.qinv[q];M=LM[qq]
 inverse.append(int(grid[qq,int((-M[0,0]*u-M[0,1]*v)%12)+12*int((-M[1,0]*u-M[1,1]*v)%12)]))
inverse=np.array(inverse,dtype=np.int32);perms={}
def perm(h):
 if h not in perms:
  q,u,v=states[h];M=LM[q]
  aa=(u+states[:,1]*M[0,0]+states[:,2]*M[0,1])%12
  bb=(v+states[:,1]*M[1,0]+states[:,2]*M[1,1])%12
  perms[h]=grid[qt[q,states[:,0]],aa+12*bb]
 return perms[h]
def act(v,h):return v[perm(int(inverse[h]))]
C=np.zeros((size,d),dtype=np.int16)
for j,col in enumerate(D['integral_cycle_columns']):
 for e,v in col:C[e,j]=v
assert np.array_equal(C[nc],np.eye(d,dtype=np.int16))
def path(h):
 out=np.zeros(size,dtype=np.int16)
 while h:
  p,a=D['parent'][h]
  if a==1:out[p]+=1;out[h]-=1
  h=p
 return out
source37=json.loads((OLD/'d_cm_fermat_exponent4.json').read_text())
A=source37['summary']['A_H'];beta=source37['summary']['beta_H']
rec=next(r for r in D['candidate_conjugators'] if r['A_Q']==[1,0,0,1] and r['beta_Q']==[3,4,8,3])
base=next(v for v in rec['lifts'] if v['A']==A and v['beta']==beta)
ss,rr=base['s_image'],base['r_image'];PA=path(A);PB=path(beta);Pr=path(hr);Pt=act(Pr,hs)
E=PB-act(PB,ss)+act(PA-act(PA,rr)+act(Pr,A),ss)-Pt
assert np.array_equal(C@E[nc],E)
Mss=act(C,ss)[nc];Mt=act(C,ht)[nc]
F0=np.concatenate([np.eye(d,dtype=np.int16)-Mss,Mss-Mt],axis=1)
projectC=np.zeros((R.size,d),dtype=np.int16);np.add.at(projectC,R.projection,C)
S4=projectC[R.nc]
projectQ=np.zeros((576,d),dtype=np.int16);np.add.at(projectQ,states[:,0],C)
SQ=projectQ[V.chN]
def projection4(P):
 out=np.zeros(R.size,dtype=np.int32);np.add.at(out,R.projection,P);return out
def projectionQ(P):
 out=np.zeros(576,dtype=np.int32);np.add.at(out,states[:,0],P);return out
assert R.projection[A]==V.targetA[0] and R.projection[beta]==V.targetB[0]
rhsA=(V.targetA[1]-projection4(PA))[R.nc]%4
rhsB=(V.targetB[1]-projection4(PB))[R.nc]%4
W=R.W['basis'].T;w=W.shape[1];assert w==316
oldG6=json.loads((OLD/'d_cm_fermat_mixed_compatible.json').read_text())
targetA2=np.array(oldG6['target_A_G2_path'],dtype=np.int16)
targetB2=np.array(oldG6['target_beta_G2_path'],dtype=np.int16)
rhsA2=(targetA2-projectionQ(PA))[V.chN]%2
rhsB2=(targetB2-projectionQ(PB))[V.chN]%2
variables=2*d+2*w;rows=d+2*R.d+194
F=np.zeros((rows,variables),dtype=np.uint8);rhs=np.zeros(rows,dtype=np.uint8)
F[:d,:2*d]=F0%4;rhs[:d]=-E[nc]%4
p=d
F[p:p+R.d,:d]=S4%4;F[p:p+R.d,2*d:2*d+w]=-W%4;rhs[p:p+R.d]=rhsB;p+=R.d
F[p:p+R.d,d:2*d]=S4%4;F[p:p+R.d,2*d+w:]=-W%4;rhs[p:p+R.d]=rhsA;p+=R.d
F[p:p+97,:d]=2*SQ%4;rhs[p:p+97]=2*rhsB2;p+=97
F[p:p+97,d:2*d]=2*SQ%4;rhs[p:p+97]=2*rhsA2;p+=97
assert p==rows and F.shape==(2117,2938)

def affine2(A,b):
 basis={}
 for row,c in zip(np.packbits(A%2,axis=1,bitorder='little'),b):
  v=int.from_bytes(row.tobytes(),'little');c=int(c)
  while v:
   j=v.bit_length()-1
   if j not in basis:basis[j]=(v,c);break
   vv,cc=basis[j];v^=vv;c^=cc
  if not v and c:return None,len(basis)
 piv=sorted(basis);free=[j for j in range(A.shape[1]) if j not in basis]
 mask=sum(1<<j for j in free)
 def solve(rng):
  v=int.from_bytes(rng.bytes((A.shape[1]+7)//8),'little')&mask
  for j in piv:
   vv,c=basis[j]
   if ((vv&v).bit_count()&1)^c:v^=1<<j
  return np.array([(v>>j)&1 for j in range(A.shape[1])],dtype=np.uint8)
 return solve,len(basis)
def affine4(A,b):
 A=np.column_stack([A,b]).copy()&3;r=0;piv=[];nr,nc=A.shape
 for j in range(nc-1):
  hits=np.flatnonzero(A[r:,j]&1)
  if not len(hits):continue
  k=r+int(hits[0]);A[[r,k]]=A[[k,r]]
  if A[r,j]==3:A[r]=(3*A[r])&3
  factors=A[r+1:,j].copy();A[r+1:]=(A[r+1:]-factors[:,None]*A[r])&3
  piv.append(j);r+=1
  if r%256==0:print('unit pivots',r,'elapsed',round(time.time()-started,2),flush=True)
  if r==nr:break
 assert not np.any(A[r:,:-1]&1)
 if np.any(A[r:,-1]&1):return None,{'unit_rank':r,'inconsistent_even_row':True}
 free=[j for j in range(nc-1) if j not in piv]
 B=(A[r:,free]//2).astype(np.uint8);b=(A[r:,-1]//2).astype(np.uint8)
 solve2,rank2=affine2(B,b)
 if solve2 is None:return None,{'unit_rank':r,'even_rank':rank2,'inconsistent_even_row':False,'inconsistent_binary_system':True}
 def solve(rng):
  x=np.zeros(nc-1,dtype=np.uint8)
  x[free]=solve2(rng)+2*rng.integers(0,2,len(free),dtype=np.uint8)
  for k in range(r-1,-1,-1):x[piv[k]]=(int(A[k,-1])-int(A[k,:-1]@x))%4
  return x
 return solve,{'unit_rank':r,'even_rank':rank2,'solution_C4_parameters':len(free)-rank2,
               'solution_C2_parameters':rank2,'solution_log2_size':2*len(free)-rank2}
solver,algebra=affine4(F,rhs)
print('common constrained Z4 system',json.dumps(algebra),flush=True)
if solver is None:
 result={'summary':{'matrix_shape':list(F.shape),'solvable':False,'algebra':algebra,
  'scope':'The exact recorded conjugators only; no complete same-action centralizer exhaustion is inferred.',
  'elapsed_seconds':round(time.time()-started,3)}}
 (OUT/'d_cm_fermat_degree8_joint.json').write_text(json.dumps(result,indent=2)+'\n')
 raise AssertionError('Exact fixed-conjugator common system is inconsistent.')

coc={tuple(map(int,k.split(','))):v for k,v in base['linear_S3_cocycle'].items()}
alpha=[]
for q,u,v in states:
 du,dv=coc[tuple(LM[q].ravel())];alpha.append(int(grid[q,int((u+du)%12)+12*int((v+dv)%12)]))
assert len(set(alpha))==size
indices=np.empty((d,size),dtype=np.int32);st=states[nc]
for h in range(size):
 q,u,v=states[int(inverse[alpha[h]])];M=LM[q]
 aa=(u+st[:,1]*M[0,0]+st[:,2]*M[0,1])%12
 bb=(v+st[:,1]*M[1,0]+st[:,2]*M[1,1])%12
 indices[:,h]=grid[qt[q,st[:,0]],aa+12*bb]
cols=[(np.array([e for e,v in col],dtype=np.int32),np.array([v for e,v in col],dtype=np.int16)) for col in D['integral_cycle_columns']]
def kernel_matrix(edge,mod):
 transported=edge[indices]%mod;T=np.empty((d,d),dtype=np.int16)
 for j,(edges,values) in enumerate(cols):T[:,j]=transported[:,edges]@values%mod
 return T
def rank2(A):
 basis={}
 for row in np.packbits(A%2,axis=1,bitorder='little'):
  v=int.from_bytes(row.tobytes(),'little')
  while v:
   j=v.bit_length()-1
   if j not in basis:basis[j]=v;break
   v^=basis[j]
 return len(basis)
rng=np.random.default_rng(38092026);trials=[];edge0=PA-PB;edge0[A]+=1
for trial in range(1,257):
 z=solver(rng);assert not np.any((F@z-rhs)&3)
 b4=z[:d].astype(np.int16);a4=z[d:2*d].astype(np.int16)
 T2=kernel_matrix((edge0+C@(a4-b4))%2,2);rank=rank2(T2);trials.append(rank)
 print('generation trial',trial,'rank',rank,flush=True)
 if rank==d:break
assert trials[-1]==d
a3=np.array(source37['a_mod12'],dtype=np.int16)%3
b3=np.array(source37['beta_correction_mod12'],dtype=np.int16)%3
a12=(9*a4+4*a3)%12;b12=(9*b4+4*b3)%12
PA12=PA+C@a12;PB12=PB+C@b12
defect=PB12-act(PB12,ss)+act(PA12-act(PA12,rr)+act(Pr,A),ss)-Pt
assert not np.any(defect%12)
diffA=(projection4(PA12)-V.targetA[1])[R.nc]%4
diffB=(projection4(PB12)-V.targetB[1])[R.nc]%4
assert R.W['contains'](diffA) and R.W['contains'](diffB)
assert not np.any((S4@a4-W@z[2*d+w:]-rhsA)%4)
assert not np.any((S4@b4-W@z[2*d:2*d+w]-rhsB)%4)
assert not np.any((projectionQ(PA12)-targetA2)%2)
assert not np.any((projectionQ(PB12)-targetB2)%2)

basiswords=json.loads((OLD/'d_cm_fermat_mixed_generate.json').read_text())['basis_words']
def invword(w):return [0 if a==0 else 3-a for a in reversed(w)]
def base_word(h):
 w=[]
 while h:h,a=D['parent'][h];w.append(a)
 return list(reversed(w))
def correction_word(coeff):
 out=[]
 for v,w in zip(coeff,basiswords):
  v=int(v)
  if v>6:v-=12
  block=w if v>=0 else invword(w)
  for i in range(abs(v)):out.extend(block)
 return out
Aw=correction_word(a12)+base_word(A);Bw=correction_word(b12)+base_word(beta)
rs=np.array(D['right_s'],dtype=np.int32);rtrans=np.array(D['right_r'],dtype=np.int32);rtrans2=rtrans[rtrans]
def model(w):
 h=0;P=np.zeros(size,dtype=np.int32)
 for a in w:
  if a==0:h=int(rs[h])
  else:
   k=int(rtrans[h] if a==1 else rtrans2[h]);P[h]+=1;P[k]-=1;h=k
 return h,P
cusp=Bw+[0]+invword(Bw)+Aw+[1]+invword(Aw)+[2,0]
q,P=model(cusp);assert q==0 and not np.any(P%12)
print('full mixed cusp word checked',len(cusp),'letters',flush=True)
gen=[model(Bw+[0]+invword(Bw)),model(Aw+[1]+invword(Aw))]
assert [q for q,p in gen]==[ss,rr]
gen.append((int(inverse[rr]),-act(gen[1][1],int(inverse[rr]))))
check=np.zeros((d,d),dtype=np.int16)
for j,w in enumerate(basiswords):
 q=0;P=np.zeros(size,dtype=np.int32)
 for a in w:
  h,v=gen[a];P+=act(v,q);q=mul(q,h)
 assert q==0;check[:,j]=P[nc]%12
T4=kernel_matrix((edge0+C@(a4-b4))%4,4);T3=kernel_matrix((edge0+C@(a3-b3))%3,3)
assert np.array_equal(check%4,T4) and np.array_equal(check%3,T3)
assert rank2(T4)==d
# T3 is literally the previously verified generating mod-three matrix.
oldT3=kernel_matrix((edge0+C@((np.array(source37['a_mod12'])%3)-(np.array(source37['beta_correction_mod12'])%3)))%3,3)
assert np.array_equal(T3,oldT3)

def affine(w):
 M=np.eye(2,dtype=np.int64);v=np.zeros(2,dtype=np.int64)
 LS=np.array([[0,1],[1,0]],dtype=np.int64);LR=np.array([[0,-1],[1,-1]],dtype=np.int64)
 for a in w:
  if a==0:M=M@LS
  elif a==1:v+=M[:,0];M=M@LR
  else:v+=M[:,0]+M[:,1];M=M@(LR@LR)
 return M,v
MM,bab=affine(Bw);assert np.array_equal(MM,np.eye(2,dtype=np.int64))
k=int(bab[1]-bab[0]);assert k%6==0
def mm(a,b):return mul(a[0],b[0]),(a[1]+act(b[1],a[0]))%12
def ii(a):
 h=int(inverse[a[0]]);return h,-act(a[1],h)%12
def conjugate(a,b):return mm(mm(a,b),ii(a))
def eq(a,b):return a[0]==b[0] and not np.any((a[1]-b[1])%12)
identity=(0,np.zeros(size,dtype=np.int16))
X=model([2,0,2,0])
def power(a,n):
 out=identity
 while n:
  if n&1:out=mm(out,a)
  a=mm(a,a);n//=2
 return out
assert eq(power(X,144),identity)
S=(hs,np.zeros(size,dtype=np.int16));RR=(hr,Pr)
newX=power(X,k%144);newA=(A,PA12%12);newB=(beta,PB12%12)
newBp=mm(newX,newB);FF=mm(mm(mm(S,newBp),S),ii(newBp))
U=ii(mm(S,RR));VV=mm(mm(S,U),S)
assert eq(mm(mm(mm(U,ii(FF)),VV),FF),mm(ii(FF),mm(U,VV)))
assert eq(mm(mm(mm(ii(FF),VV),FF),U),mm(mm(VV,U),FF))
assert eq(mm(FF,conjugate(S,FF)),identity)
oldPA=PA+C@np.array(source37['a_mod12'],dtype=np.int16)
oldPB=PB+C@np.array(source37['beta_correction_mod12'],dtype=np.int16)
oldX=power(X,source37['summary']['Ihara_gauge_exponent']%144)
newS=conjugate(newX,conjugate(newB,S));newR=conjugate(newX,conjugate(newA,RR))
oldS=conjugate(oldX,conjugate((beta,oldPB%12),S))
oldR=conjugate(oldX,conjugate((A,oldPA%12),RR))
comparison={}
for name,new,old in [('s',newS,oldS),('r',newR,oldR)]:
 assert new[0]==old[0]
 delta=(new[1]-old[1])%12
 assert not np.any(delta%3)
 assert not np.any(projectionQ(delta)%6)
 comparison[name]={'different_mod12':bool(np.any(delta)),
  'different_mod2':bool(np.any(delta%2)),'support_mod12':int(np.count_nonzero(delta)),
  'same_normalized_G6_image':True,'same_normalized_J3_image':True}
assert any(v['different_mod12'] for v in comparison.values())
mu={1:1,2:-1,3:-1,4:0,5:-1,6:1,7:-1,8:0}
def witt(n):return sum(mu[a]*4**(n//a) for a in range(1,n+1) if n%a==0)//n
restricted=[]
for degree in range(1,9):
 total=0;v=degree
 while True:
  total+=witt(v)
  if v%2:break
  v//=2
 restricted.append(total)
assert restricted==[4,10,20,70,204,690,2340,8230] and sum(restricted)==11568
assert sum(restricted)-(7+403)==11158
# An explicit nonzero element of the exact remaining source kernel.
# K is marked by the four actual words retained in D33; each twelfth power
# has trivial image in H12 because its K-image has exponent dividing12.
ell1=list(V.Kwords[0])*12;ell2=list(V.Kwords[1])*12
assert model(ell1)[0]==model(ell2)[0]==0
kernelword=(ell1+ell2+invword(ell1)+invword(ell2))*2
q,p=model(kernelword);assert q==0 and not np.any(p%12)
q,kw=V.collapse(kernelword)
assert q==V.e and kw==([1]*12+[2]*12+[-1]*12+[-2]*12)*2
# The Magnus leading term of a_i^12 is X_i^4.  The commutator has leading
# term X1^4 X2^4 + X2^4 X1^4, whose square has four distinct degree16 words.
u=(0,)*4+(1,)*4;v=(1,)*4+(0,)*4
leading16=[a+b for a in (u,v) for b in (u,v)]
assert len(set(leading16))==4 and all(len(a)==16 for a in leading16)
summary={'common_quotient_order':'2304 * 2^403','constrained_matrix_shape':list(F.shape),
 'algebra':algebra,'generation_ranks_mod2_trials':trials,'kernel_generation_ranks':{'2':d,'3':d},
 'literal_cusp_word_length':len(cusp),'all6912_coordinates_checked':True,'all1153_basis_images_checked':True,
 'exact_D33_T3_conjugator_images_matched':True,'exact_D33_G6_conjugators_retained':True,
 'previous_J12_action_replaced':True,'retains_previous_J3_action':True,
 'beta_integral_F_abelianization':bab.tolist(),'Ihara_gauge_exponent':k,
 'both_m0_hexagons_checked':True,'normalized_representative_comparison':comparison,
 'joint_finite_quotient':'J12 fiber product over C with T3=B/D9K',
 'joint_finite_quotient_order':'54 * 12^1153 * 2^11165',
 'T3_restricted_dimensions':restricted,'T3_K_log2_order':sum(restricted),
 'kernel_joint_to_J12_order':'2^11158','kernel_joint_to_T3_order':'2^1903 * 3^1154',
 'remaining_source_kernel':'([L,L] L^12) intersect D9(K)',
 'nonzero_remaining_kernel_word':'[a1^12,a2^12]^2',
 'remaining_kernel_word_B_length':len(kernelword),'remaining_kernel_Magnus_leading_degree':16,
 'scope':'Actual generating component and exact common conjugator equality. The full relative source beyond this finite joint quotient remains unresolved.',
 'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,'a_mod12':a12.tolist(),'beta_correction_mod12':b12.tolist(),
 'A_word':Aw,'beta_word':Bw,'A_common_W_coefficients':z[2*d+W.shape[1]:].tolist(),
 'beta_common_W_coefficients':z[2*d:2*d+W.shape[1]].tolist(),
 'A_common_difference':diffA.tolist(),'beta_common_difference':diffB.tolist(),
 'remaining_kernel_Magnus_leading_monomials':leading16}
(OUT/'d_cm_fermat_degree8_joint.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
