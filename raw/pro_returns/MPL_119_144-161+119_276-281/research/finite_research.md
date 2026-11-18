# Finite-geometry research support

Prepared after the transcription freeze by the finite-research subagent, GPT-6 Astra; run `finite_research`, 18 November 2026. The execution environment does not expose a separate effort setting, so none is asserted. No scan was viewed and no transcription file was edited: the evidence compared here is the root reader's frozen transcription and the supplied context.

These are candidate research notes and their verification support, to be integrated by the root reader. They are not a second transcription or a second visual audit. The identifiers F01–F20 are provisional and can be mapped to the final notes' identifiers.

## Sources and status

The supplied `context/hua_project/119.modern.tex` is credited throughout as **Hua, modernised reading of cote 119**, not as a transcription or an established result. Its page numbers are one below the present scan numbers: its pp. 154–160 correspond to scans 155–161. Context subsection locators below include exact file lines so the distinctions can be checked in the supplied file.

`context/notes/RESULTS_STATE.md` contains no registered theorem on the precise affine-plane incidence axioms, the small group extensions, or the outer-S6 dictionary. The nearest entries it explicitly flags are **LM4 D.12** and **LM4 F.7** (both Open, return's claim, lines 396 and 402, from `LM4_FINITE_GROUP_ACTIONS_results.csv`), and **LM4_SUCCESSOR B.38/B.39** (Open, return's claim, lines 405/412, from `LM4_SUCCESSOR_results.csv`). These concern profinite torsion or centralizers; none is proved or refuted by the elementary finite computations here. **IMPL P3** (candidate prompt item: Open, line 401, from `IMPLICATIONS.md`) and **EXIT_TOWER E.24** (Open, return's claim, line 399, from `EXIT_TOWER_results.csv`) occur only as limits on possible links to the tower.

Every candidate had its own context search. The actual queries and hits are retained in `finite_context_search.tsv`; absence of an exact register entry is a search result, not an assertion that the wider archive lacks the subject. The full source registers referenced by RESULTS_STATE were not supplied and were not opened.

## Candidate notes, each one to four sentences

### F01 — Cote 119, scan 159, A), second display line — reading question

The frozen reading quantifies over “∀ a,b∈E” without a distinctness condition, so taking a=b gives |a∩a|=3>1 and makes A) literally impossible. Hua, modernised reading of cote 119, “Trialité des bi-ditriades” (`119.modern.tex`, lines 804–813, his p. 158), silently treats the requirement as pairwise intersection of distinct triples; the note should preserve the frozen quantifier and explicitly distinguish that repaired mathematical reading. No exact RESULTS_STATE entry concerns this issue; LM4 D.12 is only a remote finite-group connection and remains Open.

### F02 — Cote 119, scan 159, A), whole displayed criterion — unproved claim

With a≠b added as an explicitly external refinement, the twelve triples contain 12·3=36 distinct unordered pairs, exhausting the 36 pairs of nine points and hence giving a Steiner triple system. Hua, “Trialité des bi-ditriades” (`119.modern.tex`, lines 804–813), already supplies this counting argument and identifies the unique system with AG(2,3); the present check adds an exhaustive enumeration of all 840 labelled systems and verifies that all belong to the orbit of the affine plane, rather than claiming a new classification. The computation is ordinary reproducible Python, not a proof-assistant certificate, and no exact RESULTS_STATE theorem settles this finite statement.

### F03 — Cote 119, scan 159, B), marginal NB and final NB — unproved claim

The assertions “b) résulte de a) et c)” and “exactᵗ 3 ‘droites’” do follow from a) and c): projection to any two classes identifies V with their nine pairs, while a fixed point belongs to three blocks. For a fixed block D, its four points each lie in two further blocks, all eight are different by c), and these are the eight other blocks, proving b). This completes the short argument reported but not fully expanded by Hua, “Trialité des bi-ditriades” (`119.modern.tex`, lines 815–834); no exact RESULTS_STATE entry is involved.

### F04 — Cote 119, scan 159, final NB, “c implique déjà que card V=9” — unproved claim, refuted as a stand-alone implication

