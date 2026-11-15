# Intake of the final return of ANABELIAN_149_PUSH (14 November 2026)

By Claude Fable 5.2 at effort high (effort set at launch; sub-agent of the main session, Claude Opus 5.5 at effort
max), 14 November 2026, 16:13–16:35 UTC (clock read at 16:19 and 16:22). Brief:
`BRIEF_INTAKE_ANABELIAN_FINAL_20261114.md` in this folder.

The return is by GPT-6 Astra (ChatGPT Pro mode); everything it states is that model's claim. **(mine)** marks my
remarks. Its code was read nowhere and run nowhere. Folder of the return:
`longue_marche_pro_pilot_20261104\answers\ANABELIAN_149_PUSH_final_20261114T1558Z_unzipped\ANABELIAN_149_PUSH\`
(below: `R\`). Register: 221 rows, 188 proved, 15 known, 11 refuted, 7 unresolved (A.30, A.C2.6, D.U1–D.U4, F.9).

Verdict words: **sound** = I followed the proof and found no error; **statement level** = I read the register row
(statement, dependencies, notes) and judge only that it is well formed and agrees with its neighbours; **certificate**
= the row rests on a program output that nobody on our side has reproduced.

## 0. Headline

1. **New and sound, as far as I followed:** A.C2.20 with A.C2.19, A.C2.7, A.C2.8, A.C2.5. A curve `C` of genus ≥ 2
   over a field finitely generated over `F_p` satisfies A1 as soon as it has, geometrically, a connected cyclic étale
   cover of odd degree `n` prime to `p` whose primitive (conductor-`n`) Jacobian factor has `p`-rank zero. I followed
   the whole chain of these five proofs and found no error. It turns A1 into one existence question about covers.
2. **New, resting on certificates:** A.C2.26, A1 for every genus-two curve over `F_4` (all 64 geometric classes), and
   so for every curve over a field finitely generated over `F_2` in one of those classes. Unreproduced.
3. **A1 itself is not decided**, and neither are D1–D4 and the classification F.9. No row changed status in the last
   two checkpoints.
4. **The stop was the three-hour rule working as meant** (section 2).
5. **Nothing found wrong** in the 25 rows. Nothing I would call doubtful; the strong claims that need a referee
   before use are F.45 (reconstruction over `Q̄(t)`), D.30 (it applies a modularity theorem I did not open), and the
   certificates of A.C2.25–A.C2.26.

## 1. Verdicts on the 25 rows without an intake

### 1.1 Part A (scans 35–36; item A1). Fourteen rows

The mechanism, which the rows share. In characteristic `p`, a collision (`P ≠ Q` with conjugate sections in the
geometrically prime-to-`p` group) gives, on every prime-to-`p` Galois cover `D → C` and after a finite extension, lifts
`P′, Q′` with `T = [Q′ − P′]` a `p`-primary torsion point of `J_D` (A.3, which is R4 (d) of the prompt). A.C2.7: `T`
has trivial stabilizer in the deck group `G`, because `δT = T` gives `δQ′ + P′ ~ Q′ + δP′`, two distinct effective
divisors of degree two, and `D` is not hyperelliptic (an odd-order automorphism of `P¹` has a fixed point; the deck
action is free). So an element of `G` that acts trivially on the `p`-primary torsion excludes the collision. For a
cyclic cover of genus two in characteristic two, A.C2.5 computes which characters carry 2-rank: with `B` the bundle of
locally exact differentials and `Θ = {L : H⁰(B ⊗ L) ≠ 0}` (Raynaud's theta divisor, here a curve in `J_C`),
Frobenius maps `H¹(C, Lⁱ) → H¹(C, L²ⁱ)` and is zero exactly when `Lⁱ ∈ Θ`; so the characters in a doubling orbit
carry 2-rank exactly when the orbit misses `Θ`.

| Row | What it states | Verdict | What I read |
|---|---|---|---|
| A.C2.19 | Genus two, characteristic two, any odd `n`: A1 holds if every doubling orbit on `(Z/n)^×` meets `{i : Lⁱ ∈ Θ}` for a line bundle `L` of exact order `n`. Characters of smaller conductor may survive. | **Sound (mine).** | `R\sections\A_arbitrary_primitive_prym.tex`, lines 1–187, in full; `A_char2_theta.tex` lines 3–129 (A.C2.5); `A_char2_deck.tex` lines 3–135 (A.C2.7, A.C2.8). |
| A.C2.20 | Every `p`, every genus ≥ 2: A1 holds if there is a connected cyclic étale cover of odd degree `n` prime to `p` whose primitive factor `P_n = im ∏_{ℓ∣n}(1 − σ^{n/ℓ})` has `p`-rank zero. | **Sound (mine)**, given A.3 and, for odd `p`, A.29l (statement read, proof not). | `R\sections\A_general_primitive_prym.tex`, lines 1–212, in full. |
| A.C2.17 | The same for `n = ℓᵃmᵇ` (two primes); every theta point of exact odd order `n` with `⟨2, −1⟩ = (Z/n)^×` suffices. | Statement level; contained in A.C2.19, whose proof I followed. | Register row. |
| A.C2.23 | A primitive `p`-rank-zero cyclic stage inside an abelian total cover of `C` descends to a cyclic cover of `C` with the same property. So abelian towers add nothing to the criterion. | Statement level; plausible (a faithful character of the stage extends to the abelian group). | Register row. |
| A.C2.21 | A cyclic subgroup of order `n` meets `Θ` in a set `S` with `|S|(|S| − 1) ≤ 2(n − 1)`; conductors 127 and 257 can never give primitive rank zero. | Statement level; the counting step is right **(mine)**: a non-zero class `P − Q` on a genus-two curve has at most two such representations. | Register row. |
| A.C2.14 | For every finite set `S` of odd primes there is an ordinary genus-two curve in characteristic two whose `Θ` has no `S`-supported torsion; all its `S`-abelian covers are ordinary with faithful deck action. A limit of the method, not a counterexample. | Statement level. Long proof (smoothing, level structures, a Lang–Weil twist), unread. Needs a referee if the successor prompt leans on it. | Register row. |
| A.C2.13, A.C2.15, A.C2.16, A.C2.18 | Explicit curves and two-parameter families with theta points of exact order 7, 5, 15; A1 for them. | Statement level; **certificate**. Superseded in weight by A.C2.19/20 and A.C2.26. | Register rows. |
| A.C2.22 | A1 for 46 of the 48 ordinary geometric classes of genus two over `F_4`, by norm identities with annihilators 3, …, 49. | **Certificate.** | Register row. |
| A.C2.24 | The two remaining classes ("203/302"): Jacobian simple with CM field `Q(√2, √(−7+4√2))`; many primary theta packets empty; the 73-primary packet is `{±1, ±27}`. | **Certificate**; now only a record of why small conductors fail. | Register row. |
| A.C2.25 | Those two classes have a cyclic cover of degree `2454499369 = 7·31·2503·4519` with primitive 2-rank zero (1296 doubling orbits, each with an explicit theta point over `F_{2^18}`). All 48 ordinary classes done. | **Certificate**; the theorem it feeds (A.C2.19) is sound. | Register row; report lines 563–626. |
| A.C2.26 | The twelve classes of 2-rank one have annihilators 5, 7, 11, 13, 19, 39; with rank zero (no 2-torsion, A.1) this gives A1 for every genus-two curve over `F_4`. | **Certificate.** The count 64 = 48 + 12 + 4 is right **(mine)**. | Register row. |

What I checked in A.C2.20 **(mine)**, since everything hangs on it:
- `A·T` is `p`-primary torsion in `P_n`, hence zero; so `Σ_S (−1)^{|S|}(a_S P′ − a_S Q′)` is the divisor of a function
  `f` of degree `d = 2^{ω(n)}` with simple zeros and poles in two free deck orbits.
- The field `M` generated by the deck translates of `f` has `[K̄(D) : M] = e` dividing `d` and genus at most
  `(d/e − 1)²` (induction with Castelnuovo–Severi; I redid the algebra: the bound loses `as(a − 1)(s − 1) ≥ 0`).
  `n > (d − 1)²` for every odd `n > 1`, so `e > 1`.
- `G` acts faithfully and freely on the curve `Z` of `M` (orders coprime to `e`), so `g(Z) = 1`; a zero fibre of
  `D → Z` is reduced and meets each orbit at most once, so `e = 2`.
- So `C` is a ramified double cover of a genus-one curve `E₀`. For odd `p` that is a case already settled (A.29l,
  A.25). For `p = 2`: the Deuring–Shafarevich formula on the cartesian squares `D_m → Z_m` over `C → E₀` gives
  `f(D_m) = m r₁ + 2ε − 1`, and Möbius inversion gives `f(P_n) = r₁ φ(n) > 0`, against the hypothesis.
  The citations to open: Poonen 2007 (Lemma 2.2, Corollary 2.3), Crew 1984 (Corollary 1.8).

**Novelty (not checked against the literature by me).** The run searched and found no source for the criterion or for
the `F_4` theorem and claims no priority. Its own literature audit (report lines 609–620) says what the known
existence theorems give: Raynaud's and Pop–Saïdi's covers are non-ordinary in the new part, which is weaker than
`p`-rank zero of a whole primitive block; Hoshi 2022 and Ozman–Pries 2019 likewise. I did not open Saïdi–Tamagawa to
see whether they ask if their exceptional set is empty.

### 1.2 Part D (scans 56, 59–63, 126–127; items D1–D4). Four rows

| Row | What it states | Verdict | What I read |
|---|---|---|---|
| D.30 | For a continuous non-cuspidal section `s` of the tripod over `Q`, the pull-back `ρ_{s,ℓ}` of the Legendre Tate module is absolutely irreducible. Finite ramification of one `ρ_{s,ℓ}`, `ℓ ≥ 5`, is equivalent to: the local sections are integral points at almost all places; and then the system `(ρ_{s,ℓ})_ℓ` is the Tate module of an elliptic curve over `Q`. | **Sound as far as followed (mine)**; conditional by its own statement. It rests on D.6 (local sections are points or cusps: the run's audit of the unrefereed OpenAI paper of 6 October 2026), on D.25 (integral local points at a set of primes of density one; unread) and on Pan 2022, Theorem 1.0.4 (not opened by me). | `R\sections\D_legendre_modularity_extension.tex`, lines 1–327, in full. |
| D.31 | Under almost-everywhere integrality: if a non-constant unit is regular and non-zero at every cusp that occurs as a local centre, `s` is a rational point. For the tripod, at most one cusp label suffices. | **Sound (mine)**, given D.3 (the prompt's R23) and Stix's Corollary 5 as the run uses it. | `R\sections\D_finite_cusp_extension.tex`, lines 1–159, in full. |
| D.32 | The level-`N` neighbourhoods of a tripod section with full `GL₂(Z/N)` image have three rational cusp orbits and unit rank two, so they never supply the unit D.31 needs; `λ = 3` gives an infinite 5-power tower of this kind. | Statement level. It closes a route; it claims nothing about sections. | Register row. |
| D.29 | A family of local points whose values at `t − 2` fail the restricted-product condition of D.27 although every character-wise reciprocity sum vanishes. The tuple is not claimed to come from a section. | Statement level. A counterexample to a proposed implication. | Register row. |

The argument of D.30 that I followed **(mine)**: an invariant line would give characters `η` and `η⁻¹χ_ℓ` with `η` of
finite order (Hodge–Tate characters of `G_Q`); at a positive density of primes of D.25 the trace of Frobenius would
be `1 + v`, against the Weil bound for the good elliptic curve `E_{x_v}`. Under finite ramification, modularity gives
weight-one purity everywhere outside a finite set, which excludes non-integral ordinary points (`j` has a pole) and
cuspidal places (trace `±(v + 1)`). The idea of feeding a point that survives descent into modularity is in
Helm–Voloch 2011, which the run cites; D.30 is its form for sections of the tripod.

What D1 now needs, in the run's words and mine: (1) finite ramification of one `ρ_{s,ℓ}`; (2) the case where cusps
with two different labels occur at finitely many places. Neither is proved.

### 1.3 Part F (scan 52; item F2). Seven rows

All seven use the corrected convention: a pinned morphism of étale topoi preserves closed points (Carlson–Haine–Wolf
2024, Definition 2.19). Report lines 1613–1621: the prompt's R27 summarised "pinned" as "given with its commutation
isomorphism", and with that literal reading no field of characteristic 0 reconstructs (F.1, F.17, earlier
checkpoints). The error was in our prompt's wording, not in LM5-F.50.

| Row | What it states | Verdict | What I read |
|---|---|---|---|
| F.45 | Reconstruction of all finite-type schemes from their étale topoi holds over every finitely generated extension `L` of `Q̄` of positive transcendence degree, and over every subfield of `L` of positive transcendence degree over `Q`. `Q̄(t)` reconstructs; `Q̄` does not. | First half **sound (mine)**; second half unread. A strong claim: **referee before use**. | `R\sections\F_algebraic_constants_extension.tex`, lines 1–330 of 482; report lines 1781–1793. |
| F.47 | `Frac(F[t]^h_{(t)})` and all its algebraic extensions fail, for every `F` of characteristic 0: `t ↦ t + t²` lifts to an automorphism that centralizes the whole Galois group `Ẑ(1) ⋊ G_F`. So a field of finite transcendence degree with a henselian valuation of residue characteristic 0 and residue transcendence degree one less fails. | Statement level; the mechanism is right **(mine)**: `1 + t` has all roots in a henselian field, so the substitution preserves every `t^{1/n}`-extension compatibly. | Register row; report lines 2124–2130. |
| F.48 | The same for value groups of any finite rational rank under the Abhyankar equality. | Statement level. | Register row. |
| F.43 | Reconstruction over every subfield of a finitely generated extension of `K^solv`, `K` finitely generated over `Q`. | Statement level; a chain on F.24–F.37 of earlier checkpoints. | Register row. |
| F.44 | The same with "solvable" replaced by any proper class of finite groups closed under subgroups, quotients and extensions and containing the cyclic groups; an increasing union of reconstructing fields (`⋃ Q^{D_m} = Q̄`) does not reconstruct. | Statement level. | Register row. |
| F.46 | F.44 and F.45 combined over `K₀/Q̄` of positive transcendence degree. | Statement level. | Register row. |
| F.49 | Reconstruction over finitely generated extensions of a Hilbertian Galois extension `k/D` containing `Q̄`, `D` finitely generated of positive transcendence degree; smallness of `Gal(k/DQ̄)` suffices. | Statement level. | Register row. |

The step of F.45 I followed **(mine)**: a Kummer class on a punctured line with actual values at all points is
`κ(b₀) + Σ λ_j [P_j]` with `λ_j ∈ Ẑ`; evaluating at a point `α` and at its conjugate `σα` and applying a geometric
valuation `v_i` with `v_i(P_j(α)) = δ_{ij}`, `v_i(P_j(σα)) = 0`, which stays integer-valued on `MQ̄` because constant
extensions are unramified at it, gives `λ_i = −v_i(σb_α / b_α) ∈ Z`. That replaces the number-field valuations of
the earlier proofs. Consistency checks **(mine)**: `G_{Q̄(t)}` is free, hence slim (F.39 is not violated); `F[t]^h`
does not embed in a function field over `Q̄` (it contains all roots of `1 + t`), so F.45 and F.47 do not collide.

F.9 stays unresolved: sufficient classes (F.37, F.43–F.46, F.49) on one side, necessary conditions (F.39–F.41,
F.47–F.48) on the other, and F.42 shows that no criterion in the Galois group with its cyclotomic character exists.

## 2. The stop

**Verdict (mine): the INCOMPLETE marking is the three-hour rule working as meant.** The run stopped at its eleventh
hourly check because the work that would come next no longer moved an open item, not because of what the hour before
had produced.

The run's lines (`R\ANABELIAN_149_PUSH_report.md`):
- lines 2070–2075: "we made the next hourly assessment … **Decision: stop further research and complete the final
  INCOMPLETE package under the user's progress rule in request.md.** Source integration, compilation, visual
  verification and archival checks continue to completion; they are delivery work and are not being counted as
  further mathematical progress."
- lines 2093–2105: "The assessment concerns the **current next mathematical work**, rather than treating the
  preceding hour's accomplishments as an automatic reason for another hour. The finite-field and degeneration agents
  both report that their universal routes have stalled. The exact A1 gap is existence of an odd cyclic theta subgroup
  meeting every primitive doubling orbit. … Repeating bounded censuses would add examples without supplying the
  missing universal implication."
- lines 2107–2113, for D1–D4: "the section-derived compatible system still lacks a uniform residual-conductor bound
  on infinitely many coefficient primes, or another proof of finite ramification. … No new
  noncongruence-neighbourhood existence theorem or puncture/birational lift has been established."
- lines 2115–2122, for F.9: "Continuing only to enlarge examples or restate the CHW geometric test would not
  complete that requested determination."
- lines 2132–2136: "Seven numbered obligations remain Unresolved. No unresolved item is relabelled as a theorem".

What supports the verdict **(mine)**:
- Was it moving A1 when it stopped? The last hour gave A.C2.25 and A.C2.26: the last 14 of the 64 classes over
  `F_4`. That is the main question, but a census; the general step (A.C2.19, A.C2.20) came in the ninth hour. The
  run's diagnosis of what a universal proof needs (report lines 563–626) is exact: the Weil-type bound controls
  theta points in additive cosets (error under 988 against 9363 expected, in its own example) and is useless for a
  single doubling orbit (6 expected, error bound 1.28 million).
- No item changed state after checkpoint 08 (which closed C4): 7 unresolved rows at checkpoints 08, 10 and the
  final, while the proved rows went 163 → 183 → 188.
- The seven earlier checks each said "continue" with a named advance on an open item (Part B done at hour 4, Part C
  at hour 7, Part E at hour 8, the criterion at hour 9). The rule was applied each hour, not once.
- One could argue for a stop an hour earlier (hour 10 was census and sufficient classes). That is a matter of an
  hour, and hour 10 found the conductor that closed `F_4`.
- The run left routes named and untried: a new estimate for theta points on multiplicative orbits, and a cover with
  non-abelian total group in which a whole stable block disappears. Under the prompt's push rule alone it should have
  gone on; the three-hour paragraph says that the check takes precedence, and the run cites it.

## 3. What it means

### 3.1 For Grothendieck's text (cote 149)

- **Scans 35–36** (his p. 17; `MPL_149_001-090_transcription.tex`, lines 504–523). His "Il est cependant possible
  que l'injectivité de (*) reste valable sans hyp. de caractéristique" is still undecided in general. Proved in the
  return: every hyperelliptic curve in odd characteristic (A.19), so all of genus two outside characteristic two;
  every prime-to-`p` Galois cover of a curve of genus one (A.29l) and the solvable ones of genus zero; every
  genus-two curve over `F_4`. His sentence "Il se pourrait qu'on puisse en déduire `P = Q`" is the same question:
  A.3 proves his covering condition equivalent to equality of the sections, so A2 has no content beyond A1.
- What the return adds to his sentence **(mine)**: he observes that `Q′ − P′` is `p`-torsion on every cover. The new
  fact is that this class has a free orbit under the deck group (A.C2.7), so a collision forces the deck group of
  every prime-to-`p` Galois cover to act faithfully on the `p`-torsion of its Jacobian, with
  `f(D) − f(C) ≥ m_p(G)`. A companion note on scan 36 should say this: it is the deduction he was looking for, made
  as far as "one cover with a `p`-rank-zero primitive part".
- **Scan 52** (his p. 25 verso; lines 705–709). He asks whether `X ↦ X_ét` is faithful and "peut-être pleinement
  fidèle" after inverting universal homeomorphisms, with the margin "`S` de car. 0 ?". The return's answer: over a
  field it depends on the field and on the closed-point condition. It holds over the classes of F.37, F.43–F.46,
  F.49 (among them `Q^solv`, `Q̄(t)`); it fails over `Q̄`, real closed fields, Laurent series fields and the
  henselian fields of F.47–F.48. Nothing is said over a general noetherian base.
- **Scans 56, 59–63, 126–127** (Conjectures A, B, B′, and a), b) of §4): D1–D4 undecided; D.30–D.32 are conditional
  reductions for the tripod. (B′ for abstract actions was refuted in an earlier checkpoint, D.14.)
- **Scans 99–104**: no new row; Parts B and C were complete before.

### 3.2 For the Longue Marche runs and our open items

- **LM6_POINTS_AS_SECTIONS (running).** Its intake must be read against D.25–D.32 and C.7h: the same sections of the
  tripod over `Q`. If LM6 proves or uses finite ramification of `ρ_{s,ℓ}`, D.30–D.31 finish the case of one cusp
  label; if LM6 has a section with infinitely many non-integral local points, D.30 says its Legendre representation
  is infinitely ramified and absolutely irreducible.
- **The E.65 chain (LM7_PUSH D.50, E.58, E.65; the CM parity character on `GT̂₀`).** No row of the final changes it.
  One link **(mine, a lead)**: D.30 and D.32 work with the monodromy of the Legendre family along a section; the
  frames of the E.65 chain are path cocycles to its two CM fibres. For a section `s` of the tripod the same two
  parities are defined on `ρ_{s,ℓ}`; whether they agree for every section, Galois or not, is a test of the kind the
  expert asked for. Not posed by the run.
- **LM8_PUSH Part A (LM8 G.20), LM7, LM8.** Nothing new beyond section 14 (C.7h). D.32's tower at the prime 5
  concerns the Legendre family, not the curve `y² = x³ − x` of G.20.
- **Boggi-A5 and Poincaré.** No row of the final bears on it. E.13–E.14 (section 14) remain the only contact.
- **LM5 (scan 52 of cote 149, its Part F).** Every place where we cite LM5-F.50 must use the closed-point
  definition; F.37 and F.43–F.49 now contain and extend it; LM5-F.44's question over `Q^solv` is answered (F.23, F.31,
  earlier checkpoints).

### 3.3 Implications the run did not draw (mine, unchecked)

1. **A1 in genus two is now a question in characteristic two only.** A.19 covers every hyperelliptic curve in odd
   characteristic. The run says so only inside A.30's notes. The smallest undecided instances are genus-two curves
   over `F_8` and `F_16`, and in odd characteristic non-hyperelliptic curves of genus three that are not prime-to-`p`
   Galois covers of a curve of genus ≤ 1.
2. **The existence statement is an Artin-type heuristic, and the heuristic says yes.** In a cyclic subgroup of order
   `n` of `J(F_Q)` the expected number of theta points in a doubling orbit is about `s/Q`, `s = ord_n(2)`. When 2
   has large order modulo `n` the orbits are few and each should be met. In the run's own example the expectation
   is 6 per orbit for 1296 orbits, so a miss was not excluded in advance; for larger fields the margin grows. A
   proof needs equidistribution of discrete logarithms of points of a curve, which Weil bounds do not give.
3. **A cheaper sufficient target.** By A.C2.5 (C2.17) one theta point of exact prime order `ℓ` with
   `⟨2, −1⟩ = F_ℓ^×` suffices. By A.C2.12 each prime contributes finitely many theta points, and by A.C2.14 no
   finite set of primes works for all curves; so the statement to aim at is: for each curve, infinitely many primes
   `ℓ` have a theta point of exact order `ℓ^a`. Then Artin's conjecture on average over those `ℓ` would finish.
4. **The criterion wants a non-abelian form.** The proof of A.C2.20 uses only an element of `Z[G]` that kills the
   `p`-primary torsion and whose support gives a divisor in two free orbits. For a non-abelian `G` an isotypic block
   of `p`-rank zero gives such an element; the controlled-field step then needs the block's support to be small.
   Raynaud's and Tamagawa's theorems produce non-ordinary blocks in solvable covers; whether a whole block can be
   made to vanish there is the open point the run names (`R\audit\A_nonabelian_Raynaud_gap.md`, not opened by me).
5. **F.9 has a natural candidate the run does not test:** the necessary condition of F.39–F.40 (for every finite
   `E/k`, no non-trivial automorphism of `k̄` centralizes `G_E`) separates `Q` from the field of F.42 and holds in
   every proved positive class. Is it sufficient? The fields to test are those with a henselian valuation with
   transcendence defect, which the run names as the barrier.

## 4. Before anything builds on it: for a referee (Claude Opus 5.5 at effort max)

In this order.
1. **A.C2.20 and its chain**: A.3 (already followed in the FLAGGED_149 intake as R4 (d)), A.C2.5, A.C2.7, A.C2.19,
   A.C2.20, and A.29l (`R\sections\A.tex` from line 4866; unread by any intake). Open Poonen 2007 and Crew 1984 at
   the cited places. This is the result most likely to be published and the base of the successor prompt.
2. **A.C2.25 and A.C2.26**: reproduce the certificates with our own program (theirs is read, not run): the theta
   generator of order `M` over `F_{2^18}` and the 1296 orbits for the classes 203/302; the seven norm identities for
   the rank-one classes; the Raynaud origin `B = W₁ + W₂ − W_∞`. Hashes are in the register rows.
3. **D.30 and D.31**: open Pan 2022 (Theorem 1.0.4 with Conjecture 1.0.1: regular weights, `ℓ ≥ 5`, no residual
   hypothesis), Stix 2015 Corollary 5, and D.25; state plainly that D.6 rests on the unrefereed paper of 6 October.
4. **F.45** (lines 330–482 unread), then F.43, F.44, F.46, F.49 as one chain on F.24–F.37; F.47–F.48; and F.1/F.17,
   because they change how LM5-F.50 is cited.
5. **Still open from section 14**: E.14 and E.13 (HMT 2025 not opened by anyone), C.7h and C.7u, F.42.
6. A.C2.14 if the successor prompt uses it to exclude fixed-prime strategies.

Not done by me: the PDF check (365 pages; the two PDFs differ in byte size, not compared), any source opening, any
computation.

## 5. Next prompts: proposals (no prompt edited; for the field expert to weigh)

### (a) A successor for what is unresolved

Working name ANABELIAN_149_PUSH_2. Main question first, with most of the time.

- **A1.** Prove or refute A1. State as settled material: A.3, A.C2.7, A.C2.19, A.C2.20, A.19, A.29l, A.29m,
  A.C2.26 (each to be confirmed where used). Routes, as routes:
  1. the existence statement `E(C)`: every curve of genus ≥ 2 over `F̄_p` has a cyclic étale cover of odd degree
     prime to `p` with primitive part of `p`-rank zero; in genus two and characteristic two, a cyclic subgroup of
     `J` in which `Θ` meets every primitive doubling orbit (report lines 563–626);
  2. the prime-order target of 3.3 (3);
  3. the non-abelian form of the criterion and block vanishing in solvable covers (3.3 (4));
  4. higher genus: the same analysis with Raynaud's `Θ_B` where the character spaces are no longer lines;
  5. the smallest instances of 3.3 (1), computed, as test cases, never as the item.
  The prompt must say that a census over a further finite field does not move the item.
- **D1.** Two exact statements to prove or refute: (i) for a non-cuspidal section of the tripod over `Q`, one
  `ρ_{s,ℓ}` with `ℓ ≥ 5` is ramified at finitely many primes (equivalently, almost all local points are integral);
  (ii) under (i), cusps with two different labels cannot both occur. With D.30–D.31 they give D1. Then D2–D4 as in
  the first prompt, starting from D.23 (central lifts exist) and D.27–D.29.
- **F2 / F.9.** Prove or refute that the condition of F.39–F.40 is sufficient; decide the fields with a henselian
  valuation with transcendence defect; restate with F.42 that the criterion cannot be in Galois data alone.
- **Drop**: A2 as a separate item (A.3); Parts B, C, E (complete, pending referee); D5 (settled).

Background files: this return's `sections\` for Parts A, D, F with the report passages named above and the
register; the first prompt's zip for the literature it already has; added in LaTeX where a source exists: Raynaud
(the theta divisor of `B`; the 2002 paper on solvable covers), Tamagawa 2003 and Pop–Saïdi 2003 on tame fundamental
groups, Ozman–Pries 2019, Hoshi 2022, Achter–Casalaina-Martin 2024, Katz's estimate (Proposition 9.1.3 as cited),
Poonen 2007, Crew 1984, Pan 2022, Helm–Voloch 2011, Harari–Voloch 2010, Stix 2015, Carlson–Haine–Wolf 2024,
Bary-Soroker–Paran 2013. Bibliographic data are the run's; I verified none.

How it starts from this return: the prompt quotes A.C2.20 and `E(C)` in full, names the two D gaps and the F
candidate, and forbids re-proving the 214 settled rows.

### (b) New results into the background of unsent prompts

- **LM6_POINTS_AS_SECTIONS** (`longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM6_POINTS_AS_SECTIONS`):
  running, so nothing goes in; for its intake and any successor: D.25–D.32, C.7h, and for sections over finite
  fields A.3, A.C2.7, A.C2.20, A.C2.26.
- **A successor of LM5** (Part F, scan 52), when written: F.1 and F.17 (the definition), F.7, F.37, F.42,
  F.43–F.49, and F.9 as the open item. The R27 wording must not be reused.
- **LM8_PUSH** and **EXIT_TOWER** (unsent): nothing from the 25 new rows; the proposals of section 14.3 stand (C.7h
  for LM8_PUSH Part A; E.13–E.14 for EXIT_TOWER Part E and LM8_PUSH C.8).
- **The companion to cote 149**: the notes of 3.1 on scans 35–36 and 52.

## 6. What I read and what I did not

**Read in full (part 1):** the prompt as sent (`PROMPT.md`, 84 KB); the Longue Marche expert's
`KNOWLEDGE_HANDOFF.md`; both transcription files of cote 149 (scans 1–136; the first-pass files named in the brief,
so the second-pass corrections quoted in the prompt are not in the text I read); section 14 of `INTAKE_20261114.md`.
Not opened: the `*_notes.md` and `*_doubts.md` files, the background zip, any scan image, any paper.

**Read (part 2):** both DIFF files; the register rows of the 25 new statements and of the 7 unresolved ones, in
full, and an index of all 221 (first 160 characters each); the report's item table, lines 563–626, 911–915,
1611–1634, 1781–1793, 1849–1853, 2048–2136; in `sections\`: `A_char2_theta.tex` (all), `A_char2_deck.tex` lines
1–135, `A_arbitrary_primitive_prym.tex` (all), `A_general_primitive_prym.tex` (all),
`D_legendre_modularity_extension.tex` (all), `D_finite_cusp_extension.tex` (all),
`F_algebraic_constants_extension.tex` lines 1–330; the statement of A.29l. The opening of `EXPERT_ON_BOGGI_A5.md`
and of `EXPERT_IMPLICATIONS_E65_LM.md` (about 3 KB each).

**Not read:** the proofs of A.C2.13–A.C2.18, A.C2.21–A.C2.26, D.29, D.32, F.43, F.44, F.46–F.49 and the second half
of F.45; A.29l's proof and D.25; `audit\`, `code\`, `history\`, `sources\`, the bibliography, the PDFs; the nested
checkpoint folders. Context when the reading stopped: about 380k tokens (the coordinator's reading at 16:22 UTC).
