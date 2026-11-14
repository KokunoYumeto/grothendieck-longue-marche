#!/usr/bin/env python3
"""All genus-two epimorphic A5 surface tuples with exact Aut(A5) maps.

Enumeration is streamed in the fourth free generator.  The complete
five-Klein-subgroup action proves Aut(A5)=S5 in the retained matrices.
No inference from a target group order is used to identify a source.
"""
from pathlib import Path
from hashlib import sha256
from collections import deque
import json
import time
import numpy as np
from sympy.combinatorics import Permutation
from de_wajnryb_free_model import build
from de_wajnryb_s3_model import perm_word, word_values

HERE = Path(__file__).resolve().parent


def group_data():
    old = np.load(HERE/'de_ferrari_a5_model.npz')
    perms, sm = old['S5_permutations'], old['S5_multiplication']
    si = np.argsort(sm, axis=1)[:, 0]
    even = np.array([j for j, p in enumerate(perms) if
                     sum(p[i] > p[k] for i in range(5) for k in range(i+1, 5)) % 2 == 0])
    assert len(even) == 60 and even[0] == 0
    reverse = np.full(120, -1, dtype=np.int64)
    reverse[even] = np.arange(60)
    mul = reverse[sm[even[:, None], even[None, :]]]
    inv = reverse[si[even]]
    conj = np.array([reverse[sm[sm[g, even], si[g]]] for g in range(120)])
    assert len({tuple(x) for x in conj}) == 120
    assert all(np.array_equal(a[mul], mul[a[:, None], a[None, :]]) for a in conj)
    def closure(generators):
        reached = {0}
        queue = deque([0])
        while queue:
            a = queue.popleft()
            for b in generators:
                c = int(mul[a, b])
                if c not in reached:
                    reached.add(c)
                    queue.append(c)
        return sum(1 << i for i in reached)
    subgroups = {1: ()}
    queue = deque([1])
    while queue:
        h = queue.popleft()
        for t in range(60):
            if h >> t & 1:
                continue
            gs = subgroups[h]+(t,)
            hnew = closure(gs)
            if hnew not in subgroups:
                subgroups[hnew] = gs
                queue.append(hnew)
    full = (1 << 60)-1
    assert full in subgroups and len(subgroups) == 59
    maximal = [h for h in subgroups if h != full and not any(
               h != k and k != full and h & k == h for k in subgroups)]
    assert sorted(h.bit_count() for h in maximal) == [6]*10+[10]*6+[12]*5
    klein = [h for h in subgroups if h.bit_count() == 4]
    assert len(klein) == 5
    for h in klein:
        assert all(mul[t, t] == 0 for t in range(60) if h >> t & 1)
    index = {h: i for i, h in enumerate(klein)}
    klein_actions = []
    for a in conj:
        klein_actions.append([index[sum(1 << int(a[t]) for t in range(60) if h >> t & 1)] for h in klein])
    assert len({tuple(a) for a in klein_actions}) == 120
    # Any automorphism permutes exactly these five Klein groups. Its
    # kernel fixes every inner permutation, hence every element, since
    # the actual inner action on the five groups is injective.
    assert len({tuple(klein_actions[g]) for g in even}) == 60
    return mul, inv, conj, subgroups, maximal, klein_actions


