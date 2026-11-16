"""Solve the full simultaneous UT4/scalar128 homogeneous frame system.

All576 ordinary joint-fixed,216 T joint-fixed,240 U S-fixed and87
old-center norm-zero binary directions are retained. The actual full20
witness is checked in the original law. The root scalar-cover verifier
must separately evaluate the resulting correction in its original law.
Existing witnesses are read-only.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json,itertools,numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
path=HERE/'check_A66_W0_twenty_sframe.py'
src=path.read_text().split('out=dict(scope=')[0]
D={'__file__':str(path),'__name__':'__A68_model__'}
with redirect_stdout(StringIO()):exec(compile(src,str(path),'exec'),D)
O=D['O'];P=D['P'];mul=O['fm'];pw=O['fp'];flin=O['flin'];fva=O['fva'];fsm=O['fsm']
zero=D['zero'];AZ=D['AZ'];TZ=D['TZ'];ZZ=D['ZZ'];pairs=D['pairs'];triples=D['triples'];pi=D['pindex']
root=json.loads((ROOT/'records/full_cubic_scalar_frame_lift.json').read_text())
ce=json.loads((ROOT/'work_CE/full_scalar_norm_formula_certificate.json').read_text())
raw=json.loads((ROOT/'work_CE/next_cup_cocycle_matrices.json').read_text())
J=json.loads((ROOT/'work_CE/A66_UT4_frame_surjection.json').read_text())['J']
def tup(x):return tuple(tup(v)for v in x)if isinstance(x,list)else x
M=np.array([[mul(a,b)for b in range(8)]for a in range(8)],dtype=np.uint8)
def mm(A,B):
 out=np.zeros((A.shape[0],B.shape[1]),dtype=np.uint8)
 for j in range(A.shape[1]):out^=M[A[:,j,None],B[j,None,:]]
 return out
def ker(A):
 A=A.copy();r=0;piv=[]
 for j in range(A.shape[1]):
  nz=np.flatnonzero(A[r:,j])
  if not len(nz):continue
  k=r+int(nz[0]);A[[r,k]]=A[[k,r]];A[r]=M[pw(int(A[r,j]),6),A[r]]
  for k in range(A.shape[0]):
   if k!=r and A[k,j]:A[k]^=M[A[k,j],A[r]]
  piv.append(j);r+=1
  if r==A.shape[0]:break
 out=[]
 for j in range(A.shape[1]):
  if j not in piv:
   v=np.zeros(A.shape[1],dtype=np.uint8);v[j]=1
   for i,k in enumerate(piv):v[k]=A[i,j]
   out.append(tuple(int(x)for x in v))
 return out
def mat(key,exp=1):return np.array([[pw(a,exp)for a in col]for col in raw[key]],dtype=np.uint8).T
I=np.eye(36,dtype=np.uint8)
S2,C2,B2=[mat(k)for k in('S2','C2','BETA2')];D2=mm(B2,C2)
TJF=ker(np.vstack((I^S2,I^D2)));assert len(TJF)==12
S3,C3,B3=[mat(k,5)for k in('S2','C2','BETA2')];D3=mm(B3,C3)
USF=ker(I^S3);assert len(USF)==20
ZJF=tup(root['correction_joint_fixed_weight_basis']);assert len(ZJF)==12
for v in ZJF:
 vv=np.array(v,dtype=np.uint8).reshape((36,1));assert not mm(I^S3,vv).any()and not mm(I^D3,vv).any()
BFRAME=D['BFRAME'];ba=D['ba'];va=D['va'];star=D['star'];h1a=D['h1a'];em=D['em'];ei=D['ei'];na=D['na'];ein=D['ein'];ONE=D['ONE'];SS=D['SS']
eff=h1a(O['HB'],va(ba(BFRAME[0]),D['CW']))
def tnorm(t):return tuple(fva(star(eff[i],t[pi[j,k]]),star(t[pi[i,j]],eff[k]))for i,j,k in triples)
def znorm(z):return tuple(tuple(__import__('functools').reduce(int.__xor__,(mul(J[i][j],z[j][w])for j in range(16)),0)for w in range(36))for i in range(4))
def unorm(u):return tuple(fva(v,flin([tuple(int(x)for x in D3[:,j])for j in range(36)],v))for v in u)
def pack(rows):return sum(int(v)<<(3*(36*i+j))for i,row in enumerate(rows)for j,v in enumerate(row))
cols=[];labels=[]
for lab,sc in zip(ce['all_Z_binary_labels'],ce['all_Z_norm_columns']):
 i,j,a=lab;z=[zero]*16;z[i]=fsm(a,ZJF[j])
 cols.append(pack(znorm(z))|(int(sc)<<432));labels.append(('Z',i,j,a))
for i in range(6):
 for j,v in enumerate(TJF):
  for a in(1,2,4):
   t=[zero]*6;t[i]=fsm(a,v)
   cols.append(pack(tnorm(t)));labels.append(('T',i,j,a))
for i in range(4):
 for j,v in enumerate(USF):
  for a in(1,2,4):
   u=[zero]*4;u[i]=fsm(a,v)
   cols.append(pack(unorm(u)));labels.append(('U',i,j,a))
oldlabels=[lab for lab in root['correction_binary_labels']if lab[0]=='old_center']
for lab,sc in zip(oldlabels,ce['old_M_norm_columns']):
 _,i,j,a=lab;cols.append(int(sc)<<432);labels.append(('M',i,j,a))
assert len(cols)==576+216+240+87
piv={}
for i,x in enumerate(cols):
 mask=1<<i
 while x:
  j=x.bit_length()-1
  if j not in piv:piv[j]=(x,mask);break
  x^=piv[j][0];mask^=piv[j][1]
target=int(ce['target'])<<432;rem=target;sol=0
for j in sorted(piv,reverse=True):
 if rem>>j&1:rem^=piv[j][0];sol^=piv[j][1]
print('Combined system:1119 binary variables, rank',len(piv),'; target solvable:',rem==0,flush=True)
T=[zero]*6;U=[zero]*4;Z=[zero]*16;mc=zero
if not rem:
 for i,(kind,j,k,a)in enumerate(labels):
  if sol>>i&1:
   if kind=='Z':Z[j]=fva(Z[j],fsm(a,ZJF[k]))
   elif kind=='T':T[j]=fva(T[j],fsm(a,TJF[k]))
   elif kind=='U':U[j]=fva(U[j],fsm(a,USF[k]))
   else:mc=fva(mc,fsm(a,tup(root['old_center_norm_kernel_basis'][j])))
 chk=0
 for i,c in enumerate(cols):
  if sol>>i&1:chk^=c
 assert chk==target
 oldq=(O['AA0'],mc,O['HN0'])
 q=((oldq,tuple(T)),tuple(U+Z))
 assert ein(q,SS)==SS
 bf=em(BFRAME,q)
 assert D['ph'](SS)==ein(bf,SS)
 norm=em(ei(bf),na(ei(bf)))
 assert norm==ONE,('full20 norm failed',norm)
 print('Literal full20 correction: source s conjugacy and complete lower/higher norm PASS',flush=True)
 # Check every k-basis T column in the original group law. Binary linearity
 # follows because the entire correction subgroup is abelian.
 for i in range(6):
  for j,v in enumerate(TJF):
   t=[zero]*6;t[i]=v
   qq=((O['ONE'],tuple(t)),ZZ)
   assert ein(qq,SS)==SS
   n=em(ei(em(BFRAME,qq)),na(ei(em(BFRAME,qq))))
   assert n[0]==P['ONE'] and not any(any(x)for x in n[1][4:])
   assert n[1][:4]==tnorm(t),(i,j,'T formula')
 print('All72 F8 T-column formulas match the original full20 group law: PASS',flush=True)
else:bf=None
out=dict(scope='Complete simultaneous system within the stated homogeneous Z/T/U/old-M correction families for the stored [6,0] affine datum',
 binary_variables=len(cols),rank=len(piv),labels=labels,columns=cols,target=target,remainder=rem,solution_mask=sol if not rem else None,
 Z_joint_basis=ZJF,T_joint_basis=TJF,U_Sfixed_basis=USF,
 ordinary_correction=Z,T_correction=T,U_correction=U,old_center_correction=mc,
 corrected_full20_BFRAME=bf,full20_direct_checks='PASS'if not rem else'not_applicable',
 scalar_status='Coefficient equations solved; root original-cover verification remains required')
(HERE/'A68_simultaneous_scalar_frame_solution.json').write_text(json.dumps(out,indent=2)+'\n')
