"""Exact arithmetic certificates for A.69; no numerical approximations.

Run: python deliverable/code/a_main_finite_support.py
The geometric and Galois arguments are proved in A_finite_support.tex.
"""
import sympy as s

x, y, z, c, b = s.symbols("x y z c b")
curve = y*y + y - x**3 + 1
cyclo = z*z + z + 1

def reduced(poly):
    return s.rem(s.rem(s.expand(poly), cyclo, z), curve, y)

def mod2(poly):
    return s.Poly(reduced(poly), x, y, z, modulus=2).as_expr()

# On y^2+y=x^3-1, these are the coordinates of [-2](x,y).
slope = 3*x*x/(2*y+1)
xx = slope*slope - 2*x
yy = y - slope*(x-xx)
assert reduced(s.fraction(s.cancel(yy*yy+yy-xx**3+1))[0]) == 0

# At the chosen dyadic embedding b^3=3 has b=3 mod4, hence b^2=1 mod4.
g = (z*z*x-y-2)/(x-y-2)
gminus2 = (z*z*xx-yy-2)/(xx-yy-2)
numerator, denominator = s.fraction(s.cancel(gminus2-g**4))
numerator = reduced(numerator)
assert all(int(a) % 2 == 0 for a in s.Poly(numerator, x, y, z).coeffs())
half = mod2(numerator/2)
expected = ((z+1)*x**11 + z*x**10*y + x**9
            + (z+1)*x**8*y + x**6*y + x**6
            + z*x**4*y + (z+1)*x*x + z*x*y)
assert mod2(half-expected) == 0
assert half != 0
assert mod2(denominator-(x+y)**8) == 0

# Only (1,1), an order-three cusp, can make the affine denominator zero.
assert s.Poly(curve.subs(y, x)-(x+1)**3, x, modulus=2).is_zero

# Pole orders at O are ord_O(x)=-2 and ord_O(y)=-3.
# The coefficient field variable z has no pole.  Reduction has y-degree<=1.
terms = s.Poly(half, x, y, z).terms()
pole_terms = [(2*i+3*j, (i,j,k), int(a)) for (i,j,k),a in terms]
highest = max(t[0] for t in pole_terms)
assert highest == 23
assert [t[1] for t in pole_terms if t[0] == highest] == [(10,1,1)]

# E/F2 has three points, so Frobenius_2 has characteristic polynomial T^2+2.
affine2 = [(a,d) for a in range(2) for d in range(2)
           if (d*d+d-a**3+1) % 2 == 0]
assert affine2 == [(1,0),(1,1)]

# Pure coefficient-two witness: S=(b/c^2,-1/2), c^3=2.
h = (z*z*c-1)/(c-1)
value_at_two_torsion = (2*z*z-c*c)/(2-c*c)
diff = s.fraction(s.cancel(h-value_at_two_torsion))[0]
assert s.rem(s.rem(diff, c**3-2, c), cyclo, z) == 0
conjugates = [(z*z*(z**j*c)-1)/(z**j*c-1) for j in range(3)]
norm_num = s.fraction(s.cancel(s.prod(conjugates)-1))[0]
assert s.rem(s.rem(norm_num, c**3-2, c), cyclo, z) == 0

q, cc, zz = 31, 4, 25
assert pow(cc,3,q) == 2
assert (zz*zz+zz+1) % q == 0
hh = ((zz*zz*cc-1)*pow(cc-1,-1,q)) % q
assert hh == 27 and pow(hh,(q-1)//2,q) == q-1

# For p>=5, conjugating b through b,z*b,z^2*b telescopes the three g-values.
gg = (b*b*z*z*x-y-2)/(b*b*x-y-2)
conjugate_product = s.prod(gg.subs(b,z**j*b) for j in range(3))
product_num = s.fraction(s.cancel(conjugate_product-1))[0]
assert s.rem(product_num, cyclo, z) == 0

print("E(F2) affine points:", affine2, "; total=3; Frobenius_4=[-2]")
print("Reduced numerator of g0([-2]Q)-g0(Q)^4 is divisible by2.")
print("Half-numerator modulo2:", s.expand(half))
print("Denominator modulo2 on E: (x+y)^8")
print("Exact pole order of half-numerator at O:", highest)
print("Unique highest-pole monomial: z*x^10*y")
print("Minimum inert Cartan orbit: 5^2-1=24 >23")
print("Minimum split Cartan orbit: (7-1)^2=36 >23")
print("h=g(S2)=(z^2*c-1)/(c-1); product of its three cubic conjugates=1")
print("Nonsquare certificate: q=31, c=4, z=25, h=27, h^15 mod31=30")
print("Product of the three b-conjugates of g is identically1.")
print("All exact assertions passed.")
