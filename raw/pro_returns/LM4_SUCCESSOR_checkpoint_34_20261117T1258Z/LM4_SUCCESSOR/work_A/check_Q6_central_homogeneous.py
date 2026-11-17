"""Reconstructed exact search and direct witness for the Q6 central frames.

The known pre-outage core mask is used only as a candidate. Every quadratic
identity, original group operation, and final frame equation is recomputed.
The independent C++ program can rediscover the same candidate by Gray search.
"""
from pathlib import Path
import json, runpy
import numpy as np
HERE=Path(__file__).resolve().parent
globals().update(runpy.run_path(str(HERE/'check_Q6_central_cover.py')))
assert sol is not None and zsol is None

def bit_kernel(cols):
 piv={};ker=[]
 for j,value in enumerate(cols):
  v=int(value);aux=1<<j
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i][0];aux^=piv[i][1]
   else:piv[i]=(v,aux);break
  if not v:ker.append(aux)
 return ker

def reducer(cols):
 piv={}
 for value in cols:
  v=int(value)
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i]
   else:piv[i]=v;break
 def reduce(value):
  v=int(value)
  for i in sorted(piv,reverse=True):
   if v>>i&1:v^=piv[i]
  return v
 return reduce,len(piv)

KH=bit_kernel(ECOLS)
assert len(KH)==277
NBITS=[packed(fsm(a,v))for v in ZNORM for a in(1,2,4)]
nreduce,nrank=reducer(NBITS)
HOM=[]
for mask in KH:
 tc=AA0;sc=AA0
 for j,(kind,i,a)in enumerate(LABELS):
  if mask>>j&1:
   vv=tuple(fsm(a,row)for row in(TBASE if kind=='tau'else SBASE)[i])
   if kind=='tau':tc=av(tc,vv)
   else:sc=av(sc,vv)
 HOM.append((tc,sc))

def qnorm(pair):
 t,u=pair;pt=(t,ZA,HN0);pu=(u,ZA,HN0)
 nt=em(pt,na(pt));du=ein(ei(BFRAME),na(pu));nu=em(pu,du)
 assert nt[0]==nu[0]==AA0 and nt[2]==nu[2]==HN0
 return nreduce(packed(fva(nt[1],nu[1])))

FM=np.array([[fm(i,j)for j in range(8)]for i in range(8)],dtype=np.uint8)
LEFT=np.array([i for i,j in vpairs]);RIGHT=np.array([j for i,j in vpairs])
NHOM=[tuple(np.array(v,dtype=np.uint8)for v in pair)for pair in HOM]
def polar_pair(pair,other):
 total=np.zeros((8,8),dtype=np.uint8)
 for aa,bb in zip(pair,other):
  total^=np.bitwise_xor.reduce(FM[aa[:,LEFT,None],bb.T[RIGHT][None,:,:]],axis=1)
  total^=np.bitwise_xor.reduce(FM[aa[:,RIGHT,None],bb.T[LEFT][None,:,:]],axis=1)
 z=tuple(int(total[i,j]^(total[j,i]if i!=j else 0))for i,j in zpairs)
 return nreduce(packed(z))

QVAL=[qnorm(pair)for pair in HOM]
BP=[[0]*len(HOM)for _ in HOM]
for i in range(len(HOM)):
 for j in range(i):BP[i][j]=BP[j][i]=polar_pair(NHOM[i],NHOM[j])
for i,j in((0,1),(8,16),(99,201),(175,276)):
 pair=tuple(av(a,b)for a,b in zip(HOM[i],HOM[j]))
 assert qnorm(pair)==QVAL[i]^QVAL[j]^BP[i][j]

def qvalue(mask):
 ids=[i for i in range(len(HOM))if mask>>i&1];out=0
 for ii,i in enumerate(ids):
  out^=QVAL[i]
  for j in ids[:ii]:out^=BP[i][j]
 return out

target=nreduce(packed(s_square[1]))
RCOL=[sum(BP[i][j]<<(108*j)for j in range(len(HOM)))for i in range(len(HOM))]
RAD=bit_kernel(RCOL);RV=[qvalue(mask)for mask in RAD]
assert len(RAD)==250
rred,rrank=reducer(RV);assert rrank==8
span={}
def addspan(v):
 while v:
  i=v.bit_length()-1
  if i in span:v^=span[i]
  else:span[i]=v;return True
 return False
