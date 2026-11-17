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

## Steps the manuscript itself marks as unverified or withdraws

These entries index the author's reservations; the diplomatic `\unsure` marks are the transcriber's doubts and are not evidence that the author doubted a claim. References to N-items give the contextual comparison and relevant research-register IDs.

| Item | Cote/scan and file lines | Kind | His words and the status of the step |
|---|---|---|---|
| S01 | 116/005:3–4 | self-flagged | **“fort asphérique (réciproque ?)”**, with a separate marginal question mark, leaves the converse of the gluing characterization unverified; see N04 and DSS STRATA D.1–D.2. |
| S02 | 116/007:10–14 | conjecture | **“On s'intéresse”** is the doubtful reading introducing sought conditions making both inclusions weak equivalences, and **“on n'a pas envie de le supposer ici”** removes the desired left-exactness assumption from the problem; see N09, rather than treating the problem as solved by N10. |
| S03 | 117/004:23–31 | conjecture | **“On a sans doute”** qualifies the proposed mapping object and its possible explicit simplicial model; see N17 and DSS PATHS C.1–C.2. |
| S04 | 117/004:39–45 | self-flagged | The marginal description **“particulièrement peu comprises”** is itself a doubtful reading, so it is evidence of an apparent reservation about truncations and invariants, with the lexical uncertainty retained; see N18. |
| S05 | 117/005:3–6 | self-flagged | **“Cas additif seulement ?!?”** qualifies the proposed K-theory invariants; the question is not answered on the subsequent leaves, and N18 distinguishes it from the enriched-Hom results in DSS PATHS C.8–C.10. |
| S06 | 117/005:21–23 | self-flagged | The margin dated **“24.11.83”** asks for **“Relations entre ces Hom internes”** and the Homhot objects, ending **“??”**; see N19 and RS GALOIS G.6. |
| S07 | 117/005:33–36 | conjecture | **“Sauf peut-être”**, **“il semble”**, and **“Dégager les bons axiomes”** mark a programme for description by a pair \((M,W)\), not an established presentation theorem; see N18, N27 and N41. |
| S08 | 117/006:23 | self-flagged | **“à préciser”** or **“bien préciser”** follows the strict two-contravariant assignment, leaving a specification problem in the variance formalism; see N20 and DSS BISITE F.1/F.8. |
| S09 | 117/010:17–18 | self-flagged | **“Il faut faire Attention”** asks whether Hot 2 should be restricted to **“f cofibrants”**; this is a reservation about the proposed axiom, distinct from the later model-specific uncertainty in S12. |
| S10 | 117/014:35–37 | self-flagged | **“Attention”**, the doubtful **“il n'est pas clair”**, and **“sauf pour I fini”** mark the infinite-product issue in the localization example; see N21 and R06. |
| S11 | 117/020:4–17 | conjecture | **“peut-on en trouver un troisième”** asks for a common presentation realizing a given isomorphism of theories; the page supplies neither the pair nor the comparison maps, as discussed in N27 under RS GALOIS B.13/G.6. |
| S12 | 117/020:22–24 | self-flagged / unproved claim | **“J'ai prouvé”** asserts a proof of left adjoints elsewhere, while **“mais non encore”** and **“Il est possible”** explicitly leave right adjoints and possible finiteness assumptions unresolved; see N28 and Q03. |
| S13 | 117/021:33–44 | withdrawn in the same text | **“généralement pas d'adjoint à gauche”**, qualified by **“sans doute”**, is immediately reversed by **“Si pourtant”** on the same scan; N29–N30 separate the withdrawal from the unproved exactness argument offered for it. |
| S14 | 117/021:59–60 | self-flagged | **“[ou g fibrant ??]”** asks whether the alternate hypothesis suffices for left base change; N31 compares DSS STRATA D.4 and BISITE F.2 without deleting the two question marks. |
| S15 | 117/021:63–64 | self-flagged | **“[ou g cofibrant ??]”** is the dual unresolved alternative for right base change; it remains distinct from the main hypothesis written on \(f\), as explained in N31 and R07. |
| S16 | 117/022:8–22,36–45 | self-flagged / unproved claim | **“je présume”**, a question mark and the circled \(i^*=j_!\) initially qualify the adjoint cofinality step, but **“Résulte du diagramme comm.”** subsequently offers a sketch; N35–N36 record both stages rather than calling the step simply unanswered. |
| S17 | 117/022:27–28 | self-flagged | **“Cas des catégories filtrantes ??”** and the cofinal-functor continuation are a marginal project, without the total-asphericity or universal-colimit quantifiers of RS TOTASPH D.7 / RESIDUE F.7; see Q02 and N37. |
| S18 | 117/023:3–19 | conjecture | **“On veut”** requests surjectivity on arrows and **“elle a des chances”** qualifies bijectivity on objects; N38–N39 distinguish both from an established equivalence of categories or strong W(7). |
| S19 | 116/004:25; 116/006:3 | withdrawn in the same text | **“asphérique”** is struck and replaced by a doubtful equivalence abbreviation on scan 004 and by **“équiv. faible”** on scan 006; this is an authorial change of terminology whose exact scope must not be standardized retrospectively, as in N02/N06. |
| S20 | 117/008:15–45; 117/010:6–18 | withdrawn in the same text | The first integration scheme through \(L_A\) is cancelled before the separate Hot 2 adjoint formulation; the later presheaf sketch on 117/022 reuses a method without reinstating the entire cancelled draft, as in N22. |
| S21 | 117/021:83–90 | withdrawn wording / unproved claim | The word **“iso”** is struck after **“foncteurs loc.”** in Hot 6, leaving the localization formulation; this is a local correction of the asserted conclusion, while N34 separately addresses the ambiguity in its hypothesis. |

## Reading questions raised after the freeze

No entry in this section changes the transcription, the page files, their doubt marks or their hashes. Hua's page labels generally follow the archive foliation, one lower than the supplied PDF scan number; all references here use the supplied scan number and name the modernised subsection.

### R01 — Right versus left adjoint in the general gluing paragraph

**Kind:** reading question. **Source:** 116/007:14; context/hua_project/116.modern.tex:304–315, “Le point de vue inverse”; bears on N09–N10.

The frozen reading is **“a un adjoint à droite \(f^*\)”**, whereas Hua explicitly corrects it to a left adjoint, citing the neighbouring formulas and the intended limit-preserving functor. Scan 008:3 itself says **“adjoint à g.”**, so the disagreement is already internal to these leaves. The correction may be mathematically motivated, but it is not a license to change the visible word in scan 007.

### R02 — The functor named in the retraction margin

**Kind:** reading question. **Source:** 116/004:30–33; context/hua_project/116.modern.tex:193–205, “Le cylindre d'un morphisme de topos”; bears on N03.

The frozen margin reads \(r^*(F_1)\), whereas Hua reports the leaf as writing \(i_*(F_1)\) and introduces \(r\) as his own name for the retraction. The same tuple motivates both interpretations, so agreement of the mathematics cannot decide the letter or exponent. The frozen version and its local uncertainty in the tuple remain the source for this return.

### R03 — Fibrant versus filtered on the loose base-change leaf

**Kind:** reading question. **Source:** 116/010:7–22; context/hua_project/116.modern.tex:354–370, “Un feuillet séparé”; bears on N12 and Q03.

The frozen text reads **“A fibrant”**, while Hua reads **“A filtrante”** and interprets the comma/fibre comparison using a precofibred functor. Hua also treats the isolated marginal mark as \(f\), whereas the frozen reading is an integral sign followed by **“dans Hot”**. Neither the extra hypothesis nor the alternative letter is imported into the transcription.

### R04 — The global Hom integral and the distinct Hom symbols

**Kind:** reading question. **Source:** 117/002:10–19,32–33; context/hua_project/117.modern.tex:180–225, “La structure des dérivateurs”; bears on N14–N15.

The frozen displays retain the differing Homht/Homhot readings and \(\int_I\), while Hua normalizes the Hom names and replaces the integral by \(\mathrm{holim}_I\). His interpretation resolves a mathematical issue but loses evidence relevant to the later distinction between integration and cointegration. The notes therefore keep the possible correction separate from the author's written formula.

### R05 — Which functor is said to commute with sums

**Kind:** reading question. **Source:** 117/010:37–39; context/hua_project/117.modern.tex:340–345, “Les adjoints”; bears on N23.

The frozen marginal reading assigns the commutation phrase to \(f_!\), with uncertainty in its words, while Hua quotes it with \(f^*\) and explains why Hot 3 would justify that assertion. The mathematical availability of either sum-preserving functor cannot settle the exponent and does not remove the recorded doubt. This is a local reading discrepancy, not a reason to strengthen the axiom list.

### R06 — A negative warning versus an asserted axiom

**Kind:** reading question. **Source:** 117/014:35–37; context/hua_project/117.modern.tex:379–385, “Quatre exemples”; bears on N21 and DSS PATHS D.16.

The frozen margin reads **“il n'est pas clair”** with a doubt mark, followed by the finite-index qualification. Hua's prose says that the margin affirms Hot 1, then warns that infinite products are problematic. These are materially different descriptions of the author's position, so the frozen negative warning is reported as such without claiming that the contextual interpretation settles the ink.

### R07 — The base-change condition belongs to the displayed outer map

**Kind:** reading question. **Source:** 117/021:53–64; context/hua_project/117.modern.tex:466–485, “Propriétés formelles”; bears on N31 and DSS BISITE F.2/F.8.

In the frozen square the horizontal arrows run \(A'\to A\), \(B'\to B\), and the outer vertical arrow is \(f:A\to B\); the hypotheses are written on \(f\). Hua reverses the horizontal orientation in his square and says the condition should be moved to \(f'\). This reorientation must be distinguished from a correction of the original square, especially before comparing covariant and presheaf conventions.

### R08 — Exactness and quasi-isomorphisms on the derived-sheaf page

**Kind:** reading question. **Source:** 117/021:38–44; context/hua_project/117.modern.tex:451–461, “Quatre exemples”; bears on N29–N30.

The frozen words are **“est exact !”** and **“transforme quasi-isom. en iso”**, whereas Hua attributes **“exact à gauche”** and quasi-isomorphism preservation to the leaf. The ordinary left Kan extension has an exactness problem in either reconstruction, but the particular faulty step differs. Both literal readings are therefore recorded without replacing the source by the more expected derived-category formulation.

### R09 — The corrected adjoint and the residual i/j labels

**Kind:** reading question. **Source:** 117/022:8–22; context/hua_project/117.modern.tex:519–536, “Cofinalité”; bears on N35–N36.

The final inserted adjoint direction is **“gauche”**, but the later composite retains frozen alternatives \(i_!\mid j_!\) and \(p_0i\mid p_0j\). Hua explicitly writes \(j\) to make the composition well typed. That correction explains the proposed argument but does not resolve the remaining letter shapes or erase the preceding crossed directions.

### R10 — Scope of the modern adjunction reference

**Kind:** reading question about a reference, not an alternative transcription. **Source:** 117/018:6–27; context/hua_project/117.modern.tex:393–419, “Quatre exemples”; bears on N26 and RS Hua 117-adjunction-equivalence-criterion.

Hua identifies the criterion with Gurski–Johnson–Osorno, Theorem 1.11, but the checked theorem also assumes that the right adjoint is a map extension, an inclusion identical on objects. The elementary unit/counit argument discussed in N26 is the reason a related general-adjunction statement holds under weak-equivalence closure assumptions. The primary-reference record states this distinction rather than citing an exact hypothesis match.

### R11 — What is crossed out after the adjunction argument

**Kind:** reading question. **Source:** 117/018:16–33; context/hua_project/117.modern.tex:419, “Quatre exemples”; bears on N26–N27.

Hua says that the conclusion after **“Donc”** is crossed out and elects to write it. The frozen apparatus instead places the readable deletion on the reused address **“Monsieur Grothendieck”**, while leaving the conclusion live. This is a disagreement about the state of the page and remains a reading question; the later context cannot change the already frozen deletion assignment.

### R12 — Order of the locally constant tuple

**Kind:** reading question. **Source:** 116/006:8; context/hua_project/116.modern.tex:276–281, “Le point de vue inverse”; bears on N07.

The frozen NB gives \((F_1,f^*F_1,u)\) and an uncertain final \(\mathcal X_0/\mathcal X_1\) index, whereas Hua writes the components in the convention used on scan 004. This is a sensible normalization of the intended gluing datum, but it is not the tuple read on scan 006. No consistency correction has been made.

### R13 — The programme's altered item letters

**Kind:** reading question. **Source:** 117/004:33–45 and 117/005:3–9; context/hua_project/117.modern.tex:240–270, “Un programme”; bears on N18–N19.

The frozen text preserves struck and inserted letters, including the doubtful opening \(i)\mid h)\) on scan 005. Hua presents a reordered continuous programme in modernized form. Its useful thematic ordering must not be treated as evidence that all original item letters were unambiguous or mutually consistent.

## Titles, authorial pagination, counts and dates

The table distinguishes a title or date actually written on a sheet from the archive's catalogue descriptions and foliation. A source's printed date dates that reused document, without dating the mathematical annotation on its other side.

