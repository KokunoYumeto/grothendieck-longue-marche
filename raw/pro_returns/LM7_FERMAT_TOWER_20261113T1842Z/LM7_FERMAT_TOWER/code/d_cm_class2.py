#!/usr/bin/env python3
"""Exact class-two exponent-three refinement of the D.25 CM shadows.

B=C2*C3 -> Q=SL2(Z/12)/+/-1, N free rank97.
The target is B/(Gamma_3(N) N^3), with central layer Lambda^2 F3^97.
All group words are evaluated by collapsing the Bass--Serre graph's tree.
The order32 normal subgroup of Q reduces the obstruction by exact averaging.
"""
from pathlib import Path
from collections import deque
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np

OUT=Path(__file__).resolve().parent
started=time.time()
with redirect_stdout(io.StringIO()):D=runpy.run_path(str(OUT/'d_cm_shadow.py'))
Q,ix,one,qs,qr=D['Q'],D['ix'],D['one'],D['qs'],D['qr']
qm,adj,root,v2,v3=D['qm'],D['adj'],D['root'],D['v2'],D['v3']
E=len(Q);d=97;p=3;inv2=2
qr2=qm(qr,qr)
paths={root:[]};queue=deque([root]);tree=set()
while queue:
 v=queue.popleft()
 for w,e in adj[v]:
  if w not in paths:
   paths[w]=paths[v]+[(e,1 if v[0]=='s' else -1)]
   tree.add(e);queue.append(w)
chords=[i for i in range(E) if i not in tree];chord={e:i for i,e in enumerate(chords)}
def inverse_path(path):return [(e,-sgn) for e,sgn in path[::-1]]
edge_cycles=[paths[v2[q]]+[(i,1)]+inverse_path(paths[v3[q]])
             for i,q in enumerate(Q) if i not in tree]
def edge_to_bword(path):
 assert len(path)%2==0
 q=one;word=[]
 for k in range(0,len(path),2):
  e,sgn=path[k];f,sgnf=path[k+1];assert sgn==1 and sgnf==-1
  a,b=Q[e],Q[f]
  if q!=a:assert qm(q,qs)==a;word.append(0);q=a
  if b==q:continue
  if qm(q,qr)==b:word.append(1)
  else:assert qm(q,qr2)==b;word.append(2)
  q=b
 if q!=one:assert q==qs;word.append(0);q=one
 return word
Nwords=[edge_to_bword(path) for path in edge_cycles]
def invert(word):return [0 if a==0 else 3-a for a in word[::-1]]
def evaluate(word):
 q=one;v=np.zeros(d,dtype=np.int16);z=np.zeros((d,d),dtype=np.int16)
 def append_edge(e,sgn):
  nonlocal v,z
  k=chord.get(e)
  if k is None:return
  # BCH(v,z)*(sgn e_k,0); z is stored as its skew matrix.
  add=inv2*sgn*v
  z[:,k]=(z[:,k]+add)%p;z[k,:]=(z[k,:]-add)%p
  v[k]=(v[k]+sgn)%p
 for letter in word:
  if letter==0:q=qm(q,qs)
  else:
   qq=qm(q,qr if letter==1 else qr2)
   append_edge(ix[q],1);append_edge(ix[qq],-1);q=qq
 return q,v,z
for i,w in enumerate(Nwords):
 q,v,z=evaluate(w);assert q==one and not np.any(z)
 assert np.array_equal(v,np.eye(d,dtype=np.int16)[i])

# Chord coordinates give integral C and the exact Q action.
C=np.zeros((E,d),dtype=np.int16)
for j,path in enumerate(edge_cycles):
 for e,sgn in path:C[e,j]+=sgn
assert np.array_equal(C[chords],np.eye(d,dtype=np.int16))
M={}
for q in Q:
 tmp=np.zeros_like(C);tmp[np.array(D['all_left'][ix[q]],dtype=int)]=C
 M[q]=tmp[chords]%p
