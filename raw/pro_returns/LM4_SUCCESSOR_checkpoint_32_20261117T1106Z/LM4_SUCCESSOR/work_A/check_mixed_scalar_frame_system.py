"""One simultaneous exact scalar-class, scalar-norm and old-UT4 frame system.
The correction subgroup has zero abelianized coordinates and is abelian.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json
HERE=Path(__file__).resolve().parent
model=HERE/'check_mixed_scalar_action.py'
D={'__file__':str(model),'__name__':'__mixed704_model__'}
with redirect_stdout(StringIO()):exec(compile(model.read_text().split('out=dict(scope=')[0],str(model),'exec'),D)
globals().update({k:v for k,v in D.items()if k not in('__file__','__name__')})
SF3=tuple(j3(v)for v in O['SF'])
def d3(v):return act(O['HB'],act('c',(v,),3),3)[0]
JF=tuple(flin(SF3,v)for v in O['fkernel']([fva(v,d3(v))for v in SF3]));assert len(JF)==12
NB=(0,1,2,3,5,4,6,7);zp=[zi[NB[i],NB[j]]for i,j in slots]
freez=[zi[i,j]for i in range(4)for j in range(4)]
J=tup(json.loads((ROOT/'work_CE/A66_UT4_frame_surjection.json').read_text())['J'])
assert len(J)==4
Tpairs=[(i,j)for i in range(4)for j in range(i+1,4)];Tpi={ij:i for i,ij in enumerate(Tpairs)}
Utriples=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
def h2(key,v):return act(key,(v,),2)[0]
SF2=tuple(tuple(fp(x,2)for x in v)for v in O['SF'])
def d2(v):return h2(O['HB'],h2('c',v))
TJ=tuple(flin(SF2,v)for v in O['fkernel']([fva(v,d2(v))for v in SF2]));assert len(TJ)==12
EFF=act(O['HB'],av(B[0],CW))[:4]
def star(a,b):return tuple(fm(x,y)for x,y in zip(a,b))
def tnorm(t):return tuple(fva(star(EFF[i],t[Tpi[j,k]]),star(t[Tpi[i,j]],EFF[k]))for i,j,k in Utriples)
def znorm(z):return tuple(tuple(xor(fm(J[i][j],z[freez[j]][w])for j in range(16))for w in range(36))for i in range(4))
def unorm(u):return tuple(fva(v,d3(v))for v in u)
def pack(v):return sum(x<<(3*j)for j,x in enumerate(v))
def packrows(rows):return pack(tuple(x for row in rows for x in row))
def class_formula(z):return fva(fcoc(A0,z,S[0],Z0),fcoc(S[0],Z0,A0,z))
BI=gi(B)
def scalar_norm(q):
 n=gm(q,gin(BI,na(q)))
 assert n[0]==A0 and n[1]==M0 and n[2]==Z0 and n[4]==H0
 return n[3]
# output order: oldUT4 432bits, scalar s-class960bits, scalar norm960bits.
SHIFT_CLASS=432;SHIFT_NORM=1392
cols=[];labels=[];QDIR=[]
for i in range(48):
 if i>zp[i]:continue
 base=JF if i==zp[i]else SF3
 for j,v in enumerate(base):
  for a in(1,2,4):
   z=[zero]*48;z[i]=fsm(a,v)
   if i!=zp[i]:z[zp[i]]=d3(z[i])
   z=tuple(z);q=(A0,M0,z,U0,H0)
   cc=class_formula(z);nn=scalar_norm(q)
   if j==0 and a==1:
    actual=gm(gin(q,S),gi(S));assert actual[:3]==ONE[:3]and actual[4]==H0 and actual[3]==cc
   cols.append(packrows(znorm(z))|(pack(cc)<<SHIFT_CLASS)|(pack(nn)<<SHIFT_NORM));labels.append(('Z',i,j,a));QDIR.append(q)
print('Ordinary joint-fixed directions',len(cols),'bits: actual scalar class/norm evaluated.',flush=True)
for i in range(6):
 for j,v in enumerate(TJ):
  for a in(1,2,4):
   t=[zero]*6;t[i]=fsm(a,v);cols.append(packrows(tnorm(t)));labels.append(('T',i,j,a));QDIR.append(None)
for i in range(4):
 for j,v in enumerate(SF3):
  for a in(1,2,4):
   u=[zero]*4;u[i]=fsm(a,v);cols.append(packrows(unorm(u)));labels.append(('U',i,j,a));QDIR.append(None)
VB36=[tuple(int(i==j)for j in range(36))for i in range(36)]
OMN=[fva(v,O['na']((O['AA0'],v,H0))[1])for v in VB36]
OMK=tuple(O['fkernel'](OMN));assert len(OMK)==29
for i,v in enumerate(OMK):
 for a in(1,2,4):
  m=oldm(fsm(a,v));q=(A0,m,Z0,U0,H0);nn=scalar_norm(q)
  assert gin(q,S)==S
  cols.append(pack(nn)<<SHIFT_NORM);labels.append(('M',i,0,a));QDIR.append(q)
# A basis of the actual central norm image; retain exact preimages.
cpiv={};CBAS=[]
for i in range(320):
 for a in(1,2,4):
  u=stem(tuple(a if i==j else 0 for j in range(320)));nu=fva(u,permu(u,NB));v=pack(nu)
  while v:
   j=v.bit_length()-1
   if j in cpiv:v^=cpiv[j]
   else:cpiv[j]=v;CBAS.append(u);break
for i,u in enumerate(CBAS):
 cols.append(pack(fva(u,permu(u,NB)))<<SHIFT_NORM);labels.append(('SCALAR',i,0,1));QDIR.append((A0,M0,Z0,u,H0))
assert len(CBAS)==168
TARGET=(pack(SCLASS)<<SHIFT_CLASS)|(pack(bn[3])<<SHIFT_NORM)
sol,rank=O['bit_solve'](cols,TARGET)
print('Simultaneous variables',len(cols),'rank',rank,'target solvable',sol is not None,flush=True)
OUT=dict(scope='Specified mixed32 affine action; full stated homogeneous ordinary/T/U/oldM/newscalar correction space. No full affine exhaustion.',
 labels=labels,columns=cols,target=TARGET,rank=rank,solution_mask=sol,
 Z_joint_basis=JF,S3_basis=SF3,T_joint_basis=TJ,old_M_norm_kernel=OMK,new_scalar_norm_preimages=CBAS,
 output_shifts=dict(class_bits=SHIFT_CLASS,norm_bits=SHIFT_NORM))
if sol is not None:
 z=Z0;m=M0;uc=U0;tc=[zero]*6;uu=[zero]*4;oldmc=M0
 chk=0
 for i,(kind,j,k,a)in enumerate(labels):
  if sol>>i&1:
   chk^=cols[i]
   if kind=='Z':z=av(z,QDIR[i][2])
   elif kind=='M':m=fva(m,QDIR[i][1]);oldmc=fva(oldmc,fsm(a,OMK[j]))
   elif kind=='SCALAR':uc=fva(uc,QDIR[i][3])
   elif kind=='T':tc[j]=fva(tc[j],fsm(a,TJ[k]))
   else:uu[j]=fva(uu[j],fsm(a,SF3[k]))
 assert chk==TARGET
 q=(A0,m,z,uc,H0);nb=gm(B,q)
 assert gin(nb,S)==ph(S)
 assert gm(gi(nb),na(gi(nb)))==ONE
 assert av(av(znorm(z),tnorm(tc)),unorm(uu))==(zero,)*4
 print('Original704 law: corrected literal s-conjugacy and negative norm PASS.',flush=True)
 OUT.update(ordinary_correction=z,old_center_correction=oldmc,scalar_correction=uc,T_correction=tc,U_correction=uu,corrected_scalar_frame=nb,direct704='PASS')
else:
 # Exact dual annihilator, not a timeout or search failure.
 piv={}
 for col in cols:
  v=col
  while v:
   j=v.bit_length()-1
   if j in piv:v^=piv[j]
   else:piv[j]=v;break
 rem=TARGET
 for j in sorted(piv,reverse=True):
  if rem>>j&1:rem^=piv[j]
 j0=rem.bit_length()-1
 row=1<<j0
 for j in sorted(piv):
  if (row&piv[j]).bit_count()%2:row^=1<<j
 assert all((row&c).bit_count()%2==0 for c in cols)and(row&TARGET).bit_count()%2==1
 OUT.update(unsolved_annihilator=row,reduced_remainder=rem)
 print('Exact linear annihilator saved; scope is the specified correction family.',flush=True)
(HERE/'mixed_scalar_frame_system.json').write_text(json.dumps(OUT,indent=2)+'\n')
