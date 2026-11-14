#!/usr/bin/env python3
"""Whole J=K6 intersect F-prime joined to all Gaussian Frattini coordinates.

The source is first generated and derived on all original points. Only
then are the old retained points taken and the95 actual sixth powers
adjoined. No list of old finite-image preimages replaces this source.
"""
from pathlib import Path
import hashlib
import json
import time
import numpy as np

from a_cm_distribution_e62 import certify
from a_cm_kn23_source import certify_fixed
from a_cm_gl23_pc import Sifter
from de_a6_schreier_certificate import read_certificate, verify_words

HERE = Path(__file__).resolve().parent
STEM = 'bc_gaussian_kn_common'


def word(w, generators):
    p = np.arange(generators.shape[1], dtype=np.uint16)
    letters = {1: generators[0], 2: generators[1],
               -1: np.argsort(generators[0]), -2: np.argsort(generators[1])}
    for a in w:
        p = letters[a][p]
    return p


def main():
    start = time.monotonic()
    inputs = ['a_cm_kn23_model.json', 'a_cm_kn23_model.npz',
              'a_cm_kn23_source.npz', 'a_cm_kn23_ab_lattice.json',
              'a_cm_kn23_ab_lattice.npz', 'a_cm_kn23_full.json',
              'a_cm_kn23_full_projected.bin',
              'bc_gaussian_pro3_frattini_model.json',
              'bc_gaussian_pro3_frattini_model.npz',
              'a_cm_distribution_e62.py', 'a_cm_kn23_source.py',
              'de_a6_schreier.cpp', 'a_cm_fixed_base.cpp']
    hashes = {n: hashlib.sha256((HERE / n).read_bytes()).hexdigest() for n in inputs}
    oldmeta = json.loads((HERE / inputs[0]).read_text())
    old = np.load(HERE / inputs[1])
    gmeta = json.loads((HERE / 'bc_gaussian_pro3_frattini_model.json').read_text())
    gaussian = np.load(HERE / 'bc_gaussian_pro3_frattini_model.npz')
    assert oldmeta['source_basis_words_in_F'] == gmeta['all_97_literal_N_words']
    oldN = old['common_N']
    GN = gaussian['N_generator_permutations']
    assert oldN.shape == (97, 11691) and GN.shape == (97, 2592)
    common = np.array([np.r_[a, 11691 + b] for a, b in zip(oldN, GN)], dtype=np.uint16)
    ni, nc = certify(STEM + '_N', common, greedy=True)
    print('Actual common N order', ni['order'], flush=True)
    di, dc = certify(STEM + '_N_derived', common[ni['selected_original_indices']], derived=True)
    print('Actual common Nprime order', di['order'], flush=True)
    oldpoints = np.load(HERE / 'a_cm_kn23_source.npz')['retained_projection_points']
    assert oldpoints.shape == (7501,)
    points = np.r_[oldpoints, np.arange(11691, 14283)]
    inverse = np.full(14283, -1, dtype=np.int64)
    inverse[points] = np.arange(len(points))
    derived = inverse[dc['strong'][:, points]]
    assert np.all(derived >= 0)
    lattice = np.load(HERE / 'a_cm_kn23_ab_lattice.npz')
    lmeta = json.loads((HERE / 'a_cm_kn23_ab_lattice.json').read_text())
    extras = []
    gaussian_sixths = []
    for j, row in enumerate(lmeta['kernel_words']):
        w = row['literal_F_word']
        assert [sum((a == k) - (a == -k) for a in w) for k in (1, 2)] == [0, 0]
        p = word(w, gaussian['F_generator_permutations'])
        # Check the literal word against the saved integer N-abelian
        # lift used by E71, including the complete multiplication order.
        q = np.arange(2592, dtype=np.uint16)
        for a, exponent in zip(GN, row['N_abelian_column']):
            b = a if exponent >= 0 else np.argsort(a)
            for _ in range(abs(exponent)):
                q = b[q]
        assert np.array_equal(p, q)
        p2 = p[p]
        p4 = p2[p2]
        p6 = p2[p4]
        gaussian_sixths.append(p6)
        oldfull = lattice['kernel_basis_sixth_full_values'][j]
        oldprojected = lattice['kernel_basis_sixth_projected_values'][j]
        oi = np.full(11691, -1, dtype=np.int64)
        oi[oldpoints] = np.arange(7501)
        assert np.array_equal(oi[oldfull[oldpoints]], oldprojected)
        extras.append(np.r_[oldprojected, 7501 + p6])
    assert len(extras) == 95
    combined = np.r_[derived, np.array(extras, dtype=np.uint16)]
    oldfullmeta = json.loads((HERE / 'a_cm_kn23_full.json').read_text())
    oldcertificate = read_certificate(HERE / oldfullmeta['source_certificate'])
    verify_words(oldcertificate)
    oldS = Sifter(oldcertificate)
    assert all(oldS.contains(a[:7501]) for a in combined)
    ji, jc = certify_fixed(STEM + '_J_projected', combined, oldcertificate['base'])
    oldprefix = len(oldcertificate['base'])
    prefix_order = 1
    for n in ji['orbit_lengths'][:oldprefix]:
        prefix_order *= n
    assert prefix_order == oldS.order == int(oldfullmeta['entire_correction_order'])
    kernel_indices = np.flatnonzero(jc['depths'] >= oldprefix)
    fullkernel = jc['strong'][kernel_indices]
    assert np.array_equal(fullkernel[:, :7501],
                          np.tile(np.arange(7501), (len(fullkernel), 1)))
    kernel = fullkernel[:, 7501:] - 7501
    ki, kc = certify(STEM + '_old_kernel', kernel, greedy=True)
    gi, gc = certify(STEM + '_Gaussian', jc['strong'][:, 7501:] - 7501, greedy=True)
    assert int(gi['order']) == 3**27
    assert int(ki['order']) * oldS.order == int(ji['order'])
    common_order, remainder = divmod(oldS.order * int(gi['order']), int(ji['order']))
    assert remainder == 0
    out = {'status': 'PASS_COMPLETE_WHOLE_J_GAUSSIAN_FRATTINI_COMMON_IMAGE',
           'literal_N_word_lists_identical': True,
           'full_source_degree': 14283, 'retained_source_degree': 10093,
           'all_95_literal_sixth_powers_replayed': True,
           'actual_N_source': ni, 'actual_Nprime_source': di,
           'whole_J_source': ji, 'Gaussian_projection': gi,
           'kernel_over_entire_E71_image': ki,
           'entire_E71_projection_order': str(oldS.order),
           'exact_common_quotient_order': str(common_order),
           'domain': 'J=K6 intersect F-prime, generated by N-prime and95 actual sixth powers',
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'input_sha256': hashes, 'seconds': round(time.monotonic() - start, 6)}
    np.savez_compressed(HERE / (STEM + '.npz'),
                        actual_common_N=common, retained_projection_points=points,
                        actual_projected_Nprime_generators=derived,
                        actual_gaussian_sixth_values=np.array(gaussian_sixths),
                        whole_J_input_generators=combined,
                        old_prefix_base=np.array(oldcertificate['base']),
                        kernel_strong_indices_in_joint=kernel_indices)
    (HERE / (STEM + '.json')).write_text(json.dumps(out, indent=2) + '\n')
    assert all(hashlib.sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print('Whole J order', ji['order'], 'common quotient', common_order, flush=True)
    print(out['status'], out['seconds'], flush=True)


if __name__ == '__main__':
    main()
