#!/usr/bin/env python3
"""Exact certificates for the rank-three Haran extension and a failed cusp tuple."""
from collections import Counter, deque
from itertools import product, permutations
from pathlib import Path
import json


def mul18(a, b):
    x, y, e = a
    u, v, f = b
    sign = -1 if e else 1
    return ((x + sign*u) % 3, (y + sign*v) % 3, (e+f) % 2)


def generated(mul, one, gens):
    seen = {one}
    queue = deque([one])
    while queue:
        a = queue.popleft()
        for g in gens:
            b = mul(a, g)
            if b not in seen:
                seen.add(b)
                queue.append(b)
    return seen


def mul_perm(a, b):
    return tuple(a[b[i]] for i in range(3))


def inv_perm(a):
    return tuple(a.index(i) for i in range(3))


def pow_perm(a, n):
    ans = (0, 1, 2)
    while n:
        if n & 1:
            ans = mul_perm(ans, a)
        a = mul_perm(a, a)
        n //= 2
    return ans


def prod_perm(*args):
    ans = (0, 1, 2)
    for a in args:
        ans = mul_perm(ans, a)
    return ans


def cycle_name(a):
    seen, cycles = set(), []
    for i in range(3):
        if i in seen:
            continue
        cycle, j = [], i
        while j not in seen:
            seen.add(j)
            cycle.append(j+1)
            j = a[j]
        if len(cycle) > 1:
            cycles.append("(" + " ".join(map(str, cycle)) + ")")
    return "".join(cycles) or "1"


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def power(a, n):
    ans = tuple(range(len(a)))
    while n:
        if n & 1:
            ans = compose(ans, a)
        a = compose(a, a)
        n //= 2
    return ans


def cycles(a):
    seen, out = set(), []
    for i in range(len(a)):
        if i in seen:
            continue
        cycle, j = [], i
        while j not in seen:
            seen.add(j)
            cycle.append(j+1)
            j = a[j]
        out.append(cycle)
    return out


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def twisted_homology_checks():
    rows = []
    for p in (3, 5):
        epsilon_p = -1 if p == 3 else 1
        for name, eta, zeta in (("chi_1", -1, 1),
                                ("chi_2", 1, -1),
                                ("chi_3", -1, -1)):
            e = epsilon_p if eta == 1 else 1
            k = 0 if eta == 1 else 1
            A = [[e, 0, 0], [0, 0, 1], [(1-zeta)*k, eta, 0]]
            v = [eta-1, zeta-1, zeta-1]
            Av = [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]
            assert Av == v
            # The square of pullback differs from eta*I by a coboundary.
            A2 = [[sum(A[i][k]*A[k][j] for k in range(3))
                   for j in range(3)] for i in range(3)]
            pivot = next(i for i in range(3) if v[i] % p)
            for j in range(3):
                col = [(A2[i][j]-(eta if i == j else 0)) % p
                       for i in range(3)]
                scalar = col[pivot]*pow(v[pivot] % p, -1, p) % p
                assert all((col[i]-scalar*v[i]) % p == 0 for i in range(3))
            d = det3(A)
            assert d == -e*eta
            rows.append({"p":p, "character":name,
                "values_on_l_a_b":[eta,zeta,zeta],
                "cocycle_pullback_matrix":A, "fixed_coboundary_vector":v,
                "determinant_on_twisted_H1":d,
                "square_on_twisted_H1":eta})
    assert all(r['determinant_on_twisted_H1'] == 1 for r in rows if r['p']==3)
    assert [r['character'] for r in rows if r['p']==5 and
            r['determinant_on_twisted_H1']==-1] == ['chi_2']
    return rows


