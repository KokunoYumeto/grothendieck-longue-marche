# EXIT_ONE_TYPE: background

Written by Claude Fable 5.2 (effort max), 12 November 2026, as reader R-GLUE of the Montpellier archive programme. A draft, not authority: every argument below is a sketch by one reader, checked by no one. It is attached so that the leads of the prompt can be checked step by step and corrected.

## 1. Sources and their status

- Cote 147, scans 106–190, and cote 149, scans 128–136: first-pass transcriptions by GPT-6 Astra (ChatGPT Pro mode). No second pass. No scan image was opened for this note. The readings that carry mathematics are R1–R19 and R26–R29 of `RGLUE_DICTIONARY_20261112.md`.
- STRATA, RESIDUE, BISITE: returns of GPT-6 Astra (ChatGPT Pro mode) to prompts of the companion work on *Les Dérivateurs*. Claims. No review at full effort exists.
- Hunches H3, H4 and the statements S2, S25 of our planning notes: guesses by Claude Fable 5.2, restated in the prompt as Leads 1–6 after the reading.

## 2. His constructions of 147 §11 in present terms

| His object (scan) | What it is |
|---|---|
| `D_d` (106–108) | pairs (point, germ of an intersection of `d` local branches); the normalization of the locus where at least `d` branches meet; `D_0 = X` |
| `D_{d,d′}`, `D_{d_0,…,d_r}` (108–113, 128) | flags of such germs at one point; source map finite étale, target map a local immersion of codimension `d − d′` |
| `𝒟` (114–121) | the category in analytic spaces with objects `∐ D_d` and arrows `∐ D_{d,d′}`; arrows go from the deeper germ to the shallower |
| `D_d^*` (127) | the open stratum of codimension `d` (normalized) |
| `T_d`, `G_d`, `P_d` (121–123) | lattice of meridians; the torus `T_d ⊗ G_m`; the product of the punctured normal bundles of the `d` branches |
| `Π_{d_*}`, `Π̃_{d_*}` (129–131) | `Π_1` of `D^*_{d_*}` and of `P^*_{d_*}` |
| generization (133–139) | `Π̃_{d_0,d_1,…} → Π̃_{d_1,…}`: a point of `X^*` near the deeper stratum is near the shallower one |
| `𝒱_{D′,Y}`, `𝒱^*_{D′,Y}` (140–148) | germ of neighbourhoods of `D′`, and its part outside `Θ` |
| `X^{*∞}` (150) | the punctured neighbourhood of the whole divisor: the link at infinity of `X^*` |
| `𝒱^{d′_0}_{d_*,d″_0}` (168) | for strata `A ⊂ B ⊂ R` of codimensions `d_0 ≥ d′_0 ≥ d″_0`: the tube of `A` in the closure of `R`, minus the branches of `R` through `B`; up to homotopy a `(S¹)^{d′_0 − d″_0}`-bundle over `A` |

## 3. Sketches behind the leads

**Lead 1.** Over a point `x` the fibre of `X^log → X` is `(S¹)^{I(x)}`; over the stratum `D_d^*` it is the bundle of unit normal directions of the `d` branches, which is `P_d^*` modulo `(R_{>0})^d`. The closed face over `D_d` is the restriction of `X^log` to (the normalization of) the closed stratum; it is a manifold with corners whose interior is the open face, so the inclusion of the open face is a homotopy equivalence. The open face over `D^*_{d_0}` lies in the closed face over `D_{d_1}` for every flag: this inclusion, followed by the inverse of that equivalence, should be his `γ`. The boundary of `X^log` is the union of the closed faces, and a union of closed faces is the homotopy colimit of the faces over the nerve of their incidence category: his gluing theorem.

**Lead 2.** For strata `S ⊂ S̄′` of codimensions `d > d′` let `H` be the space of exit paths from `S` to `S′`; it is homotopy equivalent to a `(S¹)^{d−d′}`-bundle over (a finite cover of) `S`, and the mapping space between two points is a homotopy fibre of `H → S × S′`. It is discrete exactly when `π_k(H) → π_k(S) × π_k(S′)` is injective for `k = 1` and bijective for `k ≥ 2`. For `S = S′` this is asphericity of `S`. If all strata are aspherical, `H` is aspherical, `π_1(H)` is an extension of `π_1(S)` by `Z^{d−d′}`, and the condition is that this lattice injects into `π_1(S′)`. Reduction to the open stratum: let `L′` be the link of `S′` in `X^*`, so that `π_1(L′) → π_1(S′)` is onto with kernel the image of the fibre lattice `Z^{d′}`. The lattice `Z^d` at a point of `S` splits as `Z^{d′} ⊕ Z^{d−d′}` (branches containing `S′`, and the others), maps to `π_1(L′)` and on to `π_1(X^*)`. If `v ∈ Z^{d−d′}` dies in `π_1(S′)`, its image in `π_1(L′)` equals that of some `w ∈ Z^{d′}`; then `v − w` dies in `π_1(X^*)`, so `v = w = 0` by (ii).

