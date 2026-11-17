"""Lift the actual integral free-center half through the old norm kernel."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
d=json.loads((ROOT/'records/full_cubic_scalar_frame_lift.json').read_text())
e=json.loads((ROOT/'work_CE/full_scalar_integral_frame_gate.json').read_text())
def mul(a,b):
 r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return r
def pw(a,n):
 r=1
 for _ in range(n):r=mul(r,a)
 return r
def lin(cols,v):
 out=[0]*len(cols[0])
 for c,a in zip(cols,v):
  for i,x in enumerate(c):out[i]^=mul(a,x)
 return out
def solve(cols,t):
 bas={}
 for i,c in enumerate(cols):
  x=list(c);q=[int(j==i)for j in range(len(cols))]
  for j in sorted(bas):
   if x[j]:
    b,v=bas[j];a=x[j]
    x=[z^mul(a,w)for z,w in zip(x,b)];q=[z^mul(a,w)for z,w in zip(q,v)]
  j=next((i for i,z in enumerate(x)if z),None)
  if j is not None:
   a=pw(x[j],6);bas[j]=([mul(a,z)for z in x],[mul(a,z)for z in q])
 x=list(t);q=[0]*len(cols)
 for j in sorted(bas):
  if x[j]:
   b,v=bas[j];a=x[j]
   x=[z^mul(a,w)for z,w in zip(x,b)];q=[z^mul(a,w)for z,w in zip(q,v)]
 return len(bas),(None if any(x) else q)
cols=[lin(d['old_center_projection_columns'],v)for v in d['old_center_norm_kernel_basis']]
r,s=solve(cols,e['initial_half_center']);assert r==10 and s is not None
v=lin(d['old_center_norm_kernel_basis'],s)
assert lin(d['old_center_projection_columns'],v)==e['initial_half_center']
print('Old center norm kernel -> full free center10 has rank10: PASS')
print('Required integral free half has exact old norm-zero lift:',v)
(HERE/'A69_integral_half_old_center_lift.json').write_text(json.dumps(dict(
 scope='Exact old-center norm-zero lift of the required free integral half; norm-kernel basis is from the original-law root certificate',
 projection_rank=r,projection_columns=cols,basis_coefficients=s,
 old_center_correction=v,free_half_center=e['initial_half_center']),indent=2)+'\n')
