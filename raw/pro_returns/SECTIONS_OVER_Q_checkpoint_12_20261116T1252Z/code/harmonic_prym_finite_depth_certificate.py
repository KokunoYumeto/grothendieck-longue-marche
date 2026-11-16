"""Exact finite arithmetic for A.158; no global Selmer computation is used."""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp

base = Path(__file__).resolve().parent
M = 325596479663
a = F(573*M*M, 4*191**4)
C = F(573*M*M, 191**2)
assert 382**2*a == C

def v2(q):
    q = F(q)
    if not q:
        return 10**9
    n, d = abs(q.numerator), q.denominator
    return (n & -n).bit_length() - (d & -d).bit_length()

assert v2(C) == 0 and v2(a) == -2
T2 = F(31, 2)
old_coefficients = [F(529, 382), F(147, 382), F(4089852535355054689, 191)]
assert old_coefficients[0]*old_coefficients[1]*old_coefficients[2] == a
old_punctures = [F(0), F(1), F(1, 2)]
ratios = [(T2-c)/a_i for c, a_i in zip(old_punctures, old_coefficients)]
assert all(v2(z) == 0 for z in ratios)
assert all((z.numerator*pow(z.denominator, -1, 32)) % 32 == 17 for z in ratios)
assert all(pow(z, 4, 32) == 17 for z in (5, 3, 5))
assert (5*3*5) % 8 == 3
assert v2(T2) == -1
assert 4*T2*(1-T2) == -899
assert 2*0 - 2*v2(T2) == 2
assert all(pow(z, 4, 16) == 1 for z in range(1, 16, 2))
x, y, b = sp.symbols('x y b')
translated = (-b*y/x**2)**2 - (b/x)**3 - b*(b/x)
assert sp.cancel(translated.subs(y**2, x**3+b*x)) == 0
assert sp.cancel(b/(b/x)-x) == 0
assert sp.cancel(-b*(-b*y/x**2)/(b/x)**2-y) == 0

threshold_checks = 0
for r in range(-256, 257):
    first = 1 + max(r, 2-r)//4
    for n in range(1, 130):
        middle = 3-4*n <= r <= 4*n-1
        assert middle == (not (r <= 2-4*n or r >= 4*n))
        assert middle == (n >= first)
        assert (2-r <= 2-4*n) == (r >= 4*n)
        threshold_checks += 1

iteration_checks = 0
for r in range(-128, 129):
    z = r-4 if r < 0 else (-4 if r == 0 else (-2 if r == 1 else -r-2))
    for n in range(1, 65):
        assert z <= 2-4*n
        if n < 64:
            assert z < 0
            z -= 4
        iteration_checks += 1

# Literal proper module: V^6=-(V^4+V^2+1).
def rmul(A, B):
    out = [0]*11
    for i in range(6):
        for j in range(6):
            out[i+j] += A[i]*B[j]
    for j in range(10, 5, -1):
        c = out[j]
        for k in (0, 2, 4):
            out[j-6+k] -= c
    return out[:6]

delta = [-1, 1, 0, 0, 0, 0]
power = [1, 0, 0, 0, 0, 0]
powers = [power]
for k in range(1, 4*32+3):
    power = rmul(power, delta)
    powers.append(power)
classes = []
for m in range(1, 33):
    modulus = 2**m
    assert any(c % modulus for c in powers[4*m+1])
    assert all(c % modulus == 0 for c in powers[4*m+2])
    first_zero = next(k for k, A in enumerate(powers) if all(c % modulus == 0 for c in A))
    assert first_zero == 4*m+2
    classes.append({'m': m, 'class': first_zero, 'order_power_of_two': 6*m+3})

# Hensel points on the original harmonic curve near all four boundary points.
# At finite boundaries use Z=2T:
# 191^4 Z(Z-1)(Z-2)=2*573*M^2 W^4.
# At infinity use S=1/T, V=W/T:
# 191^4(4S-6S^2+2S^3)=573*M^2 V^4.
den = 191**4
def eval_poly(cs, z):
    value = 0
    for c in reversed(cs):
        value = value*z+c
    return value

