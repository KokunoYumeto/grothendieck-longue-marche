# Prompt items for GPT-6 Astra (ChatGPT Pro mode)

Draft for sign-off. Drafter: the shape-map successor (Claude Fable 5.2, effort high). 13 November 2026, 14:20 UTC
(machine clock). What was read is listed at the head of `COMBINED_IMPLICATIONS.md`; the three floor answers present
at 14:17 UTC are taken in.

**Rules for every item.** Each item is a statement. It is finished only when it is proved or refuted; a refutation
comes with the corrected statement, proved. Partial results are steps to record and build on. No prompt text is
written here; whoever writes a prompt from these items runs
`python -I -B C:/Users/user/Documents/claude_tools/push_rule_pro_prompts.py --lint-math <PROMPT.md>` before it
goes to the user. "Known" lists what the conference has, with its status as in `COMBINED_IMPLICATIONS.md`
(line numbers A 1, B 4, … refer to it).

## 1. FRAISSE_EXACT (the prompt of N1–N6; drafted and packaged by the Dérivateurs successor, not sent)

By its author's status note: N1 = Part B, N2 = Part A, N3 = Part C, N4 = Part D, N5 = Part E, N6 = Part F. From
the part headings and Parts A–F as read by the drafter, the following conference items are already in it: C1 and
its test (A.2, A.3 (iv)); the Reiter and convex properties (Lead 2, A.3 (v)); floor intake_Q1 (C.4); floor
Derivateurs_expert_Q1 (B.2, B.3 (b), B.5); the three regimes (Part E); the age of finite sets with an equivalence
relation and an independent linear order (class (3) of A.4); exactness over Q from compact subgroups with dense
union (Lead 5). The items below are additions for its author to place. Each is a statement to prove or refute.

- **FE-1 (from R4 L3; to A.4, class (3), as a lead).** Let b be two inequivalent points x < y, c the structure
  x₁ < y₁ < x₂ < y₂ with x₁ ~ x₂ and y₁ ~ y₂, and α₁ = (x₁, y₁), α₄ = (y₁, x₂): b → c. Statement: for every ring R in
  which 2 is not a unit, no element β of R[A(c, d)] of augmentation 1 satisfies βα₁ = βα₄, for any d; hence colim_A
  is not exact over Z or over F₂. Then: colim_A is exact over Q and over F_p for every odd p.
  Known: the first sentence, by a parity argument on the order of the two classes (A 14; no second reader); the
  second is a sketch.
