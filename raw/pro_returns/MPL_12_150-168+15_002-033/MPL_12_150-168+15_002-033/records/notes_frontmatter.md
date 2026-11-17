# Research notes — MPL_12_150-168+15_002-033

## Scope, method, and status of the evidence

This report accompanies the complete diplomatic transcription of the **45 supplied scan pages**: cote 12, scans 150–168, followed by cote 15, scans 002–014, 016–024, 026, 028, 030 and 032. The isolated “49 pages” in the task description does not match either the stated 19 + 26 breakdown or the actual image manifest; the two blank pages and four previously transcribed pages identified in the prompt were not supplied and are not reconstructed here. There are 34 text sheets, 10 reused typed sheets, and one cover.

The primary transcriber viewed the whole page and both supplied detail images of every page, completed the page inventory, and performed the second visual audit in one continuous transcription stream. No OCR was used. The page files and combined transcription were frozen at **2026-11-17 00:29:05 UTC**; the context was opened at **00:29:10 UTC**, after the freeze. Mathematical research and independent checks began afterward, and no contextual or literature comparison has changed a frozen reading.

All supplied earlier transcriptions and research notes remain **first-pass claims**, as README.md directs. RESULTS_STATE labels such as Proved, Refuted, Known and Open are retained as the research returns' claims unless that register expressly records a referee verdict; no new referee status is conferred here. An unchecked planning question, a manuscript assertion, a published theorem, and an explicit calculation in this report are kept distinct.

Each numbered item has an allowed kind, a current witness or an explicitly identified contextual witness, a brief quotation where applicable, a context comparison, and the relevant register IDs and statuses. Its substantive note is one to four sentences; metadata and equations do not expand that prose into an unbounded essay. The phrase “own idea” includes a counterexample or construction independently worked here and never means a claim of historical novelty; its confidence and reason are stated.

Locators of the form **12/156:L4** refer to line 4 of the frozen page file for cote 12, scan 156, not a counted manuscript line. **CT** means context/MPL_16+47+54+44_transcription.tex; **CN** is its companion notes file; **N15a** means context/same_cote_15/MPL_15_087-138_notes.md; **N15b** means context/same_cote_15/MPL_15_195-228+18_002-017_notes.md; **RS** means context/notes/RESULTS_STATE.md. The records folder preserves the research memoranda, bounded context-search logs, and full supporting constructions.

## Answers to the questions supplied with the packet

| Question | Answer warranted by this selection | Main notes |
|---|---|---|
| Is the category of motives built on the Lefschetz correspondence rings of cote 16? | **The actual conditional construction is now visible**, at 12/150–154: all rational homological correspondences, additive/idempotent completion under the stated semisimplicity hypotheses, cohomological projectors, tensor structure, and Tate inversion. No identification with modules over the particular universal Lefschetz operator ring of 16/014–018 is written. | M01–M08 |
| Is the Lefschetz \(\mathfrak{sl}_2\) inside the motivic Galois group? | The specified correspondence action does not automatically define a natural tensor automorphism action. The projective-line test already reported in N15a L03/§111 is retained as a first-pass lead, and the new tensor construction gives no missing subgroup morphism. Beauville's published analogue lands in invertible correspondences. | M22–M23 |
| Is its Cartan cocharacter the motivic grading? | The Lefschetz Cartan eigenvalue on \(H^i(X)\) is shifted by the dimension: \(i-\dim X\), whereas the tensor grading uses \(i\). A functorial tensor grading is central in the tensor automorphism group; the object-dependent shift and the naturality conditions must be addressed before any identification. | M05, M23; Beauville, 2008, Theorem 3.3 |
| Which standard-conjecture lettering is used? | Align by mathematical content, not by alphabetical position: the secure operational matches are draft A → printed A and draft C → printed B; draft B → printed D and draft D → printed C remain provisional. The current pages state assumptions without giving the missing standalone draft definitions. | M24 and the dictionary below |
| Does cote 14 implement the singular-hypersurface programme of 16/047? | **The supplied material does not decide this.** The actual cote-14 pages and full return are absent; truncated register leads cannot answer for them. The reused pages in this packet are identifiable with Lipman's surface-singularity text and are not evidence that Grothendieck carried out that separate motivic programme. | R11–R12 |
| Where is his motivic Galois exact sequence over \(\mathbf Q\)? | It is **not written in these 45 pages**. The cover and the opening heading specify a finite ground field, and the current Artin quotient is \(\widehat{\mathbf Z}\); N15b M06 separately reports a local extension at 18/006. The modern rational Nori sequence is stated in R02 with its exact hypotheses, without attributing it to a missing manuscript line. | R01–R02 |
| Is there a written period conjecture? | None occurs in the current selection. N15b reports a live strong \(g+u\) formulation at 18/011, a cancelled normalized draft at 18/012, and live elliptic \(4\)-or-\(2\) transcendence questions at 18/013; these remain reported witnesses pending their separate visual review. Independently, Grothendieck's own published de Rham paper contains an elliptic period/quasiperiod conjecture. | R03–R04, R16; Grothendieck, 1966, p. 102, note 10 |
| Which claims are theorems for Nori and Ayoub? | The classical group comparison with fixed embedding and appropriate coefficients, and rational pure Nori/André semisimplicity, are precise later results. Identifying every motivated morphism with an algebraic correspondence, general Hodge fullness, or a motivic t-structure requires additional arguments. | M25–M27 and the S15 table below |
| Do these pages supply motives over a base with six operations? | They supply specified pure-motive operations and restricted base change for Deuring categories. They do not supply a six-operation formalism with all adjunction and exchange compatibilities. | R15 |

