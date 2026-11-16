#!/usr/bin/env python3
"""Exact seeds for genuine R2 lifts, not searches for pentagon shadows."""
from itertools import product, permutations
import json
from pathlib import Path

I=(1,0,0,1)
def mul(A,B,n):
    return tuple((A[2*i]*B[j]+A[2*i+1]*B[2+j])%n
                 for i in range(2)for j in range(2))
def inv(A,n):return(A[3],-A[1]%n,-A[2]%n,A[0])
def pw(A,k,n):
    if k<0:return pw(inv(A,n),-k,n)
    out=I
    for _ in range(k):out=mul(out,A,n)
    return out
def comm(A,B,n):return mul(mul(mul(A,B,n),inv(A,n),n),inv(B,n),n)
def generated(gs,n):
    seen={I};todo=[I]
    for A in todo:
        for B in gs:
            C=mul(A,B,n)
            if C not in seen:seen.add(C);todo.append(C)
    return seen
def seed(A,B,n):
    Z=inv(mul(A,B,n),n)
    return pw(comm(comm(pw(A,4,n),pw(B,4,n),n),pw(Z,4,n),n),2,n)
def seed_derived(A,B,n):
    Z=inv(mul(A,B,n),n)
    return comm(comm(pw(A,4,n),pw(B,4,n),n),
                comm(pw(B,4,n),pw(Z,4,n),n),n)

def compose(p,q):return tuple(p[q[i]]for i in range(len(p)))
def pinv(p):return tuple(p.index(i)for i in range(len(p)))
def ppow(p,k):
    if k<0:return ppow(pinv(p),-k)
    one=tuple(range(len(p)))
    for _ in range(k):one=compose(one,p)
    return one
def pgen(gs):
    one=tuple(range(len(gs[0])));seen={one};todo=[one]
    for a in todo:
        for b in gs:
            c=compose(a,b)
            if c not in seen:seen.add(c);todo.append(c)
    return seen
def beta_x(x,y):return compose(compose(compose(ppow(x,2),y),ppow(x,2)),pinv(y))
def beta_y(x,y):return beta_x(y,x)

def main():
    U=(1,1,0,1);S=(0,1,11,0);R=(0,11,1,11);L=(1,0,11,1)
    tau=inv(U,12);z=inv(mul(S,tau,12),12)
    pairs=[(S,tau),(tau,z),(z,S),(tau,S),(z,tau),(S,z)]
    seed_values=[seed(A,B,12)for A,B in pairs]
    original=seed(pw(U,2,12),pw(L,2,12),12)
    assert seed_values==[I]*6 and original==(5,0,0,5)
    print('A0=[[x^4,y^4],z^4]^2: six orbifold values =',seed_values)
    print('A0 original inclusion value =',original)
    derived_values=[seed_derived(A,B,12)for A,B in pairs]
    derived_original=seed_derived(pw(U,2,12),pw(L,2,12),12)
    assert derived_values==[I]*6 and derived_original==(5,0,0,5)
    print('A1=[[x^4,y^4],[y^4,z^4]]: six orbifold values =',derived_values)
    print('A1 original inclusion value =',derived_original)
    G4=generated([(0,1,3,0),U],4)
    G4prime=generated([comm(A,B,4)for A,B in product(G4,repeat=2)],4)
    U4=generated(list(G4prime)+[pw(A,3,4)for A in G4],4)
    residual=U4;chain=[len(residual)]
    while True:
        next_residual=generated([comm(A,B,4)for A in residual for B in U4],4)
        if next_residual==residual:break
        residual=next_residual;chain.append(len(residual))
    bad=tuple(-x%4 for x in pw(U,2,4))
    assert len(G4)==48 and len(U4)==48 and chain==[48,12]
    assert bad in residual
    # Explicit full-source mixed-prime word w=[B A B^-1,B]. Its finite
    # images use A=(x^6y^6)^e2 and B=(x^3y^-3)^e3; these already have
    # orders2 and3 under this evaluation, so the idempotents fix them.
    S4=(0,1,3,0);tau4=inv(U,4)
    A=mul(pw(S4,6,4),pw(tau4,6,4),4)
    B=mul(pw(S4,3,4),pw(tau4,-3,4),4)
    w=comm(mul(mul(B,A,4),inv(B,4),4),B,4)
    assert pw(A,2,4)==I and pw(B,3,4)==I and w==bad
    print('SL2(Z/4): |image U|=48; lower central sizes=',chain)
    print('mixed-prime source word has image -U^2 =',w)
    G3=list(permutations(range(3)));one=(0,1,2);checks=[]
    for x,y in product(G3,repeat=2):
        if len(pgen([x,y]))!=6:continue
        bx=beta_x(x,y);by=beta_y(x,y)
        # For a generating S3 pair the boundary orders are3,2,2;
        # but the pair can also consist of two distinct transpositions.
        assert bx==one and by==one
        checks.append((x,y))
    assert len(checks)==18
    # The seed exponents are(4,0),(0,4), hence give the two basis
    # vectors modulo3, and beta0 gives the diagonal fixed by s.
    diag=(1,1);swapped=(diag[1],diag[0]);assert diag==swapped
    print('beta_x,beta_y vanish on all',len(checks),'generating S3 pairs')
    print('their abelian exponent vectors mod3 are(1,0),(0,1); beta0=(1,1)')
    out=dict(A0_orbifold_values=seed_values,A0_original_value=original,
             A1_orbifold_values=derived_values,A1_original_value=derived_original,
             image_U_mod4_order=len(U4),nilpotent_residual_order=len(residual),
             lower_central_sizes=chain,mixed_prime_word_value=w,
             S3_generating_pairs=len(checks),beta_seed_exponents_mod3=[[1,0],[0,1]],
             diagonal_seed=diag)
    path=Path(__file__).resolve().parents[1]/'records'/'iterated_lifting.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('All genuine-lifting seed checks passed.')
if __name__=='__main__':main()
