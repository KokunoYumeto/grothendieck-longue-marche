"""Exact finite certificates for the reconstruction of SQ A.134/A.139.

Only the initial local certificate and finite identities are executed here.
The infinite refinement and all large primes are proved in the accompanying text.
"""
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path
from collections import Counter
import json

Q = 155564491
r = 1119169
a = [F(529, 382), F(147, 382), F((13*Q)**2, 191)]
cusp = [F(0), F(1), F(1, 2)]
c = F(-338, 191)
d = 7*17*Q
rho = F(34, 7*Q)
S = [2, 3, 7, 13, 17, 23, 139, 191, r]
disc = [[-1146, -382], [382, 191*23*13*Q], [191, -3]]

def primes(n):
    return [p for p in range(2, n+1)
            if all(p % t for t in range(2, isqrt(p)+1))]

def residue(x, p):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, p) % p

def vu(x, p, modulus=None):
    x = F(x)
    assert x
    n, den, v = x.numerator, x.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    modulus = p if modulus is None else modulus
    return v, n * pow(den, -1, modulus) % modulus

def leg(x, p):
    z = pow(x % p, (p-1)//2, p)
    return -1 if z == p-1 else z

def hilbert_root(vx, ux, D, p):
    vb, ub = vu(F(D), p, 8 if p == 2 else p)
    if p == 2:
        e = ((ux-1)//2)*((ub-1)//2)
        e += vx*((ub*ub-1)//8) + vb*((ux*ux-1)//8)
        return (-1)**(e % 2)
    return ((-1)**((vx*vb*((p-1)//2)) % 2)
            * leg(ux, p)**(vb % 2) * leg(ub, p)**(vx % 2))

assert Q == 139*r
assert all(r % j for j in range(2, isqrt(r)+1))
prod_a = a[0]*a[1]*a[2]
assert prod_a == F(318039202706815117780707, 27871484)
assert c*(c-1)*(c-F(1, 2))/prod_a == -rho*rho
assert F(d)/(2*rho) == F(1088951437, 2)**2
assert d == 18512174429

# Good primes through 5000: ordinary residue points except the indicated
# smooth branch above h at 457. At that prime take T=h+a_h*457^4.
centres = []
for p in primes(5000):
    if p in S:
        continue
    aa = [residue(x, p) for x in a]
    cc = [residue(x, p) for x in cusp]
    inv = [pow(x, -1, p) for x in aa]
    powers = {pow(x, 4, p) for x in range(1, p)}
    found = None
    for t in range(p):
        vals = [(t-cc[i])*inv[i] % p for i in range(3)]
        if all(x in powers for x in vals):
            found = {'p': p, 'kind': 'interior', 'T_mod_p': t,
                     'fourth_power_residues': vals}
            break
    if found is None:
        for i in range(3):
            vals = [(cc[i]-cc[j])*inv[j] % p for j in range(3)
                    if j != i]
            if all(x in powers for x in vals):
                found = {'p': p, 'kind': 'boundary', 'index': i,
                         'other_fourth_power_residues': vals}
                break
    assert found is not None, p
    centres.append(found)
assert [z for z in centres if z['kind'] != 'interior'] == [
    {'p': 457, 'kind': 'boundary', 'index': 2,
     'other_fourth_power_residues': [residue(F(1, 2)/a[0], 457),
                                    residue(-F(1, 2)/a[1], 457)]}]
assert all(leg(D, 457) == 1 for D in disc[2])

# Special centres. The displayed rational T values themselves work by
# Hensel: valuation divisible by four and nonzero fourth-power unit.
bad_centres = {}
root_data = {}
for p in S:
    T = a[0]
    if p == 2:
        T = F(31, 2)
    elif p == 17:
        T = 1+a[1]*17**4
    elif p in [139, r]:
        T = F(1, 2)+a[2]
    rows = []
    for i in range(3):
        z = (T-cusp[i])/a[i]
        v, u = vu(z, p, 256 if p == 2 else p)
        assert v % 4 == 0
        if p == 2:
            wanted = [5, 3, 5][i]
            roots = [x for x in range(1, 256, 2)
                     if x % 8 == wanted and pow(x, 4, 256) == u]
            assert roots
            x = roots[0]
        else:
            assert pow(u, (p-1)//gcd(4, p-1), p) == 1
            wanted = None
            if (i, p) in [(0, 3), (0, 191), (1, 13), (1, 23),
                          (1, 191), (1, r), (2, 3), (2, 191)]:
                wanted = 1
            if (i, p) == (1, 139):
                wanted = -1
            roots = [x for x in range(1, p)
                     if pow(x, 4, p) == u
                     and (wanted is None or leg(x, p) == wanted)]
            assert roots, (i, p, u, wanted)
            x = roots[0]
        rows.append({'index': i, 'v_ratio': v, 'unit_ratio': u,
                     'root_unit_residue': x, 'root_valuation': v//4,
                     'root_symbols': [hilbert_root(v//4, x, D, p)
                                      for D in disc[i]]})
    bad_centres[str(p)] = str(T)
    root_data[str(p)] = rows

products = [[1, 1] for i in range(3)]
nontrivial = []
for ps, rows in root_data.items():
    for row in rows:
        i = row['index']
        for j, sign in enumerate(row['root_symbols']):
            products[i][j] *= sign
            if sign == -1:
                nontrivial.append({'place': ps, 'index': i,
                                   'D': disc[i][j]})
# Negative X_0 at infinity, positive X_1 and X_h.
for j, D in enumerate(disc[0]):
    assert D < 0
    products[0][j] *= -1
    nontrivial.append({'place': 'infinity', 'index': 0, 'D': D})
assert products == [[1, 1], [1, 1], [1, 1]], products

# Uniform local Brauer checks at exceptional odd primes.
assert leg(1146, 139) == leg(1146, r) == 1
assert leg(d, 23) == leg(d, 191) == 1
assert residue(F(1)-c, 7) == 2 and leg(2, 7) == 1
fourths17 = {pow(x, 4, 17) for x in range(17)}
allowed17 = [t for t in range(17) if all(
    residue((F(t)-cusp[i])/a[i], 17) in fourths17
    for i in range(3))]
assert allowed17 == [1]
assert leg(residue(a[0], 17), 17) == 1
assert residue(c, 17) == 9
assert leg(9, 17) == leg(8, 17) == 1
assert d % 8 == 5

result = {
    'statements': ['E.160', 'E.161', 'E.163', 'E.164'],
    'status': 'PASS',
    'constants': {'Q': Q, 'r': r, 'a': [str(x) for x in a],
                  'c': str(c), 'd': d, 'rho': str(rho)},
    'finite_good_prime_bound': 5000,
    'finite_good_prime_count': len(centres),
    'types': dict(Counter(x['kind'] for x in centres)),
    'good_centres': centres,
    'special_centres': bad_centres,
    'special_root_certificate': root_data,
    'six_symbol_products_including_infinity': products,
    'nontrivial_root_symbols': nontrivial,
    'initial_valuation_normalizers': ['1', '17', '457'],
    'allowed_integral_T_mod_17': allowed17,
    'scope': ('Finite initial certificate and exact identities only. '
              'The root-stabilizer intersection, mixed-exponent induction, '
              'large-prime Weil bound, and section obstruction are proofs in the text.')
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: v for k, v in result.items()
                  if k not in ['good_centres', 'special_root_certificate']}, indent=2))
