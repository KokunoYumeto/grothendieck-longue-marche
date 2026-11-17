#!/usr/bin/env python3
"""Exact finite source-subgroup membership for the actual w1 factors.

Membership failures are not assertions about the whole source image.
"""
from pathlib import Path
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'
sys.path.insert(0,str(P))
from weighted_stallings import WeightedFold

def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(x)
    return a
def inv(w):return[-x for x in w[::-1]]
def sub(w,a):return red(y for x in w for y in(a[abs(x)] if x>0 else inv(a[abs(x)])))
def mp(a):return{int(i):w for i,w in a.items()}

base=json.loads((P/'w_pencil_fiber_data.json').read_text())
check=json.loads((ROOT/'work_CE/w_pencil_independent_certificate.json').read_text())
adapt=json.loads((P/'w_source_adapted_basis.json').read_text())
rho=mp(check['corner_to_original_fiber'])
source=mp(base['source_fiber_words'])
chosen=adapt['source_word_indices']
groups={'nine_source_words':[source[i] for i in chosen],
        'all13_source_words':list(source.values())}
newold=mp(adapt['new_basis_in_initial']);oldnew=mp(adapt['initial_basis_in_new'])
for i in range(1,13):assert sub(newold[i],oldnew)==[i] and sub(oldnew[i],newold)==[i]
for j,i in enumerate(chosen,1):assert newold[j]==source[i]

queries={f'exterior_{i}':rho[i] for i in range(1,10)}
for i,j in ((1,2),(3,4),(5,6),(8,9)):
    queries[f'pair_product_{i}_{j}']=red(rho[i]+rho[j])
queries['local_boundary']=sub([10,11,12],rho)
queries['point_push']=sub([-10],rho)
queries['common_exterior_conjugator']=sub([-10,-12,-11,-10],rho)
out={}
for label,words in groups.items():
    f=WeightedFold(words,allow_relations=True)
    generators={i+1:w for i,w in enumerate(words)}
    results={}
    for name,w in queries.items():
        answer=f.rewrite(w)
        if answer is not None:assert sub(answer,generators)==red(w)
        results[name]=None if answer is None else list(answer)
    out[label]=results
    print(label)
    for name,answer in results.items():print(' ',name,':' ,'YES '+str(answer) if answer is not None else 'NO (only this finite subgroup)')

out['source_adapted_basis_checks']=24
out['corner_generators_in_source_adapted_basis']={i:sub(w,oldnew) for i,w in rho.items()}
out['actual_w1_action_in_source_adapted_basis']={i:sub(sub(w,mp(base['old_and_filled_actions']['1'])),oldnew) for i,w in newold.items()}
out['scope']='Exact finite generated source-word subgroups only. No negative membership assertion about the full old-action orbit subgroup.'
(ROOT/'work_CE/w1_source_pair_factor_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all returned source expansions and24 independent source-adapted basis inverses.')