| Item | Cote/scan | Kind | Title, count or dating evidence |
|---|---|---|---|
| T01 | 116/002:3–4 | reading question / title evidence | **“Mapping cone”** is the title on the cover; no authorial page total accompanies it. |
| T02 | 116/004:3 | reading question / section-title evidence | **“Relation entre morphismes de topos et recollements de topos.”** heads the main discussion, without a separate authorial page number or total. |
| T03 | 117/002:3–4 | reading question / title and date evidence | **“Structure des dérivateurs”** is underlined, with **“déc. 83”** in the margin; this dates the title sheet's mathematical discussion, not every leaf of the cote. |
| T04 | 117/005:21–23 | reading question / date evidence | **“24.11.83”** belongs to the internal-Hom margin, and thus supplies a separate dated mathematical intervention from the December title. |
| T05 | 117/006:2–4 | reading question / title and pagination evidence | **“Théorie (de variance) homotopique \(\mathcal H\)”** starts the exposition with the authorial number **1**. |
| T06 | 117/006,008,010,012,014,016,018,020,021 | reading question / pagination evidence | These nine leaves carry the authorial sequence **1,2,3,4,5,6,7,8,9**, respectively; this is a visible sequence, not a written declaration that the entire dossier has nine pages. |
| T07 | 117/022:56 | reading question / cancelled-title evidence | The pale reversed and struck inscription is frozen as doubtful **“Théorie\|Flèches … flèches\|fibres … II”**; neither a secure complete title nor an authorial page count can be recovered from it. |
| T08 | 116/011:15,21 | reading question / reused-document date evidence | The typed thesis notice is dated **19 JUIN 1981** and announces **30 JUIN 1981**; these are evidence about the reused notice, not a secure date for the mapping-cone notes. |
| T09 | 117/019:5 | reading question / reused-document date evidence | The accounting sheet explicitly carries **1981**, while the comparable sheets at 117/007,009,011,013,015,017 provide no equally secure explicit year in the transcription. |
| T10 | 117/024:4,15–16 | reading question / reused-document date evidence | The DEA meeting circular is dated **15 avril 1983**, announces **28 avril**, and concerns **1983–1984**; these are distinct documentary dates rather than a pagination statement. |
| T11 | 117/026:7,22,68 | reading question / reused-document date evidence | The ministry letter carries **30 Mars 1983**, a receipt stamp **11. AVR. 1983**, and a forwarding date **13 Avril 1983**. |
| T12 | all 34 supplied scans | reading question / count evidence | No explicit authorial dossier total such as “19 pages” or “Pages 1–67” occurs in this set; **9 supplied pages in cote 116 plus 25 in cote 117** is the delivery count, and scan 116/009 is omitted as blank by the supplied prompt. |

The remaining corner numbers are treated as archival foliation in TeX comments; none has been promoted to `\mspage`. Hua's modernized page references have been translated to scan references in these notes, not used as an independent numbering authority.

## Individual comparison with every entry of NEW_RESULTS.md

The twelve numbered entries and all three unnumbered notices are covered separately. The “review” metadata below is a concise attribution to the supplied register; its exact `Proved by`, `Checked by`, proof path and manuscript locator are preserved in `working/context_catalog.json`, without implying that those other proof files were supplied or inspected here.

### NR01 — NEW_RESULTS 1: finite monoids, finite type and bounded homology

**Kind:** unpursued implication. **Source:** NR line 18; no occurrence in the supplied scans. **Review reported:** “not yet (Pro check prompt drafted)”; earlier finite-dimensional subcase attributed separately to CATHOT G.4. **Register locator:** V ms.51–52; OWN_RESULTS §2.

No finite monoid, universal group, bounded-homology criterion or realization classification occurs on these leaves. The general model programme at 117/004–005 does not anticipate this specific theorem or its sharp converse. The later FINMON headline results in RS likewise receive no new finite-model evidence here.

### NR02 — NEW_RESULTS 2: Miller's theorem with a cohomological bound

**Kind:** unpursued implication. **Source:** NR line 19; no occurrence in the supplied scans. **Review reported:** “not yet”. **Register locator:** OWN_RESULTS §1; tool for result 1.

There is no map from a finite group's classifying space, cohomological vanishing hypothesis or restriction on the target fundamental group. The all-coefficient cohomology of the topos gluing in 116/004:26–28 is a different statement and gives no proof of this refinement (N02).

### NR03 — NEW_RESULTS 3: Kan–Thurston without small quotients and E.17

**Kind:** unpursued implication. **Source:** NR line 20; no occurrence in the supplied scans. **Review reported:** GALOIS B.11–B.12 followed by a medium review and read at max; the independent OWN_RESULTS §3 proof not yet checked and its cardinality bound quoted from memory. **Register locators:** GALOIS B.10–B.12; OWN_RESULTS §3; V ms.46, VII ms.129–132, IX ms.22–23.

The mapping-object expectations at 117/004:23–31 and 117/005:9–23 have no acyclic BG presentation, cardinal bound or groupoid-valued ind-object conclusion. Thus they provide motivation for mapping-space questions, not the specific result catalogued in DSS PATHS D.K2–D.K5. The selected older RS CATHOT E.17 Open entry should not erase the later review information explicitly supplied by NR 3.

### NR04 — NEW_RESULTS 4: uncountably many maps to S²

**Kind:** unpursued implication. **Source:** NR line 21; no occurrence in the supplied scans. **Review reported:** “not yet”. **Register locators:** OWN_RESULTS §4; CATHOT D.6; V ms.43–46.

No hypothesis involving infinitely many sphere retracts, H¹ or π_n(S³) is stated, and no countability argument occurs. The loop staircase at 117/025 is not such an argument (N40). RS's newer S2COUNT headline is a separate claimed advance; these leaves neither verify it nor add a model for it.

### NR05 — NEW_RESULTS 5: at least 34 arrows for RP² posets

**Kind:** unpursued implication. **Source:** NR line 22; no occurrence in the supplied scans. **Review reported:** “not yet”. **Register locators:** OWN_RESULTS §5; CATHOT G.8.

RP², arrow counts and minimal finite posets do not appear. Neither the two-stratum topos picture nor the loop drawings give a candidate for this minimization problem.

### NR06 — NEW_RESULTS 6: small-category census for S¹, S² and S³

**Kind:** unpursued implication. **Source:** NR line 23; no occurrence in the supplied scans. **Review reported:** the entry says “not yet”, while its credit field records earlier independent enumerations. **Register locators:** OWN_RESULTS §6 and code; CATHOT G.14–G.15; XII appendix ms.8–11.

No explicit finite category or monoid is enumerated and none of the minima or uniqueness statements is made. “Modèles” at 117/004:4 is too general to count as a 1983 form of the census (N17). The register's distinctions between earlier calculations, later new clauses and a full review are retained.

### NR07 — NEW_RESULTS 7: a reversible localizer not detected by spectra

**Kind:** unpursued implication. **Source:** NR line 24; no occurrence in the supplied scans. **Review reported:** “not yet (prompt REVERSIBLE_LOCALIZERS drafted)”. **Register locators:** RESULT_REVERSIBLE_NOT_STABLE.md; POLES F.14(1); XII §5 and XVI §3.

The sphere-null cofibre class W_S and its RP∞/RP² distinction are absent. Hot 7 at 117/023 is a different gluing requirement and does not assert reversibility (Q01, N38). The separate RS REVLOC F.1 claim addresses failure of relative Theorem A, so it must not be substituted for a review of NR 7's spectral-detection assertion.

### NR08 — NEW_RESULTS 8: failure of XII Theorem 2 for W∞

**Kind:** unpursued implication. **Source:** NR line 25; nearest manuscript 117/023:3–22. **Review reported:** TOTASPH A.13 checked and its 37-object category recomputed by the stated medium review; the Pro return and max expert reported agreement. **Register locators:** DERIVATEURS_EXPERT/FINDINGS F-G1; TOTASPH A.13; XII ms.78 and listed consequences.

The finite acyclic/non-aspherical join counterexample does not occur in these scans, and Hot 7 does not formulate the strong cube or reverse-excision axiom. The supplied companion's actual strong W(7) statement is located in Q01, while RS POLES B.2 concerns the weaker forward gluing assertion. The register's broad sentence about which later arguments survive is not independently audited here.

### NR09 — NEW_RESULTS 9: homology localizers fail Loc(7F)

**Kind:** unpursued implication. **Source:** NR line 26; no occurrence in the supplied scans. **Review reported:** “not yet”. **Register locators:** FINDINGS F3-5; XVI ms.105.

No trefoil complement, circle base or homology-localizer intrinsic-factorization obstruction is present. The uncertainty about f_* at 117/020:22–24 is about a Kan adjoint, not a proof of failure of Loc(7F) (N28).

### NR10 — NEW_RESULTS 10: total fixed-origin paths force totality of Y

**Kind:** unpursued implication. **Source:** NR line 27; nearest manuscript 117/025. **Review reported:** “not yet”. **Register locators:** FINDINGS F2-11; XII ms.102–103,112.

The staircase gives iterated loop symbols but no fixed-origin category Ch(Y;y₀,−), simple-connectivity hypothesis or totality implication. DSS PATHS E.12 and RS totality entries concern precise categorical tests that are absent from the drawing (N40).

### NR11 — NEW_RESULTS 11: total W∞-asphericity does not imply filteredness

**Kind:** unpursued implication. **Source:** NR line 28; nearest manuscript 116/003:46 and 117/022:27–28. **Review reported:** TOTASPH C.1–C.10 followed, C.8–C.9 recomputed, and the Isbell–Mitchell source traced/opened by the stated reviews. **Register locators:** TOTASPH C.5–C.10; II ms.36–36ter; RS TOTASPH C.10 and PRETOT A.12.

Neither the conjecture with its totality quantifier nor the Δ_inj counterexample is stated in this package. The supplied companion places the question already on II ms.36, before the later corrected discussion on 36bis–36ter, so the register's shorthand “conjecture of … 36ter” should not be used as its first-occurrence locator (Q02). The different totality-to-exact-Ab-colimits question remains Open in the selected RS TOTASPH D.7 / RESIDUE F.5 entries.

### NR12 — NEW_RESULTS 12: RP² is not the classifying space of a finite monoid

**Kind:** unpursued implication. **Source:** NR line 29; no occurrence in the supplied scans. **Review reported:** medium and max checks, including published Miller/Atiyah sources, are explicitly reported. **Register locators:** CATHOT G.4/G.6; G6_VERDICT.md and EMAIL_CLAIMS_CHECK.md; register says sent to the author 12 November 2026.

No finite-monoid or universal-group argument occurs here, so the pages supply neither an early statement nor a counterexample to this reported result. The review and communication history is attributed to NR rather than independently verified or repeated as a new action.

### NRK1 — Unnumbered notice: Isbell–Mitchell, Theorem 3

**Kind:** unpursued implication. **Source:** NR line 31; no occurrence in the supplied scans. **Status copied:** “Known after all (listed so that nobody claims them)”; source points back to item 11.

The notice's affine-category filteredness fact and its bibliographic attribution do not occur in the manuscript. Its contribution to the counterexample and the separate exactness-to-totality bridge are the contextual facts reported under NR11, not results newly proved by this return.

### NRK2 — Unnumbered notice: uniqueness in Nielsen realization

**Kind:** unpursued implication. **Source:** NR line 32; no occurrence in the supplied scans. **Status copied:** “Known after all (listed so that nobody claims them)”; Harvey 1971 is the supplied attribution, without an independent manuscript locator.

No Nielsen realization problem, mapping class group or uniqueness theorem appears. The broad word “modèles” is not evidence for this separate moduli problem.

### NRK3 — Unnumbered notice: special localizers and accessibility

**Kind:** reading question. **Source:** NR line 33; nearest manuscript 116/007:8 and 117/018:32–33. **Status copied:** “Known after all (listed so that nobody claims them)”; Cisinski, Astérisque 308, Corollary 4.2.22 is the supplied attribution.

The word **“accessible”** qualifies a topos gluing functor in cote 116, while **“spéciales”** names diagram theories presented by pairs in cote 117. Neither passage states the characterization of a special fundamental localizer by accessibility (N09, N27). The bibliographic assertion is therefore preserved as a contextual notice, not used to resolve RS GALOIS B.13 from shared terminology.

## Individual comparison with all 255 dossier statements

Every selected DSS row has its own entry below, in the source order: STRATA 10, PATHS 76, BISITE 113 and RESIDUE 56. The status and earlier manuscript locator are copied from the supplied dossier; a blank locator is explicitly marked rather than reconstructed. The short topic is an index label, not a replacement statement; the exact statements, original rows and status cells are preserved in `working/context_catalog.json`.

The second column cites the line of `context/DOSSIER_STATEMENTS_WITH_STATUS.md` and its own earlier-manuscript locator; those older locators do not refer to a supplied Montpellier scan. The third column identifies evidence in the present package, or says **none** for no occurrence of that particular statement. Each last-column comparison is one note, with its kind in the third column; N/Q references lead to the source quotations and fuller analysis above.

### STRATA D

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **STRATA D.1** — Exceptional adjunction chains | claim (return: Known); DSS:15; I ms.1–9; Lead 4 | 116/004–008; 117/021:70–80; unpursued implication | Partial precursor: the open/closed topos gluing and the fully faithful Kan adjoints are present, but no exceptional fourth adjoint or support-image classification is stated; see N01, N10 and N33. |
| **STRATA D.2** — Support sequences and stable recollement | claim (return: Known); DSS:16; I ms.2–9; Lead 4 exactness clauses | 116/005:5–16; unpursued implication | The relative-cohomology sequence is a concrete analogue, not the coherent fibre/cofiber square or stable strong recollement theorem; “cohomologie relative” is the relevant source phrase (N05). |
| **STRATA D.3** — Poset lifting tests for smoothness/properness | claim (return: Proved); DSS:17; I ms.53–56; Lead 4 map classification | **none**; unpursued implication | Absent: no finite-poset outgoing or incoming lifting-poset criterion is formulated, and the words “fibrant” and “cofibrant” in Hot 4 do not define one (N31). |
| **STRATA D.4** — Strict base change and its converse tests | claim (return: Proved); DSS:18; I ms.49–59; VI ms.162–169; Lead 4 | 116/010:3–17; 117/021:53–64; unproved claim | Hot 4 proposes the two base-change isomorphisms with hypotheses and questioned alternatives, but does not prove the universal space-valued converses; its covariant convention must be converted (N12, N31). |
| **STRATA D.5** — Topological versus categorical properness | claim (return: Refuted); DSS:19; Ib-C003; I ms.53–59; GALOIS D.9; Lead 4 | **none**; unpursued implication | Absent: no proposed characterization by topological properness, strict fibres, or local product structure occurs, so the register's refutation is neither repeated nor contradicted here. |
| **STRATA D.6** — Four-object diamond example | claim (return: Proved); DSS:20; VIc-C008 strictness comparison; Lead 4 | **none**; unpursued implication | Absent: there is no diamond map to the walking arrow and no comparison between its fibration, opfibration and fibre-bundle properties. |
| **STRATA D.7** — Inclusions, projections and component conditions | claim (return: Proved); DSS:21; I ms.54–56; Lead 4 examples and edge cases | 116/006:10–18; 117/021:70–80; unpursued implication | The notes discuss open/closed pieces and fully faithful indexing, but supply no poset classification by sieves/cosieves or smooth/proper product-projection theorem (N08, N33). |
| **STRATA D.8** — Geometric interpretation of finite-poset coefficients | claim (return: Proved); DSS:22; Lead 4 constructible base-change comparison | **none**; unpursued implication | Absent: no finite-poset constructible coefficient dictionary or ambient geometric comparison is given; the topos construction in N01 is a different level of statement. |
| **STRATA D.9** — Slice and closure variance | claim (return: Proved); DSS:23; I ms.54; XII ms.59 | 116/006:10–18; 116/010:8–17; reading question | The labels on Top(Δ₁) and the comma/fibre comparison make variance relevant, but neither the cited closure formula nor the correction of the I ms.54 target is written here (N08, N12). |

