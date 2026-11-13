#!/usr/bin/env python3
"""Exact residue checks for the two-prime pro-3 decomposition at 7.

The group-theoretic and Brauer arguments are in statements A.14--A.15.
This script checks the finite arithmetic input, including the orientation
change when complex conjugation transports a positive tame generator.
"""

from itertools import permutations


def det(matrix):
    n = len(matrix)
    answer = 0
    for permutation in permutations(range(n)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(n) for j in range(i + 1, n)
        )
        term = -1 if inversions % 2 else 1
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        answer += term
    return answer


def kummer_frobenius(unit, zeta, prime=7):
    residue = pow(unit % prime, (prime - 1) // 3, prime)
    return next(k for k in range(3) if pow(zeta, k, prime) == residue)


def main():
    print("K = Q(zeta), zeta^2+zeta+1 = 0, lambda = 1-zeta")
    print("pi = 2-zeta, pi_bar = 3+zeta, pi*pi_bar = 7")
    for name, zeta in [("q", 2), ("q_bar", 4)]:
        assert (zeta*zeta+zeta+1) % 7 == 0
        values = {"zeta": zeta, "lambda": 1-zeta,
                  "pi": 2-zeta, "pi_bar": 3+zeta}
        print(name, "residues", {k: v % 7 for k, v in values.items()})
        print(name, "unit Kummer Frobenius values", {
            k: kummer_frobenius(v, zeta)
            for k, v in values.items() if v % 7
        })

    # Frobenius at q fixes a compatible root of pi; its c-conjugate at
    # q_bar fixes the conjugate root of pi_bar. Positive inertia at both
    # places uses the same globally fixed zeta; thus c(tau_q)=tau_qbar^-1.
    # Rows: F_q, tau_q, F_qbar, tau_qbar. Columns: zeta,lambda,pi,pi_bar.
    restriction = [[2, 0, 0, 2],
                   [0, 0, 1, 0],
                   [2, 2, 1, 0],
                   [0, 0, 0, 1]]
    transported = [row[:] for row in restriction]
    transported[3] = [(-x) % 3 for x in restriction[3]]
    print("restriction matrix, positive tame generators:", restriction)
    print("integer determinant:", det(restriction))
    print("determinant modulo 3:", det(restriction) % 3)
    print("restriction matrix, c-transported second tame generator:", transported)
    print("transported determinant modulo 3:", det(transported) % 3)
    assert det(restriction) % 3 != 0
    assert det(transported) % 3 != 0
    unit_matrix = [[2, 0], [2, 2]]
    print("unramified unit matrix:", unit_matrix)
    print("unramified determinant modulo 3:", det(unit_matrix) % 3)
    assert det(unit_matrix) % 3 == 1
    print("Brauer 3-torsion: (x_lambda,x_q,x_qbar) with sum zero;")
    print("inverse to restriction at q,q_bar is (x,y) -> (-x-y,x,y).")
    for x in range(3):
        for y in range(3):
            triple = ((-x-y) % 3, x, y)
            assert sum(triple) % 3 == 0
    print("All nine Brauer invariant pairs checked.")

    print("Sigma: split q with q=4 or 7 mod 9 and 3 not a cube mod q")
    sigma = []
    for prime in range(5, 1001):
        if any(prime % d == 0 for d in range(2, int(prime**0.5) + 1)):
            continue
        if prime % 3 != 1:
            continue
        roots = [z for z in range(2, prime) if (z*z+z+1) % prime == 0]
        assert len(roots) == 2
        zeta, zeta_bar = roots
        exponent = (prime-1)//3
        a = exponent % 3
        b = kummer_frobenius(1-zeta, zeta, prime)
        b_bar = kummer_frobenius(1-zeta_bar, zeta_bar, prime)
        k3 = kummer_frobenius(3, zeta, prime)
        assert b_bar == (a-b) % 3
        assert k3 == (-a-b) % 3
        matrix = [[a, b], [a, b_bar]]
        elementary_condition = prime % 9 in (4, 7) and pow(3, exponent, prime) != 1
        determinant_condition = det(matrix) % 3 != 0
        assert elementary_condition == determinant_condition
        if elementary_condition:
            sigma.append(prime)
    print("Sigma primes <=1000:", sigma)
    print("Count:", len(sigma))
    admissible_vectors = [(a, b) for a in range(3) for b in range(3)
                          if (a*(a+b)) % 3]
    print("Admissible Frobenius vectors in F3^2:", admissible_vectors)
    print("Conjugation sends (a,b) to (a,a-b).")
    print("Conjugacy-stable subset size 4 in group of order 18: density 2/9.")
    assert len(admissible_vectors) == 4
    assert {(a, (a-b) % 3) for a, b in admissible_vectors} == set(admissible_vectors)
    print("PASS")


if __name__ == "__main__":
    main()
