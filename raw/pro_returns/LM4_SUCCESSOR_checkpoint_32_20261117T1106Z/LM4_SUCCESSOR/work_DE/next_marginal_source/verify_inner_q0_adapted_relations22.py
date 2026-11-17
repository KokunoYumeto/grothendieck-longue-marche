#!/usr/bin/env python3
"""Independent simultaneous ten-relator comparison in the q0 Y basis."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/inner_bad_orbifold_words22.json',
       ROOT/'work_CE/next_symmetric_nodes/inner_q0_adapted_basis22.json',
       Path(__file__).with_name('inner_q0_source22.json')]
D,CE,OWN=[json.loads(p.read_text()) for p in paths]
def red(w,c):
 a=[]
 for x in w:
  x=c if abs(x)==c else int(x)
  if a and (a[-1]==-x or a[-1]==x==c):a.pop()
  else:a.append(x)
 return tuple(a)
def inv(w,c):return red((-x for x in reversed(w)),c)
def sub(w,A,c):
 ans=[]
 for x in w:ans.extend(A[abs(x)] if x>0 else inv(A[-x],c))
 return red(ans,c)
J={int(k):tuple(v) for k,v in OWN['q0_adapted_basis_in_old'].items()}
Ji={int(k):tuple(v) for k,v in OWN['old_basis_in_q0_adapted'].items()}
assert J=={int(k):tuple(v) for k,v in CE['Y_in_old'].items()}
assert Ji=={int(k):tuple(v) for k,v in CE['old_in_Y'].items()}
rows=[]
for loop in D['loops'][1:]:
 for node in loop['nodes']:
  record=next(r for r in CE['all_ten_relations']
              if r['name']==loop['name'] and r['physical_labels']==node['physical_labels'])
  changed=sub(node['relation'],Ji,3)
  assert changed==tuple(record['new_relation'])
  assert sub(changed,J,2)==red(node['relation'],2)
  assert [list(sub(w,Ji,3)) for w in node['meridians']]==record['new_meridians']
  prefix=tuple(record['cyclic_prefix']);core=tuple(record['cyclic_core'])
  assert red(prefix+core+inv(prefix,3),3)==changed
  rows.append({'name':loop['name'],'physical_labels':node['physical_labels'],
               'new_relation':changed,'round_trip':'PASS'})
assert len(rows)==10
for j in range(1,7):
 lifted=sub(CE['source_h_action'][str(j)],J,2)
 assert lifted==tuple(OWN['adapted_source_operator_on_Y_in_old'][str(j)])
out={'status':'PASS','inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
     'all_basis_coordinates_agree':True,'all_six_source_operator_coordinates_agree':True,
     'all_ten_simultaneous_relators':rows,
     'scope':'Exact common marked presentation comparison. No post-filling HNN injection or annular fixed-subgroup theorem.'}
Path(__file__).with_name('inner_q0_adapted_relations_independent22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all12 common basis coordinates and all6 source-operator images.')
print('PASS all10 simultaneous relation words, peripheral pairs, cyclic conjugators and literal round trips.')
