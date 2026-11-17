# Research working record: weights, levels, admissibility and direct images

Research after the transcription freeze only; no page, transcription, doubt or inventory file has been edited. Prepared by the research subagent for root's synthesis. All manuscript quotations below are from the frozen page files, including their uncertainty where relevant; mathematical corrections remain research notes. This record is not an independent transcription.

## Provenance and notation

- **P**: `work/MPL_12_099-149/pages/MPL_12_099-149_12_scanNNN.tex`; locators below use cote/scan and the paragraph, formula or margin, rather than artificial manuscript line numbers.
- **H**: `context/hua_project/12.modern.tex`, credited throughout as **Hua, modernised reading of cote 12**; H's page numbering is one less than the scan numbering. H is an AI-produced interpretation, not a primary witness and not our result.
- **CT**: `context/MPL_16+47+54+44_transcription.tex`; **CN**: the corresponding `_notes.md`, an earlier unreviewed research return.
- **RS**: `context/notes/RESULTS_STATE.md`; `12-immersion-level-bound` is Hua's conjectural candidate, with intake “new to us”, not a reviewed theorem. `WG2` entries are unchecked planning questions; other run statuses remain those stated in RS.
- In the analysis, “Hodge level” means the maximum of \(|a-b|\) over nonzero Hodge types of the weight-graded pieces; it is distinguished from geometric generation level, the dimension type of 12/125, and coniveau. These meanings must not be silently identified.

## Note records

### W01 — Properness and the maximal quotient of the expected weight

**Witness:** 12/099, item 6; 12/105–106, Proposition 1 and Corollary 1. **Kind:** unpursued implication. **Quote:** “le plus grand quotient ... de poids i”. **Context search:** `quotient | poids | résolution`; H, “Le plan (page 98)” and “Poids de la cohomologie $\ell$-adique d'une variété singulière ou non propre (pages 104 à 108)”; relation: restates the planned distinction and adds its worked spectral sequence. **RS:** WG2 §2.4 #3, unchecked plan; no settled RS theorem used.

The outline distinguishes a quotient of the cohomology of a proper singular variety from the image in the cohomology of a smooth compactification of an open smooth variety; the two directions should be retained in any explanatory reconstruction. Deligne (1974, Proposition 8.2.5) later identifies the weight-\(i\) quotient for proper \(X\) through a proper surjective smooth model, giving an exact comparison for the first statement. This does not assert that the full mixed cohomology injects into a resolution.

### W02 — The normalization map in the two-line example is not injective

**Witness:** 12/101, final diagram. **Kind:** unpursued implication; explicit counterexample calculation credited to Hua. **Quote:** “inj?”. **Context search:** `normalisation | contre-exemple | inj`; H, “Un contre-exemple (page 100)”; relation: confirms H's calculation and adds a published contextual link. **RS:** no settled entry; bears on the weight/level part of WG2 §2.4 #3 only as method.

For the configuration drawn, localization gives \(H_c^1(X)=\mathbb Q\), \(H_c^1(Y)=\mathbb Q\), and \(H_c^1(U)=0\), while \(\widetilde Y\) is the disjoint union of two affine lines and has \(H_c^1(\widetilde Y)=0\); hence the proposed injection fails. This is Hua's reconstruction, and the frozen transcription independently supports its incidence assumptions without correcting the source's malformed displays. A relevant published comparison is Grothendieck's April 1969 addition to *Hodge's general conjecture* (p. 300), which warns that an earlier general support statement was false and retains a proper, rational, constant-coefficient version; Deligne (1974, Remark 8.2.9) also records an insufficient earlier justification. These references locate a closely related restriction, without establishing that this particular sheet supplied the published correction.

### W03 — The low-degree table separates purity from semisimplicity

**Witness:** 12/104, both margins and the paragraph after the \(H^2\) table. **Kind:** unproved claim. **Quote:** “morceaux purs sont semi-simples”. **Context search:** `semi-simple | poids`; CT 16/049, “category of motives which is semi-simple”; H, “Deux feuillets d'approche (pages 101 et 103)”; relation: adds a low-degree cohomological version to CT's conditional motivic yoga. **RS:** WG2 §2.3 #7 and §2.4 #3, unchecked plans.

Purity of Frobenius eigenvalues does not alone imply arithmetic semisimplicity, and the exceptional treatment of weight 2 on this sheet indicates that the category and geometric hypotheses matter. The later geometric semisimplicity theorem applies after passing to the geometric base, with its normality/lissity hypotheses, rather than declaring every pure arithmetic representation semisimple (Deligne, 1980, Theorem 3.4.1(iii)). The sheet should therefore be read as an expectation about geometric constituents or motives, not a proved formal consequence of the weight table.

### W04 — A pure arithmetic self-extension tests the scope of the claim

**Witness:** 12/104; 12/111–114, extension-closed admissibility and Corollary 5.2. **Kind:** own idea. **Quote:** “extensions”; “semi-simplicité”. **Context search:** `extension | semi-simplicité | strictement spécial`; H, “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)”; relation: differs from H's categorical collapse of effective admissibility into strict speciality. **RS:** WG2 §2.3 #7, unchecked plan. **Confidence:** high, because the counterexample is a two-dimensional continuous representation and its invariant line can be checked directly.

