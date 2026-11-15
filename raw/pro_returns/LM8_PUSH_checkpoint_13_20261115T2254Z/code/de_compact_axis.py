#!/usr/bin/env python3
"""Exact finite certificates for D75's actual affine axis quotient.

This does not replace the proof of continuous duality or inverse limits.
It checks the finite orbit and translation-defect calculation, and the
exact 5-adic log ratio used in the finite-support infinite-factor example.
"""
from collections import deque
from fractions import Fraction
from pathlib import Path
import json


def valuation(n, p=5):
    if n == 0:
        return 10**9
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def determinant(a):
    a = [[Fraction(x) for x in row] for row in a]
    ans = Fraction(1)
    for i in range(len(a)):
        k = next(j for j in range(i, len(a)) if a[j][i])
        if i != k:
            a[i], a[k] = a[k], a[i]
            ans = -ans
        p = a[i][i]
        ans *= p
        for j in range(i+1, len(a)):
            q = a[j][i]/p
            for k in range(i, len(a)):
                a[j][k] -= q*a[i][k]
    return ans


rows = []
for depth in range(6):
    modulus = 5**(depth+1)
    translation = 5**depth
    seen = set()
    orbits = []
    for start in range(modulus):
        if start in seen:
            continue
        queue = deque([start])
        seen.add(start)
        orbit = []
        while queue:
            z = queue.popleft()
            orbit.append(z)
            for w in ((z+translation) % modulus, 2*z % modulus):
                if w not in seen:
                    seen.add(w)
                    queue.append(w)
        labels = {min(valuation(z), depth) for z in orbit}
        assert len(labels) == 1
        orbits.append((next(iter(labels)), len(orbit)))
    assert len(orbits) == depth+1
    # The j-th ball function has translation-one difference 1 at
    # z=5**i-1 exactly for j<=i, and difference 0 at z=1.
    defects = []
    for i in range(1, depth+1):
        z = 5**i-1
        row = []
        for j in range(1, depth+1):
            f = lambda x: int(x % (5**j) == 0)
            assert f(2)-f(1) == 0
            row.append(f(z+1)-f(z))
        defects.append(row)
    det = determinant(defects)
    assert det == 1
    rows.append({
        "depth": depth,
        "modulus": modulus,
        "orbit_sizes_by_valuation": sorted(orbits),
        "invariant_function_rank_mod_constants": depth,
        "translation_one_defect_matrix": defects,
        "defect_determinant": int(det),
    })


precision = 20
terms = 2*(precision+2)


def log_sum(x):
    return sum((Fraction((-1)**(m+1)*x**m, m)
                for m in range(1, terms+1)), Fraction(0))


# Tail term has valuation >= m-v5(m) >= m/2 for m>=2.
# For m>terms this exceeds precision+2. Both logs have valuation 1,
# so dividing loses only one digit; the reported ratio has >=20 digits.
log16 = log_sum(15)
log81 = log_sum(80)
ratio = log16/log81
assert valuation(ratio.numerator) == valuation(ratio.denominator) == 0
modulus = 5**precision
c = ratio.numerator*pow(ratio.denominator, -1, modulus) % modulus
assert c % 5 == 3
assert valuation(log16.numerator)-valuation(log16.denominator) == 1
assert valuation(log81.numerator)-valuation(log81.denominator) == 1

prime_examples = []
for depth in range(1, 6):
    step = 5**(depth+1)
    k = 1
    while not (k % 5 and prime(1+k*step)):
        k += 1
    q = 1+k*step
    assert valuation(q-1) == depth+1
    prime_examples.append({"q": q, "local_depth": depth,
                           "split_compact_factor_rank": depth})

result = {
    "status": "PASS",
    "scope": "Finite affine axis orbit and mass-functional certificates only; continuous global duality is proved in D75.",
    "affine_orbits": rows,
    "log_ratio": {
        "definition": "log(16)/log(81)",
        "precision_power_of_5": precision,
        "residue": c,
        "modulus": modulus,
        "terms_in_each_log": terms,
        "tail_bound": "For m>44, v5(x^m/m)>=m/2>22; ratio loses at most one digit.",
        "residue_mod_5": c % 5,
    },
    "prime_examples": prime_examples,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
