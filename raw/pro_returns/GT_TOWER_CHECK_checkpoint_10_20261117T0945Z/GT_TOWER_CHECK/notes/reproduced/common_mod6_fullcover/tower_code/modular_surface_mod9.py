#!/usr/bin/env python3
"""Test the actual Γ(12) action on the class-two exponent-nine quotient of K4.

K4=ker(F(a,b)->(Z/4)^2). The characteristic finite source is
F(a,b)/(gamma3(K4) K4^3), of order16*9^153.
No identification with the modular rank97 layer is assumed.
"""
import numpy as np,json
from pathlib import Path
from collections import deque
m=4;n=17
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(int(x))
 return tuple(out)
def inverse(w):return tuple(-x for x in reversed(w))
def sub(w,images):return red(x for a in w for x in (images[a-1] if a>0 else inverse(images[-a-1])))
labels=[(i,j) for j in range(m) for i in range(m)];index={x:i for i,x in enumerate(labels)}
def step(q,k,s=1):
 a=list(q);a[k]=(a[k]+s)%m;return tuple(a)
def section(q):return (2,)*q[1]+(1,)*q[0]
tree={(index[(i,j)],0) for j in range(m) for i in range(m-1)}|{(index[(0,j)],1) for j in range(m-1)}
chords=[(q,k) for q in range(m*m) for k in range(2) if (q,k) not in tree]
assert len(chords)==n;chordindex={x:i+1 for i,x in enumerate(chords)}
def rewrite(w):
 q=(0,0);out=[]
 for x in w:
  k=abs(x)-1
  if x>0:
   edge=(index[q],k);q=step(q,k)
   if edge in chordindex:out.append(chordindex[edge])
  else:
   q=step(q,k,-1);edge=(index[q],k)
   if edge in chordindex:out.append(-chordindex[edge])
 assert q==(0,0)
 return red(out)
basis=[section(labels[q])+(k+1,)+inverse(section(step(labels[q],k))) for q,k in chords]
for i,w in enumerate(basis):assert rewrite(w)==(i+1,)
def restrict(g):return tuple(rewrite(sub(w,g)) for w in basis)
normalizer_words=[restrict(((1,),(2,1))),restrict(((1,-2),(2,)))]
deck_words=[tuple(rewrite((g,)+w+(-g,)) for w in basis) for g in (1,2)]
pairs=[(i,j) for i in range(n) for j in range(i+1,n)];nc=len(pairs);dim=n*nc
def rref(A):
 A=np.array(A,dtype=np.int16).copy()%9;r=0;p=[]
 for c in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,c]%3)
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*pow(int(A[r,c]),-1,9)%9
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r]
  A[ns]=(A[ns]-A[ns,c,None]*A[r])%9;p.append(c);r+=1
  if r==len(A):break
 return A[:r],p
def minv(M):
 A,p=rref(np.hstack((M,np.eye(n,dtype=np.int16))))
 assert p[:n]==list(range(n));return A[:,n:]
def wedge(v,w):return np.array([(v[i]*w[j]-v[j]*w[i])%9 for i,j in pairs],dtype=np.int16)
def wedgeM(M):
 a=np.array([i for i,j in pairs]);b=np.array([j for i,j in pairs])
 return (M[a[:,None],a[None,:]]*M[b[:,None],b[None,:]]-M[a[:,None],b[None,:]]*M[b[:,None],a[None,:]])%9
inner=[]
for i in range(n):
 inner.append(np.stack([wedge(np.eye(n,dtype=np.int16)[i],np.eye(n,dtype=np.int16)[j]) for j in range(n)],axis=1).reshape(-1))
inner,ipiv=rref(inner);free=[i for i in range(dim) if i not in ipiv];odim=len(free)
assert odim==2295
def project(C):
 C=np.asarray(C).reshape(-1,dim)%9;out=(C[:,free]-C[:,ipiv]@inner[:,free])%9
 return out[0] if len(out)==1 else out
def lift(C):
 out=np.zeros(dim,dtype=np.int16);out[free]=C;return out.reshape(nc,n)
