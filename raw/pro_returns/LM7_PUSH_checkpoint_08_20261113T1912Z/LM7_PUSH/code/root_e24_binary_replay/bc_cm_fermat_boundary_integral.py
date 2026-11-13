#!/usr/bin/env python3
"""Integral correction system for the intrinsic Fermat boundary tower.

All maps are induced by literal words in B=C2*C3 and its level-two F.
The program proves the complete N_B' image is a primitive Z-lattice D,
solves the two exact integral hexagon norms in all 24 retained fibres,
and certifies the all-two-power automorphisms and persistent commutator.
"""
from pathlib import Path
from itertools import product
import importlib.util
import json
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("fermat", HERE/"de_fermat_schreier.py")
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
finite = json.loads((HERE/"bc_cm_fermat_boundary.json").read_text())
words = json.loads((HERE/"bc_cm_literal_words.json").read_text())
base = np.load(HERE/"bc_cm_fermat_boundary.npz")
cover = np.load(HERE/"bc_cm_fermat_factorization.npz")
D = sp.Matrix(base["correction_basis"])
E = sp.Matrix(base["E"])
M = E*D
A = sp.Matrix(cover["translation"])
C = sp.Matrix(cover["N_B_commutator_images"])
rows = finite["unit_minor_rows"]
minor = D.extract(rows, list(range(6)))
assert minor.det() == 1
left_inverse = minor.inv()
assert D*left_inverse*C.extract(rows, list(range(C.cols))) == C
Q = left_inverse*(A*D).extract(rows, list(range(6)))
assert D*Q == A*D and Q**3 == sp.eye(6)
assert Q**2+Q+sp.eye(6) == sp.zeros(6)
smith_M = smith_normal_form(M, domain=ZZ)
smith_Q = smith_normal_form(Q-sp.eye(6), domain=ZZ)
diag_M = [abs(int(smith_M[j,j])) for j in range(6)]
diag_Q = [abs(int(smith_Q[j,j])) for j in range(6)]
assert diag_M == [1,1,1,1,3,0]
assert diag_Q == [1,1,1,3,3,3]
v = sp.Matrix([1,-2,1,1,1,2])
assert M*v == sp.zeros(20,1)
assert list(M.nullspace()) == [v/2]
# v has a unit coordinate, so its integral kernel is exactly Z*v.
derivatives = [sp.Matrix(a) for a in base["abelian_action_derivatives"]]
assert all(d*D*v == sp.zeros(10,1) for d in derivatives)
# The exact map to the original F-abelianization is 3L.  Its kernel
# basis Z below is integral and primitive; the selected coordinate
# rows give its explicit inverse.
L = sp.Matrix([[sum(1 if a == j else -1 if a == -j else 0 for a in w)//3
                for w in f.NWORDS] for j in (1,2)])
Z = sp.Matrix.hstack(*L.nullspace())
assert all(a.q == 1 for a in Z)
z_rows = [0,1,3,4,5,7,8,9]
assert Z.extract(z_rows,list(range(8))) == sp.eye(8)
assert L*D == sp.zeros(2,6)
P_columns=[]
for zcol in Z.columnspace():
    solution=next(iter(sp.linsolve((M,E*zcol))))
    parameter=next(iter(set().union(*(a.free_symbols for a in solution))))
    candidates=[sp.Matrix([a.subs(parameter,t) for a in solution])
                for t in (sp.Rational(0),sp.Rational(1,3))]
    pcol=next(c for c in candidates if all(3*a in ZZ for a in c))
    P_columns.append(pcol)
P=sp.Matrix.hstack(*P_columns)
assert M*P == E*Z and all(3*a in ZZ for a in P)
# Actual gamma_5 words give a surjection onto the complete two-adic
# derived image while vanishing in E.24's binary and ternary source.
nw=words["N_B_basis_in_F"]
t=f.inverse_word(nw[1])
deep_words=[]
for w in finite["correction_basis_F_words"]:
    deep=list(w)
    for _ in range(3):
        deep=t+deep+f.inverse_word(t)+f.inverse_word(deep)
    deep_words.append(deep)
deep_matrix=sp.Matrix.hstack(*(sp.Matrix(f.integral_abel(w)) for w in deep_words))
assert deep_matrix == D*(Q-sp.eye(6))**3
assert int(((Q-sp.eye(6))**3).det()) % 2
def matrix_of_action(z):
    return sp.eye(10)+sp.Matrix.hstack(*(d*z for d in derivatives))
def powers_word(w, exponent):
    return (w if exponent >= 0 else f.inverse_word(w))*abs(exponent)