Hua, “Trialité des bi-ditriades” (`119.modern.tex`, lines 825–834), objects that c) alone does not imply |V|=9, and this remains correct even with the manuscript's four-element-block hypothesis retained. For four disjoint triples E₀,…,E₃, take the eighteen blocks Eᵢ∪{b}, one for every i<j and b∈Eⱼ: each cross-class pair occurs exactly once, but |V|=18. This explicitly checked counterexample refines the condition to a)+c) as in F03; it does not refute the intended affine-plane model or change any RESULTS_STATE status.

### F05 — Cote 119, scan 159, upper and lower margins — unpursued implication

The construction “Ê=E∐{∞}” and the four new blocks Eᵢ∪{∞} complete the incidence structure to thirteen points and thirteen four-point lines, with unique join and meet. Hua, “Trialité des bi-ditriades” (`119.modern.tex`, lines 836–843), explains the duality with PG(2,3) minus a point, but its final footnote instead reports a doubtful “E≅V∐{∞}”; the frozen reading supplies separate hatted sets and their full completion rule, so that footnote should not control the transcription. The complete finite incidence check supports the projective interpretation; no exact RESULTS_STATE entry concerns this completion.

### F06 — Cote 119, scan 156, C₁ display and following paragraph — reading question

The four directions have permutation group S₄ of order 24, whereas the full nine-point affine-plane automorphism group has order 432, so the display containing “Aut(V)(F₃)” needs its underlined notation and intended quotient explained before those groups are identified. Hua, “Carrés duaux et plan affine” (`119.modern.tex`, lines 752–768), retains the direction group PGL₂(F₃), and the current finite model shows that the map from AGL₂(F₃) to directions has an eighteen-element kernel. This adds a precise distinction to Hua's interpretation rather than correcting the frozen middle term; there is no exact RESULTS_STATE claim on this notation.

### F07 — Cote 119, scan 160, III.5, second exact sequence — unproved claim

The written prime is explicitly defined by the equal-sign condition “ε(σ)=ε(σ′),” so it should not be read as a commutator-subgroup notation. On the affine-plane interpretation the kernel is F₃²⋊{±1}, of order 18, matching the equal-parity subgroup of S₃×S₃ and giving 18·24=432. Hua, “Le second plan” (`119.modern.tex`, lines 877–891), already gives this interpretation; the present computation rechecks its concrete permutation action and does not claim novelty or a change to RESULTS_STATE.

### F08 — Cote 119, scan 160, III.5 — own idea; high confidence, explicit lift obstruction

The direction extension 1→F₃²⋊{±1}→AGL₂(F₃)→S₄→1 is not split, an implication not pursued on the page. The matrix A=((0,1),(-1,0)) induces a double transposition on the four directions but A²=−I; every affine lift has linear part ±A, so no lift is an involution, while a section would have to preserve its order. This strengthens the kernel description in Hua, “Le second plan” (`119.modern.tex`, lines 877–891), with a targeted proof and a check that all fifty-four lifts of the three double transpositions have order four; the confidence concerns this precise group extension only, and there is no exact RESULTS_STATE entry.

### F09 — Cote 119, scan 160, II, first exact sequence — reading question

If “bi-di-triade” here denotes an unordered pair of three-element blocks, the familiar block-permutation sequence has kernel S₃×S₃ and quotient C₂, and splits after choosing a bijection between the two blocks. Hua, “Le second plan” (`119.modern.tex`, lines 858–867), leaves the last quotient unread, whereas the frozen reading proposes Z₂ or an ornate group initial with index 2; this adds a plausible quotient without supplying a missing definition of the manuscript's term. The possible change in terminology between “bi-di-triade” and “quadritriade” should remain a research question, since the later affine-plane group has order 432 and cannot be conflated with this seventy-two-element wreath product; no relevant register result resolves that terminology.

### F10 — Cote 119, scan 160, III.2, prose after the cube group — reading question

The literal group of F₃-linear automorphisms preserving a system of three independent lines is the monomial group of order 2³·3!=48, while the written Aut⁺(Cub₃) has order 24 under the rotation interpretation. Requiring determinant one produces the twenty-four-element subgroup acting as S₄ on the four body diagonals, so an orientation condition or a scalar quotient is needed to make the rightmost prose match the preceding group. Hua, “Le second plan” (`119.modern.tex`, lines 869–877), avoids this marginal prose because of its reading uncertainty; the present check isolates the missing mathematical distinction without claiming the ink contains the repair, and it has no exact RESULTS_STATE counterpart.

