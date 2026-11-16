"""Exact necessary dyadic two-isogeny descent conditions.

K_2=Q_2(sqrt(2)), O=Z_2[sqrt(2)], pi=sqrt(2).
For E_b:y^2=x^3+b*x, the squareclass d of x has quartic
N^2=d U^4+(b/d)V^4.  Every field point has a primitive integral
(U,V), covered by U=1 or V=1 with U nonunit.  Reduction modulo
pi^L therefore gives a rigorous necessary condition.

The program only asserts finite congruence exclusions.  It does
not infer local solubility or a Mordell-Weil rank from surviving
residue classes.
"""
from itertools import product
from pathlib import Path
import json

BASE=Path(__file__).resolve().parent
M=7*13*23*139*1119169
B=(3*1146*M*M,2*1146*M*M)

def ring(L):
    ma,mb=2**((L+1)//2),2**(L//2)
    def red(z): return (z[0]%ma,z[1]%mb)
    def add(z,w): return red((z[0]+w[0],z[1]+w[1]))
    def mul(z,w): return red((z[0]*w[0]+2*z[1]*w[1],z[0]*w[1]+z[1]*w[0]))
    def inv(z):
        assert z[0]%2
        d=pow((z[0]*z[0]-2*z[1]*z[1])%ma,-1,ma)
        return red((d*z[0],-d*z[1]))
    vals=list(product(range(ma),range(mb)))
    return red,add,mul,inv,vals

red5,add5,mul5,inv5,vals5=ring(5)
sq_units={(1,0),(3,2)}
units=[u for u in vals5 if u[0]%2]
def canonical_unit(u):
    return min(mul5(red5(u),s) for s in sq_units)
unit_reps=sorted({canonical_unit(u) for u in units})
assert len(unit_reps)==8
assert {mul5(u,u) for u in units}==sq_units
classes=[(e,u) for e in range(2) for u in unit_reps]

def class_key(e,u): return f"{e}:{u[0]}:{u[1]}"
def v2(n):
    if not n: return 10**9
    n=abs(n); return (n&-n).bit_length()-1
def local_class(z):
    a,b=z
    v=min(2*v2(a),2*v2(b)+1)
    assert v<10**9
    for _ in range(v):
        assert a%2==0
        a,b=b,a//2
    assert a%2
    return class_key(v%2,canonical_unit((a,b)))

def test(sign,L):
    red,add,mul,inv,vals=ring(L)
    b=tuple(sign*x for x in B)
    squares={}
    for z in vals: squares.setdefault(mul(z,z),z)
    fourths=[(z,mul(mul(z,z),mul(z,z))) for z in vals]
    nonunit_fourths=[z for z in fourths if z[0][0]%2==0]
    answer={}
    for e,u in classes:
        d=u if not e else (2*u[1],u[0])
        bdivpi=b if not e else (b[1],b[0]//2)
        quotient=mul(red(bdivpi),inv(red(u)))
        d=red(d)
        witness=None
        for V,V4 in fourths:
            rhs=add(d,mul(quotient,V4))
            if rhs in squares:
                witness={"U":[1,0],"V":V,"N":squares[rhs]}
                break
        if witness is None:
            for U,U4 in nonunit_fourths:
                rhs=add(mul(d,U4),quotient)
                if rhs in squares:
                    witness={"U":U,"V":[1,0],"N":squares[rhs]}
                    break
        answer[class_key(e,u)]=witness
    return answer

data={"M":M,"B":B,"unit_square_residues_mod_pi5":sorted(sq_units),
      "unit_representatives":unit_reps,"precision_results":{}}
for sign in [1,-1]:
    previous=set(class_key(e,u) for e,u in classes)
    for L in [5,7,9,11,13]:
        ans=test(sign,L)
        surviving={k for k,v in ans.items() if v is not None}
        assert surviving<=previous
        previous=surviving
        data["precision_results"][f"{sign}:{L}"]=ans
        print("sign",sign,"precision",L,"surviving",len(surviving),sorted(surviving))

data["local_class_examples"]={
    "-1":local_class((-1,0)),
    "epsilon":local_class((1,1)),
    "pi":local_class((0,1)),
    "b":local_class(B),
    "-b":local_class(tuple(-x for x in B)),
}
(BASE/"harmonic_prym_dyadic_filter_data.json").write_text(json.dumps(data,indent=2))
print("PASS: finite necessary congruence filters, including primitive integral charts.")
print("No rank or local-solubility conclusion is inferred from surviving classes.")
