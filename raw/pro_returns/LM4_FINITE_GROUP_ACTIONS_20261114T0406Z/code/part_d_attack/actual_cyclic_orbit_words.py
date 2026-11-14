#!/usr/bin/env python3
"""Reduced-word checks for the original cyclic-orbit comparison.

The first factor has order two, the second order three.  These are
universal standard-source identities, with no proposed nonstandard h.
"""
import json
from pathlib import Path


def red(word):
    out = []
    for factor, power in word:
        order = (2, 3)[factor]
        power %= order
        if not power:
            continue
        if out and out[-1][0] == factor:
            power = (out.pop()[1] + power) % order
        if power:
            out.append((factor, power))
    return tuple(out)


def mul(*words):
    return red(item for word in words for item in word)


def inv(word):
    return red((factor, -power) for factor, power in reversed(word))


def power(word, exponent):
    if exponent < 0:
        return power(inv(word), -exponent)
    result = ()
    for _ in range(exponent):
        result = mul(result, word)
    return result


def conj(word, target):
    return mul(word, target, inv(word))


A, B = ((0, 1),), ((1, 1),)
X = mul(power(B, 2), A, B, A)
Y = mul(A, B, A, power(B, 2))
Z = inv(mul(X, Y))
checks = []


def check(name, left, right):
    assert left == right, (name, left, right)
    checks.append({"name": name, "passed": True})


check("first factor order two", power(A, 2), ())
check("second factor order three", power(B, 3), ())
check("inversion of X", conj(A, X), inv(X))
check("inversion of Y", conj(A, Y), inv(Y))
check("Omega sends X to Y", conj(B, X), Y)
check("Omega sends Y to Z", conj(B, Y), Z)
check("Omega sends Z to X", conj(B, Z), X)
check("Omega acts on the negative involution", conj(B, A), mul(inv(Y), A))
check("original normalized reflection", conj(inv(B), A), mul(X, A))
check("first basis recovery", mul(conj(inv(B), A), A), X)
check("second basis recovery", mul(A, conj(B, A)), Y)


def quotient(word):
    return tuple(sum(n for f, n in word if f == i) % (2, 3)[i] for i in range(2))


check("X in named index-six kernel", quotient(X), (0, 0))
check("Y in named index-six kernel", quotient(Y), (0, 0))
check("Z in named index-six kernel", quotient(Z), (0, 0))

# For CO.10 the letters A,B now denote the standard t,kappa factors.
# A word with a trailing j is (word,1); j fixes A and inverts B.
def J(word):
    return red((f, n if f == 0 else -n) for f, n in word)


def emul(*elements):
    word, parity = (), 0
    for target, bit in elements:
        word = mul(word, J(target) if parity else target)
        parity ^= bit
    return word, parity


s = (A, 1)
U = emul((power(B, 2), 0), s, (B, 0), s)
V = emul(s, (B, 0), s, (power(B, 2), 0))
rho_x = power(mul(A, B), -2)
check("canonical first restriction equals original positive formula", U, (rho_x, 0))
check("canonical second restriction equals original positive formula", V, (conj(B, rho_x), 0))

result = {
    "title": "Original cyclic-orbit universal word checks",
    "status": "PASS",
    "named_checks": len(checks),
    "checks": checks,
    "scope": "Universal coproduct and standard semidirect identities only; no nonstandard actual h is assigned.",
}
output = json.dumps(result, indent=2) + "\n"
Path(__file__).with_name("actual_cyclic_orbit_words_output.json").write_text(output)
print(output, end="")
