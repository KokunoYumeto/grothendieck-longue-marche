# Foundations module: Parts A and E

This report covers the assigned Parts A and E only. It makes no assertion that the other parts or the integrated LM5 package are finished. The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority is claimed for the proofs or examples.

| Prompt item | Statements | Outcome within this module |
|---|---|---|
| What is to be settled: §§1–4 and the fundamental multi-Galois envelope | A.1–A.22 | (a)/(b): the discrete results are proved with the precise corrections below; the missing pro section and tower are supplied. |
| Lead 1 | A.1–A.4, A.15–A.19, A.21 | (b), with replacement proved: discrete multi-Galois, pro-multi-Galois, and profinite multi-Galois are distinct notions. “Every object is locally constant” needs the local-connectedness repair; pro variants use generation and continuity. |
| Lead 3, higher-theory implication | E.7–E.9 | (b), with replacement proved: ordinary 2-pushouts do not automatically compute higher shape; genuine infinity-topos descent does. The complete ordinary statement is in root Part C. |
| A(a) | A.1–A.4 | (b), with strongest stated repair proved: the Boolean counterexample refutes unrestricted recognition; either local connectedness or enough points separately repairs it, and both are necessary within the all-LC class. Explicit exactness axioms are given. |
| A(b) | A.5–A.8 | (a): all five conditions of 1.5 and its N.B.; 1.3–1.4, 1.7–1.10, 1.11; definitions 1.2, 1.6, 1.9; explicit 1.12 Hom-groupoid and automorphisms. |
| A(c) | A.9, A.22, E.1–E.4 | (a), with the exact higher-language and hypercompletion qualifications: theorem 2.1 needs no points; all finite Postnikov stages and their universal properties are constructed. |
| A(d) | A.10–A.12 | (b), with replacement proved: both requested phenomena are constructed. The literal beta-equivalence claim fails without a point in every component; exact alpha/beta criteria are proved. |
| A(e) | A.15–A.21 | (a)/(b): missing §3 developed, with precise replacements for ordinary point and universal-cover assertions; intrinsic pro-groupoids distinguished from arbitrary strict presentations and limits. |
| A(f) | A.13–A.14 | (a) discretely; (b) for unqualified profinite faithfulness, with the open-stabilizer correction and field application proved. |
| E(a) | E.1–E.2, E.5 | (a): shape and its truncations exist without point or connectivity hypotheses; exact representability condition for actual stages. |
| E(b) | E.3–E.4 | (a): the manuscript's first envelope is the classifying topos of its 1-truncated shape, and the finite-stage tower is the Postnikov tower for spaces with a contractible open basis. |
| E(c) | E.5–E.14 | (a)/(b): exhaustive A–C index; all-level constructions or explicit obstructions. The n=4 and n=5 finite-homotopy exodromy tests are positive, with the added meridian, goodness, and coherent finite-congruence checks. |

## Principal mathematical decisions

1. **Unrestricted Proposition 1.1 is false.** For the complete atomless Boolean algebra `RO(R)`, every object of its sheaf topos is locally constant. The proof uses the decomposition into subterminals and a bounded Boolean-valued well-order argument. The locale has no points: a completely prime filter on a complete Boolean algebra produces an atom. This is a complete counterexample, not an appeal to an unspecified pointless topos.

2. **Either proposed extra hypothesis separately is exact.** Within the class where every object is locally constant, being a groupoid presheaf topos, being locally connected, and having enough points are equivalent. Local connectedness plus Booleanity makes every connected object an atom; a single cover trivializing a coproduct of atom representatives supplies small projective generators. Enough points instead makes every subobject Boolean algebra atomic, and gives the same conclusion.

3. **Theorem 2.1 is point-free.** A connected covering family that splits every locally constant object gives an explicit groupoid by componentwise Cech descent. This is weaker than requiring the whole generating family to be simply connected. The inclusion preserves finite limits and arbitrary colimits because every diagram is split over the same cover.

4. **The literal point-based definition in 2.3 is not always the intrinsic fundamental groupoid.** The finite category `0 ⇉ 1 → 2` with the two composites equal gives distinct morphisms of points which become identical on locally constant objects. The coperfect locale of `R^3` gives a nondegenerate locally and globally simply connected topos without points. The nucleus is proved explicitly. Each locale trivializing cover omits one closed countable set in the ordinary ball; its complement is simply connected by the polygonal cone argument. The ordinary trivializations are transported back on the original fixed opens and glued, without treating their ordinary union as a fixed locale open.

5. **The pro-theory needs three distinct constructions.** Locally constant objects are the union of splitting categories; their sums/filtered-colimit enlargement is the Galois topos; an abstract inverse-limit group is a third object. The closure proof only uses images and relations of maps between locally constant objects. It does not assert that arbitrary subobjects of locally constant objects in an ambient topos are locally constant.

