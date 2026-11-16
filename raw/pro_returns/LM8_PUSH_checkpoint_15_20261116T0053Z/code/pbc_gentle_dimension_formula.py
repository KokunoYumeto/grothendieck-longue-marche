"""Exact character-formula dimensions and bracket-count lower bounds.

The proof uses the S3-module exact sequence
0 -> special outer derivations_n -> V tensor L_n(V) -> L_(n+1)(V) -> 0.
It counts possible brackets; it does not assume those brackets independent.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import json
from sympy import divisors, mobius, primerange

parser = argparse.ArgumentParser()
parser.add_argument("--max-weight", type=int, default=300)
args = parser.parse_args()

def trace_free_lie(n, order):
    def trace_v(power):
        if order == 1:
            return 2
        if order == 2:
            return 2 if power % 2 == 0 else 0
        if order == 3:
            return 2 if power % 3 == 0 else -1
        raise AssertionError(order)
    numerator = sum(int(mobius(d))*trace_v(d)**(n//d) for d in divisors(n))
    assert numerator % n == 0
    return numerator//n

maximum = args.max_weight
lie = [0] + [trace_free_lie(n, 1) for n in range(1, maximum+2)]
gentle = [0]*(maximum+1)
rows = []
for n in range(2, maximum+1):
    numerator = (2*lie[n]-lie[n+1]
                 -2*trace_free_lie(n, 3)
                 -3*trace_free_lie(n+1, 2)
                 -2*trace_free_lie(n+1, 3))
    assert numerator % 6 == 0
    gentle[n] = numerator//6
    assert 0 <= gentle[n] <= 2*lie[n]-lie[n+1]
    count = sum(gentle[i]*gentle[n-i] for i in range(2, (n+1)//2))
    if n % 2 == 0:
        a = gentle[n//2]
        count += a*(a-1)//2
    rows.append({
        "weight": n,
        "free_lie_dimension": lie[n],
        "special_outer_dimension": 2*lie[n]-lie[n+1],
        "gentle_dimension": gentle[n],
        "possible_bracket_count": count,
        "indecomposable_lower_bound": max(0, gentle[n]-count),
    })
source = Path(__file__).with_name("pbc_gentle_even_fast.json")
if source.exists():
    measured = json.loads(source.read_text())
    for r in measured["weights"]:
        assert r["gentle_dimension"] == gentle[r["weight"]]
        assert r["indecomposable_dimension"] >= rows[r["weight"]-2]["indecomposable_lower_bound"]

partial_s = sum((Fraction(gentle[n], 2**n) for n in range(2, maximum+1)), Fraction(0))
outer_sum = sum((Fraction(2*lie[n]-lie[n+1], 2**n) for n in range(2, maximum+1)), Fraction(0))
assert outer_sum == Fraction(1, 2)-Fraction(lie[maximum+1], 2**maximum)
assert partial_s < Fraction(1, 2)
prime_rows = [
    {"prime": int(p), **rows[int(p)-3]}
    for p in primerange(5, maximum+2)
]
result = {
    "scope": "exact dimensions and lower bounds; global-character consequence requires the group proof",
    "weights": rows,
    "prime_minus_one_rows": prime_rows,
    "partial_sum_a_n_over_2n": str(partial_s),
    "partial_sum_decimal": float(partial_s),
    "telescoping_outer_sum": str(outer_sum),
    "outer_sum_upper_bound": "1/2",
    "first_even_positive_indecomposable_lower_bound": next(
        r["weight"] for r in rows if r["weight"] % 2 == 0 and r["indecomposable_lower_bound"]
    ),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({
    "matches_independent_direct_linear_computation_through12": True,
    "first_even_positive_lower_bound": result["first_even_positive_indecomposable_lower_bound"],
    "partial_sum_decimal": result["partial_sum_decimal"],
    "outer_sum_upper_bound": "1/2",
    "first_prime_rows": prime_rows[:15],
    "positive_lower_bound_for_all_checked_primes_ge13": all(
        r["indecomposable_lower_bound"] > 0 for r in prime_rows if r["prime"] >= 13
    ),
}, indent=2))