### STRATA G

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **STRATA G.2** — Totality and universal simplicial colimits | claim (return: Proved); DSS:24; XII ms.88–89; TOTASPHB.11 | **none**; unpursued implication | Absent: “i est tot 0-asph.” is about a functor, and the filtered-category margin has no universal homotopy-colimit/strict-colimit test (Q02, N13, N37). |

### PATHS A

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **PATHS A.P1** — Path components and localized Hom | claim (return: Proved); DSS:32; VII ms.65–74 | 117/003; 117/004:23–31; unpursued implication | The higher-arrow sketches and tentative Hom object are thematic antecedents only: no full path category, component-set identification or composition-compatible comparison is defined (N16–N17). |
| **PATHS A.P2** — Sequential model and Grothendieck roof | claim (return: Proved); DSS:33; VII ms.99–110 | **none**; unpursued implication | Absent: no preorder-cofinal sequence of path types, fibred comparison roof or proof that its two legs are weak equivalences appears. |
| **PATHS A.1** — Fibred and opfibred comparison span | claim (return: Proved); DSS:34; VII ms.99-110; VIIb-C026 | **none**; unpursued implication | Absent: there is no construction of the specified span from Grothendieck total categories to a sequential colimit. |
| **PATHS A.2** — Filtered Cat-colimits | claim (return: Proved); DSS:35; VII ms.108-109; VIIb-C026 | 117/022:27–28; conjecture | “Cas des catégories filtrantes ??” motivates a cofinality question, but does not state the Grothendieck-total-category to ordinary Cat-colimit comparison (N37). |
| **PATHS A.3** — Comma criterion for total-category invariance | claim (return: Proved); DSS:36; VII ms.99-110; VIIb-C026 | 117/022:3–22; unpursued implication | Only adjoint-pair cofinality is attempted; no necessary-and-sufficient comma-contractibility test for every strict category-valued coefficient is stated (N35–N36). |
| **PATHS A.4** — Insufficiency of preorder cofinality | claim (return: Refuted); DSS:37; VII ms.99-109; VIIb-C026 | **none**; unpursued implication | Absent: neither the disputed preorder-cofinality inference nor its counterexample is present. |
| **PATHS A.5** — A nonfiltered total shape with incorrect Cat-colimits | claim (return: Refuted); DSS:38; After TOTASPH correction; VIIb-C026 | **none**; unpursued implication | Absent: Δ_inj, the diagram Bℕ^(n+1), and its contrasting total-category and ordinary-colimit homology do not occur (Q02). |
| **PATHS A.6** — Exact abelian colimits on Δ_inj | claim (return: Proved); DSS:39; TOTASPH C.7-C.10 verification | **none**; unpursued implication | Absent: the scans contain neither Δ_inj nor the exactness-to-totality bridge; NR 11 and RS PRETOT A.12 supply the contextual lead, not these pages. |
| **PATHS A.7** — Three classes of colimit shapes | claim (return: Proved); DSS:40; Part A; VIIb-C026 | **none**; unpursued implication | Absent: no chain of inclusions between filtered, universally correct Cat-colimit and totally aspherical shapes is stated. |
| **PATHS A.8** — Intrinsic recognition of correct Cat-colimit shapes | claim (return: Open); DSS:41; Part A | 117/022:27–28; unpursued implication | The filtered margin is adjacent motivation only and provides no intrinsic classification or answer to the connected converse; see N37 and RS RESIDUE F.7. |
| **PATHS A.9** — Subdivision without a categorical-homotopy inverse | claim (return: Proved); DSS:42; POLES D.6 verification; VIIc-A046; V-I066 | **none**; unpursued implication | Absent: no six-face triangle boundary, subdivision map or enumeration of reverse monotone maps occurs. |

### PATHS B

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **PATHS B.1** — Full and weak-vertical path categories | claim (return: Proved); DSS:43; VII ms.27–78 | 117/003; unpursued implication | The loose arrows do not specify allowed path types or weak vertical maps, so no literal inclusion or strict concatenation law can be read from them (N16). |
| **PATHS B.2** — Restricted paths and hammocks | claim (return: Known); DSS:44; Lead1 weak-vertical identification | **none**; unpursued implication | Absent: there is no hammock mapping simplicial set, Grothendieck nerve comparison or strict reduction argument. |
| **PATHS B.3** — Failure of a literal path-category isomorphism | claim (return: Refuted); DSS:45; Lead1 forcing claim | **none**; unpursued implication | Absent: the inclusion J is not defined, so neither its alleged categorical isomorphism nor the saturated-marking counterexample is stated. |
| **PATHS B.4** — Isomorphism-only and all-arrow markings | claim (return: Proved); DSS:46; Lead2 | 117/014:4–34; 117/016:21–27; unpursued implication | Isomorphisms are discussed as a weak class in the general localization example, but no full-path discreteness or J-equivalence assertion is attached to that case (N25). |
| **PATHS B.5** — Short fractions and weak vertical arrows | claim (return: Known); DSS:47; Part B HCF/model/fibrant-object sufficient statements on restricted side | **none**; unpursued implication | Absent: no calculus of homotopy fractions, short-fraction category or marking-forced vertical-arrow proof is given. |
| **PATHS B.6** — Coherent comparison split in Hot | claim (return: Proved); DSS:48; VII ms.68–70;PartB partial comparison | 117/004:23–31; unpursued implication | A mapping object is expected, but no comparison from full paths to localization mapping spaces or splitting of J in Hot is constructed (N17). |
| **PATHS B.7** — Backward-square hammock reduction | claim (return: Proved); DSS:49; PartB grid-sweep reduction | **none**; unpursued implication | Absent: no identity-padding or grid-sweep reduction of a backward commuting square is described. |
| **PATHS B.8** — The unrestricted-vertical comparison problem | claim (return: Open); DSS:50; PartB central unrestricted-vertical comparison | 117/003–004; unpursued implication | The sketches do not distinguish the two vertical-arrow conventions, and hence give no answer to the open J-comparison problem (N16–N17). |
| **PATHS B.9** — Finite comparison search | claim (return: Proved); DSS:51; PartB requested finite search | **none**; unpursued implication | Absent: there is no bounded search, list of 132 examples or mod-2 homology comparison. |

### PATHS C

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **PATHS C.P1** — Contractible categories of type maps | claim (return: Proved); DSS:52; VII ms.86–94 | **none**; unpursued implication | Absent: increasing endpoint-preserving type maps and their contractibility are not defined or proved. |
| **PATHS C.P2** — Coherent descent to the reachability preorder | claim (return: Proved); DSS:53; VII ms.99–123 | **none**; unpursued implication | Absent: neither a reachability preorder nor coherent descent of a path-space diagram occurs. |
| **PATHS C.P3** — General wide-marking comparisons | claim (return: Proved); DSS:54; CATHOT E.26(1),(2),(3);VIIc-A046 in Hot;V-I066 in Hot | **none**; unpursued implication | Absent: no statement of the three CATHOT E.26 comparisons or their hypotheses is present. |
| **PATHS C.P4** — Mixed-sign blocks and canonical composition | claim (return: Proved); DSS:55; CATHOT E.27;IX-037 raw path composition;VII ms.125–127 | **none**; unpursued implication | Absent: the loose zigzags on 117/003 do not define padding blocks, units or block-independent composition. |
| **PATHS C.P5** — Noninvertibility in Cat hot | claim (return: Refuted); DSS:56; VIIc-A046 in Cat hot;V-I066 strong independence inference | **none**; unpursued implication | Absent: no four-object crown or q_L map tests the difference between Cat hot and Hot. |
| **PATHS C.1** — Raw paths as a strict enrichment | claim (return: Proved); DSS:57; IX-037 | 117/004:23–31; conjecture | “On a sans doute” introduces a possible mapping complex, but no strict associative/unital enrichment or product-preserving Kan replacement is constructed (N17). |
| **PATHS C.2** — Hammocks as simplicial localization | claim (return: Known); DSS:58; IX-037 | 117/004:23–31; unpursued implication | The expected mapping object is related in aim, but weak-vertical hammocks and the composition-compatible localization theorem are absent (N17). |
| **PATHS C.3** — Pointed Cartesian versus smash units | claim (return: Proved); DSS:59; IX-044; IX-049 | **none**; unpursued implication | Absent: no absorbing-zero composition, identity-equals-zero obstruction or S⁰ unit is discussed. |
| **PATHS C.4** — Pointed model-category enrichment | claim (return: Proved); DSS:60; IX-044; IX-049; IX-052 | **none**; unpursued implication | Absent: the programme mentions models and resolutions but does not construct Kan mapping spaces on cofibrant-fibrant objects with smash composition. |
| **PATHS C.5** — Fundamental groupoids of mapping complexes | claim (return: Known); DSS:61; IX-040; IX-041; IX-072 | 117/003; 117/004:23–31; unpursued implication | The π₁ sketch and Hom expectation provide a theme, not a natural comparison with Quillen's groupoid or specified basepoint paths (N16–N17). |
| **PATHS C.6** — Loop/suspension formulas | claim (return: Proved); DSS:62; IX-084; IX-087 | 117/025:4–79; unpursued implication | The loop staircase is a geometric precursor, but no mapping-space loop/suspension identity or adjunction is stated; Hua supplies the fibre-sequence interpretation (N40). |
| **PATHS C.7** — π₁ representability is insufficient | claim (return: Refuted); DSS:63; IX-084; tests (a) and (c) | **none**; unpursued implication | Absent: there is no assertion that representability of π₁ functors forces mapping-space loop formulas, and no counterexample to it. |
| **PATHS C.8** — Truncated derived Hom for complexes | claim (return: Proved); DSS:64; IX-061; IX-065; IX-070 | 117/004:39–45; 117/005:9–30; 117/021:4–15; unpursued implication | Complexes, truncations and internal Hom occur separately, but their D^{≤0}(k)-valued enrichment, derived-tensor composition and homotopy-group calculation are not assembled (N18–N19, N29). |
| **PATHS C.9** — General additive enrichment remains open | claim (return: Open); DSS:65; IX-061; IX-065; IX-070 | 117/005:3–6; 117/012:31–33; unpursued implication | The additive K-theory question and the additivity of adjoints do not supply the missing enriched-Hom axioms; this open entry is not resolved (N18, N23). |
| **PATHS C.10** — Pointed and ind-category path refinements | claim (return: Open); DSS:66; IX-044; IX-049; IX-052; IX-072 | **none**; unpursued implication | Absent: no pointed ind-category construction or stabilized full-path refinement is specified. |

