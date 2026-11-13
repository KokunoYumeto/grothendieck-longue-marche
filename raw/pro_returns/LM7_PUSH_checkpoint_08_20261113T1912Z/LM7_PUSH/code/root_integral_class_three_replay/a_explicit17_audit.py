#!/usr/bin/env python3
"""Audit B.20 against the independent arithmetic-agent word collector."""
from pathlib import Path
from itertools import combinations
import contextlib
import importlib.util
import io
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ga',HERE/'a_ihara_gamma2_action.py')
ga=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(ga)
raw=json.loads((HERE/'a_k_lattice.out').read_text())
psi=sp.Matrix(raw['Weil_graph_matrix'])
u,v,c=[sp.Matrix(a) for a in raw['V_generator_matrices']]
pairs=list(combinations(range(10),2))
index={p:i for i,p in enumerate(pairs)}

def wedge(a):
    return sp.Matrix([[a[i,k]*a[j,l]-a[i,l]*a[j,k]
                       for k,l in pairs] for i,j in pairs])

b0=sp.zeros(45,1)
b0[index[8,9]]=3
for i in range(8):
    b0[index[i,8]]=psi[i,1]
    b0[index[i,9]]=-psi[i,0]
n2,c2=wedge(v*u.inv()),wedge(c)
b=(sp.eye(45)-c2)*b0
assert n2*b0==b0 and n2*b==b and c2*b==-b
geometry=json.loads((HERE/'bc_explicit17.json').read_text())
assert list(b)==geometry['b_coordinates']
assert b[44]==6
p=sp.Matrix(json.loads((HERE/'a_ihara_lattice.json').read_text())['A7_to_Schreier_basis'])
bs=np.array(wedge(p)*b,dtype=np.int64).reshape(-1)%3
cert=np.load(HERE/'a_frobenius17_mixed_gluing_local_certificate.npz')
source=np.array(geometry['normalized_source_coordinates_mod3'],dtype=np.int64)
assert not np.any(cert['source_m'][:45,:45].astype(np.int64)@source%3)
assert np.array_equal(cert['source_n'][:45,:45].astype(np.int64)@source%3,bs)
detector=np.load(HERE/'bc_explicit17_certificate.npz')
ell=detector['detector_functional'].astype(np.int64)
row=detector['detector_row_on_gluing_target'].astype(np.int64)
assert np.array_equal(row@cert['target_quotient'].astype(np.int64)%3,ell)
known=cert['known_gluing'].astype(np.int64)
unknown=cert['unknown_gluing'].astype(np.int64)
assert int(row@known[:,:45]@source%3)==1
assert not np.any(row@known[:,45:]%3)
assert all(int(row@a[:,:45]@source%3)==0 for a in unknown)
assert all(not np.any(row@a[:,45:]%3) for a in unknown)
assert np.flatnonzero(ell).tolist()==[0,1,2,3,86,158,214,256,286]
assert np.all(ell[np.flatnonzero(ell)]==2)
print(json.dumps({'integral_n_fixed_c_minus':True,'proper_wedge_coefficient':6,
                  'exact_A7_to_Schreier_comparison':True,
                  'nine_term_detector_indices':np.flatnonzero(ell).tolist(),
                  'detector_value_on_actual_source_family':1,
                  'all_68_unknown_directions_annihilated':True,
                  'all_21_local_conjugators_annihilated':True,
                  'uses_arithmetic_agent_word_collector_matrices':True,
                  'status':'PASS'},indent=2))
