# Advisory review of the game-theory research notes

Prepared after the transcription freeze, solely from the frozen page files and supplied context. No manuscript images were opened, no OCR was used, and no transcription file was changed. The mathematical checks below are advisory reasoning, not a literature review, a novelty claim, or a referee certification.

## Context and reference conventions

`context/notes/RESULTS_STATE.md`, **Orientation for this package**, explicitly says that no row of the research registers meets these folders and that there are no results to use and check; its later matching-entry sections each contain zero entries. Thus **no relevant result-register ID exists for these game items**: the honest cross-reference is that orientation and the zero-matching-entry statement, not a manufactured LM/FINMON/PATHS identifier. The background programme's category or finite-model entries do not settle any of the game questions below merely because the manuscript mentions a category of paths.

All references to Hua mean **Michel Hua's project, modernised reading of cote 68**, `context/hua_project/68.modern.tex`, treated as an interpretation and a source of leads. Hua uses archive foliation: his page n corresponds to supplied cote-68 scan n+1; the package ends at scan 032 / archive foliation 31, so Hua's later pages 32–33, his third game draft on page 47, and all claims about them are context-only evidence, not inspected manuscript evidence in this package.

## Candidate items

Each numbered item below is separately usable as a research-note item. The register qualification above applies to every item.

### G01 — Distinct initiative/complement conventions

**Location:** 68/002–003 and 024, initiative definitions and complement notation. **Kind:** reading question. The first draft writes initiative as `i` and uses `\bar C(j)=C\setminus C(j)`, while the restart writes `\alpha` and excludes terminals from `\bar C(j)`; these are substantive convention changes, not inconsistent transcription. This **differs from** Hua, “Le fil du dossier, et les conventions” and “Les données (page 1),” which explicitly normalize both drafts to the second convention, so comparison of formulae must restore the terminal exclusions before deciding whether they agree.

### G02 — Termination is weaker than finite height

**Location:** 68/002–003, definitions of `C_i`, `C_\infty`, and the length function. **Kind:** unpursued implication. The words about lengths and the displayed natural-number-valued function distinguish a bound depending on the starting position from the assertion that every play is finite. This **restates and supports** Hua, “Parties, et positions de longueur bornée (pages 1 et 2),” whose counterexample has one root followed by forced branches of every finite length; no claim that absence of infinite plays alone gives `C=C_\infty` should be attributed to the supplied proof.

### G03 — The admitted finite-play step

**Location:** 68/004 marginal hypothesis and 006, proof of the universal-successor direction, approximately the middle. **Kind:** self-flagged: a step he himself marks as unverified. The proof explicitly says “admettons qu’elle est finie,” with the marginal no-infinite-play hypothesis, before showing preservation of `G(j)`; preservation by itself supplies no termination argument. This **supports and sharpens** Hua, “Théorème 1 : l’équation de point fixe (pages 3 à 6),” by identifying the manuscript's own admission rather than reporting only a modern criticism.

### G04 — A two-position test of the admitted step

**Location:** 68/006, strategy retaining all successors in `G(j)`. **Kind:** own idea; **confidence high**, because every possible play can be inspected directly. For a player-controlled position `a` and a winning terminal `t`, set `R(a)={a,t}`: both positions are winning, yet the proposed all-winning-successors strategy permits `a,a,a,…`. This **adds a smaller diagnostic example to** Hua's example in “Théorème 1 : l’équation de point fixe”; it diagnoses the failure of the proposed strategy, and by itself does **not** prove nonexistence of a greatest winning strategy.

### G05 — The first patched-successor proof is repaired by separating the return case

**Location:** 68/004–005 and 026–027, proof at a position controlled by j. **Kind:** withdrawn in the same text. The naive instruction to replace the move at `x` by a winning successor is followed by the return-to-`x` issue on 005; the second draft makes the repair explicit with “Si `x_0` est gagnant pour `\Sigma_1` … Sinon.” This **restates and supports** Hua, “Théorème 1” and “Le théorème de point fixe, démontré (pages 25 à 28),” while retaining the different drafting states rather than describing the first attempt as already clean.

### G06 — Greatest winning strategies need more than local winning successors

**Location:** 68/006 and 008–009, “il y en a une plus grande.” **Kind:** unproved claim. The proof checks that a compatible finite play stays in the winning region, but the advertised greatest strategy needs the termination assumption carried from the preceding discussion and the successor-stability of `\Gamma`. This **supports** Hua, “La plus grande stratégie gagnante (pages 5, 7 et 8),” whose formulation supplies those hypotheses; the stability condition is written in the manuscript but not formally expanded there.

