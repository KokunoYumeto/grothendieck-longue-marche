#!/usr/bin/env python3
"""Authorized A74 structural preservation integration after root/DE PASS."""
from pathlib import Path
import hashlib,json

root=Path(__file__).resolve().parents[1]
changed=[]
def put(rel,s):
    (root/rel).write_text(s);changed.append(rel)
p=root/'notes/fgh_A74_draft.tex'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='1bd358a105dcaa547dd55788b60492b3c76f2b795dc82e828f2b1b26dd026e90'
s=p.read_text().replace('% A.74 candidate: notes only, awaiting full independent audits.',
    '% A.74: full root and DE proof/source audits PASS; reuses the exact A71--A73 certificates.')
put('sections/A_two_group_abelian_products.tex',s)
p=root/'sections/A.tex';s=p.read_text();needle='\\input{sections/A_semidihedral_two_power.tex}'
assert s.count(needle)==1 and 'A_two_group_abelian_products.tex' not in s
put('sections/A.tex',s.replace(needle,needle+'\n\\input{sections/A_two_group_abelian_products.tex}'))
p=root/'sections/A_general_cover_frontier.tex';s=p.read_text()
needle='the total genus. Products of two nonabelian Sylow factors and\nthe universal question remain outside these conclusions.'
assert needle in s
replacement='''the total genus.
A.74 extends the odd-abelian preservation theorem to all three
two-group families, including every quotient closure and
every intermediate. The same actual connected isogeny
pullback, separately proved tree condition and literal
rational-path lift apply to quaternion and semidihedral
factors as well. Products of two nonabelian Sylow factors,+arbitrary two-groups and the universal question remain
outside these conclusions.'''.replace('factors,\\+arbitrary','factors,\narbitrary')
# Keep the prose replacement literal and free of patch escape artifacts.
replacement=replacement.replace('factors,\\+arbitrary','factors,\narbitrary').replace('factors,+arbitrary','factors,\narbitrary')
put('sections/A_general_cover_frontier.tex',s.replace(needle,replacement))
row=json.loads((root/'notes/fgh_A74_row.json').read_text())
row['notes']=row['notes'].replace('Unregistered candidate pending full independent audits.',
    'Registered after full root and DE proof/source audits PASS; exact A71–A73 certificates are reused, with no new numerical inference.')
put('notes/fgh_A74_row.json',json.dumps(row,indent=2)+'\n')
p=root/'notes/a_results.json';rows=json.loads(p.read_text());assert not any(x['id']=='A.74' for x in rows)
rows.append(row);put('notes/a_results.json',json.dumps(rows,indent=2)+'\n')
p=root/'notes/fgh_A74_sources.md';s=p.read_text();backup=root/'notes/fgh_A74_sources_before_registration.md'
if not backup.exists():backup.write_text(s);changed.append(str(backup.relative_to(root)))
s=s.replace('Status: unregistered notes candidate, awaiting full independent audits. Complete proof notes/fgh_A74_draft.tex.',
    'Status: registered as A.74 after full root and DE proof/source audits PASS. Canonical proof sections/A_two_group_abelian_products.tex; exact audited original notes/fgh_A74_draft.tex remains preserved. The only proof-file editorial change is the registered status comment.')
put('notes/fgh_A74_sources.md',s)
for rel in changed:
    if rel.endswith('.tex'):
        b=(root/rel).read_bytes();s=b.decode()
        assert not any(x<32 and x not in(9,10) for x in b)
        assert s.count('\\[')==s.count('\\]')
        assert '\\+arbitrary' not in s
record={'status':'REGISTERED; root and DE full audits PASS','id':'A.74',
    'candidate_preserved':'notes/fgh_A74_draft.tex','editorial_changes':['Registered status comment'],
    'new_numerical_computation':False,'reused_exact_certificates':['code/a_dihedral_abelian_products.py','code/a_quaternion_two_power.py','code/a_semidihedral_two_power.py'],
    'bibliography_changed':False,'global_assembly_changed':False,
    'changed_files':{rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in changed}}
put('notes/fgh_A74_integration.json',json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'id':'A.74','changed_files':len(changed)},indent=2))
