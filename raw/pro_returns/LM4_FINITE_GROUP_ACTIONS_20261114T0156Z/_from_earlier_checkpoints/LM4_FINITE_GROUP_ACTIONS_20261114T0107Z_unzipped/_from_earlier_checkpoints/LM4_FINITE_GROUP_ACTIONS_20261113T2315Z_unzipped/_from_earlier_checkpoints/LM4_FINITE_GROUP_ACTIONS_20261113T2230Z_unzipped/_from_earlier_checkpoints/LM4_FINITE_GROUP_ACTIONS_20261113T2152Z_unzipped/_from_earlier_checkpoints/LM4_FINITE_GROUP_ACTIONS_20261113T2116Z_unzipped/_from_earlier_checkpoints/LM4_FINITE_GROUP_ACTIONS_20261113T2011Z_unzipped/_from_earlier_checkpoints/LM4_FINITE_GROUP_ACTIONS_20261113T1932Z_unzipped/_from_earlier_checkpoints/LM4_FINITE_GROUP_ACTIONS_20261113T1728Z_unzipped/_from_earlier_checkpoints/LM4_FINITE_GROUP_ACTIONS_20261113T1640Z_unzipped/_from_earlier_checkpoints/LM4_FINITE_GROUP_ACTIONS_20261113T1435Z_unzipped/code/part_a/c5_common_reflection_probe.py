#!/usr/bin/env python3
"""Exact finite labels and H1 matrices for a common-reflection comparison.

This is an auxiliary computation for the continuing F.7 attack.
It does not assert that the full fixed intersection is trivial.
"""
from itertools import permutations, combinations
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
import modular_a5_gt0_f7 as mod
import c5_seven_kernel_exact as alg
from c5_centralizer_labels_f11 import C, R, THETA, ZETA, cinverse, maps_point


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

    # These are exact cohomological residue computations; the written note
    # must supply the actual completion and ramification-labelling maps.
    result = {
        "status": "PASS",
        "scope": "Auxiliary exact common-C2 quotient and integral cohomology calculation. No full fixed-intersection triviality assertion.",
        "beta": beta,
        "beta_word_in_a_b": words[beta],
        "tau_orbit_pairs": [sorted(J) for J in pairs],
        "beta_permutation_of_six_orbits": permutation,
        "s0": s0.encoded(),
        "quotient_beta_formula": "V -> common/V",
        "common": common.encoded(),
        "normalized_family": "r_j(s)=((zeta^j-s)/(zeta^j+s))^2; distinguished pole-pair coordinate1",
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
    }
    target = Path(__file__).with_name("c5_common_reflection_probe_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: result[k] for k in (
        "status", "scope", "beta", "beta_word_in_a_b", "tau_orbit_pairs",
        "beta_permutation_of_six_orbits", "source_cohomology_map_rank",
        "fixed_difference_rank", "nonzero_smith_diagonal", "rational_kernel_basis")}, indent=2))


if __name__ == "__main__":
    main()
