# Algebra checks for scans 033–037

**Run:** SP32_CW_156-3, research subtask `/root/package_tools`; ChatGPT GPT-6 Astra Pro; reasoning effort not exposed. **Scope:** mathematical work on the already frozen text, with no scan inspection, transcription change, web research, or TeX compilation. `RESULTS_STATE.md` was read first. The sweep is used as a lead, never as a proof certificate.

The principal finding is positive: the relativization argument of scans 035–037 works under the **marginally strengthened** Boolean compatibility assumption explicitly adopted at scan 034. The separate expectation at scan 037 that every clopen element is compatible with everything does **not** follow, even with that strengthening. Several literal formulas require research qualifications, which do not authorize alterations to the frozen text.

## Assumptions and context locators

Write `x ⊙ y` for the manuscript's compatibility relation, `¬x` for its complementary element, and `c(x)` for its least closed majorant. The strengthened assumption **PB** means that each finite pairwise compatible family is contained in a Boolean subalgebra whose elements are mutually compatible and whose operations agree with the indicated order meets, joins and complements. This is the substantive reading of scan 033's margin “ils engendrent une ... alg. de Boole”, expressly included by scan 034's “avec 4) renforcé marginalement”; the arguments below do not claim that PB follows from mere order identities.

The coherent algebraic interpretation uses the maximum compatible disjoint complement in scan 033, together with PB. It does not impose the uncertain literal branch `X'' ∧ X = ∅`, which would collapse the algebra; see ALG-11. Likewise, Boolean De Morgan calculations use the lattice join, with the distinction from the written cup recorded in ALG-12.

Context shorthand used below:

- **E34:** `SP32_CW_156-3_context/Esquisse_cote119_copy1_API_transcription.tex`, marker `119/34`, PDF page 35, typescript p. 32, lines 1487–1506: provisional tame axioms and possible additional axioms.
- **E39:** the same file, marker `119/39`, PDF page 40, typescript p. 37, lines 1711–1743: finite families of closed subspaces and globally tame spaces as differences of closed compact spaces.
- **E42:** the same file, marker `119/42`, PDF page 43, typescript p. 40, lines 1851–1883: stability conditions in an axiomatic theory.
- **E44:** the same file, marker `119/44`, PDF page 45, typescript p. 42, lines 1945–1964: a closed tame rare exceptional subset, with no assertion that it is finite.
- **S3:** `SP32_CW_156-3_sweep3/readings/156-3.md`, §1.6, lines 139–165, and §1.7, lines 169–176. These are an earlier reader's claims; the full non-total concrete model is explicitly left unchecked there.
- **S7:** `SP32_CW_156-3_sweep3/readings/156-7.md`, §2.2, lines 349–354, and §2.3, lines 367–392. The six-element support lattice and the later restriction to compatible supports provide comparisons, not inherited proofs.

**Register scope.** `RESULTS_STATE.md` has no settled entry proving these partial Boolean or relative closure claims. **MPL_150_044-084 Q9** is the relevant thematic lead about tame axioms and comparison of tame theories, not a theorem being used; **WG2 B15 (§1.2)** concerns a much stronger shape comparison which these algebraic checks do not settle. No register status is changed. Searches for `bool`, `compat`, `relativ`, `rare`, `fronti`, `stabilit`, and `partie mod` were made in the supplied context; the exact Boolean relativization is added by these pages, not found in the Esquisse packet.

## Item notes

### ALG-01 — Compatible Boolean generation is an assumption with mathematical content

**Scan/place:** 033, margin opposite axiom 4; 034, L16–20. **Kind:** unproved claim / own clarification. **Quote:** “ils engendrent une ... alg. de Boole”; “avec 4) renforcé marginalement”. **Context/relation:** E34 and S3 §1.6; adds a precise local algebra requirement to the provisional axiomatic programme. **Register IDs:** bears thematically on MPL_150_044-084 Q9; none directly settled. **Confidence:** high for the stated distinction, because of the explicit finite countermodel in Appendix A.

Pairwise compatibility plus the displayed order identities alone does not force all generated Boolean elements to remain compatible: Appendix A gives a 32-element Boolean lattice with a deliberately narrower compatibility relation. This does not refute the manuscript's relativization theorem, since scan 034 explicitly adopts the stronger marginal assumption PB. If distributivity is instead formalized in a genuinely partial signature with every displayed composite required to lie in the compatibility domain, that domain requirement already supplies additional closure; the weak countermodel is not a counterexample to that stronger interpretation.

