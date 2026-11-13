"""Exact F_3 Fox-module audit for the inert-prime calculation in E.59.

Let R=F_3[u,v]/(u^3,v^3), X=1+u, Y=1+v, and let
M=ker(R^2 -> R), (A,B) |-> uA+vB.  This is H_1(Phi P,F_3)
for the free pro-three group P on x,y, with its actual deck action.
The involution x |-> x, y |-> y^-1 acts on Fox vectors by
(A,B) |-> (A(X,Y^-1), -Y^-1 B(X,Y^-1)).

The program verifies the full fixed space, all 81 vectors in it, the
cyclic R-module ranks, explicit independent generators and annihilating
relations.  All operations are exact in F_3; no external package is used.
The accompanying E.59 proof gives the covering/Fox comparison maps.
"""
from itertools import product
from pathlib import Path
from collections import Counter
from fractions import Fraction
import json

P = 3
MONOMIALS = [(i,j) for i in range(3) for j in range(3)]
INDEX = {m:k for k,m in enumerate(MONOMIALS)}
ZERO = (0,)*9

def add(a,b):
    return tuple((x+y)%P for x,y in zip(a,b))

def scale(n,a):
    return tuple(n*x%P for x in a)

def mono(i,j):
    z = [0]*9
    if i<3 and j<3:
        z[INDEX[i,j]]=1
    return tuple(z)

ONE,U,V = mono(0,0),mono(1,0),mono(0,1)

def mul(a,b):
    z = [0]*9
    for k,(i,j) in enumerate(MONOMIALS):
        for l,(r,s) in enumerate(MONOMIALS):
            if i+r<3 and j+s<3:
                z[INDEX[i+r,j+s]] += a[k]*b[l]
    return tuple(x%P for x in z)

def power(a,n):
    z=ONE
    for _ in range(n):
        z=mul(z,a)
    return z

def substitute(a,u,v):
    z=ZERO
    for k,(i,j) in enumerate(MONOMIALS):
        z=add(z,scale(a[k],mul(power(u,i),power(v,j))))
    return z

def pairadd(a,b):
    return (add(a[0],b[0]),add(a[1],b[1]))

def pairscale(n,a):
    return (scale(n,a[0]),scale(n,a[1]))

def act(r,a):
    return (mul(r,a[0]),mul(r,a[1]))

def flat(a):
    return a[0]+a[1]

def boundary(a):
    return add(mul(U,a[0]),mul(V,a[1]))

V_INV=add(scale(2,V),mul(V,V))
Y_INV=add(ONE,V_INV)

def conjugation(a):
    return (substitute(a[0],U,V_INV),
            mul(scale(-1,Y_INV),substitute(a[1],U,V_INV)))

def rank(rows):
    rows=[list(r) for r in rows]
    pivot=0
    for col in range(len(rows[0]) if rows else 0):
        found=next((i for i in range(pivot,len(rows)) if rows[i][col]),None)
        if found is None:
            continue
        rows[pivot],rows[found]=rows[found],rows[pivot]
        rows[pivot]=[pow(rows[pivot][col],-1,3)*a%3 for a in rows[pivot]]
        for i in range(len(rows)):
            if i!=pivot and rows[i][col]:
                a=rows[i][col]
                rows[i]=[(x-a*y)%3 for x,y in zip(rows[i],rows[pivot])]
        pivot+=1
        if pivot==len(rows):
            break
    return pivot

R_BASIS=[mono(i,j) for i,j in MONOMIALS]
PAIR_BASIS=[(r,ZERO) for r in R_BASIS]+[(ZERO,r) for r in R_BASIS]
boundary_rank=rank([boundary(a) for a in PAIR_BASIS])
fixed_relation_rank=rank([boundary(a)+flat(pairadd(conjugation(a),pairscale(-1,a)))
                          for a in PAIR_BASIS])