assert np.array_equal(M[qs]@M[qs]%p,np.eye(d,dtype=np.int16))
assert np.array_equal(M[qr]@M[qr]@M[qr]%p,np.eye(d,dtype=np.int16))
# Fixed paths to representatives in Q are the same BFS as D.25.
reps={one:[]};queue=deque([one])
while queue:
 q=queue.popleft()
 for a,g in ((0,qs),(1,qr)):
  qq=qm(q,g)
  if qq not in reps:reps[qq]=reps[q]+[a];queue.append(qq)

O=[]
for q in D['H']:
 a=D['red'](D['flift'](q),3)
 aa=((a[0]*a[0]+a[1]*a[2])%3,(a[0]*a[1]+a[1]*a[3])%3,
     (a[2]*a[0]+a[3]*a[2])%3,(a[2]*a[1]+a[3]*a[3])%3)
 if aa in [(1,0,0,1),(2,0,0,2)]:O.append(q)
assert len(O)==32
Oset=set(O)
for q in O:
 for g in (qs,qr):
  gi=D['canon'](D['inv'](g));assert qm(qm(g,q),gi) in Oset

upper=np.triu_indices(d,1);zdim=len(upper[0]);assert zdim==4656
def vector(z):return np.array(z[upper]%p,dtype=np.int16)
def matrix(v):
 z=np.zeros((d,d),dtype=np.int16);z[upper]=v%p;z[(upper[1],upper[0])]=-v%p
 return z
def action(q,z):return ((M[q]@z)%p@M[q].T)%p
def average(z):
 total=np.zeros((d,d),dtype=np.int16)
 for q in O:total+=action(q,z)
 return (2*total)%p # 32^-1 = 2 in F3
def char(q):
 # Integral graph character: edges - vertices + connected components.
 fix2=sum(qm(q,a) in (a,qm(a,qs)) for a in Q)//2
 fix3=sum(qm(q,a) in (a,qm(a,qr),qm(a,qr2)) for a in Q)//3
 return (576 if q==one else 0)-fix2-fix3+1
