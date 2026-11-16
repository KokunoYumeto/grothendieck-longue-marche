"""Exact non-torsion certificates for the marked Prym section.

Only rational arithmetic and direct enumeration at good primes are used.
The generic certificate specializes at a=2. Two CM specializations are
included to distinguish their moving points from torsion-frame data.
"""
from fractions import Fraction as F
import json


def twice(A, B, point):
    x, y = map(F, point)
    slope = (3*x*x + 2*A*x + B)/(2*y)
    u = slope*slope - A - 2*x
    return u, -y + slope*(x-u)


def finite_record(A, B, C, point, p):
    discriminant = 16*(A*A*B*B - 4*B**3 - 4*A**3*C
                       - 27*C*C + 18*A*B*C)
    assert discriminant % p
    points = [(x, y) for x in range(p) for y in range(p)
              if (y*y - x**3 - A*x*x - B*x - C) % p == 0]

    def plus(P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        x, y = P
        u, v = Q
        if x == u and (y+v) % p == 0:
            return None
        if P == Q:
            slope = (3*x*x + 2*A*x + B)*pow(2*y, -1, p) % p
        else:
            slope = (v-y)*pow(u-x, -1, p) % p
        w = (slope*slope - A - x-u) % p
        return w, (-y + slope*(x-w)) % p

    Q = (point[0] % p, point[1] % p)
    assert Q in points
    multiples = [None]
    R = None
    for n in range(1, len(points)+2):
        R = plus(R, Q)
        multiples.append(R)
        if R is None:
            break
    assert R is None
    return {'prime': p, 'curve_order': len(points)+1,
            'point_order': n, 'successive_multiples': multiples}


cases = [
    ('a=2', 2, -8, 0, (-1, 3), (5, 7)),
    ('CM j=0', 0, 0, 8, (1, 3), (5, 13)),
    ('CM j=1728', 0, -36, 0, (-3, -9), (5, 11)),
]
out = []
for name, A, B, C, Q, primes in cases:
    assert Q[1]**2 == Q[0]**3 + A*Q[0]**2 + B*Q[0] + C
    recs = [finite_record(A, B, C, Q, p) for p in primes]
    # A point order divisible by three at one good prime forces
    # three to divide a putative rational torsion order. Such torsion
    # injects at the other good prime (which is not three), where the
    # entire finite curve has order prime to three.
    assert any(r['point_order'] % 3 == 0 for r in recs)
    assert any(r['curve_order'] % 3 != 0 for r in recs)
    out.append({'name': name, 'coefficients_A_B_C': [A, B, C],
                'point': Q, 'double': [str(t) for t in twice(A, B, Q)],
                'good_reduction_certificates': recs,
                'conclusion': 'non-torsion over Q by prime-to-p torsion injection'})

assert twice(2, -8, (-1, 3)) == (F(9, 4), F(15, 8))
print(json.dumps({'cases': out,
                  'generic_consequence': 'The rational marked Prym section is not torsion, because a torsion section would specialize to torsion at the smooth fibre a=2.',
                  'scope': 'This proves non-torsion. It does not identify a full-GT frame character or infer geometric mod-three indivisibility from arithmetic specialization.'},
                 indent=2))
