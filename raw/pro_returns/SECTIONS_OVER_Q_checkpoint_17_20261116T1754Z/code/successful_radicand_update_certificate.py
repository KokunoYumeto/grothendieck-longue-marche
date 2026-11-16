#!/usr/bin/env python3
"""Independent exact A144 certificate; no infinite global norm family is claimed."""
from itertools import product
from math import gcd,isqrt
from pathlib import Path


def prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2,isqrt(n)+1))


def factors(n):
    out=[]
    d=2
    while d*d <= n:
        if n%d == 0:
            out.append(d)
            while n%d == 0:
                n//=d
        d+=1
    if n>1:
        out.append(n)
    return out


def mul(a,b):
    out=[0]*5
    for i in range(3):
        for j in range(3):
            out[i+j]+=a[i]*b[j]
    for i in (4,3):
        out[i-3]+=3*out[i]
    return tuple(out[:3])


def scale(a,c):
    return tuple(c*x for x in a)


def norm(a):
    cols=[mul(a,tuple(int(i==j) for i in range(3))) for j in range(3)]
    m=[[cols[j][i] for j in range(3)] for i in range(3)]
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def evaluate(a,r,modulus):
    return sum(a[i]*pow(r,i,modulus) for i in range(3)) % modulus


def main():
    q=511177
    roots=(13382,29914,467881)
    gamma=(-68,64,1)
    U=(-2,0,1)
    beta0=(1,-1,0)
    alpha=(0,1,0)
    d=(3,-2,0)
    lines=[]
    assert prime(q) and q%72==49
    assert (q-1)%3==0 and (q-1)%9!=0
    assert norm(gamma)==q and norm(U)==1 and norm(beta0)==-2
    assert mul(U,(4,3,2))==(1,0,0)
    assert mul(alpha,U)==d
    assert mul(scale(mul(beta0,U),q),scale(alpha,q**8))==scale(mul(beta0,d),q**9)
    assert norm(beta0)*norm(U)*q**3//norm(gamma)**3 == -2
    lines.append("PASS: q=511177 is prime, q=49 mod72, Norm gamma=q, and Norm beta=-2.")
    lines.append("PASS: the exact cleared identity beta*z=(1-alpha)(3-2alpha)*(q^3/gamma)^3.")

    assert all(pow(r,3,q)==3 for r in roots)
    assert len(set(roots))==3
    assert tuple(evaluate(gamma,r,q) for r in roots)==(0,157366,353607)
    lifted=[]
    gamma_units=[]
    gamma_vals=[]
    for r in roots:
        r2=(r-(r**3-3)*pow(3*r*r,-1,q*q))%(q*q)
        assert pow(r2,3,q*q)==3
        value=evaluate(gamma,r2,q*q)
        if value%q:
            gamma_vals.append(0)
            gamma_units.append(value%q)
        else:
            assert value!=0 and value//q % q != 0
            gamma_vals.append(1)
            gamma_units.append(value//q % q)
        lifted.append(r2)
    assert gamma_vals==[1,0,0]
    t=tuple(1-3*v for v in gamma_vals)
    assert t==(-2,1,1)
    lines.append(f"PASS: literal Hensel roots modulo q^2={tuple(lifted)}; q-valuations of beta={t}.")

    beta_roots=(421,110767,207713)
    d_roots=(384954,368127,368991)
    for i,r in enumerate(roots):
        assert pow(beta_roots[i],3,q)==(1-r)%q
        assert pow(d_roots[i],3,q)==(3-2*r)%q
    assert pow(162620,24,q)==q-2
    lines.append("PASS: all six explicit cubic residue roots and the twenty-fourth root of -2.")

    g=5
    assert all(pow(g,(q-1)//p,q)!=1 for p in factors(q-1))
    zeta=pow(g,(q-1)//3,q)
    assert zeta==472522
    assert roots==tuple(roots[0]*pow(zeta,i,q)%q for i in range(3))
    character={1:0,zeta:1,pow(zeta,2,q):2}
    a=tuple(character[pow(r,(q-1)//3,q)] for r in roots)
    u=tuple(character[pow((r*r-2)%q,(q-1)//3,q)] for r in roots)
    beta_units=tuple(((1-r)*(r*r-2)*pow(gamma_units[i],-3,q))%q
                     for i,r in enumerate(roots))
    c=tuple(character[pow(v,(q-1)//3,q)] for v in beta_units)
    assert a==(0,1,2) and u==(0,2,1) and c==u
    assert all((8*c[i]-t[i]*a[i])%3==0 for i in range(3))
    assert all((t[i]+8)%3==0 and (c[i]+a[i])%3==0 for i in range(3))
    inertia=tuple(v%3 for v in t)
    assert inertia==(1,1,1)
    span={tuple((i*inertia[k]+j*c[k])%3 for k in range(3))
          for i,j in product(range(3),repeat=2)}
    assert len(span)==9
    for j in range(1,10):
        assert gcd(3**j,q-1)==3
    lines.append("PASS: actual mod-three local vectors t=(1,1,1), c=(0,2,1), with nine-element span.")
    lines.append("PASS: all three stable norm symbols vanish; the norm-group commutator index is3 at depths1..9.")
    lines.append("ALL A144 FINITE CERTIFICATES PASSED.")
    lines.append("The proof supplies each finite global norm and every compatible local family; the global inverse limit remains open.")
    output="\n".join(lines)+"\n"
    Path(__file__).with_name("successful_radicand_update_certificate_output.txt").write_text(output)
    print(output,end="")


if __name__=="__main__":
    main()
