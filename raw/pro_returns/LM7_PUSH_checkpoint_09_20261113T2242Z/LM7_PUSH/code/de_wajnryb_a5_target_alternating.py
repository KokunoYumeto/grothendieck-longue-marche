#!/usr/bin/env python3
"""Constructive alternating-subgroup certificate for the actual A5 target.

A power of an actual generator word isolates one three-cycle.  Literal
conjugates with a connected support hypergraph generate the full alternating
group on their support.  The two target orbits are retained separately.
"""
from pathlib import Path
from hashlib import sha256
from math import factorial, gcd, lcm
import json
import random
import sys
import time
import numpy as np
from de_wajnryb_s4_fibres import power

HERE = Path(__file__).resolve().parent


def cycles(p):
    unseen = np.ones(len(p), dtype=bool)
    result = []
    for start in range(len(p)):
        if unseen[start]:
            row, q = [], start
            while unseen[q]:
                unseen[q] = False
                row.append(int(q))
                q = int(p[q])
            assert q == start
            result.append(row)
    return result


def orbit_sets(generators):
    unseen = set(range(generators.shape[1]))
    orbits = []
    while unseen:
        q = min(unseen)
        orbit = {q}
        queue = [q]
        unseen.remove(q)
        for a in queue:
            for p in generators:
                b = int(p[a])
                if b not in orbit:
                    orbit.add(b)
                    unseen.remove(b)
                    queue.append(b)
        orbits.append(sorted(orbit))
    return orbits


def rank2(rows):
    basis = {}
    for row in rows:
        v = sum(int(x) << i for i, x in enumerate(row))
        while v:
            j = v.bit_length()-1
            if j in basis:
                v ^= basis[j]
            else:
                basis[j] = v
                break
    return len(basis)


