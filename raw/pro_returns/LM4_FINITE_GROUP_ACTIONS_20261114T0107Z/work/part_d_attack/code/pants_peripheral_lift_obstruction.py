#!/usr/bin/env python3
"""Finite lift comparison for the actual D74 pants peripheral maps.

This checks a deliberately specified relative embedding problem.  It is not
a counterexample to D74.40 and does not construct a nonstandard involution.
The source E is used through its proved elementary abelian quotient
A=H_1(E,F_2), with coordinates (x,y,s).  Every homomorphism E -> B factors
through A because B is elementary abelian.  The three full dihedral source
groups are used through their actual rotation-mod-2 quotients.
"""
from itertools import product, permutations
from pathlib import Path
import json


def linear(images, value):
    out = 0
    for i, image in enumerate(images):
        if value & (1 << i):
            out ^= image
    return out


def a5_comparison():
    identity = tuple(range(5))
    elements = [p for p in permutations(range(5))
                if sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2 == 0]
    multiply = lambda p, q: tuple(p[q[i]] for i in range(5))
    inv = {p: tuple(p.index(i) for i in range(5)) for p in elements}
    conjugate = lambda p, g: multiply(multiply(g, p), inv[g])

    def generated(generators):
        known, todo = {identity}, [identity]
        while todo:
            old = todo.pop()
            for generator in generators:
                new = multiply(old, generator)
                if new not in known:
                    known.add(new)
                    todo.append(new)
        return known

    def order(p):
        power, out = p, 1
        while power != identity:
            power = multiply(power, p)
            out += 1
        return out

    checks = []

    def check(name, condition):
        assert condition, name
        checks.append({"name": name, "passed": True})

    involutions = [p for p in elements if order(p) == 2]
    a = (1, 0, 3, 2, 4)  # (12)(34)
    b = (2, 3, 0, 1, 4)  # (13)(24)
    c = (1, 0, 4, 3, 2)  # (12)(35)
    xlocal, ylocal, zlocal = multiply(b, a), multiply(b, a), multiply(c, a)
    check("A5_has_60_elements", len(elements) == 60)
    check("A5_has_15_involutions", len(involutions) == 15)
    check("all_involutions_are_conjugate", {conjugate(a, g) for g in elements} == set(involutions))
    local_data = {}
    for name, rotation in [("D_x", xlocal), ("D_y", ylocal), ("D_z", zlocal)]:
        check(name + "_dihedral_relations", multiply(a, a) == identity and
              conjugate(rotation, a) == inv[rotation])
        local_data[name] = {"rotation": rotation, "reflection": a,
                            "rotation_order": order(rotation),
                            "image_order": len(generated([a, rotation]))}
    check("local_rotation_orders_are_2_2_3", [local_data[n]["rotation_order"]
                                              for n in local_data] == [2, 2, 3])
    check("first_local_reflection_is_distinct_from_rotation", a != xlocal)
    check("local_image_orders_are_4_4_6", [local_data[n]["image_order"]
                                           for n in local_data] == [4, 4, 6])

    pairs = [(x, y) for x, y in product(involutions, repeat=2)
             if order(multiply(x, y)) == 3]
    records, candidates = [], []
    for x, y in pairs:
        Q = generated([x, y])
        normalizer = [g for g in elements if {conjugate(q, g) for q in Q} == Q]
        commuters = [g for g in normalizer if multiply(g, x) == multiply(x, g)]
        assert len(Q) == 6 and set(normalizer) == Q
        assert set(commuters) == {identity, x}
        possible_s = [s for s in commuters if order(s) == 2 and s != x]
        candidates.extend((x, y, s) for s in possible_s)
        records.append({"x": x, "y": y, "Q_order": len(Q),
                        "normalizer_order": len(normalizer),
                        "centralizer_in_normalizer_order": len(commuters),
                        "possible_s_count": len(possible_s)})
    check("all_rotation_pairs_enumerated", len(pairs) == 60)
    check("every_pair_generates_a_self_normalizing_order_six_group", all(
        row["Q_order"] == row["normalizer_order"] == 6 for row in records))
    check("all_normalizer_commuters_are_one_or_x", all(
        row["centralizer_in_normalizer_order"] == 2 for row in records))
    check("no_possible_image_of_s", not candidates)
    # The actual e_2 exponent is 1 modulo 2 and 0 modulo 3.
    endpoints = {"D_x": [a, multiply(xlocal, a)],
                 "D_y": [a, multiply(ylocal, a)], "D_z": [a, a]}
    transports = {}
    for name, endpoint_pair in endpoints.items():
        transports[name] = [next(g for g in elements if conjugate(a, g) == t)
                            for t in endpoint_pair]
    check("canonical_e2_endpoints_all_have_actual_conjugators", all(
        conjugate(a, transports[name][i]) == endpoints[name][i]
        for name in endpoints for i in range(2)))

    # Make the local projections injective while retaining the A5 obstruction.
    # This is the actual quotient of E obtained from F_ab modulo 6.
    A = list(product(range(6), range(6), range(2)))
    one_A = (0, 0, 0)

    def mul_A(g, h):
        sign = -1 if g[2] else 1
        return ((g[0] + sign * h[0]) % 6, (g[1] + sign * h[1]) % 6, g[2] ^ h[2])

    def mul_B(g, h):
        return multiply(g[0], h[0]), mul_A(g[1], h[1])

    def perm_power(g, n):
        out = identity
        for _ in range(n):
            out = multiply(out, g)
        return out

    check("actual_abelian_mod_six_quotient_has_order_72", len(A) == 72)
    # The chosen original b_z has the t1 class, hence its vector modulo 2
    # is (1,0).  The proof covers every possible actual mod-six vector.
    z_reflections = [(i, j) for i in (1, 3, 5) for j in (0, 2, 4)]
    source = list(product(range(6), range(2)))
    mul_source = lambda g, h: ((g[0] + (-1 if g[1] else 1) * h[0]) % 6, g[1] ^ h[1])
    graph_checks = []
    cases = [("D_x", (1, 0), (0, 0), xlocal), ("D_y", (0, 1), (0, 0), ylocal)]
    cases += [("D_z", (5, 5), w, zlocal) for w in z_reflections]
    for name, v, w, rotation in cases:
        def local_graph(g):
            r, eps = g
            image_A = ((r * v[0] + eps * w[0]) % 6,
                       (r * v[1] + eps * w[1]) % 6, eps)
            image_A5 = multiply(perm_power(rotation, r), a if eps else identity)
            return image_A5, image_A
        images = [local_graph(g) for g in source]
        is_hom = all(local_graph(mul_source(g, h)) == mul_B(local_graph(g), local_graph(h))
                     for g, h in product(source, repeat=2))
        injective_projection = len({im[1] for im in images}) == 12
        assert is_hom and injective_projection
        graph_checks.append({"peripheral": name, "A_rotation_vector": v,
                             "A_reflection_vector": w, "image_order": len(set(images)),
                             "projection_image_order": len({im[1] for im in images}),
                             "is_homomorphism": is_hom,
                             "projection_injective_on_local_image": injective_projection})
    check("all_actual_local_graph_maps_checked", len(graph_checks) == 11)
    check("all_local_projections_are_isomorphisms_onto_their_images", all(
        row["projection_injective_on_local_image"] and row["image_order"] == 12
        for row in graph_checks))
    gamma0 = lambda g: (a if g[2] else identity, g)
    check("section_class_comparison_gamma0_is_a_global_lift", all(
        gamma0(mul_A(g, h)) == mul_B(gamma0(g), gamma0(h)) for g, h in product(A, repeat=2)))
    return {
        "A": {"group": "(Z/6)^2 semidirect_inversion C2", "order": 72,
              "actual_phi_on_x_y_s": [[1, 0, 0], [0, 1, 0], [0, 0, 1]]},
        "B": {"group": "A5 x A", "order": 4320},
        "pi": "second coordinate B -> A; kernel A5 x {1}",
        "permutation_convention": "zero-based arrays, multiply(p,q)=p composed with q",
        "A5_elements": elements,
        "A5_involutions": involutions,
        "local_dihedral_maps": local_data,
        "canonical_e2_endpoint_images": endpoints,
        "endpoint_transports_from_a": transports,
        "local_graph_definition": "sigma_j(d)=(rho_j(d),phi(d))",
        "local_graph_map_checks": graph_checks,
        "section_lift": "gamma0(e)=(a^u(e),phi(e)); u:E->C2 is the actual quotient",
        "all_rotation_pair_checks": records,
        "checks": checks, "check_count": len(checks),
        "all_passed": all(check["passed"] for check in checks),
        "reason": "Q=<gamma(x),gamma(y)> is normal in gamma(E); its normalizer in A5 has no involution centralizing gamma(x) other than gamma(x), whereas the D_x map requires a distinct one.",
        "scope": "The endpoint classes are compatible up to ker(pi)-conjugacy. This is still an auxiliary relative-lift obstruction, not a test of D74.40."
    }


