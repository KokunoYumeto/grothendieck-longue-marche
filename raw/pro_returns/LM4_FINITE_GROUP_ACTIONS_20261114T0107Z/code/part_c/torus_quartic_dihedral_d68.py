#!/usr/bin/env python3
"""Exact word, cover-module, and dihedral quotient checks for D.68.

The primary matrix models verify identities used by the proof. They
do not assert that a chosen primary model is realized by a full action.
"""
from collections import Counter
from math import isqrt
from pathlib import Path
import json


COUNTS = Counter()


def check(category, condition):
    assert condition, category
    COUNTS[category] += 1


def word(*parts):
    out = []
    for part in parts:
        for letter in part:
            if out and out[-1] == -letter:
                out.pop()
            else:
                out.append(letter)
    return tuple(out)


def inverse(w):
    return tuple(-a for a in reversed(w))


def substitute(w, images):
    return word(*(images[a] if a > 0 else inverse(images[-a])
                  for a in w))


def comm(a, b):
    return word(a, b, inverse(a), inverse(b))


def mm(a, b, modulus=None):
    out = [[sum(x*y for x, y in zip(row, col))
            for col in zip(*b)] for row in a]
    return out if modulus is None else [[x % modulus for x in row] for row in out]


def ma(*matrices):
    return [[sum(a[i][j] for a in matrices)
             for j in range(len(matrices[0][0]))]
            for i in range(len(matrices[0]))]


def scale(k, a):
    return [[k*x for x in row] for row in a]


def reduced_matrix(a, n):
    return [[x % n for x in row] for row in a]


def norm4(a, n=None):
    identity = [[int(i == j) for j in range(len(a))]
                for i in range(len(a))]
    a2 = mm(a, a, n)
    result = ma(identity, a, a2, mm(a2, a, n))
    return result if n is None else reduced_matrix(result, n)


ID = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
J = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
MINUS_J = scale(-1, J)
I_MINUS_J = ma(ID, MINUS_J)
INCLUSION = [[2, 0, 0], [0, 1, 1]]
ELL = [[0, 1, -1]]
BOUNDARY = [[0], [-1], [1]]
ZERO3 = [[0]*3 for _ in range(3)]


def schreier(w):
    """Exact transversal 1,x rewriting for ker(x->1,y->0)."""
    state, out = 0, ()
    for letter in w:
        if letter == 1:
            contribution = () if state == 0 else (1,)
            state ^= 1
        elif letter == -1:
            contribution = (-1,) if state == 0 else ()
            state ^= 1
        else:
            generator = 2 if state == 0 else 3
            contribution = (generator if letter > 0 else -generator,)
        out = word(out, contribution)
    assert state == 0
    return out


