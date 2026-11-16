"""Independent outside-S divisor certificate for compact S-unit candidates.

Every field operation is rational or finite polynomial arithmetic.
At primes outside S the monogenic equation is etale. Exact factor norms
and, where needed, literal Hensel factors compute each prime valuation.
The original compact expressions are never expanded.
"""
from pathlib import Path
from fractions import Fraction as Q
import json
import re
import sys
from collections import defaultdict
from math import isqrt
from sympy import Poly, Symbol, factorint

sys.set_int_max_str_digits(0)
base = Path(__file__).resolve().parent
d = 649
radicand = 3 * d**6
S = {2, 3, 11, 59}
raw = (base / "two_inert_compact_units_pari_output.txt").read_text()
candidates = defaultdict(list)
factor_index = {}
factors = []
for i, j, exponent, expression in re.findall(
    r"^SFACTOR (\d+) (\d+) (-?\d+) (\[.*\])$", raw, re.M
):
    polynomial = tuple(Q(s.strip()) for s in expression[1:-1].split(","))
    polynomial += (Q(0),) * (9 - len(polynomial))
    assert len(polynomial) == 9
    if polynomial not in factor_index:
        factor_index[polynomial] = len(factors)
        factors.append(polynomial)
    candidates[int(i)].append((int(exponent), factor_index[polynomial]))
assert sorted(candidates) == list(range(1, 9))


def field_multiply(x, y):
    z = [Q(0)] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            z[i + j] += a * b
    for k in (4, 3):
        z[k - 3] += 3 * z[k]
    return tuple(z[:3])


def field_cube(x):
    return field_multiply(field_multiply(x, x), x)


def relative_norm(x):
    A, B, C = [tuple(x[j + 3 * k] * d**(2 * k) for k in range(3)) for j in range(3)]
    w = (Q(0), Q(d * d), Q(0))
    terms = [
        field_cube(A),
        field_multiply(w, field_cube(B)),
        field_multiply(field_multiply(w, w), field_cube(C)),
        tuple(-3 * a for a in field_multiply(w, field_multiply(field_multiply(A, B), C))),
    ]
    return tuple(sum(term[i] for term in terms) for i in range(3))


def rational_norm(x):
    a, b, c = relative_norm(x)
    return a**3 + 3 * b**3 + 9 * c**3 - 9 * a * b * c


def valuation_integer(n, p):
    if n == 0:
        return 10**9
    n = abs(n)
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def valuation_fraction(q, p):
    return valuation_integer(q.numerator, p) - valuation_integer(q.denominator, p) if q else 10**9


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def polynomial_multiply(a, b, modulus=None):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    if modulus:
        c = [x % modulus for x in c]
    return trim(c)


def polynomial_subtract(a, b, modulus):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] -= x
    return trim([x % modulus for x in c])


def polynomial_divmod(a, b, modulus):
    a = trim([x % modulus for x in a])
    b = trim([x % modulus for x in b])
    assert b != [0]
    quotient = [0] * max(1, len(a) - len(b) + 1)
    lead_inverse = pow(b[-1], -1, modulus)
    while len(a) >= len(b) and a != [0]:
        degree = len(a) - len(b)
        coefficient = a[-1] * lead_inverse % modulus
        quotient[degree] = coefficient
        for j, x in enumerate(b):
            a[degree + j] = (a[degree + j] - coefficient * x) % modulus
        trim(a)
    return trim(quotient), a


def inverse_polynomial(a, modulus_polynomial, p):
    r0, r1 = modulus_polynomial[:], a[:]
    t0, t1 = [0], [1]
    while r1 != [0]:
        quotient, remainder = polynomial_divmod(r0, r1, p)
        r0, r1 = r1, remainder
        t0, t1 = t1, polynomial_subtract(t0, polynomial_multiply(quotient, t1, p), p)
    assert len(r0) == 1 and r0[0] != 0
    scaled = [v * pow(r0[0], -1, p) % p for v in t0]
    return polynomial_divmod(scaled, modulus_polynomial, p)[1]


def is_prime_trial(p):
    return p >= 2 and all(p % q for q in range(2, isqrt(p) + 1))


def polynomial_power(a, exponent, modulus_polynomial, p):
    result = [1]
    while exponent:
        if exponent & 1:
            result = polynomial_divmod(polynomial_multiply(result, a, p), modulus_polynomial, p)[1]
        a = polynomial_divmod(polynomial_multiply(a, a, p), modulus_polynomial, p)[1]
        exponent //= 2
    return result


def polynomial_gcd(a, b, p):
    while b != [0]:
        a, b = b, polynomial_divmod(a, b, p)[1]
    return [v * pow(a[-1], -1, p) % p for v in a]


