# Research comparison with Michel Hua’s modernised reading of cote 46

## Scope, provenance, and limits

This comparison was made after the transcription freeze of 17 November 2026, 11:42:33 UTC. I read `context/README.md`, `context/notes/RESULTS_STATE.md`, `context/hua_project/README.md`, and the complete `context/hua_project/46.modern.tex`, and compared its relevant passages with the frozen page fragments. I did not inspect manuscript images, edit any transcription, or independently verify the leaves outside the supplied selection. All references below to the manuscript are therefore references to the root agent’s frozen diplomatic reading, whose doubt marks remain operative.

Hua’s file is explicitly an AI-produced interpretation, dated 3 October 2026 with a revision dated 21 October, not a diplomatic transcription or an independently checked witness. Its page n corresponds to scan n+1 here. Its own scope statement excludes the reused typescripts, while the present package transcribes those faces; it also treats the rest of cote 46 through its page 94, beyond the current selection. `RESULTS_STATE.md` identifies no earlier reviewed project result on this cote; its directly relevant foreign-project item is **46-homeomorphism-affine**. The other nearest ledger items, **LM1_GROUP_SCHEMES_rerun_20261112 A.9/B.8** and **LM6 F.6**, are programme comparisons, not results settled by these leaves.

## Principal findings

### H01 — The affineness theorem is corroborated, but the register’s hypothesis claim is unsupported by this reading

**File/scan:** 46:018, lemma opening. **Kind:** reading question. **Quote:** “de préschémas”; “qui est un homéomorphisme … est affine.” **Bears on:** **46-homeomorphism-affine**; `RESULTS_STATE.md`, orientation and findings sections.

The frozen reading has an inserted “de préschémas,” whereas Hua, *Un lemme d’affinité, et les groupes infinitésimaux (pages 17 et 18)*, and the findings register read a finite-presentation hypothesis that they then declare unnecessary. On the frozen reading there is no such hypothesis to remove, so the register should retain the affineness result while treating the alleged strengthening as a reading question. The theorem itself is independently corroborated by the Stacks Project, Lemma 29.46.4, Tag 04DE, which even allows a homeomorphism onto a closed subset.

### H02 — The live proof already makes the target affine

**File/scan:** 46:018, live proof. **Kind:** unpursued implication / context correction. **Quote:** “On peut supposer S affine”; “Comme f′ est un morphisme de schémas affines.” **Bears on:** **46-homeomorphism-affine**.

Hua’s footnote objects that choosing an arbitrary affine V inside f(U) does not make its inverse image affine without a separatedness condition, and replaces V by a principal open. The frozen text first reduces S to an affine scheme, however, so f′:U→S is a morphism between affines and is affine; the inverse image of the chosen affine V is consequently affine, exactly as the manuscript says. Thus Hua’s principal-open argument is a valid alternative proof, but the proposed repair is not needed for the live proof as transcribed.

### H03 — What is withdrawn is the first proof, not the affineness lemma

**File/scan:** 46:018, cancelled and live proof blocks. **Kind:** withdrawn in the same text. **Quote:** cancelled “Étant radiciel, il est séparé”; live “On peut supposer S affine.” **Bears on:** **46-homeomorphism-affine**.

The first proof is cancelled, including its radicial/separated and quasi-coherent-direct-image discussion, and a shorter local proof follows on the same scan. The lemma remains live after the cancellation of “radiciel surjectif” and “universel,” so this is a withdrawal of a proof route and surplus hypotheses, not a retraction of the affineness conclusion. Hua records the broad cancellation but the frozen transcription preserves the internal revisions and the precise replacement proof.

### H04 — The noncommutative conjugation step needs qualification

**File/scan:** 46:006, two successive displays. **Kind:** unpursued implication / mathematical check. **Quote:** “u a f(g)=b f(ug)”; “b^{-1}a=f(u)u^{-1}.” **Bears on:** **LM1_GROUP_SCHEMES_rerun_20261112 A.9/B.8**, only as a different torsor/equalizer construction; no change to their open status.

