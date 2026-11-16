#!/usr/bin/env python3
"""Register the fully audited A64; requires explicit root approval."""
from pathlib import Path
import json
import shutil
import sys

r=Path(__file__).resolve().parents[1]
assert '--root-approved' in sys.argv
assert (r/'notes/root_A64_audit.md').exists()
assert (r/'notes/pbc_A64_audit.md').exists()
assert json.loads((r/'notes/fgh_A64_certificate.json').read_text())['status']=='PASS'
source=r/'notes/fgh_A64_draft.tex'
s=source.read_text().replace('Theorem V.3.1, pp.144--145','Theorem V.3.1, p.145')
source.write_text(s)
s=s.replace('% A.64 candidate; notes only, pending full independent audits.',
            '% A.64: root and PBC full proof/source/certificate audits PASS.')
s=s.replace(r'\begin{statement}{A.64}{Open}{Candidate: torsion enlargement outside the geometric closure order}',
            r'\begin{statement}{A.64}{Proved}{Torsion enlargement outside the geometric closure order}')
s=s.replace(r'\begin{proof}[Candidate proof, pending independent audits]',r'\begin{proof}')
s=s.replace('notes/fgh_A64_certificate.py','code/a_torsion_enlargement_closure.py')
(r/'sections/A_torsion_enlargement_closure.tex').write_text(s)
code=(r/'notes/fgh_A64_certificate.py').read_text().replace(
    "'statement':'A64 candidate, not registered'", "'statement':'A64, fully independently audited'")
(r/'code/a_torsion_enlargement_closure.py').write_text(code)
for suffix in ('.json','.out'):
    shutil.copyfile(r/('notes/fgh_A64_certificate'+suffix),r/('code/a_torsion_enlargement_closure'+suffix))
for src,dst in [('root_A64_certificate_rerun.out','a_torsion_enlargement_closure_root_rerun.out'),
                ('pbc_A64_independent_rerun.out','a_torsion_enlargement_closure_pbc_rerun.out')]:
    shutil.copyfile(r/'notes'/src,r/'code'/dst)
p=r/'sections/A.tex'; s=p.read_text()
anchor=r'\input{sections/A_heisenberg_ordinary_enlargements.tex}'
assert anchor in s and 'A_torsion_enlargement_closure.tex' not in s
p.write_text(s.replace(anchor,anchor+'\n'+r'\input{sections/A_torsion_enlargement_closure.tex}'))
row=json.loads((r/'notes/fgh_A64_row.json').read_text())
row.update(status='Proved',where_proved='sections/A_torsion_enlargement_closure.tex')
row['notes']=row['notes'].replace('Unregistered full candidate pending independent audits.',
    'Registered after full root and PBC proof/source/certificate audits PASS.')
(r/'notes/fgh_A64_row.json').write_text(json.dumps(row,indent=2)+'\n')
p=r/'notes/a_results.json'; rows=json.loads(p.read_text())
assert not any(z['id']=='A.64' for z in rows)
rows.append(row); p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'sections/A_general_cover_frontier.tex'; s=p.read_text()
anchor='The comparison to the smaller marked curve is an open immersion.'
assert anchor in s
addition=r'''
A.64 removes the congruence restriction in this enlargement conclusion:
every odd Heisenberg prime and every positive enlargement integer now
satisfy both assertions. More generally, if an enlargement integer has
a prime outside the original geometric closure order, the actual tame
good model at that prime gives rational cusp companions and full
fixed inertia at all coefficient primes, including that residue prime.
This includes residue two. It is still an enlargement of the removed
set on the same compactification, with no fixed-lift or cofinality claim.
'''
p.write_text(s.replace(anchor,anchor+'\n'+addition))
p=r/'notes/root_cover_frontier_results.json'; rows=json.loads(p.read_text())
for z in rows:
    if z['id']=='A.45':
        assert z['status']=='Open'
        if isinstance(z['depends_on'],str):z['depends_on']+='; A.64'
        elif 'A.64' not in z['depends_on']:z['depends_on'].append('A.64')
        z['notes']+=' A64 proves every odd Heisenberg isogeny enlargement for all m, and the general prime-outside-closure enlargement criterion, including residue2. This gives no finite refinement over the original map or fixed-element lifting. Universal TaskA5 remains Open.'
p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'notes/fgh_A64_sources.md'; s=p.read_text().replace(
    'Candidate `notes/fgh_A64_draft.tex` is notes-only, pending full independent audits.',
    'Registered after full root and PBC proof/source/certificate audits PASS; the original candidate is retained as provenance.')
s=s.replace('printed144–145 (PDF160–161)','printed145 (the theorem statement)')
s+='\nRoot primary page checks and exact rerun are in `notes/root_A64_audit.md`; the full PBC independent audit is in `notes/pbc_A64_audit.md`. Canonical proof and certificate are `sections/A_torsion_enlargement_closure.tex` and `code/a_torsion_enlargement_closure.py`.\n'
p.write_text(s)
(r/'notes/fgh_A64_audit.md').write_text('''# A64 registration and audit record

Registered after root and PBC full independent proof/source/certificate audits PASS. Detailed ledgers: notes/root_A64_audit.md and notes/pbc_A64_audit.md. The candidate, original certificate, source ledger and independent reruns remain retained.

Canonical proof: sections/A_torsion_enlargement_closure.tex. Exact certificate: code/a_torsion_enlargement_closure.py, with JSON/output and both independent reruns. The actual prime-to-residue tame extension, residue-two potential-good model, equal finite-flat torsion clusters, exact ramified source counts and inert pure-p-power rational fibre were checked independently. Silverman VII5.5's printed locator is corrected to197, its characteristic-two proof cross-reference to199, and V3.1 to145.

A45 remains Open. The general conclusion concerns further puncturing and a changed map to U; it does not give finite refinement over the original map, quotient fixed lifting, or cofinality.
''')
with (r/'notes/fgh.md').open('a') as f:
    f.write('\n\n## A.64: prime-outside-closure and all odd Heisenberg enlargements\n\nRegistered after root and PBC full audits and exact reruns PASS. An enlargement integer with a prime outside the actual closure order gives all-prime fixed inertia; the tame model includes residue2, and source cluster sizes are c or1+e(c−1). Combined with A63 and the separate inert pure-p-power O-fibre argument, every odd Heisenberg cover has both assertions for every isogeny enlargement. Universal TaskA5 remains Open; no finite-refinement, fixed-lift or cofinality claim is made.\n')
print('A64 integrated with full audited proof, canonical exact certificate, owner row and scoped Open frontier.')
