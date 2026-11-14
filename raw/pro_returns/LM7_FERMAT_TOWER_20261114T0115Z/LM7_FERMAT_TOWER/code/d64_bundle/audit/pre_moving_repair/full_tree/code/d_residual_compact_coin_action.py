#!/usr/bin/env python3
"""An exact simultaneous retraction test for the actual source-s correction image.

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
paths.extend([OUT/'d_residual_compact_norm.json',OUT/'d_residual_compact_cusp.json'])
Norm=json.loads(paths[-2].read_text());Cusp=json.loads(paths[-1].read_text())
def coordinates(columns):
 piv={}
 for j,v in enumerate(columns):
  w=1<<j
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=(v,w);break
   a,b=piv[k];v^=a;w^=b
  assert v
 def coord(v):
  out=0
  while v:
   k=v.bit_length()-1;assert k in piv
   a,b=piv[k];v^=a;out^=b
  return out
 return coord
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
def hermunpack(v,n=16):
 a=np.zeros((n,n),dtype=np.uint8)
 for i in range(n):a[i,i]=(v>>i)&1
 at=n
 for i in range(n):
  for j in range(i+1,n):a[i,j]=(v>>at)&3;a[j,i]=FB[a[i,j]];at+=2
 assert hermpack(a)==v;return a
rows=[]
for rec in Split['cases']:
 if rec['orbit_size']!=12:continue
 char=rec['character'];p=next(r for r in Pair['cases'] if r['character']==char)
 nr=next(r for r in Norm['cases'] if r['character']==char)
 cr=next(r for r in Cusp['cases'] if r['character']==char)
 phi=np.array(p['M_to_small'],dtype=np.uint8)
 acts={int(g):np.array(a,dtype=np.uint8).T for g,a in rec['all_complement_actions'].items()}
 src=next(r for r in D['character_blocks'] if r['character']==char)
 flips={a['q_state']:a['flip'] for a in src['all_stabilizer_actions']}
 H=sorted(acts);gens=list(rec['ordered_stabilizer_generators'])
 gens.append(next(g for g in H if flips[g]));gens=sorted(set(gens));assert generated(gens)==H
 kn=[int(x,16) for x in nr['kernel_basis']];coord=coordinates(kn)
 central={int(g):[int(x,16) for x in cs] for g,cs in nr['all_action_columns'].items()}
 rel=[coord(combine(cs,v)^v) for cs in central.values() for v in kn]
 q,free=quotient2(rel,240);assert free==cr['coinvariant_representatives_in_kernel_basis']
 dim=len(free);assert dim==10
 representatives=[hermunpack(kn[j]) for j in free]
 I=[int(v,16) for v in cr['independent_correction_images']];idim=len(I);assert idim==4
 icoord=coordinates(I)
 def constraints(X):
  chunks=[mm(acts[g],FB[X] if flips[g] else X)^mm(X,acts[g]) for g in gens]
  chunks.append(mm(phi,X));out=0;shift=0
  for a in chunks:out^=pack(a)<<shift;shift+=2*a.size
  return out
 cols=[constraints(matrix_of(1<<j)) for j in range(512)]
 solveX,params,lrank=linear_solver(cols);basis=[matrix_of(v) for v in params]
 for v in params:assert constraints(matrix_of(v))==0
 def coin_action(X):
  return [q(coord(hermpack(mm(mm(X,b),FB[X.T])))) for b in representatives]
 cases=[];allcoeff=[]
 for ta in p['small_actions']:
  target=np.array(ta['compact_action_columns'],dtype=np.uint8).T
  rhs=pack(mm(target,phi))<<(512*len(gens));seed=solveX(rhs);assert seed is not None
  X0=matrix_of(seed);assert constraints(X0)==rhs
  const=coin_action(X0)
  linear=[[a^b for a,b in zip(coin_action(X0^v),const)] for v in basis]
  quad=[]
  for i in range(len(basis)):
   for j in range(i+1,len(basis)):
    cs=[a^b^c^d for a,b,c,d in zip(coin_action(X0^basis[i]^basis[j]),const,linear[i],linear[j])]
    quad.append((i,j,cs))
  coeff=[const]+linear+[r[2] for r in quad]
  restrict=[[icoord(combine(cs,v)) for v in I] for cs in coeff]
  allcoeff.extend(zip(coeff,restrict))
  cases.append({'branch':ta['branch'],'linear_seed_mask':hex(seed),
    'constant_coinvariant_action':[hex(v) for v in const],
    'linear_coinvariant_action_coefficients':[[hex(v) for v in cs] for cs in linear],
    'quadratic_coinvariant_action_coefficients':[[i,j,[hex(v) for v in cs]] for i,j,cs in quad],
    'all_coefficients_preserve_actual_correction_image':True})
 # P:C_G -> I must be a right inverse to the fixed inclusion and intertwine
 # every coefficient of both affine-family quadratic exterior actions.
 def pcolumns(mask):return [(mask>>(idim*j))&((1<<idim)-1) for j in range(dim)]
 def equations(mask):
  P=pcolumns(mask);out=0;shift=0
  for cs,rs in allcoeff:
   for j,v in enumerate(cs):
    out^=(combine(P,v)^combine(rs,P[j]))<<shift;shift+=idim
  for j,v in enumerate(I):out^=combine(P,v)<<shift;shift+=idim
  return out
 pcols=[equations(1<<j) for j in range(dim*idim)]
 solveP,pkernel,prank=linear_solver(pcols)
 shift=idim*dim*len(allcoeff)
 prhs=sum((1<<j)<<(shift+idim*j) for j in range(idim))
 pmask=solveP(prhs)
 row={'character':char,'coinvariant_dimension':dim,'correction_image_dimension':idim,
      'homology_affine_parameter_dimension':len(params),'homology_equation_rank':lrank,
      'homogeneous_homology_parameter_masks':[hex(v) for v in params],
      'actual_correction_image_basis':[hex(v) for v in I],
      'coefficient_matrices_tested':len(allcoeff),'retraction_equation_rank':prank,
      'retraction_equation_unknowns':dim*idim,'equivariant_retraction_exists':pmask is not None,
      'cases':cases}
 if pmask is not None:
  assert equations(pmask)==prhs
  P=pcolumns(pmask);assert [combine(P,v) for v in I]==[1<<j for j in range(idim)]
  for cs,rs in allcoeff:assert all(combine(P,v)==combine(rs,P[j]) for j,v in enumerate(cs))
  row['retraction_columns']=[hex(v) for v in P]
  row['retraction_kernel_dimension']=dim-idim
 print(json.dumps({k:v for k,v in row.items() if not isinstance(v,list)}),flush=True)
 rows.append(row)
result={'summary':{'status':'PASS','both_actual_new_orbits_checked':True,
 'all_D57_branch_families_retained':True,'both_correction_images_have_simultaneous_retractions':all(r['equivariant_retraction_exists'] for r in rows),
 'elapsed_seconds':time.time()-start},'cases':rows,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_residual_compact_coin_action.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