On \(\operatorname{Spec}\mathbb F_q\), send geometric Frobenius to \(\begin{pmatrix}1&1\\0&1\end{pmatrix}\), extending continuously through \(\widehat{\mathbb Z}\to\mathbb Z_l\); this is a nonsplit extension of \(\mathbb Q_l\) by itself, although every eigenvalue has weight 0. It is effectively admissible of weight 0 under the extension-closed definition, whereas weight-0 special objects come from finite monodromy \(H^0\)-representations and are semisimple over \(\mathbb Q_l\). Thus even a hypothesis making geometric special constituents semisimple would not collapse the entire extension-closed admissible category into strict special objects. The manuscript's actual argument in 12/114 first uses dévissage and only then semisimplicity on special constituents, so this example criticizes the overstrong summary, not that dévissage strategy.

### W05 — The “wrong order” of weights is a question about extension categories

**Witness:** 12/104, final paragraph. **Kind:** conjecture / self-flagged. **Quote:** “il semble ... mélange de poids dans le mauvais ordre”; “peut-être non triviale”. **Context search:** `mauvais ordre | extension | poids`; H, “Deux feuillets d'approche (pages 101 et 103)”; relation: restates the uncertainty and specifies what must be checked. **RS:** LM7 C.1 [Known, run claim] and C.8 [Refuted, run claim], by the distinction between mixed realizations and a choice of splitting, not as a proof of this question.

A precise test must specify the base field, the direction of the extension, and whether the category is arithmetic representations, mixed Hodge structures or conjectural motives. In a category with a strict functorial increasing weight filtration, an extension whose subobject has strictly higher weight than its quotient splits by lifting the lower weight subobject; the draft has not yet established that formalism for its geometric definition. Its concern is therefore useful evidence for why weight order and the existence of a canonical filtration require proof, and it does not authorize identifying all mixed-object splittings in the Fermat tower.

### W06 — Ordinary and compactly supported cohomology have different ranges

**Witness:** 12/105–108, constant-coefficient discussion. **Kind:** unpursued implication / literature comparison. **Quote:** “Par dualité”; “effectif”. **Context search:** `poids | supports propres | dualité`; H, “Poids de la cohomologie $\ell$-adique d'une variété singulière ou non propre (pages 104 à 108)”; relation: confirms the principal constant-coefficient ranges. **RS:** WG2 §3.2 #7, unchecked six-operation plan.

For a separated finite-type \(n\)-dimensional variety, the constant-coefficient compactly supported range is \(\max(0,2(i-n))\le w\le i\), whereas for smooth \(X\) ordinary cohomology has \(i\le w\le2\min(i,n)\). The analogous Hodge-type bounds for arbitrary separated complex varieties are given in Deligne (1974, Theorem 8.2.4), and the arithmetic compact-support and smooth lower-weight statements occur in Deligne (1980, Corollaries 3.3.3–3.3.5). These comparisons establish the numerical realization statements in their modern settings; they do not identify Hodge level with the manuscript's geometric level or supply arithmetic semisimplicity.

### W07 — What the weight argument actually makes degenerate

**Witness:** 12/105–106, the normal-crossing spectral sequence. **Kind:** unproved claim with a reconstructible argument. **Quote:** “dégénérée par des raisons de poids”. **Context search:** `dégénère | poids q`; H, “Poids de la cohomologie $\ell$-adique d'une variété singulière ou non propre (pages 104 à 108)”; relation: adds the page-of-degeneration distinction to H's summary. **RS:** WG2 §3.2 #7, unchecked plan.

The first differential can connect terms of the same pure weight, so the argument concerns \(E_2\), after forming cohomology of the alternating complex of strata. For \(r\ge2\), a differential from bidegree \((p,q)\) to \((p+r,q-r+1)\) connects distinct pure weights and is zero in the relevant realization category. This gives the graded constituents of a filtration, not a canonical splitting of the abutment into them.

### W08 — Strong resolution is an admitted input, not a result here

**Witness:** 12/105, opening; 12/107–108, descent induction; 12/113, margin. **Kind:** self-flagged. **Quote:** “résolution forte (que nous admettons)”. **Context search:** `résolution | descente | propre`; H, “Poids de la cohomologie $\ell$-adique d'une variété singulière ou non propre (pages 104 à 108)” and “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)”; relation: restates the assumption and separates a later substitute. **RS:** WG2 §3.2 #7, unchecked plan.

