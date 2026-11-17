#!/usr/bin/env python3
"""Complete actual40-node half filling and exact six-source detector limitation."""
from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[2]
paths=[R/'work_CE/next_symmetric_nodes/annular_two_operator25.json',R/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json']
D,K=[json.loads(p.read_text()) for p in paths]
def red(w):
 s=[]
 for z in w:
  if s and s[-1]==-z:s.pop()
  else:s.append(z)
 return tuple(s)
def inv(w):return tuple(-z for z in reversed(w))
def mul(*words):return red(z for w in words for z in w)
def sub(w,A):return red(z for j in w for z in (A[abs(j)] if j>0 else inv(A[-j])))
def comm(a,b):return mul(a,b,inv(a),inv(b))
keep={1:1,2:2,3:3,4:4,5:5,10:6,11:7};bar={6,7,8,9}
def fill(w):return red(keep[abs(j)]*(1 if j>0 else -1) for j in w if abs(j) in keep)
pairs=[]
for r in K['all40_node_factor_pairs']:
 a,b=r['first_factor'],r['second_factor'];i,j=abs(a['signed_core']),abs(b['signed_core'])
 assert (i<5)!=(j<5)
 A,B=fill(a['word_F11']),fill(b['word_F11'])
 assert (not A or not B) and not comm(A,B)
 pairs.append({'side':r['side'],'name':r['name'],'sheet':r['sheet'],'colors':[i,j],'filled_factors':[A,B]})
actions={}
for name,A in D['source_ordinary_actions'].items():
 A={int(i):tuple(w) for i,w in A.items()}
 assert all(not fill(A[i]) for i in bar)
 actions[name]={j:fill(A[i]) for i,j in keep.items()}
for op in ['m','v']:
 for i in range(1,8):
  assert sub(actions[op][i],actions[op+'_inverse'])==(i,)
  assert sub(actions[op+'_inverse'][i],actions[op])==(i,)
sources=[tuple(r['fiber11']) for r in D['actual_six_source_normal_forms'][:4]]
new={i+1:fill(w) for i,w in enumerate(sources)};new.update({5:(5,),6:(6,),7:(7,)})
a=(1,-4,-1)
b=mul(inv(a),(-1,),a)
d=(2,1,-3,-1,-2)
e=mul(inv(d),(-5,-2,5),d)
inverse={1:a,2:b,3:d,4:e,5:(5,),6:(6,),7:(7,)}
for i in range(1,8):
 assert sub(new[i],inverse)==(i,)
 assert sub(inverse[i],new)==(i,)
assert sub(a,new)==(1,)
assert actions['m'][1]==(1,) and actions['m_inverse'][1]==(1,)
assert actions['m'][3]==(3,) and actions['m_inverse'][3]==(3,)
source_word=comm((6,),a)
assert len(source_word)==8
U=sub(a,{i+1:w for i,w in enumerate(sources)})
A={int(i):tuple(w) for i,w in D['source_ordinary_actions']['m'].items()}
free_residue=mul(sub(U,A),inv(U))
assert free_residue and not fill(free_residue)
out={'status':'PASS_COMPLETE_ONE_SIDED_FILLING_WITH_NONFAITHFUL_SOURCE_DETECTOR','time_utc':datetime.now(timezone.utc).isoformat(),'inputs':[{'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],'all40_cross_half_pairs':pairs,'free7_generator_names':['a','B','d','e','f','g','x'],'all_four_signed_free7_source_actions':actions,'source_contact_plus_retained_basis':new,'old_free7_in_source_basis':inverse,'source6_word_in_quotient_kernel':source_word,'actual_F11_word_U':U,'actual_free_F11_operator_residue':free_residue,'counts':{'cross_half_node_pairs':40,'filled_signed_barred_images':16,'signed_free7_inverse_checks':28,'basis_inverse_checks':14},'scope':'An exact actual whole-source-operator free7-by-free2 quotient. The displayed nontrivial free-source word is killed by this quotient only; its actual status modulo the complete N is not decided by this certificate.'}
p=R/'work_DE/next_marginal_source/one_sided_source_detector26.json';p.write_text(json.dumps(out,indent=2)+'\n')
print('PASS all40 node pairs cross the four-label halves; entire retained/source normal orbit killed uniformly.')
print('PASS all16 discarded signed images, all28 free7 inverse checks and all14 source-basis inverse checks.')
print('Four source contacts plus f,g,x form a literal free7 basis; source6 detector kills nontrivial8-letter [m,s1 s4^-1 s1^-1].')
print('Actual pre-node F11 operator residue length',len(free_residue),'; no membership conclusion modulo N.')