def second_candidate_checks():
    group24 = list(permutations(range(4)))
    failures = []
    for a,l in product(group24, repeat=2):
        actual = compose(power(a,5),power(l,5))
        expected = power(compose(a,l),5)
        atype = sorted(map(len,cycles(actual)))
        etype = sorted(map(len,cycles(expected)))
        if atype != etype:
            failures.append({"a":cycles(a),"l":cycles(l),
                "a_to_epsilon_l_to_epsilon":cycles(actual),
                "al_to_epsilon":cycles(expected),
                "actual_cycle_type":atype,"expected_cycle_type":etype})
    assert len(failures) == 96
    chosen = failures[0]
    assert chosen['a'] == [[1],[2,3,4]]
    assert chosen['l'] == [[1,2,3,4]]
    return {"basis":"a,b^(-epsilon),b^epsilon*l",
        "fourth_loop":"(a*l)^(-1)",
        "tested_permutation":"(1 2)(3 4)",
        "tested_multiplier":"-epsilon", "epsilon_mod_12":5,
        "reduced_required_conjugacy":"a^epsilon*l^epsilon ~ (a*l)^epsilon",
        "S4_pairs_tested":24**2,"nonconjugacy_witness_count":len(failures),
        "displayed_witness":chosen}


def main():
    group18 = list(product(range(3), range(3), range(2)))
    identity18 = (0, 0, 0)
    for a, b, c in product(group18, repeat=3):
        assert mul18(mul18(a, b), c) == mul18(a, mul18(b, c))
    counts = Counter(len(generated(mul18, identity18, (a,b)))
                     for a,b in product(group18, repeat=2))
    assert max(counts) == 9 and 18 not in counts
    generators = ((1,0,0), (0,1,0), (0,0,1))
    assert len(generated(mul18, identity18, generators)) == 18
    for a in group18:
        if a[2]:
            assert mul18(a,a) == identity18

    group6 = list(permutations(range(3)))
    epsilon, kappa = 5, 3  # actual profinite exponents reduced modulo exp(S3)=6
    failures = []
    for l,a,b in product(group6, repeat=3):
        P = prod_perm(l, a, pow_perm(b, epsilon))
        phiP = prod_perm(pow_perm(l, epsilon), b, pow_perm(l, kappa),
                        pow_perm(a, epsilon), inv_perm(pow_perm(l,kappa)))
        expected = pow_perm(P, epsilon)
        conjugates = {prod_perm(h, expected, inv_perm(h)) for h in group6}
        if phiP not in conjugates:
            failures.append({"l":cycle_name(l), "a":cycle_name(a),
                "b":cycle_name(b), "P":cycle_name(P),
                "phi_P":cycle_name(phiP), "P_to_epsilon":cycle_name(expected)})
    chosen = next(row for row in failures if row['l']=='(1 2)' and row['a']=='(2 3)')
    out = {"quotient_order": len(group18), "associativity_checks":18**3,
           "ordered_generating_pairs_tested":18**2,
           "pair_generated_subgroup_order_histogram":dict(sorted(counts.items())),
           "minimum_number_of_generators":3,
           "displayed_three_generators":generators,
           "every_element_outside_C3_squared_is_an_involution":True,
           "four_puncture_candidate":{
               "basis": "l,a,b^epsilon",
               "fourth_loop_inverse": "P=l*a*b^epsilon",
               "epsilon_mod_6":epsilon,"kappa_mod_6":kappa,
               "S3_assignments_tested":len(group6)**3,
               "nonconjugacy_witness_count":len(failures),
               "displayed_witness":chosen},
           "twisted_H1_checks":twisted_homology_checks(),
           "second_four_puncture_candidate":second_candidate_checks(),
           "basis_independent_necessary_conditions":{
               "permutation_type":"double transposition",
               "multiplier":"-epsilon",
               "canonical_all_cusps_negative_character_on_l_a_b":[1,-1,-1]},
           "scope": "Every (1,2) marking and every (0,4) marking with an identity or single-transposition cusp permutation is excluded. Both displayed (0,4) candidates fail. D.29 constructs another double-transposition marking using a genuine three-cusp automorphism and its inverse, and identifies the resulting extension with this Haran extension by b'=tau(a)."}
    Path(__file__).with_name('haran_rank3_output.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
