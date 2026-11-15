#!/usr/bin/env python3
"""Exact certificates accompanying the all-degree proof in A.27.

The proof is the prefix normal form, not the finite rank checks below.
Only standard-library integer and rational arithmetic is used.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


def add(*polys):
    result = {}
    for poly in polys:
        for word, coeff in poly.items():
            result[word] = result.get(word, 0) + coeff
            if not result[word]:
                del result[word]
    return result


def scale(poly, scalar):
    return {w: scalar*c for w, c in poly.items() if scalar*c}


def mul(left, right):
    result = {}
    for u, a in left.items():
        for v, b in right.items():
            result[u+v] = result.get(u+v, 0) + a*b
            if not result[u+v]:
                del result[u+v]
    return result


def bracket(left, right):
    return add(mul(left, right), scale(mul(right, left), -1))


def gen(i):
    return {(i,): 1}


def power(poly, n):
    result = {(): 1}
    for _ in range(n):
        result = mul(result, poly)
    return result


def lyndon(word):
    return all(word < word[j:] for j in range(1, len(word)))


@lru_cache(None)
def lb(word):
    if len(word) == 1:
        return gen(word[0])
    cut = next(j for j in range(1, len(word)) if lyndon(word[j:]))
    return bracket(lb(word[:cut]), lb(word[cut:]))


def basis(degree):
    return [lb(w) for w in product(range(4), repeat=degree) if lyndon(w)]


def deriv(images, poly):
    result = {}
    for word, coeff in poly.items():
        for j, letter in enumerate(word):
            for replacement, scalar in images[letter].items():
                target = word[:j]+replacement+word[j+1:]
                result[target] = result.get(target, 0)+coeff*scalar
                if not result[target]:
                    del result[target]
    return result


def rank_mod(columns, prime=1000003):
    pivots = {}
    for column in columns:
        work = {}
        for word, coeff in column.items():
            coeff = Fraction(coeff)
            value = coeff.numerator*pow(coeff.denominator, -1, prime) % prime
            if value:
                work[word] = value
        while work:
            first = min(work)
            if first not in pivots:
                inverse = pow(work[first], -1, prime)
                pivots[first] = {w: a*inverse % prime for w, a in work.items()}
                break
            factor = work[first]
            for w, a in pivots[first].items():
                new = (work.get(w, 0)-factor*a) % prime
                if new:
                    work[w] = new
                else:
                    work.pop(w, None)
    return len(pivots)


a, b, c, d = [gen(j) for j in range(4)]
omega1, omega2 = bracket(a, b), bracket(c, d)
omega = add(omega1, omega2)

# Triangular bimodule basis: every binary word is the unique leading word
# of omega^r core omega^s, or of a pure omega power. Lexicographic minimum
# in this numerical encoding is the leading word for a>b in the proof.
normal_records = []
for degree in range(9):
    seen = set()
    for word in product(range(2), repeat=degree):
        rest, left, right = word, 0, 0
        while rest[:2] == (0, 1):
            left += 1
            rest = rest[2:]
        if not rest:
            key = ("pure", left)
            poly = power(omega1, left)
        else:
            while rest[-2:] == (0, 1):
                right += 1
                rest = rest[:-2]
            assert rest and rest[:2] != (0, 1) and rest[-2:] != (0, 1)
            key = (left, rest, right)
            poly = mul(mul(power(omega1, left), {rest: 1}),
                       power(omega1, right))
        assert key not in seen
        seen.add(key)
        assert min(poly) == word and poly[word] == 1
    normal_records.append({"degree": degree, "triangular_basis_size": len(seen)})
    assert len(seen) == 2**degree

# Exact CM/local coordinate identities. Fractions here certify rational
# graded coordinates only, including at ell=3.
p1 = add(a, scale(c, 2))
p2 = scale(add(scale(b, 2), scale(d, -1)), Fraction(1, 3))
q1 = scale(add(b, d), Fraction(1, 3))
q2 = add(c, scale(a, -1))
P, Q = bracket(p1, p2), bracket(q1, q2)
A, B = bracket(p1, q1), bracket(p2, q2)
assert add(A, B) == omega
assert scale(add(P, A, scale(B, 2), scale(Q, 2)), Fraction(1, 3)) == omega1
assert scale(add(scale(P, -1), scale(A, 2), B, scale(Q, -2)),
             Fraction(1, 3)) == omega2
# One rational torus example, alpha=2, alpha_bar=3. The arithmetic proof
# uses an actual ordinary Frobenius with ratio of infinite order.
tomega1 = scale(add(scale(P, 4), scale(A, 6), scale(B, 12), scale(Q, 18)),
                Fraction(1, 3))
tomega2 = scale(add(scale(P, -4), scale(A, 12), scale(B, 6), scale(Q, -18)),
                Fraction(1, 3))
assert add(tomega1, tomega2) == scale(omega, 6)
assert rank_mod([omega1, omega2, tomega1, tomega2]) == 3

# Finite consistency checks for all-degree formula A.27.3. Coefficients
# include the apparent cancellation values lambda=-m1 and lambda=-m2.
T = [scale(bracket(omega1, a), 2), scale(bracket(omega1, b), 2),
     bracket(omega2, c), bracket(omega2, d)]
rank_records = []
for lam in (-2, -1, 0, 1, 2):
    images = [add(T[j], scale(bracket(omega, gen(j)), lam)) for j in range(4)]
    assert deriv(images, omega) == {}
    for degree in range(1, 7):
        source = basis(degree)
        rank = rank_mod(deriv(images, poly) for poly in source)
        kernel = len(source)-rank
        expected = ({2: 2, 4: 1, 6: 2}.get(degree, 0) if lam == 0
                    else (1 if degree == 2 else 0))
        assert kernel == expected, (lam, degree, kernel, expected)
        row = {"m1": 2, "m2": 1, "lambda": lam, "degree": degree,
               "source_dimension": len(source), "rank_mod_1000003": rank,
               "kernel_dimension": kernel}
        rank_records.append(row)
        print(json.dumps(row), flush=True)

out = {
    "statement": "A.27",
    "scope": "Certificates for explicit identities and finite consistency checks; the all-degree proof is the prefix normal-form argument in sections/A_D3_fixed_all.tex.",
    "triangular_normal_form": normal_records,
    "CM_identities": "All three identities A.27.13 passed over Q.",
    "two_boundary_planes": "rank(U+tU)=3, so dim(U intersect tU)=1 for alpha=2, alpha_bar=3",
    "kernel_checks": rank_records,
    "geometric_input": "Both edge lengths are nonzero; the cusp specializes to the node because f*O=3P and both elliptic component maps have positive degree."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
print("PASS: triangular bases, CM identities, plane intersection, and all kernel checks", flush=True)
