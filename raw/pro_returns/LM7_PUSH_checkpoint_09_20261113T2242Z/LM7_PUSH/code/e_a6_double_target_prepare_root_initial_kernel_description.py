#!/usr/bin/env python3
"""Actual joint target after killing U^53 times SL2(F5)^19, U=SL2(F9).

The old781-point A6/signed quotient is retained literally.  The424-point
block records the binary central Nielsen cross term, and the last four
points record the actual global affine-two character.  On the quotient
by the displayed perfect free subgroup this permutation map is faithful:
the first530 points retain p and alpha modulo inner automorphisms, the
next251 retain the signed quotient, the424 retain E and M, and the last
four retain t.  An inner alpha has exactly its unique inner lift to U;
these and the two free translations are precisely the killed factors.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_sl2_5_solvable import quotient_permutation

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_target_root'
DEGREE = 1209


def permutation(H, L, g, l):
    old = np.asarray(H.old.permutation(H.project_a6(g), True).array_form,
                     dtype=np.int64)
    signed = np.asarray(quotient_permutation(L, l).array_form, dtype=np.int64)
    out = list(old) + list(530 + signed)
    p = g[H.ps]
    E = g[H.es].reshape(53, 2)
    M = g[H.ms].reshape(2, 2)
    assert (M[0, 0]*M[1, 1] - M[0, 1]*M[1, 0]) % 2 == 1
    Mi = np.array([[M[1, 1], M[0, 1]], [M[1, 0], M[0, 0]]]) % 2
    points = list(product(range(2), repeat=2))
    index = {v:i for i, v in enumerate(points)}
    for j in range(53):
        for z in range(2):
            for t in points:
                v = Mi @ np.array(t) % 2
                zz = int(z + E[j] @ v) % 2
                out.append(781 + 8*int(p[j]) + 4*zz + index[tuple(v)])
    gi = H.inv(g)
    Mi, ti = gi[H.ms].reshape(2, 2), gi[H.ts]
    out.extend(1205 + index[tuple((Mi @ np.array(v) + ti) % 2)] for v in points)
    ans = np.asarray(out, dtype=np.uint16)
    assert np.array_equal(np.sort(ans), np.arange(DEGREE))
    return ans


def main():
    started = time.monotonic()
    names = ['e_a6_double_model_root.py', 'e_a6_double_model_root.npz',
             'de_a6_gl_target_prepare.npz', 'de_ferrari_sl2_5_solvable.py',
             'e_a6_double_cover_root.npz', 'de_ferrari_a6_kernels.npz']
    hashes = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    H, L = FerrariA6Double(), FerrariSL2Five()
    hg, lg = [H.a, H.b, H.c], [L.a, L.b, L.c]
    arrays = [permutation(H, L, g, l) for g, l in zip(hg, lg)]
    saved = np.load(HERE/'de_a6_gl_target_prepare.npz')
    for label, p in zip(['a', 'b', 'c'], arrays):
        assert np.array_equal(p[:781], saved[label])
    gs, ls = hg + [H.inv(g) for g in hg], lg + [L.inv(g) for g in lg]
    for g, l in zip(gs, ls):
        p = permutation(H, L, g, l)
        for h, m in zip(gs, ls):
            q = permutation(H, L, h, m)
            assert np.array_equal(q[p], permutation(H, L, H.mul(g, h), L.mul(l, m)))
    a, b, c = arrays
    assert np.array_equal(a[b[a]], b[a[b]])
    assert np.array_equal(b[c[b]], c[b[c]])
    assert np.array_equal(a[c], c[a])
    with (HERE/(STEM+'.input')).open('w') as out:
        out.write(f'{DEGREE} 3\n')
        for p in arrays:
            out.write(' '.join(map(str, p))+'\n')
    np.savez_compressed(HERE/'e_a6_double_target_prepare_root.npz', a=a, b=b, c=c)
    result = {
        'status':'PASS_EXACT_JOINT_DOUBLE_A6_SIGNED_TARGET_QUOTIENT',
        'degree':DEGREE, 'retained_old_quotient_degree':781,
        'central_binary_cross_block_degree':424, 'affine_two_block_degree':4,
        'all36_literal_generator_product_comparisons':True,
        'all_braid_relations_verified':True,
        'actual_perfect_free_kernel':'SL2(F9)^53 times SL2(F5)^19',
        'old_quotient_original_arrays_retained_literally':True,
        'complete_order_and_derived_series_are_separate_certificates':True,
        'input_sha256':hashes, 'seconds':round(time.monotonic()-started, 3),
    }
    (HERE/'e_a6_double_target_prepare_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
