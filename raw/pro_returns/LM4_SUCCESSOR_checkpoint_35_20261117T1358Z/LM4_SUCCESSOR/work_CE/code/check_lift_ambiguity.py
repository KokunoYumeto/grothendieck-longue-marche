"""Exact finite certificates for B.42--B.44.

This checks the small Frobenius factorization, the integer bounds in
the Jordan argument, and the sparse coefficient conditions for the
degree-10000 S_n polynomial.  It does not pretend to enumerate its
splitting field; the local inertia and permutation proofs are in TeX.
"""
from math import factorial, gcd
import sympy as S

x = S.symbols('x')
f5 = x**5-x-1
f3 = S.Poly(f5, x, modulus=3)
small_gcd = f3.gcd(S.Poly(x**9-x, x, modulus=3))
assert small_gcd.degree() == 0
# A reducible degree-five polynomial has an irreducible factor of
# degree one or two, each dividing x^(3^2)-x over F_3.
print('x^5-x-1 mod3: gcd with x^9-x =', small_gcd.as_expr())
print('Irreducible mod3 by the degree-five factor bound: PASS')

g2 = x**2+x+1
h2 = x**3+x**2+1
assert S.Poly(f5-g2*h2, x, modulus=2).is_zero
assert all(int(g2.subs(x, a)) % 2 for a in (0, 1))
assert all(int(h2.subs(x, a)) % 2 for a in (0, 1))
assert S.Poly(f5, x, modulus=2).gcd(
    S.Poly(S.diff(f5, x), x, modulus=2)).degree() == 0
print('mod2 = (x^2+x+1)(x^3+x^2+1), irreducible square-free factors: PASS')

J = factorial(98)
for q, rank in ((2, 2500), (3, 3333)):
    log_floor = 0
    while q**(log_floor+1) <= J:
        log_floor += 1
    assert q**log_floor <= J < q**(log_floor+1)
    bound = 97+log_floor
    assert rank > bound
    print(f'q={q}: floor(log_q(98!))={log_floor}; '
          f'section-rank bound={bound}; A_10000 rank={rank}: PASS')

simple_order = factorial(10000)//2
automorphism_kernel_bound = 576**576
assert simple_order > automorphism_kernel_bound
print('10000!/2 > 576^576: PASS '
      f'(bit lengths {simple_order.bit_length()} > '
      f'{automorphism_kernel_bound.bit_length()})')

n = 10000
coefficients = {n: 1, n-1: 15, 2: 10, 0: 30}
mod2 = {i: a % 2 for i, a in coefficients.items() if a % 2}
mod3 = {i: a % 3 for i, a in coefficients.items() if a % 3}
assert mod2 == {n: 1, n-1: 1}
assert mod3 == {n: 1, 2: 1}
assert all(a % 5 == 0 for i, a in coefficients.items() if i < n)
assert coefficients[0] % 25 != 0
assert coefficients[0] % 2 == 0 and coefficients[0] % 4 != 0
assert coefficients[0] % 3 == 0 and coefficients[0] % 9 != 0
assert gcd(n-1, 2) == 1
assert gcd(n-2, 3) == 1
print('f = x^10000 + 15*x^9999 + 10*x^2 + 30')
print('Eisenstein at5: PASS')
print('mod2 = x^9999*(x+1), v_2(constant)=1, 9999 prime to2: PASS')
print('mod3 = x^2*(x^9998+1), v_3(constant)=1, 9998 prime to3: PASS')
print('Local argument yields a 9999-cycle and one transposition; '
      'the transitive group is S_10000.')
print('All finite checks: PASS')
