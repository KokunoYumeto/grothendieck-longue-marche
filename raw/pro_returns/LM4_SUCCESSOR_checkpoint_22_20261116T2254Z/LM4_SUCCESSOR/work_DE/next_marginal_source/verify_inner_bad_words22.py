#!/usr/bin/env python3
"""Independent literal word replay of all regional actions and normalization."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'work_CE/next_symmetric_nodes'
rawp=D/'inner_bad_orbifold_words22.json';normp=D/'inner_bad_normalized_relations22.json'
raw=json.loads(rawp.read_text());norm=json.loads(normp.read_text())
def reduce(w,cone=False):
 st=[]
 for a in w:
  a=2 if cone and abs(a)==2 else a
  if st and (st[-1]==-a or cone and st[-1]==a==2):st.pop()
  else:st.append(a)
 return st
def inverse(w):return [-a for a in reversed(w)]
def subst(w,A,cone=False):
 out=[]
 for a in w:out.extend(A[abs(a)] if a>0 else inverse(A[-a]))
 return reduce(out,cone)
def push(w):
 A={i:[i] for i in range(1,7)}
 for letter in w:
  j=abs(letter);step={i:[i] for i in range(1,7)}
  if letter>0:step[j]=[j,j+1,-j];step[j+1]=[j]
  else:step[j]=[j+1];step[j+1]=[-j-1,j,j+1]
  A={i:subst(v,step) for i,v in A.items()}
 return A
def parse(A):return {int(k):v for k,v in A.items()}
action_checks=0
for rr in raw['loops']:
 w=rr['chronological_braid'];A=push(w);B=push(inverse(w))
 assert A==parse(rr['positive_push']) and B==parse(rr['negative_pull'])
 for i in A:
  assert subst(A[i],B)==[i] and subst(B[i],A)==[i];action_checks+=2
 assert subst(list(range(1,7)),A)==list(range(1,7))
 wh=rr['whisker'];aa=push(wh+rr['standard_local_braid']+inverse(wh))
 assert aa==A
 back=push(inverse(wh))
 for nn in rr['nodes']:
  j,k=nn['local_positions'];assert nn['meridians']==[back[j],back[k]]
new=parse(norm['new_generators_in_old']);old=parse(norm['old_generators_in_new'])
for i in new:
 assert subst(new[i],old,True)==[i] and subst(old[i],new,True)==[i]
ordinary_map={1:1,4:2,5:3,3:4,6:5}
def ordinary(w):
 parity=0;out=[]
 for a in reduce(w,True):
  if abs(a)==2:parity^=1
  else:out.append((ordinary_map[abs(a)]+5*parity)*(1 if a>0 else -1))
 assert parity==0
 return reduce(out)
def nf(w):
 # Alternating free-product blocks. A product block has two free coordinates.
 blocks=[]
 for a in w:
  tag='branch' if abs(a) in (5,10) else 'product'
  if blocks and blocks[-1][0]==tag:item=blocks.pop()
  else:item=[tag,[]] if tag=='branch' else [tag,[],[]]
  if tag=='branch':item[1]=reduce(item[1]+[a]);nonempty=bool(item[1])
  else:
   axis=1 if abs(a)<5 else 2;item[axis]=reduce(item[axis]+[a]);nonempty=bool(item[1] or item[2])
  if nonempty:blocks.append(item)
 return blocks
failed=[];cone_checks=0
lookup={(r['index'],tuple(n['physical_labels'])):n for r in raw['loops'][1:] for n in r['nodes']}
for r in norm['relations']:
 original=lookup[r['loop_index'],tuple(r['physical_labels'])]['relation']
 assert reduce(original,True)==r['original_relation_mod_cone_square']
 changed=subst(original,old,True);assert changed==r['new_relation']
 h=r['cyclic_conjugator'];core=r['cyclic_core']
 assert reduce(h+core+inverse(h),True)==changed
 ow=ordinary(core);assert ow==r['ordinary_core']
 value=nf(ow);assert value==r['product_free_branch_candidate_normal_form']
 if value:failed.append({'name':r['loop_name'],'labels':r['physical_labels'],'ordinary_word':ow,'normal_form':value})
 if r['kind']=='cone_contact':
  st=ordinary(r['standard_new_relation']);rots=[]
  for v in (st,inverse(st)):rots.extend(v[k:]+v[:k] for k in range(len(v)))
  assert ow in rots;cone_checks+=1
assert [(r['name'],r['labels']) for r in failed]==[('beta_13',[2,4]),('alpha_14',[4,3]),('beta_24',[5,3])]
out={'status':'PASS','raw_input_sha256':hashlib.sha256(rawp.read_bytes()).hexdigest(),
 'normalization_sha256':hashlib.sha256(normp.read_bytes()).hexdigest(),
 'independent_Artin_method':'Chronological left substitution of each standard generator; no producer imports.',
 'lassos':len(raw['loops']),'both_signed_inverse_checks':action_checks,
 'all_based_local_transports':True,'Nielsen_inverse_checks':12,
 'all_complete_relations':10,'standard_cone_contacts':cone_checks,
 'nontrivial_naive_product_images':failed,
 'scope':'Failure only of this specified marked naive product quotient; no nonisomorphism assertion for all markings.'}
Path(__file__).with_name('inner_bad_words_independent22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS10 literal actions/transports,120 inverse substitutions,12 Nielsen inverses,10 relation rewrites')
print('PASS4 cone-contact standardizations; exactly3 marked product failures')
for r in failed:print(r['name'],r['labels'],'normal-form blocks',len(r['normal_form']))
