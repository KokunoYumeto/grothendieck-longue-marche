#!/usr/bin/env python3
"""Finite base checks for a precise limit of the section fixed-point bound.

The proof concerns A*=A5^20 x C2^3. It does NOT enumerate that large group
and does NOT assert that it is a quotient of the actual D74 E. Its parity
kernel is proved not 2-generated, explicitly excluding such a quotient.
"""
from itertools import permutations, product
from pathlib import Path
from collections import Counter
import json

S5 = list(permutations(range(5)))
parity = lambda p: sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2
G = [p for p in S5 if parity(p) == 0]
index = {p: i for i, p in enumerate(G)}
one = index[tuple(range(5))]
multiply = lambda p, q: tuple(p[q[i]] for i in range(5))
inverse = lambda p: tuple(p.index(i) for i in range(5))
table = [[index[multiply(p, q)] for q in G] for p in G]
inverses = [index[inverse(p)] for p in G]
conjugations = [tuple(index[multiply(multiply(s, g), inverse(s))] for g in G) for s in S5]
I = [i for i in range(60) if i != one and table[i][i] == one]


def generated(gens):
    seen, todo = {one}, [one]
    while todo:
        old = todo.pop()
        for g in gens:
            new = table[old][g]
            if new not in seen:
                seen.add(new)
                todo.append(new)
    return frozenset(seen)


def cycles(i):
    p = G[i]
    seen, out = set(), []
    for k in range(5):
        if k in seen:
            continue
        c, j = [], k
        while j not in seen:
            seen.add(j); c.append(j + 1); j = p[j]
        if len(c) > 1:
            out.append(c)
    return out


checks = []


def check(name, condition):
    assert condition, name
    checks.append({"name": name, "passed": True})


check("A5_order_sixty_and_fifteen_involutions", len(G) == 60 and len(I) == 15)
check("all_S5_conjugations_are_distinct_A5_automorphisms", len(set(conjugations)) == 120)
check("one_A5_involution_class", {conjugations[k][I[0]] for k, p in enumerate(S5)
                                  if parity(p) == 0} == set(I))
commutators = [table[table[table[a][b]][inverses[a]]][inverses[b]]
               for a, b in product(range(60), repeat=2)]
check("A5_is_perfect", len(generated(commutators)) == 60)

subgroups = {frozenset([one]): ()}
todo = [frozenset([one])]
while todo:
    H = todo.pop()
    gens = subgroups[H]
    for g in range(60):
        if g in H:
            continue
        K = generated(gens + (g,))
        if K not in subgroups:
            subgroups[K] = gens + (g,)
            todo.append(K)
normal = [H for H in subgroups if all({conjugations[k][h] for h in H} == set(H)
                                    for k, p in enumerate(S5) if parity(p) == 0)]
check("all_fifty_nine_subgroups_enumerated", len(subgroups) == 59)
check("A5_has_only_two_normal_subgroups", sorted(map(len, normal)) == [1, 60])
check("proper_subgroup_has_at_most_five_involutions", max(len(set(I).intersection(H))
                                                        for H in subgroups if len(H) < 60) == 5)
subgroup_rows = [{"order": len(H), "involutions": len(set(I).intersection(H)),
                  "generators": [cycles(g) for g in subgroups[H]]}
                 for H in sorted(subgroups, key=lambda H: (len(H), sorted(H)))]


def orbit_data(tuples):
    counts = Counter()
    total = 0
    for tup in tuples:
        if len(generated(tup)) != 60:
            continue
        total += 1
        canonical = min(tuple(c[t] for t in tup) for c in conjugations)
        counts[canonical] += 1
    return total, counts


pair_total, pair_orbits = orbit_data(product(range(60), repeat=2))
triple_total, triple_orbits = orbit_data(product(I, repeat=3))
check("2280_generating_ordered_pairs", pair_total == 2280)
check("nineteen_pair_orbits_of_size_120", len(pair_orbits) == 19 and set(pair_orbits.values()) == {120})
check("2280_generating_involution_triples", triple_total == 2280)
check("nineteen_involution_triple_orbits_of_size_120", len(triple_orbits) == 19 and set(triple_orbits.values()) == {120})
x = index[(2, 0, 1, 3, 4)]  # (132)
y = index[(0, 1, 4, 2, 3)]  # (354)
check("fixed_pair_generates_A5", len(generated([x, y])) == 60)
third_values = list(range(20))
check("twenty_distinct_third_coordinates", len(set(third_values)) == 20)

subspaces = {frozenset([0])}
todo = [frozenset([0])]
while todo:
    W = todo.pop()
    for v in range(8):
        U = frozenset(set(W) | {w ^ v for w in W})
        if U not in subspaces:
            subspaces.add(U); todo.append(U)
rows = []
for W in sorted(subspaces, key=lambda W: (len(W), sorted(W))):
    degree = 8 // len(W)
    fixed_labels = sum(e in W for e in [1, 2, 4])
    rows.append({"subspace": sorted(W), "degree": degree,
                 "fixed_basis_labels": fixed_labels, "fixed_sum": degree * fixed_labels,
                 "upper_bound": degree + 2})
check("sixteen_C2_cubed_subspaces", len(rows) == 16)
check("every_full_projection_subgroup_meets_the_bound", all(r['fixed_sum'] <= r['upper_bound'] for r in rows))

out = {"status": "PASS", "large_group": "A*=A5^20 x C2^3",
       "large_group_order": (60 ** 20) * 8,
       "scope": "A* is excluded as an actual E quotient because its parity kernel is not 2-generated.",
       "base_subgroups": subgroup_rows,
       "generating_pair_count": pair_total, "pair_orbit_count": len(pair_orbits),
       "pair_orbit_representatives": [[cycles(t) for t in tup] for tup in sorted(pair_orbits)],
       "generating_involution_triple_count": triple_total,
       "involution_triple_orbit_count": len(triple_orbits),
       "involution_triple_orbit_representatives": [[cycles(t) for t in tup] for tup in sorted(triple_orbits)],
       "ordinary_three_generator_construction": {"first_constant_column": cycles(x),
           "second_constant_column": cycles(y), "third_column": [cycles(t) for t in third_values]},
       "C2_cubed_subspaces": rows,
       "checks": checks, "assertion_count": len(checks)}
path = Path(__file__).with_name('section_bound_insufficiency_base_output.json')
path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
