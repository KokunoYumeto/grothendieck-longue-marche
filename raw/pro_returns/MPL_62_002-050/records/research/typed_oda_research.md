# Typed-sheet and Oda research evidence

Research agent: `typed_oda_research`. Research only, after the transcription freeze. No supplied manuscript JPG was viewed, no transcription was performed, and no TeX file was changed. All manuscript statements below refer to the frozen page text, not an independent palaeographic reading. The supplied README and `notes/RESULTS_STATE.md` were read in full. Only Oda's supplied PDF was extracted and one of its pages was rendered for mathematical verification.

## 1. Scope and page concordance

The two reused typescript sequences must be separated from the interleaved handwritten material. Their printed foliation provides a reading order, not a date, authorship attribution, or proof that every page of either underlying typescript is supplied.

| Series | Scan | Printed page | Manuscript page | Content |
|---|---:|---:|---:|---|
| n°276 | 022 | 9 | 21 | Complete filtered modules; series criterion |
| n°276 | 024 | 10 | 23 | Finite products; formal power series |
| n°276 | 026 | 11 | 25 | Formal power series; filtered lifting begins |
| n°276 | 049 | 13 | 48 | Graded generators; topological Nakayama |
| n°276 | 047 | 15 | 46 | Noetherian consequences; enveloping algebra |
| n°276 | 045 | 16 | 44 | Enveloping-algebra proof; completion |
| n°276 | 043 | 17 | 42 | Completion of quotients; exactness |
| n°276 | 041 | 18 | 40 | Quotients of completions; completed scalars |
| n°276 | 020 | 20 | 19 | Artin–Rees begins |
| n°272 | 029 | 39 | 28 | Residue approximation; independent valuations |
| n°272 | 039 | 43 | 38 | Fundamental inequality; algebraic extensions |
| n°272 | 037 | 44 | 36 | Rank and discreteness under extension |
| n°272 | 035 | 45 | 34 | Places with algebraically closed target |
| n°272 | 033 | 46 | 32 | Place existence; editorial paragraph; extensions |
| n°272 | 031 | 47 | 30 | Number and localizations of extensions |

Thus printed pages 12, 14, and 19 are gaps in the supplied n°276 sequence, and printed pages 40–42 are a gap in the supplied n°272 sequence. In particular, the continuation of Proposition 6 after printed 11 and the statement of Proposition 7 before printed 13 are not visible in this selected sequence. The n°272 bracket mentioning “le rédacteur” and Samuel cannot safely be assigned to Grothendieck's individual voice solely because these sheets occur in his papers.

**Context/result-register relation.** This evidence bears on **WG2 §1.1 #3** (archive organization) and limits the use of **WG2 §2.4 #4** (second cote47 witness / earlier cote44 theorems). These typed algebra propositions are not an earlier numbered version of cote44's cycle-theoretic Th.1–7. Their occurrence among scans042–050 also cautions against treating the range of **Hua, findings register, 62-triples-rigidified-moduli** as one uninterrupted moduli argument. The other research agent owns the actual handwritten moduli claim.

## 2. n°272: detailed note candidates and checks

### V01. Scan029, Corollaries 1–3: residue approximation is weaker than full approximation

The preceding statement supplies a Chinese-remainder/residue-separation construction for the intersection of finitely many incomparable valuation rings. The special elements in Corollary2 have value zero at one valuation and strictly positive value at the others. This is the assertion invoked on scan031; it must not be replaced by the stronger independent-valuation theorem lower on scan029. Anscombe, Dittmann, and Fehm (2020, §5.2) explicitly distinguish residue approximation for incomparable valuations from arbitrary approximation for independent ones.

**Context search:** cote16 scan052, the reused “Algèbres étales et le différente (4), Tribu n°65,” contains instructions about DVR differents and tame complete extensions. It supplies related valuation background but no second copy of this residue-approximation argument. No direct matching proposition was found in cotes47,54,44. **Confidence:** high; the precise internal citation is visible on scan031.

### V02. Scan029, Proposition3: exact hypothesis for simultaneous approximation

The stated pairwise independence means no nontrivial common coarsening (equivalently no proper common valuation overring). Distinct rank-one valuation rings satisfy this; pairwise distinct valuation rings of higher rank need not. Anscombe et al. (2020, Theorem1.2 and footnotes2,4) state the stronger strict-inequality form and identify its Bourbaki locator as *Commutative Algebra*, VI.7.2, Theorem1. The paper's Theorem1.3 explains that relaxing independence requires compatibility in the common coarsenings.

