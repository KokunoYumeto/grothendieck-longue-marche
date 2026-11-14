#!/usr/bin/env python3
"""All epimorphic S4 genus-two surface tuples and their actual action.

The full S4 automorphism group is verified from complete Cayley maps.
Every subgroup and every surface tuple is enumerated exactly; the
quotient by simultaneous automorphisms has an explicit point map.
"""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
from collections import deque
import argparse
import json
import time
import numpy as np
from sympy.combinatorics import Permutation
from de_wajnryb_free_model import build
from de_wajnryb_s3_model import perm_word, word_values

HERE = Path(__file__).resolve().parent


def group_data():
    elements = list(permutations(range(4)))
    ix = {p: i for i, p in enumerate(elements)}
    mul = np.array([[ix[tuple(a[b[i]] for i in range(4))]
                     for b in elements] for a in elements], dtype=np.int64)
    inv = np.array([next(j for j in range(24) if mul[i, j] == mul[j, i] == 0)
                    for i in range(24)], dtype=np.int64)
    conj = np.array([[mul[mul[g, x], inv[g]] for x in range(24)]
                     for g in range(24)], dtype=np.int64)
    orders = [int(Permutation(list(p)).order()) for p in elements]
    cls = [len(set(conj[:, i])) for i in range(24)]
    a, b = ix[(1, 0, 2, 3)], ix[(1, 2, 3, 0)]
    automorphisms = []
    attempts = 0
    for aa in range(24):
        if orders[aa] != orders[a] or cls[aa] != cls[a]:
            continue
        for bb in range(24):
            if orders[bb] != orders[b]:
                continue
            attempts += 1
            mapping = np.full(24, -1, dtype=np.int64)
            mapping[0] = 0
            queue = deque([0])
            consistent = True
            while queue and consistent:
                q = queue.popleft()
                for t, tt in ((a, aa), (b, bb)):
                    qn, image = int(mul[q, t]), int(mul[mapping[q], tt])
                    if mapping[qn] == -1:
                        mapping[qn] = image
                        queue.append(qn)
                    elif mapping[qn] != image:
                        consistent = False
                        break
            if consistent and len(set(mapping)) == 24:
                assert np.array_equal(mapping[mul], mul[mapping[:, None], mapping[None, :]])
                automorphisms.append(mapping)
    assert len(automorphisms) == 24
    assert {tuple(p) for p in automorphisms} == {tuple(p) for p in conj}
    def closure(generators):
        reached = {0}
        queue = deque([0])
        while queue:
            q = queue.popleft()
            for t in generators:
                qt = int(mul[q, t])
                if qt not in reached:
                    reached.add(qt)
                    queue.append(qt)
        return sum(1 << q for q in reached)
    subgroups = {1: ()}
    queue = deque([1])
    while queue:
        h = queue.popleft()
        for t in range(24):
            if h >> t & 1:
                continue
            gs = subgroups[h]+(t,)
            hnew = closure(gs)
            if hnew not in subgroups:
                subgroups[hnew] = gs
                queue.append(hnew)
    full = (1 << 24)-1
    assert full in subgroups
    maximal = [h for h in subgroups if h != full and not any(
               h != k and k != full and h & k == h for k in subgroups)]
    assert len(subgroups) == 30 and sorted(h.bit_count() for h in maximal) == [6, 6, 6, 6, 8, 8, 8, 12]
    return elements, mul, inv, conj, subgroups, maximal, attempts