charO={q:char(q) for q in O}
odim=sum((charO[q]**2-charO[qm(q,q)])//2 for q in O)//32
qchar={q:char(q) for q in Q}
qdim=sum((qchar[q]**2-qchar[qm(q,q)])//2 for q in Q)//576
print('Central dimension:',zdim,'; order32 invariant dimension:',odim,
      '; rational Q-coinvariant dimension:',qdim,flush=True)

# Build the image of the Reynolds operator without a 4656-square matrix.
bas={};basis=[]
for i in range(d):
 for j in range(i+1,d):
  z=np.zeros((d,d),dtype=np.int16)
  for q in O:
   a,b=M[q][:,i],M[q][:,j]
   z+=np.outer(a,b)-np.outer(b,a)
  v=vector(2*z)
  for pos in sorted(bas,reverse=True):v=(v-int(v[pos])*bas[pos])%p
  if np.any(v):
   pos=int(np.flatnonzero(v)[-1]);v=v*pow(int(v[pos]),-1,p)%p
   bas[pos]=v;basis.append(v)
  if len(basis)==odim:break
 if len(basis)==odim:break
assert len(basis)==odim
B=np.stack(basis,axis=1);pivots=sorted(bas,reverse=True)
def inverse_mod(A):
 n=A.shape[0];aug=np.concatenate([A.copy()%p,np.eye(n,dtype=np.int16)],axis=1)
 for j in range(n):
  k=next(k for k in range(j,n) if aug[k,j])
  aug[[j,k]]=aug[[k,j]];aug[j]=aug[j]*pow(int(aug[j,j]),-1,p)%p
  factors=aug[:,j].copy();factors[j]=0
  aug=(aug-factors[:,None]*aug[j])%p
 assert np.array_equal(aug[:,:n],np.eye(n,dtype=np.int16))
 return aug[:,n:]
coord=inverse_mod(B[pivots])
def coordinates(z):
 v=vector(z);c=coord@v[pivots]%p
 assert np.array_equal(B@c%p,v)
 return c
SB=np.stack([coordinates(action(qs,matrix(v))) for v in basis],axis=1)
RB=np.stack([coordinates(action(qr,matrix(v))) for v in basis],axis=1)
eye=np.eye(odim,dtype=np.int16)
L=np.concatenate([eye-SB,SB@(eye-RB)%p],axis=1)%p
def solver(A):
 bas={};null=[]
 for j,col in enumerate(A.T):
  v=col.copy();w=np.zeros(A.shape[1],dtype=np.int16);w[j]=1
  for pos in sorted(bas,reverse=True):
   a=int(v[pos]);bv,bw=bas[pos];v=(v-a*bv)%p;w=(w-a*bw)%p
  if np.any(v):
   pos=int(np.flatnonzero(v)[-1]);a=pow(int(v[pos]),-1,p)
   bas[pos]=(v*a%p,w*a%p)
  else:null.append(w)
 def solve(rhs):
  v=rhs.copy()%p;w=np.zeros(A.shape[1],dtype=np.int16)
  for pos in sorted(bas,reverse=True):
   a=int(v[pos]);bv,bw=bas[pos];v=(v-a*bv)%p;w=(w+a*bw)%p
  if not np.any(v):assert np.array_equal(A@w%p,rhs%p)
  return not np.any(v),w,v
 return solve,len(bas)
solve,rank=solver(L)
print('Reduced central correction matrix:',L.shape,'rank:',rank,
      'cokernel dimension:',odim-rank,flush=True)
def nullspace_mod(A):
 A=A.copy()%p;n,m=A.shape;row=0;piv=[]
 for col in range(m):
  hits=np.flatnonzero(A[row:,col])
  if not len(hits):continue
  k=row+int(hits[0]);A[[row,k]]=A[[k,row]]
  A[row]=A[row]*pow(int(A[row,col]),-1,p)%p
  factors=A[:,col].copy();factors[row]=0;A=(A-factors[:,None]*A[row])%p
  piv.append(col);row+=1
  if row==n:break
 ans=[]
 for j in range(m):
  if j in piv:continue
  v=np.zeros(m,dtype=np.int16);v[j]=1
  for k,col in enumerate(piv):v[col]=-A[k,j]%p
  ans.append(v)
 return ans
fixed_r=nullspace_mod(np.eye(d,dtype=np.int16)-M[qr])
r_defects=[]
for v in fixed_r:
 cw=[]
 for i,nw in enumerate(Nwords):cw+=nw*int(v[i])
 q,vv,z=evaluate(cw+[1]+invert(cw)+[2]);assert q==one and not np.any(vv)
 r_defects.append(z)
print('r-fixed vectors:',len(fixed_r),'for all lower-conjugator freedoms at3',flush=True)

def kernel_average_correction(z):
 # (1-P)z = (1-s)a+(1-r)b; telescoping each O-element word.
 a=np.zeros((d,d),dtype=np.int16);b=np.zeros_like(a)
 for g in O:
  suffix=one
  for letter in reps[g][::-1]:
   zz=action(suffix,z)
   if letter==0:a+=zz;suffix=qm(qs,suffix)
   else:b+=zz;suffix=qm(qr,suffix)
  assert suffix==g
 a=2*a%p;b=2*b%p
 assert np.array_equal((a-action(qs,a)+b-action(qr,b))%p,(z-average(z))%p)
 # Convert (1-r)b to s(1-r)b+(1-s)(1-r)b.
 return (a+b-action(qr,b))%p,b

records=[]
for row in D['records']:
 if not(row.get('finite_automorphism') and row.get('mod3_automorphism')):continue
 a=D['canon'](tuple(row['A']));b=D['canon'](tuple(row['beta']))
 wa=[];wb=[]
 for i,w in enumerate(Nwords):
  wa+=w*row['mod3_A_cycles'].get(str(i),0)
  wb+=w*row['mod3_beta_cycles'].get(str(i),0)
 wa+=reps[a];wb+=reps[b]
 cusp=wb+[0]+invert(wb)+wa+[1]+invert(wa)+[2,0]
 q,v,z=evaluate(cusp);assert q==one and not np.any(v)
 target=(-z)%p;proj=average(target);rhs=coordinates(proj)
 good,w,rem=solve(rhs)
 rec={'A':row['A'],'beta':row['beta'],'missing_coset':row['missing_coset'],
      'class2_lift':bool(good),'base_cusp_word_length':len(cusp),
      'reduced_defect':rhs.tolist(),'reduced_obstruction':rem.tolist()}
 if good:
  cb,ca=kernel_average_correction(target)
  cb=(cb+matrix(B@w[:odim]%p))%p;ca=(ca+matrix(B@w[odim:]%p))%p
  corrected=(cb-action(qs,cb)+action(qs,ca-action(qr,ca)))%p
  assert np.array_equal(corrected,target)
  rec['beta_central_coefficients']={str(i):int(x) for i,x in enumerate(vector(cb)) if x}
  rec['A_central_coefficients']={str(i):int(x) for i,x in enumerate(vector(ca)) if x}
  rec['full_4656_coordinate_equation_checked']=True
  rec['generation_certificate']='The rank97 mod3 abelianization from D25 is unchanged; Frattini of the exponent3 class2 free kernel is its commutator.'
 # Changes A -> A c with c centralizing r moduloNab/3 leave the same G3
 # action. Beta's order2 centralizer lifts automatically through3-groups.
 shifted=[action(qm(qs,a),z) for z in r_defects]
 additional=np.stack([coordinates(average(z)) for z in shifted],axis=1)
 augsolve,augrank=solver(np.concatenate([L,additional],axis=1))
 action_good,action_w,action_rem=augsolve(rhs)
 rec['same_G3_action_lifts']=bool(action_good)
 rec['rank_including_conjugator_freedom']=augrank
 rec['action_obstruction']=action_rem.tolist()
 if action_good:
  extra=sum((int(action_w[2*odim+i])*z for i,z in enumerate(shifted)),np.zeros((d,d),dtype=np.int16))%p
  target0=(target-extra)%p
  cb,ca=kernel_average_correction(target0)
  cb=(cb+matrix(B@action_w[:odim]%p))%p
  ca=(ca+matrix(B@action_w[odim:2*odim]%p))%p
  corrected=(cb-action(qs,cb)+action(qs,ca-action(qr,ca))+extra)%p
  assert np.array_equal(corrected,target)
  rec['action_lift_certificate']={
    'right_r_centralizer_coefficients':action_w[2*odim:].tolist(),
    'beta_central_coefficients':{str(i):int(x) for i,x in enumerate(vector(cb)) if x},
    'A_central_coefficients':{str(i):int(x) for i,x in enumerate(vector(ca)) if x},
    'full_4656_coordinate_equation_checked':True}
 records.append(rec)
 print('pair',len(records),'extra' if row['missing_coset'] else 'compatible',
       'LIFT' if good else 'OBSTRUCTED',
       'same-action lift' if action_good else 'same-action obstructed',flush=True)

summary={'prime':p,'Q_order':576,'N_rank':97,'central_dimension':zdim,
 'normal_prime_to_3_subgroup_order':32,'averaged_dimension':odim,
 'rational_Q_coinvariant_dimension':qdim,'reduced_matrix_shape':list(L.shape),
 'reduced_rank':rank,'central_obstruction_dimension_mod3':odim-rank,
 'tested_pairs':len(records),
 'compatible_lifts':sum(r['class2_lift'] and not r['missing_coset'] for r in records),
 'extra_CM_lifts':sum(r['class2_lift'] and r['missing_coset'] for r in records),
 'r_centralizer_fixed_dimension':len(fixed_r),
 'rank_with_conjugator_freedom':sorted(set(r['rank_including_conjugator_freedom'] for r in records)),
 'same_action_compatible_lifts':sum(r['same_G3_action_lifts'] and not r['missing_coset'] for r in records),
 'same_action_extra_lifts':sum(r['same_G3_action_lifts'] and r['missing_coset'] for r in records),
 'class2_quotient_order':'576 * 3^(97+4656)',
 'combined_quotient_order':'576 * 2^97 * 3^(97+4656)',
 'kernel_definition':'Gamma_3(N) N^3; combined with [N,N]N^2 by intersection',
 'scope':'Actual finite quotient shadows. A passed central equation plus existing mod3 rank97 proves automorphism; full profinite lift is not inferred.',
 'elapsed_seconds':round(time.time()-started,3)}
out={'summary':summary,'basis_pivots':pivots,
     'r_centralizer_basis':[v.tolist() for v in fixed_r],'pairs':records}
(OUT/'d_cm_class2.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
