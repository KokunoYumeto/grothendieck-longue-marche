"""Finite exact part of the uniform p>=13 character-rank bound.

The n>=1000 tail is proved analytically in the accompanying note.
This independent sieve implementation checks every even n from12 to998
and compares its exact dimensions with the previous formula through300.
"""
from fractions import Fraction
from pathlib import Path
import json

MAXIMUM = 1000
mu = [1]*(MAXIMUM+2)
is_prime = [True]*(MAXIMUM+2)
is_prime[0] = is_prime[1] = False
for p in range(2, MAXIMUM+2):
    if not is_prime[p]:
        continue
    for multiple in range(p, MAXIMUM+2, p):
        mu[multiple] *= -1
        if multiple > p:
            is_prime[multiple] = False
    for multiple in range(p*p, MAXIMUM+2, p*p):
        mu[multiple] = 0

traces = [[0]*(MAXIMUM+2) for _ in range(3)]
for d in range(1, MAXIMUM+2):
    if not mu[d]:
        continue
    values = (2, 2 if d % 2 == 0 else 0,
              2 if d % 3 == 0 else -1)
    for n in range(d, MAXIMUM+2, d):
        for j, value in enumerate(values):
            traces[j][n] += mu[d]*value**(n//d)
for j in range(3):
    for n in range(1, MAXIMUM+2):
        assert traces[j][n] % n == 0
        traces[j][n] //= n

a = [0]*(MAXIMUM+1)
b = [0]*(MAXIMUM+1)
for n in range(2, MAXIMUM+1):
    value = (2*traces[0][n]-traces[0][n+1]-2*traces[2][n]
             -3*traces[1][n+1]-2*traces[2][n+1])
    assert value % 6 == 0
    a[n] = value//6
    b[n] = sum(a[i]*a[n-i] for i in range(2, (n+1)//2))
    if n % 2 == 0:
        b[n] += a[n//2]*(a[n//2]-1)//2

previous = json.loads(Path(__file__).with_name(
    "pbc_gentle_dimension_formula.json").read_text())
for row in previous["weights"]:
    n = row["weight"]
    assert a[n] == row["gentle_dimension"]
    assert b[n] == row["possible_bracket_count"]

checked = [[n, a[n], b[n], a[n]-b[n]] for n in range(12, 1000, 2)]
assert all(row[3] > 0 for row in checked)
assert 300*100**2 <= 2**50
assert 101**4 < 2*100**4
assert Fraction(100,303)-Fraction(1,100) > Fraction(8,25)
assert Fraction(1,3)+Fraction(1,100) < Fraction(7,20)
tail_bound = Fraction(875,648)*Fraction(7,16)+Fraction(35,8)*Fraction(7,2000)
assert tail_bound < 1
result = {
    "scope": "finite exact verification plus rational constants of the analytic tail bound",
    "every_even_weight12_through998_has_positive_lower_bound": True,
    "checked_even_rows": checked,
    "independent_sieve_agrees_with_previous_formula_through300": True,
    "tail_cutoff": 1000,
    "tail_upper_bound_for_b_n_over_a_n": str(tail_bound),
    "tail_bound_strictly_below_one": True,
    "analytic_tail_proof_required": True,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({
    "checked_even_weights": len(checked),
    "first": checked[0],
    "last_weight": checked[-1][0],
    "all_positive": True,
    "independent_formula_comparison": True,
    "tail_cutoff": 1000,
    "tail_upper_bound": str(tail_bound),
    "tail_bound_decimal": float(tail_bound),
}, indent=2))
