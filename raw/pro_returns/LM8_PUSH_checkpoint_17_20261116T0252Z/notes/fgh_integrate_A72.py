#!/usr/bin/env python3
"""Authorized A72 integration after full root and DE audits."""
from pathlib import Path
import hashlib,json,subprocess,sys

root=Path(__file__).resolve().parents[1]
changed=[]
def put(rel,s):
    (root/rel).write_text(s);changed.append(rel)
draft=root/'notes/fgh_A72_draft.tex'
assert hashlib.sha256(draft.read_bytes()).hexdigest()=='9cc005920ae12725c780277742fa25c9000e03004e8c1930dc7a3dfc1d9d0226'
text=draft.read_text().replace('% A.72 candidate: notes only, awaiting full independent audits.',
    '% A.72: full root and DE proof/source/exact-certificate audits PASS.')
text=text.replace('notes/fgh_A72_certificate.py','code/a_quaternion_two_power.py')
put('sections/A_quaternion_two_power.tex',text)
code=(root/'notes/fgh_A72_certificate.py').read_text().replace('A.72, unregistered','A.72, registered after full audits')
put('code/a_quaternion_two_power.py',code)
with (root/'code/a_quaternion_two_power.out').open('w') as f:
    subprocess.run([sys.executable,str(root/'code/a_quaternion_two_power.py')],stdout=f,stderr=subprocess.STDOUT,check=True)
changed+=['code/a_quaternion_two_power.json','code/a_quaternion_two_power.out']
old=json.loads((root/'notes/fgh_A72_certificate.json').read_text());new=json.loads((root/'code/a_quaternion_two_power.json').read_text())
assert old['status']==new['status']=='PASS'
for x in (old,new):x.pop('candidate',None)
assert old==new

p=root/'sections/A.tex';s=p.read_text();needle='\\input{sections/A_dihedral_abelian_products.tex}'
assert s.count(needle)==1 and 'A_quaternion_two_power.tex' not in s
put('sections/A.tex',s.replace(needle,needle+'\n\\input{sections/A_quaternion_two_power.tex}'))

p=root/'sections/A_general_cover_frontier.tex';s=p.read_text()
needle='Jacobian is needed. Products of two nonabelian Sylow factors\nand the universal question remain outside these conclusions.'
assert needle in s
replacement='''Jacobian is needed.
A.72 settles every actual generalized-quaternion two-group
closure and every intermediate. Its central quotient is one
of the classified dihedral covers. A primitive cyclotomic
anti-invariant factor could only have rank zero or be ordinary;
the ordinary case would force a component orbit twice as large
as its total genus, using the quaternion group's unique
involution and the ordinary fourth-root obstruction. The
actual elliptic abelianization quotient gives the required
two-primary cusp divisors. Products of two nonabelian Sylow
factors and the universal question remain outside these conclusions.'''
put('sections/A_general_cover_frontier.tex',s.replace(needle,replacement))

row=json.loads((root/'notes/fgh_A72_row.json').read_text())
row['notes']=row['notes'].replace('Unregistered candidate awaiting full independent audits.',
    'Registered after full root and DE proof/source/exact-certificate audits PASS.')
row['notes']=row['notes'].replace('Unregistered candidate pending full independent audits.',
    'Registered after full root and DE proof/source/exact-certificate audits PASS.')
put('notes/fgh_A72_row.json',json.dumps(row,indent=2)+'\n')
p=root/'notes/a_results.json';rows=json.loads(p.read_text());assert not any(x['id']=='A.72' for x in rows)
rows.append(row);put('notes/a_results.json',json.dumps(rows,indent=2)+'\n')

p=root/'notes/fgh_A72_sources.md';s=p.read_text()
backup=root/'notes/fgh_A72_sources_before_registration.md'
if not backup.exists():backup.write_text(s);changed.append(str(backup.relative_to(root)))
s=s.replace('Status: unregistered candidate, pending complete independent audits. Full proof is notes/fgh_A72_draft.tex. Only notes/code files have been written during the canonical checkpoint freeze.',
    'Status: registered as A.72 after full root and DE proof/source/exact-certificate audits PASS. Canonical section sections/A_quaternion_two_power.tex; canonical code code/a_quaternion_two_power.py/.json/.out. Original candidate and its exact outputs remain preserved. Canonical edits change only status and certificate path. The parent independently reran the complete original certificate with byte equality; the canonical rerun again matches every mathematical JSON field.')
s=s.replace('A70 (fully root/DE audited notes candidate, awaiting integration)', 'A70 (registered after full root/DE audits)')
put('notes/fgh_A72_sources.md',s)
for rel in changed:
    if rel.endswith('.tex'):
        b=(root/rel).read_bytes();s=b.decode()
        assert not any(x<32 and x not in(9,10) for x in b)
        assert s.count('\\[')==s.count('\\]')
record={'status':'REGISTERED; root and DE full audits PASS','id':'A.72',
    'candidate_preserved':'notes/fgh_A72_draft.tex','exact_rerun':'PASS, all mathematical JSON fields equal',
    'editorial_changes':['Registered status comment','Canonical certificate path','Certificate registration metadata'],
    'bibliography_changed':False,'global_assembly_changed':False,
    'changed_files':{rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in changed}}
put('notes/fgh_A72_integration.json',json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'id':'A.72','changed_files':len(changed)},indent=2))
