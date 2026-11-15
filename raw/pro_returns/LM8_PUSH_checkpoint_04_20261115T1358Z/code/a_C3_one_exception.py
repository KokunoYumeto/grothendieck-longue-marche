#!/usr/bin/env python3
"""Symbolic identities used in the unbounded proof of A.29."""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import sympy as sp


def add(*polys):
    result = {}
    for poly in polys:
        for word, coeff in poly.items():
            result[word] = sp.expand(result.get(word, 0)+coeff)
            if not result[word]:
                del result[word]
    return result


def scale(poly, scalar):
    return {w: sp.expand(c*scalar) for w, c in poly.items() if c*scalar}


def mul(left, right):
    result = {}
    for u, a in left.items():
        for v, b in right.items():
            result[u+v] = sp.expand(result.get(u+v, 0)+a*b)
            if not result[u+v]:
                del result[u+v]
    return result


def bracket(left, right):
    return add(mul(left, right), scale(mul(right, left), -1))


def gen(i):
    return {(i,): 1}


def deriv(images, poly):
    result = {}
    for word, coeff in poly.items():
        for j, letter in enumerate(word):
            for replacement, scalar in images[letter].items():
                target = word[:j]+replacement+word[j+1:]
                result[target] = sp.expand(result.get(target, 0)+coeff*scalar)
                if not result[target]:
                    del result[target]
    return result


# All 15 independent entries of a general skew six-by-six matrix.
J = sp.zeros(6)
for j in (0, 2, 4):
    J[j, j+1], J[j+1, j] = 1, -1
S = sp.zeros(6)
parameters = []
for i in range(6):
    for j in range(i+1, 6):
        symbol = sp.Symbol(f"s{i}{j}")
        parameters.append(symbol)
        S[i, j], S[j, i] = symbol, -symbol
A = S*J.inv()
assert A*J == J*A.T == S
t, V = gen(0), [gen(j+1) for j in range(6)]
omega = add(*({(i+1, j+1): J[i, j]} for i in range(6)
              for j in range(6) if J[i, j]))
omega_A = add(*({(i+1, j+1): S[i, j]} for i in range(6)
                for j in range(6) if S[i, j]))
images = [{}]
for i in range(6):
    Av = add(*(scale(V[j], A[j, i]) for j in range(6)))
    images.append(bracket(t, Av))
assert deriv(images, omega) == bracket(t, omega_A)


# D(t)=0,D(u)=[t,z]. Projection z->u sends D(f) to [t,f].
def lyndon(word):
    return all(word < word[j:] for j in range(1, len(word)))


@lru_cache(None)
def lie_word(word):
    if len(word) == 1:
        return gen(word[0])
    cut = next(j for j in range(1, len(word)) if lyndon(word[j:]))
    return bracket(lie_word(word[:cut]), lie_word(word[cut:]))


abstract_images = [{}, bracket(gen(0), gen(2)), {}]
records = []
for degree in range(1, 9):
    checked = 0
    for word in product(range(2), repeat=degree):
        if not lyndon(word):
            continue
        f = lie_word(word)
        Df = deriv(abstract_images, f)
        projected = add(*({tuple(1 if x == 2 else x for x in w): coeff}
                          for w, coeff in Df.items()))
        assert projected == bracket(gen(0), f)
        checked += 1
    records.append({"abstract_degree": degree, "Lyndon_projection_checks": checked})

out = {
    "statement": "A.29",
    "status": "all exact identities passed",
    "generic_matrix_parameters": len(parameters),
    "self_adjointness": "A J = J A^T = S for a general skew matrix S",
    "quadratic_identity": "D(Omega)=[t,Omega_A] exactly",
    "projection_identity": "z->u sends D(f) to [t,f]",
    "projection_checks": records,
    "scope": "The argument applies in every degree by the derivation rule; finite basis checks certify the implemented conventions only. No actual arithmetic matrix is computed."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
