"""Exact ordinary16-cup s norms at the D-fixed weight pairs, W_free=0.
The canonical-c cocycle, including its actual inner part, is retained.
This is a necessary local gate before the old global central equations.
"""
from pathlib import Path
import json,itertools
HERE=Path(__file__).resolve().parent
M=json.loads((HERE.parent/'next_cup_cocycle_matrices.json').read_text())
ad=json.loads((HERE.parent/'Q6_integral_affine_data.json').read_text())
old=json.loads((HERE.parents[1]/'work_A/A66_cubic_twenty_result.json').read_text())
vp=json.loads((HERE.parent/'Q6_new_center_variation.json').read_text())['opposite_weight_pairs']
partner={}
for i,j in vp:partner[i]=j;partner[j]=i
def mul(a,b):
 out=0
 while b:
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out
def pw(a,n):
 out=1
 for _ in range(n):out=mul(out,a)
 return out
def add(a,b):return tuple(x^y for x,y in zip(a,b))
def va(a,b):return tuple(add(x,y)for x,y in zip(a,b))
def apply(cs,v):
 out=[0]*36
 for a,col in zip(v,cs):
  if a:
   for i,b in enumerate(col):out[i]^=mul(a,b)
 return tuple(out)
def cols1(name):return [tuple(pw(x,4)for x in c)for c in M[name]]
B=cols1('BETA2');C=cols1('C2');S=cols1('S2')
B3=[tuple(pw(x,3)for x in c)for c in B]
C3=[tuple(pw(x,3)for x in c)for c in C]
def rowsop(cs,a):return tuple(apply(cs,v)for v in a)
def red(a):return(a&1)|(((a>>2)&1)<<1)|(((a>>4)&1)<<2)
wc=tuple(tuple(red(x)for x in r)for r in ad['new_c_inner_free_O'])
L=[r[:4]for r in old['canonical_c_corrections'][4:]]
VC=tuple(tuple(r[8:])for r in old['canonical_c_corrections'][4:])
assert all(not any(r[4:8])for r in old['canonical_c_corrections'][4:])
zero=(0,)*36;AZ=(zero,)*4;ZZ=(zero,)*16
def cup(a,b):return tuple(tuple(mul(pw(x,2),y)for x,y in zip(a[r],b[i]))for r in range(4)for i in range(4))
def gm(g,h):
 a,z,e=g;b,w,f=h
 if e:b,w=rowsop(B,b),rowsop(B3,w)
 return(va(a,b),va(va(z,w),cup(a,b)),e^f)
ONE=(AZ,ZZ,0)
def gi(g):
 a,z,e=g;out=(a,va(z,cup(a,a)),e)
 if e:out=(rowsop(B,out[0]),rowsop(B3,out[1]),e)
 assert gm(g,out)==gm(out,g)==ONE
 return out
def inner(g,h):return gm(gm(g,h),gi(g))
def j3(v):return tuple(pw(v[partner[i]],4)for i in range(36))
def lc(a):
 ja=[j3(v)for v in a];out=[]
 for row in L:
  v=zero
  for c,x in zip(row,ja):v=add(v,tuple(mul(c,y)for y in x))
  out.append(v)
 return tuple(out)
def ca(g):
 a,z,e=g;g=inner((wc,ZZ,0),(rowsop(C,a),rowsop(C3,z),e))
 corr=lc(g[0])
 if e:corr=va(corr,va(VC,rowsop(B3,VC)))
 return(g[0],va(g[1],corr),e)
B0=(wc,ZZ,1)
assert rowsop(C,wc)==wc and rowsop(S,wc)==wc
assert ca(ca(B0))==B0
baseline=gm(gi(B0),ca(gi(B0)))
assert baseline[0]==AZ and baseline[2]==0
K=baseline[1]
print('Canonical c including all actual cocycle terms; W0 baseline norm computed: PASS')

def lapply(v):
 return tuple(sumxor(mul(a,b)for a,b in zip(row,v))for row in L)
def sumxor(xs):
 out=0
 for a in xs:out^=a
 return out
def outer(v):return tuple(mul(pw(v[r],2),v[i])for r in range(4)for i in range(4))
def solve(v):
 rows=[list(row)+[a]for row,a in zip(L,v)];piv=[];j=0
 for i in range(4):
  k=next((k for k in range(j,16)if rows[k][i]),None)
  assert k is not None
  rows[j],rows[k]=rows[k],rows[j];c=pw(rows[j][i],6);rows[j]=[mul(c,a)for a in rows[j]]
  for k in range(16):
   if k!=j and rows[k][i]:
    c=rows[k][i];rows[k]=[a^mul(c,b)for a,b in zip(rows[k],rows[j])]
  piv.append(i);j+=1
 if any(not any(row[:4])and row[4]for row in rows):return None
 ans=tuple(rows[i][4]for i in range(4));assert lapply(ans)==v;return ans

sp=[next(i for i,v in enumerate(c)if v)for c in S]
bp=[next(i for i,v in enumerate(c)if v)for c in B]
cp=[next(i for i,v in enumerate(c)if v)for c in C]
records=[]
for lam in(8,20):
 bar=partner[lam];kl=tuple(v[lam]for v in K);kb=tuple(v[bar]for v in K)
 assert bp[cp[lam]]==lam and bp[cp[bar]]==bar
 allowed=[]
 for u in itertools.product(range(8),repeat=4):
  v4=solve(add(kl,outer(u)))
  if v4 is None:continue
  v=tuple(pw(a,2)for a in v4)
  if add(add(kb,outer(v)),lapply(tuple(pw(a,4)for a in u)))!=(0,)*16:continue
  allowed.append((u,v))
 print('Weight pair',lam,bar,'allowed right-correction pairs:',len(allowed),flush=True)
 # Each listed candidate is checked in the full original ordinary law,
 # with all S mates present and the actual canonical-c inner coefficients.
 for u,v in allowed:
  aa=[[0]*36 for _ in range(4)]
  for idx,vals in((lam,u),(bar,v)):
   for row,a in enumerate(vals):
    aa[row][idx]=a;aa[row][sp[idx]]=mul(S[idx][sp[idx]],a)
  aa=tuple(map(tuple,aa));assert rowsop(S,aa)==aa
  assert rowsop(B,rowsop(C,aa))==aa
  Q=(aa,ZZ,0);newB=gm(B0,Q);norm=gm(gi(newB),ca(gi(newB)))
  assert norm[0]==AZ and norm[2]==0
  assert all(row[lam]==row[bar]==row[sp[lam]]==row[sp[bar]]==0 for row in norm[1])
 records.append(dict(lambda_weight=lam,opposite_weight=bar,S_mates=[sp[lam],sp[bar]],
                     beta_images=[bp[lam],bp[bar]],baseline_lambda=kl,baseline_opposite=kb,
                     right_corrections=allowed))
out=dict(scope='Necessary W_free=0 ordinary s-normalizer local equations; old global central norm remains separate',
         L_c=L,records=records,conversion='Right correction u; affine t=(p-wc)=beta*u, with the recorded beta weight permutation and its scalar weights',
         beta_columns=B,checks='Every listed candidate verified in actual ordinary group law')
(HERE.parent/'A66_W0_local_frame_pairs.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact enumeration of both opposite-weight pairs: PASS')
