#!/usr/bin/env python3
"""Independent Kummer-line verification of the two division polynomials.

Reads python-flint from the geometric agent's installed dependency directory;
writes only this agent's JSON.  It does not rerun the certificate producer.
"""
from functools import cache
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] /
                       "agent_geometric" / "native"))
from flint import nmod_poly

x=nmod_poly([0,1],2)
one=nmod_poly([1],2)

@cache
def kummer(n):
    if n==1:
        return x,one
    if n%2==0:
        a,b=kummer(n//2)
        return a**4,b**4
    m=n//2
    a,b=kummer(m)
    c,d=kummer(m+1)
    s=a*d+c*b
    t=b*d
    top=x*s*s+t*t
    bottom=s*s
    common=top.gcd(bottom)
    top=top//common
    bottom=bottom//common
    assert top.gcd(bottom)==one
    return top,bottom

@cache
def division(n):
    if n==0:return nmod_poly([],2)
    if n in (1,2,4):return one
    if n==3:return x**4+x
    m=n//2
    if n%2==0:return division(m)**4
    return division(m+2)*division(m)**3+division(m-1)*division(m+1)**3

def pmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1;b>>=1
    return r

def pmod(a,b):
    while a.bit_length()>=b.bit_length():
        a^=b<<(a.bit_length()-b.bit_length())
    return a

def pgcd(a,b):
    while b:a,b=b,pmod(a,b)
    return a

def main():
    modulus=sum(1<<j for j in (0,1,2,5,8,9,10,14,38))
    sq=[2]
    for _ in range(38):sq.append(pmod(pmul(sq[-1],sq[-1]),modulus))
    assert sq[38]==2
    assert pgcd(sq[19]^2,modulus)==1
    assert pgcd(sq[2]^2,modulus)==1
    rows=[]
    for n in (191,229):
        a,b=kummer(n)
        psi=division(n)
        assert b==psi*psi
        assert a.degree()==n*n
        assert b.degree()==n*n-1
        assert psi.gcd(psi.derivative())==one
        rows.append({"n":n,"kummer_numerator_degree":a.degree(),
                     "kummer_denominator_degree":b.degree(),
                     "division_degree":psi.degree(),
                     "denominator_equals_division_square":True,
                     "division_squarefree":True})
    out={"status":"all independent exact assertions passed",
         "field_modulus_rabin_irreducible":True,"field_modulus":modulus,
         "tests":rows}
    Path(__file__).with_name("elliptic_torsion_polynomial_review_output.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out))

if __name__=="__main__":main()
