#!/usr/bin/env python3
"""Export the literal double-A6 source over the unchanged old A6 source.

All pure evaluations have identity affine-two image.  The packed model
therefore retains the exact restriction (p, alpha, E, k); its multiplication
is the restriction of the full 271-coordinate holomorph, checked below.
"""
from pathlib import Path
from hashlib import sha256
import struct
import json
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_schreier_certificate import read_certificate, verify_words

HERE = Path(__file__).resolve().parent
WIDTH = 6 + 36*212
KERNEL = 36*159
STEM = 'e_a6_double_kernel_prepare_root'


def pack(e):
    p, h = e
    h = np.asarray(h).reshape(36, 271)
    assert np.array_equal(h[:, 212:216], np.broadcast_to([1, 0, 0, 1], (36, 4)))
    assert not np.any(h[:, 269:271])
    out = np.empty(WIDTH, dtype=np.uint16)
    out[:6] = p
    z = out[6:].reshape(36, 212)
    z[:, :106] = h[:, :106]
    z[:, 106:159] = h[:, 106:212].reshape(36, 53, 2) @ np.array([1, 2])
    z[:, 159:212] = h[:, 216:269]
    return out


def unpack(v):
    v = np.asarray(v, dtype=np.int64)
    p, z = v[:6], v[6:].reshape(36, 212)
    h = np.zeros((36, 271), dtype=np.int64)
    h[:, :106] = z[:, :106]
    h[:, 106:212] = np.stack((z[:, 106:159] % 2, z[:, 106:159] // 2), axis=-1).reshape(36, 106)
    h[:, 212:216] = [1, 0, 0, 1]
    h[:, 216:269] = z[:, 159:212]
    return p, h.reshape(6, 6, 271)


def main():
    started = time.monotonic()
    files = ['e_a6_double_model_root.py', 'e_a6_double_cover_root.npz',
             'e_a6_double_model_root.npz', 'de_a6_schreier_full_ordered.bin',
             'de_a6_schreier_full_ordered.npz', 'de_ferrari_a6_source_compression.json',
             'de_a6_schreier.cpp']
    hashes = {p: sha256((HERE / p).read_bytes()).hexdigest() for p in files}
    H = FerrariA6Double()
    affine_one = np.array([1, 0, 0, 1, 0, 0])
    assert np.array_equal(H.project_affine2(H.x), np.broadcast_to(affine_one, (6, 6)))
    assert np.array_equal(H.project_affine2(H.y), np.broadcast_to(affine_one, (6, 6)))
    W = InducedCombined(H, load_data())
    original = [W.letters[0], W.letters[1]]
    cert = read_certificate(HERE / 'de_a6_schreier_full_ordered.bin')
    verify_words(cert)
    compression = json.loads((HERE / 'de_ferrari_a6_source_compression.json').read_text())
    keep = np.concatenate(compression['retained_original_canonical_orders'])
    renumber = np.full(38160, -1, dtype=np.int64)
    renumber[keep] = np.arange(len(keep))
    ordered = np.load(HERE / 'de_a6_schreier_full_ordered.npz')
    point_order, point_inverse = ordered['point_order'], ordered['point_order_inverse']

    def base(e):
        values = H.project_a6(e[1])
        out = []
        for q in range(6):
            for i in range(6):
                p = np.asarray(H.old.permutation(values[q, i]).array_form)
                out.extend(1060*(6*int(e[0][q])+i)+p)
        compressed = renumber[np.asarray(out)[keep]]
        assert np.all(compressed >= 0)
        return point_inverse[compressed[point_order]]

    bp = np.array([base(g) for g in original], dtype=np.uint16)
    assert np.array_equal(bp, cert['original'])
    gs = original + [W.letters[-1]]
    for g in gs:
        assert W.equal(unpack(pack(g)), g)
        for h in gs:
            assert np.array_equal(base(W.mul(g, h)), base(h)[base(g)])
    rng = np.random.default_rng(621113)
    values = [W.one] + original
    controls = []
    for i in range(192):
        op = 2+i % 4
        a, b = map(int, rng.integers(len(values), size=2))
        value = (W.mul(values[a], values[b]) if op == 2 else W.inv(values[a]) if op == 3
                 else W.comm(values[a], values[b]) if op == 4 else W.conj(values[a], values[b]))
        assert W.equal(unpack(pack(value)), value)
        controls.append((op, a, b, pack(value)))
        values.append(value)
    kernel_controls = []
    for i in range(159):
        v = np.zeros(KERNEL, dtype=np.int64)
        # Every local basis coordinate occurs in all 36 actual source blocks.
        v[np.arange(36)*159+i] = 1
        e = (W.id, H.relative_kernel_element(v.reshape(6, 6, 159)))
        assert W.equal(unpack(pack(e)), e)
        assert np.array_equal(H.relative_kernel_vector(e[1]).ravel(), v)
        kernel_controls.append((pack(e), v))
        for g in original:
            c = W.conj(g, e)
            cv = H.relative_kernel_vector(c[1]).ravel()
            kernel_controls.append((pack(c), cv))
    # Nonuniform supports also exercise every induced block permutation.
    for _ in range(50):
        v = rng.integers(2, size=KERNEL)
        e = (W.id, H.relative_kernel_element(v.reshape(6, 6, 159)))
        for g in original:
            c = W.conj(g, e)
            kernel_controls.append((pack(c), H.relative_kernel_vector(c[1]).ravel()))
    path = HERE / 'e_a6_double_kernel_model_root.bin'
    with path.open('wb') as f:
        f.write(struct.pack('<6I', 0xA62F1C01, 1, WIDTH, H.uid, H.z, H.autone))
        for table in (H.um, H.ui, H.am, H.ai, H.auto):
            f.write(np.asarray(table, dtype='<u2').tobytes())
        f.write(np.asarray(H.character, dtype=np.uint8).tobytes())
        for e in [W.one]+original:
            f.write(pack(e).astype('<u2').tobytes())
        f.write(struct.pack('<I', len(controls)))
        for op, a, b, v in controls:
            f.write(struct.pack('<3I', op, a, b))
            f.write(v.astype('<u2').tobytes())
        f.write(struct.pack('<II', KERNEL, len(kernel_controls)))
        for e, v in kernel_controls:
            f.write(e.astype('<u2').tobytes())
            f.write(np.asarray(v, dtype=np.uint8).tobytes())
        f.write(struct.pack('<II', bp.shape[1], 2))
        f.write(bp.astype('<u2').tobytes())
    np.savez_compressed(HERE / 'e_a6_double_source_root.npz',
                        s=bp[0], r=bp[1], source_coset_s=original[0][0],
                        source_coset_r=original[1][0], full_s=original[0][1], full_r=original[1][1])
    out = {'status': 'PASS_EXACT_BINARY_SOURCE_EXPORT',
           'all_six_pure_pair_affine2_images_identity': True,
           'all_induced_values_have_M_identity_and_translation_zero': True,
           'packed_model_is_exact_restriction_of_full_holomorph': True,
           'all_36_evaluations_retained': True,
           'base_generators_match_unchanged_complete_A6_certificate': True,
           'base_degree': bp.shape[1], 'packed_coordinate_count': WIDTH,
           'relative_kernel_ambient_dimension': KERNEL,
           'independent_Python_operation_controls': len(controls),
           'kernel_coordinate_and_conjugation_controls': len(kernel_controls),
           'input_sha256': hashes, 'binary_sha256': sha256(path.read_bytes()).hexdigest(),
           'seconds': round(time.monotonic()-started, 3)}
    (HERE / (STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    assert all(sha256((HERE / p).read_bytes()).hexdigest() == v for p, v in hashes.items())
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()
