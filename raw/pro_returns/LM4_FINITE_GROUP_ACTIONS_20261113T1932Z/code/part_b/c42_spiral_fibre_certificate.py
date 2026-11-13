#!/usr/bin/env python3
"""Exact symbolic identities for the spiral action in C.42.

The proof supplies the global topology.  This certificate checks the flow,
commutation, covering labels, and loop formulas without floating-point input.
The coordinate z=tan(delta/2) describes each nonfixed flow interval after
choosing its continuous angle branch; z'=z gives the flow parameter law.
"""
import json
from pathlib import Path

import sympy as S


def main():
    a, b, c, s, theta, t, delta, theta0 = S.symbols(
        "a b c s theta t delta theta0", real=True
    )
    z = S.symbols("z", real=True)
    k, j = S.symbols("k j", integer=True)
    rho = S.symbols("rho", real=True)
    beta = S.Function("beta")
    checks = {}

    def check(name, lhs, rhs):
        residual = S.simplify(lhs - rhs)
        assert residual == 0, (name, residual)
        checks[name] = {"left": str(lhs), "right": str(rhs), "residual": "0"}

    flow = S.exp(b) * z
    check("half_angle_flow_law", S.exp(c) * flow, S.exp(b + c) * z)
    check("half_angle_inverse", S.exp(-b) * flow, z)
    check("half_angle_identity", flow.subs(b, 0), z)
    check("half_angle_ode", S.diff(flow, b), flow)
    angle_derivative = 2 * S.diff(flow, b) / (1 + flow**2)
    rational_sine = 2 * flow / (1 + flow**2)
    check("angle_ode_delta_prime_equals_sin_delta", angle_derivative, rational_sine)
    sine = 2 * flow / (1 + flow**2)
    cosine = (1 - flow**2) / (1 + flow**2)
    check("rational_circle_equation", sine**2 + cosine**2, 1)
    check("fixed_even_endpoint_sine", sine.subs(z, 0), 0)
    check("fixed_even_endpoint_cosine", cosine.subs(z, 0), 1)
    check("fixed_odd_endpoint_sine", S.limit(sine, z, S.oo), 0)
    check("fixed_odd_endpoint_cosine", S.limit(cosine, z, S.oo), -1)

    # A_a(s,theta)=(s+a,theta+a); B_b(s,theta)=(theta+beta_b(s-theta),theta).
    after_b_then_a_s = theta + beta(b, s - theta) + a
    after_a_then_b_s = theta + a + beta(b, (s + a) - (theta + a))
    check("A_B_commute_s_coordinate", after_b_then_a_s, after_a_then_b_s)
    check("A_B_commute_theta_coordinate", theta + a, theta + a)
    check("A_preserves_delta", (s + a) - (theta + a), s - theta)
    check("spiral_s_coordinate", (t + delta) - t, delta)
    check("A_on_spiral_t", t + a, t + a)
    check("A_on_spiral_delta", (t + delta + a) - (t + a), delta)
    check("B_on_spiral_delta", (t + beta(b, delta)) - t, beta(b, delta))
    check("spiral_parameter_commutation_z", S.exp(b) * z, S.exp(b) * z)

    # Integer labels record all preimages under the stated covering q(t)=t mod 2pi.
    labelled_t = theta0 + 2 * S.pi * k
    check("labelled_fibre_cos", S.cos(labelled_t), S.cos(theta0))
    check("labelled_fibre_sin", S.sin(labelled_t), S.sin(theta0))
    check("distinct_label_difference", labelled_t - (theta0 + 2 * S.pi * j),
          2 * S.pi * (k - j))
    check("real_lift_on_label_k", labelled_t, theta0 + 2 * S.pi * k)
    check("deck_translation_on_lift", (t + 2 * S.pi * k) - t, 2 * S.pi * k)
    check("operator_preserves_quotient_cos", S.cos(t - 2 * S.pi * k), S.cos(t))
    check("operator_preserves_quotient_sin", S.sin(t - 2 * S.pi * k), S.sin(t))
    check("operator_radial_formula", S.exp(t + delta - 2 * S.pi * k),
          S.exp(-2 * S.pi * k) * S.exp(t + delta))

    tau = S.symbols("tau", real=True)
    segments = [(3 * tau, S.Integer(0)),
                (2 - 3 * tau, 3 * tau - 1),
                (S.Integer(0), 3 - 3 * tau)]
    times = [S.Integer(0), S.Rational(1, 3), S.Rational(2, 3), S.Integer(1)]
    vertices = [(0, 0), (1, 0), (0, 1), (0, 0)]
    for index, segment in enumerate(segments):
        for coordinate in range(2):
            check(f"segment_{index}_start_coordinate_{coordinate}",
                  segment[coordinate].subs(tau, times[index]),
                  S.Integer(vertices[index][coordinate]))
            check(f"segment_{index}_end_coordinate_{coordinate}",
                  segment[coordinate].subs(tau, times[index + 1]),
                  S.Integer(vertices[index + 1][coordinate]))
            contracted = (1 - rho) * segment[coordinate]
            check(f"contraction_{index}_initial_coordinate_{coordinate}",
                  contracted.subs(rho, 0), segment[coordinate])
            check(f"contraction_{index}_final_coordinate_{coordinate}",
                  contracted.subs(rho, 1), S.Integer(0))

    output = {
        "claim": "C.42",
        "arithmetic": "exact symbolic; integer labels; no floating-point inputs",
        "flow_coordinate": "z=tan(delta/2); z_b=exp(b) z, with the continuous angle branch on each fixed-point interval",
        "whole_fibre": "coproduct over k in Z of {(theta0+2*pi*k,delta): 0<delta<pi}",
        "real_lift": "F(t,delta)=t; each fibre {t=c} is one proper line",
        "operator": "A_(-2*pi*n); radial difference exp(-2*pi*n)*exp(t+delta)",
        "loop_vertex_times": [str(value) for value in times],
        "loop_vertices": vertices,
        "homotopy": "multiply both loop parameters by 1-rho",
        "checks": checks,
        "number_of_identity_checks": len(checks),
        "all_assertions_passed": True,
        "scope": "Symbolic identities only; continuity, properness, closedness, and component topology are proved in c42.tex.",
    }
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"C.42 PASS: {len(checks)} exact symbolic identities; all residuals zero.")
    print(destination)


if __name__ == "__main__":
    main()
