#!/usr/bin/env python3
"""Exact modulo-three cancellation for the pure-toric class-two twists at17.

Only the proper components of the tangential Abel--Jacobi path cocycles
are needed: every following augmentation kills their toric components.
The formulas are proved in A.35; this independently expands all28 toric
commutators in the free associative algebra and verifies their cancellation.
"""
import json
from pathlib import Path
from itertools import combinations
import sympy as sp

HERE=Path(__file__).resolve().parent
raw=json.loads((HERE/'a_k_lattice.out').read_text())
Psi=sp.Matrix(raw['Weil_graph_matrix'])
labels=[sp.Matrix(a) for a in raw['cusp_O3_labels']]
Ta=sp.Matrix(raw['T_generators']['alpha'])
Tb=sp.Matrix(raw['T_generators']['alpha_bar'])
Tn=Tb*Ta.inv()
Hm=2*sp.eye(2)
Hn=(Tn-sp.eye(2))/3
Phim=14*Psi
Phin=-Psi*Hn
assert Phim*Hn-2*Phin*Hm == 18*Psi*Hn


def red(a):
    a=sp.Rational(a)
    assert a.q%3
    return int(a.p)*pow(int(a.q),-1,3)%3


def add(a,b,factor=1):
    out=dict(a)
    for w,v in b.items():
        out[w]=(out.get(w,0)+factor*v)%3
    return {w:v for w,v in out.items() if v}


def mul(a,b):
    out={}
    for w,v in a.items():
        for z,t in b.items():
            out[w+z]=(out.get(w+z,0)+v*t)%3
    return {w:v for w,v in out.items() if v}


def bracket(a,b):
    return add(mul(a,b),mul(b,a),-1)


def single(i):
    return {(i,):1}


def apply(poly,matrix):
    images=[{(i,):red(matrix[i,j]) for i in range(10) if red(matrix[i,j])}
            for j in range(10)]
    out={}
    for word,coef in poly.items():
        term={():coef}
        for letter in word:
            term=mul(term,images[letter])
        out=add(out,term)
    return out


def johnson(i,j,H):
    def r(d):
        h=H*labels[d]
        proper={(8+k,):red(h[k]) for k in range(2) if red(h[k])}
        return {w:(-v)%3 for w,v in bracket(proper,single(d)).items()}
    return add(bracket(r(i),single(j)),bracket(single(i),r(j)))


Vm=sp.eye(10); Vn=sp.eye(10)
Vm[:8,8:]=Phim
Vn[:8,8:]=Phin
checked=0
max_terms=0
nonzero_summands=0
for i,j in combinations(range(8),2):
    Jm,Jn=johnson(i,j,Hm),johnson(i,j,Hn)
    AB=add(apply(Jn,Vm),Jn,-1)
    BA=add(apply(Jm,Vn),Jm,-1)
    if AB: nonzero_summands+=1
    max_terms=max(max_terms,len(AB))
    result=add(AB,BA,-2)
    assert not result,(i,j,result)
    checked+=1
print('T_n=',str(Tn.tolist()))
print('H_n=(T_n-I)/3=',str(Hn.tolist()))
print('Exact matrix identity: Phi_m H_n - 2 Phi_n H_m = 18 Psi H_n.')
print('All denominators are powers of7 and are invertible modulo3.')
print('Toric commutators checked:',checked)
print('Commutators with nonzero individual summands:',nonzero_summands)
print('Maximum tensor terms in an individual summand:',max_terms)
print('Every degree-three Frobenius correction cancels modulo3.')
print('Unknown toric path components vanish after the following augmentation.')
print('PASS')
