#!/usr/bin/env python3
"""Exact remaining compact and cusp modules on the arithmetic orbits.

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

New=json.loads((OUT/'d_orbit12_projective_kernel.json').read_text())
rows=[]
for B in D['character_blocks']:
 if len(B['orbit'])!=12:continue
 rec=next(r for r in New['blocks'] if r['character']==B['character'])
 acts={a['q_state']:(np.array(a['columns'],dtype=np.uint8).T,a['flip']) for a in B['all_stabilizer_actions']}
 H=sorted(acts);H0=sorted(g for g,(m,f) in acts.items() if not f)
 c=rec['C3_generator'];tau=rec['normalizing_involution'];sig=rec['central_semilinear_exchange']
 sylow=generated(rec['V4_states']+[tau,sig]);assert len(sylow)==16
 F=np.array(B['regular_A4_basis_columns'],dtype=np.uint8).T
 cusps=np.array(B['cusp_columns'],dtype=np.uint8).T
 q0,j0=quotient(cusps);qc=mm(q0,F);jc=mm(inv(F),j0)
 mc={g:mm(mm(qc,m),FB[jc] if flip else jc) for g,(m,flip) in acts.items()}
 M=np.array(rec['compact_complement_columns'],dtype=np.uint8).T;jM=right_inverse(M.T).T
 cm={g:mm(mm(jM,mc[g]),FB[M] if acts[g][1] else M) for g in H}
 for g in H:assert np.array_equal(mm(mc[g],FB[M] if acts[g][1] else M),mm(M,cm[g]))
 c2=int(T[c,c]);I=np.eye(16,dtype=np.uint8)
 weights=[]
 for z in [1,2,3]:
  proj=I^MUL[FB[z],cm[c]]^MUL[MUL[FB[z],FB[z]],cm[c2]]
  assert np.array_equal(mm(proj,proj),proj)
  weights.append(rank(proj))
 assert sum(weights)==16
 R=mm(inv(F),cusps);jR=right_inverse(R.T).T
 cr={g:mm(mm(jR,acts[g][0]),FB[R] if acts[g][1] else R) for g in H}
 for g in H:assert np.array_equal(mm(acts[g][0],FB[R] if acts[g][1] else R),mm(R,cr[g]))
 def realcols(A,flip):
  ans=[]
  for j in range(len(A)):
   for z in [1,2]:
    v=MUL[FB[z] if flip else z,A[:,j]]
    ans.append(sum(int(x)<<(2*i) for i,x in enumerate(v)))
  return ans
 nr=[0]*96
 for g in sylow:nr=[a^b for a,b in zip(nr,realcols(cr[g],acts[g][1]))]
 assert xor_rank(nr)==6
 out={'character':B['character'],'compact_complement_dimension_F4':16,
   'compact_complement_C3_weights_1_z_z2':weights,
   'Hom_of_one_projective_E_to_dual_complement_dimension_F4':weights[2],
   'cusp_dimension_F4':48,'actual_unordered_Sylow_order':16,
   'full_real_cusp_Sylow_norm_rank':xor_rank(nr),'projective_expected_norm_rank':6,
   'compact_complement_actions':{str(g):m.T.tolist() for g,m in cm.items()},
   'cusp_actions':{str(g):m.T.tolist() for g,m in cr.items()}}
 rows.append(out);print(json.dumps({k:v for k,v in out.items() if k not in ['compact_complement_actions','cusp_actions']}),flush=True)
result={'summary':{'status':'PASS','actual_arithmetic_orbits':2,'cusp_projectivity_checked_over_full_unordered_Sylow':True,
 'elapsed_seconds':time.time()-start},'cases':rows,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [OUT/'d_arithmetic_A4_twisted.json',OUT/'d_orbit12_projective_kernel.json']}}
(OUT/'d_remaining_compact_modules.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
