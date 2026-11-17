#!/usr/bin/env python3
from pathlib import Path
from collections import defaultdict
import json,hashlib
R=Path(__file__).resolve().parents[2]
P=R/'work_CE/next_symmetric_nodes'
D=json.loads((P/'annular_two_operator25.json').read_text())
K=json.loads((P/'family_kernel_schreier25.json').read_text())
C=json.loads((P/'source_abelian_levels25.json').read_text())
def reduce(w):
 s=[]
 for z in w:
  if s and z==-s[-1]:s.pop()
  else:s.append(z)
 return tuple(s)
def chi(w):return sum((z==3)-(z==-3) for z in w)
family={1,2,3,4,6,7,8,9};retained={5:1,10:2,11:3}
for op in K['all_four_signed_source_operators'].values():
 for rec in op['family_images'].values():assert chi(rec['retained_head'])==0
 for key,rec in op['retained_images'].items():assert chi(rec['retained_head'])==int(int(key)==11)
for row,certificate in zip(D['actual_six_source_normal_forms'][:4],C['actual_four_contact_vectors']):
 t=();vec=defaultdict(int)
 for z in row['fiber11']:
  if abs(z) in family:vec[t,abs(z)]+=1 if z>0 else -1
  else:t=reduce(t+(retained[abs(z)]*(1 if z>0 else -1),))
 assert not t
 vec={k:v for k,v in vec.items() if v}
 expected={(tuple(x['head']),x['color']):x['coefficient'] for x in certificate['complete_vector']}
 assert vec==expected and len(vec)==2
 for (head,label),value in vec.items():assert value==-1 and chi(head)==int(label>=6)
print('PASS independent all32 head/all12 retained checks and exact four full source vectors; levels0/1 and coefficients-1 asserted.')
