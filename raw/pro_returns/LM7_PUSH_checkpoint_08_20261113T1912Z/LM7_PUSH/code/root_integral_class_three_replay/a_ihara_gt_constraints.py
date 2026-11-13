#!/usr/bin/env python3
"""Exact necessary GT symmetry/hexagon constraints in the Fermat quotient.

This computes an enlarged set containing the actual Frob7 Ihara element;
it does not identify any arbitrary member as the arithmetic element.
Conventions: alpha(x)=x^7, alpha(y)=f^-1 y^7 f,
f(x,y)f(y,x)=1, f(x,y)x^3 f(z,x)z^3 f(y,z)y^3=1,
z=(xy)^-1. The true element also satisfies the pentagon.
"""
from pathlib import Path
import importlib.util,itertools,json
import numpy as np
import sympy as sp
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
data=np.load(HERE/'de_fermat_schreier_certificate.npz')
comp=json.loads((HERE/'a_ihara_lattice.json').read_text())
B=sp.Matrix(comp['A7_to_Schreier_basis'])
araw=json.loads((HERE/'a_k_lattice.out').read_text())
target=np.array((B*sp.Matrix(araw['V_generator_matrices'][0])*B.inv()).tolist(),dtype=np.int64)%3

def solve(A,b):
 A=np.asarray(A,dtype=np.int64)%3;b=np.asarray(b,dtype=np.int64).reshape(-1,1)%3
 aug=np.hstack((A,b));r=0;piv=[]
 for col in range(A.shape[1]):
  choices=np.flatnonzero(aug[r:,col])
  if not len(choices):continue
  rr=r+int(choices[0]);aug[[r,rr]]=aug[[rr,r]];aug[r]=aug[r]*int(aug[r,col])%3
  for i in range(aug.shape[0]):
   if i!=r:aug[i]=(aug[i]-aug[i,col]*aug[r])%3
  piv.append(col);r+=1
 if np.any(aug[r:,-1]):return None
 part=np.zeros(A.shape[1],dtype=np.int64)
 for rr,col in enumerate(piv):part[col]=aug[rr,-1]
 free=[j for j in range(A.shape[1]) if j not in piv]
 ker=np.zeros((A.shape[1],len(free)),dtype=np.int64)
 for kk,j in enumerate(free):
  ker[j,kk]=1
  for rr,col in enumerate(piv):ker[col,kk]=-aug[rr,j]%3
 assert np.array_equal(A@part%3,b[:,0]) and not np.any(A@ker%3)
 return part,ker,r

def autom(images):
 def sub(word):
  out=[]
  for a in word:out.extend(images[a] if a>0 else f.inverse_word(images[-a]))
  return out
 vals=[f.literal(sub(w)) for w in f.NWORDS]
 A=np.stack([v[0] for v in vals],axis=1);J=np.stack([v[1] for v in vals],axis=1)
 return A,J,f.exterior(A)

SA,SJ,SW=autom({1:[2],2:[1]})
RA,RJ,RW=autom({1:[2],2:[-2,-1]})
R2A=RA@RA%3;R2J=(RJ@RA+RW@RJ)%3;R2W=RW@RW%3

def acted(g,A,J,W):
 a,z=g
 return A@a%3,(J@a+W@z)%3

x3=f.literal([1]*3);y3=f.literal([2]*3);z3=f.literal([-2,-1]*3)
def relation(fa,fz):
 g=(fa,fz)
 sym=f.multiply(g,acted(g,SA,SJ,SW))
 h=f.zero()
 for v in [g,x3,acted(g,R2A,R2J,R2W),z3,acted(g,RA,RJ,RW),y3]:h=f.multiply(h,v)
 return sym,h

hom=np.vstack((data['homology_linear'].reshape(10,-1).T,f.F_AB_DIV3,
               np.eye(10,dtype=np.int64)+SA,np.eye(10,dtype=np.int64)+RA+R2A))%3
rhs=np.concatenate(((target-data['constant_ab']).reshape(-1),np.zeros(2,dtype=np.int64),
                    np.zeros(10,dtype=np.int64),-x3[0]-y3[0]-z3[0]))%3
sol=solve(hom,rhs);assert sol is not None
part,ker,r=sol
print('Homology necessary equations: rank',r,'free parameters',ker.shape[1])
cent=np.vstack((np.eye(45,dtype=np.int64)+SW,np.eye(45,dtype=np.int64)+RW+R2W))%3
cc=solve(cent,np.zeros(90,dtype=np.int64));assert cc is not None
print('Central symmetry/hexagon coefficient rank',cc[2],'kernel dimension',cc[1].shape[1])
solutions=[]
for coordinates in itertools.product(range(3),repeat=ker.shape[1]):
 fa=(part+ker@np.array(coordinates,dtype=np.int64))%3
 sym,h=relation(fa,np.zeros(45,dtype=np.int64))
 assert not np.any(sym[0]) and not np.any(h[0])
 csol=solve(cent,-np.concatenate((sym[1],h[1])))
 if csol is None:continue
 fz,cz,rank=csol
 assert all(not np.any(a) for v in relation(fa,fz) for a in v)
 au,ju=f.generator_images(fa,fz,7)
 assert np.array_equal(au,target)
 solutions.append((fa,fz,ju))
print('Compatible homology choices:',len(solutions),'of',3**ker.shape[1])
print('Each retains central kernel dimension',cc[1].shape[1])
assert solutions
base=solutions[0][2]
central_effect=[]
for col in cc[1].T:
 fa,fz,j=solutions[0]
 aa,jnew=f.generator_images(fa,(fz+col)%3,7)
 central_effect.append((jnew-j).reshape(-1)%3)
variations=[(j-base).reshape(-1)%3 for fa,fz,j in solutions]+central_effect
vmat=np.stack(variations,axis=1)
print('Affine span dimension of remaining Johnson variations:',f.rank(vmat))
artifact={'f_homology_representatives':[a.tolist() for a,z,j in solutions],
          'f_central_representatives':[z.tolist() for a,z,j in solutions],
          'central_kernel':cc[1].tolist(),
          'base_Johnson_matrix':base.tolist(),
          'Johnson_variation_columns':vmat.tolist(),
          'actual_f_not_identified':True}
(HERE/'a_ihara_gt_constraints.json').write_text(json.dumps(artifact,indent=2)+'\n')
print('PASS: exact necessary constraints only; no pentagon/arithmetic identification assumed.')
