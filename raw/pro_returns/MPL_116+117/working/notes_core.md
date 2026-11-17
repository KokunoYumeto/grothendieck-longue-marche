# Research notes — MPL_116+117

## Scope, status and reference conventions

The diplomatic transcription was frozen at **2026-11-17 18:22:23 UTC**, after all 34 page audits and before the context archive's contents were opened. These notes interpret the frozen readings; they do not amend them. A separate final hash check is recorded in progress.log.

A reference such as **116/004:25–35** means cote 116, supplied scan 004, lines 25–35 of its page TeX file; the accompanying equation, paragraph or margin description locates the ink. These are file-line references, not a claim that the manuscript has that many physical lines. **RS** means context/notes/RESULTS_STATE.md; **DSS** means context/DOSSIER_STATEMENTS_WITH_STATUS.md; **NR** means context/NEW_RESULTS.md. Context paths refer to the supplied context archive, whose source files are not duplicated in this return.

The statuses copied in the coverage tables are the supplied sources' statuses. “Proved”, “Known”, “Refuted” and “Open” in those tables are **the earlier run's claims**, except where an explicitly reported review is identified; this return does not independently certify those research returns or change their statuses. Even a reported review is attributed to the register, rather than treated as a review performed here. The two externally checked references are listed at the end.

“Absent” below means absent as a statement, proof or specified example from the **entire supplied 116/002–008,010–011 and 117/002–026**, not absent from Grothendieck's work. It never means that a keyword search alone proves absence. All mathematical passages were read visually before the freeze and reread as frozen text for the comparisons.

## Direct answers to the planning questions

### Q01 — Strong W(7): no occurrence established in this package
**Kind:** unpursued implication / bounded source comparison. **Sources:** 117/023:3–22; NR 8; RS POLES B.2, TOTASPH A.9 and MPL_106+107 first-appearance lead.

The manuscript's **“Hot 7”** asks for surjectivity on Hom sets after restriction to two full sieves or two full cosieves, and tentatively for bijectivity on objects; it does not assert that any two of equivalence on an intersection, on both pieces, and on their union imply the third. The strong W(7) is explicitly present in the supplied companion's source block at **DER_XIIb-a.tex:767–805, manuscript pp. 76–77**, with its any-two-imply-the-third conclusion on p. 77 and the biconditional W(7 bis) at **711–744, pp. 75–76**. Those are contextual witnesses, not evidence of its first historical occurrence: neither the present scans nor the excerpts of other packages' notes supplied in RS permit a first-appearance date elsewhere in the archive.

### Q02 — “Totally aspherical implies filtered”: not stated here
**Kind:** bounded source comparison. **Sources:** 116/003:46; 117/022:27–28; NR 11; RS TOTASPH C.10, D.7, PRETOT A.12, RESIDUE F.5.

The loose assertion **“i est tot 0-asph.”** concerns a functor and a zero-level condition, while **“Cas des catégories filtrantes ??”** asks about cofinality; neither states the proposed converse for a totally \(W_\infty\)-aspherical category. The supplied companion explicitly places that question at **DER_II-a.tex:1319–1320, manuscript p. 36**, followed by the retracted attempted negative answer and its correction on **pp. 36bis–36ter**; calling p. 36ter its first occurrence would lose the earlier question. NR 11 reports the checked \(\Delta_{\mathrm{inj}}\) counterexample, whereas the different exactness converse is still labelled Open in the selected TOTASPH D.7 / RESIDUE F.5 rows, so the present pages should not be credited with settling either.

### Q03 — Relative Theorem A in 1983: these scans do not establish it
**Kind:** unproved claim / bounded source comparison. **Sources:** 117/020:21–24, 117/021:53–67, 117/022:3–45; DSS BISITE A.1, A.32 and RESIDUE B.1–B.9; RS GALOIS B.3, REVLOC F.1, MPL_105 R08 and MPL_134-8_043-087 H4.

