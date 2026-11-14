#!/usr/bin/env python3
"""Actual compact projective kernel and equivariant affine retractions.

The two arithmetic orbit12 stabilizers are used literally.  This records
their full projective compact part, an actual zero-norm complement, all
affine/small/cusp maps, and every cross/self exterior norm.  The source
automorphism and integral transport are proved separately.
"""
from pathlib import Path
from itertools import combinations
import numpy as np
import json,hashlib,time
OUT=Path(__file__).resolve().parent;start=time.time()
path=OUT/'d_arithmetic_A4_twisted.json';D=json.loads(path.read_text())
T=np.array(D['Q_multiplication'],dtype=np.int16);A4=D['A4_states']
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
FB=np.array([0,1,3,2],dtype=np.uint8);Z=np.array([1,2,3],dtype=np.uint8)
def mm(a,b):
 out=np.zeros((a.shape[0],b.shape[1]),dtype=np.uint8)
 for k in range(a.shape[1]):out^=MUL[a[:,k,None],b[k,None,:]]
 return out
def rr(a):
 a=np.array(a,dtype=np.uint8,copy=True);row=0;p=[]
 for c in range(a.shape[1]):
  at=np.flatnonzero(a[row:,c])
  if not len(at):continue
  j=row+int(at[0]);a[[row,j]]=a[[j,row]];a[row]=MUL[FB[a[row,c]],a[row]]
  v=a[:,c].copy();v[row]=0;a^=MUL[v[:,None],a[row,None,:]]
  p.append(c);row+=1
  if row==len(a):break
 return a,p
def rank(a):return len(rr(a)[1])
def inv(a):
 n=len(a);r,p=rr(np.column_stack([a,np.eye(n,dtype=np.uint8)]));assert p[:n]==list(range(n));return r[:,n:]
def solve(a,b):
 n=a.shape[1];r,p=rr(np.column_stack([a,b]));assert all(c<n for c in p)
 x=np.zeros((n,b.shape[1]),dtype=np.uint8)
 for i,c in enumerate(p):x[c]=r[i,n:]
 assert np.array_equal(mm(a,x),b);return x
def right_inverse(a):
 p=rr(a)[1];assert len(p)==len(a)
 out=np.zeros((a.shape[1],len(a)),dtype=np.uint8);out[p]=inv(a[:,p]);return out
def null(a):
 r,p=rr(a);free=[j for j in range(a.shape[1]) if j not in p]
 n=np.zeros((a.shape[1],len(free)),dtype=np.uint8);n[free,np.arange(len(free))]=1
 n[np.array(p),:]=r[:len(p),free]
 assert not np.any(mm(a,n));return n
def quotient(c):
 r,p=rr(c.T);free=[j for j in range(c.shape[0]) if j not in p]
 q=np.zeros((len(free),c.shape[0]),dtype=np.uint8);q[np.arange(len(free)),free]=1
 q[:,p]=r[:len(p),free].T
 j=np.zeros((c.shape[0],len(free)),dtype=np.uint8);j[free,np.arange(len(free))]=1
 assert not np.any(mm(q,c));assert np.array_equal(mm(q,j),np.eye(len(free),dtype=np.uint8))
 return q,j
def generated(gens):
 seen={0};todo=[0]
 for g in todo:
  for h in gens:
   k=int(T[g,h])
   if k not in seen:seen.add(k);todo.append(k)
 return sorted(seen)
def order(g):
 h=0
 for k in range(1,100):
  h=int(T[h,g])
  if h==0:return k
 raise AssertionError(g)