def main():
    sys.set_int_max_str_digits(0)
    start = time.monotonic()
    filename = 'de_wajnryb_a5_g2.npz'
    original = np.load(HERE/filename)['sigma']
    edges = np.r_[original, np.argsort(original, axis=1)]
    labels = list(range(1, len(original)+1))+list(range(-1, -len(original)-1, -1))
    lookup = {a: i for i, a in enumerate(labels)}
    orbits = orbit_sets(original)
    assert sorted(map(len, orbits)) == [576, 1440]
    point_orbit = {p: i for i, orbit in enumerate(orbits) for p in orbit}
    rng = random.Random(76052026)
    word, p, witnesses = [], np.arange(original.shape[1]), {}
    attempts = 0
    # A successful certificate is checked from its literal word, independently
    # of the search condition.  Exhaustion is only a recorded search failure.
    for step in range(200000):
        j = rng.randrange(len(edges))
        word.append(labels[j])
        p = edges[j][p]
        if step % 7:
            continue
        attempts += 1
        cc = cycles(p)
        threes = [row for row in cc if len(row) % 3 == 0]
        if len(threes) != 1 or len(threes[0]) != 3:
            continue
        triple = threes[0]
        orbit_index = point_orbit[triple[0]]
        if orbit_index in witnesses:
            continue
        assert all(point_orbit[q] == orbit_index for q in triple)
        exponent = 1
        for row in cc:
            if len(row) != 3:
                exponent = lcm(exponent, len(row))
        assert gcd(exponent, 3) == 1
        exponent *= exponent % 3
        isolated = power(p, exponent)
        nontrivial = [row for row in cycles(isolated) if len(row) > 1]
        assert len(nontrivial) == 1 and len(nontrivial[0]) == 3
        witnesses[orbit_index] = {'literal_word': list(word), 'power': str(exponent),
                                  'three_cycle': nontrivial[0],
                                  'all_other_cycles_killed': True,
                                  'original_cycle_lengths': [len(row) for row in cc]}
        print(json.dumps({'found_orbit': orbit_index, 'size': len(orbits[orbit_index]),
                          'word_length': len(word), 'three_cycle': nontrivial[0]}), flush=True)
        if len(witnesses) == len(orbits):
            break
    search_report = {'isolated_orbit_count': len(witnesses), 'attempts': attempts,
                     'steps': len(word), 'required_orbit_count': len(orbits)}
    if len(witnesses) != len(orbits):
        out = {'status': 'INCOMPLETE_THREE_CYCLE_SEARCH', **search_report,
               'scope': 'No generation or exclusion conclusion from the incomplete search.',
               'seconds': round(time.monotonic()-start, 6)}
        (HERE/'de_wajnryb_a5_target_alternating.json').write_text(json.dumps(out, indent=2)+'\n')
        print(json.dumps(out, indent=2), flush=True)
        return
    records = []
    for orbit_index, orbit in enumerate(orbits):
        witness = witnesses[orbit_index]
        # Independent reconstruction of the selected generator word.
        check = np.arange(len(p))
        for a in witness['literal_word']:
            check = edges[lookup[a]][check]
        check = power(check, int(witness['power']))
        triple = witness['three_cycle']
        expected = np.arange(len(p))
        for a, b in zip(triple, triple[1:]+triple[:1]):
            expected[a] = b
        assert np.array_equal(check, expected)
        parent = list(range(len(p)))
        size = [1]*len(p)
        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return False
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
            return True
        steps, selected = [], []
        current = np.array(triple)
        for k in range(500000):
            changed = union(int(current[0]), int(current[1]))
            changed = union(int(current[0]), int(current[2])) or changed
            if changed:
                selected.append({'prefix_length': len(steps), 'three_cycle': current.tolist()})
            if size[find(orbit[0])] == len(orbit):
                break
            j = rng.randrange(len(edges))
            steps.append(labels[j])
            # This is g^-1 c g in the right-action permutation convention.
            current = edges[j][current]
        assert size[find(orbit[0])] == len(orbit), ('conjugate support graph incomplete', orbit_index)
        assert {q for q in range(len(p)) if find(q) == find(orbit[0])} == set(orbit)
        # The replay uses only the saved conjugator walk and selected triples.
        current = np.array(triple)
        at = {row['prefix_length']: row['three_cycle'] for row in selected}
        seen = []
        for k in range(len(steps)+1):
            if k in at:
                assert current.tolist() == at[k]
                seen.append(current.tolist())
            if k < len(steps):
                current = edges[lookup[steps[k]]][current]
        assert len(seen) == len(selected)
        records.append({'orbit_index': orbit_index, 'orbit_size': len(orbit),
                        'orbit_points': orbit, **witness,
                        'conjugator_walk': steps, 'selected_conjugate_three_cycles': selected,
                        'support_hypergraph_connected': True})
        print(json.dumps({'connected_orbit': orbit_index, 'size': len(orbit),
                          'conjugator_steps': len(steps), 'selected_three_cycles': len(selected)}), flush=True)
    parities = []
    for g in original:
        row = []
        for orbit in orbits:
            pos = {p: i for i, p in enumerate(orbit)}
            restricted = np.array([pos[int(g[p])] for p in orbit])
            row.append((len(orbit)-len(cycles(restricted))) % 2)
        parities.append(row)
    rank = rank2(parities)
    order = 2**rank
    for orbit in orbits:
        order *= factorial(len(orbit))//2
    out = {'status': 'PASS_CONSTRUCTIVE_FULL_ALTERNATING_TARGET_KERNEL',
           'orbits': [len(orbit) for orbit in orbits],
           'literal_generator_parity_rows': parities, 'parity_image_rank': rank,
           'target_order': str(order), 'target_order_formula':
               f'2^{rank} * '+ ' * '.join(f'({len(orbit)}!/2)' for orbit in orbits),
           'records': records, 'three_cycle_search': search_report,
           'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
           'input_sha256': {filename: sha256((HERE/filename).read_bytes()).hexdigest(),
                            'de_wajnryb_s4_fibres.py': sha256((HERE/'de_wajnryb_s4_fibres.py').read_bytes()).hexdigest()},
           'seconds': round(time.monotonic()-start, 6)}
    (HERE/'de_wajnryb_a5_target_alternating.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: v for k, v in out.items() if k not in {'records', 'input_sha256', 'target_order'}}, indent=2), flush=True)


if __name__ == '__main__':
    main()
