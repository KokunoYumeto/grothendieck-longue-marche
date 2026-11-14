#!/usr/bin/env python3
"""A finite P4 comparison EXCLUDED from the actual D74 quotient family.

This does not construct an actual D74 quotient with deficient generation.
It enumerates the forbidden S5 models and the resulting exact restrictions
on f under one fixed full free-group quotient Fhat(x,y)->A5.
"""
from itertools import permutations, product
from pathlib import Path
import json

n = 5
one = tuple(range(n))
S5 = list(permutations(range(n)))


def mul(p, q):
    return tuple(p[q[i]] for i in range(n))


def inv(p):
    return tuple(p.index(i) for i in range(n))


def conj(p, g):
    return mul(mul(g, p), inv(g))


def parity(p):
    return sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n)) % 2


def generated(gens):
    known, todo = {one}, [one]
    while todo:
        old = todo.pop()
        for g in gens:
            new = mul(old, g)
            if new not in known:
                known.add(new)
                todo.append(new)
    return known


def order(p):
    v, k = p, 1
    while v != one:
        v, k = mul(v, p), k + 1
    return k


def cycles(p):
    seen, out = set(), []
    for i in range(n):
        if i in seen:
            continue
        v, j = [], i
        while j not in seen:
            seen.add(j)
            v.append(j + 1)
            j = p[j]
        if len(v) > 1:
            out.append(v)
    return out


checks = []


def check(name, condition):
    assert condition, name
    checks.append({"name": name, "passed": True})


A5 = {p for p in S5 if parity(p) == 0}
transpositions = [p for p in S5 if sum(p[i] != i for i in range(n)) == 2]
a, b, c, d = [(1, 0, 2, 3, 4), (0, 2, 1, 3, 4),
              (0, 1, 3, 2, 4), (0, 1, 2, 4, 3)]
x, y = mul(b, a), mul(d, c)
z = inv(mul(x, y))
check("S5_has_120_elements_and_ten_transpositions", len(S5) == 120 and len(transpositions) == 10)
check("the_four_path_factors_generate_S5", len(generated([a, b, c, d])) == 120)
check("the_named_orientation_pair_generates_A5", generated([x, y]) == A5)
check("the_original_z_has_order_five", order(z) == 5)
triple_orders = {}
for triple in product(transpositions, repeat=3):
    size = len(generated(triple))
    triple_orders[size] = triple_orders.get(size, 0) + 1
check("all_thousand_section_triples_were_enumerated", sum(triple_orders.values()) == 1000)
check("no_three_transpositions_generate_S5", 120 not in triple_orders)
check("maximum_triple_image_order_is_24", max(triple_orders) == 24)
check("one_transposition_normally_generates_S5", len(generated([conj(a, g) for g in S5])) == 120)
fixed = [sum(t[i] == i for i in range(n)) for t in [a, b, d]]
check("the_actual_section_bound_rejects_this_model", sum(fixed) == 9 and sum(fixed) > n + 2)
inverters = [g for g in S5 if conj(z, g) == inv(z)]
check("all_five_z_inverters_are_even_involutions", len(inverters) == 5 and
      all(parity(g) == 0 and order(g) == 2 for g in inverters))
check("no_odd_z_inverting_involution_exists", not [g for g in inverters if parity(g) == 1])

x_reflections = [g for g in transpositions if conj(x, g) == inv(x)]
y_reflections = [g for g in transpositions if conj(y, g) == inv(y)]
check("three_transposition_reflections_for_each_named_rotation", len(x_reflections) == len(y_reflections) == 3)
forbidden = []
for aa, cc in product(x_reflections, y_reflections):
    bb, dd = mul(x, aa), mul(y, cc)
    ff = mul(cc, aa)
    check("P4_candidate_%d_has_four_transpositions" % len(forbidden),
          all(t in transpositions for t in [aa, bb, cc, dd]))
    check("P4_candidate_%d_has_full_S5_image" % len(forbidden),
          len(generated([aa, bb, cc, dd])) == 120)
    check("P4_candidate_%d_preserves_x_y_alpha_formulas" % len(forbidden),
          conj(x, aa) == inv(x) and
          conj(y, aa) == mul(mul(inv(ff), inv(y)), ff))
    check("P4_candidate_%d_fails_original_z_conjugacy" % len(forbidden),
          not any(conj(inv(z), u) == conj(z, aa) for u in A5))
    forbidden.append({"a": cycles(aa), "b": cycles(bb), "c": cycles(cc),
                      "d": cycles(dd), "forbidden_f": cycles(ff),
                      "forbidden_f_tuple": ff})
check("nine_distinct_forbidden_f_values", len({tuple(row['forbidden_f_tuple']) for row in forbidden}) == 9)
out = {"status": "PASS", "scope": "These P4->S5 maps cannot factor through any actual D74 q4.",
       "fixed_F_to_A5_quotient": {"x": cycles(x), "y": cycles(y), "z": cycles(z)},
       "triple_image_order_histogram": triple_orders,
       "natural_action": {"degree": n, "three_fixed_point_counts": fixed,
                          "sum": sum(fixed), "actual_upper_bound": n + 2},
       "z_inverters": [cycles(g) for g in inverters],
       "forbidden_f_values": forbidden,
       "checks": checks, "assertion_count": len(checks)}
target = Path(__file__).with_name("actual_quotient_section_bound_output.json")
target.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
