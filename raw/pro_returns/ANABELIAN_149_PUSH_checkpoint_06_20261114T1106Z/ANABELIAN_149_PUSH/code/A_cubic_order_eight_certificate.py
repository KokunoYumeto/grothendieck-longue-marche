#!/usr/bin/env python3
"""Exact universal coefficient identities for the order-eight exclusion.

The proof giving these norm equations from principal divisors is in A.29e
and audit/A_ordinary_auxiliary_packet.md.  This certificate verifies the
symbolic polynomial coefficients in characteristic two; it does not
replace the geometric proof or claim a higher-power exclusion.
"""
import json
from pathlib import Path
import sympy as S


def mod2(expression, variables):
    return S.Poly(S.expand(expression),*variables, modulus=2).as_expr()


def main():
    z,p,q,w,beta,alpha,K=S.symbols('z p q w beta alpha K')
    a=S.symbols('a0:6')
    variables=(z,p,q,w,beta,alpha,K)+a
    H=z**3+1
    F=beta*H**3+alpha*H
    A=sum(a[i]*z**i for i in range(6))
    lhs=mod2(A*A+H*A+F,variables)
    rhs=mod2(K*(z+p)**4*(z+q)**4*(z*z+w*z+w*w),variables)
    expected_left={10:a[5]**2,9:beta,8:a[4]**2+a[5],7:a[4]}
    expected_right={10:K,9:K*w,8:K*w*w,7:S.Integer(0)}
    rows=[]
    for degree in (10,9,8,7):
        left=S.Poly(lhs,z).coeff_monomial(z**degree)
        right=S.Poly(rhs,z).coeff_monomial(z**degree)
        assert mod2(left-expected_left[degree],variables)==0
        assert mod2(right-expected_right[degree],variables)==0
        rows.append({'degree':degree,'left':str(left),'right':str(right)})
    # The formerly exceptional beta=1 case: move the omitted root to1.
    # With q=zeta*p, put R=zeta^2*p^4; then p^4*q^4=R^2.
    R=S.symbols('R')
    variables_exception=(z,R,alpha)+a[:4]
    A_exception=z**5+sum(a[i]*z**i for i in range(4))
    F_exception=H**3+alpha*H
    left_exception=mod2(A_exception**2+H*A_exception+F_exception,variables_exception)
    right_exception=mod2((z**8+R*z**4+R**2)*(z**2+z+1),variables_exception)
    exception_rows=[]
    for degree,left_expected,right_expected in ((1,a[1],R**2),(5,a[2]+1,R),(4,a[2]**2+a[1],R)):
        left=S.Poly(left_exception,z).coeff_monomial(z**degree)
        right=S.Poly(right_exception,z).coeff_monomial(z**degree)
        assert mod2(left-left_expected,variables_exception)==0
        assert mod2(right-right_expected,variables_exception)==0
        exception_rows.append({'degree':degree,'left':str(left),'right':str(right)})
    assert mod2(((R+1)**2+R**2)-R,(R,))==R+1
    # At the next power B need not be constant.  Check the term that
    # invalidates simply repeating the order-eight contradiction.
    aa=S.symbols('u0:10')
    bb=S.symbols('v0:5')
    variables2=(z,beta,alpha)+aa+bb
    A2=sum(aa[i]*z**i for i in range(10))
    B2=sum(bb[i]*z**i for i in range(5))
    norm=mod2(A2*A2+H*A2*B2+F*B2*B2,variables2)
    coefficient=S.Poly(norm,z).coeff_monomial(z**15)
    assert mod2(coefficient-(beta*bb[3]**2+aa[8]*bb[4]+aa[9]*bb[3]),variables2)==0
    result={'claim':'A.29e','all_passed':True,'order_eight_top_coefficients':rows,
            'contradiction':'a4=0, a5=beta*w, a5^2=beta/w and w^3=1 give beta^2=beta; beta is neither0 nor1',
            'order_sixteen_z15_coefficient':str(coefficient),
            'higher_power_exclusion_claimed':False}
    result['beta_one_additional_coefficients']=exception_rows
    result['beta_one_conclusion']='R=1, hence p^4=zeta and p=zeta, which is a Weierstrass coordinate; no non-Weierstrass point survives'
    out=json.dumps(result,indent=2,sort_keys=True)+'\n'
    Path(__file__).with_suffix('.json').write_text(out)
    print(out,end='')


if __name__=='__main__':main()
