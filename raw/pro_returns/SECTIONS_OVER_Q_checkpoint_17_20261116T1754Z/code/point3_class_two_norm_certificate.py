#!/usr/bin/env python3
"""Exact module, quadratic arithmetic and finite-sheet checks for A209.

The source proves the global Selmer bound from all good places, the real
embedding and the complete local group at3. This program checks its exact
arithmetic and every element of the specified finite geometric quotient.
"""
from itertools import product
from math import isqrt
from pathlib import Path
import json

base = Path(__file__).resolve().parent

# Exact arithmetic in Z[r], r^2=6.
def add(x, y):
    return (x[0]+y[0], x[1]+y[1])
def mul(x, y):
    return (x[0]*y[0]+6*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(n, x):
    return (n*x[0], n*x[1])
def norm(x):
    return x[0]**2-6*x[1]**2

one = (1, 0)
epsilon = (5, 2)
pi2, pi3 = (2, 1), (3, 1)
nd, nt = (9, -3), (0, -3)
assert norm(epsilon) == 1
assert norm(pi2) == -2 and norm(pi3) == 3
assert mul(pi2, pi2) == scale(2, epsilon)
assert mul(pi3, pi3) == scale(3, epsilon)
assert mul(nd, pi3) == (9, 0)
assert mul(nd, scale(-1, pi2)) == nt
assert 2**2 < 6 < 3**2
assert 24 < (2*3)**2  # Minkowski bound sqrt(24)/2 < 3.
assert all((x*x+1) % 3 for x in range(3))  # no norm-minus-one unit.
assert not any(x*x == 7 for x in range(4))
assert (5-2*2) > 0 and norm(epsilon) > 0

# Sixteen global S-unit squareclasses in the ordered basis
# (-1, epsilon, pi2, pi3). At the negative real embedding the signs
# are (-,+,-,+). At3, pi3 is the uniformizer and the other three
# residue classes are all the nonsquare2 in F3.
survivors = []
tests = []
for a, b, c, d in product(range(2), repeat=4):
    negative_sign = (a+c) % 2
    local3_unramified_bit = (a+b+c) % 2
    passed = negative_sign == 0 and local3_unramified_bit == 0
    assert passed == (a == c and b == 0)
    row = {'exponents': [a,b,c,d], 'negative_sign': negative_sign,
           'local3_unramified_bit': local3_unramified_bit, 'passed': passed}
    tests.append(row)
    if passed:
        survivors.append([a,b,c,d])
assert len(survivors) == 4
assert sorted(survivors) == sorted([[u,0,u,v] for u,v in product(range(2),repeat=2)])

# The literal norm projection is the pair-sum map in the cyclic branch
# basis e0,e1,e2,e3. Rotation is the geometric deck transformation.
def project(bits):
    return (bits[0]^bits[2], bits[1]^bits[3])
def rotate(bits, k=1):
    k %= 4
    return tuple(bits[(i-k) % 4] for i in range(4))
def reflect(bits):
    return tuple(bits[-i % 4] for i in range(4))
kernel = [b for b in product(range(2),repeat=4) if project(b)==(0,0)]
assert len(kernel) == 4
assert set(kernel) == {(a,b,a,b) for a,b in product(range(2),repeat=2)}
equivariance_checks = 0
for bits in product(range(2), repeat=4):
    for j, reflection in product(range(4), range(2)):
        acted = rotate(reflect(bits) if reflection else bits, j)
        target = project(bits)
        if j % 2:
            target = target[::-1]
        assert project(acted) == target
        equivariance_checks += 1

# Qbar=(F2^2) semidirect C8, with the deck generator swapping the bits.
def swap(a):
    return ((a & 1) << 1) | ((a >> 1) & 1)
def action(a, j):
    return swap(a) if j % 2 else a
def multiply(x, y):
    return (x[0] ^ action(y[0], x[1]), (x[1]+y[1]) % 8)
def inverse(x):
    return (action(x[0], -x[1]), -x[1] % 8)
identity = (0,0)
group = list(product(range(4), range(8)))
assert len(group) == 32
for x, y, z in product(group, repeat=3):
    assert multiply(multiply(x,y),z) == multiply(x,multiply(y,z))
for x in group:
    assert multiply(x,inverse(x)) == identity
def commutator(x, y):
    return multiply(multiply(multiply(x,y),inverse(x)),inverse(y))
commutators = {commutator(x,y) for x,y in product(group,repeat=2)}
assert commutators == {(0,0),(3,0)}
assert all(commutator(c,x)==identity for c,x in product(commutators,group))
meridians = [(0,1),(1,3)]
generated = {identity}
while True:
    nxt = generated | {multiply(x,y) for x in generated for y in meridians}
    if nxt == generated:
        break
    generated = nxt
assert set(group) == generated

# Independent finite residue calculation for every actual local sheet.
p = 1129
assert all(p % q for q in range(2,isqrt(p)+1))
theta = [16,430,1113,699]
assert all(pow(t,4,p)==54 for t in theta)
assert [168*t % p for t in theta] == theta[1:]+theta[:1]
r = [theta[0]**2*pow(3,-1,p) % p, theta[1]**2*pow(3,-1,p) % p]
assert r == [838,291] and all(x*x % p == 6 for x in r)
def bit(a):
    a %= p
    assert a
    value = pow(a,(p-1)//2,p)
    assert value in (1,p-1)
    return int(value == p-1)
def square_roots(a):
    return [x for x in range(p) if x*x % p == a % p]
global_rows = []
for name, values in [
    ('minus_pi2', [-(2+x) % p for x in r]),
    ('pi3', [(3+x) % p for x in r]),
    ('N_D', [(9-3*x) % p for x in r]),
    ('N_T', [(-3*x) % p for x in r])
]:
    assert [bit(x) for x in values] == [0,0]
    global_rows.append({'name':name,'values':values,
                        'square_roots':[square_roots(x) for x in values]})
t = 828
radicand = -t*pow(1-t,3,p)*pow(24,-1,p) % p
zs = [z for z in range(1,p) if pow(z,8,p)==radicand]
assert len(zs) == 8
sheets = []
for z in zs:
    x = -6*z*z*pow(1-t,-1,p) % p
    y = -18*z*pow(1-t,-1,p) % p
    assert (y*y-x**5+54*x) % p == 0
    v = tuple(bit(x-a) for a in theta)
    nv = tuple(bit(x*x-3*a) for a in r)
    assert nv == project(v) == (1,1)
    assert 8*pow(z,7,p) % p
    sheets.append({'z':z,'x':x,'y':y,'cyclic_Kummer':v,
                   'norm_values':[(x*x-3*a) % p for a in r],
                   'projected_Kummer':nv})

data = {
    'field':'L=Q(r), r^2=6; K=L(theta), theta^2=3r',
    'S_unit_basis':['-1','5+2r','2+r','3+r'],
    'squareclass_conditions':tests,
    'exact_survivors':survivors,
    'global_projected_Selmer_basis':['-(2+r)','3+r'],
    'dihedral_equivariance_checks':equivariance_checks,
    'geometric_group_order':len(group),
    'geometric_group_nilpotency_class':2,
    'associativity_checks':len(group)**3,
    'commutator_subgroup':sorted(commutators),
    'residue_prime':p,
    'quadratic_field_embeddings':r,
    'global_square_witnesses':global_rows,
    'all_eight_sheets':sheets,
    'scope':'Finite identities and complete displayed candidate elimination; the source proves the all-place Selmer bound and actual arithmetic quotient maps.'
}
out = '\n'.join([
    'A209 quadratic-norm/class-two certificate: PASS',
    'Exact quadratic unit, prime and Kummer norm identities: PASS',
    'All16 global squareclasses: exactly4 survive the real and3-adic tests',
    'Surviving basis: -(2+sqrt6), 3+sqrt6; both are actual projected D,T classes',
    f'Dihedral module equivariance checks: {equivariance_checks}',
    'Actual quotient: order32, class2; all32768 associativity checks pass',
    'At1129 the two global generators are squares in both quadratic factors',
    'All8 local cover sheets have projected Kummer vector(1,1)',
    data['scope']
]) + '\n'
stem = Path(__file__).with_suffix('')
stem.with_name(stem.name+'_data.json').write_text(json.dumps(data,indent=2)+'\n')
stem.with_name(stem.name+'_output.txt').write_text(out)
print(out,end='')
