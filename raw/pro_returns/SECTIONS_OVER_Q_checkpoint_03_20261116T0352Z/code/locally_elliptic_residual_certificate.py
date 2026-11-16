"""Finite certificate for E: y^2=x(x-1)(x-3), coefficient prime 7.

The mathematical use of this computation is explained in
work/notes/finite_ramification_continuation.md.  No external package is needed.
"""


def point_count(q):
    return 1 + sum(
        (y * y - x * (x - 1) * (x - 3)) % q == 0
        for x in range(q)
        for y in range(q)
    )


def valuation(n, p):
    answer = 0
    while n % p == 0:
        answer += 1
        n //= p
    return answer


delta = 16 * 3**2 * (1 - 3) ** 2
c4 = 16 * (3**2 - 3 + 1)
q = 5
count = point_count(q)
trace = q + 1 - count
disc7 = (trace**2 - 4 * q) % 7
squares7 = sorted({a * a % 7 for a in range(7)})

print(f"E: y^2=x(x-1)(x-3)")
print(f"Delta={delta}; c4={c4}")
print(f"v_3(Delta)={valuation(delta, 3)}; v_3(c4)={valuation(c4, 3)}")
print(f"#E(F_5)={count}; a_5={trace}")
print(f"Frobenius discriminant modulo 7={disc7}; squares modulo 7={squares7}")
print(f"Discriminant is nonsquare: {disc7 not in squares7}")
print(f"7 does not divide v_3(Delta): {valuation(delta, 3) % 7 != 0}")
print(f"Good reduction at 7: {delta % 7 != 0}")

assert count == 4
assert disc7 not in squares7
assert valuation(delta, 3) == 2
assert valuation(c4, 3) == 0
assert delta % 7 != 0
