#!/usr/bin/env python3
"""Literal T23 arrows to the signed quotient and binary affine target."""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_two_model import FerrariTwo

HERE = Path(__file__).resolve().parent


def main():
    started = time.monotonic()
    names = ['de_ferrari_degree6_kernel.py', 'de_ferrari_degree4_lift.py',
             'de_ferrari_two_model.py', 'e_a6_double_target_quotient_root.json',
             'e_a6_double_target_quotient_root.npz', 'e_a6_double_model_root.py']
    hashes = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    F, B, H = FerrariTwo(6), FerrariTwo(2), FerrariA6Double()
    small = np.load(HERE/'e_a6_double_target_quotient_root.npz')
    affine = small['signed_to_affine_two_values']
    table = small['signed_Cayley_table']
    # Automorphism indices are local to each model instance. Reconstruct
    # the entire literal Cayley graph in this instance before comparing
    # the saved arrays or looking up any newly evaluated word.
    edges = small['quotient_generator_permutations'].T
    seen, elements, image_values = {tuple(B.one):0}, [B.one], [0]
    for i, g in enumerate(elements):
        for j, h in enumerate((B.a, B.b, B.c)):
            gh = B.mul(g,h)
            key, value = tuple(gh), int(edges[image_values[i],j])
            ix = seen.get(key)
            if ix is None:
                seen[key] = len(elements)
                elements.append(gh)
                image_values.append(value)
            else:
                assert image_values[ix] == value
    assert len(elements) == 1536
    assert np.array_equal(np.array(elements),small['binary_class_two_elements'])
    assert np.array_equal(image_values,small['binary_to_signed_values'])
    values = {tuple(g):int(q) for g,q in zip(elements,image_values)}
    fg, bg, hg = [F.a,F.b,F.c], [B.a,B.b,B.c], [H.a,H.b,H.c]
    for f,b,h in zip(fg,bg,hg):
        assert np.array_equal(F.to_lower(f,B),b)
        assert np.array_equal(affine[values[tuple(b)]],H.project_affine2(h))
    fs, bs, hs = fg+[F.inv(g) for g in fg], bg+[B.inv(g) for g in bg], hg+[H.inv(g) for g in hg]
    for f,b,h in zip(fs,bs,hs):
        for g,c,k in zip(fs,bs,hs):
            actual = F.to_lower(F.mul(f,g),B)
            expected = B.mul(b,c)
            assert np.array_equal(actual,expected)
            value = values[tuple(actual)]
            assert value == table[values[tuple(b)],values[tuple(c)]]
            assert np.array_equal(affine[value],H.project_affine2(H.mul(h,k)))
    for f,b,h in zip(F.x,B.x,H.x):
        assert np.array_equal(F.to_lower(f,B),b)
        assert np.array_equal(affine[values[tuple(b)]],H.project_affine2(h))
    for f,b,h in zip(F.y,B.y,H.y):
        assert np.array_equal(F.to_lower(f,B),b)
        assert np.array_equal(affine[values[tuple(b)]],H.project_affine2(h))
    result = {
        'status':'PASS_LITERAL_T23_TO_SIGNED_AND_AFFINE_TWO',
        'binary_arrow':'Degree-six Magnus quotient to degree-two truncation, then the saved1536-element map to S_L',
        'all3_braid_generator_arrows_verified':True,
        'all36_signed_generator_products_verified':True,
        'all6_pure_substitution_pairs_verified':True,
        'all1536_binary_elements_reconstructed_in_current_model':True,
        'all4608_positive_Cayley_edges_replayed_in_current_model':True,
        'actual_solvable_quotient_order':96,
        'affine_values_agree_with_double_A6_coordinates':True,
        'input_sha256':hashes, 'seconds':round(time.monotonic()-started,3),
    }
    (HERE/'e_a6_double_target_old_maps_root.json').write_text(json.dumps(result,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n,h in hashes.items())
    print(json.dumps(result,indent=2),flush=True)


if __name__ == '__main__':
    main()
