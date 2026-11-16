#!/usr/bin/env python3
"""Integrate fully audited A62 after explicit root approval."""
from pathlib import Path
import json
import shutil
import sys

r = Path(__file__).resolve().parents[1]
assert '--root-approved' in sys.argv
assert (r/'notes/pbc_A62_audit.md').exists()
assert json.loads((r/'notes/fgh_A62_certificate.json').read_text())['status'] == 'PASS'
s = (r/'notes/fgh_A62_draft.tex').read_text()
assert '^{,p}' not in s
assert 'III.6.2(a),(c),(d)' in s
s = s.replace('% A.62 candidate. Notes only until full independent audits.',
              '% A.62: full independent root and PBC proof/source/certificate audits PASS.')
s = s.replace(r''' h=\frac{\psi_p-g^p}{p}\in\Z_p[x],\qquad
 H_0=\frac{h}{g^p},\qquad
 \frac{\psi_p}{g^p}=1+pH_0.''',r''' \begin{gathered}
 h=\frac{\psi_p-g^p}{p}\in\Z_p[x],\qquad H_0=\frac{h}{g^p},\\
 \frac{\psi_p}{g^p}=1+pH_0.
 \end{gathered}''')
s = s.replace(r''' 1+pH_0(P+T)
   =\frac{c_T}{\gamma_T^p q_T(P)^p}(1+pH_0(P)),
 \qquad
 \overline H_0(P+\overline T)
          =\overline H_0(P)+\overline\epsilon_T.''',r''' \begin{aligned}
 1+pH_0(P+T)
   &=\frac{c_T}{\gamma_T^p q_T(P)^p}(1+pH_0(P)),\\
 \overline H_0(P+\overline T)
   &=\overline H_0(P)+\overline\epsilon_T.
 \end{aligned}''')
s = s.replace(r''' D^2\overline h
   =\overline g^{p-2}(D\overline g)^2
      -\overline g^{p-1}D^2\overline g,
                \qquad DF=-DU.''',r''' \begin{gathered}
 D^2\overline h
   =\overline g^{p-2}(D\overline g)^2
      -\overline g^{p-1}D^2\overline g,\\
 DF=-DU.
 \end{gathered}''')
s = s.replace('The accompanying exact\ncertificate checks the division differential,',
              'The exact certificate\n\\path{code/a_heisenberg_ordinary.py} checks the division differential,')
(r/'sections/A_heisenberg_ordinary.tex').write_text(s)
for suffix in ('.py','.json','.out'):
    shutil.copyfile(r/('notes/fgh_A62_certificate'+suffix),
                    r/('code/a_heisenberg_ordinary'+suffix))
for suffix in ('.json','.out'):
    shutil.copyfile(r/('notes/pbc_A62_independent_rerun'+suffix),
                    r/('code/a_heisenberg_ordinary_pbc_rerun'+suffix))
p = r/'sections/A.tex'
s = p.read_text()
anchor = r'\input{sections/A_heisenberg_inert.tex}'
assert anchor in s and 'A_heisenberg_ordinary.tex' not in s
p.write_text(s.replace(anchor,anchor+'\n'+r'\input{sections/A_heisenberg_ordinary.tex}'))
row = json.loads((r/'notes/fgh_A62_row.json').read_text())
row['where_proved'] = 'sections/A_heisenberg_ordinary.tex'
row['notes'] = ('Registered after complete independent root and PBC proof/source/code audits PASS. '
 'Exact certificate at p=5,13,17 checks actual division functions, the full Verschiebung curve identity '
 'and rational differential pullback, every critical multiplicity and genus. Over an unramified Gauss DVR, '
 'the actual characteristic-zero translation identity normalized modulo p^2 makes the divided differential '
 'descend through the separable CM isogeny. Its descended function has one pole of orderp and derivative mu*x, '
 'so exactly one triple and p-3 simple zeros. Actual charts yield p degree4 tails and p(p-3) degree2 tails, '
 'with an ordinary elliptic main component; the genus sum proves compact type. The p^2 cusps form p rational '
 'clusters ofp marks away from all tails. A42 gives full fixed inertia at every coefficient prime and packet; '
 'A59 gives all normalizers. Together A61/A62 settle the full odd-prime Heisenberg family uniformly. '
 'The family is not claimed cofinal; universal TaskA.5 remains Open.')
