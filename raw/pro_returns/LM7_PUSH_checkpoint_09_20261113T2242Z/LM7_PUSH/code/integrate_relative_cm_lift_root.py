#!/usr/bin/env python3
"""Integrate E58 and complete E2 after whole-proof and isolated code audits."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent
saved = ROOT / 'research/checkpoint08_relative_cm_prior_passages.json'
assert not saved.exists()
audit = json.loads((ROOT / 'code/audit_relative_cm_lift_root.json').read_text())
assert audit['all_passed'] and audit['all_original_files_unchanged']
assert audit['all_mathematical_json_fields_identical']
for name, digest in audit['protected_files'].items():
    assert sha256((ROOT / name).read_bytes()).hexdigest() == digest, name

names = ['LM7_PUSH_paper.tex', 'sections/E_agent.tex',
         'code/assemble_register.py', 'research/report_body.md',
         'LM7_PUSH_references.bib']
old = {name: (ROOT / name).read_text() for name in names}
updated = dict(old)
agent = updated['sections/E_agent.tex']
start = agent.index(r'\begin{statement}{E.2}{Open}')
end = agent.index(r'\begin{statement}{E.3}', start)
old['E2_open_passage'] = agent[start:end]
replacement = r'''\begin{statement}{E.2}{Proved}{The full profinite gentle group reaches the extra CM coset}
There is an actual full profinite gentle pair
$(1,f)\in\widehat{\mathrm{GT}}_0$ whose E.1 CM bits are $(1,0)$.
In the actual modular source $\mathcal B=C_2\amalg C_3$, put
$H=F'F^3$, with $F=\ker(\mathcal B\to S_3)$. The pair can be
chosen with $f\in R_{\rm nil}(H)$, and its normalized full
automorphism fixes $\tau=sr$ literally. Its unique pure
$r$- and $s$-conjugators $A,\beta$ have the exact images
\[
 q(A)=[5I],\qquad q(\beta)=1,
 \qquad q:\mathcal B\longrightarrow
      \operatorname{SL}_2(\Z/12)/\{\pm I\}.
\]
Thus the full gentle group reaches the extra CM coset in Task E.2.
The twelve particular extra representatives recorded by LM7 D.25
are all excluded by E.9. The asserted equivalence between their
genuineness and the full CM existence question is consequently false.
\end{statement}
\begin{proof}
E.58 proves the complete relative pronilpotent lifting theorem
with every actual peripheral conjugator retained. For the specified
$H$, its two-primary source has a pro-two-kernel map to the actual
joint image of $Q$ and $\mathcal B/H$. Coprime complement conjugacy
supplies an $r$-centralizer element over $([5I],1)$. Put this element
in the two-primary component and the identity in every other component
of the relative fibre product. These are specified conjugators for
the identity relative automorphism. The lifting theorem gives a full
automorphism with these frames and $f\in R_{\rm nil}(H)\subset F'$.
The full free-product centralizers make its pure frames unique.
E.1's positive representatives then give bits $(1,0)$, as proved
and independently computed in E.58. Its equality $q\Phi=q$
also gives its actual $G_6$ shadow. E.9's complete finite exclusion
applies to every one of the twelve old representatives, while the
constructed full pair supplies a genuine point in the whole CM
matrix fibre. This proves both the positive existence result and
the stated failure of the proposed representative reduction.
\end{proof}

'''
updated['sections/E_agent.tex'] = agent[:start] + replacement + agent[end:]

main = updated['LM7_PUSH_paper.tex']
anchor = r'\InputIfFileExists{sections/E_a6_uniform_agent.tex}{}{}'
assert main.count(anchor) == 1
main = main.replace(anchor, anchor + '\n' +
    r'\InputIfFileExists{sections/E_relative_cm_lift_agent.tex}{}{}')
prior = 'The two complex-multiplication questions in Part E remain under investigation.'
assert main.count(prior) == 1
main = main.replace(prior,
    'The relative lifting theorem constructs an actual full gentle pair '
    'in the extra complex-multiplication coset, with the exact positive '
    'CM bits $(1,0)$ and every prescribed finite conjugator retained. '
    'Task E.2 is complete. The full pentagon question E.3 remains under investigation.')
updated['LM7_PUSH_paper.tex'] = main

lines = updated['code/assemble_register.py'].splitlines()
changed = []
for index, line in enumerate(lines):
    if not line.strip().startswith("('"):
        continue
    row = ast.literal_eval(line.strip().rstrip(','))
    if row[0] != 'E.2':
        continue
    assert row[2].startswith('OPEN:')
    old['E2_coverage_row'] = row
    state = ('E.58 constructs an actual full multiplier-one gentle pair '
        'in the extra CM coset, with positive bits (1,0). Its relative '
        'pronilpotent lifting theorem retains all three prescribed '
        'conjugators through every finite source. For H=F-prime F-cube, '
        'the exact two-primary centralizer lift gives the unique pure '
        'frames A=[5I], beta=V=1 modulo twelve, with f in R_nil(H). '
        'The whole proof and every finite source/sign calculation pass '
        'independent audit. E.9 excludes all twelve earlier particular '
        'representatives, so their asserted equivalence with full CM '
        'existence is false. The constructed automorphism has an actual '
        'new G6 shadow in the whole CM matrix fibre. All earlier finite '
        'refinements and whole-fibre results remain in the paper.')
    lines[index] = ' ' + repr((row[0], row[1] + '; E.58', '(a) Proved', state)) + ','
    changed.append(row[0])
assert changed == ['E.2']
updated['code/assemble_register.py'] = '\n'.join(lines) + '\n'

body = updated['research/report_body.md']
scope = ('The only unresolved task rows are E.2 and E.3. The report therefore '
    'remains INCOMPLETE, and work continues on the entire CM-coordinate '
    'fibres and the full pentagon comparison.')
assert body.count(scope) == 1
body = body.replace(scope,
    'The only unresolved task row is E.3, the extra CM coset for full '
    'profinite GT with the pentagon. Parts A, B, C, D and F and Tasks '
    'E.1--E.2 are complete. The report remains INCOMPLETE while the full '
    'pentagon comparison continues.')
start = body.index('1. **E.2--E.3:**')
end = body.index('\n', start)
old['current_E2_E3_remaining_paragraph'] = body[start:end]
body = body[:start] + (
    '1. **E.3:** The full profinite GT CM image remains undecided. '
    'E.58 resolves the gentle-group question E.2 by an actual full '
    'source construction; its three peripheral equations do not '
    'supply the four-strand pentagon equation. E.17--E.57 retain '
    'the explicit whole CM families through the stated finite '
    'four- and five-strand targets, the complete two- and three-primary '
    'boundary families, full higher-prime boundary factors, the joint '
    'A6 and signed Ferrari source, and all symplectic congruence '
    'levels. All complete proof and certificate audits named above '
    'are retained. The exact new comparisons are the SL2(F3) Ferrari '
    'source and the central-three A6 Ferrari source; their full '
    'source kernels and whole correction fibres are active work. '
    'For each source, a failed literal word is retained only as '
    'the failure of that word, until its complete correction fibre '
    'is determined. The parallel proof route compares the actual '
    'four-strand pentagon maps with the unique full accessory '
    'frames of E.58. Compatibility through every finite four-strand '
    'quotient, or a complete finite exclusion of every extra-CM '
    'fibre, remains to be proved.') + body[end:]
anchor = '\n## Main arithmetic results'
assert body.count(anchor) == 1
section = r'''
## Completion of the full gentle CM question

E.58 proves the relative form of D.50 for every open normal subgroup U of the actual free pants or modular source. The quotient by R_nil(U) is the actual fibre product of all relative pro-p sources over the specified finite quotient Gamma/U. In every finite embedding problem, the stable lower-central residual of the actual U-image has [E,A]=A, and every auxiliary scalar cover has nilpotent U-image. The complete subgroup counts and prescribed-conjugator compactness argument therefore give a full peripheral lift.

For the CM construction, H=F-prime F-cube has index 54. The fixed E.1 map to Q=SL2(Z/12)/{plus or minus I} has q(F)=C2^2 times SL2(F3) and q(H)=C2^2 times Q8. Its actual joint source with B/H has order 1728. The literal H-word [x,y]^2 maps to ([5I],1). Coprime complement conjugacy lifts this specified r-centralizer value through the pro-two kernel. Its two-primary coordinate, with identity at all other primes, is a genuine r-conjugator for the identity on the whole relative pronilpotent source. The full relative theorem retains that frame, together with identity s and cusp frames. After the exact cusp normalization, f lies in R_nil(H), and the unique pure accessory frames have images A=[5I], beta=V=1. E.1's positive convention gives the CM bits (1,0). Thus the full gentle group reaches the extra CM coset, and E.2 is proved.

The full automorphism induces the identity on Q, so it preserves the actual kernel N_B and its characteristic subgroup N_B-prime N_B^6. It therefore has a genuine G6 shadow. E.9 has already excluded all twelve particular old representatives. Together these two proved results refute the proposed equivalence between genuineness of one of those representatives and existence in the whole CM matrix fibre. The complete G6 source itself does not factor through the relative pro-two H source: x^6=tau^(-12) has a primitive N_B homology class and order six in G6. Its 24-edge integral cycle is explicitly checked. This failed factorization is preserved with its exact map and element; it is not used to pass an old shadow through the construction.

Root and the arithmetic reader both read the complete E.58 proof and finite program. Root independently opened Herfort--Ribes, Theorem B-prime, Section 4, printed page 159; its factor-centralizer equality gives the uniqueness of both pure accessory frames. Root's isolated standard-library replay takes 0.206 seconds and reproduces every mathematical JSON field, with all nine protected files unchanged. The finite certificate checks the 576-element Q source, all 9216 products in its pure CRT splitting, the 54-element affine quotient, the 1728-element actual joint source and its common quotient, the literal central word, the positive signs and the primitive cycle. The first erroneous sign assertion used the negative lexicographic r representative and is preserved with its failure; the corrected certificate uses E.1's specified positive R. Every prior E.2 open passage, coverage row and affected complete source is retained in research/checkpoint08_relative_cm_prior_passages.json. E.3 remains the active full-pentagon question.
'''
body = body.replace(anchor, '\n' + section.strip() + '\n' + anchor)
updated['research/report_body.md'] = body

bib = (ROOT / 'research/E58_references.bib').read_text()
assert 'BCHerfortRibes1985' not in updated['LM7_PUSH_references.bib']
note = "note = {Theorem B in the introduction; Theorem B' in Section 4, p. 159}"
assert note in bib
bib = bib.replace(note,
    "note = {verified: complete primary article opened independently by root "
    "and both proof readers. Theorem B' in Section 4, printed p. 159, "
    "and its proof give the factor-centralizer equality used in E.58; "
    "the precise applications are to the actual factors C2 and C3.}")
updated['LM7_PUSH_references.bib'] += '\n' + bib

saved.write_text(json.dumps(old, indent=2) + '\n')
for name in names:
    (ROOT / name).write_text(updated[name])
acceptance = {
    'accepted_statement': 'E.58', 'completed_task': 'E.2',
    'full_gentle_extra_CM_exists': True, 'positive_CM_bits': [1, 0],
    'old_twelve_representative_equivalence': 'Refuted by E.9 and E.58 together.',
    'proof_sha256': audit['protected_files']['sections/E_relative_cm_lift_agent.tex'],
    'independent_root_replay_seconds': audit['elapsed_seconds'],
    'full_root_and_arithmetic_proof_reads': True,
    'preserved_prior_passages': str(saved.relative_to(ROOT)),
    'remaining_task': 'E.3',
}
(ROOT / 'research/checkpoint08_relative_cm_acceptance.json').write_text(
    json.dumps(acceptance, indent=2) + '\n')
with (ROOT / 'research/root_searches_02.md').open('a') as stream:
    stream.write('''

136. Root opened the full primary Herfort--Ribes1985 article, Section4,
     printed page159, TheoremB-prime and its proof (turn547view0).
     Applied to the actual C2 and C3 factors, it gives the pure-frame
     uniqueness used in E58; no centralizer assertion is inferred
     solely from a finite quotient.

137. Root read every line of E58 and its standard-library certificate.
     The complete relative source lift, actual local fibre product,
     pro-two centralizer lift, exact full cusp normalization and
     positive E1 signs all pass. Arithmetic's independent full review
     also passes. Root's isolated replay passes in0.206s, reproduces
     every mathematical JSON field, and preserves all9 protected
     files. E58 is integrated and E2 is proved. The exact E9 exclusion
     together with E58 refutes the earlier twelve-representative
     equivalence. E3 is the remaining global task.
''')
print(json.dumps(acceptance, indent=2))
