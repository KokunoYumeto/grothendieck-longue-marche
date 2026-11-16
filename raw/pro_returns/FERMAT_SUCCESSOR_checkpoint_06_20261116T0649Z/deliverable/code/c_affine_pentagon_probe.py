"""Actual distinct-endpoint affine B4 quotients and all five f evaluations.

This exploratory exact calculation computes the common free-group image,
not a Cartesian product of independently selected f values.  It reports
the source and derived-source orders before deciding enumeration feasibility.
"""
import argparse
from collections import deque
import json
from pathlib import Path
from sympy.combinatorics import Permutation, PermutationGroup

parser = argparse.ArgumentParser()
parser.add_argument("--modulus", type=int, default=3)
parser.add_argument("--relations", choices=("base", "all", "none"), default="base")
parser.add_argument("--enumerate-limit", type=int, default=1000000)
parser.add_argument("--complete-orbits", action="store_true")
args = parser.parse_args()
m = args.modulus
I = (0, 0, 1, 0, 0, 1)


def mul(g, h):
    u, v, a, b, c, d = g
    x, y, e, f, k, l = h
    return ((u+a*x+b*y) % m, (v+c*x+d*y) % m,
            (a*e+b*k) % m, (a*f+b*l) % m,
            (c*e+d*k) % m, (c*f+d*l) % m)


def inverse(g):
    u, v, a, b, c, d = g
    assert (a*d-b*c) % m == 1
    return ((-d*u+b*v) % m, (c*u-a*v) % m,
            d % m, -b % m, -c % m, a % m)


T = (0, 0, 1, 1, 0, 1)
U = (0, 0, 1, 0, -1 % m, 1)
C = (1, 0, 1, 1, 0, 1)
assert mul(mul(T, U), T) == mul(mul(U, T), U)
assert mul(mul(C, U), C) == mul(mul(U, C), U)
assert mul(T, C) == mul(C, T)
assert T != C
a, b, e = mul(T, T), mul(U, U), mul(C, C)
c, d = mul(mul(U, a), inverse(U)), mul(mul(C, b), inverse(C))
initial = [(b, e), (mul(a, c), mul(d, e)), (a, b),
           (a, mul(b, d)), (mul(c, b), e)]
pairs = []


def include(pair):
    if pair not in pairs:
        pairs.append(pair)
    return pairs.index(pair)


pentagon_indices = [include(pair) for pair in initial]
relation_indices = []
relation_pairs = initial if args.relations == "all" else [initial[2]] if args.relations == "base" else []
if args.complete_orbits:
    expanded = []
    for x, y in relation_pairs:
        z = inverse(mul(x, y))
        for pair in [(x, y), (y, x), (z, x), (x, z), (y, z), (z, y)]:
            if pair not in expanded:
                expanded.append(pair)
    relation_pairs = expanded
for x, y in relation_pairs:
    z = inverse(mul(x, y))
    relation_indices.append({"xy": include((x, y)), "yx": include((y, x)),
                             "zx": include((z, x)), "yz": include((y, z))})


def permutation(g):
    u, v, a, b, c, d = g
    return [(u+a*x+b*y) % m + m*((v+c*x+d*y) % m)
            for y in range(m) for x in range(m)]


def block_permutation(elements):
    values = []
    for j, g in enumerate(elements):
        values += [j*m*m + p for p in permutation(g)]
    return Permutation(values)


X, Y = [block_permutation([pair[j] for pair in pairs]) for j in (0, 1)]
source = PermutationGroup([X, Y])
derived = source.derived_subgroup()
summary = {"modulus": m, "relations_checked_at": args.relations,
           "complete_six_substitution_orbits": args.complete_orbits,
           "number_of_distinct_evaluation_pairs": len(pairs),
           "faithful_permutation_degree": len(pairs)*m*m,
           "source_order": int(source.order()), "derived_source_order": int(derived.order()),
           "derived_generators": len(derived.generators),
           "pentagon_indices": pentagon_indices, "relation_indices": relation_indices,
           "distinct_braid_endpoints": True,
           "scope": "Actual common image of F2 and F2-prime in the five pentagon evaluations and the specified necessary gentle equations; no CM-frame bridge or profinite-lift assertion."}


def decode(permutation_value):
    """Recover the affine element on each block; verify every point.

    SymPy multiplies permutations in the opposite composition convention
    from mul above. This has no effect on the subgroup or its derived
    subgroup as sets. All equations below use our explicit affine mul.
    """
    answer = []
    for j in range(len(pairs)):
        offset = j*m*m
        images = [permutation_value(offset+i)-offset for i in range(m*m)]
        u, v = images[0] % m, images[0] // m
        a, c = (images[1] % m-u) % m, (images[1] // m-v) % m
        b, d = (images[m] % m-u) % m, (images[m] // m-v) % m
        element = (u, v, a, b, c, d)
        assert permutation(element) == images
        answer.append(element)
    return answer


def necessary_gentle(values):
    for relation in relation_indices:
        fxy, fyx, fzx, fyz = [values[relation[k]] for k in ("xy", "yx", "zx", "yz")]
        if mul(fyx, fxy) != I or mul(mul(fzx, fyz), fxy) != I:
            return False
    return True


def pentagon_holds(values):
    f0, f1, f2, f3, f4 = [values[i] for i in pentagon_indices]
    return mul(mul(f0, f1), f2) == mul(f3, f4)


survivors = []
failures = []
if derived.order() <= args.enumerate_limit:
    visited = 0
    for f_value in derived.generate_schreier_sims():
        visited += 1
        values = decode(f_value)
        if necessary_gentle(values):
            if pentagon_holds(values):
                survivors.append(values)
            else:
                failures.append(values)
    assert visited == derived.order()
    summary.update({"enumeration_complete": True,
                    "elements_enumerated": visited,
                    "necessary_gentle_survivors": len(survivors)+len(failures),
                    "pentagon_survivors": len(survivors),
                    "pentagon_failures": len(failures),
                    "surviving_base_images": len({tuple(v[pentagon_indices[2]]) for v in survivors}),
                    "rejected_base_images": len({tuple(v[pentagon_indices[2]]) for v in failures})})
else:
    summary["enumeration_complete"] = False
payload = {"summary": summary, "evaluation_pairs": pairs,
           "source_generators": [list(X.array_form), list(Y.array_form)],
           "derived_generators": [list(g.array_form) for g in derived.generators],
           "survivor_values": survivors, "failure_values": failures}
name = "c_affine_pentagon_" + str(m) + "_" + args.relations + ("_orbits" if args.complete_orbits else "")
(Path(__file__).parent / (name + ".json")).write_text(json.dumps(payload, indent=2) + "\n")
print(json.dumps(summary, indent=2), flush=True)
