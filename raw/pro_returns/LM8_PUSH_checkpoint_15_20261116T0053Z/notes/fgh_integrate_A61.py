#!/usr/bin/env python3
"""Integrate the complete A61 proof after root/DE/PBC approval."""
from pathlib import Path
import json
import shutil
import sys

r = Path(__file__).resolve().parents[1]
assert '--audits-passed' in sys.argv
assert 'A.61' in (r/'notes/root_A61_D75_audit.md').read_text()
assert (r/'notes/de_A61_audit.md').exists()
assert (r/'notes/pbc_A61_audit.md').exists()
assert json.loads((r/'notes/fgh_A61_certificate.json').read_text())['status'] == 'PASS'
s = (r/'notes/fgh_A61_draft.tex').read_text()
s = s.replace('% A.61 candidate. Unregistered pending full independent audits.',
              '% A.61: root, DE and PBC full independent proof/source/certificate audits PASS.')
s = s.replace('all nontrivial\narithmetically normalized procyclic subgroups are',
              'all nontrivial\narithmetically normalized pro-\\(\\ell\\) cyclic subgroups are')
s = s.replace(r''' \overline h(P+t)-\overline h(P)
       =\frac{R(P+t)^{p+1}}a
          +(S(P+t)-S(P))^p,
 \qquad \operatorname{ord}_P(\overline h-\overline h(P))=p+1.''',
              r''' \begin{aligned}
 \overline h(P+t)-\overline h(P)
       &=\frac{R(P+t)^{p+1}}a+(S(P+t)-S(P))^p,\\
 \operatorname{ord}_P(\overline h-\overline h(P))&=p+1.
 \end{aligned}''')
s = s.replace('The accompanying exact program checks the',
              'The exact program \\texttt{code/a_heisenberg_inert.py}\nchecks the')
(r/'sections/A_heisenberg_inert.tex').write_text(s)
for suffix in ('.py', '.json', '.out'):
    shutil.copyfile(r/('notes/fgh_A61_certificate'+suffix),
                    r/('code/a_heisenberg_inert'+suffix))
shutil.copyfile(r/'notes/de_A61_rerun.out',r/'code/a_heisenberg_inert_de_rerun.out')
shutil.copyfile(r/'notes/pbc_A61_independent_rerun.json',r/'code/a_heisenberg_inert_pbc_rerun.json')
p = r/'sections/A.tex'
s = p.read_text()
anchor = r'\input{sections/A_heisenberg_seven.tex}'
assert anchor in s and 'A_heisenberg_inert.tex' not in s
p.write_text(s.replace(anchor,anchor+'\n'+r'\input{sections/A_heisenberg_inert.tex}'))
row = json.loads((r/'notes/fgh_A61_row.json').read_text())
row['where_proved'] = 'sections/A_heisenberg_inert.tex'
row['notes'] = ('Registered after complete independent root, DE and PBC proof/source audits and exact reruns PASS. '
 'The proof is uniform for every p congruent to3 modulo4. The divided operator E=D^p/p modp identifies '
 'the actual derivative Dh=R^p with DR=a in F_p^times, and Frobenius roots A,S satisfy DS=RA/a. '
 'This kills every hidden degree-p Taylor term. Actual smooth main and tail charts yield one supersingular '
 'elliptic component and p genus-p(p-1)/2 Artin--Schreier tails. The genus sum forces compact type. '
 'All p^2 cusps lie on a rational marked tree overO. A41--42 give full fixed inertia for every coefficient '
 'prime and packet; A59 gives all normalizers using the actual exponent-p Heisenberg deck group. '
 'Certificates at p=3,7,11,19 support the uniform proof and do not replace it. Universal TaskA.5 remains Open; '
 'no cofinality or general nilpotent fixed-group theorem is asserted.')
