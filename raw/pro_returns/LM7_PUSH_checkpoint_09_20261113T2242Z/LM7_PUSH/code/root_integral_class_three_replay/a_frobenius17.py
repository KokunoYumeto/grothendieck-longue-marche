#!/usr/bin/env python3
"""Exact checks for A.27: the unramified-at-three Heisenberg field and Frob17.

No floating-point logarithms are used.  Cyclotomic-ring identities are reduced
in Z[t]/(t^6+t^3+1), and the three-adic exponent is lifted by integer powers.
"""

from a_inert_prime import is_prime, mul, power


def add9(a, b):
    return tuple(x+y for x, y in zip(a, b))


def neg9(a):
    return tuple(-x for x in a)


def mul9(a, b):
    result = [0]*11
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    for k in range(10, 5, -1):
        result[k-3] -= result[k]
        result[k-6] -= result[k]
    return tuple(result[:6])


ONE = (1, 0, 0, 0, 0, 0)
THETA = (0, 1, 0, 0, 0, 0)


def power9(a, n):
    result = ONE
    while n:
        if n & 1:
            result = mul9(result, a)
        a = mul9(a, a)
        n //= 2
    return result


def substitute9(a, image):
    result = (0,)*6
    for coefficient in reversed(a):
        result = mul9(result, image)
        result = add9(result, (coefficient, 0, 0, 0, 0, 0))
    return result


def hmul(g, h):
    """Normal form sigma^a tau^b rho^z, [sigma,tau]=rho."""
    a, b, z = g
    aa, bb, zz = h
    return ((a+aa) % 3, (b+bb) % 3, (z+zz-aa*b) % 3)


def hc(g):
    a, b, z = g
    return (a, (a-b) % 3, (-a*(a+1)//2-z) % 3)


def finite_theta(prime):
    zeta = (0, 1)
    for a in range(prime):
        for b in range(prime):
            x = power((a, b), (prime*prime-1)//9, prime)
            cube = power(x, 3, prime)
            if cube == zeta:
                return x
            if cube == power(zeta, 2, prime):
                return power(x, 2, prime)
    raise AssertionError("primitive ninth root not found")


def sub(prime, x, y):
    return tuple((a-b) % prime for a, b in zip(x, y))


def lift_exponent(base, target, digits):
    """Return a mod 3^digits with base^a=target mod 3^(digits+1)."""
    exponent = 0
    for n in range(digits):
        modulus = 3**(n+2)
        options = [exponent + digit*3**n for digit in range(3)]
        solutions = [x for x in options if pow(base, x, modulus) == target % modulus]
        assert len(solutions) == 1
        exponent = solutions[0]
    return exponent


def main():
    zeta = power9(THETA, 3)
    lam = add9(ONE, neg9(zeta))
    us = [add9(ONE, neg9(power9(THETA, 1+3*i))) for i in range(3)]
    omega = mul9(us[1], power9(us[2], 2))
    sigma_omega = substitute9(omega, power9(THETA, 4))
    conjugate_omega = substitute9(omega, power9(THETA, 8))
    assert mul9(mul9(us[0], us[1]), us[2]) == lam
    assert mul9(sigma_omega, lam) == mul9(omega, power9(us[0], 3))
    assert conjugate_omega == neg9(omega)
    print("Ring: Z[theta]/(theta^6+theta^3+1), coefficients from degree0 to5.")
    print("omega=(1-theta^4)*(1-theta^7)^2:", omega)
    print("Verified Norm(1-theta)=lambda; sigma(omega)/omega=(1-theta)^3/lambda; c(omega)=-omega.")

    elements = [(a, b, z) for a in range(3) for b in range(3) for z in range(3)]
    for g in elements:
        assert hc(hc(g)) == g
        for h in elements:
            assert hc(hmul(g, h)) == hmul(hc(g), hc(h))
        if g[0] == 0:
            assert hmul(g, hc(g)) == (0, 0, 0)
    print("Verified all27 Heisenberg elements and729 products under c: sigma->tau*sigma, tau->tau^-1, rho->rho^-1.")
    print("Every rational inert Frobenius with q=-1 mod9 squares to1 in this degree27 quotient.")

    checked = []
    for prime in range(2, 1001):
        if not is_prime(prime) or prime % 9 != 8:
            continue
        theta0 = finite_theta(prime)
        zz = (0, 1)
        ll = (1, prime-1)
        for i in range(3):
            theta = mul(theta0, power(zz, i, prime), prime)
            u1 = sub(prime, (1, 0), power(theta, 4, prime))
            u2 = sub(prime, (1, 0), power(theta, 7, prime))
            om = mul(u1, power(u2, 2, prime), prime)
            assert power(theta, 3, prime) == zz
            assert power(om, prime, prime) == tuple(-x % prime for x in om)
            assert power(ll, (prime*prime-1)//3, prime) == (1, 0)
            assert power(om, (prime*prime-1)//3, prime) == (1, 0)
            if prime == 17:
                roots = [(a, b) for a in range(prime) for b in range(prime)
                         if power((a, b), 3, prime) == om]
                print("q17 theta", theta, "omega", om, "cube roots ofomega", roots,
                      "cubic residue", power(om, 96, prime))
        checked.append(prime)
    print("All three theta choices verified for q=-1 mod9 through1000:", checked)

    for digits in (2, 4, 6, 8, 12):
        aa = lift_exponent(7, -17, digits)
        modulus = 3**digits
        commutator = (-aa*aa*pow(2, -1, modulus)) % modulus
        assert aa % 3 == 0 and aa % 9 != 0
        assert pow(7, 2*aa, 3**(digits+1)) == 17**2 % 3**(digits+1)
        print("q17 modulus3^", digits, "a=log(-17)/log7", aa,
              "commutator exponent -a^2/2", commutator)
    print("The normalized integral class-two Frobenius is u^a*(cuc)^a*[u,cuc]^(-a^2/2).")
    print("v3(a)=1, while the entire exponent-three Heisenberg Frobenius is trivial.")
    print("PASS")


if __name__ == "__main__":
    main()
