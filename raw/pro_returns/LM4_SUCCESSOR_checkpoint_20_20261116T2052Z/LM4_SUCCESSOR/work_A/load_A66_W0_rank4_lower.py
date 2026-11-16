"""Exact finite-head model for the actual six cross-cup extension.

Read-only verification of the stored A64 witness against the original group laws.
The stored new witnesses are checked without solving for or mutating them.
The imported old-model initialization reconstructs its coefficient matrices.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json,sys
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):O=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
wpath=HERE/'A66_W0_rank4_partial.json'
cup_path=HERE/'A66_W0_rank4_lower_result.json'
cup_witness=json.loads(cup_path.read_text())
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
CCOR=tup(cup_witness['canonical_c_corrections'])
PCOR=tup(cup_witness['positive_corrections'])
def ca(g):
 old,z=c0(g);return(old,tv(z,eta6(old,CCOR)))
def p0(g):
 og,z=g;n=nin(WW,(ac(og),z,og[2]));old=op(og)
 assert n[0]==ac(old) and n[2]==old[2]
 return(old,n[1])
def ph(g):
 old,z=p0(g);return(old,tv(z,eta6(g[0],PCOR)))
def na(g):return ph(ca(g))
assert RR[1]==tup(cup_witness['source_R_central'])
assert ca(SS)==SS and ca(RR)==ctarget and ca(TT)==ei(TT)
assert ca(ca(SS))==SS and ca(ca(RR))==RR
assert ph(TT)==TT and na(TT)==ei(TT)
assert na(na(SS))==SS and na(na(RR))==RR
BFRAME=tup(cup_witness['BFRAME'])
JFRAME=(tup(w['JFRAME']),TZ)
assert BFRAME[0]==tup(w['BFRAME'])
assert ph(SS)==ein(BFRAME,SS)
assert em(ei(BFRAME),na(ei(BFRAME)))==ONE
assert not any(any(v)for v in PCOR)
assert not any(any(v)for v in ww)
print('W0 lower-cup model: actual source, canonical c, identity free-cusp positive action and s-frame PASS; r coordinates not tested.')