Hua, *Torseurs tordus par un endomorphisme : quand forment-ils une gerbe ?*, correctly distinguishes the actual noncommutative consequence b=uaf(u)^{-1} from the following manuscript display, which need not follow unless an additional commutation relation holds. The gerbe criterion nevertheless survives: comparison with the neutral object gives a=u^{-1}f(u), whose local surjectivity is equivalent, by inversion and changing u to u^{-1}, to local surjectivity of u↦f(u)u^{-1}. This is a check of the argument, not a correction of the frozen formula.

### H05 — The quotient is written as an open immersion, not already an isomorphism

**File/scan:** 46:007, bracketed quotient display. **Kind:** reading question. **Quote:** “imm ouvert”; “si G est connexe.” **Bears on:** **WG2 §1.1 #3**, group-scheme and torsor programme.

Hua, *Le théorème de Lang (page 6)*, says a manuscript isomorphism G/N→G needs connectedness restored. The frozen diagram is explicitly labelled “imm ouvert,” while connectedness appears separately in the surjectivity statement and the end of the proof, so this particular alleged repair is unsupported by the present reading. The published Lang theorem remains a genuine contextual match, but the diagram’s actual label should govern the historical account.

### H06 — Finiteness of the fixed group needs a finite-type convention

**File/scan:** 46:007–008. **Kind:** own idea. **Quote:** “un groupe étale fini”; “le gr. discret … (constant).” **Confidence:** high, because an explicit constant-group example separates smoothness from quasi-compactness. **Bears on:** **WG2 §1.1 #3**; indirect **LM1_GROUP_SCHEMES_rerun_20261112 A.9/B.8**.

If “lisse” is interpreted only as smooth, hence locally of finite presentation, the assertion that N is finite requires a finite-type/quasi-compact convention: the constant group scheme ℤ over F_q is smooth and has Frobenius equal to the identity, so its fixed group is infinite. Hua’s wording silently works with an algebraic group of finite type, which is a sufficient convention but is not supplied by the isolated word “lisse.” Separately, a nontrivial finite constant group shows why connectedness must be carried into the corollary’s surjectivity argument: its Lang map is constant.

### H07 — Two early wording differences remain reading questions

**File/scan:** 46:005 and 008. **Kind:** reading question. **Quote:** “Σ en groupoïdes, avec une section marquée (G,f)”; “non dégénérée.” **Bears on:** **WG2 §1.1 #3**.

Hua’s first torsor subsection tentatively describes an action on a groupoid, whereas the frozen insertion describes a marked section; its subsection on Frobenius-rigidified vector bundles calls the defining adjective illegible and substitutes “inversible,” whereas the frozen reading is “non dégénérée.” These are differences of wording and categorical emphasis to revisit against the ink, not grounds for altering the frozen text. In particular the existence of the marked neutral object is exactly what supports the passage from the gerbe to N-torsors.

### H08 — Frobenius powers and ordinary ideal powers must be distinguished

**File/scan:** 46:011 and 019. **Kind:** own idea. **Quote:** “J^p”; “identique au voisinage infinitésimal d’ordre p^ν.” **Confidence:** high for the algebraic distinction; the intended historical convention for “ordre” remains unresolved. **Bears on:** **WG2 §1.1 #3**; Hua, *Frobenius relatif, morphismes non ramifiés et étales* and *Un lemme d’affinité, et les groupes infinitésimaux*.

Hua correctly replaces ordinary-power notation in its exposition by the ideal I^[p^ν] generated by p^ν-th powers, but that is an interpretation rather than the literal notation on the leaves. For G=G_a² in characteristic 2, the Frobenius kernel is Spec k[x,y]/(x²,y²), of length 4, whereas the thickenings defined by (x,y)² and (x,y)³ have lengths 3 and 6, so neither ordinary first- nor second-order thickening agrees with it. The manuscript’s augmentation-ideal characterization is therefore more precise than an unqualified identification with an ordinary infinitesimal neighbourhood.

