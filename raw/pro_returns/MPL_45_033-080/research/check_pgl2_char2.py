"""Independent finite check of the PGL_2 characteristic-two H^1 example.

Uses 2x2 matrices modulo scalar matrices over F_2, not the derived bracket
formula, to enumerate all 512 linear endomorphisms of the 3-dimensional Lie
algebra. The symbolic proof over every characteristic-two field is in the
companion memo. No input transcription files are changed.
"""

from itertools import product
import json
from pathlib import Path

VECTORS = tuple(product(range(2), repeat=3))
ZERO = (0, 0, 0)
H, X, Y = (1, 0, 0), (0, 1, 0), (0, 0, 1)
BASIS = (H, X, Y)


def add(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def matrix(v):
    a, b, c = v
    return ((a, b), (c, 0))


def matrix_product(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % 2
                       for j in range(2)) for i in range(2))


def bracket(u, v):
    uv = matrix_product(matrix(u), matrix(v))
    vu = matrix_product(matrix(v), matrix(u))
    comm = tuple(tuple(uv[i][j] ^ vu[i][j] for j in range(2))
                 for i in range(2))
    # Subtract the lower diagonal entry times I to choose the representative.
    return (comm[0][0] ^ comm[1][1], comm[0][1], comm[1][0])


def apply(columns, v):
    result = ZERO
    for coefficient, column in zip(v, columns):
        if coefficient:
            result = add(result, column)
    return result


def is_derivation(columns):
    checks = [apply(columns, bracket(u, v)) ==
              add(bracket(apply(columns, u), v),
                  bracket(u, apply(columns, v)))
              for u, v in product(VECTORS, repeat=2)]
    return all(checks)


def flat(columns):
    return tuple(a for column in columns for a in column)


def rank(rows):
    rows = [list(r) for r in rows]
    pivots = 0
    for column in range(len(rows[0]) if rows else 0):
        pivot = next((r for r in range(pivots, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[pivots], rows[pivot] = rows[pivot], rows[pivots]
        for r in range(len(rows)):
            if r != pivots and rows[r][column]:
                rows[r] = [a ^ b for a, b in zip(rows[r], rows[pivots])]
        pivots += 1
    return pivots


assert bracket(H, X) == X
assert bracket(H, Y) == Y
assert bracket(X, Y) == ZERO
assert all(bracket(v, v) == ZERO for v in VECTORS)
assert all(add(add(bracket(u, bracket(v, w)), bracket(v, bracket(w, u))),
               bracket(w, bracket(u, v))) == ZERO
           for u, v, w in product(VECTORS, repeat=3))

endomorphisms = tuple(product(VECTORS, repeat=3))
derivations = tuple(m for m in endomorphisms if is_derivation(m))
inners = tuple(tuple(bracket(v, b) for b in BASIS) for v in VECTORS)
assert len(set(inners)) == 8
assert set(inners) <= set(derivations)

D = (ZERO, X, ZERO)
assert is_derivation(D) and D not in inners
der_rank = rank([flat(d) for d in derivations])
inner_rank = rank([flat(d) for d in inners])
assert (len(derivations), der_rank, inner_rank) == (64, 6, 3)

# Three representatives for End(span(x,y))/k*Id, in columns h,x,y.
outer_representatives = (D, (ZERO, ZERO, X), (ZERO, Y, ZERO))
assert all(is_derivation(d) for d in outer_representatives)
assert rank([flat(d) for d in inners + outer_representatives]) == 6

result = {
    "field": "F_2",
    "basis": ["h=diag(1,0) mod kI", "x=E12 mod kI", "y=E21 mod kI"],
    "bracket_implementation": "matrix commutator, reduced modulo scalar matrices",
    "brackets": {"[h,x]": "x", "[h,y]": "y", "[x,y]": "0"},
    "alternating_checks": 8,
    "jacobi_checks": 512,
    "endomorphisms_enumerated": len(endomorphisms),
    "derivation_identity_checks_per_endomorphism": 64,
    "derivations_count": len(derivations),
    "derivations_dimension": der_rank,
    "inner_derivations_count": len(set(inners)),
    "inner_derivations_dimension": inner_rank,
    "ordinary_H1_dimension": der_rank - inner_rank,
    "D_images": {"h": "0", "x": "x", "y": "0"},
    "D_is_derivation": is_derivation(D),
    "D_is_inner": D in inners,
    "all_assertions_passed": True,
}
output_path = Path(__file__).with_name("check_pgl2_char2_result.json")
output_path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
