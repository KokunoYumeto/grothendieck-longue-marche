#!/usr/bin/env python3
"""Exact finite shadow of the standard D.61/D.64 negative torus action.

The quotient is the class-three BCH group on the free nilpotent Lie algebra
of rank two over F_5. Symbolic rational polynomial checks prove associativity
and the involution identities before reduction modulo five. All 3125 group
elements are then generated and inspected. This certificate does not assert
that fixed elements in this finite quotient lift to full fixed elements.
"""

from collections import deque
from itertools import product
from pathlib import Path
import hashlib
import json
import sympy as sp


P = 5
ZERO = (0, 0, 0, 0, 0)
X = (1, 0, 0, 0, 0)
Y = (0, 1, 0, 0, 0)
checks = []


def check(name, assertion):
    assert assertion, name
    checks.append(name)


def bch(u, v, half=sp.Rational(1, 2), twelfth=sp.Rational(1, 12)):
    a, b, c, d, e = u
    f, g, h, i, j = v
    k = a * g - b * f
    return (
        a + f,
        b + g,
        c + h + half * k,
        d + i + half * (a * h - c * f) + twelfth * (a - f) * k,
        e + j + half * (b * h - c * g) + twelfth * (b - g) * k,
    )


def neg(u):
    return tuple(-a for a in u)


def omega(u):
    return (u[0], -u[1], -u[2], -u[3], u[4])


def equal_poly(u, v):
    return all(sp.expand(a - b) == 0 for a, b in zip(u, v))


def beta_poly(u):
    return bch(bch(Y, omega(u)), neg(Y))


u = sp.symbols("u0:5")
v = sp.symbols("v0:5")
z = sp.symbols("z0:5")
check("BCH associativity as five rational polynomial identities",
      equal_poly(bch(bch(u, v), z), bch(u, bch(v, z))))
check("BCH identity", equal_poly(bch(u, ZERO), u) and equal_poly(bch(ZERO, u), u))
check("BCH inverse", equal_poly(bch(u, neg(u)), ZERO))
check("omega is an involution", equal_poly(omega(omega(u)), u))
check("omega is an automorphism", equal_poly(omega(bch(u, v)), bch(omega(u), omega(v))))
check("beta is an involution", equal_poly(beta_poly(beta_poly(u)), u))
check("beta is an automorphism", equal_poly(beta_poly(bch(u, v)), bch(beta_poly(u), beta_poly(v))))


def mul(u, v):
    return tuple(int(a) % P for a in bch(u, v, pow(2, -1, P), pow(12, -1, P)))


def inv(u):
    return tuple(-a % P for a in u)


def om(u):
    return tuple(a % P for a in omega(u))


def beta(u):
    return mul(mul(Y, om(u)), inv(Y))


def comm(u, v):
    return mul(mul(mul(u, v), inv(u)), inv(v))


def power(u, n):
    r = ZERO
    for _ in range(n):
        r = mul(r, u)
    return r


all_q = set(product(range(P), repeat=5))
generated = {ZERO}
queue = deque([ZERO])
while queue:
    q = queue.popleft()
    for s in (X, Y, inv(X), inv(Y)):
        r = mul(q, s)
        if r not in generated:
            generated.add(r)
            queue.append(r)
check("X,Y generate every BCH coordinate", generated == all_q)
check("Q has 3125 elements", len(all_q) == 3125)
check("every element has exponent dividing five", all(power(q, P) == ZERO for q in all_q))
check("finite omega preserves multiplication by both generators",
      all(om(mul(q, s)) == mul(om(q), om(s)) for q in all_q for s in (X, Y)))
check("finite beta preserves multiplication by both generators",
      all(beta(mul(q, s)) == mul(beta(q), beta(s)) for q in all_q for s in (X, Y)))

c = comm(X, Y)
missing = comm(Y, comm(Y, X))
check("beta sends the actual commutator cusp to its inverse", beta(c) == inv(c))
check("actual cusp has order five", c != ZERO and power(c, 5) == ZERO)
check("the nested commutator has coordinate minus e5", missing == (0, 0, 0, 0, 4))

fixed_omega = {q for q in all_q if om(q) == q}
fixed_beta = {q for q in all_q if beta(q) == q}
a_image = {power(X, n) for n in range(P)}
check("omega fixed set has exactly the two displayed coordinates",
      fixed_omega == {(a, 0, 0, 0, e) for a in range(P) for e in range(P)})
check("omega has 25 fixed elements", len(fixed_omega) == 25)
check("beta has 25 fixed elements", len(fixed_beta) == 25)
check("the full standard fixed group has five-element image", len(a_image) == 5)
check("the missing fixed nested commutator is outside that image",
      missing in fixed_omega and missing not in a_image)


def emul(s, t):
    q, e = s
    r, f = t
    return (mul(q, beta(r) if e else r), (e + f) % 2)


def einv(s):
    q, e = s
    return (beta(inv(q)) if e else inv(q), e)


def econj(s, t):
    return emul(emul(s, t), einv(s))


identity_e = (ZERO, 0)
v_image = (ZERO, 1)
w_image = (inv(Y), 1)
check("v and w retain the two literal reflection formulas",
      emul(v_image, v_image) == identity_e and emul(w_image, w_image) == identity_e)
