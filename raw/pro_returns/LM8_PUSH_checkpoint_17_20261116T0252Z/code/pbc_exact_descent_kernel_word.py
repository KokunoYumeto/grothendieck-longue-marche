#!/usr/bin/env python3
"""Exact free-product and signed-matrix certificate for the closed-U ghost.

No finite matrix check substitutes for the six full free-product identities.
The word is formed in the temporary marking x=tau^-2, y=s*x*s.
"""
from pathlib import Path
import hashlib
import json


def reduce_free(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def inverse(word):
    return tuple(-a for a in reversed(word))


def comm(a, b):
    return reduce_free(a + b + inverse(a) + inverse(b))


def substitute(word, x, y):
    images = {1: x, 2: y, -1: inverse(x), -2: inverse(y)}
    return reduce_free(tuple(b for a in word for b in images[a]))


def gamma_reduce(word):
    """C2*C3 normal form: syllables (factor, exponent), S=1,R=2."""
    out = []
    for a in word:
        fac = abs(a)
        order = 2 if fac == 1 else 3
        exponent = (1 if a > 0 else -1) % order
        if out and out[-1][0] == fac:
            exponent = (out.pop()[1] + exponent) % order
        if exponent:
            out.append((fac, exponent))
    return tuple(out)


def mm(a, b, m):
    return tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) % m
                 for i in range(2) for j in range(2))


def mi(a, m):
    return (a[3] % m, -a[1] % m, -a[2] % m, a[0] % m)


def matrix_word(word, x, y, m):
    out = (1, 0, 0, 1)
    images = {1: x, 2: y, -1: mi(x, m), -2: mi(y, m)}
    for a in word:
        out = mm(out, images[a], m)
    return out


def run():
    x, y = (1,), (2,)
    z = inverse(x+y)
    inner = comm(x*2, y*2)
    outer = comm(inner, z*2)
    word = reduce_free(outer*2)
    assert sum(a == 1 for a in word) == sum(a == -1 for a in word)
    assert sum(a == 2 for a in word) == sum(a == -2 for a in word)
    # rho=(x,y,z)->(y,z,x), theta swaps x,y.  These are the six
    # actual representatives rho^i and rho^i theta, not guessed matrices.
    substitutions = [(x, y), (y, z), (z, x), (y, x), (z, y), (x, z)]
    phi_x, phi_y = (-2, 1), (1,)  # tau^-1=R^-1 S, and S.
    full = []
    for i, (a, b) in enumerate(substitutions):
        sigma_word = substitute(word, a, b)
        gamma_word = substitute(sigma_word, phi_x, phi_y)
        normal_form = gamma_reduce(gamma_word)
        assert normal_form == ()
        full.append({'representative': ['1', 'rho', 'rho^2', 'theta',
                                        'rho theta', 'rho^2 theta'][i],
                     'x_image_in_F': list(a), 'y_image_in_F': list(b),
                     'full_gamma_word': list(gamma_word),
                     'free_product_normal_form': list(normal_form)})
    # Transfer to the question's old marking: x_new=y_old^-1,
    # y_new=x_old^-1.  The OLD filling is x_old=S, y_old=SR.
    old_word = substitute(word, (-2,), (-1,))
    old_gamma = substitute(old_word, (1,), (1, 2))
    assert gamma_reduce(old_gamma) == ()
    old_inverse_gamma = substitute(inverse(old_word), (1,), (1, 2))
    assert gamma_reduce(old_inverse_gamma) == ()
    matrices = []
    for m in (3, 4, 12):
        U, S = (1, 1, 0, 1), (0, 1, -1 % m, 0)
        X = mm(U, U, m)
        Y = mm(mm(S, X, m), mi(S, m), m)
        vals = [matrix_word(t, X, Y, m) for t in (inner, outer, word)]
        expected = (2, 0, 0, 2) if m == 3 else ((1, 0, 0, 1) if m == 4 else (5, 0, 0, 5))
        assert vals[-1] == expected
        matrices.append({'modulus': m, 'x': X, 'y': Y,
                         'inner_commutator': vals[0], 'outer_commutator': vals[1],
                         'word': vals[2]})
    return {'status': 'PASS', 'word': '[[x^2,y^2],z^2]^2',
            'temporary_marking': 'x=tau^-2, y=s*x*s, z=(x*y)^-1',
            'freely_reduced_word': list(word), 'reduced_length': len(word),
            'abelianization': [0, 0], 'six_actual_full_fillings': full,
            'old_marking_word': list(old_word),
            'old_filling_normal_form': list(gamma_reduce(old_gamma)),
            'old_inverse_filling_normal_form': list(gamma_reduce(old_inverse_gamma)),
            'signed_original_matrices': matrices,
            'scope': 'Exact full C2*C3 word identities and finite signed congruence values. The closed-normal relative lifting and full ghost are proved in the accompanying note.'}


if __name__ == '__main__':
    result = run()
    result['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