def inverse(g):return next(j for j in range(576) if T[g,j]==0)
def xor_rank(cols):
 b={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in b:b[p]=v;break
   v^=b[p]
 return len(b)
def pack(a):return sum(int(v)<<(2*j) for j,v in enumerate(a.ravel()))
def hermpack(a):
 assert np.array_equal(a,FB[a.T]);assert np.all(a.diagonal()<2)
 v=list(map(int,a.diagonal()))
 for i in range(len(a)):
  for j in range(i+1,len(a)):v.extend([int(a[i,j])&1,int(a[i,j])>>1])
 return sum(x<<j for j,x in enumerate(v))
sig=573;V4=[g for g in A4 if order(g)<=2];assert len(V4)==4
rows=[]
for B in D['character_blocks']:
 if len(B['orbit'])!=12:continue
 acts={a['q_state']:(np.array(a['columns'],dtype=np.uint8).T,a['flip']) for a in B['all_stabilizer_actions']}
 H=sorted(acts);H0=sorted(g for g,(m,f) in acts.items() if not f)
 assert len(H)==48 and len(H0)==24 and sig in H and acts[sig][1]
 c=next(g for g in A4 if order(g)==3)
 c2=int(T[c,c]);C3=[0,c,c2]
 tau=next(g for g in H0 if order(g)==2 and g not in A4 and T[T[g,c],g]==c2)
 assert generated(V4+[c,tau])==H0
 P2=generated(V4+[tau]);assert len(P2)==8
 reps=sorted({min(int(T[g,h]) for h in C3) for g in H0});assert len(reps)==8 and reps[0]==0
 F=np.array(B['regular_A4_basis_columns'],dtype=np.uint8).T
 theta=np.array(B['regular_projection_columns'],dtype=np.uint8).T
 cusps=np.array(B['cusp_columns'],dtype=np.uint8).T
 q0,j0=quotient(cusps);qc=mm(q0,F);jc=mm(inv(F),j0)
 smallC=np.array(B['target_cusp_columns'],dtype=np.uint8).T
 qs,js=quotient(smallC);phi=mm(mm(qs,theta),jc)
 assert rank(phi)==4 and np.array_equal(mm(phi,qc),mm(qs,theta))
 mc={g:mm(mm(qc,m),FB[jc] if flip else jc) for g,(m,flip) in acts.items()}
 for g,(m,flip) in acts.items():assert np.array_equal(mm(qc,m),mm(mc[g],FB[qc] if flip else qc))
 qt,jt=quotient(np.column_stack([mc[g]^np.eye(48,dtype=np.uint8) for g in V4]))
 assert qt.shape==(12,48)
 Pchi=np.eye(48,dtype=np.uint8)^MUL[3,mc[c]]^MUL[2,mc[c2]]
 PU=np.eye(96,dtype=np.uint8)^MUL[3,acts[c][0]]^MUL[2,acts[c2][0]]
 assert np.array_equal(mm(Pchi,Pchi),Pchi)
 assert np.array_equal(mm(mc[c],Pchi),MUL[2,Pchi])
 assert not np.any(mm(theta,PU))
 iota=lambda v:mm(mm(mc[tau],mc[sig]),FB[v])
 iotaU=lambda v:mm(mm(acts[tau][0],acts[sig][0]),FB[v])
 assert np.array_equal(iota(iota(np.eye(48,dtype=np.uint8))),np.eye(48,dtype=np.uint8))
 raw=mm(Pchi,jt);cand=[]
 for j in range(raw.shape[1]):
  for z in [1,2]:
   v=MUL[z,raw[:,j:j+1]];cand.append(v^iota(v))
 cand=np.column_stack(cand);chosen=rr(mm(qt,cand))[1]
 assert len(chosen)==4
 vs=[cand[:,j:j+1] for j in chosen]
 Es=[];Us=[]
 for v in vs:
  assert np.array_equal(iota(v),v) and np.array_equal(mm(mc[c],v),MUL[2,v])
  E=np.column_stack([mm(mc[g],v) for g in reps]);assert rank(E)==8
  assert not np.any(mm(phi,E))
  # The trace-one lift has the exact compact image, character, exchange,
  # and small affine zero simultaneously.
  w=mm(PU,solve(qc,MUL[2,v]));w^=iotaU(w)
  assert np.array_equal(mm(qc,w),v) and not np.any(mm(theta,w))
  assert np.array_equal(iotaU(w),w)
  U=np.column_stack([mm(acts[g][0],w) for g in reps])
  assert np.array_equal(mm(qc,U),E) and not np.any(mm(theta,U))
  Es.append(E);Us.append(U)
 E=np.column_stack(Es);U=np.column_stack(Us);assert rank(E)==32
 jE=right_inverse(E.T).T
 me={g:mm(mm(jE,mc[g]),FB[E] if acts[g][1] else E) for g in H}
 for g in H:
  assert np.array_equal(mm(mc[g],FB[E] if acts[g][1] else E),mm(E,me[g]))
  assert np.array_equal(mm(acts[g][0],FB[U] if acts[g][1] else U),mm(U,me[g]))
  assert all(not np.any(me[g][8*i:8*i+8,8*j:8*j+8]) for i in range(4) for j in range(4) if i!=j)
 # Coinduction gives actual H0-linear retractions from four C3-eigen
 # functionals.  Every identity column, not only the generators, is used.
 eq=[];rhs=[]
 for i,g in enumerate(reps):
  vals=mm(mc[inverse(g)],E)
  for j in range(32):
   eq.append(vals[:,j]);rhs.append([int(j//8==k and j%8==i) for k in range(4)])
 eig=mc[c].T^MUL[2,np.eye(48,dtype=np.uint8)]
 eq.extend(eig);rhs.extend([[0]*4 for _ in range(48)])
 functionals=solve(np.array(eq,dtype=np.uint8),np.array(rhs,dtype=np.uint8)).T
 R=np.vstack([mm(functionals[k:k+1],mc[inverse(g)]) for k in range(4) for g in reps])
 assert np.array_equal(mm(R,E),np.eye(32,dtype=np.uint8))
 for g in H0:assert np.array_equal(mm(R,mc[g]),mm(me[g],R))
 sigmaR=mm(mm(me[sig],FB[R]),FB[mc[sig]])
 R=MUL[2,R]^MUL[3,sigmaR]
 assert np.array_equal(mm(R,E),np.eye(32,dtype=np.uint8))
 for g in H:
  assert np.array_equal(mm(R,mc[g]),mm(me[g],FB[R] if acts[g][1] else R))
 ecompact=mm(E,R);assert np.array_equal(mm(ecompact,ecompact),ecompact)
 remainder=null(R);assert remainder.shape==(48,16)
 jr=right_inverse(remainder.T).T
 remainder_norm=np.zeros((16,16),dtype=np.uint8)
 for g in P2:
  m=mm(mm(jr,mc[g]),remainder)
  assert np.array_equal(mm(mc[g],remainder),mm(remainder,m))
  remainder_norm^=m
 assert not np.any(remainder_norm)
 finite_projectors=[]
 for i in range(4):
  e=mm(mm(Us[i],R[8*i:8*i+8]),qc)
  assert np.array_equal(mm(e,e),e) and rank(e)==8
  assert not np.any(mm(theta,e)) and not np.any(mm(e,mm(inv(F),cusps)))
  for g,(m,flip) in acts.items():assert np.array_equal(mm(e,m),mm(m,FB[e] if flip else e))
  for old in finite_projectors:assert not np.any(mm(e,old)) and not np.any(mm(old,e))
  finite_projectors.append(e)
 # Exact exterior maps of all six cross modules and four self modules.
 gens=V4+[c,tau,sig];crosses=[];selves=[]
 for i,j in combinations(range(4),2):
  norm=[0]*128;rels=[]
  for g in H:
   L=me[g][8*i:8*i+8,8*i:8*i+8];M=me[g][8*j:8*j+8,8*j:8*j+8]
   cols=[];flip=acts[g][1]
   for a in range(8):
    for b in range(8):
     outer=MUL[L[:,a,None],FB[M[None,:,b]]]
     for z in [1,2]:cols.append(pack(MUL[FB[z] if flip else z,outer]))
   assert xor_rank(cols)==128
   norm=[x^y for x,y in zip(norm,cols)]
   if g in gens:rels.extend(v^(1<<k) for k,v in enumerate(cols))
  coinv=128-xor_rank(rels);nr=xor_rank(norm);assert nr==coinv
  crosses.append({'summands':[i,j],'global_dimension':1536,'coinvariant_dimension':coinv,
                  'norm_rank':nr,'norm_injective':True,'all_norm_columns':[hex(v) for v in norm]})
 for i in range(4):
  norm=[0]*64;rels=[]
  hrep=[(a,a,1) for a in range(8)]+[(a,b,z) for a in range(8) for b in range(a+1,8) for z in [1,2]]
  for g in H:
   M=me[g][8*i:8*i+8,8*i:8*i+8];cols=[];flip=acts[g][1]
   for a,b,z in hrep:
    z=int(FB[z]) if flip else z
    v=MUL[z,MUL[M[:,a,None],FB[M[None,:,b]]]]
    if a!=b:v^=MUL[FB[z],MUL[M[:,b,None],FB[M[None,:,a]]]]
    cols.append(hermpack(v))
   norm=[x^y for x,y in zip(norm,cols)]
   if g in gens:rels.extend(v^(1<<k) for k,v in enumerate(cols))
  coinv=64-xor_rank(rels);nr=xor_rank(norm)
  selves.append({'summand':i,'global_dimension':768,'coinvariant_dimension':coinv,
                 'norm_rank':nr,'norm_kernel_dimension':coinv-nr,'all_norm_columns':[hex(v) for v in norm]})
 rec={'character':B['character'],'H0_order':24,'H_order':48,'V4_states':V4,'C3_generator':c,
      'normalizing_involution':tau,'central_semilinear_exchange':sig,'induction_coset_representatives':reps,
      'projective_compact_dimensions_F4':[8]*4,'compact_complement_dimension_F4':16,
      'compact_complement_Sylow_norm_rank':0,'all_small_images_zero':True,
      'all_cusp_projections_zero':True,'compact_embedding_columns':E.T.tolist(),
      'affine_embedding_columns':U.T.tolist(),'compact_retraction_rows':R.tolist(),
      'compact_complement_columns':remainder.T.tolist(),
      'four_affine_idempotent_rows':[e.tolist() for e in finite_projectors],
      'all_projective_actions':{str(g):m.T.tolist() for g,m in me.items()},
      'cross_norms':crosses,'self_norms':selves}
 rows.append(rec)
 print(json.dumps({k:v for k,v in rec.items() if not isinstance(v,(list,dict)) or k in ['character','projective_compact_dimensions_F4']}),flush=True)
 print(json.dumps({'character':B['character'],'cross_coinvariants':[x['coinvariant_dimension'] for x in crosses],
                   'self_coinvariants':[x['coinvariant_dimension'] for x in selves],
                   'self_norm_ranks':[x['norm_rank'] for x in selves]}),flush=True)
result={'summary':{'status':'PASS','actual_arithmetic_base_order':46656,'actual_target_order':3888,
                   'two_orbit12_blocks_checked':True,'global_new_cross_dimension':sum(x['global_dimension'] for b in rows for x in b['cross_norms']),
                   'cross_coinvariant_dimension':sum(x['coinvariant_dimension'] for b in rows for x in b['cross_norms']),
                   'self_coinvariant_dimension':sum(x['coinvariant_dimension'] for b in rows for x in b['self_norms']),
                   'self_norm_rank':sum(x['norm_rank'] for b in rows for x in b['self_norms']),
                   'arithmetic_source_lift_requires_separate_proof':True,'elapsed_seconds':time.time()-start},
        'blocks':rows,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
(OUT/'d_orbit12_projective_kernel.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
