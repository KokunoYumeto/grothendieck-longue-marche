# Research-note draft: mathematical scans 146–170

This post-freeze research draft was made from the frozen TeX, never from images and never by changing the transcription. File names below refer to `pages/`; line numbers are approximate TeX line numbers, not manuscript line numbers. The relevant supplied comparison is **Hua, findings register, 84-chi-trivialised-extension-product**, reproduced in `context/notes/RESULTS_STATE.md`, “Findings of another project”; its status is **conjecture/candidate, AI-produced, unverified**, and its cited source range includes our scans 146–170 as an aggregate rather than locating individual formulas. Its other cited page ranges lie outside this packet, so absence here does not refute what those other pages may contain.

Per-item searches are recorded in `records/context_queries_early.json`. All three context files were searched, including `LM2_CONGRUENCE_ROWS.md`; the GT/congruence entries do not settle any of these extension-calculus assertions merely because they also contain words such as “extension,” “matrix,” or “tensor.” The notation `E_1\wedge E_2` and `E_1\vee E_2` is treated here as the manuscript’s named operations, not silently identified with exterior powers or ordinary direct sums.

## E146.1 — The multiplicative coefficient is a local assertion

**File/scan/lines:** `MPL_84_146-193_84_scan146.tex`, 146, 13 and 31–37. **Kind:** unproved claim. **Context comparison:** adds explicit local evidence to Hua, findings register, **84-chi-trivialised-extension-product**; no matching settled context entry.

The circled “\(b=b_1b_2\)” is accompanied by the changes “\(b'_1=b_1+\unsure{\chi|\gamma}u_1\)” and “\(b'_2=b_2+\unsure{\chi|\gamma}u_2\),” so a proof must check independence of splittings rather than simply multiply two chosen coordinates. This supports the local coefficient part of Hua’s claim, while the tensor interpretation requires the indicated Hom domains and the surviving doubt over the scalar to be respected. It does not itself construct associativity, a unit, or an inverse.

## E146.2 — The two displayed matrices do not require division by two

**File/scan/lines:** `MPL_84_146-193_84_scan146.tex`, 146, 5–9. **Kind:** unpursued implication. **Context comparison:** adds a concrete integral calculation to Hua, **84-chi-trivialised-extension-product**; no matrix identity with these entries was found elsewhere in the supplied context.

For the two displayed matrices “\(\begin{pmatrix}2&0\\-b_1&0\end{pmatrix}\)” and “\(\begin{pmatrix}0&0\\b_1&2\end{pmatrix}\),” direct multiplication gives sum \(2I\), both cross-products zero, and squares equal to twice the respective matrix. These are integral identities, but replacing either matrix by half of itself to obtain an idempotent would require an additional hypothesis. `early_formula_checks.py` verifies the four identities without deciding the doubtful names of the operators.

## E146.3 — A residue class is a useful, limited invariant

**File/scan/lines:** `MPL_84_146-193_84_scan146.tex`, 146, 31–37. **Kind:** own idea. **Confidence:** high for the conditional algebraic observation, because the polynomial identity is checked exactly; no claim of novelty. **Context comparison:** refines only the local coefficient clause of Hua, **84-chi-trivialised-extension-product**.