def wordlie(w):
 v=np.zeros(n,dtype=np.int16);z=np.zeros(nc,dtype=np.int16)
 for a in w:
  u=np.zeros(n,dtype=np.int16);u[abs(a)-1]=1 if a>0 else 8
  z=(z+5*wedge(v,u))%9;v=(v+u)%9
 return v,z
def aut(words):
 vz=[wordlie(w) for w in words];M=np.stack([v for v,z in vz],axis=1);D=np.stack([z for v,z in vz],axis=1)
 return project(D@minv(M)%9),M
gens=[aut(w) for w in normalizer_words];deck=[aut(w) for w in deck_words]
actcache={}
def act(M,C):
 key=tuple(map(int,M.reshape(-1)))
 if key not in actcache:actcache[key]=(wedgeM(M),minv(M))
 W,Mi=actcache[key];return project((W@lift(C)%9)@Mi%9)
def mul(g,h):return ((g[0]+act(g[1],h[0]))%9,g[1]@h[1]%9)
def power(g,k):
 out=(np.zeros(odim,dtype=np.int16),np.eye(n,dtype=np.int16))
 for _ in range(k):out=mul(out,g)
 return out
central=power(mul(mul(gens[0],gens[1]),gens[0]),4)
assert not np.any(central[0]) and np.array_equal(central[1],np.eye(n,dtype=np.int16))
print('PASS actual SL2(Z) outer action on the characteristic order16*9^153 surface quotient',flush=True)

linear=[np.eye(2,dtype=np.int16)];idx={tuple(linear[0].reshape(-1)):0};paths=[()]
reps=[(np.zeros(odim,dtype=np.int16),np.eye(n,dtype=np.int16))]
UG=np.array([[1,1],[0,1]],dtype=np.int16);LG=np.array([[1,0],[-1,1]],dtype=np.int16)
for qi,M in enumerate(linear):
 for j,L in enumerate((UG,LG)):
  N=M@L%12;key=tuple(map(int,N.reshape(-1)))
  if key not in idx:
   idx[key]=len(linear);linear.append(N);paths.append(paths[qi]+(j+1,));reps.append(mul(reps[qi],gens[j]))
assert len(linear)==1152
print('PASS all1152 matrices in SL2(Z/12), with actual surface representatives',flush=True)

def inverse_aut(g):
 N=minv(g[1]);return (-act(N,g[0])%9,N)
def log_IA(g):
 a=(g[1]-np.eye(n,dtype=np.int16))%9
 assert not np.any(a%3)
 Z=(g[0]-5*(act(g[1],g[0])-g[0]))%9
 return np.concatenate((Z,a.reshape(-1)))
def exp_IA(X):
 Z=X[:odim];a=X[odim:].reshape(n,n);assert not np.any(a%3)
 M=(np.eye(n,dtype=np.int16)+a)%9
 C=(Z+5*(act(M,Z)-Z))%9
 return C,M
def bracket(X,Y):
 Ma=np.eye(n,dtype=np.int16)+X[odim:].reshape(n,n)
 Mb=np.eye(n,dtype=np.int16)+Y[odim:].reshape(n,n)
 z=(act(Ma%9,Y[:odim])-Y[:odim]-act(Mb%9,X[:odim])+X[:odim])%9
 return np.concatenate((z,np.zeros(n*n,dtype=np.int16)))
def field_rref(A):
 A=np.asarray(A,dtype=np.int16).copy()%3;r=0;piv=[]
 for c in range(A.shape[1]):
  ns=np.flatnonzero(A[r:,c])
  if not len(ns):continue
  k=r+int(ns[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,c]==1 else 2)%3
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r]
  A[ns]=(A[ns]-A[ns,c,None]*A[r])%3;piv.append(c);r+=1
  if r==len(A):break
 return A[:r],piv
