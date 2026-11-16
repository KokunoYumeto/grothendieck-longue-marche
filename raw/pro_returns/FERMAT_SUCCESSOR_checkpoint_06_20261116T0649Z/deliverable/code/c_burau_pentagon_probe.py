"""A different finite four-strand quotient: reduced Burau at t mod p.

The three matrices are derived by quotienting the unreduced four-dimensional
matrices by their common fixed vector (1,1,1,1). All braid relations are
checked directly before taking the faithful projective permutation action.
"""
import argparse
import json
from pathlib import Path
from sympy.combinatorics import Permutation, PermutationGroup

parser = argparse.ArgumentParser()
parser.add_argument("--prime", type=int, default=5)
parser.add_argument("--parameter", type=int, default=2)
parser.add_argument("--common", action="store_true")
parser.add_argument("--complete-orbits", action="store_true")
parser.add_argument("--enumerate-limit", type=int, default=1000000)
parser.add_argument("--output-suffix", default="")
args = parser.parse_args()
p, t = args.prime, args.parameter


def mul(a, b):
    return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3)) % p
                 for i in range(3) for j in range(3))


I = (1, 0, 0, 0, 1, 0, 0, 0, 1)


def inv(a):
    rows = [[a[3*i+j] for j in range(3)] + [int(i == j) for j in range(3)] for i in range(3)]
    for k in range(3):
        pivot = next(j for j in range(k, 3) if rows[j][k] % p)
        rows[k], rows[pivot] = rows[pivot], rows[k]
        z = pow(rows[k][k], -1, p)
        rows[k] = [z*x % p for x in rows[k]]
        for j in range(3):
            if j != k:
                z = rows[j][k]
                rows[j] = [(x-z*y) % p for x, y in zip(rows[j], rows[k])]
    answer = tuple(x for row in rows for x in row[3:])
    assert mul(a, answer) == I
    return answer


S = [tuple(z % p for z in M) for M in
     [(1-t, t, 0, 1, 0, 0, 0, 0, 1),
      (1, 0, 0, 0, 1-t, t, 0, 1, 0),
      (1, 0, -1, 0, 1, -1, 0, 0, -t)]]
assert mul(mul(S[0], S[1]), S[0]) == mul(mul(S[1], S[0]), S[1])
assert mul(mul(S[1], S[2]), S[1]) == mul(mul(S[2], S[1]), S[2])
assert mul(S[0], S[2]) == mul(S[2], S[0])
assert S[0] != S[2]
a, b, e = [mul(s, s) for s in S]
c, d = mul(mul(S[1], a), inv(S[1])), mul(mul(S[2], b), inv(S[2]))
initial = [(b, e), (mul(a, c), mul(d, e)), (a, b), (a, mul(b, d)), (mul(c, b), e)]


def projective(v):
    z = next(x for x in v if x % p)
    return tuple(x*pow(z, -1, p) % p for x in v)


points = sorted({projective((x, y, z)) for x in range(p) for y in range(p) for z in range(p) if x or y or z})
pointindex = {q: j for j, q in enumerate(points)}


def permutation(a):
    return [pointindex[projective(tuple(sum(a[3*i+k]*q[k] for k in range(3)) % p for i in range(3)))] for q in points]


pair_data = []
for j, (x, y) in enumerate(initial):
    H = PermutationGroup([Permutation(permutation(x)), Permutation(permutation(y))])
    D = H.derived_subgroup()
    row = {"pair_index": j, "order": int(H.order()), "derived_order": int(D.order()),
           "second_derived_order": int(D.derived_subgroup().order())}
    pair_data.append(row)
    print(json.dumps(row), flush=True)

pairs = initial[:]
relations = []


def include(pair):
    if pair not in pairs:
        pairs.append(pair)
    return pairs.index(pair)


relation_pairs = initial[:]
if args.complete_orbits:
    relation_pairs = []
    for x, y in initial:
        z = inv(mul(x, y))
        for pair in [(x, y), (y, x), (z, x), (x, z), (y, z), (z, y)]:
            if pair not in relation_pairs:
                relation_pairs.append(pair)
for x, y in relation_pairs:
    z = inv(mul(x, y))
    relations.append({"xy": include((x, y)), "yx": include((y, x)),
                      "zx": include((z, x)), "yz": include((y, z))})
summary = {"prime": p, "parameter": t, "projective_degree": len(points),
           "complete_six_substitution_orbits": args.complete_orbits,
           "braid_relations_verified": True, "distinct_endpoints": True, "pair_groups": pair_data}
if args.common:
    gen = []
    for j in (0, 1):
        values = []
        for k, pair in enumerate(pairs):
            values += [k*len(points)+i for i in permutation(pair[j])]
        gen.append(Permutation(values))
    H = PermutationGroup(gen)
    summary["common_source_order"] = int(H.order())
    print("Common source order", summary["common_source_order"], flush=True)
    D = H.derived_subgroup()
    summary["common_derived_order"] = int(D.order())
    print("Common derived order", summary["common_derived_order"], flush=True)
    summary["common_second_derived_order"] = int(D.derived_subgroup().order())
    print("Common second derived order", summary["common_second_derived_order"], flush=True)
    if D.order() <= args.enumerate_limit:
        unit = Permutation(list(range(len(points))))
        before, after, failed = 0, 0, 0
        base_before, base_after = set(), set()
        for f in D.generate_schreier_sims():
            v = []
            for j in range(len(pairs)):
                shift = j*len(points)
                v.append(Permutation([f(shift+i)-shift for i in range(len(points))]))
            if not all(v[r["xy"]]*v[r["yx"]] == unit and
                       v[r["xy"]]*v[r["yz"]]*v[r["zx"]] == unit for r in relations):
                continue
            before += 1
            base_before.add(tuple(v[2].array_form))
            if v[2]*v[1]*v[0] == v[4]*v[3]:
                after += 1
                base_after.add(tuple(v[2].array_form))
            else:
                failed += 1
        summary.update({"enumeration_complete": True, "necessary_gentle_candidates": before,
                        "pentagon_survivors": after, "pentagon_failures": failed,
                        "base_images_before": len(base_before), "base_images_after": len(base_after),
                        "same_base_image_set": base_before == base_after})
    else:
        summary["enumeration_complete"] = False
(Path(__file__).parent / ("c_burau_"+str(p)+"_"+str(t)+args.output_suffix+".json")).write_text(
    json.dumps({"summary": summary, "braid_matrices": S, "evaluation_pairs": pairs, "relations": relations}, indent=2)+"\n")
print(json.dumps(summary, indent=2), flush=True)
