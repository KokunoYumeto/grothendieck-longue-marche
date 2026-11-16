#!/usr/bin/env python3
"""Exact certificates for FF.40--FF.41 and FF.46--FF.47 kernel tests.

Polynomials are integral coefficient tuples in ascending powers of p.
Unipotent matrices are computed over Z, so the identities remain true
after reduction at every prime, including 2. These finite checks do not
certify the infinite Galois, Kummer, or topos arguments.
"""


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    return trim(tuple((a[i] if i < len(a) else 0)
                      + (b[i] if i < len(b) else 0)
                      for i in range(max(len(a), len(b)))))


def scale(c, a):
    return trim(tuple(c * x for x in a))


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def power(a, n):
    out = (1,)
    for _ in range(n):
        out = mul(out, a)
    return out


a1, a2, a3, a4, a6 = (1,), (0,), (0,), (0,), (0, -1)
b2 = add(power(a1, 2), scale(4, a2))
b4 = add(scale(2, a4), mul(a1, a3))
b6 = add(power(a3, 2), scale(4, a6))
b8 = add(add(mul(power(a1, 2), a6), scale(4, mul(a2, a6))),
         add(scale(-1, mul(mul(a1, a3), a4)),
             add(mul(a2, power(a3, 2)), scale(-1, power(a4, 2)))))
c4 = add(power(b2, 2), scale(-24, b4))
c6 = add(add(scale(-1, power(b2, 3)), scale(36, mul(b2, b4))),
         scale(-216, b6))
delta = add(add(scale(-1, mul(power(b2, 2), b8)),
                scale(-8, power(b4, 3))),
            add(scale(-27, power(b6, 2)), scale(9, mul(mul(b2, b4), b6))))
