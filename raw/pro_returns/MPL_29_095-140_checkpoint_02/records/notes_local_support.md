# Local research support — cote 29, scans 095–140

Prepared 2026-11-18 after the root agent's transcription freeze (06:04:22 UTC). This is support for the root agent, not the final research notes or a shared result register. No scan, crop, or other source image was opened, and no transcription, page inventory, authoring script, or shared register was changed. All source comparisons below refer to the **frozen `.tex` readings**, including their explicit uncertainties, not to an independent inspection of the ink.

The supplied context is **Hua, modernised reading of cote 29**, an AI-produced interpretation, not a diplomatic transcription. Its own header says it changes hypotheses and notation to obtain mathematically correct statements, and identifies the separate transcription as controlling citations to Grothendieck; that separate transcription was not supplied here. No novelty, publication status, or final truth status is inherited from Hua or from the run statuses in `RESULTS_STATE.md`.

## Materials read and pagination

Read the context README, `hua_project/README.md`, and `notes/RESULTS_STATE.md`; read all of frozen pages 095, 097, 099, 106, 108, 109, 110, 111, 112, 118, 131, 132, 133, and 135. In `context/hua_project/29.modern.tex`, read the opening/header, the complete requested additional span **1381–2256**, the discussions covering pp.87–110 and the start of pp.112–115, the start of pp.116–120, and the supplied discussions covering the end of pp.124–129 and pp.130–134; whole-file keyword searches supplement those readings. This is not a claim that this agent alone read the entire modern file; the root is coordinating collective coverage.

Use **Hua page + 1 = our scan**. Direct examples: Hua p.130 is our scan131; Hua p.132 is scan133; Hua p.134 is scan135. These are archive/page locators, not dates. All modern-file line locators below are working aids, not substitute source-page references.

| Our scan | Hua page | Relevant material |
|---|---:|---|
| 095, 097, 099 | 94, 96, 98 | Reused typescript: diagonalizable groups, Corollaries 3.2–3.5 and start of §4 |
| 106 | 105 | EGA IV typescript, IV-878, §§17.4–17.5 |
| 108 | 107 | Comaximal ideals and Chinese remainder map |
| 109 | 108 | “Ad majorem fonctori gloriam” typescript |
| 110 | 109 | Product decompositions and monic factors; inserted connectedness |
| 111 | 110 | Local ring/completion notation and sketches |
| 112 | 111 | “Notes pour SGA 7” heading |
| 118 | 117 | Cancelled inverted typescript fragment (2.1.14.6) |
| 131 | 130 | Relative functor of pointed torsors |
| 132 | 131 | English typescript I-6, rational structures and “5. Conjugates” |
| 133 | 132 | Proposed representability criterion |
| 135 | 134 | Localization gluing lemma and inserted neighborhood condition |

## Candidate notes for the root (each narrative is 1–4 sentences)

Local labels below are provisional support labels; the root assigns final note/result IDs. “Relation” means the frozen source compared with the named context, except where explicitly described as an independent check of the context formulation.

### L01 — Keep the direction of the CRT implication

