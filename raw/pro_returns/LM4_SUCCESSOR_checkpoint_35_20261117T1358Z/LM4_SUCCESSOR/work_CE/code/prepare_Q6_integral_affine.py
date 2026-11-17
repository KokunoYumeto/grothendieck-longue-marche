"""Prepare exact mixed O/k affine data over the stored A56 witness.
Free cusp rows first4; binary s-complement rows last4. All outputs are
under work_CE. The old witness is read-only. Central coordinates are left
to the separate class-two construction.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json,hashlib
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):I=runpy.run_path(str(HERE/'check_Q6_integral_cusp.py'))
G=I['G'];n=36;kzero=(0,)*36
fm,fp=G['fm'],G['fp'];fva,fsm,flin=G['fva'],G['fsm'],G['flin']
VB,EB,RES=G['VB'],G['EB'],G['RES']
S,R,CV,BETA=G['S'],G['R'],G['CV'],G['BETA']
NS,MR=G['NS'],G['MR'];BS,CS=G['BS'],G['CS']
red,TEICH=I['red'],I['TEICH'];add,neg,mult=I['add'],I['neg'],I['mult']
vadd,vsub,scale=I['vadd'],I['vsub'],I['scale'];app=I['apply']
SO,RO,CO,BO=I['S'],I['R'],I['C'],I['BETA']
def mix(cols,values):return tuple(flin(values,c)for c in cols)
def fsolve(cols,target):
 rows=[list(row)+[t]for row,t in zip(zip(*cols),target)];rows,p=G['frref'](rows)
 assert len(p)==len(cols) and len(cols)not in p
 out=tuple(rows[i][-1]for i in range(len(cols)))
 assert flin(cols,out)==target
 return out
# Integral cusp coordinates that reduce to the actual old tres basis.
oldqcols=[G['tres'](G['fbasis'](o[0]))for o in I['good']]
oldqO=[tuple(TEICH[x]for x in col)for col in oldqcols]
def oldcusp(v):
 out=(0,)*4
 for a,col in zip(I['cusp'](v),oldqO):out=vadd(out,scale(a,col))
 return out
mat=[oldcusp(app(SO,v))for v in I['EF']]
def osolve_square(cols,target):
 # Same local-ring solver, valid in dimension4 as well.
 return I['solve'](cols,target)
RF=[]
for j in range(4):
 coeff=osolve_square(mat,I['vec'](j,4));v=(0,)*36
 for a,col in zip(coeff,I['EF']):v=vadd(v,scale(a,col))
 assert oldcusp(app(SO,v))==I['vec'](j,4)
 RF.append(v)
# New cohomology basis: cusp first, then s; columns in old EB.
EC=[G['coordinates'](RES,(0,)*4+G['fbasis'](i,4))for i in range(4)]
ES=[G['coordinates'](RES,G['fbasis'](i,4)+(0,)*4)for i in range(4)]
E=EC+ES
assert G['frank'](E)==8
# Positive/negative cohomology operators from the actual boundary data.
POS=[];CE=[]
for v in RES:
 POS.append(G['coordinates'](RES,flin(BS,v[:4])+v[4:]))
 CE.append(G['coordinates'](RES,flin(CS,v[:4])+v[4:]))
newPOS=[G['coordinates'](E,flin(POS,col))for col in E]
newCE=[G['coordinates'](E,flin(CE,col))for col in E]
for i in range(4):
 assert newPOS[i]==G['fbasis'](i,8) and newCE[i]==G['fbasis'](i,8)
 assert newPOS[4+i]==(0,)*4+BS[i] and newCE[4+i]==(0,)*4+CS[i]
# Literal new cocycles differ from the linear old basis by a coboundary.
a=[]
for i in range(4):
 oldS=flin(EB,EC[i]);vr=tuple(red(x)for x in RF[i])
 av=fsolve([NS[j]+MR[j]for j in range(36)],oldS+vr)
 assert fva(oldS,flin(NS,av))==kzero and flin(MR,av)==vr
 a.append(av)
a.extend([kzero]*4)
BSVAL=mix(ES,EB)
assert all(G['sres'](v)==G['fbasis'](i,4) and G['tres'](v)==(0,)*4 for i,v in enumerate(BSVAL))
# Original actual c-inner term, recomputed from source s,r identities.
GammaD=tuple(flin(CV,v)for v in mix(CE,EB))
RC=[flin(CV,flin(R,flin(CV,v)))for v in VB]
SYS=[NS[j]+fva(VB[j],RC[j])for j in range(36)]
WC=[]
for j in range(8):
 target=fva(EB[j],GammaD[j])+fva(EB[j],flin(S,flin(R,flin(R,EB[j]))))
 WC.append(fsolve(SYS,target))
# Read the restored exact witness, preserving its literal affine frame.
wpath=HERE.parents[1]/'work_A/Q6_actual_central_solution.json'
wraw=wpath.read_bytes();witness=json.loads(wraw)
Wold=tuple(map(tuple,witness['WE'][0]));Pold=tuple(map(tuple,witness['BFRAME'][0]))
assert tuple(witness['BFRAME'][2][0])==G['zero'] and witness['BFRAME'][2][1]==G['beta']
EW=mix(E,Wold);EWC=mix(E,WC);EP=mix(E,Pold)
# The cochain change is Inn(a) after linear basis change.
Wnew=EW # L_new fixes a (only the free cusp block is nonzero).
WCnew=tuple(fva(fva(a[i],EWC[i]),flin(CV,a[i]))for i in range(8))
Pnew=tuple(fva(fva(EP[i],a[i]),flin(BETA,a[i]))for i in range(8))
# Integral c-inner terms in the normalized source cocycles.
RCO=I['compose'](CO,I['compose'](RO,CO));R2O=I['mpow'](RO,2)
CSYS=[vsub(I['VB'][j],app(SO,I['VB'][j]))+vsub(I['VB'][j],app(RCO,I['VB'][j]))for j in range(36)]
VC=[]
for i,vr in enumerate(RF):
 target=(0,)*36+vsub(app(CO,vr),app(SO,app(R2O,vr)))
 vv=I['solve'](CSYS,target)
 assert app(CO,vv)==vv and tuple(red(x)for x in vv)==WCnew[i]
 VC.append(vv)
# Positive inner terms lift the actual old witness inside the literal
# tau-invariant free O-lattice.
TFk=[tuple(red(x)for x in v)for v in I['TF']]
WO=[]
for i in range(4):
 cc=G['coordinates'](TFk,Wnew[i]);v=(0,)*36
 for aa,col in zip(cc,I['TF']):v=vadd(v,scale(TEICH[aa],col))
 assert tuple(red(x)for x in v)==Wnew[i] and app(I['T'],v)==v and app(CO,v)==v
 WO.append(v)
QO=[vadd(v,w)for v,w in zip(VC,WO)]
assert all(app(CO,v)==v for v in QO)
# Lift the literal mod2 beta frame by joint invariants of S and beta*C.
DO=I['compose'](BO,CO);grp=[I['ID'],SO,DO,I['compose'](SO,DO)]
seen=set();JF=[];rep=[]
for j in range(36):
 if j in seen:continue
 o={A[0][j]for A in grp};seen|=o;v=[0]*36
 for A in grp:
  k=A[0][j];ww=A[1][j]
  assert v[k] in (0,ww);v[k]=ww
 vv=tuple(v);assert app(SO,vv)==vv and app(DO,vv)==vv
 JF.append(vv);rep.append(j)
assert len(JF)==12
PO=[];TCOR=[]
for i in range(4):
 t0=fva(Pnew[i],tuple(red(x)for x in QO[i]));tt=(0,)*36
 for j,col in zip(rep,JF):tt=vadd(tt,scale(TEICH[t0[j]],col))
 assert tuple(red(x)for x in tt)==t0 and app(SO,tt)==tt and app(DO,tt)==tt
 pp=vadd(QO[i],tt)
 assert tuple(red(x)for x in pp)==Pnew[i]
 assert vsub(pp,app(SO,pp))==vsub(QO[i],app(SO,QO[i]))
 norm=vadd(vsub(pp,app(DO,pp)),vsub(app(BO,QO[i]),QO[i]))
 assert norm==(0,)*36
 PO.append(pp);TCOR.append(tt)
# Explicit cochain-coordinate checks at the literal generators.
newS=(tuple((0,)*36 for _ in range(4))+BSVAL)
newR=tuple(tuple(red(x)for x in v)for v in RF)+(kzero,)*4
oldD_s=EB;oldD_r=(kzero,)*8
assert tuple(fva(v,flin(NS,aa))for v,aa in zip(mix(E,oldD_s),a))==newS
assert tuple(fva(v,flin(MR,aa))for v,aa in zip(mix(E,oldD_r),a))==newR
out={
 'status':'Exact executed affine preparation; no central18 norm asserted',
 'ring':{'polynomial':'X^3+X+1 over Z/4','encoding':'base4 coefficients a0+4a1+16a2','teich_generator':I['zeta']},
 'source_witness_sha256':hashlib.sha256(wraw).hexdigest(),
 'source_witness':str(wpath),
 'basis_order':'four free cusp O rows, then four binary s rows',
 'new_basis_columns_in_old_EB':E,'cochain_coboundary_in_V8':a,
 'free_s_values':[(0,)*36]*4,'free_r_values':RF,
 'binary_s_values':BSVAL,'binary_r_values':[kzero]*4,
 'old_c_inner':WC,'new_c_inner_free_O':VC,'new_c_inner_binary_k':WCnew[4:],
 'positive_inner_free_O':WO,'positive_inner_binary_k':Wnew[4:],
 'negative_inner_free_O':QO,
 's_frame_free_O':PO,'s_frame_binary_k':Pnew[4:],
 's_frame_joint_fixed_corrections_O':TCOR,
 'literal_old_s_frame_after_change_mod2':Pnew,
 'positive_binary_cohomology_columns':BS,'c_binary_cohomology_columns':CS,
 's_frame_head':witness['BFRAME'][2],
 'free_cusp_coordinate_convention':'old tres basis, lifted through the four integral orbit functionals',
 'checks':'source identities, literal reduction, integral c norm, positive cusp, integral s conjugacy and s-normalizer norm all passed'
}
op=HERE.parent/'Q6_integral_affine_data.json';op.write_text(json.dumps(out,indent=2))
print('Old EB -> free cusp4 / binary s4 basis and literal cochain correction: PASS')
print('Free source cocycles d(s)=0, d(r)=RF; binary cusp restrictions0: PASS')
print('Actual integral c-inner terms reduce to the transformed old terms and are C-fixed: PASS')
print('Positive inner terms retain the stored WE reduction and are literally tau/C-fixed: PASS')
print('s-frame retains literal stored BFRAME reduction after the cochain correction: PASS')
print('Integral s-conjugacy and involutory s-normalizer equations: PASS')
print('Saved',op)
print('Old witness SHA256',out['source_witness_sha256'])
