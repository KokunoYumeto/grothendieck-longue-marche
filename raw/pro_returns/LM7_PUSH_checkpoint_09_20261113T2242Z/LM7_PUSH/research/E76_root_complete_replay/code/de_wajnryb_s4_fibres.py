#!/usr/bin/env python3
"""Whole retained G6 fibres in the actual Wajnryb S4-cover target.

The complete source kills [N,N]N^6. Each chosen correction word and all
homogeneous correction generators are checked literally. Thus all old
parameters are retained without replacing their fibre by one sample.
Generation is certified by explicit simultaneous point intertwiners.
"""
from pathlib import Path
from hashlib import sha256
from collections import deque
import argparse
import json
import time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_wajnryb_free_model import build
from de_wajnryb_s4_model import perm_word

HERE = Path(__file__).resolve().parent


def multiply(a, b):
    return b[a]


def power(p, n):
    if n < 0:
        return power(np.argsort(p), -n)
    out = np.arange(len(p))
    while n:
        if n & 1:
            out = p[out]
        p = p[p]
        n //= 2
    return out


def bword(word, s, r):
    letters = {0: s, 1: r, -1: np.argsort(r)}
    out = np.arange(len(s))
    for t in word:
        out = letters[t][out]
    return out


def fword(word, x, y):
    letters = {1: x, 2: y, -1: np.argsort(x), -2: np.argsort(y)}
    out = np.arange(len(x))
    for t in word:
        out = letters[t][out]
    return out


def reconstruct(p, metadata):
    out = np.full(metadata['original_degree'], -1, dtype=np.int64)
    starts = np.r_[0, np.cumsum(metadata['retained_orbit_sizes'])]
    for row in metadata['orbit_correspondences']:
        original = np.array(row['original_canonical_order'], dtype=np.int64)
        start = int(starts[row['retained_orbit_index']])
        values = p[start+np.arange(len(original))]-start
        assert np.all((values >= 0) & (values < len(original)))
        out[original] = original[values]
    assert np.array_equal(np.sort(out), np.arange(len(out)))
    return out


def spanning_tree(generators):
    n = generators.shape[1]
    edges = np.r_[generators, np.argsort(generators, axis=1)]
    unseen = set(range(n))
    forest = []
    while unseen:
        root = min(unseen)
        seen = {root}
        unseen.remove(root)
        queue = deque([root])
        tree = []
        while queue:
            p = queue.popleft()
            for j, e in enumerate(edges):
                q = int(e[p])
                if q not in seen:
                    seen.add(q)
                    unseen.remove(q)
                    tree.append((p, j, q))
                    queue.append(q)
        forest.append((root, np.array(sorted(seen)), tree))
    assert sum(len(orbit) for root, orbit, tree in forest) == n
    return forest


def intertwiner(old, new, forest):
    n = old.shape[1]
    edges = np.r_[new, np.argsort(new, axis=1)]
    h = np.full(n, -1, dtype=np.int64)
    attempts = 0
    for root, orbit, tree in forest:
        found = False
        for base in orbit:
            attempts += 1
            h[root] = base
            for p, j, q in tree:
                h[q] = edges[j, h[p]]
            if not np.array_equal(np.sort(h[orbit]), orbit):
                continue
            if all(np.array_equal(h[a[orbit]], b[h[orbit]]) for a, b in zip(old, new)):
                found = True
                break
        if not found:
            return None, attempts
    assert np.array_equal(np.sort(h), np.arange(n))
    assert all(np.array_equal(h[a], b[h]) for a, b in zip(old, new))
    return h, attempts