The claim **“J'ai prouvé l'existence des \(f_!\)”**, the proposed cartesian base-change formulas, and the adjoint-pair cofinality argument are substantial evidence of the intended formalism, but none states the relative implication \(u/s\in W\) for every \(s\in S\Rightarrow u\in W\). The later source block **DER_XVI.tex:129–138, manuscript p. 3**, explicitly distinguishes that implication from the absolute Theorem A; the word “localisateur fondamental” in 117/020 supplies no axiom list that would resolve the distinction. **Cote 118 is not supplied**, and the context contains no transcription of it, so the joint historical question “117,118” remains unresolved by this package rather than receiving a negative answer about what he knew in 1983.

### Q04 — What is positively present in 1983
**Kind:** unpursued implication. **Sources:** 117/002:3–41, 117/006–023; RS GALOIS B.13, G.6; DSS BISITE F.1–F.9.

The dated title **“Structure des dérivateurs”** and the later exposition give strict indexed categories, restriction, proposed left and right adjoints, integration and cointegration, base change, full-faithfulness assertions, several models, and a gluing requirement. This is strong manuscript evidence for an early derivator programme, with explicit unresolved points; it is not a verified instance of every modern Der 1–4 axiom, since joint conservativity of evaluations is not stated and the exactness conditions differ. The distinction matters when comparing these leaves with register assertions whose hypotheses already assume a modern derivator.

### Q05 — The mapping-cone folder is about topoi and presheaf gluing
**Kind:** unpursued implication. **Sources:** 116/004–008; RS Hua 116-presheaf-gluing-continuous-gluing-functor; DSS STRATA D.1–D.2, BISITE F.9.

The central construction is a topos glued from an open part and its closed complement, with sheaves written as triples and with a displayed relative-cohomology sequence; it is not introduced as a cone in a triangulated category. The passage to \(X_0^{op}\times X_1\to\mathrm{Ens}\) is a concrete precursor to the crossing-arrow gluing viewpoint mentioned in the README, but the supplied DSS contains no STRATA C.1 statement to compare in full. No assertion about cote 115 is inferred from this neighbouring folder.

## Mathematical notes from cote 116

### N01 — The gluing datum and the total topos
**Kind:** unproved claim. **Source:** 116/004:9–19, equations (1)–(2) and NB.

The words **“topos total associé”** introduce \(C(f)\), and the triples \((F_0,F_1,u)\) express its sheaves, with the alternative \(F_1\to f_*F_0\) written explicitly. This supports the gluing interpretation in **Hua, modernised reading of cote 116, “Le cylindre d'un morphisme de topos”**, and bears on DSS STRATA D.1–D.2 / BISITE F.9, but the manuscript gives no exceptional-adjoint chain or stable recollement theorem. The local doubt at \(f_0^*\) in the first expression is retained rather than removed using the alternative formula.

### N02 — All-coefficient cohomology is the stated test
**Kind:** unproved claim. **Source:** 116/004:21–28, equation (3).

After replacing “asphérique”, he writes **“pour tout faisceau \(F\)”** and an isomorphism \(H^*(\mathcal X,F)\to H^*(\mathcal X_1,i_1^*F)\). The quantifier is stronger than a statement only about constant coefficients, but the page does not supply the proof or define precisely the equivalence notion carried by the corrected abbreviation. Compare RS GALOIS D.2 and DSS BISITE A.19 for the importance of retaining the coefficient class; their local-system and universal-base-change hypotheses are not silently present here.

### N03 — Retraction and the meaning of “mapping-cone”
**Kind:** unpursued implication. **Source:** 116/004:30–37, Re NB.

The marginal **“rétraction \(r\)”** and amalgam formula explain why **Hua, modernised reading of cote 116, “Le cylindre…”**, interprets the construction as cylinder-like while reserving cone-like information for relative cohomology. This is a useful connection with the factorization themes of DSS PATHS E.5 and BISITE E.9, but neither a categorical mapping-path construction nor a smooth/proper factorization is given on this page. The terminology and the imperfect tuple remain exactly as frozen.

### N04 — The proposed converse is a separate problem
**Kind:** conjecture / self-flagged. **Source:** 116/005:3–4.

The characterization through a gluing functor preserving arbitrary inverse limits and having a **left-exact left adjoint** is followed by **“fort asphérique (réciproque ?)”**. The question asks for a converse to the asserted property of the closed inclusion, not merely for the converse direction of the presheaf reconstruction on scan 008. It remains open on these leaves, as also noted by **Hua, “Le fil du dossier, et les conventions”**; DSS STRATA D.1–D.2 does not settle this topos-specific converse.

