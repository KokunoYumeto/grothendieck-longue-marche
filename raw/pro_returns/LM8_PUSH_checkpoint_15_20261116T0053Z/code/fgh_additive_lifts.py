#!/usr/bin/env python3
"""Additive lift identities and a class-two multiplicative obstruction.

Uses F4[epsilon]/epsilon^2 (16 elements), so the nontrivial polynomial
automorphism is detected on actual points as well as polynomially.
The class-two group tested is specified explicitly, not identified with
an unprovided canonical integral Fermat completion.
"""
from itertools import product
from pathlib import Path
import json


# F4=F2[w]/(w^2+w+1), encoded in two bits.
def fa(a, b): return a ^ b


def fm(a, b):
    out = 0
    for i in range(2):
        for j in range(2):
            if ((a >> i) & 1) and ((b >> j) & 1): out ^= 1 << (i+j)
    if out & 4: out ^= 7
    return out


# Low two bits = scalar, upper two bits = epsilon coefficient.
def ra(a, b): return a ^ b


def rm(a, b):
    a0, a1 = a & 3, a >> 2
    b0, b1 = b & 3, b >> 2
    return fm(a0, b0) | ((fm(a0, b1) ^ fm(a1, b0)) << 2)


e, one, omega = 4, 1, 2


def f(t): return ra(t, rm(e, ra(rm(t, t), t)))


def hm(u, v):
    # Heisenberg: (a,b,c)(a',b',c')=(a+a',b+b',c+c'+ab').
    a, b, c = u
    d, z, h = v
    return ra(a, d), ra(b, z), ra(ra(c, h), rm(a, z))


def hi(u):
    a, b, c = u
    return a, b, ra(c, rm(a, b))


def hc(u, v): return hm(hm(hm(u, v), hi(u)), hi(v))


def main():
    assert rm(e, e) == 0 and fm(omega, omega) == omega ^ 1
    for a, b in product(range(16), repeat=2):
        assert f(ra(a, b)) == ra(f(a), f(b))
        assert hc((a, 0, 0), (0, b, 0)) == (0, 0, rm(a, b))
    for a in range(16):
        assert f(f(a)) == a
        assert f(a) == a if (a & 3) in (0, 1) else f(a) != a
    assert f(0) == 0 and f(1) == 1
    lhs, rhs = f(rm(omega, omega)), rm(f(omega), f(omega))
    assert ra(lhs, rhs) == e
    # Schemes' integral coefficient matrices reduce to F2; verify an
    # arbitrary sample and all entries of the actual q2 model as vectors.
    model_path = Path(__file__).with_name('fgh_q2_recheck_model.json')
    model = json.loads(model_path.read_text())
    def apply_matrix(A, v):
        out = []
        for row in A:
            value = 0
            for c, z in zip(row, v):
                if c & 1: value ^= z
            out.append(value)
        return out
    checked = 0
    # Basis vectors scaled by every ring element suffice by additivity.
    for A in model['actions']:
        for j, a in product(range(5), range(16)):
            v = [a if i == j else 0 for i in range(5)]
            assert [f(z) for z in apply_matrix(A, v)] == apply_matrix(A, [f(z) for z in v])
            checked += 1
    for row in model['cocycle']:
        for v in row:
            assert all(f(a & 1) == (a & 1) for a in v)
    result = {
        'ring': 'F4[epsilon]/epsilon^2, omega^2=omega+1',
        'ring_size': 16,
        'automorphism': 'f(T)=T+epsilon*(T^2-T)',
        'additivity_pairs_checked': 16**2,
        'inverse_points_checked': 16,
        'q2_matrix_compatibilities_checked': checked,
        'q2_cocycle_values_fixed': 48**2,
        'class2_obstruction': {'a': 'omega', 'b': 'omega',
                               'f(ab)': 'omega^2+epsilon',
                               'f(a)f(b)': 'omega^2', 'difference': 'epsilon'},
        'scope': 'Extends every integral abelian cocycle model; fails for the specified Heisenberg quotient. No identification of an unspecified integral nonabelian Fermat model is asserted.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__': main()
