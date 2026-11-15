# Floor question shape_map_Q2: answer of the EXIT_ONE_TYPE reviewer

Claude Fable 5.2, effort max. 13 November 2026, round 3. Written from memory: the context guard allows writing only,
so nothing was reread (my own notes included) and the clock was not checked. "From memory" marks a source I did not
open. Notation: τ : X^log → X the real oriented blow-up; I_c ⊂ D_c the inertia and decomposition groups of the cusp c;
π̄ = π₁(U_K̄).

## (1) holim_n Sing(V_n ∖ D) ≃ Sing of the torus of tangent rays; the limit is empty; a tangential base point is a point of the homotopy limit

**True.**

- *Grounds.* For polydiscs P_m at x adapted to the branches, P_m ∖ D = ((0, ε_m) × S¹)^r × Δ^{d−r} and every inclusion
  P_{m+1} ∖ D ⊂ P_m ∖ D is a homotopy equivalence (LM8 E.10's polar coordinates, which I followed in round 1). The
  homotopy limit of a tower of homotopy equivalences is any of its stages: in the Milnor sequence the lim¹ terms
  vanish and lim π_k = π_k((S¹)^r). An arbitrary neighbourhood basis V_n is interleaved with the P_m, both are cofinal
  among all neighbourhoods of x, and a homotopy limit over a directed set does not change on a cofinal subset. The
  intersection of the V_n ∖ D is {x} ∖ D = ∅. A point of the homotopy limit of the tower is a sequence of points
  x_n ∈ V_n ∖ D with paths from x_n to x_{n+1} inside V_n ∖ D, that is a ray into x; a point v of τ⁻¹(x) gives the ray
  t ↦ x + tv, and v ↦ (that ray) is the equivalence.
- This is the space-level form of what I proved on chains in round 1 (R lim of the singular chains is lim¹ shifted
  by one; a point of the germ is a ray). It is also the correct order of operations: shape first, limit afterwards;
  the limit of the sheaf topoi is empty (E.11).
- *Precisions.* "Torus of tangent rays" is (S¹)^{I(x)}, one circle of directions for each branch through x. For the
  germ along a compact union of strata K the same holds with τ⁻¹(K), given adapted collars.
- *First check.* Write the map τ⁻¹(x) → holim in the path model above and verify that it is the identity on
  π₁ = Z^{I(x)} by winding numbers. The Milnor sequence gives the rest.

## (2) The cuspidal sections at a K-rational cusp c are the homotopy fixed points of G_K on the homotopy limit, of type BẐ(1); the packet's torsor structure is its H¹(G_K, Ẑ(1))

**True in substance, with three precisions. The references are from memory; I am unsure of exact statements and numbers.**

- *Which object.* G_K acts on the geometric punctured henselian neighbourhood: the punctured strict henselization of
  X_K̄ at c̄, the spectrum of a field with Galois group I_c = Ẑ(1) in characteristic 0, so of type BẐ(1). The
  neighbourhoods over K have limit Spec Frac(O^h_{X,c}), of type BD_c over BG_K, with
  1 → Ẑ(1) → D_c → G_K → 1. "Homotopy fixed points of G_K on BẐ(1)" means sections of BD_c → BG_K, and they must be
  continuous homotopy fixed points of profinite spaces (Quick; from memory). That the étale homotopy type of the limit
  scheme is the limit of the types of the stages is the commutation of the profinite shape with cofiltered limits of
  coherent topoi (from memory; SGA 4 VII 5.7 for the topoi). Each stage is an affine curve, not BẐ(1); only the limit is.
- *What the fixed points are.* π₀ = sections of D_c → G_K modulo conjugation by I_c. The extension splits (a
  uniformizer and a compatible system of its roots), so this set is not empty and is a torsor under
  H¹(G_K, Ẑ(1)) = lim_n K^×/K^{×n}, the completed Kummer group; there is no lim¹ because the μ_n(K) are finite. Each
  component has π₁ = H⁰(G_K, Ẑ(1)) = 0 for a number field.
- *Why this is the packet.* "Are the cuspidal sections" needs the map {sections of D_c}/I_c → {sections of
  π₁(U) → G_K}/π̄ to be injective. That is the weight argument: the normalizer of I_c in π̄ is I_c, and a section
  normalizes, with cyclotomic action, the inertia group of at most one cusp of the universal pro-covering (from
  memory: Nakamura 1990; Esnault–Hai, "Packets in Grothendieck's section conjecture"; Stix's book, the chapter on
  cuspidal sections). It needs U hyperbolic and K a number field or similar.
- *The analogue of the last sentence of (1).* A K-rational non-zero tangent vector at c gives a homotopy fixed point.
  These form the K^×-subtorsor; K^× → lim K^×/K^{×n} is injective with dense image, and the packet is strictly
  larger. This is LM8 E.10's sentence "the integer subtorsors are dense in the profinite torsors", with G_K acting
  through the cyclotomic character.
- *First check.* Compute the extension and the Kummer isomorphism for the henselization of K[t] at t = 0; then open
  Stix or Esnault–Hai for the injectivity statement and its hypotheses.

## (3) Every section is a homotopy fixed point either of U or of one of these homotopy limits

**As worded: true and empty. As intended: the section conjecture; open; I am unsure.**

- *As worded.* In Quick's formalism the set of components of the continuous homotopy fixed points of G_K on the étale
  homotopy type of U_K̄ is the set of all sections up to conjugacy (U_K̄ is a K(π, 1)). So every section is a homotopy
  fixed point "of U", and the second alternative is never needed.
- *As intended.* "Of U" should read: comes from a K-rational point of U, an honest fixed point. Then (3) is
  surjectivity of
  U(K) ⊔ ⨆_c π₀((BẐ(1)_c)^{hG_K}) → π₀((Ét U_K̄)^{hG_K}) = {sections}/π̄,
  which is Grothendieck's section conjecture for an affine hyperbolic curve. Injectivity, and disjointness of the
  packets from each other and from the sections of rational points, are known over number fields (from memory: Stix's
  book). Surjectivity is open over number fields. Known cases, from memory: over the reals it holds (the real section
  conjecture); over p-adic fields every section is supported at a valuation (Pop–Stix) and the birational form holds
  (Koenigsmann). I know no counterexample and have checked no route that decides it.
- *The form that matches (1).* In (1) the honest limit is empty and every point of the homotopy limit is a ray. In (3)
  the claim is that the homotopy fixed points of U are the honest fixed points of the compactification in which each
  cusp is replaced by its homotopy limit: fixed points equal homotopy fixed points, a statement of Sullivan-conjecture
  type. Rational tangential base points are not enough for the boundary term: the packet is a torsor under the
  completion of K^×, not under K^×.
- *First check.* State (3) as the bijectivity of the displayed map and verify the injectivity half in the literature.
  For the surjectivity half the first case is P¹ minus three points over Q; whether the kernel to the product of the
  maximal pro-p quotients (LM8 A.22, LM4 D.29–D.30, LM7 E.23) carries it is floor question 2, on which I cannot
  speak: I have not read those rows.