### N05 — Relative cohomology of a morphism
**Kind:** unpursued implication. **Source:** 116/005:5–16, (5), (5′) and definition.

The two sequences replace the cohomology of the total gluing topos by that of its closed part and define **“\(\mathcal X_1\operatorname{mod}\mathcal X_0\)”**, with **“\(f\) sous-entendu”** inserted. This is concrete evidence for a relative-cohomology interpretation of the construction, adjacent to the support/fibre sequences in DSS STRATA D.2 and BISITE F.9. Passing from this abelian-cohomology sequence to a coherent stable-derivator recollement would require additional data and is not performed here.

### N06 — Reduction of equivalence to the open inclusion
**Kind:** unproved claim. **Source:** 116/006:3–8.

He again replaces **“asphérique”** by **“équiv. faible”** and asserts that the property of \(f\) is equivalent to that of the open inclusion into \(\mathcal X\). The retraction of N03 suggests a two-out-of-three argument, as explained in **Hua, “Le point de vue inverse”**, but that interpretation depends on a specified equivalence class and on the closed leg belonging to it. It is not the assertion in DSS PATHS E.5 that every category functor has a weak-equivalence/smooth-proper factorization.

### N07 — Locally constant coefficients and the reversed tuple
**Kind:** unproved claim / reading question. **Source:** 116/006:8, NB.

The NB identifies locally constant sheaves by a tautological gluing map, but writes \((F_1,f^*F_1,u)\) and leaves the final \(\mathcal X_0/\mathcal X_1\) index doubtful. **Hua, “Le point de vue inverse”** reverses the tuple into the convention of scan 004; that is an interpretation, not a reading adopted here. The intended local-coefficient comparison bears on RS GALOIS D.2 and DSS BISITE A.19, but the source does not make their base-change assertions.

### N08 — An open subtopos as a map to \(\operatorname{Top}(\Delta_1)\)
**Kind:** unproved claim. **Source:** 116/006:10–18.

The text explicitly associates an open subtopos with a map to \(\operatorname{Top}(\Delta_1)\), whose universal open and closed pieces are labelled \(0\) and \(1\). This supports the two-stratum organization described by **Hua, “Le point de vue inverse”** and is adjacent to RS STRATA 0.1 / DSS STRATA D.9. The variance of those two labels should be checked from the displayed convention, not inferred from a later entrance/exit terminology.

### N09 — General gluing without the extra exactness
**Kind:** conjecture / unproved claim. **Source:** 116/007:3–14.

He seeks conditions ensuring that **“les deux inclusions”** are weak equivalences and explicitly says of left exactness of \(f^*\) that **“on n'a pas envie de le supposer ici”**. The inserted **“accessible”** qualifies the gluing functor; it does not assert accessibility of a fundamental localizer, so it does not settle RS GALOIS B.13 or POLES F.14. The same paragraph's “adjoint à droite” differs from scans 005 and 008 and is recorded separately in R01.

### N10 — Presheaf gluing and crossing arrows
**Kind:** unproved claim / contextual identification. **Sources:** 116/007:14–116/008:13; RS Hua 116-presheaf-gluing-continuous-gluing-functor.

The explicit criterion and bifunctor support **Hua's findings-register entry 116-presheaf-gluing-continuous-gluing-functor** and his subsection “Le point de vue inverse”; the page states the equivalence but stops at the bifunctor rather than constructing the collage. The primary-source check confirms Hua's reference to **SGA 4 IV, Exercise 9.5.10(b–c)**, so this is a historical manuscript occurrence of a published construction, not a novelty claim. Its relevance to later coherent gluing is structural; it does not by itself provide the enhanced gluing excluded from ordinary homotopy categories in DSS BISITE E.13.

### N11 — A concrete continuation of the bifunctor
**Kind:** own idea, confidence high for the construction, moderate for the intended application. **Source:** 116/008:5–13; context: Hua “Le point de vue inverse”, RS STRATA B.2.

