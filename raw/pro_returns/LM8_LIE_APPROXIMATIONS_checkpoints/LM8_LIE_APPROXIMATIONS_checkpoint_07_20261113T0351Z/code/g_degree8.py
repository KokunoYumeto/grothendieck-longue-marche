#!/usr/bin/env python3
"""Exact remaining degree-eight parameter, without an arithmetic value claim.

The actual CM arithmetic line has the form A8 + lambda B8 in the
universal geometric subspace.  This script proves that boundary, CM
symmetry, metabelian coefficients, and all known dimension tests through
fourteen cannot determine lambda.  It deliberately does not label any
chosen lambda as arithmetic.
"""
from g_embedding import *

def lower(D,k):
    for _ in range(k):
        D=dbracket((y,{}),D)
    return D

def linear_transport(D,images):
    """Conjugation by an involution specified by its images of x,y."""
    def subst(P):
        out={}
        for w,a in P.items():
            term={():a}
            for k in w:
                term=mul(term,images[k])
            out=add(out,term)
        return out
    # Only the involution interchanging x,y is used here.
    return subst(D[1]),subst(D[0])

def main():
    first=lower(epsilon(8),3)
    raw=dbracket(epsilon(4),lower(epsilon(4),2))
    rawgcd=reduce(gcd,(int(a) for a in deriv_coords(raw,8).values()))
    assert rawgcd>0
    A=scale(first,sp.Rational(1,120))
    B=scale(raw,sp.Rational(1,rawgcd))
    assert metah(A)=={'3,3':'1'}
    assert metah(B)=={}
    assert not derivative(A,c) and not derivative(B,c)
    assert weight(A)==weight(B)==(4,4)
    assert rank_by_weight([A,B],8)=={'4,4':2}
    assert linear_transport(A,(y,x))==scale(A,-1)
    assert linear_transport(B,(y,x))==scale(B,-1)
    assert characters(8)['4,4']==3
    # Published factorization, including Nakamura's factor-twelve erratum.
    theta=-6*4*sp.bernoulli(4)/4*sp.Rational(1-5**6,1-5**3)
    assert theta==sp.Rational(126,5)
    kappa_over_d3=theta/12
    h_over_d3=-kappa_over_d3/((1-5**6)*sp.factorial(3)**2)
    assert kappa_over_d3==sp.Rational(21,10)
    assert h_over_d3==sp.Rational(1,267840)
    # Exact earlier ambient injections are independent of the parameter.
    special_data=json.loads(Path(__file__).with_name('g_special_results.json').read_text())
    rows={r['degree']:r for r in special_data['even_degrees']}
    dim={m:rows[m]['CM_invariant_dimension'] for m in rows}
    expected={10:dim[4]*dim[6],
              12:dim[4]*dim[8]+dim[6]*(dim[6]-1)//2,
              14:dim[4]*dim[10]+dim[6]*dim[8]}
    for m,n in expected.items():
        assert rows[m]['CM_lower_even_bracket_rank']==n
    arithmetic={2:0,4:1,6:3,8:3}
    arithmetic[10]=5+arithmetic[4]*arithmetic[6]
    arithmetic[12]=5+arithmetic[4]*arithmetic[8]+arithmetic[6]*(arithmetic[6]-1)//2
    arithmetic[14]=7+arithmetic[4]*arithmetic[10]+arithmetic[6]*arithmetic[8]
    out={'status':'remaining arithmetic scalar lambda is not determined',
         'A8':'F^3 epsilon8 / 120',
         'B8':f'[epsilon4,F^2 epsilon4] / {rawgcd}',
         'A8_Lyndon':describe(A),'B8_Lyndon':describe(B),
         'metabelian_h':{'A8':metah(A),'B8':metah(B)},
         'ambient_middle_dimension':3,'universal_geometric_middle_dimension':2,
         'coefficient':{'chiell44_over_chi4_conductor4':str(theta),
             'kappa33_over_d_cubed_chi4_conductor4':str(kappa_over_d3),
             'h_over_d_cubed_chi4_conductor4':str(h_over_d3),
             'actual_derivation':'d^3 chi4^(4) / 267840 * (A8 + lambda B8)'},
         'parameter_independent_tests':['special equation','CM order4 invariant',
             'complex-conjugation swap sign minus',
             'prescribed metabelian coefficient',
             'universal geometric membership','dimension and bracket tests through14'],
         'ambient_injective_bracket_dimensions':expected,
         'arithmetic_dimensions_independent_of_lambda':arithmetic,
         'scope':'This is a one-parameter reduction of an unresolved arithmetic embedding, not a realization of the candidate family as Galois images.'}
    Path(__file__).with_name('g_degree8_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