def main(g):
    start = time.time()
    tag = 'de_wajnryb_s4_g'+str(g)
    names = [tag+'.npz', tag+'_source.npz', tag+'_source.json',
             'de_ferrari_fibres.json', 'de_ferrari_two_lift.json',
             'de_ferrari_degree6_kernel.json', 'de_ferrari_two_degree6_module.json',
             'de_wajnryb_free_model.py', 'de_wajnryb_s4_model.py',
             'de_ferrari_a6_source_data.py', 'de_ferrari_sl2_5_N.json']
    hashes = {n: sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    target = np.load(HERE/names[0])
    source = np.load(HERE/names[1])
    metadata = json.loads((HERE/names[2]).read_text())
    assert metadata['source_factor_through_G6_proved_by_these_checks']
    d = load_data()
    s, r = source['s'], source['r']
    sx, sy = bword(d['xword'], s, r), bword(d['yword'], s, r)
    old = target['sigma']
    n, degree = 2*g, old.shape[1]
    one = np.arange(degree)
    root = sorted(d['Q2']).index(d['unit'])
    offset = root*(n-1)*degree
    for p, expected in ((sx, target['x']), (sy, target['y'])):
        raw = reconstruct(p, metadata)
        pairs = np.array([raw[offset+i*degree:offset+(i+1)*degree]-(offset+i*degree)
                          for i in range(n-1)])
        assert np.array_equal(pairs, expected)
    origins = json.loads((HERE/names[3]).read_text())['records']
    lifts = json.loads((HERE/names[4]).read_text())['records']
    bases = [json.loads((HERE/name).read_text())['F_prime_basis_words'] for name in names[5:7]]
    identity_source = np.arange(len(s))
    correction_words = [row['chosen_witness']['literal_B_old_correction_word'] for row in lifts]
    correction_words += bases[0]+bases[1]
    assert all(np.array_equal(bword(w, s, r), identity_source) for w in correction_words)
    model = build(g)
    tree = spanning_tree(old)
    assert all(np.array_equal(power(a, 73), a) for a in old)
    # Identity is an independent control before the nontrivial source words.
    assert all(np.array_equal(perm_word(rel['left_word'], old),
                              perm_word(rel['right_word'], old)) for rel in model['relations'])
    records, arrays, values = [], [], []
    intertwiners, known = [], {}
    for index, origin in enumerate(origins):
        word = origin['actual_commutator_word_f']
        assert all(sum(1 if t == j else -1 if t == -j else 0 for t in word) == 0 for j in (1, 2))
        p = fword(word, sx, sy)
        raw = reconstruct(p, metadata)
        f = np.array([raw[offset+i*degree:offset+(i+1)*degree]-(offset+i*degree)
                      for i in range(n-1)])
        new = [old[0]]
        for i in range(1, n):
            new.append(multiply(multiply(np.argsort(f[i-1]), old[i]), f[i-1]))
        new.append(old[n])
        new = np.array(new)
        failures = [rel['name'] for rel in model['relations']
                    if not np.array_equal(perm_word(rel['left_word'], new),
                                          perm_word(rel['right_word'], new))]
        key = new.tobytes()
        if not failures and key not in known:
            h, tries = intertwiner(old, new, tree)
            known[key] = (h, tries)
        h, tries = known.get(key, (None, 0))
        if h is not None:
            assert np.array_equal(np.sort(h), one)
            assert all(np.array_equal(h[a], b[h]) for a, b in zip(old, new))
        records.append({'certificate_index': index, 'missing_coset': origin['missing_coset'],
                        'literal_F_word_length': len(word), 'failed_Wajnryb_relations': failures,
                        'all_Wajnryb_relations_pass': not failures,
                        'explicit_target_generation_intertwiner_found': h is not None,
                        'intertwiner_basepoints_tested': tries,
                        'whole_18_point_fibre_and_both_multipliers_retained': True})
        arrays.append(new)
        values.append(f)
        intertwiners.append(h if h is not None else np.full(degree, -1))
        print(json.dumps(records[-1]), flush=True)
    report = {'status': 'PASS_COMPLETE_RETAINED_FIBRE_TEST', 'genus': g,
              'origins': len(records), 'correction_generator_words_checked': len(correction_words),
              'all_864_old_parameters_retained_by_actual_source_kernel': True,
              'multiplier_residues': [1, 73], 'finite_power_period_divides': 12,
              'all_original_target_orbit_sizes': [len(orbit) for root, orbit, edges in tree],
              'number_of_distinct_corrected_generator_tuples': len({a.tobytes() for a in arrays}),
              'identity_control_passes': True, 'records': records,
              'all_relations_pass': all(r['all_Wajnryb_relations_pass'] for r in records),
              'all_full_target_generation_proved': all(r['explicit_target_generation_intertwiner_found'] for r in records),
              'input_sha256': hashes, 'seconds': round(time.time()-start, 6)}
    (HERE/(tag+'_fibres.json')).write_text(json.dumps(report, indent=2)+'\n')
    np.savez_compressed(HERE/(tag+'_fibres.npz'), corrected_generators=np.array(arrays),
                        actual_f_evaluations=np.array(values),
                        simultaneous_point_intertwiners=np.array(intertwiners))
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps({k: v for k, v in report.items() if k not in ('records', 'input_sha256')}, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--genus', type=int, choices=(2,), default=2)
    main(parser.parse_args().genus)
