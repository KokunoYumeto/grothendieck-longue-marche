"""Assemble the exact81-relation total presentation after local reductions.

The fiber part is a quotient of the checked partial HNN by24 H relators.
No injection of its base or edge groups after quotienting is asserted.
"""
from pathlib import Path
import contextlib,io,json,hashlib
with contextlib.redirect_stdout(io.StringIO()):
 import reduce_other_triples_hnn as H
from weighted_stallings import multiply as mul,inverse as iv,substitute as sub
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
Z=json.loads((ROOT/'work_CE/zero_nodes_hnn_reductions.json').read_text())
T=json.loads((HERE/'minimal_other_triple_relations.json').read_text())
B=json.loads((HERE/'ratio_pencil_words.json').read_text())
rels=[]
for r in Z['rows']:
 result,steps=H.britton(r['original_commutator'])
 assert result==tuple(r['reduced_H_relator'])
 assert all(abs(x)!=11 for x in result)
 rels.append({'origin':r['name'],'word':result})
for r in T['rows']:
 assert len(r['available_H_relation_indices'])==3
 for j in (0,1):
  rel=r['relations'][j];result,steps=H.cyclic_britton(rel['original'])
  assert result==tuple(rel['result']) and all(abs(x)!=11 for x in result)
  rels.append({'origin':r['name']+f':local{j}','word':result})
assert len(rels)==24
old_to_new={i:(i,) for i in range(1,21)};old_to_new[10]=(10,-11)
new_to_old={i:(i,) for i in range(1,21)};new_to_old[10]=(10,11)
actions=[]
for r in B['loops']:
 if r['name'] not in ('base1','base2'):continue
 A=H.art(r['word']);Ai=H.art(iv(r['word']))
 Anew={i:sub(sub(new_to_old[i],A),old_to_new) for i in range(1,21)}
 Ainew={i:sub(sub(new_to_old[i],Ai),old_to_new) for i in range(1,21)}
 for i in range(1,21):assert sub(Anew[i],Ainew)==(i,)==sub(Ainew[i],Anew)
 actions.append({'name':r['name'],'images_special_basis':Anew,'inverse_images_special_basis':Ainew})
files=[ROOT/'work_CE/zero_nodes_hnn_reductions.json',HERE/'minimal_other_triple_relations.json',HERE/'ratio_pencil_words.json']
out={'scope':__doc__,'fiber_generators':list(range(1,21)),'source_H_omitted_generator':11,
 'missing_retained_generator_b':11,'retained_base_generators':['tau1','tau2'],
 'b_relations':[{'domain':d,'range':r} for d,r in zip(H.DD,H.RR)],
 'H_relators':rels,'retained_actions':actions,
 'relation_count':{'b_edge_equations':17,'H_relators':24,'retained_action_equations':40,'total':81},
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
 'limitation':'All29 untransformed filled relations still admit the x7 S4 obstruction. The actual retained-base translates are essential; no uniform source normality is inferred.'}
(HERE/'reduced_pencil_presentation.json').write_text(json.dumps(out,indent=2)+'\n')
print('Independent replay of8 zero-node reductions and16 selected triple relations: PASS')
print('Both retained actions and inverse actions in the actual special basis: PASS')
print('Generators22; listed relations17+24+40=81; Euler count1-22+81=60.')
print('PASS: exact finite total presentation; base/edge injection after the H quotient remains unproved.')
