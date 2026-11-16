#!/usr/bin/env python3
"""Exact finite-ring certificates for A.130; no field-only rank tests."""
from itertools import product
from math import gcd
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

lines=[]
def record(s):
    lines.append(s)
    print(s,flush=True)

def group(n,r):
    N=3**n; d=N//3; modulus=3**r; depth=max(n,r)
    basis=sp.zeros(N,2*d)
    for j in range(2*d):
        basis[j,j]=1
        basis[j%d+2*d,j]=-1
    out=[]
    for a in range(N):
        for u in range(3**depth):
            if u%3==0:continue
            moved=sp.zeros(N,2*d)
            for i in range(N):
                moved[(a+u*i)%N,:] += u*basis[i,:]
            out.append((moved[:2*d,:].applyfunc(lambda z:int(z)%modulus),u%modulus))
    return 2*d,out

def kernel_size(A,modulus):
    diagonal=smith_normal_form(A,domain=ZZ)
    out=modulus**A.cols
    for i in range(min(A.rows,A.cols)):
        value=int(diagonal[i,i])
        if value:
            out=out//modulus*gcd(value,modulus)
    return out

def image_size(A,modulus):
    return modulus**A.cols//kernel_size(A,modulus)

def kron_vectors(a,b):
    return sp.Matrix([x*y for x in a for y in b])

for n,r in [(1,1),(1,2),(1,3),(2,1),(2,2)]:
    k,G=group(n,r); modulus=3**r; d=3**(n-1)
    t0=sp.zeros(k,1);t0[0]=-1;t0[d]=1
    rows=[]
    for g,chi in G:
        inverse=pow(chi,-1,modulus)
        for j in range(k):
            e=sp.eye(k)[:,j]
            row=inverse*kron_vectors(g*e,g*t0)-kron_vectors(e,t0)
            rows.append([int(z)%modulus for z in row])
    constraints=sp.Matrix(rows)
    assert kernel_size(constraints,modulus)==3**n
    # Every surviving dual character has order three, proved by comparing
    # the full kernel with its intersection with 3B=0.
    assert kernel_size(sp.Matrix.vstack(constraints,3*sp.eye(k*k)),modulus)==3**n
    record(f'n={n},r={r}: transported q0 annihilator has order3^{n}; '
           f'it is killed by3; actual group order {len(G)}.')

def affine_matrix(ts,G,k,modulus):
    rows=len(ts)*k+k*k
    cols=len(ts)*len(G)*k
    A=sp.zeros(rows,cols)
    col=0
    for p,t in enumerate(ts):
        for g,chi in G:
            gt=g*t
            inv=pow(chi,-1,modulus)
            for j in range(k):
                A[p*k+j,col]=1
                vec=-inv*kron_vectors(g[:,j],gt)
                for i,value in enumerate(vec):
                    A[len(ts)*k+i,col]=int(value)%modulus
                col+=1
    return A

# The precision-nine affine problem is solved by finite abelian image sizes,
# not by Gaussian elimination over a field.
k,G=group(1,2);modulus=9
t0=sp.Matrix([-1,1]);checks=0;soluble=0
tests_t=[sp.Matrix([a,b]) for a,b in product(range(9),repeat=2)
         if (a+2*b)%4==0]
tests_c=[sp.Matrix([a,b]) for a,b in product(range(9),repeat=2)
         if (2*a+b)%5==0]
for t in tests_t:
    A=affine_matrix([t0,t],G,k,modulus)
    image=image_size(A,modulus)
    for c in tests_c:
        target=sp.Matrix([0,0,-int(c[0]),-int(c[1]),0,0,0,0])
        possible=image_size(A.row_join(target),modulus)==image
        quadratic=(int(t[0]*c[1]-t[1]*c[0])%3)==0
        assert possible==quadratic
        checks+=1;soluble+=possible
record(f'Precision-nine affine systems: {checks} exact systems; '
       f'{soluble} soluble; solvability equals the mod-three quadratic test.')

characters=0
for m in [3,9,27]:
    for common in [1,3]:
        if common>m:continue
        fibre=[(a,b) for a in range(m) for b in range(m)
               if (a-b)%common==0]
        from_factors={tuple((u*a+v*b)%m for a,b in fibre)
                      for u in range(m) for v in range(m)}
        # (a,b) -> (a,(b-a)/common) identifies the group with
        # Z/m x Z/(m/common), giving its entire character group.
        abstract={tuple((u*a+common*v*((b-a)//common))%m for a,b in fibre)
                  for u in range(m) for v in range(m//common)}
        assert from_factors==abstract
        characters+=len(abstract)
record(f'Bounded-character fibre products: {characters} actual characters '
       'all decompose through the two factor maps.')
record('ALL CHECKS PASSED. Scalar Hilbert reciprocity and global existence '
       'are proved in the accompanying source, not inferred from sampling.')
Path(__file__).with_name('relative_cyclic_precision_certificate_output.txt').write_text(
    '\n'.join(lines)+'\n')