The draft assumes a smooth compactification with a normal-crossing boundary and later invokes proper descent for iterated fibre products that themselves need not be smooth. De Jong (1996, Theorem 4.1 and the introduction's hypercover construction) supplies alterations and proper hypercovers, allowing many rational realization arguments to be rebuilt without the full birational resolution assumed here. It would overstate this comparison to say that alterations prove strong resolution or automatically preserve every integral or geometric-level claim in the draft.

### W09 — Nonseparated schemes remain a separate scope question

**Witness:** 12/107, smooth nonseparated case. **Kind:** self-flagged. **Quote:** “le niveau ne serait-il ≤2n−i ?”. **Context search:** `non séparé | niveau`; H, “Poids de la cohomologie $\ell$-adique d'une variété singulière ou non propre (pages 104 à 108)”; relation: restates the question, rather than applying the separated theorem without comment. **RS:** WG2 §3.2 #7, unchecked plan.

The manuscript uses an affine-cover spectral sequence and deliberately weakens the lower-weight claim in the nonseparated case. Deligne (1974, Example 8.3.7) similarly extends the construction to nonseparated schemes while distinguishing the additional smooth-case weight assertion from the separated theorem. The present note records the dimension-bound question without promoting it to a theorem for every nonseparated scheme.

### W10 — The Deligne step supplies a derived decomposition under Lefschetz

**Witness:** 12/108 and 12/114, the Leray sequences; 12/122, the coefficient reduction. **Kind:** unpursued implication / literature comparison. **Quote:** “D'après Deligne”; “morceau”. **Context search:** `Deligne | dégénère | Lefschetz`; H, “Deux feuillets d'un rapport, lus dans l'ordre 122 puis 120” and “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)”; relation: confirms the intended mathematical input but not the provenance of unretained typed faces. **RS:** WG2 §3.2 #7, unchecked plan.

Deligne (1968, Theorem 1.5 and Proposition 2.4) constructs a derived decomposition from the Lefschetz condition, which implies the Leray degeneration used here. For a direct summand of \(R^jg_*\mathbb Q_l\), applying a further derived direct image can therefore justify the asserted “piece” of total cohomology. The reduction from an arbitrary subquotient to such a direct summand remains a separate semisimplicity step, explicitly noticed in the manuscript.

### W11 — The missing coefficient weight in 12/109 is substantive

**Witness:** 12/109, C.2 and the final question mark. **Kind:** own idea / reading question. **Quote:** “poids ... ≤Inf(2i,2n)”; “?”. **Context search:** `coefficients | j | poids`; H, “Poids de la cohomologie $\ell$-adique d'une variété singulière ou non propre (pages 104 à 108)”, final footnote; relation: confirms H's objection, without adopting H's replacement as a transcription. **RS:** no settled RS entry. **Confidence:** high, because the degree-zero example is immediate.

Take \(X=\operatorname{Spec}k\), \(i=n=0\), and \(F=H^1(E_{\bar k},\mathbb Q_l)\) for an elliptic curve, so that \(j=1\). Then \(H^0(X_{\bar k},F)=F\) has weight 1, contradicting the displayed upper bound 0; the parameter \(j\) cannot disappear in that generality. Hua already identifies this defect and supplies a modernized replacement; the frozen text retains the original formula and its question mark.

### W12 — The lower-bound margin concerns a support distinction

**Witness:** 12/108, margin adjacent to the compact-support paragraph. **Kind:** reading question. **Quote:** “les poids sont-ils ≥j”. **Context search:** `les poids | j | supports`; H, “Poids de la cohomologie $\ell$-adique d'une variété singulière ou non propre (pages 104 à 108)”, footnote after B; relation: differs from H's unqualified affirmative answer. **RS:** no settled RS entry.

Hua answers using the lower bound \(i+j\) for ordinary cohomology of a smooth base, whereas the frozen margin sits beside the paragraph on \(H_c^i\). That argument does not answer the compact-support version: invariants at a multiplicative elliptic degeneration can have weight 0 even when the lisse coefficient has weight 1. The attachment must remain a reading question, and the two mathematical interpretations should be stated separately.

### W13 — A Tate degeneration refutes the proposed sharper twisted weight bound

**Witness:** 12/108, the two upper-bound questions; 12/120, the first questioned coefficient display. **Kind:** own idea. **Quote:** “2Inf(i,n)+j ?”. **Context search:** `strictement spécial | 2inf | j`; H, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)” and “La filtration par le niveau (pages 34 et 35)”; relation: contradicts the questioned extension to general strictly special coefficients, which H leaves open, and H's earlier blanket assertion that \(R^rf_*\) raises coefficient weights by at most \(2r\). **RS:** bears on `12-immersion-level-bound` only by separating its constant-coefficient statement from the proposed coefficient variant; does not refute the former. **Confidence:** high, because tame inertia cohomology of the rank-two degeneration is explicit.

Let \(a:U\hookrightarrow C\) be an open smooth curve and \(\pi:E\to U\) an elliptic family with split multiplicative reduction at a missing rational point, and put \(F=R^1\pi_*\mathbb Q_l\), which is strictly special of weight 1. At that point the local representation has \(0\to\mathbb Q_l\to V\to\mathbb Q_l(-1)\to0\) with nonzero unipotent inertia, so \(H^1(I,V)=V_I(-1)=\operatorname{coker}[N:V\to V(-1)]=\mathbb Q_l(-2)\); hence \((R^1a_*F)_y\) has weight 4, while the proposed bound with \(i=n=j=1\) is 3. The local exact sequence is exhibited in Ito, Kato, Nakayama, and Usui (2020, Remark 3.2.11), and the weight-monodromy convention agrees with Deligne (1980, Theorem 1.8.4). This is a test of the proposed bound, not a claim of novelty or a change to the source.

### W14 — The same local model explains low compact-support weights

**Witness:** 12/108, lower-bound margin; 12/113, lower range independent of \(j\). **Kind:** own idea. **Quote:** “2(i−n)”. **Context search:** `borne inférieure | j | poids`; H, “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)”, explanation after Theorem 5.1; relation: supports H's observation that the lower bound need not depend on coefficient weight. **RS:** no settled RS entry. **Confidence:** high, because the global monodromy, local invariant lines and localization injection are explicit. **Independent check:** `records/independent_weight_examples_check.md`, V1 and “Compact-support counterpart”.