### ALG-02 — The closure and formal boundary identities can be proved directly

**Scan/place:** 033, axioms 5–7 and interior margin; 034, first display and (a),(b). **Kind:** unpursued implication / own proof. **Quote:** “un plus petit ... Y ... tel que X ⊂ Y”; “X ... fermé rare”. **Context/relation:** E39 and E44; adds algebraic closure calculations to the context's use of closed and rare subspaces. **Register IDs:** MPL_150_044-084 Q9, thematic only. **Confidence:** high, from order arguments and Boolean calculations on compatible elements.

The least-closed-majorant definition makes `c` extensive, monotone and idempotent, and the meet of two compatible closed elements is closed. With `i(x)=¬c(¬x)` and `Fr(x)=c(x)∧c(¬x)`, one has `x≤Fr(x) ⇔ i(x)=0`, whereas `x=Fr(x) ⇔ x is closed and i(x)=0`. Thus (b) implies (a) formally, while the converse requires an additional property of the intended one-dimensional model.

### ALG-03 — The one-dimensional rarity assertion is independent of the abstract axioms

**Scan/place:** 034, L11–15, conditions (a)–(c). **Kind:** unproved claim / own counterexample to an unrestricted reading. **Quote:** “Dans le cas d'espèce, conditions équivalentes”; “X est fini”. **Context/relation:** E44; the context also uses rare exceptional sets but does not identify rarity with finiteness. **Register IDs:** MPL_150_044-084 Q9; no exact settled claim. **Confidence:** high for independence, from an explicit closure algebra.

For the full Boolean algebra `P(N)` with indiscrete closure `c(∅)=∅` and `c(S)=N` for nonempty `S`, all of 1–7 and PB hold, but the even integers have empty interior, are infinite, and are not equal to their frontier `N`. Consequently the three-way equivalence is a special assertion about the concrete one-dimensional tame family, not an abstract consequence of 1–7. The finite model in Appendix D also has an element with empty interior which is not closed, so the missing implication (a)⇒(b) already fails in a finite closure algebra.

### ALG-04 — The repeated frontier in axiom 8 has no mixed-pair force

**Scan/place:** 034, L4–5. **Kind:** reading question / logical scope check. **Quote:** “Fr X ∪ Fr X est modéré”. **Context/relation:** S3 §1.6 and its open-reading list, lines 227–228; differs from a silently corrected mixed-frontier formula. **Register IDs:** none directly.

The frozen text repeats `Fr X`, so the conclusion does not mention `Y` and cannot express the mixed condition on `Fr X ∪ Fr Y` that the surrounding discussion suggests. As a self-compatibility assertion it is already automatic from comparability, and as an ordinary union it is simply the same frontier again. This is a research reading question only: no second occurrence is changed to `Y`, and no deleted “ssi” is restored.

### ALG-05 — The minus sign in the Boolean-ring formula is valid

**Scan/place:** 034, L21–24, algebraic display. **Kind:** targeted mathematical clarification. **Quote:** “X∨Y=X+Y−XY”. **Context/relation:** S3 §1.6, line 153; confirms the algebraic translation under PB. **Register IDs:** none directly.

With `X+Y` defined as symmetric difference and `XY=X∧Y`, the containing Boolean ring has characteristic two, so `−XY=+XY` and the displayed union-as-join identity is correct. Its four Boolean truth-value cases verify the formula without replacing the written minus sign. The operations are being used within a compatible Boolean block.

### ALG-06 — The unit of the relative algebra is A

**Scan/place:** 035, L12, first verification display. **Kind:** unproved claim / mathematical correction recorded only in notes. **Quote:** “1 ... =X”. **Context/relation:** S3 §1.7, line 170, has the same proposed correction; independently justified here by the definition of the interval. **Register IDs:** none directly.

The poset `M_A={Y:Y≤A}` has greatest element `A`, since `A` belongs to it and bounds every member; an unrelated varying `X≤A` is generally not its unit. This confirms the mathematical correction suggested by the sweep, but the frozen transcription's surviving `X` is preserved. The subsequent principal-ideal proof uses relative unit `A` explicitly.

### ALG-07 — Relative complementation and the principal Boolean ideal are sound

