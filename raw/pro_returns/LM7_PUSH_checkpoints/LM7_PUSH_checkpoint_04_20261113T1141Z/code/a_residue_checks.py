#!/usr/bin/env python3
"""Exact checks for the rank-44 residue calculation and its counterexamples.

This verifies finite linear algebra used by the proofs. It does not purport to
compute Frobenius matrices of the full arithmetic fundamental group.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import json


def v3(n):
    n = abs(int(n))
    assert n
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def fermat_points(p):
    # Disjoint normalized projective charts: z=1, then y=1,z=0, then [1:0:0].
    pts = [(x, y, 1) for x in range(p) for y in range(p)
           if (x**3 + y**3 + 1) % p == 0]
    pts += [(x, 1, 0) for x in range(p) if (x**3 + 1) % p == 0]
    if 1 % p == 0:
        pts.append((1, 0, 0))
    return pts

Pplus, Pminus = 5, 3
wedge_plus = comb(Pplus, 2) + comb(Pminus, 2)
wedge_minus = Pplus * Pminus
assert (wedge_plus, wedge_minus) == (13, 15)
points2 = fermat_points(2)
assert len(points2) == 3
trace2 = 2 + 1 - len(points2)
assert trace2 == 0
# Rational characteristic factors determine the determinant on every stable lattice.
det_wedge = (2 - 1)**wedge_plus * (-2 - 1)**wedge_minus
det_tensor = (1 - trace2 + 2)**Pplus * (1 + trace2 + 2)**Pminus
det_total = det_wedge * det_tensor
assert abs(det_total) == 3**23

# W has the basis (P,Q,A,Abar,B,Bbar,C,Cbar), O is minus their sum.
basis = ['P','Q','A','Abar','B','Bbar','C','Cbar']
e = [[int(i == j) for i in range(8)] for j in range(8)]
eO = [-1]*8
w = [eO[i] + e[0][i] for i in range(8)]
for cusp in [eO]+e:
    ratios = {Fraction(a,b) for a,b in zip(w,cusp) if b}
    assert not (len(ratios) == 1 and all(b or a == 0 for a,b in zip(w,cusp)))
# v0 = 3v_P in the tangential cusp-path formula.
v0 = [Fraction(-2), Fraction(-1), Fraction(-1,2), Fraction(-1,2),
      Fraction(-1), Fraction(-1), Fraction(-3,2), Fraction(-3,2)]
v0_wedge_eP = {(basis[i],basis[j]):v0[i]*e[0][j]-v0[j]*e[0][i]
               for i,j in combinations(range(8),2)}
assert v0_wedge_eP[('P','Q')] == 1
# All denominators are 3-adic units, and at least one coefficient is a unit.
assert all(x.denominator % 3 for x in v0_wedge_eP.values())
assert any(x and x.numerator % 3 for x in v0_wedge_eP.values())

out = {
    'rank_K': comb(10,2)-comb(2,2),
    'rank_wedge_W': comb(8,2), 'rank_T_tensor_W':2*8,
    'cusp_permutation_plus_minus':[Pplus,Pminus],
    'wedge_cusp_permutation_plus_minus':[wedge_plus,wedge_minus],
    'E_F2_points':points2, 'E_F2_trace':trace2,
    'det_D2_wedge_factor':det_wedge,
    'det_D2_tensor_factor':det_tensor,
    'v3_det_D2':v3(det_total),
    'T1_tame_vector': [3**23*x for x in w],
    'T1_vector_is_cusp_multiple':False,
    'commutator_origin_wedge_primitive':True,
    'origin_wedge_nonzero_coefficients':{
       str(k):str(v) for k,v in v0_wedge_eP.items() if v
    },
    'K_complex_conjugation_plus_minus':[21,23]
}
print(json.dumps(out, indent=2))
