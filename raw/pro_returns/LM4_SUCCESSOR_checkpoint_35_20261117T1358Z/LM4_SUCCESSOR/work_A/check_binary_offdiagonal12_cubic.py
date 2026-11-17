"""Actual twelve offdiagonal binary-binary ordinary-cup quotient.
Research only: no full scalar-refinement or arbitrary-affine exhaustion claim.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json,sys
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):O=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
wpath=Path(sys.argv[1])if len(sys.argv)>1 else HERE/'A66_W0_local_compatible_partial.json'
outname=sys.argv[2]if len(sys.argv)>2 else 'binary_offdiagonal12_cubic_result.json'
w=json.loads(wpath.read_text())
def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
O['phi0'].__globals__['WE']=tup(w['WE']);O['ph'].__globals__['PSHIFT']=tup(w['PSHIFT'])
op,oc=O['ph'],O['ca'];fm,fp,flin,fva,fsm=O['fm'],O['fp'],O['flin'],O['fva'],O['fsm']
zero=(0,)*36;AZ=(zero,)*4;TZ=(zero,)*12
ad=json.loads((HERE.parent/'work_CE/Q6_integral_affine_data.json').read_text())
E=tup(ad['new_basis_columns_in_old_EB']);ag=tup(ad['cochain_coboundary_in_V8'])
def va(a,b):return tuple(fva(v,w)for v,w in zip(a,b))
def star(a,b):return tuple(fm(x,y)for x,y in zip(a,b))
def sq(v):return tuple(fm(x,x)for x in v)
def fourth(v):return sq(sq(v))
def j3(v):return tuple(fp(v[O['partner'][i]],4)for i in range(36))
def ji3(v):return tuple(fp(v[O['partner'][i]],2)for i in range(36))
def hv(h,v):return flin(O['hcols'](h),v)
HC={}
def h3(h,v):
 if h not in HC:HC[h]=[tuple(fp(x,3)for x in c)for c in O['hcols'](h)]
 return flin(HC[h],v)
def hat(h,a):return tuple(hv(h,v)for v in a)
def h3t(h,a):return tuple(h3(h,v)for v in a)
def newa(g):return va(va(O['mix'](E,g[0]),ag),hat(g[2],ag))
SELECT=(4,5,6,7)
PERM=(1,0,3,2)
CPERM=(0,1,3,2)
BPERM=(1,0,2,3)
slots=[(r,i)for r in range(4)for i in range(4)if r!=i]
assert len(slots)==12
zperm=[slots.index((PERM[r],PERM[i]))for r,i in slots]
czperm=[slots.index((CPERM[r],CPERM[i]))for r,i in slots]
bzperm=[slots.index((BPERM[r],BPERM[i]))for r,i in slots]
def perm_a(a):return tuple(a[j]for j in PERM)
def perm_z(z):return tuple(z[j]for j in zperm)
def cperm_a(a):return tuple(a[j]for j in CPERM)
def cperm_z(z):return tuple(z[j]for j in czperm)
def ac(g):return tuple(newa(g)[i]for i in SELECT)
def cup(a,b):return tuple(star(sq(a[r]),b[i])for r,i in slots)
N1=(AZ,TZ,O['HN0'])
def nm(g,h):
 a,z,q=g;b,t,r=h;hb=hat(q,b)
 return(va(a,hb),va(va(z,h3t(q,t)),cup(a,hb)),O['hmul'](q,r))
def ni(g):
 a,z,h=g;hh=O['hinv'](h)
 out=(hat(hh,a),h3t(hh,va(z,cup(a,a))),hh)
 assert nm(g,out)==nm(out,g)==N1
 return out
def nin(g,h):return nm(nm(g,h),ni(g))
ONE=(O['ONE'],TZ)
def em(g,h):
 b,z=g;c,t=h
 return(O['em'](b,c),va(va(z,h3t(b[2],t)),cup(ac(b),hat(b[2],ac(c)))))
def ei(g):
 b,z=g;bb=O['ei'](b)
 out=(bb,h3t(bb[2],va(z,cup(ac(b),ac(b)))))
 assert em(g,out)==em(out,g)==ONE
 return out
def ein(g,h):return em(em(g,h),ei(g))
def ep(g,n):
 out=ONE
 while n:
  if n&1:out=em(out,g)
  g=em(g,g);n>>=1
 return out
SS=(O['SS'],TZ);ra=hat(O['HR'],ac(O['RR']))
nr=nin((ra,TZ,O['HN0']),(AZ,TZ,O['HR']))
assert nr[0]==ac(O['RR'])
RR=(O['RR'],nr[1]);TT=em(SS,RR)
assert ep(SS,2)==ep(RR,3)==ONE
def cv(v):return flin(O['CV'],v)
ags=tuple(ag[i]for i in SELECT)
ecw=tuple(O['mix'](E,O['WC'])[i]for i in SELECT)
CW=va(va(ecw,ags),tuple(cv(v)for v in cperm_a(ags)))
epw=tuple(O['mix'](E,tup(w['WE'])[0])[i]for i in SELECT)
PW=va(va(epw,ags),perm_a(ags))
CV3=[tuple(fp(x,3)for x in c)for c in O['CV']]
def cv(v):return flin(O['CV'],v)
def cv3(v):return flin(CV3,v)
def c0(g):
 b,z=g
 n=nin((CW,TZ,O['HN0']),(tuple(cv(v)for v in cperm_a(ac(b))),tuple(cv3(v)for v in cperm_z(z)),O['hc'](b[2])))
 old=oc(b);assert n[0]==ac(old)and n[2]==old[2]
 return(old,n[1])
def p0(g):
 b,z=g;n=nin((PW,TZ,O['HN0']),(perm_a(ac(b)),perm_z(z),b[2]));old=op(b)
 assert n[0]==ac(old)and n[2]==old[2]
 return(old,n[1])
def eta(g,c):
 v=zero
 for a,x in zip(c[:8],newa(g)):v=fva(v,fsm(a,j3(x)))
 return fva(v,fva(c[8:],h3(g[2],c[8:])))
def etas(g,cs):return tuple(eta(g,c)for c in cs)
def basis(i,n):return tuple(int(i==j)for j in range(n))
CB=[basis(i,44)for i in range(44)];VB=O['VB']
def sr(v):return fourth(O['sres'](ji3(v)))
cc=[eta(oc(O['SS']),v)+eta(oc(O['RR']),v)for v in CB]
assert O['frank'](cc)==44
cs,cr=c0(SS),c0(RR);ct=em(em(SS,ei(RR)),SS);CCOR=[]
for j in range(12):
 sol=O['fsolve'](cc,fva(cs[1][j],SS[1][j])+fva(cr[1][j],ct[1][j]));assert sol is not None;CCOR.append(sol)
def ca(g):
 b,z=c0(g);return(b,va(z,etas(b,CCOR)))
assert ca(SS)==SS and ca(RR)==ct and ca(TT)==ei(TT)
assert ca(ca(SS))==SS and ca(ca(RR))==RR
BB=(tup(w['BFRAME']),TZ);JS=(tup(w['JFRAME']),TZ)
ps,pt=p0(SS),p0(TT);bs=ein(BB,SS)
pc=[eta(O['TT'],v)+sr(h3(O['HB'],eta(O['SS'],v)))for v in CB]
assert O['frank'](pc)==40
PCOR=[]
for j in range(12):
 sol=O['fsolve'](pc,fva(pt[1][j],TT[1][j])+sr(h3(O['HB'],fva(ps[1][j],bs[1][j]))))
 assert sol is not None;PCOR.append(sol)
def ph(g):
 b,z=p0(g);return(b,va(z,etas(g[0],PCOR)))
def na(g):return ph(ca(g))
assert ph(TT)==TT
sd,rd=na(na(SS)),na(na(RR));assert sd[0]==SS[0]and rd[0]==RR[0]
cob=[fva(v,h3(O['HS'],v))+fva(v,h3(O['HR'],v))for v in VB]
INNER=[]
for j in range(12):
 sol=O['fsolve'](cob,fva(sd[1][j],SS[1][j])+fva(rd[1][j],RR[1][j]));assert sol is not None;INNER.append(sol)
INNER=tuple(INNER)
assert h3t(O['HT'],INNER)==INNER and tuple(cv3(INNER[bzperm[j]])for j in range(12))==INNER
assert ein((O['ONE'],INNER),SS)==sd and ein((O['ONE'],INNER),RR)==rd
out=dict(scope='Actual binary offdiagonal12 ordinary-cup quotient; specified old affine action and s-frame class; no arbitrary-old-data exhaustion',source_witness=str(wpath),
 canonical_c_corrections=CCOR,positive_corrections=PCOR,inner_square=INNER,source_R_central=RR[1],
 inner_nonzero=any(any(v)for v in INNER),selected_positive_inner=PW,mixed_slots=[(SELECT[r],SELECT[i])for r,i in slots])
print('Actual binary offdiagonal12 source/canonical-c/peripheral action: PASS',flush=True)
fixed=[j for j in range(12)if bzperm[j]==j]
assert [slots[j]for j in fixed]==[(2,3),(3,2)]
fixed_bad=[j for j in fixed if any(INNER[j])]
out.update(negative_fixed_slots=[(SELECT[slots[j][0]],SELECT[slots[j][1]])for j in fixed],fixed_square_failure_coordinates=fixed_bad)
print('Initial inner square nonzero:',out['inner_nonzero'],'; fixed-copy failures:',fixed_bad,flush=True)
assert all(cv3(j3(v))==j3(v)for v in O['TF'])
if not fixed_bad:
 ACOR=[zero]*12
 for j in range(12):
  if j<bzperm[j]:ACOR[j]=INNER[j]
 ACOR=tuple(ACOR)
 assert va(ACOR,tuple(cv3(ACOR[bzperm[j]])for j in range(12)))==INNER
 assert h3t(O['HT'],ACOR)==ACOR
 old_ph=ph
 def ph(g):return ein((O['ONE'],ACOR),old_ph(g))
 assert ph(TT)==TT and na(na(SS))==SS and na(na(RR))==RR
 out['inner_action_correction']=ACOR;out['initial_inner_nonzero']=out['inner_nonzero'];out['inner_nonzero']=False
 print('Regular-pair correction gives negative square one: PASS',flush=True)
 b=(tup(w['BFRAME']),TZ);bg=ein(b,SS);target=ph(SS)
 cc=[fva(v,h3(target[0][2],v))for v in VB];co=[]
 for j in range(12):
  sol=O['fsolve'](cc,fva(target[1][j],bg[1][j]));assert sol is not None;co.append(sol)
 b=(b[0],tuple(co));assert ein(b,SS)==target
 norm_value=em(ei(b),na(ei(b)));assert norm_value[0]==O['ONE']
 SF3=[j3(v)for v in O['SF']]
 def dn(v):return h3(O['HB'],cv3(v))
 nc=[fva(v,dn(v))for v in SF3];fixes=[zero]*12;sbad=[]
 for j in range(12):
  assert h3(O['HS'],norm_value[1][j])==norm_value[1][j]
  assert norm_value[1][bzperm[j]]==dn(norm_value[1][j])
  if j<bzperm[j]:fixes[j]=norm_value[1][j]
  elif j==bzperm[j]:
   sol=O['fsolve'](nc,norm_value[1][j])
   if sol is None:sbad.append(j)
   else:fixes[j]=flin(SF3,sol)
 out['s_failure_coordinates']=sbad;out['s_initial_norm']=norm_value[1]
 print('Fixed-copy s-normalizer failures:',sbad,flush=True)
 if not sbad:
  b=em(b,(O['ONE'],tuple(fixes)))
  assert ein(b,SS)==target and em(ei(b),na(ei(b)))==ONE
  out['BFRAME']=b;print('Complete actual12 s-conjugacy and norm PASS',flush=True)
else:
 print('Fixed-copy square is unchanged by the complete literal-cusp inner freedom; stored old-data scope only.',flush=True)
out['r_frame_status']='not_tested'
(HERE/outname).write_text(json.dumps(out,indent=2)+'\n')
print('No conclusion about other old affine data, complete scalar refinement, or the full involution.',flush=True)
