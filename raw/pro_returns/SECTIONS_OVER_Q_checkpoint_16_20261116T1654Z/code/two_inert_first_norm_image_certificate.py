"""Finite unit-coordinate calculation in the complete first norm image.

The compact S-unit expressions are evaluated after taking their exact
relative norm. A primitive order-nine character of U determines all
unit exponents modulo nine, without expanding any enormous product.
"""
from pathlib import Path
from fractions import Fraction as Q
import json
import re
import sys
from sympy import primerange

sys.set_int_max_str_digits(0)
base = Path(__file__).resolve().parent
raw = (base / "two_inert_compact_units_pari_output.txt").read_text()
d = 649
factors = {}
for i, j, exponent, expression in re.findall(
    r"^SFACTOR (\d+) (\d+) (-?\d+) (\[.*\])$", raw, re.M
):
    polynomial = tuple(Q(s.strip()) for s in expression[1:-1].split(","))
    polynomial += (Q(0),) * (9 - len(polynomial))
    factors.setdefault(int(i), []).append((int(exponent), polynomial))


def multiply(x, y):
    z = [Q(0)] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            z[i + j] += a * b
    for k in (4, 3):
        z[k - 3] += 3 * z[k]
    return tuple(z[:3])


def cube(x):
    return multiply(multiply(x, x), x)


def relative_norm(x):
    A, B, C = [tuple(x[j + 3 * k] * d**(2 * k) for k in range(3)) for j in range(3)]
    w = (Q(0), Q(d * d), Q(0))
    terms = [
        cube(A),
        multiply(w, cube(B)),
        multiply(multiply(w, w), cube(C)),
        tuple(-3 * a for a in multiply(w, multiply(multiply(A, B), C))),
    ]
    return tuple(sum(term[i] for term in terms) for i in range(3))


norms = {}
for compact in factors.values():
    for _, polynomial in compact:
        norms.setdefault(polynomial, relative_norm(polynomial))


def evaluate(polynomial, alpha, p):
    z = 0
    for coefficient in reversed(polynomial):
        z = (z * alpha + coefficient.numerator * pow(coefficient.denominator, -1, p)) % p
    return z


answers = []
for p in primerange(2000, 10000):
    if (p - 1) % 9:
        continue
    for alpha in range(p):
        if alpha**3 % p != 3:
            continue
        unit = (alpha * alpha - 2) % p
        primitive = pow(unit, (p - 1) // 9, p)
        if pow(primitive, 3, p) == 1:
            continue
        assert pow(primitive, 9, p) == 1
        logs = {pow(primitive, exponent, p): exponent for exponent in range(9)}
        assert len(logs) == 9
        values = {polynomial: evaluate(norm, alpha, p) for polynomial, norm in norms.items()}
        assert all(values.values())  # Every factor's rational norm has support <=1721.
        norm_values = {}
        for i, compact in factors.items():
            value = 1
            for exponent, polynomial in compact:
                value = value * pow(values[polynomial], exponent % (p - 1), p) % p
            norm_values[i] = value
        gamma2 = (alpha - 1) % p
        delta2 = (alpha * alpha + alpha + 1) % p
        gamma11 = (alpha + 2) % p
        delta11 = (alpha * alpha - 2 * alpha + 4) % p
        gamma59 = (2 + 2 * alpha - alpha * alpha) % p
        delta59 = (10 - alpha + 6 * alpha * alpha) % p
        divisor_generators = {
            1: gamma2,
            2: pow(gamma2, 2, p),
            3: pow(delta2, 3, p),
            4: alpha,
            5: pow(gamma11, 3, p),
            6: delta11,
            7: gamma11 * gamma59 % p,
            8: delta59,
        }
        exponents = []
        for i in range(1, 9):
            normalized = norm_values[i] * pow(divisor_generators[i], -1, p) % p
            exponent = logs[pow(normalized, (p - 1) // 9, p)]
            exponents.append(exponent)
        k = (exponents[5] + exponents[7] - 2 * exponents[6]) % 9
        assert k % 3 == 1
        scalar_correction = ((1 - k) // 3) % 3
        # Independently certified angular components of w0=s6*s8/s7^2:
        # (valuation, angular log)=(1,1) at11, (1,0) at59.
        theta = [(2 + 2 * scalar_correction) % 3, (1 + 2 * scalar_correction) % 3]
        seed_classes = []
        for z in range(9):
            B = (-2 - theta[0] * z) % 3
            C = (-1 - theta[1] * z) % 3
            b = (z + 3 * B) % 9
            c = (z + 3 * C) % 9
            seed_classes.append((z, 0, b, c))
        row = {
            "p": p,
            "alpha": alpha,
            "U": unit,
            "primitive_ninth_root": primitive,
            "norm_values": norm_values,
            "norm_unit_exponents_mod9": exponents,
            "w0_norm_unit_exponent_mod9": k,
            "scalar_correction_mod3": scalar_correction,
            "eta_stable_characters": theta,
            "next_seed_classes_mod9": seed_classes,
        }
        if answers:
            assert row["norm_unit_exponents_mod9"] == answers[0]["norm_unit_exponents_mod9"]
        answers.append(row)
        print("PASS:", "p", p, "alpha", alpha, "norm-unit exponents", exponents, "k", k, "theta", theta)
        if len(answers) == 3:
            break
    if len(answers) == 3:
        break

assert len(answers) == 3
assert len(set(map(tuple, answers[0]["next_seed_classes_mod9"]))) == 9
result = {
    "checks": answers,
    "scope": "Exact first S-unit norm image and next local norm conditions; no fixed-S preimage in K3 or infinite global family is asserted.",
}
(base / "two_inert_first_norm_image_certificate_data.json").write_text(json.dumps(result, indent=2) + "\n")
print("PASS: three independent ninth-power residue witnesses agree.")
print("The nine next-step seed classes modulo9 are:", answers[0]["next_seed_classes_mod9"])
