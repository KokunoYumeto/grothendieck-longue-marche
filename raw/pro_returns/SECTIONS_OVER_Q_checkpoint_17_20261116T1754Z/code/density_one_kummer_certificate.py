"""Finite exact certificate for the finite-level warning in A.76.

The density-one theorem uses Chebotarev and the doubled-exponent proof,
not a numerical extrapolation from these tests.
"""
from pathlib import Path
from sympy import Symbol, expand, primerange, I


z = Symbol('z')
assert expand((z*z - 2)*(z*z + 2)*(z*z + 2*z + 2)*(z*z - 2*z + 2)) == z**8 - 16
assert expand((1+I)**8) == 16
assert 4 % 8 != 0

# Roots are sqrt(2)*zeta_8^k.  The element u in (Z/8)^* sends
# sqrt(2) to (-1)^eps sqrt(2), eps=(u^2-1)/8 modulo2.
fixed = {}
for u in (1, 3, 5, 7):
    eps = ((u*u - 1)//8) % 2
    permutation = [(u*k + 4*eps) % 8 for k in range(8)]
    assert sorted(permutation) == list(range(8))
    fixed[u] = [k for k in range(8) if permutation[k] == k]
    assert fixed[u]
assert [len(fixed[u]) for u in (1, 3, 5, 7)] == [8, 2, 4, 2]

tested = 0
for p in primerange(3, 10001):
    symbols = [pow(a % p, (p-1)//2, p) for a in (2, -2, -1)]
    assert all(s in (1, p-1) for s in symbols)
    assert symbols[0]*symbols[1]*symbols[2] % p == 1
    assert 1 in symbols
    # Independent finite-field nth-power criterion, without root selection.
    from math import gcd
    assert pow(16 % p, (p-1)//gcd(8, p-1), p) == 1
    tested += 1

out = (
    'A.76 finite certificate: all checks passed.\n'
    'Exact factorization ofZ^8-16 and identity(1+i)^8=16 verified.\n'
    f'Fixed-root counts foru=1,3,5,7 inGal(Q(mu8)/Q): {[len(fixed[u]) for u in (1,3,5,7)]}.\n'
    f'Odd primes tested through10000: {tested}; square-cover and eighth-power tests all pass.\n'
    'Valuation4 is not divisible by8, giving the exact dyadic obstruction.\n'
    'The universal odd-prime assertion and density-one injectivity are proved in the text.\n'
)
Path(__file__).with_name('density_one_kummer_certificate_output.txt').write_text(out)
print(out, end='')