check("conjugation by w acts by omega on all of Q",
      all(econj(w_image, (q, 0)) == (om(q), 0) for q in all_q))
check("the actual X cusp-transporter identity is preserved",
      econj((X, 0), v_image) == emul((c, 0), v_image))
involutions = {(q, 1) for q in all_q if emul((q, 1), (q, 1)) == identity_e}
v_orbit = {econj((q, 0), v_image) for q in all_q}
check("the quotient has one conjugacy class of outside involutions", involutions == v_orbit)
check("that quotient class has 125 elements", len(involutions) == 125)
check("Y squared conjugates v to w in the finite quotient", econj((power(Y, 2), 0), v_image) == w_image)

tv = {q for q in all_q if econj((q, 0), v_image) == v_image}
tw = {q for q in all_q if econj((q, 0), w_image) == v_image}
check("both finite transporter sets have 25 elements", len(tv) == 25 and len(tw) == 25)
right_orbits = {frozenset(mul(q, a) for a in a_image) for q in tw}
check("the actual full-w centralizer image acts on its transporter set",
      all(orbit <= tw for orbit in right_orbits))
check("the transported other-section set has five classes of five elements",
      len(right_orbits) == 5 and all(len(orbit) == 5 for orbit in right_orbits))
check("the right orbits partition the finite transporter set",
      set().union(*right_orbits) == tw)

index = len(all_q)
boundary_count = index // P
genus = (2 + index - boundary_count) // 2
check("the actual surface-cover Euler characteristic is retained",
      2 - 2 * genus - boundary_count == -index)
check("the cover has 625 cusps and genus 1251", boundary_count == 625 and genus == 1251)

c_image = {power(c, n) for n in range(P)}
boundary_cosets = {frozenset(mul(q, l) for l in c_image) for q in all_q}
fixed_boundary_cosets = {
    coset for coset in boundary_cosets
    if frozenset(beta(q) for q in coset) == coset
}
check("the actual cusp cosets are the 625 right cosets of its five-element image",
      len(boundary_cosets) == 625)
check("the specified involution fixes exactly 25 boundary lifts", len(fixed_boundary_cosets) == 25)


def cusp_transporter(t):
    # The full word sends v to c^t v; its two parity formulas are literal.
    if t % 2 == 0:
        return power(c, t // 2)
    return mul(power(c, (t - 1) // 2), X)


incidence_edges = []
for coset in sorted(fixed_boundary_cosets, key=lambda s: min(s)):
    q = min(coset)
    residues = [t for t in range(P)
                if econj((q, 0), emul((power(c, t), 0), v_image)) == v_image]
    assert len(residues) == 1
    t = residues[0]
    endpoints = tuple(mul(q, cusp_transporter(s)) for s in (t, t + P))
    assert all(e in tv for e in endpoints)
    incidence_edges.append(endpoints)
check("both internal cusp-section labels map to actual cusp-class vertices",
      len(incidence_edges) == 25 and all(a in tv and b in tv for a, b in incidence_edges))
adjacency = {q: [] for q in tv}
for a, b in incidence_edges:
    adjacency[a].append(b)
    adjacency[b].append(a)
check("the fixed-cusp incidence graph has degree two at each of its 25 vertices",
      all(len(v) == 2 for v in adjacency.values()))
components = []
unseen = set(tv)
while unseen:
    start = min(unseen)
    component = {start}
    frontier = [start]
    while frontier:
        q = frontier.pop()
        for r in adjacency[q]:
            if r not in component:
                component.add(r)
                frontier.append(r)
    unseen -= component
    components.append(component)
check("the actual cusp fusion graph is five cycles of length five",
      sorted(map(len, components)) == [5] * 5
      and all(a != b for a, b in incidence_edges))

report = {
    "status": "PASS",
    "scope": "An exact quotient of the standard full two-section torus extension; no fixed-point surjectivity is inferred.",
    "field": "F_5",
    "group_order": len(all_q),
    "extension_order": 2 * len(all_q),
    "BCH_coordinates": ["X", "Y", "[X,Y]", "[X,[X,Y]]", "[Y,[X,Y]]"],
    "cusp_coordinate": c,
    "missing_fixed_coordinate": missing,
    "omega_fixed_order": len(fixed_omega),
    "beta_fixed_order": len(fixed_beta),
    "full_fixed_group_image_order": len(a_image),
    "outside_involution_count": len(involutions),
    "outside_involution_conjugacy_classes": 1,
    "cover_index": index,
    "cover_boundary_count": boundary_count,
    "cover_genus": genus,
    "cover_cusp_section_classes": len(tv),
    "cover_other_section_classes": len(right_orbits),
    "cover_fixed_boundary_lifts": len(fixed_boundary_cosets),
    "cusp_incidence_vertex_count": len(tv),
    "cusp_incidence_edge_count": len(incidence_edges),
    "cusp_incidence_component_sizes": sorted(map(len, components)),
    "cusp_incidence_edges": incidence_edges,
    "checks": checks,
    "check_count": len(checks),
    "symbolic_associativity": "All five rational polynomial differences vanish identically; denominators 2 and 12 are invertible modulo 5.",
    "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
target = Path(__file__).with_name("torus_fixed_quotient_shadow_output.json")
target.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
