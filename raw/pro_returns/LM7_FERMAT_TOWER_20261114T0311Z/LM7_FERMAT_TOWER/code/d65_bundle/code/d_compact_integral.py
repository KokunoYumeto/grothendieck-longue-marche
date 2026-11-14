#!/usr/bin/env python3
"""Integral modulo-four compact lattices from the actual marked graph.

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

paths=[OUT/'d_compact_splitting_maps.json',OUT/'d_orbit12_projective_kernel.json',OUT/'d_residual_compact_pairing.json',OUT/'d_arithmetic_affine_base.json',OUT/'d_residual_compact_norm.json']
Split,New,Pair,Aff,Norm=[json.loads(p.read_text()) for p in paths]
QL=np.array([np.array(Aff['Q_linear_image_matrices'][j],dtype=np.int16).T for j in Aff['Q_to_linear_image']],dtype=np.int16)
vr=np.array(Aff['affine_r_translation'],dtype=np.int16)
S=1;R=2
LIFT=np.array([0,1,4,5],dtype=np.uint8);TEICH=np.array([1,4,15],dtype=np.uint8)
def add(a,b):return (((a&3)+(b&3))%4+4*(((a>>2)+(b>>2))%4)).astype(np.uint8)
def neg(a):return ((-(a&3).astype(np.int16))%4+4*((-(a>>2).astype(np.int16))%4)).astype(np.uint8)
def mul(a,b):
 a0=(a&3).astype(np.int16);a1=(a>>2).astype(np.int16);b0=(b&3).astype(np.int16);b1=(b>>2).astype(np.int16)
 return ((a0*b0-a1*b1)%4+4*((a0*b1+a1*b0-a1*b1)%4)).astype(np.uint8)
def mat(a,b):
 a0=(a&3).astype(np.int64);a1=(a>>2).astype(np.int64);b0=(b&3).astype(np.int64);b1=(b>>2).astype(np.int64)
 return ((a0@b0-a1@b1)%4+4*((a0@b1+a1@b0-a1@b1)%4)).astype(np.uint8)
def bar(a):return (((a&3).astype(np.int16)-(a>>2))%4+4*((-(a>>2).astype(np.int16))%4)).astype(np.uint8)
def red(a):return ((a&1)+2*((a>>2)&1)).astype(np.uint8)
def half(a):
 assert not np.any((a&1)|((a>>2)&1))
 return (((a&3)//2)+2*((a>>2)//2)).astype(np.uint8)
def scalar(z,a):return mul(np.full_like(a,z),a)
def inverse4(a):
 n=len(a);b=LIFT[inv(red(a))]
 b=mat(b,add(scalar(2,np.eye(n,dtype=np.uint8)),neg(mat(a,b))))
 assert np.array_equal(mat(a,b),np.eye(n,dtype=np.uint8));return b
def leftinv4(a):
 p=rr(red(a).T)[1];assert len(p)==a.shape[1]
 out=np.zeros((a.shape[1],len(a)),dtype=np.uint8);out[:,p]=inverse4(a[p]);return out
def quotient4(c):
 p=rr(red(c).T)[1];free=[j for j in range(len(c)) if j not in p]
 assert len(p)==c.shape[1]
 q=np.zeros((len(free),len(c)),dtype=np.uint8);q[np.arange(len(free)),free]=1
 q[:,p]=neg(mat(c[free],inverse4(c[p])))
 j=np.zeros((len(c),len(free)),dtype=np.uint8);j[free,np.arange(len(free))]=1
 assert not np.any(mat(q,c));assert np.array_equal(mat(q,j),np.eye(len(free),dtype=np.uint8));return q,j
def rightinv4(a):return leftinv4(a.T).T
def cpow(g,n):
 v=0
 for j in range(n):v=int(T[v,g])
 return v
def cusp4(ell):
 chain=np.zeros(576,dtype=np.uint8);q=0;v=np.zeros(4,dtype=np.int16)
 for j in range(12):
  q=int(T[q,S]);chain[q]=add(chain[q],TEICH[int(ell@v%3)])
  v=(v+QL[q]@vr)%3;q=int(T[q,R]);chain[q]=add(chain[q],neg(TEICH[int(ell@v%3)]))
 assert q==0 and not np.any(v);return chain
rows=[]
for rec in Split['cases']:
 if rec['orbit_size']!=12:continue
 ell=np.array(rec['character'],dtype=np.int16);char=rec['character']
 B=next(r for r in D['character_blocks'] if r['character']==char)
 N=next(r for r in New['blocks'] if r['character']==char)
 P=next(r for r in Pair['cases'] if r['character']==char)
 U4=np.array(P['integral_cycle_lifts_mod4_columns'],dtype=np.uint8).T;free=B['source_free_edges']
 assert np.array_equal(U4[free],np.eye(96,dtype=np.uint8))
 F=np.array(B['regular_A4_basis_columns'],dtype=np.uint8).T;Fi=inv(F)
 acts={a['q_state']:(np.array(a['columns'],dtype=np.uint8).T,a['flip']) for a in B['all_stabilizer_actions']}
 H=sorted(acts);H0=[g for g in H if not acts[g][1]];raw={}
 for g in H:
  out=np.zeros_like(U4);out[T[g]]=bar(U4) if acts[g][1] else U4
  A=out[free];assert np.array_equal(mat(U4,A),out)
  expected=mm(mm(F,acts[g][0]),FB[Fi] if acts[g][1] else Fi)
  assert np.array_equal(red(A),expected);raw[g]=A
 t=int(T[S,R]);tp=[cpow(t,j) for j in range(12)]
 reps=sorted({min(int(T[g,h]) for h in tp) for g in range(576)});assert len(reps)==48
 cusp=[]
 for g in reps:
  chain=np.zeros(576,dtype=np.uint8);chain[T[g]]=cusp4(ell@QL[g]%3)
  assert np.array_equal(mat(U4,chain[free,None])[:,0],chain)
  cusp.append(chain[free])
 cusp=np.array(cusp,dtype=np.uint8).T;assert np.array_equal(red(cusp),np.array(B['cusp_columns'],dtype=np.uint8).T)
 q,jsection=quotient4(cusp);mc={}
 for g in H:
  X=mat(mat(q,raw[g]),bar(jsection) if acts[g][1] else jsection)
  assert np.array_equal(mat(q,raw[g]),mat(X,bar(q) if acts[g][1] else q));mc[g]=X
 c=N['C3_generator'];tau=N['normalizing_involution'];sig=N['central_semilinear_exchange'];cosets=N['induction_coset_representatives']
 pc=scalar(3,add(add(np.eye(48,dtype=np.uint8),scalar(15,mc[c])),scalar(4,mc[int(T[c,c])])) )
 assert np.array_equal(mat(pc,pc),pc) and np.array_equal(mat(mc[c],pc),scalar(4,pc))
 J=mat(mc[tau],mc[sig]);assert np.array_equal(mat(J,bar(J)),np.eye(48,dtype=np.uint8))
 E2=np.array(N['compact_embedding_columns'],dtype=np.uint8).T;M2=np.array(N['compact_complement_columns'],dtype=np.uint8).T
 columns=[]
 for k in range(4):
  v=mat(pc,LIFT[E2[:,8*k:8*k+1]])
  v=add(scalar(12,v),mat(J,bar(scalar(12,v))))
  assert np.array_equal(red(v),E2[:,8*k:8*k+1]);assert np.array_equal(mat(J,bar(v)),v)
  columns.extend(mat(mc[g],v)[:,0] for g in cosets)
 E=np.column_stack(columns);assert np.array_equal(red(E),E2)
 eleft=leftinv4(E);me={}
 for g in H:
  X=mat(mat(eleft,mc[g]),bar(E) if acts[g][1] else E)
  assert np.array_equal(mat(mc[g],bar(E) if acts[g][1] else E),mat(E,X));me[g]=X
 R2=np.array(N['compact_retraction_rows'],dtype=np.uint8)
 lam=[]
 for k in range(4):
  v=LIFT[R2[8*k:8*k+1]]
  v=scalar(3,add(add(v,scalar(15,mat(v,mc[c]))),scalar(4,mat(v,mc[int(T[c,c])]))))
  assert np.array_equal(mat(v,mc[c]),scalar(4,v));lam.append(v)
 ret=np.vstack([mat(lam[k],mc[inverse(g)]) for k in range(4) for g in cosets])
 ret=mat(inverse4(mat(ret,E)),ret)
 assert np.array_equal(red(ret),R2)
 sigma=mat(mat(me[sig],bar(ret)),bar(mc[sig]))
 ret=add(scalar(12,ret),scalar(int(bar(np.array(12,dtype=np.uint8))),sigma))
 assert np.array_equal(mat(ret,E),np.eye(32,dtype=np.uint8)) and np.array_equal(red(ret),R2)
 for g in H:assert np.array_equal(mat(ret,mc[g]),mat(me[g],bar(ret) if acts[g][1] else ret))
 M=mat(add(np.eye(48,dtype=np.uint8),neg(mat(E,ret))),LIFT[M2]);assert np.array_equal(red(M),M2)
 mi=leftinv4(M);ma={}
 for g in H:
  X=mat(mat(mi,mc[g]),bar(M) if acts[g][1] else M)
  assert np.array_equal(mat(mc[g],bar(M) if acts[g][1] else M),mat(M,X))
  assert np.array_equal(red(X),np.array(rec['all_complement_actions'][str(g)],dtype=np.uint8).T)
  ma[g]=X
 for g in H:
  for h in [c,tau,sig]:assert np.array_equal(mat(ma[g],bar(ma[h]) if acts[g][1] else ma[h]),ma[int(T[g,h])])
 # Literal integral exterior model: Hermitian coordinates carry an extra
 # minus sign on character exchange, from the determinant of conjugation
 # on the two-dimensional coefficient lattice.
 norm=[];traces=[]
 basis=[(i,i,1) for i in range(16)]+[(i,j,z) for i in range(16) for j in range(i+1,16) for z in [1,4]]
 for i,j,z in basis:
  A=np.zeros((16,16),dtype=np.uint8);A[i,j]=z;A[j,i]=bar(np.array(z,dtype=np.uint8))
  total=np.zeros_like(A)
  for g in H:
   v=mat(mat(ma[g],bar(A) if acts[g][1] else A),bar(ma[g].T))
   if acts[g][1]:v=neg(v)
   total=add(total,v)
  assert not np.any(red(total))
  v=half(total);assert np.array_equal(v,FB[v.T]);norm.append(hermpack(v))
 for i in range(16):
  for j in range(16):
   for z in [1,4]:
    A=np.zeros((16,16),dtype=np.uint8);A[i,j]=z;total=np.zeros_like(A)
    for g in H:total=add(total,mat(mat(ma[g],bar(A) if acts[g][1] else A),inverse4(ma[g])))
    assert not np.any(red(total));traces.append(pack(half(total)))
 row={'character':char,'integral_cusp_columns':cusp.T.tolist(),'compact_quotient_rows':q.tolist(),'compact_section_columns':jsection.T.tolist(),
  'integral_projective_columns':E.T.tolist(),'integral_projective_retraction_rows':ret.tolist(),'integral_complement_columns':M.T.tolist(),
  'all_integral_complement_actions':{str(g):v.T.tolist() for g,v in ma.items()},
  'full_Hermitian_divided_norm_rank':xor_rank(norm),'full_Hermitian_divided_norm_columns':[hex(v) for v in norm],
  'full_End_divided_trace_rank':xor_rank(traces),'full_End_divided_trace_columns':[hex(v) for v in traces],
  'actual_integral_group_relations_checked':len(H)*3}
 rows.append(row);print(json.dumps({'character':char,'status':'PASS','Hermitian_divided_norm_rank':xor_rank(norm),'End_divided_trace_rank':xor_rank(traces)}),flush=True)
result={'summary':{'status':'PASS','coefficient_ring':'(Z/4)[omega]/(omega^2+omega+1)','elapsed_seconds':time.time()-start},'cases':rows,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths+[path]}}
(OUT/'d_compact_integral.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
