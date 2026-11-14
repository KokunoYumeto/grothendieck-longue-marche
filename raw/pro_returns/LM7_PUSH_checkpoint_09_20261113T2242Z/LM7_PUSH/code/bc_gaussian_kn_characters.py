#!/usr/bin/env python3
"""All twelve exact Gaussian characters in the whole-J/E71 common image."""
from pathlib import Path
import hashlib
import itertools
import json
import numpy as np

from bc_gaussian_pro3_frattini_model import mul, inv, uinv, rank3
from de_a6_schreier_certificate import read_certificate, verify_words

HERE = Path(__file__).resolve().parent
STEM = 'bc_gaussian_kn_characters'


def rref3(rows):
    a = np.array(rows, dtype=np.int64) % 3
    r = 0
    pivots = []
    for j in range(a.shape[1]):
        q = next((i for i in range(r, len(a)) if a[i, j]), None)
        if q is None:
            continue
        a[[r, q]] = a[[q, r]]
        a[r] = a[r] * int(a[r, j]) % 3
        for i in range(len(a)):
            if i != r:
                a[i] = (a[i] - a[i, j] * a[r]) % 3
        pivots.append(j)
        r += 1
    return a[:r], pivots


def annihilator(rows):
    a, pivots = rref3(rows)
    out = []
    for j in range(a.shape[1]):
        if j not in pivots:
            v = np.zeros(a.shape[1], dtype=np.int64)
            v[j] = 1
            for i, p in enumerate(pivots):
                v[p] = -a[i, j] % 3
            out.append(v)
    return np.array(out, dtype=np.uint8)


class GaussianCharacters:
    def __init__(self):
        model = np.load(HERE / 'bc_gaussian_pro3_frattini_model.npz')
        self.elements = [tuple(tuple(map(int, u)) for u in g) for g in model['P_elements']]
        self.coords = [tuple(map(int, u)) for u in model['P_Hall_coordinates']]
        self.at = {g: i for i, g in enumerate(self.elements)}
        self.coord = {g: q for g, q in zip(self.elements, self.coords)}
        aut = np.load(HERE / 'bc_gaussian_pro3_frattini_characters.npz')
        self.aut = {k: aut[k + '_automorphism'] for k in ('A', 'B')}
        self.phi = model['deck_automorphism']
        pts = list(itertools.product(range(3), repeat=3))
        pos = {p: i for i, p in enumerate(pts)}
        self.p108 = []
        for g in self.elements:
            out = []
            for j, a in enumerate(g):
                r, s, t, u, v, w = uinv(a)
                out.extend(27*j + pos[((x+r*y+u*z+w) % 3,
                                      (y+s*z+v) % 3, (z+t) % 3)] for x, y, z in pts)
            self.p108.append(np.array(out, dtype=np.uint16))
        self.lookup = {p.tobytes(): i for i, p in enumerate(self.p108)}
        assert len(self.lookup) == 2187

    def decode(self, permutation):
        assert len(permutation) == 2592
        indices = []
        for k in range(6):
            p = permutation[432*k:432*(k+1)] - 432*k
            i = self.lookup[p[:108].tobytes()]
            indices.append(i)
            j = i
            for sheet in range(4):
                assert np.array_equal(p[108*sheet:108*(sheet+1)],
                                      108*sheet + self.p108[j])
                j = int(self.phi[j])
        return indices

    def values(self, permutation):
        indices = self.decode(permutation)
        out = []
        for i, j, name in [(0, 5, 'B'), (1, 4, 'B'), (2, 3, 'A')]:
            g = self.elements[indices[i]]
            h = self.elements[indices[j]]
            delta = mul(h, inv(self.elements[int(self.aut[name][indices[i]])]))
            q = self.coord[delta]
            assert q[:3] == (0, 0, 0)
            a, b = self.coord[g][:2]
            out.extend([a % 3, b % 3, q[3], q[4]])
        return np.array(out, dtype=np.uint8)

    def old_gaussian_values(self, permutation):
        indices = self.decode(permutation)
        return np.array([self.coords[i][:2] for i in indices], dtype=np.uint8) % 3


