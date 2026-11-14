#!/usr/bin/env python3
"""Literal permutation-module comparison for the two compact complements.

Helpers and field conventions are retained verbatim from the audited D63
program. This new calculation extracts each actual M-to-small compact map
and computes the full semilinear Hermitian norm, its kernel, and its image
in the small marked curve. No source lift is inferred from these ranks.
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

paths=[OUT/'d_compact_splitting_maps.json',OUT/'d_orbit12_projective_kernel.json',OUT/'d_residual_compact_pairing.json',OUT/'d_compact_rigid_source.json']
Split,New,Pair,Rigid=[json.loads(p.read_text()) for p in paths]
rows=[]
for rec in Split['cases']:
 if rec['orbit_size']!=12:continue
 char=rec['character'];N=next(r for r in New['blocks'] if r['character']==char)
 P=next(r for r in Pair['cases'] if r['character']==char)
 B=next(r for r in D['character_blocks'] if r['character']==char)
 act={int(g):np.array(v,dtype=np.uint8).T for g,v in rec['all_complement_actions'].items()}
 flip={a['q_state']:a['flip'] for a in B['all_stabilizer_actions']}
 H0=[g for g in act if not flip[g]];c=N['C3_generator'];tau=N['normalizing_involution'];sig=N['central_semilinear_exchange']
 S3=generated([c,tau]);assert len(S3)==6
 fixed=null(np.vstack([act[c]^np.eye(16,dtype=np.uint8),act[tau]^np.eye(16,dtype=np.uint8)]))
 phi=np.array(P['M_to_small'],dtype=np.uint8)
 nr=rank(mm(phi,fixed));print(json.dumps({'character':char,'S3_fixed_rank':fixed.shape[1],'small_image_rank':nr}),flush=True)
 assert nr==4
 J=mm(fixed,right_inverse(mm(phi,fixed)))
 sm=np.array(rec['all_small_compact_actions'][str(sig)],dtype=np.uint8).T
 J=MUL[2,J]^MUL[3,mm(mm(act[sig],FB[J]),FB[sm])]
 assert np.array_equal(mm(phi,J),np.eye(4,dtype=np.uint8))
 assert np.array_equal(mm(act[sig],FB[J]),mm(J,sm))
 for g in S3:assert np.array_equal(mm(act[g],J),J)
 reps=sorted({min(int(T[g,h]) for h in S3) for g in H0});assert len(reps)==4
 E=np.column_stack([mm(act[g],J) for g in reps]);assert rank(E)==16
 Ei=inv(E);assert np.array_equal(mm(phi,E),np.tile(np.eye(4,dtype=np.uint8),(1,4)))
 permacts={}
 for g in act:
  X=mm(mm(Ei,act[g]),FB[E] if flip[g] else E)
  if not flip[g]:
   expected=np.zeros((16,16),dtype=np.uint8)
   for j,h in enumerate(reps):
    image=min(int(T[T[g,h],k]) for k in S3);i=reps.index(image)
    expected[4*i:4*i+4,4*j:4*j+4]=np.eye(4,dtype=np.uint8)
   assert np.array_equal(X,expected)
  else:
   # sigma is central and therefore fixes the four S3 cosets.
   Y=mm(mm(Ei,act[sig]),FB[E])
   assert np.array_equal(Y,np.kron(np.eye(4,dtype=np.uint8),sm))
  permacts[str(g)]=X.T.tolist()
 H=np.array(P['M_pairing'],dtype=np.uint8);form=mm(mm(E.T,H),FB[E])
 diag=form[:4,:4];off=form[:4,4:8]
 assert all(np.array_equal(form[4*i:4*i+4,4*j:4*j+4],diag if i==j else off) for i in range(4) for j in range(4))
 rigid=next(r for r in Rigid['cases'] if r['character']==char);rcases=[]
 for row in rigid['cases']:
  X=mm(mm(Ei,np.array(row['rigid_compact_action_columns'],dtype=np.uint8).T),E)
  diagonal=X[:4,:4];offdiagonal=X[:4,4:8]
  assert all(np.array_equal(X[4*i:4*i+4,4*j:4*j+4],diagonal if i==j else offdiagonal) for i in range(4) for j in range(4))
  rcases.append({'branch':row['branch'],'beta_Q_state':row['beta_Q_state'],'diagonal_block':diagonal.tolist(),'offdiagonal_block':offdiagonal.tolist()})
 row={'character':char,'S3_states':S3,'S3_fixed_rank':fixed.shape[1],'small_image_rank':nr,'coset_representatives':reps,
      'small_section_columns':J.T.tolist(),'permutation_comparison_columns':E.T.tolist(),'inverse_comparison_columns':Ei.T.tolist(),
      'all_actions_columns':permacts,'pairing_diagonal_block':diag.tolist(),'pairing_offdiagonal_block':off.tolist(),'rigid_actions':rcases}
 rows.append(row)
 print(json.dumps({'character':char,'status':'PASS','diagonal_pairing_rank':rank(diag),'difference_pairing_rank':rank(diag^off),'offdiagonal_pairing_rank':rank(off)}),flush=True)
result={'summary':{'status':'PASS','actual_modules_compared':2,'elapsed_seconds':time.time()-start},'cases':rows,
        'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths+[path]}}
(OUT/'d_compact_permutation.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
