# The field expert on intake section 13 (cote 150, scans 1–43)

By Claude Fable 5.2 at effort max, the reviewer of EXIT_ONE_TYPE; no sub-agents, no web. 14 November 2026, 09:53 UTC.

**Read.** `INTAKE_20261114.md`, section 13 (by Claude Fable 5.2 at effort high). Of the return (first-pass
transcription and notes by GPT-6 Astra, ChatGPT Pro mode; claims, not certified): the transcription of scans 4–5
(lines 268–400), 28–30 and 39–41, in the `.tex`. Not read: the notes, the doubts, the pages, the other scans, the
EXIT_TOWER prompt as it now stands (I know it as of 13 November, before Part E (e)), LM5 F.32, STRATA C and F.
My own review of EXIT_ONE_TYPE was in my context. "Mine" = worked out here, checked by no one.

## (a) The sense of the intake's findings

1. **P1a1 and "the whole family locally trivial": right, with one precision.** Scan 39, margin, reads as the intake
   says: condition (1) (each `Σ_{d′} → Σ_d` fibrant) "est trop faible"; for fixed `d` the stratification formed by
   the `Σ_{d ⨿ δ}` over `Σ_d` must be locally trivial. The run's two-lines example is right. The precision (mine):
   the two axioms do different work. Separate fibrations are the hypothesis of Miller's theorem (a homotopically
   stratified space in Quinn's sense, pairwise conditions), and that is all the mapping-space formula of P1a1
   needs. Local triviality of the stratified family is what gives conical charts, hence the Segal condition of scan
   40 up to homotopy and exodromy. For a normal crossings pair it is automatic (local product charts), so no
   statement of EXIT_ONE_TYPE changes; in a general theory it is the hypothesis to carry.
2. **P1d1: right.** His gluing `X̂ = X^* ⨿_Ẋ C(p)` is the strict pushout along a collar that presents the homotopy
   pushout `S ∪_L T` of P1d1. "Pour les isos" makes it an equivalence of groupoids of equipped objects, not of
   categories. No proof of P1d1 in it, as the intake says.
3. **The sphere test: right.** Cut space of the open stratum `D²`, boundary `S¹`, link map `S¹ → pt`, cone a disc:
   `S²`. It is P1c2's first example read geometrically: gluing with the link kept gives `S²`.
4. **The span of scan 41 is the link term `E`: yes (mine).** `Σ_{01}` is the boundary face of the deployed open
   stratum over the closed one, `s : Σ_{01} → Σ_0` its link fibration, `b : Σ_{01} → Σ_1` the boundary immersion.
   The classifying space of the category of crossing arrows is the link (P1a2 (3), checked in my review), which is
   `Σ_{01}` up to homotopy; `b` is a cofibration, so the pushout of the span is the homotopy pushout of C.3.
   More: the whole datum of scans 39–42 is a model of the exit ∞-category. Put `N_n = ∐ Σ_{i_0 ≤ … ≤ i_n}`.
   Condition (3) says `N_2 = N_1 ×_{N_0} N_1` strictly, `s` is a fibration so the pullback is a homotopy pullback,
   and the only invertible arrows are the identities `Σ_{ii} = Σ_i`: a complete Segal space. Its mapping space
   from `x` to `y` is the homotopy fibre of `(s, b) : Σ_{ij} → Σ_i × Σ_j`, which is P1a1's formula once
   `Σ_{ij}` is identified with the link. I did not write out that identification.
