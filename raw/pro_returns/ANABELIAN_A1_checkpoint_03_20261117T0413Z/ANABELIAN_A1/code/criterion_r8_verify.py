"""Independent, read-only verification of the R8 rational-witness certificates.

Run from the delivery directory with python-flint installed:
    python code/criterion_r8_verify.py

The field polynomials are checked by a separate binary Rabin implementation.
The stored divisor sequence is reconstructed by coprime CRT interpolation,
not by the producer's general Cantor-addition routine.  Doubling, normalized
Cartier scalars, all absolute-Frobenius products, and the extra symmetries are
then checked exactly.  No random choices or producer imports occur here.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import time

from flint import fq_default_ctx, fq_default_poly_ctx, fmpz_mod_poly_ctx

ROOT = Path(__file__).resolve().parent


def bit_rem(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def bit_gcd(a, b):
    while b:
        a, b = b, bit_rem(a, b)
    return a


def bit_square(a, modulus):
    ans = 0
    while a:
        low = a & -a
        ans ^= 1 << (2 * (low.bit_length() - 1))
        a ^= low
    return bit_rem(ans, modulus)


def prime_factors(n):
    ans = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            ans.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        ans.append(n)
    return ans


def binary_irreducible(modulus, degree):
    assert modulus.bit_length() == degree + 1 and modulus & 1
    checkpoints = {degree // p for p in prime_factors(degree)}
    x = 2
    records = []
    for i in range(1, degree + 1):
        x = bit_square(x, modulus)
        if i in checkpoints:
            g = bit_gcd(x ^ 2, modulus)
            assert g == 1
            records.append({"exponent": i, "residue": x, "gcd": g})
    assert x == 2
    return records


def multiplicative_order(a, n):
    t, j = a % n, 1
    while t != 1:
        t = t * a % n
        j += 1
    return j


def verify(ell):
    start = time.monotonic()
    source = ROOT / f"r8_rational_witness_{ell}.json"
    raw = source.read_bytes()
    data = json.loads(raw)
    degree = data["field_degree"]
    extension = data["constant_extension_degree"]
    assert data["ell"] == ell and data["base_field_degree"] == 38
    assert degree == 38 * extension
    assert prime_factors(ell) == [ell]
    assert extension == multiplicative_order(-2**19, ell)
    assert pow(2, degree, ell) == 1

    coeffs = data["field_modulus_coefficients"]
    modulus = sum(int(c) << i for i, c in enumerate(coeffs))
    rabin = binary_irreducible(modulus, degree)
    k = fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(coeffs), var="z", fq_type="FQ_NMOD")
    R = fq_default_poly_ctx(k)
    x, one, zero = R.gen(), R.one(), R.zero()

    def decode(n):
        assert isinstance(n, int) and 0 <= n < 2**degree
        return k([(n >> i) & 1 for i in range(n.bit_length())])

    def encode(a):
        return sum(int(v) << i for i, v in enumerate(a.to_list()))

    def poly(values):
        return R([decode(n) for n in values])

    def monic(a):
        assert a != zero
        return a / a[a.degree()]

    t = decode(data["t"])
    base_coeffs = [int(i in (38, 14, 10, 9, 8, 5, 2, 1, 0)) for i in range(39)]
    base_modulus = sum(c << i for i, c in enumerate(base_coeffs))
    base_rabin = binary_irreducible(base_modulus, 38)
    assert R(base_coeffs)(t) == 0
    assert t ** (2**38) == t and t**4 != t
    den = t**3 + 1
    A = (x*x + t*t*x + t) / den
    B = (t*x*x + x + t*t) / den
    J = (x**3 + 1) / den
    assert A**3 + B**3 == J**2 + J

    shift = poly(data["reduced_shift"])
    scale = decode(data["coordinate_scale"])
    reduced = A**3 + shift**2 + shift
    assert reduced.degree() == 5
    assert reduced[2] == reduced[4] == 0 and reduced[5] == scale
    assert scale == t*t / den**3
    h, f = poly(data["h"]), poly(data["f"])
    assert h == R([scale**-3])
    assert f == reduced.compose(scale*x) / scale**6
    assert f.degree() == 5 and f[5] == 1
    assert (f + h*R.zero()).degree() == 5

    divisors = [(one, zero)] + [(poly(d["u"]), poly(d["v"])) for d in data["divisors"]]
    assert len(divisors) == ell
    assert divisors[1] == (poly(data["torsion_divisor"]["u"]), poly(data["torsion_divisor"]["v"]))
    for u, v in divisors[1:]:
        assert u.degree() == 2 and u[2] == 1 and v.degree() < 2
        assert (v*v + h*v + f) % u == zero

    # The cubic interpolant is unique modulo u^2 because h is a unit.
    # Verify not just the target polynomial but the reduced y-coordinate.
    scalars = [k.zero()] * ell
    tangent_interpolants = [None] * ell
    for i in range(1, ell):
        u, v = divisors[i]
        Q, rem = divmod(v*v + h*v + f, u)
        assert rem == zero
        tangent = v + u * ((Q / h[0]) % u)
        norm, rem = divmod(tangent*tangent + h*tangent + f, u*u)
        assert rem == zero and tangent.degree() == 3
        target_u, target_v = divisors[2*i % ell]
        assert monic(norm) == target_u
        assert (tangent + h) % target_u == target_v
        assert norm == tangent[3]**2 * target_u
        c = tangent[3] * target_u[1]
        assert c != 0 and c == decode(data["cartier_scalars"][i-1])
        scalars[i] = c
        tangent_interpolants[i] = tangent

    # Reconstruct iD + D by CRT for every nonexceptional i.
    # This uses a different addition path from the producer's general xgcd
    # formula, and the one repeated-input case was checked by tangent above.
    u1, v1 = divisors[1]
    crt_count = 0
    for i in range(2, ell-1):
        u, v = divisors[i]
        gcd, inv, unused = u.xgcd(u1)
        assert gcd == one, (ell, i, "unexpected common support")
        interp = v + u * (((v1+v)*inv) % u1)
        assert interp % u == v and interp % u1 == v1
        norm, rem = divmod(interp*interp + h*interp + f, u*u1)
        assert rem == zero
        result_u = monic(norm)
        assert (result_u, (interp+h) % result_u) == divisors[i+1]
        crt_count += 1
    assert divisors[-1] == (u1, (v1+h) % u1)
    # Together, D != 0 and the preceding chain imply exact prime order ell.

    # Verify that the saved random elliptic points do lie on E and that the
    # sum of their pullbacks is the stated generator, by separate CRT again.
    elliptic_points = [tuple(map(decode, point)) for point in data["elliptic_points"]]
    pullbacks = []
    for which, (X, Y) in enumerate(elliptic_points, 1):
        assert Y*Y+Y == X**3
        abscissa = (A if which == 1 else B).compose(scale*x)
        u = monic(abscissa-X)
        y_shift = shift.compose(scale*x)
        if which == 2:
            y_shift += J.compose(scale*x)
        v = ((R([Y])+y_shift) / scale**3) % u
        assert (v*v+h*v+f) % u == zero
        pullbacks.append((u, v))
    u, v = pullbacks[0]
    w, z = pullbacks[1]
    gcd, inv, unused = u.xgcd(w)
    assert gcd == one
    interp = v + u * (((z+v)*inv) % w)
    norm, rem = divmod(interp*interp+h*interp+f, u*w)
    assert rem == zero
    result_u = monic(norm)
    assert (result_u, (interp+h) % result_u) == divisors[1]

    # Evaluate the product directly with separately accumulated squares,
    # rather than the producer's Horner-style recurrence.
    squared = []
    for c in scalars:
        row = [c]
        for s in range(1, degree):
            row.append(row[-1]**2)
        squared.append(row)
    multipliers = [k.zero()] * ell
    for i in range(1, ell):
        prod, j = k.one(), i
        for s in range(degree):
            prod *= squared[j][degree-1-s]
            j = 2*j % ell
        assert j == i
        assert prod == decode(data["linear_frobenius_multipliers"][i-1])
        assert prod != 0 and prod != 1
        multipliers[i] = prod

    # Consequences not used by the producer provide extra exact cross-checks.
    for i in range(1, ell):
        assert multipliers[2*i % ell] == multipliers[i]**2
        assert multipliers[-i % ell] == multipliers[i]
        assert multipliers[i]**(2**19) == multipliers[i]
        assert multipliers[(-2**19*i) % ell] == multipliers[i]**(2**38)

    # Record the distinct degree-19 minimal polynomials over F_2 and their
    # occurrence counts in the coherent q-Frobenius characteristic polynomial.
    minimal = Counter()
    for a in multipliers[1:]:
        conj, b = [], a
        while b not in conj:
            conj.append(b)
            b *= b
        assert b == a and len(conj) == 19
        polynomial = one
        for b in conj:
            polynomial *= x + b
        assert all(c == 0 or c == 1 for c in polynomial)
        bits = sum(int(c == 1) << i for i, c in enumerate(polynomial))
        minimal[bits] += 1
    assert all(count % 19 == 0 for count in minimal.values())
    return {
        "ell": ell,
        "field_degree": degree,
        "constant_extension_degree": extension,
        "field_modulus_bits": modulus,
        "field_rabin_tests": rabin,
        "base_rabin_tests": base_rabin,
        "source_sha256": sha256(raw).hexdigest(),
        "exact_prime_order": True,
        "checked_nonzero_divisors": ell-1,
        "checked_crt_additions": crt_count,
        "checked_tangent_doublings": ell-1,
        "checked_cartier_scalars": ell-1,
        "checked_frobenius_multipliers": ell-1,
        "multipliers_equal_one": 0,
        "all_multipliers_in_F2_19": True,
        "minimal_polynomial_bits_and_exponents": [
            {"bits": bits, "exponent": count//19} for bits, count in sorted(minimal.items())
        ],
        "ord_ell_2": multiplicative_order(2, ell),
        "seconds": time.monotonic()-start,
    }


if __name__ == "__main__":
    results = []
    for ell in (191, 229):
        result = verify(ell)
        results.append(result)
        print(json.dumps(result, sort_keys=True), flush=True)
    target = ROOT / "criterion_r8_verify.json"
    target.write_text(json.dumps({"verified": results}, indent=2)+"\n")
    print("Both certificates independently verified: exact orders, divisor arithmetic, and all Cartier/Frobenius multipliers.")