Following the collage interpretation credited to Hua, take objects from \(X_0\sqcup X_1\), retain each piece's Hom sets, set \(\operatorname{Hom}(x_0,x_1)=h(x_1,x_0)\), and put no arrows from \(X_1\) back to \(X_0\); functoriality of \(h\) supplies composition. This directly checks the category-level meaning of the displayed variance and would be a suitable starting point for testing which extra conditions make both inclusions equivalences. It supplies no automatic answer to N09 and no theorem about exit infinity-categories.

### N12 — Strict fibre versus comma category
**Kind:** unproved claim. **Source:** 116/010:3–17.

The leaf says **“\(A\) fibrant”** and asserts the inverse-limit comparison between \(A_{/b}\) and \(A_b\) for all indicated \(F\), without defining “fibrant” or spelling out an adjunction. This is a genuine local precursor to the pointwise/base-change problem in DSS STRATA D.4 and BISITE F.1–F.2, but not relative Theorem A. **Hua, “Un feuillet séparé”**, reads “filtrante” and supplies a precofibred hypothesis, so the difference must remain a reading question rather than an imported hypothesis.

### N13 — The loose localization note does not define totality
**Kind:** unproved claim. **Source:** 116/003:23–46.

The adjunction-like diagrams, full-faithfulness/localization list and **“i est tot 0-asph.”** are unconnected shorthand with several uncertain indices. They may relate to the later Hot 5–6 assertions, but neither the universal final-image definition in RS TOTASPH A.2 / POLES H.2 nor the converse in NR 11 is written here. No implication from total \(W_\infty\)-asphericity to filteredness can be extracted from this isolated phrase.

## Mathematical notes from cote 117

### N14 — Three levels of Hom and their adjunctions
**Kind:** unproved claim. **Source:** 117/002:7–41, equations (1)–(3″).

The dated sheet distinguishes an ordinary Hom set, a homotopy-type-valued Hom, and an internal object over \(I\), and writes adjunction formulas at all three levels. This bears directly on the motivation for RS GALOIS E.11 / G.6 and DSS BISITE F.7, but supplies neither a definition of the internal object nor a functorial higher-coefficient construction on a bare derivator. **Hua, “La structure des dérivateurs”**, also cautions that the internal formula needs more than the ordinary adjunction; a projection-formula hypothesis cannot be inferred from the boxed display alone.

### N15 — The integral in the global Hom formula
**Kind:** reading question / unproved claim. **Source:** 117/002:16–19,32–33.

The source uses \(\int_I\) and says **“en intégrant \(\int_J\)”**, while **Hua, “La structure des dérivateurs”**, replaces this by a homotopy limit. The later definitions on 117/010–012 distinguish integration from cointegration, creating a real internal comparison problem, but the unknown meaning of the internal Hom prevents using that later convention to correct the earlier dated sheet. Compare DSS BISITE F.7–F.8 and the limits of coefficient enrichment in RS GALOIS G.6.

### N16 — Higher arrows without a path-category construction
**Kind:** unpursued implication. **Source:** 117/003, especially the \(\pi_0,\pi_1\), parallel-arrow and zigzag clusters.

The sheet contains higher-arrow sketches and the loose symbols associated in the frozen reading with \(\mathrm{Cl}(M,W)\), but no definition of a path type, marked vertical arrows, hammock comparison, endpoint category or composition theorem. It is a thematic antecedent for DSS PATHS A.P1 and B–C, not a source occurrence of their precise results. The cancelled right-hand side of the \(\pi_1\) expression and the cropped lower edge are particularly unsuitable as evidence for a completed theorem.

### N17 — The mapping-object programme is explicitly tentative
**Kind:** conjecture. **Source:** 117/004:23–31.

**“On a sans doute”** introduces a mapping object in Hot and a possible explicit simplicial complex, with a possible richer theory for the external Hom. This anticipates the problem addressed by DSS PATHS C.1–C.2, C.5 and D.20, but gives none of their coherent constructions or hypotheses. RS GALOIS G.6 remains a separate construction problem, not answered by this expectation.

### N18 — Truncations, invariants and K-theory are separate desiderata
**Kind:** conjecture. **Sources:** 117/004:39–45; 117/005:3–6,33–36.

