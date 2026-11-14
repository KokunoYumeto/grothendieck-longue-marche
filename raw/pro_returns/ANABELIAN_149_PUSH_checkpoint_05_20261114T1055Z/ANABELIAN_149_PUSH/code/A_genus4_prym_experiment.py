#!/usr/bin/env python3
"""Exact Mumford and Frobenius certificate for Claim A.29c.

All field and polynomial arithmetic is exact.  The proof reducing geometric
2-primary points to this finite field is in the manuscript.  The full
composition/reduction formulas are documented in the adjacent audit note.
"""

from pathlib import Path
import json


DEGREE = 12
MODULUS = 0x1009
ORDER = (1 << DEGREE) - 1


def bits_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a >> DEGREE:
            a ^= MODULUS
    return result


EXP = [1] * ORDER
LOG = [-1] * (ORDER + 1)
for i in range(1, ORDER):
    EXP[i] = bits_mul(EXP[i - 1], 3)
assert len(set(EXP)) == ORDER
assert bits_mul(EXP[-1], 3) == 1
for i, element in enumerate(EXP):
    LOG[element] = i


def fm(a, b):
    return EXP[(LOG[a] + LOG[b]) % ORDER] if a and b else 0


def fi(a):
    assert a
    return EXP[-LOG[a] % ORDER]


def fp(a, exponent):
    return EXP[LOG[a] * exponent % ORDER] if a else int(exponent == 0)


C = next(x for x in range(ORDER + 1) if fm(x, x) ^ x ^ 1 == 0)


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] ^= value
    for i, value in enumerate(b):
        out[i] ^= value
    return trim(out)


def scale(a, scalar):
    return trim([fm(value, scalar) for value in a])


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] ^= fm(left, right)
    return trim(out)


