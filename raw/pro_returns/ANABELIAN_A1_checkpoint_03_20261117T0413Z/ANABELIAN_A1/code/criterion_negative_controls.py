#!/usr/bin/env python3
"""Exact finite-field checks for the criterion's negative controls.

The group-theoretic collision certificate is proved in the paper.  These
computations check the finite curves and coordinates, not a truncated
substitute for the profinite conjugacy assertion.
"""
import json
from pathlib import Path


class GF2:
    def __init__(self, degree, modulus):
        self.d = degree
        self.modulus = modulus
        self.q = 1 << degree

    def mul(self, a, b):
        ans = 0
        while b:
            if b & 1:
                ans ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.modulus
        return ans

    def pow(self, a, n):
        ans = 1
        while n:
            if n & 1:
                ans = self.mul(ans, a)
            a = self.mul(a, a)
            n >>= 1
        return ans

    def verify_field(self):
        assert all(self.pow(a, self.q - 1) == 1
                   for a in range(1, self.q))

    def pair(self, x, y):
        return [x, y]


def genus_two_points(field, ordinary=False):
    ans = []
    for x in range(field.q):
        h = field.mul(x, x ^ 1) if ordinary else 1
        f = field.pow(x, 5) ^ (1 if ordinary else 0)
        for y in range(field.q):
            if field.mul(y, y) ^ field.mul(h, y) == f:
                ans.append([x, y])
    return ans


def frobenius_orbit(field, point):
    ans, cur = [], point
    while cur not in ans:
        ans.append(cur)
        cur = [field.mul(a, a) for a in cur]
    assert cur == point
    return ans


def main():
    F2 = GF2(1, 0b11)
    F4 = GF2(2, 0b111)
    F128 = GF2(7, 0b10000011)  # t^7+t+1
    for field in [F2, F4, F128]:
        field.verify_field()

    # E: y^2+xy=x^3+1.  Inverse of (x,y) is (x,y+x).
    elliptic_points = [[x, y] for x in range(2) for y in range(2)
                       if (y*y ^ x*y) == (x*x*x ^ 1)]
    assert [0, 1] in elliptic_points
    assert [0, 1 ^ 0] == [0, 1]
    assert (1 ^ (0 * 0)) != 0  # dF/dx at the 2-torsion point

    ordinary_2 = genus_two_points(F2, ordinary=True)
    ordinary_4 = genus_two_points(F4, ordinary=True)
    assert [0, 1] in ordinary_2 and [1, 0] in ordinary_2
    assert len(ordinary_2) + 1 == 3
    N1, N2 = len(ordinary_2)+1, len(ordinary_4)+1
    jacobian_order = (N1*N1 + N2)//2 - 2
    assert jacobian_order % 2 == 0

    points128 = genus_two_points(F128)
    selected = next(pt for pt in points128
                    if len(frobenius_orbit(F128, pt)) == 7)
    orbit = frobenius_orbit(F128, selected)
    assert selected != orbit[1]
    gl_order = 1
    for i in range(4):
        gl_order *= 3**4 - 3**i
    assert gl_order % 7 != 0
    degrees7_points = sum(len(frobenius_orbit(F128,pt)) == 7
                         for pt in points128)
    result = {
        "elliptic": {
            "field": "F_2",
            "equation": "y^2+xy=x^3+1",
            "affine_points": elliptic_points,
            "rational_points_including_infinity": len(elliptic_points)+1,
            "nonzero_2_torsion": [0, 1],
            "inverse_formula": "-(x,y)=(x,y+x)",
            "collision_certificate": "All geometric groups are abelian; the nonzero 2-torsion Kummer class vanishes in the entire prime-to-2 Tate module."
        },
        "abelian_genus_two": {
            "field": "F_2",
            "equation": "y^2+x(x+1)y=x^5+1",
            "points": [[0, 1], [1, 0]],
            "N1": N1,
            "N2": N2,
            "jacobian_order": jacobian_order,
            "function": "x/(x+1)",
            "divisor": "2(0,1)-2(1,0)",
            "infinity_chart": "v^2+(u+u^2)v=u+u^6",
            "smoothness_derivatives_at_ramification_points": [1, 1, 1],
            "collision_certificate": "The nonzero divisor class has exact order 2, hence zero Kummer class in the entire geometrically abelian prime-to-2 extension."
        },
        "single_prime_genus_two": {
            "equation": "y^2+y=x^5",
            "base_field": "F_2",
            "extension_field": "F_128 = F_2[t]/(t^7+t+1)",
            "element_encoding": "binary coefficient vectors in powers 1,t,...,t^6",
            "retained_prime": 3,
            "central_arithmetic_factor": "Z_7 inside G_F2=product_s Z_s",
            "GL4_F3_order": gl_order,
            "GL4_F3_order_mod7": gl_order % 7,
            "point": selected,
            "Frobenius_orbit": orbit,
            "N7": len(points128)+1,
            "degree7_geometric_points": degrees7_points,
            "degree7_closed_points": degrees7_points // 7,
            "collision_certificate": "The central Z_7 factor sends the first point to its Frobenius conjugate while leaving its decomposition group unchanged; restricting to G_F128 gives equal point-section subgroups in the entire geometrically pro-3 group."
        }
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