**Lead 3.** Blow up a point `p` on one branch `D_1` of a surface: the exceptional curve `E` meets the strict transform at one point `q`; a small loop around `E` is a small loop around `D_1`, so the two meridians at `q` are equal in `π_1(U)`, and inside `E` the stratum `E − q` is an affine line in which the meridian of `q` dies. Blow up a double point `D_1 ∩ D_2`: `m_E = m_1 + m_2`, the lattices at the two new double points are `⟨m_1, m_E⟩` and `⟨m_2, m_E⟩`, the open stratum of `E` is `C^*` and the meridian of either end generates its fundamental group. Blow up a point of a curve of double points in a threefold: `E = P²` meets the two strict transforms in two lines, the open stratum of `E` is `C × C^*`, and a lattice of rank 2 maps to `Z`.

**Lead 5.** The boundary of `X^log` is covered by the closed faces; the spectral sequence of this cover has `E_1^{p,q}` the sum of the `H^q` of the faces over the components of the `D_{p+1}`. The faces are torus bundles over manifolds with corners homotopic to open strata; the weight-zero part of their cohomology is `H^0`. Taking weight zero (an exact functor on mixed Hodge structures) leaves the cochain complex of the dual complex. This needs the mixed Hodge structure on the link (Durfee; Durfee–Saito) and care with rational coefficients.

**Lead 6, the hexagon.** `X = C³`, `Θ = {z_1 z_2 z_3 = 0}`. `D_1^*`: three copies of `(C^*)²`, and `P_1^*` three copies of `(C^*)³`. `D_2^*`: three copies of `C^*`, `P_2^*` three copies of `(C^*)³`. `D^*_{2,1}`: six copies of `C^*` (an axis and one of the two planes through it), `P^*_{2,1}` six copies of `(C^*)³`. Every map `P^*_{2,1} → P_2^*` (forget the plane) and every generization `P^*_{2,1} → P_1^*` is an isomorphism on `π_1 = Z³`, all compatible with the identification with `π_1((C^*)³)`. The homotopy colimit is a graph of spaces over the hexagon with vertices 1, 12, 2, 23, 3, 13: `(S¹)³ × S¹`. The truth is `(C^*)³` near `Θ`, with group `Z³`. With the flags (3), (3,1), (3,2), (3,2,1) the hexagon becomes the barycentric subdivision of a triangle. General `k`: for `C^{k+2}` the flags in codimensions `≤ k + 1` give `(S¹)^{k+2}` times the boundary of a `(k+1)`-simplex, which differs from `(S¹)^{k+2}` in `π_k`.

**Lead 6, by dimension.** Lift to Teichmüller space; for a multicurve the region where its curves are short is contractible, and these regions meet along unions of multicurves; the nerve is the poset of multicurves. Restricting to multicurves with at least `d − k` components selects `k + 1` consecutive ranks of the face poset of the curve complex. In genus 0 the link of a simplex with `c` curves is a join of curve complexes of spheres with holes, of total dimension `n − 4 − c`, each a wedge of spheres of top dimension: the complex is homotopy Cohen–Macaulay.

## 4. Tests, with the answers we expect (all unchecked)

- `(P¹, ∞)`: (i) holds, (ii) fails; the mapping space is a circle. `(P¹, {0, 1, ∞})`: both hold.
- `M̄_{0,5}`: both hold (multitwists generate free abelian groups in the mapping class group of the cut surface).
- Smooth projective toric surface with its toric boundary: both hold; `π_1(U) = Z²` and every lattice is a basis of it or a primitive vector.
- `C̄_1 × C̄_2`: holds exactly when every puncture loop of each factor has infinite order in the fundamental group of that factor and the factors are aspherical; fails for a factor `A¹`.
- `y² = x³ + t`: the total space is `C²` with `t = y² − x³`, the fibre over 0 a cuspidal cubic; three blow-ups give components of multiplicities 1, 2, 3, 6. `π_1(U)` is the braid group on three strands, with `t` the degree. The meridians of the components of multiplicity 2, 3, 6 are conjugate to `σ_1σ_2`, `σ_1σ_2σ_1` and the central element `(σ_1σ_2)³`. At the two double points on the component of multiplicity 6 that involve multiplicities 2 and 3 the lattices have kernels spanned by `(3, −1)` and `(2, −1)`; at the double point with the strict transform the lattice injects.

## 5. Literature named in the prompt (from memory; to be opened and verified)

Kato–Nakayama (1999), log Betti cohomology and the space `X^log`. Deligne (1989), *Le groupe fondamental de la droite projective moins trois points*, §15 (tangential base points). Lurie, *Higher Algebra*, Appendix A (exit paths). Douteau–Waas (2022), homotopy links and stratified homotopy theories. Jansen (2023), the stratified homotopy type of the Deligne–Mumford compactification. Haine–Porta–Teyssier (2024), exodromy beyond conicality. Thuillier (2007), *Géométrie toroïdale et géométrie analytique non archimédienne*. Stepanov (2006), on the dual complex of a resolution. Payne (2013), *Boundary complexes and weight filtrations*. Chan–Galatius–Payne (2021), tropical curves, graph complexes and top weight cohomology of `M_g`. Harer (1986), the virtual cohomological dimension of the mapping class group. Abramovich–Karu–Matsuki–Włodarczyk (2002), weak factorization. Quillen (1978) and Björner (1980) on Cohen–Macaulay posets and rank selection. Morrow (1973) and Ramanujam (1971) on minimal normal completions of surfaces.