### H09 — The marked-section observation adds something Hua did not decipher

**File/scan:** 46:019, margin. **Kind:** unpursued implication. **Quote:** “Ne fait intervenir que la section marquée de G, et pas la structure de groupe.” **Bears on:** **WG2 §1.1 #3**.

Hua records a largely unread marginal remark about a neighbourhood and section; the frozen reading explicitly removes the group law from this construction. It points to the same Frobenius thickening for an arbitrary pointed S-scheme: take the inverse image of the Frobenius-twisted marked section, whose affine ideal is generated by p^ν-th powers of the augmentation ideal. The comparison narrows what is genuinely group-theoretic in Proposition 2 without asserting that all subsequent group-scheme statements generalize.

### H10 — The missing p-th-power quotient is a genuine mathematical issue

**File/scan:** 46:021, final display. **Kind:** own idea. **Quote:** “R_X^*/O_X^* … est injectif.” **Confidence:** high, because p-th powers have zero logarithmic differential. **Bears on:** **WG2 §1.1 #3**; Hua, *La p-torsion du groupe de Picard*.

The literal quotient in the frozen display cannot inject under dlog in characteristic p: for example x^p in the fraction field of k[x]_(x) is not a unit but has zero logarithmic differential. Hua’s additional quotient by rational p-th powers repairs that formal defect in its modern exposition, and it is appropriate to credit that distinction rather than replace the manuscript formula. This does not by itself settle the subsequent normal-local-ring question.

### H11 — Normality does not justify the announced reduction by itself

**File/scan:** 46:021, last paragraph. **Kind:** unproved claim. **Quote:** “on est ramené au cas où X est … régulier.” **Bears on:** **WG2 §1.1 #3**; Hua, *La p-torsion du groupe de Picard*; Oda comparison delegated separately.

Hua isolates the missing passage: codimension-one valuations can show that a relevant Weil divisor is divisible by p, but normality alone does not make its quotient by p locally principal. This identifies a proof obligation and does not yet refute the claim for ordinary regular Kähler differentials, because reflexively regular rational forms and sections of Ω¹ need not agree on a singular normal scheme. A class-group example alone must therefore not be presented as a counterexample to the exact manuscript question.

### H12 — Hua changes the two site-theoretic conditions

**File/scan:** 46:034 and 036. **Kind:** reading question / context correction. **Quote:** “a) … une équivalence des topos étales”; “b) … le carré est cartésien”; “Donc b) ⇒ a)”; “Peut-être que a) implique aussi b).” **Bears on:** **WG2 §1.1 #3**; no tower/GT register claim is settled.

Hua, *Une version axiomatique (pages 33 et 35)*, folds the cartesian-square requirement into a) and reconstructs b) as an isomorphism with the identity functor, then discusses a reverse implication under those altered labels. The frozen text separates topos equivalence from the representable relative-Frobenius isomorphism and explicitly proves b)⇒a), leaving a)⇒b) tentative. Consequently Hua’s version cannot serve as a witness resolving the manuscript’s question; any new proof must first specify the “standart” topology, its subcanonicity, and the universal base-change requirement.

### H13 — Published Brauer–Severi arguments closely match the first proposition sheet

**File/scan:** 46:041. **Kind:** unpursued implication / literature parallel. **Quote:** “de degré 1 sur chaque fibre”; “et dualité des projectifs.” **Bears on:** **WG2 §1.1 #3**; **LM6 F.6** only to delimit a different meaning of “section.”

Hua, *Définition et premiers énoncés (page 40)*, correctly identifies the degree-one criterion and section-implies-projective-bundle argument, and Grothendieck’s published *Le groupe de Brauer II*, §0, pp.288–289, supplies the dual-incidence-divisor proof matching the inserted phrase. *Le groupe de Brauer I*, §8.1 and §8.4, matches the descent/obstruction setting. This is a close published parallel, not evidence that the undated leaf precedes the publications or that a section-conjecture open item has been solved.

### H14 — The generic splitting criterion requires its hypotheses to be recorded

