# Research notes: MPL_15_195–228 + MPL_18_002–017

## Scope, evidence and locators

These notes concern all **49 supplied scans**: cote 15, scans 195–228, and cote 18, scans 2–7 and 9–17. They were written after the complete transcription, second reading and notation audit were frozen at **2026-11-15 13:53:15 UTC**; the context archive was opened at **13:53:25 UTC**. Research comparisons and mathematical interpretations have made **no changes to the frozen transcription**.

A locator such as `15/195:L9–19` means cote 15, scan 195, lines 9–19 of **the individual page file** `pages/MPL_15_195-228+18_002-017_15_scan195.tex`; it never means lines of the combined transcription. `18/011` similarly identifies `pages/MPL_15_195-228+18_002-017_18_scan011.tex`. Every observation has a kind, a short manuscript quotation, its location, its context comparison, and the relevant results-ledger status; its substantive body contains one to four sentences. An ellipsis in a short quotation abbreviates the quotation only: the diplomatic transcription remains the full witness.

**CT** means the supplied `context/MPL_16+47+54+44_transcription.tex`; **CN** means `context/MPL_16+47+54+44_notes.md`. CT references identify the cote and scan within that file, while CN references identify its observation headings; where a context line number is given, it belongs to that context file and is explicitly distinguished from a new page-file line number. These supplied transcriptions and earlier research notes are **first-pass claims**, not independently verified readings or established results. The supplied Oda article is a primary printed source. The full cote 12, 13 and 14 texts named in the planning documents are not supplied; truncated cote 14 extracts in the ledger do not substitute for them.

Every ledger ID below refers to `context/notes/RESULTS_STATE.md`, rebuilt on 15 November 2026 at 12:08 UTC. **Known, Proved, Refuted and Open retain the status of the named return**, unless the register expressly records review; this report does not promote a first-pass note or an unchecked planning item to a reviewed result. “Bears on” denotes a substantive connection; broad WG2 associations are identified as project links where no dedicated result exists. Each numbered observation has its own executed `rg` search for its listed terms in the supplied context, documented in `records/research_context_searches.json`; “adds” means an addition relative to those supplied materials, not a claim of historical priority.

The page order is the order requested for this package. It does not establish the chronology of revisions. In particular, the wholesale cancellation on 18/012 is evidence that this draft was cancelled, not by itself evidence that Grothendieck abandoned the conjecture's truth. Reused typescripts are fully transcribed and discussed as their own texts; their Lie-theoretic terminology is not evidence for a claim about motives written on another sheet.

## Answers to the questions supplied with the package