def abelian_columns(words, rank=3):
    columns = [[w.count(i)-w.count(-i) for i in range(1, rank+1)]
               for w in words]
    return [list(row) for row in zip(*columns)]


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def main():
    x, y = (1,), (2,)
    cusp = comm(x, y)
    basis_rows = [
        ((1, 0), {1: x, 2: y}, {1: x, 2: y}),
        ((0, 1), {1: (1, 2, -1), 2: (-1,)},
         {1: (-2,), 2: (2, 1, -2)}),
        ((1, 1), {1: x, 2: (2, -1)},
         {1: x, 2: (2, 1)})
    ]
    for chi, forward, backward in basis_rows:
        for generator in (1, 2):
            check("basis_inverse_words", substitute(forward[generator], backward)
                  == (generator,))
            check("basis_inverse_words", substitute(backward[generator], forward)
                  == (generator,))
        check("cusp_basis_words", comm(forward[1], forward[2]) == cusp)
        for generator, expected in ((1, 1), (2, 0)):
            value = sum(chi[abs(letter)-1] for letter in forward[generator]) % 2
            check("basis_character_labels", value == expected)

    n_images = {1: (1, 1), 2: y, 3: (1, 2, -1)}
    check("cover_words", schreier(cusp) == (3, -2))
    expected_deck = {1: (1,), 2: (3,), 3: (1, 2, -1)}
    for generator in (1, 2, 3):
        actual = word(x, n_images[generator], inverse(x))
        rewritten = schreier(actual)
        check("cover_words", rewritten == expected_deck[generator])
        check("cover_words", substitute(rewritten, n_images) == actual)
    check("cover_words", schreier((1, 2, 1, 2)) == (3, 1, 2))

    # The actual geometric quarter-turn, in the third adapted basis.
    alpha = {1: (2, 1), 2: (-1, -1, -2)}
    for generator in (1, 2):
        iterate = (generator,)
        for _ in range(4):
            iterate = substitute(iterate, alpha)
        check("geometric_words", iterate == (generator,))
    check("geometric_words", word(x, substitute(cusp, alpha), inverse(x)) == cusp)
    orbit = [x]
    for _ in range(3):
        orbit.append(substitute(orbit[-1], alpha))
    check("geometric_words", word(*orbit) == cusp)
    s_words = [schreier(substitute(n_images[i], alpha)) for i in (1, 2, 3)]
    t_words = [schreier(word(x, substitute(n_images[i], alpha), inverse(x)))
               for i in (1, 2, 3)]
    expected_s = [[1, -1, -1], [1, -1, 0], [1, 0, -1]]
    expected_t = [[1, -1, -1], [1, 0, -1], [1, -1, 0]]
    check("geometric_matrices", abelian_columns(s_words) == expected_s)
    check("geometric_matrices", abelian_columns(t_words) == expected_t)
    for original, rewritten in zip(
            [substitute(n_images[i], alpha) for i in (1, 2, 3)], s_words):
        check("geometric_words", substitute(rewritten, n_images) == original)

    integral_models = 0
    for aa in range(-15, 16, 2):
        for bb in (-1, 1):
            cc = -(aa*aa+1)//(2*bb)
            dd, ee = (1-aa)//2, (-1-aa)//2
            handle = [[aa, 2*bb], [cc, -aa]]
            tt = [[aa, bb, bb], [cc, dd, ee], [cc, ee, dd]]
            ss = mm(J, tt)
            check("integral_matrix_identities", mm(handle, handle) == [[-1, 0], [0, -1]])
            check("integral_matrix_identities", mm(J, tt) == mm(tt, J))
            check("integral_matrix_identities", mm(tt, tt) == MINUS_J)
            check("integral_matrix_identities", mm(ss, ss) == MINUS_J)
            check("integral_matrix_identities", mm(INCLUSION, tt) == mm(handle, INCLUSION))
            check("integral_matrix_identities", mm(tt, BOUNDARY) == BOUNDARY)
            check("integral_matrix_identities", mm(ss, BOUNDARY) == scale(-1, BOUNDARY))
            check("integral_matrix_identities", norm4(tt) == scale(2, I_MINUS_J))
            check("integral_matrix_identities", norm4(ss) == ZERO3)
            check("integral_matrix_identities", mm(ELL, ss) == scale(-1, ELL))
            check("dyadic_unit_obstruction", reduced_matrix(norm4(tt), 2) == ZERO3)
            check("dyadic_unit_obstruction", reduced_matrix(BOUNDARY, 2) != [[0], [0], [0]])
            check("dyadic_character", reduced_matrix(handle, 2) == [[1, 0], [1, 1]])
            integral_models += 1

    scalar_models = []
    for q in range(5, 98):
        if not prime(q) or q % 4 != 1:
            continue
        half = pow(2, -1, q)
        for u in range(q):
            if u*u % q != q-1:
                continue
            dd, ee = (u-1)*half % q, (u+1)*half % q
            tt = [[u, 0, 0], [0, dd, ee], [0, ee, dd]]
            ss = mm(J, tt, q)
            for name, lhs, rhs in [
                    ("scalar_matrix_identities", mm(tt, tt, q), reduced_matrix(MINUS_J, q)),
                    ("scalar_matrix_identities", mm(ss, ss, q), reduced_matrix(MINUS_J, q)),
                    ("scalar_matrix_identities", mm(ELL, ss, q), reduced_matrix(ELL, q)),
                    ("scalar_matrix_identities", norm4(tt, q), ZERO3),
                    ("scalar_matrix_identities", norm4(ss, q), reduced_matrix(scale(2, I_MINUS_J), q)),
                    ("scalar_matrix_identities", mm(INCLUSION, tt, q),
                     mm([[u, 0], [0, u]], INCLUSION, q))]:
                check(name, lhs == rhs)
            scalar_models.append({"q": q, "u": u})

    dihedral_models = 0
    for modulus in [4, 8, 16, 32]+[q for q in range(3, 98) if prime(q)]:
        dyadic = modulus & (modulus-1) == 0
        choices = [(1, j) for j in range(modulus) if not dyadic or j % 2]
        if not dyadic:
            choices.append((-1, 0))
        for multiplier, shift in choices:
            def mul(a, b):
                return ((a[0]+(-1 if a[1] else 1)*b[0]) % modulus,
                        (a[1]+b[1]) % 2)

            def act(a):
                return ((-multiplier*a[0]+a[1]*shift) % modulus, a[1])

            def epow_action(a, k):
                for _ in range(k):
                    a = act(a)
                return a

            def emul(a, b):
                qpart = mul(a[:2], epow_action(b[:2], a[2]))
                return (qpart[0], qpart[1], (a[2]+b[2]) % 4)

            rr, reflection = (1, 0), (0, 1)
            check("finite_dihedral_relators", mul(act(reflection), act(reflection)) == (0, 0))
            check("finite_dihedral_relators", mul(mul(act(reflection), act(rr)), act(reflection))
                  == ((multiplier % modulus), 0))
            check("finite_dihedral_relators", (1-multiplier)*shift % modulus == 0)
            for exponent in range(modulus):
                for parity in (0, 1):
                    element = (exponent, parity)
                    check("finite_dihedral_square", act(act(element)) == element)
                    if multiplier == -1:
                        check("negative_coordinate_identity", act(element) == element)
            for mm_value in (0, 1, modulus-1):
                vv = (mm_value, 1, 1)
                square = emul(vv, vv)
                fourth = emul(square, square)
                kappa = shift-(1+multiplier)*mm_value
                check("finite_cusp_root_formula", square ==
                      (((1+multiplier)*mm_value-shift) % modulus, 0, 2))
                check("finite_cusp_root_formula", fourth == ((-2*kappa) % modulus, 0, 0))
                if dyadic:
                    check("finite_cusp_root_unit", kappa % 2 == 1)
            dihedral_models += 1

    result = {
        "claim": "D.68", "status": "PASS",
        "integral_double_cover_models": integral_models,
        "scalar_primary_models": scalar_models,
        "finite_dihedral_models": dihedral_models,
        "checks": dict(COUNTS), "total_checks": sum(COUNTS.values()),
        "standard_quartic_cover_words": {"S": s_words, "T": t_words},
        "standard_quartic_cover_matrices": {"S": expected_s, "T": expected_t},
        "scope": "Exact algebraic identities and finite-coordinate consequences. No scalar full-action realization or full section-generation assertion."
    }
    destination = Path(__file__).with_name("torus_quartic_dihedral_d68_output.json")
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                     ("claim", "status", "integral_double_cover_models",
                      "finite_dihedral_models", "checks", "total_checks", "scope")}, indent=2))


if __name__ == "__main__":
    main()
