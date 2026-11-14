#!/usr/bin/env python3
"""Solve the actual mixed quotient cusp equations with the exact D33 T3 images."""
from pathlib import Path
import json,time
import numpy as np
import d_cm_fermat_homology_image as V

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
rhsA=(V.targetA[1]-projection4(PA))[R.nc]%8
rhsB=(V.targetB[1]-projection4(PB))[R.nc]%8
W8=R.W['basis'].T;assert W8.shape[1]==378
oldG6=json.loads((OLD/'d_cm_fermat_mixed_compatible.json').read_text())
targetA2=np.array(oldG6['target_A_G2_path'],dtype=np.int16)
targetB2=np.array(oldG6['target_beta_G2_path'],dtype=np.int16)
rhsA2=(targetA2-projectionQ(PA))[V.chN]%2
rhsB2=(targetB2-projectionQ(PB))[V.chN]%2

# GENERATION_HELPERS
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

# The exact inverse image of W8 in Z2^385 has this integral lattice basis.
# Its pivot columns are triangular; seven free columns carry 8 times a unit.
freeW=[j for j in range(R.d) if j not in R.W['pivots']]
assert len(freeW)==7
lattice_rows=np.concatenate([R.W['basis'],8*np.eye(R.d,dtype=np.int32)[freeW]],axis=0)
column_order=R.W['pivots']+freeW
tri=lattice_rows[:,column_order]
assert not np.any(np.tril(tri,-1))
assert list(np.diag(tri))==R.W['scales']+[8]*7
assert sum(int(v).bit_length()-1 for v in np.diag(tri))==410
Z=lattice_rows.T

PRECISION=8;MODULUS=2**PRECISION
variables=2*d+2*R.d+194;rows=d+2*R.d+194
F_exact=np.zeros((rows,variables),dtype=np.int32);rhs_exact=np.zeros(rows,dtype=np.int32)
F_exact[:d,:2*d]=F0;rhs_exact[:d]=-E[nc]
p=d
F_exact[p:p+R.d,:d]=S4
F_exact[p:p+R.d,2*d:2*d+R.d]=-Z
rhs_exact[p:p+R.d]=rhsB;p+=R.d
F_exact[p:p+R.d,d:2*d]=S4
F_exact[p:p+R.d,2*d+R.d:2*d+2*R.d]=-Z
rhs_exact[p:p+R.d]=rhsA;p+=R.d
F_exact[p:p+97,:d]=SQ
F_exact[p:p+97,2*d+2*R.d:2*d+2*R.d+97]=-2*np.eye(97,dtype=np.int16)
rhs_exact[p:p+97]=rhsB2;p+=97
F_exact[p:p+97,d:2*d]=SQ
F_exact[p:p+97,2*d+2*R.d+97:]=-2*np.eye(97,dtype=np.int16)
rhs_exact[p:p+97]=rhsA2;p+=97
F=(F_exact%MODULUS).astype(np.uint8);rhs=(rhs_exact%MODULUS).astype(np.uint8)
assert p==rows and F.shape==(2117,3270)

