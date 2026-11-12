#!/usr/bin/env python3
"""Independent sparse-word verification of ceh_pro2_cover.cpp certificates.

The C++ search uses bit-packed polynomials and Gaussian elimination.
This verifier uses sets of literal words, reconstructs all automorphisms
from group commutators, and checks supplied dual inconsistency certificates
by addition only. It also independently closes the geometric image.
"""
from collections import deque
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

WORDS = tuple(w for n in range(5) for w in product(range(3), repeat=n))
INDEX = {w: i for i, w in enumerate(WORDS)}
ONE = frozenset([()])
ZERO = frozenset()
GEN = tuple(frozenset([(), (i,)]) for i in range(3))

def plus(a, b):
    return a ^ b

def times(a, b):
    out = set()
    for u in a:
        for v in b:
            if len(u) + len(v) <= 4:
                w = u + v
                if w in out:
                    out.remove(w)
                else:
                    out.add(w)
    return frozenset(out)

def inverse(a):
    assert () in a
    h, term, result = a ^ ONE, ONE, ONE
    for _ in range(4):
        term = times(term, h)
        result ^= term
    assert times(a, result) == ONE == times(result, a)
    return result

def conjugate(c, a):
    return times(times(c, a), inverse(c))

def commutator(a, b):
    return times(times(times(a, b), inverse(a)), inverse(b))

def substitution(a, p):
    aug = tuple(q ^ ONE for q in a)

    @lru_cache(None)
    def monomial(w):
        if not w:
            return ONE
        return times(monomial(w[:-1]), aug[w[-1]])

    out = ZERO
    for w in p:
        out ^= monomial(w)
    return out

def compose(a, b):
    return tuple(substitution(a, q) for q in b)

def rows(a, b):
    """Equations c*b_i=a_i*c, including constant term of c fixed to one."""
    out = [0] * (3 * len(WORDS))
    for k in range(3):
        for w in a[k] ^ b[k]:
            out[k * 121 + INDEX[w]] ^= 1 << 39
        for j, w in enumerate(WORDS[1:40]):
            for v in b[k]:
                if len(w) + len(v) <= 4:
                    out[k * 121 + INDEX[w + v]] ^= 1 << j
            for v in a[k]:
                if len(w) + len(v) <= 4:
                    out[k * 121 + INDEX[v + w]] ^= 1 << j
    return out

def main():
    cert_path = (Path(sys.argv[1]) if len(sys.argv) > 1 else
                 Path(__file__).with_name("ceh_pro2_certificates.json"))
    raw = cert_path.read_bytes()
    data = json.loads(raw)
    assert data["witness_mask"] == 1
    x, y, z = GEN
    P = times(times(x, y), z)
    delta = (conjugate(y, z), y, x)
    dinverse = (z, y, conjugate(inverse(y), x))
    assert compose(delta, dinverse) == GEN == compose(dinverse, delta)
    assert compose(delta, delta) == tuple(conjugate(y, q) for q in GEN)
    xy, yz = times(x, y), times(y, z)
    twists = ((conjugate(xy, x), conjugate(xy, y), z),
              (x, conjugate(yz, y), conjugate(yz, z)))
    tinverses = ((conjugate(inverse(xy), x), conjugate(inverse(xy), y), z),
                 (x, conjugate(inverse(yz), y), conjugate(inverse(yz), z)))
    for t, ti in zip(twists, tinverses):
        assert compose(t, ti) == GEN == compose(ti, t)
        assert substitution(t, P) == P
    group, queue = {GEN}, deque([GEN])
    while queue:
        a = queue.popleft()
        for t in twists:
            b = compose(t, a)
            if b not in group:
                group.add(b)
                queue.append(b)
                assert len(group) <= 128
    assert len(group) == data["geometric_group_order"] == 128

    # This construction uses actual group commutators, not the C++ Lie formula.
    ax = commutator(commutator(x, y), y)
    ay = commutator(x, commutator(x, y))
    alpha = (conjugate(ax, x), conjugate(ay, y), z)
    assert substitution(alpha, P) == P
    assert compose(alpha, alpha) == GEN
    target = compose(compose(alpha, delta), alpha)
    orbit = set()
    for record in data["certificates"]:
        a, ai = GEN, GEN
        for j in record["twist_word"]:
            assert j in (0, 1)
            a = compose(twists[j], a)
            ai = compose(ai, tinverses[j])
        assert a in group and compose(a, ai) == GEN == compose(ai, a)
        b = compose(compose(a, delta), ai)
        assert b not in orbit
        orbit.add(b)
        eq = rows(target, b)
        check = 0
        for i in record["equation_rows"]:
            check ^= eq[i]
        assert check == 1 << 39, "The dual certificate must give 0=1."
    assert len(orbit) == len(data["certificates"]) == 64
    # The listed orbit is closed under conjugation by both generators and inverses.
    for b in orbit:
        for t, ti in zip(twists, tinverses):
            assert compose(compose(t, b), ti) in orbit
            assert compose(compose(ti, b), t) in orbit
    assert delta in orbit
    report = {
        "algebra_field": "F_2",
        "algebra_word_lengths": [0, 1, 2, 3, 4],
        "algebra_dimension": len(WORDS),
        "geometric_aut_image_order": len(group),
        "geometric_deck_orbit_size": len(orbit),
        "dual_inconsistency_certificates_verified": len(data["certificates"]),
        "all_orbit_elements_covered": True,
        "witness_built_from_group_commutators": True,
        "witness_fixes_boundary_product": True,
        "witness_involutive_on_this_quotient": True,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
    }
    print(json.dumps(report, indent=2))
    Path(__file__).with_name("ceh_pro2_verification.json").write_text(
        json.dumps(report, indent=2) + "\n")

if __name__ == "__main__":
    main()