5. **Scan 5, faithfulness: the failure is real.** As read: "3° bis (en présence de 1° et 2°) implique la fidélité".
   Counterexample: `I = {a < b}`, `X_a = X_b = X ≠ ∅` satisfies 1°, 2°, 3° bis, and `X_b ⊂ X_a` with `b ≰ a`.
   (With `a, b` incomparable the same spaces violate 2°; the run's R05 must be the chain.) Requiring the family to
   be strictly increasing does not save it: `a, b < c` and `a, b < d`, `X_c = X_d = X_a ⨿ X_b`.
   What is true (mine, one line): 2° and 3° imply fidelity. If `X_i ⊂ X_j` then `X_i = ⋃_{k ≤ i, j} X_k`; a point of
   `X_i^*` lies in some `X_k` with `k ≤ i, j` and in no `X_k` with `k < i`, so `k = i ≤ j`. By his own NB on scan 4,
   3° bis gives 3° in the presence of 4° (density). So he most likely meant 3°, or 3° bis with 4°. The words
   "3° bis (en présence de 1° et 2°)" are an insertion over a deletion: second pass.
6. **Scan 29, the infimum: true as he means it, false globally.** His proof works inside the Boolean interval
   `I_{i,j} ≅ 𝒫(S)`, and his margin on scan 28 says "les Inf dans `I_{i,j}`". There `k′ = Inf(k, j′)` exists and is
   a predecessor of `k`. In `I` it can fail (the run's poset `u, v < a, b < j`): the infimum computed in `I_{u,j}`
   is `u`, in `I_{v,j}` it is `v`. The statement is local along `X_i`, which is what the cube-corner structure
   needs. The global failure is the case of two closed strata meeting in two components, and it occurs in
   `M̄_{2,1}` (see (b)).
7. **Scan 40 against LM5 F.32: the same condition on two different objects (mine; F.32 not read).** Cote 147's
   category `𝒟` has as arrows the choices of sub-branch-sets: its source maps are finite coverings. Cote 150's `Σ`
   has the links as arrows: its source maps are fibrations with the links as fibres. Both satisfy the strict
   fibre-product condition. P1a1 uses both in succession: the incidence cover `F_{ST} → S`, then the torus bundle
   `L_{ST} → F_{ST}`. "Restates" is right for the Segal condition only.

## (b) Implications, and the poset of stable graphs settled

Order as in cote 150: `G ≤ G′` when `G′` is a contraction of `G` (the closed stratum of `G` lies in that of `G′`).
All of this is mine, by hand.

- **Intervals.** Genus 0: Boolean. A stable tree is its set of splits, contraction removes splits, so the poset is
  the face poset of the complex of compatible splits, and `[σ, τ] ≅ 𝒫(σ ∖ τ)`. Genus ≥ 1: false for isomorphism
  classes as soon as a graph has two edges with isomorphic contractions. Smallest: (1,2), the cycle of two
  genus-0 vertices with one leg each; both contractions give the one-loop graph, and the interval up to the open
  stratum is a chain of three. For every `g ≥ 2`: the vertex of genus `g − 2` with two loops. (1,1) is Boolean.
- **The intersection axiom** `X_i ∩ X_j = ⋃_{k ≤ i,j} X_k`: holds for every `(g, n)`. It is the frontier condition:
  a point of both closed strata has a graph that contracts to both.
- **Infima.** Genus 0: two strata with a common lower bound have the infimum `σ ∪ τ`. False for (2,1): the
  divisors `Δ_0` (one loop) and `Δ_1` (genus 1 | genus 1 with the leg) have two maximal common degenerations, the
  loop on either side of the separating edge; the leg makes them non-isomorphic. This is exactly `u, v < a, b < j`.
  For (2,0) the two are isomorphic. Genus 1: I found no failure and did not classify.
- **What it means.** His axioms c) and (14) are axioms on the deployment, not on the coarse index poset. For
  `M̄_{g,n}` the index is the category of stable graphs with contractions (for `G → G/C` the factorizations are
  the subsets of `C`), and the target maps `b` are immersions, not embeddings, exactly where the poset fails to
  be Boolean. This is P4a1 (components of flags do not form a category) seen from his side, and it is the margin of
  cote 147, scan 78 ("peut-être que des immersions locales"), which EXIT_TOWER Part A (c) asks to decide. Lead for
  that task: genus 0, always embeddings; smallest local immersion, (1,2), the two-edge cycle in the closure of the
  one-loop stratum.
- **EXIT_ONE_TYPE.** Nothing to correct. Cote 150 supplies the manuscript form of P1a1, P1a2, P1d1 and P4e, and (a) 4
  gives the statement that ties them: `Σ` is a Segal model of the exit ∞-category.
- **STRATA.** C.3 has its geometric span (scan 41); F.3 its positive counterpart (the sphere glues correctly with
  links).
- **LM5, LM8.** LM5 Part F (c), (d): cote 150's index objects answer "which object replaces the category of
  components". LM8 Part F: nothing until §15 (pro-neighbourhoods) is transcribed; my statements A and B of the
  conference (the limit of the sheaf topoi is empty, the pro-object and the compact model are right) are what §15
  should be read against.

## (c) EXIT_TOWER: the four proposals

My word on the hold: send EXIT_TOWER with these four texts; do not wait for package 42.

1. **Reword. Part A, new task after (b).** "Cote 150, scans 39–42. For a chain of contractions
   `G_0 → G_1 → … → G_k` of stable graphs of type `(g, n)` let `Σ_{G_0 → … → G_k}` be the corresponding face of the
   real oriented blow-up of `M̄_{g,n}` along its boundary, as a stack with the automorphisms of the chain. Prove or
   refute: (i) these form a simplicial stack on the nerve of the category of stable graphs with contractions, and
   every concatenation square is cartesian, `Σ_{G_0 → G_1 → G_2} = Σ_{G_0 → G_1} ×_{Σ_{G_1}} Σ_{G_1 → G_2}`;
   (ii) each source map `Σ_{G → G/C} → Σ_G` is a locally trivial bundle with fibre the torus `(S¹)^C`; (iii) each
   target map `Σ_{G → G/C} → Σ_{G/C}` is an immersion onto a boundary face, and it is an embedding exactly for the
   pairs found in (c); (iv) the simplicial space is a complete Segal space whose ∞-category is the exit category of
   (b), so that its homotopy category is `𝔐(g, n)` of (a); (v) its levelwise sets of components are the symmetric
   semisimplicial set of chains of stable graphs of EXIT_ONE_TYPE P4a2, and they do not form a category (P4a1,
   P4d1)."
2. **Keep, reworded. Part A, same task, last clause.** "Cote 150, scans 8, 18–19, 39 ('Cela est trop faible').
   Prove that over each stratum `M_G` the whole family of deployed pieces, with its stratification by the faces
   indexed by the subsets of `E(G)`, is locally trivial as a stratified family on the stack, and compute its
   monodromy: the action of `Aut(G)` on `E(G)` and the lattice of Dehn twists `Z^{E(G)}`."
3. **Keep. Part D (a), added sentences.** "Cote 150, scans 32–35 and 37. Prove that the topological stack `M̄_{g,n}`
   is recovered from the cut space of the open part (the real oriented blow-up), its boundary faces with their
   collars, and the attaching maps, by `X̂ = X^* ⨿_Ẋ C(p)` and induction on the strata; write the spaces and maps
   for (0,4), (0,5), (1,1), (1,2); prove that the result does not depend on the order of the induction, as a
   canonical isomorphism; and say after which stage of the induction the fundamental groupoid is that of
   `M̄_{g,n}` (compare EXIT_ONE_TYPE P5a2, P5a3)."
4. **Reword: the answers are known to us, ask for proofs. Part A (a), added sentences.** "Cote 150, scans 28–30.
   For the set of isomorphism classes of stable graphs of type `(g, n)` ordered by contraction, prove or refute
   each: (i) in genus 0 every interval is Boolean, two strata with a common lower bound have an infimum, and the
   poset is the face poset of the complex of compatible splits; (ii) for (1,2) the interval from the two-edge cycle
   to the open stratum is a chain of three elements, and for every `g ≥ 2` so is the interval from the graph with
   two loops; (iii) for (2,1) the divisors `Δ_0` and `Δ_1` have two maximal common lower bounds and no infimum;
   (iv) `X_G ∩ X_{G′} = ⋃_{Γ ≤ G, G′} X_Γ` for every `(g, n)`; (v) his axiom c) of scan 28 holds for the category of
   stable graphs with contractions: for `G → G/C` the intermediate contractions are the subsets of `C`. Then
   determine every `(g, n)` for which the poset of isomorphism classes has Boolean intervals, and every `(g, n)`
   for which it has the infima of (i)."

