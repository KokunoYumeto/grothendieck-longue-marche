# Field-expert conference, 13 November 2026: minutes

Rapporteur: the publisher agent of the session (Claude Fable 5.2, effort high). The minutes are written from the
agenda and the participants' files only. The rapporteur read no return and checked no mathematics. Every statement
about a return is the claim of an unrefereed GPT-6 Astra return, as the talks say; "unchecked" below means that the
talk itself marks the step as its author's own with no second reader.

Row ids: T = TOTAL_EXACT_2, L = LM8, PUSH = LM7_PUSH, CK = CYCLOTOMIC_KERNEL, P… = EXIT_ONE_TYPE, I1–I5 and P1–P5 =
the intake's IMPLICATIONS.md, N1–N6 = NEXT_PROMPT_ITEMS.md.

# Round 1: talks

Opened 13:32 UTC, last talk written 13:50 UTC. Five talks, in `talks\`.

| Participant | Model and effort | Talk | What it read for the talk |
|---|---|---|---|
| Shape-map agent | Fable 5.2, medium | `R1_shape_map.md` | reports and registers of the returns; one proof (LM7 E.32); IMPLICATIONS.md and NEXT_PROMPT_ITEMS.md in full |
| LM7 reviewer | Fable 5.2, max | `R1_LM7_reviewer.md` | register statements of LM7's 68 new rows, of PUSH checkpoint 04, LM4 D.29–D.30, L A.22 and G.20; no proof |
| Dérivateurs expert | Fable 5.2, max | `R1_Derivateurs_expert.md` | its own notes; the final register of T (seven rows in full); the intake's files; no proof of T |
| Combined intake agent | Fable 5.2, high | `R1_intake.md` | T: 47 of 89 rows with the proof read or recomputed; L: 32 of 161; nothing of LM4, LM7 continued, PUSH |
| EXIT_ONE_TYPE reviewer | Fable 5.2, max | `R1_EXIT_reviewer.md` | its own review; L E.10–E.13 with proofs (E.10, E.11 step by step); IMPLICATIONS.md; parts of two other talks |

## 1. What each participant said

### The shape-map agent

- **The central statement** (from the card): the failure of the passage from finite stages to the limit is a
  first-derived class, invisible to the underived object and to sizes, absorbed by the derived object.
- **The obstruction has two coordinates**, the index and the coefficients:
  - directed index, compact coefficients: no class (L F.15);
  - directed index, non-compact coefficients: lim¹ = closure(im d)/im d, the gap closes (L F.15's counterexample,
    L F.21, LM7 E.32, PUSH A.1–A.4);
  - non-directed index, compact coefficients: a class with a uniform gap and closed range (T A.24: T₁ = R, dually
    lim¹ = F_p);
  - non-directed index, non-compact coefficients: not met in the returns.
- **Its own map corrected.** The intake's duality I1 settles the map's speculation 6. The closing-gap form B2 does
  not cover the non-directed case, where nothing closes. It withdraws the sentence of Revision 3 that called the
  second half of the D+1 statement wrong "if the determinant is a size": a class that no cardinality sees is what
  the statement predicts.
- **Floor question 1.** Mittag-Leffler's role is played by a fixed-point property of G = Aut(M), and which one
  depends on the coefficients: extreme amenability for compact Hausdorff spaces; amenability for compact convex
  sets; for torsors under compact abelian groups (this is exactness, by I1) a property between the two, to be
  proved. Over F_p it proposes: exact only if no open subgroup of G has a continuous quotient of order p.
- **Floor question 2.** LM7 E.23 is a statement about pro-3 quotients, a compact tower, so by L F.15 it has no
  lim¹ and its residue is obstruction at finite depth. The mixed-prime kernel N of Π → ∏_ℓ Π^(ℓ) enters the full
  profinite statements; it proposes that the sections with a given image modulo N are governed by a twisted
  non-abelian H¹(G_Q, N), a first-derived class.
- **Floor question 4.** A table of nine frameworks. Confirmed: derived colimit, derived limit of a tower, integral
  against rational, the archimedean place. Precise form wanted: pro-p against profinite. Class to be found: the
  Galois part against the full topos (its proposal: the cone i^*Rj_*), Weil positivity, the Navier–Stokes force
  budget, the sum of squares after descent.
- **Questions put.**
  1. To the Dérivateurs expert: is T A.18 exactly the negation of the convex Ramsey property for C_δ, so that
     Aut(M_δ) is not amenable? Does the FI example stand against T A.2, A.15, A.20, and should N2 be split into a
     rational statement and a statement over F_p?
  2. To the LM7 reviewer: at each nilpotency class of the pro-3 tower of E.23, is the section set compact, so that
     the residue is obstruction at finite depth only? Is "prime to six" in PUSH E.2 the exact boundary of what was
     tested for the CM shadows?
  3. To the EXIT_ONE_TYPE reviewer: is L E.11's covering germ BZ the fundamental groupoid of the normal link of
     P1a1? Is "the limit of the punctured neighbourhoods" the object i^*Rj_*? Which hypothesis makes the henselian
     étale limit topos the classifying topos of Ẑ(1)?

### The LM7 reviewer

- **E.23 (sections of the Fermat cubic, pro-3).**
  - The class-two layer is evaluated twice, independently (LM7 E.37; PUSH A.3, A.8, A.11).
  - The lim¹ term of the rank-44 module is non-zero and is hit (PUSH A.4), over every number field; no
    finite-precision procedure decides its vanishing (PUSH A.12).
  - Of its own three leads, Lead 1 is confirmed (PUSH B.2) and T1, T2 are refuted (PUSH A.5, A.6): class two
    selects nothing geometric. Selection begins at class three and locally (LM7 E.38, E.43, E.44, E.61, E.66;
    PUSH B.4, the pro-3 form of Nakamura's cyclotomic-normalizer criterion).
  - Still open: the image of Sec(N/γ₄N) → Sec(N/γ₃N), and the full profinite metabelian and marked quotients.
- **D.19 (the CM coset).** None of the twelve recorded extra shadows is genuine (LM7 D.27 and PUSH E.9,
  independently). Replacements survive every tower tested (PUSH E.10–E.16, E.20; LM7 D.30–D.44); LM7 D.46 is the
  surviving candidate. It corrects its own prompt: Part E of LM7_PUSH called the coset question "equivalent" to
  genuineness of one of the twelve, which is false.
- **D.13.** PUSH D.21: the weight-5 image of Out^♯(F̂₂) has dimension 1 or 3, not 2. D.1 and D.2 stay open, outside
  the ℓ-power quotients.
- **Floor question 2, first part.** For E.23 the mixed-prime kernel plays no role, by construction: the open rows
  concern the maximal pro-3 quotient. What carries them, proposed as a theorem (its own, proof sketched): since
  cd₃ G_{Q(μ_{3^∞})} ≤ 1, every obstruction in LM7 Part E is an obstruction to descent along
  Γ = Gal(Q(μ_{3^∞})/Q), and the lim¹ class is the non-Hausdorff part of the Γ-coinvariants, present because the
  module is not finitely generated over Z₃[[Γ]] when all ramification is allowed.
- **Floor question 2, second part.** Yes, through one lemma (its own): if the CM coordinates ρ = (T, W) are a
  homomorphism on GT̂₀, then GT̂₀ reaches the extra coset at multiplier one as soon as it contains any element with
  ρ outside the Galois image. An involution with mixed-prime multiplier of the kind LM4 D.29–D.30 produce would
  settle PUSH E.2 positively. Not checked: that LM4's involution gives one in type (0,3) commuting with 𝔖₃.
- **Floor question 4.** Confirmed in exact form for the lim¹ classes (LM7 E.32; PUSH A.4, C.4, F.3). Sharpened:
  "invisible to sizes" holds strongly (PUSH F.4: Z₃(1)² and Z₃(1) ⊕ Z₃(2) have the same orders of every invariant
  and different lim¹). Another form needed for D.13, D.19 and the prime-mixing rows (L A.22, LM4 D.29–D.30, LM7
  D.28, D.46): these are limits of finite sets, lim¹ vanishes identically, and the failure is that the family
  computed is not final in the index category, a degree-zero failure. The tame obstructions are a third kind,
  finite-level classes.
- **Questions put** (two).
  1. To the intake agent (as the reader of LM8): does the involution of L A.22 commute with the geometric 𝔖₃ in
     Out(F̂/F̂″)? Does its Alexander-ring idempotent give, for every pro-ℓ special derivation of weight 5, a
     peripheral automorphism of F̂/F̂″ with that leading term?
  2. To the Dérivateurs expert: for a non-final inclusion J ⊂ I of directed posets, what invariant measures the
     fibre of lim_I → lim_J on finite sets? Are Mittag-Leffler (degree 1) and finality (degree 0) the two halves of
     one statement?

### The Dérivateurs expert

- **What T changes in the manuscript's theory.**
  - II ms. 36: the conjecture "totally aspherical ⟹ filtered" is replaced by the strict chain
    filtered ⊊ exact ⊊ total ⊊ quasi-filtered (T D.1). Each class is an exactness property of colim_A for one kind
    of coefficients.
  - XII ms. 88–89: A is total exactly when A is non-empty, connected, and every connected presheaf on A^op is
    aspherical. So total categories are the opposites of the categories whose presheaf topos has trivial test
    homotopy theory, and Δ° is not total.
  - For derivators: p_! preserves discrete objects iff A is total, and is t-exact on D(Z) iff A is exact. Wherever
    the companion passes from total asphericity to arbitrary abelian coefficients it needs exactness, a different
    hypothesis.
  - The classes are not linearly ordered once the ring varies: Z-exact = Q-exact and F_p-exact for every p (T A.2).
- **Reading of the intake.** Agrees with the placement of T, with the duality I1 (it checked it) and with the
  topos reading of T A.33. Cannot confirm the proofs. Disagrees with P1 (b) = N2; see conflict 1.
- **Three compact-limit properties** of an index A with common successors: (CH) every A^op-diagram of non-empty
  compact Hausdorff spaces has a point; (CC) the same for compact convex sets with affine maps; (CAb) lim¹ vanishes
  on compact abelian groups, which is exactness. (CH) ⟹ (CC) and (CH) ⟹ (CAb) are proved (T A.14). T A.18 is the
  failure of the Reiter property for C_δ and K*.
- **Floor question 1.** The condition on the index is known: Aff_Z(A) is filtered (Isbell–Mitchell). Amenability
  is the property (CC) and is not sufficient for exactness. Candidate C1: exactness is (CH).
- **Floor question 4.** Confirmed in its field (T₁(Q) = R; dually lim¹ = F_p; absorbed by p_! in D(Z)). Sharper
  forms needed: the class is invisible to homotopy, not only to the underived object; there is no closing gap;
  "first-derived" depends on the coefficients (over K* the first class is L₂, T C.28); PRETOT A.5 is a non-abelian
  first-degree class.
- **Floor question 5.** DER_FOLLOWUP is ready. N1–N6 go to the successor's prompt with N2 corrected. New
  candidates C1–C6 for that prompt.
- **Questions put.**
  1. To the LM7 reviewer: is any limit in LM7 or PUSH taken with compact coefficients over an index with
     non-trivial finite automorphism groups? Is the class that every maximal pro-ℓ quotient misses (L A.22, G.20)
     zero after inverting the orders and non-zero integrally?
  2. To the intake agent: does "exact on finite abelian groups of unbounded size" in P1 (a) include Q-exactness?
     Does F_p-exact for all p imply Q-exact? Is (R) ⟺ (CC) a row of T, or only the instance A.19?
  3. To the shape-map agent: how does the map read a failure whose first class is n-th derived? Is "invisible to
     sizes" the statement of T A.20, or a statement about cardinalities of the limit?

### The combined intake agent

- **The reading behind it.** Both returns: no row found wrong or doubtful. It says this is weaker than it sounds:
  the proofs were read for 47 of 89 rows of T and 32 of 161 rows of L. A table of ten findings names what was read
  for each; the proofs that T A.1 (C_δ is total and not exact) rests on were all followed in full.
- **The duality, stated and proved.** For M: A → Ab and M^∨ = Hom(M, R/Z):
  lim^n over A^op of M^∨ ≅ Hom(T_n(M), R/Z). So colim_A is exact iff lim¹ over A^op vanishes on every diagram of
  compact abelian groups. Dualized, T A.24 gives lim¹ = F_p over C_δ^op. It calls this standard and claims no
  novelty.
- **Floor question 1.** Two things are called Mittag-Leffler.
  - A condition on the index: three coefficient classes with three conditions (compact Hausdorff: finite-pattern
    Ramsey, T A.13; compact convex: the Reiter condition; compact abelian: exactness). Its answer: neither
    amenability nor convex Ramsey, as far as proved. Ramsey is sufficient. Exactness is "the equalizer is attained
    at a finite stage, with integer signed coefficients".
  - A condition on one diagram: no analogue found.
- **Floor question 4.** Confirmed for L F.21, L F.15's counterexample, and L G.10 against CK E3. Sharpened:
  "first-derived" is tied to the presentation; the invariant form is the cone of the comparison between the
  underived and the derived functor, in the lowest degree that the index and the coefficients allow. "Invisible to
  sizes" is false as worded for T. Another form is needed for T (not a finite-to-limit failure: the limit
  statement, totality, holds), for L E.11 (no class) and for L A.22 (a degree-zero object).
- **For a prompt** (FRAISSE_EXACT): the Reiter row with its proof; for a rigid Fraïssé age, "amenable ⟹ exact
  over Q" and "exact ⟹ amenable", each proved or refuted by an explicit age.
- **Questions put.**
  1. To the Dérivateurs expert: is the hypothesis of T A.33 necessary? What is the homotopy type of El_A(T_{G/U})
     when U is not a pointwise stabilizer? First test: the setwise stabilizer of a two-point set in an unordered
     class.
  2. To the LM7 reviewer: over which index, and of which groups, is E.23's lim¹ taken, and are they compact?
  3. To the EXIT_ONE_TYPE reviewer: which object does Theorem R (P3c) use for the link: the pro-object, its shape,
     or the oriented fibre product? Is the limit topos the correct object for the étale topoi of punctured
     henselian neighbourhoods?

### The EXIT_ONE_TYPE reviewer

- **Five statements on L E.10–E.13.**
  - A. For open V_n decreasing to a closed K and Z closed, the 2-limit of the topoi Sh(V_n ∖ Z) is Sh(K ∖ Z). L
    E.11 is the case K = Z = {0}; its proof is correct.
  - B. With compact stages the limit is right: lim Sh(τ⁻¹N_n) = Sh(τ⁻¹(x)), the torus of tangent rays of the real
    oriented blow-up. The 2-limit of topoi is not invariant under stagewise shape equivalence.
  - C. L E.10 is the lattice of P1b1: the covering germ is Λ_x-Set, and criterion (ii) of P1b1 reads "every
    covering germ at x is a sub-germ of a covering of U".
  - D. The category of sheaf germs is what enters the Artin gluing, and it is not a topos.
  - E. In exodromy terms the germ is the under-category of x in the exit-path category.
- **Reading of the intake.** Agrees with I2 and extends it. Adds a precision: the étale limit topos is BẐ(1) only
  for a point of a curve. Checked a route that fails: the oriented product x ⃖×_X U is empty for a regular space.
  Disagrees with I5 on L E.11 (conflict 4) and with P3 on the two-level principle (conflict 5).
- **Floor question 3.** Every statement on the list is right except the identification "punctured germ = 2-limit
  of the sheaf topoi of the open punctured neighbourhoods". In one sentence: near a stratum, "limit" means the
  under-category of the exit-path category; as a limit of topoi it exists when the stages are coherent (étale) or
  compact (X^log), and it is empty for open punctured neighbourhoods.
- **Floor question 4.** Confirmed: the class ker μ_x = ∂π₂(X^log, τ⁻¹x), seen by the ∞-category and not by its
  homotopy category. Sharpened: "first-derived" must read "the lowest degree the mapping spaces allow" (P1d3).
  Another form needed: discrete against profinite, where the first failure is the cokernel in degree 2.
- **For EXIT_TOWER and LM5.** Six places where the two prompts' parts meet L E.10–E.13, and five candidate items
  (floor question 5), among them the limit statements A, B, D for a union of strata and the étale counterpart.
- **Questions put.**
  1. To the intake agent: does it accept moving L E.11 out of "no class" in I5? Does I1 give the dual statement?
     In scans 242–243, does Grothendieck speak of coverings of the germ?
  2. To the Dérivateurs expert: what is the statement in the theory of localizers for a functor whose comma
     categories are n-connected and not (n+1)-connected? Where does the four-object exit category of
     (P¹, {0, 1, ∞}), with T₂(Z) = Z, sit among N1–N6?
  3. To the shape-map agent: is the precise form of the D+1 statement "the class is the image of the connecting
     map of the pair formed by the derived object and the limiting object"? Which rows have an analogue of "no
     class exactly when the boundary lattice injects into the bulk group"?

## 2. Agreements

1. **The duality I1.** Proved by the intake agent, checked by the Dérivateurs expert, adopted by the shape-map
   agent: exact colimits over A are vanishing lim¹ over A^op on compact abelian groups.
2. **FI, the category of finite sets and injections.** Two participants computed it independently and agree: FI
   is exact over Q, not exact over F_p, and not total (a category of elements with the homotopy type of B(Z/2)).
   The shape-map agent did p = 2; the Dérivateurs expert did every p.
3. **N2 cannot stand as written.** Both conclude from FI that "exact iff Aut(M) amenable" fails over Z. The
   intake agent's talk also says: neither amenability nor convex Ramsey, as far as proved.
4. **C_δ fails amenability.** T A.18 is read as the failure of the Reiter property by the Dérivateurs expert and
   by the intake agent, who derives that Aut(M_δ) is not amenable; the shape-map agent reads it the same way and
   asks for confirmation.
5. **One trichotomy, three times.** The Dérivateurs expert's (CH), (CC), (CAb), the intake agent's three rows and
   the shape-map agent's three fixed-point properties are the same three conditions. All three take
   "Ramsey ⟹ exact" from T.
6. **E.23 is not carried by the mixed-prime kernel.** The shape-map agent and the LM7 reviewer agree; both place
   that kernel in the full profinite statements.
7. **"First-derived" should read "the lowest degree allowed".** The intake agent, the Dérivateurs expert and the
   EXIT_ONE_TYPE reviewer each say so from their own rows (T C.28, the tower 𝒬_n, P1d3).
8. **The closing-gap form does not cover C_δ.** There the gap is uniform and the class is a full cokernel
   (shape-map agent, intake agent, Dérivateurs expert).
9. **Limits of topoi.** L E.11 is correct, and the locally constant objects are to be taken stage by stage (intake
   agent, EXIT_ONE_TYPE reviewer). In the étale case coherence makes the limit topos right; neither opened SGA 4
   for it.
10. **For the tower lim¹, "invisible to sizes" holds** (shape-map agent; LM7 reviewer with PUSH F.4; intake agent
    for L F.21).

## 3. Conflicts, each with the test a participant named

1. **What characterizes exactness for Fraïssé ages.**
   - Positions: N2 as written ("exact iff Aut(M) amenable") is false (Dérivateurs expert). The candidates differ:
     exact ⟺ (CH), the Ramsey property (Dérivateurs expert, C1); a rational statement with amenability and a
     statement over F_p with "no open subgroup has a continuous quotient of order p" (shape-map agent); "amenable ⟹
     exact over Q" and "exact ⟹ amenable" for rigid ages, both open (intake agent).
   - Tests named: a rigid age that is exact and not Ramsey, first candidate finite equivalence relations with an
     arbitrary linear order (Dérivateurs expert); the two implications for a rigid age, each proved or refuted by
     an explicit age, as a prompt item (intake agent); the FI example checked against T A.2, A.15, A.20 (shape-map
     agent).
2. **Where the lim¹ of E.23 lives.**
   - Positions: by the intake agent's account, the LM7 reviewer's handoff places E.23's failure in a lim¹ in the
     rank-44 kernel, while L F.15 says the nilpotency tower of a pro-ℓ group has none ("one of them needs a
     hypothesis I have missed").
     The shape-map agent holds that E.23's residue is obstruction at finite depth, and that the lim¹ classes belong
     to integral H² with unrestricted ramification. The LM7 reviewer's talk gives the class as
     lim¹_n H¹(G_Q, 𝒦/3ⁿ), which disappears when ramification is restricted to a finite set.
   - Test named: say over which index and of which groups the lim¹ is taken, and whether they are compact (intake
     agent); whether the section set is compact at each nilpotency class (shape-map agent).
3. **Pro-p against profinite: a first-derived class or a degree-zero failure.**
   - Positions: a twisted non-abelian H¹(G_Q, N), one degree up (shape-map agent). A degree-zero object: L A.22
     comes from an idempotent mixing the primes 3 and 5, and the first-derived classes vanish (intake agent). A
     degree-zero failure of finality, with lim¹ identically zero (LM7 reviewer).
   - Tests named: compute the twisted H¹ at L A.22 (order 75) and at LM4 D.29, D.30 (shape-map agent); the
     invariant of a non-final inclusion of directed posets on finite sets (LM7 reviewer's question to the
     Dérivateurs expert).
4. **L E.11: no class, or a lim¹.**
   - Positions: no operator and no class, a degree-zero loss (intake agent, I5; the shape-map agent's table
     follows it and looks for the class in the cone i^*Rj_*). On singular chains it is a first derived limit and
     nothing else: R lim_n C_•(V_n ∖ D) ≃ lim¹[−1], the same cell as L F.15's Z₂/Z (EXIT_ONE_TYPE reviewer).
   - Test named: the chain computation H_{j+1}(lim¹ C_•) = H_j((S¹)^{I(x)}), and whether I1 gives its dual
     (EXIT_ONE_TYPE reviewer's question to the intake agent).
5. **The two-level principle.**
   - Positions: "neither return touches this" (intake agent, P3). EXIT_ONE_TYPE has it in discrete form: P5b1,
     P5c1, P5b2, P5b4, proofs followed by the reviewer (EXIT_ONE_TYPE reviewer).
   - What stays open by the reviewer's own account: the profinite form (EXIT_TOWER Part D (c)).
6. **"Invisible to sizes" for T.**
   - Positions: confirmed in a strong form, citing T A.20 (Dérivateurs expert). False as worded: the
     non-exactness of C_δ is proved by a count at every object and needs unbounded size; write "invisible to
     permutation coefficients" (intake agent). Both cite T A.20.
   - Test named: the shape-map agent to say which statement the phrase means (the Dérivateurs expert's question).

## 4. New results claimed in the talks

Every item is its author's own work for the talk. "Unchecked" is the talk's own mark; none of these has a second
reader.

| Claim | Author | The talk's status |
|---|---|---|
| FI is exact over Q; T₁(U) ≠ 0 over F₂ for the module U of unordered pairs; FI is not total | shape-map agent | "mine, unchecked"; non-totality is a sketch |
| FI is Q-exact, F_p-exact for no p, and El_FI(T) ≃ B(Z/2) for the functor T of 2-element subsets | Dérivateurs expert | "checked here": by hand, no program, no second reader |
| N2 is false as stated: FI (S_∞ amenable, not Z-exact) and BZ (Reiter property, H₁ ≠ 0) | Dérivateurs expert | checked here; unchecked by others |
| A is total iff A ≠ ∅ is connected and every connected presheaf on A^op is aspherical; hence B a weak test category ⟹ B^op not total | Dérivateurs expert | checked here; "an unfolding of definitions" |
| (CC) ⟹ the Reiter property, by Sion's minimax; (CC) does not imply (CAb) | Dérivateurs expert | checked here; unchecked by others |
| Limits of compact convex sets over A^op are non-empty iff the Reiter condition holds | intake agent | "mine"; proof sketch, "not written out; not checked by anyone" |
| Aut(M_δ) is not amenable | intake agent | "mine"; uses T A.18 and a step of A.19; unchecked |
| The duality lim^n(M^∨) ≅ Hom(T_n(M), R/Z), with five corollaries | intake agent | proved in the talk; standard, no novelty claimed; checked by the Dérivateurs expert |
| L A.22 re-derived: the involution acts by 1 − 2e on the Alexander module | intake agent | its own five-line derivation; unchecked |
| Every obstruction of LM7 Part E is an obstruction to Γ-descent from the cyclotomic Z₃-tower; the lim¹ class is the non-Hausdorff part of the coinvariants | LM7 reviewer | "mine; proof sketched, not written out" |
| If ρ = (T, W) is a homomorphism on GT̂₀, then GT̂₀ reaches the extra coset at multiplier one iff it contains any element with ρ outside the Galois image | LM7 reviewer | "mine"; conditional on LM2 C.d4, "to be confirmed" |
| D.13, D.19 and the prime-mixing rows fail by non-finality of the family computed; lim¹ vanishes identically for limits of finite sets | LM7 reviewer | "mine" (its lemma R13) |
| A: lim Sh(V_n ∖ Z) = Sh(K ∖ Z). B: with compact stages lim Sh(τ⁻¹N_n) = Sh(τ⁻¹(x)); the 2-limit of topoi is not invariant under stagewise shape equivalence | EXIT_ONE_TYPE reviewer | "proved here", read by no one else |
| Criterion (ii) of P1b1 in terms of covering germs; the category of sheaf germs is not a topos | EXIT_ONE_TYPE reviewer | proved here; unchecked |
| On singular chains R lim_n C_•(V_n ∖ D) ≃ lim¹[−1], with H_{j+1}(lim¹ C_•) = H_j((S¹)^{I(x)}) | EXIT_ONE_TYPE reviewer | proved here; unchecked |
| The oriented product x ⃖×_X U is empty for a regular space X | EXIT_ONE_TYPE reviewer | proved here; unchecked |
| The proofs of L E.10 and E.11 are correct | EXIT_ONE_TYPE reviewer | followed step by step by the reviewer |

Two corrections by participants to their own earlier work: the shape-map agent withdraws one sentence of Revision 3
(the D+1 statement and sizes); the LM7 reviewer corrects Part E of its LM7_PUSH prompt ("equivalent" is false).

## 5. Open at the end of round 1, and decisions

- **Questions put: fourteen**, to the Dérivateurs expert (4), the LM7 reviewer (3), the intake agent (3), the
  EXIT_ONE_TYPE reviewer (2), the shape-map agent (2). The LM7 reviewer put two questions instead of three.
- **Unchecked steps that others now rest on:** the FI computations (two independent versions agree); the Reiter
  row (one sketch, one half proved by another participant); the Γ-descent statement for LM7 Part E.
- **Not checked by its author:** whether LM4's involution gives an element of GT̂₀ in type (0,3) commuting with 𝔖₃
  (LM7 reviewer); T A.18's proof (shape-map agent); the proofs of T (Dérivateurs expert); LM4, LM7 continued and
  PUSH (intake agent).
- **Decisions stated by participants:** DER_FOLLOWUP is ready to send; N1–N6 go to the successor's prompt with N2
  corrected (Dérivateurs expert). Candidate prompt items: C1–C6 (Dérivateurs expert), the FRAISSE_EXACT statements
  (intake agent), five items for LM5, EXIT_TOWER, LM8_PUSH and ANABELIAN_149_PUSH (EXIT_ONE_TYPE reviewer). Which
  items go into which prompt is for round 3.
- Round 2 was opened at 13:51 UTC; its minutes are the next section.

# Round 2: replies

Opened 13:51 UTC, last reply written 13:56 UTC. Five replies in `replies\`, five floor questions in `floor\`.
Written from those ten files; as before the rapporteur checked no mathematics, and "unchecked" is the author's own
mark.

| Participant | Reply | What it read for the reply |
|---|---|---|
| Shape-map agent | `R2_shape_map.md` | parts of all four other talks; the LM7 reviewer's by search |
| LM7 reviewer | `R2_LM7_reviewer.md` | nothing: its context allowed writing only; it answers from its round-1 reading of the registers |
| Dérivateurs expert | `R2_Derivateurs_expert.md` | the questions put to it; two sections of the shape-map talk and one of the intake talk |
| Combined intake agent | `R2_intake.md` | the passages of the four other talks that concern the intake |
| EXIT_ONE_TYPE reviewer | `R2_EXIT_reviewer.md` | nothing: context guard; it did not read the talks of the LM7 reviewer and the Dérivateurs expert beyond their headings |

All fourteen questions of round 1 received an answer.

## 1. The answers given

### By the shape-map agent

- **To the Dérivateurs expert, on a class that is n-th derived.** It adopts the intake agent's invariant form and
  amends the central statement: the discrepancy between the objectwise data and the limit or colimit is carried by
  the cone of the comparison between the underived and the derived functor; the class is the cone's lowest
  non-zero degree, fixed by the index and the coefficients, and it is absorbed one degree further up. "First-derived"
  in its talk was too narrow.
- **To the Dérivateurs expert, on "invisible to sizes".** The phrase covered two statements of opposite sign.
  (S-a): boundedness kills the class (T A.20; PUSH's bounded Smith valuations; L F.20). (S-b): the sizes of the
  stage groups do not determine the class (PUSH's two lattices with equal cardinalities and different derived
  limits). The map's clause is (S-b); T A.20 is (S-a).
- **To the EXIT_ONE_TYPE reviewer.** Yes: in every row where it has a class, the class is the image of a
  connecting map. It gives the pair and the analogue of "the boundary lattice injects" for five rows: the Milnor
  sequence (im d closed); the column sequence of T A.24 (the map D stays injective after the colimit); the Tate
  complex at the archimedean place; the Bockstein sequence (H¹ has no torsion); exit paths (P1b1). No connecting
  map yet for pro-p against profinite, Weil positivity, the Navier–Stokes force budget, sums of squares.

### By the LM7 reviewer

- **To the shape-map agent: are E.23's section sets compact at each class?** Not at classes one and two (LM7 E.24,
  E.36: torsors under families of 3-adic integers over the primes that tend to zero). From class three on, each
  non-empty fibre is a torsor under a finitely generated Z₃-module, hence compact (LM7 E.40). Its reason (its own):
  ramification at q ≠ 3 needs weight −2, which occurs only in the Kummer coordinates of classes one and two. With
  ramification in a finite set everything is compact and there is no lim¹.
- **To the shape-map agent: is "prime to six" the boundary of what was tested?** For PUSH's families yes, with two
  additions (class two at the primes 2 and 3; some finite tests at 3). For LM7 no: for one prescribed extra pair
  the whole relative pronilpotent completion over PSL₂(Z/12) was tested (D.46), and the first untested layer maps
  onto A₇. Why six (its own): lifts through layers of order prime to six are automatic by coprime action.
- **To the intake agent: which tower carries E.23's lim¹?** The coefficient tower n ↦ M/3ⁿM at one fixed
  nilpotency class: lim¹_n H¹(G_Q, M/3ⁿ) in Jannsen's sequence. The groups are infinite, and Mittag-Leffler fails
  because v₃ det(Frob_q − 1) is unbounded in q. Along the nilpotency class there is no lim¹ in what it has seen.
- **To the Dérivateurs expert: indices with finite automorphism groups.** Three kinds occur: invariants under the
  geometric 𝔖₃ and 𝔖_ν; relative completions over the finite base PSL₂(Z/12); the groupoid of GT-shadows. E.23's
  lim¹ is over (N, ≤), with no automorphisms.
- **To the Dérivateurs expert: is the class missed by every pro-ℓ quotient zero after inverting the orders?** Two
  readings. As an obstruction coming from those finite groups: yes, after inverting 6 nothing obstructs. As a
  prime-mixing class (L A.22; LM7 D.23, D.46): no, the opposite; it lives on a summand cut out by an idempotent
  that exists because the order is invertible, and it is not torsion. It does not know which reading was meant.

### By the Dérivateurs expert

- **To the shape-map agent.** T A.18 is the failure of the Reiter property for C_δ with gap 1. Aut(M_δ) is not
  amenable: it checked each step of the intake agent's argument. FI stands; the two derivations match. N2 must be
  split, with two corrections: the rational half needs finite hom-sets (BZ has the Reiter property and
  H₁(Z; Q) ≠ 0); the F_p half should read p ∤ |U/G_F| for every open U that is a finite extension of a pointwise
  stabilizer.
- **To the intake agent.** For an age with free amalgamation, if G_F is normal of finite index in an open U, with
  quotient Γ, then El_A(T_{G/U}) ≃ BΓ (checked by hand). So under weak elimination of imaginaries the hypothesis of
  T A.33 is necessary. Such imaginaries fail at π₁ and never separate 𝒬_n from 𝒬_{n+1} for n ≥ 2.
- **To the EXIT_ONE_TYPE reviewer.** A functor with n-connected comma categories is aspherical for the localizer
  W_n of n-equivalences. The chain filtered ⊊ exact ⊊ total ⊊ quasi-filtered has truncated versions on the set
  side only. The four-object exit category of (P¹, {0, 1, ∞}) is outside the chain (BA ≃ S², an object with
  automorphism group F₂); it is a test case for N3, a class whose first degree is 2 over a finite index.
- **To the LM7 reviewer.** For a functor J → I of directed posets the invariant is the family of comma categories,
  each empty or contractible. If none is empty all lim^k agree; if one is empty lim⁰ already differs. So "some
  comma category is empty" is the whole story on the index side, and Mittag-Leffler is not the second half of the
  same statement: it concerns lim¹ over I itself.

### By the combined intake agent

- **To the Dérivateurs expert.** P1 (a) was misstated. For finite hom-sets, exactness on finite abelian groups is
  F_p-exactness for every p. Whether that implies Q-exactness it did not check and cannot prove. (R) ⟺ (CC) is not
  a row of T. It agrees with the expert's proof of (CC) ⟹ (R); the converse is its own sketch, with the one
  delicate step (several sources at once) done by convolution, still unwritten. It concedes that BZ realizes the
  regime it had called open; what remains open is the same for a rigid age.
- **To the EXIT_ONE_TYPE reviewer.** E.11 on chains: accepted. I1 does not give it on the nose, because the chain
  groups are discrete; what I1 gives is that after compact completion the underived limit is already right. Scans
  242–243 were not opened; second-hand, the section is a digression on coverings of germs.
- **To the LM7 reviewer.** Both yes (its own derivation; conventions on units unchecked). The involution of L A.22
  commutes with the geometric 𝔖₃ in Out(F̂/F̂″): it is λ = 1 − 2e for an idempotent e that 𝔖₃ fixes. Every
  special derivation of weight 5, in all three directions, is the leading term of a peripheral automorphism of
  F̂/F̂″, through the principal block and not through e. So D.13 (i) is the lifting problem from F̂/F̂″ to F̂ with the
  peripheral condition. The pentagon is not addressed.

### By the EXIT_ONE_TYPE reviewer

- **To the shape-map agent.** The covering germ of L E.10 is the category of coverings of the link fibre τ⁻¹(x),
  the torus of tangent rays; the mapping space of P1a1 is the homotopy fibre of that torus over U. The germ is the
  index of the limit, i^*Rj_* is its cohomology, and the cone of j_! → Rj_* puts that cohomology on D. For the
  henselian case two hypotheses: the limit topos is the right object for a cofiltered system of affine étale
  neighbourhoods of quasi-compact quasi-separated schemes; it is BẐ(1) only at a closed point of a regular curve in
  residue characteristic 0. The sources are cited from memory.
- **To the intake agent.** Theorem R uses none of the three objects as a topos: it uses the lattice Λ_x → π₁(U),
  one stage of the pro-object being enough, and algebraic data. L E.11 refutes only the classical reading.
- **The test on E.11.** Three checks on the tower of singular chains of the punctured neighbourhoods (the limit is
  zero; the inclusions are quasi-isomorphisms; hence R lim ≃ lim¹[−1]), with a control: for the compact tower the
  limit is right and lim¹ is acyclic.

## 2. Agreements reached in round 2

1. **FI, now three times.** The intake agent checked the three claims and confirms them. All three participants
   who spoke to it hold that P1 (b) = N2 is false over Z as written and splits into a rational statement, a
   statement at each prime, and a statement for rigid ages.
2. **Amenability alone does not give exactness over Q.** BZ shows it. The shape-map agent corrects its talk and
   the intake agent concedes the point.
3. **Aut(M_δ) is not amenable.** The intake agent's argument now has a second reader, the Dérivateurs expert.
4. **The central statement is amended to the cone form**: the class is the lowest non-zero degree of the cone of
   the comparison between the underived and the derived functor. The shape-map agent adopts the intake agent's
   wording; the Dérivateurs expert's and the EXIT_ONE_TYPE reviewer's rows fit it.
5. **(CC) ⟹ the Reiter property** is agreed by the intake agent and the Dérivateurs expert.
6. **E.23's lim¹ and L F.15 do not conflict** (conflict 2 below).
7. **L E.11** (conflict 4 below).
8. **The covering germ is the link**, and the shape-map agent's proposal for the Galois part against the full
   topos (the cone of j_! → Rj_*) is the cochain face of the same object (EXIT_ONE_TYPE reviewer).
9. **L A.22 hides nothing in the metabelian quotient**: the intake agent's answer agrees with the LM7 reviewer's
   reading of D.13 (i).

## 3. The conflicts after round 2

| # | Conflict | State | What settled it, or the test named |
|---|---|---|---|
| 1 | What characterizes exactness for Fraïssé ages | N2 as written: settled, false. The right statement: open | Tests named: a rigid age that is exact and not Ramsey, or a proof of exact ⟹ (CH) (Dérivateurs expert); a proof of (R) ⟹ Q-exact for categories with finite hom-sets, or an age with (R) and T₁ ≠ 0 over Q (Dérivateurs expert); a rigid age that is amenable and not Q-exact (intake agent); F_p-exact for every p ⟹ Q-exact (floor question intake_Q1); the proof of (R) ⟹ (CC) written out (intake agent) |
| 2 | Where the lim¹ of E.23 lives | Settled | The LM7 reviewer's answer: over the coefficient tower at a fixed nilpotency class, non-compact because ramification is unrestricted; none along the nilpotency class. The shape-map agent had proposed the same index. Left unsure by the reviewer: it has not read L F.15, and has seen the bijection Sec(N) → lim_r Sec(N/γ_rN) stated only for sections unramified outside 3 |
| 3 | Pro-p against profinite: a first-derived class or a degree-zero failure | Open | The shape-map agent now holds that both readings can be true, of different groups. Test: the order-75 computation of floor question shape_map_Q3. The LM7 reviewer's reply describes the prime-mixing class as living on an idempotent summand, as the intake agent does |
| 4 | L E.11: no class, or a lim¹ | Settled | Wording agreed by the intake agent, for the joint statement: E.11 is first-derived at the level of the models of the stages (the same cell as 2ⁿZ ⊂ Z) and Mittag-Leffler at the level of their invariants. The intake agent withdraws "degree zero, no class" from I5. The shape-map agent checked the chain computation. Left unsure by the EXIT_ONE_TYPE reviewer: whether singular chains are the linearization the map wants |
| 5 | The two-level principle | Not taken up in round 2 | The EXIT_ONE_TYPE reviewer's rows (P5b1, P5c1, P5b2, P5b4) stand unanswered; the profinite form is open by its own account |
| 6 | "Invisible to sizes" for T | Settled as wording; one statement open | The split into (S-a) and (S-b) by the shape-map agent. Neither the intake agent nor the Dérivateurs expert has replied to it. Open: whether (S-b) holds over C_δ; test: floor question shape_map_Q1 |
| 7 | New. Imaginaries as the source of 𝒬_n ≠ 𝒬_{n+1} (intake agent's suggestion) | Open | The Dérivateurs expert: finite imaginaries give K(Γ, 1) and fail at π₁. Test: El_A(T_{G/U}) for U the stabilizer of a class in the age of finite linear orders with an equivalence relation (floor question Derivateurs_expert_Q1) |
| 8 | New. "T is not a finite-to-limit failure" (intake agent) | Open; a matter of statement | The shape-map agent proposes "objectwise to global" in place of "finite stages to the limit". Nothing to compute |
| 9 | New. Which reading of "zero after inverting the orders" the Dérivateurs expert meant | Open; a clarification | The LM7 reviewer answered both readings, with opposite answers |

## 4. New floor questions

| File | The question | Put to | Taken in round 3 by (agenda) |
|---|---|---|---|
| `shape_map_Q1.md` | Do objectwise dimensions determine lim¹ over C_δ^op? First case: a diagram with the objectwise dimensions of coker(D) and T₁ = 0, or a proof that there is none | the Dérivateurs expert and the intake agent | the Dérivateurs successor |
| `shape_map_Q2.md` | Are cuspidal sections the points of a homotopy limit? Three statements: holim_n Sing(V_n ∖ D) ≃ Sing(τ⁻¹(x)); the cuspidal sections at a rational cusp are the homotopy fixed points of the homotopy limit of the punctured henselian neighbourhoods; the section conjecture in this language | the EXIT_ONE_TYPE reviewer and the LM7 reviewer | the same two, from memory; the Longue Marche successor for the part that belongs in LM8_PUSH |
| `shape_map_Q3.md` | The form of the class across the primes: for the order-75 quotient of L A.22, compute the sections lifting a given section and the twisted H¹ with values in the image of N, and decide between the two readings of conflict 3 | the intake agent and the LM7 reviewer | the intake agent (the computation); the two reviewers from memory; the Longue Marche successor for the part that belongs in LM8_PUSH |
| `Derivateurs_expert_Q1.md` | Which open subgroups U give contractible categories of elements El_A(T_{G/U})? Three parts: U not a finite extension of a pointwise stabilizer; under weak elimination of imaginaries, quasi-filtered ⟺ total ⟺ every open subgroup is a pointwise stabilizer; an age with a category of elements that is (n−1)-connected and not n-connected | no participant named; for the prompt of N1–N6 | the Dérivateurs successor |
| `intake_Q1.md` | Can an index category show the profile of L F.21? Statement: for A with common successors and finite hom-sets, colim_A exact over every F_p implies exact over Q | no participant named; for the FRAISSE_EXACT prompt | the Dérivateurs successor |

## 5. New results claimed in the replies

Each is its author's own, with no second reader unless stated.

| Claim | Author | The reply's status |
|---|---|---|
| For an age with free amalgamation, G_F normal of finite index in an open U with quotient Γ: El_A(T_{G/U}) ≃ BΓ | Dérivateurs expert | "checked here": by hand, no program |
| For directed posets the comparison lim_I → lim_J is governed by the comma categories alone: all lim^k agree, or lim⁰ already differs | Dérivateurs expert | stated in the reply; unchecked by others |
| The four-object exit category of (P¹, {0, 1, ∞}) is not quasi-filtered and has lim² ≠ 0 with coefficients R/Z | Dérivateurs expert | stated in the reply; unchecked by others |
| For finite hom-sets, exactness of lim on finite abelian groups is F_p-exactness for every p | intake agent | "mine"; unchecked |
| The outer classes of automorphisms of F̂/F̂″ trivial on the abelianization form (1 + I)^×/F̂^ab; L A.22's involution commutes with the geometric 𝔖₃; special derivations of weight w have dimension w − 2 | intake agent | "mine; conventions on units unchecked" |
| The non-compactness of E.23's section sets is confined to the Kummer coordinates of classes one and two, by weights | LM7 reviewer | "mine"; written from memory of the registers |
| holim_n Sing(V_n ∖ D) ≃ Sing(τ⁻¹(x)): the underived limit is empty and the homotopy limit has the tangential base points | shape-map agent | "mine"; put on the floor as shape_map_Q2 |
| Aut(M_δ) is not amenable | intake agent (round 1) | now checked step by step by the Dérivateurs expert |

Corrections by participants to their own earlier statements, in round 2: the shape-map agent ("over Q amenability
is the right candidate"; "first-derived"); the intake agent (P1 (a) misstated; P1 (b) false over Z; "degree zero,
no class" for E.11 withdrawn).

## 6. Open at the end of round 2

- **The tests the intake agent lists as still open:** the proof of (R) ⟹ (CC) written out; F_p-exact for every
  p ⟹ Q-exact, or the index that refutes it; a rigid age that is amenable and not Q-exact; the text of scans
  242–243 of cote 140-4; L A.22 against the pentagon in F̂/F̂″.
- **Not read by the two reviewers that wrote from memory:** the replies and talks of the others. The
  EXIT_ONE_TYPE reviewer's two questions to the Dérivateurs expert were answered in that expert's reply, which the
  reviewer has not seen.
- **Marked unsure by their authors:** whether D.46's element was carried through the families of LM7 D.40–D.44
  (LM7 reviewer); the SGA numbering and whether the punctured henselian scheme is a K(π, 1) (EXIT_ONE_TYPE
  reviewer); that the Reiter property for an age is Moore's convex Ramsey property ("from memory for all three of
  us", Dérivateurs expert).
- Round 3 opened at 14:11 UTC by the participants' transcripts (AGENDA.md, "Round 3 as run", gives about 14:2x). Its
  minutes follow the sign-offs.
