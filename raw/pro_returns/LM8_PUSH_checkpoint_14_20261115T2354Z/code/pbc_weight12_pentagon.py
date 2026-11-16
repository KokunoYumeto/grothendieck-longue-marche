"""Selected exact pentagon coefficient rows in degree twelve.

The backward derivation algorithm contracts one adjacent output pair at
a time.  It computes a coefficient without constructing all degree-13
polynomials.  Discovery is modular; every retained row is then recomputed
over the integers before the asserted linear relation is checked.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
from math import lcm
import hashlib
import json
import random
import time
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
started = time.monotonic()
PRIME = 65521

def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for w, c in p.items():
            out[w] += c
    return {w: c for w, c in out.items() if c}

def scale(p, a):
    return {w: c*a for w, c in p.items() if c*a}

def bracket(p, q):
    out = defaultdict(int)
    for u, a in p.items():
        for v, b in q.items():
            out[u+v] += a*b
            out[v+u] -= a*b
    return {w: c for w, c in out.items() if c}

def lyndon(w):
    return all(w < w[i:] for i in range(1, len(w)))

@lru_cache(None)
def standard(w):
    if len(w) == 1:
        return {w: 1}
    for i in range(1, len(w)):
        if lyndon(w[i:]):
            return bracket(standard(w[:i]), standard(w[i:]))
    raise AssertionError(w)

letters = "abc"
def edge(i, j):
    d = [{}, {}, {}]
    d[i] = bracket({letters[i]: 1}, {letters[j]: 1})
    d[j] = scale(d[i], -1)
    return tuple(d)

def inner(letter):
    return tuple(bracket({letter: 1}, {t: 1}) for t in letters)

def dadd(*ds):
    return tuple(add(*(d[i] for d in ds)) for i in range(3))

t12, t13, t23 = edge(0, 1), edge(0, 2), edge(1, 2)
t14, t24, t34 = inner("a"), inner("b"), inner("c")
pairs = [
    (1, t12, t23),
    (1, dadd(t12, t13), dadd(t24, t34)),
    (1, t23, t34),
    (-1, t12, dadd(t23, t24)),
    (-1, dadd(t13, t23), t34),
]

def operator_coefficient_vector(word, base, dx, dy, modulus):
    contractions = {}
    for a, b in product(letters, repeat=2):
        pair = a+b
        contractions[pair] = [
            (letter, dx[i].get(pair, 0), dy[i].get(pair, 0))
            for i, letter in enumerate(letters)
            if dx[i].get(pair, 0) or dy[i].get(pair, 0)
        ]
    dtype = np.int64 if modulus else object

    @lru_cache(None)
    def rec(w):
        if len(w) == 1:
            return np.array([int(w == base)], dtype=dtype)
        half = 1 << (len(w)-2)
        out = np.zeros(2*half, dtype=dtype)
        for i in range(len(w)-1):
            for letter, cx, cy in contractions[w[i:i+2]]:
                v = rec(w[:i]+letter+w[i+2:])
                if cx:
                    out[:half] += cx*v
                if cy:
                    out[half:] += cy*v
        if modulus:
            out %= modulus
        return out
    value = rec(word)
    return value

def coefficient_row(word, base, associative_basis, modulus):
    length = len(word)-1
    dtype = np.int64 if modulus else object
    operator = np.zeros(1 << length, dtype=dtype)
    for sign, dx, dy in pairs:
        operator += sign*operator_coefficient_vector(word, base, dx, dy, modulus)
    if modulus:
        operator %= modulus
        matrix = np.array(associative_basis, dtype=np.int64) % modulus
        # All entries are below 65521 and the dot has at most 4096 terms:
        # this is strictly below signed 64-bit overflow.
        return [int(v) for v in (matrix@operator) % modulus]
    return [int(sum(a*b for a, b in zip(row, operator)))
            for row in associative_basis]

def polynomial_vector(p, n):
    out = [0]*(1 << n)
    for word, c in p.items():
        index = 0
        for letter in word:
            index = 2*index + (letter == "y")
        out[index] = c
    return out

# Validate the independent backward algorithm against the complete,
# previously checked degree-seven defect.
q7_data = json.loads((HERE/"pbc_q7.json").read_text())
q7 = add(*(scale(standard(w), c) for w, c in q7_data["standard_lyndon_terms"]))
q7_vector = polynomial_vector(q7, 7)
validation = []
for base in letters:
    terms = q7_data["full_defect"][base]
    choices = list(terms)[:3] + list(terms)[-3:]
    if base == "a":
        choices += ["aaaaabcb"]
    for word in choices:
        observed = coefficient_row(word, base, [q7_vector], None)[0]
        assert observed == terms.get(word, 0), (base, word, observed, terms.get(word))
        validation.append([base, word, observed])
print("backward_algorithm_validation", len(validation), "coefficients", flush=True)

space_path = HERE/"pbc_gentle_even_fast.json"
space = next(r for r in json.loads(space_path.read_text())["weights"] if r["weight"] == 12)
basis_polynomials = [
    add(*(scale(standard(w), c) for w, c in zip(space["standard_lyndon_words"], row) if c))
    for row in space["integral_basis_coordinates"]
]
associative_basis = [polynomial_vector(p, 12) for p in basis_polynomials]
functional = json.loads((HERE/"pbc_gentle_weight12_integral.json").read_text())[
    "primitive_integral_functional"]

def rank_mod(rows):
    if not rows:
        return 0
    matrix = [[x % PRIME for x in r] for r in rows]
    rank = 0
    for col in range(7):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inv = pow(matrix[rank][col], -1, PRIME)
        matrix[rank] = [x*inv % PRIME for x in matrix[rank]]
        for i in range(rank+1, len(matrix)):
            c = matrix[i][col]
            matrix[i] = [(x-c*y) % PRIME for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
    return rank

rng = random.Random(20261115)
candidates = [("a", "a"*8+"bcbcb"),
              ("a", "a"*8+"bccbb"),
              ("a", "a"*7+"bcbcbc")]
for _ in range(120):
    counts = rng.choice([(9,2,2), (8,3,2), (7,3,3), (6,4,3), (5,4,4)])
    word = list("a"*counts[0]+"b"*counts[1]+"c"*counts[2])
    rng.shuffle(word)
    candidates.append((rng.choice(letters), "".join(word)))
selected = []
rows = []
rank = 0
for number, (base, word) in enumerate(candidates, 1):
    row = coefficient_row(word, base, associative_basis, PRIME)
    new_rank = rank_mod(rows+[row])
    if new_rank > rank:
        selected.append((base, word))
        rows.append(row)
        rank = new_rank
        print("new_row", number, base, word, "rank", rank,
              "seconds", round(time.monotonic()-started, 3), flush=True)
    if rank_mod(rows+[functional]) == rank:
        break
else:
    raise AssertionError("selected rows do not yet detect the functional")

exact_rows = []
for base, word in selected:
    row = coefficient_row(word, base, associative_basis, None)
    exact_rows.append(row)
    print("exact_row", base, word, row, flush=True)
matrix = sp.Matrix(exact_rows)
solution, parameters = matrix.T.gauss_jordan_solve(sp.Matrix(functional))
solution = solution.subs({p: 0 for p in parameters})
assert matrix.T*solution == sp.Matrix(functional)
denominator = lcm(*(int(x.q) for x in solution))
integer_combination = [int(x*denominator) for x in solution]
assert denominator == 698922 and denominator % 13 != 0
assert matrix.T*sp.Matrix(integer_combination) == denominator*sp.Matrix(functional)
result = {
    "scope": "exact linear pentagon coefficient identity on the integral degree12 gentle space",
    "source_space_sha256": hashlib.sha256(space_path.read_bytes()).hexdigest(),
    "degree7_independent_backward_validation": validation,
    "selected_coefficient_labels": selected,
    "exact_coefficient_rows": exact_rows,
    "rational_row_combination": [str(x) for x in solution],
    "integer_row_combination": integer_combination,
    "common_denominator": denominator,
    "denominator_is_13_adic_unit": True,
    "primitive_integral_functional": functional,
    "exact_linear_identity_verified": True,
    "consequence": "every exact linear pentagon solution in this space is killed by the primitive functional",
    "full_GT_comparison_required": True,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({
    "exact_linear_identity_verified": True,
    "coefficient_row_rank": matrix.rank(),
    "rational_row_combination": result["rational_row_combination"],
    "seconds": round(time.monotonic()-started, 3),
}, indent=2))