Over an odd finite field \(k=\mathbb F_q\) in which \(-1\) is a square, take the Legendre elliptic family \(\pi:E\to U=\mathbb P^1_k-\{0,1,\infty\}\), \(y^2=x(x-1)(x-\lambda)\), and \(F=R^1\pi_*\mathbb Q_l\). Its geometric monodromy is \(\mathrm{SL}_2\), so \(H^0(U_{\bar k},F)=0\) (Katz, 2012, Chapter 15, p. 77). At both \(\lambda=0\) and \(1\), split multiplicative reduction gives an invariant line \(\mathbb Q_l\) of weight 0, and localization therefore injects \(\mathbb Q_l^2\) into \(H_c^1(U_{\bar k},F)\). Thus the lower bound \(w\ge j\) fails for \(j=1\), whereas the manuscript's \(w\ge2(i-n)=0\) remains compatible with this example.

### W15 — A duality display contains two different weight sets

**Witness:** 12/112, Proposition 3.3(d). **Kind:** reading question. **Quote:** “2n−Φ={n−i ...}”. **Context search:** `2n | dualité | poids`; H, “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)”, Proposition 3.3(d); relation: differs in the literal set displayed, which H normalizes. **RS:** no settled RS entry.

Under the stated Tate convention, dualizing weight \(i\) and twisting by \(-n\) gives weight \(2n-i\), whereas the frozen set-builder expression contains \(n-i\). Already \(F=\mathbb Q_l\), \(n=1\), gives \(F^\vee(-1)=\mathbb Q_l(-1)\) of weight 2 rather than 1. This records an internal mathematical discrepancy without deciding whether the manuscript intended a different letter or omitted a coefficient.

### W16 — Intersecting weight constraints is not tautological in the proposed definition

**Witness:** 12/111, final margin; 12/112, definition 4.1 and warning. **Kind:** self-flagged. **Quote:** “il n'est pas tautologique”; “plus fort que la conjonction”. **Context search:** `tautologique | conjonction | filtration`; H, “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)”, definitions 3.1–4.1; relation: adds the exact logical warning to the modernized account. **RS:** `12-immersion-level-bound`, a candidate rather than an established category-theoretic identification.

The definition asks for the existence of geometric presentations and filtrations, so two separate witnessing filtrations do not automatically give a common one satisfying both restrictions. Modern canonical weight filtrations supply useful realization-level comparisons, but they do not by themselves prove that the same geometric constituents simultaneously witness a specified level bound. This is one reason not to replace the manuscript's “weight and level” class by a conjunction of numerical eigenvalue and Hodge-type inequalities.

### W17 — The theorem is deliberately narrowed to strictly special coefficients

**Witness:** 12/108, dévissage insertion; 12/113, opening of Theorem 5.1; 12/114, Corollary 5.2. **Kind:** withdrawn in the same text / self-flagged. **Quote:** “par dévissage (possible ici ?)”; “strictement spécial”; “semi-simplicité utilisée!”. **Context search:** `facteur direct | sous-quotient | semi-simplicité`; H, “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)”; CT 16/049; relation: adds an explicit restriction to the older semisimplicity programme. **RS:** WG2 §2.3 #7 and §2.4 #3, unchecked plans.

The broad coefficient hypothesis is visibly deleted and replaced by a direct-summand hypothesis in 12/113, while 12/114 recovers a broader statement conditionally through the semisimplicity part of Tate's conjectures. The change addresses the fact that a cohomological functor does not transport an arbitrary subquotient as though it were a direct summand. Both the initial doubt on 12/108 and the restriction/conditional recovery on 12/113–114 should be indexed rather than summarized as one unconditional theorem.

### W18 — The spread-out reduction has separate inseparability and resolution inputs

**Witness:** 12/113, proof and margins; 12/127, bracket after the smooth open. **Kind:** unproved claim / self-flagged. **Quote:** “fini plat radiciel”; “on est obligé ... d'admettre une extension radicielle”. **Context search:** `radiciel | résolution | base`; H, “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)” and “Divers types de $\mathbb{Q}_{\ell}$-faisceaux (pages 124 à 136)”; relation: restates the procedural need and adds its scope. **RS:** WG2 §3.2 #7, unchecked plan.

A finite universal homeomorphism is invisible to the étale topos, but that invariance alone does not produce the smooth proper relative compactification with relative normal crossings required in the proof. Such a model is first arranged generically using the admitted resolution input and then spread out, with a shrinking or stratification of the base. The two operations should remain distinct when checking whether the argument proves a global statement on the original base.

### W19 — Corollary 5.2 uses dévissage, not a collapse of categories

**Witness:** 12/114, proof of Corollary 5.2. **Kind:** reading question / unpursued implication. **Quote:** “par dévissage et déf”; “alors par semi-simplicité F est ... spécial”. **Context search:** `effectivement admissible | strictement spécial | dévissage`; H, “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)”, Corollary 5.2; relation: differs from H's sentence “effectivement admissible devient strictement spécial”. **RS:** WG2 §2.3 #7, unchecked plan.

The source reduces to special constituents through a filtration before applying semisimplicity, which is a weaker and more defensible claim than saying that every effectively admissible extension becomes strictly special. W04 gives an explicit arithmetic self-extension showing why the distinction matters. This correction belongs only to the explanatory account and leaves the conditional corollary to be checked through its long exact sequences.

### W20 — The unconditional admissibility corollary still needs its own proof

