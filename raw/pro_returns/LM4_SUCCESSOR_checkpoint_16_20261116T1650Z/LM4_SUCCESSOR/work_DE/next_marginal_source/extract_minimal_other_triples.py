"""Two-relator local descriptions of the remaining eight triple fillings.

The full Artin action verifies every absorbed local prefix. Exact cyclic
Britton certificates compare the resulting local relations with the
rank17 partial HNN. No subgroup injection in a subsequent quotient is
assumed.
"""
from pathlib import Path
import contextlib,io,json,itertools
with contextlib.redirect_stdout(io.StringIO()):
 import reduce_other_triples_hnn as H
from weighted_stallings import reduce_word as red,inverse as iv,multiply as mul,substitute as sub
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'remaining_pencil_braids.json').read_text())
new={i:(i,) for i in range(1,21)};new[10]=(10,-11)
standards={i:H.art((i,i+1,i,i,i+1,i)) for i in range(1,19)}
def comm(a,b):return mul(a,b,iv(a),iv(b))
rows=[]
for row in D['loops']:
 if not row['name'].startswith('other_triple_'):continue
 local=mul(*(v['word'] for v in row['forward_segments'][1:]))
 found=None
 for cut in range(len(local)+1):
  prefix=local[:cut];rotated=mul(local[cut:],prefix);A=H.art(rotated)
  for i,S in standards.items():
   if A==S:found=(prefix,i);break
  if found:break
 assert found,('no standard full twist after a local prefix',row['name'],local)
 prefix,i=found;W=mul(row['forward_segments'][0]['word'],prefix);A=H.art(W)
 assert H.art(local)==H.art(mul(prefix,(i,i+1,i,i,i+1,i),iv(prefix)))
 ms=[sub(A[j],new) for j in range(i,i+3)];P=mul(*ms)
 relations=[]
 for j,m in enumerate(ms):
  rel=comm(P,m);result,history=H.cyclic_britton(rel)
  relations.append({'local_meridian':j,'original':rel,'result':result,'cyclic_history':history,
    'remaining_b_letters':sum(abs(x)==11 for x in result)})
 good=[j for j,r in enumerate(relations) if not r['remaining_b_letters']]
 rows.append({'name':row['name'],'absorbed_local_prefix':prefix,'standard_start_index':i,
  'meridians_special_basis':ms,'central_product':P,'relations':relations,
  'available_H_relation_indices':good,'two_H_relations_suffice':len(good)>=2})
 print(row['name'],'prefix',prefix,'three b counts',[r['remaining_b_letters'] for r in relations],
       'two H relations suffice',len(good)>=2,'lengths',[len(r['result']) for r in relations],flush=True)
(HERE/'minimal_other_triple_relations.json').write_text(json.dumps({'scope':__doc__,'rows':rows},indent=2)+'\n')
print('PASS: all eight exact local full-twist conjugacies and minimal relation comparisons.')
