#!/usr/bin/env python3
"""Exact nonmetabelian coordinates and a finite class-nine group certificate.

No Galois value of the second coordinate is computed or claimed.  The
finite automorphisms constructed here witness that this coordinate is
visible on a characteristic finite Magnus quotient, and are labelled
as ambient automorphisms only.
"""
from g_degree8 import *


def word(s):
    return tuple('xy'.index(z) for z in s)


def numerator_mod(a, modulus):
    a=sp.Rational(a)
    return int(a.p)*pow(int(a.q),-1,modulus)%modulus


def main():
    A=scale(lower(epsilon(8),3),sp.Rational(1,120))
    B=scale(dbracket(epsilon(4),lower(epsilon(4),2)),sp.Rational(1,2))
    C=tuple(add(p,q,sp.Rational(31,20)) for p,q in zip(A,B))
    w0,w1=map(word,['xxxxxyyyy','xxxxyxyyy'])
    alpha=lambda D:-D[0].get(w0,0)
    nu=lambda D:D[0].get(w1,0)+4*D[0].get(w0,0)
    assert [(alpha(D),nu(D)) for D in [A,B,C]]==[
        (1,sp.Rational(-31,20)),(0,1),(1,0)]
    assert metah(C)=={'3,3':'1'} and metah(B)=={}
    assert not derivative(C,c) and not derivative(B,c)
    assert weight(C)==weight(B)==(4,4)
    assert linear_transport(C,(y,x))==scale(C,-1)
    assert linear_transport(B,(y,x))==scale(B,-1)
    Ccoords=describe(C)
    denominators=sorted({int(sp.denom(a)) for D in [C,B] for p in D for a in p.values()})
    assert denominators==[1,2,4]
    # Both are integral Lie vectors at5, not only integral associative vectors.
    assert all(int(sp.denom(sp.Rational(a))) in [1,2,4]
               for table in Ccoords.values() for a in table.values())
    # These integral dual coordinates prove saturation without a numerical rank.
    assert sp.Matrix([[alpha(C),alpha(B)],[nu(C),nu(B)]]).det()==1

    modulus,maxlen=125,9
    one={():1}

    def plus(P,Q,k=1):
        out=dict(P)
        for w,a in Q.items():
            out[w]=(out.get(w,0)+k*a)%modulus
            if not out[w]:out.pop(w)
        return out

    def product(P,Q):
        out={}
        for u,a in P.items():
            for v,b in Q.items():
                if len(u)+len(v)<=maxlen:
                    w=u+v;out[w]=(out.get(w,0)+a*b)%modulus
        return {w:a for w,a in out.items() if a}

    def inverse(P):
        z=plus(P,one,-1)
        total,term=dict(one),dict(one)
        for _ in range(maxlen):
            term=product(term,z)
            if not term:break
            total=plus(total,term,-1 if _%2==0 else 1)
        assert product(P,total)==one and product(total,P)==one
        return total

    @lru_cache(None)
    def hall_group(w):
        if len(w)==1:return {():1,w:1}
        j=next(j for j in range(1,len(w)) if is_lyndon(w[j:]))
        U,V=hall_group(w[:j]),hall_group(w[j:])
        out=product(product(U,V),product(inverse(U),inverse(V)))
        assert all(len(t)>=len(w) for t in out if t)
        assert {t:a for t,a in out.items() if len(t)==len(w)}=={
            t:int(a)%modulus for t,a in expand(w).items() if int(a)%modulus}
        return out

    def hall_product(D):
        ans=[];records={}
        for name,P in zip('xy',D):
            value=dict(one);exponents={}
            for j,a in coords(P,2,9).items():
                w=lyndon(2,9)[j]
                h=hall_group(w)
                exponent=numerator_mod(a,modulus)
                # These actual commutators are central and their square error
                # has degree18, so this is their exact power in the quotient.
                power=plus(one,plus(h,one,-1),exponent)
                value=product(value,power)
                exponents[''.join('xy'[i] for i in w)]=exponent
            expected=plus(one,{w:numerator_mod(a,modulus) for w,a in P.items()})
            assert value==expected
            ans.append(value);records[name]=exponents
        return tuple(ans),records

    certificates=[]
    for z in [0,1]:
        D=tuple(add(p,q,z) for p,q in zip(C,B))
        central,exponents=hall_product(D)
        errors=tuple(plus(h,one,-1) for h in central)
        images=tuple(product(h,{():1,(i,):1}) for i,h in enumerate(central))

        def apply(P,sign=1):
            out=dict(P)
            for i in range(2):out=plus(out,errors[i],sign*P.get((i,),0))
            return out

        for i,img in enumerate(images):
            assert apply(img,-1)=={():1,(i,):1}
        basecomm=product(product({():1,(0,):1},{():1,(1,):1}),
                         product(inverse({():1,(0,):1}),inverse({():1,(1,):1})))
        assert apply(basecomm)==basecomm
        first=errors[0]
        actual_alpha=(-first.get(w0,0))%modulus
        actual_nu=(first.get(w1,0)+4*first.get(w0,0))%modulus
        assert (actual_alpha,actual_nu)==(1,z)
        certificates.append({'z':z,'alpha_mod125':actual_alpha,'nu_mod125':actual_nu,
           'central_Hall_exponents_mod125':exponents,
           'inverse_verified':True,'boundary_verified':True})

    out={
      'status':'Proved',
      'arithmetic_lambda_status':'Open; no arithmetic value of nu was computed',
      'words':{'w0':'xxxxxyyyy','w1':'xxxxyxyyy'},
      'associative_coefficients':{
        name:{'w0':str(D[0].get(w0,0)),'w1':str(D[0].get(w1,0)),
              'alpha':str(alpha(D)),'nu':str(nu(D))}
        for name,D in [('A8',A),('B8',B),('C8',C)]},
      'C8':'A8 + (31/20) B8',
      'C8_Lyndon':Ccoords,
      'integral_ambient_lattice_at5':'Z5*C8 + Z5*B8',
      'saturation_certificate':'alpha(C8)=1,nu(C8)=0,alpha(B8)=0,nu(B8)=1; both vectors integral at5',
      'coefficient_denominators':denominators,
      'arithmetic_formula':'lambda = 31/20 + nu(D8(sigma))/alpha(D8(sigma)), when alpha is nonzero',
      'known_arithmetic_alpha':'d^3 chi_4^(4)(sigma)/267840 on the eighth Johnson subgroup, with G.16 normalization',
      'finite_characteristic_quotient':'image of P5 in 1+I of (Z/5^r)[[P5]]/(I^10), Magnus generators 1+X,1+Y',
      'group_word_test_modulus':modulus,
      'group_word_test_max_length':maxlen,
      'ambient_group_word_certificates':certificates,
      'universal_constraints':{
        'CM_character':[4,4],'swap_sign':-1,
        'membership':'A8,B8 lie in Enriquez b3 contained in r_ell^gr by Proposition4.19 and SL2/bracket closure',
        'all_orders':'exp(t*(A8+lambda*B8)) lies in R_ell^gr for every lambda over Q5',
        'finite_order_transport':'H1 of a finite group in a characteristic-zero prounipotent group vanishes by successive averaging; conjugation retains the leading degree8 vector'},
      'scope':'The ambient lattice is not the actual arithmetic image lattice. The constructed finite quotient automorphisms are ambient examples, not Galois elements. A nonzero arithmetic alpha exists by G.15, but its integral image and the corresponding nu remain unevaluated.'
    }
    Path(__file__).with_name('g_degree8_nonmet.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
