# Advisory post-freeze review: convolution and rearrangement leaves

This report uses only the frozen page files and the supplied textual context, not the manuscript images. No transcription file was changed. `context/notes/RESULTS_STATE.md` explicitly says that there are **0 matching open, settled, intake, research-note, or planning-register rows** for these folders; therefore no relevant result ID can honestly be attached to the items below. All contextual readings are credited to **Hua, modernised reading of cote 68**, an AI-produced interpretation supplied in `context/hua_project/68.modern.tex`, not an authoritative transcription or an established result of this project.

Hua's “pages 14–21” correspond here to supplied scans 015–022; these are contextual page locators, not a finding of authorial page numbering. Candidate labels C01–C17 below are local labels for this advisory report only, never RESULTS_STATE IDs. The parent should select, merge, and verify the useful candidates; the notes are not substitutes for the manuscript-reading judgments.

## Candidate notes

### C01 — Scratch profiles have a concrete interpretation

**File/scan:** 68/015–016, numeric arrays and boxed `3 2 2 2`. **Kind:** unpursued implication. **Register:** no matching result ID. **Context:** Hua §IV, “Les brouillons (pages 14 à 16)” (lines 957–976), **restates and checks**.

Hua interprets the strings of integers as sorted convolution multiplicities and explicitly labels this interpretation his project's own; the frozen scans supply the corresponding arrays and the identity ending `2G+{u}`. Independently recomputing in `G=Z/4`, with `V_1={0,2}`, `x=1`, `u=2`, and `E=V_1∪{x}`, gives `1_E*1_E=2·1_G+δ_2`, profile `(3,2,2,2)`, so that particular contextual interpretation is supported. The checks do not decide the difficult indices, adjectives, or crossed-out signs of scan015.

### C02 — E/F products: model and asserted positivity

**File/scan:** 68/017, upper formulas `E_i`, `F_i`, and three product expansions. **Kind:** unproved claim. **Register:** no matching result ID. **Context:** Hua §IV, “Les brouillons” (lines 978–990), **restates with an explicit qualification**.

The page asserts positive-coefficient product expansions but gives no proof there, and the frozen interval formula for the second family has an unresolved `F_i|F_j` index. Hua reconstructs the model as `G=Z/(2m+1)`, with odd and even interval families; that ambient group identification is an interpretation, not a formula displayed in the frozen page. Finite checks for cyclic orders 3, 5, 7, 9, and 11 support all three positive-cone patterns in that reconstruction, but a general counting argument and the relation to the later axioms still deserve a separate proof.

### C03 — A family of sets is not automatically its positive cone

**File/scan:** 68/017, upper inclusion and lower condition c). **Kind:** reading question. **Register:** no matching result ID. **Context:** Hua §IV, “Les brouillons” (lines 991–1005), **differs**.

The upper formula literally places `A(tilde g)*A(tilde h)` in `A(tilde g·tilde h)`, while the lower axioms send a product to the separately defined cone `C(tilde g tilde h)`, and use `B(tilde h)` for the second factor. Hua regularizes the lower formula to two A-families and the cone, a coherent reconstruction which should not erase the page's distinction. If both A-families literally consist of indicators, the top inclusion needs another interpretation: even `1_{[-1,1]}*1_{[-1,1]}` has coefficient 3 at zero and is not itself an indicator.

### C04 — The context adds surjectivity

**File/scan:** 68/017, reversed-orientation homomorphism and kernel; 68/022, bottom exact sequence. **Kind:** reading question. **Register:** no matching result ID. **Context:** Hua §IV, “Les brouillons” (lines 991–1016), **differs**.

The frozen page gives a homomorphism `tilde G --rho--> G` and `i:{}_2G ≃ Ker rho`, without a surjectivity assertion, whereas Hua calls the homomorphism “surjectif” and reads the letter as eta. The isolated sequence `0→{}_2G→G --2-->G` in 022 has no terminal zero; it therefore does not by itself assert surjectivity of doubling, which would fail for `G=Z`. The interpretation of tilde G as a group of half-centres is a useful contextual proposal, but its construction and exact hypotheses remain open on these supplied leaves.

