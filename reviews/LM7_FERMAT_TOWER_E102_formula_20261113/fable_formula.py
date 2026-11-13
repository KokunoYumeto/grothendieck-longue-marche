"""The closed formula for E.102 (Claude Fable 5.2 at effort max, 13 Nov 2026).  No linear algebra here: only the
table of the six pieces (principal case) and the sign multiplicities.

Input: (dp, dm) = c-signs on D_0, the part of the cusp lattice C not touched by the Weil-pairing glue:
       (dp, dm) = (C_plus - 1, C_minus - 1) = (2, 4) for the return's data (c-signs on C: (3, 5)).
Output: the multiplicities of C_3, C_9, C_27, C_81, the free rank and the number of unit pivots of
        C_4 = K_4 / (T_4 - 1) K_4^{J=+1},  K_4 = Lambda^2 Lambda^2 V.
"""
from math import comb

# Table (principal case: chi = N(pi), pi = 1 mod 3, N(pi) != 1 mod 9, pi != conj(pi) mod 9):
# piece -> (Q+, Q-) as lists of exponents e (cyclic factors C_{3^e})
TABLE = {
    "a  Lambda^2 Lambda^2 V1        (rank 15)": ([3, 3], [2, 2, 4]),
    "b  chi^2 Lambda^2 V1           (rank  6)": ([1], [1, 3]),
    "c  chi^2 S^2 V1                (rank 10)": ([1, 4], [2]),
    "d  chi^4                       (rank  1)": ([1], []),
    "e  chi Lambda^2 V1 (x) V1      (rank 24)": ([1, 3, 3, 4], [1, 2, 3, 3]),
    "f  chi^3 V1                    (rank  4)": ([1], [2]),
}


def multiplicities(dp, dm):
    a, b = comb(dp, 2) + comb(dm, 2), dp * dm            # c-signs (a, b) of Lambda^2 D_0
    return [(1, 0), (dp * dp + dm * dm, 2 * dp * dm), (a, b), (comb(a, 2) + comb(b, 2), a * b),
            (dp, dm), (dp * a + dm * b, dp * b + dm * a)]


def smith(dp, dm):
    count = {1: 0, 2: 0, 3: 0, 4: 0}
    for (qp, qm), (mp, mm) in zip(TABLE.values(), multiplicities(dp, dm)):
        for e in qp:
            count[e] += mp
        for e in qm:
            count[e] += mm
    vp, vm = 2 + dp, 2 + dm                              # c-signs on V (V_1 has signs (2, 2))
    A, B = comb(vp, 2) + comb(vm, 2), vp * vm            # c-signs on Lambda^2 V
    kplus, kminus = comb(A, 2) + comb(B, 2), A * B       # c-signs on K_4
    return count, kminus, kplus - sum(count.values())


def closed_polynomials(dp, dm):
    n, a, b = dp + dm, comb(dp, 2) + comb(dm, 2), dp * dm
    return {1: n * n + n + a + comb(a, 2) + comb(b, 2) + dp * a + dm * b,
            2: b + dm + dp * b + dm * a,
            3: 2 + 2 * b + 2 * n,
            4: a + dp}


if __name__ == "__main__":
    for dp, dm in ((2, 4), (4, 2), (0, 6), (6, 0), (3, 3), (1, 5)):
        count, free, unit = smith(dp, dm)
        assert count == closed_polynomials(dp, dm)
        print("D_0 signs (%d,%d): Z^%d + C3^%d + C9^%d + C27^%d + C81^%d   (unit pivots %d)" % (
            dp, dm, free, count[1], count[2], count[3], count[4], unit))