**File/scan:** 46:043. **Kind:** unproved claim / literature parallel. **Quote:** “Si S régulier”; “strictement loc factoriel.” **Bears on:** **WG2 §1.1 #3**.

Hua, *Critères de trivialité (page 42)*, invokes generic injectivity of the Brauer group to explain the manuscript’s criterion. Grothendieck’s *Le groupe de Brauer II*, Corollary 1.10 and preceding hypotheses 1.3–1.4, printed p.293, provide a precise noetherian/strict-local-factorial form of that input. The manuscript’s compressed formulation should not be turned into a hypothesis-free statement about all schemes or all normal schemes.

### H15 — The section of λ is announced, and Hua’s empty-system explanation remains a proposal

**File/scan:** 46:045 and 047. **Kind:** reading question / unproved claim. **Quote:** “ayant d’ailleurs une section canonique”; “Donc … représentable ssi … Pic.” **Bears on:** **WG2 §1.1 #3**; indirect **LM1_GROUP_SCHEMES_rerun_20261112 A.9/B.8**, without a general representability conclusion.

Hua, *Systèmes linéaires paramétrés par un schéma de Brauer–Severi*, proposes the empty linear system as the canonical section, but the leaf does not describe the section and its definition of parametrizing Brauer–Severi schemes does not explicitly include an empty projective space. That explanation should therefore remain attributed to Hua and conditional on the intended convention. If a section exists and SystLin is represented, its idempotent retraction makes Pic representable because schemes admit equalizers; the substantive unresolved part is the actual functor and effective descent, which scan045 expressly flags.

### H16 — The frozen insertion is mono, while Hua prints épi

**File/scan:** 46:047, proof. **Kind:** reading question. **Quote:** “un mono[morphisme] P̌→P(Q).” **Bears on:** **WG2 §1.1 #3**.

Hua’s subsection on linear systems calls this map an “épimorphisme,” whereas the frozen transcription has an inserted “mono.” The distinction changes the proof problem and must not be silently neutralized by the desired conclusion. This is a concrete comparison for any later palaeographic check, not authorization to change the current transcription.

### H17 — The linearity input, not just monomorphy, is needed in that proof

**File/scan:** 46:047. **Kind:** own idea. **Quote:** “je dis que c’est un isom sur un P(E).” **Confidence:** high for the logical distinction, because the Veronese embedding is an explicit counterexample to the bare implication. **Bears on:** **WG2 §1.1 #3**; **LM1_GROUP_SCHEMES_rerun_20261112 B.8** only as a concrete representability/descent comparison.

A monomorphism of a projective space into P(Q) does not alone identify its image with P(E) for a vector quotient E of Q: the conic Veronese embedding P¹→P² is already a counterexample to that standalone inference. The construction-specific missing input is that the pulled-back tautological invertible sheaf has degree one on geometric fibres, giving a fibrewise linear embedding and the desired quotient bundle after descent. This isolates what “par descente” must establish without refuting the intended statement.

### H18 — Keep the obstruction in cohomology before identifying it with a Brauer class

**File/scan:** 46:043 and 047. **Kind:** own idea. **Quote:** “une certaine obstruction dans H²(S,O_S^*)”; “ξ … ne provenant pas d’un L.” **Confidence:** high as a formulation check; sign depends on the projective-duality convention. **Bears on:** **WG2 §1.1 #3**.

Hua interprets the last assertion through the relative Picard obstruction, a useful bridge, but a general Leray boundary first lands in H²(S,G_m), not automatically in the Azumaya Brauer group. For the specific ξ supplied by a finite-rank Brauer–Severi system, comparison of descent cocycles identifies that obstruction, up to the duality sign, with the associated Brauer class and explains why splitting P̌ and representing ξ by a line bundle coincide. The current pages suggest this comparison but do not write out its cocycle verification.

### H19 — Divisor schemes give a concrete continuation to seek, not a completed result here