### PATHS D

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **PATHS D.1** — Size-bounded IX tests | claim (return: Proved); DSS:67; IX ms.22-23; IX-080 | 117/006:6–23; 117/008:15–45; unpursued implication | Smallness is edited and large presheaf categories enter a cancelled draft, but the two representability directions and typed IX tests are not formulated (N20, N22). |
| **PATHS D.2** — Five-arrow category and enhancement | claim (return: Refuted); DSS:68; IX ms.23; IX-080; Lead 3; CATHOT E.14; Kaledin addendum (iii) | **none**; unpursued implication | Absent: no five-arrow pointed category, all-shape rectification proof or Kaledin enhancement test appears. |
| **PATHS D.3** — Finite categories with products | claim (return: Proved); DSS:69; IX ms.23 | 117/014:4–22; unpursued implication | The represented example assumes completeness and cocompleteness, but no finite-category preorder theorem or missing-square counterexample is stated. |
| **PATHS D.4** — Rectification and constant-diagram Hom | claim (return: Proved); DSS:70; IX ms.22; IX-080; Lead 3 | 117/006:25–48; unpursued implication | The evaluation functor α_A is specified, but no rectification hypothesis identifies constant-diagram Hom with maps out of BA (N20). |
| **PATHS D.5** — Failure of semisimplicial restriction surjectivity | claim (return: Refuted); DSS:71; VII-c ms.134 companion; IX-080 | **none**; unpursued implication | Absent: the six-object suspension-poset/parallel-arrow example is not present, and Hot 7 concerns a different restriction map (N38). |
| **PATHS D.6** — Loop identities and representability | claim (return: Proved); DSS:72; IX-081, IX-088; IX ms.22-25 | 117/025; unpursued implication | The staircase does not prove the implication from higher loop identities to representability or test whether finite-poset invariance gives both operations (N40). |
| **PATHS D.7** — Rectification under derivability/model hypotheses | claim (return: Known); DSS:73; Lead 3; Part D(2) | 117/004:4–21; unpursued implication | Models and resolutions are listed as necessary structures, but finite-direct versus all-universe rectification hypotheses are not stated (N17, N41). |
| **PATHS D.8** — Finite intrinsic cofibration axioms | claim (return: Proved); DSS:74; XII ms.228-234,272; POLES A.8-A.9/G.26 addendum (i)-(iv) | 117/010:17–18; unpursued implication | The word “cofibrants” marks a reservation about Hot 2; it does not assert CF1–CF4 or a finite-direct rectification theorem (N23). |
| **PATHS D.9** — Diamond and finite-set failures | claim (return: Refuted); DSS:75; POLES addendum (i) | **none**; unpursued implication | Absent: neither the diamond-lattice counterexample nor finite sets testing CF5–CF6 is given. |
| **PATHS D.10** — Cubes do not suffice for finite posets | claim (return: Refuted); DSS:76; Part D(3) cubical test | **none**; unpursued implication | Absent: there is no cubical rectification criterion or circle-poset degree-two obstruction. |
| **PATHS D.11** — Finite simplicial models fail at Bℤ | claim (return: Proved); DSS:77; Part D(3) finite posets versus BZ and BK question | **none**; unpursued implication | Absent: no finite-simplicial-set rectification example, Nielsen monodromy or BK-fibrant opposite is discussed. |
| **PATHS D.12** — Contractible fence and BK fibrancy | claim (return: Refuted); DSS:78; Part D(3) converse BK question | **none**; unpursued implication | Absent: no nine-vertex fence or unfillable Ex² horn occurs. |
| **PATHS D.13** — Ordinary relative poset localization need not rectify | claim (return: Refuted); DSS:79; STRATA B.8 addendum; Part D(3) | 117/021:83–90; unpursued implication | Hot 6's unqualified “localisation” is adjacent to the ordinary-versus-homotopical issue, but neither circle nor BC₂ relative-poset counterexample is in the manuscript (N34). |
| **PATHS D.14** — Kaledin's shape classes | claim (return: Known); DSS:80; Recent results Kaledin; GALOIS F.5 addendum | **none**; unpursued implication | Absent: no Pos/Pos+/Pos+− shape classes or recognition theorem occur; the manuscript's small-category domain is a different specification. |
| **PATHS D.15** — Recognition of the naive enhancement | claim (return: Known); DSS:81; Recent results Kaledin (i),(iv); Part D(3) | 117/020:4–17; unpursued implication | The common-presentation question is related in motivation, but no equivalence to coherent localized diagram categories or enhancement-recognition criterion is stated (N27). |
| **PATHS D.16** — Infinite-product failure in localization | claim (return: Proved); DSS:82; Recent results Kaledin (ii),(iii) | 117/014:35–37; self-flagged | The margin explicitly warns that Hot 1 is unclear except for finite I, anticipating the need for an infinite-product qualification; it gives no bounded-winding counterexample (N21). |
| **PATHS D.17** — Later cofibration axioms and Kan extensions | claim (return: Proved); DSS:83; XIII ms.7-12,50-59; XVII ms.39-40; XIX ms.33-38,48; Part D(4) | 117/010:6–18; 117/020:21–24; unpursued implication | Left adjoints are proposed and then claimed proved for Cat/localizers, but no Cof0–Cof4 hierarchy or filtered-colimit upgrade is supplied (N23, N28, N41). |
| **PATHS D.18** — Accessible localizers and Thomason models | claim (return: Known); DSS:84; POLES G.24/E.2 addendum; Part D(2),(3) | 117/020:21–24; unproved claim | “Un localisateur fondamental” and a claimed proof of f_! occur, but no accessibility assumption, Thomason model or intrinsic-fibration criterion is given; the missing right adjoint is explicit (N28). |
| **PATHS D.19** — Locally constant Set descent is not a localizer | claim (return: Refuted); DSS:85; GALOIS A.5 addendum; Part D(1) | **none**; unpursued implication | Absent: no e→BC₂→e two-out-of-three test is present; the local-constant sheaf note in 116/006 does not formulate this class. |
| **PATHS D.20** — Coherent arrows versus arrows in Ho | claim (return: Known); DSS:86; Recent results references; STRATA C.7 addendum | 117/023:3–22; unpursued implication | Hot 7 asks only for lifting arrows across a gluing restriction and remains tentative on objects, making coherent versus ordinary gluing relevant without proving their equivalence (N38–N39). |
| **PATHS D.21** — Mapping-space upgrade from all diagram shapes | claim (return: Proved); DSS:87; GALOIS mapping-space upgrade suggestion | 117/018:16–27; unpursued implication | Equivalence is asserted at every localized diagram category in an adjunction situation, but no Kaledin-shape criterion upgrades an arbitrary comparison to an infinity-equivalence (N26). |
| **PATHS D.22** — Remaining recognition problems | claim (return: Open); DSS:88; IX-080; Part D(3); recent/additional unresolved questions; same-ID RS:438 | 117/020:4–24; unpursued implication | The common-model and missing-f_* questions give early formulations of part of the recognition problem, without resolving the register's finite, cardinal, BK or nonaccessible-localizer cases (N27–N28; RS PATHS D.22). |
| **PATHS D.23** — Homology localizers lack intrinsic fibrations | claim (return: Proved); DSS:89; POLES C.4-C.5 addendum; Part D(2) cofibration-fibration asymmetry | **none**; unpursued implication | Absent: no nonzero-spectrum localizer or free-group obstruction to enough intrinsic fibrations is constructed. |
| **PATHS D.K1** — Acyclic maps as epimorphisms in Hot | claim (return: Proved); DSS:90; GALOIS B.9 verification; CATHOT E.17 reduction | **none**; unpursued implication | Absent: there is no acyclic-map epimorphism theorem or weak double-pushout codiagonal criterion. |
| **PATHS D.K2** — Large simple acyclic groups | claim (return: Proved); DSS:91; GALOIS B.10 verification; KT_mu | **none**; unpursued implication | Absent: no group embedding into a simple acyclic group or prescribed-cardinality construction occurs. |
| **PATHS D.K3** — Kan–Thurston without small quotients | claim (return: Proved); DSS:92; GALOIS B.11 verification; KT_mu; CATHOT E.17 | **none**; unpursued implication | Absent: no acyclic BG presentation or small-quotient bound is stated; NR 3 is a contextual result only. |
| **PATHS D.K4** — Invariant ind-objects factor through groupoids | claim (return: Proved); DSS:93; GALOIS B.12 verification; CATHOT E.17 | **none**; unpursued implication | Absent: there is no small filtered ind-object theorem, W₁ factorization or groupoid-completion ind-isomorphism. |
| **PATHS D.K5** — Hom invariance forces a 1-type | claim (return: Proved); DSS:94; V ms.44-46; Lead 3 size correction; CATHOT E.17 | 117/004:23–31; 117/005:9–23; unpursued implication | Hom objects are expected and their relation queried, but the all-small-shape invariance hypothesis and resulting 1-type restriction are absent (N17, N19). |

### PATHS E

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **PATHS E.1** — Endpoint fibres and path spaces | claim (return: Known); DSS:95; CATHOT E.20-E.25; VIIc-C004; VIIc-C005 | 117/003; unpursued implication | The path-like sketches do not define exact endpoint fibres, even translation or constant-tail maps, so the all-arrows theorem is not stated (N16). |
| **PATHS E.2** — Strict monoidal categorical loops | claim (return: Proved); DSS:96; Part E; IX-037 | 117/025:4–79; unpursued implication | Iterated Ω labels are present, but no categorical loop object, strictly monoidal composition or A∞ comparison is given (N40). |
| **PATHS E.3** — All-type endpoint smooth but not proper | claim (return: Refuted); DSS:97; VII ms.161-166; Part E; STRATA path test | **none**; unpursued implication | Absent: there is no all-type endpoint functor or walking-arrow failure of properness/lifting. |
| **PATHS E.4** — Eventual alternating endpoint map | claim (return: Refuted); DSS:98; Part E; filtered-union lifting distinction | **none**; unpursued implication | Absent: no alternating path colimit or distinction between smooth/proper and strict Grothendieck lifting occurs. |
| **PATHS E.5** — Categorical mapping-path factorization | claim (return: Proved); DSS:99; Part E; XII ms.188-207 | 116/004:30–37; 117/004:7–10; unpursued implication | The mapping-cylinder/retraction construction is an analogue for topoi and cylinders are in the programme, but no factorization of every category functor with homotopy fibres is given (N03, N06). |
| **PATHS E.6** — Rectangular-band endpoint counterexample | claim (return: Refuted); DSS:100; STRATA E.11 test case | **none**; unpursued implication | Absent: no five-element rectangular-band monoid or endpoint-lifting test occurs. |
| **PATHS E.7** — Interval pushout-product is not intrinsic | claim (return: Refuted); DSS:101; POLES H.6; TOTASPH F.23; Part E | **none**; unpursued implication | Absent: neither the interval pushout-product nor its failure to be an intrinsic cofibration is formulated. |
| **PATHS E.8** — Interval cotensors and incorrect exact fibres | claim (return: Proved); DSS:102; Part E; dual interval assertion | **none**; unpursued implication | Absent: there is no finite-interval cotensor construction or constant-section versus endpoint-fibre comparison. |
| **PATHS E.9** — Dependence of pullback preservation on W | claim (return: Refuted); DSS:103; GALOIS/STRATA localizer qualification; Part E | 117/021:53–64; unpursued implication | Hot 4 does not specify how “fibrant/cofibrant” changes with the localizer, so it supplies no universal preservation theorem across larger W and no counterexample (N31). |
| **PATHS E.10** — Marking components do not determine exit paths | claim (return: Refuted); DSS:104; STRATA proposed general stratified reading | **none**; unpursued implication | Absent: no stratification by components of the marked subcategory or exit-path identification is proposed. |
| **PATHS E.11** — Alternative strict bifibration over a monoid | claim (return: Open); DSS:105; STRATA E.11; VIc-C022 | **none**; unpursued implication | Absent: the unresolved rectangular-band bifibration replacement problem has no specified example or construction on these leaves. |
| **PATHS E.12** — Contractible fixed-origin paths need not be total | claim (return: Known); DSS:106; TOTASPH G.1-G.6; XIIba-C005 | 117/025; unpursued implication | The loop drawing does not identify a fixed-origin all-type path category or assert totality/filteredness; NR 10 is a separate implication (N40). |
| **PATHS E.13** — Finite tests fail to be faithful | claim (return: Refuted); DSS:107; VIIc-C004 faithfulness question; CATHOT F.2 verification | **none**; unpursued implication | Absent: neither a restricted-Yoneda faithfulness assertion nor the finitary symmetric-group shift occurs. |