def module_basis(A):
 A=np.asarray(A,dtype=np.int16).copy()%9;r=0;piv=[]
 for c in range(A.shape[1]):
  ns=np.flatnonzero(A[r:,c]%3)
  if not len(ns):continue
  k=r+int(ns[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*pow(int(A[r,c]),-1,9)%9
  ns=np.flatnonzero(A[:,c]);ns=ns[ns!=r]
  A[ns]=(A[ns]-A[ns,c,None]*A[r])%9;piv.append(c);r+=1
  if r==len(A):break
 assert not np.any(A[r:]%3)
 T,tp=field_rref(A[r:]//3)
 assert not np.any(T[:,piv])
 return A[:r],piv,T,tp
def member(v,data):
 U,up,T,tp=data;v=np.asarray(v,dtype=np.int16).copy()%9
 if len(U):v=(v-v[...,up]@U)%9
 if np.any(v%3):return False
 v=v//3
 if len(T):v=(v-v[...,tp]@T)%3
 return not np.any(v)

rows=[];bad=0
for qi,M in enumerate(linear):
 for j,L in enumerate((UG,LG)):
  ri=idx[tuple(map(int,(M@L%12).reshape(-1)))];h=mul(reps[qi],gens[j])
  g=mul(h,inverse_aut(reps[ri]))
  if np.any((g[1]-np.eye(n,dtype=np.int16))%3):bad+=1
  rows.append(log_IA(g))
assert bad==0
rows=np.array(rows);data=module_basis(rows);U,up,T,tp=data
print('Actual Γ12 logarithmic module before bracket closure:',len(U),'free and',len(T),'order3',flush=True)
iteration=0
while True:
 old=2*len(U)+len(T);extra=[]
 for i,x in enumerate(U):
  for y in U[:i]:extra.append(bracket(x,y))
  for y in 3*T:extra.append(bracket(x,y))
 data=module_basis(np.vstack((U,3*T,np.array(extra))));U,up,T,tp=data;iteration+=1
 print('Γ12 Lie closure',iteration,':',len(U),'free and',len(T),'order3',flush=True)
 if 2*len(U)+len(T)==old:break

# Check the logarithm law and all actual generators against the module.
assert member(rows,data)
for i in range(min(12,len(rows))):
 x=rows[i];y=rows[(37*i+19)%len(rows)]
 lhs=log_IA(mul(exp_IA(x),exp_IA(y)))
 assert np.array_equal(lhs,(x+y+5*bracket(x,y))%9)
print('PASS exact class-two logarithm law in the actual Γ12 image',flush=True)

h=mul(gens[0],gens[1]);hi=inverse_aut(h)
q=idx[(5,0,0,5)];g=reps[q]
delta=mul(mul(mul(g,h),inverse_aut(g)),hi);c=log_IA(delta)
assert member(c,data)
def theta(X):return log_IA(mul(mul(h,exp_IA(X)),hi))
basis=np.vstack((U,3*T));theta_basis=np.array([theta(x) for x in basis])
assert member(theta_basis,data)
equations=np.array([(theta(x)-x-5*bracket(x,c))%9 for x in basis])
equation_module=module_basis(equations);soluble=member(c,equation_module)
print('Exact5I-coset CM-centralizer lift to actual exponent9 surface image:',soluble,flush=True)
print('Actual Γ12 image order:3^',2*len(U)+len(T),flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),actual_generator_logs=rows,
 free_module_basis=U,free_pivots=np.array(up),torsion_module_basis=T,torsion_pivots=np.array(tp),
 CM_C=h[0],CM_M=h[1],coset_representative_C=g[0],coset_representative_M=g[1],
 coset_commutator_log=c,centralizer_equations=equations,
 equation_free_basis=equation_module[0],equation_free_pivots=np.array(equation_module[1]),
 equation_torsion_basis=equation_module[2],equation_torsion_pivots=np.array(equation_module[3]))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exact CM centralizer lifting in actual exponent9 K4 surface quotient',
 'characteristic_surface_quotient_order':'16*9^153','actual_Gamma12_free_Z9_rank':len(U),
 'actual_Gamma12_torsion_F3_rank':len(T),'actual_Gamma12_image_order_log3':2*len(U)+len(T),
 'bad_CM_coset_mod12':[[5,0],[0,5]],'bad_coset_lifts':bool(soluble),
 'lie_closure_iterations':iteration},indent=2)+'\n')
