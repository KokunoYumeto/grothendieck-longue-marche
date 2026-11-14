#!/usr/bin/env python3
"""Determine which remaining Johnson parameters are seen on actual cusp words.

This is a finite exact linear-algebra check.  It does not assign arithmetic
path values from divisor or abelian data.
"""
from pathlib import Path
import importlib.util, json, contextlib, io
import numpy as np

HERE=Path(__file__).resolve().parent
def load(name):
    spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(obj)
    return obj
f=load('de_fermat_schreier')
g=load('a_ihara_gauge')
raw=json.loads((HERE/'a_ihara_mod9_compare.json').read_text())
J=np.array(raw['Johnson_variations'],dtype=np.int64)
H=np.array(raw['metabelian_variations'],dtype=np.int64)
blind=J@g.kernel(H)%3
B=np.array(json.loads((HERE/'a_ihara_lattice.json').read_text())['A7_to_Schreier_basis'],dtype=np.int64)

def evaluate(A, vectors):
    return np.einsum('ijk,jl->ilk',A.reshape(45,10,-1),vectors).reshape(-1,A.shape[1])%3

cusp=evaluate(blind,f.CUSP_VECTORS)
full=evaluate(J,f.CUSP_VECTORS)
proper=evaluate(blind,B[:,8:])
print('Total Johnson uncertainty:',f.rank(J))
print('Total uncertainty restricted to all nine cusp words:',f.rank(full))
print('Metabelian-invisible uncertainty:',f.rank(blind))
print('Invisible uncertainty on actual cusp words:',f.rank(cusp))
print('Invisible uncertainty on the two integral proper lifts:',f.rank(proper))
remain=blind@g.kernel(cusp)%3
print('Invisible uncertainty after fixing every actual cusp path action:',f.rank(remain))
print('Remaining uncertainty modulo c/O-fixing coordinate changes:',
      f.rank(np.hstack((g.D,remain)))-f.rank(g.D))
print('PASS: exact tests use the saved integral lattice and literal cusp words.')
