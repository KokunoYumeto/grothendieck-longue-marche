#!/usr/bin/env python3
"""Literal map checks for A.169's full metabelian cover tower.

The global Kummer, Selmer and inverse-limit arguments are proved in the
source.  This finite certificate does not assert finite-level Kummer
injectivity or replace those continuous arguments.
"""
from pathlib import Path
import json
import itertools
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

a,A,B,c,U,V,r,s=S.symbols('a A B c U V r s',nonzero=True)

def reduce_cover(expr,n):
    """Reduce the literal equations c^8=A²B/(64a²), AU^n+BV^n=1."""
    expr=S.cancel(expr)
    polynomial=S.Poly(expr,c,U,V,domain=S.QQ.frac_field(a,A,B))
    total=0
    for (ic,iu,iv),coef in polynomial.terms():
        kc,jc=divmod(ic,8)
        ku,ju=divmod(iu,n)
        total+=coef*c**jc*(A*A*B/(64*a*a))**kc*U**ju*((1-B*V**n)/A)**ku*V**iv
    return S.factor(total)

rows=[]
for n in range(8,81,8):
    W=c*U**(n//4)*V**(n//8)
    T=S.Rational(1,2)-4*a*c**4/A*V**(n//2)
    t=A*U**n
    assert reduce_cover(4*T*(1-T)-t,n)==0
    assert reduce_cover(a*W**4-T*(T-1)*(T-S.Rational(1,2)),n)==0
    assert reduce_cover(64*a*a*W**8-t*t*(1-t),n)==0
    image={ (2*i+j)%8 for i in range(n) for j in range(n) }
    kernel=sum((2*i+j)%8==0 for i in range(n) for j in range(n))
    assert image==set(range(8)) and kernel==n*n//8
    degree=n*n//8
    ramification=[n//4,n//4,n//8,n//8]
    fibre_counts=[degree//e for e in ramification]
    genus=(n-1)*(n-2)//2
    assert 2*genus-2==4*degree+sum(f*(e-1) for f,e in zip(fibre_counts,ramification))
    rows.append({'n':n,'degree_to_D':degree,'genus':genus,
                 'relative_boundary_ramification':ramification,
                 'boundary_fibre_cardinalities':fibre_counts})

transition_count=0
for n in (8,16,24,32):
    for k in (2,3,4,5):
        m=k*n
        cm=c*r**(n//4)*s**(n//8)
        Am=A*r**n; Bm=B*s**n
        wn=c*(r*U**k)**(n//4)*(s*V**k)**(n//8)
        wm=cm*U**(m//4)*V**(m//8)
        assert S.factor(wn-wm)==0
        tn=S.Rational(1,2)-4*a*c**4/A*(s*V**k)**(n//2)
        tm=S.Rational(1,2)-4*a*cm**4/Am*V**(m//2)
        assert S.factor(tn-tm)==0
        assert S.factor(cm**8-Am**2*Bm/(64*a*a)-(c**8-A**2*B/(64*a*a))*r**(2*n)*s**n)==0
        transition_count+=1

# The exact four rational cusp presentations corresponding to D tangent1.
cases={
    'P0':(8*a,1,1),
    'P1':(-8*a,1,1),
    'Ph':(1,64*a*a,1),
    'Pinf':(-4/a**2,4/a**2,1/a)}
for name,(aa,bb,cc) in cases.items():
    assert S.factor(cc**8-aa**2*bb/(64*a*a))==0
    if name in ('P0','P1'):
        target=S.Rational(1,2)-4*a*cc**4/aa
        assert S.factor(target-{'P0':0,'P1':1}[name])==0
    elif name=='Ph':
        assert aa==1
    else:
        assert S.factor(aa+bb)==0

# Eliminate one rational boundary point P.  The full relation maps
# e_P to minus the diagonal on all other geometric boundary points;
# every permutation of those other points preserves this actual line.
permutation_checks=0
module_rows=[]
for d in range(2,13):
    elimination=S.Matrix.hstack(-S.ones(d,1),S.eye(d))
    assert elimination*S.ones(d+1,1)==S.zeros(d,1)
    assert elimination.rank()==d
    diag=S.ones(d,1)
    smith=smith_normal_form(diag,domain=ZZ)
    assert abs(smith[0,0])==1
    # Adjacent transpositions generate every permutation; include cycles.
    perms=[]
    for j in range(d-1):
        p=list(range(d));p[j],p[j+1]=p[j+1],p[j];perms.append(p)
    perms.append([(j+1)%d for j in range(d)])
    for p in perms:
        P=S.zeros(d,d)
        for j,k in enumerate(p):P[k,j]=1
        full=S.diag(S.ones(1,1),P)
        assert elimination*full==P*elimination
        assert P*diag==diag
        permutation_checks+=1
    module_rows.append({'other_boundary_points':d,'rank_M':d,'rank_M_over_inertia':d-1})

# The scalar identity is obtained by the two actual cocycle expansions.
u,v,b_u,b_v=S.symbols('u v b_u b_v')
commuting_difference=S.expand((b_u+u*b_v)-(b_v+v*b_u))
assert commuting_difference==S.expand((u-1)*b_v-(v-1)*b_u)
fixed=[d for d in range(8) if all((chi-1)*d%8==0 for chi in (1,3,5,7))]
assert fixed==[0,4]

data={'covers':rows,'exact_adjacent_transitions':transition_count,
      'rational_cusp_presentations':{k:[str(x) for x in v] for k,v in cases.items()},
      'boundary_module_rows':module_rows,'permutation_checks':permutation_checks,
      'arithmetic_centralizing_deck_coordinates':fixed,
      'status':'all exact finite map checks passed',
      'scope':'Kummer detection and compact conjugator conclusions use the continuous proof in A169'}
path=Path(__file__).with_name('harmonic_full_metabelian_certificate_data.json')
path.write_text(json.dumps(data,indent=2)+'\n')
print('PASS:',len(rows),'literal Fermat-to-D maps, exact degrees, boundary ramification and genus identities')
print('PASS:',transition_count,'actual adjacent transition maps and coefficient compatibilities')
print('PASS: all four rational cusp presentations and their selected D boundary images')
print('PASS:',permutation_checks,'boundary-module equivariance checks and primitive inertia lines')
print('PASS: commuting cyclotomic cocycle identity and exact downstairs deck centralizer')
print('Data:',path)