### BISITE A

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **BISITE A.1** — Historical versus relative localizer axioms | claim (return: Proved); DSS:115; XVI ms.1--3 | 117/020:21–24; reading question | “Un localisateur fondamental” is used without an axiom list, so the pages cannot identify absolute Loc(3) with relative Loc(3 bis); this is the central limitation in Q03 and N28. |
| **BISITE A.2** — Intrinsic fibrations and closure | claim (return: Proved); DSS:116; XII ms.207--209; GALOIS D.1 | 116/010:7; 117/021:59–64; unpursued implication | “Fibrant” occurs, but no all-arrows-in-a-slice pullback test or composition/retract closure proof defines an intrinsic fibration class (N12, N31). |
| **BISITE A.3** — Coarse, universal and local relative classes | claim (return: Proved); DSS:117; XII ms.210,220; GALOIS A.5 | **none**; unpursued implication | Absent: no W_S, W_S^u and W_S^L family with its base-change quantifiers is defined. |
| **BISITE A.4** — Raw reindexing and postcomposition | claim (return: Proved); DSS:118; XII ms.226--227,248 | 117/016:13–25; unpursued implication | The distinction between weak-arrow preservation and commutation with Kan adjoints is explicit, but the fine slice classes and descended postcomposition construction of this row are absent (N25). |
| **BISITE A.5** — Universal saturation of test classes | claim (return: Proved); DSS:119; XII ms.222 | **none**; unpursued implication | Absent: no universal test-class closure, idempotence or largest-class characterization is formulated. |
| **BISITE A.6** — Transporter Galois connection | claim (return: Proved); DSS:120; II ms.83--89, (6.7) | **none**; unpursued implication | Absent: no pair of transporter operations T_W and K_W or antitone correspondence occurs. |
| **BISITE A.7** — Transporter composition criterion | claim (return: Proved); DSS:121; II Proposition 6.1, ms.88--89 | **none**; unpursued implication | Absent: the pages give no closed transporter pair or equivalence between composition closure and stabilization. |
| **BISITE A.8** — Noncomposing transporter on a chain | claim (return: Refuted); DSS:122; II first versions (6.2)--(6.5) | **none**; unpursued implication | Absent: there is no four-object chain with the indicated marked arrows or counterexample to transporter composition. |
| **BISITE A.9** — Smooth/proper stabilizers and the proposed inclusion | claim (return: Proved); DSS:123; II ms.66,89; XII ms.225--226 | 117/021:53–64; reading question | The source's “fibrant/cofibrant” base-change hypotheses are not defined by aspherical/coaspherical stabilizers, and no inclusion of their intersection in an intrinsic class is proposed (N31). |
| **BISITE A.10** — Three fibre-localization axioms | claim (return: Proved); DSS:124; XII ms.215--218; XIIc B055--B065 | **none**; unpursued implication | Absent: the three slice equivalences/equality assertions and their strong-saturation distinction are not stated. |
| **BISITE A.11** — Enough intrinsic fibrations and universal weakness | claim (return: Proved); DSS:125; XIII ms.10--11; XVI 4.4.1 | **none**; unpursued implication | Absent: no W-then-intrinsic factorization hypothesis or equality Fib_W∩W=W^u appears. |
| **BISITE A.12** — Functorial replacement of intermediate subcategories | claim (return: Proved); DSS:126; XII ms.217--218; XIIc B060--B065 | 117/018:6–27; unpursued implication | An adjunction criterion induces equivalences on diagram localizations, which is related in method, but the functorial-replacement/intermediate-subcategory theorem is not stated (N26). |
| **BISITE A.13** — Failure of fibre axioms (a)+(b)⇒(c) | claim (return: Refuted); DSS:127; XII ms.207,217--218; XIIc B062 | **none**; unpursued implication | Absent: no six-object lattice counterexample or enhanced version of the failed implication occurs. |
| **BISITE A.14** — Fine axiom systems and all-base variance | claim (return: Proved); DSS:128; XII ms.225--227 | **none**; unpursued implication | Absent: no pair of L/P-tested fine slice theories or equivalence from smooth/proper structural objects is constructed. |
| **BISITE A.15** — Four fibration classes and Loc(7) | claim (return: Proved); DSS:129; XVI ms.27--41; POLES A.5--A.6 | 117/020:21–24; reading question | The localizer example does not list Loc(7a–c/F), reference localizers or categorical-contractibility tests, so none can be inferred from the claim about f_! (N28). |
| **BISITE A.16** — Replacement transfer of fibration axioms | claim (return: Proved); DSS:130; XVI 4.4.1,4.4.9,4.4.10; POLES A.13--A.14 | **none**; unpursued implication | Absent: no A⇒B⇒C chain or transfer between two fibration classes with commuting replacements appears. |
| **BISITE A.17** — Brown's implication with terminal maps | claim (return: Proved); DSS:131; XVI 4.4.3; POLES A.13 | **none**; unpursued implication | Absent: no factorization/terminal-map hypotheses or equivalence of the three Brown conditions is given. |
| **BISITE A.18** — Constant-coefficient fibrations need not compose | claim (return: Refuted); DSS:132; I ms.117--118; GALOIS D.3 | 116/004:26–28; 116/006:8; unpursued implication | All-sheaf and locally constant coefficients are mentioned, but no universal weak rational fibration class or finite composition counterexample is present (N02, N07). |
| **BISITE A.19** — Local-coefficient repair | claim (return: Proved); DSS:133; I ms.79--81,117--123; GALOIS D.2; same-ID RS:455 | 116/004:26–28; 116/006:8; unpursued implication | The coefficient quantifiers are relevant precursors, but no universal strict-base-change direct-image hypothesis or asymmetric upstairs conclusion is proved (N02, N07; RS GALOIS D.2 and BISITE A.19). |
| **BISITE A.20** — Properness versus locally constant fibres | claim (return: Refuted); DSS:134; I ms.102; Ib-C003; GALOIS D.9; STRATA D.5 | **none**; unpursued implication | Absent: the endpoint inclusion with empty-to-point comma transition and the refuted local-constancy claim are not stated. |
| **BISITE A.21** — Products and one intrinsic pullback leg | claim (return: Proved); DSS:135; XII ms.241--248 | 116/010:3–17; 117/021:53–64; unpursued implication | There are fibre/comma and base-change proposals, but no localized fibrant-slice product theorem or one-intrinsic-leg replacement comparison (N12, N31). |
| **BISITE A.22** — Weak Quillen factorization axioms | claim (return: Proved); DSS:136; XIII ms.7--12,27--28; PATHS D.17 | 117/004:12–21; unpursued implication | Resolutions are part of the programme, but M2, M′, M″ and the resulting two intrinsic factorizations are not specified. |
| **BISITE A.23** — Lifting adjunctions on diagram structures | claim (return: Proved); DSS:137; XIII ms.45--50 | 117/016:13–25; unpursued implication | The author distinguishes preservation of weak arrows from preservation of Kan operations, but gives no objectwise lifting pairs, comma-initiality test or injective-fibrancy calculation (N25). |
| **BISITE A.24** — Ordinary Kan extensions may not descend | claim (return: Refuted); DSS:138; XIII ms.45--50 | 117/021:33–44; unproved claim | “Si pourtant” attempts to derive Lf_! from ordinary exactness, exposing precisely a missing descent justification; the coinvariant test in N30 is this return's diagnostic example, not manuscript content (N29). |
| **BISITE A.25** — Noetherian sober Alexandrov qualification | claim (return: Proved); DSS:139; XIII ms.60--67 | **none**; unpursued implication | Absent: no sobriety, noetherian condition or infinite-poset classification occurs. |
| **BISITE A.26** — Finite intrinsic axioms do not give all Kan extensions | claim (return: Refuted); DSS:140; XIII ms.50--59; PATHS D.9 | 117/010:17–18; 117/020:23–24; self-flagged | The source expressly reserves possible cofibrancy and finiteness restrictions, but supplies neither the finite-axiom theorem nor its counterexample (N23, N28). |
| **BISITE A.27** — Closed lifting pairs and trivial-class equalities | claim (return: Proved); DSS:141; XIII ms.27--29,57 | **none**; unpursued implication | Absent: no closedness argument identifying the designated trivial classes with C∩W and F∩W is written. |
| **BISITE A.28** — Uniform diagram theorem and admissibility | claim (return: Proved); DSS:142; XIII ms.57--72 | 117/014:24–37; 117/020:21–24; 117/021:4–44; unpursued implication | Localized diagrams and derived complexes are explicit examples, but their uniform model structures and the admissibility hypotheses needed for pointwise Kan formulas are not supplied (N21, N28–N29). |
| **BISITE A.29** — Polarity requires closure after joins | claim (return: Proved); DSS:143; II section 5, ms.69--80, especially (5.20) | **none**; unpursued implication | Absent: no join operation on transporter/stabilizer classes or double-closure correction occurs. |
| **BISITE A.30** — Unions need not preserve composition | claim (return: Refuted); DSS:144; II ms.65--67 | **none**; unpursued implication | Absent: no union-of-arrow-classes argument or composition counterexample is given; union of indexing subcategories in Hot 7 is a different construction. |
| **BISITE A.31** — The bi-site remark is a question | claim (return: Proved); DSS:145; VI ms.81--84; XII ms.222--225 | **none**; unpursued implication | Absent: no bi-site definition or unresolved site-like axiom package is written in this folder. |
| **BISITE A.32** — Absolute axioms do not imply relative Theorem A | claim (return: Refuted); DSS:146; XVI Loc (1,2,3)/(3 bis); POLES A.16 | 117/020:21–24; 117/022:3–45; reading question | Neither the claimed existence of f_! nor the adjoint cofinality argument identifies which localizer axioms are assumed, and no counterexample or proof of the relative implication appears (Q03). |
| **BISITE A.33** — Converse cocartesianness needs conservativity | claim (return: Refuted); DSS:147; XII ms.273--275; POLES G.17--G.18 | 117/023:3–22; unpursued implication | Hot 7 concerns surjectivity on Hom sets across a union, not reflection of cocartesian squares or a conservative-functor criterion (N38). |
| **BISITE A.34** — Stabilizers versus cancelled antitone correspondence | claim (return: Refuted); DSS:148; II cancelled section 4, ms.65--68 | **none**; unpursued implication | Absent: the cancelled integration draft is unrelated to the cancelled transporter correspondence discussed by this row (N22). |

### BISITE B

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **BISITE B.1** — Comma-test variance | claim (return: Proved); DSS:149; VI ms.81--84; XII ms.222 | 116/010:8–17; unpursued implication | The loose comma/fibre comparison gives related notation, but no definition of two fine equivalence classes by under- and over-comma tests (N12). |
| **BISITE B.2** — Simplicial slice test and base hypothesis | claim (return: Known); DSS:150; Lead 1; VI ms.81--84 | **none**; unpursued implication | Absent: no simplicial slice recognition statement or condition on its base appears. |
| **BISITE B.3** — Enhanced nerve comparison | claim (return: Proved); DSS:151; Lead 1; VI ms.81--84 | **none**; unpursued implication | Absent: the scans do not compare enhanced category and simplicial slice localizations through the nerve. |
| **BISITE B.4** — Failure of the all-simplicial-base recipe | claim (return: Refuted); DSS:152; Lead 1 | **none**; unpursued implication | Absent: no literal slice recipe over arbitrary simplicial bases or counterexample to it is proposed. |
| **BISITE B.5** — Dictionary for smoothness and properness | claim (return: Known); DSS:153; I ms.54; XII ms.224--225 | 116/010:3–17; 117/021:53–64; unpursued implication | The proposed base-change statements are related, but no exact comma-test/smoothness/properness dictionary is given (N12, N31). |
| **BISITE B.6** — Maximal localization class | claim (return: Proved); DSS:154; XII ms.222; II ms.66 and 88--89 | **none**; unpursued implication | Absent: no largest arrow class presenting a fine localization is identified for every fundamental localizer. |
| **BISITE B.7** — Three minimal-localizer fibration classes | claim (return: Proved); DSS:155; XII ms.225--226; STRATA D.5--D.6 | **none**; unpursued implication | Absent: the source does not distinguish intrinsic, Grothendieck and smooth/proper fibration classes at W∞. |
| **BISITE B.8** — Smooth proper path resolution | claim (return: Proved); DSS:156; VII ms.161--169; PATHS E.9 | 117/025; unpursued implication | The loop staircase is not a path-resolution construction and supplies no smoothness/properness verification (N40). |
| **BISITE B.9** — Threshold for complementarity | claim (return: Proved); DSS:157; XII ms.225--226; POLES E.5; STRATA G.5 | **none**; unpursued implication | Absent: no localizer interval or equivalence characterizing complementarity is stated. |
| **BISITE B.10** — Finite truncation localizers fail complementarity | claim (return: Refuted); DSS:158; XII ms.225--226; POLES C.8--C.9; STRATA G.3--G.4 | 117/004:39–40; unpursued implication | Truncation is listed as a poorly understood operation, but no W_n complementarity assertion or counterexample occurs (N18). |
| **BISITE B.11** — Covering obstruction for homology theories | claim (return: Refuted); DSS:159; XII ms.225--226; POLES C.10; PATHS E.9 | **none**; unpursued implication | Absent: no covering tests complementarity for all nonzero spectra or homology theories. |
| **BISITE B.12** — Finite bifibration obstruction | claim (return: Proved); DSS:160; GALOIS D.4--D.5; XII ms.225--226 | **none**; unpursued implication | Absent: there is no finite bifibration comparing W₁ with rational local-system equivalences. |
| **BISITE B.13** — Local-coefficient behaviour of covering witnesses | claim (return: Proved); DSS:161; GALOIS D.3; POLES C.10; PATHS E.9 | **none**; unpursued implication | Absent: no covering witness is tested against distinct local-coefficient classes. |
| **BISITE B.14** — Cohomological fibrations versus proper maps | claim (return: Refuted); DSS:162; I ms.117--118; GALOIS D.2 and D.9 | 116/004:26–28; 117/021:53–64; unpursued implication | Cohomology and proposed base change occur, but no identification of cohomological fibrations with proper maps is asserted or refuted (N02, N31). |
| **BISITE B.15** — Finite coefficient example table | claim (return: Proved); DSS:163; GALOIS D.3--D.5; I ms.117--123 | **none**; unpursued implication | Absent: the inherited finite coefficient maps and their smooth/proper/intrinsic table are not present. |
| **BISITE B.16** — Accessibility of coefficient localizations | claim (return: Proved); DSS:164; VI ms.81--84; XII ms.222--226 | 117/020:21–24; unpursued implication | The Cat/localizer example gives no accessibility theorem for coefficient localizers; its explicit missing f_* prevents reading it as the full general assertion (N28). |
| **BISITE B.17** — Intrinsic fibrations for W_n | claim (return: Known); DSS:165; POLES C.8--C.9; STRATA G.4 | **none**; unpursued implication | Absent: no truncation-localizer intrinsic-fibration criterion is formulated. |
| **BISITE B.18** — Bounds on a homology intrinsic class | claim (return: Proved); DSS:166; POLES C.10; XII ms.225--226 | **none**; unpursued implication | Absent: no inclusions bounding a homology intrinsic-fibration class are given. |
| **BISITE B.19** — Fence construction and path factorization | claim (return: Proved); DSS:167; VII ms.161--169; PATHS E.4--E.5 | 117/003; 117/025; unpursued implication | Path-like drawings occur, but no full fence category or functorial mapping-path factorization is defined (N16, N40). |
| **BISITE B.20** — Word reversal does not repair endpoint maps | claim (return: Refuted); DSS:168; VII ms.161--166; PATHS E.3 | **none**; unpursued implication | Absent: no reversal of path words or endpoint-functor counterexample is discussed. |
| **BISITE B.21** — Bifibration replacement problem | claim (return: Open); DSS:169; STRATA E.11; PATHS E.6 and E.11; same-ID RS:428 | **none**; unpursued implication | Absent: no replacement of a smooth/proper representative by a strict bifibration is proposed, so the selected RS BISITE B.21 open entry receives no construction. |
| **BISITE B.22** — Maximal simplicial classes on all bases | claim (return: Proved); DSS:170; Lead 1; XII ms.222--226; same-ID RS:456 | **none**; unpursued implication | Absent: the corrected all-base simplicial recipe and maximal pullback-preserving classes are not supplied; RS BISITE B.22 remains contextual only. |

