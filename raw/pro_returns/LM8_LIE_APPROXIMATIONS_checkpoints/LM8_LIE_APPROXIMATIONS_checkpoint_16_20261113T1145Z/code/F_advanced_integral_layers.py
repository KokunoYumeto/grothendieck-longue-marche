"""Exact arithmetic checks for F.22; only the Python standard library is used.

This certifies the finite arithmetic inputs and explicit torsion cocycle.
Section counts are consequences of F.22's proved Galois cohomology calculation,
not a computational presentation or enumeration of the absolute Galois group.
"""
from fractions import Fraction
from itertools import product
from math import factorial, gcd
from pathlib import Path
import json

OUT = Path(__file__).with_suffix(".json")


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    sign = 1
    ans = Fraction(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        v = a[k][k]
        ans *= v
        for i in range(k + 1, len(a)):
            t = a[i][k] / v
            for j in range(k + 1, len(a)):
                a[i][j] -= t * a[k][j]
            a[i][k] = 0
    ans *= sign
    assert ans.denominator == 1
    return int(ans)


def sylvester(f, g):
    m, n = len(f) - 1, len(g) - 1
    rows = []
    for k in range(n):
        rows.append([0] * k + f + [0] * (n - 1 - k))
    for k in range(m):
        rows.append([0] * k + g + [0] * (m - 1 - k))
    return rows


def order(a, modulus):
    x = 1
    for k in range(1, modulus + 1):
        x = x * a % modulus
        if x == 1:
            return k
    raise AssertionError("order not found")


def bracket(a, b):
    result = {}
    for u, cu in a.items():
        for v, cv in b.items():
            result[u + v] = result.get(u + v, 0) + cu * cv
            result[v + u] = result.get(v + u, 0) - cu * cv
    return {word: coefficient for word, coefficient in result.items()
            if coefficient}


def rank_mod5(rows):
    a = [[x % 5 for x in row] for row in rows]
    k = 0
    for j in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(k, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        inv = pow(a[k][j], -1, 5)
        a[k] = [x * inv % 5 for x in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                t = a[i][j]
                a[i] = [(x - t * y) % 5 for x, y in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k


disc_matrix = sylvester([1, 1, 1, 1, 1], [4, 3, 2, 1])
disc = determinant(disc_matrix)
assert disc == 125
# pi>3 and sqrt(125)<12 imply a strict bound below the following value.
minkowski_upper = Fraction(factorial(4), 4**4) * Fraction(4, 3)**2 * 12
assert minkowski_upper == 2
assert 125 < 12**2
inertia = {str(q): order(q, 5) for q in (2, 3)}
assert set(inertia.values()) == {4}

unit_characters = {0: 3, 1: 1, 2: 1, 3: 0}
brauer_characters = {0: 2, 1: 0, 2: 0, 3: 0}
cohomology_mod5 = []
for j in range(1, 5):
    h1 = sum(m for e, m in unit_characters.items()
             if (e + j - 1) % 4 == 0)
    h2 = sum(m for e, m in brauer_characters.items()
             if (e + j - 1) % 4 == 0)
    unit_matrix = [pow(2, e + j - 1, 5)
                   for e, m in unit_characters.items() for _ in range(m)]
    brauer_matrix = [pow(2, j - 1, 5)] * 2
    assert h1 == sum(t == 1 for t in unit_matrix)
    assert h2 == sum(t == 1 for t in brauer_matrix)
    cohomology_mod5.append(dict(
        weight=j, H1_dimension=h1, H2_dimension=h2,
        twisted_unit_generator_diagonal=unit_matrix,
        twisted_brauer_generator_diagonal=brauer_matrix))
assert [x["H1_dimension"] for x in cohomology_mod5] == [3, 0, 1, 1]
assert [x["H2_dimension"] for x in cohomology_mod5] == [2, 0, 0, 0]

residue_orders = {
    "K4_localization_K3_residues": {str(q): q**2 - 1 for q in (2, 3, 5)},
    "K6_localization_K5_residues": {str(q): q**3 - 1 for q in (2, 3, 5)}
}
assert all(n % 5 for d in residue_orders.values() for n in d.values())

x, y = {(0,): 1}, {(1,): 1}
c = bracket(x, y)
u, v = bracket(x, c), bracket(y, c)
hall = [[x, y], [c], [u, v],
        [bracket(x, u), bracket(y, u), bracket(y, v)]]
assert bracket(y, u) == bracket(x, v)
assert not bracket(c, c)
hall_certificate = []
for weight, basis in enumerate(hall, 1):
    words = list(product((0, 1), repeat=weight))
    rows = [[p.get(w, 0) for w in words] for p in basis]
    rank = rank_mod5(rows)
    assert rank == len(basis)
    hall_certificate.append(dict(
        weight=weight, rank=rank,
        polynomials=[{"".join("xy"[i] for i in word): coefficient
                      for word, coefficient in sorted(p.items())}
                     for p in basis]))
assert [row["rank"] for row in hall_certificate] == [2, 1, 2, 3]

cyclic_cocycle_checks = []
for r in range(1, 7):
    modulus, cover = 5**r, 5**(r + 1)
    length = 4 * 5**r
    assert pow(2, length, cover) == 1
    assert pow(2, length // 2, cover) != 1
    assert pow(2, length // 5, cover) != 1
    u = 1
    norm, action_power = 0, 1
    for j in range(length):
        z = ((u**4 - 1) // 5) % modulus
        next_u = 2 * u % cover
        next_z = ((next_u**4 - 1) // 5) % modulus
        # This verifies the generator recurrence, including the final wrap.
        assert next_z == (z + pow(u, 4, modulus) * 3) % modulus
        norm = (norm + action_power) % modulus
        action_power = action_power * 16 % modulus
        u = next_u
    assert u == 1 and norm == 0 and action_power == 1
    coboundaries = {15 * a % modulus for a in range(modulus)}
    assert len(coboundaries) == modulus // 5
    assert 3 % modulus not in coboundaries
    assert 5 * 3 % modulus in coboundaries
    triples = {tuple(3 * a % 5 for a in t)
               for t in product(range(5), repeat=3)}
    assert len(triples) == 125
    cyclic_cocycle_checks.append(dict(
        r=r, coefficient_modulus=modulus,
        cyclotomic_cover_modulus=cover, group_order=length,
        group_generator=2, action_on_generator=16 % modulus,
        cocycle_generator_value=3 % modulus,
        norm_operator=norm, all_generator_values_are_cocycles=True,
        coboundary_count=len(coboundaries), H1_order=5,
        generator_nonzero=True, three_layer_parameters=125,
        recurrence_checks=length, reduction_of_generator_value=3 % 5))

section_counts = []
for r in range(1, 9):
    section_counts.append(dict(
        r=r, class1=5**(6*r), class2=5**(6*r),
        class3=5**(8*r), class4=5**(8*r+3),
        class2_fibre=1, class3_fibre=5**(2*r), class4_fibre=125))

data = dict(
    statement="F.22",
    status="Proved",
    scope="Actual integral pro-5 arithmetic action over G_Q,{2,3,5}; lower-central classes1-4; no crystalline condition",
    cyclotomic_field=dict(
        polynomial=[1, 1, 1, 1, 1], sylvester_matrix=disc_matrix,
        discriminant=disc, strict_minkowski_upper=2,
        strict_bound_reason="pi>3 and sqrt(125)<12",
        inert_prime_orders=inertia, ramified_prime=5,
        S_prime_count=3, class_number=1),
    mod5_character_multiplicities=dict(
        unit_module=unit_characters, Brauer_module=brauer_characters),
    cohomology_mod5=cohomology_mod5,
    integral_central_cohomology=[
        dict(weight=2, H1="0", H2="0"),
        dict(weight=3, H1="Z5", H2="0"),
        dict(weight=4, H1="Z/5", H2="0",
             torsion_cocycle="(chi(g)^4-1)/5")],
    residue_K_orders=residue_orders,
    Hall_layers=hall_certificate,
    metabelian_quotient_unchanged_through_class=4,
    cyclic_cocycle_checks=cyclic_cocycle_checks,
    finite_section_counts=section_counts,
    count_method="Theorem-derived exact counts, not an enumeration of an absolute Galois group presentation",
    relative_Fermat_image="Exactly the classes with all six abelian Kummer coordinates divisible by5^r",
    all_relative_Fermat_levels="Entire fibre above abelian zero: Z5^2 torsor at class3;125 class4 lifts over every point",
    rationalization="Class3 injective; each class4 fibre over the rationalized image has125 elements",
    qualifications=[
        "Set products require choices of origins; no canonical coordinates are asserted.",
        "The actual Ihara action is retained; only its central graded layers are diagonal.",
        "The relative Fermat kernels are induced from the original tripod quotient.",
        "Unrestricted ramification and class5 or higher are not computed here."])
OUT.write_text(json.dumps(data, indent=2) + "\n")
print(json.dumps(dict(
    statement=data["statement"], status=data["status"],
    discriminant=disc, class_number=1,
    H1_mod5_dimensions=[x["H1_dimension"] for x in cohomology_mod5],
    H2_mod5_dimensions=[x["H2_dimension"] for x in cohomology_mod5],
    integral_H1=["0", "Z5", "Z/5"],
    integral_H2=["0", "0", "0"],
    finite_cocycle_checks=sum(x["recurrence_checks"]
                             for x in cyclic_cocycle_checks),
    finite_class4_fibre=125, output=str(OUT)), indent=2))