def old_values(permutation):
    assert len(permutation) == 7501
    points = list(itertools.product(range(3), repeat=2))
    out = []
    for j in range(6):
        p = permutation[4903+9*j:4903+9*(j+1)] - (4903+9*j)
        minus_v = points[int(p[0])]
        v = tuple(-a % 3 for a in minus_v)
        expected = [points.index(tuple((a-b) % 3 for a, b in zip(t, v))) for t in points]
        assert np.array_equal(p, expected)
        out.append(v)
    return np.array(out, dtype=np.uint8)


def check_character_words(certificate, chars):
    original = np.array([chars(g) for g in certificate['original']], dtype=np.uint8)
    values = []
    for op, a, b in certificate['nodes']:
        op, a, b = map(int, (op, a, b))
        if op == 0:
            v = np.zeros(12, dtype=np.int64)
        elif op == 1:
            v = original[a].astype(np.int64)
        elif op == 2:
            v = (values[a] + values[b]) % 3
        elif op == 3:
            v = -values[a] % 3
        elif op == 4:
            v = np.zeros(12, dtype=np.int64)
        elif op == 5:
            v = values[b]
        else:
            raise AssertionError(op)
        values.append(v)
    strong = np.array([chars(g) for g in certificate['strong']], dtype=np.uint8)
    for node, v in zip(certificate['words'], strong):
        assert np.array_equal(values[int(node)], v)
    return strong


def main():
    inputs = ['bc_gaussian_pro3_frattini_model.py',
              'bc_gaussian_pro3_frattini_model.npz',
              'bc_gaussian_pro3_frattini_characters.npz',
              'bc_gaussian_kn_common.json', 'bc_gaussian_kn_common.npz',
              'bc_gaussian_kn_common_J_projected.bin',
              'bc_gaussian_kn_common_old_kernel.bin',
              'bc_gaussian_kn_common_Gaussian.bin']
    hashes = {n: hashlib.sha256((HERE / n).read_bytes()).hexdigest() for n in inputs}
    G = GaussianCharacters()
    joint = read_certificate(HERE / 'bc_gaussian_kn_common_J_projected.bin')
    kernel = read_certificate(HERE / 'bc_gaussian_kn_common_old_kernel.bin')
    gaussian = read_certificate(HERE / 'bc_gaussian_kn_common_Gaussian.bin')
    for c in (joint, kernel, gaussian):
        verify_words(c)
    allchars = check_character_words(gaussian, G.values)
    kernelchars = check_character_words(kernel, G.values)
    assert rank3(allchars) == 12
    for p in np.r_[joint['original'], joint['strong']]:
        assert np.array_equal(old_values(p[:7501]), G.old_gaussian_values(p[7501:]-7501))
    ordinary = [0, 1, 4, 5, 8, 9]
    weight_three = [2, 3, 6, 7, 10, 11]
    assert not np.any(kernelchars[:, ordinary])
    r = rank3(kernelchars)
    annih = annihilator(kernelchars)
    meta = json.loads((HERE / 'bc_gaussian_kn_common.json').read_text())
    quotient = int(meta['exact_common_quotient_order'])
    out = {'status': 'PASS_ALL_TWELVE_CHARACTERS_IN_WHOLE_J_COMMON_IMAGE',
           'entire_Gaussian_character_rank': 12,
           'old_kernel_character_rank': r,
           'old_kernel_weight_three_rank': rank3(kernelchars[:, weight_three]),
           'old_kernel_ordinary_six_characters_zero': True,
           'complete_common_character_annihilator': annih.tolist(),
           'finite_common_quotient_order': str(quotient),
           'order_detected_by_complete_Frattini_characters': str(3**(12-r)),
           'finite_common_order_equals_character_order': quotient == 3**(12-r),
           'literal_E67_six_translation_projection_compared_on_all_inputs_and_strong_words': True,
           'all_kernel_and_full_character_DAGs_replayed': True,
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'input_sha256': hashes}
    np.savez_compressed(HERE / (STEM + '.npz'),
                        full_characters=allchars, old_kernel_characters=kernelchars,
                        common_character_annihilator=annih)
    (HERE / (STEM + '.json')).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
