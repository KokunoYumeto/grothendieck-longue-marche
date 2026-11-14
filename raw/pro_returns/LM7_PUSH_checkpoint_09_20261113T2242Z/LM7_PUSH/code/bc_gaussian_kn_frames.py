#!/usr/bin/env python3
"""Complete framed Gaussian norm maps in the E70 class-three detector."""
from pathlib import Path
import hashlib
import json
import time
import numpy as np

from bc_gaussian_pro3_frattini_model import X, Y, ONE, mul, inv, power
from bc_gaussian_kn_characters import GaussianCharacters

HERE = Path(__file__).resolve().parent
STEM = 'bc_gaussian_kn_frames'


def main():
    start = time.monotonic()
    C = GaussianCharacters()
    one = (ONE, 0)

    def phi(g, n):
        i = C.at[g]
        for _ in range(n % 4):
            i = int(C.phi[i])
        return C.elements[i]

    def gm(a, b):
        return mul(a[0], phi(b[0], a[1])), (a[1]+b[1]) % 4

    def gi(a):
        return phi(inv(a[0]), -a[1]), -a[1] % 4

    def gp(a, n):
        v = one
        for _ in range(n):
            v = gm(v, a)
        return v

    def gc(a, b):
        return gm(gm(a, b), gi(a))

    x, y, z = (X, 1), (inv(Y), 2), (ONE, 1)
    assert gm(gm(x, y), z) == one and gp(y, 2) == gp(z, 4) == one
    zframes = {}
    for h in C.elements:
        zframes.setdefault(gc((h, 0), z), []).append(h)
    assert len(zframes) == 729 and all(len(v) == 3 for v in zframes.values())
    inner = {(gc(gp(x, j), y), gc(gp(x, j), z)): j for j in range(4)}
    model = json.loads((HERE / 'bc_gaussian_heisenberg_model.json').read_text())
    assert all(q[3] == 0 for row in model['records'] for q in row['six_absolute_values'])
    known = {tuple(tuple(map(int, q[:3])) for q in row['six_absolute_values']): i
             for i, row in enumerate(model['records'])}
    rows = []
    allvalues = []
    allcharacters = []
    norm_actions = set()
    allowed_actions = set()
    raw_frames = 0
    for hy in C.elements:
        yi = gc((hy, 0), y)
        zi = gi(gm(x, yi))
        assert zi[1] == 1
        if gp(zi, 4) != one:
            continue
        assert zi in zframes
        xx = gm(gp(x, 2), yi)
        yy = gm(gp(zi, 2), yi)
        assert xx[1] == yy[1] == 0
        u, v = C.coord[xx[0]], C.coord[yy[0]]
        determinant = (u[0]*v[1]-u[1]*v[0]) % 3
        assert determinant == 1
        norm_actions.add((yi, zi))
        for hz in zframes[zi]:
            raw_frames += 1
            gs = (inv(hy), hy, hz, inv(hz), mul(inv(hz), hy), mul(inv(hy), hz))
            chars = []
            allowed = True
            for i, j, name in [(0, 5, 'B'), (1, 4, 'B'), (2, 3, 'A')]:
                delta = mul(gs[j], inv(C.elements[int(C.aut[name][C.at[gs[i]]])]))
                q = C.coord[delta]
                if q[:3] != (0, 0, 0):
                    allowed = False
                    break
                a, b = C.coord[gs[i]][:2]
                chars.extend([a % 3, b % 3, q[3], q[4]])
            if not allowed:
                continue
            allowed_actions.add((yi, zi))
            lower = []
            for g in gs:
                a, b, e, _, _ = C.coord[g]
                lower.append((a % 3, b % 3, (e+2*a*b) % 3))
            key = tuple(lower)
            assert key in known
            rows.append({'index': len(rows), 'hy_Hall': C.coord[hy], 'hz_Hall': C.coord[hz],
                         'X_image_Hall': u, 'Y_image_Hall': v,
                         'E69_framed_target_index': known[key],
                         'specified_inner_x_power_0_to_3': inner.get((yi, zi)),
                         'six_Hall_values': [C.coord[g] for g in gs],
                         'twelve_Frattini_characters': chars})
            allvalues.append([C.at[g] for g in gs])
            allcharacters.append(chars)
    byold = {}
    for row in rows:
        byold.setdefault(str(row['E69_framed_target_index']), []).append(row['index'])
    inputs = ['bc_gaussian_pro3_frattini_model.py', 'bc_gaussian_pro3_frattini_model.npz',
              'bc_gaussian_pro3_frattini_characters.npz', 'bc_gaussian_kn_characters.py',
              'bc_gaussian_heisenberg_model.json']
    out = {'status': 'PASS_COMPLETE_FRAMED_GAUSSIAN_CLASS_THREE_NORM_ENUMERATION',
           'free_kernel_order': 2187, 'all_hy_elements_examined': 2187,
           'all_hz_elements_indexed': 2187, 'order_four_conjugacy_class_size': 729,
           'centralizer_order': 3, 'all_cusp_preserving_action_count': len(norm_actions),
           'all_cusp_preserving_frame_count': raw_frames,
           'source_graph_framed_target_count': len(rows),
           'source_graph_action_count': len(allowed_actions),
           'specified_inner_x_0_to_3_framed_count': sum(r['specified_inner_x_power_0_to_3'] is not None for r in rows),
           'specified_inner_x_0_to_3_action_count': len({r['specified_inner_x_power_0_to_3'] for r in rows
                                                      if r['specified_inner_x_power_0_to_3'] is not None}),
           'framed_target_indices_over_E69': byold,
           'records': rows,
           'scope': 'Complete finite class-three framed norm maps satisfying the actual six-coordinate source graph; full pro-three realization is separately proved for the displayed inner families.',
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'input_sha256': {n: hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in inputs},
           'seconds': round(time.monotonic()-start, 6)}
    np.savez_compressed(HERE/(STEM+'.npz'),
                        six_P3_element_indices=np.array(allvalues, dtype=np.uint16),
                        twelve_Frattini_characters=np.array(allcharacters, dtype=np.uint8))
    (HERE/(STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('records', 'input_sha256')}, indent=2))


if __name__ == '__main__':
    main()
