#!/usr/bin/env python3
"""Exact labels, quotient maps, and homology checks for F.12.

The full fixed intersection is identified in the accompanying proof.
No assertion that this intersection is trivial is made here.
"""
from itertools import permutations, combinations
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import modular_a5_gt0_f7 as mod
import c5_seven_kernel_exact as alg
from c5_centralizer_labels_f11 import (
    C, R, THETA, ZETA, cinverse, maps_point, canonical, mm, mi, IDENTITY
)


def main():
    G = {p for p in permutations(range(5)) if mod.parity(p) == 0}
    one = tuple(range(5))
    a, b = (1, 0, 3, 2, 4), (2, 1, 4, 3, 0)
    d = mod.multiply(a, b)
    tau = (4, 1, 3, 2, 0)
    D = mod.generated([d], 5)
    N = mod.generated([d, tau], 5)
    words, queue = mod.quotient_transversal(G, a, b)
    cosets = []
    for g in queue:
        cc = frozenset(mod.multiply(g, h) for h in D)
        if cc not in cosets:
            cosets.append(cc)
    index = {cc: i for i, cc in enumerate(cosets)}
    action = {g: tuple(index[frozenset(mod.multiply(g, h) for h in cc)]
                       for cc in cosets) for g in G}
    V4 = {g for g in G if mod.multiply(g, tau) == mod.multiply(tau, g)}
    beta = min(V4-N)
    assert len(V4) == 4 and mod.order(beta) == 2
    assert mod.generated([d, tau, beta], 5) == G
    assert mod.multiply(beta, tau) in V4-N
    A, B = [1, 3, 5, 6, 2], [4, 7, 9, 11, 8]
    pairs = [frozenset([0, 10])] + \
            [frozenset([A[j], B[(-j) % 5]]) for j in range(5)]
    assert set().union(*pairs) == set(range(12))
    for J in pairs:
        assert {action[tau][j] for j in J} == J
    permutation = [pairs.index(frozenset(action[beta][j] for j in J)) for J in pairs]
    assert all(permutation[permutation[i]] == i and permutation[i] != i
               for i in range(6))

    # The branch-labelled double-cover source has coordinate s, with s^2=t.
    # r_j(s)=((zeta^j-s)/(zeta^j+s))^2, j=0..4, with distinguished r_0=1
    # for the pole-pair. The other five coordinates are numbered 1..5.
    s0 = C(0, THETA**2-2)*ZETA
    t0 = C(1-THETA**2)*(ZETA**2)
    assert s0*s0 == t0
    values = [C(1)] + [((ZETA**j-s0)*cinverse(ZETA**j+s0))**2 for j in range(5)]
    common = values[permutation[0]]
    assert all(values[i]*values[permutation[i]] == common for i in range(6))
    # Thus beta descends exactly to V -> common/V, swapping the branch values.
    k = C(1-THETA**2)
    ma = canonical((-k, k, C(-1), k))
    md = canonical((ZETA, C(0), C(0), C(1)))
    mb = mm(ma, md)
    matrices = {1: ma, 2: mb, -2: mi(mb)}
    mbeta = IDENTITY
    for letter in words[beta]:
        mbeta = mm(mbeta, matrices[letter])
    assert maps_point(mbeta, s0, -s0)
    assert maps_point(mbeta, -s0, s0)
    T = canonical((C(1), -s0, C(1), s0))
    transformed = mm(mm(T, mbeta), mi(T))
    assert transformed[0] == transformed[3] == C(0)
    cc = transformed[1]*cinverse(transformed[2])
    assert cc*cc == common

    # Six target difference characters split the abelianization map of F.11.
    # The finite configuration labels are 0,1,2 fixed with exponents 0,2,4,
    # followed by 3,4,5 moving with exponents 0,1,4.
    fixed_exp, moving_exp = [0, 2, 4], [0, 1, 4]
    abelian_character_pairs = [(3, 4), (3, 0), (5, 0), (3, 1), (5, 1), (4, 0)]
    roots = [ZETA**j for j in range(5)]
    character_slopes_and_constants = []
    for i, j in abelian_character_pairs:
        def linear(label):
            if label < 3:
                return C(0), roots[fixed_exp[label]]
            return roots[moving_exp[label-3]], C(0)
        ai, bi = linear(i)
        aj, bj = linear(j)
        aa, bb = ai-aj, bi-bj
        assert aa != C(0)
        root = -bb*cinverse(aa)
        character_slopes_and_constants.append((aa, bb, root))
    assert [row[2] for row in character_slopes_and_constants] == [C(0)]+roots

    # Standard integral H1 cohomology basis for M0,8 normalized at 0,1,infinity.
    generators = [("L", i) for i in range(1, 6)] + \
                 [("M", i) for i in range(1, 6)] + \
                 [("N", i, j) for i, j in combinations(range(1, 6), 2)]
    gi = {g: i for i, g in enumerate(generators)}
    dimension = len(generators)
    assert dimension == 20
    zero = lambda: sp.zeros(1, dimension)
    def L(i):
        out = zero()
        if i:
            out[gi[("L", i)]] = 1
        return out
    def difference(i, j):
        assert i != j
        out = zero()
        if 0 in (i, j):
            out[gi[("M", max(i, j))]] = 1
        else:
            out[gi[("N", min(i, j), max(i, j))]] = 1
        return out
    aa = permutation[0]
    rows = []
    for gen in generators:
        if gen[0] == "L":
            i = gen[1]
            row = L(aa)-L(permutation[i])
        elif gen[0] == "M":
            i = gen[1]
            row = difference(aa, permutation[i])-L(permutation[i])
        else:
            _, i, j = gen
            row = L(aa)+difference(permutation[i], permutation[j]) \
                -L(permutation[i])-L(permutation[j])
        rows.append(row)
    involution = sp.Matrix.vstack(*rows)
    assert involution*involution == sp.eye(dimension)

    # Columns of the divisor matrix are s=0, infinity, +zeta^j, -zeta^j.
    cusps = ["0", "infinity"] + ["+zeta^"+str(j) for j in range(5)] + \
            ["-zeta^"+str(j) for j in range(5)]
    divisor = sp.zeros(dimension, 12)
    for row, gen in enumerate(generators):
        if gen[0] == "L":
            j = gen[1]-1
            divisor[row, 2+j] += 2
            divisor[row, 7+j] -= 2
        elif gen[0] == "M":
            j = gen[1]-1
            divisor[row, 0] += 1
            divisor[row, 1] += 1
            divisor[row, 7+j] -= 2
        else:
            _, ia, ib = gen
            ja, jb = ia-1, ib-1
            jj = (3*(ja+jb)) % 5  # twice jj = ja+jb modulo5.
            divisor[row, 0] += 1
            divisor[row, 1] += 1
            divisor[row, 2+jj] += 1
            divisor[row, 7+jj] += 1
            divisor[row, 7+ja] -= 2
            divisor[row, 7+jb] -= 2
    assert divisor*sp.ones(12, 1) == sp.zeros(dimension, 1)
    keep = [i for i in range(12) if i != 1]  # omit the infinity meridian.
    source = divisor[:, keep]
    fixed_difference = (sp.eye(dimension)-involution)*source
    smith = smith_normal_form(fixed_difference, domain=ZZ)
    diag = [int(smith[i, i]) for i in range(min(smith.shape)) if smith[i, i]]

    # The base abelianization vanishes on the joint seven-map kernel.
    # In the index-two source this leaves the five anti-invariant classes
    # e_(+zeta^j)-e_(-zeta^j). The beta equation has exactly two relations.
    anti = sp.zeros(11, 5)
    for j in range(5):
        anti[j+1, j] = 1
        anti[j+6, j] = -1
    restricted = fixed_difference*anti
    relation1 = sp.Matrix([[1, -1, 1, 0, 0]])
    relation2 = sp.Matrix([[0, -1, 0, 1, 1]])
    row_coefficients = []
    for i in range(dimension):
        row = restricted.row(i)
        first, second = row[0], row[3]
        assert row == first*relation1+second*relation2
        row_coefficients.append([int(first), int(second)])
    assert restricted.row(5) == 2*relation1
    assert restricted.row(8) == 2*relation2
    kernel_basis = [sp.Matrix([-1, 0, 1, 0, 0]),
                    sp.Matrix([1, 1, 0, 1, 0]),
                    sp.Matrix([1, 1, 0, 0, 1])]
    assert all(restricted*v == sp.zeros(dimension, 1) for v in kernel_basis)

    # The explicitly lifted F.11 commutator is
    # e_(-zeta)-e_(+zeta), since its other factor has odd winding about0.
    word_class = -anti[:, 1]
    word_defect = fixed_difference*word_class
    assert word_defect[0] == 4

    result = {
        "status": "PASS",
        "scope": "Exact common-C2 quotient, six-character abelian splitting, integral source restrictions, and one explicit procyclic winding defect. No full fixed-intersection triviality assertion.",
        "beta": beta,
        "beta_word_in_a_b": words[beta],
        "tau_orbit_pairs": [sorted(J) for J in pairs],
        "beta_permutation_of_six_orbits": permutation,
        "s0": s0.encoded(),
        "quotient_beta_formula": "V -> common/V",
        "common": common.encoded(),
        "beta_Mobius_matrix": [x.encoded() for x in mbeta],
        "T_conjugated_beta_matrix": [x.encoded() for x in transformed],
        "normalized_family": "r_j(s)=((zeta^j-s)/(zeta^j+s))^2; distinguished pole-pair coordinate1",
        "F11_abelian_splitting_pairs": abelian_character_pairs,
        "F11_character_pullback_roots": [x[2].encoded() for x in character_slopes_and_constants],
        "F11_character_divisor_matrix_on_finite_source_punctures": [[int(i == j) for j in range(6)] for i in range(6)],
        "target_cohomology_basis": generators,
        "source_cusp_order": cusps,
        "divisor_matrix": [list(map(int, divisor.row(i))) for i in range(dimension)],
        "beta_cohomology_matrix": [list(map(int, involution.row(i))) for i in range(dimension)],
        "source_homology_basis_omits": "infinity",
        "source_cohomology_map_rank": source.rank(),
        "fixed_difference_matrix": [list(map(int, fixed_difference.row(i))) for i in range(dimension)],
        "fixed_difference_rank": fixed_difference.rank(),
        "nonzero_smith_diagonal": diag,
        "rational_kernel_basis": [[str(v) for v in column] for column in fixed_difference.nullspace()],
        "anti_invariant_difference_matrix": [list(map(int, restricted.row(i))) for i in range(dimension)],
        "anti_invariant_two_relations": [list(map(int, relation1)), list(map(int, relation2))],
        "anti_invariant_row_coefficients": row_coefficients,
        "anti_invariant_integral_kernel_basis": [list(map(int, v)) for v in kernel_basis],
        "F11_word_lifted_homology": list(map(int, word_class)),
        "F11_word_winding_defect": list(map(int, word_defect)),
        "F11_word_first_character_defect": int(word_defect[0]),
    }
    target = Path(__file__).with_name("c5_common_reflection_f12_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in (
        "status", "scope", "beta", "beta_word_in_a_b", "tau_orbit_pairs",
        "beta_permutation_of_six_orbits", "source_cohomology_map_rank",
        "fixed_difference_rank", "nonzero_smith_diagonal",
        "anti_invariant_two_relations", "anti_invariant_integral_kernel_basis",
        "F11_word_first_character_defect")}, indent=2))


if __name__ == "__main__":
    main()
