"""Exact finite stress checks for A.23's mixed ramification bookkeeping.

The proof is the two inductions in sections/A.tex.  This finite enumeration
is not a proof for all n.  It independently checks the numerical genus,
local index, and full-branch assertions for small prime powers, including
partial ramification and genus-zero/genus-one third quotients.
"""

from itertools import product
from math import gcd
from pathlib import Path
import json


def genus(n, exponents):
    numerator = -2 * n + sum(n - gcd(n, a) for a in exponents)
    assert numerator % 2 == 0
    return 1 + numerator // 2


def checks():
    prime_powers = [(4, 2), (8, 2), (9, 3), (16, 2), (25, 5)]
    count = 0
    full_count_reductions = 0
    lower_degree_base_cases = 0
    third_genera = {"zero": 0, "one": 0, "at_least_two": 0}
    witnesses = {}
    for n, ell in prime_powers:
        for r in range(3, 5):
            for initial in product(range(1, n), repeat=r - 1):
                last = (-sum(initial)) % n
                if last == 0:
                    continue
                exponents = initial + (last,)
                if gcd(n, *exponents) != 1 or genus(n, exponents) < 2:
                    continue
                count += 1
                full = [i for i, a in enumerate(exponents) if a % ell]
                prime_genus = genus(ell, [a % ell for a in exponents])
                assert len(full) == sum(gcd(n, a) == 1 for a in exponents)
                if prime_genus == 0:
                    lower_degree_base_cases += 1
                    assert (n // ell) < n
                    continue
                assert prime_genus >= 1
                assert len(full) >= (4 if ell == 2 else 3)
                for i in full:
                    for j in full:
                        if i == j:
                            continue
                        b = [0] * r
                        b[i], b[j] = exponents[i], (-exponents[i]) % n
                        assert genus(n, b) == 0
                        h = [(a - b0) % n for a, b0 in zip(exponents, b)]
                        assert h[i] == 0
                        assert all(h[t] == exponents[t] for t in range(r) if t not in (i, j))
                        assert sum(a % ell != 0 for a in h) < len(full)
                        assert gcd(n, *h) == 1  # an unchanged full-index place remains
                        assert genus(n, h) < genus(n, exponents)
                        # The auxiliary cover is etale away from i,j; at i,j
                        # both source and auxiliary have full tame index n.
                        for t, (a, b0) in enumerate(zip(exponents, b)):
                            e_c = n // gcd(n, a)
                            e_b = n // gcd(n, b0)
                            assert e_c % e_b == 0
                        g_h = genus(n, h)
                        key = "zero" if g_h == 0 else "one" if g_h == 1 else "at_least_two"
                        third_genera[key] += 1
                        full_count_reductions += 1
                        witness_key = f"n{n}_{key}"
                        witnesses.setdefault(witness_key, {
                            "n": n, "ell": ell,
                            "exponents": list(exponents), "selected": [i, j],
                            "genus_C": genus(n, exponents),
                            "third_exponents": h, "genus_H2": g_h,
                            "full_before": len(full),
                            "full_after": sum(a % ell != 0 for a in h),
                        })

    # Deliberately mixed full/partial 2-power ramification.
    n = 8
    exponents = [1, 1, 1, 1, 4]
    h = [0, 2, 1, 1, 4]
    assert genus(n, exponents) == 9 and genus(n, h) == 5
    assert genus(2, [a % 2 for a in h]) == 0
    witnesses["mixed_degree_eight"] = {
        "n": 8, "exponents": exponents, "genus_C": 9,
        "third_exponents": h, "genus_H2": 5,
        "third_prime_quotient_genus": 0,
        "consequence": "outer degree-four induction, despite partial ramification",
    }

    coprime_local_cases = 0
    for a in range(2, 25):
        for b in range(2, 25):
            if gcd(a, b) != 1:
                continue
            for ea in range(1, a + 1):
                if a % ea:
                    continue
                for eb in range(1, b + 1):
                    if b % eb:
                        continue
                    assert gcd(ea, eb) == 1
                    coprime_local_cases += 1

    assert all(third_genera.values())
    return {
        "passed": True,
        "scope": "Finite exact arithmetic stress checks; the universal proof is A.23.",
        "prime_powers": prime_powers,
        "connected_hyperbolic_branch_vectors": count,
        "genus_zero_prime_quotient_base_cases": lower_degree_base_cases,
        "full_branch_reductions": full_count_reductions,
        "third_quotient_genus_counts": third_genera,
        "coprime_local_index_cases": coprime_local_cases,
        "witnesses": witnesses,
    }


if __name__ == "__main__":
    result = checks()
    output = Path(__file__).with_name("A_cyclic_ramification_checks_output.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "witnesses"}, indent=2))
