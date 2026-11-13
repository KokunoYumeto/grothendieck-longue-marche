#!/usr/bin/env python3
"""Exact A6 automorphism and relative peripheral-class computation.

Construct A6 from all360 even permutations, enumerate every automorphism
from the images of one literal generating pair, and retain its actual
360-point map.  Composition is then computed from the two generator
images.  The resulting group is used without substituting an abstract
outer quotient.  Relative class products over its order-four quotient
are counted exactly, with actual generating witnesses when found.
"""

from collections import Counter, deque
from itertools import permutations, product
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    S = module.Group('A6', [p for p in permutations(range(6)) if module.parity(p) == 0],
                     module.perm_mul, tuple(range(6)))
    assert S.size == 360
    x = S.index[(1, 2, 3, 0, 5, 4)]
    y = S.index[(1, 2, 3, 4, 0, 5)]
    assert S.orders[x] == 4 and S.orders[y] == 5
    assert len(S.generated([x, y])) == 360
    xy_order = S.orders[S.mul[x][y]]
    comm_order = S.orders[S.commutator(x, y)]
    print('A6 actual generating pair:', S.elements[x], S.elements[y],
          'orders', S.orders[x], S.orders[y], xy_order, comm_order, flush=True)

    def candidate(aa, bb):
        image = [-1]*S.size
        image[S.one] = S.one
        todo = deque([S.one])
        while todo:
            g = todo.popleft()
            for u, v in ((x, aa), (y, bb)):
                h = S.mul[g][u]
                target = S.mul[image[g]][v]
                if image[h] >= 0:
                    if image[h] != target:
                        return None
                else:
                    image[h] = target
                    todo.append(h)
        assert all(i >= 0 for i in image)
        if len(set(image)) != S.size:
            return None
        return tuple(image)

    maps = {}
    tried = 0
    for aa in range(S.size):
        if S.orders[aa] != 4:
            continue
        for bb in range(S.size):
            if S.orders[bb] != 5 or S.orders[S.mul[aa][bb]] != xy_order:
                continue
            if S.orders[S.commutator(aa, bb)] != comm_order:
                continue
            tried += 1
            value = candidate(aa, bb)
            if value is not None:
                maps[(aa, bb)] = value
    assert len(maps) == 1440
    print('PASS: exhaustive generator-image enumeration gives1440 automorphisms;',
          tried, 'candidate pairs tested', flush=True)
    E = module.Group('Aut(A6)', sorted(maps),
                     lambda a, b: (maps[a][b[0]], maps[a][b[1]]), (x, y))
    inner = frozenset(E.index[(S.conjugate(g, x), S.conjugate(g, y))]
                      for g in range(S.size))
    assert len(inner) == 360
    assert all(maps[E.elements[E.mul[a][b]]][s] == maps[E.elements[a]][maps[E.elements[b]][s]]
               for a, b in ((a, (17*a+1) % E.size) for a in range(E.size))
               for s in range(S.size))
    Q, projection, representatives = E.quotient(inner, 'Out(A6)')
    assert Q.size == 4 and sorted(Q.orders) == [1, 2, 2, 2]
    nonzero = [q for q in range(4) if q != Q.one]
    a, b = nonzero[:2]
    bits = {Q.one: 0, a: 1, b: 2, Q.mul[a][b]: 3}
    outer = [bits[projection[g]] for g in range(E.size)]
    assert all(outer[E.mul[g][h]] == outer[g] ^ outer[h]
               for g in range(E.size) for h in range(E.size))
    outer_reps = [next(g for g in range(E.size) if outer[g] == i) for i in range(4)]
    print('PASS: actual inner kernel order360; outer quotient C2^2', flush=True)

    unseen, classes = set(range(E.size)), []
    while unseen:
        g = min(unseen)
        c = {E.conjugate(h, g) for h in inner}
        unseen -= c
        assert len({outer[h] for h in c}) == 1
        classes.append(c)
    class_of = {g: i for i, c in enumerate(classes) for g in c}
    action = [[class_of[E.conjugate(r, min(c))] for c in classes] for r in outer_reps]
    assert all(action[i][action[j][k]] == action[i ^ j][k]
               for i, j in product(range(4), repeat=2) for k in range(len(classes)))
    metadata = [{'index': i, 'representative': min(c), 'outer': outer[min(c)],
                 'order': E.orders[min(c)], 'size': len(c)} for i, c in enumerate(classes)]
    print('Relative inner classes (index,outer,order,size):',
          [(r['index'], r['outer'], r['order'], r['size']) for r in metadata], flush=True)

    # Prove A6 simplicity directly by normal closures of every nontrivial
    # conjugacy class.  This also identifies the kernel as an actual chief.
    Sclasses, remainder = [], set(range(S.size))
    while remainder:
        g = min(remainder)
        c = S.conjugacy_class(g)
        remainder -= c
        closure = S.generated(list(c))
        assert len(closure) == (1 if g == S.one else 360)
        Sclasses.append({'representative': g, 'order': S.orders[g], 'size': len(c),
                         'normal_closure_order': len(closure)})
    assert len(Sclasses) == 7
    print('PASS: all seven A6 classes have the required normal closures', flush=True)

    profile_counts = Counter()
    profile_pairs = {}
    for u in range(E.size):
        if outer[u] != 1:
            continue
        for v in range(E.size):
            if outer[v] != 2:
                continue
            w = E.inv[E.mul[u][v]]
            key = (class_of[u], class_of[v], class_of[w])
            profile_counts[key] += 1
            profile_pairs.setdefault(key, []).append((u, v))
    assert sum(profile_counts.values()) == 360**2
    anomalies, generation_trials = [], 0
    for key in sorted(profile_counts):
        comparisons = []
        for shifts in product(range(4), repeat=3):
            target = tuple(action[shifts[i]][key[i]] for i in range(3))
            if profile_counts[target] != profile_counts[key]:
                comparisons.append((shifts, target, profile_counts[target]))
        if not comparisons:
            continue
        generator = None
        for u, v in profile_pairs[key]:
            generation_trials += 1
            if len(E.generated([u, v])) == E.size:
                generator = (u, v, E.inv[E.mul[u][v]])
                break
        if generator is not None:
            anomalies.append({'source_profile': key,
                              'source_weak_count': profile_counts[key],
                              'source_generating_triple': generator,
                              'different_comparisons': [
                                  {'outer_conjugators': shifts, 'target_profile': target,
                                   'target_weak_count': count}
                                  for shifts, target, count in comparisons]})
            print('Generating source with unequal weak count:', anomalies[-1], flush=True)
            if any(c[2] == 0 for c in comparisons):
                break
    if not anomalies:
        print('No unequal relative weak count over the three nonzero outer cosets.', flush=True)
    has_obstruction = any(c['target_weak_count'] == 0 for a in anomalies
                          for c in a['different_comparisons'])
    print('Generation trials for unequal profiles:', generation_trials, flush=True)
    print('Exact zero-target obstruction found:', has_obstruction, flush=True)

    payload = {'status': 'PASS_A6_ACTUAL_OUTER_CLASS_COMPUTATION',
               'A6_elements': S.elements, 'A6_generators': [x, y],
               'A6_classes': Sclasses, 'automorphism_generator_pairs': E.elements,
               'automorphism_maps': [maps[p] for p in E.elements],
               'inner_indices': sorted(inner), 'outer_coordinates': outer,
               'outer_representatives': outer_reps,
               'relative_classes': [sorted(c) for c in classes],
               'relative_class_metadata': metadata, 'outer_class_action': action,
               'nonzero_outer_profile_counts': [
                   {'classes': key, 'count': profile_counts[key]}
                   for key in sorted(profile_counts)],
               'generation_trials': generation_trials,
               'generating_count_anomalies': anomalies,
               'zero_target_obstruction': has_obstruction,
               'scope': 'The actual chief extension Aut(A6)->Out(A6), with its complete '
                        'relative class products in the three nonzero outer cosets. '
                        'No inference to a pro-five leading term is made.'}
    HERE.joinpath('a_peripheral_a6_outer.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'], flush=True)


if __name__ == '__main__':
    main()
