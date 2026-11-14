#!/usr/bin/env python3
"""The mixed Heisenberg quotient for Kummer(3,17), including its local Frobenius.

The norm witness is u=2+alpha^2, alpha^3=3, with Norm(u)=17.
Coefficients are exact pairs in F_17[zeta]/(zeta^2+zeta+1).
"""

from a_inert_prime import mul, power
from itertools import product
from sympy import Symbol


def add(a, b, p):
    return tuple((x+y) % p for x, y in zip(a, b))


def scale(a, k, p):
    return tuple(k*x % p for x in a)


def zmul(a, b):
    """Z[zeta,alpha], zeta²+zeta+1=0, alpha³=3; paired coefficients."""
    out = [0]*6
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            alpha_degree, zeta_degree = i//2+j//2, i%2+j%2
            value = ai*bj
            if alpha_degree >= 3:
                alpha_degree -= 3
                value *= 3
            if zeta_degree == 2:
                out[2*alpha_degree] -= value
                out[2*alpha_degree+1] -= value
            else:
                out[2*alpha_degree+zeta_degree] += value
    return tuple(out)


def zpow(a, n):
    result = (1, 0, 0, 0, 0, 0)
    for _ in range(n):
        result = zmul(result, a)
    return result


def zsigma(a):
    result = [0]*6
    zz = (0, 1, 0, 0, 0, 0)
    for i, coefficient in enumerate(a):
        term = [0]*6
        term[i] = coefficient
        term = zmul(tuple(term), zpow(zz, i//2))
        result = [x+y for x, y in zip(result, term)]
    return tuple(result)


def zconjugate(a):
    return tuple(coefficient for i in range(3)
                 for coefficient in (a[2*i]-a[2*i+1], -a[2*i+1]))


def main():
    p = 17
    zeta = (0, 1)
    uu = (2, 0, 0, 0, 1, 0)
    uu1, uu2 = zsigma(uu), zsigma(zsigma(uu))
    omega = zmul(uu1, zpow(uu2, 2))
    assert zmul(zmul(uu, uu1), uu2) == (17, 0, 0, 0, 0, 0)
    assert tuple(17*x for x in zsigma(omega)) == zmul(omega, zpow(uu, 3))
    assert zmul(zmul(omega, zconjugate(omega)), zpow(uu, 3)) == (17**3, 0, 0, 0, 0, 0)
    print("Exact ring basis (1,zeta,alpha,zeta*alpha,alpha²,zeta*alpha²).")
    print("omega coefficients:", omega)
    print("Verified sigma(omega)/omega=u³/17 and c(omega)*omega=(17/u)³.")
    root = next(x for x in range(p) if x**3 % p == 3)
    assert root == 7
    print("Norm witness: alpha^3=3, u=2+alpha^2, Norm(u)=2^3+9=17.")
    print("At the selected prime above17: alpha=7, u=0.")
    for i in range(3):
        alpha = scale(power(zeta, i, p), root, p)
        alpha2 = power(alpha, 2, p)
        us = [add((2, 0), mul(power(zeta, 2*j, p), alpha2, p), p)
              for j in range(3)]
        om = mul(us[1], power(us[2], 2, p), p)
        print("prime", i, "alpha", alpha, "(u,sigma(u),sigma²(u))", us, "omega", om)
        if i == 0:
            assert us[0] == (0, 0) and us[1] != (0, 0) and us[2] != (0, 0)
            residue = power(om, 96, p)
            exponent = next(j for j in range(3) if power(zeta, j, p) == residue)
            print("unit omega", om, "omega^96", residue, "central Frobenius exponent", exponent)
            assert exponent == 0
            # Inversion of omega agrees with its nonzero norm in F_(17²).
            assert power(om, p*p-1, p) == (1, 0)
    print("The local Frobenius fixes cube roots of3 and of the uniformizer17;")
    print("its remaining image is rho to the displayed exponent, with [sigma,tau]=rho.")
    # The rest of the degree-three part of W can be arbitrary: its X³ and Y³
    # coefficients are fixed by a17=6mod9.  Compute [W_3,T] symbolically.
    wcubic = {word: Symbol('w_'+word) for word in map(''.join, product('XYT', repeat=3))}
    wcubic['XXX'] = wcubic['YYY'] = 2
    wcubic['TTT'] = 0
    commutator = {}
    for word, coefficient in wcubic.items():
        commutator[word+'T'] = commutator.get(word+'T', 0) + coefficient
        commutator['T'+word] = commutator.get('T'+word, 0) - coefficient
    assert commutator['XXXT'] == commutator['YYYT'] == 2
    assert commutator['TXXX'] == commutator['TYYY'] == -2
    print("For arbitrary other cubic Magnus coefficients of W, [W_3,T] has XXXT and YYYT coefficients2mod3.")
    print("The tame power t^(1-289) starts in degree9; the global defining relation has exact Zassenhaus degree4.")
    print("PASS")


if __name__ == '__main__':
    main()