**Own explicit test:** take a rank-one valuation w with residue field admitting two distinct nontrivial valuations, and compose w with each residue valuation. The resulting refinements are distinct but share w, so arbitrary targets incompatible modulo w cannot be simultaneously approximated. **Context:** same limited cote16scan052 link as V01; no contribution to the profinite completions in LM7E.30 or the cycle questions in WGH9 / WG2§2.3#12.

### V03. Scan029 bracket: editorial decision, not mathematical doubt

The bracket concluding “mais on s'en fout” declines to develop a stronger observation. Record it as an editorial or unpursued implication rather than a conjecture or a failed proof. The proof of Proposition3 itself is absent from this face, and printed pages40–42 are not supplied in this typescript sequence.

### V04. Scan039, Proposition1 proof: fundamental inequality

The linear-independence proof is the standard argument for
\([\Gamma_{v'}:\Gamma_v][\kappa(v'):\kappa(v)]\leq[L:K]\)
for a finite field extension with a chosen valuation extension. The Stacks Project, Lemma15.125.2, Tag0ASH, gives precisely this inequality and the same product of representatives of value cosets and linearly independent residues. The text establishes an inequality for one extension; it does not assert equality, defectlessness, or the stronger sum over all extensions.

**Reading caution:** the coefficient subscripts in equation(3) simplify relative to the preceding double indices. They can be retained as a reading question without changing the formula or declaring the argument invalid. **Context:** cote16scan052 invokes complete DVR extensions for a different construction; its stronger local setting should not be silently imported here. **Confidence:** high.

### V05. Scans039→037, Proposition2: algebraic, not necessarily finite, extensions

