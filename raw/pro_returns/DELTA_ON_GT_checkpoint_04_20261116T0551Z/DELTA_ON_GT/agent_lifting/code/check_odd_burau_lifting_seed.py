"""Actual R2 seed for the F7 five-point quotient, not a GT-shadow census.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from itertools import permutations
from pathlib import Path
import json
import sympy as sy

# Universal identities over Z[w], reduced modulo w^2+w+1.
w=sy.Symbol('w')
def reduce_ring(M):
    return M.applyfunc(lambda z:sy.rem(sy.expand(z),w*w+w+1,w))
AA=sy.Matrix([[1-w,w,0],[1,0,0],[0,0,1]])
BB=sy.Matrix([[1,0,0],[0,1-w,w],[0,1,0]])
CC=sy.Matrix([[1,0,-1],[0,1,-1],[0,0,-w]])
EI=sy.eye(3)
XX=[reduce_ring(AA*AA),reduce_ring(BB*BB),reduce_ring(CC*CC),
    reduce_ring((AA*BB*AA)**2),reduce_ring((CC*BB*CC)**2)]
assert all(reduce_ring((XX[j]-EI)**2)==sy.zeros(3)for j in(3,4))
v=sy.Matrix([1,1,1]);ell=sy.Matrix([[1,w,w*w]])
assert all(reduce_ring(T*v)==v and reduce_ring(ell*T)==reduce_ring(ell)for T in(AA,BB))
assert reduce_ring(ell*v)==sy.zeros(1,1)
flag=sy.Matrix([[1,0,0],[1,1,0],[1,-w*w,w]])
assert reduce_ring(sy.Matrix([[flag.det()]]))[0]==w
fi=reduce_ring(w*w*flag.adjugate())
assert reduce_ring(fi*flag)==EI
for T in(AA,BB):
    tri=reduce_ring(fi*T*flag)
    assert all(tri[i,j]==0 for i in range(3)for j in range(i))
    assert [tri[i,i]for i in range(3)]==[1,-w,1]
assert all(T.subs(w,1).applyfunc(lambda z:z%3)==EI for T in XX)

I=(1,0,0,0,1,0,0,0,1)
def norm(a):
    a=tuple(x%7 for x in a);u=pow(next(x for x in a if x),-1,7)
    return tuple(u*x%7 for x in a)
def mul(a,b):
    return norm(tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))%7
                      for i in range(3) for j in range(3)))
def power(a,n):
    out=I
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
def inv(a):
    r=[list(a[3*i:3*i+3])+[int(i==j)for j in range(3)] for i in range(3)]
    for j in range(3):
        k=next(k for k in range(j,3)if r[k][j]);r[j],r[k]=r[k],r[j]
        u=pow(r[j][j],-1,7);r[j]=[u*x%7 for x in r[j]]
        for k in range(3):
            if k!=j:
                u=r[k][j];r[k]=[(x-u*y)%7 for x,y in zip(r[k],r[j])]
    ans=norm(tuple(x for row in r for x in row[3:]));assert mul(a,ans)==I
    return ans
def prod(*gg):
    r=I
    for g in gg:r=mul(r,g)
    return r
def comm(a,b):return prod(a,b,inv(a),inv(b))
def order(a):return next(n for n in range(1,1009)if power(a,n)==I)
def seed28(x,y):
    z=inv(mul(x,y));xx,yy,zz=[power(t,28)for t in(x,y,z)]
    return comm(comm(xx,yy),comm(yy,zz))
a=norm((-1,2,0,1,0,0,0,0,1))
b=norm((1,0,0,0,-1,2,0,1,0))
c=norm((1,0,-1,0,1,-1,0,0,-2))
assert prod(a,b,a)==prod(b,a,b) and prod(b,c,b)==prod(c,b,c)
assert mul(a,c)==mul(c,a) and power(prod(a,b,c),4)==I
X=(power(a,2),power(b,2),power(c,2),power(prod(a,b,a),2),power(prod(c,b,c),2))
records=[]
for i,j in ((2,3),(4,0),(1,2),(3,4),(0,1)):
    x,y=X[i],X[j];z=inv(mul(x,y));triples=list(permutations((x,y,z)))
    pre=[seed28(u,v)for u,v,w in triples]
    final=[power(v,7)for v in pre]
    assert final==[I]*6
    records.append({'pair':[i+1,j+1],'peripheral_orders':[order(t)for t in(x,y,z)],
                    'orders_before_seventh_power':[order(v)for v in pre],
                    'all_six_final_values_are_one':True})

I2=(1,0,0,1)
def mm(a,b):return tuple(sum(a[2*i+k]*b[2*k+j]for k in range(2))%12 for i in range(2)for j in range(2))
def ii(a):return (a[3],-a[1]%12,-a[2]%12,a[0])
def pp(a,n):
    out=I2
    for _ in range(n):out=mm(out,a)
    return out
def cc(a,b):return mm(mm(mm(a,b),ii(a)),ii(b))
def seed2(x,y):
    z=ii(mm(x,y));xx,yy,zz=[pp(v,28)for v in(x,y,z)]
    return pp(cc(cc(xx,yy),cc(yy,zz)),7)
U=(1,1,0,1);L=(1,0,11,1)
orig=seed2(pp(U,2),pp(L,2));assert orig==(5,0,0,5)
ox,oy=pp(U,2),pp(L,2);oz=ii(mm(ox,oy))
assert all(pp(t,12)==I2 for t in(ox,oy,oz))
uniform_q=[]
for m in(2,4,8,10):
    qx,qy,qz=[pp(t,m)for t in(ox,oy,oz)]
    val=cc(cc(qx,qy),cc(qy,qz));assert val==(5,0,0,5)
    uniform_q.append({'exponent_mod12':m,'q12_value':val})
S=(0,1,11,0);tau=ii(U);z=ii(mm(S,tau))
orb=[seed2(u,v)for u,v,w in permutations((S,tau,z))]
assert orb==[I2]*6
out={'seed':'([[x^28,y^28],[y^28,z^28]])^7',
     'universal_square_zero_unipotence_X4_X5':True,
     'universal_primitive_invariant_flag_A_B':True,
     'flag_basis_determinant':'omega',
     'all_Xi_residue_three_are_one':True,
     'all_even_exponents_prime_to_three':uniform_q,
     'original_q12_value':orig,'six_orbifold_q12_values':orb,
     'five_point_pair_certificates':records,
     'scope':'The universal identities prove LI9: compactness supplies one actual Delta1,Dk1 gentle element whose five pentagon factors vanish at every adelic primitive-cube-root Burau congruence level. The explicit word additionally kills all five F7 pair kernels. GT membership is not asserted.'}
dest=Path(__file__).resolve().parents[1]/'records'/'odd_burau_lifting_seed.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