### F11 — Cote 119, scan 160, IV.2, and scan 155, chapter 4 — unpursued implication

“GP(1,F₅)” is compatible with S₅: PGL₂(F₅) has 120 elements and its faithful transitive action is on six projective points, so the five-element heading is not a reason to reject the group isomorphism. Hua, “Le second plan” (`119.modern.tex`, lines 901–905), makes exactly this distinction, and the finite check realizes its PGL₂(F₅) as the stabilizer of one pentad, acting as the full S₅ on the other five. This agrees with the primary constructions in Cameron, §2, and Howard–Millson–Snowden–Vakil, §1, while the links to LM4 F.7 (Open, return's claim) concern only the finite group model, not a proof about profinite centralizers.

### F12 — Cote 119, scan 160, IV.1, right margin and orientation display — unproved claim

The phrase “non précisé” matters: PGL₂(F₄) acts by the sixty even permutations on its five projective points, and adjoining Frobenius gives all 120 permutations. Frobenius interchanges the two elements of F₄\{0,1} and is a transposition on the five points, explaining the proposed orientation torsor through the two field generators. Hua, “Le second plan” (`119.modern.tex`, lines 893–904), already supplies this semilinear interpretation; direct arithmetic in F₂[a]/(a²+a+1) rechecks it here, and no RESULTS_STATE theorem on these finite objects is being reopened.

### F13 — Cote 119, scan 155, dictionary A), “Ens₅ … Biicos.” — own idea; medium confidence, categorical reading supported by stabilizers

Read the displayed comparison as a possible equivalence of structure groupoids, not as an equality between a five-point set and the six biicosahedral structures on a fixed six-point set. In the model explained by Hua, “Le premier plan” (`119.modern.tex`, lines 661–713), both connected groupoids have automorphism group S₅, so their equivalence is compatible with those different underlying-set cardinalities. This interpretation is supported by the neighbouring “Ens₆≃Ens₆” and group-isomorphism language, but the manuscript does not spell out the functor or morphisms; no exact RESULTS_STATE entry settles that semantic choice.

### F14 — Cote 119, scan 155, chapter 4, “L'autodualité” — unproved claim

Hua, “Le premier plan” (`119.modern.tex`, lines 661–713), identifies the dual six-point set through the exceptional outer action of S₆; the explicit syntheme model produces fifteen matchings and six one-factorizations, and a transposition acts on the latter as three disjoint transpositions. The computation verifies the full 720-element action, and the primary literature supplies this construction and the associated paired-icosahedron model, so the present task should treat the duality as a known comparison rather than a new theorem. The unresolved part on these pages is the “avec axiomes” dictionary between his three perspectives, not the existence of an outer automorphism; the nearest RESULTS_STATE pointers LM4 D.12/F.7 remain Open and are not settled by it.

### F15 — Cote 119, scan 156, last main lines and bottom order insertion — reading question

Hua, “Carrés duaux et plan affine” (`119.modern.tex`, lines 765–775), objects to an order-10 subgroup of an ambient group it reads as 2·(3!)²=72, but that divisibility objection does not transfer to the frozen alternatives 2·(8!) or 2·(6!), both divisible by ten. If the three Gα are indexed equivariantly by the three square structures on the four directions, their stabilizer in AGL₂(F₃) has order 144, so neither “order 10” nor “order 16” can describe that full faithful stabilizer. The arithmetic possibility “index 10 in a group of order 2·6!=1440” is a low-confidence reading lead only—Gα is not defined here and no identification with S₆ has been proved—and no RESULTS_STATE entry resolves this passage.

### F16 — Cote 119, scans 156–157, Q*, Q∨ and bottom “OK!” — unproved claim

The relations “Q*≃ε∧Q” on 156 and “Q*=ε∧Q∨” on 157 require a definition of Q∨ and of the torsor action on square structures before their compatibility can be checked. Hua, “Carrés duaux et plan affine” (`119.modern.tex`, lines 719–745), explicitly follows the first formula and declines to reconstruct the missing definitions; the frozen transcript adds the variants and cancellations that a future proof must reconcile. The final “OK!” is the author's local sign check, not a supplied proof of the whole dictionary, and it does not settle the open profinite questions LM4 D.12/F.7 mentioned by RESULTS_STATE.

### F17 — Cote 119, scans 155–157 and 161, icosahedral programme — own idea; medium confidence, useful finite input with a clear missing bridge

The marked vertex, edge and biface correspondences are candidates for organizing explicit finite orbit data in the A₅ centralizer questions flagged by RESULTS_STATE as LM4 F.7 and LM4_SUCCESSOR B.38/B.39 (all Open, return's claims). Hua, “Le premier plan” and “Carrés duaux et plan affine” (`119.modern.tex`, lines 671–745), supplies the finite A₅/S₅ interpretation, whereas these scans add the author's diagrammatic choices of marked structures. Confidence is medium because one would still need maps to the appropriate punctured-sphere or profinite mapping-class actions, and finite permutation data alone cannot establish the centralizer comparison.

### F18 — Cote 119, scan 155, “Dualité des hexagrammes” — own idea; medium confidence, primary comparison but no tower theorem

Howard–Millson–Snowden–Vakil use the outer-S₆ geometry to study invariants of six points in projective space, giving a concrete modern comparison for the manuscript's three-perspective programme. This extends Hua's group-theoretic reading (`119.modern.tex`, “Le premier plan,” lines 661–713) toward configurations of marked projective points, but it supplies neither the tower's two-level finality nor its arithmetic image. The relevant RESULTS_STATE items IMPL P3 and EXIT_TOWER E.24 therefore remain Open; the confidence is medium because the invariant-theoretic bridge is explicit in the cited paper, while no compatible tower functor is constructed here.

### F19 — Cote 119, scan 157, Syl₂/Syl₃ labels — unproved claim

The finite S₆ interpretation supports the displayed Sylow types: disjoint three-cycles generate C₃² of order 9, and a dihedral Sylow group on four letters times the transposition of the remaining two generates D₈×C₂ of order 16. These are maximal 3- and 2-powers dividing 6!, respectively, so the abstract group types stated by Hua, “Carrés duaux et plan affine” (`119.modern.tex`, lines 747–750), have an immediate construction; the subscript D₄ in the frozen transcription is kept as written rather than changed to another dihedral naming convention. This is a finite check, not a result about the torsion of profinite GT₀ in LM4 D.12, which remains Open.

### F20 — Cote 119, scans 155 and 161, chapter plan and last paragraph — self-flagged

“avec axiomes” on 155 and “il faudrait un exposé sur les réalisations géométriques” on 161 identify work the manuscript itself leaves to be written. Hua, “Le premier plan” and “Le second plan” (`119.modern.tex`, lines 656–660 and 907–910), treats the pages as a repeatedly revised plan, but paraphrases the last phrase as geometric relations rather than the frozen “réalisations géométriques.” This adds a precise distinction between an abstract finite-group dictionary and its geometric realization, and supports the standing planning question in `context/README.md` without changing any mathematical result's status.

## Proof details and exact computational scope

### General deduction of B(b) from B(a,c)

Let E be the disjoint union of four three-element classes, and let V consist of four-element subsets meeting each class once. By c), projection to two chosen classes is both surjective and injective, so |V|=9. If x lies in one class, c) gives one block for each of the three elements of any other chosen class, and a) prevents duplication, giving three blocks through x. Two distinct blocks cannot have two points in common: a) puts those points in distinct classes and c) then forces equality. For a fixed D, its four points each lie in two other blocks; these eight blocks are distinct and exhaust V\{D}, proving that each other block meets D once. This is a general proof from the stated finite axioms, not merely a verification of the coordinate example.

