#!/usr/bin/env python3
"""Exact finite audit for A146; it does not prove the analytic density limit.

Outputs finite CRT densities, every good special-fibre point through p=251,
and complete elliptic finite-group checks at detecting primes through p=3000.
The infinite-prime tail estimates are proved in the accompanying TeX source.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
DATA = HERE / "harmonic_infinite_primary_data.json"


def primes_to(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = b"\x00" * (((n - p * p) // p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


PRIMES = primes_to(3000)
K = 573
N = 1146
Q0 = Fraction(325596479663, 72962)
A = K * Q0 * Q0


def good(p):
    return p != 2 and K % p and Q0.numerator % p and Q0.denominator % p


def residue(q, p):
    q = Fraction(q)
    return q.numerator * pow(q.denominator, -1, p) % p


def curve_points(p, coeff):
    roots = {}
    for y in range(p):
        roots.setdefault(y * y % p, []).append(y)
    out = [None]
    for x in range(p):
        for y in roots.get((x**3 + coeff * x) % p, []):
            out.append((x, y))
    return out


def add(P, Q, p, coeff):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    xx, yy = Q
    if x == xx:
        if (y + yy) % p == 0:
            return None
        slope = (3 * x * x + coeff) * pow(2 * y, -1, p) % p
    else:
        slope = (yy - y) * pow(xx - x, -1, p) % p
    xr = (slope * slope - x - xx) % p
    return xr, (slope * (x - xr) - y) % p


def mul(n, P, p, coeff):
    ans = None
    while n:
        if n & 1:
            ans = add(ans, P, p, coeff)
        P = add(P, P, p, coeff)
        n >>= 1
    return ans


def phi(P, p):
    if P is None or P[0] == 0:
        return None
    x, y = P
    invx = pow(x, -1, p)
    return ((x - N * N * invx) * pow(4, -1, p) % p,
            y * (1 + N * N * invx * invx) * pow(8, -1, p) % p)


def squarefree(n):
    for p in PRIMES:
        if p * p > n:
            return True
        if n % (p * p) == 0:
            return False
    return True


def encoded(P):
    return "O" if P is None else list(P)


data = {"finite_CRT": [], "special_fibres": [], "reduction_groups": []}

# Literal reduced-residue enumeration for all mixed patterns at 3, 5, 7.
crt_primes = (3, 5, 7)
crt_residues = 0
for mask in range(1 << len(crt_primes)):
    selected = {p for i, p in enumerate(crt_primes) if mask >> i & 1}
    moduli = {p: p if p in selected else p * p for p in crt_primes}
    modulus = 8
    expected = Fraction(1, 4)
    phi_modulus = 4
    for p in crt_primes:
        modulus *= moduli[p]
        phi_q = p - 1 if p in selected else p * (p - 1)
        phi_modulus *= phi_q
        expected *= 1 - Fraction(1, phi_q)
    allowed = 0
    units = 0
    for u in range(modulus):
        if gcd(u, modulus) != 1:
            continue
        units += 1
        if u % 8 == 3 and all(u % moduli[p] != moduli[p] - 1
                             for p in crt_primes):
            allowed += 1
    assert units == phi_modulus
    assert Fraction(allowed, units) == expected
    crt_residues += modulus
    data["finite_CRT"].append({
        "S": sorted(selected), "modulus": modulus, "units": units,
        "allowed": allowed, "density": str(expected)})
print("Finite mixed CRT density identities:", len(data["finite_CRT"]),
      "patterns;", crt_residues, "literal residues checked.")

# The actual good plane quartic, its map q, then phi and t=-4T(T-1).
total_model_points = 0
for p in PRIMES:
    if p > 251:
        break
    if not good(p):
        continue
    a = residue(A, p)
    q0 = residue(Q0, p)
    h = pow(2, -1, p)
    fourth_roots = {}
    for w in range(p):
        fourth_roots.setdefault(a * pow(w, 4, p) % p, []).append(w)
    points = 1  # unique infinity point, mapping to O_E then O_F
    boundary = [("infinity", "O")]
    for t in range(p):
        f = t * (t - 1) * (t - h) % p
        for w in fourth_roots.get(f, []):
            points += 1
            P = (N * (2 * t - 1) % p, 8 * K * K * q0 * w * w % p)
            x, y = P
            assert (y * y - x**3 + N * N * x) % p == 0
            Z = phi(P, p)
            if Z is not None:
                u, v = Z
                assert (v * v - u**3 - K * K * u) % p == 0
            is_boundary = t in (0, 1, h)
            assert (Z in (None, (0, 0))) == is_boundary
            tripod = -4 * t * (t - 1) % p
            assert (tripod in (0, 1)) == is_boundary
            if is_boundary:
                assert w == 0
                # F'(t) = 3t^2 - 3t + 1/2, unit at each branch point.
                assert (3 * t * t - 3 * t + h) % p != 0
                boundary.append((t, encoded(Z)))
    assert len(boundary) == 4
    total_model_points += points
    data["special_fibres"].append({"p": p, "points": points, "boundary": boundary})
print("Actual good plane-quartic special fibres:", len(data["special_fibres"]),
      "primes;", total_model_points, "points and all four boundary images checked.")

# At p=3 mod8 with (p+1)/4 squarefree, an integer realizing all odd
# divisibilities and arbitrary 2-primary data is the 2-primary projector c.
total_E_points = 0
for p in PRIMES:
    if not good(p) or p % 8 != 3 or not squarefree((p + 1) // 4):
        continue
    E = curve_points(p, -(N * N))
    F = curve_points(p, K * K)
    assert len(E) == len(F) == p + 1
    odd = (p + 1) // 4
    c = odd * pow(odd, -1, 4)
    assert c % 4 == 1 and c % odd == 0
    E2 = {None, (0, 0), (N % p, 0), (-N % p, 0)}
    assert len(E2) == 4
    reduced_images = set()
    for P in E:
        two_part = mul(c, P, p, -(N * N))
        assert two_part in E2
        Z = phi(two_part, p)
        assert Z in (None, (0, 0))
        assert Z == mul(c, phi(P, p), p, K * K)
        reduced_images.add(Z)
    assert reduced_images == {None, (0, 0)}
    total_E_points += len(E)
    data["reduction_groups"].append({
        "p": p, "order": p + 1, "odd_squarefree_part": odd,
        "two_primary_projector": c, "image": ["O", [0, 0]]})
print("Complete detecting-prime finite-group checks:", len(data["reduction_groups"]),
      "primes;", total_E_points, "E-points, exact projectors, and commuting isogeny images.")

# A finite lower estimate for the empty-S product and elementary convergent tail.
product = Fraction(1, 4)
for p in PRIMES:
    if p != 2:
        product *= 1 - Fraction(1, p * (p - 1))
data["empty_S_product_through_3000"] = str(product)
data["empty_S_product_decimal"] = float(product)
data["counts"] = {"CRT_patterns": len(data["finite_CRT"]),
                  "CRT_residues": crt_residues,
                  "model_primes": len(data["special_fibres"]),
                  "model_points": total_model_points,
                  "group_primes": len(data["reduction_groups"]),
                  "group_points": total_E_points}
print("Finite empty-S product through 3000:", format(float(product), ".12f"),
      "(finite comparison, not the proof of the limiting density).")
DATA.write_text(json.dumps(data, indent=2) + "\n")
print("ALL EXACT INFINITE-PRIMARY FINITE CERTIFICATES PASSED.")