assert c4 == (1,)
assert delta == (0, 1, -432)
assert add(power(c4, 3), scale(-1, power(c6, 2))) == scale(1728, delta)
print("FF.41 integral polynomial certificates")
print("b2 = 1; b4 = 0; b6 = -4*p; b8 = -p")
print("c4 = 1; c6 = -1 + 864*p; Delta = p - 432*p^2")
print("c4^3 - c6^2 = 1728*Delta: verified")
print("For every prime p, 1-432*p is a p-adic unit; v_p(Delta)=1.")


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mm(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def ma(a, b, sign=1):
    return [[x + sign * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def inverse_unipotent(a):
    n = len(a)
    eye = identity(n)
    u = ma(a, eye, -1)
    out, term = eye, eye
    for exponent in range(1, n):
        term = mm(term, u)
        out = ma(out, term, (-1) ** exponent)
    assert mm(a, out) == eye == mm(out, a)
    return out


def elementary(n, i, j):
    out = identity(n)
    out[i - 1][j - 1] = 1
    return out


def comm(a, b):
    return mm(mm(mm(a, b), inverse_unipotent(a)), inverse_unipotent(b))


x = [elementary(9, i, i + 1) for i in range(1, 9)]
u = comm(comm(x[0], x[1]), comm(x[2], x[3]))
v = comm(comm(x[4], x[5]), comm(x[6], x[7]))
w = comm(u, v)
assert u == elementary(9, 1, 5)
assert v == elementary(9, 5, 9)
assert w == elementary(9, 1, 9)
print("FF.40 UT_9(Z) certificates, [a,b]=a*b*a^(-1)*b^(-1)")
print("[[x1,x2],[x3,x4]] = 1 + E_(1,5): verified")
print("[[x5,x6],[x7,x8]] = 1 + E_(5,9): verified")
print("[1 + E_(1,5), 1 + E_(5,9)] = 1 + E_(1,9): verified")
print("The last entry is 1 over Z, so remains nonzero modulo every prime.")
print("No global Tate parameter q, topos map, or infinite theorem is computed.")


# A finite certificate for the abstract IA obstruction.  The coordinate
# group is (Z/q)^3 x (Z/q)^3 with B(a,a')=(a1*a2',a1*a3',a2*a3').
# Bilinearity of B proves associativity over Z as well as modulo q.
from itertools import product


def c2_mul(g, h, q):
    a, c = g[:3], g[3:]
    b, d = h[:3], h[3:]
    correction = (a[0]*b[1], a[0]*b[2], a[1]*b[2])
    return tuple((a[i]+b[i]) % q for i in range(3)) + tuple(
        (c[i]+d[i]+correction[i]) % q for i in range(3))


def c2_inv(g, q):
    a, c = g[:3], g[3:]
    diagonal = (a[0]*a[1], a[0]*a[2], a[1]*a[2])
    return tuple(-x % q for x in a) + tuple(
        (-c[i]+diagonal[i]) % q for i in range(3))


def c2_conj(w, g, q):
    return c2_mul(c2_mul(w, g, q), c2_inv(w, q), q)


def c2_ia(g, q):
    a, b, c, d12, d13, d23 = g
    return a, b, c, (d12+b-a) % q, d13, d23


generators = ((1, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0),
              (0, 0, 1, 0, 0, 0))
print("Abstract four-puncture IA certificate (no arithmetic compatibility)")
for modulus in (2, 3, 4, 5, 8):
    gx, gy, gz = generators
    xy = c2_mul(gx, gy, modulus)
    desired = (c2_conj(xy, gx, modulus),
               c2_conj(xy, gy, modulus), gz)
    assert desired == tuple(c2_ia(g, modulus) for g in generators)
    assert c2_ia(xy, modulus) == xy
    assert c2_ia(c2_mul(xy, gz, modulus), modulus) == c2_mul(xy, gz, modulus)
    matching_xy = []
    matching_all = []
    for abc in product(range(modulus), repeat=3):
        # Central coordinates do not change conjugation.
        candidate = abc+(0, 0, 0)
        images = tuple(c2_conj(candidate, g, modulus) for g in generators)
        if images[:2] == desired[:2]:
            matching_xy.append(abc)
        if images == desired:
            matching_all.append(abc)
    assert matching_xy == [(1, 1, 0)]
    assert matching_all == []
    print(f"mod {modulus}: unique inner candidate on x,y = (1,1,0); "
          "none fixes z as required")

elements = list(product(range(2), repeat=6))
assert len({c2_ia(g, 2) for g in elements}) == 64
for g in elements:
    assert c2_mul(g, c2_inv(g, 2), 2) == (0,)*6
    for h in elements:
        assert c2_ia(c2_mul(g, h, 2), 2) == c2_mul(c2_ia(g, 2), c2_ia(h, 2), 2)
print("Order-64 group: all 4096 products preserve the IA map; it is bijective.")
print("The finite IA example is not asserted to commute with G_E or define a topos ghost.")


# FF.47: the same word automorphism on the full free profinite group
# is detected by a genus-zero degree-three permutation cover.
from itertools import permutations


def perm_mul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def perm_inv(a):
    return tuple(a.index(i) for i in range(len(a)))


def perm_conj(a, b):
    return perm_mul(perm_mul(a, b), perm_inv(a))


def cycle_count(a):
    seen = set()
    count = 0
    for i in range(len(a)):
        if i not in seen:
            count += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = a[j]
    return count


s3 = list(permutations(range(3)))
perm_identity = (0, 1, 2)
tx, ty, tz, tw = (1, 0, 2), (0, 2, 1), (1, 0, 2), (2, 1, 0)
original = (tx, ty, tz, tw)
total = perm_identity
for branch in original:
    total = perm_mul(total, branch)
assert total == perm_identity
generated = {perm_identity}
while True:
    enlarged = generated | {perm_mul(g, t) for g in generated for t in original}
    if enlarged == generated:
        break
    generated = enlarged
assert generated == set(s3)
ramification = sum(3-cycle_count(t) for t in original)
assert ramification == 4
assert (-2*3+ramification+2)//2 == 0
pc = perm_mul(tx, ty)
transformed = (perm_conj(pc, tx), perm_conj(pc, ty), tz, tw)
assert transformed != original
conjugators = [s for s in s3 if tuple(perm_conj(s, t) for t in original) == transformed]
assert conjugators == []
common_centralizer = [s for s in s3 if perm_conj(s, tz) == tz and perm_conj(s, tw) == tw]
assert common_centralizer == [perm_identity]
print("FF.47 full-profinite S3 cover certificate")
print("Branch tuple ((12),(23),(12),(13)): product=1; generated group=S3.")
print("Degree=3; total ramification=4; smooth completion genus=0.")
print("Partial conjugation changes the tuple; none of 6 simultaneous conjugators works.")
print("This tests the full profinite word automorphism; S3 is not a p-group.")


# FF.48: the Lattes degree-nine cover has full group F_3^2 semidirect C_2.
# This checks the finite monodromy/core calculation, not the geometric theorem.
lattes_points = list(product(range(3), repeat=2))
lattes_group = [(a, b, sign) for a, b in lattes_points for sign in (1, -1)]


def lattes_mul(g, h):
    a, b, s = g
    c, d, t = h
    return ((a+s*c) % 3, (b+s*d) % 3, s*t)


def lattes_inv(g):
    a, b, s = g
    return ((-s*a) % 3, (-s*b) % 3, s)


def lattes_conj(g, h):
    return lattes_mul(lattes_mul(g, h), lattes_inv(g))


def lattes_perm(g):
    a, b, s = g
    return tuple(lattes_points.index(((a+s*x) % 3, (b+s*y) % 3))
                 for x, y in lattes_points)


assert len(lattes_group) == 18
assert len({lattes_perm(g) for g in lattes_group}) == 18
for g in lattes_group:
    for h in lattes_group:
        assert lattes_perm(lattes_mul(g, h)) == perm_mul(lattes_perm(g), lattes_perm(h))
lattes_h = {(0, 0, 1), (0, 0, -1)}
lattes_core = set(lattes_h)
for g in lattes_group:
    lattes_core &= {lattes_conj(g, h) for h in lattes_h}
assert lattes_core == {(0, 0, 1)}
assert len({lattes_perm(g)[0] for g in lattes_group}) == 9
translation_group = {(a, b, 1) for a, b in lattes_points}
assert len(translation_group) == 9
for g in lattes_group:
    assert {lattes_conj(g, h) for h in translation_group} == translation_group
print("FF.48 Lattes finite-group certificate")
print("F_3^2 semidirect {+1,-1}: order18; faithful transitive action of degree9.")
print("All324 products agree with permutation composition; reflection core is trivial.")
print("The translation subgroup is normal of order9, giving the original double-cover quotient.")


# FF.48, trigonal genus-one consequence: complete finite lifting certificate.
# The S4 quotient acts on the three partitions of four letters into two pairs.
from pathlib import Path
import json

four_pairings = [frozenset((frozenset(a), frozenset(b)))
                 for a, b in (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))]


def s4_to_s3(g):
    return tuple(four_pairings.index(frozenset(frozenset(g[i] for i in pair)
                                             for pair in matching))
                 for matching in four_pairings)


def tuple_product(seq, n):
    ans = tuple(range(n))
    for g in seq:
        ans = perm_mul(ans, g)
    return ans


def generated_permutations(seq, n):
    found = {tuple(range(n))}
    while True:
        enlarged = found | {perm_mul(g, h) for g in found for h in seq}
        if enlarged == found:
            return found
        found = enlarged


s4 = list(permutations(range(4)))
s4_transpositions = [g for g in s4 if cycle_count(g) == 3]
s3_transpositions = sorted({s4_to_s3(g) for g in s4_transpositions})
assert len(s4_transpositions) == 6 and len(s3_transpositions) == 3
transposition_lifts = {g: [h for h in s4_transpositions if s4_to_s3(h) == g]
                       for g in s3_transpositions}
assert all(len(v) == 2 for v in transposition_lifts.values())
for g in s4:
    for h in s4:
        assert s4_to_s3(perm_mul(g, h)) == perm_mul(s4_to_s3(g), s4_to_s3(h))
s3_nonidentity = [g for g in s3 if g != tuple(range(3))]
index_preserving_lifts = {
    g: [h for h in s4 if s4_to_s3(h) == g and 4-cycle_count(h) == 3-cycle_count(g)]
    for g in s3_nonidentity
}
recillas_certificates = []
lift_counts = []
ramification_counts = {}
for branch_count in (4, 5, 6):
    valid_count = 0
    for cubic_tuple in product(s3_nonidentity, repeat=branch_count):
        if sum(3-cycle_count(g) for g in cubic_tuple) != 6:
            continue
        if tuple_product(cubic_tuple, 3) != tuple(range(3)):
            continue
        if len(generated_permutations(cubic_tuple, 3)) != 6:
            continue
        good_lifts = []
        for lifted_tuple in product(*(index_preserving_lifts[g] for g in cubic_tuple)):
            if tuple_product(lifted_tuple, 4) != tuple(range(4)):
                continue
            if len(generated_permutations(lifted_tuple, 4)) == 24:
                good_lifts.append(lifted_tuple)
        assert good_lifts
        lift_counts.append(len(good_lifts))
        chosen = good_lifts[0]
        assert tuple(s4_to_s3(g) for g in chosen) == cubic_tuple
        assert (-2*3+sum(3-cycle_count(g) for g in cubic_tuple)+2)//2 == 1
        assert (-2*4+sum(4-cycle_count(g) for g in chosen)+2)//2 == 0
        recillas_certificates.append({"cubic_tuple": cubic_tuple, "quartic_tuple": chosen,
                                      "number_of_transitive_lifts": len(good_lifts)})
        valid_count += 1
    ramification_counts[branch_count] = valid_count
assert ramification_counts == {4: 72, 5: 270, 6: 240}
assert len(recillas_certificates) == 582
assert set(lift_counts) == {12}
certificate_path = Path(__file__).resolve().parent / "F_recillas_certificates.json"
certificate_path.write_text(json.dumps(recillas_certificates, indent=2)+"\n")
print("FF.48 trigonal genus-one finite lifting certificate")
print("All19375 nonidentity tuples of lengths4,5,6 examined.")
print("Total-index6, product1, full S3:72 tuples of length4;270 of length5;240 of length6.")
print("Every tuple has exactly12 index-preserving lifts with product1 generating S4.")
print("Cubic source genus1; quartic source genus0; all582 explicit witnesses saved.")
print("Certificate file: F_recillas_certificates.json")
