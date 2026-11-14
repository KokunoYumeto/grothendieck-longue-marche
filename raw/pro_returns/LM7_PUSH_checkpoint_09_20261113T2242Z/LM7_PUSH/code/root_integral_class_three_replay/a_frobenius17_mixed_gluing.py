#!/usr/bin/env python3
"""Exact mod-three mixed central gluing maps with all W/D6 freedoms retained.

This is a finite computation on the actual module from A.38.  The two
unknown degree-three mixed coefficients and every degree-four/five
source correction are retained.  The program does not assign those
coefficients to the arithmetic Frobenius or assert integral local
cuspidality of an arbitrary mod-three source parameter.
"""
from pathlib import Path
from itertools import product
import contextlib
import importlib.util
import io
import json
import argparse
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ga', HERE/'a_ihara_gamma2_action.py')
ga = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(ga)
g, f = ga.g, ga.f
cert = np.load(HERE/'a_ihara_gamma2_action_certificate.npz')
SMALL = {k: cert['small_'+k].astype(np.int64) for k in ('m', 'n', 'c')}
ACTION = {k: cert['action_'+k].astype(np.int64) for k in ('m', 'n', 'c', 't')}
I55 = np.eye(55, dtype=np.int64)
IL = np.eye(375, dtype=np.int64)
eo = np.zeros(10, dtype=np.int64)
eo[6] = 1
jt = np.stack([np.array([eo[i]*(j==k)-eo[j]*(i==k)
                        for i, j in ga.PAIRS], dtype=np.int64)
               for k in range(10)], axis=1) % 3
SMALL['t'] = ga.automorphism(np.eye(10, dtype=np.int64), jt)
assert np.array_equal(ga.gamma2_action(SMALL['t']), ACTION['t'])

degree_cache = {}
action_cache = {I55.astype(np.int8).tobytes(): IL}
for name in SMALL:
    action_cache[SMALL[name].astype(np.int8).tobytes()] = ACTION[name]


def action(s):
    key = s.astype(np.int8).tobytes()
    if key in action_cache:
        return action_cache[key]
    a, j = s[:10, :10], s[10:, :10]
    akey = a.astype(np.int8).tobytes()
    if akey not in degree_cache:
        degree_cache[akey] = ga.degree3(a)
    tensor = np.einsum('kab,ai,bj->kij', ga.TRIPLE, j, a, optimize=True) % 3
    cross = np.stack([tensor[:, i, j]-tensor[:, j, i]
                      for i, j in ga.PAIRS], axis=1) % 3
    ans = np.block([[f.exterior(a), np.zeros((45, 330), dtype=np.int64)],
                    [cross, degree_cache[akey]]]) % 3
    action_cache[key] = ans
    return ans


def apply(s, d):
    return action(s) @ d % 3


def multiply(left, right):
    a, da = left
    b, db = right
    return ga.mm(a, b), (da+apply(a, db)) % 3


def inverse(pair):
    a, da = pair
    ai = ga.inverse(a)
    return ai, -apply(ai, da) % 3


def power(pair, n):
    if n < 0:
        return power(inverse(pair), -n)
    out = I55, np.zeros_like(pair[1])
    while n:
        if n & 1:
            out = multiply(out, pair)
        pair = multiply(pair, pair)
        n //= 2
    return out


def commutator(left, right):
    a, da = left
    b, db = right
    ai, bi = ga.inverse(a), ga.inverse(b)
    conjugate = ga.mm(ga.mm(a, b), ai)
    comm = ga.mm(conjugate, bi)
    delta = (da-apply(conjugate, da)+apply(a, db)-apply(comm, db)) % 3
    return comm, delta


def symmetric(pair):
    s, d = pair
    conjugate = ga.mm(ga.mm(SMALL['c'], s), SMALL['c'])
    cd = ACTION['c'] @ d % 3
    exact = power(multiply(pair, (conjugate, cd)), 2)
    expected = 2*(d+cd) % 3
    assert np.array_equal(exact[1], expected)
    assert np.array_equal(ga.mm(SMALL['c'], exact[0]),
                          ga.mm(exact[0], SMALL['c']))
    assert np.array_equal(ACTION['c'] @ exact[1] % 3, exact[1])
    return exact


