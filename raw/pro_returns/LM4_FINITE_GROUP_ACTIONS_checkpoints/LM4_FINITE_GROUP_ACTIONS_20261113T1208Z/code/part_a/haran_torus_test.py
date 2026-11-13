#!/usr/bin/env python3
"""D.39: exact finite cusp obstructions and the regular mod-two module."""
from itertools import product
from pathlib import Path
import json


def generated(identity, generators, multiply):
    seen, todo = {identity}, [identity]
    for value in todo:
        for generator in generators:
            nxt = multiply(value, generator)
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return seen


def verify(group, identity, multiply, inverse, a, b, epsilon, kappa):
    def power(g, n):
        result = identity
        for _ in range(n):
            result = multiply(result, g)
        return result

    def order(g):
        for n in range(1, len(group) + 1):
            if power(g, n) == identity:
                return n
        raise AssertionError

    def commutator(g, h):
        return multiply(multiply(multiply(g, h), inverse(g)), inverse(h))

    aa = multiply(multiply(inverse(b), power(a, epsilon)), b)
    bb = multiply(inverse(b), power(a, kappa))
    c = commutator(a, b)
    ac = commutator(aa, bb)
    required = inverse(c)  # (-epsilon)_7=-1, and c has order7.
    from_c = [g for g in group if multiply(multiply(g, c), inverse(g)) == ac]
    from_inverse = [g for g in group
                    if multiply(multiply(g, required), inverse(g)) == ac]
    class_c = {multiply(multiply(g, c), inverse(g)) for g in group}
    class_inverse = {multiply(multiply(g, required), inverse(g)) for g in group}
    assert order(a) == order(b) == 3
    assert order(c) == order(ac) == 7
    assert from_c and not from_inverse
    assert class_c.isdisjoint(class_inverse)
    return {
        "group_order": len(group),
        "a": a, "b": b,
        "a_order": order(a), "b_order": order(b),
        "generated_order": len(generated(identity, [a, b], multiply)),
        "commutator": c,
        "alpha_a": aa, "alpha_b": bb, "alpha_commutator": ac,
        "required_commutator_power": required,
        "commutator_order": order(c),
        "conjugators_from_c": len(from_c),
        "conjugators_from_required_inverse": len(from_inverse),
        "class_of_c": sorted(class_c),
        "class_of_inverse_c": sorted(class_inverse),
    }


def main():
    vectors = list(product(range(2), repeat=2))
    # The cohomology action is the contragredient of the homology matrix.
    # In characteristic two A^-1=A, so the matrix is A^transpose.
    def cohomology_action(v):
        return v[0], (v[0] + v[1]) % 2

    def norm(v):
        av = cohomology_action(v)
        return (v[0] + av[0]) % 2, (v[1] + av[1]) % 2

    norm_image = {norm(v) for v in vectors}
    norm_kernel = {v for v in vectors if norm(v) == (0, 0)}
    assert norm_image == norm_kernel == {(0, 0), (0, 1)}
    assert all(cohomology_action(cohomology_action(v)) == v for v in vectors)
    regular_module = {
        "homology_matrix_mod2": [[1, 1], [0, 1]],
        "cohomology_matrix_mod2": [[1, 0], [1, 1]],
        "norm_image": sorted(norm_image),
        "norm_kernel": sorted(norm_kernel),
        "positive_degree_C2_cohomology_dimension": 0,
        "consequence_proved_in_tex": "The split Hochschild-Serre spectral sequence gives dim H^n(E,F2)=1 for n>=3. Brown restriction gives one H-conjugacy class of involutions."
    }
    frobenius = list(product(range(7), range(3)))

    def fm(a, b):
        return (a[0] + pow(2, a[1], 7) * b[0]) % 7, (a[1] + b[1]) % 3

    def fi(a):
        return (-pow(2, -a[1], 7) * a[0]) % 7, -a[1] % 3

    # epsilon=8 mod21, kappa=0 mod21.
    first = verify(frobenius, (0, 0), fm, fi, (0, 1), (1, 1), 8, 0)
    assert first["generated_order"] == 21
    assert first["alpha_commutator"] == first["commutator"] == (1, 0)

    def canonical(a):
        a = tuple(v % 7 for v in a)
        return min(a, tuple(-v % 7 for v in a))

    def pm(a, b):
        return canonical((a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                          a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))

    def pi(a):
        return canonical((a[3], -a[1], -a[2], a[0]))

    psl = sorted({canonical(a) for a in product(range(7), repeat=4)
                  if (a[0]*a[3]-a[1]*a[2]) % 7 == 1})
    assert len(psl) == 168
    # epsilon=29 mod84, kappa=21 mod84.
    second = verify(psl, canonical((1, 0, 0, 1)), pm, pi,
                    (0, 1, 6, 1), (0, 2, 3, 1), 29, 21)
    result = {
        "claim": "D.39",
        "convention": "[a,b]=aba^-1b^-1; matrices are modulo scalar +/-I",
        "regular_mod2_module": regular_module,
        "frobenius_21": first,
        "PSL2_F7": second,
        "scope": "The finite quotients explicitly obstruct the natural cusp. The complete proof in haran_torus_test.tex excludes every pants or torus marking: trace obstructs pants, and the unique involution class with trivial kernel-centralizer contradicts the nonzero Z3 cusp subgroup fixed by its norm-adjusted involution."
    }
    Path(__file__).with_name("haran_torus_test_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
