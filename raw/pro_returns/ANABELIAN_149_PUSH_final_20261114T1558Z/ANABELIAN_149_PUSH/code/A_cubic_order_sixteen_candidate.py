#!/usr/bin/env python3
"""Exact Bezout certificate for the proposed universal order-sixteen exclusion.

This is a candidate until the geometric parametrization in the accompanying
audit note is independently reviewed.  The program proves its algebraic
elimination assertions by saving and checking Bezout identities, not by
sampling parameters.  SymPy is used for exact polynomial arithmetic over F2.
"""
import json
from pathlib import Path
import sympy as S

v,x,z=S.symbols('v x z')
D=S.GF(2).frac_field(v)
PHI=S.Poly(v**4+v**3+v**2+v+1,v,modulus=2)


def coefficients(poly):
    return [int(poly.nth(i))%2 for i in range(poly.degree()+1)] if not poly.is_zero else [0]


def serialize_x(poly):
    out=[]
    for i in range(poly.degree()+1):
        num,den=S.fraction(poly.nth(i))
        out.append({'numerator':coefficients(S.Poly(num,v,modulus=2)),
                    'denominator':coefficients(S.Poly(den,v,modulus=2))})
    return out


def strip_allowed(poly):
    out=poly
    for factor,root in ((v,0),(v+1,1)):
        while out.eval(root)==0:
            out=S.exquo(out,S.Poly(factor,v,modulus=2))
    return out.monic()


def bezout_obstruction(left,right):
    u,w,g=S.gcdex(left,right)
    assert g==S.Poly(1,x,domain=D)
    denominator=S.Poly(1,v,modulus=2)
    for pol in (u,w):
        for co in pol.all_coeffs():
            _,den=S.fraction(co)
            denominator=S.lcm(denominator,S.Poly(den,v,modulus=2))
    U=u.mul_ground(D.from_sympy(denominator.as_expr()))
    W=w.mul_ground(D.from_sympy(denominator.as_expr()))
    assert U*left+W*right==S.Poly(denominator.as_expr(),x,domain=D)
    assert all(S.fraction(c)[1]==1 for pol in (U,W) for c in pol.all_coeffs())
    return strip_allowed(denominator),{'U':serialize_x(U),'W':serialize_x(W),
            'right_hand_side':coefficients(denominator),
            'identity':'U*P0+W*Pi=right_hand_side in F2(v)[x]'}