6. **Even a strict pro-presentation need not be the intrinsic pro-groupoid.** In A.21, `C_n = coproduct_{k>=1} B(Z/p^min(n,k))` has connected nonempty transition fibres and the same limit topos as `D = coproduct_{k>=1} B(Z/p^k)`, but the pro-groupoid is not constant: any map to constant `D` factors through a uniform stage, whose vertex groups have uniformly bounded exponent. The target has unbounded exponents. Accordingly A.18 uses the intrinsic fundamental pro-groupoids of the topoi. Hoyois's Corollary 3.20 is an essential-image recognition theorem and does not assert recovery of every arbitrary strict presentation.

7. **The finite-test warning is verified.** The shift on finitary permutations is conjugation on every finite support, but is not globally conjugate to the identity. Its finite quotients all factor through sign. An explicit commutator gives a 3-cycle from any nontrivial normal subgroup of the finitary alternating group, supplying the full simplicity argument.

8. **The Postnikov tower has the manuscript's geometric variance.** Its maps are `E -> E_[n] -> E_[n-1]`; inverse images run oppositely. Actual classifying stages exist exactly when the truncated shapes are constant pro-objects. Local constant shape is a sufficient intrinsic condition. For a locally contractible space all finite stages are its singular Postnikov stages; the full singular shape is obtained from hypersheaves. An unqualified statement about the full ordinary sheaf shape is false, as Carchedi's Example 2.2.4 explains.

9. **Ordinary mixed gluing retains the effective link, not always the geometric one.** The ordinary category has the homotopy pushout through `BK`, for `K = im(H -> G x Q)`. The geometric link model has the pushout through `BH`. Their stable-coefficient discrepancy is the inflation cofiber shifted by `-1`. The sphere with one boundary point is the basic counterexample. This agrees with the parent agent's corrected B.3/B.4 and with the Remords.

10. **The n=5 comparison requires more than aspherical strata.** The ten meridian vectors in `H1(M_0,5,Z)=Z^5` give primitive rank-one and rank-two normal lattices. Every incident pair has Smith invariants `(1,1)`. This kills the fundamental groups of the exit mapping fibres. Goodness of the free-by-free group and the link groups then controls their profinite shapes. A compact-context congruence argument, after a coordinatewise clopen-rectangle refinement in finitely many simplicial degrees, upgrades finite-set representations to coherent diagrams in all pi-finite values. The full proof is coordinated with F.43.

## Manuscript and attached-return reading record

- Read the checked LM_P01 and LM_P02 transcriptions for §§1–4, including every numbered statement and both point-related margins. Read LM_P03 §7, including the struck draft and corrected profinite diamond.
- Independently inspected the actual cote 140-2 images for scans **6, 8, 11, 12, 13, 14, 15, 17, 18**. Review-sized copies are in `sources/`. The scan-30 image was not present among the extracted selected images; its entry in `readings.csv` states that the mathematical decision uses the checked revised transcription and is not an independent palaeographic ruling.
- The reading register has **18 rows**, covering every doubtful reading used by this module. It distinguishes a forced mathematical typing correction from a tentative reading of the handwriting. In particular, scan 11's proposition number is editorially 1.11 because 1.10 precedes it and 1.12 follows; the final handwritten digit is not claimed newly legible.
- Read GALOIS F.1–F.4, F.7–F.8, the relevant B.3 proof, and C.7–C.10. The inherited coefficient-relative results are used only in the stated enhanced/specified-map scope. The unresolved bare ordinary-category reconstruction claim in F.8 is neither assumed nor presented as settled by this package.
- Read the CATHOT C.1–C.4 level-one localization argument and the relevant ind cautions. No pro-topos proof depends on the unresolved ind-representation assertion.
- Read PATHS E.13 and reproduced its shift argument with the finite-quotient consequence and explicit simplicity proof.
- Read STRATA A.1–A.3 and checked the exact Alexandrov/hypercompletion qualification against the primary Aoki and BGH texts.
- Audited root B.3 and C.2. The continuous cohomology proof is valid for the stated torsion scope by coherent inverse-limit continuity; the surjective profinite hole-filling pushout is valid in all ordinary topoi. The generic non-surjective profinite pushout counterexample is not a counterexample to that special theorem.
- Read and independently checked the displayed n=5 vectors and the argument of F.43. Suggested and included the finite coherent-diagram factorization step, including coordinatewise clopen refinement.

## Primary literature verified

All bibliography entries are marked `verified` in the limited sense required by the prompt: the source was actually opened, and the note states the passages used. No entry is an invented reference. The principal exact sources are:

