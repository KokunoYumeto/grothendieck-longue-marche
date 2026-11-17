"""An ordered F13 free basis with all eight deleted generators in their actual partial source images."""
from pathlib import Path
import json
from weighted_stallings import substitute as sub,multiply as mul,inverse as inv,WeightedFold
P=Path(__file__).resolve().parent
m=json.loads((P/'tangent_bundle_nielsen_actions.json').read_text())
b=json.loads((P/'tangent_infinity_action.json').read_text())
d=json.loads((P/'tangent_ordered_family.json').read_text())
o=json.loads((P/'tangent_partial_source_words.json').read_text())
source={i+1:tuple(r['word']) for i,r in enumerate(m['source_orbit_words'])}
for j,w in m['killed_basis_source_expansions'].items():
 assert sub(w,source)==tuple(m['new_basis_in_old'][str(j)])
# The existing expressions are conjugates of single actual source orbits.
exp={int(j):tuple(w) for j,w in m['killed_basis_source_expansions'].items()}
cores={}
for j,w in exp.items():
 h=[];core=w
 while len(core)>1 and core[0]==-core[-1]:h.append(core[0]);core=core[1:-1]
 assert len(core)==1
 r=m['source_orbit_words'][abs(core[0])-1]
 parity=sum(abs(a)==2 for a in r['action_path'])%2
 assert parity==(1 if j in [2,6] else 0)
 cores[j]={'source_conjugator':h,'source_core':core,'core_family_parity':parity,'core_seed':r['seed'],'core_action_path':r['action_path']}
print('Existing U basis expressions are conjugates of actual source meridians in the correct partial family: PASS')
ordered={int(i):tuple(w) for i,w in d['ordered_basis_in_V'].items()};f=WeightedFold(list(ordered.values()))
# U2/U6 in the V marking; these inverses are already checked by B81.
v=json.loads((P/'tangent_node_strips.json').read_text());u_v={int(j):tuple(w) for j,w in v['new2_basis_in_V'].items()}
U2=f.rewrite(u_v[2]);U6=f.rewrite(u_v[6]);assert U2 is not None and U6 is not None
O={int(j):tuple(w) for j,w in o['other_family_V_in_ordered_basis'].items()}
# New basis order: four V, then O1,U2,O4,U6, then five retained generators.
newold={j:(j,) for j in range(1,14)}
newold.update({5:O[1],6:U2,7:O[4],8:U6})
fnew=WeightedFold(list(newold.values()))
oldnew={j:fnew.rewrite((j,)) for j in range(1,14)}
assert all(w is not None for w in oldnew.values())
for j in range(1,14):assert sub(newold[j],oldnew)==(j,) and sub(oldnew[j],newold)==(j,)
print('All26 inverse Nielsen substitutions for the source-contained ordered13 basis: PASS')
print('Constant-family U2/U6 in ordered basis:',U2,U6)
out={'description':__doc__,'new_basis_in_standard_ordered':newold,'standard_ordered_in_new_basis':oldnew,'source_core_family_checks':cores,'new_basis_families':{'moving':[1,2,3,4],'constant':[5,6,7,8],'retained':[9,10,11,12,13]},'scope':'The eight deleted basis elements lie in their actual partial source-kernel images, which are normal in the full source image. Their normal closures in F13 are the two ambient family kernels. No equality of source and ambient kernels is inferred.'}
(P/'tangent_source_ordered_basis.json').write_text(json.dumps(out,indent=2)+'\n')