def family(a,b):
    r=v**4;t=r*r
    l3=r+a;l2=r+(a^b);l1=a^b
    n1=(v*v+a)/v**4
    square=D.from_sympy((l3*n1*n1+l2+n1*n1+n1)/t)
    assert all(i[0]%2==0 for p in (square.numer,square.denom) for i,c in p.terms())
    m1=sum(v**(i[0]//2) for i,c in square.numer.terms())/sum(v**(i[0]//2) for i,c in square.denom.terms())
    if l1==0:
        m0=((b^1)*x*x+m1*x)/n1
    else:
        m0=((l2*(b^1)+1)*x*x+l2*m1*x+b*m1*m1+n1*n1+x+m1*n1)/(l2*n1)
    T1=x*x+m1*x+m0*n1
    C4=t*m0*m0+l3*x*x+l2*m1*m1+l1*n1*n1+b+T1
    C0=b*m0*m0+x*x+m0*x
    expr=[t*x*x+l3*m1*m1+l2*n1*n1+l1+n1*n1+x+m1*n1,
          l2*m0*m0+l1*x*x+b*m1*m1+n1*n1+x+m1*n1,
          l3*m0*m0+(l2+1)*x*x+l1*m1*m1+b*n1*n1+m0*x+n1*n1+n1,
          C4*C4+t*C0]
    polynomials=[S.Poly(e,x,domain=D) for e in expr]
    # Independently re-expand the binary quadratic form to check all indexing.
    to_x=lambda e:S.Poly(e,x,domain=D)
    zero=to_x(0)
    def plus(left,right):
        return [(left[i] if i<len(left) else zero)+(right[i] if i<len(right) else zero)
                for i in range(max(len(left),len(right)))]
    def times(left,right):
        out=[zero]*(len(left)+len(right)-1)
        for i,c in enumerate(left):
            for j,d in enumerate(right):out[i+j]=out[i+j]+c*d
        return out
    L0=list(map(to_x,[b,l1,l2,l3,t]));M=list(map(to_x,[m0,m1,1]))
    N=list(map(to_x,[x,n1]));H=list(map(to_x,[1,0,0,1]));N2=times(N,N)
    form=plus(times(L0,plus(times(list(map(to_x,[0,1])),N2),times(M,M))),
              times(H,plus(times(list(map(to_x,[1,1])),N2),times(M,N))))
    assert form[8]==to_x(t)
    assert form[7].is_zero and form[6].is_zero
    assert form[5]==polynomials[0] and form[2]==polynomials[1] and form[3]==polynomials[2]
    assert form[4]**2+to_x(t)*form[0]==polynomials[3]
    if l1==0:assert form[1].is_zero
    else:assert (to_x(l2)*form[1]+form[2]).is_zero
    return polynomials,m0,m1,n1


def field_multiply(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&16:a^=31
    return out


def field_power(a,n):
    out=1
    while n:
        if n&1:out=field_multiply(out,a)
        a=field_multiply(a,a);n//=2
    return out


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,q in enumerate(a):c[i]^=q
    for i,q in enumerate(b):c[i]^=q
    return trim(c)


def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,q in enumerate(a):
        for j,r in enumerate(b):c[i+j]^=field_multiply(q,r)
    return trim(c)


def scale(a,b):return trim([field_multiply(q,b) for q in a])


def divide(a,b):
    a=trim(a);b=trim(b);assert b!=[0]
    q=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        d=len(a)-len(b);c=field_multiply(a[-1],field_power(b[-1],14));q[d]^=c
        a=add(a,[0]*d+scale(b,c))
    return trim(q),a


def xgcd(a,b):
    aa,bb=a,b;u0,u1=[1],[0];w0,w1=[0],[1]
    while b!=[0]:
        q,r=divide(a,b);a,b=b,r
        u0,u1=u1,add(u0,multiply(q,u1));w0,w1=w1,add(w0,multiply(q,w1))
    factor=field_power(a[-1],14)
    a,u0,w0=scale(a,factor),scale(u0,factor),scale(w0,factor)
    assert add(multiply(u0,aa),multiply(w0,bb))==a
    return a,u0,w0


def reduce_coefficient(expr):
    num,den=S.fraction(expr)
    n=S.rem(S.Poly(num,v,modulus=2),PHI)
    d=S.rem(S.Poly(den,v,modulus=2),PHI)
    assert not d.is_zero
    c=S.rem(n*S.invert(d,PHI),PHI)
    return sum((int(c.nth(i))%2)<<i for i in range(4))


def evaluate(poly,a):
    out=0
    for c in reversed(poly):out=field_multiply(out,a)^c
    return out


def main():
    cases=[];exception=None
    for a,b in ((0,0),(1,0),(0,1),(1,1)):
        print(f'Checking universal conic case a={a}, b={b}',flush=True)
        ps,m0,m1,n1=family(a,b)
        o1,c1=bezout_obstruction(ps[0],ps[1]);o2,c2=bezout_obstruction(ps[0],ps[2])
        U,W,g=S.gcdex(o1,o2)
        assert U*o1+W*o2==g
        expected=PHI if (a,b)==(0,1) else S.Poly(1,v,modulus=2)
        # The obstruction can carry a repeated factor; its radical is enough.
        assert g.monic()==expected or g.monic()==expected**2
        case={'a':a,'b':b,'P':list(map(serialize_x,ps)),
              'm0':serialize_x(S.Poly(m0,x,domain=D)),
              'm1':str(m1),'n1':str(n1),
              'obstruction_1':coefficients(o1),'obstruction_2':coefficients(o2),
              'bezout_1':c1,'bezout_2':c2,
              'combined_bezout_U':coefficients(U),'combined_bezout_W':coefficients(W),
              'combined_gcd':coefficients(g)}
        cases.append(case)
        if (a,b)==(0,1):exception=(ps,m0,m1,n1)
    assert all(field_power(a,15)==1 for a in range(1,16))
    ps,m0,m1,n1=exception
    fps=[[reduce_coefficient(p.nth(i)) for i in range(p.degree()+1)] for p in ps]
    d,u,w=xgcd(fps[0],fps[1]);g,e,f=xgcd(d,fps[2])
    row=[multiply(e,u),multiply(e,w),f]
    assert add(add(multiply(row[0],fps[0]),multiply(row[1],fps[1])),multiply(row[2],fps[2]))==g
    assert g==[10,1] # x+v^3+v in F2[v]/Phi5(v).
    assert all(divide(p,g)[1]==[0] for p in fps)
    n0=10;m0v=evaluate([reduce_coefficient(S.Poly(m0,x,domain=D).nth(i)) for i in range(3)],n0)
    m1v=reduce_coefficient(m1);n1v=reduce_coefficient(n1)
    assert (m0v,m1v,n1v)==(11,6,8)
    common=field_multiply(n0,field_power(n1v,14))
    assert common==9
    assert evaluate([m0v,m1v,1],common)==evaluate([n0,n1v],common)==0
    result={'status':'candidate geometric reduction; all algebraic identities verified','all_passed':True,
            'cases':cases,'exceptional_field':'F2[v]/(v4+v3+v2+v+1)',
            'exceptional_P_coefficients':fps,'exceptional_bezout_row':row,'exceptional_common_gcd':g,
            'exceptional_n0':n0,'exceptional_m0':m0v,'exceptional_m1':m1v,'exceptional_n1':n1v,
            'common_root_of_M_and_N':common,
            'conclusion':'Every surviving algebraic candidate has M,N with a common root, violating the reduced rational parametrization.'}
    output=json.dumps(result,indent=2,sort_keys=True)+'\n'
    Path(__file__).with_suffix('.json').write_text(output)
    print(json.dumps({k:v for k,v in result.items() if k not in ('cases','exceptional_P_coefficients','exceptional_bezout_row')},indent=2,sort_keys=True))


if __name__=='__main__':main()
