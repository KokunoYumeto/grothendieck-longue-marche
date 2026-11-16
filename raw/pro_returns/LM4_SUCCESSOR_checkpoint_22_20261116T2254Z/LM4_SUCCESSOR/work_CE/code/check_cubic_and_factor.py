"""Finite matrix and homomorphism checks for C.11, C.20, C.24, C.25."""
from itertools import product, permutations
import sympy as s

T=s.Matrix([[0,-1],[1,-1]])
J=s.Matrix([[0,1],[-1,0]])
R=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
U=s.diag(R,R)
H=s.zeros(6)
H[:3,3:]=s.eye(3);H[3:,:3]=-s.eye(3)
assert T**3==s.eye(2) and T.T*J*T==J
assert U**3==s.eye(6) and U.T*H*U==H and H.det()==1
e=s.Matrix([1,1,1,0,0,0]);f=s.Matrix([0,0,0,1,1,1])
assert U*e==e and U*f==f and (e.T*H*f)[0]==3
assert (T-s.eye(2)).det()==3
print('C.24: cyclotomic and paired regular blocks invariant and unimodular; fixed norm pairing=3. PASS')
for q in (7,13,19,31):
    rank=2+3*(q-1)
    assert rank==3*q-1 and rank%2==0
    print(f'C.24: q={q}, rank={rank}, genus={rank//2}, fixed rank={q-1}.')

S3=list(permutations(range(3)));one=tuple(range(3))
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def inv(a):return tuple(a.index(i) for i in range(3))
def power(a,n):
    b=one
    for _ in range(n):b=mul(b,a)
    return b
def conj(a,b):return mul(mul(a,b),inv(a))
maps=[]
for x,y,z in product(S3,repeat=3):
    if power(x,3)==one and power(y,3)==one and power(z,2)==one:
        if conj(z,x)==x and conj(z,y)==inv(y):maps.append((x,y,z))
assert len(maps)==12
assert sum(z==one for x,y,z in maps)==3
print('C.25: exactly 12 homomorphisms from the projective countermodel to S3: 3 with z=1, 9 with z a transposition. PASS')

# Degree-two quotient of the free group at 2: X^2,Y^2,[X,Y].
count=0
for a,b,c,d in product(range(2),repeat=4):
    A=s.Matrix([[a,c],[b,d]])
    if int(A.det())%2!=1 or any(int(v)%2 for v in A*A-s.eye(2)):continue
    D=s.Matrix([[a,c,0],[b,d,0],[a*b,c*d,1]])
    im={tuple(int(z)%2 for z in (s.eye(3)+D)*s.Matrix(v)) for v in product(range(2),repeat=3)}
    assert (0,0,1) not in im
    count+=1
assert count==4
print('C.11: all four involutive GL2(F2) matrices have commutator class outside image(1+action) in degree two. PASS')

A=s.Matrix([[1,-2],[1,-1]])
deck=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
Tc=s.Matrix([[1,-1,-1],[1,0,-1],[1,-1,0]])
inc=s.Matrix([[2,0,0],[0,1,1]])
assert A*A==-s.eye(2) and Tc*Tc==-deck and inc*Tc==A*inc
assert s.eye(3)+Tc+Tc**2+Tc**3==2*(s.eye(3)-deck)
assert (deck*Tc)**2==-deck
print('C.20: adapted integral quartic sample verifies deck, inclusion, square and norm identities. PASS')
