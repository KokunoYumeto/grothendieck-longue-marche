"""Exact finite-module controls for the abelian norm-free criterion.

No geometric realization is asserted. The first module has a nonzero
primitive component for every prime-degree quotient but none for its
cyclic order-nine quotients. A repaired module and a nonconstant-deck
Frobenius example check the converse and the orbit-sum construction.
"""
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def multiply(a, b, modulus):
    n = modulus.bit_length() - 1
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & (1 << n):
            a ^= modulus
        b >>= 1
    return result


def power(a, n, modulus):
    result = 1
    while n:
        if n & 1:
            result = multiply(result, a, modulus)
        a = multiply(a, a, modulus)
        n >>= 1
    return result


F4, F64 = 0b111, 0b1000011
assert all(power(a, 3, F4) == 1 for a in range(1, 4))
assert all(power(a, 63, F64) == 1 for a in range(1, 64))
omega = 2
zeta = power(2, 7, F64)
assert power(zeta, 9, F64) == 1 and power(zeta, 3, F64) != 1


def groups(n, m):
    elements = tuple(product(range(n), range(m)))
    def add(a, b):
        return ((a[0] + b[0]) % n, (a[1] + b[1]) % m)
    subgroups = {frozenset({(0, 0)})}
    queue = list(subgroups)
    for H in queue:
        for g in elements:
            generated = set(H)
            multiple = g
            while multiple not in H:
                generated.update(add(h, multiple) for h in H)
                multiple = add(multiple, g)
            K = frozenset(generated)
            if K not in subgroups:
                subgroups.add(K)
                queue.append(K)
    return elements, sorted(subgroups, key=lambda H: (len(H), sorted(H)))


def action(g, v, components):
    return tuple(multiply(a, power(root, (r*g[0] + s*g[1]) % order, mod), mod)
                 for a, (mod, root, order, r, s) in zip(v, components))


def norm(H, v, components):
    value = [0] * len(v)
    for h in H:
        for i, a in enumerate(action(h, v, components)):
            value[i] ^= a
    return tuple(value)


def stabilizer(A, v, components):
    return frozenset(g for g in A if action(g, v, components) == v)


def kernel(A, component):
    _, _, order, r, s = component
    return frozenset(g for g in A if (r*g[0] + s*g[1]) % order == 0)


def records(A, subgroups, v, components):
    ans = []
    for H in subgroups:
        value = norm(H, v, components)
        stab = stabilizer(A, value, components)
        ans.append({"H": sorted(H), "index": len(A)//len(H),
                    "norm": value, "stabilizer": sorted(stab), "free": stab == H})
    return ans