| Source | Exact passages used | Primary URL |
|---|---|---|
| Makkai & Reyes (1977), *First Order Categorical Logic* | Proposition 3.4.8; Theorem 4.2.1; Proposition 4.3.4 | https://sinhp.github.io/files/CT/makkai-reyes-book.pdf |
| Dubuc (2004), *On the representation theory of Galois and atomic topoi* | Theorem 1.1.1; Theorems 3.3.5–3.3.6; Example 3.5.2; Propositions 5.1.2–5.1.4 | https://arxiv.org/pdf/math/0208222 |
| Hoyois (2018), *Higher Galois theory* | Definition 2.3; Remark 2.8; Proposition 2.15; Definition 3.2; Theorem 3.13; Corollaries 3.19–3.20; Theorem 4.3 | https://arxiv.org/pdf/1506.07155 |
| Lurie (2017), *Higher Algebra* | Appendix A, especially A.1.8–A.1.9, A.1.15 and A.4.19 | https://www.math.ias.edu/~lurie/papers/HA.pdf |
| Carchedi (2021), *On the étale homotopy type of higher stacks* | Example 2.2.4; Proposition 2.2.7 and its proof; Proposition 2.2.12 | https://higher-structures.math.cas.cz/api/files/issues/Vol5Iss1/Carchedi |
| Dugger & Isaksen (2004), *Topological hypercovers and A1-realizations* | Theorems 1.1–1.2 in the opened arXiv version; hypercover result is published Theorem 1.3 | https://arxiv.org/pdf/math/0111287 |
| Aoki (2023), *Tensor triangular geometry of filtered objects and sheaves* | Theorem A.6 and **Examples** A.11–A.13 | https://arxiv.org/pdf/2001.00319 ; https://doi.org/10.1007/s00209-023-03210-z |
| Bhatt & Scholze (2015), *The pro-étale topology for schemes* | Lemma 7.4.5; Example 7.4.9; Lemma 7.4.10 | https://www.math.uni-bonn.de/people/scholze/proetale.pdf |
| Stacks Project | Theorem 58.6.2, Tag 0BND | https://stacks.math.columbia.edu/tag/0BND |
| SGA 4 II | Exposé VI, Corollary 8.7.7 with 8.7.1 and Remark 8.7.8 | https://www.cmls.polytechnique.fr/perso/orgogozo/SGA4/tomes/tome2.pdf |
| Barwick–Glasman–Haine (2020), *Exodromy* | §5.1; Theorem 10.1.8; Proposition 11.6.3; Corollary 11.6.6; Proposition 12.6.4; Corollaries 12.6.6–12.6.7 | https://clarkbar.github.io/papers/exodromy_book.pdf |

Searches covered groupoid-topos recognition, Boolean-valued and localic counterexamples, prodiscrete/localic Galois theory, the precise higher Galois hypotheses, hypersheaf versus ordinary shape, Alexandrov comparison, and finite stratified exodromy. These searches and the direct proofs are not presented as a priority investigation.

## Executed computations

`code/foundations_checks.py` uses exact integer/rational arithmetic and SymPy. Its complete output is `code/foundations_checks.output.json`; every assertion passed.

- The finite category in A.10: 3 objects, 7 arrows, all **21** composable associativity triples; two distinct parallel point arrows; terminal object in each representable slice; rational nerve Betti numbers `[1,0,0]`.
- A.20: all permutations on supports of sizes 1 through 6, **873** cases in total; shift-conjugation and parity agree. The explicit normal-subgroup commutator was checked for the **59** nonidentity even permutations on five letters, with two fresh letters.
- A.21: compatibility of the pro-Hom coordinates `a/2^n` with the stage maps and divisibility of the finite-stage inverse-limit coordinates. The infinite statement is proved in the text, not inferred from a bounded search. For the additional strict system, the exponent obstruction was checked at stages 1 through 8 for primes 2,3,5; the formula k=n+1 proves it for every stage.
- E.7: the cellular ranks and Betti numbers of the sphere and the point, displaying the degree-two discrepancy.
- E.8: factorial transition maps annihilate finite positive-degree coefficients for moduli 2 through 12 and degrees 2,4,6,8. The all-modulus result is the displayed divisibility proof.
- E.12: all **15** compatible meridian pairs, their exact Smith invariants, and a specific unit minor for every pair.
- E.13: joins of two-point sets for ranks 0 through 4, with all simplex counts and exact mod-2 Betti numbers, confirming the finite stages are spheres.
- `code/build_registers.py` generated the exact requested CSV headers and checked that their **36** statement IDs match the ordered LaTeX paragraphs: A.1–A.22 and E.1–E.14. Its output is included.
- `code/finalize_fragments.py` records the mechanical insertion of section/folio/scan references and the status/longtable normalization; its output is included. It is an editorial helper rather than mathematical evidence.

## Integration and limitations of this module's verification

The fragments require the standard AMS mathematics/proof packages and `longtable`, with no custom statement macro. E.14 is deliberately a multipage `longtable`. Mathematical labels are manual `A.n` and `E.n`; the CSV records one row for every such statement. The parent owns the unified bibliography, LuaLaTeX build, overflow correction, PDF rendering, final statement audit, and checkpoint saving. This module does not claim a standalone PDF typesetting check. Parent compilation and final visual checks should supply those counts in the integrated report.

The all-level decisions are for the precise language specified in E.1–E.14. In particular, no ordinary point category is silently enriched with a topology, no arbitrary strict pro-presentation is silently identified with an intrinsic fundamental pro-groupoid, no finite-coefficient comparison is called an unrestricted shape equivalence, and no unenhanced reconstruction question from GALOIS F.8 is used as a premise. These are scope decisions with positive replacements and explicit counterexamples, not unresolved A/E tasks.
