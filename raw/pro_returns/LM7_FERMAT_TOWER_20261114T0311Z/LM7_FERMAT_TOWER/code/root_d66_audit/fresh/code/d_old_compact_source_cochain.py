#!/usr/bin/env python3
"""Actual projective edge extension and cusp-fixed cochain for the old a4 cover.

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

def invreal4(a):
 a=np.array(a,dtype=np.int64)%4;n=len(a)
 b=inv((a%2).astype(np.uint8)).astype(np.int64)
 b=b@(2*np.eye(n,dtype=np.int64)-a@b)%4
 assert np.array_equal(a@b%4,np.eye(n,dtype=np.int64));return b

def postscalar(a,z):
 a0=z&3;a1=z>>2;v=a.reshape(len(a),-1,2)
 return np.stack((a0*v[:,:,0]+a1*v[:,:,1],-a1*v[:,:,0]+(a0-a1)*v[:,:,1]),axis=2).reshape(a.shape)%4

ipath=OUT/'d_old_compact_integral.json';Int=json.loads(ipath.read_text());paths.append(ipath)
char=[0,1,0,0];ellchar=np.array(char,dtype=np.int16)
ir=next(x for x in Int['cases'] if x['character']==char)
rec=next(x for x in Split['cases'] if x['character']==char)
B=next(x for x in D['character_blocks'] if x['character']==char)
P=next(x for x in Pair['cases'] if x['character']==char)
acts={a['q_state']:(np.array(a['columns'],dtype=np.uint8).T,a['flip']) for a in B['all_stabilizer_actions']}
H=sorted(acts);Syl=ir['Sylow_states'];assert len(H)==72 and len(Syl)==8
ma={int(g):np.array(x,dtype=np.uint8).T for g,x in ir['all_integral_cover_actions'].items()}
ma_real={g:real4(x,acts[g][1]) for g,x in ma.items()}
M4=np.array(ir['integral_projective_cover_columns'],dtype=np.uint8).T
idem=np.array(ir['actual_equivariant_idempotent_mod4'],dtype=np.uint8)
qc=np.array(ir['compact_quotient_rows_mod4'],dtype=np.uint8)
U4=np.array(P['integral_cycle_lifts_mod4_columns'],dtype=np.uint8).T
F=mat(mat(leftinv4(M4),idem),qc)
assert np.array_equal(mat(F,mat(np.array(ir['compact_section_columns_mod4'],dtype=np.uint8).T,M4)),np.eye(16,dtype=np.uint8))
ordinary=np.zeros((16,576),dtype=np.uint8);ordinary[:,B['source_free_edges']]=F
assert np.array_equal(mat(ordinary,U4),F)
seedcols=ir['regular_seed_coordinates'];seed=np.eye(32,dtype=np.int64)[:,seedcols]
regular=np.column_stack([ma_real[g][:,i] for i in seedcols for g in Syl])
ri=invreal4(regular);identity_rows=[k*8+Syl.index(0) for k in range(4)]
C=seed@ri[identity_rows]%4
check=sum(ma_real[g]@C@ma_real[inverse(g)] for g in Syl)%4
assert np.array_equal(check,np.eye(32,dtype=np.int64))
ordinary_real=C@real4(ordinary)%4
scalarM=real4(scalar(4,np.eye(16,dtype=np.uint8)));scalarMi=scalarM@scalarM%4
avg=3*(ordinary_real+scalarM@postscalar(ordinary_real,15)+scalarMi@postscalar(ordinary_real,4))%4
extension=np.zeros_like(avg)
for g in H:
 gi=inverse(g);cols=np.array([[2*int(T[gi,q]),2*int(T[gi,q])+1] for q in range(576)]).ravel()
 u=avg[:,cols].copy()
 if acts[g][1]:u[:,1::2]=-u[:,0::2]-u[:,1::2]
 extension+=ma_real[g]@u
extension%=4
edge=fromreal4(extension)
assert np.array_equal(mat(edge,U4),F)
for g in H:
 assert np.array_equal(edge[:,T[g]],mat(ma[g],bar(edge) if acts[g][1] else edge))
print(json.dumps({'stage':'edge extension','character':char,'cycle_rank':96,'cover_rank':16,'all_stabilizer_checks':72}),flush=True)

reps=[];which={}
for q in range(576):
 if q in which:continue
 i=len(reps);reps.append(q)
 for h in H:which[int(T[q,h])]=i
assert len(reps)==8 and len(which)==576
def action(a,q,v):
 out=np.zeros_like(v)
 for i,k in enumerate(reps):
  qk=int(T[q,k]);j=which[qk];h=int(T[inverse(reps[j]),qk]);assert h in H
  value=mat(ma[h],(bar(v[i]) if acts[h][1] else v[i])[:,None])[:,0]
  phase=int(ellchar@QL[inverse(reps[j])]@a%3)
  out[j]=scalar(int(TEICH[phase]),value)
 return out

def realvec(v):return np.column_stack((v.ravel()&3,v.ravel()>>2)).ravel().astype(np.int64)
def ovec(v):return (v[0::2]+4*v[1::2]).astype(np.uint8).reshape(8,16)
def action_matrix(a,q):
 cols=[]
 for j in range(256):
  v=np.zeros(256,dtype=np.int64);v[j]=1
  cols.append(realvec(action(a,q,ovec(v))))
 return np.array(cols,dtype=np.int64).T

w=np.array([edge[:,inverse(k)] for k in reps],dtype=np.uint8)
for q in range(576):
 assert np.array_equal(action(np.zeros(4,dtype=np.int16),q,w)[0],edge[:,q])
sM=action_matrix(np.zeros(4,dtype=np.int16),S);rM=action_matrix(vr,R);tM=sM@rM%4
ident=np.eye(256,dtype=np.int64)
assert np.array_equal(sM@sM%4,ident) and np.array_equal(rM@rM@rM%4,ident)
t12=ident.copy();norm=np.zeros_like(ident)
for i in range(12):norm=(norm+t12)%4;t12=t12@tM%4
assert np.array_equal(t12,ident)
wv=realvec(w);rhs=(sM-tM)@wv%4
assert not np.any(norm@rhs%4)
lin=(tM-ident)%4;cols=rr((lin%2).astype(np.uint8))[1]
rows=rr((lin[:,cols].T%2).astype(np.uint8))[1]
sol=np.zeros(256,dtype=np.int64);sol[cols]=invreal4(lin[np.ix_(rows,cols)])@rhs[rows]%4
assert np.array_equal(lin@sol%4,rhs)
etas=(ident-sM)@sol%4;etar=(ident-rM)@(wv+sol)%4
assert not np.any((etas+sM@etar)%4)
assert not np.any((ident+sM)@etas%4) and not np.any((ident+rM+rM@rM)@etar%4)
result={'summary':{'status':'PASS','character':char,'base_order':46656,'global_cover_rank_Z4':256,'cusp_order':12,
                   'cusp_difference_rank':len(cols),'elapsed_seconds':time.time()-start},
 'unordered_coset_representatives':reps,'coefficient_of_one_map_rows_mod4':C.tolist(),
 'edge_extension_columns_mod4':edge.T.tolist(),'cycle_projection_rows_mod4':F.tolist(),
 'global_edge_generator_mod4':wv.tolist(),'cusp_normalizing_vector_mod4':sol.tolist(),
 'source_s_conjugator_mod4':sol.tolist(),'source_r_conjugator_mod4':((wv+sol)%4).tolist(),
 'source_s_homology_mod4':etas.tolist(),'source_r_homology_mod4':etar.tolist(),
 's_action_rows_mod4':sM.tolist(),'r_action_rows_mod4':rM.tolist(),'t_action_rows_mod4':tM.tolist(),
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths+[path]}}
(OUT/'d_old_compact_source_cochain.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
