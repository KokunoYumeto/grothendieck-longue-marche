# Supplementary research-coverage review

## Scope

Reviewed the frozen per-page TeX, the 22 LF items, the 24 algebra items, the current main-note scaffold, and exact contextual passages. No source image was viewed; no frozen transcription, page, or doubts file was edited. The following additions prioritize substantive gaps rather than expanding every reused exercise. `CT` and `CN` mean `context/MPL_16+47+54+44_transcription.tex` and `context/MPL_16+47+54+44_notes.md`; both remain unreviewed first-pass witnesses/leads.

## Recommended additions

### S01 — Finite-prime avoidance needs neither comaximality nor infinite residue fields

**Witness:** `pages/MPL_60_036-070_60_scan052.tex`, L22–26; `pages/MPL_60_036-070_60_scan048.tex`, L4–12. **Kind:** unpursued implication. **Quote:** “deux à deux distincts”; “Card(A/p) ≥ 2”; “distincte de λ(p)”. **Context comparison:** searches for avoidance/Chinese remainders found no matching result in CT/CN; CT16/052's Fitting/different outline and CT54/004–006's generic-flatness discussion are different constructions. **RESULTS:** no directly matching theorem; **WG2 §2.4 #3** and **MPL_15_195-228+18_002-017 R01** apply only to scope/provenance, respectively an unchecked plan and first-pass lead.

**Proposed item (3 sentences):** The proof first solves the finitely many bad fibres after semilocalization, then avoids one prohibited scalar at each remaining exceptional height-one prime. The stated avoidance lemma requires distinct primes, not pairwise comaximal ideals, and the later use needs only two residue values, so neither a global Chinese-remainder prescription nor an infinite residue field may be silently assumed. This adds a constructive local-to-global mechanism absent from the supplied Fitting and generic-flatness context.

### S02 — A saturated rank-one submodule need not be a global summand

**Witness:** `pages/MPL_60_036-070_60_scan050.tex`, L4–14; `pages/MPL_60_036-070_60_scan048.tex`, L6–12; compare current `pages/MPL_60_036-070_60_scan064.tex`, L4. **Kind:** own idea / unpursued implication. **Quote:** “M/Ax soit sans torsion”; “facteur direct ... pour tout p”. **Context comparison:** **CT16/009**, primitive decomposition (6.4), and **CN16:9:3–4** concern primitive Lefschetz summands, not a primitive vector in a lattice; **CT16/049** discusses conditional algebraic splittings in a different category. **Relation:** differs and adds a separating example. **RESULTS:** **WG2 §2.4 #3**, **MPL_14_087-132 M09**, and **MPL_15_195-228+18_002-017 R01** remain unchecked/first-pass comparison leads.

**Proposed item (3 sentences):** The constructed element is primitive at every height-one localization, which makes its quotient torsion-free under the source's standing hypotheses, but this does not make it a unimodular element of the global module. For A=k[X,Y] and x=(X,Y) in A², the quotient A²/Ax is isomorphic to (X,Y) and is torsion-free, while Ax cannot split off globally because no coefficients a,b satisfy aX+bY=1. **Confidence: high**, from the explicit kernel/cokernel calculation; this is distinct from Lefschetz primitive decomposition and from the contextual hope for algebraic splittings of motives.

### S03 — The reduction theorem isolates a rank-one ideal; Dedekind projectivity supplies the splitting

**Witness:** `pages/MPL_60_036-070_60_scan048.tex`, L14; `pages/MPL_60_036-070_60_scan046.tex`, L4–6 and L16–24. **Kind:** unpursued implication. **Quote:** “M/L ... isomorphe à un idéal de A”; “puisque L₁ est libre”; “M est projectif”. **Context comparison:** **CT16/049** and **CN16:49:3–5** concern conditional semisimplicity of algebraic correspondences, not projectivity of finite torsion-free modules over Dedekind rings; **CT16/052** mentions different/Fitting ideals without this rank reduction. **Relation:** adds a separate algebraic reduction and differs from motivic semisimplicity. **RESULTS:** **MPL_14_087-132 M09**, **WG2 §2.3 #7**, and **WG2 §2.4 #3**, all first-pass leads or unchecked plans; no supplied settled result directly applies.

**Proposed item (3 sentences):** The induction splits the intermediate extension by the free module L₁, obtaining a free submodule of rank n−1 and a rank-one ideal quotient, but it does not assert that the final extension by that ideal splits over the original higher-dimensional normal ring. In the following Dedekind specialization the ideal is projective, so the same reduction yields M≅A^{n−1}⊕I and places the remaining obstruction in the ideal class of I. This complements A04/A05/A18 and must not be read as a semisimplicity theorem for all modules or for motives.

**Source-completeness caveat:** The reused sequence jumps from internal **4-38** (scan052) to **4-40** (scan050): the proof of Lemma6, the opening of Lemma7, and the full statement associated with the later “th.6” cannot all be recovered from this selection alone. The surviving pages support the mechanism and conclusion described above, but a scholarly reconstruction must retain the omitted-source-hypothesis boundary rather than reconstructing the missing page as though it were transcribed.

### S04 — Boundary duality supplies the one-unit shift

**Witness:** `pages/MPL_60_036-070_60_scan061.tex`, L4–16 and L19–26. **Kind:** own idea / unpursued implication. **Quote:** “en cat. dérivée”; “au décalage d'une unité près”. **Context comparison:** **CT47/011**, remark4, and **CN F20** concern proper Fourier-transform duality; **CT54/003–007** and **CN D01–D05** concern abelian de Rham/Cartier duality. **Relation:** adds a boundary-specific consequence, differing from those settings; lexical searches located no earlier boundary-cone construction. **RESULTS:** no direct matching result; **MPL_14_002-044 A36** is only a first-pass convention comparison, and **LM7 E.23** is unrelated.

