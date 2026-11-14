#!/usr/bin/env python3
"""Exact finite comparisons for the unnumbered tau/cusp follow-up.

The A5 map is the actual D77 endomorphism of the standard full coproduct.
It is NOT claimed to be rho*i for the labelled retraction in the new note.
The S3 calculation tests the canonical full-to-pro-2 coproduct comparison.
All permutation multiplication is (p*q)(i)=p(q(i)).
"""
from itertools import permutations
from pathlib import Path
import json


def permutation_tools(n):
    identity = tuple(range(n))

    def mul(p, q):
        return tuple(p[q[i]] for i in range(n))

    def inv(p):
        return tuple(p.index(i) for i in range(n))

    def power(p, k):
        if k < 0:
            return power(inv(p), -k)
        result = identity
        while k:
            if k & 1:
                result = mul(result, p)
            p = mul(p, p)
            k >>= 1
        return result

    def conj(p, g):
        return mul(mul(g, p), inv(g))

    def generated(generators):
        known, todo = {identity}, [identity]
        while todo:
            old = todo.pop()
            for generator in generators:
                new = mul(old, generator)
                if new not in known:
                    known.add(new)
                    todo.append(new)
        return known

    def order(p):
        q, count = p, 1
        while q != identity:
            q, count = mul(q, p), count + 1
        return count

    def cycles(p):
        seen, result = set(), []
        for i in range(n):
            if i not in seen:
                cycle, j = [], i
                while j not in seen:
                    seen.add(j)
                    cycle.append(j + 1)
                    j = p[j]
                if len(cycle) > 1:
                    result.append(cycle)
        return result

    return identity, mul, inv, power, conj, generated, order, cycles


checks = []


def check(name, condition):
    assert condition, name
    checks.append({"name": name, "passed": True})


def coproduct_comparison():
    one, mul, inv, power, conj, generated, order, cycles = permutation_tools(3)
    a = (1, 0, 2)  # (12)
    b = (0, 2, 1)  # (23)
    t = mul(b, a)
    image = generated([a, b])
    check("S3_factor_generators_are_involutions", order(a) == order(b) == 2)
    check("S3_rotation_has_order_three", order(t) == 3)
    check("S3_dihedral_inversion_relation", conj(t, a) == inv(t))
    check("S3_full_product_map_is_onto", len(image) == 6)
    check("S3_image_is_not_a_2_group", len(image) % 3 == 0)
    return {
        "a_cycles": cycles(a), "b_cycles": cycles(b), "t_ba_cycles": cycles(t),
        "image_order": len(image), "rotation_order": order(t),
        "canonical_map": "Zhat semidirect C2 -> Z2 semidirect C2; (lambda,e) -> (lambda_2,e)",
        "kernel": "product of Z_l over odd primes l",
        "kernel_element_test": "the idempotent e_3 has residue 1 mod 3, so t^e_3 maps to t in S3",
    }


def d77_original_z_comparison():
    one, mul, inv, power, conj, generated, order, cycles = permutation_tools(5)
    A5 = [p for p in permutations(range(5))
          if sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2 == 0]
    a = (1, 0, 3, 2, 4)  # (12)(34)
    b = (2, 4, 0, 3, 1)  # (13)(25)
    c = (3, 2, 1, 0, 4)  # (14)(23)
    x, y = mul(b, a), mul(c, a)
    z = inv(mul(x, y))
    commutator = mul(mul(mul(x, y), inv(x)), inv(y))
    g = mul(mul(x, commutator), inv(x))
    delta_g = conj(g, a)
    Y = mul(mul(g, y), inv(delta_g))
    image_c = conj(c, g)
    image_x, image_y = x, Y
    image_z = inv(mul(image_x, image_y))
    check("D77_A5_has_sixty_elements", len(A5) == 60)
    check("D77_named_factors_have_order_two", all(order(t) == 2 for t in [a, b, c]))
    check("D77_q_source_is_A5", generated([a, b, c]) == set(A5))
    check("D77_q_orientation_kernel_is_A5", generated([x, y]) == set(A5))
    check("D77_g_is_132", cycles(g) == [[1, 3, 2]])
    check("D77_conjugated_c_is_a", image_c == a)
    check("D77_Y_is_identity", Y == one)
    check("D77_endomorphism_orientation_image_order_five", len(generated([image_x, image_y])) == 5)
    check("D77_endomorphism_extension_image_order_ten", len(generated([a, b, image_c])) == 10)
    check("D77_original_boundary_relation", mul(mul(x, y), z) == one)
    check("D77_image_boundary_relation", mul(mul(image_x, image_y), image_z) == one)
    check("D77_original_z_and_image_z_have_order_five", order(z) == order(image_z) == 5)
    check("D77_original_z_reflection_is_b", conj(z, b) == inv(z))
    check("D77_image_z_reflection_is_b", conj(image_z, b) == inv(image_z))
    table = []
    for residue in range(1, 5):
        x_conjugators = [u for u in A5 if conj(power(x, residue), u) == image_x]
        z_conjugators = [u for u in A5 if conj(power(z, residue), u) == image_z]
        table.append({"unit_residue_mod_5": residue,
                      "x_conjugator_count": len(x_conjugators),
                      "z_conjugator_count": len(z_conjugators)})
    x_residues = [row["unit_residue_mod_5"] for row in table if row["x_conjugator_count"]]
    z_residues = [row["unit_residue_mod_5"] for row in table if row["z_conjugator_count"]]
    check("D77_x_admissible_unit_residues_are_1_4", x_residues == [1, 4])
    check("D77_z_admissible_unit_residues_are_2_3", z_residues == [2, 3])
    check("D77_no_common_x_z_unit_residue", not set(x_residues).intersection(z_residues))
    return {
        "source": "E0=C2(a)*C2(b)*C2(c); F0=Fhat(x=ba,y=ca)",
        "full_endomorphism": "Phi(a)=a; Phi(b)=b; Phi(c)=g c g^-1; g=x[x,y]x^-1",
        "quotient_values": {name: cycles(value) for name, value in
                            [("a", a), ("b", b), ("c", c), ("x", x), ("y", y),
                             ("z", z), ("g", g), ("Phi_x", image_x),
                             ("Phi_y", image_y), ("Phi_z", image_z)]},
        "source_image_order": 60, "Phi_orientation_image_order": 5,
        "Phi_extension_image_order": 10,
        "unit_power_conjugacy_table": table,
        "scope": "This Phi is not the labelled tau=rho*i when f=1: that tau equals the identity by q4*i=id.",
    }


output = {
    "status": "PASS",
    "coproduct_comparison": coproduct_comparison(),
    "d77_original_z_comparison": d77_original_z_comparison(),
    "checks": checks,
    "assertion_count": len(checks),
}
destination = Path(__file__).with_name("tau_cusp_and_coproduct_comparison_output.json")
destination.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
