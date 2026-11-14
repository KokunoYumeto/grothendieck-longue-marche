#!/usr/bin/env python3
"""Literal joint A6/A5/E62 base, seeded by certified original B words."""
from pathlib import Path
from hashlib import sha256
import json
import struct
import time
import numpy as np
from de_a6_schreier_certificate import read_certificate, verify_words
from de_a6_triple_base_prepare import evaluate

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_E62_base_prepare_root'


def main():
    started = time.monotonic()
    names = ['de_a6_a5_common_source.bin', 'de_a6_a5_common_source.npz',
             'a_cm_gl23_joint.npz', 'de_a6_triple_base.cpp',
             'de_a6_schreier.cpp']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    old = read_certificate(HERE / names[0])
    verify_words(old)
    old_arrays = np.load(HERE / names[1])
    assert np.array_equal(old['original'], np.array([old_arrays['s'], old_arrays['r']]))
    extra = np.load(HERE / names[2])['joint_B_generators']
    assert old['degree'] == 11010 and extra.shape == (2, 4764)
    images = evaluate(old['nodes'], extra, old['words'])
    original = np.column_stack((old['original'], old['degree'] + extra)).astype(np.uint16)
    strong = np.column_stack((old['strong'], old['degree'] +
                              np.array([images[int(w)] for w in old['words']]))).astype(np.uint16)
    n = original.shape[1]
    verify_words({**old, 'degree': n, 'original': original, 'strong': strong})
    with (HERE / 'e_a6_double_E62_base_seed_root.bin').open('wb') as stream:
        def integer(v):
            stream.write(struct.pack('<I', int(v)))
        integer(0x41365354)
        integer(n)
        integer(0)
        integer(2)
        stream.write(original.astype('<u2').tobytes())
        integer(len(old['base']))
        for b in old['base']:
            integer(b)
        integer(len(strong))
        for w, depth, p in zip(old['words'], old['depths'], strong):
            integer(w)
            integer(depth)
            stream.write(p.astype('<u2').tobytes())
        integer(len(old['nodes']))
        stream.write(np.asarray(old['nodes'], dtype='<u4').tobytes())
    np.savez_compressed(HERE / (STEM + '.npz'),
                        s=original[0], r=original[1],
                        old_base_points=np.arange(11010),
                        E62_points=np.arange(11010, n),
                        seed_original_word_nodes=old['words'])
    result = {'status': 'PASS_LITERAL_A6_A5_E62_BASE_SEED',
              'old_base_degree': 11010, 'E62_degree': 4764, 'joint_degree': n,
              'all_seed_strong_words_replayed_in_both_actual_sources': True,
              'seed_strong_generator_count': len(strong),
              'seed_is_not_a_complete_joint_certificate': True,
              'input_sha256': hashes,
              'seconds': round(time.monotonic() - started, 6)}
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / name).read_bytes()).hexdigest() == h
               for name, h in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
