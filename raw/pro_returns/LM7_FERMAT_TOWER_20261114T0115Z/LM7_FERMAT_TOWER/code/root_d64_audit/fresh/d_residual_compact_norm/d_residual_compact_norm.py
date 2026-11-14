#!/usr/bin/env python3
"""Exact residual compact norm and its marked small-curve comparison.

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

paths=[OUT/'d_arithmetic_A4_twisted.json',OUT/'d_arithmetic_A4_projective.json',OUT/'d_orbit12_projective_kernel.json',OUT/'d_compact_splitting_maps.json']
Old=json.loads(paths[1].read_text());New=json.loads(paths[2].read_text());Split=json.loads(paths[3].read_text())
def hbasis(n):
 ans=[]
 for i in range(n):
  a=np.zeros((n,n),dtype=np.uint8);a[i,i]=1;ans.append(a)
 for i in range(n):
  for j in range(i+1,n):
   for z in [1,2]:
    a=np.zeros((n,n),dtype=np.uint8);a[i,j]=z;a[j,i]=FB[z];ans.append(a)
 assert all(hermpack(a)==1<<j for j,a in enumerate(ans))
 return ans
def lin(cols,v):
 ans=0
 while v:
  b=v&-v;ans^=cols[b.bit_length()-1];v^=b
 return ans
def echelon(columns):
 piv={};originals=[]
 for j,v in enumerate(columns):
  w=v
  while w:
   k=w.bit_length()-1
   if k not in piv:piv[k]=w;originals.append(j);break
   w^=piv[k]
 return piv,originals
def kernel(columns):
 piv={};ans=[]
 for j,v in enumerate(columns):
  mask=1<<j
  while v:
   k=v.bit_length()-1
   if k not in piv:piv[k]=(v,mask);break
   w,m=piv[k];v^=w;mask^=m
  if not v:ans.append(mask)
 assert all(lin(columns,v)==0 for v in ans)
 return ans
rows=[]
for source in D['character_blocks']:
 char=source['character'];orbit=len(source['orbit'])
 rec=next(r for r in Split['cases'] if r['character']==char)
 H=sorted(map(int,rec['all_complement_actions']))
 flips={a['q_state']:a['flip'] for a in source['all_stabilizer_actions']}
 F=np.array(source['regular_A4_basis_columns'],dtype=np.uint8).T
 cusp=np.array(source['cusp_columns'],dtype=np.uint8).T
 q0,j0=quotient(cusp);qc=mm(q0,F);jc=mm(inv(F),j0)
 theta=np.array(source['regular_projection_columns'],dtype=np.uint8).T
 smallR=np.array(source['target_cusp_columns'],dtype=np.uint8).T
 qs,js=quotient(smallR);phi=mm(mm(qs,theta),jc)
 if orbit==8:
  prior=next(r for r in Old['blocks'] if r['character']==char)
  M=np.array(prior['compact_decomposition_columns'],dtype=np.uint8).T[:,32:]
 else:
  prior=next(r for r in New['blocks'] if r['character']==char)
  M=np.array(prior['compact_complement_columns'],dtype=np.uint8).T
 target=mm(phi,M);assert target.shape==(4,16) and rank(target)==4
 acts={int(g):np.array(a,dtype=np.uint8).T for g,a in rec['all_complement_actions'].items()}
 small={int(g):np.array(a,dtype=np.uint8).T for g,a in rec['all_small_compact_actions'].items()}
 for g in H:assert np.array_equal(mm(target,acts[g]),mm(small[g],FB[target] if flips[g] else target))
 bas=hbasis(16);sbas=hbasis(4)
 projection=[hermpack(mm(mm(target,b),FB[target.T])) for b in bas]
 assert xor_rank(projection)==16
 norms=[0]*256;smallnorms=[0]*16;relations=[];actions={}
 for g in H:
  A=acts[g];B=small[g];flip=flips[g]
  cols=[hermpack(mm(mm(A,FB[b] if flip else b),FB[A.T])) for b in bas]
  scols=[hermpack(mm(mm(B,FB[b] if flip else b),FB[B.T])) for b in sbas]
  assert all(lin(projection,v)==lin(scols,projection[j]) for j,v in enumerate(cols))
  norms=[a^b for a,b in zip(norms,cols)]
  smallnorms=[a^b for a,b in zip(smallnorms,scols)]
  relations.extend(v^(1<<j) for j,v in enumerate(cols));actions[g]=cols
 for g,cols in actions.items():assert all(lin(cols,v)==v for v in norms)
 assert all(lin(norms,v)==0 for v in relations)
 assert [lin(projection,v) for v in norms]==[lin(smallnorms,v) for v in projection]
 kn=kernel(projection);nker=[lin(norms,v) for v in kn]
 nr=xor_rank(norms);nkr=xor_rank(nker);image=xor_rank([lin(projection,v) for v in norms])
 relker=[]
 for cols in actions.values():relker.extend(lin(cols,v)^v for v in kn)
 coin=256-xor_rank(relations);kernelcoin=240-xor_rank(relker)
 row={'character':char,'orbit_size':orbit,'compact_M_dimension_F4':16,'small_compact_dimension_F4':4,
      'M_self_coinvariants':coin,'M_self_norm_rank':nr,'small_norm_rank':xor_rank(smallnorms),
      'norm_image_rank_on_small':image,'kernel_self_dimension_per_pair':240,
      'kernel_self_coinvariants':kernelcoin,'kernel_self_norm_rank':nkr,
      'target_map_columns':target.T.tolist(),'all_norm_columns':[hex(v) for v in norms],
      'small_projection_columns':[hex(v) for v in projection],
      'kernel_basis':[hex(v) for v in kn],'kernel_norm_columns':[hex(v) for v in nker],
      'all_action_columns':{str(g):[hex(v) for v in cols] for g,cols in actions.items()}}
 rows.append(row)
 print(json.dumps({k:v for k,v in row.items() if k not in ['target_map_columns','all_norm_columns','small_projection_columns','kernel_basis','kernel_norm_columns','all_action_columns']}),flush=True)
result={'summary':{'status':'PASS','four_actual_arithmetic_orbits':True,'kernel_self_dimension':sum(r['orbit_size']*240 for r in rows),
 'kernel_self_coinvariants':sum(r['kernel_self_coinvariants'] for r in rows),'kernel_self_norm_rank':sum(r['kernel_self_norm_rank'] for r in rows),
 'elapsed_seconds':time.time()-start},'cases':rows,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_residual_compact_norm.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)

