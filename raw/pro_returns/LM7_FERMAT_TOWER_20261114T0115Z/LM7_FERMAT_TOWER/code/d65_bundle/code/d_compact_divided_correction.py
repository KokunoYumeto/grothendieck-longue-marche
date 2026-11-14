#!/usr/bin/env python3
"""Exact divided-norm and actual source-correction comparison.

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

paths=[OUT/'d_compact_integral.json',OUT/'d_residual_compact_norm.json',OUT/'d_residual_compact_cusp.json',OUT/'d_residual_compact_pairing.json',OUT/'d_compact_rigid_source.json']
Int,Norm,Cusp,Pair,Rigid=[json.loads(p.read_text()) for p in paths]
def lin(cs,v):
 out=0
 while v:
  b=v&-v;out^=cs[b.bit_length()-1];v^=b
 return out
def matof(v):return np.array([(v>>(2*j))&3 for j in range(256)],dtype=np.uint8).reshape((16,16))
def coords(cols):
 piv={}
 for j,v in enumerate(cols):
  mask=1<<j
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=(v,mask);break
   w,m=piv[k];v^=w;mask^=m
  assert v
 def co(v):
  mask=0
  while v:
   k=v.bit_length()-1;assert k in piv
   w,m=piv[k];v^=w;mask^=m
  return mask
 return co
def solvecols(cols,target):
 piv={}
 for j,v in enumerate(cols):
  mask=1<<j
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=(v,mask);break
   w,m=piv[k];v^=w;mask^=m
 mask=0
 while target:
  k=target.bit_length()-1
  if k not in piv:return None
  w,m=piv[k];target^=w;mask^=m
 return mask
rows=[]
for irec in Int['cases']:
 char=irec['character'];N=next(r for r in Norm['cases'] if r['character']==char)
 C=next(r for r in Cusp['cases'] if r['character']==char)
 P=next(r for r in Pair['cases'] if r['character']==char)
 A=next(r for r in Rigid['cases'] if r['character']==char)
 fullnorm=[int(v,16) for v in irec['full_Hermitian_divided_norm_columns']]
 trace=[int(v,16) for v in irec['full_End_divided_trace_columns']]
 kb=[int(v,16) for v in N['kernel_basis']];kn=[lin(fullnorm,v) for v in kb]
 # This is a norm on the actual integral lattice. All integral choices
 # above a mod-two class give the same divided reduction because the
 # un-divided full norm is even on the whole Hermitian module.
 checked=0
 for g,cs in N['all_action_columns'].items():
  ac=list(map(lambda x:int(x,16),cs))
  for v,nv in zip(kb,kn):assert lin(fullnorm,lin(ac,v))==nv;checked+=1
 free=C['coinvariant_representatives_in_kernel_basis'];nc=[kn[j] for j in free]
 sc=[int(v,16) for v in C['source_s_correction_columns']]
 assert all(lin(nc,v)==0 for v in sc)
 assert xor_rank(nc)==6 and xor_rank(sc)==4
 phi=np.array(P['M_to_small'],dtype=np.uint8);K=null(phi);assert K.shape==(16,12)
 tcs=[];input_columns=[]
 for k in range(12):
  for j in range(16):
   for z in [1,2]:
    a=np.zeros((16,16),dtype=np.uint8);a[:,j]=MUL[z,K[:,k]]
    v=lin(trace,pack(a));assert not np.any(mm(phi,matof(v)))
    tcs.append(v);input_columns.append(pack(a))
 hr=xor_rank(tcs)
 hform=np.array(P['M_pairing'],dtype=np.uint8);omega=FB[inv(hform)]
 cases=[]
 for r in A['cases']:
  X=np.array(r['rigid_compact_action_columns'],dtype=np.uint8).T
  lc=[]
  for v in tcs:
   a=matof(v);b=mm(mm(a,omega),FB[X.T])^mm(mm(X,omega),FB[a.T]);lc.append(hermpack(b))
  rankl=xor_rank(lc);same=xor_rank(lc+nc)==rankl==6
  solutions=[solvecols(lc,v) for v in nc]
  assert same and all(v is not None for v in solutions)
  assert all(lin(lc,v)==target for v,target in zip(solutions,nc))
  assert xor_rank(solutions)==6 and all(lin(solutions,v)==0 for v in sc)
  cases.append({'branch':r['branch'],'beta_Q_state':r['beta_Q_state'],'linearized_pairing_rank':rankl,
                'same_image_as_divided_norm':same,'right_inverse_factors_through_actual_norm_image':True,'all_linearized_bivector_columns':[hex(v) for v in lc],
                'right_inverse_on_coinvariant_representatives':[hex(v) for v in solutions]})
 row={'character':char,'kernel_divided_norm_rank':xor_rank(kn),'coinvariant_dimension':len(nc),'source_s_image_rank':xor_rank(sc),
      'source_s_image_equals_divided_norm_kernel':xor_rank(sc)==len(nc)-xor_rank(nc),
      'norm_invariance_columns_checked':checked,'allowable_projective_trace_half_rank':hr,
      'kernel_divided_norm_columns':[hex(v) for v in kn],'coinvariant_divided_norm_columns':[hex(v) for v in nc],
      'projective_trace_input_columns':[hex(v) for v in input_columns],
      'projective_trace_half_columns':[hex(v) for v in tcs],'cases':cases}
 rows.append(row);print(json.dumps({k:v for k,v in row.items() if isinstance(v,(str,int,bool)) or k=='character'}),flush=True)
result={'summary':{'status':'PASS','both_new_arithmetic_orbits_checked':True,'all_four_finite_framings_checked':True,
 'elapsed_seconds':time.time()-start},'cases':rows,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths+[path]}}
(OUT/'d_compact_divided_correction.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
