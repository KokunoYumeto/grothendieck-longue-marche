# Opened sources for Parts D–E

All entries in `DE_refs.bib` are marked verified. The following list records the exact material used, not a general reading list. Mathematical proofs in `sections/DE_agent.tex` give the comparison maps and check the hypotheses. Author drafts are identified as drafts.

| Key | Exact source opened | Statement actually used | Hypotheses checked / role |
|---|---|---|---|
| DE_StacksPurity | https://stacks.math.columbia.edu/tag/0BMB | Lemma 58.21.4 (Tag0BMB) | Normal source local ring; regular target local ring; quasi-finite; equal positive local dimensions; unramified at source codimension-one generizations. Applied to finite normalizations of regular models. |
| DE_Temkin | https://math.huji.ac.il/~temkin/teach/math583/notes.pdf | Theorem2.7.6; Theorem3.4.4; Corollaries3.4.6,3.5.3 | Henselization and strictly henselian tame extension classification. In residue characteristic zero wild inertia is trivial. Every character pairing is written in D4. |
| DE_KuhlmannTame | https://fvkuhlmann.de/MTHTVF.pdf | Section2.2; Corollary2.9; Theorem1.2 | Defect formula and defectlessness in residue characteristic zero, used in D4 splitting. Dated14March2014 author manuscript. |
| DE_KuhlmannHensel | https://www.fvkuhlmann.de/bookch9.pdf | Theorem9.44 and Corollary9.45, pp240–241 | Independent nontrivial henselian valuations force separable closure; incomparable henselian valuations have separably closed common-coarsening residue. The proofs were read. Draft has unrelated unresolved cross-references; none is used as an asserted theorem. |
| DE_HJP | https://www.tau.ac.il/~jarden/Articles/paper78.pdf | Lemma7.1, Proposition7.3(a), pp44–46 | Splitting of the residue Galois homomorphism for a henselian valued field. D4 also proves the characteristic-zero case directly by a maximal unchanged-residue extension. |
| DE_Hoshi | https://www.ms.u-tokyo.ac.jp/journal/pdf/jms210201.pdf | Proposition2.4(i)–(ii), pp169–170; Lemma2.8, pp175–176 | Connected noetherian separated normal characteristic-zero base, hyperbolic polycurve and compatible fiber. Trait extension criterion and injective fiber sequence. |
| DE_BES | https://www.math.uni-frankfurt.de/~stix/research/preprints/BORNE_EMSALEM_STIX-lifting_short20150324.pdf | Proposition8 and proof; Remark9; Proposition16 and proof; Theorem27 | Torus torsor over geometrically connected geometrically unibranch characteristic-zero variety; exact homotopy sequence and Chern transgression. E4 independently proves finite-cover/nth-root criterion. Theorem27 has positive-genus and torsion-packet hypotheses and gives only a cuspidally central lift; these limitations are checked in ZD10. |
| DE_Bresciani | https://link.springer.com/article/10.1007/s00222-023-01220-6 | TheoremsA,B,C; Lemma23 | Smooth geometrically connected curve over a field finitely generated over Q; TheoremA uses birational liftability after k(t) base change. ZD11 proves how universal manuscript lifting implies and is implied by universal geometric/cuspidal classification. |
| DE_Bresciani PDF | https://ricerca.sns.it/retrieve/e8dd3446-30ed-4281-868b-2e63a94c233f/Bresciani%20-%20On%20the%20birational%20section%20conjecture%20with%20strong%20birationality%20assumptions.pdf | Publisher text checked against repository PDF | Inventiones235(2024),129–150; online26September2023. |
| DE_CyclotomicReturn | Attached `new_results/CYCLOTOMIC_KERNEL_return/` | B6–B8,C6,C8 | Reread actual arguments; D9 uses their explicit quotient/centralizer calculations. C8's nonzero diagonal does not imply E4 left exactness; E5 computes the obstruction. |

## Manuscript reading coverage

The entire section4 transcription, scans105–136, was read, including all comments, margins, deletions, and doubtful alternatives. Named F rows are covered by D1–D10 and E1–E6. Additional substantive claims are covered by ZD1–ZD11. Every supplied section4 scan image was visually inspected: scans116,119,120,122,123,124,126,127,130,131,133,134,135. Images of scans105–115,117–118,121,125,128–129,132,136 are not supplied among the attached section4 images, so no claim of visual checking of those pages is made.

## Additional source searches and rejected shortcuts

- Riemann–Zariski searches found Temkin's `Relative Riemann–Zariski spaces`, https://math.huji.ac.il/~temkin/papers/RZ.pdf, Theorem3.5.1 on stability of open domains under finite unions. ZD4 instead gives the direct common-model proof in the exact setting of the manuscript, and a self-contained nonscheme argument.
- Temkin's Exercise2.7.9 asserts a decomposition-normalizer identity too broadly for the arbitrary valuations at issue. It is not used. D10 proves the exact alternatives; divisible-group examples show why the trivial-decomposition case needs separate treatment.
- Searches for current birational section/cuspidalization results checked Bresciani2024 against results published in2025–2026. None of the opened results supplies the arbitrary splitting in ZD10. No conjectural result is used as a premise.
- Nakamura1994, Theorem(2.1.1), pp94–97, was opened from `sources/AB/Nakamura_1994.pdf` for a cross-audit of F17.4. Its cyclotomic-normalizer conditions match the node subgroup construction; the audit message specifies the root-product compatibility.

## No priority claim

The explicit proofs and counterexamples are AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. Source searches are recorded to distinguish checked literature inputs from calculations performed for this return.