### Standard-conjecture dictionary

The current witness 12/151–153 separates numerical/homological equivalence, Hodge positivity and projector assumptions. The A–D alignment below concerns the **supplied cote-16 draft**, not letters silently inserted into the present transcription.

| Draft letter in the supplied cote-16 context | Operational content | Printed terminology used for comparison | Evidential strength |
|---|---|---|---|
| A | Lefschetz statement for algebraic cohomology classes | A | Supported by the explicit content. |
| B | Equivalence comparison associated with the index/positivity argument | D, numerical = homological | Provisional: standalone draft B is not supplied. |
| C | Algebraicity of inverse Lefschetz operators | B | Supported by the operator content. |
| D | Projector/characteristic-polynomial criterion | C, algebraic Künneth projectors | Provisional: standalone draft D is not supplied. |

See CT 16/040, 042, 044–050; N15a L09–L10; N15b's introductory dictionary; Grothendieck (1969, §3) and Kleiman (1968, §§2–3). No equality of labels is treated as a theorem beyond those witnesses.

### S15: the modern comparisons, claim by claim

| Manuscript feature | Later theorem or formal construction | What still needs comparison |
|---|---|---|
| Semisimple correspondence category, 12/151 and 159 | Numerical motives are semisimple abelian; algebraic Künneth projectors give the specified nilpotent homological-to-numerical kernel (Jannsen, 1992, Theorem 1 and Corollary 1). | The manuscript uses a faithful cohomological realization and explicitly assumes homological = numerical; nilpotence is not equality. |
| Tensor structure and realizations, 12/152–154 | Nori's and Ayoub's classical groups are canonically isomorphic for the stated characteristic-zero, complex-embedding and PID-coefficient setting (Choudhury & Gallauer Alves de Souza, 2017, Theorem 9.1). | This does not identify this manuscript category with either construction or establish a motivic t-structure. |
| A pure semisimple category | Rational pure Nori motives agree with André's motivated category (Arapura, 2013, Theorems 6.3.3 and 6.4.1). | Surjectivity from algebraic correspondences onto all motivated correspondences is an additional algebraicity assertion. |
| Faithful Hodge/de Rham/Betti functors, 12/152 | The named modern categories carry specified realizations. | Faithfulness, full faithfulness, essential image and neutrality over the coefficient field are different properties. |
| Arithmetic quotient by Artin motives | Compatible rational Nori fibre functors give the exact descent sequence in R02 (Kahn, 2025, Theorem 5.10 and §10). | The current finite-field packet is not a manuscript witness of that sequence over \(\mathbf Q\), its splitting, or its connected-kernel identification. |
| Finite-field character group and crystalline centralizers, 15/003–014 | Honda–Tate handles abelian varieties; Milne's all-motives description retains a stated Tate hypothesis. | Neither the characteristic-zero Nori–Ayoub theorem nor the abelian classification removes that all-motives hypothesis. |

## The required table: linear statement, non-linear statement

These are precise comparisons with different hypotheses, not asserted logical implications between the columns.

