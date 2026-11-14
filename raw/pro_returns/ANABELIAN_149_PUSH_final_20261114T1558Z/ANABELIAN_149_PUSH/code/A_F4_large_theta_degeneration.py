#!/usr/bin/env python3
"""Independent integer/coset audit of the fixed large-theta witness.

This uses neither the search normalization nor Hermite normal form.
Local logarithm residues and generalized-CRT compatibility classify the
quotient of the unit group by multiplication by two exactly.
Divisor arithmetic is separately checked by A_F4_large_theta_canonical.py;
this script does not duplicate or claim independence for that arithmetic.
"""
from pathlib import Path
from math import gcd, isqrt, lcm, prod
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def log_table(p):
    # Choose the LAST primitive root, deliberately unlike the search.
    for g in range(p - 1, 1, -1):
        a, out = 1, {}
        while a not in out:
            out[a] = len(out)
            a = a * g % p
        if len(out) == p - 1:
            assert a == 1
            return g, out
    raise AssertionError("no primitive root")


def main():
    raw = (ROOT / "A_F4_large_theta_witness.json").read_bytes()
    w = json.loads(raw)
    search = json.loads((ROOT / "A_F4_large_theta_search.json").read_text())
    ps = [7, 31, 2503, 4519]
    assert all(is_prime(p) for p in ps)
    n = prod(ps)
    assert n == w["odd_exponent"] == 2454499369
    tables = [log_table(p) for p in ps]
    orders = [p - 1 for p in ps]
    vectors = [table[2] for _, table in tables]
    local_indices = [gcd(o, v) for o, v in zip(orders, vectors)]
    periods = [o // c for o, c in zip(orders, local_indices)]
    assert local_indices == [2, 6, 2, 6]
    assert periods == [3, 5, 1251, 753]
    assert all(gcd(periods[1], periods[j]) == 1 for j in [0, 2, 3])
    assert all(gcd(periods[i], periods[j]) == 3 for i, j in [(0, 2), (0, 3), (2, 3)])
    period = lcm(*periods)
    assert period == 1570005
    assert prod(orders) // period == prod(local_indices) * 3 * 3 == 1296

    def signature(index):
        assert gcd(index, n) == 1
        logs = [table[index % p] for p, (_, table) in zip(ps, tables)]
        residues = [a % c for a, c in zip(logs, local_indices)]
        times = [((a - r) // c) * pow(v // c, -1, m) % m
                 for a, r, c, v, m in zip(logs, residues, local_indices, vectors, periods)]
        return tuple(residues + [(times[2] - times[0]) % 3,
                                 (times[3] - times[0]) % 3])

    seen = set()
    for witness in w["witnesses"]:
        i = witness["index"]
        assert 0 < i < n
        value = signature(i)
        assert value not in seen
        seen.add(value)
        assert signature(2 * i % n) == value
    assert len(seen) == 1296
    expected = {(a, b, c, d, e, f)
                for a in range(2) for b in range(6)
                for c in range(2) for d in range(6)
                for e in range(3) for f in range(3)}
    assert seen == expected

    # Check every fixed witness was reindexed from the same positive packet.
    positive = search["positive_direction"]
    packet = list(search["packets"][positive].values())
    old = {(v["x"], v["y"]): v for v in packet}
    first = search["positive_theta_generator"]
    theta_index = first["index"]
    assert gcd(theta_index, n) == 1
    assert [first["x"], first["y"]] == w["theta_generator_point"]
    inv = pow(theta_index, -1, n)
    for witness in w["witnesses"]:
        v = old[(witness["x"], witness["y"])]
        assert witness["index"] == v["index"] * inv % n
        assert all(v["index"] % p == a for p, a in zip(ps, v["prime_components"]))

    # Independently compute #J(F_(4^9)) by Newton sums, not a matrix determinant.
    # The previously independently checked F4 Weil polynomial is
    # X^4 + 2 X^3 + X^2 + 8 X + 16.
    sums = [4, -2, 2, -26, 2]
    for k in range(5, 19):
        sums.append(-2 * sums[k - 1] - sums[k - 2]
                    - 8 * sums[k - 3] - 16 * sums[k - 4])
    q = 4 ** 9
    middle = (sums[9] ** 2 - sums[18]) // 2
    jac_order = q * q + 1 - (q + 1) * sums[9] + middle
    assert jac_order == w["Jacobian_order"] == 4 * 7 * n == 68725982332
    assert q + 1 - sums[9] > 0

    out = {
        "status": "PASS",
        "fixed_witness_sha256": hashlib.sha256(raw).hexdigest(),
        "method": "local discrete logarithms and pairwise generalized-CRT compatibility; no search normalization or HNF",
        "primes": ps,
        "independent_primitive_roots": [g for g, _ in tables],
        "local_indices": local_indices,
        "local_doubling_periods": periods,
        "global_doubling_period": period,
        "exact_quotient_order": 1296,
        "distinct_fixed_witness_cosets": len(seen),
        "all_quotient_signatures_covered": seen == expected,
        "fixed_witness_reindexing_checks": len(w["witnesses"]),
        "Newton_trace_9": sums[9],
        "Newton_trace_18": sums[18],
        "exact_Jacobian_order": jac_order,
        "curve_point_count": q + 1 - sums[9],
        "scope": "Exact orbit, CRT and group-order audit; divisor relations are supplied by the separately reviewed canonical checker."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
