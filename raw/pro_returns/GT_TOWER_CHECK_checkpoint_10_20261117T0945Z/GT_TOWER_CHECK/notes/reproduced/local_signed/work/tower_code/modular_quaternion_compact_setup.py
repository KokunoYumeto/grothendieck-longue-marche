#!/usr/bin/env python3
"""Actual boundary quotient of compressed quaternion cover, in Lie coordinates."""
import numpy as np,json
from pathlib import Path
D=json.loads(Path(__file__).with_name('modular_quaternion_surface.json').read_text());words=D['actual_automorphism_words']
Q=np.load(Path(__file__).with_name('modular_quaternion_homology_compressed.npz'));CP=Q['central_quotient_projection']

def rref(A):
 A=np.asarray(A,dtype=np.int16).copy()%3;r=0;ps=[]
 for j in range(A.shape[1]):
  ns=np.flatnonzero(A[r:,j])
  if not len(ns):continue
  k=r+int(ns[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*(1 if A[r,j]==1 else 2)%3
  ns=np.flatnonzero(A[:,j]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,j,None]*A[r])%3;ps.append(j);r+=1
  if r==len(A):break
 return A[:r],ps
def minv(A):
 n=len(A);R,p=rref(np.hstack((A,np.eye(n,dtype=np.int16))));assert p[:n]==list(range(n));return R[:,n:]
pairs9=[(i,j) for i in range(9) for j in range(i+1,9)]
def wedge9(v,w):return np.array([(v[i]*w[j]-v[j]*w[i])%3 for i,j in pairs9],dtype=np.int16)@CP%3
cf=[j for j in range(36) if np.array_equal(CP[j],np.eye(15,dtype=np.int16)[np.argmax(CP[j])]) and np.count_nonzero(CP[j])==1]
# Use an exact right inverse of CP.T, without presuming the free coordinate ordering.
_,pv=rref(CP.T);CL=np.zeros((36,15),dtype=np.int16);CL[pv]=minv(CP.T[:,pv]);assert np.array_equal(CP.T@CL%3,np.eye(15,dtype=np.int16))
def wedgeM9(M):
 W=np.array([[(M[i,a]*M[j,b]-M[i,b]*M[j,a])%3 for a,b in pairs9] for i,j in pairs9],dtype=np.int16)
 return CP.T@W@CL%3
def wordlie(w):
 v=np.zeros(9,dtype=np.int16);z=np.zeros(15,dtype=np.int16)
 for j in w:
  u=np.zeros(9,dtype=np.int16);u[abs(j)-1]=1 if j>0 else 2;z=(z+2*wedge9(v,u))%3;v=(v+u)%3
 return np.concatenate((v,z))
gen24=[]
for gs in words:
 B=np.stack([wordlie(w) for w in gs],axis=1);M=B[:9];A=np.zeros((24,24),dtype=np.int16);A[:,:9]=B;A[9:,9:]=wedgeM9(M);gen24.append(A)
# Schreier rewriting of (aba^-1b^-1)^2 in the literal Q8 basis.
import modular_quaternion_surface as S
cusp=S.rewrite((1,2,-1,-2)*2);seed=wordlie(cusp)
I,ip=rref([seed])
while True:
 old=len(I);extras=[I@A.T%3 for A in gen24]
 for j in range(9):
  v=np.eye(9,dtype=np.int16)[j];extras.append(np.array([np.concatenate((np.zeros(9,dtype=np.int16),wedge9(v,row[:9]))) for row in I]))
 I,ip=rref(np.vstack([I]+extras))
 if len(I)==old:break
free=[j for j in range(24) if j not in ip];dim=len(free);P=np.zeros((24,dim),dtype=np.int16);P[free]=np.eye(dim,dtype=np.int16);P[ip]=-I[:,free]%3
E=np.zeros((24,dim),dtype=np.int16);E[free]=np.eye(dim,dtype=np.int16)
assert not np.any(I@P%3)
center,cp=rref(P[9:]);center=center.T;zc=center.shape[1]
basis=[center[:,i] for i in range(zc)];ab=[]
for j in range(dim):
 e=np.eye(dim,dtype=np.int16)[j]
 if len(rref(np.stack(basis+[e]))[0])>len(basis):basis.append(e);ab.append(e)
nb=len(ab);B=np.stack(ab+[center[:,i] for i in range(zc)],axis=1);Bi=minv(B)
assert (dim,nb,zc)==(14,6,8),(dim,nb,zc)
Proj=Bi@P.T%3;Lift=E@B%3;assert np.array_equal(Proj@Lift%3,np.eye(14,dtype=np.int16))
gens=[]
for A in gen24:
 G=Proj@A@Lift%3;assert np.array_equal(Proj@A%3,G@Proj%3);assert not np.any(G[:6,6:]);gens.append(G)
brackets=np.stack([(Proj@np.concatenate((np.zeros(9,dtype=np.int16),wedge9(Lift[:9,i],Lift[:9,j])))%3)[6:] for i in range(6) for j in range(i+1,6)],axis=1)
assert len(rref(brackets)[0])==8
print('PASS exact boundary ideal dimension',len(I),'compact quotient abelian/central',nb,zc,flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),boundary_ideal=I,quotient_projection=Proj,quotient_section=Lift,actual_generator_matrices=np.array(gens),bracket_matrix=brackets,cusp_word_N8=np.array(cusp))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Actual compressed quaternion surface quotient by the normal closure of its36 peripheral loops',
 'boundary_ideal_dimension':len(I),'abelian_dimension':nb,'central_dimension':zc,'cusp_word_N8':cusp,'surface_quotient_order':'32*3^14'},indent=2)+'\n')
