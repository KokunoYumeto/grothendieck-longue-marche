#!/usr/bin/env python3
"""Compatible order-three points in the complete dihedral shadow subsystem.

These points are in its inverse limit. No order-three lift to GT_0 is claimed.
"""
import json
from pathlib import Path


def roots7(depth=10):
    root, modulus = 2, 7
    out = [{"power": 1, "modulus": 7, "root": 2}]
    for depth_now in range(2, depth + 1):
        candidates = [root + modulus * k for k in range(7)
                      if ((root + modulus * k) ** 2 + root + modulus * k + 1)
                      % (7 * modulus) == 0]
        assert len(candidates) == 1
        old_root, old_modulus = root, modulus
        root, modulus = candidates[0], 7 * modulus
        assert root % old_modulus == old_root
        assert pow(root, 3, modulus) == 1 and root % 7 == 2
        out.append({"power": depth_now, "modulus": modulus, "root": root})
    return out


def shadow(n, root_table):
    modulus = 2 * n
    cofactor, exponent = modulus, 0
    while cofactor % 7 == 0:
        cofactor //= 7
        exponent += 1
    if exponent == 0:
        u = 1
    else:
        ppart = 7 ** exponent
        root = root_table[exponent - 1]["root"]
        u = (1 + cofactor * ((root - 1) * pow(cofactor, -1, ppart) % ppart)) % modulus
        assert u % ppart == root and u % cofactor == 1 % cofactor
    assert pow(u, 3, modulus) == 1
    if n % 4 == 0:
        nu = (u - 1) // 4 if u % 4 == 1 else (u + 1) // 4
        assert nu % 2 == 0
    return {"n": n, "k_mod_n_over_2": 0, "u_mod_2n": u,
            "order": 1 if u == 1 else 3}


def least_prime_factor(n):
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return n


def main():
    roots = roots7()
    levels = [4, 6, 8, 10, 14, 18, 28, 32, 42, 70, 98, 196, 294,
              686, 1372, 2744]
    family = [shadow(n, roots) for n in levels]
    compatibility_count = 0
    for low in family:
        for high in family:
            if high["n"] % low["n"] == 0:
                assert high["u_mod_2n"] % (2 * low["n"]) == low["u_mod_2n"]
                compatibility_count += 1
    primes = []
    for q in (2, 3, 5, 7, 11, 13):
        p = least_prime_factor(2 ** q - 1)
        assert pow(2, q, p) == 1 and 2 % p != 1 and (p - 1) % q == 0
        primes.append({"desired_prime_order": q, "chosen_coordinate_prime": p,
                       "root_residue": 2})
    out = {"root_lifts_in_Z7": roots,
           "finite_dihedral_coordinates": family,
           "compatible_reduction_pairs_checked": compatibility_count,
           "prime_order_constructions": primes,
           "exact_infinite_claim": "CRT and the unique Hensel lift yield one compatible order-three point in the inverse limit of all dihedral shadows.",
           "remaining_GT0_step": "Order-bounded lifts through every isolated shadow, including the nonmetabelian refinements, have not been constructed."}
    Path(__file__).with_name("gt_shadow_all_prime_output.json").write_text(
        json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
