#!/usr/bin/env python3
"""Actual action on gamma_2(N)/gamma_4(N), modulo three.

The input is the realized arithmetic Frobenius basis of A.38.  The
degree-two/three lattice is written in the Lie commutator basis; its
comparison with group commutators uses only 1/2, a 3-adic unit.
Unknown degree-three images of the ten geometric generators do not
enter the action on this module.  All action and comparison matrices
are retained in the NPZ certificate.
"""
from pathlib import Path
from itertools import combinations_with_replacement
import contextlib
import importlib.util
import io
import json
import numpy as np

HERE = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


f = load('de_fermat_schreier')
g = load('a_ihara_gauge')
raw = json.loads((HERE / 'a_ihara_final_parameters.json').read_text())
PAIRS = list(zip(*f.UP))
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}
BASIS = [(mu, i)
         for mu in combinations_with_replacement(range(10), 3)
         for i in sorted(set(mu))[1:]]
BASIS_INDEX = {b: i for i, b in enumerate(BASIS)}
assert len(BASIS) == 330


def mm(a, b):
    return a @ b % 3


def columns(a):
    _, pivots = g.rref(a)
    return a[:, pivots] % 3, pivots


def inverse(a):
    ident = np.eye(a.shape[0], dtype=np.int64)
    rr, pivots = g.rref(np.hstack((a, ident)))
    assert pivots == list(range(a.shape[0]))
    b = rr[:, a.shape[0]:] % 3
    assert np.array_equal(mm(a, b), ident)
    return b


def power(a, n):
    if n < 0:
        return power(inverse(a), -n)
    out = np.eye(a.shape[0], dtype=np.int64)
    while n:
        if n & 1:
            out = mm(out, a)
        a = mm(a, a)
        n //= 2
    return out