**Scan/place:** 035, L16–23; 036, L1–17. **Kind:** unproved claim, proved here under PB. **Quote:** “X′∧A ... c'est la plus grande”; “un idéal d'une alg. de Boole”. **Context/relation:** E39 and S3 §1.7; adds the explicit algebra behind restriction to a subspace. **Register IDs:** MPL_150_044-084 Q9, thematic only. **Confidence:** high, proof in Appendix B.

For `X≤A`, the relative complement is `A∧¬X`, and the ambient Boolean algebra generated by a compatible family together with `A` restricts to its principal ideal `[0,A]`. This ideal is a Boolean algebra with top `A` and complement `Z↦A∧¬Z`; it is the fact that the ideal is principal which justifies the manuscript's conclusion. Under PB, the elements `A∧¬X` and `A∧¬Y` are compatible whenever `X,Y≤A` are compatible, completing the step marked “Il faut prouver”.

### ALG-08 — The relative closure proof establishes all of 1–7 conditionally

**Scan/place:** 035, L7–11; 036, L19–22; 037, L1–11. **Kind:** unproved claim / independent re-proof. **Quote:** “les conditions 1) à 7) sont encore satisfaites”; `\overline X^{(\mathcal M_A)}=\overline X^{\mathcal M}\wedge A`; “OK”. **Context/relation:** E39 and E42; adds an explicit restriction-stability theorem to the context's stability programme. **Register IDs:** MPL_150_044-084 Q9; does not settle WG2 B15 (§1.2). **Confidence:** high under the explicit hypotheses of Appendix B.

The relative closed objects are exactly `F∧A` for closed `F` compatible with `A`, and their least majorant of `X≤A` is `c_A(X)=c(X)∧A`. Axiom 7 makes `c(X),c(Y),A` pairwise compatible, so PB permits the distributive calculation proving finite-join preservation and the final compatibility argument at scan 037. These arguments do not require `A` to be closed and do not assert that every non-total concrete `Mod(L)` satisfies the abstract hypotheses.

### ALG-09 — Clopen elements need not be compatible with everything

**Scan/place:** 037, L16–21. **Kind:** conjectural expectation / own counterexample check. **Quote:** “On s'attend qu'il soit mod. ... avec Y”; “S'il en est ainsi”. **Context/relation:** S7 §2.2 has the same six-element ordered-complemented structure in its supports example, and §2.3 later restricts support comparisons to compatible configurations; adds a counterexample specifically to the present closure-algebra expectation. **Register IDs:** MPL_150_044-084 Q9, thematic only; no exact settled entry. **Confidence:** high; complete axiom check and finite certificate below. **Attribution:** model proposed by the primary reader and checked independently here.

Take the horizontal sum of `{0,1,a,a′}` and `{0,1,b,b′}`, make compatibility mean membership in a common block, and take closure to be the identity. This satisfies 1–7 and PB, yet every element is clopen while `a` and `b` are incompatible. It refutes centrality as a consequence of the abstract assumptions, while leaving the subsequent “S'il en est ainsi” statement valid as a conditional and leaving the total-order concrete model untouched. The result does not inherit or claim an independent verification of the sweep's full atelier axioms.

### ALG-10 — The live ambient closure bar changes the generated algebra if read as an operation

**Scan/place:** 036, L8–9. **Kind:** reading question / mathematical counterexample to a literal operation list. **Quote:** `0_{\mathcal M},1_{\mathcal M}\quad\overline{\phantom X}`; “et de remultiplier par A”. **Context/relation:** E42 and S3 §1.7; exposes a distinction between Boolean generation and generation with an additional closure operation. **Register IDs:** MPL_150_044-084 Q9, thematic only. **Confidence:** high for the conditional mathematical objection; the bar's intended textual role is not decided.

The frozen ambient list includes a closure bar although the relative list only has complement, meet and join. If that bar instructs adjoining closure, the two generated objects need not coincide: in `P({1,2,3})` with closed sets `∅,{1,2},U`, take `A=U` and `X={1}`, whose Boolean algebra has four elements but whose algebra with closure has eight. Thus the valid principal-ideal proof is for the Boolean operations alone; the live bar is retained as a reading/scope question rather than erased from the transcription.

### ALG-11 — The uncertain double-prime branch cannot be an ordinary complement identity

**Scan/place:** 033, L12, `unsure{X''|X'}`. **Kind:** reading question. **Quote:** `\unsure{X''|X'}\wedge X=\varnothing`. **Context/relation:** local comparison with scan 033's next sentence “involutive”; no matching claim in the Esquisse. **Register IDs:** none directly.

