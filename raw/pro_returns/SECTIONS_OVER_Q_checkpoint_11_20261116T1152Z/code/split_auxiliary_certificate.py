"""Exact finite identities for A.55; no numerical approximations.

The order-sixteen cocycle identity for every N=2^r, r>=4,
is the N/16 coefficient image of the exhaustive N=16 check.
The global reciprocity and Poitou--Tate statements are proved
in the accompanying TeX, not inferred from these calculations.
"""

from fractions import Fraction
from pathlib import Path


def beta(lam):
    assert lam % 2
    return ((lam * lam - 1) // 8) % 2


def log5(lam):
    possibilities = [
        j for j in range(4)
        if lam % 16 in (pow(5, j, 16), -pow(5, j, 16) % 16)
    ]
    assert len(possibilities) == 1
    return possibilities[0]


def choose2(n):
    return n * (n - 1) // 2


def zeta(lam, b, modulus):
    assert modulus % 16 == 0
    assert b % 2 == beta(lam)
    return (modulus // 16 * b + modulus // 2 * choose2(log5(lam))) % modulus


messages = []
modulus = 16
units = list(range(1, modulus, 2))
states = [(lam, b) for lam in units for b in range(modulus)
          if b % 2 == beta(lam)]
count = 0
for lam, b in states:
    assert log5(lam) % 2 == beta(lam)
    for mu, c in states:
        product_lam = lam * mu % modulus
        product_b = (b + lam * c) % modulus
        lhs = zeta(product_lam, product_b, modulus)
        rhs = (zeta(lam, b, modulus) +
               pow(lam, -1, modulus) * zeta(mu, c, modulus)) % modulus
        assert lhs == rhs
        assert (log5(product_lam) - log5(lam) - log5(mu)) % 4 == 0
        count += 1
messages.append(f"Twisted cocycle identities modulo16, exhaustively: {count} passed.")

coefficient_count = 0
for exponent in range(4, 13):
    modulus = 2 ** exponent
    for lam, b in states:
        zz = zeta(lam, b, modulus)
        assert 2 * zz % modulus == modulus // 8 * b % modulus
        assert 8 * zz % modulus == modulus // 2 * beta(lam) % modulus
        assert 16 * zz % modulus == 0
        assert zz == (modulus // 16 * zeta(lam, b, 16)) % modulus
        for mu in units:
            assert (modulus // 8 * (mu - pow(mu, -1, modulus))) % modulus == 0
        coefficient_count += 1
    # Evaluation at complex conjugation reduces a putative coboundary
    # for 8*zeta to these two constants; chi=5 excludes both.
    for constant in (0, modulus // 2):
        assert (-2 * constant) % modulus == 0
        assert ((pow(5, -1, modulus) - 1) * constant) % modulus == 0
        assert modulus // 2 != 0
messages.append(f"Coefficient comparisons and scaling checks: {coefficient_count} passed.")
messages.append("Exact order16: both constants permitted by complex conjugation fail at chi=5.")

pairing_count = 0
for exponent in range(4, 17):
    modulus = 2 ** exponent
    q = 73
    inertia_dual = modulus // 16 * 24 % modulus
    assert inertia_dual == modulus // 2
    # z is unramified and z(Frob)=1.  Only the (Frob,T) term
    # survives in the strict residue of z cup zeta.
    residue = pow(q, -1, modulus) * (q * q * inertia_dual) % modulus
    assert residue == modulus // 2
    assert Fraction(residue, modulus) == Fraction(1, 2)
    assert (q * q - 1) % 16 == 0
    assert (pow(q, -1, modulus) - q) * inertia_dual % modulus == 0
    pairing_count += 1
messages.append(f"Explicit q=73 pairing invariants equal 1/2: {pairing_count} passed.")


def primes_below(bound):
    return [n for n in range(2, bound)
            if all(n % d for d in range(2, int(n ** 0.5) + 1))]


def valuation(n, ell):
    answer = 0
    while n % ell == 0:
        answer += 1
        n //= ell
    return answer


bockstein_count = 0
for ell in (2, 3, 5, 7):
    for exponent in range(1, 5):
        modulus = ell ** exponent
        for q in primes_below(101):
            if q == ell:
                continue
            residue_modulus = ell ** valuation(q - 1, ell)
            for inertia in range(modulus):
                if (q - 1) * inertia % modulus:
                    continue
                residue = (q - 1) * inertia // modulus
                assert (residue % residue_modulus == 0) == (inertia == 0)
                bockstein_count += 1
messages.append(f"Local Bockstein zero iff finite inertia zero: {bockstein_count} passed.")

output = "\n".join(messages) + "\n"
Path(__file__).with_name("split_auxiliary_certificate_output.txt").write_text(output)
print(output, end="")
