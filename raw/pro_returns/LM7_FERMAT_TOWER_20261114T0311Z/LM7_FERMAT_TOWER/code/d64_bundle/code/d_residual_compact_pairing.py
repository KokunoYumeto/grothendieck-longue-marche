#!/usr/bin/env python3
"""Actual integral ribbon pairing on all four arithmetic character fibres.

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

from itertools import product
paths=[OUT/'d_arithmetic_A4_twisted.json',OUT/'d_arithmetic_A4_projective.json',OUT/'d_orbit12_projective_kernel.json',OUT/'d_compact_splitting_maps.json',OUT/'d_arithmetic_affine_base.json',OUT/'d_arithmetic_affine_homology.json',OUT/'d_arithmetic_affine_boundary.json',OUT/'d_residual_compact_norm.json']
Old=json.loads(paths[1].read_text());New=json.loads(paths[2].read_text());Split=json.loads(paths[3].read_text())
Affine=json.loads(paths[4].read_text());SmallH=json.loads(paths[5].read_text());Boundary=json.loads(paths[6].read_text());Norm=json.loads(paths[7].read_text())
Qlin=np.array([np.array(Affine['Q_linear_image_matrices'][i],dtype=np.int16).T for i in Affine['Q_to_linear_image']],dtype=np.int16)
qstar=np.array([np.array(x,dtype=np.int16).T for x in Affine['Q_linear_image_matrices']],dtype=np.int16)
qindex={tuple(a.ravel()):i for i,a in enumerate(qstar)}
st=np.array([[qindex[tuple((a@b%3).ravel())] for b in qstar] for a in qstar],dtype=np.int16)
states=[tuple(a) for a in D['Q_states']]
def qnorm(a):return min(tuple(a),tuple(-v%12 for v in a))
s=states.index(qnorm((0,1,11,0)));r=states.index(qnorm((0,11,1,11)))
ss=Affine['Q_to_linear_image'][s];rs=Affine['Q_to_linear_image'][r]
vr=np.array(Affine['affine_r_translation'],dtype=np.int16)
LIFT=np.array([0,1,4,5],dtype=np.uint8)
TEICH=np.array([1,4,15],dtype=np.uint8)
def o4add(a,b):return (((a&3)+(b&3))%4+4*(((a>>2)+(b>>2))%4)).astype(np.uint8)
def o4neg(a):return ((-(a&3))%4+4*((-(a>>2))%4)).astype(np.uint8)
def o4mul(a,b):
 a0=(a&3).astype(np.int16);a1=(a>>2).astype(np.int16);b0=(b&3).astype(np.int16);b1=(b>>2).astype(np.int16)
 return ((a0*b0-a1*b1)%4+4*((a0*b1+a1*b0-a1*b1)%4)).astype(np.uint8)
def o4mm(a,b):
 a0=(a&3).astype(np.int64);a1=(a>>2).astype(np.int64);b0=(b&3).astype(np.int64);b1=(b>>2).astype(np.int64)
 return ((a0@b0-a1@b1)%4+4*((a0@b1+a1@b0-a1@b1)%4)).astype(np.uint8)
def o4bar(a):return (((a&3).astype(np.int16)-(a>>2))%4+4*((-(a>>2).astype(np.int16))%4)).astype(np.uint8)
def mod2(a):return ((a&1)+2*((a>>2)&1)).astype(np.uint8)
def half(a):
 assert not np.any((a&1)|((a>>2)&1))
 return (((a&3)//2)+2*((a>>2)//2)).astype(np.uint8)
def ribbon(ell,table,S,R,linear,U):
 size=len(table);v2=[min(g,int(table[g,S])) for g in range(size)]
 v3=[min(g,int(table[g,R]),int(table[table[g,R],R])) for g in range(size)]
 re2=sorted(set(v2));re3=sorted(set(v3));i2={v:i for i,v in enumerate(re2)};i3={v:len(re2)+i for i,v in enumerate(re3)}
 phase=np.zeros(size,dtype=np.uint8)
 for g in re3:
  at=g;ex=0
  for _ in range(3):
   phase[at]=TEICH[ex%3]
   ex-=int(np.array(ell)@(linear[at]@vr)%3);at=int(table[at,R])
  assert at==g and ex%3==0
 B=np.zeros((len(re2)+len(re3),size),dtype=np.uint8)
 for g in range(size):B[i2[v2[g]],g]=1;B[i3[v3[g]],g]=phase[g]
 b=mod2(B);assert not np.any(mm(b,U))
 u=LIFT[U];defect=half(o4mm(B,u))
 red,piv=rr(np.column_stack([b,defect]));assert len(piv)==len(b) and max(piv)<size
 du=np.zeros_like(U);du[piv]=red[:len(piv),size:]
 u=o4add(u,o4mul(np.full_like(u,2),LIFT[du]));assert not np.any(o4mm(B,u)) and np.array_equal(mod2(u),U)
 left=u[re3];right=u[[int(table[g,R]) for g in re3]]
 ex=np.array([int(np.array(ell)@(linear[g]@vr)%3) for g in re3],dtype=np.int16)
 first=o4mm(left.T,o4mul(TEICH[ex%3,None],o4bar(right)))
 second=o4mm(right.T,o4mul(TEICH[-ex%3,None],o4bar(left)))
 twice=o4add(first,o4neg(second));h=half(twice)
 assert np.array_equal(h,FB[h.T])
 return h,u

vectors=np.array(list(product(range(3),repeat=4)),dtype=np.int16)
chords=SmallH['cycle_chords']
Omega=np.array([[(int(c,16)>>i)&1 for c in SmallH['pairing_columns_mod2']] for i in range(649)],dtype=np.uint8)
small_T=[]
for branch in Boundary['all_cases']:
 c=branch['solutions'][0]['homology_columns']
 small_T.append((branch['quarter_turn_branch'],np.array([[(int(x,16)>>i)&1 for x in c] for i in range(649)],dtype=np.uint8)))
rows=[]
for block in D['character_blocks']:
 ell=block['character'];orbit=len(block['orbit'])
 U=np.array(block['source_basis_columns'],dtype=np.uint8).T
 u=np.array(block['target_basis_columns'],dtype=np.uint8).T
 H,U4=ribbon(ell,T,s,r,Qlin,U);hs,u4=ribbon(ell,st,ss,rs,qstar,u)
 assert rank(H)==48 and rank(hs)==4
 cusp=np.array(block['cusp_columns'],dtype=np.uint8).T
 smallR=np.array(block['target_cusp_columns'],dtype=np.uint8).T
 assert not np.any(mm(H,FB[cusp])) and not np.any(mm(hs,FB[smallR]))
 embed=np.zeros((649,8),dtype=np.uint8)
 for i,g in enumerate(chords):
  q,v=divmod(g,81);z=[1,2,3][-int(np.array(ell)@vectors[v])%3]
  embed[i]=MUL[z,u[q]]
 assert rank(embed)==8
 actual=mm(mm(embed.T,Omega),FB[embed]);assert np.array_equal(actual,hs)
 q,j=quotient(cusp);qs,js=quotient(smallR)
 hc=mm(mm(j.T,H),FB[j]);ht=mm(mm(js.T,hs),FB[js]);assert rank(hc)==48 and rank(ht)==4
 theta=np.array(block['homology_projection_columns'],dtype=np.uint8).T
 phi=mm(mm(qs,theta),j)
 if orbit==8:
  rec=next(r0 for r0 in Old['blocks'] if r0['character']==ell)
  M=np.array(rec['compact_decomposition_columns'],dtype=np.uint8).T[:,32:]
 else:
  rec=next(r0 for r0 in New['blocks'] if r0['character']==ell)
  M=np.array(rec['compact_complement_columns'],dtype=np.uint8).T
 hm=mm(mm(M.T,hc),FB[M]);assert rank(hm)==16
 target=mm(phi,M)
 normrec=next(r0 for r0 in Norm['cases'] if r0['character']==ell)
 assert np.array_equal(target,np.array(normrec['target_map_columns'],dtype=np.uint8).T)
 adj=FB[mm(mm(inv(hm),target.T),ht)]
 assert rank(adj)==4 and not np.any(mm(target,adj))
 km=null(target);kr=mm(mm(km.T,hm),FB[km]);assert rank(kr)==8
 split=next(r0 for r0 in Split['cases'] if r0['character']==ell)
 for g,cols in split['all_complement_actions'].items():
  A=np.array(cols,dtype=np.uint8).T
  flip=next(a['flip'] for a in block['all_stabilizer_actions'] if a['q_state']==int(g))
  assert np.array_equal(mm(mm(A.T,hm),FB[A]),FB[hm] if flip else hm)
 ta=[]
 for branch,action in small_T:
  au=mm(action,embed); mat=solve(embed,au)
  assert not np.any(mm(qs,mm(mat,smallR)))
  tc=mm(mm(qs,mat),js)
  assert np.array_equal(mm(mm(tc.T,ht),FB[tc]),ht)
  ta.append({'branch':branch,'affine_action_columns':mat.T.tolist(),'compact_action_columns':tc.T.tolist()})
 row={'character':ell,'orbit_size':orbit,'actual_affine_pairing_rank':rank(H),'actual_small_pairing_rank':rank(hs),
      'actual_M_pairing_rank':rank(hm),'kernel_M_to_small_dimension':12,'kernel_pairing_rank':rank(kr),
      'adjoint_rank':rank(adj),'adjoint_lands_in_kernel_mod2':True,'small_pairing_matches_full649_ribbon':True,
      'M_pairing':hm.tolist(),'small_pairing':ht.tolist(),'M_to_small':target.tolist(),'small_adjoint':adj.tolist(),
      'affine_pairing':H.tolist(),'integral_cycle_lifts_mod4_columns':U4.T.tolist(),
      'small_actions':ta}
 rows.append(row)
 print(json.dumps({k:v for k,v in row.items() if k not in ['M_pairing','small_pairing','M_to_small','small_adjoint','affine_pairing','integral_cycle_lifts_mod4_columns','small_actions']}),flush=True)
result={'summary':{'status':'PASS','actual_integral_ribbon_pairings':4,'all_small_pairings_compared_to_full649_ribbon':True,
 'both_D57_actions_retained':True,'elapsed_seconds':time.time()-start},'cases':rows,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_residual_compact_pairing.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)

