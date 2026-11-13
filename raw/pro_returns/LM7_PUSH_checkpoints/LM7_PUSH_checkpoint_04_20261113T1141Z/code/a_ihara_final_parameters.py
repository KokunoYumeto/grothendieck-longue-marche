#!/usr/bin/env python3
"""Extract the exact two base-metabelian functionals determining Johnson.

Input retains the integral source f2 and full degree-seven pentagon.
All affine origins and actual 45x10 correction matrices are saved.
"""
from pathlib import Path
import importlib.util,contextlib,io,json
import numpy as np
import sympy as sp
HERE=Path(__file__).resolve().parent
def load(name):
 spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
 obj=importlib.util.module_from_spec(spec)
 with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(obj)
 return obj
f=load('de_fermat_schreier');g=load('a_ihara_gauge');meta=load('a_ihara_metabelian')
raw=json.loads((HERE/'a_ihara_pentagon_scalar_compare.json').read_text())
J=np.array(raw['Johnson_variations'],dtype=np.int64)
H=np.array(raw['metabelian_variations'],dtype=np.int64)
J0=np.array(raw['base_J'],dtype=np.int64)
H0=np.array(raw['base_metabelian'],dtype=np.int64)

def solve(A,b):
 A=np.asarray(A,dtype=np.int64)%3;b=np.asarray(b,dtype=np.int64)%3
 RR,piv=g.rref(np.column_stack((A,b)));n=A.shape[1]
 assert n not in piv
 out=np.zeros(n,dtype=np.int64)
 for i,j in enumerate(piv):out[j]=RR[i,n]
 assert np.array_equal(A@out%3,b)
 return out

order=sorted(range(len(meta.MON)),key=lambda i:(sum(meta.MON[i]),meta.MON[i]))
for degree in range(2,12):
 ids=[i for i in order if sum(meta.MON[i])+2<=degree]
 hh=H[ids]
 print('Metabelian coefficients through degree',degree,'leave Johnson dimension',
       f.rank(np.vstack((hh,J)))-f.rank(hh))

# Find the first pair of coefficient coordinates whose exact values determine J.
chosen=None
for maxdegree in range(2,13):
 allowed=[i for i in order if sum(meta.MON[i])+2<=maxdegree]
 for ii,i in enumerate(allowed):
  for j in allowed[ii+1:]:
   HH=H[[i,j]]
   if f.rank(HH)==2 and f.rank(np.vstack((HH,J)))==2:
    chosen=[i,j];break
  if chosen is not None:break
 if chosen is not None:break
assert chosen is not None
HH=H[chosen]
L=np.stack([solve(HH.T,row) for row in J],axis=0)
assert np.array_equal(L@HH%3,J)
print('Chosen actual commutator coefficient monomials:',[meta.MON[i] for i in chosen])
print('Their base values:',H0[chosen].tolist())
print('Their correction matrices have ranks:',[f.rank(L[:,i].reshape(45,10)) for i in range(2)])

# Inspect exact small Miller detectors on the final two-dimensional image.
B=sp.Matrix(json.loads((HERE/'a_ihara_lattice.json').read_text())['A7_to_Schreier_basis'])
def effect(d,partners):
 a=np.zeros(10,dtype=np.int64);a[d]=2
 b=np.zeros(10,dtype=np.int64)
 for j in partners:b[j]=1
 aa=np.array((sp.Matrix([a.tolist()])*B.inv()).tolist()[0],dtype=np.int64)%3
 bb=np.array((sp.Matrix([b.tolist()])*B.inv()).tolist()[0],dtype=np.int64)%3
 om=np.array([aa[i]*bb[j]-aa[j]*bb[i] for i,j in zip(*f.UP)],dtype=np.int64)%3
 return np.einsum('i,ijk->jk',om,L.reshape(45,10,2))%3
eff1=effect(0,[0,1]);eff2=effect(2,[2,4])
print('First Miller/vertical detector rank on the final two parameters:',f.rank(eff1))
print('Its CM translate combined detector rank:',f.rank(np.vstack((eff1,eff2))))

out={'coefficient_ring':meta.MON,'chosen_monomial_indices':chosen,
     'chosen_monomials':[meta.MON[i] for i in chosen],
     'base_coefficient_values':H0[chosen].tolist(),'base_fa':raw['base_fa'],'base_fz':raw['base_fz'],
     'base_Johnson_matrix':J0.tolist(),
     'correction_matrices':[L[:,i].reshape(45,10).tolist() for i in range(2)],
     'formula':'J_actual=J_base+sum_i (h_i-h_i_base)*correction_matrix_i overF3',
     'first_Miller_detector':eff1.tolist(),'CM_Miller_detector':eff2.tolist(),
     'scope':'Exact dependence proved; the two actual arithmetic coefficient values are still to be evaluated.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS: every affine origin and exact morphism is retained.')