def certify_irreducible(g, p):
    degree = len(g) - 1
    xbar = polynomial_divmod([0, 1], g, p)[1]
    assert polynomial_power(xbar, p**degree, g, p) == xbar
    for divisor in factorint(degree):
        frobenius = polynomial_power(xbar, p**(degree // int(divisor)), g, p)
        assert polynomial_gcd(polynomial_subtract(frobenius, xbar, p), g, p) == [1]


x = Symbol("x")
defining = [-radicand] + [0] * 8 + [1]
residue_factors = {}
hensel_calls = 0
hensel_records = []


def get_factors(p):
    if p not in residue_factors:
        assert is_prime_trial(p)
        factorization = Poly(x**9 - radicand, x, modulus=p).factor_list()[1]
        rows = []
        for factor, exponent in factorization:
            assert exponent == 1
            rows.append([int(factor.nth(i)) % p for i in range(factor.degree() + 1)])
        rows.sort(key=lambda row: (len(row), row))
        product = [1]
        for row in rows:
            certify_irreducible(row, p)
            product = polynomial_multiply(product, row, p)
        assert product == [a % p for a in defining]
        residue_factors[p] = rows
    return residue_factors[p]


def hensel_factor(g0, p, precision):
    global hensel_calls
    hensel_calls += 1
    h0, remainder = polynomial_divmod([a % p for a in defining], g0, p)
    assert remainder == [0]
    inverse_h = inverse_polynomial(h0, g0, p)
    g, h = g0[:], h0[:]
    modulus = p
    for _ in range(1, precision):
        product = polynomial_multiply(g, h)
        product += [0] * (10 - len(product))
        error = []
        for target, value in zip(defining, product):
            assert (target - value) % modulus == 0
            error.append(((target - value) // modulus) % p)
        dg = polynomial_divmod(polynomial_multiply(error, inverse_h, p), g0, p)[1]
        remaining = polynomial_subtract(error, polynomial_multiply(dg, h0, p), p)
        dh, rem = polynomial_divmod(remaining, g0, p)
        assert rem == [0]
        assert len(dg) < len(g0) and len(dh) < len(h0)
        for i, value in enumerate(dg):
            g[i] += modulus * value
        for i, value in enumerate(dh):
            h[i] += modulus * value
        modulus *= p
        g = [a % modulus for a in g]
        h = [a % modulus for a in h]
    assert polynomial_multiply(g, h, modulus) == [a % modulus for a in defining]
    hensel_records.append({"p": p, "precision": precision, "initial": g0, "lifted": g})
    return g


norms = []
norm_factorizations = []
prime_supports = []
for index, polynomial in enumerate(factors):
    norm = rational_norm(polynomial)
    assert norm != 0
    norms.append(norm)
    fs = defaultdict(int)
    for p, exponent in factorint(abs(norm.numerator)).items():
        fs[int(p)] += int(exponent)
    for p, exponent in factorint(norm.denominator).items():
        fs[int(p)] -= int(exponent)
    reconstruction = Q(1)
    for p, exponent in fs.items():
        assert is_prime_trial(p)
        reconstruction *= Q(p)**exponent
    assert reconstruction == abs(norm)
    support = set(fs)
    for coefficient in polynomial:
        support.update(int(p) for p in factorint(coefficient.denominator))
    norm_factorizations.append(dict(fs))
    prime_supports.append(support - S)

valuations = []
for index, polynomial in enumerate(factors):
    local_data = {}
    for p in sorted(prime_supports[index]):
        assert p not in S
        minimum = min(valuation_fraction(a, p) for a in polynomial if a)
        scale = Q(p)**minimum
        normalized = [a / scale for a in polynomial]
        norm_valuation = norm_factorizations[index].get(p, 0) - 9 * minimum
        assert norm_valuation >= 0
        factors_p = get_factors(p)
        reduced = [
            a.numerator * pow(a.denominator, -1, p) % p for a in normalized
        ]
        positive = [
            j for j, factor in enumerate(factors_p)
            if polynomial_divmod(reduced, factor, p)[1] == [0]
        ]
        depths = [0] * len(factors_p)
        if norm_valuation == 0:
            assert not positive
        elif len(positive) == 1:
            j = positive[0]
            degree = len(factors_p[j]) - 1
            assert norm_valuation % degree == 0
            depths[j] = norm_valuation // degree
        elif norm_valuation == sum(len(factors_p[j]) - 1 for j in positive):
            for j in positive:
                depths[j] = 1
        else:
            assert positive
            precision = norm_valuation + 1
            modulus = p**precision
            high = [
                a.numerator * pow(a.denominator, -1, modulus) % modulus
                for a in normalized
            ]
            for j in positive:
                lifted = hensel_factor(factors_p[j], p, precision)
                remainder = polynomial_divmod(high, lifted, modulus)[1]
                depth = min(valuation_integer(a, p) for a in remainder)
                assert 0 < depth < precision
                depths[j] = depth
        assert sum((len(factor) - 1) * depth for factor, depth in zip(factors_p, depths)) == norm_valuation
        local_data[p] = [minimum + depth for depth in depths]
    valuations.append(local_data)

sum_counts = 0
for candidate, compact in sorted(candidates.items()):
    total = {}
    for exponent, index in compact:
        for p, vector in valuations[index].items():
            if p not in total:
                total[p] = [0] * len(vector)
            total[p] = [a + exponent * b for a, b in zip(total[p], vector)]
    for p, vector in total.items():
        assert all(a == 0 for a in vector), (candidate, p, vector)
        sum_counts += len(vector)
    print(f"PASS: compact candidate {candidate}, all {len(total)} outside-S rational-prime supports cancel literally.", flush=True)

result = {
    "unique_factor_count": len(factors),
    "outside_rational_prime_count": len(residue_factors),
    "individual_norms": [str(a) for a in norms],
    "individual_norm_factorizations": norm_factorizations,
    "individual_outside_valuations": valuations,
    "residue_factors": residue_factors,
    "hensel_calls": hensel_calls,
    "hensel_records": hensel_records,
    "zero_prime_ideal_sums": sum_counts,
}
(base / "two_inert_compact_support_certificate_data.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print(f"PASS: {len(factors)} exact factor norms; {sum_counts} zero prime-ideal sums; {hensel_calls} literal Hensel lifts.")
print("Every displayed compact candidate is an actual S-unit; no class-group completeness was used.")