def sqrt_pro3(a):
    ident = np.eye(a.shape[0], dtype=np.int64)
    order, b = 1, a
    while not np.array_equal(b, ident):
        b = mm(mm(b, b), b)
        order *= 3
        assert order <= 3**7
    root = power(a, (order + 1)//2)
    assert np.array_equal(mm(root, root), a)
    return root


def automorphism(a, j):
    return np.block([[a, np.zeros((10, 45), dtype=np.int64)],
                     [j, f.exterior(a)]]) % 3


def triple(i, j, k):
    """Coordinates of [[X_i,X_j],X_k], with every Jacobi sign explicit."""
    out = np.zeros(330, dtype=np.int64)
    if i == j:
        return out
    mu = tuple(sorted((i, j, k)))
    minimum = mu[0]
    if j == minimum:
        out[BASIS_INDEX[(mu, i)]] += 1
    elif i == minimum:
        out[BASIS_INDEX[(mu, j)]] -= 1
    else:
        assert k == minimum
        out[BASIS_INDEX[(mu, i)]] += 1
        out[BASIS_INDEX[(mu, j)]] -= 1
    return out % 3


TRIPLE = np.stack([
    np.stack([triple(i, j, k) for k in range(10)], axis=1)
    for i, j in PAIRS], axis=1)
assert TRIPLE.shape == (330, 45, 10)


def degree3(a):
    ext = f.exterior(a)
    tensor = np.einsum('kij,ia,jb->kab', TRIPLE, ext, a,
                       optimize=True) % 3
    out = []
    for mu, i in BASIS:
        j = mu[0]
        remainder = list(mu)
        remainder.remove(i)
        remainder.remove(j)
        k = remainder[0]
        out.append(-tensor[:, PAIR_INDEX[(j, i)], k])
    return np.stack(out, axis=1) % 3


def gamma2_action(aut):
    a, j = aut[:10, :10], aut[10:, :10]
    # [J_i,A_j] + [A_i,J_j] = [[J_i],A_j] - [[J_j],A_i].
    tensor = np.einsum('kab,ai,bj->kij', TRIPLE, j, a,
                       optimize=True) % 3
    cross = np.stack([tensor[:, i, j] - tensor[:, j, i]
                      for i, j in PAIRS], axis=1) % 3
    return np.block([[f.exterior(a), np.zeros((45, 330), dtype=np.int64)],
                     [cross, degree3(a)]]) % 3


def main():
    ua, uj = f.generator_images(np.array(raw['base_fa'], dtype=np.int64),
                                np.array(raw['base_fz'], dtype=np.int64), 7)
    ca, cj = f.generator_images(*f.zero(), chi=8)
    u = automorphism(ua, uj)
    c = automorphism(ca, cj)
    v = mm(mm(c, u), c)
    uv = mm(u, v)
    d0 = mm(mm(u, c), inverse(sqrt_pro3(uv)))
    h0 = sqrt_pro3(mm(d0, c))
    m = mm(mm(inverse(h0), uv), h0)
    n = mm(v, inverse(u))
    assert np.array_equal(mm(c, m), mm(m, c))
    assert np.array_equal(mm(mm(c, n), c), inverse(n))
    small = {'u': u, 'v': v, 'c': c, 'm': m, 'n': n}
    actions = {name: gamma2_action(a) for name, a in small.items()}
    ident = np.eye(375, dtype=np.int64)
    assert np.array_equal(mm(actions['c'], actions['c']), ident)
    assert np.array_equal(mm(mm(actions['c'], actions['u']), actions['c']),
                          actions['v'])
    assert np.array_equal(gamma2_action(uv), mm(actions['u'], actions['v']))
    assert np.array_equal(mm(actions['c'], actions['m']),
                          mm(actions['m'], actions['c']))
    assert np.array_equal(mm(mm(actions['c'], actions['n']), actions['c']),
                          gamma2_action(inverse(n)))
    print('Exact functoriality and all arithmetic involution relations: PASS')

    # Compare the entire degree-three basis to the independent A.13 lattice.
    integral = json.loads((HERE / 'a_degree3_matrices.json').read_text())
    assert integral['basis'] == [[list(mu), i] for mu, i in BASIS]
    base_change = np.array(json.loads((HERE / 'a_ihara_lattice.json').read_text())
                           ['A7_to_Schreier_basis'], dtype=np.int64) % 3
    b3 = degree3(base_change)
    for name, old in zip(('u', 'v', 'c'), integral['M3_Galois_matrices']):
        old = np.array(old, dtype=np.int64) % 3
        assert np.array_equal(mm(actions[name][45:, 45:], b3), mm(b3, old))
    print('Independent integral M3 basis comparison for u,v,c: PASS')

    # The reference O cusp section has value c_O on tame inertia and zero
    # Kummer17 values on m,n.  c_O=x^3 is the seventh Schreier generator.
    eo = np.zeros(10, dtype=np.int64)
    eo[6] = 1
    tame = ident.copy()
    tame[45:, :45] = -np.einsum('kab,b->ka', TRIPLE, eo) % 3
    actions['t'] = tame
    for name in ('u', 'v', 'm', 'n'):
        assert np.array_equal(mm(actions[name], tame), mm(tame, actions[name]))
    assert np.array_equal(mm(mm(actions['c'], tame), actions['c']),
                          (2*ident-tame) % 3)
    print('Reference tame action and arithmetic compatibility: PASS')

    summaries = {}
    for names in (('m', 'n'), ('m', 'n', 't')):
        generators = [(actions[name] - ident) % 3 for name in names]
        subspace = ident
        dimensions = [375]
        for depth in range(1, 15):
            subspace, _ = columns(np.hstack([mm(a, subspace)
                                            for a in generators]))
            dimensions.append(subspace.shape[1])
            if not subspace.shape[1]:
                break
        assert dimensions[-1] == 0
        key = ','.join(names)
        summaries[key] = dimensions
        print('Augmentation powers for', key, ':', dimensions)

    # Source cocycles respecting c(m)=m and c(n)=n^-1.
    plus, _ = columns((ident + actions['c']) % 3)
    minus, _ = columns((ident-mm(actions['n'], actions['c'])) % 3)
    print('Full module c-plus rank:', plus.shape[1])
    print('Full module (nc)-minus rank:', minus.shape[1])
    print('Geometric M2 c-plus and c-minus ranks:',
          f.rank((np.eye(45, dtype=np.int64)+actions['c'][:45, :45]) % 3),
          f.rank((np.eye(45, dtype=np.int64)-actions['c'][:45, :45]) % 3))

    np.savez_compressed(HERE/'a_ihara_gamma2_action_certificate.npz',
                        **{'small_'+k: a.astype(np.int8) for k, a in small.items()},
                        **{'action_'+k: a.astype(np.int8) for k, a in actions.items()},
                        triple=TRIPLE.astype(np.int8),
                        A7_to_Schreier_M3=b3.astype(np.int8))
    artifact = {'basis_M2': [[int(i), int(j)] for i, j in PAIRS],
                'basis_M3': [[list(mu), i] for mu, i in BASIS],
                'augmentation_image_dimensions': summaries,
                'c_plus_rank': plus.shape[1], 'nc_minus_rank': minus.shape[1],
                'tame_O_vector': eo.tolist(),
                'module': 'gamma2(N)/gamma4(N) tensor F3; Lie bracket basis',
                'source_basis': 'Actual basis of A38; all W words use psi^-1 transport',
                'comparison': 'log commutator correction uses only 1/2; no division by3'}
    (HERE/'a_ihara_gamma2_action.json').write_text(json.dumps(artifact, indent=2)+'\n')
    print('PASS: complete 375-dimensional actual module action retained.')


if __name__ == '__main__':
    main()
