#!/usr/bin/env python3
"""Finite symbolic and squareclass audit for A.91."""

import sympy as sp

x, y, X, Y, t, v, d = sp.symbols("x y X Y t v d")
f = lambda a, z: z*(z-1)*(z-a)
assert sp.expand(f(1-t, 1-x)+f(t, x)) == 0
assert sp.expand(t**3*f(1/t, x/t)-f(t, x)) == 0
assert sp.expand((x-1)*x*(x-t)-f(t, x)) == 0
assert sp.expand(x*(x-t)*(x-1)-f(t, x)) == 0
assert sp.expand(((8*Y+4*X)**2-(4*X)*(4*X+1)*(4*X+16*v))/64
                 -(Y**2+X*Y-X**3-4*v*X**2-v*X)) == 0
b2, b4, b8 = 1+16*v, 2*v, -v*v
delta = sp.expand(-b2*b2*b8-8*b4**3)
assert sp.expand(delta-v*v*(1-16*v)**2) == 0

# Unit squareclasses 1,3,5,7.  The class5 is unramified, since
# X^2-X-1 is irreducible separable modulo2 and has discriminant5.
# Class7 is -1 and is ramified by (1+i)^2=2i; class3=5*7.
classes = (1, 3, 5, 7)
inertia = {1: 0, 3: 1, 5: 0, 7: 1}


def row(label, unit):
    if label == 0:
        return ((unit, 1), 1)
    if label == 1:
        return ((1, unit), 0)
    return ((unit, -unit % 8), inertia[-unit % 8])


checks = 0
for target_label in (0, 1, "infinity"):
    for target_unit in classes:
        target = row(target_label, target_unit)
        allowed = [(label, unit)
                   for label in (0, 1, "infinity") for unit in classes
                   if row(label, unit) == target]
        assert allowed == [(target_label, target_unit)]
        checks += 12

for unit in range(-255, 256, 2):
    assert int(delta.subs(v, unit)) % 2 == 1
    for label in (0, 1, "infinity"):
        cls, char = row(label, unit % 8)
        assert cls[0] in classes and cls[1] in classes and char in (0, 1)

# The three explicit parameter transformations generate the exact six values.
parameter = sp.symbols("parameter")
expected = {
    str(sp.cancel(parameter)), str(sp.cancel(1-parameter)),
    str(sp.cancel(1/parameter)), str(sp.cancel(1/(1-parameter))),
    str(sp.cancel(parameter/(parameter-1))),
    str(sp.cancel((parameter-1)/parameter)),
}
orbit = {str(parameter)}
while True:
    enlarged = orbit | {str(sp.cancel(1-sp.sympify(a))) for a in orbit}
    enlarged |= {str(sp.cancel(1/sp.sympify(a))) for a in orbit}
    if enlarged == orbit:
        break
    orbit = enlarged
assert orbit == expected

print("A.91 certificate: all checks passed.")
print("Verified the two Legendre permutation maps, translation/twist identities, and the exact good-model polynomial/discriminant.")
print(f"Checked {checks} comparisons of all three contact-four labels and all four dyadic unit squareclasses; exactly the original label survives.")
print("Checked the good discriminant and unit-class rows for256 signed odd units, including negative parameters.")
print("The two coordinate generators have exactly the stated six rational parameter transforms.")
print("The coefficient-prime rational-line theorem and full-section recognition are proof inputs, not inferred from these finite checks.")
