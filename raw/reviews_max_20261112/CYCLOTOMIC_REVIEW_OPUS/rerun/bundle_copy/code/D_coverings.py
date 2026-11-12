#!/usr/bin/env python3
"""Exact certificates for the two cyclotomic points of the three-punctured line.

All elliptic arithmetic takes place in Q[a]/(a^6-a^3+1), a=exp(2*pi*i/18).
No floating-point comparison is used.  The arithmetic proof that the exhibited
degree-81 cover separates the Galois sets is in Statement D4 of the paper.
Run: python code/D_coverings.py > code/D_coverings_output.txt
"""
from fractions import Fraction
from collections import Counter
import sympy as sp
from sympy.polys.domains import QQ, ZZ
from sympy.matrices.normalforms import smith_normal_form


def two_step_checks(bound=12):
    """Check exact root-of-unity exponents in the fibre bijection.

    For z=xi_6, w=exp(2*pi*i*(1+6*k)/(6*n)), zeta=exp(2*pi*i*j/n),
    send w to zeta^-2/w and u to lambda*u, with
    lambda=exp(2*pi*i*(1/2-j/n-(1+6*k)/(6*n))/m).
    The polynomial identity for the radicands is checked symbolically once.
    """
    w, zeta = sp.symbols('w zeta', nonzero=True)
    identity = sp.cancel((1-zeta*(zeta**-2/w)) + (1-zeta*w)/(zeta*w))
    assert identity == 0
    checks = 0
    for n in range(1, bound+1):
        for m in range(1, bound+1):
            for j in range(n):
                image = []
                for k in range(n):
                    theta = Fraction(1+6*k, 6*n)
                    theta_zeta = Fraction(j, n)
                    theta_new = -2*theta_zeta-theta
                    theta_lambda = (Fraction(1, 2)-theta_zeta-theta)/m
                    assert (n*theta_new+Fraction(1, 6)).denominator == 1
                    assert m*theta_lambda == Fraction(1, 2)-theta_zeta-theta
                    k_new = (-k-2*j) % n
                    assert (theta_new-Fraction(-1+6*k_new, 6*n)).denominator == 1
                    image.append(k_new)
                    checks += 1
                assert sorted(image) == list(range(n))
    print('Two-step radicand identity:', identity)
    print('Two-step range: 1 <= n,m <=', bound, '; every zeta in mu_n')
    print('Exact fibre-branch checks:', checks)
    print('All checks passed; the proof establishes the identity for every n,m.')


def elliptic_checks():
    a_symbol = sp.Symbol('a')
    modulus = sp.Poly(sp.cyclotomic_poly(18, a_symbol), a_symbol)
    K = QQ.algebraic_field((modulus, a_symbol))
    a = K.unit
    omega = a**6
    assert a**6-a**3+1 == K.zero
    assert omega**2+omega+1 == K.zero
    assert a**3+a**-3 == K.one

    def add(P, Q):
        if P is None: return Q
        if Q is None: return P
        x, y = P
        X, Y = Q
        if x == X and y == -Y: return None
        slope = (Y-y)/(X-x) if x != X else K(3)*x*x/(K(2)*y)
        xx = slope*slope-x-X
        return xx, slope*(x-xx)-y

    def neg(P):
        return None if P is None else (P[0], -P[1])

    def mul(n, P):
        R = None
        while n:
            if n & 1: R = add(R, P)
            P = add(P, P)
            n >>= 1
        return R

    def image(w, v):
        assert w**3+v**3 == K.one
        assert w+v != K.zero
        P = K(12)/(w+v), K(36)*(w-v)/(w+v)
        assert P[1]**2 == P[0]**3-K(432)
        return P

    def render(P):
        return 'O' if P is None else '('+', '.join(str(K.to_sympy(v)) for v in P)+')'

    def exact_order(P):
        for n in (1, 3, 9):
            if mul(n, P) is None: return n
        raise AssertionError('Order is not a divisor of 9')

    P = image(a, a**-1)
    print('\nField modulus:', modulus.as_expr())
    print('Elliptic model: Y^2=X^3-432')
    print('P =', render(P))
    print('3P =', render(mul(3, P)))
    print('Exact order of P:', exact_order(P))
    for sign, name in ((1, 'xi_6'), (-1, 'xi_6^-1')):
        orders = []
        triples = []
        print('Fibre above', name, ':')
        for i in range(3):
            for j in range(3):
                Q = image(omega**i*a**sign, omega**j*a**(-sign))
                difference = add(Q, neg(P))
                order = exact_order(difference)
                triple = mul(3, difference)
                orders.append(order)
                triples.append(triple)
                print('  i=%d,j=%d: order(Q-P)=%d; 3(Q-P)=%s' % (i,j,order,render(triple)))
        print('Order counts:', dict(sorted(Counter(orders).items())))
        if sign == -1:
            assert orders == [9]*9
            assert all(T == mul(3, P) for T in triples)
        else:
            assert Counter(orders) == Counter({1:1, 3:8})

    points7 = [(x,y) for x in range(7) for y in range(7)
               if (y*y-x*x*x+432) % 7 == 0]
    print('\nAffine F_7-points:', points7)
    print('#E(F_7), including O:', len(points7)+1)
    assert len(points7)+1 == 9
    print('Frobenius trace: 7+1-9=-1')
    W = sp.Matrix([[0,-1],[1,-1]])  # multiplication by omega
    C = sp.Matrix([[1,-1],[0,-1]])  # complex conjugation of Z[omega]
    A = sp.eye(2)+3*W              # alpha=1+3*omega
    conjugate_A = C*A*C
    delta = A-conjugate_A
    beta = -sp.eye(2)-2*W
    assert A.trace() == -1 and A.det() == 7
    assert delta*beta == 9*sp.eye(2)
    print('omega matrix:', W.tolist())
    print('Frobenius alpha matrix:', A.tolist())
    print('alpha-conjugate(alpha):', delta.tolist())
    print('Smith form:', smith_normal_form(delta, domain=ZZ).tolist())
    print('(alpha-conjugate(alpha))*(-1-2*omega):', (delta*beta).tolist())
    for n in (9,27,81):
        kernel = [(x,y) for x in range(n) for y in range(n)
                  if all(v % n == 0 for v in delta*sp.Matrix([x,y]))]
        assert all((9*x) % n == 0 and (9*y) % n == 0 for x,y in kernel)
        print('mod %d: kernel size %d; every vector is killed by 9' % (n,len(kernel)))
    print('\nDegree-81 cover: R |-> z([3]R+P).')
    print('Fibre over xi_6 contains the F-rational point R=O.')
    print('Every F-rational point over xi_6^-1 would have exact order 27,')
    print('excluded by the commutator calculation proved in Statement D4.')
    print('All exact arithmetic assertions passed.')


if __name__ == '__main__':
    two_step_checks()
    elliptic_checks()