# C9 x C3: all four cubic quotients present, all three primitive-nine
# quotient components absent.
A, subgroups = groups(9, 3)
assert len(A) == 27 and len(subgroups) == 10
cubic = [(F4, omega, 3, r, s) for r, s in ((1, 0), (0, 1), (1, 1), (1, 2))]
cubic_H = [H for H in subgroups if len(A)//len(H) == 3]
assert len(cubic_H) == 4 and {kernel(A, c) for c in cubic} == set(cubic_H)
vectors = list(product(range(4), repeat=4))
prime_free = [v for v in vectors if all(stabilizer(A, norm(H, v, cubic), cubic) == H for H in cubic_H)]
all_free = [v for v in prime_free if all(stabilizer(A, norm(H, v, cubic), cubic) == H for H in subgroups)]
assert len(prime_free) == 81 and not all_free
common_kernel = frozenset.intersection(*(kernel(A, c) for c in cubic))
assert common_kernel == frozenset({(0, 0), (3, 0), (6, 0)})

primitive9 = [(F64, zeta, 9, 1, 3*s) for s in range(3)]
repaired = cubic + primitive9
meet_irreducibles = {kernel(A, c) for c in repaired}
assert len(meet_irreducibles) == 7
assert sorted(len(A)//len(H) for H in meet_irreducibles) == [3, 3, 3, 3, 9, 9, 9]
for H in subgroups:
    strict = [K for K in subgroups if H < K]
    intersection = frozenset(A) if not strict else frozenset.intersection(*strict)
    assert (intersection != H and H != frozenset(A)) == (H in meet_irreducibles)
fixed = (1,)*7
repaired_records = records(A, subgroups, fixed, repaired)
assert all(r["free"] for r in repaired_records)

# Nonconstant deck action on C3 x C3. Frobenius swaps generators.
# It swaps the first two character components and applies squaring
# to the fourth, as required by conjugation of its character.
B, sub_B = groups(3, 3)
assert len(B) == 9 and len(sub_B) == 6
components_B = cubic
def frobenius(v):
    return v[1], v[0], v[2], multiply(v[3], v[3], F4)
def sigma(g):
    return g[1], g[0]
assert all(frobenius(action(g, v, components_B)) == action(sigma(g), frobenius(v), components_B)
           for g in B for v in vectors)
invariants = [v for v in vectors if frobenius(v) == v]
free_invariants = [v for v in invariants if all(stabilizer(B, norm(H, v, components_B), components_B) == H for H in sub_B)]
assert len(invariants) == 32 and len(free_invariants) == 9
assert (1, 1, 1, 1) in free_invariants
kernel_orbits = []
unseen = set(kernel(B, c) for c in components_B)
while unseen:
    H = next(iter(unseen)); orbit = []; current = H
    while current not in orbit:
        orbit.append(current)
        current = frozenset(sigma(g) for g in current)
    assert current == H
    unseen.difference_update(orbit)
    kernel_orbits.append([sorted(K) for K in orbit])
assert sorted(map(len, kernel_orbits)) == [1, 1, 2]
# No division by the orbit length two: distinct packets prevent
# cancellation even in characteristic two.
v = (1, 0, 0, 0)
orbit_sum = tuple(a ^ b for a, b in zip(v, frobenius(v)))
assert orbit_sum == (1, 1, 0, 0) and frobenius(orbit_sum) == orbit_sum

result = {
    "verified": True,
    "scope": "Exact finite modules only; no assertion of Jacobian realization",
    "constant_example": {
        "group": "C9 x C3", "characteristic": 2,
        "module": "F4^4 with characters (1,0),(0,1),(1,1),(1,2) modulo3",
        "all_subgroups": len(subgroups), "prime_quotient_kernels": len(cubic_H),
        "vectors_free_at_every_prime_quotient": len(prime_free),
        "vectors_free_at_every_quotient": len(all_free),
        "common_stabilizer": sorted(common_kernel),
        "missing_primitive_nine_kernels": [sorted(kernel(A, c)) for c in primitive9],
    },
    "repaired_example": {
        "module": "F4^4 plus F64^3, with primitive-nine characters a+3jb for j=0,1,2",
        "F64_modulus_bits": F64, "primitive_ninth_root_bits": zeta,
        "maximal_support_vector": fixed,
        "all_level_free_vector_count": 3**4 * 63**3,
        "all_norm_tests": repaired_records,
    },
    "nonconstant_example": {
        "group": "C3 x C3", "characteristic": 2,
        "Frobenius_on_group": "(a,b) -> (b,a)",
        "Frobenius_on_module": "(u,v,w,z) -> (v,u,w,z^2)",
        "fixed_vector_count": len(invariants),
        "all_level_free_fixed_vector_count": len(free_invariants),
        "kernel_orbits": kernel_orbits,
        "orbit_sum_in_characteristic_two": orbit_sum,
        "all_norm_tests": records(B, sub_B, (1,1,1,1), components_B),
    },
}
(ROOT / "criterion_abelian_norm.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"verified": True,
    "C9xC3_prime_quotient_free": len(prime_free),
    "C9xC3_all_quotient_free": len(all_free),
    "repaired_all_quotient_free_count": 3**4 * 63**3,
    "semilinear_fixed_count": len(invariants),
    "semilinear_all_quotient_free_count": len(free_invariants)}, indent=2))
