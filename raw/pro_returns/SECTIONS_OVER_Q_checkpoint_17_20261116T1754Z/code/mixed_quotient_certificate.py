#!/usr/bin/env python3
"""Exact finite and symbolic checks accompanying A.50 and A.51.

The profinite assertions are proved in the manuscript.  These checks
verify the coordinate identities, the listed finite group data, and
the changed factorial indices; they do not execute the large prime
recursion or assert local point matching in a finite quotient.
"""
from itertools import permutations, product
from math import factorial
import json
import sympy as sp


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    b = [0] * len(a)
    for i, v in enumerate(a):
        b[v] = i
    return tuple(b)


def closure(generators, identity):
    generators = tuple(set(generators))
    seen = {identity}
    todo = [identity]
    while todo:
        a = todo.pop()
        for b in generators:
            c = compose(a, b)
            if c not in seen:
                seen.add(c)
                todo.append(c)
    return seen


def parity(a):
    return sum(a[i] > a[j] for i in range(len(a))
               for j in range(i + 1, len(a))) % 2


def group_data(group):
    group = set(group)
    identity = tuple(range(len(next(iter(group)))))
    inv = {a: inverse(a) for a in group}
    commutators = {
        compose(compose(compose(a, b), inv[a]), inv[b])
        for a in group for b in group
    }
    derived = closure(commutators, identity)
    assert derived <= group
    exponent = 1
    while True:
        success = True
        for a in group:
            power = identity
            for _ in range(exponent):
                power = compose(power, a)
            if power not in derived:
                success = False
                break
        if success:
            break
        exponent += 1
    return {
        "order": len(group), "derived_order": len(derived),
        "abelianization_order": len(group) // len(derived),
        "abelianization_exponent": exponent,
        "commutators_checked": len(group) ** 2,
    }


def psl2_prime(p):
    """Faithful projective action on P^1(F_p); p denotes infinity."""
    result = set()
    for a, b, c, d in product(range(p), repeat=4):
        if (a * d - b * c) % p != 1:
            continue
        image = []
        for x in range(p + 1):
            num, den = (a, c) if x == p else (a * x + b, c * x + d)
            image.append(p if den % p == 0 else num * pow(den, -1, p) % p)
        result.add(tuple(image))
    return result


def symbolic_class_two():
    checks = 0
    for r in range(2, 6):
        aa = sp.symbols(f"a0:{r}")
        bb = sp.symbols(f"b0:{r}")
        cc = sp.symbols(f"c0:{r}")
        for i in range(r):
            for j in range(i + 1, r):
                left = aa[i] * bb[j] + (aa[i] + bb[i]) * cc[j]
                right = bb[i] * cc[j] + aa[i] * (bb[j] + cc[j])
                assert sp.expand(left - right) == 0
                # Pair projection keeps exactly this central polynomial.
                assert sp.expand(aa[i] * bb[j] -
                                 sp.Matrix([aa[i], aa[j]])[0] *
                                 sp.Matrix([bb[i], bb[j]])[1]) == 0
                checks += 2
    return checks


def valuation(n, p):
    result = 0
    while n % p == 0:
        result += 1
        n //= p
    return result


def factorial_precision():
    checks = 0
    for k in range(4, 17):
        for j in range(11):
            n, m = factorial(j + k), factorial(j + k + 1)
            assert n % 24 == 0 and n % 8 == 0
            assert j + k + 1 <= (n + 1) ** 4
            for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
                e, d = valuation(n, p), valuation(m, p)
                H = 2 * d + j + 3
                assert H > 2 * e
                assert H - e >= d
                checks += 2
    for modulus in range(1, 1001):
        k = 4
        while factorial(k) % modulus:
            k += 1
        for j in range(5):
            assert factorial(j + k) % modulus == 0
            checks += 1
    return checks


def main():
    s4 = set(permutations(range(4)))
    a4 = {p for p in s4 if parity(p) == 0}
    a5 = {p for p in permutations(range(5)) if parity(p) == 0}
    v4 = closure([(1, 0, 3, 2), (2, 3, 0, 1)], tuple(range(4)))
    groups = {
        "A4": group_data(a4), "V4": group_data(v4),
        "S4": group_data(s4), "A5": group_data(a5),
        "PSL2(F7)": group_data(psl2_prime(7)),
    }
    expected = {
        "A4": (12, 4, 3), "V4": (4, 1, 2),
        "S4": (24, 12, 2), "A5": (60, 60, 1),
        "PSL2(F7)": (168, 168, 1),
    }
    for name, (order, derived, exponent) in expected.items():
        row = groups[name]
        assert (row["order"], row["derived_order"],
                row["abelianization_exponent"]) == (order, derived, exponent)
    print(json.dumps({
        "symbolic_class_two_identities": symbolic_class_two(),
        "finite_groups": groups,
        "shifted_factorial_checks": factorial_precision(),
        "status": "all checks passed",
        "scope": "No large prime search, full-section construction, or local matching claimed."
    }, indent=2))


if __name__ == "__main__":
    main()
