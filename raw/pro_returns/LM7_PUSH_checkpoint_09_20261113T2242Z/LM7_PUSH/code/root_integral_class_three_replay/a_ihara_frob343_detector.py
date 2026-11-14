#!/usr/bin/env python3
"""Apply the based F343 Heisenberg descent constraint to the finite action.

Only cochain-independent equations are used: U^3=1 removes the unknown
linear central map of a Heisenberg quotient.  We test explicitly whether
the unspecified proper components of the Miller character matter.
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
f=load('de_fermat_schreier');g=load('a_ihara_gauge')
raw=json.loads((HERE/'a_ihara_final_parameters.json').read_text())
J0=np.array(raw['base_Johnson_matrix'],dtype=np.int64)
JJ=[np.array(A,dtype=np.int64) for A in raw['correction_matrices']]
U,_=f.generator_images(np.array(raw['base_fa']),np.array(raw['base_fz']),7)
W=f.exterior(U);U2=U@U%3;W2=W@W%3
assert np.array_equal(U2@U%3,np.eye(10,dtype=np.int64))
def cube(J):return (J@U2+W@J@U+W2@J)%3
Z0=cube(J0);ZZ=[cube(J) for J in JJ]
B=sp.Matrix(json.loads((HERE/'a_ihara_lattice.json').read_text())['A7_to_Schreier_basis'])
def char(a):return np.array((sp.Matrix([list(a)])*B.inv()).tolist()[0],dtype=np.int64)%3
alpha=np.zeros(10,dtype=np.int64);alpha[0]=2
beta=np.zeros(10,dtype=np.int64);beta[0]=beta[1]=1
alpha=char(alpha);beta=char(beta)
def form(a,b):return np.array([a[i]*b[j]-a[j]*b[i] for i,j in zip(*f.UP)],dtype=np.int64)%3
om=form(alpha,beta)
base=om@Z0%3;effects=np.stack([om@Z for Z in ZZ],axis=1)%3
print('Frobenius343 central matrix base rank:',f.rank(Z0))
print('Frobenius343 Johnson parameter matrix ranks:',[f.rank(Z) for Z in ZZ])
print('Zero-proper Miller detector base row:',base.tolist())
print('Its parameter coefficient rank:',f.rank(effects))
proper=[]
for i in (8,9):
 a=np.zeros(10,dtype=np.int64);a[i]=1
 op=form(char(a),beta)
 bb=op@Z0%3;ee=np.stack([op@Z for Z in ZZ],axis=1)%3
 proper.append({'index':i,'base':bb.tolist(),'effects':ee.tolist()})
 print('Proper Miller component',i,'base row',bb.tolist(),'parameter rank',f.rank(ee))
out={'base':base.tolist(),'parameter_coefficients':effects.tolist(),
     'proper_component_terms':proper,'parameter_origins':raw['base_coefficient_values'],
     'U':U.tolist(),'Frob343_base_central':Z0.tolist(),
     'Frob343_parameter_central':[Z.tolist() for Z in ZZ]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS: all dependence on unknown proper Miller character components is displayed.')