**Witness:** 12/114, Corollary 5.3; 12/129 and 12/131, alternate proof attempt. **Kind:** unproved claim. **Quote:** “sans conj. type Tate”; “Pour continuer, il faut utiliser ... complète réductibilité”. **Context search:** `sans | complète réductibilité | factorisation d'Artin`; H, “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)” and “Divers types de $\mathbb{Q}_{\ell}$-faisceaux (pages 124 à 136)”; relation: adds the tension between the asserted unconditional closure and the later explicit obstruction. **RS:** WG2 §3.2 #7, unchecked plan.

The unweighted closure of effective admissibility under \(R^if_!\) is asserted without the Tate hypothesis, but the later type-controlled proof still invokes complete reducibility to replace a subquotient by an entire geometric cohomology sheaf. A proof must explain how the Artin-curve reduction and the spectral-sequence dévissage avoid that step, or retain an additional hypothesis. The later manuscript is an attempted method, not evidence that the stronger unweighted assertion was already proved on 12/114.

### W21 — The literal level bound in Corollary 5.4 fails on an elliptic curve

**Witness:** 12/115, opening display; compare 12/108. **Kind:** own idea / reading question. **Quote:** “2(n−i+j)”. **Context search:** `2n-i+j | Corollaire 5.4`; H, “Faisceaux $\ell$-adiques admissibles et motifs virtuels (pages 110 à 114)”, Corollary 5.4; relation: differs from H's corrected expression and the earlier draft. **RS:** no settled RS entry. **Confidence:** high, because the weight-one Hodge structure of an elliptic curve supplies a direct test.

For a smooth projective elliptic curve, take \(n=i=1\), \(j=0\), and \(F=\mathbb Q_l\). The displayed bound in 12/115 gives level 0 at weight 1, whereas \(H^1\) has types \((1,0)\) and \((0,1)\), hence level 1. The earlier expression \(2n-i+j\) on 12/108 passes this test and is the expression used by Hua, but the frozen source must retain \(2(n-i+j)\).

### W22 — What the constant-coefficient immersion bound says

**Witness:** 12/116, setup; 12/118, tables; 12/120, boxed summary. **Kind:** unproved claim / unpursued implication. **Quote:** “poids ≤2Inf(i,n)”; “niveaux ≤Inf(i,n−1)”. **Context search:** `immersion | niveau | n-1`; H, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)”; relation: confirms the central displayed claim and credits H's discovery of the stronger local interpretation. **RS:** `12-immersion-level-bound` [conjectural candidate; intake “new to us”].

The dimension is that of the closure of the immersion's image, not the dimension of its point fibres, and the manuscript assumes a regular source and a resolution that is an isomorphism there. The preceding table on 12/120 is stronger than the final uniform bound: for \(i\ge n\) its levels decrease as \(2n-1-i\), reaching 0 in degree \(2n-1\). Hua's Hodge reconstruction supports this positive-dimensional constant-coefficient pattern, but the identification with every arithmetic/geometric meaning of “niveau” is not supplied by a Hodge calculation.

### W23 — Reconstructing the one-unit local gain in Hodge level

**Witness:** 12/116–120. **Kind:** own idea, verifying an argument credited to Hua. **Quote:** “n−1”. **Context search:** `F_q | boîte | fibre`; H, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)”, long footnote; relation: supports and makes explicit H's fibre-dimension mechanism. **RS:** `12-immersion-level-bound`, candidate. **Confidence:** high for the type inequality once the usual mixed-Hodge local spectral sequence is available; medium for identifying it with the manuscript's geometric-level claim.

At a boundary point, let \(h:Y'\to Y\) be a proper resolution with normal-crossing boundary \(D\), and set \(F_0=h^{-1}(y)\), \(F_q=h^{-1}(y)\cap D^{(q)}\); then \(\dim F_0\le n-1\) and \(\dim F_q\le n-q\) for \(q>0\). A term \(H^{i-q}(F_q)(-q)\) has Hodge coordinates between \(\max(0,i-n+1)\) and \(\min(i,n)\), using the proper-variety bounds of Deligne (1974, Theorem 8.2.4), so subquotients and extensions have level at most \(\min(i,2n-1-i)\). The crucial improvement is the exceptional fibre dimension for \(q=0\), rather than a new global smooth-variety bound. Hua cites Durfee (1983) for the local mixed-Hodge formalism; that paper's full text was not retrievable in this research pass, so its exact spectral-sequence indexing is a verification limit, not a checked quotation.

### W24 — The zero-dimensional edge case needs to be excluded

**Witness:** 12/120, final constant-coefficient box. **Kind:** own idea. **Quote:** “Inf(i,n−1)”. **Context search:** `dimension | n-1 | immersion`; H, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)”; relation: adds a missing boundary case to H and the candidate register. **RS:** `12-immersion-level-bound`, candidate. **Confidence:** high, because the identity of a point suffices.

For the identity immersion of a point, \(n=i=0\), the nonzero sheaf \(R^0f_*\mathbb Q_l\) has level 0, while the literal formula gives level at most \(-1\). Thus the uniform statement needs \(n\ge1\), a separate degree-zero convention, or an explicit restriction to boundary stalks and positive degrees. This edge case does not affect the nontrivial positive-dimensional table.

### W25 — The top-weight E2 term need not survive

