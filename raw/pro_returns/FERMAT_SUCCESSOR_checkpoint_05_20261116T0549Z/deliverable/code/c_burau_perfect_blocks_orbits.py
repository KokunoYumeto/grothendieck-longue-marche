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



classes=[]
for j,pair in enumerate(initial):
    pass
payload=json.loads((Path(__file__).parent / "c_burau_11_2_orbits.json").read_text())
pairs=[(tuple(x),tuple(y)) for x,y in payload["evaluation_pairs"]]
perms=[(permutation(x),permutation(y)) for x,y in pairs]
for j in range(len(pairs)):
    orders=[]
    for block in classes:
        k=block[0]
        generators=[]
        for r in (0,1):
            generators.append(Permutation(perms[k][r]+[len(points)+i for i in perms[j][r]]))
        order=int(PermutationGroup(generators).derived_subgroup().order())
        orders.append(order)
        if order in (120,1320):
            block.append(j)
            break
    else:
        classes.append([j])
    print(j,orders,classes,flush=True)
(Path(__file__).parent / "c_burau_perfect_blocks_orbits.json").write_text(json.dumps(classes,indent=2)+"\n")
