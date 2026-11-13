#!/usr/bin/env python3
"""Exact norm, local residue and class-three group certificate at seventeen.

Arithmetic fields and their comparison maps are proved in A.37. This
program verifies their polynomial identities and the entire finite group,
including every allowed image of the normalized three source generators.
"""
from itertools import product
from pathlib import Path
import json

def eadd(a, b):
    return a[0]+b[0], a[1]+b[1]

def escale(n, a):
    return n*a[0], n*a[1]

def emul(a, b):
    u, v = a
    w, z = b
    return u*w-v*z, u*z+v*w-v*z

def ecube(a):
    return emul(emul(a, a), a)

a, b, c = (-7, -1), (-3, 0), (-1, 0)
norm_numerator = eadd(eadd(ecube(a), escale(17, ecube(b))),
                     eadd(escale(289, ecube(c)),
                          escale(-51, emul(emul(a, b), c))))
assert norm_numerator == (0, 27)

def kmul(a, b):
    return tuple(x % 17 for x in emul(a, b))

def kpow(a, n):
    value = (1, 0)
    while n:
        if n & 1:
            value = kmul(value, a)
        a = kmul(a, a)
        n //= 2
    return value

zeta = (0, 1)
d0 = tuple(x * pow(3, -1, 17) % 17 for x in a)
assert d0 == (9, 11)
assert kpow(d0, 3) == zeta
assert kpow(d0, 96) == kpow(zeta, 2)
assert kpow(d0, 9) == (1, 0)
assert all((u*u+u+1) % 17 for u in range(17))

# F_(17^6) = F_289[r]/(r^3-d0), an actual degree-three extension.
# Irreducibility follows from d0^((289-1)/3) != 1 and is checked above.
zero, one = (0, 0), (1, 0)
def radd(a, b):
    return tuple(tuple((u+v) % 17 for u, v in zip(x, y))
                 for x, y in zip(a, b))

def rmul(a, b):
    out = [zero for _ in range(5)]
    for i in range(3):
        for j in range(3):
            out[i+j] = tuple((u+v) % 17 for u, v in
                              zip(out[i+j], kmul(a[i], b[j])))
    for k in (4, 3):
        out[k-3] = tuple((u+v) % 17 for u, v in
                         zip(out[k-3], kmul(out[k], d0)))
    return tuple(out[:3])

def rpow(a, n):
    value = (one, zero, zero)
    while n:
        if n & 1:
            value = rmul(value, a)
        a = rmul(a, a)
        n //= 2
    return value

r = (zero, one, zero)
assert rpow(r, 3) == (d0, zero, zero)
assert rpow(r, 289) == (zero, kpow(zeta, 2), zero)
assert rpow(r, 27) == (one, zero, zero)
for i in range(3):
    ri = (zero, kpow(zeta, i), zero)
    assert rpow(ri, 289) == rmul((kpow(zeta, 2), zero, zero), ri)

# Coordinates are tau_a s^k, with s tau_a s^-1 = tau_(S a),
# (S a)_i = a_(i-1). Thus s(r_i)=r_(i+1) and tau_a(r_i)=zeta^a_i r_i.
vectors = list(product(range(3), repeat=3))
identity = ((0, 0, 0), 0)
def shift(a, k):
    return tuple(a[(i-k) % 3] for i in range(3))

def mul(x, y):
    a, k = x
    b, ell = y
    sb = shift(b, k)
    return tuple((u+v) % 3 for u, v in zip(a, sb)), (k+ell) % 3

def inv(x):
    a, k = x
    return tuple(-v % 3 for v in shift(a, -k)), -k % 3

def power(x, n):
    value = identity
    for _ in range(n):
        value = mul(value, x)
    return value

def comm(x, y):
    return mul(mul(mul(x, y), inv(x)), inv(y))

def generated(gens):
    found, queue = {identity}, [identity]
    for x in queue:
        for y in gens:
            z = mul(x, y)
            if z not in found:
                found.add(z)
                queue.append(z)
    return found

group = {(a, k) for a in vectors for k in range(3)}
t = ((0, 0, 0), 1)
m = ((1, 0, 0), 0)
assert len(group) == 81 and generated((t, m)) == group
gamma2 = generated({comm(x, y) for x in group for y in group})
gamma3 = generated({comm(x, y) for x in group for y in gamma2})
gamma4 = generated({comm(x, y) for x in group for y in gamma3})
assert (len(gamma2), len(gamma3), len(gamma4)) == (9, 3, 1)
assert all(power(x, 9) == identity for x in group)
assert all(power(x, 3) == identity for x in gamma2)
assert all(power(x, 3) in gamma3 for x in group)
rho = ((1, 1, 1), 0)
frobenius = ((2, 2, 2), 0)
assert comm(t, comm(t, m)) == rho
assert power(rho, 2) == frobenius

sum_zero = [a for a in vectors if sum(a) % 3 == 0]
sum_one = [a for a in vectors if sum(a) % 3 == 1]
source_checks = 0
for ta in sum_zero:
    for ma in sum_one:
        for na in sum_zero:
            ti, mi, ni = (ta, 1), (ma, 0), (na, 0)
            assert power(ti, 3) == power(mi, 3) == power(ni, 3) == identity
            assert comm(ti, comm(ti, mi)) == rho
            assert comm(ti, comm(ti, ni)) == identity
            assert comm(mi, ni) == identity
            assert all(comm(ai, comm(bi, ti)) == identity
                       for ai in (mi, ni) for bi in (mi, ni))
            source_checks += 1

# The weighted radical of the order-27 subquotient:
# R=delta_0^2 delta_1 has residue d0^3=zeta. It has a cube root d0
# in F_289, whereas the individual delta_i radicals require F_(17^6).
assert kpow(d0, 3) == zeta
record = {
    'delta_numerator_coefficients_in_1_zeta': [a, b, c],
    'delta_denominator': 3,
    'exact_norm_numerator': norm_numerator,
    'residue_field_relation': 'zeta^2+zeta+1=0 over F17',
    'delta_residue': d0,
    'delta_residue_cubed': kpow(d0, 3),
    'delta_residue_cubic_character': kpow(d0, 96),
    'radical_frobenius_289_multiplier': kpow(zeta, 2),
    'radical_residue_field_degree_over_F289': 3,
    'weighted_radical_R_residue': zeta,
    'weighted_radical_R_cube_root_in_F289': d0,
    'group_order': len(group),
    'lower_central_orders': [len(group), len(gamma2), len(gamma3), len(gamma4)],
    'exponent': 9,
    'zassenhaus_D4_trivial': True,
    'all_normalized_source_image_triples_checked': source_checks,
    'commutator_convention': 'aba^-1b^-1',
    'source_characters': 'kappa_zeta(m)=1; kappa_17(t)=1; all other entries zero',
    'Frobenius_vector': frobenius[0],
    'coefficient_of_ttm': 2,
    'scope': 'A.37 proves the exact arithmetic source map and independence of the three Kummer classes; this certificate verifies its finite identities and quotient.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
print('PASS: exact norm, degree-three residue extension, all81 group elements, and729 source triples.')
