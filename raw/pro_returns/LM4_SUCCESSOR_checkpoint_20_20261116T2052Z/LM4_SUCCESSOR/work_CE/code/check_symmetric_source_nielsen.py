#!/usr/bin/env python3
"""One exact13-word Nielsen test of the actual completed source input.
This is a discrete subgroup fold, not a finite quotient search. A proper
answer does not exclude the full source orbit subgroup I.
"""
from pathlib import Path
import sys,json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
sys.path.insert(0,str(ROOT/'work_DE/next_marginal_source'))
from weighted_stallings import WeightedFold,substitute,inverse
path=P/'symmetric_full_source_data.json';raw=path.read_bytes();D=json.loads(raw)
source=[tuple(r['positive_source_word_F13']) for r in D['source_peripheral_generators']]
retained=[int(i) for i,w in D['F13_to_retained_F5'].items() if w]
assert retained==[1,4,9,12,13]
words=source+[(j,) for j in retained];assert len(words)==13
started=time.monotonic();fold=WeightedFold(words)
roots=sorted(set(fold.find(i)[0] for i in range(len(fold.parent))))
edges=[]
for u in roots:
    for label,e in sorted(fold.adj[u].items()):
        a,c,b,w=fold.edge_weight(e);assert a==u and c==label
        edges.append({'from':a,'letter':c,'to':b,'source_weight':w})
assert len(edges)%2==0
rank=len(edges)//2-len(roots)+1
back={j:fold.rewrite((j,)) for j in range(1,14)}
onto=all(w is not None for w in back.values())
if onto:
    fw={j+1:w for j,w in enumerate(words)}
    for j in range(1,14):assert substitute(back[j],fw)==(j,)==substitute(fw[j],back)
    assert len(roots)==1 and len(edges)==26
else:assert len(roots)>1
out={'scope':__doc__,'input_sha256':hashlib.sha256(raw).hexdigest(),
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'actual8_source_words':source,'actual5_retained_generators':retained,
 'test_words':words,'root_vertex':fold.find(0)[0],
 'core_vertices':roots,'core_directed_edges':edges,'core_rank':rank,
 'standard_generator_rewrites':back,'onto_F13':onto,
 'normalization_basis_inverse':back if onto else None,
 'claims_excluded':['full source orbit subgroup properness','I=R','ambient normality'],
 'elapsed_seconds':time.monotonic()-started}
if onto:
    normalized=[]
    for r in D['old_source_generators']:
        A={int(i):tuple(w) for i,w in r['source_push_F13'].items()}
        Ai={int(i):tuple(w) for i,w in r['source_pullback_F13'].items()}
        normalized.append({'name':r['name'],
            'images':{j:substitute(substitute(w,A),back) for j,w in fw.items()},
            'inverse_images':{j:substitute(substitute(w,Ai),back) for j,w in fw.items()}})
    out['actual_source_actions_in_normalized_basis']=normalized
(P/'symmetric_source_nielsen_test.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact fold: vertices',len(roots),'edges',len(edges)//2,'rank',rank,'onto F13',onto)
print('Missing standard generators:',[j for j,w in back.items() if w is None])
print('All returned inverse words checked by free substitution; full source orbit not inferred.')
print('Elapsed seconds',round(time.monotonic()-started,3))
