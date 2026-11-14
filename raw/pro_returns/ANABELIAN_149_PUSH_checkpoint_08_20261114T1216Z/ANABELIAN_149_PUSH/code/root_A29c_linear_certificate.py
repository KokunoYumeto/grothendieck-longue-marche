#!/usr/bin/env python3
"""Independent Riemann--Roch linear certificate for the A.29c finite packet.

No Jacobian addition, Mumford reduction, or Cantor formula is used here.
For non-Weierstrass P and Q=delta(P), 8(P-Q) is principal exactly when
the 13-dimensional space L(16 infinity) contains a nonzero numerator
vanishing to order at least eight at P and at iota(Q).  Dividing by
(s-s(Q))^8 then gives the requested principal divisor.  The space has
basis 1,s,...,s^8,Y,sY,s^2Y,s^3Y, since poles of s and Y have orders
two and nine and the curve has genus four.  The sixteen jet equations
must therefore have rank thirteen to exclude the claimed torsion.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json

SIZE=4096
MOD=0x1009
def raw_mul(a,b):
    z=0
    while b:
        if b&1: z^=a
        b>>=1
        a<<=1
        if a&SIZE: a^=MOD
    return z

exp=[1]
for _ in range(SIZE-2): exp.append(raw_mul(exp[-1],3))
assert len(set(exp))==SIZE-1 and raw_mul(exp[-1],3)==1
log={a:i for i,a in enumerate(exp)}
def mul(a,b): return exp[(log[a]+log[b])%(SIZE-1)] if a and b else 0
def power(a,n): return 1 if n==0 else (exp[(log[a]*n)%(SIZE-1)] if a else 0)
def inverse(a):
    assert a
    return exp[-log[a]%(SIZE-1)]
c=min(a for a in range(SIZE) if raw_mul(a,a)^a^1==0)
assert c==72

def shifted_monomial(a,n,length=8):
    return [power(a,n-j) if j<=n and j&~n==0 else 0 for j in range(length)]
def shifted_polynomial(a,coefficients):
    result=[0]*8
    for n,b in enumerate(coefficients):
        for j,z in enumerate(shifted_monomial(a,n)):
            result[j]^=mul(b,z)
    return result
H=[c,0,0,1]
F=[c,0,0,1,0,0,c,0,0,1]

def jet_basis(a,y0):
    h=shifted_polynomial(a,H)
    f=shifted_polynomial(a,F)
    assert h[0] and mul(y0,y0)^mul(h[0],y0)==f[0]
    y=[y0]
    for n in range(1,8):
        value=f[n]
        if n%2==0: value^=mul(y[n//2],y[n//2])
        for j in range(1,n+1): value^=mul(h[j],y[n-j])
        y.append(mul(value,inverse(h[0])))
    # Verify the equation through all eight coefficients independently.
    for n in range(8):
        value=mul(y[n//2],y[n//2]) if n%2==0 else 0
        for j in range(n+1): value^=mul(h[j],y[n-j])
        assert value==f[n]
    columns=[shifted_monomial(a,n) for n in range(9)]
    for n in range(4):
        m=shifted_monomial(a,n)
        out=[]
        for j in range(8):
            value=0
            for i in range(j+1): value^=mul(m[i],y[j-i])
            out.append(value)
        columns.append(out)
    return [[column[j] for column in columns] for j in range(8)]

def matrix_rank(rows):
    a=[row[:] for row in rows]
    r=0
    for col in range(13):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        factor=inverse(a[r][col])
        a[r]=[mul(factor,z) for z in a[r]]
        for i in range(r+1,len(a)):
            factor=a[i][col]
            if factor:
                a[i]=[x^mul(factor,z) for x,z in zip(a[i],a[r])]
        r+=1
    return r

def main():
    solutions={}
    for y in range(SIZE): solutions.setdefault(raw_mul(y,y)^y,[]).append(y)
    assert len(solutions)==2048 and all(len(v)==2 for v in solutions.values())
    seen=set()
    ranks=Counter()
    digest=hashlib.sha256()
    total=1
    for s in range(SIZE):
        h=power(s,3)^c
        if not h:
            total+=1
            continue
        ys=solutions.get(h^mul(c,inverse(h)),[])
        total+=len(ys)
        if not ys or not s or s in seen: continue
        seen.update({s,mul(c,s),mul(mul(c,c),s)})
        y=mul(h,ys[0])
        q=mul(c,s)
        matrix=jet_basis(s,y)+jet_basis(q,y^h)
        for row in matrix:
            for entry in row: digest.update(entry.to_bytes(2,'little'))
        rank=matrix_rank(matrix)
        ranks[rank]+=1
        assert rank==13,(s,y,rank)
    assert total==4206 and dict(ranks)=={13:700}
    result={
        'claim':'A.29c',
        'method':'Independent Riemann--Roch jet linear algebra; no divisor-addition algorithm',
        'field_modulus':'t^12+t^3+1',
        'primitive_generator':'t+1',
        'c':c,
        'points_including_infinity':total,
        'matrix_shape':[16,13],
        'nonexceptional_delta_and_hyperelliptic_orbits':700,
        'rank_histogram':dict(ranks),
        'matrix_entries_sha256':digest.hexdigest(),
        'exceptions':'s=0 and infinity are delta-fixed; the three finite Weierstrass points have order-two differences, proved geometrically',
        'all_passed':True,
    }
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text,end='')

if __name__=='__main__': main()