- **FE-2 (from R4 L1 and the Dérivateurs expert's reply; to Part A or C).** In setting (S): colim_A is exact over
  F_p if and only if it is exact over Q and p divides no index [U : G_F], U an open subgroup that is a finite
  extension of a pointwise stabilizer G_F. Known: an automorphism of prime order p of an object, acting freely on
  the hom-sets, excludes exactness over F_p (A 12); FI (A 8).
- **FE-3 (floor shape_map_Q1; to Part C.5).** Let F, F′ be diagrams of finite-dimensional F_p-vector spaces on
  C_δ^op with dim F(X) = dim F′(X) for every object X. Statement: lim¹ F and lim¹ F′ have the same dimension. First
  case: a diagram M′ on C_δ with dim M′(X) = 2|C_δ(V, X)| − |C_δ(W, X)| at every X and T₁(M′) = 0.
  Known: on the tower side the sizes do not determine the class (PUSH F.4; B 5).
- **FE-4 (from R4 4.2; to Part D.3).** For C_δ and an expansion class A* that is Ramsey (orientations with
  successor-closed embeddings and a free order; Evans–Hubička–Nešetřil), with forgetful functor u: A* → C_δ.
  Statement: colim over A* is exact over Z; u is not homotopy final; and T₁(Q_R) ≅ R over C_δ is the image of
  H₁ of the comma category W∖u with coefficients R under the edge map of the Grothendieck spectral sequence of u.
  Known: nothing; the statement is a speculation of R4 and may be refuted at its first clause.
- **FE-5 (to Part E).** For a countable directed index set and a diagram of countable abelian groups, lim¹ is zero
  or uncountable. Consequence to prove with it: a non-zero finite lim¹ on a diagram of finite groups occurs only
  over a non-directed index. Known: the case of N is in the literature (Gray; not opened; shape-map agent).
- **FE-6 (the rational half of N2 as it now stands; to A.3).** For a category A with finite hom-sets and common
  successors: the Reiter property implies exactness over Q; and exactness over Q implies the Reiter property.
  Known: BZ refutes the first without finite hom-sets (A 9); under EPPA the first holds (A 13).

## 2. LM8_PUSH

- **LP-1 (floor shape_map_Q3, as computed by the intake; the first mixed-prime case).** Setting: Π = F̂₂ for
  P¹ ∖ {0, 1, ∞} over Q, K the kernel of Π → C₃ sending x and y to one generator, Q₇₅ = V ⋊ C₃ with V the
  ζ₃-isotypic quotient of K^ab/5.
  - (a) K is the geometric fundamental group of the curve y³ = x(1 − x) with its three punctures removed, a curve E
    of genus 1 with j = 0; as a Galois module K^ab/5 = F₅(1)² ⊕ E[5], and V = E[5].
  - (b) Every section modulo V lifts to Q₇₅, and the lifts of a section with cocycle c ∈ Z¹(G_Q, C₃), up to
    conjugation by V, are a principal homogeneous set under H¹(G_Q, E_c[5]), E_c the cubic twist of E by c.
  - (c) A class of H¹(G_Q, E_c[5]) that extends to a section of every quotient of Π above Q₇₅ (through E_c[5ⁿ] for
    all n and through the class-two relative pro-5 quotient of LM8 A.23, with the local conditions the section
    imposes at 3, at 5 and at the cusps) is the Kummer class of a rational point of the twisted affine curve
    y³ = c·x(1 − x), or of a cusp.
  Known: (a) and (b) by hand, no second reader, (a) marked unchecked by its author (C 4). (c) is open; its two
  outcomes are spelled out in `floor\shape_map_Q3_answer_intake.md`.
- **LP-2 (the mixed-prime section statements; R4 section 7, item 2).** With N = ker(π̄ → ∏_ℓ π̄^{(ℓ)}):
  - (M0) if s is a section of Π → G_Q and for every ℓ its image in the maximal pro-ℓ quotient is the section of a
    rational point x_ℓ or of a cusp, then the x_ℓ are equal, or the cusps are;
  - (M1) a section of Π with the same image in Π/N as the section of a rational point or of a cusp is conjugate to
    it.
  Known: at the abelian level the primes are independent and s_ℓ^{ab} determines x_ℓ (drafter, elementary); LP-1 is
  the first case of (M1).
- **LP-3 (LM8 G.20, as the return leaves it).** With R = ⋂_ℓ ker(π → P_ℓ) for y² = x³ − x over Q(i): R^{s_b(Δ)} = 1;
  and no procyclic subgroup 1 ≠ C ⊂ R has open arithmetic normalizer. Known: the reduction (LM8 G.19, G.20; C).
- **LP-4 (LM8 A.22 against the pentagon and the lift; PUSH_ITEMS LM 2).** The involution φ_λ, λ = 1 − 2e, of
  F̂₂/F̂₂″: (a) it satisfies the image in F̂₂/F̂₂″ of the pentagon relation; (b) it lifts to an automorphism of F̂₂.
  Known: it commutes with the geometric 𝔖₃ in Out(F̂/F̂″) (C 2; no second reader); lifts through the relative pro-5
  tower (LM8 A.23–A.26; C).
- **LP-5 (floor shape_map_Q2, statement 2).** For a hyperbolic curve U over a number field K and a K-rational cusp
  c: the continuous homotopy fixed points of G_K on the geometric punctured henselian neighbourhood of c have π₀
  equal to the set of sections of D_c → G_K modulo inertia, a torsor under lim K^×/K^{×n}, and trivial π₁; the map
  from this set to the section classes of π₁(U) → G_K is injective, with image the cuspidal packet at c; the
  rational tangent vectors form the K^×-subtorsor. Known: "true on π₀, with precisions" by two participants from
  memory (D 6); the injectivity of packets is in the literature (Stix), not opened in this round.
- **LP-6 (LM8 F.12, with the criterion of LM7_PUSH).** H²_cts(G_Q, Z₅(3)) has a non-zero phantom subgroup
  lim¹_n H¹(G_Q, Z/5ⁿ(3)), and a class-three obstruction of the tripod's pro-5 tower lands in it for an explicit
  pair of Kummer classes. Known: the phantom subgroup is non-zero by the criterion B 4 and its corollary B 6,
  since G_Q acts on Z₅(2) through an infinite group; the second clause is open.
- **LP-7 (the EXIT reviewer's items 1 and 2, as that reviewer placed them: LM5 F (d), (c), or LM8_PUSH).**
  Statements A and B of its talk and the chain computation, for a closed union of strata of a normal crossings pair
  on a manifold and on an étale stack; and, for a scheme with a normal crossings divisor in characteristic 0: the
  limit of the étale topoi of the punctured étale neighbourhoods of x̄ is the étale topos of X_(x̄) ×_X U, its
  coverings are the T^{I(x)}-sets, and it is a classifying topos exactly in dimension one.

## 3. The successor of LM7_PUSH

- **PS-1 (descent along the cyclotomic tower; LM7 reviewer, R4 2.2 d).** For a finite-rank Z₃-lattice M with
  G_Q-action, Δ₃ = G_{Q(μ_{3^∞})}, Γ = Gal(Q(μ_{3^∞})/Q), X = lim_n H¹(Δ₃, M/3ⁿ): (a) H²_cts(G_Q, M) = X/(γ − 1)X;
  (b) the subgroup lim¹_n H¹(G_Q, M/3ⁿ) is closure((γ − 1)X)/(γ − 1)X; (c) for ramification confined to a finite
  set S the corresponding X_S is finitely generated over Z₃[[Γ]] and (γ − 1)X_S is closed; (d) without the
  restriction X is not finitely generated. Known: the finite-level identity (B 9).
- **PS-2 (the criterion's corollary; R4 2.2 b).** For M as in LM7_PUSH F.1: lim¹_n H¹(G_L, M/ℓⁿ) = 0 if and only if
  G_L acts on M(−1) through a finite group. Known: derived from F.3 and Chebotarev (B 6; no second reader).
- **PS-3 (the lim¹ class and the section sets; OPEN_DISAGREEMENTS item 7).** For the pro-3 group N of the Fermat
  cubic minus its cusps over Q: no section of N/γ₃N that is ramified at infinitely many primes lifts to a section
  of N. Known: such sections exist at class two (PUSH A.6; C); at every layer r ≥ 3 a lift exists iff the local
  corrections are integral and tend to zero (LM7 E.44; C).
- **PS-4 (the CM coset; LM7 reviewer).** (a) The CM coordinates ρ = (T, W) are a homomorphism on GT̂₀. (b) GT̂₀
  contains an element whose ρ lies outside the Galois image 𝒢. (c) For the bases S₄ and A₄ × C₂ of LM7 D.45 and the
  comparison named in PUSH E.2: the obstruction to survival is the class of the extension in H² with 2- or
  3-primary coefficients in the relative kernel over PSL₂(Z/12). Known: (a) is LM2 C.d4, to be confirmed; given
  (a), (b) is equivalent to reaching the extra coset at multiplier one (C 7); (c) is the reviewer's bookkeeping,
  marked unsure.
- **PS-5 (LM4's involutions and GT̂₀; LM7 reviewer; it can equally go to the LM4 continuation).** There is an
  involution in GT̂₀ acting as complex conjugation on the 2-adic part and trivially on the 3-adic part. Known: LM4
  D.29–D.30 give outer involutions with mixed-prime multiplier in types (0,4) and genus 2 (C 5); whether one exists
  in type (0,3) commuting with 𝔖₃ is unchecked.

## 4. The LM4 continuation (the run is still going)

- **L4-1 (from D.63–D.65).** In the once-punctured-torus peripheral outer group Ω: (a) every negative involution is
  conjugate to one of the two standard ones b₀, b₁; (b) every element of finite order has multiplier 1 or −1.
  Known: the centralizers of b₀ and b₁ are C₂² with multipliers ±1 (D.64, D.65; C 6); the return says it does not
  assert (a).

## 5. EXIT_TOWER, LM5, ANABELIAN_149_PUSH (the EXIT reviewer's items 3, 4, 5, as placed in its talk)

- **EX-3 (EXIT_TOWER Part C).** Lead 2 from LM8 E.12 and P1b3, for every stable (g, n).
- **EX-4 (LM5 F (f); ANABELIAN_149_PUSH).** T^{I(x)} → π_{U/K} is injective exactly when every finite covering germ at
  x is a sub-germ of a finite étale covering of U.
- **EX-5 (EXIT_TOWER Lead 6; LM5 F).** The sentence of cote 149, scan 133, on the invariance of the punctured
  completion is true for the non-archimedean punctured tube with no hypothesis and false for the archimedean link
  for compact X; test cases (P¹, {0, 1, ∞}) and M̄_{0,5}. Its author marks it a hunch with sources from memory.

## 6. Not prompt items: checks of ours that the items above lean on

- A second reader for LM7_PUSH F.1–F.3 (B 4), for R4 L3 (A 14) and for the intake's order-75 computation (C 4).
- Open the sources named from memory: Stix on packets (for LP-5); Serre, CG II §3.3 (for PS-1); Isbell–Mitchell (for
  FE-1, FE-6); Gray (for FE-5); SGA 4 VI 8.7 and VII 5.7 (for LP-7).
- Read scans 242–243 of cote 140-4 for the wording behind LM8 E.11 (intake's test 4).
- The first check of floor shape_map_Q2, statement 1 (the map on π₁ by winding numbers).