### G07 — Union of winning strategies can destroy termination

**Location:** 68/006 and 008–009, greatest-strategy assertion. **Kind:** own idea; **confidence high**, by direct examination of all transitions. Take two j-positions `a,b` and one winning terminal `t`, with `R(a)={b,t}` and `R(b)={a,t}`: strategies `({b,t},{t})` and `({t},{a,t})` each win from both nonterminals, but any common upper bound permits the infinite alternation `a,b,a,b,…`. This **restates the obstruction in and slightly simplifies the witness of** Hua, “La plus grande stratégie gagnante,” by identifying his two winning terminals, and shows why a greatest element can fail even on a finite game graph.

### G08 — What the cancelled well-order construction omits

**Location:** 68/007, cancelled whole-page draft, compared with 027–029. **Kind:** withdrawn in the same text. The cancelled argument chooses the “plus petit” initial successor from which a position is reachable, but arbitrary reachability does not make the chosen successor's winning strategy win from the reached position. The second draft replaces it by reachability along a `\Sigma_{x_1}`-compatible play, which **supports** Hua, “Théorème 1” and “Le théorème de point fixe, démontré,” in locating the actual repair.

### G09 — The root index in E(x) is mathematically decisive

**Location:** 68/027, final display defining `E(x)`, and 028, its proof. **Kind:** reading question. The frozen transcription retains `\unsure{x_0|x_1}` as the start of a `\Sigma_{x_1}`-path, whereas the next page's proof explicitly starts at `x_1`; Hua, “Le théorème de point fixe, démontré,” normalizes to `x_1` and says this is the reading required by the sequel. This **differs from Hua's normalized text** and should remain a reading question: its strong mathematical support cannot retrospectively change the frozen first reading.

### G10 — A witness to the root-index problem

**Location:** 68/027–028, `E(x)` and selector construction. **Kind:** own idea; **confidence high**, because the failure is explicit. Let an opponent root `x_0` move to j-positions `a,b`, each with moves to a winning terminal `t` or losing terminal `l`, and choose `\Sigma_a(a)=t,\Sigma_a(b)=l`, `\Sigma_b(b)=t,\Sigma_b(a)=l`, with `a<b` in the selected well-order: if `E(x)` uses paths from `x_0`, then `a∈E(b)` and the patch chooses the losing move from `b`. This **adds a diagnostic counterexample to** Hua's footnote in “Le théorème de point fixe, démontré,” explaining why the start should be `x_1` for that proof rather than merely appealing to expected notation.

### G11 — E(x) as an element of E(y) is a separate reading issue

**Location:** 68/028, lemma display. **Kind:** reading question. The frozen `E(y)\ni\unsure{E(x)|\varepsilon(x)}` differs from Hua's `\varepsilon(x)∈E(y)` in “Le théorème de point fixe, démontré”; the latter matches the later line that extends a compatible path and the inequality `\varepsilon(y)≤\varepsilon(x)`. This **differs from Hua's normalization** at a distinct overwritten symbol and should not be silently merged with the starting-index question.

### G12 — Why stationarity supplies the missing finite-play argument

**Location:** 68/029, “suite décroissante … donc stationnaire” and “finie, absurde.” **Kind:** unpursued implication. Once the two preceding readings are interpreted as in the continuation, the crucial fact is that an infinite nonincreasing sequence in a well-order eventually has constant value, so its tail follows one fixed strategy from a position already winning for that strategy. This **supports** Hua, “Le théorème de point fixe, démontré,” and shows that the second proof addresses termination itself, not just invariance of the winning set.

### G13 — Choice assumptions belong to the analysis of the proof

**Location:** 68/025, inserted joint-play lemma, and 027, “Choisissons un bon ordre.” **Kind:** unproved claim. The lemma's successive move choices and the later selection of a winning strategy for each successor plus a well-order use set-theoretic choice principles that the manuscript does not state. This **restates** the two relevant Hua footnotes in “Données, parties, stratégies (pages 23 et 24)” and “Le théorème de point fixe, démontré”: dependent choice supplies a maximal play for an already specified family, while choosing the whole family and well-order is a stronger step, so these should not be conflated into a single claimed choice-free proof.

### G14 — Safety is not winning in the auxiliary coalition game

**Location:** 68/009–012 and 029–030, “acceptable” versus “admissible,” especially 012 margin “S’il n’y a pas de parties infinies.” **Kind:** self-flagged: a step he himself marks as unverified. The coalition can prevent j's finite win by sustaining an infinite play, whereas a winning strategy for the complementary terminal target must force a finite termination, and the marginal condition is therefore essential to the proposed identification. This **supports** Hua, “Positions acceptables ; théorème 2 (pages 8 à 11),” while the second draft's “ou bien infinie” on 029 states the distinction explicitly.

