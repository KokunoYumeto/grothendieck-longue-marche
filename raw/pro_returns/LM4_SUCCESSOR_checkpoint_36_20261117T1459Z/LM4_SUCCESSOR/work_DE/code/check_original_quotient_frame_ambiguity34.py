#!/usr/bin/env python3
"""One prescribed signed mod-12 frame comparison for A.110.

This checks the finite images of the theoretically constructed continuous
rho-fixed h. It does not construct h, or infer a continuous lift from a
finite computation. There is no search over targets or frames.
"""
import argparse
import json
from pathlib import Path


def mul(a, b, modulus):
    return tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) % modulus
                 for i in range(2) for j in range(2))


def inv(a, modulus):
    assert (a[0]*a[3] - a[1]*a[2]) % modulus == 1
    return (a[3] % modulus, -a[1] % modulus,
            -a[2] % modulus, a[0] % modulus)


def neg(a, modulus):
    return tuple(-x % modulus for x in a)


def power(a, n, modulus):
    out = (1, 0, 0, 1)
    for _ in range(n):
        out = mul(out, a, modulus)
    return out


def conj(a, b, modulus):
    return mul(mul(a, b, modulus), inv(a, modulus), modulus)


def act(a, v, modulus):
    return tuple(sum(a[2*i+j]*v[j] for j in range(2)) % modulus
                 for i in range(2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--certificate', required=True)
    args = parser.parse_args()
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
        print('PASS:', name)

    n = 12
    identity = (1, 0, 0, 1)
    upper = (1, 1, 0, 1)
    lower = (1, 0, 11, 1)
    original_s = mul(mul(upper, lower, n), upper, n)
    original_r = neg(mul(upper, lower, n), n)
    h = (5, 0, 0, 5)
    beta = identity
    frame_coordinate = 0
    shear = power(upper, 8*frame_coordinate, n)
    check('original LM7_PUSH S65 matrix', original_s == (0, 1, 11, 0))
    check('original LM7_PUSH R0 matrix', original_r == (0, 11, 1, 11))
    check('original R0 has cube I modulo 12', power(original_r, 3, n) == identity)
    check('h12 has determinant one', (h[0]*h[3]-h[1]*h[2]) % n == 1)
    check('h12 is I modulo 4', tuple(x % 4 for x in h) == identity)
    check('h12 is minus I modulo 3', tuple(x % 3 for x in h) == (2, 0, 0, 2))
    check('fixed s-frame beta=1', conj(beta, original_s, n) == original_s)
    check('zero frame coordinate gives original shear V=I', shear == identity)

    line = (1, 2)  # The original rational 3-line F_3(1,-1).
    r3 = tuple(x % 3 for x in original_r)
    check('original rational line is fixed by R0 modulo 3', act(r3, line, 3) == line)
    frame_rows = []
    for label, a, expected_bit in [('identity', identity, 0), ('fixed_lift_h', h, 1)]:
        check(label + ': same r-frame conjugation', conj(a, original_r, n) == original_r)
        t = mul(inv(a, n), shear, n)
        w = mul(inv(beta, n), shear, n)
        check(label + ': original signed modulo-four T normalization',
              tuple(x % 4 for x in t) == identity)
        check(label + ': W is identity', w == identity)
        image = act(t, line, 3)
        scalar = 1 if image == line else 2 if image == (2, 1) else None
        check(label + ': rational-line action has prescribed sign',
              scalar == (1 if expected_bit == 0 else 2))
        epsilon3 = 0 if scalar == 1 else 1
        # The original epsilon_2 is a character; its value at W=I is zero.
        epsilon2 = 0
        delta = (epsilon3 + epsilon2) % 2
        check(label + ': original E65 delta value', delta == expected_bit)
        frame_rows.append(dict(label=label, A12=a, beta12=beta, T12=t, W12=w,
                               line_mod3=line, line_scalar=scalar,
                               epsilon3=epsilon3, epsilon2=epsilon2, delta=delta))

    # A single fixed-precision image of the proof's Hensel quaternion pair.
    # The two lifts below are the deterministic Hensel construction of b mod 27.
    b, precision = 1, 3
    hensel = [dict(modulus=precision, b=b)]
    while precision < 27:
        next_precision = 3*precision
        lifts = [b+precision*t for t in range(3)
                 if ((b+precision*t)**2+2) % next_precision == 0]
        check('unique Hensel digit modulo ' + str(next_precision), len(lifts) == 1)
        b, precision = lifts[0], next_precision
        hensel.append(dict(modulus=precision, b=b))
    p = 27
    i = (0, 1, 26, 0)
    j = (1, b, b, 26)
    minus_identity = (26, 0, 0, 26)
    check('quaternion i determinant one modulo 27', (i[0]*i[3]-i[1]*i[2]) % p == 1)
    check('quaternion j determinant one modulo 27', (j[0]*j[3]-j[1]*j[2]) % p == 1)
    check('quaternion squares minus I modulo 27',
          mul(i, i, p) == minus_identity and mul(j, j, p) == minus_identity)
    check('quaternion generators anticommute modulo 27', mul(i, j, p) == neg(mul(j, i, p), p))
    commutator = mul(mul(mul(i, j, p), inv(i, p), p), inv(j, p), p)
    check('quaternion commutator minus I modulo 27', commutator == minus_identity)

    certificate = dict(
        scope='One prescribed finite image certificate; continuous fixed lift proved in A.110, not inferred here.',
        original_run='LM7_PUSH', original_definitions='E.65.2--4',
        modulus=12, upper=upper, lower=lower, S65=original_s, R0=original_r,
        frame_coordinate=frame_coordinate, shear=shear, frame_rows=frame_rows,
        quaternion=dict(modulus=p, hensel_digits=hensel, i=i, j=j, commutator=commutator),
        checks=checks, check_count=len(checks), result='PASS')
    Path(args.certificate).write_text(json.dumps(certificate, indent=2) + '\n')
    print('RESULT: PASS (' + str(len(checks)) + ' exact checks; no target census)')


if __name__ == '__main__':
    main()
