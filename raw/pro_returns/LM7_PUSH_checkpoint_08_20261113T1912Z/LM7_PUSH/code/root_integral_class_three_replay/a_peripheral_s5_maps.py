#!/usr/bin/env python3
"""Actual twisted-wreath embeddings and boundary transport over S3/S4.

For every subgroup C containing a fixed transposition subgroup D*, and
every character C->C2 extending its nontrivial character, verify the
explicit embedding E(C,epsilon_C)->E(D*,epsilon).  Test the full local
power/conjugator comparison on actual wreath elements and their cycle
products.  All coefficients are literal permutations.
"""

from collections import deque
from itertools import permutations
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('finite_count', HERE/'a_peripheral_count.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def all_subgroups(G):
    one = frozenset([G.one])
    data, todo = {one: []}, deque([one])
    while todo:
        H = todo.popleft()
        for g in range(G.size):
            if g in H:
                continue
            gens = data[H]+[g]
            J = G.generated(gens)
            if J not in data:
                data[J] = gens
                todo.append(J)
    return data


def cosets(D, C):
    cs, index, reps = [], {}, []
    for d in range(D.size):
        if d in index:
            continue
        c = frozenset(D.mul[a][d] for a in C)
        index.update({a: len(cs) for a in c})
        cs.append(c)
        reps.append(d)
    action = [[index[D.mul[t][d]] for d in range(D.size)] for t in reps]
    transition = [[D.mul[D.mul[t][d]][D.inv[reps[action[i][d]]]]
                   for d in range(D.size)] for i, t in enumerate(reps)]
    assert all(k in C for row in transition for k in row)
    return {'cosets': cs, 'index': index, 'reps': reps,
            'action': action, 'transition': transition}


def main():
    S = module.Group('S5', permutations(range(5)), module.perm_mul, tuple(range(5)))
    parity = [module.parity(g) for g in S.elements]
    fibers = [[g for g in range(S.size) if parity[g] == k] for k in range(2)]
    even = fibers[0]
    s = S.index[(1, 0, 2, 3, 4)]
    tau = [S.conjugate(s, g) for g in range(S.size)]
    class_of = {g: {S.conjugate(h, g) for h in even} for g in range(S.size)}
    records = []
    for degree in (3, 4):
        D = module.Group('S'+str(degree), permutations(range(degree)),
                         module.perm_mul, tuple(range(degree)))
        t = D.index[(1, 0)+tuple(range(2, degree))]
        Dstar = D.generated([t])
        outer = {D.one: 0, t: 1}
        small = cosets(D, Dstar)
        bstar = [[outer[k] for k in row] for row in small['transition']]
        lattice = all_subgroups(D)
        embedding_cases = boundary_cases = nonempty_cases = 0
        case_data = []

        def mul(u, v, space):
            z, d = u
            w, e = v
            return (tuple(S.mul[z[i]][w[space['action'][i][d]]]
                          for i in range(len(z))), D.mul[d][e])

        def inv(u, space):
            z, d = u
            e = D.inv[d]
            return tuple(S.inv[z[space['action'][i][e]]] for i in range(len(z))), e

        def power(u, k, space):
            out = ((S.one,)*len(space['reps']), D.one)
            while k:
                if k & 1:
                    out = mul(out, u, space)
                u = mul(u, u, space)
                k >>= 1
            return out

        def conjugate(h, u, space):
            return mul(mul(h, u, space), inv(h, space), space)

        def element(d, b, seed):
            return tuple(fibers[b[i][d]][(seed+7*i) % 60]
                         for i in range(len(b))), d

        def orbits(space, d):
            unseen, result = set(range(len(space['reps']))), []
            while unseen:
                start = min(unseen)
                orbit, a = [], start
                while a in unseen:
                    unseen.remove(a)
                    orbit.append(a)
                    a = space['action'][a][d]
                assert a == start
                result.append(orbit)
            return result

        for C in sorted((C for C in lattice if Dstar <= C),
                        key=lambda C: (len(C), sorted(C))):
            chars = []
            for H in lattice:
                if H <= C and 2*len(H) == len(C) and t not in H:
                    # Index two is normal; retain the literal character.
                    char = {g: int(g not in H) for g in C}
                    assert all(char[D.mul[a][b]] == (char[a]+char[b]) % 2
                               for a in C for b in C)
                    chars.append(char)
            large = cosets(D, C)
            projection = [large['index'][t0] for t0 in small['reps']]
            for eps in chars:
                bC = [[eps[k] for k in row] for row in large['transition']]
                gauge = [eps[D.mul[t0][D.inv[large['reps'][projection[i]]]]]
                         for i, t0 in enumerate(small['reps'])]
                assert all(bstar[i][d] == (gauge[i]+bC[projection[i]][d]
                              +gauge[small['action'][i][d]]) % 2
                           for i in range(len(gauge)) for d in range(D.size))

                def embed(u):
                    z, d = u
                    return (tuple(S.mul[S.mul[s if gauge[i] else S.one][z[projection[i]]]]
                                  [s if gauge[small['action'][i][d]] else S.one]
                                  for i in range(len(gauge))), d)

                for d in range(D.size):
                    for e in range(D.size):
                        u, v = element(d, bC, 3+d), element(e, bC, 17+e)
                        assert embed(mul(u, v, large)) == mul(embed(u), embed(v), small)
                        embedding_cases += 1

                def allowed(X, origin):
                    d = X[1]
                    delta = next(o for o in orbits(large, d) if origin in o)
                    e = len(delta)
                    sign = 0
                    a = origin
                    for _ in range(e):
                        sign ^= bC[a][d]
                        a = large['action'][a][d]
                    answer = set(fibers[sign])
                    for gamma in orbits(small, d):
                        positions = [w for w in gamma if projection[w] == origin]
                        if not positions:
                            continue
                        w = min(positions)
                        r = len(gamma)//e
                        assert len(gamma) == r*e
                        wanted = class_of[power(X, len(gamma), small)[0][w]]
                        answer = {a for a in answer
                                  if (tau[S.power(a, r)] if gauge[w] else S.power(a, r)) in wanted}
                    return answer

                # Taking X in the actual intermediate image guarantees
                # a nonempty original boundary set; an independently
                # chosen H includes every permitted parity transport.
                local_records = []
                for d in range(D.size):
                    X = embed(element(d, bC, 9+d))
                    h = (5*d+1) % D.size
                    H = element(h, bstar, 23+d)
                    for lam in (1, 7, 11):
                        Xnew = conjugate(H, power(X, lam, small), small)
                        for delta in orbits(large, Xnew[1]):
                            origin_new = min(delta)
                            origin_old = large['action'][origin_new][h]
                            T = allowed(X, origin_old)
                            Tnew = allowed(Xnew, origin_new)
                            flip = bC[origin_new][h]
                            expected = {tau[S.power(a, lam)] if flip else S.power(a, lam)
                                        for a in T}
                            assert Tnew == expected
                            boundary_cases += 1
                            nonempty_cases += bool(T)
                            local_records.append({'d': d, 'h': h, 'lambda': lam,
                                                  'new_origin': origin_new,
                                                  'old_origin': origin_old,
                                                  'outer_flip': flip,
                                                  'old_allowed': sorted(T),
                                                  'new_allowed': sorted(Tnew)})
                case_data.append({'C': sorted(C), 'character': [[g, eps[g]] for g in sorted(C)],
                                  'small_to_large_cosets': projection,
                                  'embedding_gauge': gauge,
                                  'boundary_checks': local_records})
        print(D.name, 'PASS:', len(case_data), 'character extensions,',
              embedding_cases, 'literal multiplication comparisons,',
              boundary_cases, 'boundary transport comparisons,', nonempty_cases, 'nonempty')
        assert boundary_cases == nonempty_cases
        records.append({'base': D.name, 'elements': D.elements,
                        'Dstar': sorted(Dstar), 'small_coset_representatives': small['reps'],
                        'embedding_comparisons': embedding_cases,
                        'boundary_comparisons': boundary_cases,
                        'cases': case_data})

    payload = {'status': 'PASS_TWISTED_WREATH_EXACT_MAPS', 'cases': records,
               'scope': 'Actual subgroup, character, embedding, and local-cycle maps over S3/S4. '
                        'The general source-count and normalizer comparison is proved separately.'}
    HERE.joinpath('a_peripheral_s5_maps.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()
