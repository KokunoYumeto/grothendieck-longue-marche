#!/usr/bin/env python3
"""Register A65 after full root and DE approval; preserves all candidates."""
from pathlib import Path
import json
import shutil
import sys

r=Path(__file__).resolve().parents[1]
assert '--root-approved' in sys.argv
assert (r/'notes/root_A65_certificate_rerun.out').exists()
assert (r/'notes/de_A65_audit.md').exists()
assert json.loads((r/'notes/fgh_A65_certificate.json').read_text())['status']=='PASS'
s=(r/'notes/fgh_A65_draft.tex').read_text()
s=s.replace('% A.65 candidate; notes only, pending independent proof/source/code audits.',
            '% A.65: root and DE full proof/source/certificate audits PASS.')
s=s.replace(r'\begin{statement}{A.65}{Open}{Candidate: all intermediate exponent-prime class-two covers}',
            r'\begin{statement}{A.65}{Proved}{All intermediate exponent-prime class-two covers}')
s=s.replace(r'\begin{proof}[Candidate proof, pending independent audits]',r'\begin{proof}')
s=s.replace('notes/fgh_A65_certificate.py','code/a_heisenberg_intermediates.py')
(r/'sections/A_heisenberg_intermediates.tex').write_text(s)
code=(r/'notes/fgh_A65_certificate.py').read_text().replace(
    "'statement':'A65 candidate, unregistered'", "'statement':'A65, fully independently audited'")
(r/'code/a_heisenberg_intermediates.py').write_text(code)
for suffix in ('.json','.out'):
    shutil.copyfile(r/('notes/fgh_A65_certificate'+suffix),r/('code/a_heisenberg_intermediates'+suffix))
for owner in ('root','de'):
    shutil.copyfile(r/f'notes/{owner}_A65_certificate_rerun.out',
                   r/f'code/a_heisenberg_intermediates_{owner}_rerun.out')
p=r/'sections/A.tex';s=p.read_text()
anchor=r'\input{sections/A_torsion_enlargement_closure.tex}'
assert anchor in s and 'A_heisenberg_intermediates.tex' not in s
p.write_text(s.replace(anchor,anchor+'\n'+r'\input{sections/A_heisenberg_intermediates.tex}'))
row=json.loads((r/'notes/fgh_A65_row.json').read_text())
row.update(status='Proved',where_proved='sections/A_heisenberg_intermediates.tex')
row['notes']=row['notes'].replace('Unregistered full candidate pending independent audits.',
    'Registered after full root and DE proof/source/certificate audits PASS.')
(r/'notes/fgh_A65_row.json').write_text(json.dumps(row,indent=2)+'\n')
p=r/'notes/a_results.json';rows=json.loads(p.read_text())
assert not any(z['id']=='A.65' for z in rows)
rows.append(row);p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'sections/A_general_cover_frontier.tex';s=p.read_text()
anchor='set on the same compactification, with no fixed-lift or cofinality claim.'
assert anchor in s
addition=r'''
A.65 also settles every intermediate of each odd Heisenberg cover,
equivalently every cover whose geometric closure has odd-prime exponent
and nilpotency class at most two. The noncentral order-prime quotients
are treated through their actual stable-model maps, rather than by
transferring fixedness through a surjective pro-prime quotient.
'''
p.write_text(s.replace(anchor,anchor+'\n'+addition))
p=r/'notes/root_cover_frontier_results.json';rows=json.loads(p.read_text())
for z in rows:
    if z['id']=='A.45':
        assert z['status']=='Open'
        if isinstance(z['depends_on'],str):z['depends_on']+='; A.65'
        elif 'A.65' not in z['depends_on']:z['depends_on'].append('A.65')
        z['notes']+=' A65 completes every intermediate cover of every odd exponent-p Heisenberg cover, equivalently every geometric closure of exponent p and class at most two. The noncentral quotient has degree p², genus1+p(p−1)/2 and p cusps. Its actual ordinary free quotient or inert component-domination argument proves rational cusp paths directly. Universal nilpotent fixedness and TaskA5 remain Open.'
p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'notes/fgh_refs.bib';s=p.read_text()
s=s.replace('freshly reopened for actual stable-model automorphisms and rational contractions in A.63}',
 'freshly reopened for actual stable-model automorphisms and rational contractions in A.63; Proposition 9.2.5 and Theorem 9.2.7, pages 396--397, Lemma 7.5.18(b), pages 312--313, and Remark 10.4.24, page 542, freshly reopened for the actual quotient-model domination and Picard graph rank in A.65}')
s=s.replace('The exact primary text was independently retrieved and checked by root as well}',
 'Theorem 1 and Corollary 2 on page 493 were freshly reopened for the actual quotient Jacobian in A.65. The exact primary text was independently retrieved and checked by root as well}')
p.write_text(s)
p=r/'notes/fgh_A65_sources.md';s=p.read_text().replace(
 'Unregistered full candidate at `notes/fgh_A65_draft.tex`;',
 'Registered after root and DE full independent proof/source/certificate audits PASS; original candidate at `notes/fgh_A65_draft.tex`;')
s+='\nCanonical proof: `sections/A_heisenberg_intermediates.tex`; canonical exact certificate: `code/a_heisenberg_intermediates.py`. Full DE audit: `notes/de_A65_audit.md`; root approval and fresh sources are recorded in the registration ledger, with its exact rerun retained.\n'
p.write_text(s)
(r/'notes/fgh_A65_audit.md').write_text('''# A65 registration and independent audit record

Registered after full root and DE proof/source/certificate audits PASS. DE's detailed ledger is notes/de_A65_audit.md. Root read the full337-line draft, inspected and independently reran the complete certificate, and explicitly approved integration. Root fresh primary references: Liu9.2.5/9.2.7 turn1038view1;7.5.18(b) turn1038view0;10.4.24 turn1035view1; Serre–TateTheorem1/Corollary2 turn1032view2; SilvermanV3.1 turn1030view0. The author source ledger and candidate remain retained.

Canonical proof: sections/A_heisenberg_intermediates.tex. Canonical certificate: code/a_heisenberg_intermediates.py, with original output and independent root/DE reruns. The finite certificate exhausts all subgroups at3/5 and checks subgroup classification, cores, cusp orbits, genus identities and ordinary place choices through13. The written proof separately establishes the actual ordinary free quotient and the inert positive-component domination, radicial main and rational O-fibre. No wild quotient/reduction commutation or pro-prime fixed-group transfer is assumed.

A45 remains Open: the new intrinsic scope is every cover with geometric closure of odd exponent p and class at most two, not every nilpotent cover and not a cofinal family.
''')
with (r/'notes/fgh.md').open('a') as f:
    f.write('\n\n## A.65: every intermediate odd Heisenberg cover\n\nRegistered after root and DE full proof/source/certificate audits PASS. All intermediate covers of H_p, for every odd p, have both all-prime cusp assertions. The new noncentral quotient has degree p², genus1+p(p−1)/2 and p cusps. The ordinary proof chooses a Gaussian place with nonzero reduced translation; the inert proof resolves the actual morphism and dominates every positive target component, forcing rational cusp paths over the unique main O-point. This covers all geometric closures of exponent p and class at most two. Universal TaskA5 remains Open.\n')
print('A65 integrated after root/DE full PASS, with canonical proof, exact certificate, owner row and scoped frontier.')
