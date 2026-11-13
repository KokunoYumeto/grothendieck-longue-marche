#!/usr/bin/env python3
"""Exact relative three-primary quotient beyond the coprime-kernel family.

The compatible lifting theorem is proved by the fibre-product and
abelianization maps in E.20. This program verifies its finite remaining
comparison: U4(F3) kills gamma4(N) gamma2(N)^3 N^9 and retains a literal
weight-three commutator. Every finite group operation is exact.
"""
from itertools import product
from pathlib import Path
import json

P = 3
ONE = tuple(int(i == j) for i in range(4) for j in range(4))
POSITIONS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def matrix(entries):
    out = list(ONE)
    for (i,j), value in zip(POSITIONS, entries):
        out[4*i+j] = value % P
    return tuple(out)

def mul(a,b):
    return tuple(sum(a[4*i+k]*b[4*k+j] for k in range(4)) % P
                 for i in range(4) for j in range(4))

def power(a,n):
    out = ONE
    while n:
        if n & 1:
            out = mul(out,a)
        a = mul(a,a)
        n >>= 1
    return out

def inv(a):
    # All strictly upper triangular fourth powers vanish.
    A = tuple((a[i]-ONE[i]) % P for i in range(16))
    A2 = mul(A,A)
    A3 = mul(A2,A)
    out = tuple((ONE[i]-A[i]+A2[i]-A3[i]) % P for i in range(16))
    assert mul(a,out) == mul(out,a) == ONE
    return out

def comm(a,b):
    return mul(mul(mul(a,b),inv(a)),inv(b))

group = [matrix(t) for t in product(range(3), repeat=6)]
h2 = [matrix((0,a,b,0,c,0)) for a,b,c in product(range(3), repeat=3)]
h3 = [matrix((0,0,a,0,0,0)) for a in range(3)]
assert len(set(group)) == 729 and len(set(h2)) == 27 and len(set(h3)) == 3
assert all(power(a,9) == ONE and power(a,3) in h3 for a in group)
assert all(power(a,3) == ONE for a in h2)
assert all(comm(a,b) in h3 for a in group for b in h2)
assert all(comm(a,b) == ONE for a in group for b in h3)

a = matrix((1,0,0,0,0,0))
b = matrix((0,0,0,1,0,0))
c = matrix((0,0,0,0,0,1))
witness = comm(comm(a,b),c)
assert witness == matrix((0,0,1,0,0,0)) and witness != ONE

generated = {ONE}
queue = [ONE]
for element in queue:
    for generator in (a,b,c):
        value = mul(element,generator)
        if value not in generated:
            generated.add(value)
            queue.append(value)
assert generated == set(group)

out = {
    'target': 'U4(F3)',
    'target_order': len(group),
    'generator_images': [a,b,c],
    'generation_order': len(generated),
    'all_ninth_powers_are_identity': True,
    'all_cubes_are_central': True,
    'second_layer_order': len(h2),
    'second_layer_exponent_divides_three': True,
    'third_layer_order': len(h3),
    'all_second_layer_commutators_are_in_third_layer': True,
    'third_layer_is_central': True,
    'nontrivial_triple_commutator': witness,
    'source_kernel_killed': 'gamma4(N) * gamma2(N)^3 * N^9',
    'scope': 'Exact finite witness for E.20; the compatible lifting maps are proved in the paper.',
    'status': 'PASS'
}
encoded = json.dumps(out, indent=2) + '\n'
print(encoded, end='')
Path(__file__).with_suffix('.json').write_text(encoded)
