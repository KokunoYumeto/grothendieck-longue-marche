"""Working exact class-two model for A59's additional central frame problem.

This file is exploratory until the actual source and all frame equations
have been checked. It does not promote any search failure to an obstruction.
The first four multiplicity rows are over GR(4,3), the last four over F8.
"""
from pathlib import Path
import runpy,json
HERE=Path(__file__).resolve().parent
I=runpy.run_path(str(HERE.parent/'work_CE/code/check_Q6_integral_cusp.py'))
G=I['G'];ADD=I['ADD'];MUL=I['MUL'];NEG=I['NEG'];TEICH=I['TEICH']
red=I['red'];fm=G['fm'];fva=G['fva'];fsm=G['fsm'];zero=G['zero'];e=G['e']
Q=G['Q'];mul=G['mul'];inv=G['inv'];NC=G['NC'];CC=G['CC'];kappa=G['kappa']
sm=G['sm'];va=G['va'];lin=G['lin'];parity=G['parity'];s=G['s'];r=G['r']
zpairs=[(i,j)for i in range(8)for j in range(i,8)]
zfree=[i<j<4 for i,j in zpairs]
chars=G['chars'];charindex={v:i for i,v in enumerate(chars)}
partner=[charindex[sm(6,v)]for v in chars]
vpairs=[(i,j)for i,j in enumerate(partner)if i<j]
assert len(vpairs)==18
AA0=((0,)*36,)*8;ZA=(0,)*36;HN0=(zero,e)

def av(a,b):
 return tuple(tuple(ADD[x][y]for x,y in zip(v,w))if i<4 else fva(v,w)
              for i,(v,w)in enumerate(zip(a,b)))
def an(a):return tuple(tuple(NEG[x]for x in v)if i<4 else v for i,v in enumerate(a))
def za(a,b):return tuple(ADD[x][y]if free else x^y for x,y,free in zip(a,b,zfree))
def zn(a):return tuple(NEG[x]if free else x for x,free in zip(a,zfree))
def zs(c,a):
 return tuple(MUL[c][x]if free else fm(red(c),x)for x,free in zip(a,zfree))
def weight(a,j):return tuple(v[j]for v in a)
def residue(a,i):return red(a[i])if i<4 else a[i]
def tensor(a,b):
 out=[]
 for i,j in zpairs:
  if i<j<4:out.append(ADD[MUL[a[i]][b[j]]][NEG[MUL[a[j]][b[i]]]])
  elif i==j:out.append(fm(residue(a,i),residue(b,i)))
  else:out.append(fm(residue(a,i),residue(b,j))^fm(residue(a,j),residue(b,i)))
 return tuple(out)
def pcoc(a,b):
 out=ZA
 for i,j in vpairs:out=za(out,tensor(weight(a,i),weight(b,j)))
 return out
def hmul(g,h):
 n,q=g;m,t=h
 return(va(n,lin(NC[q],m)),mul[q][t])
def hinv(g):
 n,q=g;t=inv[q]
 return(sm(6,lin(NC[t],n)),t)
def hc(g):return(lin(CC,g[0]),kappa[g[1]])
def eps(h):return parity(Q[h[1]][0])
HM={}
def hmon(h):
 if h not in HM:
  cs=[G['vaction'](h[0],h[1],v)for v in G['VB']]
  pp=[];ww=[]
  for col in cs:
   nz=[i for i,a in enumerate(col)if a];assert len(nz)==1
   pp.append(nz[0]);ww.append(TEICH[col[nz[0]]])
  HM[h]=(tuple(pp),tuple(ww))
 return HM[h]
def monapply(mon,a,z=ZA):
 pp,ww=mon;out=[]
 for row,v in enumerate(a):
  w=[0]*36
  for i,x in enumerate(v):w[pp[i]]=MUL[ww[i]][x]if row<4 else fm(red(ww[i]),x)
  out.append(tuple(w))
 zz=z
 for i,j in vpairs:
  assert partner[pp[i]]==pp[j] and MUL[ww[i]][ww[j]]==1
  if pp[i]>pp[j]:zz=za(zz,zn(tensor(weight(a,i),weight(a,j))))
 return tuple(out),zz

