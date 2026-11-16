#!/usr/bin/env python3
"""Exact certificate against universal NONTRIVIAL primitive-cover existence.

The script certifies the displayed family identities and the nonempty finite
complement. It does NOT claim to enumerate an individual good parameter.
Polynomial arithmetic is in F_2[t,u], using sets of exponent pairs.
"""

import json
from pathlib import Path


def add(*args):
    out = set()
    for a in args:
        out.symmetric_difference_update(a)
    return frozenset(out)


def mul(a, b):
    out = set()
    for i, j in a:
        for k, l in b:
            v = (i + k, j + l)
            if v in out:
                out.remove(v)
            else:
                out.add(v)
    return frozenset(out)


one = frozenset([(0, 0)])
t = frozenset([(1, 0)])
u = frozenset([(0, 1)])


def power(a, n):
    out = one
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


d = add(power(t, 3), one)
X = add(power(u, 2), mul(power(t, 2), u), t)
Z = add(mul(t, power(u, 2)), u, power(t, 2))
Y = add(power(u, 3), one)

# y2=y1+Y/d and x1=X/d, x2=Z/d.
elliptic_identity = add(power(X, 3), power(Z, 3),
                        mul(d, power(Y, 2)), mul(power(d, 2), Y))
inverse_identity = add(Z, mul(t, X), mul(d, u))
pencil_identity = add(mul(Y, d), power(d, 2), mul(X, Z),
                       mul(t, mul(Z, d)), mul(t, power(X, 2)))
assert not elliptic_identity
assert not inverse_identity
assert not pencil_identity
expected_cube = frozenset([(0, 6), (2, 5), (1, 4), (4, 4),
                           (6, 3), (5, 2), (2, 2), (4, 1), (3, 0)])
assert power(X, 3) == expected_cube
assert sorted(j for i, j in power(X, 3) if j % 2) == [1, 3, 5]

# Exact elementary seed for phi(n)>=(2/3)n^(5/6), n odd.
# For primes >=5, (l-1)^6/l^5 is increasing, and the l=5 value exceeds1.
assert 4 ** 6 > 5 ** 5
assert 64 * 729 >= 64 * 243  # the l=3 factor is >=(2/3)^6
assert 27 ** 2 < 800        # (9/2)^(3/2)<10

e = 64
conductor_cutoff = 10 * e ** 3
q = 4 ** e
assert conductor_cutoff % 2 == 0
m = conductor_cutoff // 2
odd_fourth_power_sum = m * (48 * m ** 4 - 40 * m ** 2 + 7) // 15
assert m * (48 * m ** 4 - 40 * m ** 2 + 7) % 15 == 0
# Odd n=3,5,...,B-1; subtract the n=1 term and one from every other n^4.
torsion_incidence_bound = odd_fourth_power_sum - m
excluded_parameters_bound = 4 + torsion_incidence_bound
good_parameters_lower_bound = q - excluded_parameters_bound
assert good_parameters_lower_bound > 0
assert 5 + conductor_cutoff ** 5 < q + 1

result = {
    "status": "all exact identities and inequalities passed",
    "family": "y^2+y=((u^2+t^2*u+t)/(t^3+1))^3, t outside F_4",
    "elliptic_target": "E:y^2+y=x^3; A=E x E",
    "maps": {
        "x1": "(u^2+t^2*u+t)/(t^3+1)", "y1": "y",
        "x2": "(t*u^2+u+t^2)/(t^3+1)",
        "y2": "y+(u^3+1)/(t^3+1)",
        "inverse": "u=x2+t*x1",
        "pencil": "(y2+y1+1+x1*x2)/(x2+x1^2)=t"
    },
    "leading_reduced_odd_AS_coefficient": "t^2/(t^3+1)^3 at u^5",
    "genus": 2,
    "geometric_two_rank": 0,
    "jacobian_isogeny_degree": 2,
    "field": "F_(2^128)=F_(4^64)",
    "e": e,
    "q": q,
    "scalar_frobenius": (-2) ** e,
    "necessary_conductor_condition": "M(M+1)<=2(n-1), M=phi(n)/gcd(ord_n(2),e)",
    "odd_conductor_upper_bound_exclusive": conductor_cutoff,
    "number_of_odd_conductors_covered_by_counting_bound": m - 1,
    "torsion_incidence_upper_bound": torsion_incidence_bound,
    "excluded_finite_parameters_upper_bound": excluded_parameters_bound,
    "good_finite_parameters_lower_bound": good_parameters_lower_bound,
    "simpler_B5_inequality": {"left": 5 + conductor_cutoff ** 5, "right": q + 1},
    "conclusion": "Some displayed smooth C_t has no nontrivial odd cyclic etale cover with primitive two-rank zero.",
    "scope": "Existence theorem via a completely specified finite incidence complement; no individual parameter has been enumerated.",
    "A1_status_for_these_curves": "A1 holds already, since the base Jacobian has geometric two-rank zero."
    ,"degree_one_scope": "The identity cover has P_1=J_C of two-rank zero. These examples do not refute the literal A6 variant permitting degree one."
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
