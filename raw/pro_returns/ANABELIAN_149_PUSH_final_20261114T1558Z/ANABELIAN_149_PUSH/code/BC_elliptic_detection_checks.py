#!/usr/bin/env python3
"""Exact arithmetic for the elliptic example after C.7g.

This checks the displayed example only.  The finite Green-function
separation theorem is proved analytically in the manuscript.
"""
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import json


@dataclass(frozen=True)
class Cyclotomic3:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', Fraction(self.a))
        object.__setattr__(self, 'b', Fraction(self.b))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Cyclotomic3) else Cyclotomic3(value)

    def __add__(self, other):
        other = self.coerce(other)
        return Cyclotomic3(self.a+other.a, self.b+other.b)

    __radd__ = __add__

    def __neg__(self):
        return Cyclotomic3(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        return Cyclotomic3(self.a*other.a-self.b*other.b,
                           self.a*other.b+self.b*other.a-self.b*other.b)

    __rmul__ = __mul__

    def inverse(self):
        norm = self.a*self.a-self.a*self.b+self.b*self.b
        assert norm != 0
        return Cyclotomic3((self.a-self.b)/norm, -self.b/norm)

    def __truediv__(self, other):
        return self*self.coerce(other).inverse()

    def __pow__(self, exponent):
        assert exponent >= 0
        value = Cyclotomic3(1)
        for _ in range(exponent):
            value = value*self
        return value

    def serial(self):
        return [str(self.a), str(self.b)]


zero = Cyclotomic3(0)
one = Cyclotomic3(1)
zeta = Cyclotomic3(0, 1)


def negate(point):
    return None if point is None else (point[0], -point[1])


def on_curve(point):
    return point is None or point[1]**2 == point[0]**3+1


def add(point, other):
    if point is None:
        return other
    if other is None:
        return point
    x, y = point
    xx, yy = other
    if x == xx and y == -yy:
        return None
    slope = (3*x**2)/(2*y) if point == other else (yy-y)/(xx-x)
    x_new = slope**2-x-xx
    result = (x_new, slope*(x-x_new)-y)
    assert on_curve(result)
    return result


def multiply(point, integer):
    result = None
    for _ in range(integer):
        result = add(result, point)
    return result


def serial(point):
    return None if point is None else [coordinate.serial() for coordinate in point]


P = (Cyclotomic3(2), Cyclotomic3(3))
tauP = (2*zeta, Cyclotomic3(3))
twice = multiply(P, 2)
thrice = multiply(P, 3)
delta = add(P, negate(tauP))
checks = [
    {'name': 'exact cyclotomic relation', 'passed': zeta**2+zeta+1 == zero},
    {'name': 'P and tau(P) lie on Y^2=X^3+1', 'passed': on_curve(P) and on_curve(tauP)},
    {'name': '2P=(0,1)', 'passed': twice == (zero, one)},
    {'name': '3P=(-1,0)', 'passed': thrice == (-one, zero)},
    {'name': 'P has exact order six', 'passed': multiply(P, 6) is None and all(multiply(P, n) is not None for n in (1, 2, 3))},
    {'name': 'tau has order three and fixes 2P', 'passed': zeta**3 == one and (zeta*twice[0], twice[1]) == twice},
    {'name': 'P-tau(P)=(-zeta^2,0) is nonzero two-torsion', 'passed': delta == (-zeta**2, zero) and delta is not None and multiply(delta, 2) is None},
    {'name': 'both endpoints lie over t=2', 'passed': (P[1]+1)/2 == Cyclotomic3(2) and (tauP[1]+1)/2 == Cyclotomic3(2)},
]
assert all(row['passed'] for row in checks)
result = {
    'all_checks_passed': True,
    'number_of_named_checks': len(checks),
    'coefficient_field': 'Q[zeta]/(zeta^2+zeta+1), exact Fraction arithmetic',
    'curve': 'Y^2=X^3+1',
    'map': 't=(Y+1)/2, equivalently X^3=4t(t-1)',
    'P': serial(P), 'twice_P': serial(twice), 'thrice_P': serial(thrice),
    'tau_P': serial(tauP), 'P_minus_tau_P': serial(delta),
    'checks': checks,
    'scope': 'Checks the explicit torsion-pair example; does not numerically verify the Green-function or full fixed-group theorems.',
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