If the first branch is imposed literally together with involutivity, it becomes `X∧X=0`, hence `X=0` for every `X`. The single-prime branch is the compatible-disjoint complement identity used in the surrounding argument. This is a mathematical reason to flag the first branch, not permission to resolve the frozen ink doubt from context.

### ALG-12 — The written cups in De Morgan's formulas need to remain distinguished from joins

**Scan/place:** 033, margin opposite axiom 3 and L18. **Kind:** reading question / mathematical scope. **Quote:** “X∨Y ... n'est ... pas l'union X∪Y”; “(X∧Y)'=X'∪Y'”. **Context/relation:** S3 §1.6; confirms the need to preserve the page's own distinction rather than normalize it silently. **Register IDs:** none directly.

PB proves the lattice identities `¬(X∧Y)=¬X∨¬Y` and `¬(X∨Y)=¬X∧¬Y` inside a compatible block. It does not identify a lattice join with ordinary union in an ambient set representation, a distinction the page itself stresses. The written cups therefore remain literal features of the transcription, with the mathematically valid join versions recorded only as an interpretative question here.

### ALG-13 — A relative boundary need not be the intersection with the ambient boundary

**Scan/place:** 037, closure formula, extending the boundary definition of 034. **Kind:** unpursued implication / own deduction. **Quote:** `\overline X^{(\mathcal M_A)}=\overline X^{\mathcal M}\wedge A`. **Context/relation:** E39; adds a useful distinction for relative closed/open decompositions. **Register IDs:** no exact entry; does not supply the additional categorical data of STRATA D.2. **Confidence:** high, direct substitution and an explicit example.

The proved formulas give `Fr_A(X)=A∧c(X)∧c(A∧¬X)≤A∧Fr_M(X)`, with equality not forced. For `M` the interval-set Boolean algebra of the real line, `A=[0,1]` and `X=A`, the relative boundary is empty while `A∩Fr_M(A)={0,1}`. This explains why the relative proof must use the relative complement before applying closure.

### ALG-14 — Arbitrary compatible families need not have joins

**Scan/place:** 033, L5–6, distributivity insertion, and margin opposite axiom 4. **Kind:** unproved claim / scope clarification by counterexample. **Quote:** “pour une famille”; “finie si I fini”. **Context/relation:** E39 uses an explicitly finite family of closed subspaces; S3 §1.6 does not certify existence of arbitrary joins. **Register IDs:** MPL_150_044-084 Q9, thematic only. **Confidence:** high, finite-interval argument below. **Attribution:** example suggested by the primary reader and checked here.

Even for the totally ordered real line, the compatible family `Y_n={n}` has no join in the algebra of finite unions of points and intervals. Any member containing all the natural numbers contains a final ray, from which one can remove a noninteger point and remain a strictly smaller tame upper bound. Thus the displayed family distributivity must be restricted to finite families or to joins whose existence and relevant compatibility are separately supplied; the margin's possibly infinite generated Boolean algebra need not be complete.

## Appendix A — A precise weak-axiom countermodel, not a refutation of PB

Let `U={1,2,3,4,5}`, `M=P(U)`, with ordinary subset order, intersection, union, complement, and identity closure. Put `X={1,2}`, `Y={1,3}`. Define `P⊙Q` when at least one of the four sets

`P∩Q`, `P∩Qᶜ`, `Pᶜ∩Q`, `Pᶜ∩Qᶜ`

is empty, or when the unordered pair of their complementary bipartitions is the pair associated with `X` and `Y`. Equivalently, add to the first relation all pairs in the complement-and-symmetry orbit of `(X,Y)`.

This relation is reflexive, symmetric, contains comparable pairs, and is invariant under complementing either entry. Ordinary complements are the largest compatible disjoint elements, with the stated uniqueness and involution properties. All meets and joins exist globally and all distributive and De Morgan **order identities** hold, while closure axioms 5–7 hold with all elements closed.

Nevertheless `X⊙Y` and the permitted Boolean expression `(X∨Y)∧¬(X∧Y)` yields `{2,3}`, which is incompatible with `X`. Also, with `A={1,2,3,4}`, the relative complements `A\X={3,4}` and `A\Y={2,4}` are incompatible although `X⊙Y`. The second example pinpoints why compatibility of the generated expressions matters in scan 036.

