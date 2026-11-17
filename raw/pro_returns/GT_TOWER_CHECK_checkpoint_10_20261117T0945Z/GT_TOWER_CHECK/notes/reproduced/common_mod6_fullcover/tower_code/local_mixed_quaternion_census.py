#!/usr/bin/env python3
"""The literal (d,V) mixed-braid evaluation on faithful cover and mod4.
Retains the 52-dimensional block model over F3: faithful cover36,
then the permutation of the sixteen actual compact mod4 vectors.
"""
import numpy as np,json
from pathlib import Path
D=Path(__file__).parent
L=np.load(D/'local_braid_quaternion_image.npz');Q=np.load(D/'translation_quaternion_homology.npz');J=json.loads((D/'local_braid_quaternion_image.json').read_text())
def rr(A):
 A=np.asarray(A,dtype=np.int64).copy()%3;r=0;p=[]
 for j in range(A.shape[1]):
  z=np.flatnonzero(A[r:,j])
  if not len(z):continue
  k=r+int(z[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*int(A[r,j])%3
  ns=np.flatnonzero(A[:,j]);ns=ns[ns!=r];A[ns]=(A[ns]-A[ns,j,None]*A[r])%3;p.append(j);r+=1
  if r==len(A):break
 return A[:r],p
def mi(A):
 n=len(A);R,p=rr(np.hstack((A,np.eye(n,dtype=np.int64))));assert p[:n]==list(range(n));return R[:,n:]
C=Q['quaternion_component_basis'];_,cr=rr(C.T);Ci=mi(C[cr,:]);F=np.load(D/'translation_quaternion_image.npz')['form'];U=L['support_subspace'];gram=U.T@F@U%3
assert len(rr(gram)[0])==2
Ms=[];periods=[]
for M,g in zip(L['local_rank73'],J['local_automorphisms']):
 A=Ci@(M@C%3)[cr,:]%3;assert np.array_equal(C@A%3,M@C%3)
 P=np.array([[sum(1 if k==i else -1 if k==-i else 0 for k in g[j]) for j in range(2)] for i in (1,2)],dtype=np.int64)%4
 assert (P[0,0]*P[1,1]-P[0,1]*P[1,0])%4==1
 B=np.zeros((16,16),dtype=np.int64)
 for y in range(4):
  for x in range(4):
   z=P@np.array([x,y])%4;B[int(z[0]+4*z[1]),x+4*y]=1
 N=np.zeros((52,52),dtype=np.int64);N[:36,:36]=A;N[36:,36:]=B;Ms.append(N);periods.append(P)
V=Ms[0]@Ms[1]%3@Ms[0]%3;V=V@V%3;dd=Ms[2]
def mg(M):return '['+','.join('['+','.join(str(int(x))+'*Z(3)^0' for x in row)+']' for row in M)+']'
script='A:='+mg(Ms[0])+';;\nB:='+mg(Ms[1])+';;\nD:='+mg(dd)+';;\nV:='+mg(V)+';;\n'
script+='G:=Group([A,B,D]);; M:=Group([D,V]);;\n'
script+='Print("LOCAL_SIGNED_SIZE ",Size(G)," SOLVABLE ",IsSolvableGroup(G),"\\n");\n'
script+='Print("MIXED_SIZE ",Size(M)," SOLVABLE ",IsSolvableGroup(M),"\\n");\n'
script+='Print("MIXED_DERIVED_SIZE ",Size(DerivedSubgroup(M))," ABELIAN_INVARIANTS ",AbelianInvariants(M),"\\n");\n'
script+='Print("MIXED_FITTING_SIZE ",Size(FittingSubgroup(M)),"\\n");\n'
script+='N:=DerivedSubgroup(M);; Print("DERIVED_ABELIAN ",IsAbelian(N)," ABELIANIZATION ",AbelianInvariants(N)," CLASS ",NilpotencyClassOfGroup(N)," EXPONENT ",Exponent(N),"\\n");\n'
script+='Print("CENTER_SIZE ",Size(Center(M))," CENTER_INVARIANTS ",AbelianInvariants(Center(M)),"\\n");\n'
script+='Print("ORDERS_D_V_DV ",Order(D)," ",Order(V)," ",Order(D*V),"\\n");\n'
script+='Print("V2_CENTRAL ",V^2 in Center(M)," D4 ",Order(D^4)," COMM_D2_V ",Order(Comm(D^2,V)),"\\n");\nQUIT;\n'
Path(__file__).with_suffix('.g').write_text(script)
np.savez_compressed(Path(__file__).with_suffix('.npz'),local_signed_matrices=np.array(Ms),mixed_matrices=np.array([dd,V]),local_periods=np.array(periods),support_gram=gram)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Literal local mixed-braid image on faithful quaternion homology plus signed compact mod4, before any finite-pentagon implication',
 'source_words':J['local_automorphisms'],'local_periods':[x.tolist() for x in periods],'V_braid_word':[1,2,1,1,2,1],
 'mixed_generator_words':[[3],[1,2,1,1,2,1]],'support_dimension':4,'support_form_rank':2,'signed_matrix_dimension':52},indent=2)+'\n')
print('PASS exact local signed model52, support dimension4 and form rank2',flush=True)
