#!/usr/bin/env python3
"""Register A67 only after explicit root and secondary full approval."""
from pathlib import Path
import json
import shutil
import sys

r = Path(__file__).resolve().parents[1]
assert '--root-approved' in sys.argv
assert (r/'notes/root_A67_audit.md').exists()
assert (r/'notes/de_A67_audit.md').exists()
assert json.loads((r/'notes/fgh_A67_certificate.json').read_text())['status'] == 'PASS'
name = 'A_tetrahedral_covers'
code = 'a_tetrahedral_covers'
s = (r/'notes/fgh_A67_draft.tex').read_text()
s = s.replace('% A.67 candidate: notes only, pending independent full audits.',
              '% A.67: complete root and DE independent proof/source/certificate audits PASS.')
s = s.replace('notes/fgh_A67_certificate.py', f'code/{code}.py')
(r/f'sections/{name}.tex').write_text(s)
for suffix in ('.py','.json','.out'):
    shutil.copyfile(r/('notes/fgh_A67_certificate'+suffix),r/('code/'+code+suffix))
for owner in ('root','de'):
    p = r/f'notes/{owner}_A67_certificate_rerun.out'
    if p.exists():
        shutil.copyfile(p,r/f'code/{code}_{owner}_rerun.out')
p = r/'sections/A.tex'
s = p.read_text()
anchor = r'\input{sections/A_heisenberg_abelian_products.tex}'
assert s.count(anchor)==1 and f'{name}.tex' not in s
p.write_text(s.replace(anchor,anchor+'\n'+rf'\input{{sections/{name}.tex}}'))
row = json.loads((r/'notes/fgh_A67_row.json').read_text())
row['where_proved'] = f'sections/{name}.tex'
row['notes'] = row['notes'].replace(
    'Complete notes-only candidate; not registered pending full independent audits.',
    'Registered after complete root and DE independent proof/source/executed-certificate audits PASS.')
(r/'notes/fgh_A67_row.json').write_text(json.dumps(row,indent=2)+'\n')
p = r/'notes/a_results.json'
rows = json.loads(p.read_text())
assert not any(x['id']=='A.67' for x in rows)
rows.append(row)
p.write_text(json.dumps(rows,indent=2)+'\n')
p = r/'sections/A_general_cover_frontier.tex'
s = p.read_text()
anchor = 'argument; no general nilpotent fixed-group assertion follows.'
assert s.count(anchor)==1
addition = r'''
A.67 supplies a non-nilpotent family: every tetrahedral
\(A_4\) closure and every intermediate has both assertions at
all coefficient primes. The actual three-adic model has a
rational six-cusp centre and four supersingular elliptic
tails. An explicit residue-field argument treats the wild
order-three quotient and its rational two-cusp centre.
This does not extend automatically to coprime elliptic-isogeny
pullbacks: their three-adic dual graph can have cycles.
'''
p.write_text(s.replace(anchor,anchor+'\n'+addition))
p = r/'notes/root_cover_frontier_results.json'
rows = json.loads(p.read_text())
for x in rows:
    if x['id']=='A.45':
        assert x['status']=='Open'
        if isinstance(x['depends_on'],list):
            if 'A.67' not in x['depends_on']:x['depends_on'].append('A.67')
        else:x['depends_on'] += '; A.67'
        x['notes'] += ' A67 adds every tetrahedral A4 closure and intermediate, using actual degree3 isogenies, a rational marked centre at3, an explicit wild C3 quotient, and the complementary elliptic factor at2. This is a non-nilpotent family, not the universal result.'
p.write_text(json.dumps(rows,indent=2)+'\n')
p = r/'notes/fgh_A67_sources.md'
s = p.read_text().replace(
    'Status: complete notes-only candidate, not registered.',
    'Status: registered after full root and DE proof/source/executed-certificate audits PASS.')
s = s.replace('Root and DE full independent audits requested.',
              'Complete independent audit ledgers: notes/root_A67_audit.md and notes/de_A67_audit.md.')
s += f'\nCanonical proof: sections/{name}.tex. Canonical exact certificate: code/{code}.py/.json/.out. The original candidate and outputs remain intact.\n'
p.write_text(s)
p = r/'notes/fgh_A67_audit.md'
s = p.read_text().replace(
    'Status: full author audit PASS; candidate remains unregistered pending independent root and DE audits.',
    'Status: registered after full author, root and DE independent proof/source/executed-certificate audits PASS and explicit root authorization.')
s = s.replace('No canonical source, register, CSV, PDF, or frontier was modified by this candidate.',
              'The approved integration adds one canonical section and one owner row, preserving the original candidate. A45 remains Open. Root owns assembled CSV/PDF updates.')
s += '\nIndependent ledgers: notes/root_A67_audit.md and notes/de_A67_audit.md. Exact independent reruns are retained alongside the canonical certificate when available.\n'
p.write_text(s)
with (r/'notes/fgh.md').open('a') as f:
    f.write('\n\n## A.67: every tetrahedral closure and intermediate\n\nRegistered after full root and DE proof/source/certificate PASS. Actual degree3 isogeny coordinates and a V4 Kummer extension identify every A4 closure via the unique standard F2[C3] cohomology summand. Residue3 gives a rational marked centre with four supersingular elliptic tails; the wild C3 quotient is treated through exact residue fields and genus exhaustion. The complementary elliptic factor has j=4608±2688sqrt3 and supplies the coefficient2 normalizer input. Both assertions hold at all primes. The separate K_{4,h} isogeny-pullback barrier and the universal TaskA5 remain explicit.\n')
print('A67 integrated after complete root/DE approval; A45 remains Open.')