**The twelve items of 13.4.** In EXIT_TOWER, in the form for `M̄_{g,n}` only: 5 (text 2), 9 (text 4), 10 (text 3),
12 (text 1). In a successor of EXIT_ONE_TYPE, in general form: all twelve. Item 3 is settled in (a) 5 and goes in
as a statement to check, with the corrected hypothesis.

**A successor is warranted, after packages 42 and 43.** The realization he puts off on scan 43 and §14–§15 may be
in scans 44–99; writing the successor before they are read would ask for what he may have done. Its items:
(S1) orders and faithful stratifications: items 1–3, with "2° and 3° imply fidelity" and the two counterexamples;
(S2) strict conical neighbourhoods, collars, the compactness margin: item 4;
(S3) the two equisingularity axioms: separate fibrations give the mapping-space formula, local triviality of the
stratified family gives conical charts; prove both, prove they differ, prove the second for Whitney and for
definable stratifications: item 5;
(S4) the reconstruction theorems of scans 20, 23, 35, with the reading of scan 20 fixed by the second pass, and
independence of the filtration: items 6, 7, 10, 11;
(S5) cube corners `B_J × I^J` and pre-cylindrical stratifications, with the index a category when strata
self-cross: items 8, 9;
(S6) the standard presentation: `Σ` is a complete Segal space, its ∞-category is the exit ∞-category, its
realization is the space, and his deferred reconstruction is that realization with collars: item 12;
(S7) the comparison he does not make: homotopy type, constructible sheaves and exit category from the data (18),
with EXIT_ONE_TYPE P1c1 and P1d3 as the statements to recover: items 10, 12.

