#!/usr/bin/env python3
"""Actual degree-three cyclic-cover test in SL2(F3), with whole K6 corrections.

This probes only the displayed finite K3 equation.  It does not impose
simultaneous Ferrari tests or determine the full-GT character in E65.
"""
from pathlib import Path
from collections import deque
from itertools import product
from hashlib import sha256
import json
import time
from de_ferrari_a6_source_data import load_data

HERE = Path(__file__).resolve().parent


def main():
    start = time.monotonic()
    d = load_data()
    I = (1, 0, 0, 1)
    def mm(a, b):
        return tuple(v % 3 for v in (a[0]*b[0]+a[1]*b[2],
                                     a[0]*b[1]+a[1]*b[3],
                                     a[2]*b[0]+a[3]*b[2],
                                     a[2]*b[1]+a[3]*b[3]))
    G = sorted(a for a in product(range(3), repeat=4)
               if (a[0]*a[3]-a[1]*a[2]) % 3 == 1)
    ix = {a: j for j, a in enumerate(G)}
    one = ix[I]
    mult = [[ix[mm(a, b)] for b in G] for a in G]
    inverse = [ix[(a[3], -a[1] % 3, -a[2] % 3, a[0])] for a in G]
    X = ix[(1, 2, 0, 1)]
    Y = ix[(1, 0, 1, 1)]
    wone = (0, (one,)*3)
    wx = (1, (one, one, X))
    wy = (0, (Y, one, one))
    def wm(a, b):
        k, v = a
        l, w = b
        return ((k+l) % 3, tuple(mult[v[j]][w[(j+k) % 3]] for j in range(3)))
    def wi(a):
        k, v = a
        return (-k % 3, tuple(inverse[v[(j-k) % 3]] for j in range(3)))
    letters = {1: wx, -1: wi(wx), 2: wy, -2: wi(wy)}
    def ev(w):
        a = wone
        for c in w:
            a = wm(a, letters[c])
        return a
    def comm(a, b):
        return wm(wm(wm(a, b), wi(a)), wi(b))
    def ordinary(w):
        a = one
        for c in w:
            z = X if abs(c) == 1 else Y
            a = mult[a][z if c > 0 else inverse[z]]
        return a
    def c3(w):
        j, ans = 0, 0
        for c in w:
            if abs(c) == 1:
                j = (j + (1 if c > 0 else -1)) % 3
            elif j == 0:
                ans += 1 if c > 0 else -1
        assert j == 0
        return ans
    assert ev([1, 1, 1])[1][0] == X
    assert ev([2])[1][0] == Y
    assert ev([1, 2, -1])[1][0] == one
    assert ev([1, 1, 2, -1, -1])[1][0] == one
    for a in letters.values():
        assert wm(a, wi(a)) == wm(wi(a), a) == wone
    Nwords = [list(d['fword'](w)) for w in d['Nwords']]
    N = [ev(w) for w in Nwords]
    assert all(ordinary(w) == one for w in Nwords)
    vals = {}
    for i in range(97):
        for j in range(i+1, 97):
            z = comm(N[i], N[j])
            assert z[0] == 0
            a = z[1][0]
            if a != one:
                vals.setdefault(a, (i, j))
    gens = list(vals)
    expr = {one: []}
    queue = deque([one])
    while queue:
        a = queue.popleft()
        for k, b in enumerate(gens):
            ab = mult[a][b]
            if ab not in expr:
                expr[ab] = expr[a]+[k]
                queue.append(ab)
    assert len(expr) == 24
    comm_words = []
    for a in gens:
        i, j = vals[a]
        w = Nwords[i]+Nwords[j]+list(d['finv'](Nwords[i]))+list(d['finv'](Nwords[j]))
        assert ev(w)[1][0] == a and ordinary(w) == one
        comm_words.append(w)
    records = []
    base = json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    for i, rec in enumerate(base):
        f = rec['actual_commutator_word_f']
        ef = ev(f)
        assert ef[0] == 0
        target = ordinary(f)
        need = mult[inverse[ef[1][0]]][target]
        u = sum((comm_words[j] for j in expr[need]), [])
        fu = f+u
        assert ev(fu)[1][0] == target
        assert ordinary(fu) == target
        cc = c3(fu)
        assert cc % 3 == 0
        assert all(sum((1 if a > 0 else -1) for a in u if abs(a) == b) == 0
                   for b in (1, 2))
        records.append({'index': i, 'missing_coset': rec['missing_coset'],
                        'q3_f': G[target], 'q3_phi3_f_before': G[ef[1][0]],
                        'c3_before': c3(f),
                        'correction_original_N_commutator_factors':
                            [vals[gens[j]] for j in expr[need]],
                        'correction_literal_F_word': u,
                        'q3_phi3_f_after': G[ev(fu)[1][0]],
                        'c3_after': cc,
                        'whole_G6_fibre_finite_K3_equation_passes': True})
    out = {'status': 'PASS_EXACT_K3_SL23_CORRECTION_IMAGE',
           'degree_three_cover_section': ['1', 'x', 'x^2'],
           'source_x': wx, 'source_y': wy,
           'target_X': G[X], 'target_Y': G[Y],
           'actual_N_basis_rank': 97,
           'complete_original_pair_commutators_checked': 4656,
           'distinct_nonidentity_coordinate_values': len(vals),
           'q3_phi3_N_derived_image_order': len(expr),
           'q3_phi3_N_derived_image': G,
           'literal_commutator_preimages': [
               {'value': G[a], 'N_indices': vals[a], 'F_word': w}
               for a, w in zip(gens, comm_words)],
           'records': records,
           'all_24_retained_fibres_survive': len(records) == 24,
           'scope': 'Single literal K3 relation in SL2(F3); no simultaneous older-target assertion',
           'input_sha256': {n: sha256((HERE/n).read_bytes()).hexdigest()
                            for n in ('de_ferrari_a6_source_data.py',
                                      'de_ferrari_sl2_5_N.json',
                                      'de_ferrari_fibres.json')},
           'seconds': round(time.monotonic()-start, 6)}
    (HERE/'a_cm_kummer3_probe.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: v for k, v in out.items()
                      if k not in {'records', 'literal_commutator_preimages'}}, indent=2))


if __name__ == '__main__':
    main()
