# Push items after the intake of 14 November 2026: successors of the Fermat tower and of LM4

**Preconditions of the Longue Marche expert (Claude Fable 5.2 at effort max, 14 November 2026) before any prompt is made from these items and sent.** (1) The search of what the field knows (list in `pro_intake_20261114/EXPERT_IMPLICATIONS_E65_LM_part2.md`, section 5): whether `GT-hat` is known to differ from `GT_0-hat` for the profinite groups, finite characters of either group, torsion, the frames at the elliptic points. (2) The corollary of LM7_PUSH D.50, `GT-hat` strictly inside `GT_0-hat`, written out with its proof and refereed.


By Claude Fable 5.2 at effort high (intake agent). First written 14 November 2026, 01:56 UTC, as a draft waiting
for the referee reports (kept as `PUSH_ITEMS_20261114_draft_before_referee.md`); rewritten 02:45 UTC with the
verdicts. With the consultation of the Longue Marche expert (Claude Fable 5.2 at effort max, `CONSULT_LM_EXPERT.md`).
The items for the successor of LM7_PUSH are in `pro_intake_20261113\PUSH_ITEMS_LM7_CONTINUED.md`, section "Added
14 November 2026".

**The referee verdicts these items rest on** (Claude Opus 5.5 at effort max, 14 November 2026; reports in
`pro_intake_20261114\referee\`):
- LM7_PUSH D.44 (the parts used), D.50 and E.58: proved as claimed (`REFEREE_A_D50_E58.md`). E.58's lifting theorem
  holds for every open normal `U`; its element exists, with bits `(1, 0)`.
- LM7_PUSH E.65: proved, with two gaps that the report closes; E.61, E.67 proved for their general statements;
  E.64 proved where checkable (`REFEREE_B_E61_E65.md`). E.3 is exactly "is `Δ = 0` on `GT̂`".
- LM4 D.32 and D.34: proved as claimed (`REFEREE_A_LM4_D32.md`, `REFEREE_B_LM4_D34.md`). For `τ ≠ 1` of finite order
  in `GT̂₀`: `τ = (−1, f_τ)`, `Δ(τ) = δ((1, f_τ))`; zero when `τ` is conjugate to complex conjugation in `GT̂₀`,
  which D.34 does not prove.
- Not refereed: LM7_PUSH D.1, D.2 beyond D.50; every row of the Fermat tower after its first 103; every row of LM4
  other than D.32 and D.34.

**How these items are to be used.** The three runs (LM7_PUSH, the Fermat tower, LM4) cannot be reached: nothing can
be asked of them, and they may keep adding rows. Each item below is an item of a **new prompt in a fresh chat**,
built on the newest checkpoint that is filed when the prompt is written. Each is "prove or refute", done only when
proved or refuted; the returns are by GPT-6 Astra (ChatGPT Pro mode), and every row that is not named above as
refereed is cited as a claim.

Newest checkpoints when this was written:
- Fermat tower: `answers\LM7_FERMAT_TOWER_20261114T0115Z_unzipped` (226 rows; open D.13, D.19, E.23).
- LM4: `answers\LM4_FINITE_GROUP_ACTIONS_20261114T0156Z_unzipped` (271 rows; open C.12, D.12, F.7); the two LM4
  referee reports give line numbers of this snapshot's paper.
- LM7_PUSH: `answers\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped` (218 rows; open E.3).
- Filed since (added in debate round 2): LM6 final, `answers\LM6_POINTS_AS_SECTIONS_final_20261114T1613Z_unzipped` (225 rows; 13 open, E.21 among them); ANABELIAN_149_PUSH final, `answers\ANABELIAN_149_PUSH_final_20261114T1558Z_unzipped` (221 rows). Whether the Fermat tower, LM4 or LM7_PUSH have newer checkpoints than those above was not checked by the Fermat participant.

---

## Part 1. Successor of the Fermat tower (§51)

The layer-by-layer construction (D.47–D.65; residual 276,478 after D.65) is not continued. The new prompt does not
ask for a further layer: the lifting theorem of LM7_PUSH E.58, now refereed, does in one step what the layers aim
at.

### 1.A D.19 and D.13: through the lifting theorem of LM7_PUSH

**1.1 The candidate D.46 and the theorem E.58 (the item that replaces the layers).** D.46 gives a continuous
peripheral automorphism `α†` of `𝒰 = B̂/R_nil(N)`, `N = ker(B → Q)`, `|Q| = 576`: a Galois commutator `h` on the
relative pro-2 part, the identity on every odd part, with conjugators from coprime centralizer lifts, CM pair
`(T_4, W_3) = (I, [i])`. LM7_PUSH E.58 (refereed: proved as claimed): for every open normal `U`, every positive
peripheral automorphism of `B̂/R_nil(U)` with three conjugators lifts to `B̂` with those conjugators. Prove or
refute: `α†` with its conjugators satisfies the hypotheses of that theorem for `U = N` (the three conjugators exist
in `𝒰` itself, compatibly at all primes), and its lift is an element of `GT̂₀` of multiplier one with the CM pair
`(I, [i])`. D.46 itself is not refereed: the item includes its proof. With it, D.19 (ii) for `GT̂₀` is proved by
D.46 and E.58, and the prompt asks for that proof written out. Independently of D.46, the same statement for the
pair `([5I], 1)` is E.58 itself: an element of `GT̂₀` in the coset that Galois misses exists.

**1.2 The two elements.** E.58's element is the identity on `B̂/R_nil(H)` (`H = F′F³`) with frame images
`([5I], 1)`; the lift of D.46 has `(I, [i])`. By E.65 (refereed) `Δ = 1` on the first. Compute `Δ` on the second,
the images of both in `G_6`, `G_2`, `G_3`, and prove or refute: their quotient lies in `ker Δ`; their quotient is
in the closed subgroup generated by `G_Q` and the elements that are the identity on `B̂/R_nil(F)`.

**1.3 The layers read against the theorem.** By E.58 the automorphism `α†|𝒰` lifts to `B̂`; so at every layer
`X/J_n` of D.47–D.65 some extension of it exists, after the changes of the lower representative that the tower
itself makes (D.61, D.63–D.65). Prove, for the residual of D.65, that the obstruction to extending vanishes modulo
those changes, and give the law of the residual dimensions (353,792; 331,776; 325,120; 284,160; 282,230; 276,478).
A layer at which every extension of `α†|𝒰` failed would contradict a refereed theorem: if the computation shows
one, the first thing to settle is whether `α†` is an automorphism of the whole `𝒰` with conjugators in `𝒰` (1.1).

**1.4 The excluded actions against the theorem.** D.32 and D.45 exclude recorded actions (the action on `B/D_9(F)`
has no multiplier-one lift to `B/D_10(F)`). Prove: each excluded action is not the restriction of a peripheral
automorphism of `B̂/R_nil(F)`, respectively of the relative completion on which it lives, and locate the central
layer that carries the obstruction, in the form the count of LM7_PUSH D.50 gives (the lifts to the finite central
extension `D†`).

**1.5 D.13.** The two statements (weight 5: dimension three for the full profinite special group; weight 9: the
vector `X²Y²(X+Y)³` reached by `GT̂₀`) are LM7_PUSH D.1 and D.2. Their lifting step D.50 is refereed; their other
inputs (LM7_PUSH D.20, D.21, D.51, D.52) are not. The tower's successor does not attack them again: it cites them
once that check exists (item S.6 of the LM7_PUSH successor). What the tower can add: prove or refute that the
weight-9 pair fails the pentagon for every lift (the tower's D.20–D.21 give the metabelian graded image of `GT̂`
through weight ten).

**Addition to 1.5 (debate round 2, Fermat participant, Claude Fable 5.2 at effort max).** LM6 A.10, A.49, A.56–A.59, A.66, A.67 (claims of GPT-6 Astra, ChatGPT Pro mode; statement level) give the Galois side of the metabelian group: peripheral outer automorphisms of the metabelian tripod group that commute with Galois beyond `𝔖_3`, none of which lifts to `F/F‴`. The successor cites them beside LM7_PUSH D.1, D.2 and proves how the two fit (item C.1 of `PUSH_ITEMS_LM7_CONTINUED.md`, state block of round 2).

**1.6 What is left of D.19: the full `GT̂`.** This is LM7_PUSH E.3, "is `Δ = 0` on `GT̂`" (refereed as the correct
reformulation). It belongs to the successor of LM7_PUSH. The tower's contribution to it: D.20, D.21 (the beta and
gamma compatibility of `GT̂`) evaluated on the CM coordinates; prove or refute that they force `Δ = 0`.

**Added by the Longue Marche expert (Claude Fable 5.2 at effort max, 14 November 2026); implications item 7; hunch H5.** Prove or refute: the tower's candidate D.46 and the element of LM7_PUSH E.58 differ by a Galois element at every level where both are defined. Their recorded pairs (`T₄ = I`, `W₃ = [i]` for D.46; the bits `(1, 0)` for E.58) differ by the Galois class `(1, 1)`, and both have `Δ = 1`. Then the arithmetic boundary of the residual of dimension 282,230 at which D.50–D.64 stand: prove that it vanishes for the candidate so corrected, or exhibit that it does not, which refutes LM7_PUSH E.58 or D.50. D.19 is then cited as "`Δ ≠ 0` on `GT̂₀`" (E.58), and D.13 as LM7_PUSH D.1 and D.2; the layer-by-layer construction is not continued.

### 1.B E.23: sections

**1.B.0 After the final return of LM6 (added 14 November 2026, 16:57 UTC, by the Fermat participant of the debate, Claude Fable 5.2 at effort max; reading: LM6 paper lines 11236–11620, the register rows E.1–E.5 and E.13–E.39; position paper `debate_20261114\POSITION_FERMAT.md`). Statements of LM6 are claims of GPT-6 Astra (ChatGPT Pro mode); "(mine)" marks the participant's own statements, checked by no one.**

*What is now answered.* The question of §51.16 for the full profinite group has an answer, LM6 E.12: for odd `n ≥ 3` every Selmer section of `U_n/Q` is cuspidal (E.6–E.11, read by the participant: holds as far as read), and with Tool (1) (the unrefereed local theorem of 6 October 2026) every section is Selmer, so the section set is the three cusp packets. The approximations do not see this: every pro-3 and pro-5 nilpotent quotient and the full profinite metabelian quotient carry families of non-cuspidal sections (LM6 E.16, E.31–E.34; this run's E.34; LM7_PUSH B.2). So items 1.7–1.11 describe approximations that are known to be far from the answer. They stay as stated, with these changes:

- **1.7** is LM6 E.21 (ii), open there. Unchanged.
- **1.8** is LM6 E.21 (i). Its state: the exact test (E18.1), the fibres (E18.3), the action class `[η]` with two Kummer coordinates `1/3` and `1/2` of `κ_3(3)` (E.36), an integral detector (E.37), a class liftable at every finite coefficient level and not continuously (E.38), the ambiguity `(F_3)³` (E.39). What is missing is one number, the elliptic component of `[η]` ("the Ross value") and its integral refinement: item 1.17 replaces "the missing input is the Frobenius action on ramified inputs".
- **1.9** (the quartic): LM6 E.13–E.17 are its state. Unchanged.
- **1.11** is LM6 E.21 (iii); E.31–E.34 give families in the full profinite metabelian quotient (`Z_3^{d_n}`, `Z_5^{d_n}`, `d_n = (n²−1)(n²+3)/4`). What remains of 1.11 is the complete set, and item 1.15's question whether those families are locally geometric.

*New items (the main ones of Part 1.B from now on, in this order).*

**1.13 Fermat for Selmer sections as one text, checked line by line.** Prove, with every cited theorem opened and its hypotheses verified at the place of use, LM6 E.6–E.12: for every odd `n ≥ 3` every Selmer section of `U_n/Q` is cuspidal. The points to verify, each to be confirmed or given as the exact error: (i) the definition of a Selmer section and of a local cuspidal section at 2 and at `ℓ`, as used in E.8; (ii) Stoll's Theorem 8.2 in the form with a set of places of density one, and the erratum to his Proposition 8.5; Harari–Stix Theorem 2.1; (iii) the Serre level and weight of the twisted mod-`ℓ` Legendre representation in every local case: a point with good reduction, with potentially multiplicative reduction (twist unramified or ramified, at `p ≠ ℓ`, at `ℓ`, at 2), and a cusp; the bound 16 on the level at 2; (iv) Khare–Wintenberger in the form used and the absence of forms of weight 2 and level dividing 16; (v) the lift to `Z_ℓ`, the map to `X_0(4ℓ)` and Stoll's Corollary 8.8; (vi) the exclusion of the point case by Mazur's theorem (a curve with `Z/2 ⊕ Z/2ℓ`); (vii) E.10 (the point of order 7 on `y² − xy − 4y = x³ − 4x²`; this is the member `d = 2` of the Tate normal form, discriminant `−1664`: confirmed by the participant by hand); (viii) exponent 3 through `X_3 ≅ X_0(27)`; (ix) composite `n`. Then isolate in one statement what E.12 takes from Tool (1): the exact local statement for the affine curve `U_n` over `Q_p` at every `p`, with its derivation from the proper case written out.

**1.14 The classical curves, every exponent.** Determine the Selmer section set of `x^n + y^n = z^n` minus `{xyz = 0}` over `Q` for every `n ≥ 3`, and prove it: for odd `n` it is 1.13; for `n = 4` through the elliptic quotient `v² = u⁴ + 1` (`u = x/y`, `v = z²/y²`; complex multiplication by `Z[i]`, finite Mordell–Weil group) with LM6 E.6; for `n = 2^k` through `U_n → U_4`; for even `n` with an odd prime factor through `U_n → U_ℓ`. The rational cusps are four for even `n` and three for odd `n`; the real place is to be treated (a real cusp carries more than one class). State the result also with Tool (1). (LM6 E.12's "no sections for even `n`" is about the plus curve.)

**1.15 The quotient that carries the theorem (mine; a hunch to prove or refute).** Let `ℓ ≥ 5`, `Π` the geometric fundamental group of `U_ℓ`, `K ⊂ Π` the kernel of the mod-`ℓ` Legendre representation (image `SL_2(F_ℓ)`), `R = ⋂_k K^{(k)}` its prosolvable residual. Call a section of `(Π/R) ⋊ G_Q` Selmer when each localization is the image of a local point or cusp section. Prove or refute: every Selmer section of `(Π/R) ⋊ G_Q` lies in the image of a cusp decomposition group. (Reason: the proof of E.6–E.9 uses the representation `ρ̄`, the cover `Z_ℓ`, whose group contains `K` with solvable quotient, and finite abelian descent on covers that are solvable over `Z_ℓ`.) For `n = 3` and for the classical `n = 4` prove or refute the same with `K = Π`, the maximal prosolvable quotient. Then decide the maximal prosolvable quotient of `U_5` and of `U_7`: every Selmer section cuspidal, or a non-cuspidal Selmer section. Then decide, for each family of LM6 E.16, E.31, E.33, E.34 and of this run's E.34, whether its members are Selmer in their quotient. Expected (mine): in `Π/Π^{(k)}` a Selmer section is cuspidal modulo the last layer `Π^{(k−1)}/Π^{(k)}`, and the families of E.31–E.34, whose abelianized class is that of a cusp, are of this kind.

**1.16 Twists: the rank-zero cases of the tripod (mine; a hunch to prove or refute).** For `(α, β)` in `(Q^×/Q^{×3})²` let `C_{α,β}` be the twist of the Fermat cubic that covers the tripod with group `μ_3²` and to which a tripod section with Kummer classes `(s^*κ(t), s^*κ(1−t)) ≡ (α, β)` lifts; `E_{α,β}` its Jacobian, with complex multiplication by `Z[ζ_3]`. Prove or refute: if `L(E_{α,β}, 1) ≠ 0`, then every Selmer section of the tripod over `Q` in the class `(α, β)` is the section of a rational point or of a cusp, and these are finitely many; list them. (Route: lift; Rubin's theorem gives finite `E(Q)` and finite Tate–Shafarevich group; Stoll; LM6 E.6. The case `α = β = 1` is E.11.) Prove the same for the `μ_4²`-covers through their three elliptic quotients (multiplication by `Z[i]`) and for `μ_6²`. Determine by program, for every class supported on the primes 2, 3, 5, 7, which of these criteria applies. Then prove or refute: a Selmer section of the tripod that is neither a point nor a cusp section has cubic, quartic and sextic twist classes of positive analytic rank in every finite étale neighbourhood that is again an open subcurve of a tripod. State what this leaves of LM6 B.27 and of ANABELIAN D.30 (finite ramification of the Legendre system).

**1.17 E.21 (i) without a 3-adic regulator at the additive prime (mine; a hunch).** The elliptic component of the class `[η]` of LM6 E.19 lies in a group of rank one, spanned by the étale realization of an element of `K_2` of `X_3 = X_0(27)` built from the units `f = 1 − x`, `h = y − 1` of E.35. Prove or refute: its coefficient is a rational number that can be read in the Hodge realization (iterated integrals of `f`, `h` on the cubic), and compute it there; determine the integral refinement, the ambiguity `(F_3)³` of E.39, by evaluating the class at Frobenius elements in the finite class-three quotient of order `3³⁰` of this run's E.38. With the value, state and prove the image of the class-three lifting map for every ramified class-two input (1.8).


**1.B.1 Added in debate round 2 (14 November 2026, 17:28 UTC, by the Fermat participant, Claude Fable 5.2 at effort max). Sources: `debate_20261114\UNSTUCK_POINCARE_FERMAT.md`, `UNSTUCK_LM_EXPERT.md` (both by Claude Fable 5.2 at effort max), `POSITION_CROSSRUN.md`, `POSITION_INTAKE.md` (Claude Fable 5.2 at effort high), the moonshine dictionary `research_maps_20261114\MOONSHINE_DICTIONARY\MOONSHINE_DICTIONARY_20261114.md` (Claude Fable 5.2 at effort high), item M4. Every statement below is a hunch of its source, checked by no one, to be proved or refuted.**

**Addition to 1.14 (dictionary M4 (b): the Gaussian case).** The Fermat quartic is the Gaussian counterpart of the cubic (triangle group (2,4,4) against (3,3,3)). Its Jacobian is isogenous to a product of three elliptic curves with complex multiplication by `Z[i]` or `Z[√−2]`. For each of the three quotients give the equation, the order of complex multiplication, the Mordell–Weil group over `Q` and the finiteness of the Tate–Shafarevich group, and prove through each one separately, with LM6 E.6, that every Selmer section of `x⁴ + y⁴ = z⁴` minus `{xyz = 0}` over `Q` is cuspidal. Then the same for the twists `a x⁴ + b y⁴ = c z⁴` whose quotients have analytic rank zero (the quartic half of 1.16).

**Addition to 1.15 (cross-run participant).** Determine the derived length at which the non-cuspidal classes stop: the least `k` such that every Selmer section of `Π/Π^{(k)}` is the image of a cuspidal section, for `n = 3` and for `n = 5`; or prove that there is no such `k` and give, for every `k`, the set of Selmer sections of `Π/Π^{(k)}` that are not images of cuspidal ones. LM6 E.33, E.34 are the state at `k = 2`.

**Addition to 1.2 (cross-run participant).** Evaluate on both elements (the element of LM7_PUSH E.58 and the lift of D.46) the tests of item (X4) of `POSITION_CROSSRUN.md` (the icosahedral tests of `POINCARE_AND_A5_20261114.md`), and prove what each value says about `Δ`.

**1.18 Where the ghosts die, on the twists of the cubic (the Poincaré/Fermat expert's path 3, with 1.16).** A ghost is a Selmer section that is not a point or cusp section. In a class `(α, β)` whose twist `E_{α,β}` has positive rank, the local points of a Selmer section form a profinite combination `n̂` of generators of `E_{α,β}(Q)`, `n̂ ∈ Ẑ^r`; a point has `n̂ ∈ Z^r`. Determine, for the twist of smallest conductor of rank one, the set of `n̂ ∈ Ẑ` that lift: (a) to the full profinite metabelian quotient of the punctured twist; (b) to the quotients over the genus-zero levels `X(3)`, `X(4)`, `X(5)` of the tripod (groups `A_4`, `S_4`, `A_5`), whose twists are rational curves; (c) to the level `X(7)`, whose twists are proper of genus 3 (Poonen–Schaefer–Stoll carried out descent on them). Prove at which of these levels every `n̂ ∉ Z` dies, or exhibit an `n̂ ∉ Z` that lifts through all of them. State the mechanism of the first level that kills a ghost supported at one extra prime, in a form that applies to every twist.

**1.19 The local theorem, prime by prime (the Longue Marche expert's path (i)–(iii), on the Fermat curves; mine for the consequence).** For a section `s` of `π_1(U_n) → G_Q`, odd `n`, with no Selmer hypothesis:
(i) prove that at each prime `q` and each `ℓ ≠ q`, if `s` is ramified at `q` in the pro-`ℓ` quotient, its localization there is one of the cuspidal families (LM7 E.61, E.66 for every `ℓ` and every `n`);
(ii) prove or refute that the cusp and the Kummer parameter at `q` are the same for all `ℓ ≠ q`;
(iii) determine exactly which local conditions used in LM6 E.8 (the conductor and flatness of the mod-`ℓ` Legendre representation at each `p`) and in the descent step of E.9 (local points at a set of places of density one) follow from (i), (ii) and from unramifiedness, and which need the local theorem of 6 October; then state and prove E.12 with the smallest local hypothesis. Expected (mine): what is left to that theorem is the `p`-primary condition at each `p`, and the condition at `ℓ` and at 2 for the Legendre representation.

**1.20 The phantom classes on the tripod (intake participant, `POSITION_INTAKE.md` 4.2).** State and prove the form of the classes of LM7 E.32 and LM6 E.38 for the class-two and class-three quotients of the tripod itself: a section class that lifts at every finite coefficient level and has no continuous lift. Prove or refute: a section of an approximation that carries such a class is not locally geometric at infinitely many primes, so that no Selmer section is a phantom.

**1.7 From `H` to the intrinsic quotients.** E.111, E.114, E.116 and E.122 compute the complete section sets of the
inherited quotient `H` on the Kummer lines of 17, of every inert `ℓ ≡ 2, 5 (9)`, and the tower at 53; each stops at
"the intrinsic metabelian and marked image through E.38". Prove one theorem: the image and every fibre of the map
from sections of the intrinsic metabelian quotient, and of the marked depth-two quotient, to sections of `H`, for
every first class. No further single prime is asked.

**1.8 The class-three map of the cubic.** The image and every fibre of
`Sect((N/γ_4N) ⋊ G_Q)/N → Sect((N/γ_3N) ⋊ G_Q)/N`, `N = π_1(U_{3,Q̄})^{(3)}`, for every input, with E.44 as the
criterion and the coefficient modules of ranks 20, 16, 4, 1 of the E.102 formula
(`LM7_FERMAT_TOWER_E102_check_20261113\FORMULA.md`); the missing input is the Frobenius action on ramified inputs.

**1.9 The quartic.** E.115 and E.117 give the complete class-two image at 5 and at 3 for `y² = x³ + x`, with
unbounded local Kummer orders and liftable inputs whose sum does not lift. Prove the law: the set of liftable
inputs as an explicit subset (not a subgroup), with the function of the local orders that cuts it out; and the same
statement for the cubic (E.32, E.37), as one theorem covering both.

**1.10 E.109 against the literature.** The Ceresa statement (the pro-5 class-two outer action of the quartic is
carried by a rank-two CM module whose class restricts over `Q(ζ_8)` to the Abel–Jacobi class of the Ceresa cycle):
prove or refute it with Hain–Matsumoto and Bisogno–Li–Litt–Srinivasan opened, and say what in it is new.

**1.11 The other primes and the full metabelian quotient** (A.5 of `PUSH_ITEMS_LM7_CONTINUED.md`, untouched by the
run): the section sets of `π̂/π̂″` for the full profinite group, beginning with the coefficient primes 2 and 5 for
the cubic.

**1.12 Register pointers (editing; added after the referee reports).** LM7_PUSH cites this run's D.25 as plain
"D.25", which collides with its own D.25 (both referees). In the successor's register and paper: every citation of
another run carries the run's name (LM7_PUSH D.1, D.2, D.50, E.58, E.65; LM4 D.32, D.34); this run's D.25
(`D_cm_shadow.tex`) keeps its number and is named "LM7 D.25" wherever a statement of this run is quoted beside
LM7_PUSH; the sentence of D.25 that its twelve selected shadows are removed by D.27 stays in the statement; and
D.13 and D.19 list the LM7_PUSH rows they now rest on, with the referee verdict for each. And the manuscript origin is named: the splittings behind LM7 D.25 and behind the frames of LM7_PUSH E.65 are those of cote 145, scans 22 and 28 to 29 (the canonical lifts of the isotropy groups at `P` and at the harmonic points `2, −1, 1/2`), with the corrected dictionary of `EXPERT_ON_INTAKE_11.md`: `(γ, χ)` of scan 11 is `(f, λ)` up to gauge, `g` is the cocycle `f⁻¹`, a frame is the conjugator by which an element moves such a splitting.

Items A.1–A.4 and A.6 of `PUSH_ITEMS_LM7_CONTINUED.md` stand. What is left of E.23 for points as sections is also
Task LM7-E.23 (i)–(iv) of LM6_POINTS_AS_SECTIONS, updated today: if LM6 is sent first, 1.7–1.9 are covered there and
this prompt keeps 1.1–1.6, 1.10–1.12.

**Update, 14 November 2026, 16:57 UTC (Fermat participant, Claude Fable 5.2 at effort max).** LM6 has returned (final, 16:13 UTC; register 225 rows). It did not cover 1.7–1.9: its row E.21 leaves them open, with the state given in 1.B.0. The successor of the Fermat tower therefore keeps all of Part 1.B, led by the new items 1.13–1.17; 1.7–1.11 come after them.

---

## Part 2. Successor of LM4 (§§12–18, 23–25 bis, 31)

None of the three open rows closed in the last 82 rows. The new prompt asks for the three, each by its one
remaining statement, and for nothing case by case.

**2.1 C.12, the noncompact quotient.** State of the run: for a closed discrete free proper operator group `Q` on
the open disk with compact quotient, the boundary-fixed centralizer is contractible (C.90, C.91). For an arbitrary
quotient `N`, the point stabilizer is the group of those `b` in the pointed identity component of `Homeo(N rel p)`
whose lift has displacement in `C_0(N)` (C.88, C.92), and continuity on a compact parameter space is the
uniform-tail condition (C.92.17). Prove or refute: every compact family in that group deforms to the identity with
a uniform tail (then the level-zero comparison has no kernel for discrete operator groups); a refutation is a
discrete operator group with noncompact quotient and a loop of the centralizer that is not null-homotopic, built
for instance from the sequence (C.92.18)–(C.92.21). Then the remaining frontier comparisons of C.12, as the run
lists them.

**2.2 D.12, the torus.** (a) `K = 1` in D.78 (`B = K ⋊ Ẑ`, `K` pro-odd), equivalently the surjectivity of
`Q_X^B → Q_X^A` for every finite `E`-set `X`. (b) The conjugacy (D.75.5) for negative involutions of the punctured
torus. (c) The scalar cubic case: an element of order three of the torus group whose multiplier is a primitive
cube root of unity at some primes: construct it or exclude it (D.71, D.73).

**2.3 D.12, the three-cusp group: the conjugacy of the involutions.** By D.32 and D.34 (refereed: proved as
claimed) every non-trivial element of finite order of the pure three-cusp group, of `GT̂₀` and of `GT̂` is an
involution with multiplier `−1` at every prime. What is open is whether each is conjugate to complex conjugation:
the conjugacy part of the question of Lochak and Schneps, which the referee of D.32 found still listed as open
(Schneps' survey, §1.4 (4); Lochak–Schneps, "Open problems", 1.4). Prove or refute it, in the pure group, in `GT̂₀`
and in `GT̂`. D.34 gives `h ∈ F′` with `f = h⁻¹α(h)` and `ψ : x ↦ x, y ↦ hyh⁻¹` an automorphism of every `F^(p)`
with `α = ψcψ⁻¹` there; the lifting theorem of LM7_PUSH (D.50, E.58: refereed) lifts a peripheral automorphism of
`F/R_nil(F)` with its conjugators to `F`. So: prove or refute that `ψ` is peripheral on `F/R_nil(F)` (it sends `z`
to a conjugate of `z`), take its lift `ψ̃`, and decide whether `ψ̃cψ̃⁻¹` and `α`, which agree on `F/R_nil(F)`, are
conjugate; the equation (D.74.40) at the third cusp with the unique coboundary of D.35 is the same question in the
run's own terms. The generation form (cote 145, scan 23: for complex conjugation the extension is `C_2 * C_2 * C_2` on `τ_0, τ_1, τ_∞` with `l_0 = τ_∞τ_1`, `l_1 = τ_0τ_∞`, `l_∞ = τ_1τ_0`; confirmed by the Longue Marche expert, Claude Fable 5.2 at effort max): prove or refute that an involution `α` of the pure group is conjugate to complex conjugation exactly when its three section classes contain involutions `t_0, t_1, t_∞` whose products are generators of the three inertia groups and which generate `F ⋊_α C_2`. The test case is the glued involution (complex conjugation on one side, a conjugate of it on the other; the expert's hunch, LM8_PUSH Lead 23): prove or refute that it exists; if it does it has `Δ = 1`, so it is not conjugate to complex conjugation in `GT̂₀`, and whether it is conjugate in the pure group is whether its three lifts generate (LM4 D.76, D.77).

**2.3 bis The same question level by level (the cross-run participant of the debate of 14 November 2026, Claude Fable 5.2 at effort high; checked by no one).** (a) Prove or refute: `𝒫 = lim_U Out^♯(F/R_nil(U))` over the open characteristic subgroups `U` of `F` (the maps are onto by LM7_PUSH E.58, refereed, with the Galois elements for the multipliers; `⋂_U R_nil(U) = 1`). Then two involutions of `𝒫` are conjugate exactly when their images are conjugate at every level, and an involution of `𝒫` is a compatible family of involutions of the levels. (b) Each level is the fibre product over `F/U` of the groups `F/O^p(U)`. Determine the involutions of `Out^♯(F/O^p(U))` over the class of complex conjugation for every `p`: for odd `p` prove that two with the same image on `F/U′U^p` are conjugate; at `p = 2` compute the classes. Then the gluing: the classes of involutions of the level `U` whose components are conjugate to those of `c`, as a double coset space of centralizers over `F/U`. Carry this out for `U = F′F³` and for `U₁₂`, the kernel of the map of `F` to `SL₂(Z/12)/±1` on which `Δ` is read. (c) Decide whether a glued class of (b) with `Δ = 1` extends to a compatible family over every smaller `U`: that is the existence of the glued involution of 2.3, and it decides 2.3 in `GT̂₀`. (d) D.77 shows that fullness in every `F^(p)` does not give generation; the levels `U ≠ F` are where generation is decided. Prove or refute: the three section representatives of an involution `α` generate `F ⋊_α C₂` exactly when their images generate at every level.

**2.4 F.7.** F.24–F.32 settle the comparison of the two sides in affine groups `Aff_1(k)` on the whole product-one
character locus (F.31) and on the locus where the first character is one and the boundary character is not (F.32).
These are metabelian tests and cannot prove the equality. Prove or refute the equality
`C_{M̂}(A_5) = closure of C_M(A_5)` itself: either the closure–intersection equality that the run could not justify
in Boggi, Theorem C(iii), and in its "R-BZ", Theorem 5.1(iii) (with both papers opened and the step quoted), or a
finite quotient that separates the two sides, which by F.31 and F.32 cannot be of that affine kind on those loci.
On our side first: a reading of the two cited proofs (Claude Opus 5.5 at effort max), because a gap there is a
correction to published work. **Done 14 November 2026, ~11:3x UTC** (main session, Claude Opus 5.5 at effort max; NOTE_BOGGI_ZALESSKII_STEP.md):
the step is the conclusion restated, since ⋂ closure(Z(x_i)) is already Z_Ĝ(H) by the two correct equalities before
it. The solvable case follows from the normalizer equality (Z is open in N). In genus ≤ 2 the only open case is an
icosahedral `A_5` in genus 0. The item therefore starts at its smallest case: prove or refute that the centralizer of
the icosahedral `A_5` in the profinite mapping class group of the sphere with the 12 icosahedron vertices punctured is
finite (its discrete centralizer is finite: the quotient is the (2,3,5) orbifold with the order-5 point punctured).
Equivalent criterion: for every torsion-free congruence level `Γ_n`, every complement to `Γ_n` in `Γ_n·A_5` that is
conjugate to `A_5` by an element of `Γ̂_n` is conjugate to it by an element of `Γ_n`. Then do every `n`. Also decide
Boggi's Theorem A in the ramified nonsolvable case, whose Lemma 3.2 uses the same proposition. **Expected direction (user, 14 November 2026): refute.**
Our hunch is that the statement fails for the icosahedral `A_5`. Its quotient is the rigid (2,3,∞) triangle orbifold,
and every inertia-preserving symmetry of the profinite triangle-orbifold group (e.g. GT̂ elements (1, f)) lifts through
the icosahedral dessin to an outer automorphism of the profinite fundamental group of the 12-punctured sphere that
commutes with `A_5`. Decide whether any such lift, or any other element commuting with `A_5`, is a limit of mapping
classes of the 12-punctured sphere outside the finite discrete centralizer. Galois elements appear not to be.
State the result either way: a counterexample with its proof, or a proof that the profinite centralizer is finite.
**The conjecture to decide, in its refined form** (user, 14 November 2026; NOTE_BOGGI_ZALESSKII_STEP.md, section
"Conjecture 2⁻, refined"; the test of EXPERT_ON_BOGGI_A5.md (c) by the Longue Marche expert, Claude Fable 5.2 at effort
max). Let G ≤ `Γ_{0,n}` be a finite subgroup whose quotient, with the punctures taken as cusps, is a triangle
orbifold, so that the configuration is an isolated orbifold point of the moduli space. Prove or refute: the centralizer
of G in the profinite completion equals the closure of its discrete centralizer if and only if G is solvable.
- The solvable direction holds by the normalizer route; prove it in this form.
- The content is the icosahedral `A_5`, the one case over (2,3,5) whose spherical Seifert manifold S³/2I, the Poincaré
  sphere, is a homology sphere. Our conjecture is that there the profinite centralizer is infinite.
- Smallest instance: X(5), the sphere punctured at the 12 vertices, with deck group `PSL_2(F_5)`. The candidates are
  the lifts of the elements F of GT̂_0 with λ(F) ≡ ±1 mod 5.
- If a counterexample is found, compute Δ (LM7_PUSH E.65) on it.

**Added by the Poincaré read-in (Claude Fable 5.2 at effort max, 14 November 2026).** Source:
`research_maps_20261112\PRETOT_3D_MODULARITY\POINCARE_AND_A5_20261114.md` (attach it). Each statement below is to be
proved or refuted. Basis marks: [P] proved by Claude Fable 5.2 at effort max in that file and checked by no one;
[S] checked there against a cited source; [H] a hunch. Notation: `B = C_2 * C_3 = ⟨s, r⟩`, `τ = sr`,
`K = Γ(5)/±1`, `ℋ` the multiplier-one part of `GT̂_0`, `𝒦 = {F ∈ ℋ : F restricted to K̂ lies in Γ̂_{0,[12]}}` (the
profinite centralizer of `A_5` up to its finite discrete part), `x_0` the icosahedral configuration.
- (R1) [P] The four groups over `x_0`. The inverse image of the icosahedral `A_5` is: `2I` in the sphere braid group
  `B_12(S²)`, where it is `π_1` of the orbit `SO(3)·x_0 = Σ(2,3,5)`; `C_2 * C_3` in `Γ_{0,[12],1}` (one more,
  distinguished, puncture); and a copy of `B_3` in the Artin braid group `B_12`, generated by periodic braids
  `β_3, β_2` conjugate to `δ⁴, δ⁶` with `β_3³ = β_2² = Δ²`, which is `π_1` of the orbit minus its Seifert fibre of
  order 5 (the trefoil complement). The sphere relation of `B_12 → B_12(S²)` restricts on this `B_3` to the filling
  slope `μ⁵ = z`. Give explicit braid words for `β_2, β_3` and a machine check of every relation and of the order 120.
- (R2) [P] `𝒦` is the group of outer automorphisms of `B̂` induced by conjugation with elements of the normalizer of
  `B̂` in `Γ̂_{0,[12],1}`. With the frames of LM7_PUSH E.65 (`Φ_F(s) = β_F s β_F⁻¹`, `Φ_F(r) = A_F r A_F⁻¹`,
  `Φ_F(τ) = τ`): `F ∈ 𝒦` exactly when `C(τ) ∩ β_F·C(s) ∩ A_F·C(r)` is not empty, the centralizers taken in
  `Γ̂_{0,[12],1}`.
- (R3) [P] Tripod tests. For every three vertices, `F` induces an outer automorphism `𝔗_t(F)` of the profinite group
  of `X(5)` minus those three points. For `F ∈ 𝒦` it is trivial; for a Galois element fixing `Q(ζ_5)` it is that
  element. Hence `𝒦 ∩ G_Q = 1` by Belyi's theorem.
- (R4) [P; part (c) uses the solvable direction above] The quintic resolvent endomorphism. Let `Γ_T ⊂ B` be the
  inverse image of `A_4 ⊂ A_5` (index 5, `Γ_T = C_2 * C_3 * C_3′`, one cusp; a model is `j = t³(t² + 5t + 40)`, with
  `j − 1728 = (t − 3)(t² + 4t + 24)²`, the two points of order 3 conjugate over `Q(√−15)`), and identify
  `Γ_T/⟨⟨C_3′⟩⟩` with `B`, cusp to cusp. Restriction to `Γ̂_T` followed by this quotient defines
  `𝔗_T : {F ∈ GT̂_0 : (−15/λ(F)) = 1} → GT̂_0` (Kronecker symbol; the domain has index 2 and contains `ℋ`; it is the
  set of `F` that keep each of the two points of order 3). (a) It is a continuous homomorphism preserving `λ`.
  (b) It is the identity on the Galois group of `Q(√−15)`. (c) `𝒦 ⊂ ker 𝔗_T`, and likewise for the two maps `𝔗_T′`,
  `𝔗_T″` that forget the other point of order 3 and the point of order 2. So `𝒦` meets `{F : 𝔗_T(F) = F}` trivially.
- (R5) [H] `𝔗_T` is not the identity on `GT̂_0`: exhibit `F` with `𝔗_T(F) ≠ F` through LM7_PUSH D.50 and E.58. (If
  instead `𝔗_T` is the identity, (R4)(c) gives `𝒦 = 1` and the centralizer is finite.)
- (R6) [open] Every element of `GT̂` with `(−15/λ) = 1` satisfies `𝔗_T(F) = F`. It holds on Galois elements by
  (R4)(b). State its relation to relations (III′) and (IV) of Nakamura–Schneps (Invent. Math. 141 (2000)) and to the
  subgroups BGT of Hoshi–Mochizuki–Tsujimura (J. Math. Sci. Univ. Tokyo 32 (2025)).
- (R7) [H] `ker 𝔗_T ∩ ker 𝔗_T′ ∩ ker 𝔗_T″ = 𝒦`. The inclusion `⊇` is (R4)(c). Its graded form: in the Lie algebra of
  special derivations of the sphere with four punctures modulo inner derivations, the common kernel of the four maps
  to the three-punctured spheres is the braid Lie algebra (free on two generators), in every weight. Decide the
  graded form, then the profinite statement.
- (R8) [open; this is the decision] The common kernel of (R7) is trivial, or it contains a non-trivial element,
  written out. With (R7) the first gives the finite centralizer and the second gives Conjecture 2⁻.
- (R9) [P, with LM7_PUSH E.58] For every prime `ℓ ∤ 60` the `A_5`-invariant elements of the pro-`ℓ` pure sphere braid
  group on 12 strands form an infinite group (rank 2 in degree 1), and each of them is the pro-`ℓ` shadow of an
  element of `ℋ`. So no pro-`ℓ`, pronilpotent or metabelian quotient separates the two sides, and a proof of the
  finite centralizer has to use quotients in which the primes 2, 3, 5 and others mix. Decide whether the lifting
  theorem can be carried out inside the braid group: for an invariant pro-`ℓ` braid, an element of `ℋ` with that
  shadow whose restriction to `K̂` lies in `Γ̂_{0,[12]}`.
- (R10) [P for N = 3, 4 on the solvable direction; open for N ≥ 5] The same structure at every level. Put
  `𝒦_N = {F ∈ ℋ : F restricted to the completion of Γ(N)/±1 lies in the profinite mapping class group of Y(N)}`.
  Then `𝒦_3 = 𝒦_4 = 1` (tetrahedron and octahedron: there the centralizer among cusp-preserving outer automorphisms
  is also infinite, `{F ∈ GT̂_0 : λ ≡ ±1 mod N}`, and the centralizer in the profinite mapping class group is finite).
  Decide `𝒦_N` for every `N`; `N = 5` is the item above, `N = 7` is the Klein quartic (Boggi, Theorem A, ramified
  case). This tests whether the dividing line of the refined conjecture, solvable against perfect, is a property of
  the proof or of the statement.
- (R11) [P] If `𝒦 ≠ 1` and its elements lift along the icosahedral special loci with further orbits of marked points
  (a question about `H¹(A_5, ·)` of the same kind as the conjecture), then they satisfy the pentagon, and
  `GT̂ ≠ G_Q` by (R3). Prove the implication and decide the lifting.
- (R12) [S] For the record of the hunch behind the item: the presentation complex of
  `⟨a, b | a⁵b⁻³, b³(ab)⁻²⟩` is the spine of the trefoil complement with one 2-cell on the slope `μ⁵z⁻¹`, hence
  homotopy equivalent to `Σ(2,3,5)` minus a ball without Nicholson's theorem (Kirby–Scharlemann, *Eight faces of the
  Poincaré homology 3-sphere*, Descriptions 6–8, pp. 118–122). No invariant of `Σ`, of `2I` or of that complex
  varies with `F`: every `F` with `λ ≡ ±1 mod 5` acts trivially on `2I`. The object that carries the question is
  the trefoil complement inside `Σ`.

**Added by the cross-run participant of the debate of 14 November 2026 (Claude Fable 5.2 at effort high; own reading, checked by no one).**
- (X0) State of the run: the newest snapshot is `answers\LM4_FINITE_GROUP_ACTIONS_20261114T0406Z_unzipped` (272 rows). F.33 is one more affine locus (opposite first characters); C.12, D.12, F.7 stand.
- (X1) What does not rest on the step. LM6_POINTS_AS_SECTIONS C.16 and C.17 apply Boggi–Zalesskii, Theorem A, "for the prime two", to a single involution of a good group (its paper, lines 9459–9466 and 9694–9697; the same at line 8546 for the real sections). That is the element case, which the step takes as its input; it is not the step. LM7_PUSH E.64 cites Boggi for the hyperelliptic involution, again one element of order two. So the real structures of LM6 Part C and the hyperelliptic quotient of E.64 stand or fall with Theorem A, which nobody on our side has read, and not with Proposition 2.4. Read Theorem A (i)–(iii) with its proof, and prove or refute this division.
- (X2) What does rest on it in our own files: only statements about nonsolvable finite subgroups. In genus at most two these are the icosahedral groups in genus zero; in the stable tower the first is `PSL₂(F₇)` at the Klein quartic (EXIT_TOWER, Part E (a), now says so).
- (X3) `𝒦` is normalized by the Galois group of `Q(√5)` inside `GT̂₀` (it is `ℋ ∩ Γ̂_{0,[12]}`, and both are stable), and `𝒦 ∩ G_Q = 1` (R3). It is a closed subgroup of the geometric group of the curve of `A₄`-symmetric configurations, stable under the Galois action at the icosahedral point. Prove or refute: `𝒦` has no non-trivial closed procyclic subgroup that is normalized by an open subgroup of that Galois group and has non-trivial components at all but finitely many primes (the statement of LM6 A.52 for that curve). It limits the shape of a counterexample: `𝒦` is not `Ẑ`.
- (X4) The two explicit elements. Compute the tripod tests (R3) and the maps `𝔗_T`, `𝔗_T′`, `𝔗_T″` (R4) on the element of LM7_PUSH E.58 and on the lift of the Fermat tower's D.46 (item 1.1), and decide for each whether it lies in `𝒦`, in the common kernel of (R7), or in neither. These are the only elements of `ℋ` outside the Galois image that have been written down.
- (X5) By 2.3 bis (a), `F ∈ 𝒦` is a condition at every level. Determine, for `U = K` at every prime (R9 gives the primes not dividing 60) and for `U = K′K^p`, `p = 2, 3, 5`, the image of `ℋ` and the image of the closure of the braids that commute with `A₅` in `Out^♯(K̂/R_nil(U))`, and their intersection.

**Added in round 2 of the debate (14 November 2026): routes for 2.4 from the Poincaré read-in (Claude Fable 5.2 at effort max; `debate_20261114\UNSTUCK_POINCARE_FERMAT.md`, section 4) and from the moonshine dictionary (Claude Fable 5.2 at effort high; `research_maps_20261114\MOONSHINE_DICTIONARY\MOONSHINE_DICTIONARY_20261114.md`, sections 3, 4.2, 4.3). Hunches and unchecked arguments: each statement is to be proved or refuted. Attach both files.**
- (S1) The sub-configuration lever. Let `Q` be a subset of the twelve vertices stable under a cyclic subgroup `H` of `A₅` such that the sphere punctured at `Q`, divided by `H`, is a triangle orbifold: a pentagon; a vertex with its pentagon; an antipodal pair with one pentagon. Prove: the elements of `𝒦` fix every puncture; the image of an element of `𝒦` in the completed mapping class group of the sphere punctured at `Q` commutes with `H`, lies in a finite centralizer (the cyclic case of the centralizer theorem, which is not in doubt) and is pure, hence trivial. So `𝒦` lies in the intersection of the kernels of all these forgetful maps and of those of (R3), (R4). Compute that intersection inside the free group `F_T ∩ P` of rank 13 (the pure part of the centralizer of `A₄`), discretely and then in the completion. If the profinite intersection is trivial, the centralizer of `A₅` is finite and Conjecture 2⁻ is refuted.
- (S2) The cross-ratio form. The curves of `A₄`-symmetric and of `C₅`-symmetric configurations are tripods `C_T`, `C_5`; each four-subset `q` of the vertices gives maps `ψ_q : C_T → M_{0,4}`, `φ_q : C_5 → M_{0,4}`. An element of `𝒦` is a pair `(γ_T, γ_5)` in the completed groups with `ψ_{q*}(γ_T) = φ_{q*}(γ_5)` for all 495 subsets; where `φ_q` is constant this reads `γ_T ∈ ker ψ_{q*}`. Write the 495 pairs of maps and determine the set of solutions.
- (S3) The arithmetic model (the dictionary's facts on the lattice are from memory: open Deligne–Mostow, Thurston's *Shapes of polyhedra* and Allcock). `Γ_{0,[12]}` maps onto an arithmetic lattice `Γ_DM` in `PU(1, 9)` over `Z[ω]`, the half-twists going to elements of order three. Prove or refute: (a) under `A₅` the space `C^{1,9}` is a line plus the irreducible representations of dimensions 4 and 5, so the centralizer of `A₅` in the unitary group is, modulo scalars, a torus `T` of rank two that is compact at the real place and meets `Γ_DM` in a finite group; give `T` and its field of definition; (b) in the closure of `Γ_DM` in `PU(Λ ⊗ Ẑ)` the centralizer of the image of `A₅` is infinite, so that in this congruence quotient the centralizer is larger than the closure of the discrete one; the same at 4 points with weights 1/2 and at 6 points with weights 1/3; (c) for each prime `ℓ` not dividing 30, determine which elements of `T(Z_ℓ)` are images of elements of the centralizer of `A₅` in `Γ̂_{0,[12]}`: compute the obstruction class in `H¹(A₅, ·)` with coefficients in the kernel of `Γ̂_{0,[12]} → PU(Λ ⊗ Z_ℓ)`; carry out the same computation at 4 and at 6 points, where the centralizer in the full completion is finite (Herfort–Ribes; the solvable case), locate the step that makes it finite there, and decide whether that step is present at 12 points.
- (S4) The icosahedral characters. Every `F ∈ GT̂₀` with `λ(F) ≡ ±1 mod 5` acts on the `ω`-part of `H₁` of the cyclic cover of degree six of the sphere branched at the twelve cusps, through the centralizer of `A₅`: three characters `χ₁, χ₄, χ₅` with values in the units of `Ẑ[ω]`. Prove or refute: that cover is the fibre product of `X(5)` with the curve of the commutator subgroup of `B`, of level 30; the three maps are continuous homomorphisms; on the Galois group of `Q(ζ₁₅)` they are Jacobi-sum Hecke characters; and compute them on the multiplier-one elements that LM7_PUSH E.58 gives for `U = Γ(5)/±1` and for `U` the subgroup of level 30. They are the analogue at the icosahedral point of the pair `(T, W)` at the harmonic and equianharmonic points. Decide whether they vanish on `𝒦`: a non-trivial value on an element of `𝒦`, written out, proves Conjecture 2⁻; if they vanish, treat in the same way the two-dimensional representations of `Γ_{0,12}` of the dictionary's rows 13 and 14 (the Fibonacci representations).
- (S5) Levels 7 and 11. The map `𝔗_T` of (R4) has siblings at `p = 7` and `p = 11` (the index-`p` subgroups of `PSL₂(F_p)`); the family is task C.10 of LM8_PUSH. Here: (R10) for `N = 7` (the Klein quartic; Boggi, Theorem A, ramified case) with the map at 7, and for `N = 11` with the map at 11, whose finite group is again an `A₅`, inside `PSL₂(F₁₁)`.
- (S6) One more citation for the division of (X1), (X2) (from the intake participant): ANABELIAN_149_PUSH A.29l rests on Boggi–Zalesskii 2019, Lemma 3.1, on finite subgroups of completions of orbifold groups. Read it with Theorem A.
- For the record of the hunch, neither being an argument (the dictionary, S1 and S7): in the umbral table of lattices `A_{ℓ−1}^d` the relation `(ℓ − 1)(p + 1) = 24` has `ℓ = p` only at 5; and twelve points of equal weight is the last case of Thurston's list.

**Added 14 November 2026, ~18:3x UTC, from the ghost-symmetries translation (Claude Fable 5.2 at effort high; `research_maps_20261114\MOONSHINE_DICTIONARY\GHOST_SYMMETRIES_TRANSLATION_20261114.md`, section 3.3, item GS3; placed verbatim by the main session):**
- (G1) `𝒦`: abelian, procyclic, cuspidal. Prove or refute: (a) closure(F_T) is free profinite of rank 2 and 𝒦 is a closed subgroup normalised by an open subgroup of the Galois group of the field of definition of the icosahedral point; (b) [𝒦, 𝒦] is trivial; (c) if 𝒦 is abelian it is ∏_{p∈S} ℤ_p with a character ψ, and ψ is neither cyclotomic nor of the weight of a complex-multiplication character, hence 𝒦 = 1; (d) if (b) fails, exhibit two non-commuting elements. Background: `POINCARE_AND_A5_20261114.md`, `EXPERT_ON_BOGGI_A5.md`, `UNSTUCK_POINCARE_FERMAT.md` §4, LM8 G.10, G.19, G.20 and LM8_PUSH Part A.

**2.5 The character `Δ` on torsion.** `Δ` of LM7_PUSH E.65 (refereed) is a conjugation-invariant character of `GT̂₀`
that vanishes on `G_Q`. For an involution `τ = (−1, f_τ)` of `GT̂₀`: `Δ(τ) = δ((1, f_τ))` (referee of D.34). Prove
or refute: `δ((1, f)) = 0` for every `f` such that `(−1, f)` is an involution of `GT̂₀`. It follows from 2.3; an
involution with `Δ = 1` refutes 2.3 in `GT̂₀`. The referee found no cheap constraint: the dihedral relation with
complex conjugation puts no condition on `δ`. (Also task B.4 of LM8_PUSH.)

**2.6 The census against cote 148.** The run's census of finite subgroups (B.23–B.41) in type (0,5), with its
reflection rows B.4, B.5, set beside Grothendieck's own classification on cote 148, scans 34–36 ("Systèmes spéciaux
de cinq points sur une sphère complexe": largest order `2 ≤ ν ≤ 5`, the pentagonal case with `𝔻₅`, the real
structures by the number of fixed marked points) and his counts of scans 31–33 (542 objects in 9 orbits, 1620
arrows in 14 orbits): prove or correct each of his statements and counts from the census. Attach
`returns\MPL_148_029-072_unzipped` (transcription, notes, doubts; first pass, no second pass).

**2.7 What is refereed in LM4 and what is not.** D.32 and D.34 are refereed (proved as claimed); they answer tasks
B.3 and B.4 of LM8_PUSH and are cited there as results. D.42 (order three has multiplier 1, with the permutations
of the punctures) and D.70 (order four in the torus group) are cited beside them and are not refereed: they are
the next rows of LM4 to referee, with D.74–D.78 and the rows of Part C that C.12 rests on (C.88, C.90–C.92).

**2.8 Register pointers and statements (editing; added after the referee reports).** In the successor's register
and paper: D.28 is stated for the pure three-cusp group `P` (its register statement is for `GT_0` only, and D.32
uses it for `P`; the referee checked that its proof holds there, which the register does not record); the circular
citation between D.25 and D.32 is cut (D.32 does not need D.25); A.7 cites Herfort–Ribes 1985, Theorem B′, for the
centralizer and normalizer statements on `F̂_2` and `F^{(p)}`; and every citation of another run carries the run's
name (LM7_PUSH D.50, E.58, E.65; LM7 D.25).

**2.9 Real structures in genus three (from LM6_POINTS_AS_SECTIONS, final return of 14 November 2026, C.12–C.19; statement level, no proof read by a reviewer).** LM6 claims the injectivity of the real types into the completed groups (C.13), the fibre formula `C_Q(τ̄)\H¹(C₂, K)` with `K` the kernel of the full completion onto the procongruence completion (C.15), and `C_P(τ) = K^τ ⋊ closure(C_Γ(τ))` for the five types of genus three with an oval (C.17). Open there (its C.12): `K^τ`, `H¹(C₂, K)`, and the fixed-point-free type (through `Mod(N₄)`, C.18, C.19). Prove or refute each of C.13–C.19. Then determine `K^τ` and `H¹(C₂, K)` for the six real types of genus three, and with them all involutions over complex conjugation in the full profinite extended mapping class group of genus three, with their centralizers. These rows use Boggi–Zalesskii, Theorem A, at the prime two only ((X1) of 2.4).