### BISITE C

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **BISITE C.1** — Presheaf models before a choice of direction | claim (return: Proved); DSS:171; VI ms.83; XII ms.224--225; same-ID RS:447 | 117/008:15–45; 117/022:36–45; unpursued implication | Presheaf categories enter a cancelled integration scheme and later a proof sketch, but no model structure or direction-independent pullback-preservation theorem is constructed (N22, N35; RS BISITE C.1). |
| **BISITE C.2** — Two element-category candidates need not be dual | claim (return: Refuted); DSS:172; XII ms.224--225; Part C | 116/008:5–13; unpursued implication | A bifunctor for presheaf gluing is written, but no pair of category-of-elements candidates or failed test-category duality is given (N10–N11). |
| **BISITE C.3** — No general smooth/proper exchange involution | claim (return: Refuted); DSS:173; XII ms.224--225; Part C; same-ID RS:457 | 117/012:16–29; unpursued implication | Pointwise opposition swaps the proposed adjoints, but no elementwise smooth/proper exchange involution on a test category is asserted (N24; RS BISITE C.3). |
| **BISITE C.4** — Extra data transporting a duality | claim (return: Proved); DSS:174; VI ms.84; XII ms.224--225 | 117/012:16–29; unpursued implication | The formal opposite theory is related, but no specified anti-equivalence of a test category or comparison of element functors is supplied (N24). |
| **BISITE C.5** — Theorem A for strict higher slices | claim (return: Known); DSS:175; Recent-results family 317; Part C | **none**; unpursued implication | Absent: strict higher categories and their required lax/oplax slice Theorem A are not formulated. |
| **BISITE C.6** — Two strict higher fine theories | claim (return: Proved); DSS:176; Recent-results family 317; XII ms.224--225 | **none**; unpursued implication | Absent: no Street-equivalence fine classes or higher categorical duality are defined. |
| **BISITE C.7** — Cellwise opposites in strict dimension n | claim (return: Proved); DSS:177; Recent-results family 317; Part C | 117/012:16–29; unpursued implication | Opposition of the value category is written, but no separate choices of cell reversal in strict n-categories occur (N24). |
| **BISITE C.8** — Absolute model structure in dimension two | claim (return: Known); DSS:178; Recent-results family 317 | **none**; unpursued implication | Absent: no strict 2-category model structure or Thomason-type absolute theorem is stated. |
| **BISITE C.9** — Coarse consequence of a higher model theorem | claim (return: Proved); DSS:179; VI ms.83; Recent-results family 317 | **none**; unpursued implication | Absent: no higher slice localization is deduced from an absolute model structure. |
| **BISITE C.10** — Higher fine recognition and base change | claim (return: Open); DSS:180; Recent-results family 317; Parts C and E; same-ID RS:441 | 117/006:16–23; 117/021:53–64; unpursued implication | Two-functor variance and ordinary-category base change are proposed, but no indexing by strict higher bases or lax-comma recognition addresses RS BISITE C.10 (N20, N31). |

### BISITE E

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **BISITE E.1** — Formal slice construction | claim (return: Proved); DSS:181; XII ms.207–208, 216–218, 226 | 117/016:13–25; unpursued implication | The functoriality of localized diagram pairs is a related formal operation, but no L-tested fine slice construction is defined (N25). |
| **BISITE E.2** — Arbitrary raw pullback is not automatic | claim (return: Refuted); DSS:182; XII ms.226; Lead 3 | 117/016:13–25; unpursued implication | The author cautions that induced transformations need not commute with Kan operations, but no explicit failed raw-pullback example for fine slice classes is given (N25). |
| **BISITE E.3** — Recognition giving three Kan operations | claim (return: Proved); DSS:183; VI ms.108–113; XII ms.225–227 | 117/010–012; 117/020:21–24; unproved claim | All three operations are part of the proposed theory, but the fine-localization recognition hypothesis needed by this row is not proved and f_* remains unestablished in the Cat example (N23, N28). |
| **BISITE E.4** — Coefficient localization and exact squares | claim (return: Proved); DSS:184; VI ms.138–169; XII ms.226 | 117/014:24–37; 117/021:53–67; unpursued implication | The localization example and Hot 4 occur separately; no enhanced coefficient-localization theorem transports exact squares (N21, N31). |
| **BISITE E.5** — Instances and the coarse comparison | claim (return: Proved); DSS:185; VI ms.81–84, 108–113 | 117/020:21–24; 117/021:4–44; unpursued implication | Cat and complexes are explicit models, but no fine/coarse slice recognition theorem or extra comparison condition is stated (N28–N29). |
| **BISITE E.6** — Coarse versus locally constant fine theories | claim (return: Refuted); DSS:186; VI ms.108–113; arbitrary-W lead | **none**; unpursued implication | Absent: the locally constant sheaf paragraph does not identify a coarse relative homotopy theory with a locally constant fine one, or refute such an identification. |
| **BISITE E.7** — Consequences of enough intrinsic fibrations | claim (return: Proved); DSS:187; XII ms.240–261; XIII ms.7–12; PATHS D.8,D.17,D.18 | **none**; unpursued implication | Absent: no intrinsic-fibration replacement calculus is assumed or proved for all bases. |
| **BISITE E.8** — Accessible localizers with intrinsic factorization | claim (return: Known); DSS:188; XVI Loc (7 F); POLES E.2–E.3 | **none**; unpursued implication | Absent: no nullification or modality characterization of Loc(7F) appears. |
| **BISITE E.9** — Exact requirements on a path object | claim (return: Proved); DSS:189; XVI Loc (7 F); PATHS E.5 | 116/004:30–37; 117/004:7–10; unpursued implication | The cylinder/retraction and the cylinder programme are related motivation, but the universally weak source-evaluation hypothesis for mapping-path factorization is not stated (N03). |
| **BISITE E.10** — Groupoid base and collapse of the fine theories | claim (return: Proved); DSS:190; VI ms.83–84; OpenAI family 312 lead | **none**; unpursued implication | Absent: no groupoid-base test or identification with families of 1-types occurs. |
| **BISITE E.11** — Intermediate localization with replacement data | claim (return: Proved); DSS:191; XII ms.217–218; XIIc B062 | 117/018:6–27; unpursued implication | The localized adjunction criterion supplies a different equivalence mechanism, not the intrinsic slice replacements and all-intermediate-subcategory assertion of this row (N26). |
| **BISITE E.12** — Six-object failure of the third fibre axiom | claim (return: Refuted); DSS:192; XII ms.217–218; XIIc B062 | **none**; unpursued implication | Absent: no six-object lattice or strengthened-localization counterexample is given. |
| **BISITE E.13** — Ordinary homotopy categories lose coherent gluing | claim (return: Refuted); DSS:193; PATHS D.20; STRATA C.7 | 116/007–008; 117/023:3–22; unpursued implication | Presheaf gluing and the tentative Hom-surjectivity axiom are close topics, but neither identifies coherent gluing with a pullback of homotopy categories; the caution motivates N39 (N10, N38). |
| **BISITE E.14** — Nullification, modality and local Cartesian closure | claim (return: Proved); DSS:194; POLES E.2–E.3 modality/LCC comparison | **none**; unpursued implication | Absent: there is no accessible reflective localization of spaces or equivalence of its modality/LCC conditions. |

### BISITE F

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **BISITE F.1** — Der 1–4 and the three Kan operations | claim (return: Known); DSS:195; I; VI ms.138–169 | 117/006–012; 117/021:53–80; unproved claim | Several constituent axioms are directly proposed, including products, Kan adjoints and base change, but joint conservativity and the full comma formulas are not supplied; “2-contravariante” also requires a variance convention (Q04, N20–N23). |
| **BISITE F.2** — Two strict base-change theorems | claim (return: Proved); DSS:196; VI ms.138–169; STRATA D.4 | 117/021:53–64; unproved claim | Hot 4 is the clearest early form, with the two comparisons and the bracketed “ou g … ??” alternatives, but no proof or universal converse and no definition of the fibrancy terminology (N31). |
| **BISITE F.3** — Failure of unrestricted base change | claim (return: Refuted); DSS:197; Lead 3 | 117/021:59–64; unpursued implication | The manuscript already writes hypotheses on the comparisons, so it does not assert unrestricted strict-pullback exactness; the endpoint and stable counterexamples are absent (N31). |
| **BISITE F.4** — Projection formula under smoothness | claim (return: Proved); DSS:198; Lead 3; VI projection formulas | 117/002:23–28; 117/005:25–30; unpursued implication | Internal Hom and tensor adjunctions motivate the projection-formula question, but no separately cocontinuous monoidal structure, smoothness condition or projection isomorphism is stated (N14, N19). |
| **BISITE F.5** — Monoidality is insufficient for all maps | claim (return: Refuted); DSS:199; Lead 3 | 117/005:25–30; unpursued implication | A tensor-Hom relation is written, but no unqualified all-map projection formula is asserted or counterexample supplied (N19). |
| **BISITE F.6** — Restricted right projection formula | claim (return: Proved); DSS:200; Lead 3 | 117/012:4–14; 117/005:25–30; unpursued implication | Cointegration and tensor are discussed, but dualizable coefficients and homotopy-finite fibre conditions for right projection are absent (N19, N23). |
| **BISITE F.7** — Internal-Hom exchange and mates | claim (return: Proved); DSS:201; VI exchange formulas | 117/002:23–41; 117/021:66–67; unproved claim | The higher/internal Hom adjunction displays and the word “transposées” are direct antecedents, but no closed monoidal hypotheses or coherent mate proof validates all the modern exchange identities (N14–N15, N32). |
| **BISITE F.8** — Opposition of base and coefficients | claim (return: Proved); DSS:202; VI ms.84 | 117/012:16–29; reading question | The source defines H°(A)=H(A)° and swaps adjoints; the modern operation additionally opposes the base, so the two formulas are related but not literally identical (N24). |
| **BISITE F.9** — Open/closed Kan extensions and recollement | claim (return: Known); DSS:203; I; VI open–closed formulas | 116/004–008; 117/021:70–80; unpursued implication | Topos gluing, relative cohomology and fully faithful Kan adjoints supply substantial precursors, but pointed/stable support-image and recollement hypotheses are absent (N01, N05, N33). |
| **BISITE F.10** — Enhanced correspondence formalism | claim (return: Proved); DSS:204; Lead 3; Mann correspondence question | 117/021:53–67; unpursued implication | Proposed base change and formal transposition do not construct a correspondence category or its coherent enhanced functor (N32, N42). |
| **BISITE F.11** — Terminology of the Kan operations | claim (return: Proved); DSS:205; Lead 3 terminology | 117/010–012; reading question | The source calls the operations integration and cointegration and does not construct extraordinary functors, so geometric six-operation terminology cannot be assigned merely from the three adjoints (N23, N42–N43). |
| **BISITE F.12** — Smooth maps are not diagonal-closed | claim (return: Refuted); DSS:206; Mann versus later geometric-setup conventions | **none**; unpursued implication | Absent: no diagonal-stability requirement or counterexample for the class of all smooth functors occurs. |
| **BISITE F.13** — Diagram correspondences and enhancement boundary | claim (return: Known); DSS:207; Hörmann comparison | 117/021:53–67; unpursued implication | The finite list of formal properties does not provide Hörmann's correspondence construction or the enhancement needed for its coherence (N32, N42). |
| **BISITE F.14** — Comparison with relative smoothness/properness | claim (return: Proved); DSS:208; Anel–Weinberger comparison | 117/021:53–64; unpursued implication | Hot 4 gives a base-change proposal, but no comparison between categorical smooth/proper maps and a separate relative six-operation notion is proved (N31, N43). |
| **BISITE F.15** — Genus-zero strata and geometric coefficients | claim (return: Known); DSS:209; STRATA genus-zero comparison | **none**; unpursued implication | Absent: no genus-zero moduli category, stable tree or constructible coefficient dictionary is present. |
| **BISITE F.16** — Forgetting a marked point | claim (return: Proved); DSS:210; STRATA forgetting-mark question | **none**; unpursued implication | Absent: no forgetful map of marked genus-zero curves or proof of properness without smoothness occurs. |
| **BISITE F.17** — Geometric direct image in the moduli example | claim (return: Proved); DSS:211; STRATA geometric direct image and boundary base change | **none**; unpursued implication | Absent: no boundary square or geometric direct-image calculation for the marked-curve example appears. |
| **BISITE F.18** — Extending indexing to strict higher categories | claim (return: Open); DSS:212; Strict nCat-indexing question; same-ID RS:429 | 117/006:16–23; unpursued implication | “2-contravariante” describes variance on ordinary categories; it does not extend an abstract derivator's indexing domain to strict higher categories or answer RS BISITE F.18 (N20). |
| **BISITE F.19** — Proper class in a diagonal-closed setup | claim (return: Proved); DSS:213; Mann proper-class question | **none**; unpursued implication | Absent: there is no universal-ambidexterity or finite-discrete-bifibration classification (N43 gives only broader context). |

### BISITE G

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **BISITE G.1** — Stability and the tensor action | claim (return: Known); DSS:214; Lead 4 stable-derivator input | 117/005:3–6,25–30; 117/012:31–33; unpursued implication | Additivity, triangles and tensor are desiderata or examples, but no stable strong hypothesis or finite-spectral tensor action is established (N18–N19). |
| **BISITE G.2** — Canonical dualizing weight | claim (return: Proved); DSS:215; Lead 4 dualizing-object and limit-colimit clause | **none**; unpursued implication | Absent: no dualizing profunctor/weight or its variance is constructed. |
| **BISITE G.3** — Failure of a pointwise dualizing twist | claim (return: Refuted); DSS:216; Lead 4 exaggerated objectwise interpretation | **none**; unpursued implication | Absent: no one-arrow counterexample tests replacing a dualizing kernel by pointwise tensoring. |
| **BISITE G.4** — Kernel transitivity and base change | claim (return: Proved); DSS:217; Part G compatibility and transitivity | 117/021:53–67; unpursued implication | Formal base-change transposition is present, but no dualizing kernel or convolution transitivity makes this a statement about weights (N32). |
| **BISITE G.5** — Failure under unrestricted restriction | claim (return: Refuted); DSS:218; Part G unrestricted dualizing-weight base change | **none**; unpursued implication | Absent: there is no canonical weight whose behaviour under restriction is asserted or tested. |
| **BISITE G.6** — Duality on specified finite coefficients | claim (return: Proved); DSS:219; Part G suitable finiteness subcategories | 117/012:16–33; unpursued implication | Opposing the value categories is a formal construction, not an internal coefficient duality on a finite subcategory (N24). |
| **BISITE G.7** — Finite EI does not suffice uniformly | claim (return: Refuted); DSS:220; Part G finite EI scope | **none**; unpursued implication | Absent: no finite EI category or coefficient-dependent failure of homotopy-finite duality is discussed. |
| **BISITE G.8** — Finite-group duality with coefficient conditions | claim (return: Proved); DSS:221; Part G coefficient-sensitive finite EI class | **none**; unpursued implication | Absent: no finite-group duality theorem or invertibility condition on the group order is given; the related caution is in supplied Pursuing Stacks §137, not these scans (N43). |
| **BISITE G.9** — Canonical equivalence criterion for finite posets | claim (return: Known); DSS:222; Lead 4 corrected equivalence; Part G finite posets | **none**; unpursued implication | Absent: no canonical finite-poset duality functor or criterion for its equivalence appears. |
| **BISITE G.10** — Least-vertex geometric dictionary | claim (return: Proved); DSS:223; STRATA A.4 A.5; Part G prerequisite dictionary; same-ID RS:459 | **none**; unpursued implication | Absent: no barycentric least-vertex realization or geometric coefficient dictionary addresses the selected RS BISITE G.10 entry. |
| **BISITE G.11** — Minimum constructibility and Verdier duality | claim (return: Refuted); DSS:224; Lead 4 unconditional geometric identification | **none**; unpursued implication | Absent: no minimum-constructible sheaf category or failure of preservation by Verdier duality occurs. |
| **BISITE G.12** — Geometric Verdier identification | claim (return: Known); DSS:225; Part G positive geometric identification | **none**; unpursued implication | Absent: there is no geometric realization of a dualizing weight or checked constructibility hypothesis. |
| **BISITE G.13** — Failure of the unstable weighted-limit argument | claim (return: Refuted); DSS:226; Part G unstable clause | 117/012:16–29; unpursued implication | Formal opposite-category notation gives no weighted-limit duality, so the unstable obstruction is not addressed (N24). |
| **BISITE G.14** — Additional tilting equivalences | claim (return: Known); DSS:227; Lead 4 Groth-Stovicek contribution | **none**; unpursued implication | Absent: no tilting object or alternative finite-poset equivalence is constructed. |