| Theme | Linear statement | Non-linear statement | What the current pages add and what remains |
|---|---|---|---|
| Tate and anabelian Hom | For abelian varieties over finite \(k\), \(\operatorname{Hom}_k(A,B)\otimes\mathbf Z_\ell\simeq\operatorname{Hom}_{G_k}(T_\ell A,T_\ell B)\), \(\ell\ne\operatorname{char}k\) (Tate, 1966). | Over a sub-\(p\)-adic field, dominant maps to a hyperbolic curve correspond to continuous open homomorphisms of arithmetic fundamental groups over \(G_k\), modulo geometric inner conjugacy (Mochizuki, 1999, Theorem A). | 15/013 makes the finite-field endomorphism side explicit; the target at \(p\) must be the Frobenius centralizer. FLAGGED_149 B9's prime-to-\(p\) point-recognition problem remains open in the register. |
| Semisimplicity and trivial centres | For a connected affine group in characteristic zero, semisimplicity of its finite-dimensional representations corresponds to pro-reductivity; it permits a nontrivial centre (Deligne & Milne, 1982/2012, Proposition 2.23). | The geometric profinite group of a characteristic-zero hyperbolic curve is slim; its centre is trivial and its outer Galois action recovers the arithmetic extension (Mochizuki, 2004, Lemma 1.3.1 and Corollary 1.3.2). | 12/151 and 159 give the conditional semisimplicity mechanism, while 15/003 conditionally describes a commutative band. These do not prove any special centralizer assertion in LM4_SUCCESSOR. |
| Polarizations and real structures | Polarizability of an algebraic Tannakian category over \(\mathbf R\) is characterized by a compact real form of its band (Deligne & Milne, 1982/2012, Theorem 4.17). | For smooth projective hyperbolic \(X/\mathbf R\), section classes recover \(\pi_0(X(\mathbf R))\), with the stated profinite/erasability setting (Pál, 2011, Theorem 1.3). | 12/159–167 develops positivity, and 15/011 explicitly denies a real fibre functor. Compactness of the band, neutrality of a gerbe, and recovery of real connected components are distinct issues. |
| Weights and cyclotomic normalizers | Weights over number fields give \(\operatorname{Hom}_{G_k}(\mathbf Z_\ell(1),T_\ell A)=0\); the current finite-field weight and Tate maps satisfy \(\epsilon\circ i=[2]\). | Cuspidal inertia is characterized by the appropriate procyclic subgroup with an open arithmetic normalizer **and cyclotomic conjugation action**, under the non-Tate hypothesis (Stix, 2012, §5; 2008 preprint, §5.2 and Theorem 20). | The explicit character normalization on 15/013 sharpens the bookkeeping. It does not supply the missing character step in the displayed LM6 A.22 summary, and the truncated LM6 A.50 entry is not used to fill that gap. |

## Steps the manuscript itself marks as unverified

This index records the author's questions, assumptions and verification language. Editorial uncertainty macros do not themselves mean that the author questioned a claim; rows with doubtful words say so explicitly. “OK !” is listed as a claimed local check, not left on the list of unresolved questions.

| Witness | His words or marker | Scope and present note |
|---|---|---|
| 12/150 | “comment exprimer que \(T\) est fidèle ?” | Faithfulness criterion and the doubtful final functor letter; M28. |
| 12/151 | “Si on admet” homological = numerical; “si on admet l'inégalité de Hodge” | Explicit hypotheses of the construction; M01–M04, M17. |
| 12/152–153 | “Nous supposons maintenant”; “On suppose de plus” | Projectors and product compatibility are assumptions; M05–M06. |
| 12/153–154 | Full faithfulness of the Tate-twist functor is imposed. | Formal inversion uses this cancellation hypothesis; M07. |
| 12/156 | “On suppose” the normalized effective internal Homs exist. | Additional duality hypothesis; M12–M14. |
| 12/156 | “vérification facile” | The tensor/internal-Hom identity needs genuine rigidity, as M14's countermodel shows. |
| 12/157 | Marginal “?” by equivalence of the two nondegeneracy conditions when \(M=N\) | M15 gives a conditional finite-duality argument. |
| 12/158 | “autoadjoint (?)” | Same-parity nondegenerate forms give the precise criterion; M16. |
| 12/161 | Uncertain “Sans doute on le supprimera” followed by a cancelled “(iii)” | The reading and the intended redundancy remain separate; M19, M31. |
| 12/165 | “OK !” | The author claims the displayed trace check; M20 identifies its hypotheses. |
| 12/167 | “il y a lieu de vérifier”; “Ça ne doit pouvoir faire de difficulté”; “La vérification … est triviale” | Tate compatibility of the selected positive classes; M21. |
| 15/003 | “si on admet” the uncertain density/duality property; “en vertu des conj. de Tate et de Tate-Honda” | The all-motives identification retains conditional input; FF01. |
| 15/007 | “On se propose de décrire” | Programme for the category, grading, augmentation and realization family; FF09–FF10, FF21–FF22. |
| 15/009 | Uncertain marginal “vif\|vérif” | It may be a verification marker; it is not counted as a certain authorial instruction. |
| 15/016 | Uncertain “vraisemblᵗ” and “indépendamment\|indépendantes” | Tentative independence of the Deuring axioms; D30 preserves the scope ambiguity. |
| 15/024 | “on peut éliminer ce groupe …” using polarization and crystalline structure | A claimed construction without the comparison maps or stabilizer calculation; D23. |
| 15/032 | “Montrer qu'il y a une \(D\) universelle” | Explicit existence problem for the norm category; D28. |
| 15/032 | Uncertain “Généraliser”; “Noter que … commute aux chgts de base”; marginal compatibility requirement | Generalization and coherence/base-change obligations; D28–D29. |
| 15/004, reused typescript | “Proofs are omitted” | Verification is deferred by the reused surface-singularity source, not attributed as a new handwritten conjecture; R11. |
| 12/166, reused typescript | “We will sketch the proofs” | Source convention and proof-scope issue for Lemma VII.14; R14. |

