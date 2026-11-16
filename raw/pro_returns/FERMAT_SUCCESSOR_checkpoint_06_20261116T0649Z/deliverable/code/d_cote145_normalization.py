"""Exact class-two collection for the directly read cote 145 dictionary."""
import sympy as s

p, A, B, a = s.symbols('p A B a')

def mul(v, w):
    x, y, z = v
    xx, yy, zz = w
    return tuple(s.expand(t) for t in (x + xx, y + yy, z + zz - xx*y))

def power(v, n):
    x, y, z = v
    return (n*x, n*y, s.expand(n*z - x*y*n*(n-1)/2))

def inverse(v):
    return power(v, -1)

def conjugate(v, w):
    return mul(mul(v, w), inverse(v))

def image(v, ximage, yimage, cscale):
    x, y, z = v
    return mul(mul(power(ximage, x), power(yimage, y)), (0, 0, cscale*z))

x, y, c = (1,0,0), (0,1,0), (0,0,1)
rho_x, rho_y = y, inverse(mul(x,y))
g = (A,B,0)  # The omitted central coordinate cancels from conjugation.
u_x, u_y = power(x,p), conjugate(g,power(y,p))
left = image(rho_y,u_x,u_y,p*p)
right = conjugate(g,image(u_y,rho_x,rho_y,1))
expected_left=(-p,-p,-A*p-p*p)
expected_right=(-p,-p,B*p-p*(p+1)/2)
assert all(s.simplify(v-w)==0 for v,w in zip(left,expected_left))
assert all(s.simplify(v-w)==0 for v,w in zip(right,expected_right))
assert s.factor(2*(left[2]-right[2])) == -p*(2*A+2*B+p-1)
print('u rho(y):', tuple(map(s.factor,left)))
print('Int(g) rho u(y):', tuple(map(s.factor,right)))
print('Twice central difference:', s.factor(2*(left[2]-right[2])))
print('For p a profinite unit: A+B=(1-p)/2; beta=(p-1)/2.')

f = mul(mul(power(y,B),inverse(g)),power(x,A))
gnew=mul(mul(power(x,a),g),power(y,-a))
fnew=mul(mul(power(y,B-a),inverse(gnew)),power(x,A+a))
assert all(s.simplify(v-w)==0 for v,w in zip(f,fnew))
assert f[:2] == (0,0)
print('The commutator-normalized f=y^B g^-1 x^A is gauge-invariant.')
print('Complex conjugation p=-1,g=y: f=1,beta=-1.')
print('No pentagon follows from this normalization alone.')
