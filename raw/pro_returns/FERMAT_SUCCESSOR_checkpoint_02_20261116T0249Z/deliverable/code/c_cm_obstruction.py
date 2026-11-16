from itertools import product
from math import comb

def matmul(A,B,m):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%m for i in range(2) for j in range(2))
def det(A,m): return (A[0]*A[3]-A[1]*A[2])%m
I=(1,0,0,1)
for m in (2,4):
    U=(1,1,0,1); L=(1,0,-1%m,1); S=matmul(matmul(U,L,m),U,m)
    central=[A for A in product(range(m),repeat=4) if det(A,m)==1 and matmul(A,U,m)==matmul(U,A,m) and matmul(A,L,m)==matmul(L,A,m)]
    shears=[(1,t,0,1) for t in range(m) if (1,t,0,1) in central]
    gaussian=[(a,b,(-b)%m,a) for a,b in product(range(m),repeat=2) if (a*a+b*b)%m==1]
    print('modulus',m,'simultaneous centralizer=',central,'normalized shears=',shears)
    print('S=',S,'norm-one=',S in gaussian,'scalar=',S[1]==0 and S[2]==0 and S[0]==S[3])
    assert shears==[I]
    assert S in gaussian and S != I

p=[0,0,1,3,3,1,0,0] # coefficients X^(7-j)Y^j of X^2Y^2(X+Y)^3
h=[comb(9,j+1) for j in range(8)]
# 2x2 determinant from coefficients j=0,2
minor=h[0]*p[2]-h[2]*p[0]
print('weight-nine extra coefficients',p)
print('weight-nine gamma coefficients',h)
print('independence minor',minor)
assert minor==9

# D8 law: r^a s^b r^c s^d = r^(a+(-1)^b c) s^(b+d)
def mul(g,h): return ((g[0]+(-1)**g[1]*h[0])%4,(g[1]+h[1])%2)
D=list(product(range(4),range(2)))
Hi=[(a,0) for a in range(4)]
Hminus3=[(0,0),(2,0),(1,1),(3,1)]
for name,H in [('Q(i)',Hi),('Q(sqrt(-3))',Hminus3)]:
    assert all(mul(g,h) in H for g in H for h in H)
    assert all(mul(g,h)==mul(h,g) for g in H for h in H)
    print(name,'fixing subgroup',H,'abelian=True')
assert mul((1,0),(0,1)) != mul((0,1),(1,0))
print('D8 nonabelian=True; intersection field witness x^4=3 verified by its exact action law')

# The actual pure modular image modulo 12, with its unique sign modulo 4.
def generated(generators, modulus):
    found={I}
    todo=[I]
    while todo:
        a=todo.pop()
        for g in generators:
            b=matmul(a,g,modulus)
            if b not in found:
                found.add(b)
                todo.append(b)
    return found

pure12=generated([(1,2,0,1),(1,0,10,1)],12)
pure4={tuple(a%4 for a in A) for A in pure12}
pure3={tuple(a%3 for a in A) for A in pure12}
assert len(pure12)==96 and len(pure4)==4 and len(pure3)==24
u3=(1,1,0,1)
s3=(0,1,2,0)
sinv3=(0,2,1,0)
sylow3=generated([u3],3)
conjugate=matmul(matmul(s3,u3,3),sinv3,3)
assert len(sylow3)==3 and conjugate not in sylow3
print('pure image modulo 12 order',len(pure12),'modulo 4 order',len(pure4),'modulo 3 order',len(pure3))
print('SL2(F3) Sylow-3 subgroup',sorted(sylow3),'S-conjugate of U',conjugate,'outside=True')
print('Pure image is not nilpotent; B/R_nil(F) cannot map to the retained Q576 marking.')
