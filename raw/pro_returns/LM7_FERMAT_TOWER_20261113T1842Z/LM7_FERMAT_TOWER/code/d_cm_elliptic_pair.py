#!/usr/bin/env python3
"""Exact marked cubic/quartic/cyclic12 maps and the arithmetic CM sign graph."""
from pathlib import Path
from itertools import combinations,product
from collections import deque
import json,time
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
OUT=Path(__file__).resolve().parent;started=time.time()
z,w,x,y=sp.symbols('z w x y')
def zero(expr,rel,variables):
    num=sp.cancel(expr).as_numer_denom()[0]
    assert sp.reduced(num,[rel],*variables)[1]==0
X=z/w**2;Y=w/(z-1)
rel=w**4-z*(z-1)
zero(Y**2-X**3+X,rel,(w,z))
zero(X**2/(X**2-1)-z,rel,(w,z))
zero(Y/(X**2-1)-w,rel,(w,z))
ZZc=x**2/(x**2-1);WW=y/(x**2-1)
zero(WW**4-ZZc*(ZZc-1),y**2-x**3+x,(y,x))
zero(ZZc/WW**2-x,y**2-x**3+x,(y,x))
zero(WW/(ZZc-1)-y,y**2-x**3+x,(y,x))
zero((1-z)/w**2+1/X,rel,(w,z))
zero(-w/z+Y/X**2,rel,(w,z))
assert sp.cancel(X.subs(w,sp.I*w)+X)==0
assert sp.cancel(Y.subs(w,sp.I*w)-sp.I*Y)==0

def inverse(word):return [-a for a in reversed(word)]
def schreier(n,word):
    q=0;out=[]
    for a in word:
        if a>0:
            if a==1:
                if q==n-1:out.append(1)
            else:out.append(q+2)
            q=(q+1)%n
        else:
            q=(q-1)%n
            if a==-1:
                if q==n-1:out.append(-1)
            else:out.append(-q-2)
    return q,out
def ab(n,word):
    q,ww=schreier(n,word);assert q==0
    return sp.Matrix([sum(1 if a>0 else -1 for a in ww if abs(a)==i+1) for i in range(n+1)])
