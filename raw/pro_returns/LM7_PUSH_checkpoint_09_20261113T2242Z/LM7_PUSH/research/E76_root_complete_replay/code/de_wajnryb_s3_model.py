#!/usr/bin/env python3
"""Finite Wajnryb action on all epimorphic S3 surface tuples.

Every tuple has the literal boundary word equal to one. Simultaneous
Aut(S3)=Inn(S3) orbits are enumerated exhaustively, with actual point
maps, before any braid evaluation or source compression is performed.
"""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
import argparse
import json
import time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
from de_wajnryb_free_model import build

HERE = Path(__file__).resolve().parent


def s3():
    elements = list(permutations(range(3)))
    index = {p: i for i, p in enumerate(elements)}
    mul = np.array([[index[tuple(a[b[i]] for i in range(3))]
                     for b in elements] for a in elements], dtype=np.int64)
    inv = np.array([next(j for j in range(6) if mul[i, j] == mul[j, i] == 0)
                    for i in range(6)], dtype=np.int64)
    conj = np.array([[mul[mul[g, x], inv[g]] for x in range(6)]
                     for g in range(6)], dtype=np.int64)
    assert len({tuple(row) for row in conj}) == 6
    for a in range(6):
        for b in range(6):
            assert np.array_equal(mul[mul[a, b]], mul[a, mul[b]])
    generated_order = []
    for mask in range(64):
        gens = [i for i in range(6) if mask >> i & 1]
        subgroup = {0}
        todo = [0]
        while todo:
            a = todo.pop()
            for b in gens:
                c = int(mul[a, b])
                if c not in subgroup:
                    subgroup.add(c)
                    todo.append(c)
        generated_order.append(len(subgroup))
    return elements, mul, inv, conj, np.array(generated_order)


def word_values(word, tuples, mul, inv):
    out = np.zeros(len(tuples), dtype=np.int64)
    for t in word:
        value = tuples[:, abs(t)-1]
        out = mul[out, value if t > 0 else inv[value]]
    return out


def perm_word(word, generators):
    out = np.arange(generators.shape[1], dtype=np.int64)
    for t in word:
        p = generators[t-1] if t > 0 else np.argsort(generators[-t-1])
        out = p[out]
    return out


def main(g):
    start = time.time()
    names = ['de_wajnryb_free_model.py', 'de_wajnryb_free_model.json']
    hashes = {n: sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    model = build(g)
    n = model['rank']
    elements, mul, inv, conj, generated_order = s3()
    powers = 6**np.arange(n-1, -1, -1, dtype=np.int64)
    numbers = np.arange(6**n, dtype=np.int64)
    tuples = numbers[:, None] // powers[None, :] % 6
    boundary = word_values(model['boundary_word'], tuples, mul, inv)
    masks = np.bitwise_or.reduce(1 << tuples, axis=1)
    surface = boundary == 0
    epi = surface & (generated_order[masks] == 6)
    expected_all = int(6**(2*g-1)*(2+2**(2-2*g)))
    assert int(surface.sum()) == expected_all
    expected_proper = 3**n+3*2**n-3
    assert int(epi.sum()) == expected_all-expected_proper
    canon = np.full(len(tuples), -1, dtype=np.int64)
    et = tuples[epi]
    conjugate_codes = np.array([conj[h, et] @ powers for h in range(6)])
    assert all(len(set(row)) == 6 for row in conjugate_codes.T)
    canonical = np.min(conjugate_codes, axis=0)
    representatives = np.unique(canonical)
    assert len(representatives)*6 == len(et)
    rt = tuples[representatives]
    lookup = np.full(len(tuples), -1, dtype=np.int64)
    lookup[representatives] = np.arange(len(representatives))
    canon[numbers[epi]] = lookup[canonical]
    generators = []
    inverse_generators = []
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
        assert np.array_equal(perm_word(rel['left_word'], generators),
                              perm_word(rel['right_word'], generators))
    assert np.array_equal(perm_word(model['boundary_twist_word'], generators), np.arange(len(rt)))
    x, y = [], []
    for k in range(2, n+1):
        yw = tuple(range(k-1, 0, -1))+tuple(range(1, k))
        x.append(perm_word(yw, generators))
        y.append(perm_word((k, k), generators))
    x, y = np.array(x), np.array(y)
    orders = [int(Permutation(p.tolist()).order()) for p in generators]
    exact_group_order = int(PermutationGroup([Permutation(p.tolist()) for p in generators]).order()) if g == 2 else None
    stem = 'de_wajnryb_s3_g'+str(g)
    np.savez_compressed(HERE/(stem+'.npz'), sigma=generators, inverse_sigma=inverse_generators,
                        x=x, y=y, representatives=rt, representative_codes=representatives,
                        all_epimorphism_codes=numbers[epi], actual_orbit_point_map=canon,
                        S3_multiplication=mul, S3_inverse=inv, S3_conjugation=conj)
    with (HERE/(stem+'_target.input')).open('w') as out:
        out.write(f'{len(rt)} {len(generators)}\n')
        for p in generators:
            out.write(' '.join(map(str, p))+'\n')
    report = {'status': 'PASS_EXHAUSTIVE_SURFACE_S3_WAJNRYB_MODEL', 'genus': g,
              'rank_of_original_free_group': n,
              'all_tuples': len(tuples), 'boundary_identity_tuples': int(surface.sum()),
              'all_epimorphic_boundary_identity_tuples': int(epi.sum()),
              'simultaneous_AutS3_orbits': len(rt), 'every_orbit_size': 6,
              'generator_orders': orders, 'literal_presentation_relations_checked': len(model['relations']),
              'boundary_twist_killed_literally': True,
              'evaluation_pair_count': len(x), 'target_group_order': exact_group_order,
              'group_order_computed': exact_group_order is not None,
              'tuple_action': 'rho maps to rho composed with the saved free automorphism, then the same simultaneous-conjugacy orbit',
              'input_sha256': hashes, 'seconds': round(time.time()-start, 6)}
    (HERE/(stem+'.json')).write_text(json.dumps(report, indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--genus', type=int, choices=(2, 3), default=3)
    main(parser.parse_args().genus)