### G15 — A single-loop diagnostic for coalition equivalence

**Location:** 68/012, auxiliary two-player game. **Kind:** own idea; **confidence high**, by the sole possible play. A one-position game `a→a` with no terminal positions admits a strategy preventing either player's finite victory but admits no winning strategy for either player; replacing j's terminal target by its complement among terminals changes neither conclusion. This **adds a direct witness to** Hua's distinction in “Positions acceptables ; théorème 2” and tests exactly the necessity of the margin's termination qualification.

### G16 — The finite recursion is a genuine question, not a theorem established in full

**Location:** 68/013, “? Th 3” and the concluding induction on `C_i`. **Kind:** conjecture. The page's `G_\infty(j)=G(j)` is questioned, while its surviving proof yields equality after intersection with each finite-height `C_i`; consequently the conclusion follows under `C=\bigcup_i C_i`, which the margin mentions. This **supports** Hua, “« ? Th 3 » : la construction récurrente (page 12),” but the frozen uncertain conjunction in the margin should not be converted into Hua's definite disjunction “fini, ou s'il n'existe pas de partie infinie.”

### G17 — The cancelled single-play proof does not yield a uniform bound

**Location:** 68/013, crossed-out proof beginning “∃ partie … finie.” **Kind:** withdrawn in the same text. Producing one finite maximal compatible play does not bound the lengths of all plays compatible with the winning strategy, so the deleted argument cannot justify membership in any finite `G_i(j)`. The surviving induction on `C_i` **adds explicit evidence for the drafting correction discussed by** Hua, “« ? Th 3 »,” and should be distinguished from a claim that the author completed the unrestricted result elsewhere in the supplied pages.

### G18 — Failure at omega can occur without an infinite play

**Location:** 68/013, questioned equality. **Kind:** unpursued implication. Hua's “« ? Th 3 »” gives an opponent-controlled root with successor chains of every finite length, each ending in a j-winning terminal: every play wins for j, yet no finite backward stage contains the root. The supplied page **supports the question to which this is a counterexample**, and the example should be credited to Hua's modernised reading rather than presented as a newly discovered result of this run.

### G19 — Finite branching is needed only at the universal-successor positions

**Location:** 68/013, existential/universal recurrence. **Kind:** unpursued implication. Hua's sufficient condition in “« ? Th 3 »,” that every opponent position has finitely many successors, follows because the universal predecessor clause then commutes with increasing countable unions; the existential clause needs no finite-branching restriction. The formula on the supplied page **supports this sharpening of a blanket locally-finite assumption**, but the extension is Hua's mathematical interpretation, not an assertion written in the manuscript or an entry settled by the supplied research register.

### G20 — Context's transfinite indexing needs a convention

**Location:** 68/013, in comparison with Hua's transfinite discussion. **Kind:** reading question about context; **confidence high**, from the displayed definitions. Hua's “« ? Th 3 »” first uses `G_omega=union_i G_i` and assigns the unbounded finite-chain root to `G_{omega+1}`, but later displays `G_alpha=F(union_{beta<alpha}G_beta)`, which already includes that root at alpha=omega. This **differs from a consistent limit-union convention**: analysis may choose `A_0=G_0`, `A_{alpha+1}=F(A_alpha)`, `A_lambda=union_{beta<lambda}A_beta`, while the manuscript's `G_\infty` and the frozen transcription must remain unchanged.

### G21 — Fixed-point equations do not specify the least fixed point

**Location:** 68/026, local equations, with 013, recursive construction. **Kind:** unpursued implication. Hua, “Le théorème de point fixe, démontré,” observes that a nonterminating cycle with empty terminal target has both the empty set and the whole cycle as fixed points, though no position is winning; the local equations therefore require a least-fixed-point selection principle to characterize `G(j)`. The supplied pages **support that distinction**, while the transfinite argument in Hua is context analysis and the later manuscript uniqueness result he discusses lies outside the supplied scans.

### G22 — The joint-winner proposition has an empty-family convention to state

**Location:** 68/025, bracketed proposition after the inserted lemma. **Kind:** reading question. The manuscript quantifies `J'⊂J` without explicitly saying nonempty, while Hua's “Données, parties, stratégies” inserts that restriction. This **differs from the normalized context text**: if empty intersections are taken in the respective ambient sets C and C_0, the empty coalition case would incorrectly force C_0 nonempty whenever C is, whereas other empty-intersection conventions change the statement, so the missing convention should be flagged rather than silently repaired.

