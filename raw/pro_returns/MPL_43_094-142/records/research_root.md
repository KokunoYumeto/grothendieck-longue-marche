# Root research leads: functors, degree checks, and reused sheets

This working record was written after the 47 transcription hashes were frozen and the supplied context was opened. CT denotes the supplied first-pass file MPL_16+47+54+44_transcription.tex; CN denotes MPL_16+47+54+44_notes.md; RS denotes notes/RESULTS_STATE.md. CT and CN remain attributed first-pass witnesses, and a mathematical assertion in them has not thereby been independently proved. Line numbers below refer to the frozen individual page fragments.

## D01 — The site and the requested comparison with customary cohomology

**Source:** cote 43, scans 94, lines 3–8, 27–42, and 95, lines 2–4. **Kind:** self-flagged. **Words:** “Il faudrait prouver”; “étudier … si … cohomologie galoisienne”.

The site uses finite surjective morphisms as covers and the page explicitly requests comparison maps from customary group cohomology and Ext to the associated Weil sheaves. The exact task is to construct the sheafification comparison \(G\mapsto\widetilde G\) on these objects and follow its maps on resolutions, including the perfect-field qualification on scan 94. CT has a cohomological-dimension argument and an acyclic Amitsur complex on 16:30, but the context search found no definition of this quasi-scheme site, so that passage supplies a comparison target rather than a completed verification of the requested maps.

**Context search:** D01; Weil sheaves, quasi-schemes, flasque, finite covers; broader cohomology comparison CT 16:30. **RS:** WG2 §1.1 #3, as a foundation of the duality programme; no listed settled entry supplies this site comparison.

## D02 — Algebraically closed vanishing and base extension

**Source:** cote 43, scan 94, lines 27–30. **Kind:** unproved claim. **Words:** “\(H^i(k,F)=0\) pour \(i>0\)”; “commute … à l’extension du corps de base”.

The page asserts both vanishing of cohomology over an algebraically closed field and base-extension compatibility of sheaf Ext, without supplying the lifting or base-change maps. A useful proof record would identify a section \(\operatorname{Spec}k\to Y\) of each relevant cover of the terminal object and the comparison from pullback of \(\underline{\operatorname{Ext}}^i\) to Ext after field extension. CT 47:7–8 also reduces a verification to algebraically closed fibres, but 47:8 expressly leaves compatibility at the zero section unfinished; the new page therefore adds another explicit base-change assertion to that comparison file.

**Context search:** D02; “extension du corps”, “changement de base”, “base change”, algebraically closed. **RS:** WG2 §1.1 #3; no independently reviewed base-change result for this functor is listed.

## D03 — The filtered-colimit claim is expressly withdrawn

**Source:** cote 43, scans 96, lines 35–38, and 97, lines 2–3. **Kind:** withdrawn in the same text. **Words:** canceled “compatible … avec les limites inductives”; “Non, car le foncteur \(\mathbb V:k\text{-alg}\to V\text{-alg.}\) ne commute pas aux limites inductives”.

The canceled assertion continues from scan 96 onto scan 97, and the marginal “Non” gives the reason for abandoning the proposed restriction of the target category. The retained construction \(\mathcal N(F)(A)\) still uses constructible partitions and the functor \(\mathbb V\), so reconstructing its domain requires the full displayed pro-object construction. The context search produced Néron–Severi and Néron–Tate passages, including CT 16:21 and 44:4, but no second copy of this \(\mathbb V\)-colimit argument.

**Context search:** D03; Greenberg, Néron, inductive limits. **RS:** WG2 §1.1 #3; the withdrawal changes the foundational scope of the programme, with no matching settled register lemma.

## D04 — The canceled adjunction identifies the outstanding exactness check

**Source:** cote 43, scan 97, lines 19–30. **Kind:** self-flagged. **Words:** “transforme injectifs en injectifs”; “à vérifier”.