### C05 — The repeated adjective is a substantive reading question

**File/scan:** 68/020, title, definition, corollary; 021, top and implication; 022, top margin. **Kind:** reading question. **Register:** no matching result ID. **Context:** Hua §IV, “Couples prétassés (pages 19 et 20)” (lines 1090–1124), **differs**.

The frozen transcription's low-confidence reading is `pritorisé|priorisé`, with `privilégié` also listed in the doubt register; Hua instead reads **“prétassé”** at the same repeated places and explicitly says this is the word on the page. This contextual lead fits the paired stronger term in Hua's next subsection, but remains a proposed reading to test against the ink in a later edition, not a correction to the now-frozen text. Hua also reads the inserted prefix in 022 as “pré”, where the frozen version has “pri”.

### C06 — “Bons” versus “tassés” must likewise stay unresolved

**File/scan:** 68/021 §4 and corollary; 022 d) and the overwritten bracket labels. **Kind:** reading question. **Register:** no matching result ID. **Context:** Hua §IV, “Couples tassés, et la condition K (pages 20 et 21)” (lines 1147–1175, 1215–1234), **differs**.

The frozen transcription reads “Couples bons”, “bon”, and cancelled “bon” followed by inserted “pri”, whereas Hua explicitly claims “Couples tassés”, “tassé”, and the addition of “pré” over “tassé”. This is not merely a difference of modern notation: the two interpretations disagree about the literal word and the state of the insertion. The research discussion can identify the two notions by their formulas—peak extremality and full weak-majorization extremality—without silently choosing either wording.

### C07 — First partial sum: conditional endpoint issue

**File/scan:** 68/019, condition c), TeX lines 38–40. **Kind:** reading question. **Register:** no matching result ID. **Context:** Hua §IV, “La relation f′≺f (pages 18 et 19)” (lines 1063–1081), **adds a minimal check**.

Hua notes that summing from 0 through `n` with `n∈N*` misses the one-entry inequality, and deliberately modernizes the indexing. The frozen page instead preserves the uncertainty `N^{*|0}`: if the zero reading is right there need be no omission; if the star reading is right, `f′=(2,0)` and `f=(1,1)` satisfy all sums through `n≥1` but violate the largest-entry test `2≤1`. This concrete conditional counterexample explains why the tiny exponent matters without repairing it.

### C08 — Small witness to the manuscript's noncommutative doubt

**File/scan:** 68/020, “Il n'est pas clair que la relation soit symétrique”. **Kind:** own idea. **Confidence:** high, by explicit six-element multiplication and the subgroup calculation below. **Register:** no matching result ID. **Context:** Hua §IV, “Couples prétassés” (lines 1118–1125), **adds an explicit witness to its assertion**.

In `G=S_3`, let `H={e,(12)}`, `s=(123)`, `A=H`, and `B=Hs`: then `1_A*1_B=2·1_{Hs}` has peak 2, equal to the rearrangement pairing, whereas `1_B*1_A=1_{HsH}` has four coefficients equal to 1 because `H∩sHs^{-1}={e}`. Thus reversing the factors destroys peak extremality, resolving the quoted doubt negatively in this example, while respecting the manuscript's qualification for commutative G. The same example distinguishes the order of a “good” pair: the profile `(2,2)` weakly majorizes every convolution of two two-point indicators, while `(1,1,1,1)` does not.

### C09 — The self-pair criterion has a proof in the context

**File/scan:** 68/020, corollary `check f=epsilon_s*f`. **Kind:** unproved claim. **Register:** no matching result ID. **Context:** Hua §IV, “Couples prétassés” (lines 1126–1139), **restates; no new proof claimed**.

The manuscript states the self-pair criterion without proof on this leaf; Hua's project supplies the argument using comparable level sets of equal finite cardinality, forcing equality at each level. The equality of the left-translation and right-translation formulations with the same element follows on applying reflection to the first equality, so commutativity is not needed for this particular equivalence. This supplied proof should be credited to Hua's modernised reading and kept separate from the manuscript's own proof state.

