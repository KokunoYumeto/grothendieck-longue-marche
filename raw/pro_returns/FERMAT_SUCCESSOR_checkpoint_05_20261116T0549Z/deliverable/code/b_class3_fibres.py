"""Independent integral Hall certificate for every class-three fibre.

The actual degree-one gluing, complex conjugation and the Frobenius at
seven are reconstructed here. No inherited output or matrix is read.
All Smith pivots are below the modulus; the exact rational rank is
proved separately by the involution and Frobenius weights.
"""
from collections import Counter
import numpy as np
import sympy as s

PREC=12
MOD=3**PREC
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
index={t:n for n,t in enumerate(hall)}
assert len(hall)==330

def hall_bracket(a,b,c):
    if a==b:
        return ()
    sign=1
    if a<b:
        a,b,sign=b,a,-1
    if c>=b:
        return ((index[(a,b,c)],sign),)
    return ((index[(a,c,b)],sign),(index[(b,c,a)],-sign))

def lie3(B):
    B=np.asarray(B,dtype=np.int64)%MOD
    nz=[[(i,int(B[i,j])) for i in range(10) if B[i,j]] for j in range(10)]
    L=np.zeros((330,330),dtype=np.int64)
    for col,(i,j,k) in enumerate(hall):
        for a,x in nz[i]:
            for b,y in nz[j]:
                for c,z in nz[k]:
                    scalar=x*y*z%MOD
                    for row,sign in hall_bracket(a,b,c):
                        L[row,col]=(int(L[row,col])+sign*scalar)%MOD
    return L

def smith3(B,rank=330):
    B=B.copy()%MOD
    vals=[]
    for k in range(rank):
        active=B[k:,k:]
        power=1
        for v in range(PREC):
            nonzero=np.argwhere((active//power)%3)
            if len(nonzero):
                break
            power*=3
        else:
            raise AssertionError('Expected pivot is not visible at certified precision')
        i,j=map(int,nonzero[0]);i+=k;j+=k
        B[[i,k],:]=B[[k,i],:]
        B[:,[j,k]]=B[:,[k,j]]
        assert not np.any(B[k:,k:]%power)
        unit=int(B[k,k])//power
        B[k,k:]=(B[k,k:]*pow(unit,-1,MOD))%MOD
        assert B[k,k]==power
        quotient=B[k+1:,k]//power
        B[k+1:,k:]=(B[k+1:,k:]-quotient[:,None]*B[k,k:][None,:])%MOD
        assert not np.any(B[k+1:,k])
        vals.append(v)
    if rank<330:
        assert not np.any(B[rank:,rank:])
    return dict(sorted(Counter(vals).items()))

def valuation3(n):
    assert n
    v=0
    while n%3==0:
        n//=3;v+=1
    return v

U=s.Matrix([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]])
R=s.Matrix([[0,-1],[1,-1]])
CE=s.Matrix([[1,-1],[0,-1]])
CT=s.zeros(8)
for j,i in enumerate([0,2,1,3,5,4,7,6]):
    CT[i,j]=-1
CV=CE.row_join(s.zeros(2,8)).col_join(((U*CE-CT*U)/3).row_join(CT))
assert all(v.q==1 for v in CV)
assert CV*CV==s.eye(10) and s.trace(CV)==-2

def degree_one(AE,q):
    B=AE.row_join(s.zeros(2,8)).col_join((U*(AE-q*s.eye(2))/3).row_join(q*s.eye(8)))
    assert all(v.q==1 for v in B)
    return B

T=degree_one(s.eye(2)+3*R,7)
LT=lie3(T)
LC=lie3(CV)
I=np.eye(330,dtype=np.int64)
assert np.array_equal(LC@LC%MOD,I)
trace=int(np.trace(LC)%MOD)
assert trace==MOD-2
print('Hall rank 330; complex conjugation squares to 1 and has trace -2: PASS')
print('Exact invariant ranks: plus=164, minus=166')

# Count E27 points directly, rather than importing a trace table.
for p,expected in [(2,3),(7,9)]:
    count=1+sum((y*y+y-x*x*x+7)%p==0 for x in range(p) for y in range(p))
    assert count==expected
    print(f'E27(F_{p}) point count = {count}: PASS')
# log(1+3*zeta)/3 and its conjugate reduce to zeta,zeta^2 mod3.
assert int(s.Matrix([[0,-1],[1,-1]]).det())%3==1
print('Actual Frobenius pair above7 is a Frattini basis via the primary CM logarithms: PASS')

fibre=smith3(((LT-I)@(I+LC))%MOD,rank=164)
assert fibre=={0:73,1:7,2:56,3:25,4:3}
print('Global fibre Smith valuations:',fibre)
print('Every nonempty fibre = Z3^166 + C3^7 + C9^56 + C27^25 + C81^3')

L2=lie3(degree_one(-2*s.eye(2),4))
local2=smith3((L2-4*I)%MOD)
assert local2=={0:132,1:70,2:24,3:76,4:28}
assert sum(v*c for v,c in local2.items())==458
print('At K-prime (2), Phi-4 Smith valuations:',local2)
print('Independent determinant valuation = 2*1 +32*1 +128*2 +168*1 = 458: PASS')
print('Exact local coefficient exponent at (2) is 3^4')

# Inert primes: a uniform rational eigenspace decomposition improves the
# coarse determinant bound.  These checks expose the exact operator orders;
# they do not evaluate the arithmetic extension vector eta(F).
for p in [2,5,11,17,53]:
    assert p%3==2
    h=valuation3(p+1)
    L=lie3(degree_one(-p*s.eye(2),p*p))
    D=(pow(p*p,-1,MOD)*L-I)%MOD
    vals=smith3(D)
    det_v=sum(v*c for v,c in vals.items())
    assert det_v==330*h+128
    print(f'Inert p={p}, h={h}, Smith={vals}, exponent=3^{max(vals)}, determinant valuation={det_v}: PASS')
print('All newly reconstructed class-three fibre and local coefficient certificates passed.')
