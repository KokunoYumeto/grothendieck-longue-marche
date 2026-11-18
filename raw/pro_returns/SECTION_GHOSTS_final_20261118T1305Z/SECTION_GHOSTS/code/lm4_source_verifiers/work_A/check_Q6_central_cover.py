"""Actual class-two central cover for the Q6 forced-frame test.

Reconstructed from the visible pre-outage source. The search stages are
exploratory; final claims use the separate direct group-law verifier.
"""
from pathlib import Path
import runpy
globals().update(runpy.run_path(str(Path(__file__).with_name('check_Q6_forced_frame.py'))))

ZA=(0,)*36;AA0=((0,)*36,)*8;HN0=((0,)*13,e)
zpairs=[(i,j)for i in range(8)for j in range(i,8)]
def sym(v,w):
 return tuple(fm(v[i],w[j])^(fm(v[j],w[i])if i!=j else 0)for i,j in zpairs)
charindex={v:i for i,v in enumerate(chars)}
partner=[charindex[sm(6,v)]for v in chars]
vpairs=[(i,j)for i,j in enumerate(partner)if i<j]
assert len(vpairs)==18 and all(partner[partner[i]]==i for i in range(36))
KQ=[g for g in range(72)if not parity(Q[g][0])]
assert len(KQ)==36 and len({ai[mul[g][reps[0]]]for g in KQ})==36
def weight(v,i):return tuple(row[i]for row in v)
def pcoc(v,w):
 out=ZA
 for i,j in vpairs:out=fva(out,sym(weight(v,i),weight(w,j)))
 return out
def monop(cs,v,z=ZA):
 dest=[];scale=[]
 for col in cs:
  i=next(i for i,a in enumerate(col)if a);assert sum(bool(a)for a in col)==1
  dest.append(i);scale.append(col[i])
 out=z
 for i,j in vpairs:
  assert partner[dest[i]]==dest[j] and fm(scale[i],scale[j])==1
  if dest[i]>dest[j]:out=fva(out,sym(weight(v,i),weight(v,j)))
 return tuple(flin(cs,row)for row in v),out
def hmul(g,h):
 n,q=g;m,rq=h
 return(va(n,lin(NC[q],m)),mul[q][rq])
def hinv(g):
 n,q=g;rq=inv[q]
 return(sm(6,lin(NC[rq],n)),rq)
def hc(g):return(lin(CC,g[0]),kappa[g[1]])
HCACHE={}
def hcols(h):
 if h not in HCACHE:HCACHE[h]=[vaction(h[0],h[1],v)for v in VB]
 return HCACHE[h]
def eps(h):return parity(Q[h[1]][0])
HS=(zero,s);HR=(dr,r);HT=hmul(HS,HR);HB=(zero,beta)
SD,qs=monop(S,DVAL)
assert SD==DVAL
QS=fva(qs,pcoc(DVAL,DVAL))
ONE=(AA0,ZA,HN0)
def em(g,h):
 a,z,q=g;b,w,rq=h
 rb,rw=monop(hcols(q),b,w)
 zz=fva(fva(z,rw),pcoc(a,rb))
 if eps(q)and eps(rq):zz=fva(zz,QS)
 return(av(a,rb),zz,hmul(q,rq))
def ei(g):
 a,z,q=g;rq=hinv(q)
 b,_=monop(hcols(rq),a)
 _,carry=monop(hcols(q),b)
 w=fva(fva(z,carry),pcoc(a,a))
 if eps(q):w=fva(w,QS)
 out=(b,w,rq);assert em(g,out)==em(out,g)==ONE
 return out
def ep(g,n):
 out=ONE
 while n:
  if n&1:out=em(out,g)
  g=em(g,g);n>>=1
 return out
def ein(g,h):return em(em(g,h),ei(g))
SS=(DVAL,ZA,HS);RR=(AA0,ZA,HR);TT=em(SS,RR)
assert ep(SS,2)==ep(RR,3)==ONE and TT[0]==DVAL and TT[1]==ZA
print('\nUniversal central cover: center Sym²(k^8), dimension36 overF8=108 overF2.')
print('The K=O²(H) weight orbit is transitive; actual s²=r³=1 after C4 repair: PASS')

def zaction(coh,z):
 lc=[tuple(coh[i][j]for i in range(8))for j in range(8)]
 cs=[sym(lc[i],lc[j])for i,j in zpairs]
 return flin(cs,z)
assert zaction(POS,QS)==QS and zaction(CE,QS)==QS
def ln(g):return(la(g[0]),zaction(POS,g[1]),g[2])
def gn(g):
 a,z,h=g
 a,z=monop(CV,mix(CE,a),zaction(CE,z))
 if eps(h):z=fva(z,QS)
 return(a,z,hc(h))
