#!/usr/bin/env python3
"""Independent check of the saved A16 certificates, without SymPy.

All operations in F2[v] use carryless integer arithmetic.  The program reads
the candidate's saved data without executing or modifying its generator.
It verifies the universal identities as identities of rational functions,
not by specializing to sample parameters.  Mathematical exhaustiveness is
reviewed separately in audit/A_order_sixteen_independent_review.md.
"""
from dataclasses import dataclass
from pathlib import Path
import json


def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def divmod2(a, b):
    if not b:
        raise ZeroDivisionError
    q = 0
    while a and a.bit_length() >= b.bit_length():
        shift = a.bit_length() - b.bit_length()
        q ^= 1 << shift
        a ^= b << shift
    return q, a


def gcd2(a, b):
    while b:
        a, b = b, divmod2(a, b)[1]
    return a


def bits(a):
    assert a and all(c in (0, 1) for c in a)
    return sum(c << i for i, c in enumerate(a))


@dataclass(frozen=True)
class Frac:
    n: int
    d: int = 1

    def __post_init__(self):
        if not self.d:
            raise ZeroDivisionError
        g = gcd2(self.n, self.d)
        object.__setattr__(self, "n", divmod2(self.n, g)[0])
        object.__setattr__(self, "d", divmod2(self.d, g)[0])

    def __add__(self, other):
        if not isinstance(other, Frac):
            other = Frac(other)
        return Frac(mul(self.n, other.d) ^ mul(other.n, self.d),
                    mul(self.d, other.d))

    __radd__ = __add__

    def __mul__(self, other):
        if not isinstance(other, Frac):
            other = Frac(other)
        return Frac(mul(self.n, other.n), mul(self.d, other.d))

    __rmul__ = __mul__

    def __truediv__(self, other):
        return Frac(mul(self.n, other.d), mul(self.d, other.n))

    def __pow__(self, power):
        assert power >= 0
        out = Frac(1)
        for _ in range(power):
            out *= self
        return out


ZERO = Frac(0)
ONE = Frac(1)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == ZERO:
        a.pop()
    return a or [ZERO]


def add(a, b):
    out = [ZERO] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] = out[i] + c
    for i, c in enumerate(b):
        out[i] = out[i] + c
    return trim(out)


def times(a, b):
    out = [ZERO] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i+j] = out[i+j] + c*d
    return trim(out)


def scale(a, c):
    return trim([q*c for q in a])


def decode_x(a):
    return trim([Frac(bits(c["numerator"]), bits(c["denominator"])) for c in a])


def strip(a):
    assert a
    for divisor in (2, 3):  # v and v+1
        while True:
            q, r = divmod2(a, divisor)
            if r:
                break
            a = q
    return a


def local_ring_denominator(a):
    return strip(a) == 1


def ztimes(a, b):
    """z-polynomials whose coefficients are F2(v)[x]-polynomials."""
    out = [[ZERO] for _ in range(len(a) + len(b) - 1)]
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i+j] = add(out[i+j], times(c, d))
    return out


def zadd(a, b):
    return [add(a[i] if i < len(a) else [ZERO],
                b[i] if i < len(b) else [ZERO])
            for i in range(max(len(a), len(b)))]


def quotient(a, b):
    return Frac(a, b)


def expanded_coefficients(a, b):
    """Derive the z coefficients directly from the displayed rational form."""
    t = Frac(1 << 8)
    l3 = Frac((1 << 4) ^ a)
    l2 = Frac((1 << 4) ^ (a ^ b))
    l1 = Frac(a ^ b)
    n1 = quotient((1 << 2) ^ a, 1 << 4)
    table = {
        (0, 0): quotient((1 << 4) ^ (1 << 2) ^ 2 ^ 1, 1 << 6),
        (1, 0): quotient((1 << 3) ^ 1, 1 << 5),
        (0, 1): quotient((1 << 4) ^ 2 ^ 1, 1 << 6),
        (1, 1): quotient((1 << 3) ^ 2 ^ 1, 1 << 5),
    }
    m1 = table[a, b]
    x = [ZERO, ONE]
    x2 = times(x, x)
    if a ^ b:
        m0 = add(add(scale(x2, l2*Frac(b ^ 1) + ONE), scale(x, l2*m1)),
                 [Frac(b)*m1*m1 + n1*n1 + m1*n1])
        m0 = add(m0, x)
        m0 = scale(m0, ONE/(l2*n1))
    else:
        m0 = scale(add(scale(x2, Frac(b ^ 1)), scale(x, m1)), ONE/n1)
    M = [m0, [m1], [ONE]]
    N = [x, [n1]]
    L0 = [[Frac(b)], [l1], [l2], [l3], [t]]
    H = [[ONE], [ZERO], [ZERO], [ONE]]
    N2 = ztimes(N, N)
    d = zadd(ztimes(M, M), [[ZERO]] + N2)
    core = zadd(ztimes([[ONE], [ONE]], N2), ztimes(M, N))
    form = zadd(ztimes(L0, d), ztimes(H, core))
    assert form[8] == [t]
    assert form[7] == form[6] == [ZERO]
    if a ^ b:
        assert add(scale(form[1], l2), form[2]) == [ZERO]
    else:
        assert form[1] == [ZERO]
    return [form[5], form[2], form[3],
            add(times(form[4], form[4]), scale(form[0], t))], m0