(r/'notes/fgh_A62_row.json').write_text(json.dumps(row,indent=2)+'\n')
p = r/'notes/a_results.json'
rows = json.loads(p.read_text())
assert not any(z['id'] == 'A.62' for z in rows)
rows.append(row)
p.write_text(json.dumps(rows,indent=2)+'\n')
p = r/'sections/A_general_cover_frontier.tex'
s = p.read_text()
anchor = 'claim and no fixed-group assertion for every nilpotent cover.'
assert anchor in s
addition = '''
A.62 completes the ordinary-prime half by an actual unramified
translation comparison modulo \\(p^2\\) and separable-isogeny descent.
It gives \\(p\\) quartic and \\(p(p-3)\\) quadratic Artin--Schreier
tails, with all cusps on rational clusters of size \\(p\\).
Thus both assertions are now proved uniformly for the actual
exponent-\\(p\\) Heisenberg cover at every odd prime \\(p\\).
This remains a particular unbounded family of geometric subgroups.'''
p.write_text(s.replace(anchor,anchor+'\n'+addition))
p = r/'notes/root_cover_frontier_results.json'
rows = json.loads(p.read_text())
for z in rows:
    if z['id'] == 'A.45':
        if isinstance(z['depends_on'],str):
            z['depends_on'] += '; A.62'
        else:
            z['depends_on'].append('A.62')
        z['notes'] += (' A.62 completes the ordinary-prime half by actual unramified translation '
                       'comparison modulo p^2 and separable-isogeny descent. Together A61/A62 now '
                       'prove both assertions uniformly for the actual exponent-p Heisenberg cover '
                       'at every odd primep. No cofinality or universal fixed-group conclusion follows.')
p.write_text(json.dumps(rows,indent=2)+'\n')
p = r/'notes/fgh_refs.bib'
s = p.read_text()
anchor = 'Theorem V.2.3.1(b), printed page 142, reopened for the actual Frobenius endomorphism identity in A.61;'
assert anchor in s
s = s.replace(anchor,anchor+' Theorem III.6.2(a),(c),(d), printed page 83, and Theorem V.4.1(a), printed page 148, freshly reopened for the actual ordinary CM isogeny and reduction in A.62;')
p.write_text(s)
(r/'notes/fgh_A62_audit.md').write_text('''# A62 integration and audit record

Registered after complete independent root and PBC proof/source/certificate audits, all PASS. The root read the entire written proof and freshly opened Silverman V4.1(a) and III6.2(a,c,d); PBC independently read all comparisons and reran the actual certificate. Detailed PBC ledger: `notes/pbc_A62_audit.md`; root ledger is retained by the parent with its current full-audit records. Candidate, source ledger, certificate and independent reruns are preserved.

Canonical proof is `sections/A_heisenberg_ordinary.tex`, with exact `code/a_heisenberg_ordinary.py` and retained outputs. The certificate imports the preceding canonical inert-prime division-polynomial implementation; this dependency is preserved in the code directory.

The essential proof gate is an actual unramified translation identity modulo p², including its Gauss-unit normalization and potentially nonzero additive constant. It gives true isogeny descent of the differential. The pole and quarter-rotation computation then determines the descended derivative, all critical multiplicities, and their avoidance of reduced p-torsion. All integral charts, stable-component persistence, genus exhaustion and cusp-cluster comparisons were independently checked.

The two exponent commas were corrected, the Gaussian duality citation was made explicit, and the local expansion was weakened to the precise leading-order statement needed. Long displays were split at integration. No mathematical assertion changed after the independent approvals. A45 remains Open; the complete odd-prime Heisenberg family is not claimed cofinal.
''')
with (r/'notes/fgh.md').open('a') as out:
    out.write('''\n\n## A.62: the full odd-prime Heisenberg family

Registered after full independent root and PBC audits and exact reruns PASS. The ordinary-prime case uses an actual unramified translation comparison modulo p², proving that the divided differential descends through the separable degree-p CM isogeny. Its descended odd function has one pole of orderp and derivative mu*x, hence one triple and p−3 simple zeros. Actual charts give p quartic and p(p−3) quadratic Artin--Schreier tails and one ordinary elliptic main component; genus exhaustion proves compact type. All p² cusps form p rational clusters ofp marks. A42 andA59 supply both all-prime assertions. Together A61/A62 now settle the exponent-p Heisenberg family for EVERY odd primep. Universal TaskA5 remains Open and no cofinality is asserted.\n''')
print('A62 integrated with canonical proof/code/results, audits, references and scoped A45 update.')
