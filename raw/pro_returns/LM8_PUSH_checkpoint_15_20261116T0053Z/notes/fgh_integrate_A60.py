#!/usr/bin/env python3
"""Register fully audited A60 after checkpoint10 source release."""
from pathlib import Path
import json,shutil,sys
r=Path(__file__).resolve().parents[1]
assert '--root-released' in sys.argv
assert (r/'notes/de_A60_audit.md').exists()
assert 'Post-checkpoint10 A60 full root audit' in (r/'notes/root_midday_audit.md').read_text()
s=(r/'notes/fgh_A60_draft.tex').read_text()
s=s.replace('% Candidate A.60. Notes only until independent audits and checkpoint release.','% A.60: registered after full independent root and DE proof/source/certificate audits PASS.')
s=s.replace(r'\qquad h=\frac{\psi _7+1}{7},',r'\\ h&=\frac{\psi _7+1}{7},')
s=s.replace(r''' \overline h=x^{24}-2x^{22}-2x^{20}+x^{18}-x^{14}
                  -3x^{10}-x^8-x^6-3x^4\quad\text{in }\F_7[x].''',r''' \begin{aligned}
 \overline h={}&x^{24}-2x^{22}-2x^{20}+x^{18}-x^{14}\\
               &-3x^{10}-x^8-x^6-3x^4
                   \quad\text{in }\F_7[x].
 \end{aligned}''')
s=s.replace(r''' u^7-\pi^6u^6+3\pi^5u^5-5\pi^4u^4
             +5\pi^3u^3-3\pi^2u^2+\pi u=h(x),
                \qquad y^2=x^3-x.''',r''' \begin{gathered}
 u^7-\pi^6u^6+3\pi^5u^5-5\pi^4u^4\\
             {}+5\pi^3u^3-3\pi^2u^2+\pi u=h(x),
                \qquad y^2=x^3-x.
 \end{gathered}''')
s=s.replace(r''' \begin{split}
 z_0^7\bigl(V+3\eta V^2+5\eta^2V^3+5\eta^3V^4
                         +3\eta^4V^5+\eta^5V^6-V^7\bigr)
              =\frac{h(x)-h(a)}{\eta}.
 \end{split}''',r''' \begin{aligned}
 \mathcal B_\eta(V)&=V+3\eta V^2+5\eta^2V^3+5\eta^3V^4\\
                  &\qquad+3\eta^4V^5+\eta^5V^6-V^7,\\
 z_0^7\mathcal B_\eta(V)&=\frac{h(x)-h(a)}{\eta}.
 \end{aligned}''')
s=s.replace('certificate verifies (A.60.3)--(A.60.4)',r'certificate \texttt{code/a_heisenberg_seven.py} verifies'+'\n(A.60.3)--(A.60.4)')
(r/'sections/A_heisenberg_seven.tex').write_text(s)
for suffix in ['.py','.json','.out']:
 shutil.copyfile(r/('notes/fgh_A60_certificate'+suffix),r/('code/a_heisenberg_seven'+suffix))
shutil.copyfile(r/'notes/fgh_A60_certificate_root_rerun.out',r/'code/a_heisenberg_seven_root_rerun.out')
p=r/'sections/A.tex';s=p.read_text();anchor='\\input{sections/A_nilpotent_cover_normalizers.tex}'
assert anchor in s and 'A_heisenberg_seven.tex' not in s
p.write_text(s.replace(anchor,anchor+'\n\\input{sections/A_heisenberg_seven.tex}'))
row=json.loads((r/'notes/fgh_A60_row.json').read_text())
row['where_proved']='sections/A_heisenberg_seven.tex'
row['notes']='Registered after complete independent root and DE proof/source audits and exact certificate reruns PASS. The curve is explicitly the smooth proper normalization of its function field. Actual translation lifts and the quarter-rotation identify the exponent-seven Heisenberg deck group. The seven-adic model has a supersingular elliptic main component and seven genus21 Artin--Schreier tails; the genera exhaust148. The otherwise invisible degree-seven Taylor coefficient vanishes at all four non-two-torsion centres, and all lower coefficients are divisible by7 over the unramified centre field. All49 cusps lie in the rational marked cluster overO, disjoint from the seven positive-genus tails. A41--42 give all-prime full fixed inertia; A59 gives all-prime normalizer recognition. No all-inert-prime pattern, cofinality, or universal-cover assertion is inferred.'
(r/'notes/fgh_A60_row.json').write_text(json.dumps(row,indent=2)+'\n')
p=r/'notes/a_results.json';rows=json.loads(p.read_text());assert not any(z['id']=='A.60' for z in rows);rows.append(row);p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'sections/A_general_cover_frontier.tex';s=p.read_text();anchor='\n\nA.46 supplies a general'
assert anchor in s
addition='\n\nA.60 completes both assertions at every coefficient prime for\nthe next actual Heisenberg cover, of degree343, proper genus148\nand49cusps. Its explicit seven-adic model has one supersingular\nelliptic main component and seven genus21 Artin--Schreier tails;\nall marks occur on a rational tree over the origin, disjoint\nfrom those tails. This exact calculation is not an assertion\nabout every higher Heisenberg cover or every nilpotent cover.\n'
p.write_text(s.replace(anchor,addition+anchor))
p=r/'notes/root_cover_frontier_results.json';rows=json.loads(p.read_text())
for z in rows:
 if z['id']=='A.45':
  z['depends_on']+='; A.60'
  z['notes']+=' A.60 completes both all-prime assertions for the actual Heisenberg7 degree343 genus148 cover via explicit seven-adic charts and the rational cluster of all49cusps. This exact case does not assert a cofinal family or a general fixed-group theorem for nilpotent covers.'
p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'notes/fgh_refs.bib';s=p.read_text();old='verified: Proposition VII.5.5 and Exercise V.5.7;'
assert old in s
s=s.replace(old,'verified: Proposition VII.5.5, including residue characteristic two, and Exercise III.3.7 recurrence and part (f) divisor formula, printed pages 105--106, freshly reopened for A.59--A.60; Exercise V.5.7;')
p.write_text(s)
(r/'notes/fgh_A60_audit.md').write_text('''# A60 integration and audit record\n\nRegistered after root and DE independently read the whole proof, freshly opened SilvermanIII Exercise3.7, and reran the full exact certificate. Both verdicts are PASS. Full audit records are `notes/root_midday_audit.md` (Post-checkpoint10 A60) and `notes/de_A60_audit.md`; the source ledger and original candidate/certificates are retained.\n\nThe opening explicitly defines the smooth proper normalization. Long polynomial displays were split across lines at integration without changing identities; the tail binomial polynomial is merely named mathcalB_eta for layout. The actual translation lifts and exponent-seven argument, hidden degree-seven Taylor coefficient, all seven smooth chart valuations, genus exhaustion, and all49 marked sections were checked by both reviewers. No general-prime pattern is asserted.\n''')
with (r/'notes/fgh.md').open('a') as f:f.write('\n\n## A.60: complete genus148 Heisenberg-seven cover\n\nRegistered after root and DE full proof/source/certificate audits PASS. The actual degree343 cover has an explicit seven-adic compact-type model with one supersingular elliptic main component and seven genus21 Artin--Schreier tails. The genera exhaust148. All49cusps lie on a rational marked tree overO, away from every positive-genus tail. A42 supplies all-prime full fixed inertia, while A59 supplies all-prime normalizer recognition. The missing degree-seven Taylor coefficient was explicitly verified, and no general inert-prime statement is inferred from numerical pattern.\n')
print('A60 registered with canonical proof/code/results/audits/refs and A45 frontier.')
