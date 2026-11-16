"""Exact finite certificate for A.73.

The proof establishes the family for every n divisible by four.
These tests verify exact finite congruences and rational identities;
they neither infer a global point nor a completed old-coordinate tuple.
"""
from fractions import Fraction as F
from pathlib import Path


def v2_int(a):
    a = abs(a)
    assert a
    return (a & -a).bit_length() - 1


def v2(a):
    a = F(a)
    return v2_int(a.numerator) - v2_int(a.denominator)


def mod_fraction(a, modulus):
    a = F(a)
    assert a.denominator % 2
    return a.numerator * pow(a.denominator, -1, modulus) % modulus


def unit_part(a):
    a = F(a)
    e = v2(a)
    return a / F(2) ** e


lift_checks = 0


def nth_root_unit(n, target, precision):
    """Return the root in 1+4 modulo 2^(precision-v2(n))."""
    global lift_checks
    r = v2_int(n)
    assert mod_fraction(target, 2 ** (r + 2)) == 1
    root = 1
    for k in range(2, precision - r):
        modulus = 2 ** (k + r + 1)
        goal = mod_fraction(target, modulus)
        difference = (goal - pow(root, n, modulus)) % modulus
        assert difference % (2 ** (k + r)) == 0
        if difference:
            root += 2 ** k
        assert pow(root, n, modulus) == goal
        lift_checks += 1
    assert root % 4 == 1
    assert 1 <= root < 2 ** (precision - r)
    assert pow(root, n, 2 ** precision) == mod_fraction(target, 2 ** precision)
    return root


cases = []
for n in range(4, 257, 4):
    r = v2_int(n)
    odd = n // 2 ** r
    x = 1 + 3 * 2 ** r
    modulus = 2 ** (r + 2)
    powers = {pow(5, b, modulus): b for b in range(2 ** r)}
    assert len(powers) == 2 ** r
    b = powers[mod_fraction(F(-1, 3), modulus)]
    bp = powers[mod_fraction(F(-x, 3), modulus)]
    target = F(2 ** n - x, 3 * 5 ** bp)
    z = nth_root_unit(n, target, n + r + 2)
    assert (x + 3 * 5 ** bp * pow(z, n, 2 ** (n + r + 2))) % 2 ** (n + r + 2) == 2 ** n

    fibre = [F(5), F(5 ** b, 2 ** (r + n)), -F(5 ** bp * z ** n, 2 ** r)]
    c = F(-1, 3 * 2 ** r)
    punctures = [c / (1 - d) for d in fibre]
    coeff = [-d for d in punctures]
    required = [x + (1 - x) * d for d in fibre]
    assert [v2(w) for w in required] == [0, -n, n]
    assert all(mod_fraction(unit_part(w), modulus) == 1 for w in required)
    assert fibre[2] / (fibre[1] * fibre[0] ** (bp - b)) == -(2 * z) ** n
    assert [(c - t) / a for t, a in zip(punctures, coeff)] == fibre
    assert [(1 - t) / a for t, a in zip(punctures, coeff)] == required
    assert all((-t) / a == 1 for t, a in zip(punctures, coeff))
    assert len(set(punctures + [F(0), F(1), c])) == 6
    assert (1 - c) / (-c) == x

    conductor = 2 ** (r + 1)
    order = 2 ** (r - 1)
    char_log = {pow(5, k, conductor): k for k in range(order)}
    assert len(char_log) == order
    artin = pow(x, -1, conductor)
    assert artin == 1 + 2 ** r == pow(5, 2 ** (r - 2), conductor)
    assert F(char_log[artin], order) == F(1, 2)
    assert pow(artin, 2, conductor) == 1

    delta = punctures[1] - punctures[0]
    trans = lambda t: (F(t) - punctures[0]) / delta
    transformed_punctures = list(map(trans, punctures))
    base = trans(0)
    bad = trans(1)
    new = trans(c)
    assert transformed_punctures[:2] == [0, 1]
    assert (bad - new) / (base - new) == x
    assert [base - d for d in transformed_punctures] == [a / delta for a in coeff]

    if n == 8:
        assert (r, x, b, bp, z) == (3, 25, 5, 7, 445)
        assert required == [F(-95), F(-2975, 256), F(360405469272041107177734400)]
        normalized_roots = [nth_root_unit(n, unit_part(w), 64) for w in required]
        example = dict(n=n, b=b, bp=bp, z=z, required=required,
                       roots=normalized_roots)
    cases.append(n)

output = (
    'A.73 exact finite certificate: all checks passed.\n'
    f'Exponents tested: all {len(cases)} multiples of four from4 through256.\n'
    f'Exact bit-lifting congruences checked: {lift_checks}.\n'
    f'Exact fibre relations, local valuation/unit triples, Artin values, and affine maps: {len(cases)} each.\n'
    f'n=8: b={example["b"]}, bprime={example["bp"]}, z={example["z"]}.\n'
    f'n=8 required eighth powers: {example["required"]}.\n'
    f'n=8 normalized unit roots in1+4Z2 modulo2^61: {example["roots"]}.\n'
    'Each displayed normalized root has the required eighth power modulo2^64.\n'
    'Every tested cyclotomic Artin character value is exactly1/2.\n'
    'The proof gives the all-exponent and genuine Q2-root assertions; finite tests do not replace them.\n'
    'No completed old-coordinate tuple or failure of completed(G) is inferred.\n'
)
Path(__file__).with_name('higher_character_obstruction_output.txt').write_text(output)
print(output, end='')