**Witness:** 12/120, line above the final summary. **Kind:** own idea. **Quote:** “poids 2n s'identifie avec ... E2”. **Context search:** `s'identifie | E_2 | 2n`; H, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)”; relation: adds a spectral-sequence caveat to H's top-weight description. **RS:** `12-immersion-level-bound`, candidate. **Confidence:** high, because the blowup example has explicitly computable strata and abutment. **Independent check:** `records/independent_weight_examples_check.md`, V2; primary inputs in Riou (2010), Theorem 2.1 and Proposition 2.3, with the Leray sequence following Corollary 2.5.

Take \(X=\mathbb A^2-\{0\}\hookrightarrow Y=\mathbb A^2\), blow up the origin and then a point of the exceptional curve, obtaining a boundary \(D=E_1\cup E_2\) of two projective lines meeting once. At the origin, the displayed Leray sequence has \(E_2^{0,2}=H^0(E_1\cap E_2)(-2)=\mathbb Q_l(-2)\), although \((R^2f_*\mathbb Q_l)_0=0\) by purity for the punctured regular surface. A nonzero \(d_2\) to \(E_2^{2,1}\) therefore kills that top-weight term, so weight bookkeeping alone does not identify it with the abutment. The numerical bound survives; an identification needs the surviving \(E_\infty\)-subquotient or an additional degeneration argument.

### W26 — Actual fibre dimension cannot replace the local ambient parameter naively

**Witness:** 12/120, “Cas général” and final margin. **Kind:** own idea. **Quote:** “peut on remplacer par n−1 ... de dim ≤n−1 ?”. **Context search:** `dimension des fibres | d_y | n-1`; H, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)”, final paragraph; relation: qualifies the proposed relative sharpening. **RS:** `12-immersion-level-bound`, candidate; WG2 §3.2 #7, unchecked plan. **Confidence:** high for the test, because it is the punctured smooth curve.

The open immersion \(\mathbb G_m\hookrightarrow\mathbb A^1\) has zero-dimensional nonempty fibres, but its boundary stalk \(R^1f_*\mathbb Q_l=\mathbb Q_l(-1)\) has weight 2. A rule that simply substitutes fibre dimension 0 for the local parameter in \(2\min(i,n)\) would give 0 and is false. The marginal question therefore requires a precise restriction on which bound or dimension function is being replaced.

### W27 — Geometric level, Hodge level, coniveau and dimension type differ

**Witness:** 12/112, definition 4.1; 12/125, type definition. **Kind:** unpursued implication. **Quote:** “G′(−k)”; “fibres ... de dim ≤d”. **Context search:** `niveau | coniveau | type dimensionnel`; H, “Le niveau d'un motif (pages 2 et 3)”, “La filtration par le niveau (pages 34 et 35)”, “11) Le coniveau (pages 41, 42 et 57)”, and “Divers types de $\mathbb{Q}_{\ell}$-faisceaux (pages 124 à 136)”; relation: confirms that H itself describes several successive definitions, while emphasizing that their comparison is not automatic. **RS:** `12-immersion-level-bound`; WG2 §2.4 #3, unchecked plan.

Definition 4.1 allows Tate twists without increasing the stated geometric level, whereas the type in 12/125 bounds the dimension of a smooth projective source and does not explicitly make all Tate twists free. Hodge level is invariant under simultaneous shifts of the two Hodge indices, while coniveau measures support codimension, so these notions constrain one another only after specifying weight and geometric-generation hypotheses. Grothendieck (1969, pp. 300–301) explicitly formulates the gap between Hodge effectivity and motivic effectivity; the general converse should not be imported as a theorem into the local bound.

### W28 — The putative type bound with minus one has an SNC counterexample

**Witness:** 12/133, Proposition 4, uncertain overwritten bound. **Kind:** own idea already present in Hua; reading question. **Quote:** “(d+d′−1)-admissibles”, retained as an alternative in the frozen source. **Context search:** `type | d+d | croisements`; H, “Divers types de $\mathbb{Q}_{\ell}$-faisceaux (pages 124 à 136)”, footnote to Proposition 1; relation: confirms H's explicit counterexample, credited to H. **RS:** no settled RS entry; distinct from the level bound in `12-immersion-level-bound`. **Confidence:** high, because the local cohomology and weight obstruction are explicit.

For \(j:(\mathbb G_m)^d\hookrightarrow\mathbb A^d\) over a finite field with constant coefficients of type 0, the origin stalk of \(R^dj_*\mathbb Q_l\) is \(\mathbb Q_l(-d)\), of weight \(2d\). It cannot be generated by cohomology of smooth projective varieties of dimension at most \(d-1\), whose cohomological weights are at most \(2d-2\). Hua already uses this test to reject the minus-one version and modernizes the bound; our contribution is to retain the source's overwritten uncertainty and distinguish this failure from the valid Tate-invariant level estimate.

### W29 — Tate twisting does not preserve the dimension type as defined

**Witness:** 12/137, comparison of rows 0 and 2. **Kind:** own idea. **Quote:** “est donc également (d−1) admissible”. **Context search:** `Q_l(-1) | type | admissible`; H, “Divers types de $\mathbb{Q}_{\ell}$-faisceaux (pages 124 à 136)”, final paragraph; relation: exposes an intermediate step that H repeats. **RS:** WG2 §3.2 #7, unchecked plan. **Confidence:** high, because the case \(d=1\), \(p=0\) separates the two definitions.

With \(d=1\), \(E_2^{00}=\mathbb Q_l\) can have type 0, but \(E_2^{02}=\mathbb Q_l(-1)\) has weight 2 and cannot have type 0 over a finite field. Tensoring with the Tate object can instead raise dimension type by 1, which is compatible with the weaker eventual type-\(d\) assertion on the same line. The step becomes valid only after that adjustment or under a different, explicitly Tate-stable definition of type.

### W30 — Reducing coefficient dimension to one is explicitly unverified

**Witness:** 12/135, final paragraph and margin. **Kind:** self-flagged. **Quote:** “on est ramené au cas où d′=1”; “à vérifier”. **Context search:** `d'=1 | Artin | fibres connexes`; H, “Divers types de $\mathbb{Q}_{\ell}$-faisceaux (pages 124 à 136)”; relation: preserves the source's stated gap rather than treating H's narrative as a completed proof. **RS:** WG2 §3.2 #7, unchecked plan.

