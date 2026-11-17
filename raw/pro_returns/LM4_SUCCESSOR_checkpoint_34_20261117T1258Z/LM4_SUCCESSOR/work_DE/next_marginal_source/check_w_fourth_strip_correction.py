"""One exact source-membership test for the fourth product-one node correction.

Only literal membership in a bounded, explicitly generated actual source
subgroup is tested.  Failure is not exclusion from the whole source image.
"""
from pathlib import Path
import json,time
from weighted_stallings import multiply as m,inverse as inv,substitute as sub,WeightedFold
P=Path(__file__).resolve().parent
b=json.loads((P/'w_source_adapted_basis.json').read_text())
l=json.loads((P/'w_local_markings.json').read_text())
back={int(k):tuple(w) for k,w in b['initial_basis_in_new'].items()}
rr=l['all_local_markings'][4]
assert rr['name']=='base_positive_3'
per={int(j):sub(w,back) for j,w in rr['transported_peripheral_words_by_label'].items()}
g=[];w=per[7]
while len(w)>1:assert w[0]==-w[-1];g.append(w[0]);w=w[1:-1]
assert w==(12,)
C=m(inv(g),per[3],g)
a={int(j):tuple(w) for j,w in b['actions_in_new']['4'].items()}
order=[lab for lab in rr['local_order'] if lab in [3,7]]
K=m(*(C if lab==3 else (12,) for lab in order))
L=m(inv(sub(g,a)),g,K)
v=m(L,inv(K))
assert a[12]==m(L,(12,),inv(L)) and sub(C,a)==m(L,C,inv(L))
source={int(k):tuple(w) for k,w in b['all_source_words_in_new'].items()}
ops=[]
for i in range(6):
    for kind in ['actions_in_new','inverse_actions_in_new']:
        ops.append((i,kind,{int(j):tuple(w) for j,w in b[kind][str(i)].items()}))
rows=[{'source_index':j,'operator':None,'word':w} for j,w in sorted(source.items())]
for i,kind,op in ops:
    rows.extend({'source_index':j,'operator':[i,kind],'word':sub(w,op)} for j,w in sorted(source.items()))
started=time.monotonic();fold=WeightedFold([r['word'] for r in rows],allow_relations=True)
answer=fold.rewrite(v)
if answer is not None:assert sub(answer,{i+1:r['word'] for i,r in enumerate(rows)})==v
out={'description':__doc__,'normalized_deleted_core':C,'actual_action_conjugator':L,'local_pair_boundary':K,'correction':v,'source_generators':rows,'exact_source_expression':answer,'elapsed_seconds':time.monotonic()-started,'scope':'A returned expression is a literal actual H word. None means only failure in this169-generator finite subgroup, not nonmembership in H.'}
(P/'w_fourth_strip_correction.json').write_text(json.dumps(out,indent=2)+'\n')
print('Actual normalized node and correction identities PASS; correction length',len(v))
print('Tested actual source words',len(rows),'elapsed',round(out['elapsed_seconds'],3))
print('Exact expression found:',answer is not None)
if answer is not None:print('Expression in listed source generators:',list(answer))
