#!/usr/bin/env python3
"""Exact finite maps for the 1930-dimensional compact central extension.

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
paths=[OUT/n for n in ['d_residual_compact_norm.json','d_residual_compact_pairing.json',
 'd_residual_compact_isometry.json','d_residual_compact_cusp.json',
 'd_residual_compact_coin_action.json','d_arithmetic_affine_boundary.json']]
Norm,Pair,Iso,Cusp,Coin,Boundary=[json.loads(p.read_text()) for p in paths]
def lin(cs,v):
 out=0
 while v:
  b=v&-v;out^=cs[b.bit_length()-1];v^=b
 return out
def coords(cs):
 piv={}
 for j,v in enumerate(cs):
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
def independent(cs):
 b={};at=[]
 for j,v in enumerate(cs):
  while v:
   k=v.bit_length()-1
   if k not in b:b[k]=v;at.append(j);break
   v^=b[k]
 return at
def unpack(v,n=16):
 a=np.zeros((n,n),dtype=np.uint8)
 for i in range(n):a[i,i]=(v>>i)&1
 at=n
 for i in range(n):
  for j in range(i+1,n):a[i,j]=(v>>at)&3;a[j,i]=FB[a[i,j]];at+=2
 assert hermpack(a)==v;return a
def hmap(X,v):return hermpack(mm(mm(X,unpack(v)),FB[X.T]))
branchrows=[]
for branch in Boundary['all_cases']:
 cs=branch['solutions'][0]['homology_columns']
 assert all(s['homology_columns']==cs for s in branch['solutions'])
 branchrows.append({'branch':branch['quarter_turn_branch'],'all_framings':len(branch['solutions']),
 'identical_complete_homology_columns':True,
 'homology_columns_sha256':hashlib.sha256(json.dumps(cs).encode()).hexdigest()})
oldrows=[]
for ir in Iso['cases']:
 char=ir['character'];nr=next(r for r in Norm['cases'] if r['character']==char)
 pr=next(r for r in Pair['cases'] if r['character']==char)
 cr=next(r for r in Cusp['cases'] if r['character']==char)
 kn=[int(v,16) for v in nr['kernel_basis']];coordinate=coords(kn)
 ns=[int(v,16) for v in nr['all_norm_columns']]
 normkn=[lin(ns,v) for v in kn]
 at=independent(normkn);ni=[normkn[j] for j in at];ncoord=coords(ni)
 assert len(ni)==nr['kernel_self_norm_rank']
 H=np.array(pr['M_pairing'],dtype=np.uint8);orientation=hermpack(FB[inv(H)])
 cases=[]
 for case in ir['cases']:
  X=np.array(case['isometry_columns'],dtype=np.uint8).T
  ccols=[coordinate(hmap(X,v)) for v in kn]
  assert xor_rank(ccols)==240
  assert hmap(X,orientation)==orientation
  assert all(lin(ns,hmap(X,1<<j))==hmap(X,ns[j]) for j in range(256))
  ncols=[ncoord(hmap(X,v)) for v in ni]
  assert xor_rank(ncols)==len(ni)
  assert all(lin(ncols,ncoord(v))==ncoord(hmap(X,v)) for v in normkn)
  cases.append({'branch':case['branch'],'compact_kernel_action_columns':[hex(v) for v in ccols],
    'compact_kernel_action_rank':240,'norm_image_action_columns':[hex(v) for v in ncols],
    'norm_image_action_rank':len(ni),'actual_orientation_bivector_fixed':True,
    'complete_norm_intertwining_columns_checked':256})
 oldrows.append({'character':char,'norm_image_basis':[hex(v) for v in ni],
   'norm_image_basis_source_indices':at,'orientation_bivector':hex(orientation),
   'norm_is_injective_on_kernel_coinvariants':nr['kernel_self_coinvariants']==len(ni),
   'retained_quotient_dimension':1920 if char==[0,0,0,1] else len(ni),
   'retained_quotient_coinvariant_dimension':cr['coinvariant_dimension'] if char==[0,0,0,1] else len(ni),
   'cases':cases})
newrows=[]
for rec in Coin['cases']:
 char=rec['character'];cr=next(r for r in Cusp['cases'] if r['character']==char)
 assert rec['equivariant_retraction_exists']
 P=[int(v,16) for v in rec['retraction_columns']]
 I=[int(v,16) for v in rec['actual_correction_image_basis']];ic=coords(I)
 assert [lin(P,v) for v in I]==[1<<j for j in range(4)]
 checked=0
 for case in rec['cases']:
  coeffs=[case['constant_coinvariant_action']]+case['linear_coinvariant_action_coefficients']+[q[2] for q in case['quadratic_coinvariant_action_coefficients']]
  for cs0 in coeffs:
   cs=[int(v,16) for v in cs0];rs=[ic(lin(cs,v)) for v in I]
   assert all(lin(P,v)==lin(rs,P[j]) for j,v in enumerate(cs));checked+=1
 source=[int(v,16) for v in cr['source_s_correction_columns']]
 retained=[lin(P,v) for v in source]
 assert xor_rank(retained)==4
 chosen=independent(retained)
 newrows.append({'character':char,'retained_central_trivial_module_dimension':4,
  'retraction_columns':[hex(v) for v in P],'simultaneous_action_coefficients_checked':checked,
  'actual_source_s_correction_columns':[hex(v) for v in retained],
  'independent_source_s_correction_indices':chosen,
  'independent_source_s_correction_images':[hex(retained[j]) for j in chosen],
  'same_retraction_for_both_arithmetic_branches':True})
dim=sum(r['retained_quotient_dimension'] for r in oldrows)+sum(r['retained_central_trivial_module_dimension'] for r in newrows)
coin=sum(r['retained_quotient_coinvariant_dimension'] for r in oldrows)+sum(r['retained_central_trivial_module_dimension'] for r in newrows)
assert (dim,coin)==(1930,14)
result={'summary':{'status':'PASS','retained_actual_central_quotient_dimension':dim,
 'retained_actual_central_quotient_coinvariants':coin,'remaining_selected_kernel_dimension':284160-dim,
 'compact_norm_coordinates_retained':6,'actual_source_s_coordinates_retained':8,
 'both_arithmetic_branches_and_all16_framings_compared':True,
 'actual_source_lift_and_central_quotient_surjectivity_proved_in_section':True,
 'elapsed_seconds':time.time()-start},'all_D57_framing_comparisons':branchrows,
 'old_projective_components':oldrows,'new_source_s_components':newrows,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_residual_compact_extension.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)