assert boundary_rank==8
assert 18-fixed_relation_rank==4
assert all(conjugation(conjugation(a))==a for a in PAIR_BASIS)
assert all(boundary(conjugation(a))==substitute(boundary(a),U,V_INV)
           for a in PAIR_BASIS)
assert all(conjugation(act(r,a))==act(substitute(r,U,V_INV),conjugation(a))
           for r in R_BASIS for a in PAIR_BASIS)

AA=(mul(U,U),ZERO)
RAW_B=(scale(-1,mul(V,V)),mul(U,V))
BB=pairscale(2,pairadd(RAW_B,conjugation(RAW_B)))
assert BB==(scale(-1,mul(V,V)),add(mul(U,V),scale(-1,mul(U,mul(V,V)))))
FIXED_BASIS=[AA,BB,act(U,BB),act(mul(U,U),BB)]
assert rank([flat(a) for a in FIXED_BASIS])==4
assert all(boundary(a)==ZERO and conjugation(a)==a for a in FIXED_BASIS)

cases=[]
counts=Counter()
for A,B,C,D in product(range(3),repeat=4):
    w=(ZERO,ZERO)
    for c,a in zip((A,B,C,D),FIXED_BASIS):
        w=pairadd(w,pairscale(c,a))
    assert boundary(w)==ZERO and conjugation(w)==w
    uw,vw=act(U,w),act(V,w)
    uuw,uvw,vvw=act(mul(U,U),w),act(mul(U,V),w),act(mul(V,V),w)
    actual=rank([flat(act(r,w)) for r in R_BASIS])
    if B:
        predicted=5
        independent=[w,uw,vw,uuw,uvw]
        assert pairadd(pairscale(A,uuw),pairscale(B,vvw))==(ZERO,ZERO)
        assert all(act(mono(i,j),w)==(ZERO,ZERO)
                   for i,j in MONOMIALS if i+j>=3)
        annihilator="(u,v)^3 and A*u^2+B*v^2"
    elif A:
        predicted=3
        independent=[w,vw,vvw]
        assert pairadd(uw,pairscale(C*pow(A,-1,3),vvw))==(ZERO,ZERO)
        annihilator="u+(C/A)*v^2 and v^3"
    elif C:
        predicted=3
        independent=[w,uw,vw]
        assert all(act(mono(i,j),w)==(ZERO,ZERO)
                   for i,j in MONOMIALS if i+j>=2)
        annihilator="(u,v)^2"
    elif D:
        predicted=1
        independent=[w]
        assert uw==vw==(ZERO,ZERO)
        annihilator="(u,v)"
    else:
        predicted=0
        independent=[]
        assert w==(ZERO,ZERO)
        annihilator="R"
    assert actual==predicted==rank([flat(a) for a in independent])
    counts[actual]+=1
    cases.append({"coordinates":[A,B,C,D],"rank":actual,"annihilator":annihilator})

assert dict(counts)=={0:1,1:2,3:24,5:54}

# Actual Schreier/Fox basis for Phi(P), using representatives x^a y^b.
X,Y=add(ONE,U),add(ONE,V)
def geometric_sum(r,n):
    ans=ZERO
    for j in range(n):
        ans=add(ans,power(r,j))
    return ans

def representative_derivative(a,b):
    return (geometric_sum(X,a),mul(power(X,a),geometric_sum(Y,b)))

SCHREIER=[]
schreier_edges=[]
for a,b in product(range(3),repeat=2):
    for generator in ('x','y'):
        tree=(generator=='x' and b==0 and a<2) or (generator=='y' and b<2)
        if tree:
            continue
        qa,qb=((a+1)%3,b) if generator=='x' else (a,(b+1)%3)
        elementary=(ONE,ZERO) if generator=='x' else (ZERO,ONE)
        d=pairadd(representative_derivative(a,b),
                  act(mul(power(X,a),power(Y,b)),elementary))
        d=pairadd(d,pairscale(-1,representative_derivative(qa,qb)))
        assert boundary(d)==ZERO
        SCHREIER.append(d)
        schreier_edges.append([a,b,generator])
