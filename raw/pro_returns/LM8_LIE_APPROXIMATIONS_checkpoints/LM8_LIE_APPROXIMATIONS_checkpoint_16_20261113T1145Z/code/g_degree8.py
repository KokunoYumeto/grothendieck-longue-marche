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
    # The Tate recursion's commutation with N is not a CM-fibre condition:
    # N has degree-zero term -F, and no member of the candidate family
    # commutes with F.
    assert rank_by_weight([lower(A,1),lower(B,1)],8)=={'3,5':2}
    # Exact published Tate term, equations (5.46) and (7.22).
    # It has relative M-weight -6, not the -8 of the missing CM class.
    sigma8=scale(dbracket(epsilon(4),lower(epsilon(4),1)),sp.Rational(1,480))
    assert weight(sigma8)==(5,3)
    assert not derivative(sigma8,c) and metah(sigma8)=={}
    assert lower(sigma8,1)==scale(B,sp.Rational(1,240))
    source=json.loads(Path(__file__).with_name('g_embedding_results.json').read_text())
    z3=tuple(combination([(w,sp.Rational(a)) for w,a in source['z3'][z].items()]) for z in 'xy')
    sigma4=scale(lower(epsilon(4),2),sp.Rational(-1,2))
    total=tuple(add(add(a,b),cc) for a,b,cc in zip(sigma4,z3,sigma8))
    s01={w:-a for w,a in y.items()};V=y
    for n in range(1,9):
        V=bracket(x,V)
        bernoulli=sp.Rational(-1,2) if n==1 else sp.bernoulli(n)
        s01=add(s01,V,-bernoulli/sp.factorial(n))
    u={w:-a for w,a in c.items()};v={w:-a for w,a in s01.items()}
    g3=truncate(bracket(add(u,v,-1),bracket(u,v)),9)
    assert truncate(derivative(total,s01),9)==truncate(bracket(s01,g3),9)
    # Published factorization, including Nakamura's factor-twelve erratum.
    theta=-6*4*sp.bernoulli(4)/4*sp.Rational(1-5**6,1-5**3)
    assert theta==sp.Rational(126,5)
    kappa_over_d3=theta/12
    h_over_d3=-kappa_over_d3/((1-5**6)*sp.factorial(3)**2)
    assert kappa_over_d3==sp.Rational(21,10)
    assert h_over_d3==sp.Rational(1,267840)
    # Goto--Ishii, arXiv:2610.21052, Theorem 1.1, in its own basis.
    coleman44=48*(1-5**3)*(1-sp.Rational(2,1-5**3))
    assert coleman44==-6048
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
         'exact_Tate_formula_attack':{
             'source':'Dorigoni et al. (2026), equations (5.46) and (7.22); Hain-Matsumoto Proposition29.1',
             'sigma3_degree8':'[epsilon4,F epsilon4]/480',
             'Tate_character':[5,3],'ordinary_W_weight':-8,'relative_M_weight':-6,
             'metabelian_h':metah(sigma8),
             'F_sigma3_degree8':'B8/240',
             'defining_lift_verified_through_word_length':9,
             'constant_quotient_projection':'zero',
             'rank_of_F_A8_and_F_B8':2,
             'Tate_N_commutation_has_no_solution_in_CM_family':True,
             'failure':'The formula determines a geometric term of the Tate lift of the weight-three constant generator. It gives no weight-four constant generator or CM specialization of the geometric iterated-Eisenstein coefficient lambda.'},
         'scope':'This is a one-parameter reduction of an unresolved arithmetic embedding, not a realization of the candidate family as Galois images.'}
    out['local_Coleman_Ihara_attack']={
        'source':'Goto-Ishii (2026), Theorem1.1/Corollary5.5 and Remark5.6',
        'source_normalization_preserved':True,
        'p':5,'wK':4,'character':[4,4],
        'scalar_times_Lp_times_Coates_Wiles':str(coleman44),
        'B8_metabelian_image':metah(B),
        'determines_lambda':False,
        'missing_integral_data':'Coates-Wiles image lattice and comparison of local reciprocity image with the eighth Johnson subgroup'}
    Path(__file__).with_name('g_degree8_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
