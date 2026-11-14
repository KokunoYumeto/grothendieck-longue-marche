#!/usr/bin/env python3
"""Exact class-two coordinate and finite half-parameter calculations.

The quotient maps are the actual free-source maps to UT3(Z/n).
All tested coordinate tuples are checked algebraically; no arbitrary
tuple is asserted to be the image of a nonstandard original h.
omega(h) is evaluated in the full source before the quotient; only
its proved central class-two coordinate is used in this program.
"""
from itertools import product
from math import gcd, lcm
from pathlib import Path
import json

checks = []

def check(name, condition):
    assert condition, name
    checks.append({'name': name, 'passed': True})

rows = []
for n in [2, 3, 5, 7, 8, 9]:
    identity = (0, 0, 0)
    def mul(g, h):
        a,b,t = g; aa,bb,tt = h
        return ((a+aa)%n, (b+bb)%n, (t+tt-aa*b)%n)
    def inv(g):
        a,b,t = g
        return (-a%n, -b%n, (-t-a*b)%n)
    def power(g, exponent):
        if exponent < 0:
            return power(inv(g), -exponent)
        out = identity
        while exponent:
            if exponent & 1:
                out = mul(out,g)
            g = mul(g,g); exponent >>= 1
        return out
    def alpha(g):
        a,b,t = g
        return (-a%n,-b%n,t)
    def order(g):
        value,k = g,1
        while value != identity:
            value = mul(value,g); k += 1
            assert k <= 2*n
        return k
    x,y,c = (1,0,0),(0,1,0),(0,0,1)
    z = inv(mul(x,y))
    elements = list(product(range(n),repeat=3))
    check('mod%d_actual_class_two_commutator_and_inverse' % n,
          mul(mul(mul(x,y),inv(x)),inv(y)) == c and
          all(mul(g,inv(g)) == mul(inv(g),g) == identity for g in elements))
    exponent = lcm(*(order(g) for g in elements))
    check('mod%d_exact_parity_kernel_exponent' % n,
          exponent == (n if n%2 else 2*n))
    def defect(u1,u2,k):
        out = power(x,k)
        for value in [inv(u1),power(z,k),u2,power(y,k+1)]:
            out = mul(out,value)
        return out

    formula_cases = 0
    for a,b,t1,t2 in product(range(n),repeat=4):
        u1,u2 = (a,b,t1),(a,(b-1)%n,t2)
        for k in range(exponent):
            expected = (0,0,(t2-t1+k*(a-b)-k*(k+1)//2)%n)
            assert defect(u1,u2,k) == expected
            formula_cases += 1
    check('mod%d_full_endpoint_coordinate_formula' % n, formula_cases == n**4*exponent)

    sign_cases = 0
    for a,t1,t2 in product(range(n),repeat=3):
        u1,u2 = (a,a,t1),(a,(a-1)%n,t2)
        for k in range(exponent):
            assert alpha(defect(u1,u2,k)) == defect(u1,u2,-k-1)
            sign_cases += 1
    check('mod%d_diagonal_coordinate_sign_identity' % n, sign_cases == n**3*exponent)

    units = [m for m in range(2*exponent) if gcd(m,2*exponent)==1]
    root_rows = []
    for d in range(n):
        u1,u2 = identity,(0,-1%n,d)
        exact,quadratic = [],[]
        for m in units:
            k = (m-1)//2
            is_zero = defect(u1,u2,k)==identity
            is_root = (m*m-1-8*d)%(8*n)==0
            assert is_zero == is_root
            assert ((m+2*exponent)**2-m*m)%(8*n)==0
            if is_zero:
                exact.append(m)
            if is_root:
                quadratic.append(m)
        root_rows.append({'d_mod_n':d,'T_unit_residues':exact,'quadratic_unit_residues':quadratic})
    check('mod%d_all_finite_half_parameter_root_comparisons' % n,
          all(r['T_unit_residues']==r['quadratic_unit_residues'] for r in root_rows))

    gt_rows = []
    for t in range(n):
        h = power(c,t)
        # Full-source omega fixes the central class-two coordinate of h.
        u1 = h
        u2 = mul(mul(inv(h),inv(y)),inv(h))
        for k in range(exponent):
            assert defect(u1,u2,k)==(0,0,(-3*t-k*(k+1)//2)%n)
        d = (-3*t)%n
        gt_rows.append({'h_commutator_coefficient_mod_n':t,'d_mod_n':d,
                        'T_unit_residues':root_rows[d]['T_unit_residues']})
    check('mod%d_GT0_actual_coefficient_formula' % n,
          all(row['d_mod_n']==(-3*row['h_commutator_coefficient_mod_n'])%n for row in gt_rows))
    rows.append({'modulus':n,'group_order':n**3,'parity_kernel_exponent':exponent,
                 'unit_parameter_modulus':2*exponent,'square_test_modulus':8*n,
                 'coordinate_formula_cases':formula_cases,'sign_identity_cases':sign_cases,
                 'all_units':units,'class_two_root_rows':root_rows,'GT0_coefficient_rows':gt_rows,
                 'GT0_coefficients_with_nonempty_finite_zero_set':[
                     row['h_commutator_coefficient_mod_n'] for row in gt_rows if row['T_unit_residues']]})

check('GT0_finite_nonempty_root_coefficients_mod5_and_mod7',
      next(r for r in rows if r['modulus']==5)['GT0_coefficients_with_nonempty_finite_zero_set']==[0,3]
      and next(r for r in rows if r['modulus']==7)['GT0_coefficients_with_nonempty_finite_zero_set']==[0,2,6])
check('GT0_all_coefficients_have_finite_roots_at_tested_two_and_three_powers',all(
      len(row['GT0_coefficients_with_nonempty_finite_zero_set'])==row['modulus']
      for row in rows if row['modulus'] in [2,3,8,9]))

out={'status':'PASS','scope':'Actual class-two quotient identities; no nonstandard h-coordinate realization asserted',
     'rows':rows,'checks':checks,'assertion_count':len(checks),
     'total_coordinate_formula_cases':sum(row['coordinate_formula_cases'] for row in rows),
     'total_sign_identity_cases':sum(row['sign_identity_cases'] for row in rows)}
target=Path(__file__).with_name('actual_transporter_class_two_output.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