Material revisions are also recorded in the note register: the correction from “injectif” to the doubtful inserted “épim.” at 12/157, the changed formula for adjunction at 12/158, and especially the strengthened Azumaya hypothesis on 15/020. A deletion of a formulation is not automatically a withdrawal of its underlying mathematical proposition.

## Title sheets, headings, and page counts

### Titles and internal headings actually present

| Cote/scan | Title or heading, retaining uncertainty | Kind of witness |
|---|---|---|
| 12/155 | Cancelled “Décomposition canonique”; live “Niveau d'un motif” | Section heading, not a cover. |
| 12/156 | “Duals\|Duels et Homs de motifs”, with the first word doubtful | Underlined section heading. |
| 12/158 | “Involutions.” | Underlined section heading. |
| 12/159 | “Formes définies positives sur les motifs” | Double-underlined section heading. |
| 15/002 | “Groupe\|Groupes de Galois motivique\|motiviques / commutatif / Cas d'un corps de base fini” | The single supplied cover/title sheet; doubtful endings are retained. |
| 15/003 | “Catégorie des motifs sur \(\mathbf F_p=k\)” | Underlined opening mathematical heading. |
| 15/026 | “Cat. de Deuring sur \(A\)” | Underlined section heading. |
| 15/030 | “Ex 1” | Numbered example heading. |
| 15/032 | “Ex. 2” | Numbered example heading. |

There is **no explicit total-page-count statement** such as “19 pages” or “Pages 1–67” on a supplied cover or sheet. The archive catalogue titles and the packet's 19 + 26 count are external metadata, not inscriptions to be inserted into the transcription. The 24-page typed “Motifs” text mentioned in README.md is not present.

### Visible manuscript pagination and additional typed pagination

| Supplied scan range | Visible manuscript-page markers |
|---|---|
| 12/150–168 | 149–167, consecutively. |
| 15/002 | No manuscript page number visible. |
| 15/003–014 | 2–13, consecutively. |
| 15/016–024 | 15–23, consecutively. |
| 15/026, 028, 030, 032 | 25, 27, 29, 31, respectively. |

| Reused typed sheet | Additional internal typed page |
|---|---|
| 12/160 | VII.19 |
| 12/162 | VII.20 |
| 12/164 | VII.18 |
| 12/166 | VII.17 |
| 12/168 | VII.15 |
| 15/004 | 163 |
| 15/006 | 162 |
| 15/008 | 161 |
| 15/010 | 160 |
| 15/012 | 159 |

The two numbering systems and their nonsequential physical arrangement are preserved. The five cote-12 sheets concern Brauer groups and regular rings; their authorship remains unidentified. The five cote-15 sheets match Lipman (1969, §25), and this source identification does not convert physical reuse into a continuous handwritten argument.

## Numbered research register

The sections that follow contain the detailed notes. Supporting calculations for D04–D05, D13 and D25–D29 are retained in records/research_deuring.md, D04 and Constructions A–D. Construction D concerns the explicitly stated central-algebra hypotheses and restricted target 2-category; it does not prove the claims for arbitrary semisimple centres or general base-change compatibility. The assembled report incorporates the quotation and hypothesis corrections recorded in records/research_review.md; the original research memoranda remain working records.
