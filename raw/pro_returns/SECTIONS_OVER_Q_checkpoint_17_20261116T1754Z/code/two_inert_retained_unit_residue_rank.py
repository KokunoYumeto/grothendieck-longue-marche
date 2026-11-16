#!/usr/bin/env python3
"""A bounded exact residue test of the previously retained relation kernel.

This computes the rank of specified finite residue rows.  It makes no assertion
that the retained products form the full K3 unit group, nor that the finite-row
rank bounds their rank over Z.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as sp

BASE = Path(__file__).resolve().parent
raw = json.loads((BASE / 'two_inert_retained_unit_character_search_data.json').read_text())
coefficients = [[Fraction(c) for c in row['coefficient']]
                for row in raw['literal_local_rows']]
kernel = [row['exponents'] for row in raw['integer_kernel_generators']]
assert len(coefficients) == 47 and len(kernel) == 25
constant = 3**8 * 649**3
pivots = {}
witnesses = []
rows = []
physical_primes = []
for prime in sp.primerange(5, 20000):
    p = int(prime)
    if p % 3 != 1 or constant % p == 0:
        continue
    if any(c.denominator % p == 0 for row in coefficients for c in row):
        continue
    roots = sp.nthroot_mod(constant % p, 27, p, all_roots=True)
    if not roots:
        continue
    physical_primes.append(p)
    generator = int(sp.primitive_root(p))
    omega = pow(generator, (p-1)//3, p)
    assert omega != 1 and pow(omega, 3, p) == 1
    logarithm = {pow(omega, i, p): i for i in range(3)}
    for root in roots:
        x = int(root)
        assert pow(x, 27, p) == constant % p
        values = []
        for row in coefficients:
            value = 0
            for c in reversed(row):
                value = (value*x + c.numerator*pow(c.denominator, -1, p)) % p
            if value == 0:
                break
            values.append(logarithm[pow(value, (p-1)//3, p)])
        if len(values) != len(coefficients):
            continue
        row = [sum(a*b for a, b in zip(exponents, values)) % 3
               for exponents in kernel]
        rows.append({'p': p, 'root': x, 'kernel_characters': row})
        reduced = row[:]
        for pivot, basis_row in sorted(pivots.items()):
            if reduced[pivot]:
                factor = reduced[pivot]
                reduced = [(a-factor*b) % 3 for a, b in zip(reduced, basis_row)]
        if any(reduced):
            pivot = next(i for i, value in enumerate(reduced) if value)
            inverse = pow(reduced[pivot], -1, 3)
            pivots[pivot] = [a*inverse % 3 for a in reduced]
            witnesses.append(rows[-1])
        if len(rows) == 240:
            break
    if len(rows) == 240:
        break
assert len(rows) == 240 and len(physical_primes) == 60
assert len(pivots) == 1
assert [(w['p'], w['root']) for w in witnesses] == [(103, 62)]
result = {'degree_one_places': rows, 'physical_primes': physical_primes,
          'independent_rows': witnesses, 'finite_row_rank': len(pivots),
          'scope': 'Rank of these finite residue rows only; no global unit completeness or Z-rank upper bound.'}
(BASE / 'two_inert_retained_unit_residue_rank_data.json').write_text(json.dumps(result, indent=2)+'\n')
message = ('PASS: 240 exact degree-one residue rows at60 physical primes; finite row rank1\n'
           'Independent witness: p103, root62\n'
           'SCOPE: only the specified residue rows and retained products; no unit-group completeness\n')
(BASE / 'two_inert_retained_unit_residue_rank_output.txt').write_text(message)
print(message, end='')