The programme distinguishes truncations on models from operations on \(\mathcal H\), calls the relevant operations **“peu comprises”** in a doubtful reading, and asks **“Cas additif seulement ?!?”** beside \(K(\mathcal H)\) and higher \(K_n\). Neither the existence of additive values nor the words “triangles exacts” construct a K-theory invariant of an arbitrary diagram theory. Compare the additional structures required in DSS PATHS C.8–C.10 and the bare/enhanced distinction in RS GALOIS E.11.

### N19 — Internal Hom versus homotopy Hom is an autograph question
**Kind:** conjecture / self-flagged. **Source:** 117/005:9–30, especially the margin dated 24.11.83.

The margin explicitly asks for the **“Relations entre ces Hom internes”** and the Homhot objects, with “??”, while the tensor-Hom adjunction is written in the main text. This bears on DSS BISITE F.4–F.7 and RS GALOIS G.6; it is evidence that the enrichment issue was recognized, not that arbitrary tensor/projection/exchange identities were established. The date attaches to this margin and must not be extended automatically to every leaf of the cote.

### N20 — Strict indexed categories, with size and variance still being specified
**Kind:** unproved claim / self-flagged. **Source:** 117/006:6–48; 117/008:4–10.

The expressions **“2-contravariante”**, **“stricte”**, and **“à préciser”** accompany the evaluation functor \(\alpha_A\) and its naturality square. The examples use \(\operatorname{Hom}(A,M)\), so comparison with the presheaf convention in DSS BISITE F.1 requires opposition of the indexing convention. No joint-conservativity axiom for the evaluations is stated, agreeing with **Hua, “La variance”** and delimiting the relevance to RS GALOIS B.13.

### N21 — Hot 1 and the infinite-product warning
**Kind:** unproved claim / self-flagged. **Sources:** 117/008:9–10; 117/014:24–37.

Hot 1 is an axiom for the proposed theory, but the localization example carries **“Attention”** and a doubtful **“il n'est pas clair”**, with **“sauf pour \(I\) fini”**. The source thus recognizes the infinite-product issue rather than asserting its automatic resolution, unlike the sentence introducing the warning in **Hua, “Quatre exemples”**. Compare DSS PATHS D.16 and RESIDUE B.12/B.15: finite localization statements cannot simply be enlarged to arbitrary products.

### N22 — The first presheaf integration scheme is cancelled
**Kind:** withdrawn in the same text. **Sources:** 117/008:15–45; 117/010:6–18; 117/022:36–45.

The lower draft through \(L_A:\mathcal H(A)\to\mathcal H(\widehat A)\) is crossed out, and the subsequent Hot 2 instead specifies a left adjoint to restriction. The presheaf square later returns in the cofinality footnote, but that does not revive every cancelled axiom or settle the universe problem of evaluating on \(\widehat A\). **Hua, “Une première intégration, abandonnée”**, makes this useful comparison; it bears on the size cautions in RS GALOIS B.13 and DSS PATHS D.1.

### N23 — Adjoints, Fubini and the cofibrancy reservation
**Kind:** unproved claim / self-flagged. **Source:** 117/010:6–44; 117/012:4–14.

The author proposes both Kan adjoints and their iterated integral/product formulas, but asks whether one should **“se borner ici aux \(f\) cofibrants”**. These are direct early forms of part of DSS BISITE F.1; the direction written for \(f_!\) on scan 010 is inconsistent with its stated adjunction and is preserved. Existence of both adjoints in the proposal must not be confused with his explicit lack of a proof of \(f_*\) in the Cat/localizer example on scan 020.

### N24 — Pointwise opposition is not the full modern opposite convention
**Kind:** unpursued implication / reading question. **Source:** 117/012:16–29.

The displayed definition is \(\mathcal H^\circ(A)=\mathcal H(A)^\circ\), and it interchanges the two adjoints. DSS BISITE F.8 uses \(\mathbb D(S^{op})^{op}\), with base and coefficient opposition performing distinct jobs, so this is a related but differently specified operation. The unspecified two-cell variance in N20 is relevant; no fixed-base Verdier duality or dualizing weight of BISITE G follows from this paragraph.

### N25 — Preserving weak arrows does not imply preserving Kan operations
**Kind:** unproved claim. **Source:** 117/016:8–27; 117/018:4.