If the scalar in “\(b'_i=b_i+\unsure{\chi|\gamma}u_i\)” is \(\chi\), then \(b'_1b'_2-b_1b_2=\chi(u_1b_2+b_1u_2+\chi u_1u_2)\), so the product is independent of this change modulo \(\chi\). This suggests separating a residue invariant on \(V(\chi)\) from a globally defined product extension and its coherence data. The computation is compatible with the locus occurring in Hua’s invertibility statement, but neither a section called \(T_0\) nor that invertibility criterion occurs in this interval.

## E148.1 — The involution ansatz imposes a scalar condition

**File/scan/lines:** `MPL_84_146-193_84_scan148.tex`, 148, 5–23. **Kind:** unproved claim. **Context comparison:** qualifies the scope of the local evidence for Hua, **84-chi-trivialised-extension-product**.

The substitutions “\(\sigma_i=\mathrm{id}_i-\gamma\pi_i\)” lead to the boxed “\(\gamma\chi=2\),” with \(\beta=-1\) and \(\alpha=\chi\). This is a condition on this particular representation of the comparison operator and cannot be treated as a universally available choice over an arbitrary base. Conversely, failure to choose such a \(\gamma\) would not by itself disprove a different all-\(\chi\) construction of the kind claimed in Hua’s register.

## E148.2 — Three equations in the second ansatz require compatibility

**File/scan/lines:** `MPL_84_146-193_84_scan148.tex`, 148, 30–41. **Kind:** unproved claim. **Context comparison:** adds an explicit proof obligation absent from Hua, **84-chi-trivialised-extension-product**.

The underlined system “\(\lambda^2+1=\chi\), \(\lambda\mu=-1\), \(\mu^2=\gamma\)” implies \(\gamma(\chi-1)=1\), without cancelling \(\chi\). If this system is imposed together with the earlier \(\gamma\chi=2\), it forces \(\gamma=1\) and \(\chi=2\), although the page does not establish that both ansätze must be imposed simultaneously. The symbolic check records the implication, not a correction of the author’s formulas.

## E148.3 — The endomorphism sheaf is only partially defined here

**File/scan/lines:** `MPL_84_146-193_84_scan148.tex`, 148, 43–59. **Kind:** unproved claim. **Context comparison:** same extension objects as Hua, **84-chi-trivialised-extension-product**, but no matching description of this sheaf in the supplied context.

The phrase “\(\mathcal H_i=\text{\unsure{noyau} de}\)” is unfinished, followed by the purported sequence from \(\operatorname{Hom}(M,L)\) through \(\mathcal H/\mathrm{id}\) to \((\mathcal O\times\mathcal O)/\mathcal O\). To assess exactness one must specify the omitted map, the action on both ends of the extension, and whether surjectivity is local or global. Hua’s category-level summary does not supply those missing definitions.

## E148.4 — The trace-like involution needs its algebraic setting

**File/scan/lines:** `MPL_84_146-193_84_scan148.tex`, 148, 63–66. **Kind:** unpursued implication. **Context comparison:** possible additional structure on the objects in Hua, **84-chi-trivialised-extension-product**; no equivalent result found in context.

The identity “\(u+\sigma(u)=\unsure{(\lambda(u)+\mu(u))}\mathrm{id}\)” resembles the trace-plus-conjugate identity later used on scans 160 and 172. It gives a candidate trace scalar, but this line alone does not prove multiplicativity or anti-multiplicativity of \(\sigma\), nor identify \(\mathcal H\) with a quadratic algebra. Those extra properties must be checked in the actual endomorphism algebra rather than inferred from the notation.

## E150.1 — Compatibility is explicitly crossed out

**File/scan/lines:** `MPL_84_146-193_84_scan150.tex`, 150, 3–7. **Kind:** withdrawn in the same text. **Context comparison:** a caution for Hua, **84-chi-trivialised-extension-product**; the relevant words are already cancelled on scan 150.

The line beginning “Mais” and containing “\unsure{une} \unsure{compatibilité} \unsure{avec la} \(\unsure{\pi|\tau}\)-\unsure{trivialisation}” is struck through, together with the adjacent candidate diagram. It therefore records an abandoned formulation, not an accepted compatibility theorem. The later construction on scan 170 must be assessed on its own explicit conditions.

## E150.2 — The displayed double-conjugation check specializes to two

**File/scan/lines:** `MPL_84_146-193_84_scan150.tex`, 150, 16–29. **Kind:** unproved claim with a displayed local check. **Context comparison:** supports the \(\chi=2\) part of an extension comparison, not the unrestricted quantifier in Hua, **84-chi-trivialised-extension-product**.

The calculation ending “\(=x_1\)” explicitly places \(2\) beneath \(\chi\), while the page also writes “\(\pi(\pi-\chi)=0\).” Under that latter relation, the map \(s=1-\pi\) satisfies \(s^2-1=(\chi-2)\pi\), so involutivity follows at \(\chi=2\) but need not hold for arbitrary \(\chi\). This explains why the scalar hypothesis must remain visible in any interpretation of the norm-like tensor formula.

## E152.1 — A false intermediate equality is corrected and checked

**File/scan/lines:** `MPL_84_146-193_84_scan152.tex`, 152, 15–16. **Kind:** withdrawn in the same text / self-check completed. **Context comparison:** supplies an explicit internal correction not reported in Hua, **84-chi-trivialised-extension-product**.

The author cancels “\(2\chi=\chi\)” and writes “\(\chi=\chi\quad\text{o.K.!}\).” The preceding polynomial \(-\chi(1-\gamma\chi)+2(1-\gamma\chi)\chi+\gamma\chi^2\) is indeed identically \(\chi\), as the accompanying script checks. This verifies that scalar restriction only, not every compatibility of the full extension map.

## E152.2 — The boxed condition has an uncertain cancelled reading

**File/scan/lines:** `MPL_84_146-193_84_scan152.tex`, 152, 19 and 32–47. **Kind:** reading question / withdrawn in the same text. **Context comparison:** relevant to the all-\(\chi\) wording of Hua, **84-chi-trivialised-extension-product**, without resolving the frozen doubt.

The cancelled box is transcribed “\(\unsure{2=\chi|2\ne\chi}\),” whereas the subsequent live text includes “\(\gamma\chi=2\)” and the explicit choice “\(\chi=2\qquad\gamma=1\).” Neither the context nor the surrounding mathematics licenses selecting an unmarked reading of the cancelled sign. The live specialization is secure evidence for the calculation’s chosen case, rather than evidence that the cancelled formula states a general obstruction.

## E152.3 — The norm-like tensor formula is cancelled, then checked later

**File/scan/lines:** `MPL_84_146-193_84_scan152.tex`, 152, 57–77; `MPL_84_146-193_84_scan156.tex`, 156, 39–42. **Kind:** withdrawn in the same text, subsequently revisited. **Context comparison:** adds the chronology of one local calculation to Hua, **84-chi-trivialised-extension-product**.

The final expression “\(x_1\otimes x_2+(\overline{x}_1\otimes\overline{x}_2)\)” is struck through on scan 152, but the same target expression appears live with “o.K.” on scan 156. The latter verification uses the special coefficients \((2,-1,-1,1)\) and the relation between \(\pi_i\) and conjugation. The cancellation therefore should not be read as a permanent retraction of that specialized identity.

## E154.1 — Three matrix entries remain explicitly questioned

**File/scan/lines:** `MPL_84_146-193_84_scan154.tex`, 154, 34–39. **Kind:** self-flagged: unverified step. **Context comparison:** directly tests, but does not establish, the comparison asserted in Hua, **84-chi-trivialised-extension-product**.

The \(4\times4\) block table has three unresolved cells containing four “?” marks: the \(M_1\otimes M_2\) input’s components in the first three output summands. Its other entries do not determine those three maps, and the tentative “\(\tau_1\otimes\tau_2\ ?)\)” is a proposed form, not a verified coefficient. Any completed matrix in the research calculations is explicitly an interpretation, while the frozen table retains all question marks.

## E154.2 — Two compatibilities leave a Hom-valued ambiguity

**File/scan/lines:** `MPL_84_146-193_84_scan154.tex`, 154, 43–45. **Kind:** unproved claim. **Context comparison:** qualifies the word “canonical” implicit in Hua, **84-chi-trivialised-extension-product**.

The doubtful prose says the two “\unsure{homotopies|contraintes}” are compatible and leave an “\unsure{indétermination}” which is a Hom from \(M_1\otimes M_2\) to \(L_1\otimes L_2\). This is consistent with the familiar freedom to alter an extension morphism fixing its ends by a map from the quotient to the subobject, but existence and compatibility with the chosen \(\chi\)-trivialisations still require proof. In particular, the stated ambiguity cannot itself establish a unique natural comparison or monoidal coherence.

