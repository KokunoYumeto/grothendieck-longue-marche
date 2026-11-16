#!/usr/bin/env python3
"""Authorized A70/A71 owner-only integration after checkpoint14 release."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
changed = []

def put(rel, text):
    path = root/rel
    path.write_text(text)
    changed.append(rel)

draft70 = root/'notes/fgh_A70_draft.tex'
draft71 = root/'notes/fgh_dihedral_abelian_extension_draft.tex'
assert hashlib.sha256(draft70.read_bytes()).hexdigest() == 'f2d08a2d643dd99378f354ed798361fefd91f06e5c4413e9f69d8314d4b88f3d'
assert hashlib.sha256(draft71.read_bytes()).hexdigest() == 'e1eb0ad55f805e94e77d70b10e2eed8823edaf73f5acae4683e9bd6aaa5c45ae'

text70 = draft70.read_text().replace(
    '% A.70 candidate: notes only, unregistered during checkpoint freeze.',
    '% A.70: full root and DE proof/source/exact-certificate audits PASS.')
text70 = text70.replace('notes/fgh_A70_certificate.py', 'code/a_all_dihedral_two_power.py')
put('sections/A_all_dihedral_two_power.tex', text70)

text71 = draft71.read_text().replace(
    '% Unregistered candidate, notes only during the checkpoint14 freeze.',
    '% A.71: full root, DE and PBC proof/source audits PASS; exact certificate rerun PASS.')
text71 = text71.replace(
    '\\paragraph{Candidate conclusion.}\nAssuming the separately written and audited A.70, both all-prime',
    '\\begin{statement}{A.71}{Proved}{Dihedral two-power closures with an odd abelian factor}\nBoth all-prime')
text71 = text71.replace(
    'product with a second nonabelian Sylow factor.\n\n\\begin{proof}',
    'product with a second nonabelian Sylow factor. The universal\nquestion A.45 remains open.\n\\end{statement}\n\n\\begin{proof}')
text71 = text71.replace('This completes the candidate deduction.',
    'The exact subgroup and curve-degree support is retained in\n\\path{code/a_dihedral_abelian_products.py}.')
assert text71.count('\\begin{statement}{A.71}') == 1
put('sections/A_dihedral_abelian_products.tex', text71)

code_rows = [
    ('notes/fgh_A70_certificate.py', 'code/a_all_dihedral_two_power.py',
     'A.70, unregistered', 'A.70, registered after full audits',
     'notes/fgh_A70_certificate.json'),
    ('notes/fgh_dihedral_abelian_extension_certificate.py', 'code/a_dihedral_abelian_products.py',
     'Dihedral two-power times odd abelian, unregistered', 'A.71, registered after full audits',
     'notes/fgh_dihedral_abelian_extension_certificate.json')]
checks = []
for src, dst, old_status, new_status, old_json in code_rows:
    code = (root/src).read_text().replace(old_status, new_status)
    code = code.replace('for the notes-only A70.', 'for the registered A70.')
    code = code.replace('for the unregistered extension.', 'for the registered A71.')
    put(dst, code)
    output = (root/dst).with_suffix('.out')
    with output.open('w') as fh:
        subprocess.run([sys.executable, str(root/dst)], stdout=fh, stderr=subprocess.STDOUT, check=True)
    result_path = (root/dst).with_suffix('.json')
    original = json.loads((root/old_json).read_text())
    result = json.loads(result_path.read_text())
    assert original['status'] == result['status'] == 'PASS'
    for obj in (original, result):
        obj.pop('candidate', None)
    assert original == result
    changed += [str(output.relative_to(root)), str(result_path.relative_to(root))]
    checks.append({'canonical_code': dst, 'status': 'PASS', 'all_mathematical_JSON_fields_equal': True})

a_path = root/'sections/A.tex'
a = a_path.read_text()
assert 'A_all_dihedral_two_power.tex' not in a
needle = '\\input{sections/A_dihedral_two_power_fixed.tex}'
assert a.count(needle) == 1
a = a.replace(needle, needle+'\n\\input{sections/A_all_dihedral_two_power.tex}\n\\input{sections/A_dihedral_abelian_products.tex}')
put('sections/A.tex', a)

frontier = root/'sections/A_general_cover_frontier.tex'
f = frontier.read_text()
old = '''rooted marked tree. This proves the displayed uniform family;
a classification of all possible dihedral closures is not asserted.'''
new = '''rooted marked tree.
A.70 now classifies every actual two-power dihedral closure of
the fixed elliptic base and proves both assertions for all its
intermediates. The three characteristic rotation quotients are
realized by explicit elliptic two-isogenies with distinct dual
kernels; the order-four abelian case is treated separately.
A.71 permits an additional odd-order abelian factor, with every
actual intermediate included. The connected elliptic-isogeny
pullback has a separately proved compact-type model, and its
rational cusp paths lift as literal copies of the original
marked subtree. No special two-rank assertion for the enlarged
Jacobian is needed. Products of two nonabelian Sylow factors
and the universal question remain outside these conclusions.'''
assert old in f
put('sections/A_general_cover_frontier.tex', f.replace(old, new))

row70 = json.loads((root/'notes/fgh_A70_row.json').read_text())
row70['notes'] = ('Registered after full root and DE proof/source/exact-certificate audits PASS. '
    'Three Aut(D2m) generating-pair orbits for m>=4 are distinguished by their characteristic rotation quotient. '
    'Actual models with (a,b)=(0,-1),(6,1),(-6,1) realize the three fixed-base elliptic2-isogenies with distinct dual kernels. '
    'V4 is treated separately. A44 and A69, with actual norm and Frattini cusp descent, settle every intermediate. '
    'Finite field definition is required only for curves/maps/subgroups/marks; geometric paths are used up to inner conjugacy. '
    'No arbitrary nilpotent or universal A5 conclusion is made.')
row71 = {'id':'A.71','statement':'Both all-prime cusp assertions for every dihedral two-power times odd-abelian geometric closure',
    'status':'Proved','where_proved':'sections/A_dihedral_abelian_products.tex',
    'depends_on':['A.40','A.41','A.42','A.44','A.59','A.69','A.70'],'answers':['Task A.5'],
    'notes':('Registered after full root, DE and PBC proof/source audits PASS and exact certificate rerun PASS. '
        'Coprime subgroup splitting identifies every actual intermediate with a connected odd elliptic-isogeny pullback '
        'of a dihedral intermediate. The extended compact-type Abel map supplies the actual semistable map. '
        'The total nilpotent closure separately supplies potential good Jacobian and a tree, avoiding the false claim '
        'that an etale pullback always preserves compact type. Every rational cusp-joining subtree maps constantly '
        'to O and lifts as literal disjoint copies, with a distinct companion on the selected copy. '
        'A42 supplies full fixed inertia and A59 normalizers, without any new p-rank-zero assertion. '
        'Products of two nonabelian Sylows and the universal A5 statement remain Open.')}
rows_path = root/'notes/a_results.json'
rows = json.loads(rows_path.read_text())
assert not any(r['id'] in ('A.70','A.71') for r in rows)
rows.extend([row70,row71])
put('notes/a_results.json', json.dumps(rows,indent=2)+'\n')
put('notes/fgh_A70_row.json', json.dumps(row70,indent=2)+'\n')
put('notes/fgh_A71_row.json', json.dumps(row71,indent=2)+'\n')

for name, title, addition in [
    ('notes/fgh_A70_sources.md', '# A70 source and proof ledger — registered',
     'Registered as A.70 after full root and DE proof/source/exact-certificate audits PASS. Canonical section sections/A_all_dihedral_two_power.tex; code code/a_all_dihedral_two_power.py/.json/.out. Original audited draft and code remain preserved. The misleading automorphism-check comment was corrected before canonical copying, without changing executable mathematics; notes/fgh_A70_comment_precision.json records both hashes.'),
    ('notes/fgh_dihedral_abelian_extension_sources.md', '# A71 dihedral times odd-abelian source and scope ledger — registered',
     'Registered as A.71 after full root, DE and PBC proof/source audits PASS. Canonical section sections/A_dihedral_abelian_products.tex; code code/a_dihedral_abelian_products.py/.json/.out. The exact unnumbered candidate remains unchanged. Canonical edits only add the numbered Proved statement, remove conditional/candidate wording after A70 registration, and add the canonical certificate path.')]:
    path=root/name
    old_text=path.read_text()
    # Preserve the complete historical ledger before changing its current status.
    backup=path.with_name(path.stem+'_before_A70_A71_registration'+path.suffix)
    if not backup.exists():
        backup.write_text(old_text)
        changed.append(str(backup.relative_to(root)))
    body=old_text.split('\n',1)[1]
    put(name, title+'\n\n'+addition+'\n\n## Historical source ledger (preserved scope)\n'+body)

for rel in changed:
    if rel.endswith('.tex'):
        raw=(root/rel).read_bytes()
        assert not any(x < 32 and x not in (9,10) for x in raw), rel
        txt=raw.decode()
        assert txt.count('\\[') == txt.count('\\]'), rel

record = {'status':'REGISTERED, full audits PASS',
    'authorization':'Parent release and explicit integration authorization after checkpoint14 saved00:01:37UTC.',
    'statements':['A.70','A.71'], 'exact_reruns':checks,
    'audited_candidates_preserved':[str(draft70.relative_to(root)),str(draft71.relative_to(root)),
        'notes/fgh_A70_certificate_before_comment_precision.py'],
    'editorial_changes':['Registered status comments','A71 numbered statement wrapper; removed already-satisfied A70 conditional','Canonical code paths','Certificate registration metadata','A70 nonexecuted comment accuracy','A45 proved scope advanced, universal Open retained'],
    'bibliography_changed':False,'global_assembly_changed':False,
    'changed_files':{rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in changed}}
put('notes/fgh_A70_A71_integration.json',json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'statements':record['statements'],'changed_files':len(changed),'exact_reruns':checks},indent=2))
