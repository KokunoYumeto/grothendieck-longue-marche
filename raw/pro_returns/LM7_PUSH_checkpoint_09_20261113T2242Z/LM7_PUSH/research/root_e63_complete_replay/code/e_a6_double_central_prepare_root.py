#!/usr/bin/env python3
"""Exact central coinvariants over the old perfect A6 source residual.

The binary source kernel and its actual ten C conjugation maps determine
the quotient.  All ten literal C lifts and every central lift parameter
are retained in the subsequent full presentation calculation.
"""
from pathlib import Path
from hashlib import sha256
import struct
import json
import time
import numpy as np
from de_ferrari_two_core import rref2, solve2
from e_a6_double_kernel_prepare_root import pack
from de_a6_schreier_certificate import read_certificate

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_central_prepare_root'


def main():
    started = time.monotonic()
    files = ['e_a6_double_kernel_replay_root.npz', 'e_a6_double_kernel_replay_root.json',
             'de_a6_gl_central_prepare.npz', 'de_a6_schreier_residual_derived.bin',
             'e_a6_double_kernel_root.cpp', 'de_a6_triple_central.cpp']
    hashes = {p: sha256((HERE / p).read_bytes()).hexdigest() for p in files}
    raw = np.load(HERE / files[0])
    B, actions = raw['kernel_basis'], raw['C_actions']
    dimension = B.shape[1]
    assert B.shape[0] == 5724 and actions.shape == (10, dimension, dimension)
    differences = np.column_stack([a-np.eye(dimension, dtype=np.int64) for a in actions]) % 2
    comm_rank = len(rref2(differences)[1])
    solved = solve2(differences.T, np.zeros(differences.shape[1], dtype=np.int64))
    assert solved is not None
    Q = solved[1].T
    nc = Q.shape[0]
    assert Q.shape == (dimension-comm_rank, dimension)
    assert not np.any(Q @ differences % 2) and len(rref2(Q)[1]) == nc
    pivots = np.array(rref2(B.T)[1], dtype=np.int64)
    assert len(pivots) == dimension
    extended, piv = rref2(np.column_stack((B[pivots], np.eye(dimension, dtype=np.int64))))
    assert piv == list(range(dimension))
    inverse = extended[:, dimension:]
    assert np.array_equal(inverse @ B[pivots] % 2, np.eye(dimension, dtype=np.int64))
    projection = Q @ inverse % 2
    assert np.array_equal(projection @ B[pivots] % 2, Q)
    C = read_certificate(HERE / 'de_a6_schreier_residual_derived.bin')
    saved = np.load(HERE / 'de_a6_gl_central_prepare.npz')
    assert np.array_equal(C['original'], saved['C_original_source_permutations'])
    assert np.array_equal(raw['C_source_word_nodes'], saved['C_original_word_nodes'])
    assert np.array_equal(raw['literal_C_source_F_word_DAG'], saved['literal_F_word_DAG'])
    values = raw['C_source_values']
    assert values.shape == (10, 6, 6, 271)
    assert np.array_equal(values[..., 212:216], np.broadcast_to([1, 0, 0, 1], (10, 6, 6, 4)))
    assert not np.any(values[..., 269:271])
    with (HERE / 'e_a6_double_central_model_root.bin').open('wb') as f:
        f.write(struct.pack('<7I', 0xA62CE001, 1, 10, dimension, nc, C['degree'], 5724))
        f.write(np.asarray(pivots, dtype='<u4').tobytes())
        f.write(np.asarray(projection, dtype=np.uint8).tobytes())
        f.write(np.asarray(B.T, dtype=np.uint8).tobytes())
        for v in values:
            f.write(pack((np.arange(6), v)).astype('<u2').tobytes())
        f.write(np.asarray(C['original'], dtype='<u2').tobytes())
    source = (HERE / 'e_a6_double_kernel_root.cpp').read_text()
    core = source[source.index('constexpr int HW='):source.index('struct LiftedKernel {')]
    (HERE / 'e_a6_double_core_root.hpp').write_text('#pragma once\n#include <array>\n#include <map>\n'+core)
    # Adapt the exact retained presentation collector to the binary field.
    # Each explicit substitution below has its source-count recorded.
    cpp = (HERE / 'de_a6_triple_central.cpp').read_text()
    substitutions = [
        ('de_a6_triple_core.hpp', 'e_a6_double_core_root.hpp'),
        ('NG=10,NC=27,RC=NG+NC', f'NG=10,NC={nc},RC=NG+NC'),
        ('0xA63CE027', '0xA62CE001'),
        ('79', str(dimension)), ('Ternary', 'Binary'),
        ('if(a>2)', 'if(a>1)'),
        ('a[i]+3+sign*b[i]', 'a[i]+2+sign*b[i]'),
        ('3-cv[j]', '2-cv[j]'), ('%3', '%2'),
        ('// kernel coordinate, with the minus sign essential in characteristic3.',
         '// kernel coordinate; subtraction agrees with addition in characteristic two.')]
    changes = []
    for before, after in substitutions:
        count = cpp.count(before)
        assert count, before
        cpp = cpp.replace(before, after)
        changes.append({'before': before, 'after': after, 'occurrences': count})
    (HERE / 'e_a6_double_central_root.cpp').write_text(cpp)
    np.savez_compressed(HERE / (STEM+'.npz'), C_commutator_module=differences,
                        central_coinvariant_map=Q, kernel_ambient_pivot_rows=pivots,
                        central_map_on_ambient_pivots=projection)
    out = {'status': 'PASS_EXACT_BINARY_C_CENTRAL_COINVARIANTS',
           'kernel_dimension': dimension, 'C_commutator_image_dimension': comm_rank,
           'central_quotient_dimension': nc, 'full_original_C_generator_count': 10,
           'abelian_relation_column_count': 10+nc, 'all_generator_central_shift_freedoms': 10*nc,
           'C_lifts_are_same_saved_literal_source_words': True,
           'collector_header_is_exact_slice_of_executed_binary_source': True,
           'central_collector_exact_adaptations': changes, 'input_sha256': hashes,
           'seconds': round(time.monotonic()-started, 3)}
    (HERE / (STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    assert all(sha256((HERE / p).read_bytes()).hexdigest() == v for p, v in hashes.items())
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()
