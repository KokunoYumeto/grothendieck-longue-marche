#!/usr/bin/env python3
"""Exact support-prime calculation for the first integral class-three example."""
import sympy as s

q, m, alpha, gamma, u = s.symbols('q m alpha gamma u')
e = (q - 1) / 2
beta, t = (q - 1) * u, m * u
binom_qm_2 = q * m * (q * m - 1) / 2
residue = m * gamma - q * (alpha + e) * t + beta * binom_qm_2 / q + e * m * t
claimed = m * (gamma - q * alpha * u) + (q*q - 1) * u * m * (m - 1) / 2
assert s.expand(residue - claimed) == 0
print('PASS: exact positive-support residue identity')

for q_residue in range(1, 125, 25):
    for alpha_residue in range(0, 25, 5):
        for gamma_residue in range(25):
            if gamma_residue % 5 == 0:
                continue
            for u_residue in range(25):
                value = claimed.subs({q:q_residue, m:120, alpha:alpha_residue,
                                      gamma:gamma_residue, u:u_residue})
                assert value.is_Integer
                assert int(value) % 25 != 0
                assert int(value) % 5 == 0
print('PASS: all residue classes satisfying q=1 mod25, alpha=0 mod5, gamma!=0 mod5')
print('PASS: v5(Z_D)=1 and q^2-1 divisible by25 for every permitted class')
