"""Small exact coefficient helpers for the E120 certificates.

This module has no file writes or import-time computations.
"""
from fractions import Fraction as F


class QZ:
    """Q[zeta]/(zeta^2+zeta+1), with literal rational coordinates."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def coerce(other):
        return other if isinstance(other, QZ) else QZ(other)

    def __add__(self, other):
        other = self.coerce(other)
        return QZ(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return QZ(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return QZ(self.a*other.a - self.b*other.b,
                  self.a*other.b + self.b*other.a - self.b*other.b)

    __rmul__ = __mul__

    def inv(self):
        norm = self.a*self.a - self.a*self.b + self.b*self.b
        if not norm:
            raise ZeroDivisionError
        return QZ((self.a-self.b)/norm, -self.b/norm)

    def __truediv__(self, other):
        return self*self.coerce(other).inv()

    def __pow__(self, n):
        if n < 0:
            return self.inv()**(-n)
        out, base = QZ(1), self
        while n:
            if n & 1:
                out = out*base
            base = base*base
            n //= 2
        return out

    def __bool__(self):
        return bool(self.a or self.b)

    def __eq__(self, other):
        other = self.coerce(other)
        return self.a == other.a and self.b == other.b

    def key(self):
        return [str(self.a), str(self.b)]


def peripheral_block(divisors, triples):
    """Jacobi kernel -> the two Lie3 coordinates at each of eight cusps."""
    a, b = [row[1:] for row in divisors]
    block = [[0]*len(triples) for _ in range(16)]
    for col, (i,j,k) in enumerate(triples):
        for x,y,z in ((i,j,k),(j,k,i),(k,i,j)):
            determinant = a[y]*b[z] - b[y]*a[z]
            block[2*x][col] = determinant*a[x]
            block[2*x+1][col] = determinant*b[x]
    return block