| Question | Finding and evidential limit | Detailed observations |
| --- | --- | --- |
| Is the category of motives built from cote 16's lefschetzien correspondence rings? | **Not demonstrated by this excerpt.** These pages use an existing category and its realizations; they give no construction identifying its morphisms with those rings. | M01; CT16/018,049; new 15/219 and 18/011 |
| Is the Lefschetz \(\mathfrak{sl}_2\) inside the motivic Galois group? | **No such identification is supplied.** The cancelled elliptic-period \(\mathrm{SL}_2\) is not the Lefschetz action on \(H^1\) of that elliptic curve, where both Lefschetz raising and lowering vanish. | M02, R01; new 18/012–013 |
| Is his grading the weight cocharacter? | **Several different gradings occur.** On18/011 the central section is in a Levi quotient and satisfies \(\varepsilon\circ j=\mathrm{id}\); identifying it with a category-wide weight map requires an explicit convention and comparison. | M03, P14; CT16/003–018 |
| Which A–D lettering does he use? | **A partial dictionary is supported.** Manuscript A corresponds operationally to printed A, and manuscript C to printed B; the proposed B↔printed D and D↔printed C remain provisional. | M04 and the dictionary below; CT16/044–050 |
| Does cote 14 carry out CT16/047's singular-hypersurface programme? | **Undetermined from the supplied evidence.** The actual cote 14 text is missing; the new smooth-projective construction on 15/223 concerns a different cohomology-comparison question. | M05, A33 |
| Is the arithmetic motivic exact sequence over \(\mathbf Q\) written here? | **Not in these selected pages.** The sequence on 18/006 has quotient \(\pi\) and kernel \(G'(C)\) in a local comparison problem; the modern arithmetic sequence is separately identified in M06. | M06, P06, A23 |
| Is there a written period conjecture? | **Yes.** The live strong conjecture on 18/011 asks for degree \(g+u\); the cancelled normalized draft on 18/012 and the live elliptic questions on 18/013 provide additional distinct formulations. | P15–P26 |
| Which assertions survive for Nori/Ayoub groups, and which need further conjectures? | **The answer is statement-specific.** Reconstruction, comparison of classical groups, rational pure semisimplicity and arithmetic descent have modern theorems; algebraic-cycle comparison, general Hodge fullness, integral finiteness and period genericity require separate analysis. | M06–M10 and the S15 table below |

The README's expectation of a written period witness is confirmed by these scans. Its broader suggestion that the period conjecture is known only through others' reports should not be repeated as a bibliographic conclusion: Grothendieck's own published de Rham paper already discusses conjectural independence of elliptic periods and quasiperiods (Grothendieck, 1966, p. 102, note 10; P20, P26). No L-function construction or developed six-operation formalism is supplied by this selected excerpt; the relative motivic and realization questions are evidence for a programme, not its completion (A20–A27, M01, M08).

### A–D: a working dictionary with uncertainty retained

This table compares the **operational evidence in the supplied first-pass context** with the printed terminology; the present 49 scans add no new definitions of those four letters. Printed A, B and C are checked in Grothendieck (1969a, pp. 195–197), and printed D in Kleiman (1994, §5, Proposition 5-1).

| Manuscript label in CT16 | Evidence in the supplied context | Printed comparison | Status of the identification |
| --- | --- | --- | --- |
| A | Algebraic Lefschetz behaviour; the implication A plus index ⇒ B on 16/044–045 | A: Lefschetz on algebraic classes | Supported operationally; distinguish its algebraic-class clause from the cohomological hard-Lefschetz clause in the printed formulation |
| B | A plus index ⇒ B on 16/044; used in the programme of algebraic pairings and equivalence relations | D: numerical equivalence equals homological equivalence | **Provisional**; the implication is not a standalone definition |
| C | Inverse Lefschetz operators and the hyperplane-section/product induction on 16/045,048 | B: algebraicity of the Lefschetz inverse/operator | Supported operationally |
| D | The rational characteristic-polynomial consequence on 16/048, with the nearby projector discussion on 16/046 | C: algebraicity of Künneth projectors | **Provisional**; the consequence alone does not determine the definition |

### Linear statement, non-linear statement

These are precise comparisons with different hypotheses, not equivalences between entire research programmes. Each row is developed in B01–B05, which contain manuscript locators, context searches and ledger statuses.

| Pair | Linear statement | Non-linear statement | What must remain separate |
| --- | --- | --- | --- |
| Tate and anabelian Hom | For abelian varieties over a finite field, \(\operatorname{Hom}(A,B)\otimes\mathbf Z_\ell\cong\operatorname{Hom}_{G_k}(T_\ell A,T_\ell B)\), with \(\ell\ne\operatorname{char}k\) (Tate, 1966). | For hyperbolic curves over a sub-\(p\)-adic field, dominant maps correspond to continuous open arithmetic fundamental-group homomorphisms over \(G_k\), modulo geometric inner conjugacy (Mochizuki, 1999, Theorem A). | The bases, allowed maps and reconstructed objects differ; full faithfulness does not characterize an essential image. |
| Semisimplicity and trivial centres | In characteristic zero, a semisimple representation category corresponds to pro-reductivity in the connected Tannakian setting (Deligne & Milne, 1982/2012, Proposition 2.23). | A hyperbolic geometric profinite fundamental group is slim: its open subgroups have trivial centres, which enables recovery of the arithmetic extension from the outer action (Mochizuki, 2004). | A reductive group can have a large centre; \(\mathbf G_m\) supplies the elementary test in B02. |
| Polarizations and real structures | Tannakian polarization incorporates positivity and a compact real form of the band (Deligne & Milne, 1982/2012, Theorem 4.17). | For a smooth projective hyperbolic real curve, section classes recover the **connected components** of its real locus (Pál, 2011). | Neither an involution nor a section class by itself provides a polarization or singles out every real point. |
| Weights and cyclotomic normalizers | Over number fields, the Tate character cannot map equivariantly into an abelian-variety Tate module as \(\mathbf Z_\ell(1)\to T_\ell A\). | Under the non-Tate hypothesis, cusp inertia is detected by a normalizer with open arithmetic image **and cyclotomic conjugation action** (Stix, 2012, Definitions 26,29 and Theorem 30). | Open image alone omits a premise; B05 records exactly why the displayed LM6 A.22 summary and truncated A.50 claim do not close that gap. |

### S15: the modern comparison, claim by claim

The setting must be fixed before using this table: rational Nori motives over a subfield of \(\mathbf C\), a chosen Betti embedding and compatible fibre functors; the classical group-comparison theorem also allows principal-ideal-domain coefficients, but its rational pure-category consequences and the integral finiteness questions are different statements.

| Manuscript issue | Modern status in the specified setting | Remaining boundary |
| --- | --- | --- |
| Tensor automorphism groups and comparison torsors, 15/213 and 18/011 | Tannakian reconstruction and the fibre-functor torsor formalism apply to a specified neutral Tannakian category (Deligne & Milne, 1982/2012, Theorems 2.11, 3.2). | One must identify the manuscript's category and realizations. |
| Nori versus Ayoub | Their **classical motivic Galois groups** are isomorphic, including with PID coefficients (Choudhury & Gallauer Alves de Souza, 2017, Theorem 9.1). | That theorem alone is not a construction of a motivic t-structure or an equivalence of all derived motivic categories. |
| Pure semisimplicity | Rational pure Nori motives are semisimple and equivalent to André's motivated category (Arapura, 2013, Theorems 6.3.3, 6.4.1). | This does not assert semisimplicity of mixed motives. |
| Numerical semisimplicity | Jannsen's theorem is unconditional for numerical motives with characteristic-zero coefficients (Jannsen, 1992, Theorem 1). | Numerical=homological equivalence and descent of a chosen cohomological realization remain separate. |
| Arithmetic descent over \(\mathbf Q\) | There is an exact sequence of affine group schemes with proconstant absolute Galois quotient (Kahn, 2025, Theorem 5.10 and §10, checked v4). | No canonical splitting or identity-component identification is supplied by these scans. |
| Algebraic Lefschetz operators/projectors | Modern motivated morphisms can be compared with the correspondence programme. | Their representation by algebraic cycles requires the appropriate standard-conjecture comparison (M07). |
| General Hodge fullness and essential image | Fullness is separately conjectural; there are abelian-type cases (Arapura, 2013, §7.1). | The general essential-image question remains distinct (A21, M08). |
| Period-locus generation and period genericity | The single-elliptic-curve comparison in P23 has a later de Rham–Betti theorem (Kreutz et al., 2026, v3). | This does not prove the non-CM degree 4 conjecture or the stronger degree \(g+u\) statement. |
| Integral forms and crystalline points | These are additional problems in the manuscript. | A group comparison does not establish integral finiteness, admissibility or a positive-characteristic essential image (A19, M09, P03–P05). |

## Observation register