assert len(SCHREIER)==rank([flat(d) for d in SCHREIER])==10

# In the finite Magnus group, a rational Frobenius with chi mod9=-1
# has q=Y^b and involution component c.  Its square is T_b(D).
# Conjugation by y^b makes that square c-fixed and preserves its cyclic rank.
square_maps=[]
for b in range(3):
    yb=power(Y,b)
    def square_vector(d):
        return pairadd(d,act(yb,conjugation(d)))
    assert square_vector(representative_derivative(0,b))==(ZERO,ZERO)
    columns=[]
    for d in SCHREIER:
        normalized=act(yb,square_vector(d))
        expected=pairadd(act(yb,d),conjugation(act(yb,d)))
        assert normalized==expected
        assert boundary(normalized)==ZERO and conjugation(normalized)==normalized
        columns.append(flat(normalized))
    image_rank=rank(columns)
    assert image_rank==4
    square_maps.append({"b":b,"domain_dimension":10,"image_dimension":4,
                        "kernel_dimension":6,"fiber_order":3**6})

finite_group_order=2*3**12
cyclotomic_subset_order=3**11
fiber_order=3*3**6
finite_counts={r:n*fiber_order for r,n in counts.items()}
assert sum(finite_counts.values())==cyclotomic_subset_order
absolute_densities={r:str(Fraction(n,finite_group_order)) for r,n in finite_counts.items()}
assert absolute_densities=={0:'1/486',1:'1/243',3:'4/81',5:'1/9'}
assert sum(Fraction(x) for x in absolute_densities.values())==Fraction(1,6)
result={
  "ring":"F3[u,v]/(u^3,v^3)",
  "fox_boundary":"(A,B) -> u*A+v*B",
  "involution":"(A,B) -> (A(X,Y^-1),-Y^-1*B(X,Y^-1))",
  "monomial_order":[list(m) for m in MONOMIALS],
  "module_dimension":18-boundary_rank,
  "fixed_dimension":18-fixed_relation_rank,
  "fixed_basis":[{"first":a[0],"second":a[1]} for a in FIXED_BASIS],
  "checked_involution_columns":18,
  "checked_semilinear_identities":162,
  "case_count":len(cases),
  "rank_counts":dict(sorted(counts.items())),
  "schreier_basis_edges":schreier_edges,
  "schreier_basis_rank":10,
  "normalized_square_maps":square_maps,
  "finite_galois_group_order":finite_group_order,
  "cyclotomic_minus_one_subset_order":cyclotomic_subset_order,
  "preimages_per_fixed_vector":fiber_order,
  "finite_frobenius_rank_counts":dict(sorted(finite_counts.items())),
  "absolute_chebotarev_densities":dict(sorted(absolute_densities.items())),
  "relative_chebotarev_densities":{r:str(Fraction(n,81)) for r,n in sorted(counts.items())},
  "cases":cases,
  "all_checks_pass":True,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('Exact Fox module: dimension 10; involution fixed space dimension 4.')
print('Fixed basis: a=(u^2,0); b=(-v^2,uv-uv^2); u*b; u^2*b.')
print('Verified involution on 18 columns and 162 semilinear identities.')
print('All 81 fixed vectors: cyclic ranks 0:1, 1:2, 3:24, 5:54.')
print('For every case: exact independent generators and annihilating relations PASS.')
print('Actual Schreier basis: ten independent Fox vectors.')
print('All three normalized square maps: rank 4, kernel dimension 6.')
print('Finite cyclotomic subset: 177147 elements; 2187 preimages per fixed vector.')
print('Absolute Chebotarev rank densities: 0:1/486, 1:1/243, 3:4/81, 5:1/9.')
print('ALL CHECKS PASS')
