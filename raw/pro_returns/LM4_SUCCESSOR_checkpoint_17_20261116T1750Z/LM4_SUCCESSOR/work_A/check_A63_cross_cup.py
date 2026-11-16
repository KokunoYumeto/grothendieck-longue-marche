"""Exact finite-head model for the actual six cross-cup extension.

The quotient is pulled back over the profinite C. This program computes
the fixed-A56-affine-datum square; it does not exhaust other affine data.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json,sys
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):O=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
wpath=Path(sys.argv[1])if len(sys.argv)>1 else HERE/'Q6_actual_central_solution.json'
outname=sys.argv[2]if len(sys.argv)>2 else 'A63_cross_cup_square.json'
w=json.loads(wpath.read_text())
def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
O['phi0'].__globals__['WE']=tup(w['WE'])
O['ph'].__globals__['PSHIFT']=tup(w['PSHIFT'])
op,oc=O['ph'],O['ca'];oe,oi=O['em'],O['ei']
fm,fp,flin,fva,fsm=O['fm'],O['fp'],O['flin'],O['fva'],O['fsm']
zero=(0,)*36;TZ=(zero,)*6;AZ=(zero,)*4
M=json.loads((HERE.parent/'work_CE/next_cup_cocycle_matrices.json').read_text())
ad=json.loads((HERE.parent/'work_CE/Q6_integral_affine_data.json').read_text())
E=tup(ad['new_basis_columns_in_old_EB']);ag=tup(ad['cochain_coboundary_in_V8'])
def sqv(v):return tuple(fm(x,x)for x in v)
def fourth(v):return sqv(sqv(v))
def tv(a,b):return tuple(fva(v,w)for v,w in zip(a,b))
def av(a,b):return tuple(fva(v,w)for v,w in zip(a,b))
def hv(h,v):return flin(O['hcols'](h),v)
def h2v(h,v):return flin([sqv(c)for c in O['hcols'](h)],v)
def hat(h,a):return tuple(hv(h,v)for v in a)
def h2t(h,t):return tuple(h2v(h,v)for v in t)
def newa(g):
 h=g[2]
 return av(av(O['mix'](E,g[0]),ag),tuple(hv(h,v)for v in ag))
def ac(g):return newa(g)[:4]
pairs=[(i,j)for i in range(4)for j in range(i+1,4)]
def cup(a,b):return tuple(tuple(fm(x,y)for x,y in zip(a[i],b[j]))for i,j in pairs)
N1=(AZ,TZ,O['HN0'])
def nm(g,h):
 a,z,q=g;b,t,r=h;rb=hat(q,b)
 return(av(a,rb),tv(tv(z,h2t(q,t)),cup(a,rb)),O['hmul'](q,r))
def ni(g):
 a,z,h=g;hh=O['hinv'](h)
 out=(hat(hh,a),h2t(hh,tv(z,cup(a,a))),hh)
 assert nm(g,out)==nm(out,g)==N1
 return out
def nin(g,h):return nm(nm(g,h),ni(g))
ONE=(O['ONE'],TZ)
def em(g,h):
 og,z=g;oh,t=h
 return(oe(og,oh),tv(tv(z,h2t(og[2],t)),cup(ac(og),hat(og[2],ac(oh)))))
def ei(g):
 og,z=g;oo=oi(og)
 out=(oo,h2t(oo[2],tv(z,cup(ac(og),ac(og)))))
 assert em(g,out)==em(out,g)==ONE
 return out
def ein(g,h):return em(em(g,h),ei(g))
def ep(g,n):
 out=ONE
 while n:
  if n&1:out=em(out,g)
  g=em(g,g);n>>=1
 return out
SS=(O['SS'],TZ)
dr=ac(O['RR']);ra=hat(O['HR'],dr)
nr=nin((ra,TZ,O['HN0']),(AZ,TZ,O['HR']))
assert nr[0]==dr and nr[2]==O['HR']
RR=(O['RR'],nr[1]);TT=em(SS,RR)
assert ep(SS,2)==ep(RR,3)==ONE
print('Actual cross-cup source S²=R³=1; source cocycle and strict squared-scalar action: PASS')

def eta(g,co):
 out=zero
 for a,v in zip(co[:8],newa(g)):out=fva(out,fsm(a,sqv(v)))
 return fva(out,fva(co[8:],h2v(g[2],co[8:])))
def eta6(g,cos):return tuple(eta(g,co)for co in cos)
def basis(i,n):return tuple(int(j==i)for j in range(n))
CB=[basis(i,44)for i in range(44)]
def sr(v):return sqv(O['sres'](fourth(v)))
def cv(v):return flin(O['CV'],v)
def cv2(v):return flin(tup(M['C2']),v)
wc=tuple(tuple(x&1 | ((x>>2)&1)<<1 | ((x>>4)&1)<<2 for x in row)for row in ad['new_c_inner_free_O'])
ww=O['mix'](E,tup(w['WE'])[0])[:4]
WC=(wc,TZ,O['HN0']);WW=(ww,TZ,O['HN0'])
def c0(g):
 og,z=g;n=(tuple(cv(v)for v in ac(og)),tuple(cv2(v)for v in z),O['hc'](og[2]))
 n=nin(WC,n);old=oc(og)
 assert n[0]==ac(old) and n[2]==old[2]
 return(old,n[1])
ctarget=em(em(SS,ei(RR)),SS)
cs=c0(SS);cr=c0(RR)
ccols=[eta(oc(O['SS']),co)+eta(oc(O['RR']),co)for co in CB]
assert O['frank'](ccols)==44
CCOR=[]
for j in range(6):
 target=fva(cs[1][j],SS[1][j])+fva(cr[1][j],ctarget[1][j])
 sol=O['fsolve'](ccols,target);assert sol is not None;CCOR.append(sol)
def ca(g):
 old,z=c0(g);return(old,tv(z,eta6(old,CCOR)))
assert ca(SS)==SS and ca(RR)==ctarget and ca(TT)==ei(TT)
assert ca(ca(SS))==SS and ca(ca(RR))==RR
print('Canonical c reconstructed by exact44-variable source equations: PASS')

def p0(g):
 og,z=g;n=nin(WW,(ac(og),z,og[2]));old=op(og)
 assert n[0]==ac(old) and n[2]==old[2]
 return(old,n[1])
B0=(tup(w['BFRAME']),TZ)
baseS=ein(B0,SS);pS=p0(SS);pT=p0(TT)
pscols=[]
for co in CB:
 pscols.append(eta(O['TT'],co)+sr(h2v(O['HB'],eta(O['SS'],co))))
assert O['frank'](pscols)==40
PCOR=[]
for j in range(6):
 target=fva(pT[1][j],TT[1][j])+sr(h2v(O['HB'],fva(pS[1][j],baseS[1][j])))
 sol=O['fsolve'](pscols,target);assert sol is not None;PCOR.append(sol)
def ph(g):
 old,z=p0(g);return(old,tv(z,eta6(g[0],PCOR)))
def na(g):return ph(ca(g))
assert ph(TT)==TT
NS=tup(M['square_coboundary_columns'])
SD=na(na(SS));RD=na(na(RR))
assert SD[0]==SS[0] and RD[0]==RR[0]
INNER=[]
for j in range(6):
 target=fva(SD[1][j],SS[1][j])+fva(RD[1][j],RR[1][j])
 sol=O['fsolve'](NS,target);assert sol is not None;INNER.append(sol)
INNER=tuple(INNER)
assert h2t(O['HT'],INNER)==INNER
assert tuple(cv2(v)for v in INNER)==INNER
ig=(O['ONE'],INNER)
assert ein(ig,SS)==SD and ein(ig,RR)==RD
print('Positive literal cusp plus fixed-affine s-class equations: rank40 PASS')
print('Unique inner negative-square vector nonzero:',any(any(v)for v in INNER))
print('Inner vector rows:',INNER)
out=dict(scope='Specified A56 affine action/frame; no other affine choices exhausted',source_witness=str(wpath),
 coefficient='(V^(2))^6',canonical_c_corrections=CCOR,positive_corrections=PCOR,
 inner_square=INNER,inner_nonzero=any(any(v)for v in INNER),
 source_R_central=RR[1],all_source_and_square_checks='PASS')
(HERE/outname).write_text(json.dumps(out,indent=2)+'\n')

assert not out['inner_nonzero']
VB=O['VB'];S2=tup(M['S2']);R2=tup(M['R2']);C2=tup(M['C2']);B2=tup(M['BETA2'])
NS2=[fva(v,flin(S2,v))for v in VB]
bc=[]
ps=ph(SS);bs=ein(B0,SS)
for j in range(6):
 sol=O['fsolve'](NS2,fva(ps[1][j],bs[1][j]));assert sol is not None;bc.append(sol)
BFRAME=(B0[0],tuple(bc));assert ph(SS)==ein(BFRAME,SS)
bsq=em(ei(BFRAME),na(ei(BFRAME)));assert bsq[0]==O['ONE']
SF2=[sqv(v)for v in O['SF']]
def ds(v):return flin(B2,flin(C2,v))
SN=[fva(v,ds(v))for v in SF2]
bfix=[];bpossible=True
for j in range(6):
 sol=O['fsolve'](SN,bsq[1][j])
 if sol is None:bpossible=False;break
 bfix.append(flin(SF2,sol))
print('s-frame centralizer/norm dimensions:',len(SF2),O['frank'](SN),'; solvable:',bpossible)
jointcols=[fva(v,flin(S2,v))+fva(v,ds(v))for v in VB]
joint=O['fkernel'](jointcols);nb=O['independent'](SN)
jb=O['independent'](nb+joint)
assert len(nb)==8 and len(joint)==len(jb)==12
sclasses=[O['coordinates'](jb,v)[8:]for v in bsq[1]]
print('s-normalizer obstruction classes in a four-dimensional quotient:',sclasses)
ann=None;annvalue=0;annrow=None
for jj,row in enumerate(sclasses):
 if any(row):
  kk=next(i for i,x in enumerate(row)if x)
  dualcols=[tuple(col[i]for col in jb)for i in range(36)]
  ann=O['fsolve'](dualcols,basis(8+kk,12));assert ann is not None
  def dot(a,b):
   out=0
   for x,y in zip(a,b):out^=fm(x,y)
   return out
  assert all(dot(ann,v)==0 for v in SN)
  annvalue=dot(ann,bsq[1][jj]);assert annvalue==row[kk] and annvalue
  annrow=jj;break
if ann is not None:print('Explicit annihilator row',annrow,'value',annvalue,':',ann)
if bpossible:
 BFRAME=em(BFRAME,(O['ONE'],tuple(bfix)))
 assert ph(SS)==ein(BFRAME,SS)
 assert em(ei(BFRAME),na(ei(BFRAME)))==ONE

if not w.get('r_frame_norm_solved',True):
 out.update(s_frame_solvable=bpossible,r_frame_solvable=None,
            s_initial_square=bsq[1],s_obstruction_classes=sclasses,
            BFRAME=BFRAME if bpossible else None,
            r_scope='Old displayed r-frame norm unresolved; new r calculation skipped.')
 (HERE/outname).write_text(json.dumps(out,indent=2)+'\n')
 print('Actual cross-cup action and s-frame checked; broader r-frame existence is a separate argument.')
 raise SystemExit(0)
J0=(tup(w['JFRAME']),TZ)
rrb=na(RR);jr=ein(J0,ei(RR))
RB2=[h2v(rrb[0][2],v)for v in VB]
NBR=[fva(v,w)for v,w in zip(VB,RB2)]
jc=[]
for j in range(6):
 sol=O['fsolve'](NBR,fva(rrb[1][j],jr[1][j]));assert sol is not None;jc.append(sol)
JFRAME=(J0[0],tuple(jc));assert na(RR)==ein(JFRAME,ei(RR))
jsq=em(ei(JFRAME),na(ei(JFRAME)));assert jsq[0]==O['ONE']
RF2=[sqv(v)for v in O['RF']]
def dract(v):return flin(S2,flin(C2,v))
JN=[fva(v,dract(v))for v in RF2]
jfix=[];jpossible=True
for j in range(6):
 sol=O['fsolve'](JN,jsq[1][j])
 if sol is None:jpossible=False;break
 jfix.append(flin(RF2,sol))
print('r-frame centralizer/norm dimensions:',len(RF2),O['frank'](JN),'; solvable:',jpossible)
if jpossible:
 JFRAME=em(JFRAME,(O['ONE'],tuple(jfix)))
 assert na(RR)==ein(JFRAME,ei(RR))
 assert em(ei(JFRAME),na(ei(JFRAME)))==ONE
out.update(s_frame_solvable=bpossible,r_frame_solvable=jpossible,
           s_initial_square=bsq[1],r_initial_square=jsq[1],
           s_obstruction_classes=sclasses,s_norm_annihilator=ann,
           s_norm_annihilator_value=annvalue,s_norm_annihilator_coordinate=annrow,
           BFRAME=BFRAME if bpossible else None,JFRAME=JFRAME if jpossible else None)
(HERE/outname).write_text(json.dumps(out,indent=2)+'\n')
if bpossible and jpossible:
 assert ph(TT)==TT and na(na(SS))==SS and na(na(RR))==RR
 print('Actual cross-cup quotient: action square and BOTH literal old-frame normalizers PASS.')
print('No scalar-refinement or full R2 realization is inferred by this finite computation alone.')
