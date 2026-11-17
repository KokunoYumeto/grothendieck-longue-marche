#!/usr/bin/env python3
"""Exact incidence proof input for the one actual chi_sum index-two cover.
No finite quotient/period census or subgroup-depth sampling.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json',ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json']
F,S=[json.loads(p.read_text()) for p in paths]
def red(w):
 s=[]
 for x in w:
  if s and s[-1]==-x:s.pop()
  else:s.append(x)
 return s
def inv(w):return [-x for x in w[::-1]]
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,mp):return mul(*(mp[abs(x)] if x>0 else inv(mp[-x]) for x in w))
def chi(w):return sum(1 if x>0 else -1 for x in w if abs(x) in (1,2))
left=(1,2,3,4);right=(6,7,8,9);mat={};witness={}
for row in F['all40_node_factor_pairs']:
 a,b=row['first_factor'],row['second_factor'];i,j=abs(a['signed_core']),abs(b['signed_core'])
 if i in right:a,b=b,a;i,j=j,i
 assert i in left and j in right
 d=(chi(a['retained_head'])-chi(b['retained_head']))%2
 mat.setdefault((i,j),set()).add(d)
 witness.setdefault((i,j),{'side':row['side'],'name':row['name'],'sheet':row['sheet'],'first_head':a['retained_head'],'second_head':b['retained_head']})
assert len(mat)==16 and all(len(v)==1 for v in mat.values())
mat={k:next(iter(v)) for k,v in mat.items()}
expected=[[0,0,0,0],[0,0,1,1],[0,1,0,0],[0,1,0,0]]
assert [[mat[i,j] for j in right] for i in left]==expected
for name,op in F['all_four_signed_source_operators'].items():
 shifts={chi(x['retained_head']) for x in op['family_images'].values()}
 assert shifts=={{'m':0,'m_inverse':0,'v':-1,'v_inverse':1}[name]}
 for i,row in op['family_images'].items():assert row['signed_core']==int(i)
 for i,row in op['retained_images'].items():assert chi(row['retained_head'])==(0 if int(i)==11 else 1)
def family_ab(w):
 p=0;ans={}
 for x in w:
  i=abs(x);pn=p^(i in (5,10))
  if i in left+right:
   key=(p,i);ans[key]=ans.get(key,0)+(1 if x>0 else -1)
  p=pn
 assert p==0
 return {f'{p}:{i}':n for (p,i),n in sorted(ans.items()) if n}
raw=[x['fiber11'] for x in S['actual_six_source_normal_forms'][:4]]
a=mul(raw[0],inv(raw[3]),inv(raw[0]));b=mul(inv(a),inv(raw[0]),a)
d=mul(raw[1],raw[0],inv(raw[2]),inv(raw[0]),inv(raw[1]));e=inv(raw[1])
contacts=dict(zip(('A_s','B_s','D_s','E_s'),(a,b,d,e)))
ab={k:family_ab(w) for k,w in contacts.items()}
assert ab=={'A_s':{'0:1':1,'0:6':1},'B_s':{'0:2':1,'0:7':1},'D_s':{'0:3':1,'0:8':1},'E_s':{'1:4':1,'1:9':1}},ab
# Check the two analytically forced choices, and explicit exclusions of every opposite vertex.
choices=[[(0,1),(0,2),(0,3),(1,4)],[(0,6),(0,7),(0,8),(1,9)]]
def forbidden(a,b):
 p,i=a;q,j=b
 if i in right:i,j=j,i;p,q=q,p
 return i in left and j in right and (p-q)%2==mat[i,j]
exclusions=[]
for side,ch in enumerate(choices):
 opposite=right if side==0 else left
 ex={}
 for i in opposite:
  for p in (0,1):
   block=next((x for x in ch if forbidden(x,(p,i))),None)
   assert block is not None
   ex[f'{p}:{i}']={'forbidden_with':list(block)}
 exclusions.append(ex)
# The already actual one-family fillings kill both signed D defects, in both halves.
controls={}
for name in ('m','m_inverse'):
 mp={int(i):w for i,w in S['source_ordinary_actions'][name].items()}
 defect=mul(sub(d,mp),inv(d))
 for side,killed in [('kill_barred',right),('kill_unbarred',left)]:
  result=red(x for x in defect if abs(x) not in killed)
  assert not result
  controls[f'{name}/{side}']=result
out={'status':'PASS_STRUCTURAL_CORE_DELETION_BARRIER','input_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'left_colors':left,'right_colors':right,'complete_pair_parity_matrix':expected,'all16_seed_witnesses':{f'{i}:{j}':v for (i,j),v in witness.items()},'actual_contact_family_abelianizations':ab,'two_forced_choices':choices,'all_opposite_core_exclusions':exclusions,'known_one_family_D_defects':controls,'scope':'Exact proof input for core-deletion free quotients of this one index-two cover. No statement about other covers, quotients with additional relations, or arbitrary Nielsen changes.'}
(ROOT/'work_A/core_deletion_barrier27.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS complete40 seeds give16 exact pair parities and all4 signed invariants.')
print('PASS literal4 contact family-abelian vectors,2 forced choices and16 opposite-core exclusions.')
print('PASS both signed D defects vanish in each of the two known one-family fillings.')