He explicitly says a functor of pairs induces maps on all localized diagram categories without a priori commuting with \(f_!\) and \(f_*\), and tests the issue when the weak arrows are isomorphisms. This is a precise distinction between an indexed transformation and a transformation preserving the relevant Kan extensions, adjacent to DSS BISITE A.4/A.24 and RS GALOIS E.11. An equivalence at every indexing category is then singled out as a sufficient case, not inferred from \(f(W)\subset W'\) alone.

### N26 — The adjunction criterion and its unwritten weak-equivalence hypotheses
**Kind:** unproved claim. **Source:** 117/018:6–27; RS Hua 117-adjunction-equivalence-criterion.

The conditions \(f^{-1}(W')=W\) and \(fg(X')\to X'\in W'\) are explicitly transported to every diagram category, supporting **Hua's findings-register entry 117-adjunction-equivalence-criterion**. With identities and two-out-of-three in \(W'\), naturality of the counit makes \(g\) preserve weak arrows and the triangle identity makes the unit weak, so the localized adjunction is an equivalence objectwise; those closure assumptions are not written in the displayed criterion. The checked Gurski–Johnson–Osorno reference is narrower in its stated theorem because it assumes a map extension; see the reference record and R10 rather than treating Theorem 1.11 as a literal unrestricted match.

### N27 — “Special” theories and common presentations
**Kind:** conjecture. **Sources:** 117/018:32–33; 117/020:4–17.

The term **“spéciales”** applies to theories described by \((M,W)\), and the next page asks for a third pair receiving maps from two presentations and realizing a given isomorphism of theories. This is a concrete open comparison problem, not a proof that an arbitrary abstract derivator has an enhancement or that its associated localizer is accessible; compare RS GALOIS B.13, E.11 and G.6. It also should not be identified solely by vocabulary with NR's coda on “localiseur spécial”.

### N28 — Exactly what is claimed for a fundamental localizer
**Kind:** unproved claim / self-flagged. **Source:** 117/020:19–24.

The author claims left Kan adjoints already proved, expressly says **“mais non encore celle des \(f_*\)”**, and considers possible finiteness conditions on \(A,B\). This is stronger than a bare wish for \(f_!\), but weaker as historical evidence than an exhibited proof or an explicit relative Theorem A. It bears directly on RS GALOIS B.13, DSS PATHS D.18/D.22 and BISITE A.1/A.32; **Hua's “Quatre exemples”** assertion about every fundamental localizer is not used here to remove those distinctions.

### N29 — Derived sheaves: a retraction of the negative claim
**Kind:** withdrawn in the same text / unproved claim. **Source:** 117/021:17–44.

The sentence **“généralement pas d'adjoint à gauche”**, with its “sans doute” qualification, is reversed by **“Si pourtant”**. The proposed reason is the exactness of an ordinary \((f^\circ_{\mathrm{top}})_!\), followed by the literal phrase **“quasi-isom. en iso”**; no general exactness proof is supplied. This is relevant to DSS BISITE A.24, A.28 and F.1, but the correction of the existence claim does not itself validate the proposed derivation.

### N30 — An elementary test of the asserted exactness
**Kind:** own idea, confidence high, with the stated interpretation. **Source:** 117/021:38–44; context: Hua “Quatre exemples”, DSS BISITE A.24.

If the functor is ordinary left Kan extension on module diagrams for an arbitrary indexing functor, test \(BC_2\to e\) over \(k=\mathbf F_2\), where it is coinvariants. The exact sequence \(0\to k\xrightarrow{\,1\mapsto1+g\,}k[C_2]\xrightarrow{\mathrm{aug}}k\to0\) becomes a sequence whose first nonzero map is zero after coinvariants, since \(g=1\) and \(1+1=0\). Thus ordinary left Kan extension is not exact in this interpretation, and an acyclic three-term complex supplies a direct failure of preservation of quasi-isomorphisms; this diagnoses the argument rather than denying the existence of a derived left adjoint.

### N31 — Hot 4 keeps both a hypothesis and two questions
**Kind:** unproved claim / self-flagged. **Source:** 117/021:53–67.

