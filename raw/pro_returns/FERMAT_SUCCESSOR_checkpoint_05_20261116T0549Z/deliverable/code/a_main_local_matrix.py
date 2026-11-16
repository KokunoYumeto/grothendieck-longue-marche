"""Exact finite certificates for A.47's natural mixed quotient witness."""
import itertools
from sympy import symbols,discriminant,expand

p=7
I=(1,0,0,1)

def mul(A,B):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)

def inv(A):
    a,b,c,d=A;k=pow((a*d-b*c)%p,-1,p)
    return (d*k%p,-b*k%p,-c*k%p,a*k%p)

def power(A,n):
    B=I
    for _ in range(n):B=mul(B,A)
    return B

def order(A):
    B=I
    for n in range(1,1000):
        B=mul(B,A)
        if B==I:return n
    raise AssertionError(A)

def subgroup(gs):
    known={I};todo=[I]
    while todo:
        A=todo.pop()
        for B in gs:
            C=mul(A,B)
            if C not in known:known.add(C);todo.append(C)
    return known

def comm(A,B):return mul(mul(mul(A,B),inv(A)),inv(B))

G={A for A in itertools.product(range(p),repeat=4) if (A[0]*A[3]-A[1]*A[2])%p==1}
U=(1,2,0,1);L=(1,0,5,1)
assert len(G)==336 and subgroup([U,L])==G
D=(2,0,0,4);F=(3,0,0,1)
assert order(D)==3 and order(F)==6 and mul(D,F)==mul(F,D)
assert subgroup([comm(D,U),comm(D,L)])==G
conjugates={mul(mul(A,D),inv(A)) for A in G}
assert subgroup(conjugates)==G
print('Legendre unipotents generate SL2(F7), order336.')
print('Commutators with diag(2,4) generate SL2(F7); hence its derived group is the whole group.')
print('Normal closure of diag(2,4), order3, is SL2(F7); every prime-to3 quotient is trivial.')
print('Wild matrix diag(2,4) has order3; Frobenius diag(3,1) has determinant3 and commutes with it.')
for sign in (1,6):
    A=tuple(sign*a%p for a in D)
    assert A!=I
print('Neither quadratic scalar removes the nontrivial order3 inertia.')
x=symbols('x');f=x**3-3*x+1
assert discriminant(f,x)==81
assert expand(f.subs(x,x-1))==x**3-3*x*x+3
assert all(f.subs(x,a)!=0 for a in (-1,1))
print('Q(zeta9)^+ polynomial x^3-3x+1 has discriminant81 and is irreducible; its shift x^3-3x^2+3 is Eisenstein at3.')
print('Its order3 character has conductor9 and supplies the global character theta in A.47.')
print('ALL_LOCAL_MATRIX_CHECKS_PASSED')
