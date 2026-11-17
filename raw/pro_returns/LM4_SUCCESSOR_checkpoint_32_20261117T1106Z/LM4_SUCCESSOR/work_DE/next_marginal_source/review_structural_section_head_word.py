#!/usr/bin/env python3
"""Independent bounded review of the actual four-letter section operator;no Fox expansion."""
from pathlib import Path
import json,hashlib,time
R=Path(__file__).resolve().parents[2];H=Path(__file__).resolve().parent
p=R/'work_A/structural_section_head_word19.json';a=json.loads(p.read_text())
d=json.loads((R/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json').read_text())
s=json.loads((R/'work_CE/next_symmetric_nodes/symmetric_full_source_data.json').read_text())
def red(w):
 z=[]
 for k in w:
  if z and z[-1]==-k:z.pop()
  else:z.append(k)
 return tuple(z)
def iv(w):return tuple(-x for x in w[::-1])
def mp(x):return {int(k):tuple(v) for k,v in x.items()}
def ev(w,f):return red(y for k in w for y in(f[abs(k)] if k>0 else iv(f[abs(k)])))
ops=[]
for k in (6,2,-6,-2):
 row=d['old_actions'][abs(k)-1];ops.append(mp(row['geometric_push_paired' if k>0 else 'based_pullback_paired']))
def far(w):
 for f in ops:w=ev(w,f)
 return w
far_images={i:far((i,)) for i in range(1,22)};assert far_images==mp(a['actual_far_push_F21'])
old=d['retained_paired_indices'];oi={x:i+1 for i,x in enumerate(old)}
def fill(w):return red((1 if k>0 else -1)*oi[abs(k)] for k in w if abs(k) in oi)
for j,x in enumerate(old,1):assert fill(far_images[x])==(j,)
def peel(w,i):
 h=[]
 while len(w)>1 and w[0]==-w[-1]:h.append(w[0]);w=w[1:-1]
 assert w==(i,);return tuple(h)
for x in a['all_eight_literal_peripheral_head_checks']:
 i=x['slot'];ha=peel(far_images[i],i);hb=peel(far_images[i+10],i+10)
 assert list(ha)==x['A_conjugator_F21'] and list(hb)==x['B_conjugator_F21']
 assert list(fill(ha))==x['A_head'] and list(fill(hb))==x['B_head']
assert fill(peel(far_images[6],6))==fill(peel(far_images[16],16))==()
sa=next(x for x in s['old_source_generators'] if x['name']=='old_5')
so=next(x for x in s['old_source_generators'] if x['name']=='other_sheet_old_5')
assert red(tuple(sa['far_base_word'])+iv(tuple(so['far_base_word'])))==(6,2,-6,-2)
pa=mp(sa['source_push_F21']);po=mp(so['source_pullback_F21']);F=mp(d['paired_involution'])
h=tuple(a['source_correction_h_F21']);assert fill(h)==()
for i in range(1,22):
 w=ev(pa[i],po);assert list(w)==a['actual_source_push_F21'][str(i)]
 assert w==red(iv(h)+far_images[i]+h)
 assert ev(w,F)==ev(ev(F[i],pa),po)
print('PASS all21 far/source operator identities from authoritative six old actions.')
print('PASS all16 literal filled heads;selected A6=B6=0 and retainedphi=id.')
print('PASS actual two-generator B0 source word and2416-letter retained-zero correction;all21 F commutations.')
out={'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'far_operator_generators_checked':21,'source_operator_generators_checked':21,'peripheral_head_checks':16,'source_correction_length':len(h),'scope':'actual based operator and source word only;no chain or overlap inference'}
(H/'structural_section_head_word_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
