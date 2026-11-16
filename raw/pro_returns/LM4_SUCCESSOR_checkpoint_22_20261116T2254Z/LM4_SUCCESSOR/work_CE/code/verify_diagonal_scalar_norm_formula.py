"""Independent closed formula for the actual432 diagonal-scalar norm columns."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
p=json.loads((ROOT/'records/diagonal_scalar_frame_lift.json').read_text())
ad=json.loads((HERE.parent/'Q6_integral_affine_data.json').read_text())
raw=json.loads((HERE.parent/'next_cup_cocycle_matrices.json').read_text())
def mul(a,b):
 r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return r
def power(a,n):
 r=1
 for _ in range(n):r=mul(r,a)
 return r
def xor(xs):
 r=0
 for x in xs:r^=x
 return r
def proj(a):return power(a,2)^power(a,4)
def apply(cols,v):
 return [xor(mul(v[j],cols[j][i])for j in range(36))for i in range(36)]
B=[[power(x,4)for x in col]for col in raw['BETA2']]
S=[[power(x,5)for x in col]for col in raw['S2']]
C=[[power(x,5)for x in col]for col in raw['C2']]
B3=[[power(x,3)for x in col]for col in B]
def red(x):return(x&1)|(((x>>2)&1)<<1)|(((x>>4)&1)<<2)
wc=[[red(x)for x in row]for row in ad['new_c_inner_free_O']]
frame_a=p['full20_frame_projection'][0]
t=[[x^y for x,y in zip(a,b)]for a,b in zip(frame_a,wc)]
avec=[apply(B,row)for row in t]
def norm(z):
 return [proj(xor(mul(z[5*i][j],power(avec[i][j],4))^
                  mul(power(avec[i][j],2),power(z[5*i][j],4))
                  for j in range(36)))for i in range(4)]
def pack(v):return sum(x<<(3*i)for i,x in enumerate(v))
for label,want in zip(p['correction_binary_labels'],p['correction_norm_columns']):
 ii,jj,scalar=label
 mult=p['correction_shear_kernel_basis'][ii]
 v=p['correction_joint_fixed_weight_basis'][jj]
 z=[[mul(mul(scalar,c),x)for x in v]for c in mult]
 assert pack(norm(z))==want
print('All432 actual original-law norm columns equal the derived t-pairing formula: PASS')
def rank(cols):
 piv={}
 for x in cols:
  while x:
   j=x.bit_length()-1
   if j not in piv:piv[j]=x;break
   x^=piv[j]
 return len(piv)
small=[];labels=[]
for i in range(4):
 for v in (1,2,4):
  z=[[0]*36 for _ in range(16)];z[5*i][8]=v
  assert apply(S,z[5*i])==z[5*i]
  assert apply(B3,apply(C,z[5*i]))==z[5*i]
  small.append(pack(norm(z)));labels.append((i,8,v))
assert rank(small)==8
assert all(row[8]for row in avec)
print('Four diagonal ordinary coordinates supported atweight8 already give scalar rank8: PASS')
print('Affine t coefficient atweight8:',[row[8]for row in avec])
out=dict(scope='Actual eight-dimensional selected scalar norm; no claim about complete scalar kernel',
 formula='pi sum[Z_ii*(beta*t_i)^4+(beta*t_i)^2*Z_ii^4]',
 all432_columns_match=True,diagonal_weight8_labels=labels,
 diagonal_weight8_norm_columns=small,diagonal_weight8_rank=8,
 affine_coefficient_at_weight8=[row[8]for row in avec])
(HERE.parent/'diagonal_scalar_norm_formula_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