for v in RAD:assert addspan(v)
COMP=[]
for i in range(len(HOM)):
 if addspan(1<<i):COMP.append(1<<i)
assert len(COMP)==27
CQ=[rred(qvalue(v))for v in COMP]
CP=[[0]*27 for _ in range(27)]
for i in range(27):
 for j in range(i):CP[i][j]=CP[j][i]=rred(qvalue(COMP[i]^COMP[j])^qvalue(COMP[i])^qvalue(COMP[j]))
core_target=rred(target)
data=dict(n=27,q=CQ,polar=CP,target=core_target,complement=COMP,
          radical=RAD,radical_values=RV,full_target=target)
(HERE/'Q6_quadratic_core.json').write_text(json.dumps(data,indent=2)+'\n')
words=[27]
for v in CQ+[v for row in CP for v in row]+[core_target]:
 words.extend((v&((1<<64)-1),v>>64))
(HERE/'Q6_quadratic_core.in').write_text('\n'.join(map(str,words))+'\n')
print('Homogeneous class-preserving space:277 binary dimensions; polar radical250; radical image8.')
print('Remaining exact quadratic core:27 variables.')

CORE=27666
cv=0
for i in range(27):
 if CORE>>i&1:
  cv^=CQ[i]
  for j in range(i):
   if CORE>>j&1:cv^=CP[i][j]
assert cv==core_target
original=0
for i,v in enumerate(COMP):
 if CORE>>i&1:original^=v
rc,rank=bit_solve(RV,qvalue(original)^target)
assert rc is not None and rank==8
answer=original
for i,v in enumerate(RAD):
 if rc>>i&1:answer^=v
assert qvalue(answer)==target
assert answer==18677289404303020461252901246388292043973835622281379854
tc=AA0;sc=AA0
for i,(a,b)in enumerate(HOM):
 if answer>>i&1:tc=av(tc,a);sc=av(sc,b)
pt=(tc,ZA,HN0);pu=(sc,ZA,HN0)
WE=em(pt,WE)
BFRAME=em(em(pt,BFRAME),pu)
phi0.__globals__['WE']=WE
tdiff=em(phi0(TT),ei(TT));assert tdiff[0]==AA0 and tdiff[2]==HN0
PSHIFT=tdiff[1];ph.__globals__['PSHIFT']=PSHIFT
assert ph(TT)==TT and ph(SS)==ein(BFRAME,SS)
assert na(na(SS))==SS and na(na(RR))==RR
bs=em(ei(BFRAME),na(ei(BFRAME)))
assert bs[0]==AA0 and bs[2]==HN0
bz=fsolve(ZNORM,bs[1]);assert bz is not None
BFRAME=(BFRAME[0],fva(BFRAME[1],bz),BFRAME[2])
assert em(ei(BFRAME),na(ei(BFRAME)))==ONE
assert ein(ei(BFRAME),na(SS))==SS
qfinal=av(WE[0],la(WC))
assert av(qfinal,ba(qfinal))==AA0
JFRAME=(qfinal,ZA,HS)
assert na(RR)==ein(JFRAME,ei(RR))
js=em(ei(JFRAME),na(ei(JFRAME)))
assert js[0]==AA0 and js[2]==HN0
jz=fsolve(ZNORM,js[1]);assert jz is not None
JFRAME=(JFRAME[0],fva(JFRAME[1],jz),JFRAME[2])
assert em(ei(JFRAME),na(ei(JFRAME)))==ONE
assert ein(ei(JFRAME),na(RR))==ei(RR)
witness=dict(recovery='Reconstructed from reviewed source; every operation rerun.',
 core_assignment=CORE,homogeneous_mask=answer,radical_assignment=rc,
 WE=WE,PSHIFT=PSHIFT,BFRAME=BFRAME,JFRAME=JFRAME,
 s_center_correction=bz,r_center_correction=jz,all_direct_frame_checks='PASS')
(HERE/'Q6_actual_central_solution.json').write_text(json.dumps(witness,indent=2)+'\n')
print('Core candidate27666 and full homogeneous mask:',answer)
print('Original group-law checks: cusp fixation, s-conjugacy, negative square, both involutory normalizers: PASS')
print('Actual witness saved; no full-group involution or cofinality conclusion follows.')
