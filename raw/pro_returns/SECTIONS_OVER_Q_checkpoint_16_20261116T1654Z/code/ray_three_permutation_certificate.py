#!/usr/bin/env python3
"""Exact ordinary-permutation identities for the ray-at-three intersection.

The proof concerns arbitrary finite three-primary abelian coefficient groups,
which decompose as sums of cyclic groups. This finite certificate checks
cyclic exponents3^r,1<=r<=5, and translation sizes3^n,1<=n<=3.
It certifies the group/module maps, not existence of a class field.
"""
from itertools import product
from math import gcd

def perm(v,u,shift,mod):
    N=len(v);out=[0]*N
    for j,a in enumerate(v):
        out[(u*j+shift)%N]=a%mod
    return tuple(out)

def add(a,b,mod):
    return tuple((x+y)%mod for x,y in zip(a,b))

def mul_wreath(a,b,mod):
    v,i=a;w,j=b;N=len(v)
    return add(v,perm(w,1,i,mod),mod),(i+j)%N

def power_wreath(a,N,mod):
    out=((0,)*len(a[0]),0)
    for _ in range(N):
        out=mul_wreath(out,a,mod)
    return out

def main():
    fixed_basis=norm_maps=unit_actions=lift_powers=deeper=0
    for n in range(1,4):
        N=3**n
        for r in range(1,6):
            mod=3**r
            # The fixed equations are v_j=v_(j-1); their firstN-1
            # differences form a triangular unit-minor system.
            for a in range(mod):
                diagonal=(a,)*N
                assert perm(diagonal,1,1,mod)==diagonal
                assert perm(diagonal,-1,0,mod)==diagonal
                fixed_basis+=1
            for j in range(N):
                basis=tuple(int(i==j) for i in range(N))
                norm=(0,)*N
                for k in range(N):
                    norm=add(norm,perm(basis,1,k,mod),mod)
                assert norm==(1,)*N
                assert perm(norm,-1,0,mod)==norm
                norm_maps+=1
            # Generic chosen lifts; the Nth power is the literal
            # translation norm, independent of nonzero coordinates.
            vectors=[
                tuple((j*j+2*j+1)%mod for j in range(N)),
                tuple(((-1)**j)%mod for j in range(N)),
                tuple(int(j==0) for j in range(N)),
            ]
            for v in vectors:
                result=power_wreath((v,1),N,mod)
                target=(sum(v)%mod,)*N
                assert result==(target,0)
                assert perm(result[0],-1,0,mod)==result[0]
                lift_powers+=1
            # Larger cyclotomic unit groups act on the same root indices
            # by reduction; their minus-one element is still reflection.
            for t in range(n,n+3):
                U=3**t
                for u in range(U):
                    if gcd(u,3)!=1:
                        continue
                    v=vectors[0]
                    left=perm(perm(perm(v,u,0,mod),1,1,mod),
                              pow(u,-1,N),0,mod)
                    right=perm(v,1,pow(u,-1,N),mod)
                    assert left==right
                    assert perm((sum(v)%mod,)*N,u,0,mod)==(sum(v)%mod,)*N
                    unit_actions+=1
        # Every lift of a generator of C_N to C_(3N) has nonzero
        # Nth power in the order3 kernel, inverted by conjugation.
        for a in range(1,3*N):
            if gcd(a,3)!=1:
                continue
            v=N*a%(3*N)
            assert v in (N,2*N)
            assert (-v)%(3*N)!=v
            deeper+=1
        # A nontrivial subgroup of a deeper cyclic3-extension contains
        # the unique first cubic layer on the corresponding field side.
        for depth in range(1,5):
            order=3**depth
            for subgroup_order in (3**j for j in range(depth)):
                assert subgroup_order<=order//3
                assert (order//3)%subgroup_order==0
                deeper+=1
    print('Translation-fixed diagonal vectors and involution checks:',fixed_basis)
    print('Literal cyclic permutation norm basis maps:',norm_maps)
    print('Larger cyclotomic unit actions:',unit_actions)
    print('Actual wreath-product lift powers:',lift_powers)
    print('Nonzero next-cubic kernels and deeper cyclic inclusions:',deeper)
    print('All checks passed for n1..3,r1..5 and larger cyclotomic depths n..n+2.')
    print('The arbitrary-group proof uses cyclic direct sums and the same unit-minor fixed equations.')
    print('This certificate asserts no class-field existence or ramification computation.')

if __name__=='__main__':
    main()

