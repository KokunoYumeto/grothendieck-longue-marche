#!/usr/bin/env python3
"""Accept D50--D52 and complete Tasks D1/D2 after full independent audits."""
from pathlib import Path
from hashlib import sha256
import ast
import json

ROOT = Path(__file__).resolve().parent.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    proofs = {
        'sections/D_pronilpotent_lift_agent.tex':
        'b27a2116165d03c975e4022125e92fcbf3e599f25d217b350f32a8ec26ef3ff9',
        'sections/D_full_weight5_agent.tex':
        '6f0a686cb8325d660c7f8bc5d7df117b016f42d6865b4f572645f12b900b907c',
        'sections/D_full_weight9_agent.tex':
        '65f6eaa5e1310a8112b5f575cadc5304407ff4f1d7ee9cf7e3b29dc2038ab302'}
    assert all(digest(ROOT / name) == value for name, value in proofs.items())
    scalar = json.loads((ROOT / 'code/audit_scalar_cover_count_root.json').read_text())
    witness = json.loads((ROOT / 'code/audit_special_source_witnesses_final_root.json').read_text())
    assert scalar['all_passed'] and scalar['original_artifacts_unchanged']
    assert witness['all_passed'] and witness['original_artifacts_unchanged']
    assert witness['printed_D52_integral_Lyndon_coefficients_checked'] == 42
    assert all(witness['protected_sha256'][name] == value for name, value in proofs.items())
    saved = ROOT / 'research/checkpoint08_full_profinite_images_prior_passages.json'
    assert not saved.exists()
    old = {}

    agentpath = ROOT / 'sections/D_agent.tex'
    agenttext = agentpath.read_text()
    old['complete_D_agent_source'] = agenttext
    oldtitle = r'\subsection{Sources, comparison maps, and the two remaining image problems}'
    assert agenttext.count(oldtitle) == 1
    agenttext = agenttext.replace(oldtitle, r'\subsection{Sources, comparison maps, and the full leading images}')
    start = agenttext.index(r'\begin{statement}{D.1}{Open}')
    end = agenttext.index(r'\begin{statement}{D.3}', start)
    old['D1_D2_open_statements'] = agenttext[start:end]
    replacement = r'''\begin{statement}{D.1}{Proved}{The weight-five image of the full profinite special group}
For every prime $\ell\geq5$, the rational weight-five metabelian
leading image of $\operatorname{Out}^{\sharp}(\widehat F_2)$ is
\[
 (X+Y)\langle X^2,XY,Y^2\rangle_{\Q_\ell}[x,y],
 \qquad\dim_{\Q_\ell}=3.
\]
All three displayed basis vectors are leading derivation coordinates
of actual multiplier-one full profinite special automorphisms.
\end{statement}
\begin{proof}
D.51 constructs the three integral free-Lie witnesses, realizes their
complete pro-$\ell$ automorphisms, and applies D.50 with their actual
peripheral conjugators. Its commuting characteristic projection square
retains precisely these three graded coordinates. The special equation
gives the matching upper bound three. The full proof and the literal
coefficient certificate are in D.50--D.51.
\end{proof}

\begin{statement}{D.2}{Proved}{The extra weight-nine direction for the full profinite gentle group}
For every prime $\ell\geq5$, the rational weight-nine metabelian
leading image of $\widehat{\mathrm{GT}}_0$ has dimension two and is
\[
 \Q_\ell G_9[x,y]\oplus\Q_\ell p_{\mathrm{extra}}[x,y],
 \qquad
 G_n=\frac{(X+Y)^n-X^n-Y^n}{XY},\quad
 p_{\mathrm{extra}}=X^2Y^2(X+Y)^3.
\]
There is an actual full multiplier-one gentle pair with first
pro-$\ell$ pair coefficient $p_{\mathrm{extra}}[x,y]$ in weight nine.
Its normalized derivation coordinate is
$-p_{\mathrm{extra}}[x,y]$. This pair fails the full pentagon.
\end{statement}
\begin{proof}
D.52 supplies the complete integral invariant Lie witness, the actual
normalized pro-$\ell$ pair, and its full profinite lift from D.50.
The exact characteristic projection retains the whole pair. Its
coordinate and the actual Galois gamma line of D.20 are independent;
D.4 and D.8 give the matching upper bound two. The same degree-nine
pentagon map excludes the constructed extra direction. D.52 proves
each comparison and the stated pair/derivation sign.
\end{proof}

'''
    agenttext = agenttext[:start] + replacement + agenttext[end:]

    rootpath = ROOT / 'sections/D_root.tex'
    roottext = rootpath.read_text()
    old['complete_D_root_source'] = roottext
    prior = ('excluded. This statement leaves the choice between one and three\n'
             'on the unresolved task ledger.')
    assert roottext.count(prior) == 1
    roottext = roottext.replace(prior,
        'excluded. The symmetry comparison gives the displayed two possible\n'
        'dimensions; the full-source construction in D.50--D.51 proves\n'
        'that the actual value is three.')

    assembler = ROOT / 'code/assemble_register.py'
    lines = assembler.read_text().splitlines()
    changed = []
    states = {
        'D.1': ('D.50; D.51',
                'The complete rational leading image has dimension three for '
                'every prime ell at least five. D.50 lifts each complete '
                'pronilpotent peripheral automorphism, retaining all three '
                'actual conjugators, through every finite source. D.51 gives '
                'three literal integral Lie witnesses, their actual pro-ell '
                'realizations, the full characteristic projection square, '
                'and the matching upper bound. Every earlier chief comparison '
                'and finite obstruction is retained with its specified source.'),
        'D.2': ('D.50; D.52',
                'The complete rational invariant metabelian leading image has '
                'dimension two for every prime ell at least five. D.52 constructs '
                'an actual full multiplier-one gentle pair with weight-nine '
                'pair coefficient X^2Y^2(X+Y)^3 and normalized derivation '
                'coefficient its negative. D.50 retains the entire normalized '
                'pro-ell pair and every actual modular-source conjugator. The '
                'Galois gamma line and this extra direction are independent. '
                'The same complete pentagon map excludes the constructed pair. '
                'All42 printed integral witness coefficients pass exact replay.')}
    for i, line in enumerate(lines):
        if not line.strip().startswith("('"):
            continue
        row = ast.literal_eval(line.strip().rstrip(','))
        if row[0] not in states:
            continue
        old[row[0] + '_coverage'] = row
        addition, state = states[row[0]]
        assert row[2].startswith('OPEN:')
        lines[i] = ' ' + repr((row[0], row[1] + '; ' + addition,
                              '(a) Proved', state)) + ','
        changed.append(row[0])
    assert changed == ['D.1', 'D.2']

    mainpath = ROOT / 'LM7_PUSH_paper.tex'
    maintext = mainpath.read_text()
    old['complete_main_source'] = maintext
    anchor = r'\InputIfFileExists{sections/D_v4_refinement_agent.tex}{}{}'
    assert maintext.count(anchor) == 1
    addition = '\n'.join(r'\InputIfFileExists{' + name + r'}{}{}' for name in proofs)
    assert all(name not in maintext for name in proofs)
    maintext = maintext.replace(anchor, anchor + '\n' + addition)
    prior = ('Parts A, B, C and F are complete. The remaining full profinite '
             'image questions in Parts D and E are under investigation.')
    assert maintext.count(prior) == 1
    maintext = maintext.replace(prior,
        'Parts A, B, C, D and F are complete. Every multiplier-one '
        'pronilpotent peripheral automorphism lifts to the full profinite '
        'source with all prescribed conjugators. The actual special image '
        'has dimension three in weight five, and the actual gentle '
        'invariant image has dimension two in weight nine, for every '
        'prime $\\ell\\ge5$. We construct a full gentle pair in the extra '
        'weight-nine direction and prove that it fails the pentagon. '
        'The two complex-multiplication questions in Part E remain under investigation.')

    bibpath = ROOT / 'LM7_PUSH_references.bib'
    bib = bibpath.read_text()
    assert 'ATuraev2009' not in bib
    entry = r'''@misc{ATuraev2009,
 author = {Vladimir Turaev},
 title = {Sections of fiber bundles over surfaces},
 year = {2009},
 howpublished = {arXiv:0904.2692v1},
 url = {https://arxiv.org/pdf/0904.2692},
 note = {verified: primary PDF opened; Lemma 2.1, Section 2.3, and Theorem 1.2 checked with the positive-genus boundary hypothesis in Section 2.4. D.50 derives its required pants formula directly and uses this reference for the explicitly stated representation-theoretic comparison.}
}'''
    bib += '\n' + entry + '\n'

    report = ROOT / 'research/report_body.md'
    body = report.read_text()
    anchor = '\n## Main arithmetic results'
    assert body.count(anchor) == 1
    paragraph = '''
## Completion of the full profinite leading-image questions

Parts A, B, C, D and F now have a proved or refuted outcome for every requested item. The complete weight-five special image has dimension3, and the complete weight-nine gentle invariant image has dimension2, for every prime ell at least5. These conclusions are proved by actual full profinite source elements in D.50--D.52.

D.50 constructs finite scalar covers for every actual subgroup image and every invariant irreducible representation of its normal kernel, including nonfaithful representations. Its direct pants formula retains all boundary matrices; ordinary subgroup Möbius inversion counts the complete generating fibres. The joint source is the full fibre product because its common quotient has trivial conjugation action and therefore kills the kernel commutator [E,A]=A. Choosing the stable lower-central residual gives actual nilpotent refinements in every finite source. Compactness retains all three prescribed full conjugators, the whole pronilpotent automorphism, and generation of every finite quotient. The modular-source argument also retains its order-two and order-three relations and its exact cusp normalization. The earlier prosolvable argument is a proved corollary.

D.51 gives the three unscaled leading derivation coordinates (X+Y)X^2, (X+Y)XY, and (X+Y)Y^2, times [x,y]. D.52 gives the actual full gentle pair with leading pair coordinate X^2Y^2(X+Y)^3[x,y]; the corresponding normalized derivation has the negative of that coordinate. Its complete42-term doubled Lyndon table, the special equation, antisymmetry, cabling, and cyclic sum are retained. The actual characteristic pro-ell square preserves the whole pair, and the existing Galois gamma line gives the second independent direction. The same degree-nine pentagon map excludes the constructed extra pair. Thus Tasks D.1 and D.2 are proved, while D.3 retains its complete finite pentagon comparison.

Root and an independent reader have read every complete proof of D.50--D.52. The independent scalar-cover certificate checks420 projective-phase cases,848 noncentral-kernel surface cases,1088 proper-subgroup counts,136 ordinary Möbius counts,3672 literal boundary transports,331776 actual pair-group products, and the exact nonfaithful representation pullback. Root's isolated replay is literal and takes0.239 seconds. The final source-witness replay takes0.551 seconds, verifies all42 printed coefficients, and preserves every earlier vector and the first replay. Its exact rescalings of the inherited witnesses are2,3/2,-1,3, with common denominator2. The added direct cyclic-identity check changes no source vector. Every superseded D.1/D.2 statement, coverage row, current-open passage, and affected complete source is preserved in research/checkpoint08_full_profinite_images_prior_passages.json.
'''
    body = body.replace(anchor, '\n' + paragraph.strip() + '\n' + anchor)
    prefix = '1. **D.1--D.2:**'
    begin = body.index(prefix)
    end = body.index('\n', begin)
    old['D_remaining'] = body[begin:end]
    body = body[:begin] + body[end + 1:]
    assert body.count('2. **E.2--E.3:**') == 1
    body = body.replace('2. **E.2--E.3:**', '1. **E.2--E.3:**', 1)
    old['first_scope_paragraph'] = body.splitlines()[2]
    scope_note = ('\nThe only unresolved task rows are E.2 and E.3. The report '
                  'therefore remains INCOMPLETE, and work continues on the '
                  'entire CM-coordinate fibres and the full pentagon comparison.\n')
    body = body.replace('\n## Completion of the full profinite leading-image questions',
                        scope_note + '\n## Completion of the full profinite leading-image questions', 1)

    saved.write_text(json.dumps(old, indent=2) + '\n')
    agentpath.write_text(agenttext)
    rootpath.write_text(roottext)
    assembler.write_text('\n'.join(lines) + '\n')
    mainpath.write_text(maintext)
    bibpath.write_text(bib)
    report.write_text(body)
    acceptance = {'accepted_statements': ['D.50', 'D.51', 'D.52'],
                  'completed_tasks': ['D.1', 'D.2'], 'completed_part': 'D',
                  'dimensions_every_prime_at_least_five': {'D.1': 3, 'D.2': 2},
                  'complete_root_and_independent_proof_reads': True,
                  'proof_sha256': proofs,
                  'root_scalar_cover_seconds': scalar['seconds'],
                  'root_final_witness_seconds': witness['seconds'],
                  'all_printed_weight9_coefficients_checked': 42,
                  'initial_witness_program_and_audit_preserved': True,
                  'preserved_passages': str(saved.relative_to(ROOT)),
                  'remaining_global_tasks': ['E.2', 'E.3']}
    (ROOT / 'research/checkpoint08_full_profinite_images_acceptance.json').write_text(
        json.dumps(acceptance, indent=2) + '\n')
    with (ROOT / 'research/root_searches_02.md').open('a') as log:
        log.write('''

134. D51 and D52 complete root proof reads PASS; geometry's complete
     independent reads PASS. The literal D51 basis, integral realization,
     characteristic full/pro-ell square and upper bound give dimension3.
     D52's two exact S3 inner corrections, normalized centralizer and
     filtration argument, pair/derivation sign, literal full modular lift,
     independent gamma line and degree-nine pentagon map give dimension2.
     The reviewed D52 draft is preserved before its two TeX-only repairs.

135. The final witness exporter adds only a direct cyclic-sum assertion
     and its two result fields. The original exporter and its output are
     preserved at their previously audited hashes. A fresh root replay
     checks every final identity, every old vector/map unchanged, and
     all42 printed integral D52 coefficients. PASS0.551s. D50--D52 are
     accepted and integrated; Tasks D1/D2 and PartD are complete. All
     previous open passages and coverage rows are preserved verbatim.
     E2/E3 remain the two active global tasks.
''')
    print(json.dumps(acceptance, indent=2))


if __name__ == '__main__':
    main()
