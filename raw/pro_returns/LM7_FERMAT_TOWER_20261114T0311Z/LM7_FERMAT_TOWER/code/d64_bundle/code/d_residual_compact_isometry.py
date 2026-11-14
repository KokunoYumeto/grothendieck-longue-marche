#!/usr/bin/env python3
"""Actual equivariant isometry lifts on the remaining projective compact covers.

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
rows=[]
for rec in Split['cases']:
 if rec['orbit_size']!=8:continue
 char=rec['character'];p=next(r for r in Pair['cases'] if r['character']==char)
 Hm=np.array(p['M_pairing'],dtype=np.uint8);phi=np.array(p['M_to_small'],dtype=np.uint8)
 acts={int(g):np.array(a,dtype=np.uint8).T for g,a in rec['all_complement_actions'].items()}
 src=next(r for r in D['character_blocks'] if r['character']==char)
 flips={a['q_state']:a['flip'] for a in src['all_stabilizer_actions']}
 H=sorted(acts);gens=list(rec['ordered_stabilizer_generators'])
 gens.append(next(g for g in H if flips[g]));gens=sorted(set(gens));assert generated(gens)==H
 V4=[g for g in D['A4_states'] if order(g)<=2]
 rad=np.column_stack([acts[g]^np.eye(16,dtype=np.uint8) for g in V4])
 assert rank(rad)==12 and not np.any(mm(phi,rad))
 def constraints(X):
  chunks=[mm(acts[g],FB[X] if flips[g] else X)^mm(X,acts[g]) for g in gens]
  chunks.append(mm(phi,X))
  out=0;shift=0
  for a in chunks:out^=pack(a)<<shift;shift+=2*a.size
  return out
 cols=[constraints(matrix_of(1<<j)) for j in range(512)]
 solve,ker,linear_rank=linear_solver(cols)
 for v in ker:assert constraints(matrix_of(v))==0
 basis=[matrix_of(v) for v in ker];cases=[]
 for ta in p['small_actions']:
  target=np.array(ta['compact_action_columns'],dtype=np.uint8).T
  rhs=pack(mm(target,phi))<<(512*len(gens))
  seed=solve(rhs);assert seed is not None
  X0=matrix_of(seed);assert constraints(X0)==rhs
  def error(X):return hermpack(mm(mm(X.T,Hm),FB[X])^Hm)
  constant=error(X0);linear=[error(X0^v)^constant for v in basis]
  quadratic=[]
  for i in range(len(basis)):
   for j in range(i+1,len(basis)):
    quadratic.append((i,j,error(X0^basis[i]^basis[j])^constant^linear[i]^linear[j]))
  def polynomial(mask):
   z=constant^combine(linear,mask)
   for i,j,c in quadratic:
    if mask>>i&1 and mask>>j&1:z^=c
   return z
  rng=random.Random(0xD640000+ta['branch']+sum((i+1)*v for i,v in enumerate(char)))
  for trial in range(1,200001):
   mask=0 if trial==1 else rng.getrandbits(len(ker))
   if polynomial(mask)==0:
    X=matrix_of(seed^combine(ker,mask))
    assert error(X)==0 and constraints(X)==rhs and rank(X)==16
    break
  else:raise AssertionError(('fixed_seed_search_exhausted',char,ta['branch'],len(ker)))
  for g in H:assert np.array_equal(mm(acts[g],FB[X] if flips[g] else X),mm(X,acts[g]))
  assert np.array_equal(mm(phi,X),mm(target,phi))
  # Every homogeneous parameter lies in the actual small-map kernel.
  assert all(not np.any(mm(phi,b)) for b in basis)
  out={'branch':ta['branch'],'linear_rank':linear_rank,'parameter_dimension_F2':len(ker),
       'quadratic_coefficient_span_rank':xor_rank([constant]+linear+[x[2] for x in quadratic]),
       'constant':hex(constant),'linear_coefficients':[hex(v) for v in linear],
       'quadratic_coefficients':[[i,j,hex(c)] for i,j,c in quadratic],
       'fixed_seed_trial':trial,'solution_mask':hex(mask),'linear_seed_mask':hex(seed),
       'isometry_columns':X.T.tolist(),'rank':rank(X),'all_stabilizer_equations_checked':len(H),
       'actual_small_action_retained':True,'actual_pairing_error':'0x0'}
  cases.append(out)
  print(json.dumps({k:v for k,v in out.items() if k not in ['linear_coefficients','quadratic_coefficients','isometry_columns']}|{'character':char}),flush=True)
 rows.append({'character':char,'orbit_size':8,'stabilizer_generators':gens,'projective_cover_kernel_equals_V4_radical':True,
              'homogeneous_equivariant_parameter_masks':[hex(v) for v in ker],'cases':cases})
result={'summary':{'status':'PASS','actual_old_orbits':2,'both_D57_branches_solved':True,
 'every_solution_preserves_actual_compact_pairing_and_small_action':True,'elapsed_seconds':time.time()-start},
 'cases':rows,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_residual_compact_isometry.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)

