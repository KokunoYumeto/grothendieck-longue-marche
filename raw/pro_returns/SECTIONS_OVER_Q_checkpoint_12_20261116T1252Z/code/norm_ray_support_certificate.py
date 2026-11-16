"""Exact finite arithmetic identities in the A.99 divisor repair."""
from math import gcd

inverse_checks = 0
weighted_checks = 0
for ell in [3, 5, 7, 11]:
    for r in range(1, 6):
        modulus = ell ** r
        for d0 in range(1, 32):
            if gcd(d0, ell) != 1:
                continue
            d = 2 * d0
            t = pow(d, -1, modulus)
            assert (1 - t * d) % modulus == 0
            assert gcd(d, ell) == 1
            inverse_checks += 1
            for weights in [(1, 1), (1, 2), (2, 3), (1, 3, 6)]:
                for i in range(len(weights)):
                    for j in range(i + 1, len(weights)):
                        aux = [0] * len(weights)
                        aux[i] = weights[j]
                        aux[j] = -weights[i]
                        repaired_aux = [(1-t*d) * x for x in aux]
                        assert sum(a*w for a, w in zip(aux, weights)) == 0
                        assert sum(a*w for a, w in zip(repaired_aux, weights)) == 0
                        assert all(x % modulus == 0 for x in repaired_aux)
                        # A permitted completely split prime has all weights one.
                        allowed = [t*d, -t*d]
                        assert sum(allowed) == 0
                        weighted_checks += 1

ray_checks = 0
for p in [3, 5, 7, 11, 13]:
    for exponent in range(1, 6):
        ray_modulus = p ** exponent
        for coefficient in range(-5, 6):
            u0 = 1 + coefficient * ray_modulus
            assert u0*u0 % ray_modulus == 1 % ray_modulus
            ray_checks += 1
for old_norm in [-1, 1]:
    assert old_norm**2 == 1

print(f"Prime-to-ell inverse-exponent identities: {inverse_checks}")
print(f"Weighted divisor repair and support identities: {weighted_checks}")
print(f"Ray-congruence squaring identities: {ray_checks}")
print("Both possible rational unit norms become exactly one after squaring.")
print("All A.99 finite identities passed; no lower-field norm preservation is asserted.")