def main():
    # B has ordered basis (a,b,c,d); A has ordered basis (x,y,s).
    a, b, c, d = 1, 2, 4, 8
    pi_images = (4, 5, 4, 6)
    pi = lambda value: linear(pi_images, value)
    kernel = [v for v in range(16) if pi(v) == 0]
    x_lift, y_lift, z_lift = a ^ b, c ^ d, b ^ d
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append({"name": name, "passed": True})

    check("pi_is_a_homomorphism", all(pi(u ^ v) == (pi(u) ^ pi(v))
                                        for u, v in product(range(16), repeat=2)))
    check("pi_is_surjective", set(map(pi, range(16))) == set(range(8)))
    check("kernel_is_the_a_plus_c_line", kernel == [0, a ^ c])
    check("actual_section_images_are_distinct", len({pi(a), pi(b), pi(d)}) == 3)
    check("first_and_third_factor_images_merge", pi(a) == pi(c) and a != c)

    # Each D_j -> B factors through the dihedral quotient with rotation
    # order 2, hence C_2 x C_2.  Coordinates are (rotation, reflection).
    locals_data = {
        "D_x": {"B_rotation": x_lift, "B_reflection": a,
                "A_rotation": 1, "A_reflection": 4},
        "D_y": {"B_rotation": y_lift, "B_reflection": c,
                "A_rotation": 2, "A_reflection": 4},
        "D_z": {"B_rotation": z_lift, "B_reflection": b,
                "A_rotation": 3, "A_reflection": 5},
    }
    for name, data in locals_data.items():
        sig = lambda v, data=data: linear((data["B_rotation"], data["B_reflection"]), v)
        phi = lambda v, data=data: linear((data["A_rotation"], data["A_reflection"]), v)
        check(name + "_local_map_is_homomorphism", all(sig(u ^ v) == (sig(u) ^ sig(v))
                                                       for u, v in product(range(4), repeat=2)))
        check(name + "_local_triangle_commutes", all(pi(sig(v)) == phi(v) for v in range(4)))

    check("original_xyz_relation_has_nonzero_lift", x_lift ^ y_lift ^ z_lift == a ^ c != 0)
    check("original_xyz_relation_dies_after_pi", pi(x_lift ^ y_lift ^ z_lift) == 0)

    splittings = []
    for images in product(range(16), repeat=3):
        if all(pi(images[i]) == (1 << i) for i in range(3)):
            L = lambda value, images=images: linear(images, value)
            flags = {
                "D_x": L(1) == x_lift and L(4) == a,
                "D_y": L(2) == y_lift and L(4) == c,
                "D_z": L(3) == z_lift and L(5) == b,
                "three_sections": L(4) == a and L(5) == b and L(6) == d,
            }
            splittings.append({"images_of_x_y_s": list(images), **flags})
    check("all_eight_global_lifts_enumerated", len(splittings) == 8)
    check("no_global_lift_of_all_peripherals", not any(all(row[name] for name in locals_data)
                                                      for row in splittings))
    check("already_no_global_lift_of_Dx_and_Dy", not any(row["D_x"] and row["D_y"]
                                                        for row in splittings))
    section_solutions = [row for row in splittings if row["three_sections"]]
    check("unique_global_lift_of_the_three_sections", len(section_solutions) == 1)
    check("section_solution_has_typed_images", section_solutions[0]["images_of_x_y_s"] == [3, 9, 1])
    check("kernel_conjugation_is_trivial", all(k ^ v ^ k == v for k in kernel for v in range(16)))

    a5_result = a5_comparison()
    result = {
        "purpose": "Exact section/peripheral relative-lift comparison for actual D74 maps",
        "scope": "This deliberately incompatible local lift problem does not test existence in D74.40.",
        "A": {"order": 8, "basis": ["x", "y", "s"]},
        "B": {"order": 16, "basis": ["a", "b", "c", "d"]},
        "pi_basis_images": list(pi_images),
        "kernel": kernel,
        "peripheral_local_data": locals_data,
        "all_global_lifts": splittings,
        "compatible_section_lifts": section_solutions,
        "peripheral_obstruction": {
            "lift_of_xyz": x_lift ^ y_lift ^ z_lift,
            "name": "a+c",
            "image_in_A": 0,
        },
        "checks": checks,
        "check_count": len(checks),
        "all_passed": all(check["passed"] for check in checks),
        "a5_class_compatible_peripheral_comparison": a5_result,
        "total_check_count": len(checks) + a5_result["check_count"],
        "all_comparisons_passed": all(check["passed"] for check in checks) and a5_result["all_passed"],
    }
    output = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("pants_peripheral_lift_obstruction_output.json").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