### RESIDUE B

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **RESIDUE B.1** — Component-dependent absolute localizer | claim (return: Proved); DSS:235; XVI ms.1–3 | **none**; unpursued implication | Absent: no W† varying with the number of components is defined or used to separate absolute and relative Theorem A (Q03). |
| **RESIDUE B.2** — Quotient through S¹ | claim (return: Proved); DSS:236; (no manuscript locator supplied) | **none**; unpursued implication | Absent: no quotient of the homotopy category by maps factoring through S¹ or classification of its invertible maps occurs. |
| **RESIDUE B.3** — Strong saturation does not repair absolute Theorem A | claim (return: Refuted); DSS:237; XVI ms.1–3, Loc(1bis)/(1ter)+absolute Loc(3) | **none**; unpursued implication | Absent: no W_circ or rational degree condition is written; the undefined localizer terminology cannot silently import the relative theorem (Q03). |
| **RESIDUE B.4** — Finite failure certificate for relative Theorem A | claim (return: Proved); DSS:238; (no manuscript locator supplied) | **none**; unpursued implication | Absent: no 10-object/6-object/3-object poset diagram or multiplication-by-two obstruction is given. |
| **RESIDUE B.5** — Homotopy invariance and adjunctions | claim (return: Known); DSS:239; XVI Rappel1.2, ms.3 | 117/018:6–27; 117/022:8–45; unpursued implication | Adjunctions provide equivalences or integration invariance in two arguments, but no proof from literal localizer axioms of natural-homotopy invariance is supplied (N26, N35–N36). |
| **RESIDUE B.6** — Opposition under absolute axioms | claim (return: Known); DSS:240; XVI Rappel1, ms.2 | 117/012:16–29; unpursued implication | The formal opposite theory does not state that an arbitrary literal localizer is invariant under category opposition (N24). |
| **RESIDUE B.7** — Weak and strong versions of XVI Proposition 1.3 | claim (return: Proved); DSS:241; XVI Proposition1.3, ms.3–8 | **none**; unpursued implication | Absent: the two propositions and their different Theorem A requirements are not formulated; Q03 preserves rather than collapses that distinction. |
| **RESIDUE B.8** — Products need relative hypotheses | claim (return: Refuted); DSS:242; XVI Rappel2.3 and Proposition2.4, ms.9–10 | 117/014:35–37; unpursued implication | The source warns about localization and infinite products, but no counterexample to finite products of weak arrows under absolute axioms occurs (N21). |
| **RESIDUE B.9** — Weak versus modern fundamental localizers | claim (return: Known); DSS:243; (no manuscript locator supplied) | 117/020:21–24; reading question | “Localisateur fondamental” carries no defining clauses here, so it cannot decide which later literature convention is intended (Q03, N28). |
| **RESIDUE B.10** — Unfinished historical axiom audit | claim (return: Open); DSS:244; (no manuscript locator supplied) | 117/020–023; unpursued implication | These pages provide early proposals to compare, but contain neither the later XVI/XV axiom system nor its full Mayer–Vietoris implications, and therefore do not complete the registered audit (Q01, Q03). |
| **RESIDUE B.11** — Finite sums and filtered colimits do not give full decomposition | claim (return: Refuted); DSS:245; XVI ms.9, Corollary2.2 parenthesis | **none**; unpursued implication | Absent: no deduction of a full decomposition axiom from finite sums and filtered colimits is stated. |
| **RESIDUE B.12** — Finite localization and formal decomposition | claim (return: Proved); DSS:246; XVI2.1,2.2 principal clause,2.5 finite intended version,2.6; XV9.4 formal equivalences,9.5,9.6 | 117/008:9–10; 117/014:35–37; unpursued implication | Hot 1 and the finite-index qualification give a related localization/product issue, but no separate formal decomposition proof or XV/XVI equivalence is written (N21). |
| **RESIDUE B.13** — Discrete-set adjunctions | claim (return: Known); DSS:247; XVI second2.8,second2.9,2.11–2.14 | 117/002:16; 117/005:17–20; unpursued implication | π₀ and a Set-valued functor occur, but no claim makes π₀ both adjoints to the discrete-set functor for all small sets (N14, N19). |
| **RESIDUE B.14** — Formal cube implications | claim (return: Proved); DSS:248; XVI3.1, ms.18′ | 117/023:3–22; unpursued implication | Hot 7 is a Hom-surjectivity requirement, not any of the formal cube implications among localizer axioms (Q01, N38). |
| **RESIDUE B.15** — Arbitrary-arrow localization wording | claim (return: Refuted); DSS:249; XVI2.5 arbitrary-W literal wording | 117/014:24–37; unpursued implication | The finite-product caveat is relevant, but no theorem for a literally arbitrary class of arrows or missing-identity counterexample is presented (N21). |
| **RESIDUE B.16** — Near-bijective infinite component maps | claim (return: Proved); DSS:250; XVI/XV literal absolute package | **none**; unpursued implication | Absent: no near-bijection of component sets or W_nb weak localizer occurs. |
| **RESIDUE B.17** — Nontriviality equivalences under absolute axioms | claim (return: Refuted); DSS:251; XVI2.7; XV9.9,9.10,9.12,9.13 | **none**; unpursued implication | Absent: no list of nontriviality criteria or repair by relative Loc(3 bis) is given. |

### RESIDUE C

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **RESIDUE C.1** — Universal weakness from intrinsic factorization | claim (return: Proved); DSS:252; (no manuscript locator supplied) | **none**; unpursued implication | Absent: neither intrinsic-factorization hypotheses nor the equality W∩Fib_W=W^u are stated. |
| **RESIDUE C.2** — All intermediate localizations without functorial replacement | claim (return: Proved); DSS:253; XII ms.215–218,240; XIIc B062 with factorization | 117/018:6–27; unpursued implication | The adjunction criterion is a different equivalence argument and does not prove the all-intermediate-subcategory theorem from nonfunctorial intrinsic factorizations (N26). |
| **RESIDUE C.3** — Five-object fibre-axiom counterexample | claim (return: Refuted); DSS:254; XII ms.215–218; XIIc B062 without factorization | **none**; unpursued implication | Absent: no five-object, sixteen-arrow example separates the fibre axioms or improves a minimality bound. |
| **RESIDUE C.4** — Object bounds do not bound category searches | claim (return: Proved); DSS:255; (no manuscript locator supplied) | **none**; unpursued implication | Absent: no exhaustive finite-category search, arrow bound or one-object pullback classification is discussed. |
| **RESIDUE C.5** — Strictly functorial perfect path replacement | claim (return: Proved); DSS:256; (no manuscript locator supplied) | 117/025; unpursued implication | The loop sequence does not define a coaugmented slice replacement R_S or verify smooth/proper values (N40). |
| **RESIDUE C.6** — Intermediate perfect subcategories | claim (return: Proved); DSS:257; XII ms.217, F_0,S | **none**; unpursued implication | Absent: no equivalence of intermediate smooth/proper slice localizations, ordinary or enhanced, is stated. |
| **RESIDUE C.7** — Derived reindexing from intrinsic factorization | claim (return: Proved); DSS:258; XII ms.240–241, footnotes128–130 | 117/021:53–67; unpursued implication | Hot 4 proposes base change, but no intrinsic-slice construction proves derived reindexing or the two relative homotopy-fibre identities (N31–N32). |
| **RESIDUE C.8** — Minimum size of a fibre-axiom counterexample | claim (return: Open); DSS:259; (no manuscript locator supplied) | **none**; unpursued implication | Absent: no object/arrow minimization problem or example addresses this open finite-category classification. |

### RESIDUE D

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **RESIDUE D.1** — Proper-localizer criterion | claim (return: Known); DSS:260; XII ms.208,225; XVI §4; I ms.99–100 | 117/020:21–24; 117/021:53–64; unpursued implication | The localizer example and base-change proposals do not state a proper-localizer recognition criterion or its local version (N28, N31). |
| **RESIDUE D.2** — Intrinsic tests with homotopy-pullback fibres | claim (return: Proved); DSS:261; XII ms.208,225; XVI §4; I ms.99–100 | **none**; unpursued implication | Absent: no long-exact-homotopy-sequence boundary criterion for intrinsic fibrations is derived. |
| **RESIDUE D.3** — Complete W₀ criterion | claim (return: Proved); DSS:262; XII ms.208,225; XVI §4; I ms.99–100 | **none**; unpursued implication | Absent: no componentwise strict-fibre bijection and arrow-lifting criterion is given for Fib_W₀. |
| **RESIDUE D.4** — Intrinsic fibrations need not form a lifting class | claim (return: Refuted); DSS:263; XII ms.208,225; XVI §4; I ms.99–100 | **none**; unpursued implication | Absent: no right-lifting-property representation of Fib_W is proposed or refuted. |
| **RESIDUE D.5** — Local-coefficient equivalence tests | claim (return: Known); DSS:264; XII ms.208,225; XVI §4; I ms.99–100 | 116/004:26–28; 116/006:8; 117/021:4–23; unpursued implication | General sheaf, locally constant and module coefficients occur, but no π₀/π₁/universal-cover classification or W₁/W₂ identification is stated (N02, N07, N29). |
| **RESIDUE D.6** — Rational coefficients and the degree-two boundary | claim (return: Proved); DSS:265; XII ms.208,225; XVI §4; I ms.99–100 | **none**; unpursued implication | Absent: no rational local-coefficient fibration test isolates the π₂-to-π₁ boundary. |
| **RESIDUE D.7** — Remaining rational and mod-p classification | claim (return: Open); DSS:266; (no manuscript locator supplied) | **none**; unpursued implication | Absent: the notes give no arbitrary-functor fibre criterion or mod-p boundary theorem to resolve the selected open problem. |
| **RESIDUE D.8** — Nontrivial intrinsic mod-p covering | claim (return: Refuted); DSS:267; XII ms.208,225; XVI §4; I ms.99–100 | **none**; unpursued implication | Absent: no EC_p→BC_p covering or finite-p-group monodromy argument is written. |
| **RESIDUE D.9** — General homology-fibration classification | claim (return: Open); DSS:268; (no manuscript locator supplied); same-ID RS:439 | **none**; unpursued implication | Absent: no classification for arbitrary spectra, coverings or smooth/proper maps advances the selected RS RESIDUE D.9 open entry. |
| **RESIDUE D.10** — Finite example table unchanged | claim (return: Proved); DSS:269; XII ms.208,225; XVI §4; I ms.99–100; BISITE B.15 (all 48 entries) | **none**; unpursued implication | Absent: none of the eight named finite maps or their coefficient-dependent table entries is supplied. |
| **RESIDUE D.11** — Fibration-axiom table by localizer | claim (return: Proved); DSS:270; XII ms.208,225; XVI §4; I ms.99–100 | **none**; unpursued implication | Absent: no W₀/W₁/W_n/rational/W∞ comparison of Loc(7a–c/F) or intrinsic intersections is tabulated or asserted. |
| **RESIDUE D.12** — Integral/rational coverings and trivial monodromy | claim (return: Proved); DSS:271; XII ms.208,225; XVI §4; I ms.99–100 | **none**; unpursued implication | Absent: no classification of intrinsic categorical coverings by trivial monodromy appears. |

### RESIDUE F

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **RESIDUE F.1** — Totality via covariant actions | claim (return: Proved); DSS:272; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases) | 116/003:46; 117/022:27–28; unpursued implication | The source has neither the universal final-image definition nor the all-covariant-actions criterion, so its shorthand and filtered margin cannot state this equivalence (Q02). |
| **RESIDUE F.2** — Common successors and affine equalization | claim (return: Proved); DSS:273; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases) | **none**; unpursued implication | Absent: no totality argument produces common successors or an augmentation-one integral combination equalizing a parallel pair. |
| **RESIDUE F.3** — Injection and free-category examples | claim (return: Proved); DSS:274; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases); same-ID RS:473 | **none**; unpursued implication | Absent: Δ_inj subcategories, finite-set injections, injective self-maps and free directed-graph categories are not tested here (Q02; RS RESIDUE F.3). |
| **RESIDUE F.4** — Weakly terminal total categories are filtered | claim (return: Proved); DSS:275; XII ms.88; TOTASPH D.7; PATHS A.8 (specified special cases) | 117/022:30–34; unpursued implication | The example evaluates an integral at a terminal object, which is different from deducing filteredness from totality and a weakly terminal object (N35–N37). |
| **RESIDUE F.5** — Totality implies exact abelian colimits? | claim (return: Open); DSS:276; (no manuscript locator supplied); same-ID RS:421 | 117/022:27–28; unpursued implication | “Cas des catégories filtrantes ??” gives no affine-category equalization argument and does not resolve this exactness converse (N37; RS TOTASPH D.7 and RESIDUE F.5). |
| **RESIDUE F.6** — Total presheaves and dwyerienne composition | claim (return: Open); DSS:277; (no manuscript locator supplied); same-ID RS:422 | 116/007–008; 117/023:3–22; unpursued implication | Presheaf gluing and full sieve covers are present, but no restricted-action totality condition or composition of dwyerienne sieves is formulated (N10, N38; RS TOTASPH F.27 and RESIDUE F.6). |
| **RESIDUE F.7** — Universally correct Cat-colimits imply filteredness? | claim (return: Open); DSS:278; (no manuscript locator supplied); same-ID RS:425 | 117/022:27–28; unpursued implication | The filtered cofinality project has no quantifier over every Cat-valued diagram, so it neither proves this converse nor supplies the nonfiltered counterexample that would be needed (N37; RS RESIDUE F.7). |

