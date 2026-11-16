import sympy as s
x,y,z=s.symbols('x y z')
E=y*y+y-x**3+1
m=3*x*x/(2*y+1)
X=m*m-2*x;Y=y-m*(x-X)
g=(z*z*x-y-2)/(x-y-2)
g2=(z*z*X-Y-2)/(X-Y-2)
num,den=s.fraction(s.cancel(g2-g**4))
num=s.rem(s.rem(num,z*z+z+1,z),E,y)
poly=s.Poly(num,x,y,z)
assert all(int(c)%2==0 for c in poly.coeffs())
half=s.Poly(num/2,x,y,z,modulus=2).as_expr()
half=s.rem(s.rem(half,z*z+z+1,z),E,y)
half=s.Poly(half,x,y,z,modulus=2).as_expr()
print('Raw denominator:',s.factor(den))
print('Half-difference numerator modulo2:',s.factor(half,extension=None))
print('Total degree:',s.Poly(half,x,y,z).total_degree())
print('x-degree,y-degree:',s.degree(half,x),s.degree(half,y))
assert half!=0
