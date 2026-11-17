#!/usr/bin/env python3
"""Actual complete two-cut input, keeping the x-coupling words."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json'
D=json.loads(P.read_text())
def red(w):
 o=[]
 for z in w:
  if o and o[-1]==-z:o.pop()
  else:o.append(z)
 return o
def inv(w):return [-z for z in w[::-1]]
def mul(*ws):return red([z for w in ws for z in w])
def sub(w,M):return red([z for x in w for z in (M[abs(x)] if x>0 else inv(M[abs(x)]))])
def con(h,w):return mul(h,w,inv(h))
ops={s:{int(i):w for i,w in M.items()} for s,M in D['source_ordinary_actions'].items()}
delta={int(i):w for i,w in D['selected_plus_involution'].items()}
v_to_old={i:([i] if i<=5 or i==11 else [11,i,-11]) for i in range(1,12)}
old_to_v={i:([i] if i<=5 or i==11 else [-11,i,11]) for i in range(1,12)}
for i in range(1,12):
 assert sub(v_to_old[i],old_to_v)==[i]
 assert sub(old_to_v[i],v_to_old)==[i]
vmaps={s:{i:sub(sub(v_to_old[i],M),old_to_v) for i in range(1,12)}
       for s,M in ops.items()}
dv={i:sub(sub(v_to_old[i],delta),old_to_v) for i in range(1,12)}
for i in range(1,11):
 assert dv[i]==([i+5] if i<=5 else [i-5])
assert dv[11]==[-11]
couplings={}
for s in ['m','m_inverse']:
 assert all(11 not in [abs(z) for z in ops[s][i]] for i in range(1,11))
 w=ops[s][11]
 assert w[0]==11 and all(abs(z)!=11 for z in w[1:])
 couplings[s]={'basis':'H_m and x','left':[],'right':w[1:]}
for s in ['v','v_inverse']:
 assert all(11 not in [abs(z) for z in vmaps[s][i]] for i in range(1,11))
 w=vmaps[s][11]
 assert w.count(11)==1 and -11 not in w
 j=w.index(11)
 couplings[s]={'basis':'H_v and x','left':w[:j],'right':w[j+1:]}

nodes=[]
for row in D['all20_orbifold_node_relations']:
 r0,r1=row['ordinary_two_sheets']
 if row['side']=='minus':
  assert all(abs(z)!=11 for z in r0+r1)
  nodes.append({'side':'minus','name':row['name'],'H_m_relators':[r0,r1]})
 else:
  shifted=con([11],r1)
  assert shifted==sub(r0,delta)
  a,b=sub(r0,old_to_v),sub(shifted,old_to_v)
  assert all(abs(z)!=11 for z in a+b)
  nodes.append({'side':'plus','name':row['name'],'H_v_relators':[a,b],
                'second_sheet_exact_transport':'x r_sheet1 x^-1 = delta(r_sheet0)'})

def level_word(w):
 n=0;o=[]
 for z in w:
  if abs(z)==11:n+=1 if z>0 else -1
  else:
   letter=(n,z)
   if o and o[-1]==(n,-z):o.pop()
   else:o.append(letter)
 return o,n
plus_intrusion,head=level_word(ops['v'][1])
assert head==0 and any(n==1 for n,z in plus_intrusion)
assert any(n==0 for n,z in plus_intrusion)
assert any(abs(z)==11 for z in vmaps['m'][2])
result={'status':'PASS','input':str(P.relative_to(ROOT)),'sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
 'H_m_basis':'K,cKc','H_v_basis':'K,tau K tau','H_v_to_original':v_to_old,'original_to_H_v':old_to_v,
 'all_four_operators_in_H_v_basis':vmaps,'delta_in_H_v_basis':dv,
 'exact_x_couplings':couplings,'complete_regional_node_lists':nodes,
 'v_of_a_level_word':plus_intrusion,'m_of_B_outside_H_v_free_word':vmaps['m'][2],
 'scope':'Exact pre-node free splittings and complete relocated regional input. No shared invariant cut, post-node free product, or regional injection is asserted.'}
Q=ROOT/'work_CE/next_symmetric_nodes/two_regional_level_splittings26.json'
Q.write_text(json.dumps(result,indent=2)+'\n')
print('PASS all22 free-basis inverse equations and11 literal delta equations.')
print('PASS all40 signed regional-generator containment checks and4 complete x couplings.')
print('PASS both sheets of all20 local nodes; plus second sheet moved by the exact x conjugator.')
print('PASS exact pre-node obstructions: v(a) uses levels0/1; m(B) is outside the H_v free factor.')