def main():
    start = time.time()
    names = ['de_ferrari_a5_model.npz', 'de_wajnryb_free_model.py',
             'de_wajnryb_free_model.json', 'de_wajnryb_s3_model.py']
    hashes = {n: sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    model = build(2)
    mul, inv, conj, subgroups, maximal, klein_actions = group_data()
    powers = 60**np.arange(3, -1, -1, dtype=np.int64)
    prefix = np.arange(60**3, dtype=np.int64)
    first = prefix[:, None] // (60**np.arange(2, -1, -1))[None, :] % 60
    surface_count = 0
    epimorphisms = []
    for last in range(60):
        tuples = np.column_stack((first, np.full(len(first), last)))
        surface = word_values(model['boundary_word'], tuples, mul, inv) == 0
        surface_count += int(surface.sum())
        selected = tuples[surface]
        masks = np.bitwise_or.reduce(np.int64(1) << selected, axis=1)
        proper = np.zeros(len(selected), dtype=bool)
        for mask in maximal:
            proper |= masks & mask == masks
        epimorphisms.append(selected[~proper])
    et = np.concatenate(epimorphisms)
    codes = et @ powers
    sort = np.argsort(codes)
    et, codes = et[sort], codes[sort]
    assert np.array_equal(np.unique(codes), codes)
    comm = mul[mul[mul[np.arange(60)[:, None], np.arange(60)[None, :]], inv[:, None]], inv[None, :]]
    hist = np.bincount(comm.ravel(), minlength=60)
    expected = int(sum(int(hist[t])*int(hist[inv[t]]) for t in range(60)))
    assert surface_count == expected
    canonical = codes.copy()
    for a in conj:
        canonical = np.minimum(canonical, a[et] @ powers)
    representatives = np.unique(canonical)
    assert len(representatives)*120 == len(et)
    rep_index = {int(c): i for i, c in enumerate(representatives)}
    points = np.array([rep_index[int(c)] for c in canonical], dtype=np.int64)
    point_map = dict(zip(map(int, codes), map(int, points)))
    rt = representatives[:, None] // powers[None, :] % 60
    generators, inverse_generators = [], []
    for family, dest in ((model['generators'], generators), (model['inverses'], inverse_generators)):
        for automorphism in family:
            images = np.column_stack([word_values(w, rt, mul, inv) for w in automorphism])
            image_codes = images @ powers
            p = np.array([point_map[int(c)] for c in image_codes], dtype=np.int64)
            assert np.array_equal(np.sort(p), np.arange(len(rt)))
            dest.append(p)
    generators, inverse_generators = np.array(generators), np.array(inverse_generators)
    assert np.array_equal(np.argsort(generators, axis=1), inverse_generators)
    for rel in model['relations']:
        assert np.array_equal(perm_word(rel['left_word'], generators), perm_word(rel['right_word'], generators))
    assert np.array_equal(perm_word(model['boundary_twist_word'], generators), np.arange(len(rt)))
    x, y = [], []
    for k in range(2, 5):
        yw = tuple(range(k-1, 0, -1))+tuple(range(1, k))
        x.append(perm_word(yw, generators))
        y.append(perm_word((k, k), generators))
    x, y = np.array(x), np.array(y)
    orders = [int(Permutation(p.tolist()).order()) for p in generators]
    unseen, orbit_sizes = set(range(len(rt))), []
    while unseen:
        root = min(unseen)
        orbit = {root}
        queue = deque([root])
        unseen.remove(root)
        while queue:
            q = queue.popleft()
            for a in generators:
                qn = int(a[q])
                if qn not in orbit:
                    orbit.add(qn)
                    unseen.remove(qn)
                    queue.append(qn)
        orbit_sizes.append(len(orbit))
    tag = 'de_wajnryb_a5_g2'
    np.savez_compressed(HERE/(tag+'.npz'), sigma=generators, inverse_sigma=inverse_generators,
                        x=x, y=y, representatives=rt, representative_codes=representatives,
                        all_epimorphism_codes=codes, actual_orbit_point_map=points,
                        A5_multiplication=mul, A5_inverse=inv, AutA5=conj,
                        actual_five_Klein_group_actions=np.array(klein_actions))
    with (HERE/(tag+'_target.input')).open('w') as out:
        out.write(f'{len(rt)} {len(generators)}\n')
        for p in generators:
            out.write(' '.join(map(str, p))+'\n')
    report = {'status': 'PASS_EXHAUSTIVE_SURFACE_A5_WAJNRYB_MODEL', 'genus': 2,
              'all_A5_subgroups': len(subgroups), 'maximal_subgroup_orders': sorted(h.bit_count() for h in maximal),
              'AutA5_order_proved_through_actual_five_Klein_action': 120,
              'all_tuples_checked': 60**4, 'boundary_identity_tuples': surface_count,
              'independent_standard_handle_tuple_count': expected,
              'all_epimorphic_boundary_identity_tuples': len(et),
              'simultaneous_AutA5_orbits': len(rt), 'every_orbit_size': 120,
              'generator_orders': orders, 'actual_mapping_class_orbit_sizes': orbit_sizes,
              'literal_presentation_relations_checked': len(model['relations']),
              'boundary_twist_killed_literally': True, 'evaluation_pair_count': len(x),
              'group_order_computed': False, 'input_sha256': hashes,
              'seconds': round(time.time()-start, 6)}
    (HERE/(tag+'.json')).write_text(json.dumps(report, indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