# The C4 carry QS is assigned after the actual source s-vector is loaded.
QS=ZA
ONE=(AA0,ZA,HN0)
def em(g,h):
 a,z,q=g;b,w,t=h
 rb,rw=monapply(hmon(q),b,w)
 zz=za(za(z,rw),pcoc(a,rb))
 if eps(q)and eps(t):zz=za(zz,QS)
 return(av(a,rb),zz,hmul(q,t))
def ei(g):
 a,z,q=g;t=hinv(q)
 bb,_=monapply(hmon(t),an(a))
 _,carry=monapply(hmon(q),bb)
 zz=za(za(z,carry),pcoc(a,an(a)))
 if eps(q):zz=za(zz,QS)
 out=(bb,zn(zz),t)
 assert em(g,out)==em(out,g)==ONE
 return out
def ep(g,n):
 out=ONE
 while n:
  if n&1:out=em(out,g)
  g=em(g,g);n>>=1
 return out
def ein(g,h):return em(em(g,h),ei(g))

def zbits(z):
 # Eighteen coordinates in O, counted as 6 binary coefficient digits,
 # and ninety binary coordinates in k. The noncanonical base4 encoding
 # is converted digitwise; this is only a serialization, not linearity.
 out=0;shift=0
 for x,free in zip(z,zfree):
  out|=x<<shift;shift+=6 if free else 3
 assert shift==126
 return out
def central_kernel(z):
 # The new center consists of the doubled O off-diagonals only.
 out=0;shift=0
 for x,free in zip(z,zfree):
  if free:
   assert red(x)==0
   a=sum(((x>>(2*i+1))&1)<<i for i in range(3))
   out|=a<<shift;shift+=3
  else:assert x==0
 assert shift==18
 return out

print('A59 integral class-two operations prepared: center O^6 plus k^30; no frame conclusion yet.')

def tup(x):return tuple(tup(y)for y in x)if isinstance(x,list)else x
data=json.loads((HERE.parent/'work_CE/Q6_integral_affine_data.json').read_text())
DS=tup(data['free_s_values'])+tup(data['binary_s_values'])
DR=tup(data['free_r_values'])+tup(data['binary_r_values'])
HS=(zero,s);HR=(G['dr'],r);HB=tup(data['s_frame_head'])
Sraw=(DS,ZA,HS)
sq=ep(Sraw,2);assert sq[0]==AA0 and sq[2]==HN0
QS=zn(sq[1]);assert za(QS,QS)==ZA
SS=(DS,ZA,HS);assert ep(SS,2)==ONE
Rraw=(DR,ZA,HR)
cu=ep(Rraw,3);assert cu[0]==AA0 and cu[2]==HN0
RZ=zn(zs(3,cu[1]));RR=(DR,RZ,HR);assert ep(RR,3)==ONE
TT=em(SS,RR)
print('Actual integral source s²=r³=1 after the prescribed central carry and odd correction: PASS')

BS=tup(data['positive_binary_cohomology_columns'])
CS=tup(data['c_binary_cohomology_columns'])
def amix(a,coh,sign=1):
 free=a[:4]if sign==1 else tuple(tuple(NEG[x]for x in v)for v in a[:4])
 return free+tuple(G['flin'](a[4:],col)for col in coh)
def zmix(z,coh,sign=1):
 cols=[]
 for j in range(8):
  if j<4:cols.append(tuple((1 if sign==1 else 3)if i==j else 0 for i in range(8)))
  else:cols.append((0,)*4+tuple(coh[i][j-4]for i in range(4)))
 out=ZA
 for value,(i,j),free in zip(z,zpairs,zfree):
  if value:
   col=tensor(cols[i],cols[j])
   out=za(out,zs(value if free else TEICH[value],col))
 return out
assert zmix(QS,BS)==QS and zmix(QS,CS,-1)==QS
def ln(g):return(amix(g[0],BS),zmix(g[1],BS),g[2])
def gn(g):
 a,z=monapply(I['C'],amix(g[0],CS,-1),zmix(g[1],CS,-1))
 return(a,z,hc(g[2]))