### C10 — Peak extremality does not imply the stronger condition

**File/scan:** 68/021, “Cela implique que ...” after c′). **Kind:** unpursued implication. **Register:** no matching result ID. **Context:** Hua §IV, “Couples tassés, et la condition K” (lines 1176–1189), **restates and independently checks Hua's example**.

Hua's own counterexample uses `A={0,1,3,4}` and `I={0,1,2,3}` in Z: self-symmetry makes the A-pair peak-extremal, but the largest two entries of `1_A*1_A` sum to 6 while those of `1_I*1_I` sum to 7. A direct finite recomputation confirms these numbers, so the implication written on 021 is genuinely one-way in that interpretation. The example belongs to Hua's project and is not a new finding of this review.

### C11 — Why the cardinality hypothesis in K is essential

**File/scan:** 68/021, cardinality insertion and condition K; 022, top margin. **Kind:** unproved claim. **Register:** no matching result ID. **Context:** Hua §IV, “Couples tassés, et la condition K” (lines 1191–1214), **restates and sharpens the proof obligation**.

The inserted condition that S contain an indicator of every admissible finite cardinality permits the third factor to test every partial sum of a convolution, explaining the passage from peak inequalities for all products to full weak majorization. One must use both cardinality richness and pairwise peak extremality to identify `||f*g*A||∞` with the corresponding rearrangement pairing; testing just a single cardinality cannot recover all partial sums. The margin at the start of 022 again refers to K and the weaker pair condition, so the scope of those hypotheses should be retained when reading the subsequent level-set argument.

### C12 — Conditional proof of level-set closure, contrary to Hua's unconditional dismissal

**File/scan:** 68/022, b) “les E_alpha(f)∈S_0” and its bracket. **Kind:** own idea. **Confidence:** high for the stated conditional argument; the scope of K in the manuscript is a separate reading issue. **Register:** no matching result ID. **Context:** Hua §IV, “Couples tassés, et la condition K” (lines 1228–1234), **qualifies/disagrees with the footnote saying this does not follow**.

Assume translation stability, all pairs peak-extremal, and the cardinality part of K, and take a nonempty level `A=E_alpha(f)` of size n; choose an indicator `B∈S_0` with `|B|=n`. Peak extremality of `(f,B)` makes A comparable with a translate of `check B`, hence equal to it, and self-extremality of `(B,B)` makes `check B` a translate of B, giving `A∈S_0`. Thus the manuscript's bracket can support a deduction if the K hypothesis from 021 and the top margin is still in force; Hua's “does not follow” is too strong under those hypotheses, although it is correct that the deduction is not justified from mere closure properties.

### C13 — A small example when K is absent

**File/scan:** 68/022, the same level-set claim. **Kind:** own idea. **Confidence:** high, from an explicit formula on Z/3. **Register:** no matching result ID. **Context:** same subsection and footnote as C12, **adds a boundary example**.

In `G=Z/3`, put `f=δ_0+1_G=(2,1,1)` and let S consist of all translates of all convolution powers `f^n`, `n≥0`; then `f^n=δ_0+((4^n−1)/3)1_G`, so S is closed under convolution and translation and every pair is peak-extremal by aligning the distinguished point. Its only indicators are singletons, but `E_1(f)=G`, so level-set closure fails. This is a counterexample after the cardinality condition K is dropped, not a counterexample to C12 or to a reading of 022 that retains K.

### C14 — The final common-intersection step needs a nonempty-level convention

**File/scan:** 68/019, unfinished definition of E_*; 022, double-underlined “Supposons” and final intersection. **Kind:** reading question / unproved claim. **Register:** no matching result ID. **Context:** Hua §IV, “Couples tassés, et la condition K” (lines 1236–1247), **adds a missing qualification**.