The actual square has \(A'\to A\), \(B'\to B\), with \(f:A\to B\), and the conditions are written on this \(f\): “cofibrant” for left base change and “fibrant” for right base change. The alternatives **“ou \(g\) fibrant ??”** and **“ou \(g\) cofibrant ??”** remain questions; the page's covariance must be converted before comparing with the presheaf formulas of DSS STRATA D.4 and BISITE F.2/F.8. In particular, the differently oriented square in **Hua, “Propriétés formelles”** does not warrant moving the manuscript's condition to \(f'\).

### N32 — Transposition is a formal claim distinct from exactness
**Kind:** unproved claim. **Source:** 117/021:66–67.

He calls the two formulas **“transposées”** by passage to adjoints. This is an early explicit mate-calculus assertion, closely related to DSS BISITE F.7, but the existence of a mate does not establish its invertibility without the corresponding exactness hypotheses. Nothing on this page supplies the full coherent correspondence formalism of BISITE F.10 or RESIDUE I.3.

### N33 — Hot 5: fully faithful indexing
**Kind:** unproved claim. **Source:** 117/021:70–80.

The page asserts that a fully faithful \(f\) makes \(f^*\) a localization and both Kan adjoints fully faithful, with the two displayed unit/counit identities. This is a direct early statement of an ordinary fully-faithful-indexing consequence, relevant to DSS BISITE F.1/F.9, but it is not the full support-image theorem or exceptional-adjoint chain of STRATA D.1. Its proof would require the adopted Kan-extension calculus, not just the existence of the three functors.

### N34 — Hot 6 needs a meaning of “localisation”
**Kind:** unproved claim / contextual counterexample. **Source:** 117/021:83–90.

The hypothesis is simply **“\(f\) localisation”**, without a homotopical qualification. **Hua, “Propriétés formelles”**, supplies a counterexample to the ordinary categorical reading: localize a category of nerve type \(S^2\) at all arrows, obtaining a groupoid equivalent to \(e\), while restriction of constant space diagrams is not fully faithful, as maps to \(K(\mathbf Z,2)\) detect \(H^2(S^2;\mathbf Z)\). This is credited to Hua's interpretation and bears on DSS PATHS D.13/D.20 and BISITE E.13; inserting “homotopique” into the manuscript would conceal the issue.

### N35 — The cofinality presumption receives a sketch
**Kind:** self-flagged / unproved claim. **Source:** 117/022:3–45.

For \(j\dashv i\), **“je présume”** precedes the circled \(i_{\mathcal H}^*=j_!^{\mathcal H}\), but the starred continuation says **“Résulte du diagramme comm.”** and proposes a presheaf argument. This is an attempted justification of the adjoint special case, not an entirely abandoned question and not the general comma-test criterion of relative Theorem A. The argument's universe and variance assumptions, and its \(i/j\) composition labels, require checking; compare DSS BISITE F.1, RESIDUE B.5 and RS GALOIS B.3.

### N36 — A formal route to the adjoint special case
**Kind:** own idea, confidence high conditional on the two-functor convention. **Source:** 117/006:16–23; 117/022:8–22.

If the proposed indexed theory sends the unit and counit of \(j\dashv i\) to an adjunction \(i^*\dashv j^*\), uniqueness of left adjoints identifies \(i^*\) with \(j_!\), and \(p_0j=p\) then gives the integration comparison. This avoids the large presheaf categories used in his sketch, but requires checking the still-unspecified two-cell variance of “2-contravariante”. It bears on the same adjoint special case as DSS RESIDUE B.5 and does not upgrade it to GALOIS B.3's relative theorem.

### N37 — Filtered categories are only a marginal project
**Kind:** conjecture / self-flagged. **Source:** 117/022:27–28.

**“Cas des catégories filtrantes ??”** and the cofinal-functor continuation ask for a further case of integration invariance. They give no strict-colimit versus homotopy-colimit comparison, no totality quantifier, and no equalization argument. Thus RS TOTASPH D.7, RESIDUE F.5/F.7 and DSS PATHS A.2–A.8 receive a historical motivation, not a solution.

### N38 — Hot 7 concerns lifting morphisms, not reverse excision
**Kind:** conjecture / unproved claim. **Source:** 117/023:3–22.

For the cover by two full sieves or two full cosieves, **“On veut”** introduces surjectivity of the displayed Hom map, while **“elle a des chances”** qualifies the object statement. This is relevant to coherent gluing and to the limits in DSS BISITE E.13 / PATHS D.20, but it is neither faithfulness nor a categorical equivalence and does not imply strong W(7). **Hua, “Un recollement”**, cautiously calls it a neighbour of strongness; that caution is preferable to identifying it with modern Der 5.

### N39 — A coherent reformulation to test
**Kind:** own idea, confidence medium. **Source:** 117/023:8–19; context: DSS BISITE E.13, PATHS D.20, RS GALOIS G.6.

Replace strict equality of the two restricted objects by a specified isomorphism, or by coherent equivalence in an enhancement, and ask which lifting property descends to the displayed surjection on Hom sets. This is motivated by the source's tentative object-bijectivity clause and the supplied warning that homotopy categories lose coherent gluing data. It is a proposed comparison problem, not a claim that a pseudopullback formulation proves Hot 7 or reverse excision.

### N40 — The loop staircase is geometric data without a theorem
**Kind:** unpursued implication. **Source:** 117/025:4–79.

The staircase and the long sequence exhibit \(Y,X,Z,\Omega Y,\ldots,\Omega^4Y\), with \(f,g,h\), iterated loop labels and inserted \(e\)'s. **Hua, “La suite des lacets”**, interprets it as a fibre/Puppe sequence and explicitly supplies homotopy-cartesianness, which is not written on the leaf. This is relevant to DSS PATHS C.6 and E.2, but does not establish a monoidal categorical loop model, a sign convention, or any finite-category census in NR 1–6.

## Links to the supplied Pursuing Stacks text

### N41 — Models and weak equivalences as the basic data
**Kind:** unpursued implication. **Sources:** 117/005:33–36, 117/018:32–33, 117/020:4–17; context/ps_chapters_VI_VII/ps6.tex:4539–4580, §125, pp. 532–533.

The programme **“en termes de \((M,W\subset\operatorname{Fl}(M))\)”** and the special-theory comparison question closely match §125's discussion of integration and cointegration independent of chosen fibrations/cofibrations. The supplied primary text explicitly names the derivator at this point, so the connection is firmer than an inference from the title alone. It bears on RS GALOIS B.13/G.6 and DSS PATHS D.17/D.22 without settling the general enhancement problem.

### N42 — Three Kan operations versus six-operation duality
**Kind:** unpursued implication. **Sources:** 117/002:23–41, 117/005:25–30, 117/010–012; context/ps_chapters_VI_VII/ps7.tex:519–660, §136, pp. 565–568.

Section 136 explicitly connects left-derived integration, restriction, right-derived direct image, tensor and internal Hom, and asks for a broader duality formalism. The present leaves give related adjunction and internal-Hom formulas, but no extraordinary inverse-image construction, correspondence category or coherence proof. Compare DSS BISITE F.4–F.13 and RESIDUE I.3–I.5: their extra hypotheses should remain visible rather than being credited to the three-functor notation alone.

### N43 — Properness, duality and finiteness are still distinct
**Kind:** unpursued implication. **Sources:** 117/012:16–33, 117/021:53–67; context/ps_chapters_VI_VII/ps7.tex:781–865, §137, pp. 571–572.

The supplied §137 explicitly revises the relation between cohomological base change and a stronger duality notion, using infinite discrete categories and finite groups as cautions. This gives a contextual reason to distinguish the present Hot 4 proposal from ambidexterity, dualizing weights or geometric properness in DSS BISITE F.11/F.19/G.1–G.14 and RESIDUE I.1–I.8. Those refinements are absent from the present scans, even though the general questions are closely related.

### N44 — Contents entries are leads, not missing chapter evidence
**Kind:** reading question / bounded source comparison. **Sources:** context/PURSUING_STACKS_CONTENTS.md, §§60,64,69–70,85 and the unnumbered heading “Examples. Totally aspheric asphericity structures”; RS MPL_106+107 and MPL_134-8_043-087 H4.

The contents list points toward early localizer axioms, derivators and asphericity structures, but only chapters VI–VII are supplied in full. A heading about totally aspheric structures cannot establish the final-image quantifier of Q02, and a heading about integration cannot establish relative Theorem A. The first-appearance search therefore remains bounded to the present scans and the actual source passages quoted above.