def main(g=2):
    assert g == 2
    start = time.time()
    names = ['de_wajnryb_free_model.py', 'de_wajnryb_free_model.json', 'de_wajnryb_s3_model.py']
    hashes = {n: sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    model = build(g)
    n = 2*g
    elements, mul, inv, conj, subgroups, maximal, attempts = group_data()
    powers = 24**np.arange(n-1, -1, -1, dtype=np.int64)
    numbers = np.arange(24**n, dtype=np.int64)
    tuples = numbers[:, None] // powers[None, :] % 24
    surface = word_values(model['boundary_word'], tuples, mul, inv) == 0
    masks = np.bitwise_or.reduce(np.int64(1) << tuples, axis=1)
    proper = np.zeros(len(tuples), dtype=bool)
    for mask in maximal:
        proper |= masks & mask == masks
    epi = surface & ~proper
    # Independent standard-handle commutator count for the closed genus2 surface.
    comm = mul[mul[mul[np.arange(24)[:, None], np.arange(24)[None, :]], inv[:, None]], inv[None, :]]
    hist = np.bincount(comm.ravel(), minlength=24)
    standard_surface_count = int(sum(int(hist[t])*int(hist[inv[t]]) for t in range(24)))
    assert int(surface.sum()) == standard_surface_count
    et = tuples[epi]
    conjugate_codes = np.array([conj[h, et] @ powers for h in range(24)])
    assert all(len(set(row)) == 24 for row in conjugate_codes.T)
    canonical = np.min(conjugate_codes, axis=0)
    representatives = np.unique(canonical)
    assert len(representatives)*24 == len(et)
    rt = tuples[representatives]
    lookup = np.full(len(tuples), -1, dtype=np.int64)
    lookup[representatives] = np.arange(len(representatives))
    canon = np.full(len(tuples), -1, dtype=np.int64)
    canon[numbers[epi]] = lookup[canonical]
    generators, inverse_generators = [], []
    for family, dest in ((model['generators'], generators), (model['inverses'], inverse_generators)):
        for automorphism in family:
            images = np.column_stack([word_values(w, rt, mul, inv) for w in automorphism])
            codes = images @ powers
            assert np.all(epi[codes])
            p = canon[codes]
            assert np.array_equal(np.sort(p), np.arange(len(rt)))
            dest.append(p)
    generators, inverse_generators = np.array(generators), np.array(inverse_generators)
    assert np.array_equal(np.argsort(generators, axis=1), inverse_generators)
    for rel in model['relations']:
        assert np.array_equal(perm_word(rel['left_word'], generators), perm_word(rel['right_word'], generators))
    assert np.array_equal(perm_word(model['boundary_twist_word'], generators), np.arange(len(rt)))
    x, y = [], []
    for k in range(2, n+1):
        yw = tuple(range(k-1, 0, -1))+tuple(range(1, k))
        x.append(perm_word(yw, generators))
        y.append(perm_word((k, k), generators))
    x, y = np.array(x), np.array(y)
    orders = [int(Permutation(p.tolist()).order()) for p in generators]
    tag = 'de_wajnryb_s4_g2'
    np.savez_compressed(HERE/(tag+'.npz'), sigma=generators, inverse_sigma=inverse_generators,
                        x=x, y=y, representatives=rt, representative_codes=representatives,
                        all_epimorphism_codes=numbers[epi], actual_orbit_point_map=canon,
                        S4_multiplication=mul, S4_inverse=inv, S4_conjugation=conj)
    with (HERE/(tag+'_target.input')).open('w') as out:
        out.write(f'{len(rt)} {len(generators)}\n')
        for p in generators:
            out.write(' '.join(map(str, p))+'\n')
    report = {'status': 'PASS_EXHAUSTIVE_SURFACE_S4_WAJNRYB_MODEL', 'genus': g,
              'all_S4_subgroups': len(subgroups), 'maximal_subgroup_orders': sorted(h.bit_count() for h in maximal),
              'all_Cayley_automorphism_candidates': attempts, 'all_automorphisms_are_the_24_inner_maps': True,
              'all_tuples': len(tuples), 'boundary_identity_tuples': int(surface.sum()),
              'independent_standard_handle_tuple_count': standard_surface_count,
              'all_epimorphic_boundary_identity_tuples': int(epi.sum()),
              'simultaneous_AutS4_orbits': len(rt), 'every_orbit_size': 24,
              'generator_orders': orders, 'literal_presentation_relations_checked': len(model['relations']),
              'boundary_twist_killed_literally': True, 'evaluation_pair_count': len(x),
              'group_order_computed': False, 'input_sha256': hashes,
              'seconds': round(time.time()-start, 6)}
    (HERE/(tag+'.json')).write_text(json.dumps(report, indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--genus', type=int, choices=(2,), default=2)
    main(parser.parse_args().genus)
