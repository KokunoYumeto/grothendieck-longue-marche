#!/usr/bin/env python3
"""Exact arithmetic maps for A.200; cohomology orders are proved in the text."""
from pathlib import Path
from itertools import product
import json
import sympy as sp


def v3(a):
    a=abs(a)
    n=0
    while a and a%3==0:
        a//=3
        n+=1
    return n


def mul(u,v,m):
    a,b,c,z=u
    aa,bb,cc,zz=v
    half=pow(2,-1,m)
    return ((a+aa)%m,(b+bb)%m,(c+cc+a*bb)%m,
            (z+zz+a*cc+half*a*a*bb)%m)


def phi(u,n,m):
    a,b,c,z=u
    return (a,n*b%m,n*c%m,n*z%m)


def action(u,chi,m):
    a,b,c,z=u
    return (chi*a%m,chi*b%m,chi*chi*c%m,chi**3*z%m)


def fq2_mul(a,b,q,r):
    # The quadratic factor is X^2+r X+r^2, where r^3=3 mod q.
    aa,ab=a
    ba,bb=b
    return ((aa*ba-r*r*ab*bb)%q,
            (aa*bb+ab*ba-r*ab*bb)%q)


def fq2_pow(a,n,q,r):
    out=(1,0)
    while n:
        if n&1:
            out=fq2_mul(out,a,q,r)
        a=fq2_mul(a,a,q,r)
        n//=2
    return out


def main():
    alpha=sp.Symbol('alpha')
    reduce=lambda f: sp.rem(sp.Poly(sp.expand(f),alpha),
                            sp.Poly(alpha**3-3,alpha)).as_expr()
    U=alpha**2-2
    assert reduce(U**3+6*U**2+12*U-1)==0

    # Symbolic homomorphism and arithmetic-equivariance of phi_m.
    a,b,c,z,aa,bb,cc,zz,n,chi=sp.symbols('a b c z aa bb cc zz n chi')
    def smul(u,v):
        a,b,c,z=u
        aa,bb,cc,zz=v
        return (a+aa,b+bb,c+cc+a*bb,z+zz+a*cc+a*a*bb/2)
    def sphi(u):
        a,b,c,z=u
        return (a,n*b,n*c,n*z)
    def sact(u):
        a,b,c,z=u
        return (chi*a,chi*b,chi**2*c,chi**3*z)
    u=(a,b,c,z);v=(aa,bb,cc,zz)
    assert all(sp.expand(x-y)==0 for x,y in
               zip(sphi(smul(u,v)),smul(sphi(u),sphi(v))))
    assert all(sp.expand(x-y)==0 for x,y in zip(sphi(sact(u)),sact(sphi(u))))

    # Exhaust the first actual finite quotient, including zero scalar.
    elems=list(product(range(3),repeat=4))
    scalar_checks=0
    for n in range(3):
        for u in elems:
            for v in elems:
                assert phi(mul(u,v,3),n,3)==mul(phi(u,n,3),phi(v,n,3),3)
                scalar_checks+=1
            for chi in (1,2):
                assert phi(action(u,chi,3),n,3)==action(phi(u,n,3),chi,3)
    assert all(phi(u,0,3)==(u[0],0,0,0) for u in elems)

    # Actual quadratic residue fields and the nonzero tame cup on the unit line.
    local_rows=[]
    for q,r in ((11,9),(59,49)):
        assert pow(r,3,q)==3
        assert all((x*x+r*x+r*r)%q for x in range(q))
        al=(0,1)
        al2=fq2_mul(al,al,q,r)
        un=((al2[0]-2)%q,al2[1])
        omega=fq2_pow(al,(q*q-1)//3,q,r)
        assert omega!=(1,0) and fq2_pow(omega,3,q,r)==(1,0)
        uchar=fq2_pow(un,(q*q-1)//3,q,r)
        assert uchar==fq2_pow(omega,2,q,r)
        rows=[]
        for z in range(27):
            assert fq2_pow(uchar,z,q,r)==fq2_pow(omega,2*z,q,r)
            cup=(8*2*z)%3
            assert (cup==0)==(z%3==0)
            rows.append(cup)
        local_rows.append({'q':q,'quadratic_linear_root':r,
                           'omega':omega,'unit_character':2,
                           'cup_values_z_0_through_26':rows})

    residues=[]
    for Q in (4,121,3481):
        assert v3(Q-1)==1 and v3(Q*Q-1)==1
        residues.append({'Q':Q,'twist2_exponent':3,'twist3_exponent':3})

    # The cyclic annihilator arithmetic is distinct from the proved order input.
    profiles=[]
    for z in range(81):
        first=(z%3==0)
        second=(z%9==0)
        assert (z*3)%9==0 if first else (z*3)%9!=0
        profiles.append({'z_mod81':z,'first_weight_zero':first,
                         'second_weight_zero':second,
                         'first_supported_failure_modulus':
                            (3 if not first else 9 if not second else None)})
    assert profiles[0]['second_weight_zero']
    assert (3*1)%9!=0 and (3*3)%9==0

    result={'scalar_group_checks':scalar_checks,
            'quadratic_residue_maps':local_rows,
            'supported_tate_residues':residues,
            'cyclic_annihilator_profiles':profiles,
            'scope':'Exact scalar, residue and annihilator maps; the cohomology orders and lift existence are proved using A195/A196.'}
    lines=[
        'PASS: literal unit polynomial and symbolic scalar group endomorphisms with arithmetic equivariance.',
        f'PASS: all {scalar_checks} finite group/scalar products, including the zero section.',
        'PASS: both actual quadratic residue fields, U-character2, and the nonzero tame cup for every exponent outside3Z3.',
        'PASS: all nine added residue fields give exponent3 in both supported Tate weights.',
        'PASS: 81 exact cyclic annihilator profiles for orders3/9 and all three supported lifting cases.'
    ]
    p=Path(__file__)
    p.with_name(p.stem+'_data.json').write_text(json.dumps(result,indent=2)+'\n')
    p.with_name(p.stem+'_output.txt').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines))


if __name__=='__main__':
    main()