**File/scan:** 46:041, boxed margin. **Kind:** unproved claim / context continuation. **Quote:** “les Div^n_{P/S} représentables et sont des schémas de Br. Séveri.” **Bears on:** **WG2 §1.1 #3**.

The frozen margin explicitly announces the degree-n divisor schemes, while Hua’s first-mouture discussion concentrates on n=1 and locates a fuller construction in *Le schéma des n-formes (pages 57 à 59)*, corresponding to scans058–060 outside this packet. Its construction by twisting the projective space of degree-n forms is a concrete continuation lead and must remain credited to Hua until those leaves are audited. The present note neither imports those later formulas into scan041 nor treats their claimed divided-power correction as an observation on a supplied page.

## Coverage of Hua’s additional topics beyond this package

The following are **context leads only**. No manuscript quotation or proof from these out-of-range leaves has been independently verified here, and their numbers must not be included in the current title/count register.

| Hua subsection | Hua pages / corresponding scans | Relation to supplied pages and RESULTS_STATE |
|---|---|---|
| *Progroupes et groupes algébriques quasi-compacts* | 51–53 / 052–054 | A potentially relevant continuation for **LM1_GROUP_SCHEMES_rerun_20261112 A.9/B.8**: Hua discusses comparison of progroup objects, full faithfulness and an approximation theorem; the present finite Lang equalizer does not establish those general assertions. |
| *Le plan d’une théorie globale*; *Le schéma des n-formes*; *Un critère de transversalité* | 56–61 / 057–062 | A second Brauer–Severi treatment, directly connected to scan041’s Div^n margin and scan045’s effective-descent warning; claimed continuation, not a second witness of cote47 or cote44. |
| *Le groupe de Brauer global* | 62–66 / 063–067 | Hua records analytic/topological Brauer groups and fixed-rank versus arbitrary-rank realization questions; none of those questions is explicitly posed in scans002–048, and no finite-homotopy-model ledger result follows from their mere presence in his interpretation. |
| *Restriction des scalaires* | 68–70 / 069–071 | A different group-scheme/Brauer direction (purely inseparable Weil restriction, wound unipotent and norm-kernel phenomena), not a supplied completion of scan022’s height-one problem. |
| *Le théorème 90 tordu*; *Le théorème de Lang en cohomologie galoisienne*; *Cohomologie d’un groupe muni d’un automorphisme* | 72–79 / 073–080 | Hua’s claimed return to Lang and nonabelian H¹ can be compared in a later packet with scans005–009, but supplies no checked proof on the current leaves. |
| *Torsion par un cocycle, éléments automorphes*; *Une version semi-locale*; *Le cas d’une action triviale sur le corps résiduel* | 80–92 / 081–093 | Hua supplies completions, extra hypotheses and a claimed Lean check; neither the corresponding scans nor the formal proof file are supplied here, so those remain his project’s claims. |
| *Contre-exemples à passage au quotient* | 94 / 095 | Hua’s proposed replacement of PGL by a subgroup and its English cancelled closing text concern an unprovided leaf and are outside the present evidential scope. |

## Further provenance differences worth retaining

**H20 — Reused sheets. File/scans:** 46:023, 042, 044, 046, 048. **Kind:** unpursued implication. **Bears on:** **WG2 §1.1 #3** and the comparison policy represented by **MPL_136_189-234 R008 / MPL_136_235-281 N16**, both first-pass context leads.

Hua explicitly omits the reused typescripts, whereas this package preserves the uniform-structure page, the three Coxeter-graph pages and the injective-module fragment as distinct physical faces. Their text and identifiers should be kept separate from Grothendieck’s live group-scheme argument, and neither their author nor their dates can be inferred from their reuse alone. The analogous reused-sheet cautions in the supplied register support this provenance distinction but are not independent verification of these particular faces.

**H21 — Anonymous Verschiebung typescript. File/scan:** 46:027. **Kind:** reading question / context continuation. **Quote:** “V=ar”; “VF=p.” **Bears on:** **WG2 §1.1 #3**.

