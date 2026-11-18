#!/usr/bin/env python3
"""Exact word and character checks for E.180.

This checks the literal modular markings and the final linear character
identity.  It does not enumerate GT elements or replace the proof of the
common-source geometric comparison or the profinite centralizer theorem.
Only the Python standard library is used.
"""
from pathlib import Path
import hashlib
import json


# Normal forms in C2(s) * C3(r), represented by (factor, exponent).
orders = {"s": 2, "r": 3}


def reduce_word(word):
    out = []
    for factor, exponent in word:
        exponent %= orders[factor]
        if not exponent:
            continue
        if out and out[-1][0] == factor:
            exponent = (out.pop()[1] + exponent) % orders[factor]
        if exponent:
            out.append((factor, exponent))
    return tuple(out)


def multiply(*words):
    return reduce_word(t for word in words for t in word)


def inverse(word):
    return reduce_word((factor, -exponent)
                       for factor, exponent in reversed(word))


def power(word, exponent):
    if exponent < 0:
        return power(inverse(word), -exponent)
    out = ()
    for _ in range(exponent):
        out = multiply(out, word)
    return out


def conjugate(by, word):
    return multiply(by, word, inverse(by))


s, r = (("s", 1),), (("r", 1),)
tau = multiply(s, r)
u = inverse(tau)
w = multiply(tau, r)
x = power(tau, -2)
y = conjugate(s, x)
d = multiply(inverse(x), s)
v = x
a = multiply(v, d)

identities = {
    "braid_relation": (multiply(u, w, u), multiply(w, u, w)),
    "named_order_two": (multiply(u, w, u), s),
    "named_order_three": (multiply(u, w), r),
    "literal_cusp": (multiply(s, r), inverse(u)),
    "first_pure_generator": (x, power(u, 2)),
    "second_pure_generator": (y, power(w, 2)),
    "mixed_order_two": (a, s),
    "mixed_square": (power(d, 2), multiply(inverse(x), inverse(y))),
    "cusp_theta_fixes_x": (conjugate(tau, x), x),
    "cusp_theta_y": (conjugate(tau, y), power(d, 2)),
    "swapped_order_two": (multiply(d, v), conjugate(d, a)),
}
for name, (left, right) in identities.items():
    assert left == right, (name, left, right)

# Coefficients are ordered (c, rho, m, lambda, constant).
left_character = (4, -2, 1, 0, 0)
right_character = (0, 2, -1, 1, -1)
difference = tuple(x-y for x, y in zip(left_character, right_character))
assert difference == (4, -4, 2, -1, 1)

# Substitute lambda = 2m+1; no division modulo a finite even group occurs.
after_multiplier_identity = (
    difference[0], difference[1],
    difference[2] + 2*difference[3],
    difference[4] + difference[3],
)
assert after_multiplier_identity == (4, -4, 0, 0)

data = {
    "word_identities": {
        name: {"left": list(left), "right": list(right)}
        for name, (left, right) in identities.items()
    },
    "character_coordinates": ["c", "rho", "m", "lambda", "constant"],
    "left_character": left_character,
    "right_character": right_character,
    "difference": difference,
    "after_lambda_equals_2m_plus_1": after_multiplier_identity,
    "scope": "Literal C2*C3 word and continuous-character calculations only.",
}
encoded = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
data["data_sha256"] = hashlib.sha256(encoded).hexdigest()
data["status"] = "PASS"
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(data, indent=2) + "\n")
print("PASS", len(identities), "literal modular word identities")
print("character_difference_after_multiplier_identity",
      after_multiplier_identity)
print("SHA256", data["data_sha256"])