- **Witness / short source quote:** scan108, final diagram: “\(Q+Q'=A\Rightarrow QQ'=Q\cap Q'\)”; earlier “idéaux étrangers.”
- **Kind:** own idea — an independent targeted mathematical check of the context comparison.
- **Confidence / reason:** high; the CRT proof and the explicit polynomial-ideal counterexample are complete below.
- **Searches:** `étrangers`, `unitaire`, `comax`, `Q + Q'`, `Q \cap Q'`.
- **Context locator:** Hua, modernised reading of cote 29, **“Polynômes unitaires et idéaux étrangers”**, in **“Un feuillet d'EGA IV, et de l'algèbre commutative (pages 105 à 110)”**; Hua p.107 = scan108; modern lines2803–2816.
- **Relation:** **contradicts** the context's strengthened equivalence; the frozen source has only the valid implication in that place.
- **RESULTS_STATE:** no direct entry for this CRT statement; LM1 E.2/E.11 concern different group-scheme assertions.

**Candidate:** Scan108 makes surjectivity and bijectivity of the CRT map equivalent to comaximality, and then writes only “\(Q+Q'=A\Rightarrow QQ'=Q\cap Q'\).” Hua's subsection replaces the last implication by an equivalence, which is false: in \(k[x,y]\), \((x)\cap(y)=(xy)\) although \((x)+(y)\ne k[x,y]\). This counterexample concerns the modernized formulation, while the frozen source's CRT chain passes the independent check below.

### L02 — Connectedness is a substantive insertion in the monic-factor claim

- **Witness / short source quote:** scan110, inserted oval: deleted “\(A\) local,” replaced by “\(A\) connexe”; body “polynômes unitaires.”
- **Kind:** own idea — an independent re-proof of an unproved source claim and a counterexample to the context's omitted hypothesis.
- **Searches:** `unitaire`, `connexe`, `factorisations`, `décompositions`, `complété`.
- **Context locator:** same Hua subsection **“Polynômes unitaires et idéaux étrangers”**, Hua p.109 = scan110; modern lines2812–2816.
- **Relation:** **differs** by retaining the source's connectedness hypothesis; the disconnected example **contradicts** the broader context formulation, not the source with its insertion.
- **RESULTS_STATE:** no direct entry.

**Candidate:** Scan110 replaces “\(A\) local” by “\(A\) connexe” in the assertion that comaximal ideal factors of a monic principal ideal arise uniquely from monic polynomial factors, but Hua's formulation omits connectedness. That omission changes the assertion: for \(A=k\times k\), the comaximal ideals \(k[T]\times(T)\) and \((T)\times k[T]\) have product \((T,T)\), yet neither has a monic generator. For connected \(A\), the claim admits the independent proof below through the characteristic polynomials of multiplication by \(T\) on the two projective quotient summands. **Confidence: high**, because the rank argument proves the corrected statement and the component degrees give an explicit counterexample without connectedness; no novelty claim is made.

### L03 — The monic-factor proof stops before the completion argument is stated

- **Witness / short source quote:** scan110: “[petite vérification…]”; final words “on voit que c'est vrai sur les”.
- **Kind:** unverified step / unproved claim.
- **Searches:** `vérification`, `local`, `complété`, `existence`, `polynômes`.
- **Context locator:** Hua, **“Polynômes unitaires et idéaux étrangers”**, Hua pp.109–110 = scans110–111; modern lines2815–2816.
- **Relation:** **differs**: Hua completes the account by saying existence is seen on the completion; the frozen scan110 ends mid-sentence, and scan111 provides completion notation and drawings but no written proof of this assertion.
- **RESULTS_STATE:** no direct entry.

**Candidate:** Scan110 flags a “petite vérification” and ends its existence argument at “on voit que c'est vrai sur les.” Hua, “Polynômes unitaires et idéaux étrangers,” describes an existence argument on the completion, but the frozen continuation at scan111 gives only local-ring/completion notation and sketches. The characteristic-polynomial proof supplied in L02 is an independent completion of the argument, not a reading of missing words.

### L04 — Preserve the field-extension reading in the proposed criterion

- **Witness / short source quote:** scan133(v): “une ext. alg. close de \(k\)” and then “alg. clos”; the deleted intervening word and the map connector remain uncertain.
- **Kind:** reading question, with a separate targeted check of the two possible conditions.
- **Searches:** `algébrique séparable`, `alg.`, `localisation`, `corps`, `complet`.
- **Context locator:** Hua, **“Un critère de représentabilité”**, in **“Les « feuilles anciennes » : représentabilité et recollement (pages 130 à 134)”**; Hua p.132 = scan133; modern lines3469–3496, especially3481–3486.
- **Relation:** **differs**: Hua states invariance under algebraic separable extensions, while the frozen reading has algebraically closed language. Neither reading is silently substituted for the other.
- **RESULTS_STATE:** no direct entry; `29-fundamental-group-scheme-via-torsors` is adjacent thematic context, not an entry proving this criterion.

**Candidate:** In scan133(v), the frozen reading uses “alg. close” and “alg. clos,” whereas Hua, “Un critère de représentabilité,” states invariance under algebraic separable extensions and flags uncertainty in its own footnote. These conditions are mathematically different: the finite étale functor represented by \(\operatorname{Spec}\mathbb C\) over \(\mathbb R\) has no \(\mathbb R\)-point and two \(\mathbb C\)-points, while its points are unchanged by extensions between algebraically closed fields. This checks the difference between conditions; it does **not** refute Hua's implication under its stronger hypothesis or settle the doubtful source reading.

### L05 — The criterion is a proposed result with an unfinished proof

- **Witness / short source quote:** scan133: “et localisation” inserted; “alors \(F\) représentable”; last words “ils correspondent à des”.
- **Kind:** unproved claim / unverified steps.
- **Searches:** `localisation`, `limites inductives`, `complet`, `représentabilité`, `fini`.
- **Context locator:** Hua, **“Un critère de représentabilité”**, Hua p.132 = scan133; modern lines3469–3496.
- **Relation:** **restates** the criterion and its unfinished status, but **differs** at the field-extension hypothesis recorded in L04.
- **RESULTS_STATE:** no direct entry.

**Candidate:** Scan133 proposes representability by an étale separated quasi-finite object from limit compatibility, faithfully flat descent plus the inserted localization condition, complete-local invariance, separation, and fieldwise finiteness. Its proof begins over a complete local base with algebraically closed residue field, lifts the special-fibre elements uniquely, and breaks off at “ils correspondent à des.” Hua records the unfinished proof, but neither that account nor the elementary checks in this support record supplies a proof of the full criterion.

### L06 — The gluing statement includes neighborhood compatibility

- **Witness / short source quote:** scan135 insertion: “On suppose que pour tt \(s\)” and “sur un voisinage ouvert \(U\)”; the insertion also asks for maps \(\mathcal X\times_U\operatorname{Spec}(\mathcal O_t)\to X(t)\) compatible with the \(\varphi\)'s.
- **Kind:** own idea — an independent counterexample to a context strengthening; the source statement remains an unverified step.
- **Searches:** `recollement`, `voisinage ouvert`, `localisation`, `quasi-fini`, `cartésien`.
- **Context locator:** Hua, **“Le lemme de recollement”**, in **“Les « feuilles anciennes » : représentabilité et recollement”**; Hua p.134 = scan135; modern lines3498–3522.
- **Relation:** **differs**: the source inserts the neighborhood condition as a hypothesis, while Hua leaves it out of the lemma and describes realization over a neighborhood as a proposed proof strategy; source also explicitly requires Cartesian transition squares, absent from Hua's prose formulation.
- **RESULTS_STATE:** no direct entry.

**Candidate:** Scan135 inserts a hypothesis that each \(X(s)\) has an open-neighborhood model equipped with compatible maps to all the other local objects, in addition to Cartesian specialization maps and their cocycle. Hua's “Le lemme de recollement” omits that hypothesis and treats neighborhood realization as a proof strategy. The weaker context formulation is false even on \(\mathbb A^1_{\mathbb Q}\): the local objects in Check P4 below have compatible Cartesian restrictions but would force an étale morphism to have a non-open image. **Confidence: high** for that counterexample; the full source statement with the inserted condition has not been re-proved here.

### L07 — The relative torsor problem is narrower than the general finite-group question

- **Witness / short source quote:** scan131: inserted “étale” after deletion of “séparable”; “Il en serait de \(=\) pour \(G\) commutatif”; uncertain “Cas fini??”.
- **Kind:** self-flagged / unpursued extension / reading question.
- **Searches:** `fibrés pointés`, `fini et étale`, `commutatif`, `automorphisme`, `quasi-fini`, `limites`.
- **Context locator:** Hua, **“Le foncteur des fibrés pointés”**, Hua p.130 = scan131; modern lines3448–3467. Related but distinct: Hua **“La pro-représentabilité”**, pp.124–126, and the findings-register item `29-fundamental-group-scheme-via-torsors`.
- **Relation:** **adds** the source's marked uncertainty about the finite case and its commutative aside; **differs** where Hua says compatibility with limits while the frozen final sentence is the uncertain “ex. et à gauche” for faithfully flat quasi-compact morphisms.
- **RESULTS_STATE:** thematic link to `29-fundamental-group-scheme-via-torsors`, not a resolution of it; no direct entry for this relative representability problem. LM1 E.11's separated locally finitely presented group-scheme source theorem and LM1 E.2's unipotent-section theorem are different statements.

**Candidate:** Scan131 asks about the relative pointed-torsor functor for **finite étale** \(G\), under proper flat \(f\) and universal \(f_*\mathcal O_X=\mathcal O_S\), and adds the commutative aside and uncertain “Cas fini??” after the automorphism observation. Hua's “Le foncteur des fibrés pointés” captures the main question but omits those scope markers and the source's quasi-finite qualification “[cas à fibres finies].” The general finite-group case remains a question in this frozen passage; the findings-register item about strict pro-representability in the group variable does not itself answer this different relative question.

### L08 — Three diagonalizable-group typescript sheets are absent from the modern account

- **Witness / short source quotes:** scan095 “Corollaire 3.2”; scan097 inserted “avec \(H\) de type fini sur \(S\)”; scan099 “Fibrés principaux homogènes sous un groupe diagonalisable.”
- **Kind:** reading / paper-stratigraphy question, with a substantive hypothesis to retain.
- **Searches:** `diagonalis`, `Corollaire 3.2`, `Corollaire 3.3`, `Corollaire 3.4`, `Corollaire 3.5`, `D_S(M)`, `graduée`.
- **Context locator:** **no matching subsection**. Their positions are Hua pp.94,96,98, between **“Le cas où la classe s'annule : Picard formel (pages 91 et 93)”**, and **“Le théorème, et deux exemples (pages 95 et 97)”**, before **“Abhyankar semi-global… (pages 99 et 100)”**. The whole modern file has no `diagonalis` hit.
- **Relation:** **adds** previously uncovered sheets to the context's topical coverage; no historical priority or authorship claim.
- **RESULTS_STATE:** no direct result entry; the broad SGA3 placement fits these objects, but LM1 E.2/E.11 and MPL_11_043-058+56 N063/N100 do not state these corollaries. `29-formal-tame-pi1-self-intersection` concerns the interleaved handwritten material, not these three typescript faces.

**Candidate:** The inverted typescript faces at scans095,097,099 carry a coherent separate sequence, Corollaries 3.2–3.5 on diagonalizable groups followed by §4 on their principal homogeneous spaces, which Hua's modern file does not discuss. In particular scan097 inserts “avec \(H\) de type fini sur \(S\)” and later “qui implique \(N\) de type fini” in the local-diagonalization argument, so this hypothesis belongs to the recorded revision history. These sheets support the package's SGA3 connection independently of the interleaved tame-fundamental-group notes; their presence alone does not date or identify the reused typescript.

### L09 — The Bourbaki typescript is a separate documentary strand

- **Witness / short source quote:** scan109, “Ad majorem fonctori gloriam”; “J'apprends que Grothendieck n'est plus membre de Bourbaki.”
- **Kind:** reading / paper-stratigraphy question.
- **Searches:** `Ad majorem`, `Bourbaki`, `Kaplanski`, `fonctori`, `catégories`.
- **Context locator:** **no matching subsection**; Hua p.108 = scan109, inside the page span of **“Un feuillet d'EGA IV, et de l'algèbre commutative (pages 105 à 110)”** but omitted from its three subsections. Whole-file searches for `Ad majorem`, `Bourbaki`, and `Kaplanski` have no hits.
- **Relation:** **adds** documentary coverage absent from the context.
- **RESULTS_STATE:** no direct entry.

**Candidate:** Scan109 preserves the separate typescript “Ad majorem fonctori gloriam,” responding to Grothendieck's departure from Bourbaki and proposing adoption of his work on categories. Hua's account passes over this sheet while treating the neighboring algebra, and the frozen fragment stops as it introduces “une liste de questions catégoriques.” Neither a named author nor an explicit date is supplied by this frozen passage; “Bourbaki 1960” and “1936” are comparisons within the argument, not a signed dating line.

### L10 — The English rational-structure sheet interrupts the “feuilles anciennes”

- **Witness / short source quote:** scan132, “I-6”; “5. Conjugates”; “its graph \(\Gamma\) is a subspace … rational over \(k\).”
- **Kind:** reading / paper-stratigraphy question.
- **Searches:** `Conjugates`, `k-structure`, `multilinear`, `rational over`, `graph`.
- **Context locator:** **no matching subsection**; Hua p.131 = scan132, within **“Les « feuilles anciennes » : représentabilité et recollement (pages 130 à 134)”**, between the relative torsor question and the criterion. Whole-file searches for the quoted English terms have no hits.
- **Relation:** **adds** a separate reused text omitted from the modern account.
- **RESULTS_STATE:** no direct entry.

**Candidate:** Scan132 is an inverted English typescript page “I-6,” proving preservation of rational subspaces under images and inverse images, the graph criterion for a rational linear map, and beginning “5. Conjugates.” It is not a continuation of the representability argument in the adjoining handwritten pages, and Hua's subsection spanning pp.130–134 does not discuss it. A source, author, or date for that English text remains a reading question; none is inferred here.

### L11 — The EGA warning is covered, but its local wording should remain exact

- **Witness / short source quote:** scan106, “17.5. Caractérisations des morphismes lisses”; “Attention à l'ambiguïté dans ‘lisse’ !”; replacement of “noethérien” by “de type fini”.
- **Kind:** reading question / explicit revision.
- **Searches:** `17.4.10`, `17.5.1`, `IV-878`, `ambiguïté`, `lisse`, `simple`, `de type fini`.
- **Context locator:** Hua, **“« Attention à l'ambiguïté dans lisse ! »”**, Hua p.105 = scan106; modern lines2758–2779. Hua links it to **“Pic birationnel” / “Les deux corollaires et la question”**, p.74, outside this package.
- **Relation:** **restates** the typescript's principal content and correction; Hua's identification of the alternative term “simple” is contextual interpretation, not wording written in the warning itself.
- **RESULTS_STATE:** no direct entry.

**Candidate:** Scan106 supplies a substantial EGA IV typescript face, with (17.4.10), the four conditions of (17.5.1), the replacement “localement noethérien” by “localement de type fini,” and the warning about ambiguity in “lisse.” Hua covers this sheet and links the warning to “simple” in its earlier Picard discussion, but the warning on the frozen page does not itself specify that alternative term. The local correction and warning may be cited; the cross-sheet terminological explanation should be credited to Hua and kept distinct from the diplomatic wording.

### L12 — Do not convert sparse completion sketches and headings into propositions

- **Witness / short source quotes:** scan111 “\(A\) anneau local” with “intègre” deleted, “\(\widehat A\) son complété”; scan112 “Notes pour SGA 7”; scan118 cancelled “(2.1.14.6)”.
- **Kind:** reading / paper-stratigraphy question.
- **Searches:** `complété`, `intègre`, `Notes pour SGA`, `2.1.14.6`, `composante connexe`.
- **Context locator:** scan111 = Hua p.110, grouped under **“Polynômes unitaires et idéaux étrangers”** without a discussion of the sketches; scan112 = p.111, before **“Théorème de Bertini et variantes (pages 112 à 115)”**; scan118 = p.117, inside **“Comportement fonctoriel des groupes d'inertie (pages 116 à 120)”**, whose exposition does not mention the cancelled fragment.
- **Relation:** **adds** local documentary coverage; the p.110 sketches do not establish the completion proof asserted by the algebra summary.
- **RESULTS_STATE:** no direct entry.

**Candidate:** Scan111 gives completion notation and drawings with “intègre” deleted from the local-ring assumption, but no complete proposition or proof; scans112 and118 contribute respectively the heading “Notes pour SGA 7” and a cancelled formula fragment. These are sparse but distinct documentary elements not individually accounted for in Hua's mathematical exposition. Their proximity does not justify completing scan110's unfinished proof or treating the cancelled fragment as part of the inertia argument.

### L13 — The quoted doubt in Hua is not the frozen reading of scan135

- **Witness / short source quote:** scan135 final paragraph: uncertain “Je vais pour du moins ramener au local”; the following noetherian-induction wording is also uncertain.
- **Kind:** reading question.
- **Searches:** `raisonnement`, `ramener`, `récurrence`, `sûr`, `recollement`.
- **Context locator:** Hua, **“Le lemme de recollement”**, Hua p.134 = scan135; modern lines3519–3522.
- **Relation:** **differs**: Hua quotes an admission of uncertainty, but the frozen text does not contain that phrase.
- **RESULTS_STATE:** no direct entry.

**Candidate:** Hua's “Le lemme de recollement” quotes “Je ne suis pas [sûr] de mon raisonnement,” whereas the frozen scan135 ends with the uncertain reading “Je vais pour du moins ramener au local” followed by a noetherian-induction plan. Since no independent image reading is permitted in this research pass, that discrepancy remains a reading question and cannot be promoted into a source quotation or a source-authored self-flag. It has no effect on the independent counterexample to Hua's omitted hypothesis.

## Completed mathematical checks (full arguments)

These checks were performed by reasoning during this research pass; they are not inherited from the transcription process or from Hua. No formal prover or external literature was used. Their scope is precisely the displayed claims below, and none proves the full representability criterion or the gluing lemma with the source's added hypothesis.

### P1 — Correct CRT chain; counterexample to the context's converse

**Corrected statement (root to assign final ID).** For a commutative unital ring \(A\) and ideals \(I,J\), the canonical map
\[
\alpha:A/IJ\longrightarrow A/I\times A/J
\]
is surjective if and only if \(I+J=A\); in this event it is bijective and \(I\cap J=IJ\). Equality \(I\cap J=IJ\) alone says that \(\alpha\) is injective and does not imply surjectivity.

The kernel is visibly \((I\cap J)/IJ\). If \(\alpha\) is surjective, a preimage of \((1\bmod I,0\bmod J)\) gives \(a\in J\) with \(1-a\in I\), hence \(I+J=A\). Conversely, write \(u+v=1\) with \(u\in I\) and \(v\in J\). Given residues \(x\bmod I\), \(y\bmod J\), the element \(xv+yu\) maps to that pair, so \(\alpha\) is surjective. If \(z\in I\cap J\), then \(z=zu+zv\) lies in \(IJ\), proving \(I\cap J=IJ\) and therefore injectivity. This proves the chain in scan108 without Nakayama or any unstated finiteness hypothesis.

For the converse added by Hua, let \(A=k[x,y]\), \(I=(x)\), \(J=(y)\), for any field \(k\). If \(h\in(x)\cap(y)\), write \(h=yb\); reduction modulo \(x\) gives \(y\bar b=0\) in the domain \(k[y]\), hence \(b\in(x)\), so \(h\in(xy)\). The opposite inclusion is immediate, and therefore \(I\cap J=IJ=(xy)\). But \(I+J=(x,y)\) is proper, as evaluation at \((0,0)\) has this kernel. Equivalently, the CRT image consists of pairs of polynomials with the same constant term, so \((1,0)\) has no preimage. The false statement is **Hua's equivalence**, not the frozen source's implication.

### P2 — Why the connectedness omitted by Hua matters

**Refined statement (root to assign final ID).** Global monic factors require constant ranks of the two quotient summands; connectedness, explicitly inserted in scan110, supplies those ranks. The unrestricted formulation in the modernized paragraph is false.

Let \(k\) be a field and set \(A=k\times k\). Then
\[
A[T]\simeq k[T]\times k[T],\qquad P=T=(T,T),
\]
where \(P\) is a monic polynomial over \(A\). Put
\[
J=k[T]\times(T),\qquad J'=(T)\times k[T].
\]
Their sum is all of \(A[T]\), and their product is \((T)\times(T)=(P)\); consequently they give exactly the product-decomposition data under discussion.

If a monic polynomial \(Q\in A[T]\) generated \(J\), its two components \(q_1,q_2\in k[T]\) would be monic of the **same** degree, because the leading coefficient of \(Q\) is \((1,1)\). The first component ideal would force \((q_1)=k[T]\), hence \(q_1=1\) and degree 0, whereas the second would force \((q_2)=(T)\), hence \(q_2=T\) and degree 1. This is impossible; the same argument applies to \(J'\). Thus the modernized claim fails on a disconnected base even for a monic polynomial of degree 1. The source's connectedness insertion excludes this example.

### P3 — Independent proof of the connected-base monic-factor assertion

**Statement (root to assign final ID).** Let \(A\ne0\) be a commutative unital ring with connected spectrum, let \(P\in A[T]\) be monic, and let \(J,J'\subseteq A[T]\) satisfy
\[
J+J'=A[T],\qquad JJ'=(P).
\]
There are unique monic polynomials \(Q,Q'\) with \(J=(Q)\), \(J'=(Q')\), and \(P=QQ'\). No local, noetherian, or completeness hypothesis on \(A\) is needed for this formulation.

Write \(n=\deg P\), \(C=A[T]/(P)\), \(C_1=A[T]/J\), and \(C_2=A[T]/J'\). By P1,
\[
C\simeq C_1\times C_2.
\]
Since \(P\) is monic, \(C\) is finite free as an \(A\)-module, with basis \(1,T,\ldots,T^{n-1}\); for \(n=0\), it is the zero module. The two \(C_i\) are direct summands of this module, hence finite projective. Their rank functions are locally constant on \(\operatorname{Spec}A\), so connectedness makes them constant, say \(d_1,d_2\), with \(d_1+d_2=n\).

Let \(\tau_i\) be multiplication by the image of \(T\) in \(C_i\), and let \(Q_i(U)\) be its characteristic polynomial on the finite projective module \(C_i\). This is monic of degree \(d_i\); it is defined by the determinant on the top exterior power, and ordinary matrix characteristic polynomials on local free trivializations agree and hence glue. The matrix Cayley–Hamilton identity, checked after localization where the modules are free, gives \(Q_i(\tau_i)=0\). Since multiplication by a ring element kills the identity element only when that element is zero, this says \(Q_i(T)=0\) in \(C_i\). Therefore the quotient map factors as a surjection
\[
A[T]/(Q_i)\twoheadrightarrow C_i.
\]
Both sides are finite projective of constant rank \(d_i\), and the left side is actually free. Localizing at any prime of \(A\), this becomes a surjective map between free modules of equal finite rank over a local ring. Its reduction modulo the maximal ideal is an invertible square matrix, so its determinant is a unit and the map is an isomorphism. It follows that the original map is an isomorphism, and its kernel gives \(J=(Q_1)\), \(J'=(Q_2)\).

Multiplication by \(T\) on \(C\), in its monomial basis, has the companion matrix of \(P\), whose characteristic polynomial is \(P\). Under the direct-product decomposition it is the direct sum of \(\tau_1\) and \(\tau_2\), so multiplicativity of the determinant gives
\[
P=Q_1Q_2.
\]
Finally, if two monic polynomials generate the same ideal in \(A[T]\), each is a polynomial multiple of the other. Multiplication by a monic polynomial adds degrees, so the two divisibilities force equal degrees and constant multipliers; comparison of leading coefficients makes those multipliers 1. Thus each generator is unique. This proves the stated refinement but does not purport to reconstruct scan110's intended unfinished proof.

### P4 — Cartesian specialization data do not suffice for the weakened gluing lemma

**Refinement (root to assign final ID).** The existence claim for arbitrary Cartesian, cocycle-compatible localization data is false. The neighborhood compatibility hypothesis inserted in scan135 must not be dropped; this check does not prove its sufficiency.

Take \(S=\operatorname{Spec}\mathbb Q[t]\), let \(\eta\) be its generic point, and let \(K=\mathbb Q(t)\). Let \(E\) be the set of closed points \((t-n)\) for integers \(n\). Both \(E\) and its complement among closed points are infinite; for the latter, the points \((t-1/m)\), \(m\ge2\), suffice. Define
\[
X(\eta)=\operatorname{Spec}K,
\qquad
X(s)=
\begin{cases}
\operatorname{Spec}\mathcal O_{S,s},&s\in E,\\
\operatorname{Spec}K,&s\text{ closed and }s\notin E.
\end{cases}
\]
For a closed point \(s=(p(t))\), the local ring \(\mathbb Q[t]_{(p)}\) is a discrete valuation ring and inverting \(p\) gives \(K\). Hence \(\operatorname{Spec}K\to\operatorname{Spec}\mathcal O_{S,s}\) is a principal open immersion, in particular quasi-finite, étale, separated, and of finite presentation. All the prescribed \(X(s)\)'s therefore have the properties required by both the source and the weakened context statement.

There are no nontrivial chains of distinct specializations except \(\eta\rightsquigarrow s\) with \(s\) closed. For these, use the canonical map \(X(\eta)\to X(s)\); use identity maps for equal points. Every transition square is Cartesian: in either case the base change of \(X(s)\) to \(K\) is \(\operatorname{Spec}K\), since \(K\otimes_{\mathcal O_{S,s}}K=K\). The identity and cocycle conditions follow immediately; so this example satisfies even the Cartesian condition omitted from Hua's prose statement.

If an étale \(X\to S\) inducing these local objects existed, its fibre over a closed point \(s\in E\) would be a single point, its fibre over a closed point outside \(E\) would be empty, and its generic fibre would be a single point. Thus its image would be exactly \(\{\eta\}\cup E\). An étale morphism is open, so this image would have to be open. But every nonempty open subset of \(\operatorname{Spec}\mathbb Q[t]\) contains a nonempty principal open \(D(f)\), whose complement consists of finitely many closed points; hence every such open has finite complement. The complement of \(\{\eta\}\cup E\) is infinite, a contradiction.

The inserted hypothesis explains precisely what this example lacks. At \(s\in E\), a quasi-finite étale neighborhood model of \(X(s)\) has nonempty fibre at \(s\), and its image consequently contains an open neighborhood of \(s\). Compatible maps from its localizations to every \(X(t)\) would force its fibre to be empty at all closed \(t\notin E\), impossible on that neighborhood. This last observation uses the natural intended category of quasi-finite étale models; it does not resolve any uncertain word in the source insertion.

### P5 — Algebraically closed extension invariance differs from separable extension invariance

Let \(S=\operatorname{Spec}\mathbb R\), \(X=\operatorname{Spec}\mathbb C\), and let \(F\) be its functor of points over \(S\). The extension \(\mathbb C/\mathbb R\) is finite separable of degree 2, so \(X\to S\) is finite étale. For a field \(k\) over \(\mathbb R\), an element of \(F(k)=\operatorname{Hom}_{\mathbb R\text{-alg}}(\mathbb C,k)\) is exactly a root in \(k\) of \(U^2+1\).

There are no such roots in \(\mathbb R\), and in \(\mathbb C\) there are exactly two, \(i\) and \(-i\). Thus
\[
F(\mathbb R)=\varnothing,\qquad |F(\mathbb C)|=2,
\]
so the map along the algebraic separable extension \(\mathbb R\subset\mathbb C\) is not bijective. On the other hand, if \(k\subseteq k'\) are algebraically closed fields over \(\mathbb R\), both roots already lie in \(k\), and a degree 2 polynomial has no further roots in \(k'\); therefore \(F(k)\to F(k')\) is bijective. This proves that the two candidate forms of condition(v) are different, including for finite étale representable functors. It neither decides the source's uncertain phrasing nor shows that the criterion with Hua's stronger condition is false.

## Additional context coverage: lines1381–2256

The entire requested span was read. The following are useful **cross-references**, not proof checks of the claims attributed by Hua to pages outside the supplied package. Their mathematical and historical assertions remain credited to Hua unless the frozen source itself supplies them. No new CHECK_EVENTS are proposed just for this reading.

| Exact context section / subsection | Hua pages | Link to supplied frozen material | What may safely be said |
|---|---|---|---|
| “Un schéma formel modulo un sous-schéma de définition” / “Les modules cohérents”, “L'exemple, et ce qu'il calcule”, “Les revêtements” | 43,45 | scan111 writes a local ring, its completion, a closed subset and completed products; scan133 uses complete local rings | **Adds context**, not identification: Hua discusses formal completion, quotient categories and algebraization of covers. The shared objects do not turn scan111's drawings into that theorem, or complete scan110's proof. Searches: `complété`, `schéma formel`, `revêtements`, `à vérifier`. No direct RESULTS_STATE entry. |
| “Finitude en famille” | 44 | scan131's pointed-torsor functor in the varying base \(T\), with quasi-finiteness qualified by finite fibres | **Restates the family theme** already explicitly linked by Hua in “Le foncteur des fibrés pointés”; relative representability is a more specific question than a general uniform bound. Searches: `constructibilité`, `fibres`, `finitude`, `famille`. No direct RESULTS_STATE entry. |
| “Théorème de finitude relatif pour \(\pi_1\)” / “Lemme 1: un isomorphisme générique géométrique descend”, “Lemme 2: constructibilité de \(f_*\)”, “Lemme 3: \(H^1\) le long d'une partition”, “La proposition principale”, “Les deux corollaires”, “La récurrence sur la dimension” | 46–57 | scans131,133,135 combine pointed \(H^1\)-type objects, descent, localization, finite fieldwise sets and noetherian induction | **Adds a contextual comparison** of methods. Do not present these external-page summaries as a proof of the local criterion or substitute their distinct noetherian/Nagata/normality hypotheses. No direct RESULTS_STATE entry. |
| “\(\pi_1\) et \(\mathrm{Pic}^{\tau}\) birationnels: la première page” / “La question, et un mot anglais” | 59–60 | background to the later finiteness hypotheses, but no direct passage in the assigned scans | Read; **no new source-specific candidate**. |
| “Fin du théorème de finitude relatif: deux corollaires sur les produits” | 61–64 | contextual product statements recalled again in the letter of 1959, outside the assigned source-reading subset | Hua explicitly distinguishes prime-to-characteristic groups from the total group-scheme claim. This distinction may guide the root's letter notes, but this agent has not read scans125–130 and does not attribute a new source conclusion to them. Relevant context register: `29-fundamental-group-scheme-via-torsors`; no direct own-run result entry. |
| “\(\pi_1\) birationnel” / “Le lemme de Bertini de Zariski”, “Le passage à la limite sur les modèles” | 65–69 | general hypothesis discipline; scan111 deletes “intègre”, while scan106 distinguishes smoothness/regularity | Read; **no theorem transferred across these different settings**. The frozen deletion of integrality should not be reversed because a different theorem in context needs normality. |
| “Pic birationnel” / “Le théorème” | 70 | scan131 explicitly assumes universal \(f_*\mathcal O_X=\mathcal O_S\) | **Adds a same-object cross-reference**: Hua uses the same universal global-function condition in its Picard discussion. The birational/normal/proper assumptions there are different, so they do not furnish the missing relative torsor proof. Searches: `universellement`, `f_*`, `Pic`, `H^1`. No direct RESULTS_STATE entry. |
| “Pic birationnel” / “Le corollaire en caractéristique p”, “Le corollaire en caractéristique zéro”, “Les deux corollaires et la question”, “La borne uniforme, et la question finale” | 71–76 | scan106's warning about “lisse”; context's own footnote at p.105 connects the word “simple” at p.74 | **Restates Hua's terminological cross-reference**, with the source/context distinction in L11. No added proof check or claim concerning universal \(H^1\) invariance. |
| “Revêtements formels étales et théorème de Mumford: Murre revient” | 77–80 | completion and descent vocabulary in scan111; flat/étale distinctions in scans106,131 | **Adds context only**: Hua discusses ordinary étale neighborhoods and their formal completions, and where a geometric realization determines a cover. This does not establish any unwritten morphism in scan111. Searches: `étales formels`, `complétés`, `normalité`, `localisation`. |
| “Notes de lecture, et l'appel d'un champ” | 81,83,85 | scans131,133,135 explicitly invoke descent and gluing | **Adds context** to descent as a dossier-wide concern. The demand for a champ in those notes is not a proof of the relative representability or localization lemma, and no chronology is inferred. |
| “Deux feuillets de son propre tapuscrit: l'extension de Raynaud” | 82,84 | analogous presence of reused typescript sheets at scans095,097,099,106,109,132 | **Adds paper-stratigraphy context**, not an authorship or dating inference for our reused sheets. Its different finite-locally-free torsor completion statement is not silently applied to scan131's finite-étale question. |
| “Images inverses et voisinages infinitésimaux” | 86 | distinction between unramified and étale in scan106; completion/thickening vocabulary | Read; **no source-specific conclusion** beyond maintaining the difference between the two morphism classes. |

### Two optional concise cross-reference candidates

**L14 — Relative representability and finiteness in families.** Scan131's “quasi-fini sur \(S\) [cas à fibres finies]” places its pointed-torsor question beside the constructibility agenda that Hua calls “Finitude en famille” (Hua p.44; related explicit link in “Le foncteur des fibrés pointés,” p.130 = scan131). The shared object is the variation of finite torsor data with the base, but a constructibility program is not the missing representability proof. **Kind:** unpursued implication/cross-reference; **relation:** adds contextual link; **searches:** `constructibilité`, `finitude`, `fibres`, `famille`; **RESULTS_STATE:** no direct entry.

**L15 — The universal global-function hypothesis has a separate Picard use.** Scan131 explicitly underlines the universal form of \(f_*\mathcal O_X=\mathcal O_S\), while Hua, “Pic birationnel” / “Le théorème” (Hua p.70), uses the same condition in its discussion of injectivity on Picard functors. That is a useful same-object cross-reference, not a transfer of the birational argument's hypotheses or conclusion to the pointed-torsor problem. **Kind:** unpursued implication/cross-reference; **relation:** adds contextual link; **searches:** `universellement`, `Pic`, `f_*`; **RESULTS_STATE:** no direct entry.

## Proposed CHECK_EVENTS entries — root assigns IDs and writes the register

All checks below were actually performed in this research pass, 2026-11-18, by **GPT-6 Astra Pro (research-support agent; effort setting not exposed to this agent)**. The root should use its actual required schema and final IDs. These rows are proposals only; no shared register was edited. The local proof labels are support locators, not final result IDs.

| Proposed event type (allowed wording) | Exact checked claim and outcome | Refined statement / final-ID placeholder | Evidence |
|---|---|---|---|
| **refuted, with refined statement's id** | Refuted the reverse implication \(I\cap J=IJ\Rightarrow I+J=A\) in Hua's CRT equivalence, using \((x),(y)\subset k[x,y]\); also directly established the correct CRT chain retained by scan108. | Root assigns ID to P1's corrected CRT chain. Scope: context formulation. | P1; source scan108; Hua “Polynômes unitaires et idéaux étrangers,” p.107. |
| **refuted, with refined statement's id** | Refuted the monic-factor claim without connectedness using \(A=k\times k\), \(P=T\), and the two ideals of differing component ranks. | Root assigns ID to P3's connected-base theorem / P2's constant-rank refinement. Scope: context omission. | P2; source scan110; Hua same subsection, p.109. |
| **independent re-proof** | Proved that, over a nonzero ring with connected spectrum, comaximal factors of a monic principal ideal are uniquely generated by monic factors of the polynomial, using finite projective summands, characteristic polynomials and Cayley–Hamilton. | Root assigns ID to P3. This is an independent proof, not recovered source text. | P3; source scan110's connectedness insertion and unfinished argument. |
| **refuted, with refined statement's id** | Refuted existence from Cartesian specialization/cocycle data alone via local objects on \(\mathbb A^1_{\mathbb Q}\) whose proposed global image is non-open. | Root assigns ID to P4's negative refinement: specialization compatibility alone is insufficient; retain the source's neighborhood condition. No proof of sufficiency is claimed. | P4; source scan135; Hua “Le lemme de recollement,” p.134. |
| **targeted proof check** | Checked that invariance under extensions between algebraically closed fields differs from invariance under all algebraic separable field extensions, by the finite étale functor represented by \(\operatorname{Spec}\mathbb C/\mathbb R\). | Root assigns ID to the distinction in P5 / note L04. Neither criterion nor uncertain reading is resolved. | P5; source scan133(v); Hua “Un critère de représentabilité,” p.132. |

No event is proposed for merely reading context, searching terms, comparing quotations, or finding omitted sheets. No full proof check was performed for the representability criterion, the gluing statement **with** its added neighborhood hypothesis, the automorphism assertions for pointed torsors, or any of the outside-package results summarized in lines1381–2256.
