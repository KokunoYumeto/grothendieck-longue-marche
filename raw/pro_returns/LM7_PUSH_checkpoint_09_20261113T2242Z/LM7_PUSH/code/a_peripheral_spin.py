#!/usr/bin/env python3
"""Exact search for a nonzero peripheral chief-step obstruction.

Searches triples in PSL(2,p), for p in {5,7,11}, with equal ordered
conjugacy profiles but different canonical odd-order lifting invariant
in SL(2,p).  All groups and products are constructed from matrices,
with no database input.  The finite order bound is certified only for
these three explicitly supported primes.
"""

from collections import deque
from itertools import product
import argparse
import json
from pathlib import Path

P = 5
ONE = (1, 0, 0, 1)
MINUS = (4, 0, 0, 4)


def mul(a, b):
    x, y, z, t = a
    u, v, w, s = b
    return ((x*u+y*w) % P, (x*v+y*s) % P,
            (z*u+t*w) % P, (z*v+t*s) % P)


def inv(a):
    x, y, z, t = a
    return (t, -y % P, -z % P, x)


def neg(a):
    return tuple(-x % P for x in a)


def project(a):
    return min(a, neg(a))


def qmul(a, b):
    return project(mul(a, b))


def qinv(a):
    return project(inv(a))


def order(a, multiplication, identity):
    v = identity
    for n in range(1, 121):
        v = multiplication(v, a)
        if v == identity:
            return n
    raise AssertionError("order bound")


def generated(gens, multiplication, identity):
    seen = {identity}
    queue = deque([identity])
    while queue:
        a = queue.popleft()
        for b in gens:
            c = multiplication(a, b)
            if c not in seen:
                seen.add(c)
                queue.append(c)
    return seen


def main():
    global P, MINUS
    parser = argparse.ArgumentParser()
    parser.add_argument('--prime', type=int, default=5)
    parser.add_argument('--prefix', default=None)
    parser.add_argument('--first-match', action='store_true')
    args = parser.parse_args()
    P = args.prime
    if P not in (5, 7, 11):
        parser.error('the certified finite search supports --prime 5, 7, or 11')
    MINUS = (P - 1, 0, 0, P - 1)
    prefix = Path(args.prefix) if args.prefix else Path(__file__).with_suffix('')
    sl = [a for a in product(range(P), repeat=4)
          if (a[0]*a[3]-a[1]*a[2]) % P == 1]
    ps = sorted({project(a) for a in sl})
    qone = project(ONE)
    assert len(sl) == P * (P * P - 1) and len(ps) * 2 == len(sl)
    qorders = {a: order(a, qmul, qone) for a in ps}
    classes = {}
    class_sets = []
    for a in ps:
        if a in classes:
            continue
        conj = {qmul(qmul(h, a), qinv(h)) for h in ps}
        idx = len(class_sets)
        class_sets.append(conj)
        for h in conj:
            classes[h] = idx
    print(f"PSL(2,{P}) conjugacy classes (order,size):",
          [(qorders[next(iter(s))], len(s)) for s in class_sets])
    odd = [a for a in ps if qorders[a] > 1 and qorders[a] % 2]
    lifts = {}
    for a in odd:
        candidates = [b for b in [a, neg(a)]
                      if order(b, mul, ONE) == qorders[a]]
        assert len(candidates) == 1
        lifts[a] = candidates[0]
    examples = {}
    counts = {}
    for a, b in product(odd, repeat=2):
        c = qinv(qmul(a, b))
        if c not in lifts:
            continue
        spin = mul(mul(lifts[a], lifts[b]), lifts[c])
        assert spin in [ONE, MINUS]
        sign = 1 if spin == ONE else -1
        profile = tuple(classes[t] for t in (a, b, c))
        key = (profile, sign)
        if args.first_match and key in examples:
            continue
        if len(generated([a, b], qmul, qone)) != len(ps):
            continue
        counts[key] = counts.get(key, 0) + 1
        examples.setdefault(key, (a, b, c))
        if args.first_match and (profile, -sign) in examples:
            break
    print("Generating odd triples by conjugacy profile and spin:")
    for key in sorted(counts):
        print(key, counts[key])
    both = [p for p, sign in examples
            if sign == 1 and (p, -1) in examples]
    payload = {
        "sl_order": len(sl),
        "psl_order": len(ps),
        "prime": P,
        "search_scope": "first verified generating representative per profile/spin; stop at first match" if args.first_match else "exhaustive odd-order generating triples",
        "counts": [{"profile": p, "spin": s, "count": counts[(p, s)]}
                   for p, s in sorted(counts)],
        "matching_spin_profiles": both,
    }
    if both:
        profile = min(both)
        plus = examples[(profile, 1)]
        minus = examples[(profile, -1)]
        g_gens = [(plus[i], minus[i]) for i in range(2)]
        e_gens = [(lifts[plus[i]], minus[i]) for i in range(2)]
        gm = lambda a, b: (qmul(a[0], b[0]), qmul(a[1], b[1]))
        em = lambda a, b: (mul(a[0], b[0]), qmul(a[1], b[1]))
        gsize = len(generated(g_gens, gm, (qone, qone)))
        esize = len(generated(e_gens, em, (ONE, qone)))
        assert gsize == len(ps) ** 2 and esize == len(sl) * len(ps)
        swapped_lifts = [(lifts[minus[i]], plus[i]) for i in range(3)]
        obstruction = em(em(swapped_lifts[0], swapped_lifts[1]), swapped_lifts[2])
        assert obstruction == (MINUS, qone)
        conjugators = []
        for i in range(3):
            found = next(h for h in sl
                         if mul(mul(h, lifts[plus[i]]), inv(h)) == lifts[minus[i]])
            conjugators.append(found)
        payload.update({
            "status": "PASS_EXPLICIT_NONZERO_OBSTRUCTION",
            "profile": profile,
            "plus_triple": plus,
            "minus_triple": minus,
            "canonical_odd_lifts_plus": [lifts[a] for a in plus],
            "canonical_odd_lifts_minus": [lifts[a] for a in minus],
            "canonical_odd_orders": [qorders[a] for a in plus],
            "canonical_plus_product": mul(mul(lifts[plus[0]], lifts[plus[1]]), lifts[plus[2]]),
            "canonical_minus_product": mul(mul(lifts[minus[0]], lifts[minus[1]]), lifts[minus[2]]),
            "sl_conjugators_plus_to_minus": conjugators,
            "base_generated_order": gsize,
            "extension_generated_order": esize,
            "swapped_peripheral_obstruction": obstruction,
            "kernel_order": 2,
        })
        print("EXPLICIT obstruction:", obstruction)
        print("Canonical odd lifts, plus:", [lifts[a] for a in plus])
        print("Canonical odd lifts, minus:", [lifts[a] for a in minus])
        print("Base generated order:", gsize, "extension generated order:", esize)
        print("PASS_EXPLICIT_NONZERO_OBSTRUCTION")
    else:
        payload["status"] = "NO_MATCHING_PROFILE_IN_THIS_SEARCH"
        print(payload["status"])
    prefix.with_suffix(".json").write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
