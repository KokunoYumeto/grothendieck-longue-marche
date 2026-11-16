"""Exact good-reduction torsion certificate for A.150's E_b/Q(sqrt(2)).

This enumerates every point over two literal degree-one residue fields.
The proof uses prime-to-residue-characteristic torsion injection; it does
not infer a Mordell-Weil rank from finite-field point counts.
"""
from math import gcd

M = 7 * 13 * 23 * 139 * 1119169
rows = []
for p, sqrt2, expected in [(17, 6, 10), (31, 8, 32)]:
    assert sqrt2 * sqrt2 % p == 2
    assert all(p % d for d in range(2, int(p ** 0.5) + 1))
    b = 1146 * (1 + sqrt2) ** 2 * M ** 2 % p
    discriminant = -64 * b ** 3 % p
    assert discriminant != 0
    points = [(x, y) for x in range(p) for y in range(p)
              if (y * y - x * x * x - b * x) % p == 0]
    assert len(points) + 1 == expected
    rows.append((p, sqrt2, b, discriminant, expected))
    print(f"p={p}; sqrt2={sqrt2}; b={b}; discriminant={discriminant}; "
          f"affine_points={len(points)}; group_order={expected}")
    print("affine points:", points)

assert gcd(rows[0][-1], rows[1][-1]) == 2
assert rows[1][-1] % 17 != 0
assert rows[0][-1] % 31 != 0
print("PASS: orders 10 and 32 bound every torsion primary part by C2;")
print("the displayed point (0,0) realizes that C2. E_b(K)_tors = C2.")
