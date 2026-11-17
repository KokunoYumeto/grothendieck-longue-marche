"""Bounded exact source-orbit folding for a peripheral marking; not normality."""
from pathlib import Path
import json,time
from weighted_stallings import WeightedFold,inverse,substitute
HERE=Path(__file__).resolve().parent
d=json.loads((HERE/'tangent_bundle_fiber_data.json').read_text())
actions={int(k)+1:{int(i):tuple(w) for i,w in A.items()} for k,A in d['old_actions'].items()}
actions.update({-int(k)-1:{int(i):tuple(w) for i,w in A.items()} for k,A in d['old_inverse_actions'].items()})
records=[{'seed':int(k),'action_path':[],'word':list(inverse(w))} for k,w in d['new_fiber_words'].items()]
seen={tuple(r['word']) for r in records};front=records[:];started=time.monotonic()
steps=[];last=None
for depth in range(3):
 f=WeightedFold([r['word'] for r in records],allow_relations=True)
 expansions={str(j):f.rewrite((j,)) for j in d['killed_basis']}
 vertices=len({f.find(j)[0] for j in range(len(f.parent))})
 print('depth',depth,'words',len(records),'vertices',vertices,'literal_U_membership',{j:w is not None for j,w in expansions.items()},'seconds',round(time.monotonic()-started,3),flush=True)
 steps.append({'depth':depth,'word_count':len(records),'vertices':vertices,'expansions':expansions})
 last=f
 if all(w is not None for w in expansions.values()) or depth==2:break
 new=[]
 for r in front:
  for a,A in actions.items():
   w=substitute(r['word'],A)
   if w in seen or inverse(w) in seen:continue
   seen.add(w);new.append({'seed':r['seed'],'action_path':r['action_path']+[a],'word':list(w)})
 records+=new;front=new
out={'scope':'Only the displayed finite source-word membership statements. No uniform retained conjugation or kernel equality is inferred.','source_orbit_words':records,'fold_steps':steps,'literal_U_expansions':steps[-1]['expansions'],'rank_lowering_relations':last.discarded_relations}
(HERE/'tangent_seed_basis.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS exact fold and every returned expansion checked by substitution; uniform normality remains open.',flush=True)