The canceled proof proposes the precise adjunction \(\operatorname{Hom}(\Phi,\mathcal N F)\simeq\operatorname{Hom}(\mathcal N^*\Phi,F)\) and left exactness of \(\mathcal N^*\); those constructions are the unresolved ingredients behind the displayed Leray sequence. CT 16:37 supplies a concrete stalk adjunction in an injective-sheaf proof, while [Stacks, Tag 015Z](https://stacks.math.columbia.edu/tag/015Z) records the exact-left-adjoint mechanism used by that argument. The new evidence is the author's explicit verification mark on this particular \(\mathcal N\), whose proposed adjoint is canceled on the same sheet.

**Context search:** D04; injective, adjunction, adjoint; CT 16:37, 39; CN R10 is an unreviewed lead. **RS:** WG2 §1.1 #3; no listed entry establishes exactness of \(\mathcal N^*\).

## D05 — First relative-Hom acyclicity gate

**Source:** cote 43, scan 98, lines 12–19. **Kind:** self-flagged. **Words:** “si on admet”; first “vérifier”.

The first spectral sequence requires acyclicity of \(\underline{\operatorname{Hom}}_S(F,I)\) for \(\underline H^0_{S/k}\) when \(I\) is injective, which is a more specific check than merely declaring \(\mathcal N\) left exact. The comparison to document is \(R(\mathcal N\circ\underline{\operatorname{Hom}}_S(F,-))\to R\mathcal N\circ R\underline{\operatorname{Hom}}_S(F,-)\), with the two arguments and coefficient category retained. CT 16:37 provides an injective construction and CT 16:30 an acyclic complex; neither supplied passage evaluates this composite, while [Stacks, Tag 015M](https://stacks.math.columbia.edu/tag/015M) identifies the comparison morphism involved.

**Context search:** D05; acyclicity, spectral sequences, injective Hom. **RS:** WG2 §1.1 #3; no matched settled entry.

## D06 — Second relative-Hom acyclicity gate

**Source:** cote 43, scan 98, lines 21–37. **Kind:** self-flagged. **Words:** “admettant”; second “vérifier”.

The second mark concerns acyclicity of \(\underline{\operatorname{Hom}}_{S/k}(F,I)\) for \(H^0(k,-)\), and the ensuing target is the global group \(\operatorname{Ext}^*(S;F,G)\). Its comparison morphism is obtained by applying derived global sections to the relative Hom construction, so a check of the first mark does not record this second evaluation. CT 16:30's explicit complex \(C(s)\) and [Stacks, Tags 015M–015N](https://stacks.math.columbia.edu/tag/015N) provide concrete points of comparison for writing out the relevant resolutions.

**Context search:** D06; acyclicity, Ext/Hom and spectral sequences; CT 16:30, CN R18–R19 are context leads about different displayed boundedness arguments. **RS:** WG2 §1.1 #3; no matched settled entry.

## D07 — Perfection, cohomological dimension, and the residue-field map

**Source:** cote 43, scan 104, lines 2–39. **Kind:** self-flagged. **Words:** “parfait ?”; “\(T^0\) transforme injectifs en \(\Gamma_k^0\)-acycliques ??”.

The sheet puts the acyclicity question beside a bound of two, a proposed bound of one after excluding \(\mathbb Z\)-components, and compatibility with extension of the residue field. These are three proof obligations for the same displayed passage \(\Gamma_K^*G\simeq\Gamma_k^*T(G)\), and the qualification on the components must remain attached to the stronger bound. CT 16:30 derives its own bound through named earlier results and a field reduction; comparing the two passages requires a map between their coefficient objects and identification of the field hypotheses.

**Context search:** D07; dimension, Galois, perfection; CT 16:28, 30 and 52. **RS:** WG2 §1.1 #3; WG H1 only as a later proposed use of cohomological input, without changing its unchecked status.

## D08 — The first duality comparison has a written exclusion

**Source:** cote 43, scan 100, lines 6–22. **Kind:** unproved claim. **Words:** “isom si \(G\) affine sans … composantes \(G_a\)”.

The asserted Ext comparison is accompanied by an affine/no-\(G_a\)-component restriction, and its superscripts remain uncertain in the frozen reading. Scan 130 later writes a curve-level comparison with “sans composantes abéliennes”; a reconstruction must specify the passage from the \(K/k\) functor on scan 100 to \(Rf_*\) on the curve and test each written restriction at that map. CT 54:5 and 7 supplies explicit Cartier-duality arrows for \(p\)-torsion and Frobenius, which is useful comparison material for finite coefficients but gives no evaluated \(K/k\) map from scan 100.

**Context search:** D08; Cartier, affine, \(G_a\), unipotent; CT 54:5, 7. **RS:** WG2 §1.1 #3; the scope qualifications are new manuscript evidence, with no settled register identification.

## D09 — The lower Cartier–Serre–Pontryagin square is a question

**Source:** cote 43, scan 106, lines 2–51. **Kind:** self-flagged. **Words:** “Comment obtient on le carré du bas ?”.

The page names all three horizontal dualities and the two vertical functors \(T\) and \(S=\Gamma_k\), and excludes \(\mathbb Z\)-components through its prime notation. It then seeks the lower square through a degree-zero arrow \(S(\mathbb Z/n\mathbb Z)\to\mathbb Z/n\mathbb Z(-1)\), followed by an Ext/Hom calculation. CT 54:5–7 provides Cartier/Frobenius maps and CT 47:8 an explicitly unfinished compatibility map, but no supplied context passage evaluates the lower square printed here.

**Context search:** D09; Pontryagin, Frobenius, Lang, Serre duality; supplementary Cartier comparison CT 54:5–7. **RS:** WG2 §1.1 #3; this is an additional compatibility problem, not a register status update.

## D10 — The first cohomological pairing needs its degree dictionary

**Source:** cote 43, scan 107, lines 2–38, compared with scan 119, lines 3–8. **Kind:** reading question. **Words:** boxed \(H^i(A)\times H^{2-i}(B)\mathrel{-}H^2(K,G_m)\).

The opening pairing uses \(2-i\), whereas the finite ordinary-group example lower on scan 107 uses \(1-i\), and scan 119 places \({}_\infty B\) in sheaf-Ext degree one. Those three printed degree assignments should be compared through the actual evaluation and coefficient maps before treating the initial box as a finished duality statement. CT 54:3–5 names dual abelian varieties and their degree-one constructions, offering a source for identifying the intended \(A,B\) dictionary, without resolving the unfinished line on scan 107.

**Context search:** D10; duality, Tate, biextension, pairing; CT 54:3–5. **RS:** WG2 §1.1 #3; no listed reviewed result fixes this degree convention.

## D11 — A scratch sheet keeps several competing Ext degrees

**Source:** cote 43, scan 114, lines 9–57. **Kind:** reading question. **Words:** \(1-i\), \(i\), and \(i-1\) in successive retained formulas.

The sheet moves among \(H^i(K,DG)\), Ext of \(f_*G\), and a written translation \((-1)\), with several unfinished terms and overwritten indices. A comparison record should give one complex-level evaluation morphism, state its variance, and derive the resulting degrees at each of the displayed boxes; the frozen text supplies no such single completed calculation. CT 47:5–8 explicitly tracks translations and a determinant factor for its transform, so those pages provide a useful example of the degree bookkeeping required here without supplying this \(f_*\)-duality calculation.

**Context search:** D11; Ext, degree, shift; CT 47:5–8. **RS:** WG2 §1.1 #3.

## D12 — Biduality, completion, and the meaning of \(\pi_1(A)\)

**Source:** cote 43, scan 116, lines 2–30. **Kind:** unproved claim. **Words:** “compact”; “est le plus gr”; “complété de fini”.

The spectral-sequence sketch for \(\Delta^2T(A)\) compares a term of \(H^0(K,A)\) with \(\pi_1(A)\) and attaches a completion remark to the calculation. The immediate research task is to define this \(\pi_1(A)\) and its comparison morphism from the realization functor, retaining the uncertain \(\Delta|0\) at the later equality. CT 44:3 has a canceled completion argument and CT 44:8 explicitly writes \(T_\ell(J^i)\); these are comparison locators, while the present page leaves the definition and transition maps of its own completion implicit.

**Context search:** D12; biduality, completion, \(\pi_1\), Tate module; CT 44:3, 8. **RS:** WG2 §1.1 #3; WG H1 only as a possible downstream use requiring the missing dictionary.

## D13 — A displayed product and the extension written underneath it

**Source:** cote 43, scan 117, lines 8–13 and 26–41. **Kind:** unproved claim. **Words:** the displayed product in \(H^1(K,B)\); the lower short exact sequence.

The upper box presents a product decomposition, while the lower diagram supplies an extension with end terms \(\operatorname{Ext}^1(\mathcal A'^0,\mathbb Q/\mathbb Z)\) and \(\underline{\operatorname{Ext}}(U,\mathbb Q/\mathbb Z)\). To substantiate the displayed product, the missing map to locate is a section from the latter end term into \(H^1(K,B)\) whose composite with the quotient map is the identity, in the category and topology intended on the sheet. CT 54:3 and 7 also writes canonical extensions, and CT 16:19 describes a Picard extension, but none of those supplied arrows is identified here as that section.

**Context search:** D13; extension, product, splitting, unipotent; CT 54:3, 7; 16:19. **RS:** WG2 §1.1 #3.

## D14 — The finite Kummer maps must control the infinite-coefficient scratchwork

**Source:** cote 43, scan 119, lines 17–43. **Kind:** reading question. **Words:** \(H^0(K,B)\to H^0(K,B)\otimes\mathbb Q/\mathbb Z\); \(Q\subset N\).

The sheet introduces \(Q,N\) around a torsion-cohomology diagram and cancels one proposed kernel description. The displayed map into a tensor product needs an explicit formula and a transition system, so the finite-level Kummer boundary maps on scan 120 are the concrete arrows to compare with it. CT 16:21 and 23 writes a finite Kummer sequence and a passage to a Tate-module quotient; it adds a checkable template for the transition maps while leaving the current \(Q,N\) identification open.

**Context search:** D14; Kummer, tensor, transition; CT 16:21, 23. **RS:** WG2 §1.1 #3; the arithmetic application is addressed in A03–A07 and D20.

## D16 — Supports are exchanged in the proposed duality diagram

**Source:** cote 43, scan 123, lines 2–31. **Kind:** self-flagged. **Words:** \(\operatorname{Ext}_m(M,A)\overset?=D(M)\); two “?” on formal-completion arrows.

The page exchanges cohomology with support and Ext without support, then reverses arrows and shifts the degree in its open-complement row. Its later \(Y\subset Z\) diagram points to the comparison from completion along \(Y\) to completion along \(Z\), with two arrows expressly questioned. CT 16:39 supplies injective-hull data, and [Stacks, §47.18](https://stacks.math.columbia.edu/tag/0A81) exhibits the precise local-duality comparison through a dualizing complex, local cohomology, and derived completion; the task here is to identify the manuscript's \(A,D,r\) and the corresponding arrows.

**Context search:** D16; supports, Matlis, local duality; CT 16:39; CN R9–R10 remain leads. **RS:** WG2 §1.1 #3; no listed entry identifies these local-duality symbols.

## D17 — The completion limit is an explicit proof obligation

**Source:** cote 43, scan 125, lines 2–31. **Kind:** self-flagged. **Words:** \(\varinjlim_n\operatorname{Ext}^i(F/\mathcal J^nF,G)\); marginal “lim”; final “?”.

The first equality is followed by inverse-limit duals and a comparison with Ext on \(\widehat X\), but its bottom object still carries an uncertain finite-level subscript. A proof has to specify the transition maps from \(F/\mathcal J^{n+1}F\) to \(F/\mathcal J^nF\), the induced contravariant Ext maps, and the morphism from the derived inverse limit to the proposed completed object. CT 16:39's filtration of an injective hull and [Stacks, §47.10](https://stacks.math.columbia.edu/tag/0BJD) supply finite-level models; they do not evaluate the two question-marked maps on scans 123 and 125.

**Context search:** D17; completion, inverse limit, Matlis, injective hull; CT 16:39; CT 44:3 is a canceled completion draft with a surviving margin. **RS:** WG2 §1.1 #3.

## D18 — An explicit one-parameter calculation for the limit arrows

**Source:** cote 43, scans 123 and 125. **Kind:** own idea. **Confidence:** high for this calculation; the displayed free resolution and transition maps prove it. **Anchor:** “dual” beside the direct-limit formula.

For \(A=k[[t]]\), the resolution \(0\to A\xrightarrow{t^n}A\to A/(t^n)\to0\) gives \(\operatorname{Ext}^1_A(A/(t^n),A)=A/(t^n)\), and the quotient \(A/(t^{n+1})\to A/(t^n)\) induces multiplication by \(t\) on these Ext groups. The maps \([a]\mapsto a/t^n\bmod A\) identify their direct limit with \(E=k((t))/k[[t]]\). An endomorphism of \(E\) restricts on \(E[t^n]=t^{-n}A/A\) to multiplication by \(a_n\in A/(t^n)\), and compatibility is \(a_{n+1}\equiv a_n\bmod t^n\), proving \(\operatorname{End}_A(E)=\varprojlim_nA/(t^n)=A\). This gives explicit arrows for one local model of the manuscript's limit/completion pattern and a concrete comparison with the injective-hull filtration in CT 16:39.

**Context search:** D18; Matlis, injective hull, local duality, Ext; CT 16:39; [Stacks, §47.18](https://stacks.math.columbia.edu/tag/0A81). **RS:** WG2 §1.1 #3; this calculation adds a test model, with no claimed new general theorem.

## D19 — The curve category is posited, and finite cohomological dimension is admitted

**Source:** cote 43, scan 128, lines 6–30. **Kind:** self-flagged. **Words:** “définis comme les \(C\)-groupes ?”; “Cela est-il équivalent”; the uncertain reading “nous admettrons”.

The page postulates enough injectives for \(C\)-groups, asks about their relation to Weil functors on algebraic \(k\)-sets, and admits finite cohomological dimension for \(f_*\). The comparison functors printed on the sheet are \(\operatorname{Gr}_C\to\operatorname{Gr}_k\to\operatorname{QuGr}_k\), so the required proof includes their exactness properties before the spectral sequences are used. CT 16:41's derived-Hom statement records explicit boundedness alternatives and CT 16:56 discusses faithfully flat descent; the current sheet adds a curve-group construction to those leads without checking the categorical equivalence it asks for.

**Context search:** D19; faithfully flat, Weil, abelian category; supplementary boundedness CT 16:41, CN R18–R19. **RS:** WG2 §1.1 #3.

## D20 — The fundamental comparison is composition with a proposed trace

**Source:** cote 43, scan 130, lines 15–29. **Kind:** unproved claim. **Words:** “définissons un élément \(\gamma\)”; “en composant”.

The written construction sends a degree-\(i\) morphism \(u:G\to S\sigma[i]\) to \(Rf_*G\xrightarrow{Rf_*u}Rf_*(S\sigma[i])\xrightarrow{\cong}(Rf_*S\sigma)[i]\xrightarrow{\gamma[i]}\sigma[i]\), with \(\gamma:Rf_*S\sigma\to\sigma\) of degree zero and the middle arrow the shift compatibility of \(Rf_*\). This specifies the intended comparison morphism and makes the construction of \(\gamma\), together with its naturality and degree convention, the central outstanding step. CT 47:7–8 also builds a specific morphism before asking for a compatibility check, and CT 54:3 states/proposes degree-one duality; the new page contributes the explicit trace-composition recipe for the curve programme.

**Context search:** D20; trace, Hom, functoriality, pushforward; CT 47:7–8 and 54:3. **RS:** WG2 §1.1 #3; WG2 §2.3 #12 only for subsequent comparison with the duality maps in cote 44.

## D21 — The duality theorem is stated with an unsettled range

**Source:** cote 43, scan 130, lines 31–39. **Kind:** self-flagged. **Words:** the possible marginal reading “préciser”; “isom mod \(\theta\)”.

The assertion first passes through several canceled finite/proalgebraic formulations and then says “affine, et sans composantes abéliennes”; its second part adds “de type fini” and weakens the conclusion to an isomorphism modulo \(\theta\). A proof record must define the quotient or localization denoted by \(\theta\) and identify the map on kernels and cokernels used to obtain the stated Ext-to-\(\mathbb Q/\mathbb Z\) test. CT 54:5–7 gives explicit finite Cartier-dual objects, while no supplied context passage defines this \(\theta\), so its range remains an open manuscript specification.

**Context search:** D21; Cartier, abelian, affine, torsion, and the separate literal \(\theta\) query in the search record. **RS:** WG2 §1.1 #3.

## D22 — The written \((1)\) and \((2)\) need a source-level comparison

**Source:** cote 43, scan 100, line 2, and scan 132, lines 18–36. **Kind:** reading question. **Words:** \(S\sigma=(D\Delta\sigma_K)(1)\); \(S\sigma=(D\Delta\sigma)(2)\).

The two definitions occur beside different displayed functors, \(K/k\) on scan 100 and the curve map \(f\) on scan 132. Their comparison must identify the parentheses with the author's translation or coefficient convention and specify the morphism relating the two settings, including the finite étale coefficient and \(n\sigma=0\) clauses on scan 132. CT 54:5–7 supplies \(D\) for Cartier duality and CT 47:5 explicitly tracks a translation, but neither supplied formula determines the current \(D\Delta\) convention.

**Context search:** D22; Cartier, twists, translations, \(\mu_n\). **RS:** WG2 §1.1 #3; no settled entry fixes this notation.

## D23 — Opposite written translations on the Jacobian sheet

**Source:** cote 43, scan 133, lines 25–40. **Kind:** reading question. **Words:** \(Rf_*G_m(-1)\) in the first comparison and \(Rf_*G_m(1)\) in the next.

The two retained displays use opposite parenthetical signs, and the second right-hand coefficient remains the uncertain \(\sigma|\tau\) even after the text specializes to \(\mathbb Q/\mathbb Z\). Their intended relation has to be checked against the trace-composition map on scan 130, the definition on scan 132, and the degrees of \(R^{-q}f_*G_m\). CT 16:21–23 supplies Kummer and Picard/Brauer comparisons, while CT 47:5–8 illustrates a fully written translation convention; these comparisons raise a reading-and-degree question without altering either frozen sign.

**Context search:** D23; translations, complexes, idèles/adèles; CT 16:21–23 and 47:5–8. **RS:** WG2 §1.1 #3; WG2 §2.3 #12 for the subsequent Jacobian comparison.

## D24 — Reduction to the henselization is an expectation

**Source:** cote 43, scan 135, lines 4–15. **Kind:** self-flagged. **Words:** “On doit prouver”; “Il est sans doute vrai”.

The page targets coefficients concentrated at \(x\) and expects the relevant Ext on \(C\) to agree with Ext over the henselization of \(\mathcal O_{C,x}\). The arrow to construct is restriction to that local base followed by the support comparison, with the displayed \(i-2\) and the identification \(T(G)\simeq G_x\) retained. CT 16:37's stalk description and CT 16:39's local injective hull are nearby concrete tools, but the supplied context contains no evaluation of this henselian comparison for the curve-group category.

**Context search:** D24; henselian, support, local duality, Ext; CT 16:37, 39. **RS:** WG2 §1.1 #3.

## D25 — The extension-by-zero verification narrows to prime-to-\(p\) coefficients

**Source:** cote 43, scan 135, lines 18–53. **Kind:** withdrawn in the same text. **Words:** canceled “quelconque”, inserted “premier à \(p\)”; “on le vérifie par un calcul facile”.

The reduction uses the sequence \(0\to F_U\to F\to F_Y\to0\), and the claimed easy verification is confined by the final correction to \(F=\mu_n\) with \(n\) prime to \(p\). The last phrase remains unfinished, so the induced map of the two long exact sequences, including its boundary signs, is the calculation to recover. CT 16:21–23 gives finite Kummer maps and CT 54:5–7 retains characteristic-\(p\) Cartier data, providing concrete coefficient comparisons while recording no completion of this page's final sentence.

**Context search:** D25; prime-to-\(p\), Kummer, \(\mu_n\). **RS:** WG2 §1.1 #3; FLAGGED_149 B9 remains open and is not settled by a prime-to-\(p\) coefficient calculation on this sheet.

## D26 — Dualizing the localization triangle leaves a marked compatibility check

**Source:** cote 43, scan 136, lines 17–70. **Kind:** self-flagged. **Words:** “triangle exact”; marginal “?”; the boxed degree shift.

The sheet first writes the localization triangle for \(\underline H_x,\underline H_X,\underline H_U\), then reverses the arrows after dualizing into \(\mathbb Q/\mathbb Z\). Its three-row comparison contains degrees \(n-1,n-2,n-2\), and the margin tries to account for them through \(F_U\), so each boundary map and each support subscript must be identified before commutativity is claimed. CT 47:8 supplies another expressly unfinished compatibility check on a specific derived map, while the current sheet adds a localization diagram whose shift problem is independently visible.

**Context search:** D26; localization, triangle, supports, compatibility; CT 47:8. **RS:** WG2 §1.1 #3.

## D27 — The five-row diagram retains the degree corrections

**Source:** cote 43, scan 138, lines 3–18. **Kind:** self-flagged. **Words:** inserted \(3-i\), inserted \(2-i\), and final \(\simeq?\).

The five rows match global, open, and supported cohomology with a reverse column whose first two degrees are written both as unsimplified expressions and as inserted values. This is evidence for active tracking of the localization boundary: the top \(2-(i-1)\) and next \(1-(i-1)\) are the two formulas to carry through the comparison. CT 54:7 has a transposed pair of \(F,V\) sequences and CT 47:8 a compatibility problem, but neither supplies the boundary map needed for the final questioned isomorphism here.

**Context search:** D27; exact sequence, boundary, compatibility; CT 54:7 and 47:8. **RS:** WG2 §1.1 #3.

## D28 — The final support comparison remains explicitly open

**Source:** cote 43, scan 140, lines 29–39. **Kind:** self-flagged. **Words:** \(\underline H^*_{Y/k}(i_!G)\overset?{\simeq}\underline H^*_{U/k}(G)\), followed by “???”.

The page has reached extension by zero \(i_!G\), but its concluding comparison still carries the author's question marks and an unfinished following line. The localization morphisms \(\underline H_Y(i_!G)\to\underline H_X(i_!G)\to\underline H_U(G)\) are the exact maps through which to compare this box with the shifted equation on scan 136. The context search found no copy of this \(i_!\)-comparison, while CT 47:8 records its own separate named comparison morphism and unfinished verification.

**Context search:** D28; extension by zero, supports, local cohomology, \(i_!\); CT 47:8 through the related compatibility search. **RS:** WG2 §1.1 #3.

## D29 — A degree-zero test of the last boxed formula

**Source:** cote 43, scans 136 and 140. **Kind:** own idea. **Confidence:** high for the explicit test; the degree-zero sections and exact localization boundary determine it. **Anchor:** the boxed support comparison and “???”.

Work on the ordinary étale site with \(X=\mathbb P^1_k\), \(U=\mathbb A^1_k\), \(Y=\{\infty\}\), inclusions \(j:U\hookrightarrow X\), \(i:Y\hookrightarrow X\), and \(\Lambda=\mathbb Z/n\mathbb Z\) for \(n>1\) invertible in the algebraically closed field \(k\). The exact sequence \(0\to j_!\Lambda_U\to\Lambda_X\to i_*\Lambda_Y\to0\) gives \(H^0(X,j_!\Lambda_U)=\ker(\Lambda\xrightarrow{\mathrm{id}}\Lambda)=0\), and the zero stalk on \(Y\) gives \(H_Y^0(X,j_!\Lambda_U)=0\), whereas \(H^0(U,\Lambda_U)=\Lambda\). The localization boundary therefore injects \(\Lambda\) into \(H_Y^1(X,j_!\Lambda_U)\). This computes the degree behavior to compare with the unshifted box on scan 140 and the \(+1\) on scan 136; identification with the manuscript's underlined \(k\)-group-valued functors remains to be supplied.

**Context search:** D29; supports, extension by zero, and stalks; CT 16:37 for stalk-based tests, CN R10 as a lead. **Primary verification:** [Stacks 03S2, Lemma 59.70.8](https://stacks.math.columbia.edu/tag/03S2), [03S5, geometric stalks](https://stacks.math.columbia.edu/tag/03S5), and [09XP, localization](https://stacks.math.columbia.edu/tag/09XP). **RS:** WG2 §1.1 #3; no change to a listed open arithmetic assertion.

## R01 — The reused homotopy sheet makes an explicit comparison conjecture

**Source:** cote 43, scan 101, lines 33–53. **Kind:** conjecture. **Words:** “It would seem reasonable to suppose”; “the maps \(Df\) and \(\Delta\)”.

The typed author compares the dual of an intrinsic-join map with the Thom-space map induced by the diagonal and asks for equality of their stable homotopy types. The objects and arrows are written explicitly as \(Df,\Delta:X^{\gamma+\delta}\to X^\gamma\mathbin{\times\mkern-10mu\times}X^\delta\), so a study should compare those maps with their bundle identifications. The supplied context searches for James, intrinsic join, Thom, Spanier, and \(S\)-homotopy returned no matching passage. Atiyah's *Thom Complexes*, p. 309, retains the conjectural wording; see R03.

**Context search:** R01; no match in the supplied context text files. **RS:** MPL_136_235-281 N16 and MPL_136_189-234 R008 are first-pass provenance leads about reused paper; they do not identify or prove this homotopy assertion.

## R02 — The Stiefel reduction includes a numerical range to preserve

**Source:** cote 43, scan 103, lines 24–48. **Kind:** reading question. **Words:** “\(n\geq2k\) or \(k=1\)”; “In the real case suppose \(n\geq2k\)”.

The typed argument relates reducibility, stable reducibility, and the cross-section of \(O_{n,k}\to S^{dn-1}\), with a connectivity inequality used in between. The uncertain \(3n-1|dn-1\) in Lemma 6.3 should be checked against the adjacent explicit sphere and stabilization map, while the numerical restrictions must remain part of any cited result. Searches of the supplied context for Stiefel, stable reducibility, and cross-sections found no matching calculation.

**Context search:** R02; no matching context passage. **RS:** MPL_136_235-281 N16, provenance comparison only; no settled register entry on this typed theorem.

## R03 — The reused homotopy typescript matches Atiyah's Thom Complexes

**Source:** cote 43, scans 101, 103, 105, especially the theorem numbering, final conjecture, and bibliography. **Kind:** own idea. **Confidence:** high for this documentary identification, because the matched theorem sequence, comparison maps, reference order, and institutional closing are jointly specific. **Anchor:** “REFERENCES”; “Pembroke College, Cambridge”.

Scans 103 and 101 match the theorem sequence and final \(Df,\Delta\) passage in Atiyah's *Thom Complexes*, pp. 308–309, supporting identification with a version of that text. Its printed bibliography adds 5a and 17–20 to the order preserved on scan 105 and completes that sheet's pending Milnor–Spanier reference. The [publisher record](https://doi.org/10.1112/plms/s3-11.1.291) gives 1961 publication and receipt on 15 March 1960; those dates identify the published text, while the use of these particular sheets remains undated. The supplied context has no matching bibliography, so this external primary comparison adds a concrete provenance identification without changing any frozen reading.

**Context search:** R03; Atiyah, James, Thom, Hirzebruch; no match. **Primary comparison:** Atiyah, *Thom Complexes*, *Proceedings of the London Mathematical Society* (3) 11 (1961), 291–310, [primary article scan](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/atiyahthom.pdf), pp. 308–310; checked 16 November 2026. **RS:** MPL_136_095-141 1.5, MPL_136_189-234 R008, and MPL_136_235-281 N16, all first-pass provenance leads.

## R04 — The canceled connected-components argument changes its continuity claim

**Source:** cote 43, scan 108, lines 4–35. **Kind:** reading question. **Words:** inserted “\(\frac12\) continue”; bracketed “elle est continue en \(y\)”.

The crossed-out draft revises properness, universal openness, the number of geometric connected components, and the continuity wording before its reduction to a discrete valuation ring. Several words are low-confidence readings, so the exact specialization map and the direction of \(\pi(y)\geq\pi(y')\) should be checked against a complete neighboring draft before giving the paragraph theorem status. Searches for connected components and universal openness produced no matching statement in the supplied context.

**Context search:** R04; no match for the specific connected-component/open-morphism vocabulary. **RS:** no matching mathematical entry; the reused/canceled-sheet observations MPL_136_235-281 N16 bear on provenance only.

## R05 — The multiplicity lemma is questioned by its author

**Source:** cote 43, scan 110, lines 25–65. **Kind:** self-flagged. **Words:** “J’ignore si les assertions sont vraies”; “Question liée”.

The typed lemma has inserted dominance and \((S_1)\) conditions, then a margin explicitly questions the assertions without generic-point flatness. Its proof separates the \(t\)-power torsion submodule \(N\) from \(G=F/N\) and later singles out equality, while the preceding sentence literally uses “l’inégalité” in the flatness implication. CT 54:4 and 6 also revises flatness hypotheses and CT 16:56 lists flatness explicitly in an étale criterion, so the new margin supplies a precise caution to retain in that algebra comparison file.

**Context search:** R05; multiplicity, flatness, lengths; CT 54:4, 6 and 16:56. **RS:** no directly matching settled algebra lemma; MPL_136_235-281 N16 is only a provenance lead.

## R06 — A concrete test refutes the literal inequality-to-flatness sentence

**Source:** cote 43, scan 110, lines 30–36, 49–51. **Kind:** own idea. **Confidence:** high; the fibre lengths and the kernel after tensoring are explicit. **Anchor:** “Si l’inégalité est vérifiée, alors \(F\) est plat”.

Take \(R=k[[t]]\), \(X=Y=\operatorname{Spec}R\), \(f=\operatorname{id}\), and \(F=\widetilde{R\oplus k}\): the identity is proper and universally open, the support is \(X\), its component dominates \(Y\), and the zero-dimensional special fibre \(k^2\) satisfies \((S_1)\). The two lengths are \(2\) and \(1\), so the written inequality holds, but tensoring \(0\to R\xrightarrow tR\) with \(R\oplus k\) produces a nonzero kernel \(k\), proving nonflatness. This refutes the literal inequality-to-flatness implication on the supplied sheet, while the later “on ne peut avoir égalité” supplies an internal reading question about the intended statement. CT 54:4–6's explicit flatness revisions provide the contextual comparison; the frozen word remains unchanged.

**Context search:** R06; lengths and flatness; CT 54:4–6. **RS:** no register entry is revised; this is a fully specified test of the current typed sentence.

## R07 — The proper-pushforward proof displays an actual spectral-sequence collapse

**Source:** cote 43, scan 115, lines 12–31. **Kind:** unpursued implication. **Words:** “le même raisonnement”; “\(E_2^{pq}=0\) pour \(q>0\)”.

The reused sheet gives the chain \(X'\xrightarrow gX\xrightarrow fY\), a projective birational \(g\), the coherent \(F=g_*\mathcal O_{X'}(n)\), and the vanishing that collapses Leray to \(R^pf_*F\simeq R^p(fg)_*\mathcal O_{X'}(n)\). This supplies a completed instance of the resolution-and-acyclicity mechanism that the handwritten scans 97–98 still mark for verification in their own functors. CT 16:41 discusses coherence of derived Hom with explicit boundedness assumptions, giving a second concrete place to compare exactly which vanishing statement is used.

**Context search:** R07; Chow, coherence, Leray, spectral; CT 16:41. **RS:** WG2 §1.1 #3 for the methodological link; no new theorem about \(\mathcal N\) follows from the typed collapse.

## R08 — A canceled margin questions equidimensionality

**Source:** cote 43, scan 116, lines 40–44. **Kind:** self-flagged. **Words:** canceled “J’ignore si les conditions d’équidimensionnalité … sont essentielles”.

The reused canceled text questions hypotheses in 1.1(ii) and 2.6, then names a proposed Proposition 2.8 on continuity of Cohen–Macaulay conditions. Those preceding numbered statements are absent from the supplied range, and the context search found no Cohen–Macaulay or equidimensionality match. The note records an unresolved source question with its missing locators rather than reconstructing their hypotheses from the neighboring duality calculations.

**Context search:** R08; Cohen, Macaulay, equidimensionality; no match. **RS:** no matching mathematical entry; provenance only relates to MPL_136_235-281 N16.

## R09 — The crossed-out outline preserves an editorial question and local dates

**Source:** cote 43, scan 118, lines 3–60. **Kind:** self-flagged. **Words:** “Pourrait passer au Chap 0 ?”; “Bott September 1963 ?”.

The fifteen-item outline asks about moving a section to Chapter 0 and includes regular morphisms, hyperplanes, infinitesimal extensions, Grassmann spaces, and differential forms/duality. A second crossed-out list carries the James/Bott September 1963 entries and names Zariski, Dieudonné, Hilton, Kuiper, and Eells–Kuiper. The context search finds other manuscript organization and dated-letter material but no matching outline, so these dates and headings should remain attached to this face in the internal chronology.

**Context search:** R09; 1963, James, Bott, Grassmann, flat morphisms; no matching outline in CT. **RS:** WG2 §1.1 #3 for archival placement, with MPL_136_235-281 N16 as a first-pass provenance lead.

## R10 — Euler-characteristic conventions and the marginal strict inequality

**Source:** cote 43, scan 121, lines 3–35. **Kind:** reading question. **Words:** “si \(A\) est local”; marginal “\(>\)” beside “\(\geq0\)”.

The sheet defines the Euler characteristic by lengths and proves additivity, then states a Hilbert-polynomial result with a nonnegative leading coefficient and a separate marginal strict inequality. The base-ring qualification and the zero-sheaf case must be located in the preceding typescript before adopting a strict-positivity version; the page itself contains both the printed inequality and the margin. CT 16:14, 48, and 54 has polynomial/cohomological vocabulary, but no supplied passage supplies this preceding length convention.

**Context search:** R10; Euler, Hilbert, polynomial and leading coefficient. **RS:** no matching settled item; provenance comparisons MPL_136_189-234 R008 and MPL_136_235-281 N16 remain first-pass leads.

## R11 — The canceled dimension/depth draft leaves its property list empty

**Source:** cote 43, scan 129, lines 7–43. **Kind:** unproved claim. **Words:** “Soit P l’une des propriétés……”; “Montrer … certaines propriétés” (uncertain reading).

The draft relates polynomial localizations, fibre transcendence degree, dimension, and depth, then leaves the property list \(P\) unfilled in the final corollary. Its \(\nu\) is explicitly the fibre dimension, so a reconstruction can compare the maps \(A\to A[t_1,\ldots,t_n]_M\) and their residue fields before identifying which properties the final line was meant to cover. CT 54:4–6's flatness/localization arguments and CT 16:56's local algebra provide contextual maps, but no supplied context passage fills the omitted list.

**Context search:** R11; regularity, dimension, depth; CT 54:4–6 and 16:56 through the flatness searches. **RS:** no matching settled register entry.

## R12 — The faithfully flat module map is explicit

**Source:** cote 43, scan 137, lines 4–20. **Kind:** unpursued implication. **Words:** “\(x\longrightarrow1\otimes x\)”; “\(A\cap B\underline a=\underline a\)”.

The typed proof records the map \(F\to B\otimes_AF\), contraction of extended ideals, and a quotient-flatness argument as steps in the faithful-flatness equivalences. CT 16:56 explicitly invokes faithfully flat descent, while scan 128 uses faithfully flat coverings to define the curve-group sheaves; these give a concrete comparison through tensor extension and its unit map. The first printed quotient-like object is \(B\,h(A)\) and the next is \(B/h(A)\), so any citation of the exact sequence must report that textual discrepancy.

**Context search:** R12; faithfully flat, tensor, descent; CT 16:56, 54:4–6. **RS:** WG2 §1.1 #3 for the sheaf-foundation link; no listed result settles the handwritten category construction.

## R13 — Softness and partitions of unity are represented by a construction

**Source:** cote 43, scans 126, lines 4–16, and 124, lines 4–8. **Kind:** unpursued implication. **Words:** “Faisceaux mous”; “partition de l’unité”.

Scan 126 gives a local definition of softness and a constant-sheaf example obstructing extension of a prescribed section; scan 124 constructs a partition of unity using locally finite refinements and a maximal partial family. CT 16:37 proves injectivity through an explicit stalk map, so the concrete comparison task is to trace which resolution and section-extension maps each construction furnishes. The supplied context has no matching \((\mathrm{FM}_{\mathrm I}),(\mathrm{FM}_{\mathrm{II}})\) definition or continuation of the maximal-family proof.

**Context search:** R13; soft, mou, partitions of unity, sheaves; CT 16:37. **RS:** no corresponding settled entry; MPL_136_235-281 N16 bears on the reused-sheet provenance.

## R14 — The fine-sheaf embedding and extension argument span reversed scan order

**Source:** cote 43, scans 141, lines 4–12, and 139, lines 4–8. **Kind:** unpursued implication. **Words:** “isomorphe à un sous-faisceau d’un faisceau fin”; “extension à \(X\)”.

Typed page 87 on scan 141 begins the tensor embedding and a torsion-free-group lemma, whose proof continues on typed page 88 at scan 139 before the extension argument. The two actual constructions are \(F\to F\otimes_{\mathbb Z}\mathcal I\) and extension of the endomorphism \(\theta\) to \(\theta_0\) on \(G^Y\), so their maps can be compared directly with the extension-by-zero notation used on scans 135–140. CT 16:37 provides another stalk-level injectivity proof, but the supplied context has no matching pair of typed pages or FM-double-prime axiom.

**Context search:** R14; fine sheaf, extension, stalk; CT 16:37. **RS:** MPL_136_235-281 N16, provenance only; WG2 §1.1 #3 for the possible resolution-tool comparison.

## R15 — A stalkwise retraction checks the typed tensor embedding

**Source:** cote 43, scan 141, line 8. **Kind:** own idea. **Confidence:** high; the composite is explicitly the identity. **Anchor:** “\(f\longrightarrow f\otimes1\)”.

Write \(\mathcal I\) temporarily for the sheet's doubtfully read \(\mathcal I|\mathcal J\), the sheaf of germs of arbitrary \(\mathbb Z\)-valued functions: evaluation of a germ at \(x\) gives \(\mathrm{ev}_x:\mathcal I_x\to\mathbb Z\) with \(\mathrm{ev}_x(1)=1\). The homomorphism \(r_x:F_x\otimes_{\mathbb Z}\mathcal I_x\to F_x\), \(m\otimes a\mapsto\mathrm{ev}_x(a)m\), satisfies \(r_x(m\otimes1)=m\), proving the asserted injection on every stalk. This checks the particular embedding by explicit stalk morphisms and connects directly to CT 16:37's use of stalks to test an injectivity claim; a global sheaf retraction has not been constructed here.

**Context search:** R15; stalk, tensor, injective, injection; CT 16:37. **RS:** no matching settled register entry; this is a concrete verification of the current reused sheet.

