#!/usr/bin/env python3
"""Preserve and correct the inherited double-cover Kummer convention."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent


def main():
    saved = ROOT / 'research/checkpoint07_kummer_sign_prior_passages.json'
    assert not saved.exists()
    old = {}
    section = ROOT / 'sections/D_agent.tex'
    text = section.read_text()
    previous = r'''homomorphisms. The sign convention there is
$\rho_N=-c_N$, and on the stated Galois normalization it is
$\rho_N=\kappa_N$. This is an equality of the specified coefficients.'''
    replacement = r'''homomorphisms. We retain $\rho_N^{\rm dist}:=-c_N$ as
the explicitly defined negative distribution coordinate. The earlier
sentence identifying it with the positive-root Kummer character in
the displayed Galois convention requires the following correction.
For $N=2$, the exact comparison is
\[
 c_2(f_\sigma)=\kappa_2(\sigma),\qquad
 \rho_2^{\rm dist}(f_\sigma)=-\kappa_2(\sigma).
 \tag{D.5.1}
\]
Here $\kappa_2$ is defined by
$\sigma(2^{1/m})=\zeta_m^{\kappa_2(\sigma)}2^{1/m}$
using positive roots and $\zeta_m=e^{2\pi i/m}$.
We now prove the coefficient and convention maps.

The continuous homomorphism $c_2:H_2\to\widehat\Z$ is the
$y$ coordinate after $\delta_2$. On $\widehat F'$ it kills
$\widehat F''$. In the free basis
$x^2,y,xyx^{-1}$ of $H_2$, every element of $\widehat F'$
has zero first coordinate and its other two abelian coordinates
sum to zero. Conjugation by $x$ interchanges those last two
coordinates, and conjugation by $y\in H_2$ fixes them.
Moreover $[x,y]=(xyx^{-1})y^{-1}$ has $c_2$ value $-1$.
Thus the actual map from the metabelian commutator module is
\[
 c_2\bigl(A\ast[x,y]\bigr)=-A(-1,1),
 \tag{D.5.2}
\]
where $\ast$ is left conjugation. The identity follows first on
the integer linear combinations of conjugates and then on their
closure by continuity. Nakamura--Schneps use exactly
$x\mapsto x^\chi$, $y\mapsto f_\sigma^{-1}y^\chi f_\sigma$;
their equation (2.4) and Lemma 2.3 give
$f_\sigma\equiv A_\sigma\ast[x,y]$ and
$\kappa_2(\sigma)=-A_\sigma(-1,1)$
\cite[\S2, (2.1), (2.4), Lemma 2.3]{BCNakamuraSchneps2000}.
Combining these with \textup{(D.5.2)} proves
\textup{(D.5.1)}, including reduction modulo every integer.

The convention change mentioned just after their equation (2.1)
is the actual continuous free-group automorphism
\[
 \iota(x)=x^{-1},\qquad\iota(y)=y^{-1},\qquad
 \delta_2\circ\iota|_{H_2}=\iota\circ\delta_2.
 \tag{D.5.3}
\]
To verify the last equality, compare its two sides on
$x^2,y,xyx^{-1}$. The third generator is sent by $\iota$ to
$x^{-2}(xyx^{-1})^{-1}x^2$, which $\delta_2$ kills;
the first two give $x^{-1}$ and $y^{-1}$ on both sides.
Consequently $c_2(\iota f)=-c_2(f)$.
Writing $f_\sigma^{\rm Ihara}=\iota(f_\sigma)$ for the
specified change of variables gives
$-c_2(f_\sigma^{\rm Ihara})=\kappa_2(\sigma)$.
The finite distribution tests retain their literal $c_N$ maps;
all arithmetic matrix comparisons below use the displayed
Nakamura--Schneps convention.'''
    assert text.count(previous) == 1
    old['D.5_arithmetic_sentence'] = previous
    text = text.replace(previous, replacement)

    e25 = ROOT / 'sections/E_geometry_agent.tex'
    e_text = e25.read_text()
    previous = r'''every value of $\rho_3=-c_3\pmod4$; restricting both $c_2,c_3$ to
even residues still leaves both values $0,2$ of $\rho_3\pmod4$.'''
    replacement = r'''every value of the defined coordinate $\rho_3^{\rm dist}=-c_3\pmod4$;
restricting both $c_2,c_3$ to even residues still leaves both
values $0,2$ of $\rho_3^{\rm dist}\pmod4$.'''
    assert e_text.count(previous) == 1
    old['E.25_quartic_coordinate'] = previous
    e_text = e_text.replace(previous, replacement)
    previous = r'''The convention $\rho_N=-c_N$ is the one proved in D.5.
No identification of this coefficient on the whole GT source
with a different matrix-defined extension of a Galois Kummer
character is needed for this finite calculation.'''
    replacement = r'''The notation $\rho_N^{\rm dist}=-c_N$ defines the negative
coefficient coordinate. The saved JSON field
\texttt{admissible\_rho3\_mod4} records exactly $-c_3\bmod4$.
Every finite equation above uses $c_N$ itself. D.5 proves the
actual double-cover arithmetic comparison
$c_2(f_\sigma)=\kappa_2(\sigma)$ in the stated generator convention.
The proof here depends only on the five displayed coefficient maps
and their complete joint correction image.'''
    assert e_text.count(previous) == 1
    old['E.25_convention_paragraph'] = previous
    e_text = e_text.replace(previous, replacement)

    memo = ROOT / 'research/BC_modular_comparison.md'
    memo_text = memo.read_text()
    previous = "D.5's coefficient is literal: c_N is the y-coordinate of delta_N(f), and rho_N=−c_N. Its full-GT distribution identity is the opened Enriquez theorem. The comparison with the stated arithmetic Kummer character is made on the Galois image."
    replacement = ("D.5's coefficient is literal: c_N is the y-coordinate of delta_N(f), and rho_N^dist=−c_N is its defined negative coordinate. Its full-GT distribution identity is Enriquez's opened theorem. The exact double-cover comparison in the NS generator convention is c_2(f_sigma)=+kappa_2(sigma). Simultaneous inversion of x and y changes the sign, through the commuting delta_2 square proved in D.5. The earlier arithmetic-sign sentence is preserved and corrected in research/BC_kummer_two_sign_audit.md and research/checkpoint07_kummer_sign_prior_passages.json.")
    assert memo_text.count(previous) == 1
    old['modular_memo_coefficient'] = previous
    memo_text = memo_text.replace(previous, replacement)
    previous = "The independent scan found no earlier claim in D.5 or E.6 that needed this additional equality. D.5 states its exact coefficient convention and Galois comparison; E.6 uses only the induced maps (q delta_N,c_N). The preliminary proposed numerical exclusion from identifying extensions was withdrawn and is absent from the theorem files."
    replacement = ("The earlier scan concerned the proposed equality of full-GT extensions. The subsequent literal double-cover audit found and corrected D.5's arithmetic sign, while retaining the full-GT distribution identity. E.6 and E.25 use only the induced maps (q delta_N,c_N). E.29, E.38 and their later comparisons use the actual NS Theorem2.5 matrices and positive-root character directly; their matrices and labels are unchanged. The preliminary proposed numerical exclusion from identifying extensions remains withdrawn.")
    assert memo_text.count(previous) == 1
    old['modular_memo_earlier_scan'] = previous
    memo_text = memo_text.replace(previous, replacement)

    report = ROOT / 'research/report_body.md'
    body = report.read_text()
    previous = ('The coefficient convention is exactly rho_N=-c_N; agreement with a matrix-defined extension '
                'of a Kummer character on the whole GT group has not been established and is not used to exclude any point.')
    replacement = ('The saved negative-coefficient label is exactly rho_N^dist=-c_N. '
                   'D.5 now proves c_2(f_sigma)=+kappa_2(sigma) in the actual Nakamura--Schneps generator convention, '
                   'and proves the simultaneous-inversion map that changes this sign. '
                   'The finite test uses the literal c_N maps, so its coefficient sets and matrices are unchanged.')
    assert body.count(previous) == 1
    old['report_E.25_sentence'] = previous
    body = body.replace(previous, replacement)
    anchor = '\n## Sources and manuscript scope\n'
    assert body.count(anchor) == 1
    addition = r'''
### Corrected distribution-coordinate sign

The earlier D.5 proof identified the negative distribution coordinate $-c_N$ with the positive-root Kummer character while retaining the Nakamura--Schneps generator convention. The literal double-cover map proves that this sentence was wrong at $N=2$: $c_2([x,y])=-1$, conjugation by $x$ acts by minus one, and conjugation by $y$ acts trivially. Hence $c_2(A\ast[x,y])=-A(-1,1)$, which NS equation (2.4) and Lemma 2.3 identify with $+\kappa_2$. The simultaneous free-generator inversion commutes with $\delta_2$ on all three free generators and reverses $c_2$, giving the precise conversion to the Ihara variables. Both independent readers opened the primary convention paragraph and lemma. The former text and its dependent prose are preserved in `research/checkpoint07_kummer_sign_prior_passages.json`; the detailed dependency inventory is `research/BC_kummer_two_sign_audit.md`. E.25's saved `admissible_rho3_mod4` field retains its literal meaning $-c_3\bmod4$. Its coefficient sets, source words, matrices and orders are unchanged. E.29 and E.38 use NS Theorem 2.5 directly, with positive-root Kummer parameter and the explicit $-8\kappa$ matrices. E.43, E.46, E.47 and E.50 inherit that same arithmetic selection, so their finite certificates and their correcting subgroups do not change.
'''
    body = body.replace(anchor, '\n' + addition.strip() + '\n' + anchor)

    bib_paths = [ROOT / 'LM7_PUSH_references.bib', ROOT / 'research/BC_references.bib']
    bib_changes = []
    for bib in bib_paths:
        refs = bib.read_text()
        start = refs.index('@article{BCNakamuraSchneps2000,')
        end = refs.index('\n}', start)
        entry = refs[start:end]
        phrase = 'The arithmetic sign was checked again at the positive-root definition at the beginning of Section 2, the generator-convention paragraph after (2.1), (2.4), and Lemma 2.3 on author-PDF p.9; the exact double-cover and inversion maps are proved in D.5.'
        assert phrase not in entry
        assert entry.endswith('}')
        new_entry = entry[:-1] + ' ' + phrase + '}'
        old[str(bib.relative_to(ROOT)) + ':BCNakamuraSchneps2000'] = entry
        bib_changes.append((bib, refs[:start] + new_entry + refs[end:]))

    old['E.50_proof_opening_before_typography_repair'] = '\\begin{proof}\n\\paragraph{The actual finite source and its residual.}'
    saved.write_text(json.dumps(old, indent=2) + '\n')
    section.write_text(text)
    e25.write_text(e_text)
    memo.write_text(memo_text)
    report.write_text(body)
    for bib, refs in bib_changes:
        bib.write_text(refs)
    with (ROOT / 'research/root_searches_02.md').open('a') as log:
        log.write('''

109. The third checkpoint07 build reaches E50 and stops at its second
     paragraph heading with Improper prevdepth. The complete attempted
     build and source snapshot are preserved as checkpoint07_third_failure;
     no new PDF was produced. The proof now starts with ordinary prose
     before its first paragraph heading, the same repair used in E46.

110. The double-cover Kummer sign is checked from the literal map and
     reopened primary text. Root opened NS newGT.pdf (turn491view0,
     turn492view2, turn494view2), Section2 positive-root definition,
     equation2.1 and its convention paragraph, equation2.4 and Lemma2.3.
     c2([x,y])=-1, x acts by -1 and y by1, so c2(f_sigma)=+kappa2.
     The exact simultaneous-inversion automorphism commutes with delta2
     on its free basis and reverses the sign. D5's earlier arithmetic
     sentence was wrong in the stated NS convention; the former passages
     are preserved. E25 keeps its exact negative coefficient labels.
     E29/E38 use NS Theorem2.5 directly, and the dependent E43/E46/E47/E50
     arguments retain that actual Galois choice. No certificate changes.
     Enriquez's Theorem8.1 and Remark8.6 were reopened (turn493view0,
     turn494view0, turn495view0), confirming the literal delta_N/c_N
     distribution maps used in every finite test.
''')
    print(json.dumps({'corrected': ['D.5 arithmetic sign and exact inversion comparison',
                                   'E.25 negative-coordinate labels',
                                   'report and modular comparison memo'],
                      'mathematical_certificates_changed': [],
                      'preserved_passages': str(saved.relative_to(ROOT))}, indent=2))


if __name__ == '__main__':
    main()
