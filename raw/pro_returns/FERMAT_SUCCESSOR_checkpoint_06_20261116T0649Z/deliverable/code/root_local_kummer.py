"""Exact finite-level checks for D.4, without numerical p-adic logarithms.

The proof is in the paper.  Here the radical criterion is tested directly
in finite unit groups and compared to the stated Kummer-image annihilator.
"""
from pathlib import Path
from itertools import product
import json

OUT = Path(__file__).resolve().parent

def valuation(a, p):
    assert a
    k = 0
    while a % p == 0:
        a //= p
        k += 1
    return k

def image_exponent(p, ell):
    if p == ell:
        return int(ell == 2)
    if ell == 2:
        return valuation(p*p-1, 2)-2
    return valuation(pow(p, ell-1)-1, ell)-1

rows = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 31, 97]
for ell in [2, 3, 5, 7]:
    for n in [1, 2, 3]:
        N = ell**n
        modulus = ell**(n+1)
        exponent = N if ell != 2 else N//2
        powers = {pow(u, exponent, modulus)
                  for u in range(1, modulus) if u % ell}
        if ell == 2:
            powers |= {(-u) % modulus for u in powers}
        for p in primes:
            k = image_exponent(p, ell)
            annihilator = []
            for e in range(N):
                v = e if p == ell else 0
                unit = 1 if p == ell else pow(p, e, modulus)
                actual = v % exponent == 0 and unit in powers
                expected = (e * ell**k) % N == 0
                assert actual == expected, (ell, n, p, e)
                if actual:
                    annihilator.append(e)
            rows.append(dict(ell=ell, n=n, p=p, image_exponent=k,
                             annihilator_size=len(annihilator),
                             image_size=N//len(annihilator)))

joint = []
for ell, n in [(2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (5, 1)]:
    ps = [2, 3, 5]
    N = ell**n
    modulus = ell**(n+2 if ell == 2 else n+1)
    basis = 5 if ell == 2 else 1+ell
    logs = {pow(basis, d, modulus): d for d in range(N)}
    v = [int(p == ell) for p in ps]
    d = []
    for p in ps:
        if p == ell:
            d.append(0)
        elif ell == 2:
            sign = 1 if p % 4 == 1 else -1
            d.append(logs[(sign*p) % modulus])
        else:
            omega = pow(p, N, modulus)
            d.append(logs[(p*pow(omega, -1, modulus)) % modulus])
    factor = 2 if ell == 2 else 1
    image = {tuple(factor*(a*v[i]+b*d[i]) % N for i in range(3))
             for a, b in product(range(N), repeat=2)}
    radical_exponent = N if ell != 2 else N//2
    radical_modulus = ell**(n+1)
    powers = {pow(u, radical_exponent, radical_modulus)
              for u in range(1, radical_modulus) if u % ell}
    if ell == 2:
        powers |= {(-u) % radical_modulus for u in powers}
    annihilator = []
    for e in product(range(N), repeat=3):
        val = sum(v[i]*e[i] for i in range(3))
        unit = 1
        for i in range(3):
            if ps[i] != ell:
                unit = unit*pow(ps[i], e[i], radical_modulus) % radical_modulus
        actual = val % radical_exponent == 0 and unit in powers
        expected = all(sum(e[i]*h[i] for i in range(3)) % N == 0
                       for h in image)
        assert actual == expected, (ell, n, e)
        if actual:
            annihilator.append(e)
    assert len(image)*len(annihilator) == N**3
    joint.append(dict(ell=ell, n=n, primes=ps, valuation_vector=v,
                      logarithm_vector_mod_N=d, common_factor=factor,
                      image_size=len(image), ambient_size=N**3,
                      annihilator_size=len(annihilator)))

special = [dict(p=p, ell=ell, image_exponent=image_exponent(p, ell))
           for p, ell in [(2, 2), (3, 2), (7, 2), (17, 2),
                          (3, 11), (2, 1093), (2, 3511)]]
result = dict(status="PASS", single_checks=rows,
              joint_checks=joint, exceptional_examples=special)
(OUT/'root_local_kummer.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(dict(status="PASS", single_cases=len(rows),
                     joint_checks=joint, exceptional_examples=special), indent=2))
