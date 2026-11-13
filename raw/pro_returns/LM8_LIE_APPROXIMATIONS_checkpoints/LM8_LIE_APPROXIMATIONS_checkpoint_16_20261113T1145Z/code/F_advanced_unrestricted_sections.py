#!/usr/bin/env python3
"""Exact finite certificates for the genuine lim^1 cup obstruction in F.21.

The infinite sequence and obstruction are proved in F.21. This program
certifies the displayed first eight primes, their primitive roots, their
discrete logarithms, and the finite tame vanishings. It does not infer an
infinite theorem from these finitely many certificates.
"""
from pathlib import Path
from math import gcd, isqrt
import json


def trial_factors(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def trial_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def vp(n, p):
    if n == 0:
        return None
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


# The full discrete logarithms are recovered by a short exact BSGS search.
# Primality is then independently certified by an element of order q-1.
def discrete_log(g, a, q):
    m = isqrt(q - 1) + 1
    baby = {}
    x = 1
    for j in range(m):
        baby.setdefault(x, j)
        x = x * g % q
    step = pow(pow(g, m, q), -1, q)
    x = a % q
    for i in range(m + 1):
        if x in baby:
            answer = i * m + baby[x]
            assert pow(g, answer, q) == a % q
            return answer % (q - 1)
        x = x * step % q
    raise ValueError((g, a, q))


prime_root_pairs = [
    (11, 2), (101, 2), (751, 3), (13751, 11),
    (37501, 2), (62501, 2), (937501, 2), (9375001, 7),
]
rows = []
for n, (q, g) in enumerate(prime_root_pairs, 1):
    factors = trial_factors(q - 1)
    assert all(trial_prime(r) for r in factors)
    product = 1
    for r, e in factors.items():
        product *= r ** e
    assert product == q - 1
    assert gcd(g, q) == 1
    assert pow(g, q - 1, q) == 1
    order_checks = {str(r): pow(g, (q - 1) // r, q) for r in factors}
    assert all(v != 1 for v in order_checks.values())
    # Exact order q-1 in (Z/q)^* forces phi(q)>=q-1, hence q is prime.
    assert vp(q - 1, 5) == n
    fifth_residue = pow(5, (q - 1) // 5, q)
    assert fifth_residue != 1
    full_log = discrete_log(g, 5, q)
    log5 = full_log % (5 ** n)
    assert log5 % 5 != 0
    alpha5 = 1
    beta_q = 5 ** n
    tame_lift = beta_q * log5
    divided = tame_lift // (5 ** n)
    assert divided == log5
    finite_checks = []
    for r in range(1, 13):
        modulus = 5 ** min(n, r)
        assert tame_lift % modulus == 0
        finite_checks.append({'r': r, 'obstruction_modulus': modulus,
                              'obstruction_residue': 0})
    row = dict(
        n=n, q=q, primitive_root=g, factorization_q_minus_1=factors,
        primitive_order_checks=order_checks, primality_certificate='exact order q-1',
        full_discrete_log_5=full_log, logarithm_mod_5_power=log5,
        fifth_power_residue=fifth_residue, alpha_5=alpha5, beta_q=beta_q,
        tame_coordinate=tame_lift, divided_coordinate=divided,
        v5_beta=n, v5_tame=n, v5_divided=0,
        finite_obstruction_checks=finite_checks,
    )
    rows.append(row)
    print(f'n={n}, q={q}, g={g}, log_5={log5} mod {5**n}, '
          f'5^((q-1)/5)={fifth_residue}, divided valuation=0')

result = {
    'statement': 'F.21',
    'status': 'Exact finite certificates completed; the infinite assertion is proved in the manuscript.',
    'coefficient_prime': 5,
    'scope': {'prime_examples': 8, 'finite_coefficient_levels_checked': list(range(1, 13)),
              'infinite_existence': 'Chebotarev in Q(zeta_(5^(n+1)),5^(1/5)); see F.21.'},
    'rows': rows,
    'global_example': {
        'alpha': 'alpha_5=1, all other coordinates zero',
        'beta': 'beta_qn=5^n for a sequence satisfying e_qn=n and fifth residue of5 nontrivial',
        'finite_obstructions': 'All zero, since T_qn=5^n L_qn(5).',
        'integral_obstruction': 'Nonzero: the divided coordinates L_qn(5) are units and do not tend to zero.',
        'warning': 'This is not a compatible family of finite section classes. Each individual finite fibre is nonempty.',
    },
    'completion_model': {
        'H2': 'c0(I,Z5)/diag(5^e_q)c0(I,Z5), actual image without closure',
        'lim1': '{a in product Z5: diag(5^e_q)a in c0}/c0',
        'cup': 'T_q=beta_q sum_(p!=q)alpha_p L_q(p)-alpha_q sum_(p!=q)beta_p L_q(p)',
        'lift_criterion': 'Every T_q/5^e_q is integral and the divided sequence belongs to c0.',
    },
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(f'Wrote {target.name}; all exact checks passed.')
