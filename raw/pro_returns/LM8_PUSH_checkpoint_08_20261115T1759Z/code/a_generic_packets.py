#!/usr/bin/env python3
"""Exact finite-degree checks for A.24; no Galois matrix is supplied.

The unbounded kernel statements are proved in the text.  This certificate
tests possible resonances in an invertible mixed-boundary derivation and
checks the symplectic centralizer ranks in a separate free Lie algebra.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
import sympy as sp


def add(*polys):
    result = {}
    for poly in polys:
        for word, coeff in poly.items():
            result[word] = result.get(word, 0) + coeff
            if not result[word]:
                del result[word]
    return result


def scale(poly, scalar):
    return {word: scalar * coeff for word, coeff in poly.items()
            if scalar * coeff}


def mul(left, right):
    result = {}
    for u, a in left.items():
        for v, b in right.items():
            word = u + v
            result[word] = result.get(word, 0) + a * b
            if not result[word]:
                del result[word]
    return result


def bracket(left, right):
    return add(mul(left, right), scale(mul(right, left), -1))


def generator(i):
    return {(i,): 1}


def is_lyndon(word):
    return all(word < word[i:] for i in range(1, len(word)))


@lru_cache(None)
def lyndon_bracket(word):
    if len(word) == 1:
        return generator(word[0])
    # The first such suffix is the longest proper Lyndon suffix.
    cut = next(i for i in range(1, len(word)) if is_lyndon(word[i:]))
    assert is_lyndon(word[:cut])
    return bracket(lyndon_bracket(word[:cut]),
                   lyndon_bracket(word[cut:]))


def lie_basis(rank, degree):
    return [lyndon_bracket(word)
            for word in product(range(rank), repeat=degree)
            if is_lyndon(word)]


def derivation(images, poly):
    result = {}
    for word, coeff in poly.items():
        for pos, letter in enumerate(word):
            for replacement, scalar in images[letter].items():
                target = word[:pos] + replacement + word[pos + 1:]
                result[target] = result.get(target, 0) + coeff * scalar
                if not result[target]:
                    del result[target]
    return result


def sparse_rank_mod(columns, prime=1000003):
    """A nonzero minor modulo a prime certifies the corresponding Q-rank."""
    pivots = {}
    for col in columns:
        work = {word: value % prime for word, value in col.items()
                if value % prime}
        while work:
            key = min(work)
            if key not in pivots:
                inverse = pow(work[key], -1, prime)
                pivots[key] = {word: value * inverse % prime
                               for word, value in work.items()}
                break
            factor = work[key]
            for word, value in pivots[key].items():
                new = (work.get(word, 0) - factor * value) % prime
                if new:
                    work[word] = new
                else:
                    work.pop(word, None)
    return len(pivots)


def sign_substitution(poly, signs):
    result = {}
    for word, coeff in poly.items():
        factor = 1
        for letter in word:
            factor *= signs[letter]
        result[word] = coeff * factor
    return result


# Opposite eigenvalue pairs are intentional: a naive sum-of-weights
# argument would encounter zero sums, while the maximum-jet proof does not.
eigenvalues = [1, 1, -1, -1, 2, 2]
t = generator(0)
C_images = [{}] + [scale(bracket(t, generator(j + 1)), value)
                    for j, value in enumerate(eigenvalues)]
signs = [1] + [-1] * 6
for j in range(7):
    assert sign_substitution(C_images[j], signs) == scale(C_images[j], signs[j])
C_ranks = []
for degree in range(1, 5):
    basis = lie_basis(7, degree)
    rank = sparse_rank_mod(derivation(C_images, word) for word in basis)
    expected = len(basis) - (1 if degree == 1 else 0)
    assert rank == expected
    C_ranks.append({"degree": degree, "domain_dimension": len(basis),
                    "rank_mod_1000003": rank,
                    "kernel_dimension": len(basis) - rank})

x1, y1, x2, y2 = map(generator, range(4))
omega = add(bracket(x1, y1), bracket(x2, y2))
D_ranks = []
for degree in range(1, 6):
    basis = lie_basis(4, degree)
    rank = sparse_rank_mod(bracket(omega, word) for word in basis)
    expected = len(basis) - (1 if degree == 2 else 0)
    assert rank == expected
    D_ranks.append({"degree": degree, "domain_dimension": len(basis),
                    "rank_mod_1000003": rank,
                    "kernel_dimension": len(basis) - rank})
assert bracket(omega, omega) == {}

n, beta = sp.symbols("n beta")
determinant = sp.prod(value + n * beta for value in eigenvalues).expand()
assert sp.Poly(determinant, n).degree() == 6
assert sp.Poly(determinant, n).LC() == beta ** 6
J = sp.diag(*[sp.Matrix([[0, 1], [-1, 0]]) for _ in range(3)])
A = sp.diag(*eigenvalues)
assert A * J == J * A.T


def pfaffian(matrix):
    if matrix.rows == 0:
        return sp.Integer(1)
    result = 0
    for j in range(1, matrix.rows):
        keep = [i for i in range(matrix.rows) if i not in (0, j)]
        result += (-1)**(j+1) * matrix[0, j] * pfaffian(matrix.extract(keep, keep))
    return sp.expand(result)


pfaffian_polynomial = sp.expand(pfaffian((A + n * beta * sp.eye(6)) * J) / pfaffian(J))
assert sp.expand(pfaffian_polynomial**2 - determinant) == 0
assert sp.Poly(pfaffian_polynomial, n).degree() == 3
assert sp.Poly(pfaffian_polynomial, n).LC() == beta**3

# General symbolic middle-letter coefficient identity for the other cusp.
entries = sp.symbols("a0:36")
Ageneral = sp.Matrix(6, 6, entries)
general_images = [{}] + [
    add(*(scale(bracket(t, generator(k + 1)), Ageneral[k, j])
          for k in range(6))) for j in range(6)]
omega6 = add(*(bracket(generator(2*j+1), generator(2*j+2)) for j in range(3)))
image_omega6 = derivation(general_images, omega6)
middle = sp.Matrix(6, 6, lambda i, j: image_omega6.get((i+1, 0, j+1), 0))
assert middle == -Ageneral * J + J * Ageneral.T

# Exact valuations in the displayed smooth hyperelliptic models.
C_infinity = {"ord_w": -2, "ord_v": -7}
C_zero = {"ord_w": 2, "ord_v": 1}
D_infinity = {"ord_t": -2, "ord_z": -5}
ord_C_tangent = 3 * C_infinity["ord_w"] - C_infinity["ord_v"]
ord_base_tangent = 2 * C_infinity["ord_w"] - C_infinity["ord_v"]
ord_C_zero_map = C_zero["ord_w"] + C_zero["ord_v"]
ord_D_tangent = 2 * D_infinity["ord_t"] - D_infinity["ord_z"]
assert (ord_C_tangent, ord_base_tangent, ord_C_zero_map, ord_D_tangent) == (1, 3, 3, 1)

# Each tangent parameter has one factor v^{-1}, v, or z^{-1};
# the hyperelliptic involution therefore has derivative -1.
w, v = sp.symbols("w v", nonzero=True)
tvar, z = sp.symbols("t z", nonzero=True)
for parameter, variable in [(w**3/v, v), (v, v), (tvar**2/z, z)]:
    assert sp.simplify(parameter.subs(variable, -variable) + parameter) == 0

out = {
    "statement": "A.24",
    "scope": "Finite exact Lie and local-coordinate certificates; no actual Galois Johnson matrix is computed.",
    "mixed_boundary_matrix_eigenvalues": eigenvalues,
    "mixed_boundary_first_derivation_ranks": C_ranks,
    "symplectic_centralizer_ranks": D_ranks,
    "illustrative_determinant": str(determinant),
    "determinant_degree": 6,
    "determinant_leading_coefficient": str(beta**6),
    "peripheral_constraint": "A J = J A^T, certified by the general symbolic v_i t v_j coefficient matrix",
    "illustrative_pfaffian_polynomial": str(pfaffian_polynomial),
    "pfaffian_degree": 3,
    "pfaffian_leading_coefficient": str(beta**3),
    "maximum_excluded_twists_C3": 3,
    "tangent_and_ramification_orders": {
        "C_infinity_uniformizer_w3_over_v": ord_C_tangent,
        "base_uniformizer_w2_over_v_at_C_infinity": ord_base_tangent,
        "E_ab_y_wv_at_C_zero": ord_C_zero_map,
        "D_infinity_uniformizer_t2_over_z": ord_D_tangent,
        "hyperelliptic_tangent_derivative": -1,
    },
    "integral_twist_rule": "c_base^(n*kappa_l)=c_cover^(n*kappa_l/3); at l=3 first restrict kappa_l to 3 Z_3.",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
