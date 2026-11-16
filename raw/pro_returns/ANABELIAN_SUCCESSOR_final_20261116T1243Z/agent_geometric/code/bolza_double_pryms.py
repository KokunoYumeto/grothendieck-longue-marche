"""Exploratory exact Prym calculation for y^2=x^5-x in characteristic three.

F9 is F3[i]/(i^2+1); integer a+3b denotes a+bi.  For an etale
double cover corresponding to a pair of the six branch points, the Prym
elliptic curve is the double cover branched at the complementary quartet.
Its Hasse invariant vanishes in characteristic three iff its Legendre
parameter is -1=2.  This script examines all fifteen pairs, then all
rank-three subspaces of J[2].  It does not exhaust other covers.
"""
import itertools
import json


def add(x, y):
    return (x % 3 + y % 3) % 3 + 3*((x // 3 + y // 3) % 3)


def neg(x):
    return (-(x % 3)) % 3 + 3*((-(x // 3)) % 3)


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    a, b, c, d = x % 3, x // 3, y % 3, y // 3
    return (a*c+2*b*d) % 3 + 3*((a*d+b*c) % 3)


def inv(x):
    assert x != 0
    return next(y for y in range(1, 9) if mul(x, y) == 1)


def quotient(x, y):
    return mul(x, inv(y))


# All fifteen nonzero J[2] classes are even subsets of six branch points,
# modulo complementary subsets.  Use the representative omitting bit5.
def pair_vector(pair):
    vector = sum(1 << i for i in pair)
    return vector if vector < 32 else vector ^ 63


points = [None, 0, 1, 2, 3, 6]
records = []
supersingular_vectors = set()
for pair in itertools.combinations(range(6), 2):
    quartet = [points[i] for i in range(6) if i not in pair]
    if None in quartet:
        a, b, c = [x for x in quartet if x is not None]
        lam = quotient(sub(c, a), sub(b, a))
    else:
        a, b, c, d = quartet
        lam = quotient(mul(sub(c, a), sub(d, b)),
                       mul(sub(c, b), sub(d, a)))
    is_ss = lam == 2
    if is_ss:
        supersingular_vectors.add(pair_vector(pair))
    records.append({"pair_indices": pair,
                    "complementary_quartet": quartet,
                    "legendre_parameter": lam,
                    "prym_supersingular": is_ss})

even_vectors = [x for x in range(1, 32) if x.bit_count() % 2 == 0]
all_rank_three = set()
successful_rank_three = set()
for basis in itertools.combinations(even_vectors, 3):
    span = {0}
    for b in basis:
        span |= {x ^ b for x in span.copy()}
    if len(span) == 8:
        canonical = tuple(sorted(span))
        all_rank_three.add(canonical)
        if span-{0} <= supersingular_vectors:
            successful_rank_three.add(canonical)

assert len(records) == 15
assert supersingular_vectors == {3, 12, 15}
assert len(all_rank_three) == 15
assert not successful_rank_three
print(json.dumps({
    "field": "F3[i]/(i^2+1), a+3b denotes a+bi",
    "curve": "y^2=x^5-x",
    "branch_points": points,
    "double_cover_pryms": records,
    "supersingular_two_torsion_vectors": sorted(supersingular_vectors),
    "rank_three_subspaces_checked": len(all_rank_three),
    "rank_three_subspaces_with_all_seven_pryms_supersingular":
        sorted(successful_rank_three),
    "scope": "Only elementary abelian two-covers of this specified curve",
    "assertions": "all passed"
}, indent=2))