This does **not** satisfy PB, and it does not satisfy a stronger reading of distributivity which includes the compatibility of every intermediate partial-operation input. Under that stronger reading, a pairwise compatible triple forces `x⊙(y∨z)` by definability of the left side; complement invariance gives the analogous meet closure. Iterating this closure yields compatible Boolean families. Thus the issue is the precise logical formulation, not a counterexample to the explicitly strengthened theorem of scan 034.

## Appendix B — Independent proof of relativization

Assume the order, compatibility, complement, PB and closure requirements stated above. Let `M_A={x∈M:x≤A}` with inherited order and compatibility.

### B.1 Bounds and Boolean operations

The relative bounds are `0` and `A`. Compatible `x,y≤A` have ambient meet and join in `M_A`: their meet is below each, and their join is below the common upper bound `A`. Consequently these are also the relative meet and join.

Since `x≤A`, the elements `x,A` are compatible. Complement invariance and PB show that `A∧¬x` exists and is compatible with `x`. For any compatible `y≤A` disjoint from `x`, maximality of the ambient complement gives `y≤¬x`, hence `y≤A∧¬x`. The candidate itself has zero meet with `x` and join `A` with `x`, proving the relative complement formula.

For a finite pairwise compatible family `x_1,...,x_n≤A`, append `A`; PB gives an ambient Boolean algebra `B`. The principal ideal

`B|A={b∈B:b≤A}={A∧b:b∈B}`

is closed under the relative operations and is a Boolean algebra with unit `A`. The map `q_A(b)=A∧b` preserves meets, joins, zero and the relative unit, and

`q_A(¬b)=A∧¬b=A∧¬(A∧b)=¬_A q_A(b)`.

Every relative Boolean term in the `x_i` is therefore an ambient term multiplied by `A`, and conversely. This proves relative PB, complement involution, order reversal and complement invariance of compatibility. In particular `¬_A x` and `¬_A y` lie in the same block whenever `x,y≤A` are compatible. The phrase “an ideal is a Boolean algebra” is justified here because the ideal has greatest element `A`; no claim about arbitrary ideals is needed.

### B.2 Relative closed objects and least closed majorants

First, closure defined by a least closed majorant is extensive, monotone and idempotent. If `F,G` are compatible and closed, then `F∧G≤F,G` implies `c(F∧G)≤F,G`, hence `c(F∧G)≤F∧G`; extensivity gives equality.

For `x≤A`, axiom 7 applied to `x⊙A` gives `c(x)⊙A`, so `c(x)∧A` exists. If `x=F∧A` for a closed `F⊙A`, monotonicity gives `c(x)≤F`, and therefore

`x≤c(x)∧A≤F∧A=x`.

Conversely, if `x=c(x)∧A`, take `F=c(x)`. Thus the two definitions of relative closedness on scan 035 agree.

The object `c_A(x)=c(x)∧A` is relatively closed by this characterization. If a relatively closed `z=F∧A` contains `x`, then `F≥x`, so `F≥c(x)` and `z≥c(x)∧A`. This proves the relative least-majorant property, including the point in the manuscript where `Y=c(X)` must qualify as compatible with `A`.

The relative zero is closed because `c(0)=0`, and the relative unit is closed because `A≤c(A)` gives `c(A)∧A=A`.

### B.3 Join preservation and closure compatibility

For compatible `x,y≤A`, axiom 7 implies that `c(x),c(y),A` are pairwise compatible: closure preserves compatibility with the other element and with `A`, and applying the axiom to the other coordinate gives compatibility of both closures. PB therefore makes the following distributivity legitimate within one Boolean block:

`c_A(x∨y)=c(x∨y)∧A=(c(x)∨c(y))∧A=(c(x)∧A)∨(c(y)∧A)`.

Similarly, `c(x),A,y` form a compatible family, so their generated Boolean algebra contains `c(x)∧A` and `y`, proving `c_A(x)⊙y`. This is exactly relative axiom 7. Together with B.1 and B.2 it completes the conditional theorem without using the special dimension-one axiom 8 or assuming that `A` is closed.

## Appendix C — Six-element counterexample to clopen centrality

The order has bottom `0`, top `1`, and four incomparable intermediate elements `a,a′,b,b′`. The Boolean blocks are `B_a={0,1,a,a′}` and `B_b={0,1,b,b′}`; compatibility means belonging to a common block. Complement swaps `0↔1`, `a↔a′`, `b↔b′`. Set `M_f=M` and `c=id`.

