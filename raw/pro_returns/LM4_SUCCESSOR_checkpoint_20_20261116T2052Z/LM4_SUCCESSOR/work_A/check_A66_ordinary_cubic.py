"""Actual ordinary16 cubic-cup quotient over an explicit A56 witness.
This independent projection forgets all six previous cross-cup coordinates.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json,sys
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):O=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
wpath=Path(sys.argv[1])if len(sys.argv)>1 else HERE/'A63_zero_t_A56_solution.json'
outname=sys.argv[2]if len(sys.argv)>2 else 'A66_ordinary_cubic_result.json'
w=json.loads(wpath.read_text())
def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
O['phi0'].__globals__['WE']=tup(w['WE']);O['ph'].__globals__['PSHIFT']=tup(w['PSHIFT'])
op,oc=O['ph'],O['ca'];fm,fp,flin,fva,fsm=O['fm'],O['fp'],O['flin'],O['fva'],O['fsm']
zero=(0,)*36;AZ=(zero,)*4;TZ=(zero,)*16
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
def ac(g):return newa(g)[:4]
def cup(a,b):return tuple(star(sq(a[r]),b[i])for r in range(4)for i in range(4))
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
CW=tuple(tuple(x&1|((x>>2)&1)<<1|((x>>4)&1)<<2 for x in row)for row in ad['new_c_inner_free_O'])
PW=O['mix'](E,tup(w['WE'])[0])[:4]
CV3=[tuple(fp(x,3)for x in c)for c in O['CV']]
def cv(v):return flin(O['CV'],v)
def cv3(v):return flin(CV3,v)
def c0(g):
 b,z=g
 n=nin((CW,TZ,O['HN0']),(tuple(cv(v)for v in ac(b)),tuple(cv3(v)for v in z),O['hc'](b[2])))
 old=oc(b);assert n[0]==ac(old)and n[2]==old[2]
 return(old,n[1])
def p0(g):
 b,z=g;n=nin((PW,TZ,O['HN0']),(ac(b),z,b[2]));old=op(b)
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
for j in range(16):
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
for j in range(16):
 sol=O['fsolve'](pc,fva(pt[1][j],TT[1][j])+sr(h3(O['HB'],fva(ps[1][j],bs[1][j]))))
 assert sol is not None;PCOR.append(sol)
def ph(g):
 b,z=p0(g);return(b,va(z,etas(g[0],PCOR)))
def na(g):return ph(ca(g))
assert ph(TT)==TT
sd,rd=na(na(SS)),na(na(RR));assert sd[0]==SS[0]and rd[0]==RR[0]
cob=[fva(v,h3(O['HS'],v))+fva(v,h3(O['HR'],v))for v in VB]
INNER=[]
for j in range(16):
 sol=O['fsolve'](cob,fva(sd[1][j],SS[1][j])+fva(rd[1][j],RR[1][j]));assert sol is not None;INNER.append(sol)
INNER=tuple(INNER)
assert h3t(O['HT'],INNER)==INNER and tuple(cv3(v)for v in INNER)==INNER
assert ein((O['ONE'],INNER),SS)==sd and ein((O['ONE'],INNER),RR)==rd
out=dict(scope='Ordinary16-cup quotient; specified A56 affine action/frame',source_witness=str(wpath),
 canonical_c_corrections=CCOR,positive_corrections=PCOR,inner_square=INNER,source_R_central=RR[1],
 inner_nonzero=any(any(v)for v in INNER),free_positive_inner=PW)
print('Actual ordinary16 source/canonical-c/peripheral positive action: PASS',flush=True)
print('Free positive cusp inner nonzero:',any(any(v)for v in PW),'; negative inner square nonzero:',out['inner_nonzero'],flush=True)
assert all(cv3(j3(v))==j3(v)for v in O['TF'])
print('Every literal-cusp inner correction has zero negative norm: checked on full cusp basis.',flush=True)
if not out['inner_nonzero']:
 assert na(na(SS))==SS and na(na(RR))==RR
 def frame(base,gen,target,central_basis,head):
  b=(base,TZ);bg=ein(b,gen);co=[]
  cols=[fva(v,h3(target[0][2],v))for v in VB]
  for j in range(16):
   sol=O['fsolve'](cols,fva(target[1][j],bg[1][j]));assert sol is not None;co.append(sol)
  b=(base,tuple(co));assert ein(b,gen)==target
  sq=em(ei(b),na(ei(b)));assert sq[0]==O['ONE']
  nc=[fva(v,h3(head,cv3(v)))for v in central_basis]
  fixes=[]
  for j in range(16):
   sol=O['fsolve'](nc,sq[1][j])
   if sol is None:return None,O['frank'](nc),sq[1],j
   fixes.append(flin(central_basis,sol))
  b=em(b,(O['ONE'],tuple(fixes)))
  assert ein(b,gen)==target and em(ei(b),na(ei(b)))==ONE
  return b,O['frank'](nc),sq[1],None
 bf,srank,snorm,sbad=frame(tup(w['BFRAME']),SS,ph(SS),[j3(v)for v in O['SF']],O['HB'])
 if w.get('r_frame_norm_solved',True):
  jf,jrank,jnorm,jbad=frame(tup(w['JFRAME']),ei(RR),na(RR),[j3(v)for v in O['RF']],O['HS'])
 else:
  jf,jrank,jnorm,jbad=None,None,None,'Old displayed r-frame norm remains unresolved; new r test skipped.'
 out.update(BFRAME=bf,JFRAME=jf,s_rank=srank,r_rank=jrank,s_initial_norm=snorm,r_initial_norm=jnorm,
            s_failure_coordinate=sbad,r_failure_coordinate=jbad,
            r_frame_status='not_tested'if jrank is None else('solved'if jf is not None else'unsolved'),
            r_frame_solvable=None if jrank is None else jf is not None)
 if jrank is None:
  print('Ordinary s-frame rank',srank,'solvable',bf is not None,'; r-frame: not tested (broader transporter argument).',flush=True)
 else:
  print('Ordinary s-frame rank',srank,'solvable',bf is not None,'; r-frame rank',jrank,'solvable',jf is not None,flush=True)
(HERE/outname).write_text(json.dumps(out,indent=2)+'\n')
print('No exhaustion of other old affine data or scalar-refinement claim.',flush=True)
