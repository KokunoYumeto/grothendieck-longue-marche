"""Executed sphere-to-elliptic finite dictionaries, including every framing relation.
The geometric cubic/quartic covers and their inverse constructions are
proved in B.9 and B.29. Artin actions certify the displayed braid words.
"""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
H={};exec((P/'b_genus_zero.py').read_text().split('\ndata={}')[0],H)
red,inv,eq=H['red'],H['inv'],H['eq']
parents=json.loads((P/'b_parenthesized.json').read_text())
out={'mixed_models':{},'braid_checks':[]}
for m in (3,4):
 row=parents[str(m+1)];objects=row['objects'];arrows=row['arrows'];keys=[];emap=[]
 for a in arrows:
  u,v=objects[a['source']][1],objects[a['target']][1]
  key=(a['kind'],u,v,a['sigma'])
  if key not in keys:keys.append(key)
  emap.append(keys.index(key)+1)
 def word(w):return red((1 if e>0 else -1)*emap[abs(e)-1] for e in w)
 def braid(w):return red((1 if e>0 else -1)*keys[abs(e)-1][3] for e in w if keys[abs(e)-1][3])
 rels=[]
 for r in row['relations']:
  if r['type']=='outer boundary capping':continue
  w=word(r['word']);item=(tuple(w),r['type'])
  if item not in rels:rels.append(item)
 for w,t in rels:assert eq(m,braid(w),())
 dictionary=[]
 for r in row['inverse_chamber_dictionary']:
  if r['source']!=list(range(1,m+1)):continue
  w=word(r['word']);assert braid(w)==(r['sigma'],)
  dictionary.append(dict(sigma=r['sigma'],word=w))
 counts=dict(objects=len(row['shapes']),F_arrows=sum(k[0]=='F' for k in keys),B_arrows=sum(k[0]=='B' for k in keys),relations=len(rels))
 assert list(counts.values())==([2,1,2,1] if m==3 else [5,5,6,7])
 out['mixed_models'][str(m)]=dict(shapes=row['shapes'],arrows=[dict(id=i+1,kind=k[0],source=k[1],target=k[2],sigma=k[3]) for i,k in enumerate(keys)],relations=[dict(word=w,type=t) for w,t in rels],inverse_dictionary=dictionary,counts=counts)
 print('Mixed disk',m,'model:',counts,flush=True)
def check(n,name,lhs,rhs):
 assert eq(n,lhs,rhs),name
 out['braid_checks'].append(dict(strands=n,name=name,left=lhs,right=rhs))
a=(1,);b=(2,);c=(3,);s=(1,2,1);h=(1,2)*3
check(3,'S_squared_is_full_twist',s*2,h)
check(3,'S_fourth_is_boundary_twist',s*4,(1,2)*6)
check(3,'S_transports_a_to_b',s+a+inv(s),b)
check(3,'S_transports_b_to_a',s+b+inv(s),a)
check(3,'one_relator_S_presentation',(s+(-1,))*3,s*2)
q=(1,2,3)*2;delta=(1,2,3,1,2,1);z=(1,2,3)*4
check(4,'quartic_half_rotation_square',q*2,z)
check(4,'quartic_Garside_square',delta*2,z)
check(4,'quartic_S_fourth',s*4,(1,2)*6)
r=inv(s)+delta+s
check(4,'nonseparating_exchange_square',r*2,z)
check(4,'two_cycle_exchange',q+a+inv(q),c)
check(4,'two_cycle_exchange_back',q+c+inv(q),a)
check(4,'loop_bridge_embedding',a+inv(c)+r,(1,2)*3)
for n,zword in [(3,h),(4,z)]:
 for i in range(1,n):check(n,'full_twist_central_'+str(i),zword+(i,), (i,)+zword)
out['framing_data']={
 'cubic':{'root_rotation_per_scaling_loop':2,'tangent_rotation_per_scaling_loop':1,'boundary_word':h*2,'half_turn':'s^2 omega','omega_order':2,'sign_objects':[0,1]},
 'quartic':{'root_rotation_per_scaling_loop':1,'tangent_rotation_per_scaling_loop':[1,1],'full_twist_word':z,'full_twist_image':'z1 z2','sign_objects':[[0,0],[0,1],[1,0],[1,1]],'half_turn_group_relation':'(abc)^4=t1^2 t2^2'}
}
(P/'b_sphere_covers.json').write_text(json.dumps(out,indent=2)+'\n')
print(len(out['braid_checks']),'literal braid identities verified, including both S and node-exchange dictionaries.')
