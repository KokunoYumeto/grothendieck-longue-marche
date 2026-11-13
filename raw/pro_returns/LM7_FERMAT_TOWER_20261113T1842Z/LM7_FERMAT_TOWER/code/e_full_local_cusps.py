#!/usr/bin/env python3
"""Exact full-source cusp comparisons and the actual R-section obstruction.

The finite-field weight argument is proved in E.61. This program checks
its explicit R-section, its actual word preimage, every finite cusp-line
comparison, the specified detecting cover, and the local packet quotients.
"""
from pathlib import Path
from fractions import Fraction as Q
from contextlib import redirect_stdout
from io import StringIO
import argparse
import importlib.util
import json

parser = argparse.ArgumentParser()
parser.add_argument('--source-code', type=Path, default=Path(__file__).parent)
args = parser.parse_args()
spec = importlib.util.spec_from_file_location(
    'elliptic_ring', args.source_code / 'a_elliptic_rank13.py')
r = importlib.util.module_from_spec(spec)
with redirect_stdout(StringIO()):
    spec.loader.exec_module(r)

H = r.add(r.basis(0), r.basis(1), r.V)
nu = (Q(0), Q(0), H)
z = r.power(r.gy, 6)
defect = r.gp(z, r.apply(nu, r.principal), r.gi(z), r.power(nu, -4))
assert defect == r.identity
word = r.gp(r.gc, r.gp(r.gy, r.gc, r.gi(r.gy)),
            r.gcom(r.power(r.gy, 3), r.gc))
assert word == nu
assert (r.aug(H), sum(Q(k//3)*H[k] for k in range(9)),
        sum(Q(k%3)*H[k] for k in range(9)), H[9], H[10]) == (2, 0, 1, 0, 1)

# A representative of the cusp space F3^9 / F3(1,...,1).
def cusp_quotient(v):
    return tuple((v[i]-v[8]) % 3 for i in range(8))

w9 = (1, 1, 0, 0, 0, 0, 0, 0, 0)
w = cusp_quotient(w9)
line_checks = []
cusps = []
for k in range(9):
    e = tuple(int(j == k) for j in range(9))
    cusps.append(cusp_quotient(e))
    for a in range(3):
        diff = tuple((w9[j]-a*e[j]) % 3 for j in range(9))
        assert len(set(diff)) > 1
        assert cusp_quotient(diff) != (0,)*8
        line_checks.append({'cusp': list(divmod(k,3)), 'scalar': a,
                            'difference': list(diff), 'diagonal': False})
assert len(line_checks) == 27
assert all(v != (0,)*8 for v in cusps)
assert len(set(cusps)) == 9

# Every cusp's image in V/<w> has exact order3. No large permutation
# representation is substituted for this exact elementary quotient.
wline = {tuple(a*x % 3 for x in w) for a in range(3)}
assert all(v not in wline for v in cusps)
frattini_rank = 10
cover_degree = 3**(frattini_rank-1)
ramification = [3]*9
cusp_count = sum(cover_degree//e for e in ramification)
punctured_euler = -9*cover_degree
genus = (2-cusp_count-punctured_euler)//2
assert 2-2*genus-cusp_count == punctured_euler
assert (cover_degree, cusp_count, genus) == (19683, 59049, 59050)

# The numerical inertia formula for each cusp in the normalized R
# coordinates: the Frobenius module origin can be arbitrary here because
# it does not enter the displayed tame relation. No assertion about an
# actual nonbase cusp origin is extracted from these examples.
cusp_inertia_checks = 0
for i in range(3):
    for j in range(3):
        e = r.basis(3*i+j)
        for a in [-9, -3, -1, 1, 3, 9]:
            ni = (Q(0), Q(0), r.scale(e,a))
            zi = (Q(3*i), Q(3*j), r.zero)
            assert r.gp(zi, r.apply(ni,r.principal), r.gi(zi),
                        r.power(ni,-4)) == r.identity
            cusp_inertia_checks += 1

def isprime(n):
    return n >= 2 and all(n%d for d in range(2, int(n**.5)+1))

def valuation3(n):
    h = 0
    while n%3 == 0:
        n //= 3
        h += 1
    return h

packet_checks = []
for p in range(2,100):
    if not isprime(p) or p == 3:
        continue
    q = p if p%3 == 1 else p*p
    h = valuation3(q-1)
    for m in range(1,6):
        modulus = 3**m
        shifts = {(1-q)*k % modulus for k in range(modulus)}
        expected = {3**min(h,m)*k % modulus for k in range(modulus)}
        assert shifts == expected
        assert modulus//len(shifts) == 3**min(h,m)
        packet_checks.append({'p': p, 'q': q, 'modulus': modulus,
                              'cokernel_size': modulus//len(shifts)})

result = {
    'statement': 'E.61',
    'actual_R_section': {'inertia_module': list(map(str,H)),
                         'Frobenius_handles': [0,2],
                         'exact_relation_defect': 'identity',
                         'word_preimage': 'c (y c y^-1) [y^3,c]'},
    'cusp_line_checks': line_checks,
    'detecting_cover': {'Frattini_dimension': frattini_rank,
                        'degree': cover_degree,
                        'ramification_indices': ramification,
                        'cusp_count': cusp_count,
                        'compact_genus': genus,
                        'punctured_Euler_characteristic': punctured_euler},
    'cusp_inertia_relation_checks': cusp_inertia_checks,
    'finite_packet_quotients': packet_checks,
    'all_checks_passed': True,
    'scope': 'Finite and explicit group identities; the full-source classification uses the written finite-field cover and Weil proof.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('Actual eleven-module tame relation and literal word preimage: PASS')
print('All 27 cusp-line comparisons: PASS')
print('Cover degree19683, cusps59049, compact genus59050: PASS')
print(f'{cusp_inertia_checks} normalized cusp-inertia relation checks: PASS')
print(f'{len(packet_checks)} exact local packet quotients: PASS')
print('All E.61 finite certificates: PASS')