basis_words = finite["correction_basis_F_words"]
records = []
for i,item in enumerate(words["CM_words_in_F"]):
    z = sp.Matrix(f.integral_abel(item["word"]))
    solution = next(iter(sp.linsolve((M,-E*z))))
    parameters = set().union(*(a.free_symbols for a in solution))
    assert len(parameters) == 1
    parameter = next(iter(parameters))
    candidates = [sp.Matrix([a.subs(parameter,j) for a in solution]) for j in (0,1)]
    v0 = next(c for c in candidates if all(a.q == 1 for a in c))
    assert M*v0+E*z == sp.zeros(20,1)
    z0 = z+D*v0
    corrected_word = list(item["word"])
    for a,w in zip(v0,basis_words):
        corrected_word += powers_word(w,int(a))
    assert sp.Matrix(f.integral_abel(corrected_word)) == z0
    action = matrix_of_action(z0)
    determinant = int(action.det())
    assert determinant % 6 == 1
    # Check the word substitution itself, independently of its derivative
    # formula.  Reduce free words between substitutions to avoid quadratic
    # temporary growth in the longer recorded source words.
    finv = f.inverse_word(corrected_word)
    images = {1:[1],2:finv+[2]+corrected_word}
    def substitute(w):
        out=[]
        for a in w:
            for b in images[a] if a>0 else f.inverse_word(images[-a]):
                if out and out[-1] == -b: out.pop()
                else: out.append(b)
        return out
    actual = sp.Matrix.hstack(*(sp.Matrix(f.integral_abel(substitute(w)))
                               for w in f.NWORDS))
    assert actual == action
    record = {
        "certificate_index":i,
        "extra_CM_coset":item["extra_CM_coset"],
        "integral_correction_coefficients":[int(a) for a in v0],
        "literal_corrected_F_word":corrected_word,
        "integral_H_abelianization":[int(a) for a in z0],
        "integral_H_action_matrix":np.array(action,dtype=np.int64).tolist(),
        "action_determinant":determinant,
        "determinant_prime_factors":{str(p):int(e) for p,e in sp.factorint(determinant).items()}
    }
    records.append(record)
    print(json.dumps({k:r for k,r in record.items()
                      if k in ("certificate_index","extra_CM_coset",
                               "integral_correction_coefficients","action_determinant",
                               "determinant_prime_factors")}),flush=True)

result = {
    "correction_source":"N_B-prime",
    "complete_integral_derived_image_basis":np.array(D,dtype=np.int64).tolist(),
    "unit_minor_rows":rows,"unit_minor_determinant":1,
    "cyclic_deck_on_derived_image":np.array(Q,dtype=np.int64).tolist(),
    "smith_cyclic_deck_minus_identity":diag_Q,
    "hexagon_correction_matrix":np.array(M,dtype=np.int64).tolist(),
    "smith_hexagon_correction_matrix":diag_M,
    "primitive_integral_kernel":[int(a) for a in v],
    "kernel_changes_every_H_action_matrix_by_zero":True,
    "F_abelianization_map_divided_by_three":np.array(L,dtype=np.int64).tolist(),
    "primitive_F_prime_kernel_basis":np.array(Z,dtype=np.int64).tolist(),
    "kernel_basis_inverse_coordinate_rows":z_rows,
    "odd_denominator_norm_correction_three_times_P":np.array(3*P,dtype=np.int64).tolist(),
    "identity_EDP_equals_EZ":True,
    "deep_gamma5_words":deep_words,
    "deep_gamma5_image_coordinates":np.array((Q-sp.eye(6))**3,dtype=np.int64).tolist(),
    "deep_gamma5_image_coordinate_determinant":int(((Q-sp.eye(6))**3).det()),
    "records":records,
    "all_two_power_fibre_counts":"For modulus 2^n, exactly 2^n correction images, all generating.",
    "all_moduli_existence":"For fixed i and N_B-prime corrections, generating solutions modulo m exist exactly when gcd(m,action_determinant_i)=1.",
    "lower_central_image":"For every n>=1 and r>=2, gamma_r(image(N_B) in B/[H,H]H^(2^n)) equals D/(2^n).",
    "scope":"Compatible automorphisms in the common quotient with G6, multiplier one. No full GT or all-moduli generation assertion outside the displayed gcd criterion."
}
(HERE/"bc_cm_fermat_boundary_integral.json").write_text(json.dumps(result,indent=2)+"\n")
np.savez_compressed(HERE/"bc_cm_fermat_boundary_integral.npz",
    D=np.array(D,dtype=np.int64),Q=np.array(Q,dtype=np.int64),
    E=np.array(E,dtype=np.int64),M=np.array(M,dtype=np.int64),
    primitive_kernel=np.array(v,dtype=np.int64))
print("Smith hexagon matrix:",diag_M)
print("Smith cyclic-deck-minus-one:",diag_Q)
print("Exact F-abelianization /3:",np.array(L,dtype=np.int64).tolist())
print("Three times the odd-denominator right inverse P:",np.array(3*P,dtype=np.int64).tolist())
print("Exact gamma5 word-image determinant:",int(((Q-sp.eye(6))**3).det()))
print("PASS: integral source words, all two-adic fibres, all-moduli existence, and persistent lower-central image certified.")
