"""Exact coefficient algebra for the next noncentral six-cup layer.
No square or frame solution is inferred; constants belong to the actual
class-two calculation. Writes only work_CE.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json,runpy
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):P=runpy.run_path(str(HERE/'prepare_Q6_integral_affine.py'))
G=P['G'];fm=G['fm'];flin=G['flin'];fva=G['fva'];frank=G['frank'];VB=G['VB'];z=(0,)*36
sq=lambda x:fm(x,x)
four=lambda x:sq(sq(x))
def sqv(v):return tuple(sq(x)for x in v)
def fourth(v):return tuple(four(x)for x in v)
S2=[sqv(c)for c in G['S']];R2=[sqv(c)for c in G['R']]
T2=[sqv(c)for c in G['T']];C2=[sqv(c)for c in G['CV']];B2=[sqv(c)for c in G['BETA']]
R22=[flin(R2,c)for c in R2]
def sr(v):return sqv(G['sres'](fourth(v)))
def tr(v):return sqv(G['tres'](fourth(v)))
NS=[fva(e,flin(S2,e))for e in VB];NR=[fva(e,flin(R2,e))for e in VB]
ES=[sqv(v)for v in P['newS']]+NS
ER=[sqv(v)for v in P['newR']]+NR
assert len(ES)==len(ER)==44
assert all(fva(v,flin(S2,v))==z for v in ES)
assert all(fva(fva(v,flin(R2,v)),flin(R22,v))==z for v in ER)
pair=[a+b for a,b in zip(ES,ER)];assert frank(pair)==44
ET=[fva(a,flin(S2,b))for a,b in zip(ES,ER)]
# eta(c(r)) = (1+S R^-1)eta(s)+S R^-1 eta(r).
EC_S=ES
EC_R=[fva(a,flin(S2,flin(R22,fva(a,b))))for a,b in zip(ES,ER)]
assert frank([a+b for a,b in zip(EC_S,EC_R)])==44
POS=[t+sr(flin(B2,a))for t,a in zip(ET,ES)]
assert frank(POS)==40
PK=G['fkernel'](POS);assert len(PK)==4
assert all(not any(v[:8])for v in PK)
assert all(flin(T2,v[8:])==v[8:] and flin(C2,v[8:])==v[8:]for v in PK)
COB=[a+b for a,b in zip(NS,NR)];assert frank(COB)==36
# The abstract joint restriction is the actual transported rank-eight map.
RES=[sr(a)+tr(t)for a,t in zip(ES[:8],ET[:8])]
assert frank(RES)==8
out={'coefficient_module':'V^(2), squared monomial scalars; Frobenius explicit',
 'cocycle_basis_order':'8 squares of normalized source affine rows, then36 inner vectors',
 'source_s_columns':ES,'source_r_columns':ER,'source_tau_columns':ET,
 'canonical_c_s_columns':EC_S,'canonical_c_r_columns':EC_R,
 'positive_tau_and_sclass_columns':POS,'positive_kernel':PK,
 'square_coboundary_columns':COB,'joint_res8_columns':RES,
 'S2':S2,'R2':R2,'T2':T2,'C2':C2,'BETA2':B2,
 'ranks':{'source44':44,'canonical_c44':44,'positive40':40,'inner36':36,'joint_res8':8},
 'scope':'Coefficient correction algebra only; actual new square and frames not solved.'}
(HERE.parent/'next_cup_cocycle_matrices.json').write_text(json.dumps(out,indent=2))
print('Frobenius-twisted actual source cocycle basis:8 classes+36 inner; rank44 PASS')
print('Canonical c(s), c(r)=s r^-1 s evaluation matrix: rank44 PASS')
print('Positive tau36 + transported s-class4 constraints: rank40 PASS')
print('Its4-dimensional kernel consists exactly of inner tau-fixed/C-fixed vectors: PASS')
print('Source square-coboundary matrix rank36; joint cohomology restrictions rank8: PASS')
print('No actual new square or frame solution is claimed by this coefficient certificate.')
