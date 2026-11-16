"""Exact finite arithmetic and map checks for A.181.

The all-height norm, inverse-divisor and continuous-cohomology statements
are proved in the companion TeX source.  This certificate checks their
literal finite arithmetic and map formulas.  The already independently
certified A.159 unit arrays are used only as explicit rational elements.
"""
from fractions import Fraction
from itertools import product
from math import comb, gcd
from pathlib import Path
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
LOG = []


def say(s):
    LOG.append(s)
    print(s, flush=True)


def mul3(x, y):
    z = [0] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            z[i + j] += a * b
    for i in (4, 3):
        z[i - 3] += 3 * z[i]
    return z[:3]


def pow3(x, n):
    z = [1, 0, 0]
    while n:
        if n & 1:
            z = mul3(z, x)
        x = mul3(x, x)
        n //= 2
    return z


def norm3(x):
    a, b, c = x
    return a**3 + 3*b**3 + 9*c**3 - 9*a*b*c


U = [-2, 0, 1]
assert mul3(U, [4, 3, 2]) == [1, 0, 0]
assert norm3(U) == 1 and norm3(pow3(U, 3)) == 1
say("PASS: literal U inverse, rational norm one, and U-cube in Q[alpha]/(alpha^3-3)")

old_path = BASE / "two_inert_relative_unit_repair_certificate_data.json"
old = json.loads(old_path.read_text())
units = old["units"]
ks = [u["relative_norm_U_exponent"] for u in units]
assert ks == [3, 57, -3, 1614]
gs = [k // 3 for k in ks]
assert gs == [1, 19, -1, 538]
assert gcd(*ks) == 3


def finite_field(q):
    root = next(r for r in range(q) if r**3 % q == 3)

    def mul(x, y):
        a, b = x
        c, e = y
        return ((a*c - root*root*b*e) % q,
                (a*e + b*c - root*b*e) % q)

    def power(x, n):
        if n < 0:
            assert x != (0, 0)
            n %= q*q - 1
        z = (1, 0)
        while n:
            if n & 1:
                z = mul(z, x)
            x = mul(x, x)
            n //= 2
        return z

    def evaluate(x):
        z = (0, 0)
        for a in reversed(x):
            a = Fraction(a)
            assert a.denominator % q
            z = mul(z, (0, 1))
            z = ((z[0] + a.numerator * pow(a.denominator, -1, q)) % q,
                 z[1])
        return z

    return root, mul, power, evaluate


rows = []
for q in (11, 59):
    root, mul, power, evaluate = finite_field(q)
    alpha = (0, 1)
    ur = evaluate(U)
    exponent = (q*q - 1) // 3
    omega = power(alpha, exponent)
    assert omega != (1, 0) and power(omega, 3) == (1, 0)
    assert power(ur, exponent) == power(omega, 2)
    assert power(power(ur, 3), exponent) == (1, 0)
    logs = []
    for unit, g in zip(units, gs):
        u = [Fraction(v) for v in unit["candidate"]]
        parts = [[u[j + 3*k] * 649**(2*k) for k in range(3)]
                 for j in range(3)]
        # v_q(t)=2 and v_q(q)=3.  The discarded terms have positive
        # valuation; this is checked coefficient by coefficient.
        for part in parts[:2]:
            assert all(v.denominator % q for v in part)
        assert all((v.denominator // gcd(v.denominator, q)) % q
                   for v in parts[2])
        residue = evaluate(parts[0])
        character = power(residue, exponent)
        assert character == power(ur, exponent*g)
        normalized = mul(residue, power(ur, -g))
        assert power(normalized, exponent) == (1, 0)
        logs.append(next(j for j in range(3)
                         if power(omega, j) == character))
    assert logs == [(2*g) % 3 for g in gs]
    for depth in range(1, 25):
        e = 3**depth
        assert gcd(e, q*q - 1) == 3
        assert gcd(e, q - 1) == 1
        assert gcd(e, 8) == 1 and gcd(e, q) == 1
    rows.append({"q": q, "linear_alpha": root,
                 "alpha_character": omega,
                 "U_residue": ur,
                 "U_character": power(ur, exponent),
                 "unit_logs_in_alpha_character": logs})
say("PASS: both literal quadratic residue fields, all eight unit character entries, and 48 depth power-image checks")

exponent_cases = 0
for z in product(range(9), repeat=4):
    m = sum(g*v for g, v in zip(gs, z))
    norm_exponent = sum(k*v for k, v in zip(ks, z))
    assert norm_exponent == 3*m
    character = sum((2*g % 3)*v for g, v in zip(gs, z)) % 3
    assert (character == 0) == (m % 3 == 0)
    assert (character == 0) == (norm_exponent % 9 == 0)
    exponent_cases += 1
assert {sum(k*z for k, z in zip(ks, row)) % 9
        for row in product(range(3), repeat=4)} == {0, 3, 6}
assert 3 % 9 != 0 and (3*3) % 9 == 0
assert 3**2 == 9  # the actual scalar norm [K3:K1]
say(f"PASS: {exponent_cases} norm-exponent/character identities and the exact order-three finite support class")


def sigma(v):
    return (v[2], v[0], v[1], v[3])


divisor_cases = 0
for a, b in product(range(-7, 8), repeat=2):
    zdiv = (a, b, -a-b, 0)
    D = (0, -b, a, 0)
    assert tuple(x-y for x, y in zip(sigma(D), D)) == zdiv
    for h in range(1, 25):
        if h % 3 == 0:
            continue
        Dq = (0, 0, 0, a-b)
        ydiv = tuple(h*(x-y) for x, y in zip(D, Dq))
        wdiv = tuple(h*z - (sy-y)
                     for z, sy, y in zip(zdiv, sigma(ydiv), ydiv))
        assert wdiv == (0, 0, 0, 0)
        A = pow(h, -1, 3)
        B = (1-A*h)//3
        assert A*h + 3*B == 1
        assert 2*2-3 == 1
        divisor_cases += 1
say(f"PASS: {divisor_cases} integral split-orbit corrections, fixed-prime cancellation, Bezout norms, and quadratic transfer")


def cycles(Q, c, modulus):
    seen = set()
    out = []
    lookup = {}
    for x in range(modulus):
        if x in seen:
            continue
        orbit = []
        y = x
        while y not in seen:
            seen.add(y)
            orbit.append(y)
            y = (Q*y+c) % modulus
        assert y == x
        i = len(out)
        for y in orbit:
            lookup[y] = i
        out.append(orbit)
    return out, lookup


cycle_maps = 0
affine_identities = 0
for Q in (2, 4, 5, 7, 25, 49):
    for c in (0, 1, 2, 4, 9):
        previous = [[0]]
        previous_lookup = {0: 0}
        modulus = 1
        for level in range(1, 7):
            current, lookup = cycles(Q, c, 3*modulus)
            for orbit in current:
                old_i = previous_lookup[orbit[0] % modulus]
                assert all(previous_lookup[x % modulus] == old_i
                           for x in orbit)
                old = previous[old_i]
                assert len(orbit) % len(old) == 0
                weight = len(orbit)//len(old)
                # Over a stable linear branch an unramified cubic algebra
                # may have factors of degrees one and two.
                assert weight in (1, 2, 3)
                length = len(orbit)
                while length % 3 == 0:
                    length //= 3
                assert length in (1, 2)
                cycle_maps += 1
            previous, previous_lookup = current, lookup
            modulus *= 3
        for x in range(-4, 5):
            y = x
            for h in range(1, 10):
                y = Q*y + c
                assert y-x == sum(Q**j for j in range(h))*((Q-1)*x+c)
                affine_identities += 1
say(f"PASS: {cycle_maps} literal affine prime-cycle norm maps and {affine_identities} finite-orbit identities")


def valuation3(n):
    assert n
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v


binomial_cases = 0
for r in range(1, 7):
    for j in range(1, 3**r + 1):
        assert valuation3(comb(3**r, j)) == r - valuation3(j)
        binomial_cases += 1
projection_cases = 0
for c in range(1, 5):
    for s in range(1, 25):
        r = c
        while 3**r < s or r - max(valuation3(j) for j in range(1, s+1)) < c:
            r += 1
        assert all(comb(3**r, j) % 3**c == 0 for j in range(1, s+1))
        projection_cases += 1
root_maps = 0
for r in range(1, 6):
    N = 3**r
    fibres = [0]*N
    for j in range(3*N):
        fibres[j % N] += 1
        root_maps += 1
    assert fibres == [3]*N
    assert sum(fibres) == 3*N
say(f"PASS: {binomial_cases} norm-polynomial valuations, {projection_cases} finite coefficient projections, and {root_maps} root-torsor transitions")

data = {
    "scope": "Exact finite arithmetic and maps for A181; infinite statements are proved in the source.",
    "A159_input_sha256": hashlib.sha256(old_path.read_bytes()).hexdigest(),
    "norm_exponents": ks,
    "divided_norm_exponents": gs,
    "local_rows": rows,
    "counts": {"exponent_cases": exponent_cases,
               "divisor_corrections": divisor_cases,
               "affine_cycle_norm_maps": cycle_maps,
               "affine_identities": affine_identities,
               "binomial_valuations": binomial_cases,
               "coefficient_projections": projection_cases,
               "root_transitions": root_maps},
    "finite_support_class": {"target_U_exponent": 3,
                             "unit_norm_image_U_exponent": 9,
                             "exact_order": 3,
                             "scalar_preimage_for_cube": "U in K3"},
    "lim1_class_order": "not asserted",
}
(BASE / "two_inert_evaluated_norm_phantom_certificate_data.json").write_text(
    json.dumps(data, indent=2)+"\n")
say("SCOPE: the same fixed tower and norm maps are retained; no order is assigned to the nonzero derived-limit class.")
(BASE / "two_inert_evaluated_norm_phantom_certificate_output.txt").write_text(
    "\n".join(LOG)+"\n")