## E154.3 — The concluding explanation is too doubtful to support a theorem

**File/scan/lines:** `MPL_84_146-193_84_scan154.tex`, 154, 55–57. **Kind:** reading question. **Context comparison:** Hua, **84-chi-trivialised-extension-product**, suggests an extension-isomorphism interpretation but does not settle the reading.

The bottom paragraph includes “\unsure{iso|de} \unsure{d'extensions|déterminés}” and several further alternatives. It may explain why merely asking for an extension isomorphism leaves choices, but that interpretation must remain conditional because the frozen wording is substantially uncertain. The research claim should rest on the explicit matrices and diagrams, not a reconstructed fluent version of this paragraph.

## E156.1 — The question-marked scalar equality must not be divided by χ

**File/scan/lines:** `MPL_84_146-193_84_scan156.tex`, 156, 58–59. **Kind:** self-flagged: unverified step. **Context comparison:** an explicit restriction absent from the unrestricted wording of Hua, **84-chi-trivialised-extension-product**.

The author writes “\(-\chi(1-\delta\chi)\overset{?}{=}\chi\)” before “\(\delta\chi=2\).” The latter condition is sufficient, but the questioned equality alone is only \(\chi(\delta\chi-2)=0\), so equivalence needs a cancellation hypothesis or further coefficient conditions. This distinction matters on the locus \(V(\chi)\), which Hua’s separate invertibility assertion singles out.

## E156.2 — A completed tensor check has a limited scope

**File/scan/lines:** `MPL_84_146-193_84_scan156.tex`, 156, 13–24 and 39–42. **Kind:** self-check completed. **Context comparison:** adds checked local evidence for the special case underlying Hua, **84-chi-trivialised-extension-product**.

“Si \(\chi=2\), on \unsure{peut} prendre \(\delta=1\)” leads to the expression ending “\(x_1\otimes x_2+\bar x_1\otimes\bar x_2\qquad\text{o.K.}\).” The coefficient expansion is correct when \(\pi_i(x_i)=x_i-\bar x_i\), but one intermediate bar is itself doubtful in the transcription. The check establishes the interpreted polynomial identity, not a reading correction or a global categorical theorem.

## E156.3 — A new bar formula is left unfinished

**File/scan/lines:** `MPL_84_146-193_84_scan156.tex`, 156, 49–54. **Kind:** unproved claim / unfinished calculation. **Context comparison:** no completion found in the supplied context; related generally to Hua, **84-chi-trivialised-extension-product**.

The display “\(\overline{\unsure{X_i|x_i}}=x_i-\pi_i(x_i)=\bigl\{\)” stops at an opening brace and is followed by a partly cancelled tensor continuation. It does not supply an additional formula or case distinction that can safely be used in a proof. The preceding completed \(\chi=2\) calculation must therefore be kept separate from this abandoned continuation.

## E158.1 — Coefficient extraction needs faithfulness or universality

**File/scan/lines:** `MPL_84_146-193_84_scan158.tex`, 158, 30–46. **Kind:** unproved claim. **Context comparison:** adds a hypothesis check to Hua, **84-chi-trivialised-extension-product**; no relevant settled context result.

The transitions from “\((\alpha+\chi\gamma)\mathrm{id}=0\)” to “\(\alpha+\chi\gamma=0\),” and then to “\(\beta=\gamma\),” require justification. A faithful module gives the first implication, while the two scalar equalities \(\alpha=-\chi\gamma=-\chi\beta\) by themselves give only \(\chi(\beta-\gamma)=0\). A universal comparison of coefficients may supply the stronger conclusion, but the page does not state that argument, and scan 160 subsequently revises the module hypotheses.

## E158.2 — The final boxed equation is stronger than vanishing on one image

**File/scan/lines:** `MPL_84_146-193_84_scan158.tex`, 158, 63–79. **Kind:** unproved claim. **Context comparison:** a further local proof obligation for Hua, **84-chi-trivialised-extension-product**.

“\((\beta+\delta\chi-1)\pi_2(x_2)=0\)” is followed by the box “\(\beta+\delta\chi=1\).” This follows for a universal identity in independent matrix entries, or if the image being annihilated is faithful, but not from an arbitrary single map \(\pi_2\). The final formulas \(\beta=\gamma=1-\delta\chi\) and \(\alpha=-\chi(1-\delta\chi)\) should accordingly be read as the proposed coefficient family with its proof conditions made explicit.

## E160.1 — The module hypotheses are revised

**File/scan/lines:** `MPL_84_146-193_84_scan160.tex`, 160, 8–10. **Kind:** withdrawn in the same text. **Context comparison:** supplies a hypothesis missing from the short summary of Hua, **84-chi-trivialised-extension-product**.

The margin begins “\(L_1,L'_1\) \unsure{qcq} \unsure{ici.}” and immediately responds “\unsure{non.} Mais \unsure{suppos.} \(L'_1,L'_2\) loc. libres de rang fini.” This is evidence of an authorial restriction, not permission to state the later duality for arbitrary modules. The precise scope of local freeness on the other terms still has to be checked against the construction and any earlier pages outside this packet.

## E160.2 — The claimed duality requires a perfect pairing

**File/scan/lines:** `MPL_84_146-193_84_scan160.tex`, 160, 27–38. **Kind:** unproved claim. **Context comparison:** additional duality structure not stated in Hua, **84-chi-trivialised-extension-product**.

“Je dis que” introduces \(E_1^\vee\wedge E_2^\vee\simeq(E_1\wedge E_2)^\vee\), followed by a tensor–Hom identification. A proof must construct the displayed pairing, show it descends to the named extension products, and establish its perfection under the actual finite-projectivity hypotheses. The notation alone does not let one replace this with the standard duality of an ordinary tensor product.

## E160.3 — The barred and primed operators should not be conflated

**File/scan/lines:** `MPL_84_146-193_84_scan160.tex`, 160, 61–85; `MPL_84_146-193_84_scan162.tex`, 162, 4–16. **Kind:** reading question. **Context comparison:** Hua, **84-chi-trivialised-extension-product**, gives no convention resolving these local operator distinctions.

Scan 160 writes “\(\sigma(x)=\operatorname{Tr}(x).1-x\)” and boxes “\(x_1\otimes x_2+\pi'_1(x_1)\otimes\pi'_2(x_2)\),” while scan 162 defines \(\pi'(x)=\pi(x)-(\chi-1)x\). These operators can be related in the special case under discussion, but the notebook’s changes of notation and signs are not a licence to normalize the frozen primes, bars, or \(\sigma\) symbols. A rigorous reconstruction should state each chosen convention before comparing pairings.

## E162.1 — The shifted operator exposes the exceptional scalar

**File/scan/lines:** `MPL_84_146-193_84_scan162.tex`, 162, 4–30. **Kind:** unpursued implication. **Context comparison:** qualifies the all-\(\chi\) reading of Hua, **84-chi-trivialised-extension-product**.

The author’s \(\pi'=\pi-(\chi-1)\mathrm{id}\) restricts to the identity on \(L\), and the displayed tensor calculation leaves “\((\unsure{2}-\chi)x_2+\pi_2(\unsure{x_2})\).” Thus the candidate \(\mathrm{id}+\pi'_1\otimes\pi'_2\) has an extra \((2-\chi)\) term on the mixed tensor summand, disappearing in the \(\chi=2\) case. This is concrete evidence that the simple involution formula does not automatically provide the comparison for every scalar.

## E162.2 — The tensor endomorphism is still a question

**File/scan/lines:** `MPL_84_146-193_84_scan162.tex`, 162, 39–46. **Kind:** self-flagged: unverified step. **Context comparison:** the construction sought is related to Hua, **84-chi-trivialised-extension-product**, but the context adds no formula at this location.

The thick top arrow between the tensor terms is labelled “?”. Its factorization through \(E\), and compatibility with the amalgamated sum below, are precisely what need to be constructed rather than assumed. The four-term polynomial at the foot of the page is an ansatz for this problem, not a finished proof.

## E162.3 — The central lifting map is separately questioned

**File/scan/lines:** `MPL_84_146-193_84_scan162.tex`, 162, 48–54. **Kind:** self-flagged: unverified step. **Context comparison:** bears on the comparison part of Hua, **84-chi-trivialised-extension-product**.

In the three-row extension diagram the middle downward arrow from \(E\) into \(E_1\otimes E_2\) bears “?”, with the right downward map labelled \(\chi\mathrm{id}\). A proof must check this specified map on the quotient as well as its restriction on the left term; verifying only the upper pushout does not suffice. This question is distinct from merely choosing a tensor endomorphism in the preceding diagram.

## E164.1 — The complementary matrices supply an integral decomposition

**File/scan/lines:** `MPL_84_146-193_84_scan164.tex`, 164, 3–19. **Kind:** unpursued implication. **Context comparison:** adds explicit matrices for the splitting data in Hua, **84-chi-trivialised-extension-product**.

The first table is headed “\(\pi'_i\)”; the two tables give \(P_i=\begin{pmatrix}\chi&\tau_i\\0&0\end{pmatrix}\) and \(Q_i=\begin{pmatrix}0&-\tau_i\\0&\chi\end{pmatrix}\), whatever the doubtful name of the second operator. They satisfy \(P_i+Q_i=\chi I\) and \(P_iQ_i=Q_iP_i=0\), including where \(\chi\) vanishes. As on scan 146, these identities do not justify dividing by \(\chi\) to obtain complementary projections.

## E164.2 — The coefficient table tests only three tensor summands

**File/scan/lines:** `MPL_84_146-193_84_scan164.tex`, 164, 34–63. **Kind:** unproved claim. **Context comparison:** supplies partial coefficient tests for Hua, **84-chi-trivialised-extension-product**.

The four operator rows “\(1,\pi'_1,\pi'_2,\pi'_1\otimes\pi'_2\)” contain three data columns, followed by the boxed equations \(\alpha+(\beta_1+\beta_2)\chi+\gamma\chi^2=\chi\), \(\alpha+\beta_1\chi=0\), and \(\beta_2+\gamma\chi=1\). The missing fourth input summand \(M_1\otimes M_2\) is exactly where scan 154 places the unresolved entries. Consequently these partial restrictions cannot alone verify the full comparison matrix.

## E164.3 — A universal polynomial calculation isolates the remaining defect

**File/scan/lines:** `MPL_84_146-193_84_scan164.tex`, 164, 42–63; `MPL_84_146-193_84_scan154.tex`, 154, 34–39; `MPL_84_146-193_84_scan166.tex`, 166, 19–28. **Kind:** own idea. **Confidence:** high for the explicitly fixed local model, because all matrix residuals are computed exactly; no claim of novelty. **Context comparison:** a conditional test of Hua, **84-chi-trivialised-extension-product**, not a refutation of unspecified conventions.

For \(F=\alpha I+\beta_1P_1+\beta_2P_2+\delta P_1P_2\), the family \(\alpha=-\chi(1-\delta\chi)\), \(\beta_1=\beta_2=1-\delta\chi\) meets the three-summand restrictions. Against the endpoint-preserving comparison matrix, its remaining entries differ by \((2-\delta\chi)\tau_1\), \((2-\delta\chi)\tau_2\), and \(\chi(\delta\chi-2)\). Thus \(\delta\chi=2\) is sufficient, and necessary for a universal polynomial identity in independent \(\tau_i\), whereas special modules may have additional annihilators; `early_formula_checks.py` records the exact scope.

## E166.1 — Four block maps and four squares define the comparison problem

**File/scan/lines:** `MPL_84_146-193_84_scan166.tex`, 166, 3–30. **Kind:** unproved claim. **Context comparison:** gives concrete descent data for the comparison in Hua, **84-chi-trivialised-extension-product**.

“Pour définir un hom \(F\), il faut définir” introduces \(F_{11},F_{12},F_{21},F_{22}\) and the marginal “\unsure{ces} 4 \unsure{carrés} commu-\linebreak\unsure{tatifs}.” The page states the conditions \(F_{22}=0\), \(F_{21}=\alpha_1\otimes\alpha_2\), and \(F_{12}=\psi_1\otimes\psi_2\) as necessary and sufficient for successively stronger properties. The remaining block and its two nonautomatic squares still require construction; three specified blocks are not all four compatibilities.

## E166.2 — Identity on the ends is an additional requirement

**File/scan/lines:** `MPL_84_146-193_84_scan166.tex`, 166, 19–28. **Kind:** withdrawn in the same text. **Context comparison:** makes the endpoint convention essential when testing Hua, **84-chi-trivialised-extension-product**.

“l'identité” is cancelled and replaced by “un hom d'\unsure{extensions}, donc,” followed later by “de plus” before the identity condition. This distinguishes an arbitrary morphism of extensions from one fixing both identified ends, and the distinction affects whether two extensions are regarded as the same. Any counterexample or comparison with Hua must specify which of these notions it tests.

## E166.3 — Two squares are declared automatic because their composites vanish

**File/scan/lines:** `MPL_84_146-193_84_scan166.tex`, 166, 29–46. **Kind:** unproved claim with indicated verification. **Context comparison:** contributes two local checks to Hua, **84-chi-trivialised-extension-product**, without settling the remaining squares.

The text says two of the four desired squares “sont déjà commutatifs” and adds “(\unsure{les quatre} composés sont nuls).” These are the two squares involving the specified zero block and the projection or inclusion maps of the extensions. Their verification uses the usual zero composites of a short exact sequence; it leaves the two squares containing \(F_{11}\) as the substantive problem.

## E168.1 — The comparison remains marked with a question

**File/scan/lines:** `MPL_84_146-193_84_scan168.tex`, 168, 4–17. **Kind:** self-flagged: unverified step. **Context comparison:** precise local support for, and limitation on, the pushout–pullback part of Hua, **84-chi-trivialised-extension-product**.

The upper construction is marked “cocart,” the lower one “cart,” and the middle arrow \(E_1\vee E_2\to E_1\wedge E_2\) still has “?” above a cancelled doubtful \(F\). This demonstrates the intended comparison but does not prove its existence or canonicity. If the rows are exact and the end maps are identities, an existing such comparison would be an isomorphism; that conditional fact does not remove the question mark.

## E170.1 — Canonical product extensions need the tensor-exactness hypotheses

**File/scan/lines:** `MPL_84_146-193_84_scan170.tex`, 170, 4–19 and 23–36. **Kind:** unproved claim. **Context comparison:** directly supports the construction part of Hua, **84-chi-trivialised-extension-product**, with hypotheses that its short summary omits.

“On définit de façon \unsure{can.}” introduces the two extension products, while the margin calls the inclusions “\unsure{univ.} \unsure{injectfs|injectifs}.” The pushout and pullback diagrams give a concrete construction plan, but exactness of their tensor rows requires the stated universal-injectivity or suitable flatness assumptions. This is substantially more specific than an unqualified operation on every extension of arbitrary modules.

## E170.2 — A canonical comparison is asserted, but coherence is not supplied

**File/scan/lines:** `MPL_84_146-193_84_scan170.tex`, 170, 19–21. **Kind:** unproved claim. **Context comparison:** restates the intended comparison in Hua, **84-chi-trivialised-extension-product**, while leaving its symmetric-monoidal upgrade unverified here.

The bullet asserts “une \unsure{application} can. d'\unsure{extensions} de \(E_1\vee E_2\) en \(E_1\wedge E_2\).” The preceding pages expose nontrivial coefficient conditions, a Hom-valued ambiguity, and question-marked arrows; this sentence does not by itself discharge those obligations. No associator, unit constraint, symmetry constraint, or coherence diagram appears in the supplied mathematical scans 146–170. The separate editorial model in R11–R13 does verify a positive local monoidal construction and its local invertibility criterion, while leaving global identification and this particular comparison to be proved.

## E170.3 — The χ-trivialisation identities include a frozen sign doubt

**File/scan/lines:** `MPL_84_146-193_84_scan170.tex`, 170, 9–16. **Kind:** reading question. **Context comparison:** Hua, **84-chi-trivialised-extension-product**, suggests the usual splitting equations but cannot resolve the handwriting.

The displayed data include \(\alpha_i\pi_i+\varpi_i\psi_i=\chi\mathrm{id}_{E_i}\), \(\pi_i\alpha_i=\chi\mathrm{id}_{L_i}\), and “\(\psi_i\varpi_i\unsure{=|+}\chi\mathrm{id}_{M_i}\).” The research calculations below use the equality interpretation of the last line and state that convention explicitly. They do not change the frozen alternative or identify the cancelled fragments as live axioms.

## E170.4 — A conditional counterexample distinguishes equality from a sign twist

**File/scan/lines:** `MPL_84_146-193_84_scan168.tex`, 168, 9–13; `MPL_84_146-193_84_scan170.tex`, 170, 19–36; compare `MPL_84_146-193_84_scan166.tex`, 166, 19–28. **Kind:** own idea. **Confidence:** high for the explicitly specified fixed-endpoint interpretation, because the transition matrices and scalar residuals are computed; no claim of novelty or blanket refutation of Hua. **Context comparison:** conditionally contradicts the statement that the pushout and pullback products “agree” in Hua, **84-chi-trivialised-extension-product**, if that means an isomorphism inducing identities on both ends for every \(\chi\).

At \(\chi=0\), take \(L_i=M_i=\mathcal O_X\), \(\pi_i=\psi_i\), and \(\varpi_i=-\alpha_i\); the diagrams then give the Baer sum of the two extension classes for the pushout product and its negative for the pullback product. For a nonzero class \(e\in H^1(X,\mathcal O_X)\) on a smooth elliptic curve over a characteristic-zero field and a split second extension, these classes are \(e\) and \(-e\), which differ because \(2e\ne0\) (The Stacks Project Authors, n.d., Tags 0B3A and 072J). Therefore no comparison fixing both ends exists in this example, although a comparison negating the subobject does exist, so an unrecorded sign convention or restriction to \(\chi=2\) can change the verdict. The derivation below separates this precise obstruction from the existence of a product operation or a symmetric-monoidal structure, neither of which the example refutes.

## E170.5 — Canonicity requires a compatible choice across splitting changes

**File/scan/lines:** `MPL_84_146-193_84_scan146.tex`, 146, 31–37; `MPL_84_146-193_84_scan154.tex`, 154, 43–45; `MPL_84_146-193_84_scan170.tex`, 170, 19–21. **Kind:** own idea. **Confidence:** high within the explicit local model, because the change-of-basis identity is verified symbolically; no claim of novelty. **Context comparison:** refines the canonicity issue in Hua, **84-chi-trivialised-extension-product**.

Writing a local endpoint-preserving comparison as \((l,m)\mapsto(l+k(m),m)\), a change of splitting by \((u_1,u_2)\) requires \(k'-k=2t\), where \(t=u_1\tau_2+\tau_1u_2+\chi u_1u_2\). The candidate \(k=\delta\tau_1\tau_2\) changes by \(\delta\chi t\), so its gluing defect is \((\delta\chi-2)t\). This explains simultaneously the residual Hom freedom on scan 154 and the condition \(\delta\chi=2\) on scans 156–158, without promoting a choice of local matrix to a canonical global construction.

## Detailed derivation supporting E170.4–E170.5

This is a research reconstruction under explicit conventions, not missing text supplied to the edition. Let the base be a scheme or ringed space with commutative structure sheaf, let both extensions be locally split, and interpret the live splitting equations on scan 170 as

\[
0\longrightarrow L_i\xrightarrow{\alpha_i}E_i\xrightarrow{\psi_i}M_i\longrightarrow0,
\quad \alpha_i\pi_i+\varpi_i\psi_i=\chi\mathrm{id}_{E_i},\quad
\pi_i\alpha_i=\chi\mathrm{id}_{L_i},\quad\psi_i\varpi_i=\chi\mathrm{id}_{M_i}.
\]

Choose local splittings \(s_i:M_i\to E_i\), write \(E_i=L_i\oplus M_i\), and put \(\tau_i=\pi_i s_i\). Then

\[
\pi_i(l,m)=\chi l+\tau_i m,\qquad
\varpi_i(m)=(-\tau_i m,\chi m).
\]

Use the ordered four tensor summands \((L_1L_2,L_1M_2,M_1L_2,M_1M_2)\), with juxtaposition denoting tensor product. The pushout map from the first three summands to \(L_1L_2\) is \((a,b,c)\mapsto\chi a+(\mathrm{id}\otimes\tau_2)b+(\tau_1\otimes\mathrm{id})c\), so a local splitting of the pushout product is the image of \(s_1\otimes s_2\). The pullback product has a local splitting whose image in \(E_1E_2\) is

\[
w=\chi(s_1\otimes s_2)-(\tau_1\otimes s_2)-(s_1\otimes\tau_2),
\]

where the last two terms use the inclusions of the respective \(L_i\). This element has mixed and quotient coordinates \((-\tau_1,-\tau_2,\chi)\), exactly the pair prescribed by \((\varpi_1\otimes\mathrm{id},\mathrm{id}\otimes\varpi_2)\).

For new splittings \(s'_i=s_i+u_i\), one has \(\tau'_i=\tau_i+\chi u_i\). The pushout splitting changes by

\[
t=u_1\otimes\tau_2+\tau_1\otimes u_2+\chi u_1\otimes u_2,
\]

whereas expansion of the displayed \(w'\) shows that the pullback splitting changes by \(-t\). Thus, with the same identified end objects, the two resulting extension cocycles are opposite. A local comparison fixing the ends and sending the chosen pushout splitting to the pullback splitting plus \(k\) glues precisely when \(k'-k=2t\); for \(k=\delta\tau_1\otimes\tau_2\), this is the residual \((\delta\chi-2)t\) checked in the script.

For the concrete case \(\chi=0\), choose \(L_i=M_i=\mathcal O_X\), \(\tau_i=1\), and any locally free extension \(E_i\) of \(\mathcal O_X\) by itself. The globally defined maps \(\pi_i=\psi_i\) and \(\varpi_i=-\alpha_i\) satisfy the displayed splitting identities, and the inclusions are universally injective because the quotient is locally free. If the first extension has a nonzero class \(e\in H^1(X,\mathcal O_X)\) and the second is split, the computed classes are \(e\) and \(-e\). On a smooth elliptic curve over a characteristic-zero field the vector space \(H^1(X,\mathcal O_X)\) is one-dimensional (The Stacks Project Authors, n.d., Tags 0B3A, 072J and 0BY6), so such an \(e\) exists and is not killed by two; hence the two extensions are not isomorphic with both end identifications fixed. Sending the subobject by \(-\mathrm{id}\), however, removes the obstruction. This exact dependence on endpoints is why the example cannot be reported as a refutation of Hua’s whole ellipsized entry or of an unspecified sign-twisted comparison.

## Hua claim assessment restricted to scans 146–170

| Component of Hua, findings register, **84-chi-trivialised-extension-product** | Evidence in the supplied interval | Assessment |
|---|---|---|
| Extensions with a fixed \(\chi\)-splitting | Scan 170 gives the extension diagrams and identities; scans 146–168 calculate with them. | Supported as the intended objects, subject to the written universal-injectivity and local-freeness hypotheses and the frozen sign doubt. |
| Product by amalgamated sum without division | Scans 168 and 170 explicitly mark the relevant squares “cocart”; their structural maps use \(\pi_i\), not division by \(\chi\). | Supported as a construction plan; tensor exactness and the resulting splitting data still need proof in the stated category. |
| \(b=b_1\otimes b_2\) in split coordinates | Scan 146 circles \(b=b_1b_2\) and writes coordinate changes. | Direct local evidence; global descent is not proved by the circled formula alone. |
| Symmetric monoidal category for every \(\chi\) | No associativity, unit, symmetry, or coherence data are written in these mathematical scans. | R11 independently verifies a strict symmetric monoidal groupoid for fixed trivial rank-one endpoints over a commutative ring, for every \(\chi\), with automorphisms retained as in R13; global descent and identification with the manuscript's category remain unverified, and other ranges cited by Hua were not supplied. |
| Invertible iff \(T_0\) generates \(L\) on \(V(\chi)\) for \(M=\mathcal O\) | No \(T_0\), \(V(\chi)\), or inverse criterion appears here. | R12 verifies the precise local-model criterion \((\tau,\chi)=R\), equivalently that \(\tau\bmod\chi\) is a unit, strengthening E146.3's residue observation; identification with the named global section \(T_0\), varying line bundles, and the omitted manuscript passages remains conditional. |
| Pushout and pullback products agree | Scans 162 and 168 mark comparison arrows “?”; scan 170 asserts a canonical application; scans 148–158 expose \(\gamma\chi=2\) or \(\delta\chi=2\). | Supported as an authorial goal/claim; the fixed-endpoint all-\(\chi\) interpretation has the conditional obstruction in E170.4, and sign conventions or restrictions must be checked in the omitted ranges. |
| Novelty or absence of literature | Nothing on these scans establishes a literature search. | No novelty conclusion is adopted. |

## Self-flagged and completed checks in mathematical scans 146–170

| Scan | Exact or diplomatically qualified marker | State and note |
|---|---|---|
| 146 | No literal question mark or “à vérifier” in the mathematical text. | The many `\unsure` marks are editorial doubts, not authorial question marks; local claims are E146.1–E146.3. |
| 148 | Boxed \(\gamma\chi=2\); double-underlined three-equation system. | Emphasized conditions, not an explicit uncertainty marker; compatibility checked in E148.1–E148.2. |
| 150 | Crossed-out compatibility sentence and diagram; \(\chi\) visibly specialized to \(2\) in the double-bar calculation. | Withdrawal and local check, E150.1–E150.2. |
| 152 | Deleted \(2\chi=\chi\), followed by \(\chi=\chi\), “o.K.!”; cancelled doubtful box \(2=\chi\mid2\ne\chi\). | Corrected and checked scalar identity, plus an unresolved cancelled reading, E152.1–E152.2. |
| 154 | Four “?” occurrences in three cells of the block table. | Unverified entries, E154.1; the following prose records residual Hom ambiguity, E154.2. |
| 156 | “o.K.” after the tensor expansion; \(-\chi(1-\delta\chi)\overset{?}{=}\chi\). | Completed special-case check and separately questioned scalar equation, E156.1–E156.2. |
| 158 | “il reste” followed by the annihilation equation, then boxed \(\beta+\delta\chi=1\). | Remaining condition, with an unstated coefficient/faithfulness argument; no literal “?” here, E158.1–E158.2. |
| 160 | “\unsure{non.} Mais \unsure{suppos.} … loc. libres de rang fini”; “Je dis que”. | Revised hypothesis and claimed duality, E160.1–E160.2. |
| 162 | “?” on the thick tensor endomorphism; “?” on the downward map from \(E\). | Two separate construction questions, E162.2–E162.3. |
| 164 | Boxed coefficient equations; no literal “?” in this page’s tables. | Partial restrictions, E164.2–E164.3, do not complete scan 154’s missing fourth column. |
| 166 | “4 … carrés”; two declared commutative because “les quatre composés sont nuls” (partly doubtful). | Two completed-by-zero checks, two substantive remaining checks, E166.1–E166.3. |
| 168 | “?” on \(E_1\vee E_2\to E_1\wedge E_2\), with cancelled doubtful \(F\). | Central comparison unverified here, E168.1. |
| 170 | “On définit de façon \unsure{can.}”; “une … application can.”; no literal question mark. | Canonical construction/comparison asserted, E170.1–E170.2; coherence is not supplied. |

## Table and enumeration register for mathematical scans 146–170

“Total” below counts displayed cells, cases, or maps, not solutions over a finite field; no finite-field enumeration or polyhedron count occurs in this interval. Ordinary chains of equalities are not treated as enumerations unless they explicitly list components, coefficients, cases, or conditions. All parameters remain symbolic, and the original doubtful cells remain unresolved.

| ID / scan | What is listed | Parameters / domain | Displayed total | Recalculation |
|---|---|---|---|---|
| T146.1 / 146 | Pair of \(2\times2\) operator matrices | \(b_1\); coefficient \(2\) | 2 matrices, 8 cells | `early_formula_checks.py`: sums, products, squares. |
| T146.2 / 146 | Two labelled coefficient/map rows, \(b_1\) and \(-b_1\) | \(M_1,E_1,L_1\); doubtful map labels | 2 rows, 2 successive maps per row | Recompute only after fixing the source map interpretations; no numerical total claimed. |
| T146.3 / 146 | Two-factor coordinate change table | \(i=1,2\), \(u_i\in\operatorname{Hom}(M_i,L_i)\); scalar \(\chi\mid\gamma\) | 2 columns × 2 formulas = 4 formulas | Script expands the product for the explicit \(\chi\) interpretation. |
| T146.4 / 146 | Trivialisation/quasi-trivialisation terminology table | Doubtful \(\xi,\beta\) labels | 2 rows | Terminological count only; no independent formula to recalculate. |
| T148.1 / 148 | Two \(\sigma_i\) formulas and \(\alpha,\beta_i\) coefficient list | \(i=1,2\), \(\chi,\gamma\) | 2 operator definitions; 2 coefficient lines | Substitute and expand in the symbolic matrices. |
| T148.2 / 148 | Alternative coefficient system | \(\lambda,\mu,\chi,\gamma\) | 3 scalar equations | Script derives \(\gamma(\chi-1)=1\). |
| T150.1 / 150 | Actions on subobject and quotient | \(L_1\) and \(M_1=E_1/L_1\) (doubtful index in source) | 2 restrictions: \(-1,+1\) | Follows in the interpreted \(\chi=2\) model; script computes the general defect. |
| T152.1 / 152 | Coefficient restrictions and special choice | \(\chi,\gamma,\alpha,\beta\) | 2 displayed restriction equations; 4 named values in the special choice | Script checks the scalar identity; special tuple is \((\chi,\gamma,\beta,\alpha)=(2,1,-1,2)\). |
| T154.1 / 154 | Tensor decomposition | \(L_i,M_i\), \(i=1,2\) | 4 summands, with doubtful corrections in two labels | Formal expansion of \((L_1\oplus M_1)\otimes(L_2\oplus M_2)\); no silent label repair. |
| T154.2 / 154 | Block-map coefficient table | Four tensor summands as source and target; \(\chi,\tau_1,\tau_2\) | 16 cells: 9 zero, 2 \(\chi\), 2 known maps, 3 unresolved cells; 4 “?” marks | Script gives a labelled interpretive completion and its residuals, not a claimed transcription. |
| T154.3 / 154 | Endomorphism factorizations below the table | \(\alpha_i,\pi_i,\psi_i,\varpi_i\), several doubtful primes/bars | 2 factor rows | Recalculate after fixing types and conventions; no independent numerical result. |
| T156.1 / 156 | Special coefficient choice | \(\chi=2,\delta=1\) | 3 coefficients: \(\alpha=2,\beta=\gamma=-1\) | Direct substitution. |
| T156.2 / 156 | Bottom scalar test | \(\chi,\delta\) | 1 question-marked equation; 2 following condition displays | Script distinguishes \(\chi(\delta\chi-2)=0\) from \(\delta\chi=2\). |
| T158.1 / 158 | Compatibility tested on the mixed tensor summand and then \(x_2=u_2\) | \(u_1\in L_1,x_2\in E_2\); \(\alpha,\beta,\gamma,\delta,\chi\) | 1 universally quantified condition; 1 indicated special case | Expand the four-term ansatz and preserve annihilators; no number of solutions asserted. |
| T158.2 / 158 | Final coefficient family | \(\chi,\delta\) | 3 coefficients \(\beta,\gamma,\alpha\), with \(\beta=\gamma\) | Script verifies the resulting matrix restrictions. |
| T160.1 / 160 | Pair of input extensions, product extension and dual sequence | \(i=1,2\); local-freeness qualifications in margin | 2 inputs; 1 product row; 1 dual row | Structural enumeration; duality remains a proof obligation. |
| T160.2 / 160 | Restrictions on the two mixed tensor factors | \(u_1\otimes x_2\), \(x_1\otimes u_2\) | 2 formulas | Recompute from the interpreted \(P_i\) matrices; doubtful mapsto sign retained. |
| T162.1 / 162 | Restrictions of shifted \(\pi'\) | \(L\), \(E/L=L'\), \(\chi\) | 2 restriction formulas | Script checks eigenvalues \(1,1-\chi\). |
| T162.2 / 162 | Tensor-polynomial ansatz | \(\alpha,\beta,\gamma,\delta\), \(\pi_i\) | 4 terms, with doubtful indices | Script checks the explicitly named interpretation, not the uncertain glyphs. |
| T164.1 / 164 | \(\pi'_i\) and complementary operator tables | \(\chi,\tau_i\) | 2 matrices × 4 data cells = 8 cells | Script checks sum \(\chi I\) and zero cross-products. |
| T164.2 / 164 | Empty ruled frame | No entries or parameter labels supplied | 0 data cells | No value can be recomputed. |
| T164.3 / 164 | Coefficients of four operators on three tensor summands | \(1,P_1,P_2,P_1P_2\); \(LL,LM,ML\) inferred from the entries | 4 rows × 3 data columns = 12 cells; row labels are a separate column | Script constructs the full Kronecker matrices and compares the displayed restrictions. |
| T164.4 / 164 | Boxed scalar restrictions | \(\alpha,\beta_1,\beta_2,\gamma,\chi\) | 3 equations in two boxes | Script checks the one-parameter family and reports the missing fourth-summand conditions. |
| T166.1 / 166 | Block maps for comparison | \(F_{11},F_{12},F_{21},F_{22}\) | 4 maps; 3 blocks specified | Script records the three prescriptions and computes the remaining interpreted block. |
| T166.2 / 166 | Commutativity requirements | Four squares in the large diagram | 4 squares; 2 called automatic; 4 composites in those 2 squares called zero | Compositions use \(\psi_i\alpha_i=0\); substantive \(F_{11}\) squares remain. |
| T168.1 / 168 | Pushout and pullback constructions | \(L_i,E_i,M_i,\pi_i,\varpi_i\) | 2 product extensions; 1 questioned comparison; 4 horizontal extension rows | Explicit local reconstruction above checks the sign of the extension cocycles. |
| T170.1 / 170 | Input extensions and splitting identities | \(i=1,2\); \(\chi\), universal injectivity | 2 extensions; 3 live displayed identity lines for each \(i\), one with `=\|+` doubt | Script uses the declared equality interpretation; no silent disambiguation. |
| T170.2 / 170 | Canonical constructions and comparison | \(E_1\vee E_2,E_1\wedge E_2\) | 2 operations; 1 claimed application | Construction and gluing calculation above; coherence not supplied. |

## Titles and page counts in the assigned mathematical interval

No title sheet, cover, independent work title, or authorial total-page count occurs on mathematical scans 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, and 170. Their bottom pencil numbers are 145, 147, …, 169 and are transcribed as marginal numerals; they do not establish a separate authorial pagination scheme or a total of pages. Internal counts such as “2” compatibilities on scan 154 and “4” squares on scan 166 are structural counts, registered above, not page counts.
