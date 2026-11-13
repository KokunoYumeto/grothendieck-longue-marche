"""Exact finite word checks for D.64; no finite-to-profinite inference."""
from pathlib import Path
import json


def reduce_word(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def inv(word):
    return tuple(-a for a in reversed(word))


def mul(*words):
    return reduce_word(a for word in words for a in word)


def comm(a, b):
    return mul(a, b, inv(a), inv(b))


def subst(word, images):
    return mul(*(images[a] if a > 0 else inv(images[-a]) for a in word))


X, Y = (1,), (2,)
c = comm(X, Y)
alpha0 = {1: mul(Y, X, inv(Y)), 2: inv(Y)}
alpha1 = {1: Y, 2: X}
zeta0 = {1: inv(X), 2: Y}
zeta1 = {1: inv(X), 2: inv(Y)}
checks = 0
for alpha in (alpha0, alpha1):
    for a in (X, Y):
        assert subst(subst(a, alpha), alpha) == a
        checks += 1
    assert subst(c, alpha) == inv(c)
    checks += 1
for alpha, zeta in ((alpha0, zeta0), (alpha1, zeta1)):
    for a in (X, Y):
        assert subst(subst(a, zeta), zeta) == a
        assert subst(subst(a, alpha), zeta) == subst(subst(a, zeta), alpha)
        checks += 2
assert subst(c, zeta0) == mul(inv(X), inv(c), X)
assert subst(c, zeta1) == mul(inv(mul(X, Y)), c, X, Y)
checks += 2
for g, alpha in ((X, alpha0), (mul(X, Y), alpha1)):
    assert mul(g, inv(subst(g, alpha))) == c
    checks += 1


def dm(a, b, n):
    return ((a[0] + (-1 if a[1] else 1) * b[0]) % n, (a[1] + b[1]) % 2)


def di(a, n):
    return ((a[0] if a[1] else -a[0]) % n, a[1])


def dp(a, k, n):
    if k < 0:
        return dp(di(a, n), -k, n)
    out = (0, 0)
    while k:
        if k & 1:
            out = dm(out, a, n)
        a = dm(a, a, n)
        k >>= 1
    return out


dihedral_checks = 0
for n in range(2, 97):
    r, s = (1, 0), (0, 1)
    cusp = dm(dm(dm(r, s, n), di(r, n), n), s, n)
    assert cusp == (2 % n, 0)
    conjugates = {dm(dm(h, r, n), di(h, n), n)
                  for h in ((a, e) for a in range(n) for e in (0, 1))}
    assert conjugates == {(1, 0), ((-1) % n, 0)}
    for mu in range(1, 2 * n, 2):
        a0 = dm(dp(cusp, (mu - 1) // 2, n), r, n)
        a1 = dm(dp(cusp, (mu + 1) // 2, n), di(r, n), n)
        assert a0 == a1 == (mu % n, 0)
        assert (a0 in conjugates) == (mu % n in (1, (-1) % n))
        dihedral_checks += 2

result = {
    "status": "PASS",
    "exact_free_word_checks": checks,
    "dihedral_moduli": list(range(2, 97)),
    "dihedral_transporter_checks": dihedral_checks,
    "scope": "Exact finite identities only; D64 proves the all-modulus conclusion separately.",
}
target = Path(__file__).with_name("standard_negative_centralizers_d64_output.json")
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