### c alone with all block sizes still four

Index the classes by 0,1,2,3. For every i<j and every b∈Eⱼ, include Dᵢⱼᵦ=Eᵢ∪{b}. These eighteen sets are distinct and have four elements. A pair a∈Eᵢ, b∈Eⱼ with i<j lies in Dᵢⱼᵦ; every block containing points from two classes uses its entire lower-index class and just one point of the other, so it lies in no second block. This is a counterexample to c⇒|V|=9 with precisely the four-element hypothesis kept, rather than a counterexample obtained by altering block sizes.

### Equal-parity kernel identification

Write each permutation of a three-point affine line as x↦ax+b, with a∈{±1}, b∈F₃; its sign is a. A pair of such maps has equal signs precisely when the same a occurs in both coordinates, giving (x,y)↦a(x,y)+(b,c). This is exactly F₃²⋊{±1}, with the scalar acting by simultaneous inversion. The prime in the manuscript is therefore explained by its explicit parity condition, without borrowing a conventional meaning for the prime.

### Nonsplitting of the direction extension

Identify the four directions with P¹(F₃). A=((0,1),(-1,0)) exchanges the two coordinate directions and exchanges the two remaining directions, so its image is a double transposition. Its two linear lifts A and −A both square to −I. Every affine lift is x↦±Ax+t; its square has linear part −I and therefore is not the identity, while its fourth power is the identity because I+A+A²+A³=0. A section of the direction quotient would lift this order-two element to an order-two element, which is impossible. The computation independently verifies all 54 affine lifts of the three double transpositions, not just this representative.

