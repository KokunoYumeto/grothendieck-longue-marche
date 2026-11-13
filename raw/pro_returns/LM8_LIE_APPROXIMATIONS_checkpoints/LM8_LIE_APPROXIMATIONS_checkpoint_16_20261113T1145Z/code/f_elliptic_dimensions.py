#!/usr/bin/env python3
"""Exact finite computations for F.6--F.9.  No Selmer vanishing is inferred.

The free-Lie check exhausts all binary words of lengths 1,...,8 and selects
Lyndon words.  The metabelian check uses its explicit commutator basis.
The descent check evaluates the Monsky matrices for n=1,6 over F_2.
Everything here is integer or rational arithmetic; no Sage/PARI is needed.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd, comb
from pathlib import Path
import csv
import json

OUT = Path(__file__).resolve().parent


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    k = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            k += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        k += 1
    return (-1) ** k


def lyndon_words(n):
    return [w for w in product((0, 1), repeat=n)
            if all(w < w[i:] + w[:i] for i in range(1, n))]


def rank_mod_2(a):
    a = [r[:] for r in a]
    rank = 0
    for j in range(len(a[0]) if a else 0):
        k = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[k], a[rank] = a[rank], a[k]
        for i in range(len(a)):
            if i != rank and a[i][j]:
                a[i] = [x ^ y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def count_points(n, p):
    return 1 + sum((y * y - x * x * x + n * n * x) % p == 0
                   for x in range(p) for y in range(p))


def add(P, R, n):
    if P is None:
        return R
    if R is None:
        return P
    x, y = P
    u, v = R
    if x == u and y == -v:
        return None
    slope = (3 * x * x - n * n) / (2 * y) if P == R else (v - y) / (u - x)
    z = slope * slope - x - u
    return z, slope * (x - z) - y


def str_point(P):
    return None if P is None else [str(c) for c in P]


free = []
meta = []
cm = []
for n in range(1, 9):
    words = lyndon_words(n)
    witt = sum(mobius(d) * 2 ** (n // d) for d in divisors(n)) // n
    assert len(words) == witt
    trace = sum((-1) ** sum(w) for w in words)
    trace_formula = sum(mobius(d) * (0 if d % 2 else 2) ** (n // d)
                        for d in divisors(n)) // n
    assert trace == trace_formula
    minus = sum(sum(w) % 2 for w in words)
    assert minus == (witt - trace) // 2
    free.append(dict(class_n=n, graded_dim=witt, conjugation_trace=trace,
                     minus_dim=minus, local_graded_dim=1 if n == 1 else witt))
    if n == 1:
        mw, mt, mm = 2, 0, 1
    else:
        mw = n - 1
        mt = sum((-1) ** b for b in range(1, n))
        mm = sum(b % 2 for b in range(1, n))
    meta.append(dict(class_n=n, graded_dim=mw, conjugation_trace=mt,
                     minus_dim=mm, local_graded_dim=1 if n == 1 else mw))
    if n >= 2:
        for a in range(1, n):
            b = n - a
            actual = sum(sum(w) == b for w in words)
            formula = sum(mobius(d) * comb(n // d, a // d)
                          for d in divisors(gcd(a, b))) // n
            assert actual == formula
            cm.append(dict(class_n=n, a=a, b=b,
                           free_multiplicity=actual, metabelian_multiplicity=1))

tables = {}
for name, rows in [('free', free), ('metabelian', meta)]:
    local = 0
    baseline = 0
    for row in rows:
        n = row['class_n']
        local += row['local_graded_dim']
        if n >= 3:
            baseline += row['minus_dim']
        row['local_dimension'] = local
        row['global_baseline_above_class2'] = baseline
        row['exact_global_graded_expression'] = (
            'rank' if n == 1 else '0' if n == 2 else
            f"{row['minus_dim']} + delta_{n}")
    for rank in (0, 1):
        for s in (0, 1, 2):
            values = [rank if r['class_n'] == 1 else
                      rank + s + r['global_baseline_above_class2'] for r in rows]
            first = next((i + 1 for i, (g, r) in enumerate(zip(values, rows))
                          if g < r['local_dimension']), None)
            tables[f'{name}_r{rank}_s{s}'] = {
                'local': [r['local_dimension'] for r in rows],
                'global_if_delta_3_through_8_zero': values,
                'global_dimension': values,
                'first_strict_if_needed_defects_zero': first,
                'unconditional_first_strict': first,
                'higher_numeric_global_status': 'PROVED using the separate arithmetic vanishing theorem F.18, with the refined local conditions in F_elliptic.tex',
                'arithmetic_input': 'F.18: all full and metabelian dual Selmer defects in degrees3–8 vanish atp5 for E1 and E6; exact modular-symbol certificates are F_advanced_cm_power_1.json through _6.json. This word-count program does not itself prove the arithmetic vanishing.'}

assert [r['local_dimension'] for r in free] == [1, 2, 4, 7, 13, 22, 40, 70]
assert [r['local_dimension'] for r in meta] == [1, 2, 4, 7, 11, 16, 22, 29]

M1 = []
M6 = [[1, 1], [1, 1]]  # A=0, (2/3)=(-1/3)=-1 in the additive convention
assert rank_mod_2(M1) == 0
assert rank_mod_2(M6) == 1
P = Q(12), Q(36)
P2 = add(P, P, 6)
P4 = add(P2, P2, 6)
P8 = add(P4, P4, 6)
assert P2 == (Q(25, 4), Q(-35, 8))
assert P8 is not None
assert count_points(6, 5) == count_points(6, 7) == 8
assert count_points(1, 3) == 4
assert count_points(1, 5) == 8
rank_certificate = {
    'E1': {'equation': 'y^2=x^3-x', 'Monsky_matrix': M1,
           'pure_2_Selmer_dimension': 0, 'rank': 0,
           'good_reduction_counts': {'3': 4, '5': 8},
           'rational_points': ['O', '(-1,0)', '(0,0)', '(1,0)']},
    'E6': {'equation': 'y^2=x^3-36x', 'Monsky_matrix': M6,
           'pure_2_Selmer_dimension': 1, 'rank': 1,
           'point': str_point(P), '2P': str_point(P2),
           '4P': str_point(P4), '8P': str_point(P8),
           'good_reduction_counts': {'5': 8, '7': 8},
           'nontorsion_reason': 'torsion order divides gcd(8,8)=8; 8P is not O'},
    'p': 5, 'a_p_both': -2,
    'Sha_finiteness_input': 'Kolyvagin Theorem 1 plus rigorously tabulated analytic ranks; not inferred from 2-descent.'}

data = {
    'scope': 'All binary words of lengths1..8 are exhausted. Global Selmer dimensions use the separately proved arithmetic input F.18; they are not inferred from word counts or numerical sampling of cohomology.',
    'rank_certificate': rank_certificate,
    'free_graded': free, 'metabelian_graded': meta,
    'CM_character_multiplicities': cm, 'dimension_tables': tables,
    'checks_passed': True}
(OUT / 'f_elliptic_dimensions.json').write_text(json.dumps(data, indent=2) + '\n')
with (OUT / 'f_elliptic_dimensions.csv').open('w', newline='') as f:
    fields = ['quotient'] + list(free[0])
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for name, rows in [('free', free), ('metabelian', meta)]:
        writer.writerows(dict(quotient=name, **r) for r in rows)
print(json.dumps({'checks_passed': True, 'free_local': tables['free_r0_s0']['local'],
                  'metabelian_local': tables['metabelian_r0_s0']['local'],
                  'rank_certificates': rank_certificate,
                  'first_strict_by_rank_and_s': {k: v['first_strict_if_needed_defects_zero']
                                               for k, v in tables.items()}}, indent=2))