def affine_dvr(coeff,rhs):
 """DVR row elimination at precision256, retaining every integral pivot."""
 A=np.column_stack([coeff,rhs]).copy().astype(np.uint8)
 nr,nc=A.shape;r=0;piv=[];scales=[];counts=[0]*PRECISION
 for valuation in range(PRECISION):
  scale=2**valuation
  assert not np.any(A[r:,:-1]%scale)
  if np.any(A[r:,-1]%scale):
   return None,{'consistent':False,'first_failed_valuation':valuation,
     'pivot_counts':counts,'rank':r}
  for j in range(nc-1):
   hits=np.flatnonzero((A[r:,j]//scale)%2)
   if not len(hits):continue
   k=r+int(hits[0]);A[[r,k]]=A[[k,r]]
   inv=pow(int(A[r,j]//scale),-1,MODULUS)
   A[r]=(A[r]*inv).astype(np.uint8)
   assert A[r,j]==scale
   factors=A[r+1:,j]//scale
   A[r+1:]=(A[r+1:]-factors[:,None]*A[r]).astype(np.uint8)
   piv.append(j);scales.append(scale);counts[valuation]+=1;r+=1
   if r==nr:break
  print('DVR valuation',valuation,'rank',r,'elapsed',round(time.time()-started,3),flush=True)
  if r==nr:break
 assert not np.any(A[r:,:-1])
 if np.any(A[r:,-1]):
  return None,{'consistent':False,'first_failed_valuation':PRECISION,
    'pivot_counts':counts,'rank':r}
 assert r==nr,'Precision did not determine all integral invariant factors.'
 free=[j for j in range(nc-1) if j not in piv]
 def solve(rng=None):
  x=np.zeros(nc-1,dtype=np.uint8)
  if rng is not None:x[free]=rng.integers(0,MODULUS,len(free),dtype=np.uint8)
  for k in range(r-1,-1,-1):
   value=(int(A[k,-1])-int(A[k,:-1]@x))%MODULUS
   assert value%scales[k]==0
   x[piv[k]]=value//scales[k]+(0 if rng is None else (MODULUS//scales[k])*int(rng.integers(0,scales[k])))
  return x
 return solve,{'consistent':True,'rank':r,'pivot_counts':counts,
  'maximum_cokernel_valuation':max(i for i,n in enumerate(counts) if n),
  'kernel_Z2_rank':len(free),'pivots':piv,'scales':scales}

solver,algebra=affine_dvr(F,rhs)
has_multiplier=False;first_algebra=algebra
assert solver is not None,algebra
maxval=algebra['maximum_cokernel_valuation']
assert maxval<=PRECISION-3

rng=np.random.default_rng(39092026);trials=[]
edge0=PA-PB;edge0[A]+=1
for trial in range(1,129):
 z=solver(rng);assert not np.any((F@z-rhs).astype(np.uint8))
 b=z[:d].astype(np.int32);a=z[d:2*d].astype(np.int32)
 T2=kernel_matrix((edge0+C@(a-b))%2,2);rank=rank2(T2);trials.append(rank)
 print('generation trial',trial,'rank',rank,flush=True)
 if rank==d:break
assert trials[-1]==d
assert R.W['contains']((S4@a-rhsA)%8)
assert R.W['contains']((S4@b-rhsB)%8)
assert not np.any((SQ@a-rhsA2)%2) and not np.any((SQ@b-rhsB2)%2)

# Construct two exact lookahead steps using the actual signed integer matrix.
# The cokernel is killed by16.  At a step k the residual/2^k is a multiple
# of16, so the same finite system always has a solution.  The next value
# agrees modulo2^k and solves the equation modulo2^(k+8).
assert not has_multiplier and maxval==4
x=z.astype(np.int64);lookahead=[]
for k in (4,8):
 residual=rhs_exact-F_exact@x
 assert not np.any(residual%(2**(k+4)))
 target=((residual//(2**k))%MODULUS).astype(np.uint8)
 assert not np.any(target%16)
 correction_solver,correction_data=affine_dvr(F,target)
 assert correction_solver is not None and correction_data['maximum_cokernel_valuation']==4
 delta=correction_solver().astype(np.int64)
 new=(x+(2**k)*delta)%(2**(k+8))
 assert not np.any((new-x)%(2**k))
 assert not np.any((F_exact@new-rhs_exact)%(2**(k+8)))
 lookahead.append({'retained_modulus':2**k,'equation_modulus':2**(k+8),
                   'coefficient_vector':new.tolist()})
 x=new

summary={'matrix_shape':list(F.shape),'precision':MODULUS,
 'first_fixed_multiplier_test':{k:v for k,v in first_algebra.items() if k not in ('pivots','scales')},
 'uses_multiplier_column':has_multiplier,
 'integral_Smith_data':{k:v for k,v in algebra.items() if k not in ('pivots','scales')},
 'generation_ranks':trials,
 'retained_common_quotient_order':'2304 * 2^410',
 'retained_coefficient_precision_after_integral_lift':2**(PRECISION-maxval),
 'exact_common_conjugator_constraints_checked':True,
 'exact_G2_constraints_checked':True,
 'exact_signed_integer_lookahead_steps':[{'retained_modulus':t['retained_modulus'],'equation_modulus':t['equation_modulus']} for t in lookahead],
 'multiplier_parameter_mod256':int(z[-1]) if has_multiplier else 0,
 'scope':'Exact integral affine lattice solvability and generating mod2 seed. Full profinite realization beyond the homology quotient is not asserted.',
 'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,'a_mod256':a.tolist(),'beta_correction_mod256':b.tolist(),
 'complete_solution_mod256':z.tolist(),
 'lookahead_steps':lookahead,
 'W8_lattice_rows':lattice_rows.tolist(),'pivot_columns':algebra['pivots'],'pivot_scales':algebra['scales']}
(OUT/'d_cm_fermat_homology_lift.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