If all positive thresholds are included in `E_*(h)`, then levels above `max h` are empty and the displayed intersection in 022 is empty, even for a nonzero h; the definition of E_* on 019 is unfinished and does not explicitly remove these levels. If E_* means only the nonempty levels of nonzero finite-support convolutions, a chain has nonempty intersection immediately: choose a member of least cardinality, which must be contained in every other member. The substantive unproved step is therefore the double-underlined supposition that all product level sets form one common chain, together with the needed nonempty-level/zero-function convention, rather than a difficult compactness argument after that supposition.

### C15 — The chain hypothesis is stronger than individual chain structure

**File/scan:** 68/022, `bigcup E_*(A_i*B_j)` totally ordered. **Kind:** unproved claim. **Register:** no matching result ID. **Context:** Hua §IV, “Les brouillons” and “Couples tassés, et la condition K” (lines 995–1005 and 1236–1247), **adds a proof target**.

Each single function has nested superlevel sets automatically, but this does not order the level sets of different products `A_i*B_j` against one another. The common-centre and compatibility axioms in 017 are a possible mechanism for a common cone, yet 022 explicitly marks the joint-chain property as “Supposons” rather than deriving it. A next proof should show exactly which 017 axioms force common nesting and thus closure of the proposed enlarged class under convolution.

### C16 — Pairing placement differs between the frozen reading and context

**File/scan:** 68/020, annotation under `(f*g)(s)`, TeX line 26. **Kind:** reading question. **Register:** no matching result ID. **Context:** Hua §IV, “Couples prétassés” (lines 1095–1106), **differs**.

The frozen reading has `⟨f [*|,] epsilon_s check g⟩` with an unresolved product/comma, whereas Hua's footnote says the page writes `⟨f*epsilon_s,check g⟩` and moves the translation to obtain the modern identity. These placements are materially different on a noncommutative group, so the context supplies a specific future reading question rather than license to normalize the formula. The displayed equivalence of left- and right-oriented level-set formulations on the page may help a later comparison but cannot override the frozen reading.

### C17 — Contextual links beyond the supplied manuscript

**File/scan:** 68/021–022, full-product and finite-indicator inequalities. **Kind:** unpursued implication. **Register:** no matching result ID. **Context:** Hua §IV, “Couples tassés, et la condition K” (lines 1215–1227 and 1249–1262), **restates as an unverified contextual lead**.

Hua's project links K to rearrangement inequalities and the finite cyclic indicator statement to a capped-multiplicity formulation associated with Pollard, while explicitly saying the manuscript cites none of those works. Those attributions are leads for a separate primary-source literature check; this review has not verified the historical references or imported their theorems. The pages add their own incomplete centre-and-chain construction, which should be studied on its stated hypotheses instead of being treated as already covered by those contextual names.

## Check record

`convolution_examples.py` performs exact small computations and writes `convolution_examples.json`. It checks the S3 noncommutative example, Hua's peak-versus-full-majorization example, the order-four scratch profile, 270 E/F products across five odd cyclic models, and 25 products in the no-K Z/3 family. The scripts supply computational evidence for the explicitly finite claims only; they neither inspect handwriting nor prove the general E/F theorem or historical identifications.

## Final main-note QA

Reviewed R01–R22, the source key, and the verification paragraph at 2026-11-17 20:50:19 UTC. Main-note SHA-256 at review: `11517f9c0f1a15b99d49334cd1f5e040c0b574421fdca0332056d400e6690beb`.

No substantive mathematical error found: R15 has the necessary assumptions, R16 and the S3 examples are correct, R19 is valid as an explicitly conditional argument for the normalized cone axioms, and finite computations are not promoted to general proofs. Suggested one notation clarification in R05: label the doubling arrow explicitly, rather than a superscript-looking 2 on its target. Noted that Hua’s 2026-09-23 revision header explicitly records a facsimile reread changing its earlier “préféré”/“bornés” to “prétassé”/“tassé”, relevant evidence for R06/R12. No image was opened, no broad new test was run, and no main-note or transcription file was changed by this review.