**Proposed item (3 sentences):** In a fixed derived enhancement, let B_f(F)=Cone(Rf!F→Rf*F), and assume the usual Verdier-duality identifications are compatible with this canonical map. Dualizing its triangle gives D_S B_f(F)≅B_f(D_XF)[−1], since the dual of a cofiber is the corresponding fiber. **Confidence: high conditional on those six-operation hypotheses**, because the shift follows formally; this supplies a precise meaning for the page's one-unit-shift remark without repairing its doubtful connecting exponent or attributing the full independence-of-compactification proof to the manuscript.

### S05 — The discarded weight-range formulation is replaced by structured factors

**Witness:** `pages/MPL_60_036-070_60_scan065.tex`, L13–19 and L23–27; `pages/MPL_60_036-070_60_scan067.tex`, L2–13. **Kind:** withdrawn formulation in the same text / reading question. **Quote:** cancelled “L(0)=1” and “racines et pôles”; live “se permet de ... corriger”; “niveau ≤ ρ+n−1”. **Context comparison:** **CT16/017** and **CN16:17:4–5**, the cancelled/negated uniqueness attempt for a homomorphism determined by L alone, shows a separate substantive revision; it does not supply the present level definition. **Relation:** adds an internal revision, not a contradiction of the context. **RESULTS:** **MPL_14_087-132 M05** and **MPL_15_195-228+18_002-017 M03/P09** are first-pass convention leads; **WG2 §2.4 #3** remains an unchecked plan.

**Proposed item (3 sentences):** The simple absolute-value/range formulation, including L(0)=1, is struck through on065 and followed by a structured factorization, with the permitted correcting factors restricted further on067. Thus the cancelled normalization and bounds should not be carried into the later argument as live hypotheses without separate support. This records a withdrawn formulation, not a proof that its mathematical content is false, and complements LF20's analysis of the remaining lower-level problem.

## Optional addition if space permits

### S06 — Two free lattices encode the reflexive lattice

**Witness:** `pages/MPL_60_036-070_60_scan068.tex`, L13 (exercise3). **Kind:** unproved claim in reused exercise / unpursued implication. **Quote:** “M=L∩L₁”; “l'ensemble fini ... tels que L_p≠M_p”. **Context comparison:** no matching reflexive-lattice construction was located in CT/CN; **CT16/014–015** concerns an integral correspondence algebra, and **CT54/004–006** concerns generic flatness, so the comparison is one of difference. **RESULTS:** **WG2 §6. #9** is an unchecked plan about integral Lefschetz operators, not this assertion; no direct settled result applies.

**Proposed item (2 sentences):** The exercise asks for a stronger finite description than A07's finite-subfamily intersection: a reflexive lattice already contained in one free lattice is to be recovered as that lattice intersected with a second free lattice, constructed by matching finitely many height-one localizations and clearing denominators away from them. This suggests finite gluing data for the module, without asserting that the intersection itself is free or projective, and the proof request belongs to the reused source rather than to Grothendieck's handwritten conjectures.

## Standing-question and pagination review

### Unverified or unfinished steps

- The scaffold correctly separates an author's `?` from a transcriber's `\unsure` and correctly refuses to treat every “Montrer que” as Grothendieck's personal doubt.
- Its explicit entries for **037**, **053**, **055**, **059**, and **063–067** cover the materially unfinished handwritten proposals visible in the frozen text.
- **061:L26** is an asserted shift qualification, not an author-drawn question mark; add S04 to the research register rather than misclassifying the transcriber's uncertain index as an authorial “à vérifier”.
- **067:L13,20** explicitly supplies hypotheses. The scaffold already says so; preserve that wording rather than counting them as independent conjectures or proof gaps.
- For the global/local distinction in **LF07**, retain the local-category qualification developed in `records/context_research.md`, §2: the D-stable factors need not arise globally, although the local-cohomology formula supplies the usual local additivity.
- Replace the scaffold's selective list “Cancellations on043,049,051,065,067,069...” by “Cancellations throughout the selection...” or clearly label it illustrative: substantial cancellations also occur on039,041,045,047,053,055,057,061,063.
- The strongest register link for **LF03** is **MPL_7_061-072+8_001-078 Scan 061 (§66)**, internal **T.01**; for **LF09** it is **MPL_15_195-228+18_002-017 B03**. Both remain first-pass leads, but are more directly relevant than a generic planning entry.

### Titles, counts, and source sequence

The scaffold's counts agree with the frozen files and inventory: **35 scans; 17 handwritten-text sheets; 18 reused typed sheets; 18 occurrences of n°392 on those typed sheets; all numeric margins from35 through69 present once in the corresponding scan**. All listed internal typed headers agree with the page files. Physical placement, pencil medium, and authorship of those marks were not independently assessed by this reviewer, who did not inspect images.

The six listed title/heading entries are correctly treated as headings rather than separate title sheets: **039:L4**, **049:L2**, **061:L2**, **046:L8**, **052:L18**, and **068:L3**. There is no explicit total-page-count statement in the frozen text; the source gap at internal4-39 is correctly noted, and does not authorize changing scan order. The `-:-:-:-` ornaments at **062:L10** and **070:L6** are separators, not additional titles or page counts.

No additional substantive handwritten topic appears absent once LF01–LF22, the μ consistency caveat, and S04/S05 are included. The principal remaining coverage gap in the algebra register is the constructive primitive-vector/reduction argument, addressed by S01–S03; the optional S06 is useful but not required to turn the notes into a solution manual for all exercises.
