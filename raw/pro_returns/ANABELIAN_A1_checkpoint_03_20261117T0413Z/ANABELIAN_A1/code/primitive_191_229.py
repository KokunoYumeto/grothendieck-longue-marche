"""Independent exact reconstruction of the two elliptic-torsion certificates.

Requires python-flint==0.9.0.  Output coefficient arrays use ascending
coefficients, each encoded as an unsigned 64-bit little-endian integer;
bit i is the coefficient of t^i in F_2[t]/M.
"""
from pathlib import Path
from functools import lru_cache
import hashlib
import json
import struct
import time
import sys
import os

from flint import fq_default_ctx, fq_default_poly_ctx, fmpz_mod_poly_ctx, nmod_poly

OUT = Path(__file__).resolve().parent / "primitive_certificates"
OUT.mkdir(exist_ok=True)
EXPONENTS = [38, 14, 10, 9, 8, 5, 2, 1, 0]
MOD_BITS = sum(1 << i for i in EXPONENTS)

def bmod(a, b):
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a

def bgcd(a, b):
    while b:
        a, b = b, bmod(a, b)
    return a

def bsquare(a):
    ans = 0
    i = 0
    while a:
        if a & 1:
            ans ^= 1 << (2 * i)
        a >>= 1
        i += 1
    return bmod(ans, MOD_BITS)

residues = [2]
for i in range(38):
    residues.append(bsquare(residues[-1]))
assert residues[38] == 2
assert bgcd(MOD_BITS, residues[2] ^ 2) == 1
assert bgcd(MOD_BITS, residues[19] ^ 2) == 1

coefficients = [int(i in EXPONENTS) for i in range(39)]
k = fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(coefficients),
                   var="t", fq_type=os.environ.get("ANABELIAN_FQ_TYPE", "FQ_NMOD"))
t = k.gen()
R = fq_default_poly_ctx(k)
u = R.gen()
d = t**3 + 1
assert d != 0
A = (u*u + t*t*u + t) / d
B = (t*u*u + u + t*t) / d
assert B + t*A == u

def psi_factory(x, one):
    @lru_cache(None)
    def psi(n):
        if n in (1, 2, 4):
            return one
        if n == 3:
            return x**4 + x
        if n % 2 == 0:
            return psi(n//2)**4
        m = (n-1)//2
        return psi(m+2)*psi(m)**3 + psi(m-1)*psi(m+1)**3
    return psi

psi_A = psi_factory(A, R.one())
psi_B = psi_factory(B, R.one())
X = nmod_poly([0, 1], 2)
ONE = nmod_poly([1], 2)
psi_X = psi_factory(X, ONE)

@lru_cache(None)
def reduced_multiple_x(n):
    """Use chord/tangent recurrences, independently of psi recurrence."""
    if n == 1:
        return X, ONE
    if n % 2 == 0:
        a, b = reduced_multiple_x(n//2)
        return a**4, b**4
    m = n//2
    a, b = reduced_multiple_x(m)
    c, e = reduced_multiple_x(m+1)
    s = a*e + c*b
    den = s*s
    num = X*den + (b*e)**2
    g = num.gcd(den)
    return num//g, den//g

def bits(element):
    return sum(int(c) << i for i, c in enumerate(element.to_list()))

def save_poly(name, poly):
    path = OUT / name
    data = b"".join(struct.pack("<Q", bits(c)) for c in poly)
    path.write_bytes(data)
    return {"file": path.name, "degree": poly.degree(),
            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

record = {"field_modulus_exponents": EXPONENTS,
          "field_modulus_bits": MOD_BITS,
          "successive_square_residues": residues,
          "irreducibility_gcd_degrees": {"2": 0, "19": 0},
          "coefficient_encoding": "ascending unsigned uint64 little endian; bit i=t^i",
          "python_flint": "0.9.0", "certificates": []}
print("Irreducibility of degree-38 field polynomial: PASS", flush=True)
conductors = tuple(map(int, sys.argv[1:])) or (191, 229)
for n in conductors:
    start = time.monotonic()
    psi = psi_X(n)
    num, den = reduced_multiple_x(n)
    assert den == psi*psi
    assert num.gcd(den) == ONE
    print(f"n={n}: independent denominator identity PASS; psi degree={psi.degree()}",
          flush=True)
    pa, pb = psi_A(n), psi_B(n)
    print(f"n={n}: compositions ready, degrees={pa.degree()},{pb.degree()}",
          flush=True)
    # Retain no previous recurrence cache during the extended Euclidean step.
    psi_A.cache_clear()
    psi_B.cache_clear()
    psi_X.cache_clear()
    reduced_multiple_x.cache_clear()
    g, v, w = pa.xgcd(pb)
    assert g == R.one()
    assert v*pa + w*pb == R.one()
    cert = {"n": n, "psi_degree": psi.degree(),
            "multiple_numerator_degree": num.degree(),
            "multiple_denominator_degree": den.degree(),
            "gcd_degree": g.degree(),
            "polynomials": [save_poly(f"n{n}_psi_A.bin", pa),
                            save_poly(f"n{n}_psi_B.bin", pb),
                            save_poly(f"n{n}_bezout_A.bin", v),
                            save_poly(f"n{n}_bezout_B.bin", w)],
            "seconds": round(time.monotonic()-start, 3)}
    record["certificates"].append(cert)
    (OUT / ("manifest_" + "_".join(map(str,conductors)) + ".json")).write_text(
        json.dumps(record, indent=2) + "\n")
    print(json.dumps(cert, indent=2), flush=True)
print("All two full Bezout identities: PASS", flush=True)
