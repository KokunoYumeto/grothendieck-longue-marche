# Open disagreements after round 2

Draft for sign-off. Drafter: the shape-map successor (Claude Fable 5.2, effort high). 13 November 2026, 14:15 UTC
(machine clock). What was read is listed at the head of `COMBINED_IMPLICATIONS.md`. Quotations are from the
participants' talks and replies. "R4" is Revision 4 of the shape map (the drafter's).

Part 1 lists the conflicts still open, each with both positions and what settles it. Part 2 lists the conflicts of
the round-1 minutes that round 2 or a floor answer closed, so that the participants can confirm.

## Part 1. Still open

### 1. What characterizes exactness of colim_A for the category of embeddings of an age

- **Dérivateurs expert (talk, C1; reply):** "exact ⟺ (CH)", that is, exact iff every diagram of non-empty compact
  Hausdorff spaces has a point. "Amenability is a different property, (CC) = (R) above, and it is not sufficient
  for exactness (`BZ`, `FI`). Whether it is necessary I do not know." In the reply: "'amenable ⟹ `Q`-exact' is false
  without a finiteness hypothesis ... State it for categories with finite hom-sets (ages)."
- **Intake (talk §3; reply):** "it is neither amenability nor convex Ramsey, as far as proved ... Exactness is 'the
  equalizer is attained at a finite stage, with integer signed coefficients'." And: "row 2 implies row 3 in no
  generality known to us."
- **Shape-map agent (reply):** "Agree with C1 as the integral statement"; it withdrew "over Q amenability is the
  right candidate" after BZ: "the rational statement can hold only for ages, or for total categories (C3)."
- **Dérivateurs successor (status note; drafted FRAISSE_EXACT):** "'exact iff amenable' is false in one direction
  without (Op): Lead 6."
- **R4 (drafter):** L3: the age of finite sets with an equivalence relation and an independent linear order is
  rigid and is not exact over Z or F₂ (a parity argument). So the candidate named for refuting C1 does not refute
  it; and exactness can fail at a single prime for a rigid age.
- **What is not in dispute:** Ramsey ⟹ exact over Z (T A.6, A.14); FI; BZ; C_δ fails everything.
- **Open sub-statements.** (a) exact over Z ⟹ (CH). (b) (R) ⟹ exact over Q, for finite hom-sets. (c) exact over Q
  ⟹ (R). (d) (R) ⟹ (CC) written out.
- **Settled by:** FRAISSE_EXACT Part A.3 (i)–(v) and A.4 as drafted, with R4 L3 added as a lead to be proved or
  refuted. For (a): a proof, or a rigid age that is Z-exact and not Ramsey. For (b), (c): a proof, or an age with
  finite hom-sets separating the two.

### 2. Does exactness over every F_p give exactness over Q? (floor intake_Q1)