WCE=(WC,ZA,HN0)
def c0(g):return ein(WCE,gn(g))
csdiff=em(c0(SS),ei(SS));assert csdiff[0]==AA0 and csdiff[2]==HN0
CSHIFT=csdiff[1]
def ca(g):
 a,z,h=c0(g)
 if eps(g[2]):z=fva(z,CSHIFT)
 return(a,z,h)
assert ca(SS)==SS and ca(RR)==em(em(SS,ei(RR)),SS)and ca(TT)==ei(TT)
assert ca(ca(SS))==SS and ca(ca(RR))==RR
print('Actual c on the full central cover reconstructed from s,r and the C4 class: PASS')

WE=(W,ZA,HN0)
def phi0(g):return ein(WE,ln(g))
tdiff=em(phi0(TT),ei(TT));assert tdiff[0]==AA0 and tdiff[2]==HN0
PSHIFT=tdiff[1]
def ph(g):
 a,z,h=phi0(g)
 if eps(g[2]):z=fva(z,PSHIFT)
 return(a,z,h)
def na(g):return ph(ca(g))
assert ph(TT)==TT and na(na(SS))==SS and na(na(RR))==RR
BFRAME=(betaa(AA),ZA,HB)
sdiff=em(ph(SS),ei(ein(BFRAME,SS)));assert sdiff[0]==AA0 and sdiff[2]==HN0
SRES=sdiff[1]
print('Cusp-fixed central lift has an involutory negative action; s-class residue nonzero:',any(SRES))

def comm_eta(v,g):
 d=em(em((v,ZA,HN0),g),em(ei((v,ZA,HN0)),ei(g)))
 assert d[0]==AA0 and d[2]==HN0
 return d[1]
def packed(z):return sum(a<<(3*i)for i,a in enumerate(z))
def bit_solve(cs,target):
 piv={}
 for j,v in enumerate(cs):
  aux=1<<j
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i][0];aux^=piv[i][1]
   else:piv[i]=(v,aux);break
 out=0;v=target
 while v:
  i=v.bit_length()-1
  if i not in piv:return None,len(piv)
  w,a=piv[i];v^=w;out^=a
 return out,len(piv)
def expand_coeff(z,bas,blockdim):
 out=[(0,)*36 for _ in range(8)]
 for j in range(8):
  for k,v in enumerate(bas):out[j]=fva(out[j],fsm(z[j*blockdim+k],v))
 return tuple(out)
TK=fkernel(corrections);SK=fkernel(scorrections)
assert len(TK)==28 and len(SK)==92
TBASE=[expand_coeff(v,TF,len(TF))for v in TK]
SBASE=[expand_coeff(v,SF,len(SF))for v in SK]
ECOLS=[];LABELS=[]
for kind,bas,g in(('tau',TBASE,TT),('s',SBASE,SS)):
 for i,v in enumerate(bas):
  for a in(1,2,4):
   vv=tuple(fsm(a,row)for row in v)
   ECOLS.append(packed(comm_eta(vv,g)));LABELS.append((kind,i,a))
sol,rank=bit_solve(ECOLS,packed(SRES))
print('Central cusp/s-class correction rank=',rank,'of108; residue lies in image:',sol is not None)
if sol is None:
 print('UNRESOLVED CHECK: no correction found in the retained affine norm/frame solution space.')
else:
 TC=AA0;SC=AA0
 for j,(kind,i,a)in enumerate(LABELS):
  if sol>>j&1:
   v=tuple(fsm(a,row)for row in(TBASE if kind=='tau'else SBASE)[i])
   if kind=='tau':TC=av(TC,v)
   else:SC=av(SC,v)
 PT=(TC,ZA,HN0);PU=(SC,ZA,HN0)
 WE=em(PT,WE)
 BFRAME=em(em(PT,BFRAME),PU)
 tdiff=em(phi0(TT),ei(TT));assert tdiff[0]==AA0 and tdiff[2]==HN0;PSHIFT=tdiff[1]
 assert ph(TT)==TT and ph(SS)==ein(BFRAME,SS)
 assert na(na(SS))==SS and na(na(RR))==RR
 print('The actual central lift preserves s,r,tau and its negative companion squares1: PASS')
 binv=ei(BFRAME);s_square=em(binv,na(binv))
 assert s_square[0]==AA0 and s_square[2]==HN0
 ZNEG=[zaction(NEG,fbasis(i,36))for i in range(36)]
 ZNORM=[fva(fbasis(i,36),ZNEG[i])for i in range(36)]
 zsol=fsolve(ZNORM,s_square[1])
 print('Actual central s-normalizer square nonzero:',any(s_square[1]),
       '; center norm rank=',frank(ZNORM),'; correctable:',zsol is not None)
 if zsol is not None:
  BFRAME=(BFRAME[0],fva(BFRAME[1],zsol),BFRAME[2]);binv=ei(BFRAME)
  assert em(binv,na(binv))==ONE
  print('The full actual C2 x C2 s-normalizer retains the prescribed base frame: PASS')
 print('No full GT0-image conclusion is made until the mathematical construction and all retained data are reviewed.')
