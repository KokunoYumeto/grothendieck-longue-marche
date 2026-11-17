"""Exact chart and finite separation for the relative special-fiber counterexample."""
from itertools import permutations
from pathlib import Path
import json
import sympy as sp

root = Path(__file__).resolve().parents[1]
lam, z, r = sp.symbols('lambda z r')
inverse = z + r * (1 - z)
assert sp.cancel((inverse - z) / (1 - z) - r) == 0
assert sp.factor(inverse - 1) == -(r - 1) * (z - 1)
assert sp.factor(inverse - z) == -r * (z - 1)
special = z / (z - 1)
assert sp.cancel(z + special * (1 - z)) == 0
assert sp.cancel(special.subs(z, special) - z) == 0

identity = (0, 1, 2)
def mul(a, b):
    return tuple(a[b[i]] for i in range(3))
def inv(a):
    return tuple(a.index(i) for i in range(3))
def closure(gens):
    reached = {identity}
    pending = [identity]
    while pending:
        a = pending.pop()
        for b in gens:
            c = mul(a, b)
            if c not in reached:
                reached.add(c)
                pending.append(c)
    return reached

a, b = (1, 0, 2), (0, 2, 1)
s3 = set(permutations(range(3)))
assert closure([a, b]) == s3
commutator = mul(mul(mul(a, b), inv(a)), inv(b))
assert commutator != identity
assert mul(mul(commutator, commutator), commutator) == identity
diagonal = {(g, g) for g in s3}
witness = (commutator, identity)
assert witness not in diagonal

def pairmul(x, y):
    return mul(x[0], y[0]), mul(x[1], y[1])
product = {(g, h) for g in s3 for h in s3}
assert len(product) == 36 and len(diagonal) == 6
assert all(pairmul(x, y) in product for x in product for y in product)
assert all(pairmul(x, y) in diagonal for x in diagonal for y in diagonal)
result = {
    'chart': 'r=(lambda-z)/(1-z), inverse lambda=z+r(1-z)',
    'special_graph': 'r=z/(z-1), an involutory automorphism of C minus {0,1}',
    'chart_identities': 'PASS',
    'ambient_fundamental_group': 'F2 times F2, proved from the exact product chart',
    'filled_group': 'Z^3, proved by the node van Kampen calculation in the working proof',
    'product_order': len(product),
    'graph_image_order': len(diagonal),
    'permutation_generators': [a, b],
    'commutator_first_factor': commutator,
    'deletion_kernel_witness_image': witness,
    'outside_source_graph': True,
    'scope': 'Counterexample to broad relative special-fiber surjectivity, not to the actual icosahedral marginal statement.'
}
out = root / 'records/special_fiber_relative_counterexample.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))