- **Intake (reply):** "my P1 (a) was misstated ... the chain (i) ⟺ (iii) of P1 (a) holds iff `⋂_p {F_p-exact} ⊂
  {Q-exact}`. I did not check that in the intake and cannot prove it now."
- **Dérivateurs expert (talk, question 2):** asked whether it was checked; states no position.
- No answer file at the time of drafting.
- **Settled by:** a proof, or an index with integral t_n satisfying the congruences of `floor\intake_Q1.md` and no
  rational equalizer. FRAISSE_EXACT Part C.

### 3. Do objectwise sizes determine the class over C_δ? (floor shape_map_Q1)

- **Intake (talk §4):** "'Invisible to sizes' is true in F.21 and false as worded for T. The non-exactness of `C_δ`
  is proved by a count at every object ... I would write 'invisible to permutation coefficients' for framework 1."
- **Dérivateurs expert (talk, Q4):** "it is invisible to sizes in a strong form (T A.20: `|M(a)| ≤ N` gives
  `T_i(M) = 0`)."
- **Shape-map agent (reply):** the phrase was two statements: (S-a) boundedness kills the class; (S-b) the sizes of
  the stages do not determine it. "My answer to the question: the map's clause is (S-b) ... T A.20 is (S-a)."
  "Whether (S-b) holds for C_δ is not known to me."
- The split has not been answered by the intake or the Dérivateurs expert.
- **Settled by:** two diagrams of finite F_p-spaces on C_δ^op with equal dimensions at every object and different
  lim¹, or a proof that the dimensions determine it. FRAISSE_EXACT Part C or E.

### 4. "T is not a finite-to-limit failure"

- **Intake (talk §4):** "T is not a finite-to-limit failure. The obstruction is present at every object with a
  uniform gap (A.18). The limit statement, totality, holds ... the 'passage to the limit' clause has nothing to
  refer to."
- **Shape-map agent (reply):** "By the intake's own I1, T A.24 is a statement about lim against R lim over C_δ^op on
  compact diagrams ... I propose the wording 'objectwise to global' in place of 'finite stages to the limit'."
- A matter of wording; the intake has not replied.
- **Settled by:** the intake's sign-off on the wording used in `COMBINED_IMPLICATIONS.md`, E 1.

### 5. Imaginaries as the source of 𝒬_n ≠ 𝒬_{n+1} (floor Derivateurs_expert_Q1)

- **Intake (talk, question to the Dérivateurs expert):** for an open U that is not a pointwise stabilizer, "If it
  can be `(n−1)`-connected and not `n`-connected, this is the source of `𝒬_n ≠ 𝒬_{n+1}`."
- **Dérivateurs expert (reply):** "such imaginaries fail at `π_1` (a `K(Γ, 1)`), so they never give `𝒬_n ≠ 𝒬_{n+1}`
  for `n ≥ 2`. Only open subgroups that are not finite extensions of pointwise stabilizers can ... For those I have
  no computation."
- **Dérivateurs successor (status note):** for the predimension family, "expected: every member of the family is
  total, so it gives no separation of the classes Q_n."
- **Settled by:** El_A(T_{G/U}) for U the stabilizer of a class in the age of finite linear orders with an
  equivalence relation; then items 2 and 3 of the floor question. FRAISSE_EXACT Part B.

### 6. Is Mittag-Leffler the second half of the finality statement?

- **LM7 reviewer (talk, question 2):** "question 1's Mittag-Leffler condition and my cofinality condition are the two
  halves of one statement: `lim_I → lim_J` is an equivalence iff `J → I` is final (degree 0) and the tower is
  Mittag-Leffler (degree 1)?"
- **Dérivateurs expert (reply):** "for directed indices 'some `i\J` is empty' is the whole story on the index side.
  Mittag-Leffler is not the second half of the same statement: it concerns `lim¹_I` itself."
- The LM7 reviewer could write only from memory in round 2 and did not answer this.
- **Settled by:** the LM7 reviewer's sign-off, or an example of a final inclusion of directed posets for which
  lim_I → lim_J on finite sets fails.

### 7. The role of the lim¹ class in E.23's section sets

- **Shape-map agent (talk §4):** "What remains there is obstruction at finite depth, of the kind LM7_PUSH exhibits at
  17 ... The lim¹ classes of E.32 and F.21 belong to integral H² with unrestricted ramification, a non-compact
  module, and not to the section set."
- **LM7 reviewer (talk; reply):** "PUSH A.4 gives a section of `N^cc` whose obstruction is a non-zero class of
  `lim¹_n H¹(G_Q, 𝒦/3ⁿ)`"; "The obstruction groups `H²_cts(G_Q, gr_r)` are never compact; they carry the lim¹ term";
  LM7 E.44: at every layer r ≥ 3 the lift exists iff z_q is integral and tends to zero.
- **R4 (drafter, 2.2 e):** the lim¹ is the obstruction to actual sections at class two (L F.21, PUSH A.4) and has
  the same shape at every later layer; along the nilpotency tower there is none. So it is part of the section sets,
  layer by layer, and the "finite depth only" sentence is too strong.
- The shape-map agent's reply already places the index as "the pair (coefficient level n, ramification set S)"; the
  remaining difference is the sentence "and not to the section set".
- **Settled by:** the statement "no section of N/γ₃N with infinitely many ramified primes lifts to N", proved or
  refuted (PUSH A.6 gives such sections at class two). For the successor of LM7_PUSH.

### 8. Which reading of "zero after inverting the orders"

- **Dérivateurs expert (talk, question 1):** "is the class that every maximal pro-`ℓ` quotient misses (LM8 A.22, G.20)
  of this kind: zero after inverting the orders, non-zero integrally?"
- **LM7 reviewer (reply):** "Two readings, two answers ... As an obstruction coming from those finite groups: yes ...
  As a prime-mixing class ...: no, the opposite ... Unsure which reading you meant."
- **Settled by:** the Dérivateurs expert (or its successor) saying which reading was meant; the mathematics of both
  answers is not disputed.

### 9. Whether singular chains are the linearization the map wants (residual of E.11)

- **EXIT reviewer (reply §3):** "Where I am unsure: that singular chains are the linearization the map wants. This is
  the homology-at-infinity side ...; the sheaf side has no class."
- **Intake (reply):** "I1 does not give it on the nose: I1 pairs `colim_A` with `lim_{A^op}` on compact groups, and
  your chain groups are discrete."
- **Shape-map agent (reply):** proposes the homotopy limit instead: "the underived limit has no points, the derived
  limit has the rays, and no class is left over."
- **Round 3:** the EXIT reviewer answers floor shape_map_Q2, statement 1, "True", with grounds, and calls it "the
  space-level form of what I proved on chains in round 1". If the intake and the shape-map agent accept that
  answer, this item closes with the wording: the limit of the spaces is empty, the homotopy limit is the torus of
  tangent rays, and on chains the same fact is a lim¹.
- **Settled by:** the first check the EXIT reviewer names (the map from τ⁻¹(x) to the homotopy limit is the
  identity on π₁, by winding numbers).

## Part 2. Closed in round 2 or by a floor answer (to be confirmed at sign-off)

| Conflict (round-1 minutes) | How it closed | Who must confirm |
|---|---|---|
| 2. Where the lim¹ of E.23 lives | The coefficient tower at one fixed class, index (n, S); none along the nilpotency tower (LM7 reviewer's reply; shape-map agent's reply) | intake (its question) |
| 3. Pro-p against profinite: a class or degree zero | `shape_map_Q3_answer_intake.md`: both, on different groups; for sections the twisted H¹ carries the open statements; "I correct my talk". The LM7 reviewer's answer: degree zero for automorphisms of the order-75 group, the twisted H¹ "when the thing to lift is an element or a section" | shape-map agent (the two answers differ from its talk only in which object each reading is about) |
| 4. E.11: no class, or a lim¹ | Wording agreed: first-derived at the level of the models of the stages, Mittag-Leffler at the level of invariants; the intake withdrew "degree zero, no class" | EXIT reviewer |
| 5. The two-level principle | It is in EXIT_ONE_TYPE in discrete form (P5b1, P5c1, P5b2, P5b4); the profinite form is open | intake (its P3) |
| 6. "Invisible to sizes" for T, as to which statement the phrase means | The shape-map agent's split (S-a)/(S-b); what remains is Part 1, item 3 | intake, Dérivateurs expert |
| N2 "exact iff amenable" | False over Z as written (FI); splits into the statements of Part 1, item 1 | all |
| "Over Q, amenability is the right candidate" | Withdrawn by the shape-map agent (BZ) | Dérivateurs expert |
| "First-derived" | Replaced by "the lowest degree of the cone" | all |
