# Review of the return EXIT_ONE_TYPE, 13 November 2026

Reviewer: Claude Fable 5.2 (Anthropic), effort max, no sub-agents, 13 November 2026, 04:42–05:25 WEST.
Return: GPT-6 Astra (OpenAI, ChatGPT Pro mode), final delivery of 13 November 2026, 00:06 UTC, marked INCOMPLETE by
itself; 63 statements (53 Proved, 8 Refuted, 1 Known, 1 Open by its own labels). Unpacked at
`longue_marche_pro_pilot_20261104\answers\EXIT_ONE_TYPE_final_20261113T0013Z_unzipped\EXIT_ONE_TYPE\`.

## What was read

- The return: `sections\conventions.tex`, `criterion.tex`, `examples.tex`, `cusp.tex`, `boundary.tex`, `levels.tex`,
  `compactifications.tex` in full (every statement and every proof); `EXIT_ONE_TYPE_results.csv` (all 63 rows);
  the first 64 lines of `EXIT_ONE_TYPE_report.md`; `notes\source_inspection.md`; the bibliography entries of Miller
  and Jansen. Not read: the rest of the report, the readings CSV, `notes\*.md` other than named, the PDF, the
  validation logs. The return's programs were not read and not run: every computation below is my own.
- The prompt `pro_prompts_archive_20261112\EXIT_ONE_TYPE\PROMPT.md` in full; `EXIT_ONE_TYPE_EARLY_SHAPE_20261112.md`
  and `EXIT_ONE_TYPE\CHECKPOINT_DIFF_20261112.md`. The earlier checkpoints named in the diff were not opened: this
  review is of the final delivery only.
- Sources opened for the citations:
  - **Miller 2009** (J. Homotopy Relat. Struct. 4(1), 265–273): the published PDF, text extracted and read by me
    (Definitions 2.3–2.8, 4.6, Theorem 4.9 with the opening of its proof).
  - **Jansen 2023** (arXiv:2308.09551v2) and **Jansen 2024** (arXiv:2308.09550v3): the arXiv HTML pages, read
    through the fetch tool, which returns a paraphrase of the page made by a small model, with short quotations.
    The numbers, types and contents of the items below are from those paraphrases, not from the page text in my
    own context.
  - **Readdy 2005** (arXiv:math/0511420): a search summary only (it states Theorem 4.7 as the wedge of (n−2)!
    spheres of dimension n−4).
- Our own notes on Δ₀,₆ (`s6_pro_prompts_20261112_work\reviews\LEECH_Z24_QUESTION_20261113.md`, head; the head of
  `LEECH_Z24_CONSULT_20261113.md`): f-vector (25, 105, 105), H₂ ≅ Z²⁴, and 24 = b₃(M₀,₆).
- For the two blocks: `EXIT_TOWER\PROMPT.md`, lines 5–29 and 50–86 (the statements, the leads, the parts);
  `LM5_MULTI_GALOIS_TOPOI\PROMPT.md`, lines 74–106 and 166–180 (the block on cotes 149 and 147, Part F). The rows
  of CYCLOTOMIC_KERNEL and FLAGGED_149 named in task 6 of the LM5 block are taken from the early-shape note; I did
  not open those returns. Both blocks pass `push_rule_pro_prompts.py --lint`.
- No scan image was opened. The return's decisions on readings were not checked.
- No other source cited by the return was opened (Harer 1988, Ueda 1979, Svaldi 2019, Kato 1989, Payne 2013,
  Thuillier, AKMW, Harper, Chan–Galatius–Payne, Włodarczyk, Adiprasito–Pak, Durfee–Saito, Tubach, SGA 1 XII).
  Where a verdict rests on one of them the table says "source not opened".

## Programs

`checks\own_checks.py` (Python 3.13.9, standard library only; output `checks\own_checks.out`, all 19 lines PASS),
written from the paper's statements:
- the 6 relations of P5c2 and the 20 mixed relations of P5c3, tested as equalities of braids in B₅ by the Artin
  representation on F₅ (faithful): all 26 hold as stated; read in the reverse order 19 of them fail, so the
  convention matters and the return's is consistent;
- the centre of P₄ and of P₅, and that the centre of P₄ is not central in B₅ (the splitting Γ₀,₆ = F₄ ⋊ Γ₀,₅ goes
  through the complement ⟨a, b, x, y, z⟩ of Z(P₄), as the return has it);
- Δ₀,ₙ for n = 4, 5, 6: f-vectors (3), (10, 15), (25, 105, 105); reduced Betti numbers 2, 6, 24 in the top degree
  and zero elsewhere; every elementary divisor of every boundary matrix is 1 (own Smith reduction);
- P4a1: the orbit count (the fibre of π₀D₃₂₁ → π₀D₃₂ ×_{π₀D₂} π₀D₂₁ over the chosen pair has 2 elements);
- P5a1: the hexagon (6, 6, 0) and its cone (7, 12, 6); P1b2: the kernel (1, −1);
- the cusp: a² = b³ = h and the kernels (−3, 1), (−2, 1) in a faithful image of ⟨a, b | a² = b³⟩ in SL₂(Z) × Z;
  m = ab⁻¹ maps to a parabolic matrix; the relations of G_pr in Z² ⋊ Z;
- the Euler characteristics of the cell counts (1, 5, 6), (1, 9, 26, 24), (1, 7, 16, 12), (1, 6, 12, 8) and the
  strata counts 4, 26, 236.
By hand: the Hopf surface coordinates and the normal derivative of P4c3; the weights of P4c2 against
(1+2t)(1+3t) and (1+2t)(1+3t)(1+4t); formula (7) of P1d3 on (P¹, ∞).

# Part I. The statements

## 1. Verdict counts

| Verdict | Number | Statements |
|---|---|---|
| correct | 61 | all others (53 of the return's "Proved" and its 8 "Refuted": each refutation is a correct counterexample) |
| wrong | 0 | — |
| gap | 0 | — (two proofs are outlines whose missing step I supplied: P1a1, P3a-existence; see §3) |
| known | 1 | P4d2 (Readdy 2005, Theorem 4.7: search summary only; integral homology recomputed) |
| open | 1 | P3c-general — **proved by this review for projective completions** (Theorem R, §4); open for proper non-projective ones |

Depth: V = proof followed step by step; C = recomputed by my own code or by hand; K = cited source opened at the
cited place; S = the step that rests on a cited theorem was not checked (source not opened).

## 2. The table

| # | Id (paper no.) | Return | Verdict | Depth | Reason |
|---|---|---|---|---|---|
| 1 | P1a1 (Thm 1.1) | Proved | correct | V, K | Map(s,t) is the homotopy fibre over (s,t) of the torus bundle L_ST → S × T. Miller's Theorem 4.9 (p. 272) is exactly the endpoint-fixing equivalence holink ⊂ popaths for two distinct strata of a homotopically stratified space; the depth filtration of a normal crossings pair satisfies his Definition 2.8. Jansen 2024 Prop. 3.16, Cor. 3.17 are restriction to locally closed parts and descent along an étale atlas. The step from Cor. 3.17 to mapping spaces is not written in the return; supplied in §3. |
| 2 | P1a2 (Thm 1.2) | Proved | correct | V | Faces of the real oriented blow-up; no tubular embedding is chosen: the inclusions of faces are natural for étale maps, so the stack case follows levelwise. B𝓗_X ≃ ∂X^log checked for two strata. The sentence on what "the manuscript means" is a reading, not a theorem. |
| 3 | P1b1 (Thm 1.3) | Proved | correct | V | Checked in full: (1)⇔(3) by the kernel of π₁(L_ST) → π₁(S) × π₁(T), one component of the incidence cover at a time; (2)⇒(3) by pushing the local torus into the punctured normal bundle of T, no asphericity used. |
| 4 | P1b2 (Cex 1.4) | Refuted | correct | V, C | Strata C∖{0,1}, C*, C*, two points; adjacent maps inject; full map (a,b) ↦ (a+b)e_x. The removed point r is needed (with E° = A¹ the adjacent map at q would fail). |
| 5 | P1b3 (Prop 1.5) | Proved | correct | V | Sequence (4); (37) is exact for the open stratum when U_J is the punctured tube inside U. If U_J were the tube minus D_J alone, the closed D_J would give an exact sequence too: the answer depends on his definition of U_J (scan 132, not checked by me). |
| 6 | P1c1 (Thm 1.6) | Proved | correct | V | Checked in full. (1) Π₁X and the constructible sheaves of sets (= Fun(h𝓔, Set); h𝓔 is determined by the Π₁-system with its flags) need no hypothesis; (2) aspherical strata give X as the homotopy colimit of the BΠ₁; (3) with injectivity 𝓔 = h𝓔. |
| 7 | P1c2 (Cex 1.7) | Refuted | correct | V | (P¹, ∞) and (P¹ × C, P¹ × 0); the second has the same groupoid diagram as (C², C × 0). |
| 8 | P1d1 (Thm 1.8) | Proved | correct | V | Checked in full. Shapes B𝓔 ≃ X and B(h𝓔); two strata: BA ∪_{BG} BB against BA ∪_{B(im G)} BB. |
| 9 | P1d2 (Prop 1.9) | Proved | correct | V | Fibres S², Pⁿ, S² × S². |
| 10 | P1d3 (Thm 1.10) | Proved | correct | V, C | Checked in full: levelwise connectivity gives (r+1)-connectedness; the spectral sequence has one term in total degree r+2; relative Hurewicz applies on universal covers. Formula (7) gives Z for (P¹, ∞). The quadric example is right (closed object initial in h𝓔). |
| 11 | P1e1 | Proved | correct | V | |
| 12 | P1e2 | Proved | correct | V | Hom(p_i, u) = G/H_i. |
| 13 | P1e3 | Proved | correct | V, K | 1 + 10 + 15 objects, 30 incidences. Jansen 2023: Construction 3.18 is the Charney–Lee category with Hom(σ,τ) = {γ : γσ ≤ τ}/Δ_σ; Corollary 6.6 identifies the exit ∞-category of the stack of stable curves with it; Theorem 6.7 is the exodromy equivalence. The return's formula is Jansen's with ≤ read as reverse inclusion. |
| 14 | P1e4 | Proved | correct | V | Hom(σ,τ) = N/N_σ. |
| 15 | P1e5 | Proved | correct | V | (i) fails exactly at a factor (0,0), (ii) exactly at a factor (0,1). |
| 16 | P1e-roots (1.16) | Proved | correct | V | Corrects Lead 4: a root along the same boundary multiplies meridians and keeps the kernel. |
| 17 | P1e-cusp (1.17) | Proved | correct | V, C | Meridians m, b, a, h; kernels (−3,1), (−2,1); ⟨m,h⟩ injects. |
| 18 | P1e-cusp-proper (1.18) | Proved | correct | V, C | G_pr = Z² ⋊ Z; third kernel (−6,1). |
| 19 | P1e-cusp-stack (1.19) | Proved | correct | V | [F × Δ/μ₆] is good; it is a weighted blow-up of the cusp point, not a root stack. |
| 20 | P1e-finite (1.20) | Proved | correct | V | |
| 21 | P2a (Thm 2.1) | Proved | correct | V | Non-stratal centre: E and all s strict transforms meet (t > 0), kernel (−1,…,−1,1). |
| 22 | P2b (Thm 2.2) | Proved | correct | V | The reverse asphericity argument (∂: π₂(S) → Zʳ dies because Zʳ injects into π₁(U)) is his own argument of 149, scan 134, made into a proof. |
| 23 | P3a-core-necessity (3.1) | Proved | correct | V | |
| 24 | P3a-core (3.2) | Proved | correct | V | |
| 25 | P3a-existence (3.3) | Proved | correct | V | The necessity proof is brief; the missing step is in §3. |
| 26 | P3a-minimal (3.4) | Proved | correct | V | Bounds −2 and 2 checked (a self-nodal curve loses 4 when its node is blown up). |
| 27 | P3a-analytic-scope (3.5) | Proved | correct | V | |
| 28 | P3a-Picard (3.6) | Proved | correct | V | The two covers have genus 2 (Riemann–Hurwitz checked). |
| 29 | P3a-examples (3.7) | Proved | correct | V, S | Items 1, 4 and the algebraic parts of 2, 3 checked. The analytic list for (C*)² and its reduction rest on Ueda 1979, Theorem 2 and Proposition 3: source not opened. |
| 30 | P3a-scope (3.8) | Refuted | correct | V | Hopf against toric (b₁); root stack against scheme (inertia); E_q × A¹ (analytic good completion, no algebraic one). |
| 31 | P3b-discrete (3.9) | Proved | correct | V | |
| 32 | P3b-completion (3.10) | Proved | correct | V | Centre of F̂_r by Gaschütz modules; cyclic subgroups by M. Hall's completion of an immersed circle. |
| 33 | P3b-horizontal-profinite (3.11) | Proved | correct | V | |
| 34 | P3b-vertical (3.12) | Proved | correct | V | A conditional theorem; its hypotheses are worded loosely. Precise form in §3. |
| 35 | P3b-vertical-counterexample (3.13) | Refuted | correct | V | Wording: the kernel has rank one in a lattice of rank two (the register says "rank-two vertical kernel"). |
| 36 | P3b-profinite (3.14) | Proved | correct | V, S | SGA 1 XII 5.1, 5.2 not opened. |
| 37 | P3c-Mori (3.15) | Proved | correct | V, S | The A¹ argument is group-theoretic and holds for proper pairs; the P¹ case uses a Kähler class; nefness is Svaldi 2019, Theorem 1.1: source not opened. |
| 38 | P3c-morphism (3.16) | Proved | correct | V, S | Negativity lemma applied correctly; Kato's chart criterion not opened. |
| 39 | P3c-crepant (3.17) | Proved | correct | V | |
| 40 | P3c-toric (3.18) | Proved | correct | S | Toric weak factorization (Włodarczyk, Morelli); the cited place not opened. |
| 41 | P3c-weak-strong (3.19) | Proved | correct | S | A remark on what two theorems do not give; no mathematical statement of its own. Adiprasito–Pak not opened. |
| 42 | P3c-general (Conj 3.20) | Open | **open in the return; proved here for projective completions** | — | §4. |
| 43 | P3c-flop-test (3.21) | Proved | correct | V | Shorter: (K+D)·C = n − 1, so crepancy forces n = 1, and then C minus a point is an A¹ in a stratum. |
| 44 | P4a1 (Prop 4.1) | Refuted | correct | V, C | |
| 45 | P4a2 (Thm 4.2) | Proved | correct | V | |
| 46 | P4b (Prop 4.3) | Proved | correct | V | |
| 47 | P4c1 (Thm 4.4) | Proved | correct | V, S | The combinatorial lemma checked (a non-stratal centre adds a cone over a join with a simplex). Payne p. 307, AKMW 0.3.1, Harper, Thuillier: not opened. |
| 48 | P4c3 (Ex 4.5) | Refuted | correct | V, C | g(u,v) = (u+1, αv); meridian (0,1); normal derivative 1; both links T³. |
| 49 | P4c2 (Thm 4.6) | Proved | correct | V, C | Weight argument checked, k = 0 and k = 1 included. Agrees with H²(M₀,₅) = Q⁶ and H³(M₀,₆) = Q²⁴ in top weight. Durfee–Saito, Tubach, Payne not opened. |
| 50 | P4d1 (Prop 4.7) | Proved | correct | V, S | (1,1): point against BC₂. Chan–Galatius–Payne, Abramovich–Caporaso–Payne not opened. |
| 51 | P4d2 (Thm 4.8) | Known | known | C | The tree/laminar-family bijection is proved in the paper; the homotopy type is Readdy's theorem (search summary only). Integral homology recomputed: Z², Z⁶, Z²⁴, no torsion; agrees with our own computation of 13 November. |
| 52 | P4e (Prop 4.9) | Proved | correct | V | |
| 53 | P5a1 (Prop 5.1) | Refuted | correct | V, C | Z⁴ against Z³. |
| 54 | P5a2 (Thm 5.2) | Proved | correct | V | Depth ≤ r is (r−1)-connected in L; sharp by C^{r+1}. |
| 55 | P5a3 (Cor 5.3) | Proved | correct | V | (247) gives Π₁X*; (C, 0) excludes Π₁X. |
| 56 | P5b1 (Thm 5.4) | Proved | correct | V | Nerve of the cover of Teichmüller space by the sets V_σ. |
| 57 | P5b2 (Thm 5.5) | Proved | correct | V, S | Rank selection checked, infinite case included. The sphere theorem is cited as Harer 1988, Ch. 4, Thm 4.1: not opened (I know it as Harer 1986, Thm 3.5). |
| 58 | P5b3 (Prop 5.6) | Proved | correct | V | Proves the case k = d − 1 by Morse theory on the Stein manifold M₀,ₙ. |
| 59 | P5b4 (Prop 5.7) | Refuted | correct | V, S | (2,1), k = 3: the curve complex is a wedge of 2-spheres. It also refutes the guess of Lead 4 of EXIT_TOWER as worded (§5). |
| 60 | P5c1 (Thm 5.8) | Proved | correct | V | Join estimates checked case by case. |
| 61 | P5c2 (Prop 5.9) | Proved | correct | C | The 6 relations hold in B₄. Not the form asked in Part 5(c) (§5). |
| 62 | P5c3 (Prop 5.10) | Proved | correct | C, V | The 20 relations hold in B₅; (1, 9, 26, 24); the syzygy argument is right. Same remark. |
| 63 | P5c4 (Thm 5.11) | Proved | correct | V | Counts 24, 12, 8 are those of the three aspherical models. Same remark. |

## 3. Steps supplied

**P1a1, the stack case.** Jansen's Corollary 3.17 gives Π(X,P) as the colimit over the Čech nerve of the exit
∞-categories of the atlas levels. Mapping spaces of a colimit of ∞-categories are not computed levelwise in
general; here they are, for this reason. Restrict to two strata (Jansen, Prop. 3.16 (1)). An ∞-category over the
poset {0 < 1} with ∞-groupoid fibres 𝒮, 𝒯 is the same thing as a span of spaces 𝒮 ← L → 𝒯, with L the space of
crossing arrows and Map(s,t) the homotopy fibre of L → 𝒮 × 𝒯; this is an equivalence of ∞-categories, colimits of
∞-groupoids in ∞-categories are ∞-groupoids, and pullback to a point of {0 < 1} preserves colimits. So the colimit
is computed on spans, objectwise, and L of the stack is the homotopy colimit of the links of the atlas levels, which
is the homotopy type of the link stack because links commute with étale pullback. For a quotient [M/G] by a discrete
group this reads Map(x, y) = ∐_g Map_M(x, gy), which is what formula (1) gives.

**P3a-existence, necessity.** Let W dominate Y and a good X. The fringe T of W is exceptional over X and contracts
to smooth points of a corner refinement W_c of X. The morphism W → Y contracts a subset T′ of the curves of T and
curves of the core that carry no fringe. Then W → W_c factors through W/T′, which is smooth near the image of T
because it is locally Y; a birational morphism of smooth surfaces is a composite of point blow-downs; so the fringe
of Y, which is the image of T, contracts to smooth points.

**P3b-vertical, the precise form.** Let (B̄, ∂B̄) be a good normal crossings pair (a stack is allowed), C̄ → B̄ a
family of stable pointed curves, smooth over B = B̄ ∖ ∂B̄, with the marked sections removed to give U → B, and take a
smooth toroidal resolution of the total space with its toroidal boundary. Then the total pair is good; if the
completed lattices of the base inject into the completion of π₁(B), so do those of the total pair. The proof in the
return is correct for this statement: the local lattice N sits in 0 → Z·(vanishing cycle or puncture loop) → N →
(base lattice), and the kernel maps into π₁ of a fibre, which injects by P3b-discrete. The sentence about
"recursively compatible" towers is this statement applied repeatedly; for the genus-zero tower M̄₀,ₙ₊₁ → M̄₀,ₙ it
applies as it stands.

## 4. P3c-general: proved for projective completions

**Theorem R (this review; the proof has been checked by no one else).** Let U be a smooth complex algebraic
threefold and (X, D), (Y, E) smooth projective completions with normal crossings boundaries, both good. Then they
are joined over U by a finite sequence of blow-ups and blow-downs along smooth closures of boundary strata, every
intermediate pair being good. More precisely there are a tower X_s → X of such blow-ups and a toroidal morphism
X_s → Y; so the good projective completions of U are the smooth projective toroidal embeddings of U whose conical
complexes have a common subdivision with that of (X, D).

*Reduction to simple normal crossings.* Blowing up closures of strata in order of increasing dimension makes the
boundary simple normal crossings and keeps goodness (P2a, P2b). Assume D, E simple.

*Step 1 (from the return).* K_X + D and K_Y + E are nef (P3c-Mori), and on a common resolution the log discrepancy
divisors agree (P3c-crepant). Hence every component E_j of E has log discrepancy 0 for (X, D). For a log smooth pair
the divisors of log discrepancy 0 are the monomial valuations at strata (A_X(v) ≥ Σ v(z_i) over a regular system of
parameters at the centre, with equality only for monomial v, and the sum is v(D) only when the parameters are the
equations of the branches). So E_j is a toroidal valuation of (X, D), and it appears on a tower X′ → X of blow-ups
of smooth closures of strata. (X′, D′) is good by P2a. Every prime divisor of Y is now a prime divisor of X′.

*Step 2 (the base ideal).* Let H′ be very ample on Y, V the linear system on X′ obtained by transporting |H′| along
φ: X′ ⇢ Y (the divisors φ^*(div s), s ∈ H⁰(Y, H′), all in one class L on the smooth X′), and I its base ideal; its
cosupport is the indeterminacy locus of φ, which lies in D′ and has codimension ≥ 2. Let p: X_I → X′ be the normalized blow-up of I and q: X_I → Y the morphism it gives;
q^*H′ = p^*L − F with −F ample over X′, so q is finite on every fibre of p. Let Γ be an exceptional prime divisor
of p (a Rees valuation of I). Γ is not a divisor of X′, hence not of Y, so dim q(Γ) ≤ 1. If p(Γ) were a point, q
would be finite on Γ: impossible. So p(Γ) = B is a curve, q(Γ) = R is a curve, and Γ → B × R is finite.

*Step 3 (the fibre over a general point).* Let x ∈ B be general, J_x the set of branches of D′ through x (one
branch if B lies in one component only, two if B is a component of D′₁ ∩ D′₂), and N′ = p^{-1}(N_x) for a general
surface germ N_x through x across B. N′ is a normal surface (general fibre of a function on the normal X_I),
N′ → N_x is a modification of a smooth surface germ, and p^{-1}(x) is its exceptional tree of rational curves; its
components lie on the exceptional divisors of p over B. Each component ℓ maps finitely onto a rational curve
R_ℓ ⊂ E. Let S be the stratum of (Y, E) containing the generic point of R_ℓ. By P3c-Mori for (Y, E) there is no
nonconstant map from P¹ or from A¹ to S, so the normalization of R_ℓ has two distinct points over deeper strata,
and ℓ has two distinct points u with q(u) in a deeper stratum: q(u) ∈ E_k for some E_k not containing R_ℓ.
Such a u lies on a component of q^{-1}(E_k) other than the exceptional divisor Γ_ℓ ⊃ ℓ. The components of
q^{-1}(E_k) through a point of p^{-1}(x) are exceptional divisors over B, which meet p^{-1}(x) in whole components
of it, and strict transforms of branches D′_j, j ∈ J_x, each of which meets p^{-1}(x) in one point t_j (the strict
transform of an irreducible curve germ is one branch). So: **every component of p^{-1}(x) carries two distinct
points among the nodes of the tree and the points t_j, j ∈ J_x.**

*Step 4 (the tree).* Let M → N′ → N_x be a resolution in which the strict transforms of the germs D′_j ∩ N_x are
arrows on single exceptional curves; M → N_x is a sequence of point blow-ups, and the components of p^{-1}(x) are
the exceptional curves of M not contracted in N′ (the Rees curves). Let 𝒯₀ be the smallest subtree of the dual
tree containing the Rees curves and the arrows. For a Rees curve, all Rees curves and arrows in one branch of the
tree at it are attached to it, in N′, at one point. So Step 3 says that every Rees curve has two branches of 𝒯₀:
no Rees curve is a leaf of 𝒯₀, and the leaves of 𝒯₀ are arrows.
- One arrow (B in one component of D′ only): a tree with a Rees vertex and one arrow has a Rees leaf. Impossible.
  **So the indeterminacy locus of φ contains no point of an open stratum of codimension one.**
- Two arrows (B a stratum curve): 𝒯₀ is the path between the two arrows. The vertices on that path are exactly the
  curves created by blowing up corner points, that is the monomial valuations in the two branches (induction on the
  blow-ups: a blow-up at the meeting point of two neighbours on the path inserts a vertex in the path; any other
  blow-up attaches a vertex off it). **So every Rees valuation of I is a toroidal valuation of (X′, D′), centred on
  a stratum curve.**

*Step 5 (conclusion).* The integral closure of I is the intersection of the valuation ideals of its Rees
valuations; each is generated by monomials in the equations of the branches; so the integral closure of I is a
toroidal ideal, and X_I → X′ is a toroidal modification. Refine it by a tower X_s → X′ of blow-ups of smooth
closures of strata. (X_s, D_s) is good (P2a), and g: X_s → Y is a birational morphism of good smooth projective
pairs that is the identity on U, hence toroidal (P3c-morphism). By the weak factorization theorem for toroidal
birational morphisms between nonsingular toroidal embeddings (Włodarczyk 1997; Morelli 1996; Abramovich–Matsuki–
Rashid 1999), g is a composite of blow-ups and blow-downs along smooth closures of strata, and every pair on the way
is good by P2b. ∎

**What the proof uses that I did not open:** Svaldi 2019, Theorem 1.1 (through P3c-Mori); Kato's criterion (through
P3c-morphism); the toroidal weak factorization theorem (cited from memory: the statement and the three sources must
be opened); normality of a general fibre of a function on a normal variety.

**What remains open in P3c-general.** Proper non-projective completions: Step 1 uses the cone theorem and the
exclusion of P¹ in a stratum uses a Kähler class. Smallest undecided instance: a smooth proper non-projective
threefold completion with one good projective completion known. The statement in dimension ≥ 4: Steps 3–4 use that
the centres of the Rees valuations have codimension two.

**Consequences.** (1) Lead 4 of the prompt holds for projective threefolds, and for the torus (C*)³ every good
projective completion is toric. (2) The indeterminacy of the comparison map between two good projective
completions is a union of stratum curves; a flop inside one boundary component never occurs (P3c-flop-test is a
special case). (3) For M₀,₆ every good projective completion is a toroidal modification, followed by a toroidal
blow-down, of M̄₀,₆; its conical complex is the cone over Δ₀,₆ with another smooth subdivision.

## 5. Findings

1. **No statement is wrong.** The eight refutations are correct counterexamples. Our leads are corrected at three
   places: Lead 4's root stacks (by P1e-roots, a "Proved" statement) and its guess in the analytic and stack
   generality (P3a-scope); Lead 5's "category π₀(𝒟)" (P4a1; the same in the dictionary, RG7). P1b2 answers the
   question of Part 1(b) on relative codimension one in the negative. P5b4 refutes the extension of Lead 6 to all
   genera. Leads 1, 2, 3 and 6 are confirmed (P1a2, P1b1, P2a, P5a1–P5a2, P5b2).
2. **The Remarque and the Remords (scans 179–180).** By P1c1 the Remarque is true as he wrote it when the strata are
   aspherical, if "reconstituer" is the homotopy colimit of the classifying spaces of the groupoids with their
   canonical morphisms and 2-cells; the fundamental groupoids and the topos of sheaves of sets locally constant on
   the pieces need no hypothesis at all, which is what his margin can mean. The Remords concerns the other route,
   through the ordinary glued topos, whose shape is B(h𝓔): it gives X exactly under the injectivity of the meridian
   lattices in addition (sufficient by P1c1 (3); the comparison is 2-connected with first obstruction (7), P1d3).
3. **Part 5(c) is not delivered in the form asked.** The prompt asks for presentations of Γ₀,₅ and Γ₀,₆ as
   fundamental groups of complexes of groups, generators from the strata of dimension ≤ 1 and relations from those
   of dimension 2. P5c1 proves that such presentations exist (|P₂| is simply connected in every genus). P5c2 and
   P5c3 give instead the presentations of the iterated fibrations (F₃ ⋊ F₂ and F₄ ⋊ Γ₀,₅): correct, checked, but
   their relators are not indexed by strata, and the 24, 12, 8 identities of P5c4 are those of three aspherical
   models, attached to the strata of dimension 3 by type only. The task stays open; it is passed to EXIT_TOWER.
4. **Lead 4 of EXIT_TOWER is refuted as worded.** It guesses that P_k is (min(k, 2g − 2 + n) − 1)-connected. For
   (2, 1) and k = 3 this says 2-connected; by P5b4 the complex is a wedge of 2-spheres. The bound that the top level
   allows is min(k, h) − 1 with h the dimension of Harer's spheres (n − 4; 2g − 3 + n for g ≥ 1, n ≥ 1; 2g − 2 for
   n = 0).
5. **P1b3 and the meaning of U_J.** The answer "the open stratum" is right if U_J is the punctured tube inside U.
   The intake of scan 132 must confirm that this is his U_J.
6. **Citations.** Miller and both Jansen papers say what the return says they say, at the places cited. The return's
   note that the numbering of the toolbox paper differs between versions was not checked. Sixteen other sources were
   not opened by me (list above).
7. **The return's programs were not read.** Every numerical claim that carries weight was recomputed; the syzygy
   words of P5c3 (24 expanded identities, up to 640 factors) were not recomputed: the count 24 and the freeness
   follow from the aspherical 3-complex, which I checked.