The argument needs a dimension-controlled factorization or dévissage of the coefficient family, compatibility with its projective compactification, and a justification of the connected-fibre reduction. The reference to Lemma 3 alone does not spell out how an arbitrary higher-dimensional smooth projective family is replaced while retaining the target type bound. This is one of the clearest manuscript-designated proof obligations in the packet.

### W31 — Three spectral-sequence layers, and a final reading disagreement

**Witness:** 12/137, three-row spectral sequence and last words. **Kind:** unpursued implication / reading question. **Quote:** “deux” deleted, “trois” inserted; “qui sont traités...”. **Context search:** `trois | reste à traiter | E_infty`; H, “Divers types de $\mathbb{Q}_{\ell}$-faisceaux (pages 124 à 136)”, final paragraph; relation: supports the three-layer analysis but differs from H's final reading. **RS:** WG2 §3.2 #7, unchecked plan.

With only rows 0, 1 and 2, the middle row has an incoming image, a surviving \(E_3=E_\infty\) subquotient, and an outgoing image; the correction from two to three is mathematically meaningful. H reads the last clause as “qui reste à traiter…!!”, whereas the frozen source reads “qui sont traités...”; this changes whether the closing sentence announces a remaining base case or invokes the earlier constant-coefficient case. The transcription stays frozen, and any conclusion that the proof fails exactly at those last words must remain dependent on the unresolved reading, while the independent type-bound obstruction W28 remains valid.

### W32 — A geometric-fibre slogan cannot detect arithmetic admissibility

**Witness:** 12/125, bracket and insertion after the definition. **Kind:** reading question / unpursued implication. **Quote:** “se vérifie fibre par fibre”; “par fibre géom”. **Context search:** `fibre géom | fibre par fibre | admissible`; H, “Divers types de $\mathbb{Q}_{\ell}$-faisceaux (pages 124 à 136)”; relation: specifies a potential ambiguity in H's stratum interpretation. **RS:** no settled RS entry.

If “geometric fibre” meant forgetting every arithmetic or variation structure and retaining only a finite-dimensional \(\mathbb Q_l\)-vector space, the condition would lose the weight and geometric-origin information that the surrounding argument uses. The precise claim must retain a local system, a model over an arithmetic base, or compatible geometric presentations on strata. The source's adjacent “structure discrète” and constructibility qualifications should therefore be checked before declaring the fibrewise criterion trivial.

### W33 — At an isolated missing point there are stronger published weight bounds

**Witness:** 12/116–120, constant-coefficient immersion tables. **Kind:** unpursued implication / literature comparison. **Quote:** “poids”. **Context search:** `Durfee | Saito | semipurity`; H, “Le cas d'une immersion : les feuilles de calcul (pages 115, 117 et 119)”, long footnote; relation: checks a primary reference already named by H and restricts its application to its hypotheses. **RS:** `12-immersion-level-bound`, candidate.

When the boundary is an isolated point and the punctured variety is smooth, its ordinary link cohomology is also intersection cohomology, so the semipurity theorem gives weights at most \(i\) for \(i<n\) and strictly greater than \(i\) for \(i\ge n\) (Durfee & Saito, 1990, Theorem 4.1 and duality). This refines some permitted weights in the manuscript's broader tables, but it does not directly establish the proposed Hodge or geometric level bound. The paper treats more general links with bounds depending on the dimension of the removed set, which must not be replaced by the isolated-point special case for every immersion.

## Primary references actually inspected

