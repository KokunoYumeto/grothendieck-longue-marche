"""Independent exhaustive verifier using only explicit affine arithmetic.

The derived image of a two-generator group is the normal closure of its
commutator. Enumerate this normal closure as the orbit of 1 under
h -> h[X,Y], h -> XhX^-1, and h -> YhY^-1. These are permutations of
the finite ambient group, so the forward orbit is also closed under their
inverses. It is exactly the derived subgroup. No permutation-group or
computer-algebra package is imported.
"""
import argparse
from collections import deque
import json
from pathlib import Path
import time

parser = argparse.ArgumentParser()
parser.add_argument("--moduli", default="3,4,5,8")
args = parser.parse_args()
outdir = Path(__file__).resolve().parent


def run(m):
    started = time.time()
    identity = (0, 0, 1, 0, 0, 1)

    def mul(g, h):
        u, v, a, b, c, d = g
        x, y, e, f, k, l = h
        return ((u+a*x+b*y) % m, (v+c*x+d*y) % m,
                (a*e+b*k) % m, (a*f+b*l) % m,
                (c*e+d*k) % m, (c*f+d*l) % m)

    def inv(g):
        u, v, a, b, c, d = g
        assert (a*d-b*c) % m == 1
        return ((-d*u+b*v) % m, (c*u-a*v) % m,
                d % m, -b % m, -c % m, a % m)

    t, u, c = (0, 0, 1, 1, 0, 1), (0, 0, 1, 0, -1 % m, 1), (1, 0, 1, 1, 0, 1)
    assert t != c
    assert mul(mul(t, u), t) == mul(mul(u, t), u)
    assert mul(mul(c, u), c) == mul(mul(u, c), u)
    assert mul(t, c) == mul(c, t)
    a, b, e = mul(t, t), mul(u, u), mul(c, c)
    x13, x24 = mul(mul(u, a), inv(u)), mul(mul(c, b), inv(c))
    initial = [(b, e), (mul(a, x13), mul(x24, e)),
               (a, b), (a, mul(b, x24)), (mul(x13, b), e)]
    pairs = initial[:]

    def include(pair):
        if pair not in pairs:
            pairs.append(pair)
        return pairs.index(pair)

    relation_pairs = []
    for x, y in initial:
        z = inv(mul(x, y))
        for pair in [(x, y), (y, x), (z, x), (x, z), (y, z), (z, y)]:
            if pair not in relation_pairs:
                relation_pairs.append(pair)
    relations = []
    for x, y in relation_pairs:
        z = inv(mul(x, y))
        relations.append(tuple(include(pair) for pair in [(x, y), (y, x), (z, x), (y, z)]))
    count = len(pairs)

    def pack(elements):
        return bytes(value for element in elements for value in element)

    def unpacks(h):
        return [tuple(h[6*j:6*j+6]) for j in range(count)]

    def product(g, h):
        answer = []
        for j in range(0, len(g), 6):
            u, v, a, b, c, d = g[j:j+6]
            x, y, e, f, k, l = h[j:j+6]
            answer.extend(((u+a*x+b*y) % m, (v+c*x+d*y) % m,
                           (a*e+b*k) % m, (a*f+b*l) % m,
                           (c*e+d*k) % m, (c*f+d*l) % m))
        return bytes(answer)

    X, Y = [pack(pair[j] for pair in pairs) for j in (0, 1)]
    XI, YI = [pack(inv(pair[j]) for pair in pairs) for j in (0, 1)]
    unit = pack([identity]*count)
    commutator = product(product(product(X, Y), XI), YI)
    words = {unit: ()}
    queue = deque([unit])
    gentle = []
    survivors, failures = [], []
    base_before, base_after = set(), set()
    while queue:
        h = queue.popleft()
        word = words[h]
        successors = [(product(h, commutator), word+(1, 2, -1, -2)),
                      (product(product(X, h), XI), (1,)+word+(-1,)),
                      (product(product(Y, h), YI), (2,)+word+(-2,))]
        for value, witness in successors:
            if value not in words:
                words[value] = witness
                queue.append(value)
        values = unpacks(h)
        if not all(mul(values[yx], values[xy]) == identity and
                   mul(mul(values[zx], values[yz]), values[xy]) == identity
                   for xy, yx, zx, yz in relations):
            continue
        gentle.append(h)
        base_before.add(values[2])
        assert sum(x for x in word if abs(x) == 1) == 0
        assert sum(x//2 for x in word if abs(x) == 2) == 0
        # Re-evaluate every retained word from the two source generators.
        value = unit
        for letter in word:
            value = product(value, {1: X, 2: Y, -1: XI, -2: YI}[letter])
        assert value == h
        good = mul(mul(values[0], values[1]), values[2]) == mul(values[3], values[4])
        certificate = {"word": word, "five_values": values[:5]}
        if good:
            survivors.append(certificate)
            base_after.add(values[2])
        else:
            failures.append(certificate)

    expected = json.loads((outdir / ("c_affine_pentagon_"+str(m)+"_all_orbits.json")).read_text())
    assert pairs == [(tuple(x), tuple(y)) for x, y in expected["evaluation_pairs"]]
    s = expected["summary"]
    assert len(words) == s["derived_source_order"]
    assert len(gentle) == s["necessary_gentle_survivors"]
    assert len(survivors) == s["pentagon_survivors"]
    assert len(failures) == s["pentagon_failures"]
    assert base_before == base_after
    summary = {"modulus": m, "derived_order": len(words),
               "gentle_necessary_candidates": len(gentle),
               "pentagon_survivors": len(survivors),
               "pentagon_failures": len(failures),
               "base_images_before": len(base_before), "base_images_after": len(base_after),
               "same_base_image_set": True,
               "independent_normal_closure_enumeration": True,
               "seconds": round(time.time()-started, 3)}
    (outdir / ("c_affine_pentagon_"+str(m)+"_words.json")).write_text(
        json.dumps({"summary": summary, "survivors": survivors, "failures": failures}, indent=2)+"\n")
    print(json.dumps(summary, sort_keys=True), flush=True)
    return summary


results = [run(int(value)) for value in args.moduli.split(",")]
Path(__file__).with_suffix(".json").write_text(json.dumps(results, indent=2)+"\n")
