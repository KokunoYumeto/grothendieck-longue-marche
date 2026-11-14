#!/usr/bin/env python3
"""Exact finite pants-diagram comparison over GL(3,F2).

No map from the actual D74 E to the displayed finite group is constructed.
The large group G^8 x C2^3 is handled by the accompanying coordinate-map
proof; this script enumerates G, its subgroups, automorphisms, tuples and
all eight coordinate peripheral diagrams completely.
"""
from itertools import product
from collections import Counter
from pathlib import Path
from math import gcd
import json

permutations = []
for rows in product(range(8), repeat=3):
    perm = tuple(sum(((rows[i] & v).bit_count() % 2) << i for i in range(3)) - 1
                 for v in range(1, 8))
    if set(perm) == set(range(7)):
        permutations.append(perm)
G = sorted(set(permutations))
index = {g: i for i, g in enumerate(G)}
one = index[tuple(range(7))]
mul_perm = lambda p, q: tuple(p[q[i]] for i in range(7))
T = [[index[mul_perm(p, q)] for q in G] for p in G]
inv = [index[tuple(p.index(i) for i in range(7))] for p in G]
conj = lambda g, h: T[T[h][g]][inv[h]]


def generated(gens):
    seen, todo = {one}, [one]
    while todo:
        old = todo.pop()
        for g in gens:
            new = T[old][g]
            if new not in seen:
                seen.add(new); todo.append(new)
    return frozenset(seen)


def power(g, exponent):
    value = one
    while exponent:
        if exponent & 1:
            value = T[value][g]
        g = T[g][g]
        exponent >>= 1
    return value


def order(g):
    value, n = g, 1
    while value != one:
        value = T[value][g]; n += 1
    return n


def cycles(g):
    seen, out = set(), []
    for i in range(7):
        if i in seen:
            continue
        v, j = [], i
        while j not in seen:
            seen.add(j); v.append(j + 1); j = G[g][j]
        if len(v) > 1:
            out.append(v)
    return out


checks = []


def check(name, condition):
    assert condition, name
    checks.append({"name": name, "passed": True})


orders = [order(g) for g in range(len(G))]
I = [g for g in range(len(G)) if orders[g] == 2]
check("GL3_F2_order168", len(G) == 168)
check("twenty_one_involutions_in_one_inner_class", len(I) == 21 and
      {conj(I[0], g) for g in range(168)} == set(I))
check("exact_element_orders", dict(Counter(orders)) == {1: 1, 2: 21, 3: 56, 4: 42, 7: 48})

subgroups = {frozenset([one]): ()}
todo = list(subgroups)
while todo:
    H = todo.pop()
    for g in range(168):
        if g not in H:
            gens = subgroups[H] + (g,)
            J = generated(gens)
            if J not in subgroups:
                subgroups[J] = gens; todo.append(J)
normal = [H for H in subgroups if all({conj(h, g) for h in H} == set(H)
                                    for g in range(168))]
check("179_subgroups_enumerated", len(subgroups) == 179)
check("group_is_simple", sorted(map(len, normal)) == [1, 168])
derived_lengths = []
for H in subgroups:
    if len(H) == 168:
        continue
    D, length = H, 0
    while len(D) > 1:
        new = generated([T[T[T[a][b]][inv[a]]][inv[b]] for a, b in product(D, repeat=2)])
        assert new != D, "proper subgroup has a nontrivial perfect derived term"
        D, length = new, length + 1
    derived_lengths.append(length)
check("every_proper_subgroup_is_soluble_of_length_at_most_three", max(derived_lengths) == 3)
commutators = [T[T[T[a][b]][inv[a]]][inv[b]] for a, b in product(range(168), repeat=2)]
check("group_is_perfect", len(generated(commutators)) == 168)
check("proper_subgroups_have_at_most_nine_involutions", max(len(set(I).intersection(H))
                                                         for H in subgroups if len(H) < 168) == 9)

pairs = [pair for pair in product(range(168), repeat=2) if len(generated(pair)) == 168]
base = pairs[0]
seen, todo, tree = {one}, [one], []
while todo:
    old = todo.pop(0)
    for j, g in enumerate(base):
        new = T[old][g]
        if new not in seen:
            seen.add(new); todo.append(new); tree.append((new, old, j))
automorphisms, automorphism_images = [], []
for pair in pairs:
    mapping = [None] * 168
    mapping[one] = one
    for new, old, j in tree:
        mapping[new] = T[mapping[old]][pair[j]]
    if all(mapping[T[g][base[j]]] == T[mapping[g]][pair[j]]
           for g in range(168) for j in [0, 1]):
        assert len(set(mapping)) == 168
        automorphisms.append(tuple(mapping)); automorphism_images.append(pair)
check("complete_automorphism_enumeration_has336_maps", len(automorphisms) == 336)


def canonical(tup):
    return min(tuple(a[g] for g in tup) for a in automorphisms)


pair_orbits = Counter(canonical(pair) for pair in pairs)
triples = [triple for triple in product(I, repeat=3) if len(generated(triple)) == 168]
triple_orbits = Counter(canonical(triple) for triple in triples)
strong = {T[a][b] for a, b in product(I, repeat=2)}
filtered = [pair for pair in pairs if pair[0] in strong and pair[1] in strong
            and T[pair[0]][pair[1]] in strong]
filtered_orbits = Counter(canonical(pair) for pair in filtered)
check("19152_generating_pairs_in57_orbits", len(pairs) == 19152 and len(pair_orbits) == 57
      and set(pair_orbits.values()) == {336})
check("2352_generating_involution_triples_in7_orbits", len(triples) == 2352 and
      len(triple_orbits) == 7 and set(triple_orbits.values()) == {336})
