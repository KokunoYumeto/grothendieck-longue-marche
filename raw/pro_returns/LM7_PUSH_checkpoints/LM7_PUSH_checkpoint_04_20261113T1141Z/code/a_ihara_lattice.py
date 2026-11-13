#!/usr/bin/env python3
"""Integral Schreier homology and geometric symmetry comparison.

Exploratory comparison only; all reported identities are exact integer checks.
The literal rank-two free-group symmetries are specified, not assumed equal
to unbased curve maps without the remaining path comparison.
"""
from pathlib import Path
import importlib.util,json
import numpy as np
import sympy as sp
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
Q=sp.Matrix(f.TATE_QUOTIENT.tolist())
S=Q.T*(Q*Q.T).inv()
assert Q*S==sp.eye(2)

def substitution(word,images):
 out=[]
 for a in word:
  out.extend(images[a] if a>0 else f.inverse_word(images[-a]))
 return out

def integer_action(images):
 return sp.Matrix(np.stack([f.integral_abel(substitution(w,images)) for w in f.NWORDS],axis=1).tolist())

Cx=sp.Matrix(np.stack([f.integral_abel([1]+w+[-1]) for w in f.NWORDS],axis=1).tolist())
Cy=sp.Matrix(np.stack([f.integral_abel([2]+w+[-2]) for w in f.NWORDS],axis=1).tolist())
Cc=integer_action({1:[-1],2:[-2]})
R=integer_action({1:[2],2:[-2,-1]})
for name,A in [('deck_x',Cx),('deck_y',Cy),('conjugation',Cc),('Nielsen_order3',R)]:
 assert Q*A==(Q*A*S)*Q
 print(name,'proper matrix',(Q*A*S).tolist())
print('Literal Nielsen matrix cube identity:',R**3==sp.eye(10))
print('Deck actions commute on integral homology:',Cx*Cy==Cy*Cx)
print('Conjugation signs:',len((Cc-sp.eye(10)).nullspace()),len((Cc+sp.eye(10)).nullspace()))

raw=json.loads((HERE/'de_fermat_schreier.json').read_text())
cv=sp.Matrix(f.CUSP_VECTORS.tolist())
geom={'x0':'O','x1':'C','x2':'Cbar','y0':'Q','y1':'Bbar','y2':'B','z0':'A','z1':'P','z2':'Abar'}
order=['P','Q','A','Abar','B','Bbar','C','Cbar']
toric=cv[:,[f.CUSP_LABELS.index(next(k for k,v in geom.items() if v==d)) for d in order]]
assert toric.rank()==8
proper_x=Q*Cx*S;proper_c=Q*Cc*S
fixed=(proper_c-sp.eye(2)).nullspace()[0]
fixed=fixed*sp.ilcm(*[x.q for x in fixed])
H=sp.Matrix.hstack(fixed,proper_x*fixed)
print('Proper basis [c-fixed vector, deck_x vector]:',H.tolist(),'determinant',H.det())
print('CM matrix in this basis:',(H.inv()*proper_x*H).tolist())
print('Conjugation matrix in this basis:',(H.inv()*proper_c*H).tolist())
print('Nielsen action on named cusps:')
for j,label in enumerate(f.CUSP_LABELS):
 matches=[k for k in range(9) if R*cv[:,j]==cv[:,k]]
 print(geom[label], [geom[f.CUSP_LABELS[k]] for k in matches])

npz=np.load(HERE/'de_fermat_schreier_certificate.npz')
rank=f.rank(npz['homology_linear'].reshape(10,-1))
print('Ihara f homology-parameter influence rank:',rank)
# Impose exact mod3 cusp fixation and proper E[3] fixation.
A0=npz['constant_ab'];As=npz['homology_linear']
cvnp=np.array(cv.tolist(),dtype=np.int64)%3
qnp=np.array(Q.tolist(),dtype=np.int64)%3
out=[];rhs=[]
for A in As:
 out.append(np.concatenate(((A@cvnp%3).reshape(-1),(qnp@A%3).reshape(-1))))
right=np.concatenate((((np.eye(10,dtype=np.int64)-A0)@cvnp%3).reshape(-1),
                      (qnp@(np.eye(10,dtype=np.int64)-A0)%3).reshape(-1)))
mat=np.stack(out,axis=1)%3
print('Cusp and proper fixation equations rank:',f.rank(mat),'augmented rank:',f.rank(np.column_stack((mat,right))))
# Actual homology translation induced by the lifted base3-cycle followed
# by inverse complex multiplication; the cusp permutation is checked below.
Tr=R*Cx.inv()
Tr2=Cx*Tr*Cx.inv()
assert Tr**3==sp.eye(10) and Tr2**3==sp.eye(10) and Tr*Tr2==Tr2*Tr
assert Q*Tr==Q and Q*Tr2==Q
proj=sp.zeros(10)
for aa in range(3):
 for bb in range(3): proj+=Tr**aa*Tr2**bb
proj=proj/9
assert proj**2==proj and proj.rank()==2 and Q*proj==Q
H=-H # The positive proper vector represents -P in the cusp Weil graph.
j=proj*S*H
araw=json.loads((HERE/'a_k_lattice.out').read_text())
Psi=sp.Matrix(araw['Weil_graph_matrix'])
comparisons=[]
for sign in (1,-1):
 B=toric.row_join(j+sign*toric*Psi/3)
 integral=all(a.q==1 for a in B)
 print('Weil graph sign',sign,'integral comparison:',integral,'determinant',B.det())
 if integral and B.det() in (1,-1):comparisons.append((sign,B))
print('Number of integral unimodular comparisons:',len(comparisons))
if comparisons:
 sign,B=comparisons[0]
 expectedc=sp.Matrix(araw['V_generator_matrices'][2])
 actualc=B.inv()*Cc*B
 print('Complex conjugation agrees with A7:',actualc==expectedc)
 # Compute the unique modulo3 homology parameter image giving actual U.
 target=np.array((B*sp.Matrix(araw['V_generator_matrices'][0])*B.inv()).tolist(),dtype=np.int64)%3
 matrix=npz['homology_linear'].reshape(10,-1).T%3
 rhs=(target-npz['constant_ab']).reshape(-1)%3
 aug=np.column_stack((matrix,rhs))%3
 print('Actual U homology system rank:',f.rank(matrix),'augmented rank:',f.rank(aug))
 r=0;pivots=[]
 for col in range(10):
  choices=np.flatnonzero(aug[r:,col])
  if not len(choices):continue
  rr=r+int(choices[0]);aug[[r,rr]]=aug[[rr,r]]
  aug[r]=aug[r]*int(aug[r,col])%3
  for ii in range(aug.shape[0]):
   if ii!=r:aug[ii]=(aug[ii]-aug[ii,col]*aug[r])%3
  pivots.append(col);r+=1
 fa=np.zeros(10,dtype=np.int64)
 for rr,col in enumerate(pivots):fa[col]=aug[rr,-1]
 assert np.array_equal(matrix@fa%3,rhs)
 print('One compatible f homology vector:',fa.tolist())
 artifact={'translation_P_matrix':Tr.tolist(),'translation_zetaP_matrix':Tr2.tolist(),
           'A7_to_Schreier_basis':B.tolist(),'Weil_graph_sign':sign,
           'compatible_f_homology_mod3':fa.tolist(),'homology_parameter_rank':len(pivots)}
 (HERE/'a_ihara_lattice.json').write_text(json.dumps(artifact,default=int,indent=2)+'\n')
print('PASS (comparison data only; central arithmetic f_sigma is not yet specified)')
