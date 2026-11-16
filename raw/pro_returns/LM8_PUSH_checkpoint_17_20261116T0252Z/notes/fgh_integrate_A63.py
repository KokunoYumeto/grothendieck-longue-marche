#!/usr/bin/env python3
"""Register A63 only after complete root and DE approval."""
from pathlib import Path
import json
import shutil
import sys

r=Path(__file__).resolve().parents[1]
assert '--root-approved' in sys.argv
assert (r/'notes/root_A63_audit.md').exists()
assert (r/'notes/de_A63_audit.md').exists()
assert json.loads((r/'notes/fgh_A63_certificate.json').read_text())['status']=='PASS'
s=(r/'notes/fgh_A63_draft.tex').read_text()
assert 'p,quad' not in s and 'fghLiu2002' not in s
s=s.replace('% A.63 candidate; notes only, pending independent full audits.',
            '% A.63: full independent root and DE proof/source/certificate audits PASS.')
s=s.replace(r'\begin{statement}{A.63}{Open}{Candidate: all ordinary Heisenberg enlargements have cusp fixed groups and normalizers}',
            r'\begin{statement}{A.63}{Proved}{All ordinary Heisenberg enlargements have cusp fixed groups and normalizers}')
s=s.replace('The candidate proves both assertions of Task A.5 for every',
            'Both assertions of Task A.5 hold for every')
s=s.replace(r'\begin{proof}[Candidate proof, pending independent audits]',r'\begin{proof}')
s=s.replace('notes/fgh_A63_certificate.py','code/a_heisenberg_ordinary_enlargements.py')
(r/'sections/A_heisenberg_ordinary_enlargements.tex').write_text(s)
code=(r/'notes/fgh_A63_certificate.py').read_text().replace(
    "'candidate':'A63, unregistered notes-only'", "'statement':'A63, fully independently audited'")
(r/'code/a_heisenberg_ordinary_enlargements.py').write_text(code)
for suffix in ('.json','.out'):
    shutil.copyfile(r/('notes/fgh_A63_certificate'+suffix),
                    r/('code/a_heisenberg_ordinary_enlargements'+suffix))
for owner in ('root','de'):
    shutil.copyfile(r/f'notes/{owner}_A63_certificate_rerun.out',
                    r/f'code/a_heisenberg_ordinary_enlargements_{owner}_rerun.out')
p=r/'sections/A.tex'; s=p.read_text()
anchor=r'\input{sections/A_heisenberg_ordinary.tex}'
assert anchor in s and 'A_heisenberg_ordinary_enlargements.tex' not in s
p.write_text(s.replace(anchor,anchor+'\n'+r'\input{sections/A_heisenberg_ordinary_enlargements.tex}'))
row=json.loads((r/'notes/fgh_A63_row.json').read_text())
row.update(status='Proved',where_proved='sections/A_heisenberg_ordinary_enlargements.tex')
row['notes']=('Registered after full root and DE proof/source/certificate audits PASS. '
 'For every p=1 mod4 and m≥1, the actual degree p³m² cover has cusp count p³m²−p³+p². '
 'Connected order-p torsion translates are deeper than each actual AS tail radius. The order-p² '
 'preimage Gc fixes reduced U, so the faithful central AS translation leaves a noncentral order-p '
 'kernel acting identically on that tail. Every mark has a free orbit with identical specialization; '
 'main and rational component actions and node contraction fibres are also proved. A42 gives all-prime '
 'fixed inertia for all packets; A11 transfers normalizer recognition across the actual open immersion. '
 'An exact p41 critical point of order13 is retained as a barrier to an invalid torsion-avoidance proof. '
 'No cofinality or universal-cover conclusion.')
(r/'notes/fgh_A63_row.json').write_text(json.dumps(row,indent=2)+'\n')
p=r/'notes/a_results.json'; rows=json.loads(p.read_text())
assert not any(z['id']=='A.63' for z in rows)
rows.append(row); p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'sections/A_general_cover_frontier.tex'; s=p.read_text()
anchor='This remains a particular unbounded family of geometric subgroups.'
assert anchor in s
addition='''
A.63 further proves both assertions for every isogeny enlargement
\(C_p\setminus q_p^{-1}(E[pm])\) when \(p\equiv1\pmod4\),
for every \(m\ge1\). An actual noncentral deck subgroup fixes
each relevant special component and supplies a rational companion
for every cusp, including those whose images meet a positive-genus
tail. The comparison to the smaller marked curve is an open immersion.
'''
p.write_text(s.replace(anchor,anchor+'\n'+addition))
p=r/'notes/root_cover_frontier_results.json'; rows=json.loads(p.read_text())
for z in rows:
    if z['id']=='A.45':
        if isinstance(z['depends_on'],str):z['depends_on']+='; A.63'
        elif 'A.63' not in z['depends_on']:z['depends_on'].append('A.63')
        z['notes']+=' A63 proves all-m isogeny enlargements of every ordinary-prime Heisenberg cover, with actual noncentral component kernels supplying rational cusp companions. The universal question remains Open.'
p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'notes/fgh_refs.bib'; s=p.read_text()
s=s.replace('Proposition 10.1.21(a), printed pages 462--463, reopened for good reduction outside finitely many places in A.53}',
 'Proposition 10.1.21(a), printed pages 462--463, reopened for good reduction outside finitely many places in A.53; Proposition 10.1.16, printed pages 460--461, and Theorem 10.3.34(b), printed pages 518--519, freshly reopened for actual stable-model automorphisms and rational contractions in A.63}')
s=s.replace('Exercise V.5.7; Theorems III.6.1',
 'Corollary IV.4.4, printed page 126, and Theorem IV.7.4, printed page 134, freshly reopened for the exact connected torsion displacement in A.63; Exercise V.5.7; Theorems III.6.1')
p.write_text(s)
(r/'notes/fgh_A63_audit.md').write_text('''# A63 registration and audit record

Registered after full independent root and DE proof, source and executed-certificate audits PASS. Detailed ledgers are notes/root_A63_audit.md and notes/de_A63_audit.md. The candidate, exact source ledger and original certificate remain retained. The only change requested by the auditors was the missing backslash in a spacing command; it was fixed before integration.

Canonical proof: sections/A_heisenberg_ordinary_enlargements.tex. Canonical exact certificate: code/a_heisenberg_ordinary_enlargements.py, with outputs and both independent reruns. It imports the preserved canonical division-polynomial implementation. The actual connected-torsion displacement, residual AS kernel, generic point stabilizers, rational-component pointwise action and marked contraction-fibre comparison were independently checked. The normalizer argument uses the actual open immersion and A11, while fixedness uses A42 directly.

A45 remains Open. No finite-refinement, fixed-lift or cofinality assertion was added.
''')
with (r/'notes/fgh.md').open('a') as f:
    f.write('\n\n## A.63: all ordinary Heisenberg isogeny enlargements\n\nRegistered after root and DE full audits and exact reruns PASS. Every p=1 mod4 and every m≥1 has both all-prime assertions for the actual degree p³m² enlargement. Connected torsion translates fix reduced tail U; the noncentral kernel of the residual AS action supplies a free cusp orbit with identical specialization on each tail. Main/rational components and node fibres are handled explicitly. A42 gives fixed inertia; A11 transfers normalizers through the actual open immersion. Odd critical torsion is allowed and an exact order13 example at residue41 is retained. Universal TaskA5 remains Open.\n')
print('A63 registered with full proof, exact certificate, source/audit records and scoped frontier update.')
