"""Exhaustive ordinary16-cup negative-square test on the actual19-bit W space.

The source action correction is chosen linearly from the four cusp classes
and inner36 space. All binary-s classes are zero. This computes a quadratic
map in the19 binary W coordinates; direct random evaluations independently
check the polarization formula before exhaustive enumeration.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json,itertools,random,time
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
start=time.time()
with redirect_stdout(StringIO()):
 O=runpy.run_path(str(ROOT/'work_A/check_Q6_central_cover.py'))
data=json.loads((ROOT/'records/A66_cusp_action_space.json').read_text())
ad=json.loads((HERE.parent/'Q6_integral_affine_data.json').read_text())
cc=json.loads((ROOT/'work_A/A66_cubic_twenty_result.json').read_text())
fm,fp=O['fm'],O['fp']
MUL=np.array([[fm(a,b)for b in range(8)]for a in range(8)],dtype=np.uint8)
POW=np.array([[fp(a,n)for a in range(8)]for n in range(8)],dtype=np.uint8)
partner=np.array([O['partner'][i]for i in range(36)])
AZ=np.zeros((4,36),dtype=np.uint8);ZZ=np.zeros((16,36),dtype=np.uint8)
head0=O['HN0'];HS=O['HS'];HR=O['HR'];HT=O['HT']
HC={};HI={};HM={}
def mono(h,power=1):
 key=(h,power)
 if key not in HC:
  cols=O['hcols'](h);perm=[];sc=[]
  for col in cols:
   i=next(i for i,v in enumerate(col)if v);perm.append(i);sc.append(fp(col[i],power))
  HC[key]=(np.array(perm),np.array(sc,dtype=np.uint8))
 return HC[key]
def act(h,a,power=1):
 perm,sc=mono(h,power);out=np.empty_like(a);out[:,perm]=MUL[a,sc]
 return out
cv=np.array(O['CV'],dtype=np.uint8)
cp=np.array([np.flatnonzero(row)[0]for row in cv])
cs=np.array([row[i]for row,i in zip(cv,cp)],dtype=np.uint8)
def cact(a,power=1):
 out=np.empty_like(a);out[:,cp]=MUL[a,POW[power,cs]];return out
def hmul(a,b):
 if (a,b)not in HM:HM[a,b]=O['hmul'](a,b)
 return HM[a,b]
def hinv(h):
 if h not in HI:HI[h]=O['hinv'](h)
 return HI[h]
def cup(a,b):return MUL[POW[2,a][:,None,:],b[None,:,:]].reshape(16,36)
def gm(g,h):
 a,z,q=g;b,w,r=h;hb=act(q,b)
 return(a^hb,z^act(q,w,3)^cup(a,hb),hmul(q,r))
def gi(g):
 a,z,h=g;hh=hinv(h)
 return(act(hh,a),act(hh,z^cup(a,a),3),hh)
def inner(g,h):return gm(gm(g,h),gi(g))
def same(g,h):return g[2]==h[2]and np.array_equal(g[0],h[0])and np.array_equal(g[1],h[1])
ONE=(AZ,ZZ,head0)
E=ad['new_basis_columns_in_old_EB'];ag=ad['cochain_coboundary_in_V8']
def newa(g):
 old=O['mix'](E,g[0]);h=g[2]
 return np.array([O['fva'](O['fva'](row,x),O['flin'](O['hcols'](h),x))for row,x in zip(old,ag)],dtype=np.uint8)
dr=newa(O['RR'])[:4]
SS=(AZ,ZZ,HS)
RR=inner((act(HR,dr),ZZ,head0),(AZ,ZZ,HR))
TT=gm(SS,RR)
assert np.array_equal(RR[0],dr)
assert same(gm(SS,SS),ONE)and same(gm(gm(RR,RR),RR),ONE)
wc=np.array([[(x&1)|(((x>>2)&1)<<1)|(((x>>4)&1)<<2)for x in row]for row in ad['new_c_inner_free_O']],dtype=np.uint8)
WC=(wc,ZZ,head0)
CC=np.array([row[:4]+row[8:]for row in cc['canonical_c_corrections'][4:]],dtype=np.uint8)
assert all(not any(row[4:8])for row in cc['canonical_c_corrections'][4:])
def j3(a):return POW[4,a[:,partner]]
def eta(g,co):
 a,z,h=g;ja=j3(a);out=co[:,4:]^act(h,co[:,4:],3)
 for i in range(4):out=out^MUL[co[:,i,None],ja[i,None,:]]
 return out
def ca(g):
 a,z,h=g;n=inner(WC,(cact(a),cact(z,3),O['hc'](h)))
 return(n[0],n[1]^eta(n,CC),n[2])
assert same(ca(SS),SS)and same(ca(RR),gm(gm(SS,gi(RR)),SS))
assert same(ca(TT),gi(TT))and same(ca(ca(RR)),RR)
def right_inverse(A):
 A=A.copy();n,m=A.shape;B=np.eye(n,dtype=np.uint8);piv=[];j=0
 for col in range(m):
  ks=np.flatnonzero(A[j:,col])
  if not len(ks):continue
  k=j+int(ks[0]);A[[j,k]]=A[[k,j]];B[[j,k]]=B[[k,j]]
  inv=fp(int(A[j,col]),6);A[j]=MUL[inv,A[j]];B[j]=MUL[inv,B[j]]
  for k in range(n):
   if k!=j and A[k,col]:
    c=A[k,col];A[k]^=MUL[c,A[j]];B[k]^=MUL[c,B[j]]
  piv.append(col);j+=1
  if j==n:break
 assert j==n
 R=np.zeros((m,n),dtype=np.uint8)
 for i,col in enumerate(piv):R[col]=B[i]
 return R
CB=np.eye(40,dtype=np.uint8)
EC=eta(TT,CB).T
RI=right_inverse(EC)
def solve_cusp(target):
 out=np.zeros((16,40),dtype=np.uint8)
 for i in range(36):out^=MUL[target[:,i,None],RI[:,i][None,:]]
 return out
def pack(a):return int.from_bytes(np.asarray(a,dtype=np.uint8).tobytes(),'little')
def unpack(mask):
 return np.array([(mask>>(3*i))&7 for i in range(144)],dtype=np.uint8).reshape(4,36)
WB=[unpack(x)for x in data['cusp_action_basis']]
for W in WB:
 assert np.array_equal(act(HT,W),W)and np.array_equal(cact(W),W)
def evaluate(W):
 WW=(W,ZZ,head0);pT=inner(WW,TT)
 assert np.array_equal(pT[0],TT[0])and pT[2]==TT[2]
 co=solve_cusp(pT[1]^TT[1])
 def ph(g):
  n=inner(WW,g);return(n[0],n[1]^eta(g,co),n[2])
 def b(g):return ph(ca(g))
 assert same(ph(TT),TT)
 sd,rd=b(b(SS)),b(b(RR))
 assert np.array_equal(sd[0],SS[0])and sd[2]==SS[2]
 assert np.array_equal(rd[0],RR[0])and rd[2]==RR[2]
 return pack(np.concatenate((sd[1]^SS[1],rd[1]^RR[1]),axis=1))
const=evaluate(AZ);assert const==0
lin=[evaluate(W)^const for W in WB]
cross={}
for i in range(19):
 for j in range(i):cross[j,i]=evaluate(WB[i]^WB[j])^lin[i]^lin[j]^const
print('Actual ordinary source/canonical-c checks; cusp40->36 rank36: PASS',flush=True)
print('Quadratic coefficients extracted:',len(lin),len(cross),'seconds',round(time.time()-start,2),flush=True)
def quadratic(mask):
 out=const;ix=[i for i in range(19)if mask>>i&1]
 for i in ix:out^=lin[i]
 for j,i in itertools.combinations(ix,2):out^=cross[j,i]
 return out
rng=random.Random(66019)
for _ in range(64):
 mask=rng.randrange(1<<19);W=AZ.copy()
 for i in range(19):
  if mask>>i&1:W^=WB[i]
 assert evaluate(W)==quadratic(mask)
print('Independent64 full original-law polarization checks: PASS',flush=True)
zeros=[];value=const;prev=0
for n in range(1<<19):
 mask=n^(n>>1)
 if n:
  bit=(mask^prev).bit_length()-1;value^=lin[bit]
  other=prev&~(1<<bit)
  while other:
   low=other&-other;j=low.bit_length()-1;other^=low
   value^=cross[min(j,bit),max(j,bit)]
 if value==0:zeros.append(mask)
 prev=mask
zeros.sort()
print('All524288 W values checked; zero count:',len(zeros),flush=True)
out=dict(scope='Complete ordinary16 negative-action-square zero set on the certified19-dimensional W quotient; frame and scalar gates remain separate',
 source='records/A66_cusp_action_space.json',variables=19,constant=const,
 linear=lin,quadratic=[dict(i=i,j=j,value=v)for(i,j),v in cross.items()],
 zero_masks=zeros,zero_count=len(zeros),
 checks='Actual source/canonical c/cusp identities;64 direct-law quadratic comparisons; all2^19 inputs enumerated')
(HERE.parent/'A66_ordinary_action_zero_set.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact complete ordinary action-square gate: PASS; seconds',round(time.time()-start,2))
