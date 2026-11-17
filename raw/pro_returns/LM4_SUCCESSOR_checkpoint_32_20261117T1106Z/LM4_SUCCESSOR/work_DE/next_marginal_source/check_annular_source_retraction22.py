#!/usr/bin/env python3
"""A complete actual annular-source free-five detector, not an orbit test."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/inner_q0_adapted_basis22.json',
       Path(__file__).with_name('inner_q0_source22.json')]
D,SOURCE=[json.loads(p.read_text()) for p in paths]
def free_red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(x)
 return tuple(a)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*ws):return free_red(x for w in ws for x in w)
def sub(w,A):return mul(*(A[abs(x)] if x>0 else inv(A[-x]) for x in w))
def cone_red(w):
 a=[]
 for x in w:
  x=3 if abs(x)==3 else x
  if a and (a[-1]==-x or a[-1]==x==3):a.pop()
  else:a.append(x)
 return tuple(a)
def csub(w,A):return cone_red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[-x])))
def project(w):
 parity=0;out=[];positions={1:1,2:2,5:3,6:4};keep={1:0,2:1,5:0,6:0}
 for x in cone_red(w):
  if x==3:parity^=1
  elif abs(x)==4:out.append(5*(1 if x>0 else -1))
  elif parity==keep[abs(x)]:out.append(positions[abs(x)]*(1 if x>0 else -1))
 assert parity==0
 return free_red(out)

psi={int(k):tuple(v) for k,v in D['source_h_action'].items()}
psiinv={int(k):tuple(v) for k,v in D['source_h_inverse_action'].items()}
assert psi[3]==(3,)==psiinv[3]
mapping=[]
for j in (1,2,4,5,6):
 for side in (0,1):
  word=(j,) if side==0 else (3,j,3)
  image=project(csub(word,psi));negative=project(csub(word,psiinv))
  assert image==mul((-5,),project(word),(5,))
  assert negative==mul((5,),project(word),(-5,))
  mapping.append({'ordinary_generator':word,'projection':project(word),
                  'positive_source_operator_projection':image,
                  'negative_source_operator_projection':negative})
assert len(mapping)==10
nodes=[]
for row in D['all_ten_relations']:
 r=tuple(row['new_relation'])
 for side in (0,1):
  word=r if side==0 else (3,)+r+(3,)
  assert project(word)==()
  nodes.append({'name':row['name'],'physical_labels':row['physical_labels'],
                'cone_conjugated':bool(side),'image':[]})
assert len(nodes)==20

actual=[]
for row in SOURCE['four_contact_source_words_in_common_q0_marking']:
 image=project(row['source_word_in_q0_adapted_Y_basis'])
 actual.append({'name':row['name'],'actual_Y_word':row['source_word_in_q0_adapted_Y_basis'],
                'free5_image':image})
images={1:(2,),2:(2,5,3,4,-3,-5,-2),3:(3,),4:(1,),5:(5,)}
assert [row['free5_image'] for row in actual]==[images[j] for j in range(1,5)]
# Source order: beta11,beta22,beta33,beta44,h_C. Target: X1..X4,H.
inverse={1:(4,),2:(1,),3:(3,),4:(-3,-5,-1,2,1,5,3),5:(5,)}
for j in range(1,6):
 assert sub(images[j],inverse)==(j,)
 assert sub(inverse[j],images)==(j,)

out={'status':'PASS','inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'generic_ordinary_projection':{'U1':'X1','bar_U1':'1','U2':'1','bar_U2':'X2',
   'U5':'X3','bar_U5':'1','U6':'X4','bar_U6':'1','F':'H','bar_F':'H','h_C':'H'},
 'all_ten_generic_generators_both_source_directions':mapping,
 'all_twenty_complete_node_relators':nodes,
 'actual_four_contact_source_images':actual,
 'fifth_actual_source_image':[5],
 'source_to_target_free_basis':images,'target_to_source_inverse_basis':inverse,
 'both_five_generator_inverse_compositions':10,
 'conclusion':'The actual annular fixed-source F5 embeds as a retract of the ordinary annular group; its closure is its full free profinite completion.',
 'remaining_scope':'No equality of the annular cone centralizer with the source, or global fixed-source equality, is inferred.'}
Path(__file__).with_name('annular_source_retraction22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all10 generic ordinary mapping relations in BOTH signed directions.')
print('PASS all20 complete Reidemeister-Schreier node relators.')
print('PASS actual source images X2,(X2 H X3)X4(X2 H X3)^-1,X3,X1,H.')
print('PASS both5-generator inverse substitutions; actual annular source is a retract.')
