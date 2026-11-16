"""Lift the actual stored A56 r-frame through the Bockstein affine layer.
All old data are read-only. This is not yet a central18 frame certificate.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):P=runpy.run_path(str(HERE/'prepare_Q6_integral_affine.py'))
I=P['I'];G=P['G'];app=P['app'];add=P['vadd'];sub=P['vsub'];scale=P['scale'];red=P['red'];TEICH=P['TEICH'];flin=P['flin'];fva=P['fva'];mix=P['mix']
SO,RO,CO=P['SO'],P['RO'],P['CO'];R2=I['mpow'](RO,2)
old=P['witness'];jh=(tuple(old['JFRAME'][2][0]),old['JFRAME'][2][1])
JC=[G['vaction'](jh[0],jh[1],v)for v in G['VB']];JO=I['mon'](JC)
JI=I['mpow'](JO,5)
# No order assumption on J is needed; invert the monomial directly.
def minv(A):
 pp,ww=A;p=[0]*36;w=[0]*36
 for j,k in enumerate(pp):p[k]=j;w[k]=I['INV'][ww[j]]
 return tuple(p),tuple(w)
JI=minv(JO)
D=I['compose'](JO,CO);RP=I['compose'](JO,I['compose'](R2,JI))
assert I['compose'](D,D)==I['ID'] and I['mpow'](RP,3)==I['ID']
assert I['compose'](D,I['compose'](RP,D))==I['mpow'](RP,2)
assert RP==P['RCO']
oldJ=tuple(map(tuple,old['JFRAME'][0]));EJ=mix(P['E'],oldJ)
Jnew=tuple(fva(fva(EJ[i],P['a'][i]),flin(JC,P['a'][i]))for i in range(8))
# d'=d-delta(a0), with (1-R)a0=d(r).
GA=[];QG=[]
for vr,q in zip(P['RF'],P['QO']):
 a0=scale(3,add(scale(2,vr),app(RO,vr)))
 assert sub(a0,app(RO,a0))==vr
 qg=sub(sub(q,a0),app(CO,a0));assert app(CO,qg)==qg
 GA.append(a0);QG.append(qg)
grp=[I['ID'],RP,I['mpow'](RP,2),D,I['compose'](RP,D),I['compose'](I['mpow'](RP,2),D)]
assert all(A[1][j]==1 for A in grp for j in range(36)if A[0][j]==j)
seen=set();JF=[];reps=[]
for j in range(36):
 if j in seen:continue
 orb={A[0][j]for A in grp};seen|=orb;v=[0]*36
 for A in grp:
  k=A[0][j];assert v[k]in(0,A[1][j]);v[k]=A[1][j]
 v=tuple(v);assert app(RP,v)==v and app(D,v)==v
 JF.append(v);reps.append(j)
PJO=[];TJO=[]
for i in range(4):
 gauge_delta=sub(GA[i],app(JO,GA[i]))
 p0g=fva(Jnew[i],tuple(red(x)for x in gauge_delta))
 t0=fva(p0g,tuple(red(x)for x in QG[i]));tt=(0,)*36
 for j,col in zip(reps,JF):tt=add(tt,scale(TEICH[t0[j]],col))
 assert tuple(red(x)for x in tt)==t0
 pg=add(QG[i],tt);p=add(pg,gauge_delta)
 assert tuple(red(x)for x in p)==Jnew[i]
 # Undoing the gauge restores exact affine conjugacy of actual r^-1.
 left=add(I['vneg'](app(CO,P['RF'][i])),sub(P['QO'][i],app(RP,P['QO'][i])))
 right=sub(sub(p,app(RP,p)),app(JO,app(R2,P['RF'][i])))
 assert left==right
 norm=add(sub(p,app(D,p)),sub(app(JO,P['QO'][i]),P['QO'][i]))
 assert norm==(0,)*36
 PJO.append(p);TJO.append(tt)
# Binary coordinates are the already retained old witness after the same
# cochain basis change; their equations are checked directly in F8.
DP=[flin(JC,flin(G['CV'],v))for v in G['VB']]
RPK=[tuple(red(x)for x in app(RP,v))for v in I['VB']]
qbin=tuple(fva(x,y)for x,y in zip(mix(P['BS'],P['WCnew'][4:]),P['Wnew'][4:]))
nbin=mix(P['BS'],mix(P['CS'],tuple(flin(G['CV'],v)for v in Jnew[4:])))
for i,p in enumerate(Jnew[4:]):
 # r-source has binary value0.
 assert fva(p,flin(RPK,p))==fva(qbin[i],flin(RPK,qbin[i]))
 assert fva(fva(p,flin(JC,nbin[i])),fva(flin(JC,qbin[i]),qbin[i]))==(0,)*36
out={'status':'Actual affine r-frame conjugacy/norm and literal old reduction checked; no central18 claim',
 'source_witness_sha256':P['out']['source_witness_sha256'],
 'r_frame_head':jh,'r_frame_free_O':PJO,'r_frame_binary_k':Jnew[4:],
 'literal_old_r_frame_after_change_mod2':Jnew,
 'r_zero_gauge_free_O':GA,'gauged_negative_inner_free_O':QG,
 'r_frame_joint_fixed_corrections_O':TJO,'joint_invariant_rank_O':len(JF),
 'r_head_monomial':JO,'joint_involution_monomial':D}
(HERE.parent/'Q6_integral_rframe_data.json').write_text(json.dumps(out,indent=2))
print('Actual J head yields monomial S3: order3 rotation, order2 reflection, inversion relation: PASS')
print('All point-stabilizer Teichmuller characters are trivial; joint invariant rank:',len(JF))
print('Integral r-zero gauge and C-fixed negative parameter: PASS')
print('Literal stored JFRAME reduction retained after cochain change and gauge undoing: PASS')
print('Actual r-inverse conjugacy and involutory r-normalizer affine equations: PASS')
print('Saved Q6_integral_rframe_data.json; central18 repair remains separate.')
