#!/usr/bin/env python3
"""Integral modulo-four projective compact covers for the two old orbits.

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

# Additional data is immutable and used with its actual compact quotient map.
oldpath=OUT/'d_arithmetic_A4_projective.json';Old=json.loads(oldpath.read_text());paths.append(oldpath)

def real4(a,flip=False):
 a0=(a&3).astype(np.int64);a1=(a>>2).astype(np.int64)
 z=np.zeros((2*a.shape[0],2*a.shape[1]),dtype=np.int64)
 z[0::2,0::2]=a0;z[1::2,0::2]=a1
 z[0::2,1::2]=-a1;z[1::2,1::2]=a0-a1
 if flip:
  z[:,1::2]=-z[:,0::2]-z[:,1::2]
 return z%4

def fromreal4(a):
 z=(a[0::2,0::2]%4+4*(a[1::2,0::2]%4)).astype(np.uint8)
 assert np.array_equal(real4(z),a%4)
 return z

def f2rank(a):return rank(np.array(a,dtype=np.uint8)%2)

def graph_lift(table,S,R,linear,ell,U):
 size=len(table);re2=sorted({min(g,int(table[g,S])) for g in range(size)})
 re3=sorted({min(g,int(table[g,R]),int(table[table[g,R],R])) for g in range(size)})
 i2={g:i for i,g in enumerate(re2)};i3={g:len(re2)+i for i,g in enumerate(re3)}
 B=np.zeros((len(re2)+len(re3),size),dtype=np.uint8)
 for g in re2:B[i2[g],g]=1;B[i2[g],int(table[g,S])]=1
 for g in re3:
  at=g;ex=0
  for j in range(3):
   B[i3[g],at]=TEICH[ex%3]
   ex-=int(ell@(linear[at]@vr)%3);at=int(table[at,R])
  assert ex%3==0 and at==g
 b=red(B);assert not np.any(mm(b,U))
 lift=LIFT[U];error=half(mat(B,lift));r,p=rr(np.column_stack([b,error]));assert max(p)<size
 corr=np.zeros_like(U);corr[p]=r[:len(p),size:]
 lift=add(lift,scalar(2,LIFT[corr]));assert not np.any(mat(B,lift)) and np.array_equal(red(lift),U)
 return lift

def graph_cusps(table,S,R,linear,ell,U4,free):
 size=len(table);t=int(table[S,R]);at=0;n=0
 while True:
  n+=1;at=int(table[at,t])
  if at==0:break
 tp=[0]
 for j in range(1,n):tp.append(int(table[tp[-1],t]))
 reps=sorted({min(int(table[g,h]) for h in tp) for g in range(size)})
 cols=[]
 for g in reps:
  ellg=ell@linear[g]%3;chain=np.zeros(size,dtype=np.uint8);q=0;v=np.zeros(4,dtype=np.int16)
  for j in range(n):
   q=int(table[q,S]);chain[q]=add(chain[q],TEICH[int(ellg@v%3)])
   v=(v+linear[q]@vr)%3;q=int(table[q,R]);chain[q]=add(chain[q],neg(TEICH[int(ellg@v%3)]))
  assert q==0
  if int(ellg@v%3):continue
  out=np.zeros(size,dtype=np.uint8);out[table[g]]=chain
  assert np.array_equal(mat(U4,out[free,None])[:,0],out)
  cols.append(out[free])
 return np.column_stack(cols),n

qlin=np.array([np.array(a,dtype=np.int16).T for a in Aff['Q_linear_image_matrices']],dtype=np.int16)
qindex={tuple(a.ravel()):i for i,a in enumerate(qlin)}
table_small=np.array([[qindex[tuple((a@b%3).ravel())] for b in qlin] for a in qlin],dtype=np.int16)
qmap=np.array(Aff['Q_to_linear_image'],dtype=np.int16);s_small=int(qmap[S]);r_small=int(qmap[R])

rows=[]
for rec in Split['cases']:
 if rec['orbit_size']!=8:continue
 char=rec['character'];ell=np.array(char,dtype=np.int16)
 B=next(b for b in D['character_blocks'] if b['character']==char)
 P=next(b for b in Pair['cases'] if b['character']==char)
 O=next(b for b in Old['blocks'] if b['character']==char)
 U4=np.array(P['integral_cycle_lifts_mod4_columns'],dtype=np.uint8).T;free=B['source_free_edges']
 acts={a['q_state']:(np.array(a['columns'],dtype=np.uint8).T,a['flip']) for a in B['all_stabilizer_actions']}
 H=sorted(acts);Syl=rec['unordered_Sylow_states'];assert len(H)==72 and len(Syl)==8
 raw={}
 for g in H:
  a=np.zeros_like(U4);a[T[g]]=bar(U4) if acts[g][1] else U4
  raw[g]=a[free];assert np.array_equal(mat(U4,raw[g]),a)
 cusps,n=graph_cusps(T,S,R,QL,ell,U4,free);assert n==12 and cusps.shape==(96,48)
 assert np.array_equal(red(cusps),np.array(B['cusp_columns'],dtype=np.uint8).T)
 q,jsection=quotient4(cusps);mc={}
 for g in H:
  mc[g]=mat(mat(q,raw[g]),bar(jsection) if acts[g][1] else jsection)
  assert np.array_equal(mat(q,raw[g]),mat(mc[g],bar(q) if acts[g][1] else q))
 # The prescribed mod-two projection onto the old compact projective cover.
 decomposition=np.array(O['compact_decomposition_columns'],dtype=np.uint8).T
 decinv=np.array(O['compact_decomposition_inverse_rows'],dtype=np.uint8)
 M2=decomposition[:,32:];R2=decinv[32:];e2=mm(M2,R2)
 assert np.array_equal(mm(R2,M2),np.eye(16,dtype=np.uint8))
 for g in H:assert np.array_equal(mm(e2,red(mc[g])),mm(red(mc[g]),FB[e2] if acts[g][1] else e2))
 m2={g:np.array(rec['all_complement_actions'][str(g)],dtype=np.uint8).T for g in H}
 realM=real4(LIFT[M2])%2;realR=real4(LIFT[R2])%2
 MA={g:real4(LIFT[m2[g]],acts[g][1])%2 for g in Syl}
 norm=sum(MA.values())%2;seedcols=rr(norm.astype(np.uint8))[1];assert len(seedcols)==4
 regular=np.column_stack([MA[g][:,i] for i in seedcols for g in Syl]);assert f2rank(regular)==32
 regular_inv=inv(regular.astype(np.uint8));assert np.all(regular_inv<2)
 seed=np.eye(32,dtype=np.int64)[:,seedcols]
 at_identity=[k*8+Syl.index(0) for k in range(4)]
 A0=(realM@seed@regular_inv[at_identity]@realR)%2
 target=real4(LIFT[e2])%2;check=np.zeros((96,96),dtype=np.int64)
 for g in Syl:
  ga=real4(mc[g],acts[g][1])%2;gi=real4(mc[inverse(g)],acts[g][1])%2
  check^=(ga@A0@gi)%2
 assert np.array_equal(check,target)
 # Average over scalar C3, then over H. The index H:Sylow is nine.
 scalarw=real4(scalar(4,np.eye(48,dtype=np.uint8)));scalari=scalarw@scalarw%4
 avg=3*(A0+scalarw@A0@scalari+scalari@A0@scalarw)%4
 Ao=fromreal4(avg);ep=np.zeros((48,48),dtype=np.uint8)
 for g in H:
  ep=add(ep,mat(mat(mc[g],bar(Ao) if acts[g][1] else Ao),inverse4(mc[g])))
 assert np.array_equal(red(ep),e2)
 # Newton's idempotent polynomial is exact modulo four.
 ep2=mat(ep,ep);ep3=mat(ep2,ep)
 idem=add(scalar(3,ep2),neg(scalar(2,ep3)))
 assert np.array_equal(mat(idem,idem),idem) and np.array_equal(red(idem),e2)
 for g in H:assert np.array_equal(mat(idem,mc[g]),mat(mc[g],bar(idem) if acts[g][1] else idem))
 M4=mat(idem,LIFT[M2]);mi=leftinv4(M4);ma={}
 for g in H:
  X=mat(mat(mi,mc[g]),bar(M4) if acts[g][1] else M4)
  assert np.array_equal(mat(mc[g],bar(M4) if acts[g][1] else M4),mat(M4,X))
  assert np.array_equal(red(X),m2[g]);ma[g]=X
 for g in H:
  for h in rec['ordered_stabilizer_generators']+[O['central_exchange_state']]:
   assert np.array_equal(mat(ma[g],bar(ma[h]) if acts[g][1] else ma[h]),ma[int(T[g,h])])
 # Actual marked map to the small compact quotient, with integral cusp maps.
 smallU2=np.array(B['target_basis_columns'],dtype=np.uint8).T;smallfree=B['target_free_edges']
 smallU4=graph_lift(table_small,s_small,r_small,qlin,ell,smallU2)
 smallcusp,smalln=graph_cusps(table_small,s_small,r_small,qlin,ell,smallU4,smallfree)
 targetcusp=np.array(B['target_cusp_columns'],dtype=np.uint8).T
 cchange=solve(red(smallcusp),targetcusp);smallcusp=mat(smallcusp,LIFT[cchange])
 assert np.array_equal(red(smallcusp),targetcusp)
 qs,js=quotient4(smallcusp)
 push=np.zeros((48,96),dtype=np.uint8)
 for g in range(576):push[qmap[g]]=add(push[qmap[g]],U4[g])
 theta=push[smallfree]
 assert np.array_equal(mat(smallU4,theta),push)
 assert np.array_equal(red(theta),np.array(B['homology_projection_columns'],dtype=np.uint8).T)
 phi=mat(mat(mat(qs,theta),jsection),M4)
 assert np.array_equal(red(phi),np.array(P['M_to_small'],dtype=np.uint8))
 assert rank(red(phi))==4
 extra=mat(add(np.eye(48,dtype=np.uint8),neg(idem)),LIFT[decomposition[:,:32]])
 assert not np.any(mat(mat(mat(qs,theta),jsection),extra))
 row={'character':char,'unordered_stabilizer_order':len(H),'Sylow_states':Syl,'regular_seed_coordinates':seedcols,
      'regular_Sylow_basis_columns_mod2':regular.T.tolist(),'regular_Sylow_inverse_rows_mod2':regular_inv.tolist(),
      'ordinary_real_coefficient_of_one_map_mod2':A0.tolist(),'averaged_approximate_idempotent_mod4':ep.tolist(),
      'actual_equivariant_idempotent_mod4':idem.tolist(),'compact_quotient_rows_mod4':q.tolist(),'compact_section_columns_mod4':jsection.T.tolist(),
      'integral_projective_cover_columns':M4.T.tolist(),'all_integral_cover_actions':{str(g):X.T.tolist() for g,X in ma.items()},
      'integral_small_cycle_columns':smallU4.T.tolist(),'integral_small_cusp_columns':smallcusp.T.tolist(),
      'integral_small_quotient_rows':qs.tolist(),'integral_small_section_columns':js.T.tolist(),
      'actual_integral_cover_to_small_rows':phi.tolist(),'small_cusp_Q_width':smalln,
      'mod_two_markings_unchanged':True,'extra_projective_summand_killed_by_actual_small_map':True}
 rows.append(row);print(json.dumps({'character':char,'status':'PASS','integral_cover_rank':16,'actual_small_map_rank':4,'small_cusp_Q_width':smalln}),flush=True)
result={'summary':{'status':'PASS','coefficient_ring':'(Z/4)[omega]/(omega^2+omega+1)','actual_old_covers':len(rows),'elapsed_seconds':time.time()-start},'cases':rows,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths+[path]}}
(OUT/'d_old_compact_integral.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