### Enumeration scope

`finite_checks.py` uses only Python's standard library and integer arithmetic. It constructs the eighteen-block counterexample, the 9/12-point affine incidence structure and its 13/13 completion, all labelled STS(9) by an exact-cover search, the affine plane's complete S₉ orbit, all 432 affine transformations of F₃² and their direction actions, all 48 signed coordinate permutations in dimension three, the fifteen synthemes and six pentads of a six-element set, the full S₆ action on them, PGL₂(F₅), and PGL₂(F₄) with Frobenius. Its output is `finite_checks.json`; assertions passed on the recorded run. No computer algebra system, random sampling, external database or formal proof assistant was used.

The STS enumeration exhausts every twelve-triple system covering all 36 pairs exactly once: at each stage it chooses an uncovered pair and branches over every compatible triple containing it. The orbit search starts with the explicit affine plane and applies the eight adjacent transpositions generating S₉. Equality of the two resulting sets of 840 systems verifies uniqueness up to relabelling in this exact finite search.

The pentad calculation gives a faithful 720-element permutation action on six objects. A transposition has cycle type (2,2,2) there, certifying that the action is outer because an inner automorphism preserves cycle type. The 120 projective permutations over F₅ fix one pentad and act faithfully on the five others; this is an explicit isomorphism to S₅, so no claim rests on equality of orders alone.

## Primary literature actually opened

1. Peter J. Cameron, *From M12 to M24*, January 2015, §2, pp. 2–3: <https://cameroncounts.wordpress.com/wp-content/uploads/2015/01/m12.pdf>. The author gives the duad/syntheme/total construction, counts six totals, describes the outer action and its exchange of transpositions with triple transpositions, and explains the corresponding 3+3 partitions. This is used as a primary author exposition, not as evidence of a manuscript reading.
2. Ben Howard, John Millson, Andrew Snowden and Ravi Vakil, *A description of the outer automorphism of S₆, and the invariants of six points in projective space*, arXiv:0710.5916v1, 31 October 2007, §§1.1–1.4 and the abstract: <https://arxiv.org/html/0710.5916v1>. The opened text gives the paired-icosahedron, colored-triangle and pentad constructions and states the application to invariant theory; the present notes do not reconstruct that paper's invariant-theoretic proofs.
3. Noam Elkies, *Projective {groups, spaces, geometry}*, author-hosted Math 122 notes, paragraphs on q=4 and q=5: <https://people.math.harvard.edu/~elkies/M122.23/proj.html>. The directly used passage constructs PGL₂(F₅)≅S₅ through its six-point action and the coset action of S₆. The finite computations above provide their own independent checks of the relevant group orders and actions.

No statement about novelty or priority is made. In particular, the manuscript's 1980s date does not make an outer-S₆ construction new, and a modern comparison is not evidence that Grothendieck had the later paper's construction in mind.
