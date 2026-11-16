"""Independent exact support and dyadic-square audit of the Fisher pairing.

This verifies the finite omitted-prime justification and direct Hensel
witnesses at two.  Local solubility of the second and third quartics and
the full Selmer bound are separate obligations.
"""
from fractions import Fraction as Q
from pathlib import Path
import json,math

base=Path(__file__).resolve().parent
data=json.loads((base/'harmonic_prym_fisher_local_certificate_data.json').read_text())
def pair(z):return tuple(Q(a) for a in z)
def add(z,w):return z[0]+w[0],z[1]+w[1]
def mul(z,w):return z[0]*w[0]+2*z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def neg(z):return -z[0],-z[1]
def power(z,n):
    if n<0:
        norm=z[0]*z[0]-2*z[1]*z[1]
        return power((z[0]/norm,-z[1]/norm),-n)
    r=(Q(1),Q(0))
    while n:
        if n&1:r=mul(r,z)
        z=mul(z,z);n//=2
    return r
def norm(z):return z[0]*z[0]-2*z[1]*z[1]
def vp_int(n,p):
    if n==0:return 10000
    n=abs(n);v=0
    while n%p==0:n//=p;v+=1
    return v
def vp_rat(a,p):return vp_int(a.numerator,p)-vp_int(a.denominator,p)
def vpi(z):return min(2*vp_rat(z[0],2),2*vp_rat(z[1],2)+1)
original=list(map(pair,data['gamma_original']))
primitive=list(map(pair,data['gamma_primitive']))
bezout=list(map(pair,data['bezout']))
content=pair(data['content']);character=pair(data['character'])
assert all(mul(content,z)==a for z,a in zip(primitive,original))
assert all(a.denominator==1 for z in primitive+bezout for a in z)
total=(Q(0),Q(0))
for a,b in zip(bezout,primitive):total=add(total,mul(a,b))
assert total==(1,0)

finite={row['p'] for row in data['local_rows'] if 'p' in row}
def covered(n):
    n=abs(n)
    assert n
    for p in finite:
        while n%p==0:n//=p
    assert n==1,n
N=norm(character)
covered(N.numerator);covered(N.denominator)
D=math.lcm(*(a.denominator for a in character));covered(D)
assert D==math.prod(int(p)**e for p,e in data['character_component_denominator'].items())
M=7*13*23*139*1119169
b=(Q(3*1146*M*M),Q(2*1146*M*M))
small_coefficient=mul((Q(-4,1119169),Q(0)),b)
assert all(a.denominator==1 for a in small_coefficient)
# The ordinary polynomial discriminant of r-(4b/r)u^4 is -2^14 b^3.
discriminant=mul((Q(-(2**14)),Q(0)),power(b,3))
covered(norm(discriminant).numerator)
assert norm(discriminant).denominator==1
assert {2,3,5,7}<=finite

dyadic=[]
for name,z in [('Hilbert character',character),('primitive gamma at zero',primitive[0]),
               ('first quartic at zero',(Q(1119169),Q(0)))]:
    val=vpi(z);assert val%2==0
    unit=mul(z,power((Q(0),Q(1)),-val))
    witness=None
    for w in [(Q(1),Q(0)),(Q(1),Q(1))]:
        error=add(unit,neg(mul(w,w)))
        depth=vpi(error)
        if depth>=5:
            derivative_depth=vpi(mul((Q(2),Q(0)),w))
            assert depth>2*derivative_depth
            witness=dict(name=name,valuation=val,unit_root=[str(a) for a in w],
                         error_depth=depth,derivative_depth=derivative_depth)
            break
    assert witness is not None,name
    dyadic.append(witness)

negative=[row for row in data['local_rows'] if row['hilbert']==-1]
assert [(row['p'],row['root']) for row in negative]==[(41,17),(139,None),(38709401,15703973)]
assert math.prod(row['hilbert'] for row in data['local_rows'])==-1
report=dict(primitive_integral_bezout=True,content_identity=True,
            finite_support=sorted(finite),character_denominator=D,
            discriminant_support_covered=True,direct_dyadic_hensel=dyadic,
            remaining_obligations=['Local solubility of both larger quartics','Independent full2-Selmer upper bound'])
(base/'harmonic_prym_fisher_support_audit_data.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: exact global-content identity and integral Bezout identity1.')
print('PASS: every prime dividing the character numerator norm, denominator norm, or component denominator is included.')
print('PASS: all first-quartic discriminant primes and every residue characteristic below11 are included.')
for row in dyadic:print('Direct dyadic square witness:',row)
print('Outside this support the integral primitive quadratic has at most four zero points on the smooth genus-one reduction.')
print('For residue size q>=11 the proved point bound exceeds4; smooth lifting gives a unit value and Hilbert symbol+1.')
print('PASS: the retained local table has exactly the three stated negative symbols and product-1.')
print('No conclusion about the unresolved Selmer upper bound or other two quartics is inferred by this audit.')