check("3696_three_cusp_strongly_real_pairs_in11_orbits", len(filtered) == 3696 and
      len(filtered_orbits) == 11 and set(filtered_orbits.values()) == {336})

selected = sorted(filtered_orbits)[:8]
check("eight_pair_orbits_are_distinct", len(selected) == 8 and len({canonical(p) for p in selected}) == 8)
unit_residues = [m for m in range(168) if gcd(m, 168) == 1]
coordinate_rows = []
for j, (x, y) in enumerate(selected):
    z = inv[T[x][y]]
    a = next(a for a in I if T[x][a] in I)
    b = T[x][a]
    c = next(c for c in I if T[y][c] in I)
    d = T[y][c]
    f = T[c][a]
    h = next(h for h in range(168) if conj(c, h) == a)
    Y = conj(y, h)
    t2 = T[Y][a]
    r = next(r for r in I if T[z][r] in I)
    zr = T[z][r]
    u1 = next(u for u in range(168) if conj(b, u) == r)
    u2 = next(u for u in range(168) if conj(t2, u) == zr)
    check("coordinate%d_four_involutions" % j, all(t in I for t in [a, b, c, d]))
    check("coordinate%d_orientation_pair" % j, T[b][a] == x and T[d][c] == y
          and len(generated([x, y])) == 168)
    check("coordinate%d_alpha_formulas" % j, conj(x, a) == inv[x] and
          conj(y, a) == T[T[inv[f]][inv[y]]][f])
    check("coordinate%d_actual_coboundary_identity" % j,
          f == T[inv[h]][conj(h, a)] and conj(f, a) == inv[f])
    check("coordinate%d_distinguished_section" % j, t2 == conj(d, h) and t2 in I)
    check("coordinate%d_original_boundary_and_z_reflection" % j,
          T[T[x][y]][z] == one and conj(z, r) == inv[z] and zr in I)
    check("coordinate%d_original_endpoint_transporters" % j,
          conj(b, u1) == r and conj(t2, u2) == zr)
    vz = T[r][a]
    check("coordinate%d_original_z_conjugator_identity" % j,
          T[vz][conj(vz, a)] == one and
          T[T[T[inv[f]][y]][f]][x] == conj(T[x][y], inv[vz]))
    admissible = []
    for m in unit_residues:
        lhs = T[power(x, m)][conj(power(y, m), h)]
        rhs = power(T[x][y], m)
        us = [u for u in range(168) if conj(rhs, u) == lhs]
        if us:
            admissible.append(m)
    lhs5 = T[power(x, 5)][conj(power(y, 5), h)]
    rhs5 = power(T[x][y], 5)
    u5 = next(u for u in range(168) if conj(rhs5, u) == lhs5)
    check("coordinate%d_exact_original_cusp_equation_at_unit_residue5" % j,
          conj(rhs5, u5) == lhs5)
    boundary_pair5 = (power(x, 5), conj(power(y, 5), h))
    values = {"x": x, "y": y, "z": z, "a": a, "b": b, "c": c, "d": d,
              "f": f, "h": h, "Y": Y, "t2": t2, "r_z": r, "z_r_z": zr,
              "u1": u1, "u2": u2, "v_z": vz, "boundary_u_at5": u5}
    coordinate_rows.append({"coordinate": j, "indices": values,
        "cycles": {name: cycles(g) for name, g in values.items()},
        "rotation_orders": [orders[x], orders[y], orders[z]],
        "original_cusp_unit_residues_mod168": admissible,
        "boundary_pair_at5": boundary_pair5,
        "boundary_pair_image_order_at5": len(generated(boundary_pair5)),
        "boundary_pair_canonical_at5": canonical(boundary_pair5)})
common_units = sorted(set.intersection(*(set(row['original_cusp_unit_residues_mod168'])
                                         for row in coordinate_rows)))
base_triple = sorted(triple_orbits)[0]
check("base_G_times_C2_cubed_has_a_generating_class_triple", len(generated(base_triple)) == 168)
check("two_proper_coordinate_bound_is_strict", 3 * 9 * 9 < 21 * 21)
check("exactly_twenty_four_common_cusp_unit_residues_including5", len(common_units) == 24 and 5 in common_units)

out = {"status": "PASS", "group": "G=GL(3,F2), acting on the seven nonzero vectors",
       "large_group": "G^8 x C2^3", "large_group_order": 168 ** 8 * 8,
       "scope": "Exact finite diagram only; no quotient map from the actual D74 E is constructed.",
       "base_group_permutations": G, "identity_index": one,
       "subgroup_order_involution_histogram": {str(k): v for k, v in Counter(
           (len(H), len(set(I).intersection(H))) for H in subgroups).items()},
       "automorphism_base_pair": base, "automorphism_images_of_base_pair": automorphism_images,
       "generating_pair_count": len(pairs), "generating_pair_orbits": len(pair_orbits),
       "generating_pair_orbit_representatives": sorted(pair_orbits),
       "generating_involution_triple_count": len(triples),
       "generating_involution_triple_orbits": len(triple_orbits),
       "generating_involution_triple_orbit_representatives": sorted(triple_orbits),
       "three_cusp_pair_count": len(filtered), "three_cusp_pair_orbits": len(filtered_orbits),
       "three_cusp_pair_orbit_representatives": sorted(filtered_orbits),
       "selected_coordinate_diagrams": coordinate_rows,
       "base_generating_class_triple": [cycles(g) for g in base_triple],
       "all_units_mod168": unit_residues,
       "common_original_cusp_unit_residues_mod168": common_units,
       "checks": checks, "assertion_count": len(checks)}
target = Path(__file__).with_name('finite_pants_diagram_gl3_2_output.json')
target.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