def deriv(cs):
    return [i*cs[i] for i in range(1, len(cs))]

def hensel_branch(cs, z0, L):
    s = v2(eval_poly(deriv(cs), z0))
    assert v2(eval_poly(cs, z0)) > 2*s
    scale, divisor = 2**(s+1), 2**(2*s+1)
    def q(u):
        value = eval_poly(cs, z0+scale*u)
        assert value % divisor == 0
        return value//divisor
    u = q(0) % 2
    assert q(u) % 2 == 0
    precision = L-(2*s+1)
    for k in range(1, precision):
        if q(u) % 2**(k+1):
            u += 2**k
        assert q(u) % 2**(k+1) == 0
    z = z0+scale*u
    assert v2(eval_poly(cs, z)) >= L
    assert v2(eval_poly(deriv(cs), z)) == s
    return z, s

witnesses = []
for k in range(1, 10):
    W = 2**k
    L = 4*k+20
    cs = [-2*573*M*M*W**4, 2*den, -3*den, den]
    for label, z0 in [('P0', 0), ('P1', 2), ('Ph', 1)]:
        Z, derivative_v = hensel_branch(cs, z0, L)
        T = F(Z, 2)
        x_value = C*W*W/T
        r = 2*v2(x_value)
        expected = {'P0': 2-4*k, 'P1': 4*k, 'Ph': 4*k+2}[label]
        assert r == expected
        # The actual root differs by valuation >=L-s, beyond all displayed
        # coordinate valuations. The same valuation therefore holds after lifting.
        assert L-derivative_v > v2(Z)
        witnesses.append({'boundary': label, 'k': k, 'root_coordinate': str(T),
                          'v_pi_x': r, 'first_excluded_n': 1+max(r, 2-r)//4,
                          'polynomial_error_v2': v2(eval_poly(cs, Z)),
                          'hensel_derivative_v2': derivative_v})
for k in range(2, 10):
    V = 2**k
    L = 4*k+20
    cs = [-573*M*M*V**4, 4*den, -6*den, 2*den]
    S, derivative_v = hensel_branch(cs, 0, L)
    r = 2*v2(C*V*V/F(S))
    assert r == 4-4*k
    assert L-derivative_v > v2(S)
    witnesses.append({'boundary': 'Pinf', 'k': k, 'root_coordinate': str(S),
                      'v_pi_x': r, 'first_excluded_n': 1+max(r, 2-r)//4,
                      'polynomial_error_v2': v2(eval_poly(cs, S)),
                      'hensel_derivative_v2': derivative_v})

data = {'threshold_checks': threshold_checks,
        'doubling_iteration_checks': iteration_checks,
        'module_nilpotency_checks': classes,
        'literal_hensel_boundary_witnesses': witnesses,
        'scaling_coefficient': str(C)}
(base/'harmonic_prym_finite_depth_certificate_data.json').write_text(json.dumps(data, indent=2)+'\n')
lines = [
    'PASS: literal scaled Prym coordinate and torsion-translation curve identities',
    'PASS: frozen T=31/2, tripod t=-899, three actual unit fourth-root branches, r=2',
    'PASS: fourth powers of every odd residue exclude the alternative dyadic sheet',
    f'PASS: {threshold_checks} exact exclusion/first-depth equivalences',
    f'PASS: {iteration_checks} doubling valuation iterations',
    'PASS: actual rank-six module recurrence gives exact class4m+2 for m=1..32',
    f'PASS: {len(witnesses)} literal Hensel branches at all four boundary points',
    'No infinite local search, Selmer-order computation or unproved class-group input is used.'
]
text = '\n'.join(lines)+'\n'
(base/'harmonic_prym_finite_depth_certificate_output.txt').write_text(text)
print(text, end='')