Hua’s *Le tapuscrit « Définition du morphisme Verschiebung »* treats four pages, of which only its final page (Hua26, scan027) is supplied in this packet; scans024–026 were deliberately excluded as already handled elsewhere. His identification of an unnamed correspondent, second-person address and a lost earlier text comes from those excluded opening leaves and should be attributed to his contextual account, not asserted from scan027 itself. The supplied final page does substantiate a concrete Verschiebung construction continuing the marginal request on scan022.

**H22 — Ambiguous headings and scope counts. File/scans:** 46:003, 029, 038. **Kind:** reading question. **Bears on:** **WG2 §2.4 #4** and **WG2 §1.1 #3**.

Hua’s proposed “Jacobiennes et variétés [abéliennes ?]” at its page2 and “XV” at its page28 differ from the low-confidence frozen readings on scans003 and029, and his description of the cancelled cover at page37 likewise does not resolve its doubtful wording. These differences should remain in the reading-question register and cannot support an identification of earlier Jacobian theorems or an internal page count. Hua’s “pages1–94” is the scope of his modernised file, not a count written on one of the supplied covers.

## Primary references checked

The quotations above are from the supplied frozen manuscript fragments, not from the following published works. The publications were used for the specific corroborations indicated, with no claim of novelty or manuscript chronology.

- Grothendieck, A. (1966a). Le groupe de Brauer : I. Algèbres d’Azumaya et interprétations diverses. *Séminaire Bourbaki*, 9, Exposé 290, 199–219. https://www.numdam.org/item/SB_1964-1966__9__199_0/ — §§8.1–8.4, printed pp.216–217, for Brauer–Severi descent and the obstruction. Lecture heading: May 1965; publication year: 1966.
- Grothendieck, A. (1966b). Le groupe de Brauer : II. Théories cohomologiques. *Séminaire Bourbaki*, 9, Exposé 297, 287–307. https://www.numdam.org/item/SB_1964-1966__9__287_0/ — §0, printed pp.288–289, for the section/degree-one criterion; Corollary1.10, printed p.293, with §§1.3–1.4 hypotheses, for generic injectivity. Lecture heading: November 1965; publication year: 1966.
- Lang, S. (1956). Algebraic groups over finite fields. *American Journal of Mathematics, 78*(3), 555–563. https://doi.org/10.2307/2372673 — original paper located at https://wstein.org/papers/bib/Lang-Algebraic_Groups_Over_Finite_Fields.pdf; its opening states the Lang covering/surjectivity result. No claim about the archive’s Serre page number is derived from this source.
- The Stacks Project Authors. (2026). *The Stacks Project*, Lemma29.46.4 (Tag04DE), “Universal homeomorphisms.” https://stacks.math.columbia.edu/tag/04DE — statement and complete local proof read; the stronger closed-image version implies the manuscript lemma.
- Hua, M., project. (2026). *Schémas en groupes et fibrés principau[x] (Divers): Lecture modernisée du dossier entier* [AI-produced project interpretation, cote46; first pass3 October, revision21 October; supplied copy downloaded14 November]. `context/hua_project/46.modern.tex`. Credit is to Michel Hua’s project, not to an independently authenticated authorial manuscript witness.

### Tool source locators for root verification

- Stacks Tag04DE: `turn14view0` (also `turn1view0`), direct official URL above; theorem and proof at web lines23–25.
- Brauer I PDF: `turn22view1`, relevant extraction `turn24view1`; direct PDF https://www.numdam.org/item/SB_1964-1966__9__199_0.pdf .
- Brauer II PDF: `turn22view0`, relevant generic-injectivity extraction `turn24view2`; metadata `turn24view0`; direct PDF https://www.numdam.org/item/SB_1964-1966__9__287_0.pdf .
- Lang original PDF: `turn14search7`; bibliographic DOI above. Source search snippet is not used to fix its malformed OCR action formula.

The root agent should open cited web pages itself before using these source refs in the final chat. The main archive notes should use ordinary author–date references and these exact source locators, with sparse quotation and clear attribution to Hua where his interpretation prompted a comparison.