(r/'notes/fgh_A61_row.json').write_text(json.dumps(row,indent=2)+'\n')
p = r/'notes/a_results.json'
rows = json.loads(p.read_text())
assert not any(z['id'] == 'A.61' for z in rows)
rows.append(row)
p.write_text(json.dumps(rows,indent=2)+'\n')
p = r/'sections/A_general_cover_frontier.tex'
s = p.read_text()
old = '''from those tails. This exact calculation is not an assertion
about every higher Heisenberg cover or every nilpotent cover.'''
new = '''from those tails. A.61 extends both conclusions uniformly to
every inert-prime Heisenberg cover
\\(z^p=\\psi_p(x)\\), \\(p\\equiv3\\pmod4\\), of degree
\\(p^3\\), genus \\(1+p^2(p-1)/2\\), and \\(p^2\\) cusps.
Its divided differential operator proves the local coefficient
identity for all such primes, and the exact charts give one
supersingular elliptic main component and \\(p\\) tails of genus
\\(p(p-1)/2\\). This is an unbounded family, with no cofinality
claim and no fixed-group assertion for every nilpotent cover.'''
assert old in s
p.write_text(s.replace(old,new))
p = r/'notes/root_cover_frontier_results.json'
rows = json.loads(p.read_text())
for z in rows:
    if z['id'] == 'A.45':
        if isinstance(z['depends_on'],str):
            z['depends_on'] += '; A.61'
        else:
            z['depends_on'].append('A.61')
        z['notes'] += (' A.61 uniformly completes both all-prime assertions for every inert-prime '
                       'Heisenberg cover of degreep^3 and genus1+p^2(p-1)/2. A divided differential '
                       'operator proves the missing local coefficient identity; actual charts and '
                       'genus exhaustion give the rational marked-tree hypothesis. This unbounded '
                       'family is not claimed cofinal and does not settle all nilpotent fixed groups.')
p.write_text(json.dumps(rows,indent=2)+'\n')
p = r/'notes/fgh_refs.bib'
s = p.read_text()
old = 'freshly reopened for A.59--A.60; Exercise V.5.7;'
assert old in s
s = s.replace(old,'freshly reopened for A.59--A.61; Theorem V.2.3.1(b), printed page 142, reopened for the actual Frobenius endomorphism identity in A.61; Exercise V.5.7;')
p.write_text(s)
(r/'notes/fgh_A61_audit.md').write_text('''# A61 integration and audit record

Registered after complete independent root, DE and PBC proof/source/certificate audits, all PASS. Detailed records are `notes/root_A61_D75_audit.md`, `notes/de_A61_audit.md`, and `notes/pbc_A61_audit.md`. The original full candidate, source ledger, exact certificate and all independent reruns remain available.

Canonical proof: `sections/A_heisenberg_inert.tex`. Canonical certificate: `code/a_heisenberg_inert.py`, with output, JSON, DE rerun output and independently produced PBC JSON. The theorem is uniform in every prime p congruent to3 modulo4; computations at3,7,11,19 check the formulas but are not substituted for the argument.

The new mathematical step is the integral divided operator and the identities E(h)=−R and DS=RA/a, with every function and scalar over F_p. All reviewers checked the multinomial coefficients, exact differential identity, pole bounds, hidden Taylor term, unramified lifts, actual local charts, stable-component persistence and cusp geometry. The actual central deck extension and its exponent-p argument were also checked. The two fixed/normalizer criteria are applied only after these actual hypotheses are established.

At integration the long Taylor display was split into two aligned lines and the statement explicitly says pro-ell cyclic subgroups. These are presentation clarifications only. A45 remains Open and explicitly denies cofinality and a general nilpotent fixed-group conclusion.
''')
with (r/'notes/fgh.md').open('a') as out:
    out.write('''\n\n## A.61: uniform inert-prime Heisenberg family

Registered after complete independent root, DE and PBC audits and exact reruns PASS. For every prime p congruent to3 modulo4, the actual degreep^3 exponent-p Heisenberg cover has genus1+p^2(p−1)/2 and p^2 cusps. The uniform divided-operator argument identifies the actual critical function and kills the invisible degree-p Taylor coefficient. Explicit charts give one supersingular elliptic main component and p Artin--Schreier tails of genus p(p−1)/2; their genera exhaust the whole genus. Every cusp lies on the rational marked tree overO. A42 gives full fixed inertia at every coefficient prime and packet, and A59 gives all normalizers. This supersedes the earlier restriction of the exact wild model to p=3 and7; it does not assert cofinality or solve universal TaskA5.\n''')
print('A61 integrated: canonical proof, code, audits, row, references and scoped A45 update.')
