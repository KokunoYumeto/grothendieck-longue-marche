#!/usr/bin/env python3
"""Read the printed A159 tables first and verify their literal relative norms."""
from pathlib import Path
from fractions import Fraction as Q
import json
import re
import sys

sys.set_int_max_str_digits(0)
w = Path(__file__).resolve().parents[1]
s = (w / 'sections/two_inert_unit_coefficients_supplement.tex').read_text()
d = 649
B = 10**40
groups = re.split(r'Unit \$u_([234])\$', s)
assert len(groups) == 7
coordinates = {}
row_count = 0
for pos in range(1, len(groups), 2):
    unit = int(groups[pos])
    blocks = {}
    signs = {}
    rows = re.findall(r'^([0-8]) & ([0-9]+) & ([+-]) & ([0-9]{40}) & ([0-9]{40})', groups[pos+1], re.M)
    assert rows
    for i0, k0, sign, low, high in rows:
        i, k = int(i0), int(k0)
        assert k % 2 == 0
        signs.setdefault(i, sign)
        assert signs[i] == sign
        for offset, val in enumerate([low, high]):
            assert (i, k+offset) not in blocks
            blocks[i, k+offset] = int(val)
        row_count += 1
    assert set(signs) == set(range(9))
    nums = [sum(val*B**k for (j,k),val in blocks.items() if j == i) * (-1 if signs[i] == '-' else 1) for i in range(9)]
    coordinates[unit] = [Q(nums[i], d**(2*i//3)) for i in range(9)]

def plus(a, b):
    return [x+y for x,y in zip(a,b)]

def times(a, b, radicand=3):
    n = len(a)
    out = [Q(0)]*(2*n-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    for j in range(2*n-2, n-1, -1):
        out[j-n] += radicand*out[j]
    return out[:n]

def power(a, n):
    assert n >= 0
    out = [Q(1), Q(0), Q(0)]
    while n:
        if n & 1:
            out = times(out, a)
        a = times(a,a)
        n //= 2
    return out

U = [Q(-2), Q(0), Q(1)]
Ui = [Q(4), Q(3), Q(2)]
assert times(U,Ui) == [1,0,0]
coordinates[1] = [Q(-2),Q(0),Q(0),Q(0),Q(0),Q(0),Q(1,d**4),Q(0),Q(0)]
rad = [Q(0), Q(d*d), Q(0)]
norm_exponents = [3,57,-3,1614]
raw = json.loads((w/'code/two_inert_relative_unit_repair_certificate_data.json').read_text())
for j in range(1,5):
    cs = coordinates[j]
    assert cs == [Q(v) for v in raw['units'][j-1]['candidate']]
    aa,bb,cc = [[cs[k+3*i]*d**(2*i) for i in range(3)] for k in range(3)]
    norm = plus(plus(power(aa,3),times(rad,power(bb,3))), plus(times(times(rad,rad),power(cc,3)), [-3*x for x in times(rad,times(times(aa,bb),cc))]))
    k = norm_exponents[j-1]
    assert norm == power(U if k >= 0 else Ui, abs(k))
    assert all((cs[i]*d**(2*i//3)).denominator == 1 for i in range(9))
    assert all(6*i-9*(2*i//3) >= 0 for i in range(9))
    print(f'Unit {j}: all nine printed coefficients reconstructed; integral-element coordinates; relative norm U^{k}: PASS')

print(f'PASS: {row_count} literal two-block rows, all 27 tabulated integer coefficients, and all four exact cubic norms.')
print('Every basis element is integral by its displayed monic ninth-power equation; N(U)=(-2)^3+9=1, so all four elements are units.')
