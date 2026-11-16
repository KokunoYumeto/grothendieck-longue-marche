"""Actual class-three20-chief quotient above the A64 zero-t witness.
Exploratory action/norm computation; scalar refinement is a separate gate.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):P=runpy.run_path(str(HERE/'check_A64_cross_cup_witness.py'))
O=P['O'];fm=O['fm'];fp=O['fp'];fva=O['fva'];fsm=O['fsm'];flin=O['flin']
def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
zero=(0,)*36;AZ=(zero,)*4;TZ=(zero,)*6;ZZ=(zero,)*20
pairs=[(i,j)for i in range(4)for j in range(i+1,4)]
triples=[(i,j,k)for i in range(4)for j in range(i+1,4)for k in range(j+1,4)]
pindex={p:i for i,p in enumerate(pairs)}
zindex={(r,i):4+4*r+i for r in range(4)for i in range(4)}
def va(a,b):return tuple(fva(x,y)for x,y in zip(a,b))
def star(a,b):return tuple(fm(x,y)for x,y in zip(a,b))
def sq(v):return tuple(fm(x,x)for x in v)
def fourth(v):return sq(sq(v))
def j3(v):return tuple(fp(v[O['partner'][i]],4)for i in range(36))
def ji3(v):return tuple(fp(v[O['partner'][i]],2)for i in range(36))
def cols3(h):return [tuple(fp(x,3)for x in c)for c in O['hcols'](h)]
H3={}
def h3(h,v):
 if h not in H3:H3[h]=cols3(h)
 return flin(H3[h],v)
def h3a(h,v):return tuple(h3(h,w)for w in v)
def h1a(h,a):return tuple(P['hv'](h,v)for v in a)
def h2a(h,a):return tuple(P['h2v'](h,v)for v in a)
def cup(a,b):return tuple(star(a[i],b[j])for i,j in pairs)
def higher(a,t,b,u):
 out=[fva(star(a[i],u[pindex[j,k]]),star(t[pindex[i,j]],b[k]))for i,j,k in triples]
 out.extend(star(sq(a[r]),b[i])for r in range(4)for i in range(4))
 return tuple(out)
K1=(AZ,TZ,ZZ,O['HN0'])
def km(g,h):
 a,t,z,q=g;b,u,w,r=h;hb=h1a(q,b);hu=h2a(q,u)
 return(va(a,hb),va(va(t,hu),cup(a,hb)),va(va(z,h3a(q,w)),higher(a,t,hb,hu)),O['hmul'](q,r))
def ki(g):
 a,t,z,h=g;hh=O['hinv'](h)
 ai=h1a(hh,a);ti=h2a(hh,va(t,cup(a,a)))
 pre=(ai,ti,ZZ,hh);err=km(g,pre)
 assert err[0]==AZ and err[1]==TZ and err[3]==O['HN0']
 out=(ai,ti,h3a(hh,err[2]),hh)
 assert km(g,out)==km(out,g)==K1
 return out
def kin(g,h):return km(km(g,h),ki(g))
def ba(g):return P['ac'](g[0])
def bh(g):return g[0][2]
def ng(g):return(ba(g[0]),g[0][1],g[1],bh(g[0]))
ONE=(P['ONE'],ZZ)
def em(g,h):
 b,z=g;c,w=h;q=bh(b)
 return(P['em'](b,c),va(va(z,h3a(q,w)),higher(ba(b),b[1],h1a(q,ba(c)),h2a(q,c[1]))))
def ei(g):
 b,z=g;bb=P['ei'](b);err=em(g,(bb,ZZ))
 assert err[0]==P['ONE']
 out=(bb,h3a(bh(bb),err[1]));assert em(g,out)==em(out,g)==ONE
 return out
def ein(g,h):return em(em(g,h),ei(g))
def ep(g,n):
 a=ONE
 while n:
  if n&1:a=em(a,g)
  g=em(g,g);n>>=1
 return a
SS=(P['SS'],ZZ)
ra=h1a(O['HR'],P['ac'](O['RR']))
kr=kin((ra,TZ,ZZ,O['HN0']),(AZ,TZ,ZZ,O['HR']))
assert kr[0]==ba(P['RR']) and kr[1]==P['RR'][1]
RR=(P['RR'],kr[2]);TT=em(SS,RR)
assert ep(SS,2)==ep(RR,3)==ONE
print('Actual20-chief source S²=R³=1 and literal projection to A64: PASS',flush=True)

LC=tuple(row[:4]for row in P['CCOR']);LP=tuple(row[:4]for row in P['PCOR'])
assert all(not any(row[4:8])for row in P['CCOR']+P['PCOR'])
VC=tuple(row[8:]for row in P['CCOR']);VP=tuple(row[8:]for row in P['PCOR'])
def lval(L,a):return tuple(flin([sq(v)for v in a],row)for row in L)
def shear(L,g):
 a,t,z,h=g;out=list(z)
 for j,(i,k,l)in enumerate(triples):
  v=zero
  for r in range(4):
   v=fva(v,fsm(L[pindex[i,k]][r],z[zindex[r,l]]))
   v=fva(v,fsm(L[pindex[k,l]][r],fva(z[zindex[r,i]],star(a[i],sq(a[r])))))
  out[j]=fva(out[j],v)
 return(a,va(t,lval(L,a)),tuple(out),h)
CW=tuple(P['wc']);PW=tuple(P['ww'])
CV3=[tuple(fp(x,3)for x in c)for c in O['CV']]
def cv3(v):return flin(CV3,v)
def mono_c(g):
 a,t,z,h=g
 return(tuple(P['cv'](v)for v in a),tuple(P['cv2'](v)for v in t),tuple(cv3(v)for v in z),O['hc'](h))
def c0(g):
 n=kin((AZ,VC,ZZ,O['HN0']),shear(LC,kin((CW,TZ,ZZ,O['HN0']),mono_c(ng(g)))))
 old=P['ca'](g[0])
 assert n[0]==ba(old)and n[1]==old[1]and n[3]==bh(old)
 return(old,n[2])
VPpost=va(VP,lval(LP,PW))
def p0(g):
 n=kin((AZ,VPpost,ZZ,O['HN0']),shear(LP,kin((PW,TZ,ZZ,O['HN0']),ng(g))))
 old=P['ph'](g[0])
 assert n[0]==ba(old)and n[1]==old[1]and n[3]==bh(old)
 return(old,n[2])

def eta(g,co):
 v=zero
 for x,a in zip(co[:8],P['newa'](g[0])):v=fva(v,fsm(x,j3(a)))
 return fva(v,fva(co[8:],h3(bh(g),co[8:])))
def etas(g,cos):return tuple(eta(g,c)for c in cos)
def basis(i,n):return tuple(int(i==j)for j in range(n))
CB=[basis(i,44)for i in range(44)];VB=O['VB']
def sr3(v):return fourth(O['sres'](ji3(v)))
for h in(O['HS'],O['HR'],O['HB'],O['HT']):
 assert all(j3(P['hv'](h,v))==h3(h,j3(v))for v in VB)
assert all(j3(P['cv'](v))==cv3(j3(v))for v in VB)
cs,cr=c0(SS),c0(RR);ctarget=em(em(SS,ei(RR)),SS)
CC=[eta(P['ca'](P['SS']),v)+eta(P['ca'](P['RR']),v)for v in CB]
assert O['frank'](CC)==44
CCOR=[]
for j in range(20):
 v=fva(cs[1][j],SS[1][j])+fva(cr[1][j],ctarget[1][j])
 sol=O['fsolve'](CC,v);assert sol is not None;CCOR.append(sol)
def ca(g):
 b,z=c0(g);return(b,va(z,etas(b,CCOR)))
assert ca(SS)==SS and ca(RR)==ctarget and ca(TT)==ei(TT)
assert ca(ca(SS))==SS and ca(ca(RR))==RR
print('Literal canonical c on the actual20-chief quotient: PASS',flush=True)

BB=(P['BFRAME'],ZZ);JS=(P['JFRAME'],ZZ)
ps,pt=p0(SS),p0(TT);bs=ein(BB,SS)
PC=[eta(P['TT'],v)+sr3(h3(O['HB'],eta(P['SS'],v)))for v in CB]
assert O['frank'](PC)==40
PCOR=[]
for j in range(20):
 target=fva(pt[1][j],TT[1][j])+sr3(h3(O['HB'],fva(ps[1][j],bs[1][j])))
 sol=O['fsolve'](PC,target);assert sol is not None;PCOR.append(sol)
def ph0(g):
 b,z=p0(g);return(b,va(z,etas(g[0],PCOR)))
def bn0(g):return ph0(ca(g))
assert ph0(TT)==TT
sd,rd=bn0(bn0(SS)),bn0(bn0(RR))
assert sd[0]==P['SS']and rd[0]==P['RR']
COB=[fva(v,h3(O['HS'],v))+fva(v,h3(O['HR'],v))for v in VB]
assert O['frank'](COB)==36
INNER=[]
for j in range(20):
 target=fva(sd[1][j],SS[1][j])+fva(rd[1][j],RR[1][j])
 sol=O['fsolve'](COB,target);assert sol is not None;INNER.append(sol)
INNER=tuple(INNER);assert h3a(O['HT'],INNER)==INNER
assert ein((P['ONE'],INNER),SS)==sd and ein((P['ONE'],INNER),RR)==rd
def flat(z):return sum(z,())
def unflat(v):return tuple(v[36*i:36*(i+1)]for i in range(20))
def bact(z):return bn0((P['ONE'],z))[1]
assert all(bact(bact(tuple(v if j==i else zero for j in range(20))))==tuple(v if j==i else zero for j in range(20))for i in range(20)for v in(VB[0],VB[13]))
TF3=[j3(v)for v in O['TF']]
assert len(TF3)==4
AB=[tuple(v if j==i else zero for j in range(20))for i in range(20)for v in TF3]
AN=[flat(va(v,bact(v)))for v in AB]
acor=O['fsolve'](AN,flat(INNER));possible=acor is not None
print('Negative inner square nonzero:',any(any(v)for v in INNER),'; cusp-inner norm rank:',O['frank'](AN),'; correctable:',possible,flush=True)
out=dict(scope='Specified zero-t A64 affine datum; actual20-chief model; scalar gate separate',
 canonical_c_corrections=CCOR,positive_corrections=PCOR,source_R_central=RR[1],inner_square=INNER,
 action_square_correctable=possible,action_norm_rank=O['frank'](AN))
if not possible:
 (HERE/'A66_cubic_twenty_result.json').write_text(json.dumps(out,indent=2)+'\n')
 raise SystemExit(0)
ACOR=unflat(flin([flat(v)for v in AB],acor))
def ph(g):return ein((P['ONE'],ACOR),ph0(g))
def na(g):return ph(ca(g))
assert ph(TT)==TT and na(na(SS))==SS and na(na(RR))==RR
print('Actual20-chief negative action square: PASS',flush=True)

def frame(base,gen,target,central_basis,head):
 B=(base,ZZ);bg=ein(B,gen);change=[]
 cols=[fva(v,h3(bh(target[0]),v))for v in VB]
 for j in range(20):
  sol=O['fsolve'](cols,fva(target[1][j],bg[1][j]));assert sol is not None;change.append(sol)
 B=(B[0],tuple(change));assert ein(B,gen)==target
 norm=em(ei(B),na(ei(B)));assert norm[0]==P['ONE']
 basis20=[tuple(v if j==i else zero for j in range(20))for i in range(20)for v in central_basis]
 def da(z):return h3a(head,na((P['ONE'],z))[1])
 nc=[flat(va(v,da(v)))for v in basis20]
 sol=O['fsolve'](nc,flat(norm[1]));rank=O['frank'](nc)
 if sol is None:return None,rank,norm[1]
 fix=unflat(flin([flat(v)for v in basis20],sol));B=em(B,(P['ONE'],fix))
 assert ein(B,gen)==target and em(ei(B),na(ei(B)))==ONE
 return B,rank,norm[1]
BFRAME,srank,snorm=frame(P['BFRAME'],SS,ph(SS),[j3(v)for v in O['SF']],O['HB'])
print('s-normalizer norm rank:',srank,'; solvable:',BFRAME is not None,flush=True)
JFRAME,jrank,jnorm=frame(P['JFRAME'],ei(RR),na(RR),[j3(v)for v in O['RF']],O['HS'])
print('r-normalizer norm rank:',jrank,'; solvable:',JFRAME is not None,flush=True)
out.update(action_inner_correction=ACOR,BFRAME=BFRAME,JFRAME=JFRAME,s_norm_rank=srank,r_norm_rank=jrank,
           s_initial_norm=snorm,r_initial_norm=jnorm,s_solvable=BFRAME is not None,r_solvable=JFRAME is not None)
(HERE/'A66_cubic_twenty_result.json').write_text(json.dumps(out,indent=2)+'\n')
if BFRAME is not None and JFRAME is not None:
 print('Actual20-chief quotient: literal cusp, negative square, BOTH projected frames and BOTH normalizer norms PASS.',flush=True)
print('The nonzero scalar refinement and full framed realization are not settled here.',flush=True)
