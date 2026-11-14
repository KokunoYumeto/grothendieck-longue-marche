#!/usr/bin/env python3
"""Exact arithmetic inputs to the inert-prime presentation, A.25--A.26."""


def mul(x, y, prime):
    a, b = x
    c, d = y
    return ((a*c-b*d) % prime, (a*d+b*c-b*d) % prime)


def power(x, exponent, prime):
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = mul(result, x, prime)
        x = mul(x, x, prime)
        exponent //= 2
    return result


def is_prime(n):
    return n >= 2 and not any(n % d == 0 for d in range(2, int(n**0.5)+1))


def main():
    family, excluded = [], []
    for prime in range(2, 1001):
        if not is_prime(prime) or prime % 3 != 2:
            continue
        zeta, lam = (0, 1), (1, prime-1)
        exponent = (prime*prime-1)//3
        a = exponent % 3
        residue = power(lam, exponent, prime)
        b = next(j for j in range(3) if power(zeta, j, prime) == residue)
        assert b == 2*a % 3
        assert (a != 0) == (prime % 9 in (2, 5))
        assert power(lam, prime-1, prime) == tuple((-x) % prime for x in power(zeta, 2, prime))
        if a:
            family.append(prime)
        else:
            excluded.append(prime)
        if prime in (2, 5, 17):
            print("q", prime, "norm", prime*prime,
                  "Frobenius Kummer vector (zeta,lambda)", (a, b),
                  "determinant with tame and anti generator modulo3", (-2*a) % 3)
    print("Inert family Xi, q=2 or5 mod9, through1000:", family)
    print("Count:", len(family))
    print("Excluded inert primes q=8 mod9 through1000:", excluded)
    print("Density of Xi: 2/phi(9)=1/3; union with Sigma has density5/9.")
    # On H1 basis kappa_zeta,kappa_lambda,kappa_q, conjugation matrix.
    c_characters = [[1, 1, 0], [0, -1, 0], [0, 0, -1]]
    c_frattini = [list(row) for row in zip(*c_characters)]
    print("c on Kummer characters:", c_characters)
    print("c on the dual Frattini quotient:", c_frattini)
    for a in (1, 2):
        frob, tame, anti = [a, 2*a % 3, 0], [0, 0, 1], [0, 1, 0]
        apply_c = lambda vector: [sum(c_frattini[i][j]*vector[j] for j in range(3)) % 3 for i in range(3)]
        assert apply_c(frob) == frob
        assert apply_c(tame) == [(-x) % 3 for x in tame]
        assert apply_c(anti) == [(-x) % 3 for x in anti]
        assert (-2*a) % 3
    print("Frattini signs: global(+1,-2), local(+1,-1), complement(-1).")
    print("For an anti-invariant class x, z=x*c(x)^-1 has class2x and c(z)=z^-1 exactly.")
    print("PASS")


if __name__ == "__main__":
    main()
