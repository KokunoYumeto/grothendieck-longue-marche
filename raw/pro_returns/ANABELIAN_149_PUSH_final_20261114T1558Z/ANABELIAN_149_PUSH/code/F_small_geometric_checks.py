"""Exact finite supplements to F.49; no infinite field claim is tested here."""
from fractions import Fraction
from pathlib import Path
import json


def clean(polynomial):
    return {a: c for a, c in polynomial.items() if c}


def derivative(polynomial):
    return clean({a - 1: a * c for a, c in polynomial.items() if a})


def remainder_mod_xm_minus_one(polynomial, m):
    answer = {}
    for a, c in polynomial.items():
        answer[a % m] = answer.get(a % m, Fraction(0)) + c
    return clean(answer)


def cycle(n, letters):
    answer = list(range(n))
    for i, a in enumerate(letters):
        answer[a - 1] = letters[(i + 1) % len(letters)] - 1
    return tuple(answer)


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def generated_group(n, generators):
    identity = tuple(range(n))
    known = {identity}
    frontier = [identity]
    while frontier:
        a = frontier.pop()
        for b in generators:
            c = compose(a, b)
            if c not in known:
                known.add(c)
                frontier.append(c)
    return known


def main():
    records = []
    for m in range(2, 13):
        n = 2 * m + 1
        polynomial = {
            n: Fraction(1),
            m + 1: -Fraction(2 * n, m + 1),
            1: Fraction(n),
        }
        expected_derivative = {2 * m: Fraction(n), m: Fraction(-2 * n), 0: Fraction(n)}
        expected_remainder = {1: Fraction(2 * m * m, m + 1)}
        assert derivative(polynomial) == expected_derivative
        assert remainder_mod_xm_minus_one(polynomial, m) == expected_remainder
        records.append({
            "m": m,
            "degree": n,
            "derivative_identity": True,
            "critical_value_remainder_coefficient": str(expected_remainder[1]),
            "critical_value_identity": True,
        })
    group_records = []
    for n in (5, 7):
        group = generated_group(n, [cycle(n, list(range(1, n + 1))), cycle(n, [1, 2, 3])])
        expected = 1
        for i in range(2, n + 1):
            expected *= i
        expected //= 2
        assert len(group) == expected
        group_records.append({"n": n, "n_cycle_and_three_cycle_group_order": len(group)})
    support_records = []
    for n, triples, expected in [
        (4, [[1, 2, 3], [1, 2, 4]], 12),
        (5, [[1, 2, 3], [1, 4, 5]], 60),
        (5, [[1, 4, 5], [2, 4, 5]], 12),
    ]:
        group = generated_group(n, [cycle(n, triple) for triple in triples])
        assert len(group) == expected
        support_records.append({"letters": n, "triples": triples, "group_order": len(group)})
    result = {
        "status": "PASS",
        "claim": "F.49",
        "scope": "Exact finite polynomial and permutation supplements only; the theorem proves all m, smallness, normality, strictness and reconstruction without numerical inference.",
        "polynomial_records": records,
        "two_generator_records": group_records,
        "support_induction_records": support_records,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(records)} polynomial identities, {len(group_records)} two-generator groups, {len(support_records)} support groups")


if __name__ == "__main__":
    main()
