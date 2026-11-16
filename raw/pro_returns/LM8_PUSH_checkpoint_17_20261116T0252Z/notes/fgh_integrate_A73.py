#!/usr/bin/env python3
"""Authorized A73 integration after full root and DE audits."""
from pathlib import Path
import hashlib,json,subprocess,sys

root=Path(__file__).resolve().parents[1]
changed=[]
def put(rel,s):
    (root/rel).write_text(s);changed.append(rel)
draft=root/'notes/fgh_A73_draft.tex'
assert hashlib.sha256(draft.read_bytes()).hexdigest()=='24e5ba673c1a3d9a2bbe8fcd64a83e2781a418fc0ef39f584c371198ab87ac4a'
s=draft.read_text().replace('% A.73 candidate: notes only, unregistered pending full independent audits.',
    '% A.73: full root and DE proof/source/exact-certificate audits PASS.')
s=s.replace('notes/fgh_A73_certificate.py','code/a_semidihedral_two_power.py')
put('sections/A_semidihedral_two_power.tex',s)
code=(root/'notes/fgh_A73_certificate.py').read_text().replace('unregistered A73 proof','registered A73 proof').replace('A.73, unregistered','A.73, registered after full audits')
put('code/a_semidihedral_two_power.py',code)
with (root/'code/a_semidihedral_two_power.out').open('w') as f:
    subprocess.run([sys.executable,str(root/'code/a_semidihedral_two_power.py')],stdout=f,stderr=subprocess.STDOUT,check=True)
changed+=['code/a_semidihedral_two_power.json','code/a_semidihedral_two_power.out']
old=json.loads((root/'notes/fgh_A73_certificate.json').read_text());new=json.loads((root/'code/a_semidihedral_two_power.json').read_text())
assert old['status']==new['status']=='PASS'
for x in (old,new):x.pop('candidate',None)
assert old==new
p=root/'sections/A.tex';s=p.read_text();needle='\\input{sections/A_quaternion_two_power.tex}'
assert s.count(needle)==1 and 'A_semidihedral_two_power.tex' not in s
put('sections/A.tex',s.replace(needle,needle+'\n\\input{sections/A_semidihedral_two_power.tex}'))
p=root/'sections/A_general_cover_frontier.tex';s=p.read_text()
needle='two-primary cusp divisors. Products of two nonabelian Sylow\nfactors and the universal question remain outside these conclusions.'
assert needle in s
replacement='''two-primary cusp divisors.
A.73 supplies the same complete result for every actual
semidihedral two-group closure and its intermediates. Here
the ordinary alternative would force one orbit of elliptic
components; rooting the reduction tree at the whole group's
invariant centre makes them equidistant. Actual fixed-point
lifting and disjoint unmarked child subtrees then contradict
the total genus. Products of two nonabelian Sylow factors and
the universal question remain outside these conclusions.'''
put('sections/A_general_cover_frontier.tex',s.replace(needle,replacement))
row=json.loads((root/'notes/fgh_A73_row.json').read_text())
row['notes']=row['notes'].replace('Unregistered candidate pending complete independent audits.',
    'Registered after full root and DE proof/source/exact-certificate audits PASS.')
put('notes/fgh_A73_row.json',json.dumps(row,indent=2)+'\n')
p=root/'notes/a_results.json';rows=json.loads(p.read_text());assert not any(x['id']=='A.73' for x in rows)
rows.append(row);put('notes/a_results.json',json.dumps(rows,indent=2)+'\n')
p=root/'notes/fgh_A73_sources.md';s=p.read_text();backup=root/'notes/fgh_A73_sources_before_registration.md'
if not backup.exists():backup.write_text(s);changed.append(str(backup.relative_to(root)))
s=s.replace('Status: unregistered notes candidate, pending full root and independent audits. Full proof notes/fgh_A73_draft.tex; exact executed support notes/fgh_A73_certificate.py/.json/.out. No canonical section or register has been changed for A73.',
    'Status: registered as A.73 after full root and DE proof/source/exact-certificate audits PASS. Canonical section sections/A_semidihedral_two_power.tex; canonical code code/a_semidihedral_two_power.py/.json/.out. The exact audited draft and original certificate remain preserved. Canonical edits change only status and certificate path; the rerun matches every mathematical JSON field.')
s=s.replace('with the exact corollary located separately.', 'with exact Corollary2.16 freshly read as turn1182view0, printed23/PDF22.')
put('notes/fgh_A73_sources.md',s)
for rel in changed:
    if rel.endswith('.tex'):
        b=(root/rel).read_bytes();s=b.decode()
        assert not any(x<32 and x not in(9,10) for x in b)
        assert s.count('\\[')==s.count('\\]')
record={'status':'REGISTERED; root and DE full audits PASS','id':'A.73',
    'candidate_preserved':'notes/fgh_A73_draft.tex','exact_rerun':'PASS, all mathematical JSON fields equal',
    'editorial_changes':['Registered status comment','Canonical certificate path','Certificate registration metadata'],
    'bibliography_changed':False,'global_assembly_changed':False,
    'changed_files':{rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in changed}}
put('notes/fgh_A73_integration.json',json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'id':'A.73','changed_files':len(changed)},indent=2))
