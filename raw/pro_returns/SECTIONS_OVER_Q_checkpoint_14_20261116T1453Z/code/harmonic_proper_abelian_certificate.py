#!/usr/bin/env python3
"""Exact finite arithmetic and V4 morphism checks for A.163.

Stoll's finite-support proposition and the cohomological Selmer argument
are retained in the proof, not replaced by these finite checks.
"""
from pathlib import Path
from itertools import product
import json
import sympy as S

n,k=1146,573
points=[(0,0),(n,0),(2028,75348),(5202,365976)]
assert all(y*y==x*x*x-n*n*x for x,y in points)
assert 2028==3*26**2 and 5202==2*51**2
# Basis (-1,2,3,191): the actual connecting classes of these four points.
vectors=[1,14,4,2]
span={0}
for v in vectors:
    span|={a^v for a in tuple(span)}
assert len(span)==16 and span==set(range(16))

primitive3=[(u,v) for u,v in product(range(3),repeat=2) if (u,v)!=(0,0)]
assert all((u**4+191**2*v**4)%3 for u,v in primitive3)
assert all((u**4+v**4)%3 for u,v in primitive3)
assert pow(-9%191,(191-1)//2,191)==190
primitive191=0
for u,v in product(range(191),repeat=2):
    if u or v:
        assert (u**4+9*v**4)%191 != 0
        primitive191+=1

T,W,a=S.symbols('T W a',nonzero=True)
rt=S.sqrt(2)
poly=T*(T-1)*(T-S.Rational(1,2))
maps={
 '1':(T,W),
 'j0':(T,-W),
 'j+':(1/(2*T),W/(rt*T)),
 'j-':(1/(2*T),-W/(rt*T)),
}
def compose(f,g):
    return tuple(S.simplify(z.subs({T:g[0],W:g[1]},simultaneous=True)) for z in f)
for name,mp in maps.items():
    expr=S.together(a*mp[1]**4-poly.subs(T,mp[0]))
    num,den=S.fraction(expr)
    assert S.factor(num.subs(W**4,poly/a))==0,(name,expr)
    assert compose(mp,mp)==maps['1']
assert compose(maps['j+'],maps['j-'])==maps['j0']
assert compose(maps['j-'],maps['j+'])==maps['j0']
for f,g in product(maps.values(),repeat=2):
    assert compose(f,g)==compose(g,f)

I=S.eye(3)
J0=S.diag(1,-1,-1)
Jp=S.Matrix([[-1,0,0],[0,0,-1/rt],[0,-rt,0]])
Jm=J0*Jp
assert J0*J0==I and Jp*Jp==I and Jm*Jm==I
assert J0*Jp==Jp*J0 and Jp*Jm==J0
assert I+J0+Jp+Jm==S.zeros(3)
projectors=[(I+mat)/2 for mat in (J0,Jp,Jm)]
assert all(p.rank()==1 and p*p==p for p in projectors)
for j in range(3):
    for h in range(3):
        assert projectors[j]*projectors[h] == (projectors[j] if j==h else S.zeros(3))
assert sum(projectors,S.zeros(3))==I
# The displayed differential matrices are themselves direct pullbacks.
basis=[1/W**2,1/W**3,T/W**3]
for name,mat in [('j0',J0),('j+',Jp),('j-',Jm)]:
    mp=maps[name]
    derivative=S.diff(mp[0],T)
    for j,w in enumerate(basis):
        pull=S.simplify(w.subs({T:mp[0],W:mp[1]},simultaneous=True)*derivative)
        rhs=sum(mat[h,j]*basis[h] for h in range(3))
        assert S.simplify(pull-rhs)==0,(name,j)

data={
 'elliptic_points':points,
 'connecting_basis':['-1','2','3','191'],
 'point_squareclass_vectors':vectors,'span_size':len(span),
 'primitive_mod3_checks':2*len(primitive3),
 'primitive_mod191_checks':primitive191,
 'Sel_psi_size':16,'Sel_phi_size':1,'Sel2_E_size':16,
 'V4_curve_maps':{name:[str(v) for v in mp] for name,mp in maps.items()},
 'differential_matrices':{name:[[str(v) for v in row] for row in mat.tolist()]
                          for name,mat in [('j0',J0),('j+',Jp),('j-',Jm)]},
 'jacobian_map_compositions':'Psi Phi=[2]_J and Phi Psi=[2]_(E x Res_K/Q E_b)',
 'Sha2_result':'Sha(E/Q)[2^infinity]=0; 4 Sha(J/Q)[2^infinity]=0',
 'source_scope':'Stoll Proposition3.6 controls the specified finite-support inverse-Selmer class without a Sha finiteness assumption',
 'status':'all literal finite checks passed'
}
out=Path(__file__).with_name('harmonic_proper_abelian_certificate_data.json')
out.write_text(json.dumps(data,indent=2)+'\n')
print('PASS: four actual elliptic points give all16 connecting classes')
print('PASS:',len(primitive3)*2,'primitive mod3 and',primitive191,'primitive mod191 quartic exclusions')
print('PASS: all V4 curve maps, compositions, and invariance identities')
print('PASS: all9 pulled-back differential identities and three orthogonal rank-one projectors')
print('Sel_psi size16; Sel_phi size1; fullSel2(E) size16 by the exact sequence proved in A.163')
print('Jacobian pull/push compositions are[2]; the target two-primary Sha exponent is2')
print('No odd-primary Sha computation is claimed for E or J.')
print('Data:',out)
