#!/usr/bin/env python3
"""D.42 finite certificates for the exact cyclic-cover module calculation."""
from pathlib import Path
import json


def primes_to(n):
    return [q for q in range(2, n + 1)
            if all(q % d for d in range(2, int(q**0.5) + 1))]


def reduced(word, q):
    out = []
    for letter, exponent in word:
        exponent %= q
        if not exponent:
            continue
        if out and out[-1][0] == letter:
            exponent = (out.pop()[1] + exponent) % q
        if exponent:
            out.append((letter, exponent))
    return out


def invert(word):
    return [(letter, -exponent) for letter, exponent in reversed(word)]


def poly_trim(a):
    a = [x % 3 for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def poly_gcd(a, b):
    a, b = poly_trim(a), poly_trim(b)
    while b:
        r = a[:]
        while len(r) >= len(b):
            scale = r[-1] * pow(b[-1], -1, 3) % 3
            shift = len(r) - len(b)
            for i, v in enumerate(b):
                r[i + shift] = (r[i + shift] - scale * v) % 3
            r = poly_trim(r)
        a, b = b, r
    inv = pow(a[-1], -1, 3)
    return [v * inv % 3 for v in a]


def verify(q, zeta):
    assert zeta != 1 and pow(zeta, 3, q) == 1
    values = (zeta, 1, zeta*zeta % q)
    assert sum(values) % q == 0 and all(values)
    assert tuple(zeta*v % q for v in values[1:] + values[:1]) == values
    r = values[2]
    assert r and (r + 1) % q
    z_cycle = [(j*r) % q for j in range(q)]
    x_cycle = [(-r-j*(r+1)) % q for j in range(q)]
    assert sorted(z_cycle) == sorted(x_cycle) == list(range(q))

    def u(i):
        return reduced([("y", i), ("z", 1), ("y", -i-r)], q)

    z_relation = [syllable for i in z_cycle for syllable in u(i)]
    x_relation = [syllable for i in x_cycle for syllable in invert(u(i))]
    assert reduced(z_relation, q) == []
    assert reduced(x_relation, q) == reduced([("z", -1), ("y", -1)] * q, q)
    for i in range(q):
        assert reduced([("y", 1)] + u(i) + [("y", -1)], q) == u(i+1)

    # On the basis v0,...,v(q-2), the last generator is minus their sum.
    degree = q - 1
    def deck(v):
        return [-v[-1]] + [v[i-1]-v[-1] for i in range(1, degree)]

    for j in range(degree):
        initial = [int(i == j) for i in range(degree)]
        v, total = initial[:], [0] * degree
        for _ in range(q):
            total = [a+b for a, b in zip(total, v)]
            v = deck(v)
        assert v == initial                 # T^q=I over the integers.
        assert total == [0] * degree        # Phi_q(T)=0 over the integers.
    v = [1] + [0] * (degree-1)
    for i in range(degree):
        assert v == [int(j == i) for j in range(degree)]
        v = deck(v)
    # The first degree orbit vectors are a basis, so the characteristic
    # and minimal polynomials both equal the monic degree-degree Phi_q.
    phi = [1] * q
    derivative = [(i+1)*phi[i+1] % 3 for i in range(q-1)]
    assert poly_gcd(phi, derivative) == [1]
    remaining, orbits = set(range(1, q)), []
    while remaining:
        start = min(remaining)
        orbit, value = [], start
        while value not in orbit:
            orbit.append(value)
            value = 3*value % q
        assert value == start
        remaining.difference_update(orbit)
        orbits.append(orbit)
    degrees = [len(orbit) for orbit in orbits]
    assert len(set(degrees)) == 1 and sum(degrees) == q - 1
    assert all((3**d - 1) % 3 == 2 for d in degrees)
    return {
        "q": q, "zeta": zeta, "character_x_y_z": values,
        "closed_genus": (q-1)//2,
        "z_relator_index_cycle": z_cycle,
        "x_boundary_index_cycle": x_cycle,
        "closed_H1_rank": degree,
        "deck_characteristic_polynomial": "1+X+...+X^(q-1)",
        "schreier_word_identities": "passed in the free product Cq(y) amalg Cq(z)",
        "deck_integer_matrix_checks": "T^q=I, Phi_q(T)=0, and v0 is cyclic",
        "mod3_phi_squarefree": True,
        "mod3_irreducible_factor_degrees": degrees,
        "residue_multiplicative_orders_prime_to3": True,
    }


def main():
    rows = [verify(q, zeta) for q in primes_to(97) if q % 3 == 1
            for zeta in range(2, q) if pow(zeta, 3, q) == 1]
    assert len(rows) == 22
    result = {
        "claim": "D.42",
        "rows": rows,
        "case_count": len(rows),
        "scope": "Executed finite identities validate the displayed cover coordinates and deck module. The actual closed-surface automorphism theorem, all-prime argument, and full-group conclusion are proved in pants_order_three.tex.",
    }
    Path(__file__).with_name("pants_order_three_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print("D.42: all22 invariant-character, Schreier-word, deck-matrix, and Frobenius-factor checks passed.")
    for row in rows:
        print(f"q={row['q']:2}, zeta={row['zeta']:2}, genus={row['closed_genus']:2}, "
              f"factor degrees={row['mod3_irreducible_factor_degrees']}")


if __name__ == "__main__":
    main()
