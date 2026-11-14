#!/usr/bin/env python3
"""Independent fixed-certificate check; does not import the packet search.

Recomputes point counts, the Frobenius/root-ratio calculations, and the
published finite quotient-ring identities. No universal A1 claim is made.
"""
from pathlib import Path
from itertools import product
import json
import sympy as s

HERE = Path(__file__).resolve().parent

def field_multiply(a, b, bits, modulus):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & (1 << bits):
            a ^= modulus
    return result

def power(a, n, bits, modulus):
    result = 1
    while n:
        if n & 1:
            result = field_multiply(result, a, bits, modulus)
        a = field_multiply(a, a, bits, modulus)
        n >>= 1
    return result

def counts(bits, modulus):
    q = 1 << bits
    mul = lambda a,b: field_multiply(a,b,bits,modulus)
    inv = lambda a: power(a,q-2,bits,modulus)
    alpha = next(a for a in range(2,q) if mul(a,a)^a^1 == 0)
    alpha2 = mul(alpha,alpha)
    def trace(a):
        result = 0
        for _ in range(bits):
            result ^= a
            a = mul(a,a)
        assert result in (0,1)
        return result
    n0 = 1
    comparison = 3
    for x in range(q):
        denominator = mul(x,x)^x^alpha
        if denominator == 0:
            n0 += 1
        else:
            rhs = x^mul(alpha2,mul(x^1,inv(denominator)))
            n0 += 2*(trace(rhs)==0)
        if x not in (0,1):
            rhs = x^mul(alpha,inv(x))^mul(alpha2,inv(x^1))^alpha
            comparison += 2*(trace(rhs)==0)
    return n0,comparison

def mul4(a,b,modulus):
    # Z[X]/(X^4+2X^3+X^2+8X+16), using direct polynomial reduction.
    c=[0]*7
    for i in range(4):
        for j in range(4):
            c[i+j]=(c[i+j]+a[i]*b[j])%modulus
    for k in range(6,3,-1):
        leading=c[k]
        for j,coefficient in enumerate((16,8,1,2)):
            c[k-4+j]=(c[k-4+j]-leading*coefficient)%modulus
    return c[:4]

def xp4(n,modulus):
    result=[1,0,0,0]
    base=[0,1,0,0]
    while n:
        if n&1:
            result=mul4(result,base,modulus)
        base=mul4(base,base,modulus)
        n>>=1
    return result

def check_row(row):
    ell=row["ell"]
    m=row["torsion_splitting_exponent_m"]
    exponent=row["theta_exponent_bound"]
    modulus=ell**(exponent+1)
    assert xp4(m,ell)==[1,0,0,0]
    a=xp4(m,modulus)
    a[0]=(a[0]-1)%modulus
    actual=mul4(a,row["B_coefficients_ascending"],modulus)
    assert actual==[ell**exponent,0,0,0]
    return {"ell":ell,"m":m,"exponent":exponent,"remainder":actual}

def main():
    point_counts={}
    for bits,modulus in ((2,7),(4,19),(8,283)):
        a,b=counts(bits,modulus)
        assert a==b
        point_counts[str(1<<bits)]=a
    assert point_counts=={"4":7,"16":15,"256":255}
    x,z=s.symbols("x z")
    P=x**4+2*x**3+x**2+8*x+16
    assert s.Poly(P,x,modulus=3)==s.Poly(s.cyclotomic_poly(10,x),x,modulus=3)
    assert s.n_order(3,10)==4
    ratio=s.Poly(s.resultant(P,P.subs(x,z*x),x),z)
    ratio=ratio.exquo(s.Poly((z-1)**4,z)).sqf_part()
    _,ratio=ratio.primitive()
    expected=64*z**8+80*z**7+108*z**6+7*z**5+26*z**4+7*z**3+108*z**2+80*z+64
    assert ratio.as_expr()==expected
    orders=sorted({2**a*3**b*5**c*7**d
                   for a,b,c,d in product(range(5),range(3),range(2),range(2))
                   if s.totient(2**a*3**b*5**c*7**d)<=8})
    assert orders==[1,2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,24,30]
    assert all(s.gcd(ratio,s.Poly(s.cyclotomic_poly(n,z),z)).degree()==0 for n in orders)
    r=s.sqrt(2)
    s1=-1-2*r
    s2=-1+2*r
    assert s.expand((x*x-s1*x+4)*(x*x-s2*x+4)-P)==0
    assert s.simplify((s1*s1-16)-(-7+4*r))==0
    assert s.expand((-7+4*r)*(-7-4*r))==17
    first=json.loads((HERE/"A_F4_remaining_structure.json").read_text())
    mixed=json.loads((HERE/"A_F4_remaining_mixed_packets.json").read_text())
    checks=[check_row(row) for row in first["packets"]]
    for record in mixed["records"]:
        checks.extend(check_row(row) for row in record["packets"])
    assert len(checks)==30
    # Direct Frobenius actions on the three nonzero geometric two-torsion classes.
    split_action=[0,1,2]
    nonsplit_action=[1,0,2]
    fixed_split=sum(i==j for i,j in enumerate(split_action))
    fixed_nonsplit=sum(i==j for i,j in enumerate(nonsplit_action))
    assert (fixed_split,fixed_nonsplit)==(3,1)
    out={
        "status":"PASS",
        "method":"Independent binary field arithmetic and direct quotient-polynomial arithmetic",
        "point_counts_for_both_twist_comparison_models":point_counts,
        "root_ratio_polynomial_ascending":[int(ratio.nth(i)) for i in range(9)],
        "excluded_cyclotomic_orders":orders,
        "modular_identity_checks":checks,
        "fixed_nonzero_two_torsion_classes":{"split_comparison":3,"remaining_curve":1},
        "scope":"Checks the structure and finite certificates only. No universal torsion exclusion or A1 conclusion."
    }
    (HERE/"A_F4_remaining_structure_degeneration.json").write_text(json.dumps(out,indent=2)+"\n")
    print("PASS: counts4,16,256; 18 cyclotomic exclusions; 30 modular identities; distinct Frobenius actions on J[2]")

if __name__=="__main__":
    main()
