#!/usr/bin/env python3
"""Exact degree-six universal arithmetic and CM comparison.

The zeta-generator formula is equation (5.47) of Dorigoni et al.,
Canonicalizing Zeta Generators: Genus Zero and Genus One,
Commun. Math. Phys. 407 (2026), article 12, DOI 10.1007/s00220-025-05489-x.
All brackets in that equation are standard Lyndon brackets.
The actual CM line is recorded separately from the algebraic checks:
its identification with arithmetic uses the realization argument of G.21.
"""
from g_special import *

def named(s):
    w=tuple('xy'.index(z) for z in s)
    assert is_lyndon(w),s
    return expand(w)

def combination(items):
    out={}
    for s,a in items:
        out=add(out,named(s),a)
    return out

def scale(D,a):
    return tuple({w:a*v for w,v in p.items()} for p in D)

def epsilon(n):
    V=[y]
    for j in range(n):V.append(bracket(x,V[-1]))
    q={}
    for j in range(n//2):q=add(q,bracket(V[j],V[n-1-j]),(-1)**j)
    return V[n],q

def polyadd(P,Q,a=1):return add(P,Q,a)

def timesvar(P,i):
    return {(a+(i==0),b+(i==1)):q for (a,b),q in P.items()}

def metabracket(u,v):
    ux,uy,P=u;vx,vy,Q=v
    R={(0,0):ux*vy-uy*vx} if ux*vy-uy*vx else {}
    R=polyadd(R,timesvar(Q,0),ux)
    R=polyadd(R,timesvar(Q,1),uy)
    R=polyadd(R,timesvar(P,0),-vx)
    R=polyadd(R,timesvar(P,1),-vy)
    return (0,0,R)

@lru_cache(None)
def metaword(w):
    if len(w)==1:return (1,0,{}) if w[0]==0 else (0,1,{})
    for i in range(1,len(w)):
        if is_lyndon(w[i:]):return metabracket(metaword(w[:i]),metaword(w[i:]))
    raise ValueError(w)

def metapoly(P):
    if not P:return {}
    n=len(next(iter(P)));R={}
    for j,a in coords(P,2,n).items():R=polyadd(R,metaword(lyndon(2,n)[j])[2],a)
    return R

def metah(D):
    P,Q=map(metapoly,D)
    assert all(a>0 for a,b in P)
    h={(a-1,b):v for (a,b),v in P.items()}
    assert timesvar(h,1)==Q,(h,Q)
    return {f'{a},{b}':str(v) for (a,b),v in h.items()}

def describe(D):
    ans={}
    for z,P in zip('xy',D):
        n=len(next(iter(P))) if P else 1
        ans[z]={''.join('xy'[k] for k in lyndon(2,n)[j]):str(v)
                for j,v in coords(P,2,n).items()}
    return ans

def truncate(P,n):return {w:a for w,a in P.items() if len(w)<=n}

def tree_action(U,V):
    """The derivation represented by U tensor V in Pollack section 3.3."""
    def act(z):
        total={}
        for w,a in U.items():
            pairing=(1 if z==0 else -1) if w[0]!=z else 0
            if not pairing:continue
            term=V
            for k in reversed(w[1:]):term=bracket(gen(k),term)
            total=add(total,term,-a*pairing)
        return total
    return act(0),act(1)

def main():
    z12=(combination([('xxxyxyy',3),('xxxyyxy',3),('xxyxyxy',1)]),
         combination([('xxyxyyy',-3),('xxyyxyy',-3),('xxyyyxy',-3),('xyxyxyy',-1)]))
    z3=scale(z12,sp.Rational(1,12))
    # Equation (5.46), not the apparent sign typo on sigma_3(b) in (5.53).
    sigma4=(combination([('xxyyy',-1),('xyxyy',1)]),
            combination([('xyyyy',1)]))
    F=(y,{});E=({},x)
    for D in (z3,sigma4):assert not derivative(D,c)
    assert not any(dbracket(F,z3)) and not any(dbracket(E,z3))
    assert metah(z3)=={}
    assert metah(sigma4)=={'0,2':'-1'}
    assert sigma4==scale(dbracket(F,dbracket(F,epsilon(4))),sp.Rational(-1,2))
    # Re-derive the sign and relative normalization from the defining
    # equation (1.20)/(5.41), using g_3(u,v)=[u-v,[u,v]].
    s01=scale((y,{}),-1)[0]
    V=y
    for n in range(1,7):
        V=bracket(x,V)
        bernoulli=sp.Rational(-1,2) if n==1 else sp.bernoulli(n)
        s01=add(s01,V,-bernoulli/sp.factorial(n))
    u={w:-a for w,a in c.items()}
    v={w:-a for w,a in s01.items()}
    g3=truncate(bracket(add(u,v,-1),bracket(u,v)),7)
    rhs=truncate(bracket(s01,g3),7)
    Dtotal=tuple(add(a,b) for a,b in zip(sigma4,z3))
    assert truncate(derivative(Dtotal,s01),7)==rhs
    middle=dbracket(F,dbracket(F,epsilon(6)))
    assert metah(middle)=={'2,2':'12'}
    M=scale(middle,sp.Rational(1,12))
    candidate=tuple(add(a,b,-192) for a,b in zip(middle,z3))
    assert metah(candidate)=={'2,2':'12'}
    assert weight(candidate)==(3,3)
    # Independently compare the explicit formula with Pollack's tree.
    W=bracket(y,bracket(c,bracket(x,c)))
    A=tree_action(c,W);B=tree_action(W,c)
    tilde=tuple(add(a,b) for a,b in zip(A,B))
    assert tilde==z12 or tilde==scale(z12,-1)
    tree_ratio=1 if tilde==z12 else -1
    B3chi=16*(sp.bernoulli(3,sp.Rational(1,4))-sp.bernoulli(3,sp.Rational(3,4)))
    assert B3chi==sp.Rational(3,2)
    theta=-3*4*B3chi/3*sp.Rational(1-5**4,1-5**2)
    assert theta==-156
    kappa=sp.Rational(-1,4)*theta/12
    assert kappa==sp.Rational(13,4)
    h_coefficient=-kappa/((1-5**4)*4)
    sigma_coefficient=sp.Rational(1,2*(1-5**2))
    assert h_coefficient==sp.Rational(1,768)
    assert sigma_coefficient==sp.Rational(-1,48)
    actual=tuple(add(a,b) for a,b in zip(scale(middle,h_coefficient/12),
                                        scale(z3,sigma_coefficient)))
    primitive=scale(candidate,sp.Rational(1,6))
    assert actual==scale(primitive,sp.Rational(1,1536))
    assert all(sp.denom(a)==1 for a in deriv_coords(primitive,6).values())
    assert reduce(gcd,(int(a) for a in deriv_coords(primitive,6).values()))==1
    out={'source':'Dorigoni et al. (2026), equations (1.20), (5.41), (5.46), (5.47)',
         'z3':describe(z3),'12_z3':describe(z12),
         'sigma3_degree4':describe(sigma4),'F2_epsilon6':describe(middle),
         'metabelian_h':{'z3':metah(z3),'sigma3_degree4':metah(sigma4),
                          'F2_epsilon6':metah(middle)},
         'Pollack_tree_divided_by_12z3':tree_ratio,
         'CM_line_F2epsilon6_minus_192z3':describe(candidate),
         'CM_line_primitive_vector':describe(primitive),
         'CM_coefficient_comparison':{'d_squared':'-1/4','B3_chi_minus4':'3/2',
             'chiell33_over_chi3':'-156','12kappa22_over_chi3':'39',
             'kappa22_over_chi3':'13/4',
             'metabelian_h_over_chi3':'X^2Y^2/768',
             'universal_sigma3_coefficient_over_chi3':'-1/48',
             'primitive_V6_coefficient_over_chi3':'1/1536'},
         'checks':['boundary killed','SL2 invariance of z3','metabelian z3 zero',
                   'Tate degree4 metabelian h=-Y^2','middle metabelian h=12X^2Y^2',
                   'Pollack tree comparison','defining Tate lift equation through length7',
                   'Bernoulli and coefficient identities','primitive integral V6'],
         'source_corrections':['The minus sign on sigma3(b) in equation (5.53) is incompatible with the boundary equation; (5.46) and the defining equation give plus [abbbb].',
             'Nakamura2013 p492 corrects 1995 equation (3.11.4): the theta-product Kummer exponent is 12 kappa_ij.']}
    Path(__file__).with_name('g_embedding_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
