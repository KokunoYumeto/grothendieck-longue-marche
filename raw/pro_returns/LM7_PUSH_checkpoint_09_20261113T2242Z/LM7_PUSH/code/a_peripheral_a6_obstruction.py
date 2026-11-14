#!/usr/bin/env python3
"""Exact proper-lift obstruction and complete conjugator union for A6.

Read the fully enumerated actual automorphisms from a_peripheral_a6_outer,
verify their literal generator-edge maps again, and compute both source
orbits and all64 base-centralizer choices.  The chosen kernel is Inn(A6),
the base its actual C2^2 quotient, and H3=X is an actual lift of the
prescribed nontrivial third base conjugator.
"""

from collections import Counter
from itertools import product
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    raw = json.loads(HERE.joinpath('a_peripheral_a6_outer.json').read_text())
    S = module.Group('A6', [tuple(p) for p in raw['A6_elements']],
                     module.perm_mul, tuple(range(6)))
    x, y = raw['A6_generators']
    pairs = [tuple(p) for p in raw['automorphism_generator_pairs']]
    maps = {p: tuple(v) for p, v in zip(pairs, raw['automorphism_maps'])}
    assert all(len(set(maps[p])) == 360 and maps[p][S.one] == S.one
               and all(maps[p][S.mul[g][a]] == S.mul[maps[p][g]][maps[p][a]]
                       for g in range(360) for a in (x, y)) for p in pairs)
    E = module.Group('Aut(A6)', pairs,
                     lambda a, b: (maps[a][b[0]], maps[a][b[1]]), (x, y))
    inner = frozenset(raw['inner_indices'])
    outer = raw['outer_coordinates']
    classes = [frozenset(c) for c in raw['relative_classes']]
    class_of = {g: i for i, c in enumerate(classes) for g in c}
    source = (42, 109, 225)
    assert E.mul[E.mul[source[0]][source[1]]][source[2]] == E.one
    assert len(E.generated(source[:2])) == 1440
    assert [E.orders[g] for g in source] == [2, 8, 8]
    assert [outer[g] for g in source] == [1, 2, 3]
    assert [class_of[g] for g in source] == [12, 7, 9]
    target_third = E.conjugate(source[0], source[2])
    assert class_of[target_third] == 5

    def triples(profile):
        c1, c2, c3 = [classes[i] for i in profile]
        return {(u, v, E.inv[E.mul[u][v]]) for u in c1 for v in c2
                if E.inv[E.mul[u][v]] in c3}

    original = triples((12, 7, 9))
    bad = triples((12, 7, 5))
    assert len(original) == 360 and len(bad) == 90
    conjugated_source = {tuple(E.conjugate(g, a) for a in source) for g in inner}
    assert conjugated_source == original
    bad0 = min(bad)
    bad_orbit = {tuple(E.conjugate(g, a) for a in bad0) for g in inner}
    assert bad_orbit == bad
    bad_group = E.generated(bad0[:2])
    assert len(bad_group) == 16
    assert len(bad_group & inner) == 4
    assert E.orders[bad0[0]] == 2 and E.orders[bad0[1]] == 8
    assert E.conjugate(bad0[0], bad0[1]) == E.power(bad0[1], 5)
    assert bad_group & inner == E.generated([E.power(bad0[1], 2)])
    centralizer = {g for g in inner if all(E.conjugate(g, a) == a for a in bad0)}
    assert len(centralizer) == 4
    source_centralizer = {g for g in inner if all(E.conjugate(g, a) == a for a in source)}
    assert source_centralizer == {E.one}
    print('PASS: source(2,8,8) generates order1440; its fixed relative profile has360 lifts')
    print('PASS: third conjugator H3=X changes the profile to90 weak lifts; each has image C8 semidirect_5 C2 of order16')

    action = raw['outer_class_action']
    choices, profiles = [], {}
    union = set()
    good_union = set()
    for h1, h2, h3 in product(range(4), repeat=3):
        profile = (action[h1][12], action[h2][7], action[h3][9])
        if profile not in profiles:
            values = triples(profile)
            # Every good profile is the global E-conjugate of source;
            # every bad profile is the global E-conjugate of bad0.
            source_match = next((r for r in raw['outer_representatives']
                                 if tuple(class_of[E.conjugate(r, a)] for a in source) == profile), None)
            bad_match = next((r for r in raw['outer_representatives']
                              if tuple(class_of[E.conjugate(r, a)] for a in bad0) == profile), None)
            assert (source_match is None) != (bad_match is None)
            if source_match is not None:
                transformed = {tuple(E.conjugate(source_match, a) for a in t) for t in original}
                assert transformed == values and len(values) == 360
                good_union |= values
                image_order = 1440
            else:
                transformed = {tuple(E.conjugate(bad_match, a) for a in t) for t in bad}
                assert transformed == values and len(values) == 90
                image_order = 16
            profiles[profile] = {'weak_count': len(values),
                                 'proper_count': len(values) if image_order == 1440 else 0,
                                 'common_image_order': image_order,
                                 'representative': min(values)}
            union |= values
        record = profiles[profile]
        obstruction = ((h1 >> 1) ^ h2 ^ h3 ^ (h3 >> 1)) & 1
        assert bool(record['proper_count']) == (obstruction == 0)
        choices.append({'h': [h1, h2, h3], 'profile': profile,
                        'relative_parity': obstruction, **record})
    assert len(profiles) == 8
    assert len(union) == 1800 and len(good_union) == 1440
    full_source_orbit = {tuple(E.conjugate(g, a) for a in source) for g in range(E.size)}
    full_bad_orbit = {tuple(E.conjugate(g, a) for a in bad0) for g in range(E.size)}
    assert full_source_orbit == good_union
    assert full_bad_orbit == union-good_union
    assert len(full_bad_orbit) == 360
    counts = Counter((r['weak_count'], r['proper_count']) for r in choices)
    assert counts == {(360, 360): 32, (90, 0): 32}
    print('PASS: all64 base-centralizer choices:', dict(counts))
    print('PASS: forgetful union has1800 weak/1440 proper lifts in two full E-orbits of sizes1440,360')

    def descriptions(elements):
        return [{'index': a, 'outer': outer[a], 'order': E.orders[a],
                 'images_of_generators': [S.elements[j] for j in pairs[a]]}
                for a in elements]

    # The saved complete normal-closure certificate proves simplicity;
    # this nontrivial commutator then proves perfectness.
    comm = next(S.commutator(a, b) for a in range(S.size) for b in range(S.size)
                if S.commutator(a, b) != S.one)
    assert len(S.generated(list(S.conjugacy_class(comm)))) == 360
    payload = {
        'status': 'PASS_A6_PROPER_OBSTRUCTION_AND_FORGETFUL_UNION',
        'A6_generators': [S.elements[x], S.elements[y]],
        'source_triple': descriptions(source),
        'target_third': descriptions([target_third])[0],
        'specified_base_conjugators': [0, 0, 1],
        'source_relative_profile': [12, 7, 9],
        'target_relative_profile': [12, 7, 5],
        'source_weak_and_proper_count': 360,
        'target_weak_count': 90, 'target_proper_count': 0,
        'all90_target_triples': sorted(bad),
        'bad_representative': descriptions(bad0),
        'bad_generated_subgroup': sorted(bad_group),
        'bad_group_presentation': 'r^8=s^2=1, s*r*s^-1=r^5; r=second, s=first',
        'bad_inner_centralizer': sorted(centralizer),
        'outer_base_identification': {'x': 1, 'y': 2, 'z': 3, 'addition': 'bitwise XOR'},
        'all64_conjugator_cases': choices,
        'all8_profiles': [{'profile': p, **v} for p, v in sorted(profiles.items())],
        'ordinary_weak_count': len(union), 'ordinary_proper_count': len(good_union),
        'ordinary_E_orbit_sizes': [1440, 360],
        'relative_obstruction_formula': 'q1+p2+p3+q3 mod2, for hi=pi*x+qi*y',
        'maximal_pro5_quotient_orders': {'E': 1, 'D': 1},
        'scope': 'An obstruction with specified base conjugators. Forgetting them '
                 'gives a nonempty ordinary peripheral lift fibre; no pro-five '
                 'leading-term restriction is asserted.'}
    HERE.joinpath('a_peripheral_a6_obstruction.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
