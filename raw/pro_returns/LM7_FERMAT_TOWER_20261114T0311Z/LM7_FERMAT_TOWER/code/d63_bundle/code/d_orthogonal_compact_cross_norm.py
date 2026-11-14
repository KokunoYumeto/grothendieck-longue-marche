#!/usr/bin/env python3
"""Exact cross norms from the projective part to its compact complement.

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

paths=[OUT/'d_arithmetic_A4_twisted.json',OUT/'d_orbit12_projective_kernel.json',OUT/'d_remaining_compact_modules.json']
New=json.loads(paths[1].read_text());Rem=json.loads(paths[2].read_text());rows=[]
for B in New['blocks']:
 C=next(x for x in Rem['cases'] if x['character']==B['character'])
 source=next(x for x in D['character_blocks'] if x['character']==B['character'])
 flips={x['q_state']:x['flip'] for x in source['all_stabilizer_actions']}
 E={int(g):np.array(m,dtype=np.uint8).T[:8,:8] for g,m in B['all_projective_actions'].items()}
 M={int(g):np.array(m,dtype=np.uint8).T for g,m in C['compact_complement_actions'].items()}
 H=sorted(E);assert H==sorted(M);norm=[0]*256;relations=[];actions={}
 for g in H:
  cols=[];flip=flips[g]
  for i in range(8):
   for j in range(16):
    outer=MUL[E[g][:,i,None],FB[M[g][None,:,j]]]
    for z in [1,2]:cols.append(pack(MUL[FB[z] if flip else z,outer]))
  assert xor_rank(cols)==256
  actions[g]=cols;norm=[a^b for a,b in zip(norm,cols)]
  relations.extend(v^(1<<i) for i,v in enumerate(cols))
 coin=256-xor_rank(relations);nr=xor_rank(norm);assert coin==nr==4
 # Every norm column kills every retained relation, evaluated as an actual map.
 def lin(cols,v):
  r=0
  while v:
   b=v&-v;r^=cols[b.bit_length()-1];v^=b
  return r
 assert all(lin(norm,v)==0 for v in relations)
 for g,cols in actions.items():assert [lin(cols,v) for v in norm]==norm
 rec={'character':B['character'],'identical_projective_copies':4,'fiber_dimension_F2':256,
      'global_dimension_per_copy':3072,'coinvariant_dimension_per_copy':coin,
      'norm_rank_per_copy':nr,'norm_isomorphism':True,
      'all_norm_columns':[hex(v) for v in norm],
      'all_stabilizer_action_columns':{str(g):[hex(v) for v in cols] for g,cols in actions.items()}}
 rows.append(rec);print(json.dumps({k:v for k,v in rec.items() if k not in ['all_norm_columns','all_stabilizer_action_columns']}),flush=True)
result={'summary':{'status':'PASS','actual_orbit_types':2,'new_cross_dimension':sum(r['identical_projective_copies']*r['global_dimension_per_copy'] for r in rows),
 'new_cross_coinvariants':sum(r['identical_projective_copies']*r['coinvariant_dimension_per_copy'] for r in rows),
 'compact_orthogonal_transport_requires_separate_integral_proof':True,
 'elapsed_seconds':time.time()-start},'cases':rows,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_orthogonal_compact_cross_norm.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
