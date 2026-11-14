#!/usr/bin/env python3
"""Exact source-conjugator chain maps on the two rigid compact complements.

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

import random
paths=[OUT/'d_arithmetic_A4_twisted.json',OUT/'d_compact_splitting_maps.json',OUT/'d_residual_compact_pairing.json']
Split=json.loads(paths[1].read_text());Pair=json.loads(paths[2].read_text())
def linear_solver(cols):
 piv={};ker=[]
 for j,v in enumerate(cols):
  mask=1<<j
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=(v,mask);break
   w,m=piv[k];v^=w;mask^=m
  if not v:ker.append(mask)
 def solve(v):
  mask=0
  while v:
   k=v.bit_length()-1
   if k not in piv:return None
   w,m=piv[k];v^=w;mask^=m
  return mask
 return solve,ker,len(piv)
def matrix_of(v):return np.array([(v>>(2*j))&3 for j in range(256)],dtype=np.uint8).reshape((16,16))
def combine(cols,v):
 r=0
 while v:
  b=v&-v;r^=cols[b.bit_length()-1];v^=b
 return r
def independent(cs):
 piv={};at=[]
 for j,v in enumerate(cs):
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=v;at.append(j);break
   v^=piv[k]
 return at
def quotient2(cols,n):
 piv={}
 for v in cols:
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=v;break
   v^=piv[k]
 free=[j for j in range(n) if j not in piv]
 def q(v):
  for k in sorted(piv,reverse=True):
   if v>>k&1:v^=piv[k]
  return sum(((v>>j)&1)<<i for i,j in enumerate(free))
 return q,free

from itertools import product
from collections import deque
paths.extend([OUT/'d_orbit12_projective_kernel.json',OUT/'d_arithmetic_affine_base.json'])
New=json.loads(paths[-2].read_text());Aff=json.loads(paths[-1].read_text())
def lin(cs,v):
 out=0
 while v:
  b=v&-v;out^=cs[b.bit_length()-1];v^=b
 return out
def realcols(A,flip=False):
 return [sum(int(v)<<(2*i) for i,v in enumerate(MUL[FB[z] if flip else z,A[:,j]])) for j in range(A.shape[1]) for z in [1,2]]
def coords(cols):
 piv={}
 for j,v in enumerate(cols):
  w=1<<j
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=(v,w);break
   a,b=piv[k];v^=a;w^=b
  assert v
 def co(v,check=True):
  out=0
  for k in sorted(piv,reverse=True):
   if v>>k&1:
    a,b=piv[k];v^=a;out^=b
  if check:assert not v
  return out
 return co
def unpackv(v,n):return np.array([(v>>(2*i))&3 for i in range(n)],dtype=np.uint8)
qstar=[np.array(m,dtype=np.int16).T for m in Aff['Q_linear_image_matrices']]
QL=np.array([qstar[j] for j in Aff['Q_to_linear_image']],dtype=np.int16)
S=1
def normq(v):return min(tuple(int(x)%12 for x in v),tuple(-int(x)%12 for x in v))
qi={tuple(v):i for i,v in enumerate(D['Q_states'])};R=qi[normq((0,11,1,11))]
vr=np.array(Aff['affine_r_translation'],dtype=np.int16)
vectors=list(product(range(3),repeat=4));vi={v:i for i,v in enumerate(vectors)}
vmat=np.array(vectors,dtype=np.int16)
right_s=[];right_r=[]
for q in range(576):
 right_s.extend(int(T[q,S])*81+j for j in range(81))
 shift=QL[q]@vr%3
 right_r.extend(int(T[q,R])*81+vi[tuple((np.array(v)+shift)%3)] for v in vectors)
parent=[None]*46656;parent[0]=(-1,-1);todo=deque([0])
while todo:
 g=todo.popleft()
 for tok,arr in [(0,right_s),(1,right_r)]:
  h=arr[g]
  if parent[h] is None:parent[h]=(g,tok);todo.append(h)
assert all(x is not None for x in parent)
def word_to(g):
 w=[]
 while g:
  g,tok=parent[g];w.append(tok)
 return w[::-1]
def path_terms(word):
 q=0;v=np.zeros(4,dtype=np.int16);terms=[]
 for tok in word:
  if tok==0:q=int(T[q,S])
  else:
   terms.append((q,v.copy(),1));v=(v+QL[q]@vr)%3;q=int(T[q,R]);terms.append((q,v.copy(),-1))
 return q,v,terms
beta_states={1:[476,498],3:[456,461]}
for qs in beta_states.values():
 for q in qs:assert T[q,S]==T[S,q]
rows=[]
for rec in Split['cases']:
 if rec['orbit_size']!=12:continue
 char=rec['character'];ell=np.array(char,dtype=np.int16)
 B=next(r for r in D['character_blocks'] if r['character']==char)
 N=next(r for r in New['blocks'] if r['character']==char)
 P=next(r for r in Pair['cases'] if r['character']==char)
 U=np.array(B['source_basis_columns'],dtype=np.uint8).T;free=B['source_free_edges']
 F=np.array(B['regular_A4_basis_columns'],dtype=np.uint8).T
 Fi=inv(F);cusp=np.array(B['cusp_columns'],dtype=np.uint8).T
 qc,jc=quotient(cusp)
 E=np.array(N['compact_embedding_columns'],dtype=np.uint8).T
 M=np.array(N['compact_complement_columns'],dtype=np.uint8).T
 fullinv=inv(np.column_stack([E,M]));m=fullinv[32:]
 acts={a['q_state']:(np.array(a['columns'],dtype=np.uint8).T,a['flip']) for a in B['all_stabilizer_actions']}
 H=sorted(acts);syl=rec['unordered_Sylow_states'];assert len(syl)==16
 real={g:realcols(A,flip) for g,(A,flip) in acts.items()}
 Ru=mm(Fi,cusp);rb=realcols(Ru);assert len(rb)==96
 norms=[0]*96
 for j,v in enumerate(rb):
  for g in syl:norms[j]^=lin(real[g],v)
 inds=independent(norms);assert len(inds)==6
 seeds=[rb[i] for i in inds]
 reg=[lin(real[g],v) for v in seeds for g in syl]
 co=coords(reg);identity_index=syl.index(0)
 def p_retract(v):
  out=0
  for g in syl:
   val=co(lin(real[inverse(g)],v),False)
   for i in range(6):
    if val>>(16*i+identity_index)&1:out^=reg[16*i+syl.index(g)]
  return out
 rp=[p_retract(1<<j) for j in range(192)]
 assert all(lin(rp,v)==v for v in rb)
 reps=sorted({min(int(T[g,h]) for h in syl) for g in H});assert len(reps)==3
 ret=[0]*192
 for g in reps:
  for j in range(192):ret[j]^=lin(real[g],lin(rp,real[inverse(g)][j]))
 # Odd scalar averaging makes the retraction F4-linear as well.
 scalar2=realcols(MUL[2,np.eye(96,dtype=np.uint8)])
 scalar3=realcols(MUL[3,np.eye(96,dtype=np.uint8)])
 ret=[v^lin(scalar2,lin(ret,scalar3[j]))^lin(scalar3,lin(ret,scalar2[j])) for j,v in enumerate(ret)]
 assert all(lin(ret,v)==v for v in rb)
 for g in H:assert all(lin(ret,v)==lin(real[g],ret[j]) for j,v in enumerate(real[g]))
 assert all(lin(ret,v)==lin(scalar2,ret[j]) for j,v in enumerate(scalar2))
 raw=mm(mm(Fi,jc),M)
 rawcols=realcols(raw)
 lifted=[v^lin(ret,v) for v in rawcols]
 iM=np.column_stack([unpackv(lifted[2*j],96) for j in range(16)])
 assert realcols(iM)==lifted
 assert np.array_equal(mm(qc,mm(F,iM)),M)
 for g,cc in rec['all_complement_actions'].items():
  a,flip=acts[int(g)];cm=np.array(cc,dtype=np.uint8).T
  assert np.array_equal(mm(a,FB[iM] if flip else iM),mm(iM,cm))
 chainM=mm(mm(U,F),iM)
 hform=np.array(P['M_pairing'],dtype=np.uint8);phi=np.array(P['M_to_small'],dtype=np.uint8)
 def chainmap(terms):
  out=chainM.copy()
  for h,v,sign in terms:
   phase=np.array([int(ell@QL[g]@v%3) for g in range(576)],dtype=np.int16)
   out[T[:,h]]^=MUL[np.array([1,2,3],dtype=np.uint8)[phase,None],chainM]
  assert np.array_equal(mm(U,out[free]),out)
  return mm(mm(m,qc),out[free])
 cases=[]
 for branch,qs in beta_states.items():
  target=np.array(next(r for r in P['small_actions'] if r['branch']==branch)['compact_action_columns'],dtype=np.uint8).T
  for q in qs:
   w=word_to(81*q);qe,v,terms=path_terms(w);assert qe==q and not np.any(v)
   X=chainmap(terms)
   for g,cc in rec['all_complement_actions'].items():
    A=np.array(cc,dtype=np.uint8).T;flip=acts[int(g)][1]
    assert np.array_equal(mm(A,FB[X] if flip else X),mm(X,A))
   smallok=np.array_equal(mm(phi,X),mm(target,phi))
   err=hermpack(mm(mm(X.T,hform),FB[X])^hform)
   mod4scalar=D['Q_states'][q][1]%4==0 and D['Q_states'][q][2]%4==0
   row={'branch':branch,'beta_Q_state':q,'beta_word':w,'beta_translation':[0]*4,
    'beta_mod4_scalar':mod4scalar,'rigid_compact_action_columns':X.T.tolist(),
    'rank':rank(X),'small_action_matches':smallok,'pairing_error':hex(err),'isometry':err==0}
   cases.append(row);print(json.dumps({k:v for k,v in row.items() if k not in ['rigid_compact_action_columns','beta_word']}|{'character':char}),flush=True)
 rows.append({'character':char,'equivariant_affine_M_lift_columns':iM.T.tolist(),
  'cusp_retraction_real_columns':[hex(v) for v in ret],'regular_cusp_seeds':inds,'cases':cases})
result={'summary':{'status':'PASS_FINITE_MARKED_CHAIN_TEST','elapsed_seconds':time.time()-start},'cases':rows,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_compact_rigid_source.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)