### G23 — Neutral does not mean that every outcome is infinite

**Location:** 68/030, trichotomy with disjoint `G_0(j),G_0(j')`. **Kind:** unpursued implication. The terminal targets are required to be disjoint, not exhaustive, so a terminal position winning for neither player lies in N and gives an immediate finite neutral example. This **restates and supports** Hua, “Stratégies contre j ; positions admissibles (pages 28 et 29),” and prevents interpreting the manuscript's “nulles” as only infinite draws or imposing the normal-play convention without evidence.

### G24 — The common avoidance strategy supplies a memory comparison

**Location:** 68/030, equivalence of nonwinning, admissible, and admissible for the displayed `\Sigma'`. **Kind:** unpursued implication. The displayed coalition strategy keeps play outside `G(j)` regardless of how j chooses among legal moves, including choices depending on the entire previous play; this is the argument that no history-dependent winning strategy can enlarge j's positional winning region. This **restates** Hua's explicit modern observation in “Stratégies contre j ; positions admissibles,” not a literature theorem established by the research-register rows.

### G25 — The path-category remark concerns finite paths

**Location:** 68/024–025, “catégorie des positions” and the strategy subcategory. **Kind:** unpursued implication. Finite compatible plays compose as paths and form the indicated subcategory with the same objects, whereas an infinite play has no endpoint from which ordinary path composition could proceed. This **supports Hua's precise finite-path interpretation** in “Données, parties, stratégies,” and does not by itself bear on FINMON's finite-category realization questions: even a finite graph with a cycle has infinitely many finite paths.

### G26 — The relative outcome sets precede the alternation assumption

**Location:** 68/031, definitions of `G^*,P^*,N^*`, followed by the extension `\hat\alpha`. **Kind:** unpursued implication. The relative classification is defined for any two-player initiative assignment before the additional assumption that each move changes the player; alternation is needed for the later move-by-move G/P recurrence, not for those initial definitions. This **clarifies the order within** Hua's broad subsection “Gagnantes, perdantes, nulles : le jeu alterné (pages 30 à 32),” and the supplied fragment ends before all the results of that subsection.

### G27 — A terminal can obstruct alternation even when internal edges do not

**Location:** 68/032, conditions 1) and 2). **Kind:** own idea; **confidence high**, by the two forced values of `\hat\alpha(t)`. Let positions u and v controlled by different players both move to a common terminal t: condition 1) is vacuous but no player value at t can be opposite to both predecessors. This **adds an explicit test case to** Hua's “Gagnantes, perdantes, nulles,” showing why the constancy condition on T(t) is independent and why the extension is forced precisely at terminals with predecessors.

### G28 — The final unextended alpha should remain a reading question

**Location:** 68/032, final display defining G and P. **Kind:** reading question. The first set uses `G(\alpha(x))` even for `x∈C`, although alpha was initially defined only off C_0, while P uses the extended hatted alpha; Hua's “Gagnantes, perdantes, nulles” normalizes both to the extension. This **differs from the literal frozen text**, and the surrounding sentence makes the normalized interpretation plausible without licensing a change to the transcription.

### G29 — The announced cycle-elimination section is not a supplied proof

**Location:** 68/014, sole heading “Elimination des parties circulaires (cas C fini).” **Kind:** unproved claim. The leaf supplies an announced topic but no argument, and it cannot be counted as a proof that the finite-stage construction handles finite cyclic games. This **supports** Hua, “Un paragraphe annoncé (page 13),” while Hua's broader statement that the paragraph occurs nowhere in the entire dossier is a context claim beyond the images supplied here.

## Cautions for final synthesis

1. Keep the two different counterexamples separate: a losing all-winning-successor policy does not by itself show there is no greatest winning policy; G04 and G07 address different assertions.
2. Do not call the cancelled 007 proof repaired merely by stationarity: compatible reachability from a position already winning for the eventual selected strategy is what makes the tail contradiction work.
3. Do not attribute transfinite ranks, a least-fixed-point theorem, historical names, or external literature identifications to the manuscript where Hua supplies them as modern commentary.
4. Do not import Hua's manuscript foliation 32 or 33 into this package as if scans 033 or 034 had been inspected; current page 032 ends mid-sentence, and the package's original scope is deliberate.
5. The literal `G(j)∩C(j')` in the second reconstruction line of scan 031 is correct for a position where the other player has initiative; it is not an obvious missing prime on G(j).
6. No claim above rests on a formal matching RESULTS_STATE result ID, because the supplied register explicitly says there are none for these folders.