1. Deligne, P. (1968). Théorème de Lefschetz et critères de dégénérescence de suites spectrales. *Publications Mathématiques de l'IHÉS, 35*, 107–126. https://doi.org/10.1007/BF02698925 — primary PDF: https://www.numdam.org/item/PMIHES_1968__35__107_0.pdf ; inspected Theorem 1.5 and Proposition 2.4, including the relative-composition statement. Web refs: `turn705537425view2`, `turn924672251view5`.
2. Deligne, P. (1974). Théorie de Hodge : III. *Publications Mathématiques de l'IHÉS, 44*, 5–77. https://doi.org/10.1007/BF02685881 — primary PDF: https://www.numdam.org/item/PMIHES_1974__44__5_0.pdf ; inspected Theorem 8.2.4, Proposition 8.2.5, Remark 8.2.9, and Example 8.3.7. Web refs: `turn705537425view0`, `turn762341730view2`.
3. Deligne, P. (1980). La conjecture de Weil : II. *Publications Mathématiques de l'IHÉS, 52*, 137–252. https://doi.org/10.1007/BF02684780 — inspected primary PDF hosted by the author's institution: https://publications.ias.edu/sites/default/files/Number40.pdf ; Theorems 1.8.4, 3.3.1, 3.4.1, Corollaries 3.3.3–3.3.6, §6.1. Web refs: `turn683936377view0`, `turn762341730view1`, `turn103670610view2`, `turn103670610view3`. Numdam PDF retrieval was blocked by its 13.5 MB size, so the IAS copy was used.
4. de Jong, A. J. (1996). Smoothness, semi-stability and alterations. *Publications Mathématiques de l'IHÉS, 83*, 51–93. https://doi.org/10.1007/BF02698644 — primary PDF: https://www.numdam.org/item/PMIHES_1996__83__51_0.pdf ; inspected introduction, the alterations-versus-resolution distinction and the proper-hypercover construction. Web ref: `turn683936377view1`.
5. Grothendieck, A. (1969). Hodge's general conjecture is false for trivial reasons. *Topology, 8*, 299–303. https://doi.org/10.1016/0040-9383(69)90016-0 — primary scan hosted by the University of Extremadura: https://matematicas.unex.es/~navarro/res/articles/Hodge%27s%20Conjecture%20is%20False.pdf ; inspected corrected sub-Hodge-structure formulation, motivic effectivity paragraph and April 1969 addition. Web refs: `turn683936377view2`, `turn103670610view4`.
6. Ito, T., Kato, K., Nakayama, C., & Usui, S. (2020). On log motives. *Tunisian Journal of Mathematics, 2*(4), 733–789. https://doi.org/10.2140/tunis.2020.2.733 — version of record: https://ir.library.osaka-u.ac.jp/repo/ouka/all/73732/TunJMath_2_4_733.pdf ; inspected Remark 3.2.11 (log Tate-curve exact sequence) and §6.1.9 (monodromy from the pairing), without invoking its general conjectural log-motive formalism. Web refs: `turn215224496view0`, `turn942366151view1`, `turn942366151view2`.
7. Durfee, A. H., & Saito, M. (1990). Mixed Hodge structures on the intersection cohomology of links. *Compositio Mathematica, 76*(1–2), 49–67. https://www.numdam.org/item/CM_1990__76_1-2_49_0/ — primary PDF: https://www.numdam.org/item/CM_1990__76_1-2_49_0.pdf ; inspected introduction, Theorem 4.1 statement and the distinction between intersection and ordinary link cohomology. Web ref: `turn355060902view0`.
8. Saito, M. (1989). Introduction to mixed Hodge modules. *Astérisque, 179–180*, 145–162. https://www.numdam.org/item/AST_1989__179-180__145_0/ — primary PDF: https://www.numdam.org/article/AST_1989__179-180__145_0.pdf ; inspected Theorems 1.3–1.4 (derived functor compatibility and mixed Hodge structures at a point), the weight assertions 1.7–1.10 and the link application. Web ref: `turn355060902view1`.
9. Katz, N. M. (2012). *Convolution and equidistribution: Sato–Tate theorems for finite-field Mellin transforms* (Annals of Mathematics Studies, Vol. 180). Princeton University Press. Author-hosted manuscript: https://web.math.princeton.edu/~nmk/mellin357.pdf ; inspected Chapter 15, p. 77, for the Legendre family, its purity, geometric monodromy group and local unipotent blocks. Web refs: `turn233036191view0`, `turn650332182view0`, `turn650332182view1`.
10. Riou, J. (2010, December 7). *Théorème d'annulation, d'après S. Saito & K. Sato*. https://www.imo.universite-paris-saclay.fr/~joel.riou/doc/annulation.pdf ; inspected Theorem 2.1, Proposition 2.3, and the Leray sequence following Corollary 2.5, as inputs for the independent blowup computation rather than a source containing that example. Web ref: `turn233036191view1`.

## Primary lead not fully inspected

Durfee, A. H. (1983). Mixed Hodge structures on punctured neighborhoods. *Duke Mathematical Journal, 50*(4), 1017–1040. https://doi.org/10.1215/S0012-7094-83-05043-3. Hua supplies this reference; title/volume/pages were cross-checked in the primary bibliography of Karpishpan (1991), but the publisher page returned only an iframe and the DOI could not be fetched. Do not cite a particular numbered Durfee result as checked on this basis. Publisher attempt: `turn942366151view0`.

## Algebraic checks useful for the final synthesis

The two strongest proposed corrections are independent of any reading change: W13 refutes the questioned *twisted-coefficient* weight improvement using a Tate degeneration; W25 refutes identifying a top-weight \(E_2\) term with the abutment without checking its differential. W28 is Hua's already-given counterexample to the possible dimension-type bound, and must be credited to him. W21 and W15 test literal expressions retained diplomatically; W24 is a quantifier/edge-case correction. None of these alter the status of LM6 A.22, LM7 E.23 or FLAGGED_149 B9: the geometric bounds give no detection theorem for arbitrary deep procyclic subgroups or sections.

## Per-note search execution record

All W01–W33 queries were executed using `scripts/search_context.py`; match locators, filenames, section names, cote/scan locators where present, and UTC timestamps are stored in `records/research_searches/W01.json` through `W33.json`. `records/research_searches/weights_manifest.json` summarizes the 33 queries and the matching context files and Hua subsections. The initially complete match text was inspected before packaging retained the search metadata and locators without copying supplied context into the records; these searches read supplied textual context only and did not modify frozen files.
