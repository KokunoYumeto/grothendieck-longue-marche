"""Independent original-law audit of the fixed-affine A63 s obstruction.

All output artifacts belong to work_CE.  This does not exhaust alternative
A56 affine actions or affine s frames.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy, json

HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):
    R=runpy.run_path(str(HERE/'review_A63_cross_cup.py'))
G=R['G']; O=G['O']
fm=G['fm']; flin=G['flin']; fva=G['fva']; fsm=G['fsm']
em,ei,ein,na=G['em'],G['ei'],G['ein'],G['na']
ONE,SS,TT=G['ONE'],G['SS'],G['TT']
zero,TZ=G['zero'],G['TZ']; B=G['BFRAME']; b0=G['bsq']
SF=G['SF2']; ds=G['ds']; SN=G['SN']
assert ein(B,SS)==na(SS)
assert em(ei(B),na(ei(B)))==b0
assert all(flin(G['S2'],v)==v for v in SF)

def kernel(v,j=0):
    z=list(TZ);z[j]=v;return(O['ONE'],tuple(z))
def addrow(z,v,j):
    out=list(z);out[j]=fva(out[j],v);return tuple(out)

# The module action of beta^{-1} b is derived from the actual law.
for j in range(6):
    for v in O['VB']:
        q=kernel(v,j)
        actual=ein(ei(B),na(q))
        assert actual==kernel(ds(v),j)

# All 20 k-basis directions, all three F2-basis scalars, all six copies.
columns_checked=0
for j in range(6):
    for v in SF:
        for scalar in (1,2,4):
            u=fsm(scalar,v); q=kernel(u,j); bp=em(B,q)
            assert ein(bp,SS)==na(SS)
            actual=em(ei(bp),na(ei(bp)))
            expected=(O['ONE'],addrow(b0[1],fva(u,ds(u)),j))
            assert actual==expected
            columns_checked+=1
print('Actual-law s norm variation columns checked:',columns_checked)

# An independent one-coordinate annihilator, without reusing the solver's
# chosen quotient basis: coordinate 23 vanishes on every norm column.
idx=23
assert all(v[idx]==0 for v in SN)
values=[row[idx]for row in b0[1]]
assert values==[0,0,5,0,5,5]
print('Coordinate-23 annihilator values, pairs 01,02,03,12,13,23:',values)

# Explain the four-dimensional Tate quotient by the actual monomial orbits.
def monomial(cols):
    out=[]
    for col in cols:
        nz=[i for i,v in enumerate(col)if v]
        assert len(nz)==1
        out.append((nz[0],col[nz[0]]))
    return out
sm=monomial(G['S2'])
dm=monomial([ds(v)for v in O['VB']])
seen=set(); sorbits=[]
for i in range(36):
    if i in seen:continue
    orb=sorted({i,sm[i][0]});seen.update(orb);sorbits.append(orb)
fixed=[orb for orb in sorbits if sorted(dm[i][0]for i in orb)==orb]
assert len(sorbits)==20 and len(fixed)==4
assert G['frank'](SN)==8 if 'frank' in G else O['frank'](SN)==8
print('S orbits fixed by D_s:',fixed)

# Every zero-class, literal-cusp-preserving action correction over the fixed
# old affine action is Inner(a), a in T^tau.  Verify its norm invariance in
# the actual law on a complete F2 basis, separately in all six coordinates.
TF=[G['sqv'](v)for v in O['TF']]
assert len(TF)==4
positive_checked=0
for j in range(6):
    for v in TF:
        for scalar in (1,2,4):
            a=kernel(fsm(scalar,v),j)
            assert na(a)==a and ein(a,TT)==TT and em(a,a)==ONE
            bp=em(a,B)
            def nap(g):return ein(a,na(g))
            assert nap(TT)==ei(TT)
            assert ein(bp,SS)==nap(SS)
            assert em(ei(bp),nap(ei(bp)))==b0
            positive_checked+=1
print('Actual-law positive-inner fixed-base variations checked:',positive_checked)

out=dict(scope='Fixed A56 affine action and affine s frame; old globally central frame shifts harmless',
         module='(V^(2))^6',source_dimension=20,norm_rank=8,tate_dimension=4,
         coordinate_annihilator=idx,annihilator_values=values,
         fixed_S_orbits=fixed,norm_columns_checked=columns_checked,
         positive_inner_variations_checked=positive_checked,all_checks='PASS')
(HERE.parent/'A63_s_norm_independent_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('Independent fixed-affine s-normalizer obstruction: PASS')
