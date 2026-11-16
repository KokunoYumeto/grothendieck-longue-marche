"""Exact first S-unit coordinates and tame local norm congruences.

The geometric/class-number and local norm arguments are recorded in the
accompanying proof note. This finite certificate proves the displayed
polynomial identities and every residue/congruence calculation.
"""
from itertools import product
from pathlib import Path
import json

base = Path(__file__).resolve().parent


def multiply(x, y):
    z = [0] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            z[i + j] += a * b
    for k in (4, 3):
        z[k - 3] += 3 * z[k]
    return tuple(z[:3])


def norm(x):
    a, b, c = x
    return a**3 + 3 * b**3 + 9 * c**3 - 9 * a * b * c


generators = {
    2: ((-1, 1, 0), (1, 1, 1)),
    11: ((2, 1, 0), (4, -2, 1)),
    59: ((2, 2, -1), (10, -1, 6)),
}
for q, (g, complement) in generators.items():
    assert multiply(g, complement) == (q, 0, 0)
    assert norm(g) == q and norm(complement) == q * q

unit = (-2, 0, 1)
inverse = (4, 3, 2)
assert multiply(unit, inverse) == (1, 0, 0)
assert norm(unit) == 1
assert 4**3 % 61 == 3
assert (4**2 - 2) % 61 == 14
assert pow(14, 20, 61) == 13

field_data = []
for q in (11, 59):
    rational_root = next(a for a in range(q) if a**3 % q == 3)

    def mul(x, y):
        a, b = x
        c, e = y
        return (
            (a * c - rational_root**2 * b * e) % q,
            (a * e + b * c - rational_root * b * e) % q,
        )

    def power(x, n):
        out = (1, 0)
        while n:
            if n & 1:
                out = mul(out, x)
            x = mul(x, x)
            n //= 2
        return out

    alpha = (0, 1)
    beta = (1, q - 1)
    local_unit = ((-rational_root**2 - 2) % q, -rational_root % q)
    exponent = (q * q - 1) // 3
    alpha_character = power(alpha, exponent)
    unit_character = power(local_unit, exponent)
    assert alpha_character != (1, 0)
    assert power(alpha_character, 3) == (1, 0)
    assert unit_character == power(alpha_character, 2)
    assert power(beta, exponent) == (1, 0)
    # All rational residue units are cubes in this quadratic residue field.
    for rational_unit in range(1, q):
        assert power((rational_unit, 0), exponent) == (1, 0)
    field_data.append(
        {
            "q": q,
            "rational_alpha_root": rational_root,
            "alpha_character": alpha_character,
            "U_character": unit_character,
            "beta1_character": power(beta, exponent),
        }
    )

survivors = []
for z, a, b, c in product(range(3), repeat=4):
    literal = a == 0 and (8 * 2 * z - b) % 3 == 0 and (8 * 2 * z - c) % 3 == 0
    reduced = a == 0 and b == z and c == z
    assert literal == reduced
    if literal:
        survivors.append((z, a, b, c))
assert survivors == [(0, 0, 0, 0), (1, 0, 1, 1), (2, 0, 2, 2)]

next_survivors = []
for z, a, b, c in product(range(3), repeat=4):
    # The character exponents of beta_2 relative to lambda(alpha) are 2,1.
    literal = (
        a == 0
        and (2 + 2 * z + b) % 3 == 0
        and (1 + 2 * z + c) % 3 == 0
    )
    reduced = a == 0 and b == (z + 1) % 3 and c == (z + 2) % 3
    assert literal == reduced
    if literal:
        next_survivors.append((3 * z, 3 * a, 3 * b, 3 * c))
assert next_survivors == [(0, 0, 3, 6), (3, 0, 6, 0), (6, 0, 0, 3)]

messages = [
    "PASS: all six prime-generator/complement identities and their exact cubic norms.",
    "PASS: U inverse, norm one, and literal noncube residue at alpha=4 modulo 61.",
    "PASS: both quadratic residue fields and all rational unit characters.",
    "PASS: all 81 first-parameter residue vectors; exactly 3 meet the first-step local norm conditions.",
    "PASS: all 81 cube-branch vectors; the next local conditions retain exactly 3 first-seed classes modulo 9.",
    "No global S-unit preimage or all-depth compatibility is inferred from these finite checks.",
]
output = "\n".join(messages) + "\n"
(base / "first_seed_sunit_fibre_certificate_output.txt").write_text(output)
(base / "first_seed_sunit_fibre_certificate_data.json").write_text(
    json.dumps({
        "generators": generators,
        "local_fields": field_data,
        "survivors_mod3": survivors,
        "cube_branch_next_survivors_mod9": next_survivors,
    }, indent=2) + "\n"
)
print(output, end="")
