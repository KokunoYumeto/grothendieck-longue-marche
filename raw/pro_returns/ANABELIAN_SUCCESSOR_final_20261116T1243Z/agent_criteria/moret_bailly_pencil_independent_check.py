"""Independent exact algebra/count checks for the proposed A6 refutation.

The geometric intersection/isogeny and Raynaud arguments are proved in the
accompanying review, not inferred from this finite symbolic calculation.
"""
import json
from pathlib import Path
import sympy as sp

u, t, z = sp.symbols('u t z')
d = t**3 + 1
a = u**2 + t**2*u + t
b = t*u**2 + u + t**2
c = u**3 + 1

def mod2(expr):
    return sp.Poly(sp.expand(expr), u, t, modulus=2).as_expr()

# x1=a/d, x2=b/d, y2=y1+c/d, y1^2+y1=x1^3.
checks = {
    'elliptic_second_equation': mod2(b**3+a**3+c**2*d+c*d**2) == 0,
    'inverse_u': mod2(b+t*a-u*d) == 0,
    # f=(y2+y1+1+x1*x2)/(x2+x1^2) is exactly t.
    'pencil_parameter': mod2(c*d+d**2+a*b+t*(b*d+a**2)) == 0,
}
assert all(checks.values())

# Conversely, on f=t put z=x1 and u=x2+t*x1. The difference of
# elliptic equations has one canceled denominator factor and exactly
# the desired movable-fibre factor.
R = 1+t*u+(u+t**2)*z
fibre_relation = z**3+(u+t*z)**3+R**2+R
factor_check = sp.Poly(sp.expand(fibre_relation+
    (d*z+a)*(z**2+t*z+u)), u,t,z, modulus=2).is_zero
assert factor_check
checks['movable_fibre_factorization'] = factor_check

cube = sp.Poly(mod2(a**3), u)
leading_odd_coefficient_numerator = sp.expand(cube.coeff_monomial(u**5))
assert leading_odd_coefficient_numerator == t**2

# For every prime p>=5, (p-1)^6>=p^5: substitute p=z+5.
totient_prime_polynomial = sp.Poly(sp.expand((z+4)**6-(z+5)**5), z)
assert all(x > 0 for x in totient_prime_polynomial.all_coeffs())

# M >= phi(n)/e >= 2*n^(5/6)/(3e), and M(M+1)<=2(n-1)
# imply n^(2/3)<9e^2/2, hence n<10e^3, since 100>729/8.
assert 800 > 729

e = 64
B = 10*e**3
parameters = 4**e+1
excluded_upper_bound = 5+B**5
assert excluded_upper_bound < parameters
first_e_for_this_crude_bound = next(j for j in range(1,e+1)
    if 5+(10*j**3)**5 < 4**j+1)

out = {
    'status': 'all exact symbolic and integer checks passed',
    'identities_over_F2': checks,
    'a_cubed_mod2': str(mod2(a**3)),
    'leading_odd_coefficient_after_AS_reduction': 't^2/(t^3+1)^3',
    'totient_prime_polynomial_at_p_equal_z_plus_5': str(totient_prime_polynomial.as_expr()),
    'constant_inequality': {'left': 800, 'right': 729},
    'e': e,
    'field_size': 4**e,
    'degree_cutoff_exclusive': B,
    'parameter_count': parameters,
    'excluded_parameter_upper_bound': excluded_upper_bound,
    'positive_lower_bound_on_good_parameters': parameters-excluded_upper_bound,
    'first_e_for_crude_bound_only': first_e_for_this_crude_bound,
    'scope': 'No individual parameter is enumerated or asserted here; the exact count proves a nonempty finite set once the independently audited geometric arguments are supplied.'
}
path = Path(__file__).with_name('moret_bailly_pencil_independent_output.json')
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
