"""Exact presentation, dihedral, and surface-cover certificates for D.65."""
from math import gcd
from pathlib import Path
import json


# Free product Z(z) * C2(v): 1/-1 are z/z^-1, and 2 is v.
def red(word):
    out = []
    for a in word:
        inverse = a if a == 2 else -a
        if out and out[-1] == inverse:
            out.pop()
        else:
            out.append(a)
    return tuple(out)


def wi(word):
    return tuple(a if a == 2 else -a for a in reversed(word))


def wm(*words):
    return red(a for word in words for a in word)


def wp(word, n):
    return wm(*((word if n >= 0 else wi(word),) * abs(n)))


def wc(a, b):
    return wm(a, b, wi(a), wi(b))


z, v = (1,), (2,)
X, Y = wm(z, v), wm(v, z)
g = wm(z, z)
c = wc(g, v)
word_checks = 0
assert wm(X, Y) == g
assert wc(X, Y) == c
assert wm(v, X, v) == Y
assert wm(v, Y, v) == X
assert wm(X, v) == z
assert wm(v, c, v) == wi(c)
assert wm(v, g, v) == wm(wi(c), g)
word_checks += 7
for r in range(-20, 21):
    a = wm(wp(c, r), g)
    assert wm(a, v, wi(a)) == wm(wp(c, 2*r+1), v)
    word_checks += 1
for mu in range(-31, 32, 2):
    a1 = wm(wp(c, (mu+1)//2), wi(g))
    assert wm(wi(g), wi(a1), g) == wm(wp(c, (-mu-1)//2), g)
    word_checks += 1


# Exact finite dihedral coordinates c^a v^e.
def dm(x, y, n):
    return ((x[0] + (-1 if x[1] else 1)*y[0]) % n,
            (x[1]+y[1]) % 2)


def di(x, n):
    return ((x[0] if x[1] else -x[0]) % n, x[1])


dihedral_checks = 0
unit_cases = 0
for n in range(2, 129):
    ident, V, W = (0, 0), (0, 1), (1, 1)
    # Britton reduces a vertex conjugator to the subgroup {1,V};
    # phi(V)=W is the actual HNN edge isomorphism.
    coefficients = {dm(d, ident if d == ident else W, n)
                    for d in (ident, V)}
    assert coefficients == {(0, 0), ((-1) % n, 0)}
    dihedral_checks += 1
    for r in range(n):
        image = dm(dm((r, 0), W, n), ((-r) % n, 0), n)
        assert image == ((2*r+1) % n, 1)
        dihedral_checks += 1
        if gcd(2*r+1, n) == 1:
            assert image != V
            unit_cases += 1


def hm(x, y, n):
    a, b, t = x
    aa, bb, tt = y
    return ((a+aa) % n, (b+bb) % n, (t+tt+a*bb) % n)


def hi(x, n):
    a, b, t = x
    return ((-a) % n, (-b) % n, (a*b-t) % n)


heisenberg_checks = 0
covers = []
for n in range(2, 17):
    U, V, C = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    comm = hm(hm(hm(U, V, n), hi(U, n), n), hi(V, n), n)
    assert comm == C
    for a in range(n):
        for b in range(n):
            for t in range(n):
                # U^a V^b C^(t-ab): exact inverse coordinates.
                image = hm(hm((a, 0, 0), (0, b, 0), n),
                           (0, 0, (t-a*b) % n), n)
                assert image == (a, b, t)
                heisenberg_checks += 1
    remaining = {(a, b, t) for a in range(n)
                 for b in range(n) for t in range(n)}
    boundary_lengths = []
    while remaining:
        start = next(iter(remaining))
        current, length = start, 0
        while current in remaining:
            remaining.remove(current)
            current = hm(current, C, n)
            length += 1
        assert current == start
        boundary_lengths.append(length)
    assert boundary_lengths == [n] * (n*n)
    genus = 1 + n*n*(n-1)//2
    assert 2-2*genus == -n**3+n**2
    covers.append({"n": n, "degree_in_torus_cone_group": n**3,
                   "degree_in_G_n": 2*n**3,
                   "boundary_count": n*n, "boundary_degree": n,
                   "closed_surface_genus": genus})

result = {
    "status": "PASS",
    "exact_free_product_word_checks": word_checks,
    "dihedral_identity_checks": dihedral_checks,
    "unit_residue_centralizer_exclusions": unit_cases,
    "heisenberg_inverse_coordinate_checks": heisenberg_checks,
    "exact_surface_covers": covers,
    "scope": "Finite presentation and covering identities. The full square obstruction "
             "uses D65's discrete centralizer and hereditary-conjugacy-separability proof.",
}
out = Path(__file__).with_name("standard_oneclass_square_d65_output.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