1. The bounds and compatibility of comparable pairs are immediate.
2. Compatible pairs have the ordinary infimum/supremum of their four-element Boolean block, and these are also infimum/supremum in the full six-element order.
3. Every pairwise compatible family lies in one block, apart from the shared `0,1`, so distributivity and PB hold. The finite certificate checks all 28 such families and their generated algebras.
4. For `a`, the compatible elements disjoint from it are precisely `0,a′`; the maximum is `a′`, the only compatible complement. The other cases are identical, while `0` and `1` complement each other. Complement invariance of compatibility and order reversal hold.
5. Every element is closed; identity closure satisfies the least-majorant, join-preservation and compatibility axioms. Since every complement is closed, every element is also open.

Yet `a` and `b` are incompatible. Thus clopen centrality is independent of 1–7 plus PB. The later conditional claim is correct: **if** all clopen elements are universally compatible, then they form one Boolean algebra, because compatible finite meets/joins of closed elements are closed and complements of clopens are clopen. The counterexample concerns that antecedent, not the validity of this implication.

As an ordered-complemented lattice this is the same six-element structure displayed in S7's matching-graph support example. This run checks the present Boolean/closure axioms only, not all the atelier axioms asserted by the sweep.

## Appendix D — The extra-closure generator example

Take `U={1,2,3}`, `M=P(U)`, with all pairs compatible. Let the closed objects be `∅,{1,2},U`. Thus

`c(S)=∅` for `S=∅`; `c(S)={1,2}` for nonempty `S⊆{1,2}`; and `c(S)=U` if `3∈S`.

This is the least-majorant closure of a family closed under intersections and finite unions; directly, it is extensive, monotone, idempotent and union-preserving. Consequently 1–7 and PB hold. With `A=U` and `X={1}`, Boolean generation gives

`{∅,{1},{2,3},U}`,

whereas adding `c(X)={1,2}` supplies the separate atoms `{2}` and `{3}`, hence all eight subsets. Also `i(X)=∅` and `Fr(X)={1,2}≠X`, giving a finite witness to ALG-03's missing implication.

## Appendix E — Formal boundary checks

The two closures `c(x),c(¬x)` are compatible by axiom 7 and complement compatibility; their meet is closed by Appendix B.2. Put `i(x)=¬c(¬x)`. Order reversal makes `i(x)≤x`, and

`x≤Fr(x) ⇔ x≤c(¬x) ⇔ x∧i(x)=0 ⇔ i(x)=0`.

Here all operations are within compatible Boolean blocks, and `x∧i(x)=i(x)` because `i(x)≤x`. If `x=Fr(x)`, closedness of the frontier makes `x` closed; conversely, closed `x` with `i(x)=0` has `c(¬x)=1` and hence `Fr(x)=x`.

Substitution of the relative complement and closure formulas yields

`Fr_A(x)=A∧c(x)∧c(A∧¬x)`.

Monotonicity gives `c(A∧¬x)≤c(¬x)`, proving the boundary inequality in ALG-13. This is a formal result under the abstract hypotheses, while the real-interval example demonstrates strictness.

## Appendix F — Infinite joins and the finite-family qualification

Let `M` be the Boolean algebra of finite unions of singleton points and open, closed or half-open intervals in `R`, allowing unbounded intervals. All pairs are compatible. Suppose `Z∈M` contains every natural number. A finite union of bounded intervals and points is bounded above, so some component of `Z` contains a final ray. Choose a noninteger real `q` in that ray. The set `Z\{q}` is again a finite union of allowable pieces, contains every natural number, and is strictly smaller than `Z`. Therefore there is no least upper bound of the family `{ {n}:n∈N }` in `M`.

The point is not a defect in Boolean algebra: its operations and finite generation involve finite terms only. Nor does this refute a distributivity statement explicitly conditional on existence of the displayed joins. It prevents silently supplying unrestricted join existence to the manuscript's unqualified word “famille”.

## Certificates and limits

`research/algebra_checks.py` contains no manuscript data and reproduces the finite checks. Its output is saved in `research/algebra_checks_output.json`. The weak relation model passes the order-identity version only; the six-element model passes the full compatible-family strengthening; the three-point closure model passes the full Boolean/closure assumptions. None of these computations validates a scan reading, the general non-total `Mod(L)` construction, the sweep's entire atelier theory, or a register's stronger geometric claims.