Taking unions of finite subextensions yields torsion of \(\Gamma_{v'}/\Gamma_v\) and algebraicity of the residue extension. One must retain “torsion,” not replace it by “finite,” in this general algebraic case. The finiteness statements are exactly those of Proposition1 / Stacks Tag0ASH applied to each finite subextension.

**Context:** no duplicate result found in the four cotes. This is foundational valuation material, not an answer to any open RESULTS_STATE entry.

### V06. Scan037, Corollary1: ordered-group lemma and a proof qualification

The intended lemma is correct: for an inclusion of totally ordered abelian groups \(G\subset G'\) with torsion quotient, intersection gives an order-preserving bijection of convex (“isolated”) subgroups, hence preserves valuation rank. For injectivity, if convex \(H'_1\subset H'_2\) have equal intersections with G and \(x\in H'_2\), choose \(n>0\) with \(nx\in G\); then \(nx\in H'_1\), while the ordered quotient \(H'_2/H'_1\) is torsion free, so \(x\in H'_1\). For surjectivity, the convex hull of a convex subgroup H of G in G' intersects G in H.

**Precise issue in the written proof:** equality of intersections gives an evident *quotient of a subgroup* of \(G'/G\), not directly the displayed assertion that \(H'_2/H'_1\) is isomorphic to a subgroup of \(G'/G\). More explicitly, \(H'_2/(H'_2\cap G)\) embeds in \(G'/G\), and \(H'_2/H'_1\) is a quotient of it because \(H'_2\cap G=H'_1\cap G\subset H'_1\). Torsion passes to quotients, so the argument is repaired immediately; this is a qualification of the intermediate justification, **not a counterexample to the corollary**. Alternatively the preceding nx argument avoids the subgroup sentence entirely. **Confidence:** high by direct group argument.

### V07. Scan037 bracket asking whether to extract the lemmas

The question about “dégager ... les lemmes sur les groupes ordonnés” is organizational. Extracting the lemma in V06 makes the rank invariance independent of valuation terminology and supplies exactly the explanation the bracket requests. No counterpart found in context; no result-register status changes.

### V08. Scans037→035, Corollary3: finite extension is indispensable for discreteness

The finite-index argument correctly preserves value group Z under a finite extension. Algebraic extension alone preserves rank but need not preserve discreteness: in characteristic zero, take \(K=k((t))\) and the compatible algebraic union \(L=\bigcup_n k((t^{1/n!}))\). The extended value group is Q, so the valuation remains rank one but is not discrete. This is an independent counterexample demonstrating the exact role of “finie”; it is not an objection to the written corollary.

**Context:** cote16scan052's tame Kummer plan uses finite extensions of complete DVRs and is consistent with this distinction. Its extraction-of-a-root statement is a later, more specialized problem. **Confidence:** high.

### V09. Scan035 opening bracket: internal numbering / editorial order

The statement that the corollary could be deduced directly from Proposition1 but is more naturally left with the other corollaries is an editorial preference. The bracket names “cor.2 et3” while physically following Corollary3; preserve the source numbering rather than silently normalizing it. No mathematical uncertainty follows solely from the bracket.

### V10. Scans035→033, Proposition4 and Lemma1: existence of a place

The proof reduces extension of a ring map to the existence of a k-place of an arbitrary field extension of an algebraically closed field k, and uses a maximal partial place. In the transcendental step evaluation at zero extends the place to one transcendental generator; in the algebraic step the image residue extension is algebraic, hence contained in k. This is a genuine Zorn argument, unlike the finite-dimensional arguments earlier; the finite-type hypothesis of a closed-point theorem should not be inserted as a replacement.

**Primary background:** Stacks Lemma10.50.2, Tag00I8 section, supplies valuation domination by Zorn; Lemma10.50.10 gives composition of valuations via the residue field. These support the mechanism, but do not by themselves reproduce the manuscript's exact proposition. **Context:** no direct second witness found; the algebraically closed base used in cote54 is not itself a substantive link to this place-extension theorem. **Confidence:** high in the proof structure, no claim of novel theorem.

### V11. Scan033 large editorial paragraph: proof exists; arrangement remains open

The paragraph asks whether the subsection should occur earlier, whether a direct proof of Proposition3 is worth giving, and whether Proposition4 retained at Samuel's insistence should survive. Its last parenthesis distinguishes the proposition's fate from Samuel's. These are decisions about exposition and selection, not evidence that Proposition4 is unproved: its proof has just been supplied across scans035 and033. Attribution should remain “the typescript's rédacteur,” because the paragraph does not establish individual authorship.

### V12. Scans033→031, Proposition5(a): number of extensions

The result \(1\leq r\leq[L:K]\) counts distinct prolongation valuation rings. The proof first establishes **incomparability**, using a convex subgroup H whose intersection with the base value group is zero and whose injection into the finite quotient forces H=0. It then uses the residue-separation corollary on scan029 to obtain linearly independent elements. Calling these valuation extensions “independent” would add a false general assertion in higher rank.

**Own completion of the cut-off linear-independence argument:** normalize the coefficient of minimum base valuation to 1, reduce the relation in the residue field of that selected extension, and use the chosen value pattern to get 1=0. This completes only the visible bound argument; it does not supply the absent proofs of(b),(c).

### V13. Scan031, Proposition5(b),(c): integral closure and localizations

The statements identify the intersection B with the integral closure and the distinct prolongation rings with B localized at its maximal ideals. The selected face does not finish even the bound proof and therefore does not include proofs of these later parts. Record “proof not present in supplied continuation,” rather than claiming the full underlying typescript never proves them.

**Primary related checks:** Stacks Lemma10.50.11 characterizes a normal domain as an intersection of dominating valuation rings; its scope alone is narrower than the full finite-extension localization correspondence here. Do not cite it as though it states all of Proposition5. The exact general finite-extension theorem is classical, but I have not independently opened a primary text containing the complete(b),(c) in precisely this form. **Context:** related to the normalization/DVR agenda of cote16scan052; no duplicate in the supplied context.

## 3. n°276: prioritized evidence and checks

### A01. Scan020, Artin–Rees proof stops mid-construction

The source states the usual Artin–Rees equality for a finite module E over commutative noetherian A and a submodule F, then starts the Rees algebra/module proof. Stacks Lemma10.51.2 (section Tag00IJ) gives the same equality and proof method. Homogeneous finite generation of the induced graded submodule supplies the missing continuation; the absence of printed21 here is a gap in the packet, not evidence of an unresolved theorem.

**Genuine context link:** cote44scan003 (cancelled) asserts flatness and exactness of completion of graded modules. Artin–Rees supplies the filtration comparison used in the noetherian finite-module form of that mechanism. Also cote16scan056 has a completion criterion for étaleness. Neither link is an earlier form of the cycle theorems of cote44.

### A02. Scan022, completeness versus separation

Proposition4's series criterion uses the ultrametric structure of a filtered group. The corollary allowing every quotient to be complete is not refuted merely by a nonclosed submodule: the following scan024 explicitly allows nonseparated complete rings. The quotient has its quotient filtration; adding a Hausdorff requirement would change the convention. The concluding reference to “proposition1” is an internal cross-reference question, because the series criterion on this face is Proposition4.

### A03. Scan024, product-filtration indices

With a decreasing filtration, the displayed containment with \(p,q\leq n\) is false in general: let \(A=k[[t]]\), \(A_n=t^nA\), E=F=A, p=q=0, n=1; it asserts \(A^2\subset tA^2\). The cofinal containment is obtained for p,q≥n; indeed the middle term equals \(A_nE\times A_nF\) with the usual module-product definition. This is an independent mathematical check of the frozen reading, not permission to change it. **Confidence:** high.

### A04. Scans024→026, formal power series

The coefficient criterion for \((\mathfrak m,X)^p\) uses only finitely many coefficients of any given series, so the proposition does not need a hidden finite-generation assumption on \(\mathfrak m\). The resulting topology is coefficientwise convergence in the \(\mathfrak m\)-adic topology, matching the pencilled instruction. Nonseparatedness explains why the author chooses “one” sum for each coefficient. With \(\mathfrak m=0\), any coefficient ring gives a separated complete formal-series ring for its variable ideal.

**Context:** cote44scan003's product of homogeneous pieces is a related completion construction, but requires its stated grading/adic comparison and should not be collapsed into this assertion.

### A05. Scan026, Proposition6 and the missing printed12

The visible hypotheses are completeness of source, separation of target, and surjectivity on associated graded modules. Under the usual exhaustive decreasing filtration conventions, successive correction produces a lift in each filtration piece, giving a surjective strict map; the conclusion lies after the supplied face and must be presented as an editorial reconstruction, not an observed sentence. The missing earlier filtration conventions also should be acknowledged before applying this outside the intended setting.

**Independent proof:** for y∈F_n choose x_n∈E_n with residual inF_(n+1), repeat, sum the source corrections by completeness, and use target separation to make the residual zero. This is the same lifting mechanism used in the proof of Stacks Lemma10.97.5, although that lemma is stated for adic completion/noetherianity rather than arbitrary filtered morphisms.

### A06. Scan049, graded generators / topological Nakayama

The finite-generating conclusion uses complete coefficients and a separated target, without initially assuming that target module is finite. Separation is essential: A=k[[t]], E=k((t)), m=(t) gives E/mE=0 but E≠0, so even the empty generating family of the quotient cannot generate E. The opening congruence lacks an explicit summation sign while the following expression includes one; preserve this as a reading question.

### A07. Scans047→045, enveloping algebra: finite generation missing locally

Corollary5 as an isolated statement is false for arbitrary Lie algebras over a commutative noetherian base. For an infinite-dimensional abelian Lie algebra \(\mathfrak g=\bigoplus_{i\geq1} k e_i\), its enveloping algebra is \(k[x_1,x_2,\ldots]\), with strictly ascending ideals \((x_1)\subset(x_1,x_2)\subset\cdots\). Finite generation of g **as a K-module** suffices: grU(g) is a quotient of Sym_K(g), hence of a finite-variable polynomial ring over K, and filtered noetherianity follows. Freeness/projectivity of g is not needed for this surjection; PBW isomorphism would be more than required.

**Caveat:** a missing global convention restricting g could repair the statement; the supplied face does not state one. Do not claim that finite generation as a Lie algebra suffices, or that the correction is a proved necessary-and-sufficient classification in arbitrary generality. Sierra and Walton (2014, introduction after Conjecture0.1) explicitly confirm the finite-dimensional field case, and their Theorem0.5 supplies a much stronger nonnoetherian infinite-dimensional example if one is desired. The elementary abelian example already settles the local missing hypothesis.

### A08. Scan047, noetherian power-series corollaries and editorial marks

The noetherian-base hypothesis in Corollary2 is correct, and iterating it yields the multivariable statement over every commutative noetherian base, so “field” in Corollary3 is sufficient but stronger than necessary. The question mark, ellipse, and the statement that the preceding proof has no decisive advantage over the classical proof are evidence of editorial evaluation. They do not identify a particular intended correction unless the manuscript says so.

### A09. Scans045→043, completions of quotients and strict maps

The exactness assertion is false for merely continuous morphisms: \(\mathbb Q_{discrete}\to\mathbb Q_{usual}\to0\) is an exact sequence of metrizable groups, but completion gives \(\mathbb Q\to\mathbb R\to0\), not exact at R. Strictness (the quotient topology agreeing with the image topology) is sufficient; in a Hausdorff exact sequence the kernel is closed, and completion respects the resulting quotient and closed-embedding factorization. The distinction between “représentations” and “homomorphismes topologiques” in the typescript suggests the older strict convention; it should be checked rather than accusing the author of omitting a condition he may already encode.

**Extra caution about the final sentence:** strict morphisms do not compose in complete generality. The inclusion \(\mathbb Z\to\mathbb R\), n↦nα with α irrational, and the quotient \(\mathbb R\to\mathbb R/\mathbb Z\) are strict, but their composite has a dense non-discrete image and is not strict. The specific exact-sequence argument can be justified by the quotient/closed-embedding factorizations without this overly broad closure assertion. **Confidence:** high in both counterexamples; historical terminology interpretation is medium and remains a reading/context question.

### A10. Scans045,041: target hats and completed scalars

The completion passage writes Ehat→H in a setting suggesting the completed target Hhat; the later maps make the expected target clear but do not authorize correcting the source. Scan041 similarly includes a topology clause with A where nearby notation is Ahat. These are reading questions only. The substantive quotient isomorphisms and associated-graded isomorphism are compatible with the completion mechanism already discussed.

### A11. Exactness and faithful-flatness connection to cote44

The supplied context notes already discuss cote44scan003 as entries44:3:1–5 and supplementD07. Stacks Lemmas10.97.1–2 say that noetherian completion is exact on finite modules, agrees with tensoring by the completed ring, and is flat; they do not say that arbitrary modules have faithful completion. The existing context counterexample A=k[x], I=(x), M=A/(x−1) is correct, since x−1 becomes a unit in k[[x]]. The graded TF restriction on the cancelled cote44sheet therefore matters; no proposed expansion of TF has been independently confirmed.

## 4. Oda: exact verification and limits

The supplied `Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf` has 74 physical PDF pages. Physical PDF page70 is printed131; that page was rendered and visually read. Text extraction was used only for this printed article, never for manuscript scans.

**Verified statement.** Oda (1969), Corollary5.11, printed131, treats an abelian scheme over a perfect field k of characteristic p and supplies a canonical isomorphism of left Dieudonné-ring modules
\[M({}_pX)\simeq H^1_{DR}(X).\]
It identifies the submodule \({}_F M({}_pX)=V M({}_pX)\) with \(H^0(X,\Omega_X^1)\), retains the Frobenius twist in its identification with the Frobenius-kernel module, and identifies the resulting exact sequence with
\[0\to H^0(X,\Omega_X^1)\to H^1_{DR}(X)\to H^1(X,\mathcal O_X)\to0.\]
The remark says this was conjectured in Grothendieck[15]. Corollary5.12 on the same page gives a related injection for smooth proper varieties with a rational point, with image specified by operators; its generality must not be replaced by an isomorphism for every smooth proper variety.

**Exact context relation.** In `MPL_16+47+54+44_transcription.tex`, cote54scan003 displays the Hodge extension and universal vector extension; scan005 discusses Cartier duality / Frobenius-kernel orthogonality; scan007 ends by asking whether its restricted Lie extension can be recovered from the p-torsion group scheme. The context notes already record this in supplementD03–D05, especially D05. Oda verifies reconstruction of the canonical filtered de Rham/Dieudonné module under the perfect-field hypothesis, not from the abstract group of geometric points. Matching the particular restricted Lie extension still requires its semilinear operation and variance conventions, exactly as the existing D05 cautions.

None of the n°276 or n°272 typed pages supplies a new Oda-style comparison. Their Lie-algebra noetherianity assertion concerns ordinary enveloping rings and is not a height-one group-scheme statement. The Oda article provides no second cote47 Fourier-compatibility check and no earlier form of the cycle-theoretic cote44Th.1–7. This is a genuine context54 bridge, not a solution of WG2§2.4#4.

## 5. RESULTS_STATE handling

- **WG2 §1.1 #3:** positive archival-organization contribution from the two independent reused typescript sequences; no dating or authorship inference.
- **WG2 §2.4 #4:** negative scoped evidence: the typed pages and Oda comparison do not answer the two specific witness questions.
- **WG2 §2.3 #12 / WG H9:** no mathematical advance from these elementary algebra and valuation typescripts; do not claim the repeated theorem numbers refer to the cycle statements.
- **Hua, findings register, 62-triples-rigidified-moduli:** this agent checks only the fact that several scans in its range are unrelated typed sheets; the substantive moduli claim belongs to the other agent.
- **LM7 E.30:** its abstract rational / continuous Q_l relative completion is a different construction from completion of filtered modules or uniform abelian groups here. No implication is asserted.
- Other LM “proved” or “open” entries were read as statuses of the supplied returns, not independently accepted theorems; this report changes none of them.

## 6. Verified literature and reopening locators

All web literature cited here is a primary research paper or the official Stacks Project. The Bourbaki locator below is verified through an explicit reference in a primary research paper, not by opening the book's theorem itself.

1. Anscombe, S., Dittmann, P., & Fehm, A. (2020). Approximation theorems for spaces of localities. *Mathematische Zeitschrift, 296*, 1471–1499. https://doi.org/10.1007/s00209-020-02516-6 . Official full text: https://link.springer.com/article/10.1007/s00209-020-02516-6 . Theorem1.2, footnotes2,4, and§5.2. Tool refs `turn17view0`, `turn18view2`. Bourbaki reference: *Commutative Algebra*, Chapters1–7 (1989), VI.7.2, Theorem1. Keep derived exposition from this web source under its 200-word limit in the delivered notes; the longer independent examples above are this agent's calculations.
2. Oda, T. (1969). The first de Rham cohomology group and Dieudonné modules. *Annales scientifiques de l'École Normale Supérieure, 4e série, 2*(1), 63–135. https://doi.org/10.24033/asens.1175 . Official metadata: https://numdam.org/articles/10.24033/asens.1175/ . Supplied PDF printed131/PDF70 was checked directly. DOI ends **1175**, not1170.
3. Sierra, S. J., & Walton, C. (2014). The universal enveloping algebra of the Witt algebra is not noetherian. *Advances in Mathematics, 262*, 239–260. https://doi.org/10.1016/j.aim.2014.05.007 . Author manuscript: https://www.pure.ed.ac.uk/ws/portalfiles/portal/30927140/1304.0114v3.pdf . Introduction following Conjecture0.1 and Theorem0.5; tool ref `turn20view0` (PDF page2 is article page1; repository cover first). No assertion about the current status of its broader conjecture is needed.
4. The Stacks Project Authors. (2026). *More Noetherian rings*, Lemma10.51.2 (Artin–Rees). https://stacks.math.columbia.edu/tag/00IJ . Tool ref `turn7view0`.
5. The Stacks Project Authors. (2026). *Completion for Noetherian rings*, Lemmas10.97.1–2 and10.97.5–6. https://stacks.math.columbia.edu/tag/0BNH . Tool ref `turn7view1`; direct finite-module exactness and lifting/noetherianity verification.
6. The Stacks Project Authors. (2026). Lemma15.125.2 (fundamental inequality). https://stacks.math.columbia.edu/tag/0ASH . Tool ref `turn15view0`.
7. The Stacks Project Authors. (2026). *Valuation rings*, Lemmas10.50.2,10.50.10,10.50.11 and Definition10.50.13. https://stacks.math.columbia.edu/tag/00I8 . Tool ref `turn22view0`.

## 7. Verification limits

This report is evidence for the root's notes, not replacement transcription and not a second image audit. Mathematical counterexamples and the ordered-group proof were independently checked by reasoning; no claim of novelty is made. The full general localization correspondence in n°272Proposition5(b),(c), historical meaning of “homomorphismes topologiques,” and the undefined TF in the cancelled cote44sheet have not been independently resolved from an exact primary edition. The report intentionally distinguishes these limits from the claims directly proved or verified above.

## 8. Review of the root's draft D01–D22 / E01

Read the full requested draft section without editing it. Two concrete corrections were sent to the root:

1. **D07:** E/E_n are discrete filtration quotients; they are not necessarily finite sets or finite modules. Use “filtration quotients” or “finite-level quotients,” and avoid “The finite quotients ...” without qualification.
2. **D16:** the bound r≤[L:K] on the number of prolongations is not logically weaker than the bound ef≤[L:K] for one prolongation. These are distinct estimates; neither of these bare inequalities supplies the other. Remove “and weaker than” or compare both to the full sum inequality, if separately stated with appropriate hypotheses.

D19's direct nx argument correctly repairs the intermediate ordered-group justification. D08–D09 correctly keep the strictness counterexamples separate from historical terminology. D11 correctly specifies finite generation as a module rather than as a Lie algebra. E01's perfect-field / characteristic-p restriction and distinction between filtered cohomology and the particular restricted-Lie extension agree with Oda's printed Corollary5.11. No other concrete mathematical error was found in the requested section.