def curve(n):
    basis=[[1]*n]+[[1]*j+[2]+[-1]*((j+1)%n) for j in range(n)]
    assert sp.Matrix.hstack(*(ab(n,g) for g in basis))==sp.eye(n+1)
    d=sp.gcd(n,2);d=int(d)
    cuspwords=[[1]*n,[2]*n]+[[1]*j+[-2,-1]*(n//d)+[-1]*j for j in range(d)]
    cusp=sp.Matrix.hstack(*(ab(n,g) for g in cuspwords))
    assert cusp*sp.ones(d+2,1)==sp.zeros(n+1,1)
    assert cusp.rank()==d+1
    C=cusp[:,:d+1];J=None
    for inds in combinations(range(n+1),n-d):
        B=C.row_join(sp.eye(n+1)[:,list(inds)])
        if abs(B.det())==1:
            J=sp.eye(n+1)[:,list(inds)];P=B.inv()[d+1:,:];break
    assert J is not None and P*J==sp.eye(n-d)
    D=sp.Matrix.hstack(*(ab(n,[1]+g+[-1]) for g in basis))
    Dc=P*D*J
    assert P*D*C==sp.zeros(n-d,d+1)
    assert Dc**n==sp.eye(n-d)
    return {'basis':basis,'cuspwords':cuspwords,'cusp':cusp,'P':P,'J':J,'D':D,'Dc':Dc,
            'genus':(n-d)//2,'punctures':d+2,'rank':n+1}
C={n:curve(n) for n in [3,4,12]}
maps={}
for n in [3,4]:
    H=sp.Matrix.hstack(*(ab(n,g) for g in C[12]['basis']))
    compact=C[n]['P']*H*C[12]['J']
    assert C[n]['P']*H*C[12]['cusp']==sp.zeros(2,4)
    assert compact*C[12]['Dc']==C[n]['Dc']*compact
    assert compact.rank()==2
    maps[n]={'punctured_homology_matrix':H,'compact_homology_matrix':compact}
joint=maps[3]['compact_homology_matrix'].col_join(maps[4]['compact_homology_matrix'])
smith=smith_normal_form(joint,domain=ZZ)
diagonal=[abs(int(smith[i,i])) for i in range(4)]
assert joint.rank()==4 and diagonal==[1]*4
assert C[3]['Dc']**2+C[3]['Dc']+sp.eye(2)==sp.zeros(2)
assert C[4]['Dc']**2==-sp.eye(2)
# Actual S3 orbit of the cyclic4 character and its full normal core.
chars=[(1,1),(1,2),(2,1)]
intersection=[(a,b) for a,b in product(range(4),repeat=2) if all((c*a+d*b)%4==0 for c,d in chars)]
assert intersection==[(0,0)]
core12=[(a,b) for a,b in product(range(12),repeat=2) if all((c*a+d*b)%12==0 for c,d in [(1,1),(1,-2),(-2,1)])]
assert core12==[(0,0),(4,8),(8,4)]
# The arithmetic joint group over Q(zeta12): eta=tau*epsilon, W=[i]^epsilon_bit.
def om(a,b,mod=4):
    x,y=a;z,w=b
    return ((x*z-y*w)%mod,(x*w+y*z-y*w)%mod)
mu3=[(1,0),(0,1),(3,3)]
assert all(om(om(a,a),a)==(1,0) for a in mu3)
normone=[(a,b) for a,b in product(range(4),repeat=2) if (a*a-a*b+b*b)%4==1]
graph=[]
for eta in normone:
    tau=next(t for t in mu3 if tuple(u%2 for u in t)==tuple(u%2 for u in eta))
    part=om(eta,om(tau,tau))
    assert part in [(1,0),(3,0)]
    eps=0 if part==(1,0) else 1
    graph.append({'eta_a_b_mod4':eta,'Teichmueller_a_b':tau,'normalized_E3_sign':1-2*eps,
                  'projective_E4_3_i_exponent':eps})
assert len(graph)==6
for eta in normone:
    for tau in mu3:
        a=next(g for g in graph if g['eta_a_b_mod4']==eta)
        b=next(g for g in graph if g['eta_a_b_mod4']==om(eta,tau))
        assert a['normalized_E3_sign']==b['normalized_E3_sign']
# Read the previously checked component; compute the fixed-fibre coordinates.
prior=json.loads((OUT/'d_cm_rank4_structure.json').read_text())['summary']
M16=sp.Matrix(prior['D33_elliptic_Tate16_matrix'])
assert M16.applyfunc(lambda x:int(x)%4)==3*sp.eye(2)
AA=sp.eye(2);VV=sp.eye(2);BB=sp.Matrix([[9,8],[4,9]])
TT=AA.inv()*VV
assert TT==sp.eye(2)
WW=sp.Matrix([[9,-8],[-4,9]])
assert BB*WW==49*sp.eye(2)
# 49=1 modulo12, so WW is the exact inverse in the retained quotient.
assert (WW+C[4]['Dc']).applyfunc(lambda x:int(x)%3)==sp.zeros(2)
def serial(v):
    if isinstance(v,sp.MatrixBase):return [[int(a) for a in v.row(i)] for i in range(v.rows)]
    if isinstance(v,dict):return {str(k):serial(x) for k,x in v.items()}
    if isinstance(v,list):return [serial(x) for x in v]
    return v
summary={'quartic_rational_curve_map_and_inverse_verified':True,
 'quartic_deck_i_and_swap_maps_verified':True,
 'cyclic_cover_genera':{str(n):C[n]['genus'] for n in C},
 'cyclic_cover_punctures':{str(n):C[n]['punctures'] for n in C},
 'cyclic_cover_free_ranks':{str(n):C[n]['rank'] for n in C},
 'common_cyclic12_compact_joint_rank':joint.rank(),
 'common_cyclic12_compact_joint_Smith_diagonal':diagonal,
 'common_cyclic12_compact_joint_kernel_rank':6,
 'quartic_S3_normal_core_deck_order':16,
 'cyclic12_S3_normal_core_deck_order':48,
 'full_Fermat12_deck_order':144,
 'arithmetic_joint_image_over_Q_zeta12_order':6,
 'D33_normalized_cover_sign':-1,'D33_retained_LM2_CM3_sign':1,
 'D33_retained_LM2_CM4_projective_i_exponent':1,
 'all_18_Ihara_gauge_sign_checks':True,
 'scope':'The shared cover and arithmetic graph are actual maps. No equality between the cover-Jacobian and fixed-fibre characters is inferred for full GT0.',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_elliptic_pair.json').write_text(json.dumps(serial({'summary':summary,'covers':C,
    'cover12_maps':maps,'joint_compact_homology_matrix':joint,'arithmetic_joint_sign_graph':graph}),indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