def div(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    out = [0] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient = fm(a[-1], fi(b[-1]))
        out[shift] ^= coefficient
        for i, value in enumerate(b):
            a[shift + i] ^= fm(value, coefficient)
        a = trim(a)
    return trim(out), a


def exact_div(a, b):
    quotient, remainder = div(a, b)
    assert remainder == [0]
    return quotient


def xgcd(a, b):
    r0, r1 = trim(a), trim(b)
    s0, s1, t0, t1 = [1], [0], [0], [1]
    while r1 != [0]:
        q, r2 = div(r0, r1)
        r0, r1 = r1, r2
        s0, s1 = s1, add(s0, mul(q, s1))
        t0, t1 = t1, add(t0, mul(q, t1))
    leading_inverse = fi(r0[-1])
    result = scale(r0, leading_inverse), scale(s0, leading_inverse), scale(t0, leading_inverse)
    assert add(mul(result[1], a), mul(result[2], b)) == result[0]
    return result


H = [C, 0, 0, 1]
F = add(mul(mul(H, H), H), scale(H, C))
IDENTITY = ([1], [0])


def matrix_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def determinant_bareiss(matrix):
    a = [list(row) for row in matrix]
    sign, previous = 1, 1
    for k in range(len(a) - 1):
        if a[k][k] == 0:
            pivot = next(i for i in range(k + 1, len(a)) if a[i][k])
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        for i in range(k + 1, len(a)):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def prym_orders():
    coefficients = [64, 48, 36, 20, 9, 3]
    companion = [[0] * 6 for _ in range(6)]
    for i in range(5):
        companion[i + 1][i] = 1
    for i, coefficient in enumerate(coefficients):
        companion[i][5] = -coefficient
    powers = [[int(i == j) for j in range(6)] for i in range(6)]
    result = {}
    for r in range(1, 7):
        powers = matrix_mul(powers, companion)
        if r not in (3, 6):
            continue
        difference = [[powers[i][j] - int(i == j) for j in range(6)] for i in range(6)]
        order = determinant_bareiss(difference)
        odd, valuation = order, 0
        while odd % 2 == 0:
            odd //= 2
            valuation += 1
        result[str(r)] = {"order": order, "v2": valuation, "odd_part": odd}
    assert result == {"3": {"order": 291772, "v2": 2, "odd_part": 72943}, "6": {"order": 70459436736, "v2": 6, "odd_part": 1100928699}}
    return result


def check(pair):
    u, v = pair
    assert u[-1] == 1
    assert len(v) < len(u) or u == [1]
    assert div(add(add(mul(v, v), mul(H, v)), F), u)[1] == [0]
    return pair


def reduce_pair(u, v):
    u = scale(u, fi(u[-1]))
    v = div(v, u)[1]
    check((u, v))
    while len(u) - 1 > 4:
        new_u = exact_div(add(add(mul(v, v), mul(H, v)), F), u)
        new_u = scale(new_u, fi(new_u[-1]))
        v = div(add(v, H), new_u)[1]
        u = new_u
        check((u, v))
    if u == [1]:
        v = [0]
    return check((u, v))


def cantor(left, right):
    u1, v1 = left
    u2, v2 = right
    d1, a, b = xgcd(u1, u2)
    d, e, c = xgcd(d1, add(add(v1, v2), H))
    a, b = mul(e, a), mul(e, b)
    u = exact_div(mul(u1, u2), mul(d, d))
    numerator = add(add(mul(mul(a, u1), v2), mul(mul(b, u2), v1)), mul(c, add(mul(v1, v2), F)))
    v = exact_div(numerator, d)
    return reduce_pair(u, v)


def double_hensel(pair):
    u, v = pair
    d, _, inverse_h = xgcd(u, H)
    if d != [1]:
        return None
    quotient = exact_div(add(add(mul(v, v), mul(H, v)), F), u)
    correction = div(mul(quotient, inverse_h), u)[1]
    return reduce_pair(mul(u, u), add(v, mul(u, correction)))


def negate(pair):
    u, v = pair
    return u, div(add(v, H), u)[1]


def point(s, Y):
    return check(([s, 1], [Y]))


def main():
    solutions = {}
    for y in range(ORDER + 1):
        value = fm(y, y) ^ y
        solutions.setdefault(value, []).append(y)
    assert all(len(values) == 2 for values in solutions.values())
    total_points = 1
    tested_orbits = 0
    seen_s = set()
    torsion_orbits = []
    validation_counts = {"cantor_vs_hensel_doublings": 0, "inverse_additions": 0, "three_cycle_sums": 0}
    for s in range(ORDER + 1):
        denominator = fp(s, 3) ^ C
        if denominator == 0:
            ys = [0]  # Y=0 at the normalized finite branch point.
            total_points += 1
        else:
            value = denominator ^ fm(C, fi(denominator))
            ys = [fm(denominator, y) for y in solutions.get(value, [])]
            total_points += len(ys)
        if not ys or s in seen_s:
            continue
        s_orbit = {s, fm(C, s), fm(fm(C, C), s)}
        seen_s.update(s_orbit)
        # Hyperelliptic conjugation changes D to -D, so one y suffices.
        Y = ys[0]
        P, Q = point(s, Y), point(fm(C, s), Y)
        D = cantor(P, negate(Q))
        assert cantor(D, negate(D)) == IDENTITY
        validation_counts["inverse_additions"] += 1
        R = point(fm(fm(C, C), s), Y)
        D1, D2 = cantor(Q, negate(R)), cantor(R, negate(P))
        assert cantor(cantor(D, D1), D2) == IDENTITY
        validation_counts["three_cycle_sums"] += 1
        multiple = D
        exact_power = 0 if D == IDENTITY else None
        for power in range(1, 4):
            doubled = cantor(multiple, multiple)
            independent = double_hensel(multiple)
            if independent is not None:
                assert doubled == independent
                validation_counts["cantor_vs_hensel_doublings"] += 1
            multiple = doubled
            if multiple == IDENTITY and exact_power is None:
                exact_power = power
        tested_orbits += 1
        if multiple == IDENTITY:
            torsion_orbits.append({"s":s,"s_orbit":sorted(s_orbit),"Y":Y,"order_power_of_2":exact_power,"finite_weierstrass":denominator==0,"deck_fixed":s==0})
    assert total_points == 4206
    assert all(row["finite_weierstrass"] or row["deck_fixed"] for row in torsion_orbits)
    result = {
        "claim": "A.29c",
        "status": "exact finite check; the global reduction is proved in the manuscript",
        "field": "F4096, modulus x^12+x^3+1, primitive generator x+1",
        "c": C,
        "curve_h_coefficients_low_to_high": H,
        "curve_f_coefficients_low_to_high": F,
        "total_points_including_infinity": total_points,
        "tested_delta_and_hyperelliptic_orbits": tested_orbits,
        "validation_counts":validation_counts,
        "exact_prym_orders_over_F4_power":prym_orders(),
        "orbits_with_8_times_P_minus_delta_P_zero":torsion_orbits,
        "infinity": "deck-fixed; omitted from affine enumeration",
        "all_passed":True,
    }
    output=json.dumps(result,indent=2,sort_keys=True)
    Path(__file__).with_suffix('.json').write_text(output+'\n',encoding='utf-8')
    print(output)


if __name__=='__main__':
    main()