def is_lyndon(w):
    return all(w < w[i:]+w[:i] for i in range(1, len(w)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--local-conjugator', action='store_true')
    args = parser.parse_args()
    c = ACTION['c']
    nc = ga.mm(ACTION['n'], c)
    _, mpivots = ga.columns((IL+c)[:45, :45] % 3)
    _, npivots = ga.columns((IL-nc)[:45, :45] % 3)
    assert len(mpivots) == 21 and len(npivots) == 24
    bm = np.hstack(((IL+c)[:, mpivots], np.zeros((375, 24), dtype=np.int64))) % 3
    bn = np.hstack((np.zeros((375, 21), dtype=np.int64), (IL-nc)[:, npivots])) % 3
    bt = np.zeros((375, 45), dtype=np.int64)
    local_h = np.zeros((375, 45), dtype=np.int64)
    if args.local_conjugator:
        bm = np.hstack((bm, np.zeros((375, 21), dtype=np.int64)))
        bn = np.hstack((bn, np.zeros((375, 21), dtype=np.int64)))
        local_h = np.hstack((local_h, (IL+c)[:, mpivots])) % 3
        bt = (ACTION['t']-IL) @ local_h % 3
    gen = [(SMALL['m'], bm), (SMALL['n'], bn), (SMALL['t'], bt)]
    cache = {(i,): p for i, p in enumerate(gen)}

    def lyndon(w):
        if w in cache:
            return cache[w]
        # First Lyndon suffix is the longest proper Lyndon suffix.
        cut = next(i for i in range(1, len(w)) if is_lyndon(w[i:]))
        pair = commutator(lyndon(w[:cut]), lyndon(w[cut:]))
        cache[w] = pair
        return pair

    # The known source term is m^6 [n,[n,m]] [t,[t,m]]^2.
    base = multiply(power(gen[0], 6), lyndon((0, 1, 1)))
    base = multiply(base, power(lyndon((0, 2, 2)), 2))
    base = symmetric(base)
    if args.local_conjugator:
        base = base[0], (base[1]-(action(base[0])-IL) @ local_h) % 3
    top = base[1][:45]
    lower_kernel = g.kernel(top)
    print('Normalized class-two source parameters:', 45,
          'local conjugator parameters:', 21 if args.local_conjugator else 0)
    print('Local class-two norm-Frobenius rank modulo3:', f.rank(top))
    print('Kernel dimension:', lower_kernel.shape[1])

    # Quotient the c-fixed M3 target by the exact global M3 restriction image.
    old = json.loads((HERE/'a_frobenius17_eval_m3.json').read_text())
    global_image = cert['A7_to_Schreier_M3'].astype(np.int64) @ np.array(
        old['evaluation_image_mod3_basis'], dtype=np.int64) % 3
    assert f.rank(global_image) == 15
    pc = 2*(np.eye(330, dtype=np.int64)+c[45:, 45:]) % 3
    qraw = g.kernel(global_image.T).T @ pc % 3
    quotient = ga.columns(qraw.T)[0].T
    assert quotient.shape[0] == 149
    assert not np.any(quotient @ global_image % 3)
    known_map = quotient @ base[1][45:] @ lower_kernel % 3
    print('Known cubic-term gluing rank on the necessary local kernel:', f.rank(known_map))

    labels = [(0, 1, 2), (0, 2, 1)]
    labels += [w for degree in (4, 5)
               for w in product(range(3), repeat=degree) if is_lyndon(w)]
    assert len(labels) == 68
    maps, actions, degree_rows = [], [], []
    for w in labels:
        s, d = symmetric(lyndon(w))
        assert not np.any(d[:45])
        assert np.array_equal(s[:10, :10], np.eye(10, dtype=np.int64))
        maps.append(quotient @ d[45:] @ lower_kernel % 3)
        actions.append(s[10:, :10].reshape(-1))
        degree_rows.append(len(w))
    flat = np.stack([a.reshape(-1) for a in maps], axis=1)
    geometric = np.stack(actions, axis=1)
    for degree in (3, 4, 5):
        ids = [i for i, d in enumerate(degree_rows) if d == degree]
        row_rank = f.rank(np.vstack([maps[i] for i in ids]))
        col_rank = f.rank(flat[:, ids])
        action_rank = f.rank(geometric[:, ids])
        print('Unknown degree', degree, ': source directions', len(ids),
              'gluing-map span', col_rank, 'affected-source rank', row_rank,
              'actual intrinsic-action rank', action_rank)
    invisible = flat @ g.kernel(geometric) % 3
    print('Unknown gluing-map span invisible in actual N/K action:', f.rank(invisible))
    safe = g.kernel(np.vstack(maps))
    print('Necessary local source directions killing every retained W uncertainty:', safe.shape[1])
    print('Known gluing rank on this source subspace:', f.rank(known_map @ safe % 3))

    # Record the earliest surviving map and its actual tensor source parameters.
    nonzero = [i for i, a in enumerate(maps) if np.any(a)]
    print('Nonzero unknown directions:', [list(labels[i]) for i in nonzero])
    additional = {}
    if args.local_conjugator:
        assert lower_kernel.shape == (66, 66) and np.array_equal(lower_kernel, np.eye(66, dtype=np.int64))
        independent = ga.columns(flat)[1]
        assert len(independent) == 3
        print('Independent unknown-word map indices:', independent,
              'words:', [list(labels[i]) for i in independent])
        cases = []
        for coeffs in product(range(3), repeat=3):
            evaluated = known_map.copy()
            for a, ii in zip(coeffs, independent):
                evaluated += a*maps[ii]
            evaluated %= 3
            source, conjugator = evaluated[:, :45], evaluated[:, 45:]
            rh = f.rank(conjugator)
            rjoint = f.rank(evaluated)
            rsource = f.rank(source)
            cases.append({'coefficients': list(coeffs), 'local_conjugator_rank': rh,
                          'source_rank': rsource, 'combined_rank': rjoint,
                          'source_rank_mod_local_conjugators': rjoint-rh})
        hist = {}
        for row in cases:
            key = str((row['local_conjugator_rank'], row['combined_rank'],
                       row['source_rank_mod_local_conjugators']))
            hist[key] = hist.get(key, 0)+1
        print('All27 coefficients: histogram (local conjugator, joint, residual source) ranks:', hist)
        print('Source-map ranks over all27 coefficients:', sorted(set(row['source_rank'] for row in cases)))
        all_h = np.hstack([known_map[:, 45:]]+[a[:, 45:] for a in maps])
        hquotient = g.kernel(all_h.T).T
        print('Rank of union of all local-conjugator maps:', f.rank(all_h))
        surviving_known = hquotient @ known_map[:, :45] % 3
        surviving_unknown = [hquotient @ a[:, :45] % 3 for a in maps]
        universal_sources = g.kernel(np.vstack(surviving_unknown))
        print('Source directions killing unknowns after all local conjugators:', universal_sources.shape[1])
        print('Known gluing rank on this universal source subspace:',
              f.rank(surviving_known @ universal_sources % 3))
        additional = {'independent_unknown_indices': independent,
                      'coefficient_cases': cases,
                      'union_local_conjugator_rank': f.rank(all_h),
                      'universal_source_dimension': universal_sources.shape[1],
                      'universal_known_rank': f.rank(surviving_known @ universal_sources % 3)}
    prefix = 'a_frobenius17_mixed_gluing' + ('_local' if args.local_conjugator else '')
    np.savez_compressed(HERE/(prefix+'_certificate.npz'),
                        source_m=bm.astype(np.int8), source_n=bn.astype(np.int8),
                        class2_local_map=top.astype(np.int8),
                        necessary_local_kernel=lower_kernel.astype(np.int8),
                        target_quotient=quotient.astype(np.int8),
                        known_gluing=known_map.astype(np.int8),
                        unknown_gluing=np.stack(maps).astype(np.int8),
                        unknown_intrinsic_action=geometric.astype(np.int8),
                        uncertainty_annihilator=safe.astype(np.int8))
    result = {'letters': ['m', 'n', 't'], 'unknown_lyndon_words': [list(w) for w in labels],
              'nonzero_unknown_indices': nonzero,
              'class2_local_rank': f.rank(top),
              'necessary_local_kernel_dimension': lower_kernel.shape[1],
              'known_gluing_rank': f.rank(known_map),
              'unknown_gluing_span_rank': f.rank(flat),
              'unknown_gluing_rank_invisible_in_intrinsic_action': f.rank(invisible),
              'uncertainty_annihilator_dimension': safe.shape[1],
              'known_rank_on_uncertainty_annihilator': f.rank(known_map @ safe % 3),
              'scope': 'Necessary mod3 local kernel only; no integral local-cuspidality or arithmetic W coefficients assigned.'}
    result.update(additional)
    (HERE/(prefix+'.json')).write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: all degree3/4/5 source freedoms retained through the actual maps.')


if __name__ == '__main__':
    main()