WC=tup(data['new_c_inner_free_O'])+tup(data['new_c_inner_binary_k'])
WCE=(WC,ZA,HN0)
def c0(g):return ein(WCE,gn(g))
cs=em(c0(SS),ei(SS));assert cs[0]==AA0 and cs[2]==HN0
CSHIFT=zn(cs[1]);assert za(CSHIFT,CSHIFT)==ZA
def ca(g):
 a,z,h=c0(g)
 if eps(g[2]):z=za(z,CSHIFT)
 return(a,z,h)
assert ca(SS)==SS
assert ca(RR)==em(em(SS,ei(RR)),SS)
assert ca(TT)==ei(TT)
assert ca(ca(SS))==SS and ca(ca(RR))==RR
print('Actual integral c reconstructed literally on s,r,tau: PASS')

W=tup(data['positive_inner_free_O'])+tup(data['positive_inner_binary_k'])
WE=(W,ZA,HN0)
def phi0(g):return ein(WE,ln(g))
td=em(phi0(TT),ei(TT));assert td[0]==AA0 and td[2]==HN0
PSHIFT=zn(td[1])
assert za(PSHIFT,PSHIFT)==ZA,('cusp character not order2',PSHIFT)
def ph(g):
 a,z,h=phi0(g)
 if eps(g[2]):z=za(z,PSHIFT)
 return(a,z,h)
def na(g):return ph(ca(g))
assert ph(TT)==TT
assert na(na(SS))==SS and na(na(RR))==RR
print('Actual integral positive cusp and negative square on the exact stable scalar quotient: PASS')

from contextlib import redirect_stdout
from io import StringIO
with redirect_stdout(StringIO()):OLD=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
oldw=json.loads((HERE/'Q6_actual_central_solution.json').read_text())
E=tup(data['new_basis_columns_in_old_EB']);ag=tup(data['cochain_coboundary_in_V8'])
def reduce_a(a):return tuple(tuple(red(x)for x in v)if i<4 else v for i,v in enumerate(a))
def reduce_z(z):return tuple(red(x)if free else x for x,free in zip(z,zfree))
def old_to_new0(g):
 a,z,h=g
 a=OLD['mix'](E,a);z=OLD['zaction'](E,z)
 return OLD['ein']((ag,OLD['ZA'],OLD['HN0']),(a,z,h))
os=old_to_new0(OLD['SS'])
assert os[0]==reduce_a(SS[0]) and os[2]==SS[2]
SCHAR=os[1]
def old_to_new(g):
 a,z,h=old_to_new0(g)
 if eps(h):z=G['fva'](z,SCHAR)
 return(a,z,h)
assert old_to_new(OLD['SS'])==(reduce_a(SS[0]),reduce_z(SS[1]),SS[2])
assert old_to_new(OLD['RR'])==(reduce_a(RR[0]),reduce_z(RR[1]),RR[2])
assert old_to_new(OLD['TT'])==(reduce_a(TT[0]),reduce_z(TT[1]),TT[2])
oldbeta=old_to_new(tup(oldw['BFRAME']))
assert oldbeta[0]==reduce_a(tup(data['s_frame_free_O'])+tup(data['s_frame_binary_k']))
BSTART=tuple(TEICH[x]if free else x for x,free in zip(oldbeta[1],zfree))
BFRAME=(tup(data['s_frame_free_O'])+tup(data['s_frame_binary_k']),BSTART,HB)
print('Stored old central frame transported through literal cochain/source isomorphism: PASS')
sd=em(ph(SS),ei(ein(BFRAME,SS)))
assert sd[0]==AA0 and sd[2]==HN0
print('s-conjugacy residual in new center:',central_kernel(sd[1]))
assert sd==ONE
bn=em(ei(BFRAME),na(ei(BFRAME)))
assert bn[0]==AA0 and bn[2]==HN0
print('s-normalizer square in new center:',central_kernel(bn[1]))
if __name__=='__main__':
 (HERE/'A59_integral_center_baseline.json').write_text(json.dumps(dict(
  status='Exact actual central source/action checked; final normalizer correction pending',
  QS=QS,RZ=RZ,CSHIFT=CSHIFT,WE=WE,PSHIFT=PSHIFT,BFRAME=BFRAME,
  s_square=bn[1],s_square_bits=central_kernel(bn[1])),indent=2)+'\n')
print('No simultaneous final frame or full lift claim is made by this baseline calculation.')