PHI = 31  # v^4+v^3+v^2+v+1


def fmul(a, b):
    return divmod2(mul(a, b), PHI)[1]


def fpow(a, n):
    out = 1
    while n:
        if n & 1:
            out = fmul(out, a)
        a = fmul(a, a)
        n //= 2
    return out


def reduce_frac(a):
    n = divmod2(a.n, PHI)[1]
    d = divmod2(a.d, PHI)[1]
    assert d
    return fmul(n, fpow(d, 14))


def ftrim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a or [0]


def fadd(a, b):
    return ftrim([(a[i] if i < len(a) else 0) ^
                  (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))])


def ftimes(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i+j] ^= fmul(c, d)
    return ftrim(out)


def feval(a, x):
    out = 0
    for c in reversed(a):
        out = fmul(out, x) ^ c
    return out


def main():
    here = Path(__file__).parent
    data = json.loads((here / "A_cubic_order_sixteen_candidate.json").read_text())
    records = []
    exception = None
    for case in data["cases"]:
        a, b = case["a"], case["b"]
        ps = [decode_x(q) for q in case["P"]]
        direct, m0 = expanded_coefficients(a, b)
        assert ps == direct
        assert m0 == decode_x(case["m0"])
        assert all(local_ring_denominator(c.d) for q in ps for c in q)
        obstructions = []
        for i in (1, 2):
            cert = case[f"bezout_{i}"]
            u, w = decode_x(cert["U"]), decode_x(cert["W"])
            assert all(c.d == 1 for q in (u, w) for c in q)
            rhs = bits(cert["right_hand_side"])
            assert add(times(u, ps[0]), times(w, ps[i])) == [Frac(rhs)]
            obstruction = bits(case[f"obstruction_{i}"])
            assert strip(rhs) == obstruction
            obstructions.append(obstruction)
        cu, cw = bits(case["combined_bezout_U"]), bits(case["combined_bezout_W"])
        g = bits(case["combined_gcd"])
        assert mul(cu, obstructions[0]) ^ mul(cw, obstructions[1]) == g
        assert g == (mul(PHI, PHI) if (a, b) == (0, 1) else 1)
        records.append({"a": a, "b": b, "coefficient_identity": True,
                        "both_universal_bezout_identities": True,
                        "obstruction_degrees": [q.bit_length()-1 for q in obstructions],
                        "combined_gcd_bits": g,
                        "denominators_supported_at_v_zero_or_one": True})
        if (a, b) == (0, 1):
            exception = ps, m0
    # Phi_5 has no linear factor and is not divisible by the unique irreducible
    # quadratic over F2, so this degree-four quotient is a field.
    assert divmod2(PHI, 2)[1] and divmod2(PHI, 3)[1]
    assert divmod2(PHI, 7)[1]
    assert all(fmul(a, fpow(a, 14)) == 1 for a in range(1, 16))
    exceptional_ps, exceptional_m0 = exception
    fps = [[reduce_frac(c) for c in q] for q in exceptional_ps]
    assert fps == data["exceptional_P_coefficients"]
    row = data["exceptional_bezout_row"]
    combo = [0]
    for u, q in zip(row, fps):
        combo = fadd(combo, ftimes(u, q))
    assert combo == [10, 1] == data["exceptional_common_gcd"]
    assert all(feval(q, 10) == 0 for q in fps)
    # The universal identity forces x=v^3+v at every root of Phi_5.
    n0 = 10
    n1 = reduce_frac(Frac(1, 1 << 2))
    m1 = reduce_frac(Frac((1 << 4) ^ 2 ^ 1, 1 << 6))
    m0 = feval([reduce_frac(c) for c in exceptional_m0], n0)
    assert (n1, m1, m0) == (8, 6, 11)
    root = fmul(n0, fpow(n1, 14))
    assert root == 9 == data["common_root_of_M_and_N"]
    assert feval([m0, m1, 1], root) == feval([n0, n1], root) == 0
    result = {
        "all_passed": True,
        "method": "Independent carryless binary polynomial and rational-function arithmetic; no generator execution and no parameter sampling.",
        "cases": records,
        "exceptional_field_polynomial_irreducible": True,
        "exceptional_bezout_identity": True,
        "exceptional_unique_x_bits": 10,
        "exceptional_shared_root_bits": root,
        "mathematical_review": "audit/A_order_sixteen_independent_review.md",
    }
    output = here / "A_order_sixteen_independent_review.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
