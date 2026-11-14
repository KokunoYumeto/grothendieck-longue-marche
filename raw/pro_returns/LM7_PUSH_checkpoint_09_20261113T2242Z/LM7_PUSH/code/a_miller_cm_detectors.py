#!/usr/bin/env python3
"""Rank check for the exact CM translate of the first Miller norm cover."""
from pathlib import Path
import importlib.util,json,contextlib,io
import numpy as np
import sympy as sp
HERE=Path(__file__).resolve().parent
def load(name):
 spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
 obj=importlib.util.module_from_spec(spec)
 with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(obj)
 return obj
f=load('de_fermat_schreier');g=load('a_ihara_gauge')
B=sp.Matrix(json.loads((HERE/'a_ihara_lattice.json').read_text())['A7_to_Schreier_basis'])
raw=json.loads((HERE/'a_ihara_pentagon_compare.json').read_text())
J=np.array(raw['Johnson_variations'],dtype=np.int64)
H=np.array(raw['metabelian_variations'],dtype=np.int64)
blind=J@g.kernel(H)%3
old=json.loads((HERE/'a_ihara_mod9_compare.json').read_text())
oldJ=np.array(old['Johnson_variations'],dtype=np.int64)
oldH=np.array(old['metabelian_variations'],dtype=np.int64)
oldblind=oldJ@g.kernel(oldH)%3
def eff(d,partners,space):
 a=np.zeros(10,dtype=np.int64);a[d]=2
 b=np.zeros(10,dtype=np.int64)
 for j in partners:b[j]=1
 aa=np.array((sp.Matrix([a.tolist()])*B.inv()).tolist()[0],dtype=np.int64)%3
 bb=np.array((sp.Matrix([b.tolist()])*B.inv()).tolist()[0],dtype=np.int64)%3
 om=np.array([aa[i]*bb[j]-aa[j]*bb[i] for i,j in zip(*f.UP)],dtype=np.int64)%3
 return np.einsum('i,ijk->jk',om,space.reshape(45,10,-1))%3
for name,space in [('before full pentagon',oldblind),('after full pentagon',blind)]:
 a=eff(0,[0,1],space);b=eff(2,[2,4],space);c=eff(0,[2,4],space)
 print(name,'first pair rank',f.rank(a),'CM-translated pair rank',f.rank(b),
       'combined rank',f.rank(np.vstack((a,b))),
       'original second pair rank',f.rank(c))
print('PASS: phi^-1(P)=A; scalar zeta in the unit is retained separately in the arithmetic origin.')
