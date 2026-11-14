from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1];W=R.parent
(R/'inputs').mkdir(parents=True,exist_ok=True)
rows=[]
for src,dst in [('research_e122/inputs/e119_e53_genus_transition.bin','e119_lower.bin'),
                ('research_e122/inputs/e122_literal_unit_witnesses.json','e122_witnesses.json'),
                ('research_e122/code/e53_upper_witness_verify.out','e122_witness_verify.out'),
                ('research_e123/code/e53_positional_presentation.out','e123_presentation.out')]:
 p=W/src;q=R/'inputs'/dst
 shutil.copy2(p,q)
 rows.append({'source':src,'copy':'inputs/'+dst,'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
D=json.loads((R/'inputs/e122_witnesses.json').read_text())
V=[json.loads(x) for x in (R/'inputs/e122_witness_verify.out').read_text().splitlines() if x.startswith('{')][0]
assert V['cube_identities']==22 and V['relative_norm_identities']==22
inp=[D['root_exponents'],V['root_character_matrix']]
(R/'inputs/e53_ordinary_kernel_input.txt').write_text(json.dumps(inp)+'\n')
(R/'inputs/manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'status':'PASS','inputs':rows,'literal_roots':22,'source_characters':V['rank_mod3']},indent=2))
