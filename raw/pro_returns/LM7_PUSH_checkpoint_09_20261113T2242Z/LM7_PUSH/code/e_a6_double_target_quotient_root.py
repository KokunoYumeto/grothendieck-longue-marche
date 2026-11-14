#!/usr/bin/env python3
"""Actual S_L quotient and its affine-two map for the new binary target.

The old signed target map is retained on the literal three braid words.
All1536 elements and all4608 positive Cayley edges of the binary class-two
target are replayed.  This also proves that the four-point affine map of
the double A6 target factors through S_L by the printed value table.
Perfection of its large target kernel is a separate complete certificate.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_two_model import FerrariTwo

HERE = Path(__file__).resolve().parent


def main():
    started = time.monotonic()
    names = ['de_ferrari_sl2_5_solvable.json',
             'e_a6_double_target_prepare_root.npz',
             'e_a6_double_model_root.py', 'de_ferrari_two_model.py']
    hashes = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    signed = json.loads((HERE/names[0]).read_text())
    assert signed['maximal_solvable_quotient_order'] == 96
    assert signed['binary_factor_degree'] == 2
    edges = np.asarray(signed['solvable_quotient_cayley_table_generators'], dtype=np.int64)
    words = signed['solvable_quotient_representative_B4_words']
    table = np.empty((96, 96), dtype=np.int64)
    for j, word in enumerate(words):
        v = np.arange(96, dtype=np.int64)
        for a in word:
            v = edges[v, a-1]
        table[:, j] = v
    assert np.array_equal(table[0], np.arange(96))
    assert np.array_equal(table[:, 0], np.arange(96))
    inverse = np.array([np.flatnonzero(table[g] == 0)[0] for g in range(96)])
    assert all(np.array_equal(table[table[i], j], table[i, table[:, j]])
               for i in range(96) for j in range(96))

    def comm(a, b):
        return int(table[table[table[a, b], inverse[a]], inverse[b]])

    def close(generators):
        result, queue = {0}, [0]
        for a in queue:
            for b in generators:
                c = int(table[a, b])
                if c not in result:
                    result.add(c)
                    queue.append(c)
        return result

    current = close(edges[0])
    assert len(current) == 96
    orders, derived = [96], [sorted(current)]
    for _ in range(8):
        generators = {comm(a, b) for a in current for b in current}
        current = close(generators)
        orders.append(len(current))
        derived.append(sorted(current))
        if len(current) == 1:
            break
    else:
        raise AssertionError('Displayed S_L table did not have a soluble derived series.')

    F = FerrariTwo(2)
    seen, elements, values = {tuple(F.one):0}, [F.one], [0]
    for i, g in enumerate(elements):
        for j, h in enumerate((F.a, F.b, F.c)):
            gh = F.mul(g, h)
            key, value = tuple(gh), int(edges[values[i], j])
            ix = seen.get(key)
            if ix is None:
                seen[key] = len(elements)
                elements.append(gh)
                values.append(value)
            else:
                assert values[ix] == value
    assert len(elements) == 1536 and set(values) == set(range(96))
    affine = np.full((96, 6), -1, dtype=np.int64)
    for element, value in zip(elements, values):
        actual = F.project(element)
        if affine[value, 0] < 0:
            affine[value] = actual
        else:
            assert np.array_equal(affine[value], actual)
    assert len({tuple(v) for v in affine}) == 24
    for a in range(96):
        A, v = affine[a, :4].reshape(2, 2), affine[a, 4:]
        for b in range(96):
            B, w = affine[b, :4].reshape(2, 2), affine[b, 4:]
            expected = np.r_[(A @ B % 2).ravel(), (v + A @ w) % 2]
            assert np.array_equal(affine[table[a, b]], expected)
    H = FerrariA6Double()
    prepared = np.load(HERE/names[1])
    points = list(product(range(2), repeat=2))
    point_index = {v:i for i, v in enumerate(points)}
    for j, g in enumerate((H.a, H.b, H.c)):
        assert np.array_equal(H.project_affine2(g), affine[edges[0, j]])
        gi = H.inv(g)
        M, t = gi[H.ms].reshape(2, 2), gi[H.ts]
        p = np.array([point_index[tuple((M @ np.array(v) + t) % 2)] for v in points])
        assert np.array_equal(p, prepared[['a', 'b', 'c'][j]][1205:]-1205)
    result = {
        'status':'PASS_LITERAL_SIGNED_SOLVABLE_AND_AFFINE_TWO_MAPS',
        'specified_solvable_quotient_order':96,
        'small_complete_derived_orders':orders,
        'small_complete_derived_indices':[96//n for n in orders],
        'all9216_table_associativity_vectors_checked':True,
        'all1536_binary_class_two_elements_replayed':True,
        'all4608_binary_class_two_positive_edges_replayed':True,
        'affine_two_value_map_has_image_order':24,
        'all9216_affine_value_products_checked':True,
        'affine_map_is_literal_last_four_point_block':True,
        'large_kernel_perfection_not_yet_asserted':True,
        'input_sha256':hashes, 'seconds':round(time.monotonic()-started, 3),
    }
    np.savez_compressed(HERE/'e_a6_double_target_quotient_root.npz',
        signed_Cayley_table=table, signed_inverse=inverse,
        quotient_generator_permutations=edges.T.astype(np.uint16),
        binary_class_two_elements=np.array(elements), binary_to_signed_values=np.array(values),
        signed_to_affine_two_values=affine,
        **{f'derived_elements_{i}':np.array(s) for i, s in enumerate(derived)})
    (HERE/'e_a6_double_target_quotient_root.json').write_text(json.dumps(result, indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
