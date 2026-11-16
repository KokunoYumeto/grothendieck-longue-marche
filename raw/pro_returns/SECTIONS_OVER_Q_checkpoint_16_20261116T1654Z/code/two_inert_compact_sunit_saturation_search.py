"""Independent finite residue search on literal compact S-unit candidates.

This file does not certify their S-support. A full-rank matrix only
certifies independent cube classes of the displayed field elements.
"""
from pathlib import Path
from fractions import Fraction as F
import itertools
import json
import re
import sys
from sympy import primerange

sys.set_int_max_str_digits(0)
base = Path(__file__).resolve().parent
text = (base / "two_inert_compact_units_pari_output.txt").read_text()
units = json.loads((base / "two_inert_relative_unit_repair_certificate_data.json").read_text())["units"]
factors = {}
for i, j, exponent, raw in re.findall(
    r"^SFACTOR (\d+) (\d+) (-?\d+) (\[.*\])$", text, re.M
):
    factors.setdefault(int(i), []).append(
        (int(exponent), tuple(F(s.strip()) for s in raw[1:-1].split(",")))
    )
assert sorted(factors) == list(range(1, 9))
candidate_units = [tuple(F(c) for c in row["candidate"]) for row in units]
radicand = 3 * 649**6


def evaluate(polynomial, value, p):
    out = 0
    for coefficient in reversed(polynomial):
        if coefficient.denominator % p == 0:
            return None
        out = (
            out * value
            + coefficient.numerator * pow(coefficient.denominator, -1, p)
        ) % p
    return out


echelon = {}
retained = []
trials = 0
for p in primerange(2000, 200000):
    if p % 3 != 1:
        continue
    roots = [t for t in range(p) if pow(t, 9, p) == radicand % p]
    if not roots:
        continue
    omega = next(
        pow(u, (p - 1) // 3, p)
        for u in range(2, p)
        if pow(u, (p - 1) // 3, p) != 1
    )
    log = {1: 0, omega: 1, omega * omega % p: 2}
    for t in roots:
        trials += 1
        row = []
        skip = False
        for unit in candidate_units:
            value = evaluate(unit, t, p)
            if value in (None, 0):
                skip = True
                break
            row.append(log[pow(value, (p - 1) // 3, p)])
        if skip:
            continue
        cache = {}
        for i in range(1, 9):
            character = 0
            for exponent, polynomial in factors[i]:
                if exponent % 3 == 0:
                    continue
                if polynomial not in cache:
                    value = evaluate(polynomial, t, p)
                    cache[polynomial] = (
                        None
                        if value in (None, 0)
                        else log[pow(value, (p - 1) // 3, p)]
                    )
                if cache[polynomial] is None:
                    skip = True
                    break
                character += exponent * cache[polynomial]
            if skip:
                break
            row.append(character % 3)
        if skip:
            continue
        reduced = row[:]
        for pivot, old in sorted(echelon.items()):
            multiplier = reduced[pivot]
            reduced = [(a - multiplier * b) % 3 for a, b in zip(reduced, old)]
        pivot = next((i for i, a in enumerate(reduced) if a), None)
        if pivot is None:
            continue
        inverse = pow(reduced[pivot], -1, 3)
        echelon[pivot] = [a * inverse % 3 for a in reduced]
        retained.append({"p": p, "t": t, "omega": omega, "row": row})
        print("RANK", len(echelon), "p", p, "t", t, "row", row, flush=True)
        if len(echelon) == 12:
            break
    if len(echelon) == 12:
        break

result = {
    "radicand": radicand,
    "rank": len(echelon),
    "trial_roots": trials,
    "rows": retained,
    "scope": "Independent cube classes only; S-support needs a separate exact divisor certificate.",
}
(base / "two_inert_compact_sunit_saturation_search_data.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
assert len(echelon) == 12, result
print("PASS: twelve independent cube classes of the literal compact candidates.")
print(result["scope"])
