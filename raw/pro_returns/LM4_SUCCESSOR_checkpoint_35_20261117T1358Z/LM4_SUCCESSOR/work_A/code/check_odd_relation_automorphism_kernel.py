#!/usr/bin/env python3
"""Actual first odd relation quotient; normalized peripheral kernel has 2-torsion.

This finite certificate does not claim realizability by a full positive torsion
automorphism.  The source-image and universal-relation identification are in
the accompanying research note.
"""
from itertools import product
from pathlib import Path
import json

p = 5
I = (1, 0, 0, 1)
T = (1, 4, 1, 0)

def mm(a, b):
    return tuple(x % p for x in (
        a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
        a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))

def mv(a, v):
    return ((a[0]*v[0]+a[1]*v[1]) % p,
            (a[2]*v[0]+a[3]*v[1]) % p)

tp = [I]
for _ in range(6):
    tp.append(mm(tp[-1], T))
assert tp[3] == (4, 0, 0, 4) and tp[6] == I
one = ((0, 0), 0)

def mul(a, b):
    w = mv(tp[a[1]], b[0])
    return (((a[0][0]+w[0]) % p, (a[0][1]+w[1]) % p),
            (a[1]+b[1]) % 6)

def inv(a):
    v = mv(tp[-a[1] % 6], a[0])
    return (((-v[0]) % p, (-v[1]) % p), -a[1] % 6)

def power(a, n):
    z = one
    for _ in range(n):
        z = mul(z, a)
    return z

def conj(a, b):
    return mul(mul(a, b), inv(a))

S, R = ((0, 0), 3), ((1, 0), 4)
tau = mul(S, R)
assert power(S, 2) == one and power(R, 3) == one
assert tau == ((4, 0), 1)
seen, pending = {one}, [one]
while pending:
    g = pending.pop()
    for a in (S, R):
        h = mul(g, a)
        if h not in seen:
            seen.add(h)
            pending.append(h)
assert len(seen) == 150
group = sorted(seen)
kernel = [g for g in group if g[1] == 0]
assert len(kernel) == 25
k = ((3, 3), 0)

def phi(g):
    return conj(k, (((-g[0][0]) % p, (-g[0][1]) % p), g[1]))

assert phi(tau) == tau
assert all(phi(phi(g)) == g and phi(g)[1] == g[1] for g in group)
assert all(phi(mul(g, h)) == mul(phi(g), phi(h))
           for g in group for h in group)
assert all(phi(g) == inv(g) for g in kernel)
assert phi(((1, 0), 0)) != ((1, 0), 0)
s_frames = [g for g in kernel if conj(g, S) == phi(S)]
r_frames = [g for g in kernel if conj(g, R) == phi(R)]
assert len(s_frames) == len(r_frames) == 1
assert s_frames == [k]
# Minimal polynomial X^2-X+1 is irreducible over F5, so End_C6(V)=F25.
assert not any((x*x-x+1) % p == 0 for x in range(p))
record = {
    "status": "PASS", "prime": p, "actual_group_order": len(group),
    "kernel_order": len(kernel), "T": T, "source_s": S, "source_r": R,
    "source_tau": tau, "inner_translation_k": k,
    "s_conjugator": s_frames[0], "r_conjugator": r_frames[0],
    "automorphism_product_checks": len(group)**2,
    "automorphism_square_checks": len(group),
    "literal_cusp_fixed": True, "induced_C6_action": "identity",
    "module_action": "minus identity", "automorphism_exact_order": 2,
    "scope": "Finite normalized positive peripheral automorphism kernel; no full-source torsion lift claimed."
}
out = Path(__file__).resolve().parents[1]/"odd_relation_automorphism_kernel_certificate.json"
out.write_text(json.dumps(record, indent=2)+"\n")
print("PASS: source s,r generate the actual order150 first mod5 relation quotient")
print("PASS: 22500 product identities and150 automorphism square identities")
print("PASS: literal cusp fixed, quotient C6 action identity, kernel action minus identity")
print("PASS: source s/r peripheral conjugators", s_frames[0], r_frames[0])
print("PASS: exact automorphism order2 inside the normalized peripheral kernel")
print("Scope: this is not a full-source realization or a negative norm obstruction")