### RESIDUE I

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **RESIDUE I.1** — Diagonal-stable smooth maps | claim (return: Proved); DSS:279; BISITE F.10–F.12 and F.19 | **none**; unpursued implication | Absent: no strict-diagonal test or maximality theorem characterizes discrete fibrations. |
| **RESIDUE I.2** — Space-valued ambidexterity | claim (return: Proved); DSS:280; BISITE F.10–F.12 and F.19 | **none**; unpursued implication | Absent: no comparison of left and right Kan extensions for every base change identifies the isomorphisms among discrete fibrations. |
| **RESIDUE I.3** — Enhanced smooth correspondence functor | claim (return: Proved); DSS:281; BISITE F.10–F.12 and F.19 | 117/021:53–67; unpursued implication | Base-change formulas and mates motivate the construction, but a lax symmetric monoidal span functor with enhancement/coherence is not supplied (N32, N42). |
| **RESIDUE I.4** — Cancellation flaw in a coherence reference | claim (return: Proved); DSS:282; BISITE F.10–F.12 and F.19 | **none**; unpursued implication | Absent: no suitable-decomposition axiom, walking-arrow cancellation counterexample or span-universal-property proof appears. |
| **RESIDUE I.5** — Covariant proper correspondence formalism | claim (return: Proved); DSS:283; BISITE F.10–F.12 and F.19 | 117/012:16–29; 117/021:53–67; unpursued implication | The source has formal opposition and paired base-change formulas, but no base-opposition transport of a coherent correspondence functor or trivial-twist theorem (N24, N32). |
| **RESIDUE I.6** — Pointed-space ambidexterity | claim (return: Proved); DSS:284; BISITE F.10–F.12 and F.19 | **none**; unpursued implication | Absent: no union-of-components classification of universally ambidextrous discrete fibrations is stated. |
| **RESIDUE I.7** — Reversible localizers and bare-derivator coefficients | claim (return: Open); DSS:285; (no manuscript locator supplied); same-ID RS:426 | 117/004:23–31; 117/005:21–23; 117/020:4–17; unpursued implication | The Hom and common-presentation questions recognize related missing structure, but give neither a reversible-localizer classification nor a natural coefficient-tower construction on every bare derivator (N17, N19, N27; RS GALOIS G.6/E.11). |
| **RESIDUE I.8** — Stable ambidexterity via finite bifibrations | claim (return: Proved); DSS:286; BISITE F.10–F.12 and F.19 | **none**; unpursued implication | Absent: no finite-discrete-bifibration classification or universal equality of stable Kan extensions is established (N43 supplies only a contextual caution). |
| **RESIDUE I.9** — Second coefficient stages for spectra and F_p | claim (return: Proved); DSS:287; Prompt I(3), concrete enhanced second stages for spectra and D(F_p); GALOIS E.8/E.10 independently checked; bare-derivator GALOIS E.11/G.6 remains Open | 117/005:33–36; unpursued implication | A description through (M,W) is sought, but no localized-space realization, integral π₁/π₂ condition or iterated mod-p coefficient tower is constructed (N27, N41). |

### RESIDUE J

| ID and topic | Supplied status and earlier source locator | Present scan evidence / kind | Individual comparison |
|---|---|---|---|
| **RESIDUE J.1** — Strict 2-categories over ordinary bases | claim (return: Proved); DSS:288; VI ms.83; BISITE C.10 and F.18 | **none**; unpursued implication | Absent: no Street weak equivalences or fine strict-2-category localization over an ordinary base is defined. |
| **RESIDUE J.2** — Recognition for nontrivial 2-cell bases | claim (return: Open); DSS:289; (no manuscript locator supplied) | 117/006:16–23; unpursued implication | Two-functor variance on ordinary indexing categories does not treat a walking nonidentity 2-cell as a base or supply the required coherent lax action (N20). |
| **RESIDUE J.3** — Higher pullback classes and lax-comma base change | claim (return: Open); DSS:290; (no manuscript locator supplied) | 117/021:53–67; unpursued implication | Ordinary strict-pullback Hot 4 provides no higher lax-comma Der 4 theorem or four-variance table, so the open entry remains untouched (N31–N32). |

## What the scans add to the selected RESULTS_STATE questions

Each O-item is of kind **unpursued implication** (a contextual comparison), not a change to the recorded research status. Exact selected register entries and source filenames are available in `working/context_catalog.json`; the two Hua entries at RS lines 523–524 are separately discussed in N10 and N26, with credit to his project.

| Item / register IDs | Recorded status and RS lines | Scan, words and effect |
|---|---|---|
| O01 — TOTASPH D.7; RESIDUE F.5 | Open (the return's claim), lines 427,421 | **117/022:27–28, “Cas des catégories filtrantes ??”**: adjacent cofinality motivation, but no exact-colimit comparison or affine equalization step for the open converse (N37, Q02). |
| O02 — TOTASPH F.27; RESIDUE F.6 | Open (the return's claim), lines 416,422 | **116/007–008; 117/023:3–22, “deux sous-catégories pleines”**: gluing provides a possible setting for later sieve questions, but no total-presheaf quantifier or dwyerienne composition argument (N10, N38). |
| O03 — GALOIS B.13 | Open (the return's claim), line 419 | **117/020:21–24, “J'ai prouvé l'existence des f_!, mais non encore celle des f_*”**: explicit historical evidence of an incomplete construction, with no accessibility or converse criterion (N28). |
| O04 — GALOIS G.6; GALOIS E.11; RESIDUE I.7 | Open (the return's claim), lines 420,434,426 | **117/004:23–31, “On a sans doute”; 117/005:21–23, “Relations entre ces Hom internes … ??”**: the enrichment problem is recognized, but there is no natural higher-coefficient construction on all bare derivators (N17, N19, N27). |
| O05 — POLES F.14 | Open (the return's claim), line 423 | **No direct statement**: neither the reversible-localizer classification nor its comparison with spectral homology is formulated; Hot 7 concerns a different lifting problem (Q01, NR07). |
| O06 — RESIDUE F.7; PATHS D.22 | Open (the return's claim), lines 425,438 | **117/022:27–28; 117/020:4–24**: the filtered and common-presentation questions are early motivations, without the universal Cat-colimit quantifier or a finite/cardinal recognition theorem (N27–N28, N37). |
| O07 — BISITE F.18; BISITE C.10 | Open (the return's claim), lines 429,441 | **117/006:16, “2-contravariante”**: variance on ordinary categories is present, but higher categories are not supplied as indexing bases and no lax-comma base-change theorem is stated (N20, N31). |
| O08 — GALOIS B.1; GALOIS B.3 | Proved (the return's claim), lines 463,451 | **117/022:8–45, “je présume” and “Résulte du diagramme comm.”**: the adjoint special case is discussed, but the general absolute or relative Theorem A is not written here (Q03, N35–N36). |
| O09 — REVLOC F.1 / REVERSIBLE_LOCALIZERS F.1 | New headline, RS lines 103–106; intake found the definition valid, finite witness not recomputed | **117/020:21, “localisateur fondamental”**: the absent axiom list makes the claimed separation of absolute and relative packages relevant, but these scans give no instance or rebuttal of its counterexample (Q03). |
| O10 — POLES B.2; TOTASPH A.9 | Proved / Known (the return's claims), lines 467,481 | **117/023:10–19, “surjective” and “On veut”**: Hot 7 should not be identified with either forward localizer gluing or the biconditional W(7 bis), whose exact statements are separate contextual data (Q01, N38). |
| O11 — TOTASPH C.10; PRETOT A.12 | Refuted / Proved (the return's claims), lines 482,472; PRETOT's run is listed as reviewed | **116/003:46, “i est tot 0-asph.”; 117/022:27–28**: neither phrase is the Δ_inj counterexample or the categorical totality converse, and the report adds no new proof of the reviewed item (Q02, NR11). |
| O12 — GALOIS D.2; BISITE A.19 | Proved (the return's claims), lines 466,455 | **116/004:26, “pour tout faisceau F”; 116/006:8, “localement constants”**: the coefficient distinction is explicit, but its universal-base-change repair is not stated (N02, N07). |
| O13 — STRATA 0.1; STRATA B.2 | Proved (the return's claims), lines 474–475 | **116/006:10–18; 116/008:5–13**: the two-stratum topos and crossing-arrow bifunctor are concrete links, while a coherent exit-path/constructible-coefficient theorem is absent (N08, N11). |
| O14 — RESIDUE F.3 | Proved (the return's claim), line 473 | **No direct statement**: the injection and free-category examples do not appear, so the open exactness question should not be retested using these leaves as if they contained those examples (Q02). |
| O15 — Hua 116-presheaf-gluing-continuous-gluing-functor | Literature/intake lead, line 523; intake “new to us” | **116/007–008, “il revient au = de dire”**: the equivalence and bifunctor are actually stated, with no collage proof on the leaf; the SGA reference is checked separately (N10–N11, R01). |
| O16 — Hua 117-adjunction-equivalence-criterion | Literature/intake lead, line 524; intake “new to us” | **117/018:6–27**: the hypotheses and diagramwise conclusion are present, but closure assumptions and the extra hypothesis in the cited modern theorem need qualification (N26, R10–R11). |
| O17 — MPL_105 R08; MPL_134-8_043-087 H4; MPL_106+107 leads | RS orientation lines 20–25 and excerpted research-note leads; not reviewed source transcriptions | **No new cross-package source**: the current leaves answer only the bounded questions in Q01–Q03, and the cited other packages and cote 118 were not supplied for a fresh reading. |
| O18 — GALOIS B.14 | Open (the return's claim), line 433 | **No direct statement**: the open entry concerns universal preservation and factorization by Grothendieck fibrations for a bare derivator, which is not the same problem as the missing right Kan adjoint on 117/020 (N28). |

### H01 — Headline projects outside the mathematics of this package

**Kind:** unpursued implication / bounded comparison. **Source:** all supplied scans; RS headline block, lines 37–110.

No statement about the moduli tower, GT, point-sections or the section conjecture appears, so the scans give no evidence for or against **EXIT_TOWER E.39/E.43/E.44/E.49/D.45, LM7_PUSH E.58/E.65, SECTIONS_OVER_Q A1/A.169/A.178, LM4_SUCCESSOR A.14/B.34/B.38, or ANABELIAN_SUCCESSOR A.3**. Nor do they contain the finite models or counts relevant to **FINMON C2-CP2** or **S2COUNT**; the general words “modèles” and the loop pictures are insufficient links. This preserves the source's distinct review statuses instead of transferring a review of one headline to another.

### H02 — A scope qualification for Hua's all-localizer assertion

**Kind:** reading question about a contextual claim. **Source:** 117/020:21–24; context/hua_project/117.modern.tex:432–440, “Quatre exemples”; RS GALOIS B.13 and DSS PATHS D.18/D.22.

Hua attributes the existence of both adjoints for every fundamental localizer to Cisinski, explicitly from memory. The supplied state register keeps the nonaccessible generality as an open issue, while the present leaf itself lacks f_* and considers finiteness conditions. No edition-level claim about all localizers is certified here without the exact cited hypotheses; the checked references for this return are only the two listed below.

## Source key and limits of the reference check

The relevant supplied files are `context/README.md`, `context/notes/RESULTS_STATE.md`, `context/NEW_RESULTS.md`, `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, both files under `context/hua_project/`, `context/PURSUING_STACKS_CONTENTS.md`, and `context/ps_chapters_VI_VII/ps6.tex` / `ps7.tex`. The cited companion files are under **`context/companion/chunks/`**: `DER_II-a.tex`, `DER_XIIb-a.tex` and `DER_XVI.tex`; their manuscript-page markers are locators in the supplied companion's transcription, not new visual verification of those older manuscripts.

The two externally checked primary references, followed from Hua's leads, are:

1. A. Grothendieck and J.-L. Verdier, **SGA 4 I, Exposé IV, exercise 9.5.10(a–c)**, original pp. 470–471; [checked primary PDF](https://www.normalesup.org/~forgogozo/SGA4/04/04.pdf), retypeset p. 96 (PDF index 95). Relevant notes: N10–N11 and R01.
2. N. Gurski, N. Johnson and A. M. Osorno, **Extending homotopy theories across adjunctions**, [arXiv:1508.00054, v3](https://arxiv.org/pdf/1508.00054.pdf), pp. 3–4, Definitions 1.3–1.4/1.9, Lemma 1.7 and Theorem 1.11(c). Relevant notes: N26 and R10.

The compact check record is `working/primary_references.md`; its conclusions are qualified in the notes above. Other bibliographical assertions in NR, RS and Hua are attributed to those supplied files rather than presented as independently verified literature results.

`working/context_search_log.json` records the context queries associated with the notes and comparisons, including zero-match searches. A keyword match is a discovery aid, not proof that an earlier result is correct or that a manuscript contains it; the positive comparisons rest on the frozen readings and the located contextual statements. The first-pass `working/observations.md` is a process record superseded by the audited transcription and these notes wherever they differ.

This return establishes neither a whole-archive priority date nor the contents of the missing cote 118. The 34-page diplomatic reading, its 131 doubt records, and the bounded historical comparisons are the completed work; the mathematical conjectures and contextual research claims retain the qualifications stated in their individual entries.
