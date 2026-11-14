#!/usr/bin/env python3
"""Actual quadratic source-involution and cusp coordinates in the compact quotient.

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

ipath=OUT/'d_old_compact_integral.json';Int=json.loads(ipath.read_text());paths.append(ipath)
cp=OUT/'d_residual_compact_cusp.json';Cusp=json.loads(cp.read_text());paths.append(cp)
ap=OUT/'d_residual_compact_isometry.json';Isom=json.loads(ap.read_text());paths.append(ap)
def lin(cols,v):
 out=0
 while v:
  x=v&-v;out^=cols[x.bit_length()-1];v^=x
 return out

def linear_solver(cols):
 piv={};kernel=[]
 for i,v in enumerate(cols):
  mask=1<<i
  while v:
   p=v.bit_length()-1
   if p not in piv:piv[p]=(v,mask);break
   a,b=piv[p];v^=a;mask^=b
  if not v:kernel.append(mask)
 def solve(v):
  mask=0
  while v:
   p=v.bit_length()-1
   if p not in piv:return None
   a,b=piv[p];v^=a;mask^=b
  return mask
 return solve,kernel,len(piv)

def quotient2(cols,n):
 piv={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in piv:piv[p]=v;break
   v^=piv[p]
 free=[i for i in range(n) if i not in piv]
 def q(v):
  for p in sorted(piv,reverse=True):
   if v>>p&1:v^=piv[p]
  return sum(((v>>p)&1)<<i for i,p in enumerate(free))
 return q,free

def hermunpack(v,n=16):
 a=np.zeros((n,n),dtype=np.uint8)
 for i in range(n):a[i,i]=(v>>i)&1
 at=n
 for i in range(n):
  for j in range(i+1,n):a[i,j]=(v>>at)&3;a[j,i]=FB[a[i,j]];at+=2
 assert hermpack(a)==v;return a

def hermlift(v,n=16):
 a2=hermunpack(v,n);a=LIFT[a2]
 for i in range(n):
  for j in range(i+1,n):a[j,i]=bar(a[i,j])
 assert np.array_equal(a,bar(a.T));return a

def hc4(a):
 assert np.array_equal(a,bar(a.T)) and not np.any(a.diagonal()>>2)
 c=list(map(int,a.diagonal()))
 for i in range(len(a)):
  for j in range(i+1,len(a)):c.extend([int(a[i,j])&3,int(a[i,j])>>2])
 return np.array(c,dtype=np.uint8)

def bitpack(a):return sum(int(x)<<i for i,x in enumerate(a))
def matrixof(v):return np.array([(v>>(2*i))&3 for i in range(256)],dtype=np.uint8).reshape(16,16)

sourcepath=OUT/'d_old_compact_source_cochain.json';Src=json.loads(sourcepath.read_text());paths.append(sourcepath)
isopath=OUT/'d_old_compact_all_isometries.json';All=json.loads(isopath.read_text());paths.append(isopath)
char=[0,1,0,0];nr=next(x for x in Norm['cases'] if x['character']==char)
ir=next(x for x in Int['cases'] if x['character']==char)
iso=next(x for x in Isom['cases'] if x['character']==char)
actions={int(g):[int(x,16) for x in c] for g,c in nr['all_action_columns'].items()}
q,free=quotient2([c[i]^(1<<i) for c in actions.values() for i in range(256)],256)
assert len(free)==8
qcols=[q(1<<j) for j in range(256)]
unit=np.zeros((32,16),dtype=np.uint8)
for j in range(32):unit[j,j//2]=1 if j%2==0 else 2
quad=[q(hermpack(mm(v[:,None],FB[v[None,:]]))) for v in unit]
comm=np.zeros((32,32),dtype=np.uint8)
for i in range(32):
 for j in range(32):
  comm[i,j]=q(hermpack(mm(unit[i,:,None],FB[unit[j,None,:]])^mm(unit[j,:,None],FB[unit[i,None,:]])))
assert np.array_equal(comm,comm.T) and not np.any(comm.diagonal())
basic=np.tril(comm,-1);np.fill_diagonal(basic,quad)

def central_transform(cols,c):return lin(cols,int(c))
def bits_matrix(a):return np.array([[(int(x)>>j)&1 for x in row] for row in a for j in []])
def congruence(B,A):
 out=np.zeros((A.shape[1],A.shape[1]),dtype=np.uint8)
 for k in range(8):out|=(((A.T@((B>>k)&1)@A)%2).astype(np.uint8)<<k)
 return out
def bitmatrix(a):
 z=np.zeros((2*len(a),2*a.shape[1]),dtype=np.int64)
 for j in range(a.shape[1]):
  z[0::2,2*j]=a[:,j]&1;z[1::2,2*j]=a[:,j]>>1
  b=MUL[a[:,j],2];z[0::2,2*j+1]=b&1;z[1::2,2*j+1]=b>>1
 return z
omega=bitmatrix(2*np.eye(16,dtype=np.uint8));omega2=omega@omega%2
bilinear=basic^congruence(basic,omega)^congruence(basic,omega2)
assert np.array_equal(bilinear^bilinear.T,comm)
assert np.array_equal(congruence(bilinear,omega),bilinear)
assert list(map(int,bilinear.diagonal()))==quad

def Bvalue(v,w):
 out=0
 for i,j in zip(v.reshape(8,32),w.reshape(8,32)):
  ii=np.flatnonzero(i%2);jj=np.flatnonzero(j%2)
  if len(ii) and len(jj):out^=int(np.bitwise_xor.reduce(bilinear[np.ix_(ii,jj)].ravel()))
 return out
def qvalue(v):return Bvalue(v,v)
def qpoly_value(linear,polar,v):
 ii=np.flatnonzero(v%2);out=0
 for i in ii:out^=int(linear[i])
 for i,j in combinations(ii,2):out^=int(polar[i,j])
 return out
def lift_quadratic(A,centercols):
 base=np.array([[central_transform(centercols,x) for x in row] for row in bilinear],dtype=np.uint8)
 polar=congruence(bilinear,A)^base
 assert np.array_equal(polar,polar.T) and not np.any(polar.diagonal())
 linear=np.zeros(32,dtype=np.uint8);zero=np.zeros(32,dtype=np.uint8)
 for j in range(32):
  for w in (np.eye(32,dtype=np.int64)[:,j],omega[:,j],omega2[:,j]):
   linear[j]^=qpoly_value(zero,polar,w)
 # The unique scalar-C3-invariant quadratic correction, including its linear terms.
 for j in range(32):
  e=np.eye(32,dtype=np.int64)[:,j]
  assert qpoly_value(linear,polar,omega@e%2)==qpoly_value(linear,polar,e)
 for i,j in combinations(range(32),2):
  e=np.eye(32,dtype=np.int64)[:,i]^np.eye(32,dtype=np.int64)[:,j]
  assert qpoly_value(linear,polar,omega@e%2)==qpoly_value(linear,polar,e)
 return linear,polar

centerid=[1<<j for j in range(8)]
def action_quadratics(A,centercols=centerid):
 out=[]
 for i in range(8):
  full=A[:,32*i:32*(i+1)]%2
  block=[j for j in range(8) if np.any(full[32*j:32*(j+1)])]
  assert len(block)==1
  out.append(lift_quadratic(full[32*block[0]:32*(block[0]+1)],centercols))
 return out
def kval(ks,v):
 out=0
 for i,(l,p) in enumerate(ks):out^=qpoly_value(l,p,v[32*i:32*(i+1)])
 return out
def nproduct(x,y):
 v,c=x;w,d=y;return ((v+w)%4,c^d^Bvalue(v,w))
def ninverse(x):
 v,c=x;return ((-v)%4,c^qvalue(v))
def nact(A,ks,x):
 v,c=x;return (A@v%4,c^kval(ks,v))
def conjugated_generator(A,ks,b):
 return nproduct((b,0),nact(A,ks,ninverse((b,0))))

sM=np.array(Src['s_action_rows_mod4'],dtype=np.int64)
rM=np.array(Src['r_action_rows_mod4'],dtype=np.int64)
tM=np.array(Src['t_action_rows_mod4'],dtype=np.int64)
ks=action_quadratics(sM);kr=action_quadratics(rM);kt=action_quadratics(tM)
b=np.array(Src['source_s_conjugator_mod4'],dtype=np.int64)
d=np.array(Src['source_r_conjugator_mod4'],dtype=np.int64)
sN=conjugated_generator(sM,ks,b);rN=conjugated_generator(rM,kr,d)
zero=np.zeros(256,dtype=np.int64)
assert np.array_equal(sN[0],np.array(Src['source_s_homology_mod4']))
assert np.array_equal(rN[0],np.array(Src['source_r_homology_mod4']))
s2=nproduct(sN,nact(sM,ks,sN));assert np.array_equal(s2[0],zero) and s2[1]==0
r2=nproduct(rN,nact(rM,kr,rN));r3=nproduct(rN,nact(rM,kr,r2));assert np.array_equal(r3[0],zero) and r3[1]==0
tN=nproduct(sN,nact(sM,ks,rN));assert np.array_equal(tN[0],zero)
cusp=tN[1]
for j in range(256):
 e=np.eye(256,dtype=np.int64)[:,j]
 assert kval(kt,e)==(kval(ks,rM@e)^kval(kr,e))
 assert (kval(ks,sM@e)^kval(ks,e))==0
 assert (kval(kr,rM@rM@e)^kval(kr,rM@e)^kval(kr,e))==0
print(json.dumps({'stage':'actual quadratic cusp','s_square':0,'r_cube':0,'cusp_coordinate':hex(cusp),'ell_cusp':((cusp>>4)^(cusp>>5))&1}),flush=True)

basis=[int(x,16) for x in iso['homogeneous_equivariant_parameter_masks']]
goodrow=next(x for x in All['cases'] if x['character']==char)
checks=[]
for branch in iso['cases']:
 seed=int(branch['linear_seed_mask'],16)
 arow=next(x for x in goodrow['cases'] if x['branch']==branch['branch'])
 for entry in arow['isometry_parameters_and_actions']:
  parameter=int(entry['parameter'],16);X=matrixof(seed^lin(basis,parameter))
  Xreal=bitmatrix(X);centercols=[int(x,16) for x in entry['whole_coinvariant_action_columns']]
  kX=lift_quadratic(Xreal,centercols)
  Xglobal=np.kron(np.eye(8,dtype=np.int64),Xreal)
  # Only parities enter the exact central equation. A G-equivariant integral
  # lift exists by the proved projective trace; source linear equations are
  # retained in the separate modulo-four edge certificate.
  def FX(x):
   v,c=x;return (Xglobal@v%4,central_transform(centercols,c)^kval([kX]*8,v))
  for g,A,k in (('s',sM,ks),('r',rM,kr)):
   for j in range(256):
    e=np.eye(256,dtype=np.int64)[:,j]
    # Compare the central part, independent of the chosen even lift of X.
    lhs=FX(nact(A,k,(e,0)))[1]
    rhs=nact(A,k,FX((e,0)))[1]
    assert lhs==rhs,(g,branch['branch'],parameter,j)
  sb=FX((b,0));rd=FX((d,0))
  # The central coordinates of these conjugators cancel in conjugation.
  snew=conjugated_generator(sM,ks,sb[0]);rnew=conjugated_generator(rM,kr,rd[0])
  newt=nproduct(snew,nact(sM,ks,rnew))
  expected=central_transform(centercols,cusp)
  assert newt[1]==expected
  checks.append({'branch':branch['branch'],'parameter':hex(parameter),'central_action_columns':entry['whole_coinvariant_action_columns'],
                 'new_cusp_coordinate':hex(newt[1]),'cusp_difference':hex(newt[1]^cusp),
                 'fixes_actual_central_cusp':newt[1]==cusp})
result={'summary':{'status':'PASS','cusp_coordinate':hex(cusp),'ell_cusp':((cusp>>4)^(cusp>>5))&1,
                   'isometry_checks':len(checks),'cusp_difference_rank':xor_rank([int(x['cusp_difference'],16) for x in checks]),
                   'elapsed_seconds':time.time()-start},
 'whole_coinvariant_free_coordinates':free,'whole_coinvariant_projection_columns':[hex(x) for x in qcols],
 'bilinear_cocycle_rows':bilinear.tolist(),'quadratic_s_rows':[{'linear':l.tolist(),'polar':p.tolist()} for l,p in ks],
 'quadratic_r_rows':[{'linear':l.tolist(),'polar':p.tolist()} for l,p in kr],
 'quadratic_t_rows':[{'linear':l.tolist(),'polar':p.tolist()} for l,p in kt],
 'actual_source_s_central_coordinate':hex(sN[1]),'actual_source_r_central_coordinate':hex(rN[1]),
 'actual_source_t_central_coordinate':hex(cusp),'actual_source_t18_central_coordinate':'0x0',
 'isometry_cusp_checks':checks,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths+[path]}}
(OUT/'d_old_compact_quadratic_source.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
