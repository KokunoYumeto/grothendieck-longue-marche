#!/usr/bin/env python3
"""Exact cyclotomic certificate for the AC.42 Frobenius-cocycle model.

This is an abstract cocycle calculation, not a Jacobian realization.
All polynomial computations take place in Z[X]/Phi_{3^n}(X).
"""
import json
from pathlib import Path


def valuation_two(value):
    assert value != 0
    value = abs(value)
    return (value & -value).bit_length() - 1


def orbit(base, modulus):
    result = []
    value = 1
    while value not in result:
        result.append(value)
        value = value * base % modulus
    assert value == 1
    return result


def product_in_cyclotomic_ring(exponents, m):
    """Multiply (1-2X^a), using Phi_{3^n}=1+X^m+X^(2m)."""
    modulus = 3 * m
    coefficients = [1] + [0] * (2 * m - 1)
    for exponent in exponents:
        temporary = [0] * modulus
        for i, coefficient in enumerate(coefficients):
            temporary[i] += coefficient
            temporary[(i + exponent) % modulus] -= 2 * coefficient
        for i in range(2 * m, modulus):
            coefficient = temporary[i]
            temporary[i - m] -= coefficient
            temporary[i - 2 * m] -= coefficient
        coefficients = temporary[:2 * m]
    return coefficients


def mod_two_fixed_dimension(m):
    """Binary rank of sigma_4-1 on F_4[Z]/(Z^m-omega)."""
    pivots = {}
    for i in range(m):
        quotient, residue = divmod(4 * i, m)
        for b in range(2):
            omega_power = (b + quotient) % 3
            omega_bits = (1, 2, 3)[omega_power]
            column = omega_bits << (2 * residue)
            column ^= 1 << (2 * i + b)
            while column:
                pivot = column.bit_length() - 1
                if pivot in pivots:
                    column ^= pivots[pivot]
                else:
                    pivots[pivot] = column
                    break
    return 2 * m - len(pivots)


def run():
    rows = []
    for n in range(1, 7):
        modulus = 3 ** n
        m = 3 ** (n - 1)
        fourth_power_orbit = orbit(4, modulus)
        square_orbit = orbit(2, modulus)
        assert len(fourth_power_orbit) == m
        assert set(fourth_power_orbit) == set(range(1, modulus, 3))
        assert len(square_orbit) == 2 * m
        assert set(square_orbit) == {a for a in range(modulus) if a % 3}

        q_four_product = product_in_cyclotomic_ring(fourth_power_orbit, m)
        expected = [0] * (2 * m)
        expected[0] = 1
        expected[m] = -(2 ** m)
        assert q_four_product == expected

        full_product = product_in_cyclotomic_ring(square_orbit, m)
        full_norm = 1 + 2 ** m + 2 ** (2 * m)
        assert full_product == [full_norm] + [0] * (2 * m - 1)
        assert full_norm % 2 == 1
        assert valuation_two(full_norm - 1) == m
        assert mod_two_fixed_dimension(m) == 2

        rows.append({
            "n": n,
            "torsion_order": modulus,
            "Frobenius_4_orbit_length": m,
            "Frobenius_2_orbit_length": 2 * m,
            "return_over_Q2_omega": "1 - 2^m * omega",
            "return_minus_one_valuation": m,
            "full_norm": str(full_norm),
            "full_norm_valuation": 0,
            "full_norm_minus_one_valuation": m,
            "rational_annihilator_model": "2^" + str(m),
            "semilinear_cokernel": "(Z/2^m)^2",
            "mod_two_fixed_dimension_over_F2": 2,
            "exact_polynomial_orbit_checks": True,
        })
    return {
        "status": "proved abstract algebraic cocycle; no Jacobian realization asserted",
        "coefficient": "A(X)=1-2X",
        "base_unramified_field": "Q_2(omega), omega^2+omega+1=0",
        "uniform_coefficient_minus_one_valuation": 1,
        "scope": "variable-length norms defeat a finite-type-coefficient-only bound",
        "rows": rows,
    }


if __name__ == "__main__":
    result = run()
    target = Path(__file__).with_name("frobenius_norm_obstruction_output.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
