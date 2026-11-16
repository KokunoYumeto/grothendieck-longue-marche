"""Closed full128 scalar norm formula; comparison with original-law columns.

Also computes the generous image allowing ALL ordinary joint-fixed
corrections, before imposing their UT4 compensation constraints.
"""
from pathlib import Path
import json,itertools
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
p=json.loads((ROOT/'records/full_cubic_scalar_frame_lift.json').read_text())
ad=json.loads((HERE.parent/'Q6_integral_affine_data.json').read_text())
raw=json.loads((HERE.parent/'next_cup_cocycle_matrices.json').read_text())
ordinary=json.loads((ROOT/'work_A/A66_W0_local_ordinary_result.json').read_text())
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
def apply(cols,v):return [xor(mul(v[j],cols[j][i])for j in range(len(v)))for i in range(len(cols[0]))]
B=[[power(x,4)for x in col]for col in raw['BETA2']]
def red(x):return(x&1)|(((x>>2)&1)<<1)|(((x>>4)&1)<<2)
wc=[[red(x)for x in row]for row in ad['new_c_inner_free_O']]
frame_a=p['full20_frame_projection'][0]
t=[[x^y for x,y in zip(a,b)]for a,b in zip(frame_a,wc)]
avec=[apply(B,row)for row in t]
triples=list(itertools.product(range(4),repeat=3));idx={v:i for i,v in enumerate(triples)}
def sigma(v):return [power(v[idx[k,i,j]],2)for i,j,k in triples]
def stem(v):
 a=sigma(v);b=sigma(a);return[x^y for x,y in zip(a,b)]
def znorm(z):
 return stem([xor(mul(z[4*r+i][l],power(avec[j][l],4))^
                  mul(power(avec[r][l],2),power(z[4*i+j][l],4))
                  for l in range(36))for r,i,j in triples])
mpairs=list(itertools.combinations_with_replacement(range(4),2));mi={v:i for i,v in enumerate(mpairs)}
L=[row[:4]for row in ordinary['canonical_c_corrections']]
def mnorm(m):
 Q=[[m[mi[tuple(sorted((i,j)))]]if i!=j else 0 for j in range(4)]for i in range(4)]
 return stem([xor(mul(L[4*r+i][s],power(Q[j][s],4))^
                  mul(power(L[4*i+j][s],4),power(Q[s][r],2))
                  for s in range(4))for r,i,j in triples])
def pack(v):return sum(x<<(3*i)for i,x in enumerate(v))
oldm=p['old_center_projection_columns'];oldcols=[]
for label,want in zip(p['correction_binary_labels'],p['correction_norm_columns']):
 kind,ii,jj,scalar=label
 if kind=='ordinary':
  mult=p['correction_shear_kernel_basis'][ii]
  v=p['correction_joint_fixed_weight_basis'][jj]
  z=[[mul(mul(scalar,c),x)for x in v]for c in mult]
  got=pack(znorm(z))
 else:
  v=[mul(scalar,x)for x in p['old_center_norm_kernel_basis'][ii]]
  got=pack(mnorm(apply(oldm,v)));oldcols.append(got)
 assert got==want,(label,got,want)
print('All519 full128 original-law norm columns match closed Z and old-M formulas: PASS')
def pivots(cols):
 piv={}
 for x in cols:
  while x:
   j=x.bit_length()-1
   if j not in piv:piv[j]=x;break
   x^=piv[j]
 return piv
def remainder(piv,x):
 for j in sorted(piv,reverse=True):
  if x>>j&1:x^=piv[j]
 return x
allcols=[];labels=[]
for i in range(16):
 for j,v in enumerate(p['correction_joint_fixed_weight_basis']):
  for scalar in(1,2,4):
   z=[[0]*36 for _ in range(16)];z[i]=[mul(scalar,x)for x in v]
   allcols.append(pack(znorm(z)));labels.append((i,j,scalar))
P=pivots(allcols+oldcols);target=pack(p['scalar_frame_square']);rem=remainder(P,target)
print('All ordinary joint-fixed directions plus old-center kernel: rank',len(P),'; target inimage:',rem==0)
out=dict(scope='Fixed-affine scalar norm; all-Z image is a generous relaxation of the UT4 constraints, not an exhaustion of all affine data',
 compared_original_columns=519,all_Z_binary_labels=labels,all_Z_norm_columns=allcols,
 old_M_norm_columns=oldcols,all_Z_plus_old_M_rank=len(P),
 target=target,target_remainder=rem,target_in_generous_image=rem==0,
 affine_coefficients_at8_11=[[row[8],row[11]]for row in avec])
if rem==0:
 chosen={}
 for i,x in enumerate(allcols+oldcols):
  mask=1<<i
  while x:
   j=x.bit_length()-1
   if j not in chosen:chosen[j]=(x,mask);break
   x^=chosen[j][0];mask^=chosen[j][1]
 solution=0;x=target
 for j in sorted(chosen,reverse=True):
  if x>>j&1:x^=chosen[j][0];solution^=chosen[j][1]
 assert x==0
 z=[[0]*36 for _ in range(16)];m=[0]*10
 for i,(ii,jj,scalar)in enumerate(labels):
  if solution>>i&1:
   for k,v in enumerate(p['correction_joint_fixed_weight_basis'][jj]):z[ii][k]^=mul(scalar,v)
 oldlabels=[lab for lab in p['correction_binary_labels']if lab[0]=='old_center']
 for k,(_,ii,_,scalar)in enumerate(oldlabels):
  if solution>>(len(allcols)+k)&1:
   v=[mul(scalar,a)for a in p['old_center_norm_kernel_basis'][ii]]
   m=[a^b for a,b in zip(m,apply(oldm,v))]
 got=pack([a^b for a,b in zip(znorm(z),mnorm(m))]);assert got==target
 J=json.loads((HERE.parent/'A66_UT4_frame_surjection.json').read_text())['J']
 ut4=[[xor(mul(J[i][j],z[j][k])for j in range(16))for k in range(36)]for i in range(4)]
 out.update(generous_solution_mask=solution,generous_ordinary_correction=z,
            generous_old_center_correction=m,remaining_UT4_norm=ut4)
(HERE.parent/'full_scalar_norm_formula_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
