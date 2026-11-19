# Push items for the successor of LM7 (from the intake of the continued run)

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

## Added 14 November 2026: draft items for the successor of LM7_PUSH, after checkpoint 09

By Claude Fable 5.2 at effort high (intake agent), 14 November 2026, 01:56 UTC, with the consultation of the Longue
Marche expert (Claude Fable 5.2 at effort max; `pro_intake_20261114\CONSULT_LM_EXPERT.md`). Reading behind it:
`pro_intake_20261114\INTAKE_20261114.md`, sections 1 and 9.

**Status: DRAFT, waiting for the referee reports.** Referee A (Claude Opus 5.5 at effort max) is checking D.44,
D.50, E.58; referee B (same model and effort) E.61, E.62, E.64, E.65, E.67, LM7 D.25, E.1. No successor prompt is
sent before they report (the expert's recommendation). If a referee finds an error in D.50 or E.58, items S.1–S.6
change: the first item of the successor is then the repair or the refutation of that statement.

**The run cannot be reached.** LM7_PUSH keeps writing checkpoints and takes no message. The successor is a new
prompt in a fresh chat, built on the newest checkpoint filed when it is written (now checkpoint 09: 218 rows, E.3
open; E.74–E.76 exist outside the register). Each item is "prove or refute".

**What checkpoint 09 changes in the items above.**
- B.4 (the CM coordinates form a homomorphism): claimed proved by E.65, in a sharper form: a continuous character
  `Δ : GT̂₀ → F₂` that vanishes on `G_Q`, with `Δ = 1` on the element of E.58. To be confirmed by the referee, then
  used; not asked again.
- B.5 (the non-abelian distribution test for `GT̂`): carried out for `n = 2, 3, 4, 6, 12` and in matrix form in all
  `GL_2(F_3)` and `SL_2(F_3)` epikernels (E.66, E.71). No exclusion: every final value survives. Not asked again.
- B.1–B.3 (the tower's layer route): superseded by the lifting theorem if it holds; see Part 1 of
  `pro_intake_20261114\PUSH_ITEMS_20261114.md`. B.6 stands.
- C.1, C.2 (D.13): claimed by D.1, D.2 through D.50; they wait for referee A and are not asked again.

### Items of the successor (main question: `Δ` on `GT̂`)

**S.1 The main question.** Prove or refute: `Δ = 0` on `GT̂`. If `Δ = 1` on some element of `GT̂`, then `GT̂` has
a continuous quadratic character that is trivial on `G_Q` and the Galois image is not all of `GT̂`: the prompt
says this in so many words and asks for every step of such a proof in full. Routes, each to be carried to a proof
or to the exact statement that blocks it:
 (a) the three bits of E.67.1 on `GT̂`: `ε_3(𝒟_3)`, `ε_2(𝒟_4)`, `ε_2(B_4)`, one by one;
 (b) the comparison of the triangle-cover action of Nakamura–Tsunogai–Yasuda 2010 (Proposition 4.4, Theorem 4.16)
     with the normalizer coordinate, on all of `GT̂` and not on Galois only;
 (c) the harmonic and equianharmonic equations (Nakamura–Tsunogai and sequels) and relation (III′) of
     Nakamura–Schneps: decide whether they hold for `F` exactly when `Δ(F) = 0`;
 (d) the pentagon in a quotient of the five-point group in which both CM coordinates are read, with the proof that
     the value forced there holds on `GT̂` (a finite survival statement of the kind E.59–E.73 is not an answer:
     LM8 E.16 shows that finite shadows need not lift);
 (e) the surface form (D.50.12) of the counting identity on the five-point sphere group, with the Harbater–Schneps
     description of `GT̂`.

**S.2 The finite level of `Δ`.** `Δ` is continuous with values in `F₂`, so it factors through one finite quotient of
`GT̂₀` acting on one finite characteristic quotient of `B̂`. Determine such a quotient, compute `Δ` there by
program on every shadow, and prove by the fibre criterion (an element of the limit over a directed subsystem lifts
if and only if its fibre is non-empty at every stage) that the shadow of the element of E.58 lifts. This is a
second proof of E.58 that does not go through D.50.

**S.3 §47.** With `C^φ` the subgroup of `GT̂₀` cut out by the equation of §47 (LM8_PUSH, Lead 8): prove or refute
`C^φ ⊆ ker Δ`, then `C^φ = ker Δ`. (Also task C.8 of LM8_PUSH, added today; whichever prompt is sent first carries
it.)

**S.4 Torsion.** `Δ` on every element of finite order of `GT̂₀`; zero on the conjugates of complex conjugation. With
LM4 D.12, D.32, D.34.

**S.5 The lifting theorem used once more.** Apply E.58 with `U = N = ker(B → Q)` to the Fermat tower's candidate
D.46 (Part 1, item 1.1 of `PUSH_ITEMS_20261114.md`); and determine the image of
`{F ∈ GT̂₀ : multiplier one} → Cent(R_0) × Cent(S)` (the pair `(T, W)` modulo 12): by E.58 and D.46 it contains
`(−I at 3, 1)` and `(1, [i])`; prove what the whole image is.

**S.6 Checks the successor prompt asks GPT-6 Astra to make of checkpoint 09.**
- A brute-force test of the finite theorem behind D.50 on small groups, for both sources, including a case with
  centralizer conjugators (the case E.58 uses), with code.
- The dictionary behind "Δ vanishes on Galois": on `G_{Q^ab}` the conjugators of `r` and `s` are the torsion
  representations of `y² = x³ + 1` and `y² = x³ − x`, with the correction `V = U^{8ρ}` at the cusp and the signs
  (LM7 D.15–D.17, D.25).
- E.2's sentence that an equivalence asserted in LM7 D.25 is false: every place that cites D.25 is to be corrected.
- D.2: that the weight-nine pair fails the full pentagon for every lift, not for one chosen lift.

**S.7 Not asked.** D.1, D.2, E.2 (refereed on our side, then cited). Further finite quotients of the kind
E.59–E.63, E.66, E.68–E.73.

**Attachments the successor needs** (LaTeX and registers only): checkpoint 09's register and the sections
`D_pronilpotent_lift_agent.tex`, `D_full_weight5_agent.tex`, `D_full_weight9_agent.tex`, `E_agent.tex`,
`E_relative_cm_lift_agent.tex`, `E_genus_one_sewing_agent.tex`, `E_hyperelliptic_CM_agent.tex`,
`E_cm_character_agent.tex`, `E_orbifold_CM_agent.tex`; the two referee reports; the Fermat tower's `D_cm_shadow.tex`
and `D_arithmetic_replacement.tex`; LM4's rows D.32, D.34, D.42; cote 148, scans 29–72 (the five-point diagram of
scans 31–33 with its "1620 flèches" and the request for "un syst. fondamental de relations"; the transcriber's
notes link it to E.3 and to LM7_PUSH E.46).