## (d) The zip additions for EXIT_TOWER

Confirm the transcription, the notes (labelled as the transcribing model's claims) and the doubts. Change the pages:
add scans 12–15 (the definitions of cone, collar and "strict", on which texts 1–3 turn) and 24–26 (the commuting
coordinates behind the cube corners of text 2). So: pages of scans 8, 12–15, 18–20, 22–43.

## (e) Questions for packages 42 and 43, beyond the intake's three

(d) List every section title of cote 150 from scan 44 on, with its scan numbers.
(e) Does he relate the internal category `Σ` of scans 39–43 to paths or to a fundamental groupoid: report every
occurrence of "chemin", "générisation", "groupoïde fondamental", "Π_1", "topos", "type d'homotopie", with the
sentence.
(f) Does he return to the index set: any passage where `I` is replaced by a category, where the target maps are
immersions and not embeddings, or where strata meet in several components; any mention of "multiplicités", of
Teichmüller or of `M_{g,ν}`.
(g) The final form of the equisingularity axiom: where he states "famille localement triviale" as a definition, and
whether he derives the cartesian squares of scan 40 from it.
(h) For the tubular pro-neighbourhoods "au sens des proespaces": the exact definition of the pro-object, and any
sentence on its limit (whether he takes it, and what he says it is).
(i) Does the sphere, `P¹` with a point, or any example with a simply connected open stratum reappear.

## (f) Hunches, as items for GPT-6 Astra (ChatGPT Pro mode) to prove or refute

1. For a conically stratified space with locally trivial stratified links, his `Σ` (scans 39–42) is a complete
   Segal space, its ∞-category is the exit ∞-category, and the space is the realization of `Σ` with collars; the
   reconstruction `X̂ = X^* ⨿_Ẋ C(p)` is that realization computed by induction on the strata.
2. "Separate fibrations" is Quinn's homotopically stratified condition and "the whole family locally trivial" is
   the conical condition. Decide whether exodromy (constructible sheaves are functors on the exit ∞-category)
   holds under the first alone, with the run's two-lines family as the first test.
3. For `M̄_{g,n}`: the poset of isomorphism classes of stable graphs has Boolean intervals exactly for genus 0 and
   (1,1), and the infima of scan 29 exactly for genus ≤ 1. (The first half I believe; the second is a guess.)
4. The target map `Σ_{G → G′} → Σ_{G′}` fails to be an embedding exactly at the pairs where the interval
   `[G, G′]` of isomorphism classes is not Boolean; this decides his margin of cote 147, scan 78.
5. His §15 pro-neighbourhood is the pro-object of the punctured neighbourhoods; its limit as a space or as a topos
   is empty, and its homotopy limit is the link (my conference statements A, B and floor answer (1)). To be put
   against the text when package 42 returns.

## For the second pass of cote 150, in addition to the intake's list

Scan 5: the insertion "3° bis (en présence de 1° et 2°)" and the deleted lines around it. Scan 28, margin: "les Inf
dans `I_{i,j}`". Scan 39, margin: "fortement supérieurs" and "stratification" against the deleted "famille".
