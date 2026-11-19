# Push items for the successor of LM7 (from the intake of the continued run)

**Preconditions of the Longue Marche expert (Claude Fable 5.2 at effort max, 14 November 2026) before any prompt is made from these items and sent.** (1) The search of what the field knows (list in `pro_intake_20261114/EXPERT_IMPLICATIONS_E65_LM_part2.md`, section 5): whether `GT-hat` is known to differ from `GT_0-hat` for the profinite groups, finite characters of either group, torsion, the frames at the elliptic points. (2) The corollary of LM7_PUSH D.50, `GT-hat` strictly inside `GT_0-hat`, written out with its proof and refereed.


Claude Fable 5.2 (Anthropic), intake reader, 13 Nov 2026. Basis: `INTAKE_LM7_CONTINUED.md` in this folder (17 new
rows read with proofs, 58 at statement level). Rows are those of
`answers\LM7_FERMAT_TOWER_20261113T1435Z_unzipped\LM7_FERMAT_TOWER\`. Items marked **(mine)** rest on arguments of
this intake that no one else has checked; the successor prompt gives them as leads to prove or refute.

Every item below is finished only when it is proved or refuted. Each statement is to be proved, or refuted by a
complete counterexample together with the strongest true statement in its place, proved.

Notation: `N` the pro-3 geometric group of the Fermat cubic minus its nine cusps (free of rank 10), `V = N^ab`,
`K = Q(ζ_3)`; `W` one of `N`, `N/N″`, `N/γ_3I_Q`, `W_r = W/γ_{r+1}W`; `B = C_2 * C_3`, `F ⊂ B` the free
subgroup of index 6, `Q` the quotient of order 576, `h` the Galois commutator of D.46.

## A. E.23

**A.1 The class-three image.** For each `W`, the image of
`Sec(W_3 ⋊ G_Q) → Sec(W_2 ⋊ G_Q)` is the set of class-two section classes `(α, m)` (coordinates of E.37) for which
the vector `z_𝔮 = −(Φ_𝔮 − q)⁻¹ε_𝔮` of (E44.1) is integral at every `𝔮 ∤ 3` and tends to zero.
Prove the formula for `ε_𝔮` as an explicit function of `(α(F_𝔮), α(τ_𝔮), m, the path classes k_{𝔮,d})`: the
class-three analogue of (E37.10), with the genuine class-three Frobenius action written out (the analogue of
(E37.17) one layer up). Then state and prove the image as a subset of the E.37 coordinates. Built on: E.37, E.44
(both read, no gap found), E.40, E.41.

**A.2 Cusp colourings.** By E.61 a section of `N ⋊ G_Q` that is ramified at a prime `q ≠ 3` is, at `q`, the
tangential section of one cusp `i(q)`.
- (a) For every section the cusp `i(q)` is the same at all ramified primes.
- (b) A section that is ramified at one prime `q ≠ 3` is cuspidal (it lies in the packet of a rational cusp).
- (c) The same two statements for `N/N″` (E.66) and for the marked quotient (E.71).
Method available: the presentation of E.73 (local packets coupled by the Frobenius words `Y_𝔮`); the local
obstruction of E.42 (`b/(q − 1) ∈ Z_3`), which kills the mixed classes `α_P + 3^kκ_3(p)e_Q` for `p` in the set of
E.43 and does not kill them for the other primes.

**A.3 Sections ramified at infinitely many primes (PS-3, corrected).** A section of `(N/γ_3N) ⋊ G_Q` that is
ramified at infinitely many primes lifts to a section of `N ⋊ G_Q` if and only if it is the image of a cuspidal
section. **(mine)** The restriction to non-cuspidal sections is needed: a cuspidal section twisted by a class of
`H¹(Q, Z_3(1))` with infinitely many non-zero valuations is ramified at infinitely many primes and lifts.

**A.4 The phantom inside E.37.** There is an abelian class `α` whose corrections `c_𝔮` of (E37.10) are integral at
every `𝔮` and do not tend to zero. Give it explicitly, with the primes and the 44 coordinates, in the notation of
E.37; and prove that the class of LM7_PUSH A.4 is of this form. Then reconcile the two fibre groups: E.37 has
`ℛ(Z_3) ⊕ Z_3^24 ⊕ (Z/3)^9 ⊕ (Z/9)^5`; LM7_PUSH A.3, A.8 have theirs (the reviewer records "24 against 23 + 1").

**A.5 The whole metabelian quotient.** The prompt's metabelian quotient is `π̂/π̂″` for the full profinite group;
E.37–E.89 treat its pro-3 part only. For the Fermat cubic: the set of section classes of the full profinite
metabelian quotient of the geometric group, as a fibre product over the primes and the mixed finite quotients of
the sets computed for each. State which mixed quotients impose conditions the pure pro-`p` parts do not.

**A.6 Descent form (PS-1, unchanged).** E.37 and E.44 rederived as `Γ`-descent along `Q(μ_{3^∞})`:
`H²_cts(G_Q, M) = X/(γ − 1)X`, the lim¹ part as `closure((γ − 1)X)/(γ − 1)X`. No row of the continued run
addresses it.

## B. D.19 (ii): the CM coset

The candidate after D.46–D.49: `h` on the 2-primary part, the identity on the odd parts. It exists on every
quotient of `B̂` that is a fibre product of pro-`p` groups over a base fixed by `h`.

**B.1 The first deciding quotient.** With `G_3 = B̂/(N̂′N̂³)`, `K_3 = N̂′N̂³`, `J_{3,2} = B̂/(K_3′K_3²)`,
`V_{3,2} = K_3/(K_3′K_3²)`, `W = [V_{3,2}, A]` as in (D.49.9)–(D.49.11): there is a continuous automorphism of
`B̂/(𝔯_h ∩ K_3′K_3²)` that sends `s`, `r` to conjugates of themselves, fixes `t = sr`, and induces `α_h^*` of D.49
on `𝒲_h`. The obstruction is a class in the cokernel of the correction map `(1 − s)c_β + s(1 − r)c_A` (with the
centralizer columns, as in D.45) on `W`, a module induced from a 3-group; compute it by Mackey and Shapiro, not by
matrices of size `|G_3|`. Also evaluate `|A|`, which D.49 leaves open.

**B.2 The `S_7`-marking.** For the marking (D.46.9), `M_7` its kernel: the candidate extends to a peripheral
automorphism of the relative pro-2 completion of `B̂` over `S_7 ×_{C_2} Q`, and of its relative pro-3 completion.
(The reviewer's hunch H3.)

**B.3 The general step.** Let `G` be a finite marked quotient of `B` on which a peripheral automorphism `φ` of a
larger quotient acts, and `p` a prime. Give the exact obstruction to extending `φ` to the relative pro-`p`
completion over `G`, as a cohomology class with its coefficient module, and prove that it vanishes whenever `φ` is
the identity on `G` and Galois on the pro-`p` part (this is D.46–D.49). Then determine the smallest tower
`G_0 ← G_1 ← G_2` (kernels a 3-group, then a 2-group, or the reverse) in which the class of the candidate is not
forced to vanish by that argument.

**B.4 Homomorphism (PS-4 (a)).** The CM coordinates `ρ = (T, W)` on `GT̂_0`, read from the conjugators of `r` and
`s` as in D.25 and D.46 (`T_4` through `G_3`, `W_3` through `G_2`, by (D.25.6)), form a homomorphism to
`(T_R × T_S)(Ẑ)/±1`. Consequence to prove with it: `GT̂_0` reaches the extra coset if and only if it contains an
element that is the identity on `Q` with pair `(I, [i])`.

**B.5 The non-abelian distribution test for `GT̂` (LM7_PUSH E.3).** By D.20 every element of `GT̂` satisfies
`φ_n(f) = y^{c_n(f)}f` for all `n`. Evaluate this identity for the candidate's parameter in the largest quotient
where both sides are defined (start: `B̂/[M, M]`-type quotients of D.47 with `n = 3, 4`). **(mine)** Its abelian
shadow `c_{mn} = c_m + c_n` holds for the candidate and decides nothing.

**B.6 PS-5, reworded (mine).** (a) No peripheral automorphism of `B̂` with multiplier `≡ 1` mod 3 acts on the
relative pro-2 completion over `Q_0 = S_3 × C_3` as complex conjugation does: it commutes with the deck element
`δ` of `w³ = z(z − 1)` and acts `Z_2[ζ_3]`-linearly on `T_2`, by (D.34.4). (b) `GT̂_0` contains an element with
multiplier `(−1, 1, 1, …) ∈ ∏_p Z_p^×` acting on the pure pro-2 completion of `F` as complex conjugation and
trivially on the pure pro-3 completion. For (b): the element acts on `T_2` of the cubic by a unit of
`Z_2[ζ_3]` of norm `−1`; such units exist; decide whether one is compatible with (a) and with D.36's graph.

## C. D.13

**C.1 The metabelian group (mine; H4).** Every automorphism of the pro-ℓ metabelian group `F^(ℓ)/(F^(ℓ))″` that
is the identity on the abelianization and preserves the conjugacy classes of `x`, `y`, `xy` has, in its outer
class, a representative that extends to `F̂/F̂″` by the identity on the complementary factor (the idempotent `e_0`
of `Z_ℓ[[Ẑ²]]`), with the same three properties. Consequences: the images of `Out^♯(F̂/F̂″)` and of its
`𝔖_3`-centralizer in weights 5 and 9 are 3 and 2. Then the whole group `Out^♯(F̂/F̂″)` as a group of units of
`Ẑ[[Ẑ²]]`, accounting for LM8 A.22 (deck idempotents), D.47 (coefficient primes) and this lemma.

**C.2 The first lift.** Fix `ℓ ≥ 5` and the automorphism `φ_5` of `F̂/F̂″` attached by C.1 to a weight-5 special
derivation outside the gamma line. `φ_5` lifts to an automorphism of `F̂/[F̂″, F̂]` preserving the three conjugacy
classes; then of `F̂/F̂‴`; then of the relative completions over the finite quotients of D.24 (`A_5`) and of
LM1 E.21 (the `𝔖_3`-cover). The same for the weight-9 vector `X²Y²(X+Y)³` and `GT̂_0`. The first layer with a
non-zero obstruction, or lifts at all layers with the limit, decides LM7_PUSH D.1 and D.2.

## D. Checks the successor prompt should ask GPT-6 Astra to make of the continued run

- D.27 rests on (D.25.6): `q(C_{G_2}(s) ∩ im F) = 1`, `q(C_{G_3}(r) ∩ im F) = 1`. Prove it from the module
  structure, independently of the program.
- D.45: give the degree-9 obstruction as a class in a named cohomology group, so that it can be compared with B.3.
- E.63 does not exist; say whether a statement was dropped.
- The integer `h` of E.69 and `|A|` of D.49 are left unevaluated by the return; evaluate them.


---

## Added 14 November 2026: items for the successor of LM7_PUSH, after checkpoint 09 and the referee reports

By Claude Fable 5.2 at effort high (intake agent), first written 14 November 2026, 01:56 UTC, as a draft waiting
for the referees; rewritten 02:45 UTC with their verdicts. With the consultation of the Longue Marche expert (Claude
Fable 5.2 at effort max; `pro_intake_20261114\CONSULT_LM_EXPERT.md`). Reading behind it:
`pro_intake_20261114\INTAKE_20261114.md`, sections 1 and 9.

**The referee verdicts** (Claude Opus 5.5 at effort max, 14 November 2026; reports in
`pro_intake_20261114\referee\`):
- `REFEREE_A_D50_E58.md`: LM7_PUSH D.44 (the parts used), D.50 and E.58 are **proved as claimed**. The element of
  E.58 exists, with bits `(1, 0)`. Herfort–Ribes 1985, Theorem B′, opened and confirmed. Not checked there: D.1,
  D.2, D.52 beyond D.50, and E.9.
- `REFEREE_B_E61_E65.md`: E.65 is **proved, with two gaps that the report closes** (the vanishing on Galois; the
  existence of the pure `r`-frame). E.61 and E.67 are proved for their general statements; E.64 is proved where it
  could be checked (three steps rest on E.39, on Boggi 2026 v6 and on Nakamura–Tsunogai–Yasuda 2010, not verified;
  none is used by E.65 or E.67). "Is `Δ` zero on `GT̂`?" is a correct reformulation of E.3, and it does not use
  E.58. With E.58: `Δ ≠ 0` on `GT̂` gives `GT̂ ≠ G_Q`; `Δ = 0` on `GT̂` gives `GT̂ ⊆ ker Δ ⊊ GT̂₀`.
- `REFEREE_A_LM4_D32.md`, `REFEREE_B_LM4_D34.md`: LM4 D.32 and D.34 are **proved as claimed**. For an element `τ ≠ 1`
  of finite order of `GT̂₀`: `τ = (−1, f_τ)` and `Δ(τ) = δ((1, f_τ))`; this is 0 when `τ` is conjugate to complex
  conjugation in `GT̂₀`, which D.34 does not prove.
- A defect of the register, found by both referees: LM7_PUSH E.1, E.2, E.58 and E.65 list "D.25" as a dependency
  and mean LM7 D.25 (the Fermat tower); LM7_PUSH has its own D.25, an unrelated row. E.65's dependency list also
  omits Herfort–Ribes and LM7 D.15 and lists E.62, which it does not use. E.2 and E.58 depend on each other in the
  register only: E.58's proof does not use E.2.

**The run cannot be reached.** LM7_PUSH keeps writing checkpoints and takes no message. The successor is a new
prompt in a fresh chat, built on the newest checkpoint filed when it is written (now checkpoint 09: 218 rows, E.3
open; E.74–E.76 exist outside the register). Each item is "prove or refute", except S.8, which is editing.

**What checkpoint 09 and the referees change in the items above.**
- B.4 (the CM coordinates form a homomorphism): proved by E.65 (refereed), in a sharper form: a continuous
  character `Δ : GT̂₀ → F₂` that vanishes on `G_Q`, with `Δ = 1` on the element of E.58. Cited; not asked again.
- B.5 (the non-abelian distribution test for `GT̂`): carried out for `n = 2, 3, 4, 6, 12` and in matrix form in all
  `GL_2(F_3)` and `SL_2(F_3)` epikernels (E.66, E.71; not refereed). No exclusion. Not asked again.
- B.1–B.3 (the tower's layer route): superseded by the lifting theorem E.58 (refereed); see Part 1 of
  `pro_intake_20261114\PUSH_ITEMS_20261114.md`. B.6 stands.
- C.1, C.2 (D.13): claimed by D.1, D.2 through D.50. D.50 is refereed; the other inputs of D.1 and D.2 (D.20, D.21,
  D.51, D.52) are not. They are item S.6 below.

### Items of the successor (main question: `Δ` on `GT̂`)

**S.1 The main question.** Prove or refute: `Δ = 0` on `GT̂`. The prompt states both outcomes in so many words: if
`Δ = 1` on some element of `GT̂`, then `GT̂` has a continuous quadratic character that is trivial on `G_Q` and the
Galois image is not all of `GT̂`, and every step of such a proof is written out in full; if `Δ = 0` on `GT̂`, then
`GT̂ ⊆ ker Δ ⊊ GT̂₀`, a relation that the pentagon adds to the 2-cycle and 3-cycle relations. Routes, each to be
carried to a proof or to the exact statement that blocks it:
 (a) the three bits of E.67.1 on `GT̂`: `ε_3(𝒟_3)`, `ε_2(𝒟_4)`, `ε_2(B_4)`, one by one (E.67.1 is an identity of
     characters and assigns no value: referee B);
 (b) the comparison of the triangle-cover action of Nakamura–Tsunogai–Yasuda 2010 (Proposition 4.4, Theorem 4.16;
     Propositions 4.11–4.13 for E.64.13) with the normalizer coordinate, on all of `GT̂` and not on Galois only;
 (c) the harmonic and equianharmonic equations (Nakamura–Tsunogai and sequels) and relation (III′) of
     Nakamura–Schneps: decide whether they hold for `F` exactly when `Δ(F) = 0`;
 (d) the pentagon in a quotient of the five-point group in which both CM coordinates are read, with the proof that
     the value forced there holds on `GT̂` (a finite survival statement of the kind E.59–E.73 is not an answer:
     LM8 E.16 shows that finite shadows need not lift);
 (e) the surface form (D.50.12) of the counting identity on the five-point sphere group, with the Harbater–Schneps
     description of `GT̂`.

**S.2 The finite level of `Δ`.** `Δ` is continuous with values in `F₂`, so it factors through one finite quotient of
`GT̂₀` acting on one finite characteristic quotient of `B̂`. Determine such a quotient and compute `Δ` there by
program on every shadow. E.58 is refereed, so this is no longer needed as a second proof of it; it is the finite
object on which routes (a)–(d) of S.1 are computed, and it gives the shadow test for any candidate element.

**S.3 §47.** With `C^φ` the subgroup of `GT̂₀` cut out by the equation of §47 (LM8_PUSH, Lead 8): prove or refute
`C^φ ⊆ ker Δ`, then `C^φ = ker Δ`. By E.58 the first inclusion gives `C^φ ≠ GT̂₀`. (Also task C.8 of LM8_PUSH;
whichever prompt is sent first carries it.)

**S.4 Torsion.** By LM4 D.32, D.34 (refereed) every element `τ ≠ 1` of finite order of `GT̂₀` is an involution
`(−1, f_τ)`, and `Δ(τ) = δ((1, f_τ))`. Prove or refute: `δ((1, f)) = 0` for every `f` such that `(−1, f)` is an
involution of `GT̂₀`. It follows from the conjugacy of every involution to complex conjugation, which is open (LM4
D.12; the question of Lochak and Schneps); an involution with `Δ = 1` refutes that conjugacy in `GT̂₀`.

### Additions of the Longue Marche expert (Claude Fable 5.2 at effort max, 14 November 2026)

Sources: `pro_intake_20261114/EXPERT_IMPLICATIONS_E65_LM_part2.md`, section 7 ("implications item n") and `pro_intake_20261114/EXPERT_DELTA_TAU.md` ("Δ/τ T n"). The hunches named are the expert's and are checked by no one.

**Add to S.1 (implications item 1).** Three routes, in this order. (a) The finite certificate: `Δ` factors through a finite level, so `Δ = 0` on `GT̂` holds exactly when at some finite level no pentagon shadow has parity one. Compute every pentagon shadow with its parity at the levels of the five-point group through which `Δ` is defined, with the presentation of that group by torsion generators of orders 5 and 4. A level without a shadow of parity one proves `Δ = 0`. Shadows of parity one at every level examined decide nothing (the lemma on inverse systems of finite sets); then S.11 is the question. (b) The frames, under an element of `GT̂`, of the torsion elements of orders 5, 4 and 3 of the five-point group, and the relations between these frames that the relations of the group force. (c) The harmonic equation for `GT̂` at level 12 (addition to S.3).

**Add to S.2 (implications item 8).** Determine the smallest finite quotient of `GT̂₀` through which `Δ` factors, with a program that evaluates `Δ` on every residue of that level. The same task is C.6 of LM8_PUSH: it is asked in one of the two prompts.

**Add to S.3 (implications item 2; hunch H1; Lead 24 of LM8_PUSH).** Prove or refute: `C^φ` lies in the subgroups of the harmonic and of the equianharmonic equation, and these lie in `ker Δ`, with the exact substitution between §47, those equations and relation (III′). Prove or refute: the degree-two map between the pictures of level 3 and level 4 (the tetrahedral group inside the octahedral group) is the harmonic map `w = 4λ(1 − λ)`, and the two parities of an automorphism compatible with it agree.

**Add to S.4 (implications item 4; Δ/τ T3; hunch; Lead 23 of LM8_PUSH, task B.5).** Determine `H¹(⟨c⟩, ℋ)` for complex conjugation `c` and the multiplier-one subgroup `ℋ`, its map to `F₂` through `Δ`, and the conjugacy classes of involutions of `GT̂₀`. Prove or refute: an involution with `Δ = 1` exists. Construction to decide: for `γ ∈ G_Q` with `γ(3^{1/4}) = i·3^{1/4}` and `σ = γcγ⁻¹c`, the element `σ₂` given by the product decomposition of E.58.2 (equal to `σ` on one side, the identity on the other); does the decomposition commute with conjugation by `c`, and is `σ₂c` an involution. It is asked in one of the two prompts.

**S.9 `Δ` as the sign of an idempotent (Δ/τ T1).** Prove or refute: there is a homomorphism `u : ℋ → μ₂(Z/3) × μ₂(Z/4) = {1, 5, 7, 11} ⊂ (Z/12)^×` whose two components are the two frame parities of E.65, with `u = ±1` on Galois and `u = 5` on the element of E.58, so that `Δ(F) = 1` exactly when the idempotent `(1 − u(F))/2` of `Z/12` is `4` or `9`. Determine the ring in which the two frames are one sign (the product of the reductions of `Z[ζ₃]` and `Z[i]` at the levels where the parities are read). The two parities are read on two different frames; the statement is to be corrected to the form that holds. If it holds, the structure of the globalization note (a non-trivial idempotent on a connected base) sits on the two elliptic points of the modular orbifold of sections 46 to 49.

**S.10 Characters and the CM image (Δ/τ T2; implications items 5 and 3).** Asked in LM8_PUSH, task C.9 (all continuous characters to `F₂` that vanish on Galois) and task C.7 with Lead 25 (the image of the two CM coordinates; hunch H2). Not repeated here.

**S.11 A mixed sign in `GT̂` (Δ/τ T4).** Prove or refute: `GT̂` contains an element whose frame sign modulo 12 is `5` or `7`; by E.65 this is `Δ ≠ 0` on `GT̂`. Decide first whether the product decomposition of E.58.2 holds with the pentagon, at the smallest level of the five-point group that mixes the primes 2 and 3.

**S.12 Where the structure of the globalization note could sit in the programme (Δ/τ T5, reframed 14 November 2026).** The user's note on the semiring `G(Z) = Z ⊔ {τ_G}` is where the idea came from; nothing is asked about that semiring. Its structure is: a neutral element doubled over the visible quotient and told apart by one bit; an idempotent that is not constant on a connected base; one bit left when everything arithmetic is collapsed; the doubled element as an extra fixed point of the sign. Each statement below is about objects of the programme and is to be proved or refuted; each says what it would give.

- (a) *In `GT̂₀` and its quotients.* Let `V` be the image of `GT̂₀` in the product of its pro-`ℓ`, pro-nilpotent and graded quotients. Prove or refute: `F ↦ (image of F in V, Δ(F))` maps `GT̂₀` onto `V × F₂`, and on the Galois image the second coordinate is zero. It would give: the identity is doubled over `V` by the elements of the kind of E.58, at every element of `V` and not only at the identity, and Galois is the part where the bit is tied to the visible data.
- (b) *In the frames.* Prove or refute: the frame sign of an element of `GT̂₀` is a function with values `±1` on the set of the two elliptic points of the modular orbifold; it is constant for every Galois element; every function occurs on `GT̂₀`; and `ker Δ` is the largest closed subgroup of `GT̂₀` on which it is constant. Then the same for `GT̂` on the set of all special points of the spheres with four and five points (orders 2, 3, 4, 5). It would give: `Δ` as the failure of a sign to be constant on a connected base, and E.3 as the question whether the pentagon makes it constant.
- (c) *In a module of the programme.* Find a module on which `GT̂₀` acts through its place in the tower (the first homology of the covers of level 12, the Alexander module of `F`, the first relative stages of LM8 B.31–B.35) and which has a line on which `GT̂₀` acts by `Δ`; or prove that the homology of the covers of level 12 has none. Prove or refute: for every such module `M`, `M` and its twist by `Δ` are isomorphic as Galois modules and not as modules over `GT̂₀`. It would give: the place where the bit is an eigenvalue, as the involution of LM8 A.22 is the eigenvalue `1 − 2e` on a block of the Alexander module, and a test of `Δ` on elements of `GT̂` through their action on that line.
- (d) *In the semiring of closed subsets and in the completed group ring.* Through `Δ` the semiring of closed subsets of `GT̂₀` (union and product) maps onto the semiring of subsets of `F₂`, which has four elements. Prove or refute: the closed subsets of the Galois image have image `{∅, {0}}`; the closed subsets of `GT̂` have the same image exactly when `Δ = 0` on `GT̂`; and at a finite level `K` through which `Δ` factors, the subsets of the finite set of pentagon shadows of level `K` decide it. For `ℓ` odd: the augmentation of `Z_ℓ[[GT̂₀]]` and its twist by `Δ` are two continuous ring maps to `Z_ℓ` that agree on the completed group ring of the Galois image; determine all continuous ring maps with that property (the case of values `±1` is task C.9 of LM8_PUSH). It would give: E.3 as a statement about finite sets of shadows.
- (e) *In sections 46 to 49.* The frames are the conjugators of his signed normalizers of `ρ` and `σ` (cote 140-3, §49.IV–V, scans 530–560; LM8 B.31–B.35). Prove or refute: the two frame parities are the two signs of his independently signed source; his linked source is the condition `Δ = 0`; and reconcile this with LM8 B.31, which says that for the full profinite modular group the linked and the independently signed sources coincide. Determine the chain `G_Q ⊆ C^φ ⊆ ker Δ ⊊ GT̂₀` (`C^φ` the subgroup of §47) and which inclusions are strict. It would give: the passage of the manuscript where the bit is already present, and the reading of §47 as the condition that removes it.
- (f) *The sign.* The doubled element as an extra fixed point of the sign is asked in S.4: the involutions of `GT̂₀` with `Δ = 1` (Lead 23 and task B.5 of LM8_PUSH).

Implications item 6 (the frame at the point of order five) is a prompt of its own: `pro_intake_20261114/PUSH_ITEMS_ORDER5_FRAME.md`. Implications item 7 is in the Fermat successor (`pro_intake_20261114/PUSH_ITEMS_20261114.md`, Part 1, end of 1.A).

**S.5 The lifting theorem used once more.** Apply E.58 (refereed) with `U = N = ker(B → Q)` to the Fermat tower's
candidate D.46 (Part 1, item 1.1 of `PUSH_ITEMS_20261114.md`); and determine the image of the multiplier-one
subgroup of `GT̂₀` in `Cent(R_0) × Cent(S)` (the pair `(T, W)` modulo 12): by E.58 it contains `(−I at 3, 1)`, and
with D.46 it would contain `(1, [i])`; prove what the whole image is. The manuscript side, in the corrected form (cote 145; `pro_intake_20261114\EXPERT_ON_INTAKE_11.md`, by the Longue Marche expert, Claude Fable 5.2 at effort max, which corrects section 11 of the intake): his pair `(γ, χ)` of scan 11 is the pair `(f, λ)` up to the gauge `l_0^α g l_1^{−α}`; his `g` (scan 7, `uρ = int(g)ρu`) is the cocycle `f⁻¹`, not a frame; the frames are the conjugators by which an element moves the canonical splittings over the isotropy groups at `P` and at the harmonic points (scans 22 and 28), and the `r`-frame is a primitive `A` of `g`, `g = A·ρ(A)⁻¹`. `Δ` is a function of `γ`, but not of `γ` modulo 12: the `f` of E.58 lies in the nilpotent residual of `F′F³` while its `r`-frame is `5I` modulo 12. So the image asked for here is the image of the frames, not of `γ` reduced modulo 12. `β` of scan 11 is not identified; scans 8 to 12 decide it, and whether `β = ρ_F` of E.61 is to be proved or refuted. S.1 gains no route from cote 145: his coordinates are notation for S.1, not a method.

**S.6 What is still to be checked in checkpoint 09** (asked of GPT-6 Astra in the successor, each as "prove or give
the exact error"):
- D.1 and D.2 beyond D.50: D.51 and D.52 (the pro-`ℓ` inputs), the upper bounds D.20, D.21; and for D.2, that the
  weight-nine pair fails the full pentagon for every lift, not for one chosen lift.
- The three unverified inputs of E.64: E.39 (the quartic frame `H_F`), the profinite sewing comparison E.64.3
  (Boggi 2026 v6, Theorem 2.3 and Proposition 2.6 (i)), the Galois formula E.64.13 (Nakamura–Tsunogai–Yasuda 2010,
  Propositions 4.11–4.13), each with the source opened and quoted.
- The 48 per-origin data statements of E.67, recomputed.
- E.2's sentence that an equivalence asserted in LM7 D.25 is false: every place that cites D.25 is corrected.
Done on our side, and not asked again: the brute-force test of the finite theorem behind D.50
(`referee\checks\check_d50_finite_theorem.py`); the dictionary behind "Δ vanishes on Galois" (referee B, step 9).

**S.7 Not asked.** D.50, E.58, E.61, E.65 (refereed; cited). Further finite quotients of the kind E.59–E.63, E.66,
E.68–E.73.

**S.8 Repair of the register and of the text (editing; added after the referee reports).** In the successor's own
register and paper:
- every dependency "D.25" of E.1, E.2, E.58, E.65 that means the Fermat tower's row is written "LM7 D.25", with the
  file `LM7_FERMAT_TOWER\sections\D_cm_shadow.tex`; LM7_PUSH's own D.25 (an order-five peripheral cycle) is not
  cited there;
- the dependency list of E.65 gains Herfort–Ribes 1985 (Theorem B′) and LM7 D.15, and loses E.62;
- the circular pair E.2 / E.58 is cut: E.2 depends on E.58, E.58 does not depend on E.2; the same check for
  D.1 / D.51 and D.2 / D.52;
- the register statement of E.1 gains the bit convention, which is now only in its proof;
- the two gaps of E.65 are written into its proof: the derivation of the vanishing on Galois (the models
  `y² = x³ + 1`, `y² = x³ − x`, the signs), and the existence of the pure `r`-frame for an arbitrary element;
- in D.50, the Hopficity sentence (lines 454–459 of `D_pronilpotent_lift_agent.tex`) is replaced by the standard
  argument, and Turaev 2009 is removed from the dependencies (its Theorem 1.2 is for positive genus; the pants
  case is proved in the text).
- where the frames are introduced, the dictionary with cote 145 in its corrected form (S.5): `(γ, χ) = (f, λ)` up to gauge, `g = f⁻¹` the cocycle, the frames as the conjugators of the splittings of scans 22 and 28, `β` settled from scans 8 to 12.
The two referee reports are attached to the successor so that each repair can be made against the exact place.

**Attachments the successor needs** (LaTeX and registers only): checkpoint 09's register and the sections
`D_pronilpotent_lift_agent.tex`, `D_modular_coprime_agent.tex`, `D_full_weight5_agent.tex`,
`D_full_weight9_agent.tex`, `E_agent.tex`, `E_relative_cm_lift_agent.tex`, `E_genus_one_sewing_agent.tex`,
`E_hyperelliptic_CM_agent.tex`, `E_cm_character_agent.tex`, `E_orbifold_CM_agent.tex`; the four referee reports
with `referee\checks\`; the Fermat tower's `D_cm_shadow.tex` and `D_arithmetic_replacement.tex`; LM4's register
and paper of 01:56 UTC (D.32, D.34, D.42); cote 148, scans 29–72 (the five-point diagram of scans 31–33 with its
"1620 flèches" and the request for "un syst. fondamental de relations"; the transcriber's notes link it to E.3
and to LM7_PUSH E.46). Also cote 145 (`returns\MPL_145_unzipped\`: transcription, notes, doubts; scans 5–12, 22–29, 33–38 page by page) and cote 143, scans 29–33 (`returns\MPL_143+141_unzipped\`).
