# A dictionary between the moonshine side and our work on Grothendieck's programme

By Claude Fable 5.2 at effort high (the agent that wrote `research_maps_20261112\PRETOT_3D_MODULARITY\MAP.md`),
14 November 2026, clock read at 17:18 UTC. For the main session (Claude Opus 5.5 at effort max) and the user.

The dictionary is the means. The end is section 4: what the bridge lets us infer for our results and stuck points
from the work on the Leech lattice and moonshine, each with the item for GPT-6 Astra (ChatGPT Pro mode).

**Flags.** **[opened]** = read in the source for this note, place given. **[MAP]** = opened for MAP.md on 12 November.
**[computed]** = my arithmetic, script `check_dictionary_arithmetic.py` in this folder, checked by no one else.
**[memory]** = not checked against a source. **[mine]** = my own identification or argument, checked by no one.
**Hunch** and **speculation** are marked. Returns of GPT-6 Astra (ChatGPT Pro mode) are claims unless a referee
(Claude Opus 5.5 at effort max) is named in our files. Row names such as E.58 are those of our intakes.

Short names of sources: **CDH** = Cheng, Duncan, Harvey, *Umbral Moonshine and the Niemeier Lattices*, LaTeX
`UMNL_x2.tex` in `F:\user\Documents\arxiv_latex\library\moonshine_lattices\`. **TASI** = Anagiannis, Cheng, *TASI
Lectures on Moonshine* (same folder). **Gannon** = *Moonshine Beyond the Monster*, §6.3.3 (same folder). **SPLAG** =
Conway, Sloane, *Sphere Packings, Lattices and Groups*, Chapter 8 §2 (same folder). **CMT** = Conway, McKay, Trojan,
arXiv:0811.0076 (`Papors\OS\Moonshine`). **HGA** = Uludağ, Sağlam, *Hypergeometric Galois actions*, Handbook of
Teichmüller Theory VI, pp. 484-499 (`Papors\OS\Eisenstein lattice`; the extract on disk starts at p. 484).

## 1. The dictionary

Right-hand side in the author's terms. "Match" is identity (the same object), functor (a construction carries one to
the other), or analogy.

| # | Moonshine side | Our side, in the author's terms | Match | Flags |
|---|---|---|---|---|
| 1 | A genus-zero group Γ with its Hauptmodul; the Hauptmodul of Γ₀(4) is T = (η(τ)/η(4τ))⁸ = q⁻¹ − 8 + …, monstrous class 4C | The tripod P¹ − {0,1,∞} with its coordinate: Y₀(4) ≅ Y(2), three cusps, no orbifold point; 16/λ(2τ) = T + 16 | identity | Γ^X = 4C and T^X: CDH Table "Niemeier Root Systems and Principal Moduli", Prop. `prop:TX` [opened]; the relation with λ [memory] |
| 2 | The Niemeier root system A₃⁸, lambency 4, umbral group 2.AGL₃(2) | The object the umbral table attaches to the tripod (row 1) | functor (CDH's X ↦ Γ^X) | CDH tables [opened] |
| 3 | Γ₀(2) (2B, A₁²⁴, M₂₄), Γ₀(3) (3B, A₂¹², 2.M₁₂), Γ₀(1) (1A, the Leech case in Conway moonshine) | The tripod divided by an involution, orbifold (2,∞,∞); the orbifold (3,∞,∞); the modular orbifold (2,3,∞) with group B = C₂ ∗ C₃, the oriented cartographic group | identity for the curves | classes: CDH table [opened]; signatures [memory] |
| 4 | Components of X = A_{ℓ−1}^{d}, d = 24/(ℓ−1) = p + 1, permuted by Ḡ^X ⊇ PSL₂(p), p = 23, 11, 7, 5, 3, 2 | The fibre of X₀(p) → X(1): the p + 1 darts of the dessin of X₀(p), with its cartographic group PSL₂(p) | identity of permutation groups | CDH §2.5 [MAP]; (ℓ−1)(p+1) = 24 [computed] |
| 5 | Umbral group at lambency 5: G = GL₂(5)/2, Ḡ = PGL₂(5) | The arithmetic monodromy group of X(5) over X(1) (geometric part A₅ = PSL₂(F₅), quotient F₅^× by the cyclotomic character); Ḡ = Aut(A₅) = 𝔖₅ is the group through which ĜT₀ acts on the icosahedral deck group (inner iff λ ≡ ±1 mod 5) | identity of groups; the identification is [mine] | CDH table "Umbral Groups" [opened]; our side: `EXPERT_ON_BOGGI_A5.md` (a) |
| 6 | McKay's correspondence in umbral moonshine: ℓ = 3, 4, 5 ↔ p = 11, 7, 5 ↔ 2.Alt₅, 2.Sym₄, 2.Alt₄ ↔ Ẽ8, Ẽ7, Ẽ6; "a unique subgroup of index p, a fact peculiar to the particular p" | Levels N = 5, 4, 3 of the modular tower (icosahedron, octahedron, tetrahedron; S³/2I, S³/2O, S³/2T as fillings of the trefoil complement at distance N); ℓ + N = 8. The index-p subgroups are Galois's three exceptional ones; for p = 5 it is the group Γ_T of the quintic resolvent 𝔗_T | identity of the finite groups; the alignment is [mine] | CDH Table 4 [MAP]; `POINCARE_AND_A5_20261114.md` §3, §5.2 |
| 7 | Exact divisors e ∥ m, Atkin-Lehner involutions W_e, the "+e" of Γ₀(m)+e; on theta coefficients r ↦ a(e)r with a(e) ≡ −1 mod 2e, ≡ 1 mod 2m/e | Non-trivial idempotents of ℤ/2m. For m = 6: a(3) = 5, a(2) = 7, a(6) = 11, and {1,5,7,11} is the centre of SL₂(ℤ/12). The frame 5I of LM7_PUSH E.58 is a(3) | identity of the groups {1,5,7,11}; that Δ is this is a **hunch** (4.1) | CDH (`def:OmegaMatrices`), exact divisors [opened]; a(e) [computed]; E.58: `INTAKE_20261114.md` §9.2 |
| 8 | Lambency 6 (A₅⁴D₄, group GL₂(3)) and 6+3 (D₄⁶, group 3.Sym₆), index m = 6, theta index r mod 12 | The user's marked Niemeier lattice N(A₅⁴D₄) with "its twelve theta indices"; the ℤ/12 on which Δ is read | identity (the same lattice); the link with Δ is a **hunch** | CDH tables [opened]; S6 workbench `niemeier_umbral_shadow.tex` (headings) [MAP] |
| 9 | η(τ) = Σ (12/n) q^{n²/24} = θ_{6,1} − θ_{6,5} − θ_{6,7} + θ_{6,11}: odd under a = 5 and a = 7, even under a = 11 | The generator of Mp₂(ℤ)^ab = ℤ/24 (main session's notes §3); the character (12/·) of Gal(ℚ(ζ₁₂)/ℚ) cuts out ℚ(√3) | identity | [computed] |
| 10 | Galois symmetry of modular data: G_σ = diag(χ(σ), χ(σ)⁻¹) ∈ SL₂(Ẑ), σ.S = G_σ S, σ.T = T^{χ(σ)}; signed permutations in the character basis | The outer action of G_ℚ on B̂ at congruence level: conjugation by diag(χ, 1); frames tied to the multiplier λ | identity at congruence level | Gannon (6.3.3), (6.3.4) [opened] |
| 11 | Gannon: "The Galois action (6.3.3) of RCFT is not directly related to Grothendieck's"; it factors through Ẑ^× and SL₂(Ẑ) | The faithful action on the full profinite B̂; ĜT₀ as the cusp-preserving outer automorphisms of B̂ | the gap between the two is where Δ lives (4.1) | Gannon §6.3.3 [opened] |
| 12 | Moore-Seiberg data (braiding, fusing, S, T) and their polynomial equations; Drinfeld's action of GT on braided categories | Le jeu de Lego-Teichmüller: types (0,3), (0,4), (1,1), (0,5), (1,2); pentagon and hexagons | identity in the literature (Gannon calls it a toy model of the Esquisse) | Gannon §6.3.3 [opened]; Bakalov-Kirillov [memory] |
| 13 | The Weil representation 30+6,10,15: E8³ umbral form (χ₀, χ₁), false theta of Σ(2,3,5) | The two non-abelian flat connections of Σ(2,3,5) = the two non-trivial classes of 2I → SU(2); as a representation of B it is (multiplier of η³) ⊗ (modular data of (G₂)₁, the Fibonacci category): −14/120 + 15/120 = 1/120, 34/120 + 15/120 = 49/120 | identity of T-matrices [computed]; of S-matrices not checked | exponents [MAP]; c = 14/5, h = 2/5 [memory]; sum [computed] |
| 14 | Cappelli-Itzykson-Zuber: D₄ = Ω₆(1) + Ω₆(3); E8 = Ω₃₀(1) + Ω₃₀(6) + Ω₃₀(10) + Ω₃₀(15). The D₄, E₆, E₈ invariants come from SU(2)₄ ⊂ SU(3)₁, SU(2)₁₀ ⊂ SO(5)₁, SU(2)₂₈ ⊂ (G₂)₁ | SU(3) and G₂ = Aut 𝕆 of the user's card; the main session's Valentiner group 3·A₆ ⊂ SU(3); 3.Sym₆ ⊃ 3.A₆ is the umbral group of D₄⁶ | identity for the table; the embeddings and "3.A₆ in 3.Sym₆ is the Valentiner group" [memory] | CDH Table `ADE1` [opened] |
| 15 | E8 as the icosian ring; "the icosian group is the perfect double cover 2.A₅"; the Leech lattice as a three-dimensional icosian lattice | π₁ of PRETOT's complex P and of Σ(2,3,5): the image of ℤ[2I] in the quaternions is E8; three copies with glue give Leech | functor | SPLAG Ch. 8 §2.1-2.2 [opened] |
| 16 | The Leech lattice as triples of octonions (Wilson); cyclic symmetry, coinvariant A₂ ⊗ E8 | The user's S6 workbench, Thm `wcl:thm:Leech`, `wcl:thm:fixed-coinvariant` | identity | [MAP] |
| 17 | Leech: the one Niemeier lattice without roots; the 23 others ↔ deep holes; umbral groups ↔ stabilizers of deep holes | The user's lattice J (six Leech and two A₂¹² overlattices). Speculation: the 24 classes as the cusps of one arithmetic quotient (of the even Lorentzian lattice of rank 26), the umbral groups as the finite parts of the groups at the cusps | identity for J; the rest analogy | CDH §1, §2.2 [MAP]; Conway's picture [memory] |
| 18 | Genus-zero property = the Hauptmodul is the Rademacher sum of its polar part q⁻¹ | A function on the curve determined by its polar part at one cusp. Speculation: the obstruction space is the weight-two cusp forms, i.e. the holomorphic differentials, i.e. the weight −1 part of π₁^ab of the cover; genus zero = π₁^ab purely of Tate type | analogy | TASI §4 (text after (4.8)) [opened]; the obstruction statement [memory] |
| 19 | Mock modular form, its shadow, its completion; false and mock theta "have the same asymptotic expansion at all cusps" | A cochain that is a cocycle at every finite level without being one globally: the phantom classes (LM7 E.32, LM8 F.21), and elements whose every pro-ℓ shadow is geometric (E.58) | analogy | 3dMR §1 [MAP]; our handoffs |
| 20 | Ogg: Γ₀(p)+ has genus zero iff p divides the order of the Monster (15 primes) | The primes p for which every supersingular point of M_{1,1} ⊗ F_p is F_p-rational; p-rank zero is the condition of A.C2.20 | analogy for A1 | TASI (4.8) [opened]; the supersingular form [memory] |
| 21 | x²⁴ + x + t has Galois group M₂₄ over F₂(t); x²³ + x³ + t gives M₂₃; x¹² + x + t and x¹¹ + tx² − 1 give M₁₁ over F₃(t); proof by an additive polynomial (the roots span an F₂-space of dimension 12) | Finite étale coverings of the affine line in characteristic p (x ↦ x²⁴ + x is étale on A¹ in characteristic 2), i.e. quotients of π₁(A¹) in characteristic p; additive polynomials occur in LM8 B.24d | identity | CMT §1 [opened] |
| 22 | M₂₄ = ⟨a, b⟩, a in 2B, b in 3A, ab of order 23 | A quotient of the oriented cartographic group; cycle types 2¹², 3⁶1⁶, 23·1 on 24 darts give genus 0: a planar dessin with 24 darts and cartographic group M₂₄. PSL₂(23) on the same 24 points (3⁸) gives X₀(23), genus 2 | functor | generators [memory]; genera [computed] |
| 23 | Triangulations of the sphere and the Eisenstein integers: "the square-norm of a lattice point gives the number of triangles" | Dessins that are triangulations = subgroups of B; composition with a Lattès map of the curve j = 0 subdivides (**[mine]**, 4.5) | functor | HGA Thm 6.5 [opened], special case of Thurston's theorem [memory] |
| 24 | Thurston, Deligne-Mostow: 12 points on the sphere with weights 1/6 ↔ a ball quotient by an Eisenstein lattice of signature (1,9) | M_{0,[12]}, the multiplicity of the Boggi question; the icosahedral point x₀ is a point with finite isotropy A₅ of that ball quotient | identity | [memory]; HGA cites both |
| 25 | Coxeter: B₃/⟨⟨σ^k⟩⟩ has order 24, 96, 600 for k = 3, 4, 5 | The trefoil group filled at distance N = 3, 4, 5: `POINCARE_AND_A5` Theorem 1 (2I × C₅ at N = 5) | identity | formula [memory]; values [computed] |

## 2. The bridges already outlined: checked, corrected, refuted

From `MAIN_SESSION_NOTES_20261114.md` (Claude Opus 5.5 at effort max) and MAP.md.

- **"E8 is the icosian ring, and the Leech lattice is a three-dimensional icosian lattice (Tits 1980) [memory]."**
  Checked: SPLAG Ch. 8 §2.1 ("the icosian ring is isomorphic to an E8 lattice"), §2.2 [opened]. The attribution to
  Tits I did not check. MAP.md §1 left this route open; it is closed as a statement.
- **"The extended Golay code is [I | J − A] with A the adjacency matrix of the icosahedron."** Not found by a search
  of SPLAG for "icosahedron"; stays [memory]. The remark "it gives no quotient of the mapping class group" needs a
  correction of scope: M₁₂ and M₂₄ give finite-index subgroups of Γ_{0,[12]} through the permutation of the
  punctures only, and LM4 F.7 already has the two sides equal in that quotient.
- **"12 punctures taken twice."** Sharper: 24 = 5² − 1 is the number of non-zero vectors of F₅², the 12 cusps of
  X(5) are these up to sign, and 2I = SL₂(F₅) acts on them transitively with stabilizer C₅ [mine]. So "24 = 2 × 12"
  at level 5 is the plane F₅² minus the origin.
- **"Rank 24 is where the eta phase cancels; 4 × 6 = 24 in Mp₂(ℤ)."** Consistent with row 9: η is a vector of the
  Weil representation of index 6, level 24 [computed]. Not re-derived: Mp₂(ℤ)^ab = ℤ/24.
- **"The genus-zero levels X(N), N = 2, 3, 4, 5."** Correct, and the moonshine side has the matching list: Γ₀(n) has
  genus zero exactly for n = 2, …, 10, 12, 13, 16, 18, 25, the Coxeter numbers of the A-type Niemeier root systems
  (CDH (`a_type_coxeter_list`)) [opened]. The two lists meet at level 5 in a way neither note says (S1).
- **"A₆ is a (2,4,5) quotient, not on the modular (2,3,N) tower"; the Valentiner group.** New on the moonshine side:
  3.Sym₆ is the umbral group of D₄⁶ (CDH table) [opened]. So the SU(3) analogue of 2I that Claude Fable 5.2 at effort
  max named is inside an umbral group, as 2I is inside 2.M₁₂ at ℓ = 3. That the 3.A₆ in 3.Sym₆ is the Valentiner
  group is [memory] (the group of the hexacode).
- **"H⁴(Co₀; ℤ) = ℤ/24", "the moonshine anomaly", the E8 phase.** Not checked. No source on disk was opened for them.
- **A route [hunch]: level-5 quantum SO(3) (Fibonacci) representations.** Supported from an unexpected side: row 13.
  The representation that carries the E8³ umbral form and Σ(2,3,5) is the Fibonacci modular data up to the η³
  multiplier.
- **MAP.md §5.5, "2I is not the umbral group of the case carrying χ₀, χ₁".** Stands (E8³ has Sym₃). To add: A₅ and
  its arithmetic extension are the umbral groups at ℓ = 5 (row 5).
- **MAP.md §5.6, Deligne's series: "no statement found".** Row 14 gives a first one: the E8 end of the
  Cappelli-Itzykson-Zuber list is an embedding into G₂ at level 1, the D₄ entry into SU(3) at level 1. It is from
  memory and concerns the conformal embeddings, not Deligne's dimension formula.

## 3. Surprises

Ranked by how much they surprised me.

**S1. Level 5 is the self-dual point of the umbral A-series, and the umbral group there is our arithmetic A₅.**
For X = A_{ℓ−1}^{d} the lambency ℓ (the level of the Hauptmodul) and the prime p (the components form P¹(F_p)) satisfy
(ℓ − 1)(p + 1) = 24. The pairs are (2,23), (3,11), (4,7), (5,5), (7,3), (9,2), (13,1), (25,0) [computed]. Only ℓ = 5 has
ℓ = p: 5² − 1 = 24. There G = GL₂(5)/2 and Ḡ = PGL₂(5) (CDH) [opened]: the group of X(5) over X(1) over ℚ, and
Aut(A₅). Our icosahedral question is posed in exactly this group: an element of ĜT₀ acts on A₅ through 𝔖₅ = PGL₂(5),
inner iff λ ≡ ±1 mod 5. I expected 2I only at ℓ = 3 (MAP.md); I did not expect the level-5 arithmetic group to be an
umbral group, nor a reason on the lattice side for the icosahedron to be singled out. Why it matters: the
"icosahedron is unique" of the main session's notes §1 has a third form, 5² − 1 = 24.

**S2. The tripod is in the umbral table.** Γ₀(4) is the tripod, and CDH attach to it A₃⁸ with T = q⁻¹ − 8 + … [opened].
The constants of our tripod work are Hauptmodul constants: the 16 of λ = 16q^{1/2} + … is the 16 that LM6 F.45, F.46
"select" for tangential sections (±16, per `KNOWLEDGE_HANDOFF_ANABELIAN_149.md` §6) [the match is mine; λ's expansion
from memory]. The first three A-type cases are the tripod and its two quotients by a symmetry (rows 1-3). So the
objects the author starts from are the first entries of Niemeier's list.

**S3. The frame "5I mod 12" of E.58 is an Atkin-Lehner symmetry with a name.** The centre of SL₂(ℤ/12) is {1,5,7,11}.
In the theory of index-6 Jacobi forms this is the group of Eichler-Zagier operators, 5 = a(3), 7 = a(2), 11 = a(6)
[computed from CDH's definition]. The operator of 5 is the one that makes D₄ out of A₅ (CDH Table `ADE1`), i.e.
lambency 6+3, the lattice D₄⁶; 11 is the Fricke involution. In E.58 and the Fermat tower's D.46 the non-Galois
elements have "unequal bits", i.e. frames 5 or 7; Galois elements have 1 or 11. And index 6 is the case of the user's
own lattice N(A₅⁴D₄). Two lines of work that never met use the same four numbers for what looks like the same
purpose.

**S4. One two-dimensional representation carries the E8³ umbral form, Σ(2,3,5), G₂ and the Fibonacci hunch.** Row 13:
the T-matrix of 30+6,10,15 is that of (G₂)₁ times the η³ multiplier [computed]. The two components χ₀, χ₁ would
correspond to the two simple objects 1, τ of the Fibonacci category. This joins the user's octonion bridge (MAP.md
§5.7 had found no statement) to the main session's hunch for the Boggi question, through the representation MAP.md
was about.

**S5. Galois's last letter is on both sides.** PSL₂(p) has a subgroup of index p only for p = 5, 7, 11. CDH Table 4
is built on exactly these three [MAP]. The Poincaré read-in (Claude Fable 5.2 at effort max) built the quintic
resolvent endomorphism 𝔗_T from the case p = 5. The two other cases have the same shape: the index-p subgroup of B
has genus 0 and one cusp, with (e₂, e₃) = (1,2), (3,1), (3,2) for p = 5, 7, 11 [computed]. So 𝔗_T has two siblings,
and the one at p = 11 has the icosahedral A₅ as its finite group again (A₅ ⊂ PSL₂(11) ⊂ M₁₂).

**S6. Gannon states the gap that Δ fills.** Gannon §6.3.3 [opened] writes the Galois action on modular data,
notes that it sees only Ẑ^× and SL₂(Ẑ), and says it "is not directly related to Grothendieck's". Our refereed E.58
element is an element of ĜT₀ with multiplier 1 whose frame is diag(5, 5⁻¹) mod 12: the operator of the cyclotomic
element 5 without the cyclotomic character 5. That is a precise object sitting between the two actions. The RCFT
literature has studied the left side for thirty years (Coste-Gannon, Bantay, Dong-Lin-Ng [memory]).

**S7. M_{0,[12]} is a lattice quotient, and twelve is the last case.** The multiplicity of the Boggi question is the
Thurston / Deligne-Mostow ball quotient for the Eisenstein lattice of signature (1,9); among equal weights 2/N the
integrality condition holds for N = 4, 5, 6, 8, 12 and fails after [memory, the condition recomputed by hand]. The
icosahedron is forced to 12 by the orbit of its vertices; Thurston's list stops at 12 by Gauss-Bonnet. The Leech
literature reaches this lattice (Allcock: E8 ⊕ E8 ⊕ hyperbolic plane over ℤ[ω], inside Leech ⊕ hyperbolic plane)
[memory]. This gives the icosahedral centralizer an arithmetic model that our notes do not have (4.2).

**S8. Mathieu groups are fundamental-group quotients in two of the author's settings.** As cartographic groups
(row 22: a planar dessin with 24 darts) and as groups of étale coverings of the affine line in characteristic 2 and 3
(row 21, CMT [opened]). The proof for M₂₄ is by an additive polynomial, the tool of LM8 B.24d.

**S9. What did not surprise, and one thing that is absent.** The Rademacher / phantom analogy (rows 18, 19) is the
pattern the Longue Marche expert already named ("local data at every prime, global class in a lim¹"). Absent: I
found nothing on the moonshine side that bears on F.9, and almost nothing on A1 (4.6).

## 4. Hunches for our work

Each is placed against a result or stuck point of ours, with the item for GPT-6 Astra (ChatGPT Pro mode). All
hunches are mine and unchecked. The items are statements of the task; the prompts are for the field experts to
write and lint.

### 4.1 Δ, and "is Δ = 0 on ĜT" (LM7_PUSH E.3)

**Our state.** Δ : ĜT₀ → F₂ is continuous, zero on G_ℚ, one on the element of E.58 (refereed by Claude Opus 5.5 at
effort max). It is read from frames modulo 12. Whether it vanishes on ĜT is open.

**What the bridge says.**
1. *Δ should be the class of the frame in {1,5,7,11}/{±1}.* For F of multiplier one the central part of the frame
   pair lies in the centre of SL₂(ℤ/12); Galois elements give 1 or 11 (equal bits), E.58 gives 5, D.46 gives 7.
   {1, 11} is {identity, Fricke}; {5, 7} are the two non-Fricke Atkin-Lehner operators of index 6 (S3). Hunch.
2. *Why Galois elements cannot give 5 or 7.* By Gannon (6.3.4) a Galois element acts on level-N data by
   diag(χ, χ⁻¹), so the operator a ∈ {5, 7} comes only with cyclotomic character a; multiplier one leaves ±1. Our
   refereed proof goes through the field ℚ(E₃[4]) = ℚ(x(E₄[3])); this would be the same fact read on the Weil
   representation of index 6. In the author's terms: on the multiplicity M_{1,1} the generic automorphism −1 is
   one sign for the 2-part and the 3-part of the level; an element with frame 5 changes the sign at the
   equianharmonic point and not at the harmonic point. Hunch.
3. *Why the pentagon should force Δ = 0.* Drinfeld's action of (λ, f) ∈ ĜT on a braided category needs the pentagon,
   and on a pointed braided category (an abelian group with a quadratic form) it acts through λ alone: f lies in
   the commutator subgroup and the braid action is abelian. The Weil representation of index 6 is the modular data
   of the pointed category (ℤ/12, x²/24). If Δ is the action on that category modulo ±1 (point 1), then Δ = 0 on
   ĜT, and elements of ĜT₀ outside ĜT escape because they do not act on braided categories at all. The gap in this
   reasoning: Δ is defined by frames on B̂ = π̂₁ of the modular orbifold (also of M_{0,[4]}), and the passage from
   the braid data of a category to its S and T is the genus-one-from-genus-zero step of the Lego game. Hunch, at
   about three to one that Δ = 0 on ĜT.

**Item M1 for GPT-6 Astra (ChatGPT Pro mode).** Prove or refute, in this order:
(a) for F ∈ ĜT₀ of multiplier one, the image of the pair of frames (β_F, A_F) in PSL₂(ℤ/12) lies in the image of
the centre {1,5,7,11}, and Δ(F) is its class modulo ±1; give the formula for general multiplier;
(b) F acts on the twelve theta functions θ_{6,r} (the Weil representation of Mp₂(ℤ) of index 6), compatibly with
(a), by r ↦ ar up to the signs of the Galois action on modular data; compute it for the element of E.58 and for the
candidate of LM7 D.46;
(c) for (λ, f) ∈ ĜT, compute the action on the pointed braided category (ℤ/12, x²/24) and on its modular data, and
decide whether it forces Δ(λ, f) = 0; state exactly where the pentagon is used and check that the element of E.58
fails there;
(d) the same with ℤ/2m for m = 12 and m = 30, and decide whether new characters of ĜT₀ of the kind of Δ arise from
the non-Fricke exact divisors (for m = 30 the exact divisors 6, 10, 15 are the E8 case).
Background: the referee reports in `pro_intake_20261114\referee\`; LM7_PUSH sections D.50, E.58, E.61, E.65; CDH
`UMNL_x2.tex` §§ on exact divisors and Eichler-Zagier operators; Gannon §6.3.3; Dong-Lin-Ng on the congruence
property; Drinfeld 1990 §4; Kassel-Turaev; the user's `niemeier_umbral_shadow.tex`.

### 4.2 The icosahedral centralizer (item 2.4; Conjecture 2⁻): an arithmetic model

**Our state.** 𝒦 = {F of multiplier one whose icosahedral lift lies in Γ̂_{0,[12]}}; finite or not is open; no
nilpotent or metabelian quotient can decide; the Longue Marche expert asks for "quotients in which the primes mix".

**What the bridge says.** The Eisenstein-lattice representation (S7) is such a quotient, and in it the question
becomes linear algebra over ℤ[ω].
1. Γ_{0,[12]} maps onto an arithmetic lattice Γ_DM in PU(1,9) over ℤ[ω]; the half-twists go to elements of order 3
   [memory]. The icosahedral A₅ fixes one point of the ball. By the tangent computation of the Poincaré read-in
   (T_{x₀} = V₄ ⊕ V₅, no invariant vector) the representation of A₅ on ℂ^{1,9} is a line plus V₄ plus V₅, so the
   centralizer of A₅ in the unitary group is a torus T of rank 2 after dividing by scalars: compact at infinity,
   finite in Γ_DM [mine].
2. In the congruence completion the centralizer is T(Ẑ) ∩ (closure of Γ_DM), and by strong approximation for the
   special unitary group that closure is open. So **in the congruence completion of this quotient the centralizer
   of A₅ is infinite while the discrete one is finite**: the equality of the two published proofs fails there
   [mine; a standard failure of strong approximation for a torus that is compact at infinity]. This does not
   decide 𝒦: a centralizing element of the quotient need not lift to a centralizing element of Γ̂_{0,[12]}. The
   lifting is an H¹(A₅, ·) question with coefficients in the profinite kernel, of the kind in item 2 of
   `NOTE_BOGGI_ZALESSKII_STEP.md`.
3. The same construction exists at levels 3 and 4 (4 points with weights 1/2; 6 points with weights 1/3 [memory]),
   where the centralizer in the full completion is known to be finite. So the model lets one see *where* the
   lifting fails there and whether the same obstruction is present at 12 points. That comparison is what our notes
   lack: the Poincaré read-in found the three levels alike in every respect it could test.
4. *Icosahedral CM characters.* Every F ∈ ĜT₀ with λ ≡ ±1 mod 5 commutes with A₅ on the completed group of Y(5),
   hence acts on the ω-part of H₁ of the 6-fold cyclic cover branched at the 12 cusps through the centralizer of
   A₅: three characters χ₁, χ₄, χ₅ with values in units of Ẑ[ω]. That cover is modular: it is the fibre product of
   X(5) with the curve of the commutator subgroup of B (the once-punctured curve j = 0), of level 30 [mine]. On
   Galois elements the three characters are Hecke characters of a CM field (the multiplicities are one). They are
   the analogue at the icosahedral point of the CM pair (T, W) at the harmonic and equianharmonic points, which
   the Poincaré read-in asked for ("the icosahedral point is the next point of that kind"). On 𝒦 they give a
   homomorphism to an abelian group; a non-trivial value would prove Conjecture 2⁻. Hunch: they are not all
   trivial on the multiplier-one part ℋ, and whether they vanish on 𝒦 is the decision in a computable form.

**Item M2 for GPT-6 Astra (ChatGPT Pro mode).** Prove or refute:
(a) the statement of point 1 with sources opened (Deligne-Mostow; Thurston, *Shapes of polyhedra*; Allcock), the
decomposition of ℂ^{1,9} under A₅, and the torus T with its field of definition;
(b) point 2: the centralizer of the image of A₅ in the closure of Γ_DM in PU(Λ ⊗ Ẑ) is infinite; the same at 4 and
6 points;
(c) the characters χ₁, χ₄, χ₅ on {λ ≡ ±1 mod 5}: that they are homomorphisms, their values on G_ℚ(ζ₁₅) as Jacobi-sum
characters, and their values on the multiplier-one elements produced by LM7_PUSH E.58 with U = Γ(5)/±1 and with
U the level-30 subgroup;
(d) for each prime ℓ not dividing 30: is every element of T(ℤ_ℓ) in the image of the centralizer of A₅ in
Γ̂_{0,[12]}? Compute the obstruction class in H¹(A₅, ·) for the kernel of Γ̂_{0,[12]} → PU(Λ ⊗ ℤ_ℓ); do the same
computation at 4 and 6 points, where the answer must be "no" by Herfort-Ribes and the solvable case, and locate
the step that makes it "no" there;
(e) conclude for 𝒦: either an element of 𝒦 with a non-trivial character (then Conjecture 2⁻ holds, with the element
written out), or the vanishing of the three characters on 𝒦 together with the next test, the Fibonacci
representations of Γ_{0,12} (rows 13, 14), treated in the same way.
Background: `NOTE_BOGGI_ZALESSKII_STEP.md`, `EXPERT_ON_BOGGI_A5.md`, `POINCARE_AND_A5_20261114.md`, item 2.4 of
`PUSH_ITEMS_20261114.md` with its block R1-R12, the LM4 return's F.7-F.32, the two TeX sources of Boggi and
Boggi-Zalesskii, Deligne-Mostow (`Commensurabilities among Lattices in PU(1,n)` is in the moonshine library folder),
HGA.

### 4.3 Three resolvent maps, not one (the Poincaré read-in's 𝔗_T)

**Our state.** 𝔗_T is defined on the index-2 subgroup (−15/λ) = 1 of ĜT₀ from the index-5 subgroup of B; it fixes
the Galois group of ℚ(√−15) and kills 𝒦 (unrefereed). Open: is 𝔗_T(F) = F on ĜT (statement R6).

**What the bridge says (S5).** The umbral table treats p = 5, 7, 11 as one family. The index-7 subgroup (over 𝔖₄ in
PSL₂(7)) is C₂ ∗ C₂ ∗ C₂ ∗ C₃ with one cusp; the index-11 subgroup (over A₅ in PSL₂(11)) is C₂^{∗3} ∗ C₃^{∗2} with
one cusp [computed from the fixed-point counts]. Forgetting all but one point of order 2 and one of order 3 gives
maps to B, cusp to cusp. Hunch: each gives endomorphism-type maps 𝔗⁽⁷⁾, 𝔗⁽¹¹⁾ of open subgroups of ĜT₀, Galois
elements over a quadratic field are fixed, and "𝔗(F) = F" for all of them is a family of level-p equations of the
Nakamura-Schneps kind. The case p = 7 belongs to the Klein quartic, Conjecture 3 of the note.

**Item M3.** Define the three families of maps; prove that they are continuous homomorphisms on the stated open
subgroups; find the field over which Galois elements are fixed (ℚ(√−15) for p = 5; decide it for 7 and 11);
prove or refute 𝔗(F) = F on ĜT for each; decide whether the common fixed subgroup is G_ℚ's closure-type condition
of the kind the author asks for in cote 143 ("structure « locale » éventuelle"). Background: `POINCARE_AND_A5`
§5.2 and R1-R12; CDH §2.5; Nakamura-Schneps 2000.

### 4.4 Sections of the tripod over ℚ (LM6 B.27 = ANABELIAN D.U1; D1 and its two gaps)

**Our state.** D.31: one cusp label suffices; gap (2) is two labels at finitely many places. D.32: full-level
neighbourhoods give no unit. Fermat curves of odd degree are settled for Selmer sections; x⁴ + y⁴ = z⁴ is not.

**What the bridge says.**
1. *One cusp instead of three.* On the moonshine side the passage Γ₀(p) → Γ₀(p)+ merges the cusps. For the tripod
   the corresponding move is the map j, of degree 6, to the modular orbifold with its one cusp. The function
   u = 1 − 1728/j is a unit on the tripod minus the harmonic points −1, 1/2, 2 and the equianharmonic points; it
   equals 1 at each of the three cusps. So after removing those five points, D.31's unit exists for any set of cusp
   labels [mine]. The price is the lifting of the section to the smaller curve, which is the reciprocity condition
   of ANABELIAN D.27, D.28 at the added points (the run tested the added point 2, which is a harmonic point).
   Hunch: gap (2) reduces to: a non-cuspidal section avoids the harmonic and equianharmonic points at almost all
   places, or is one of them.
2. *The Gaussian case.* The lattice side knows two crystallographic quotients of the tripod: Eisenstein
   ((3,3,3), (2,3,6); the Fermat cubic) and Gaussian ((2,4,4); the Fermat quartic) (HGA treats triangulations and
   quadrangulations as the two cases [opened]). LM6 used the first. Hunch: the quartic is within reach by the
   second, because its three elliptic quotients have complex multiplication by ℤ[i] or ℤ[√−2] and rank zero over
   ℚ [memory], so the finite-descent argument of LM6 E.6 applies.

**Item M4.** (a) Prove or refute: for a section s of the tripod over ℚ and the open subcurve U′ (tripod minus the
five points), s lifts to U′ exactly under the reciprocity condition of D.27 at each removed point; and if it
lifts, D.31 with the unit u makes s a rational point whenever the local sections are integral at almost all
places, whatever the cusp labels. (b) Prove or refute: every Selmer section of the affine Fermat quartic over ℚ is
cuspidal. (c) With (a) and (b), restate what is left of D1. Background: the two final intakes of 14 November; LM6
sections E.6-E.12; ANABELIAN sections D.25-D.32.

### 4.5 Lattès maps as an action on dessins

**What the bridge says (row 23).** Subdividing every triangle of a triangulation by an Eisenstein integer α is,
on Belyi functions, composition with the Lattès map L_α of the curve j = 0 (the map induced by multiplication by α
on E/μ₆, whose orbifold is (2,3,6)) [mine, by the ramification count; "Belyi Lattès maps" is the title of a
preprint of Zeytin cited in HGA, not opened]. These are self-correspondences of the tripod of the kind the Longue
Marche expert asked for in Path (v) ("the covers the tripod has of itself"), an infinite commutative family with
complex multiplication, defined over ℚ(ω). The Gaussian family acts on quadrangulations. HGA asks whether "an
analogue of the Grothendieck-Teichmüller group" arises from this web [opened].

**Item M5.** Prove or refute: (a) the statement on L_α; (b) the action of G_ℚ(ω) on dessins commutes with all L_α, and
the action of ĜT₀ commutes with them exactly on the subgroup where the CM coordinate T (LM7 D.25) is that of a
Galois element; (c) the Lattès semigroup acts on the set of sections of the tripod, and a section fixed up to
conjugacy by infinitely many L_α is a point or a cusp. Background: HGA; LM7 D.15-D.25; the LM8_PUSH lead on §47 as
a fixed-point condition (handoff §5.3).

### 4.6 A1 (points of proper curves in characteristic p) and F.9

**What the bridge says, honestly.** Little. The condition of A.C2.20 (a primitive part of p-rank zero) is the
supersingular condition, and Ogg's theorem is a statement about where supersingular points are rational (row 20).
I found no theorem on the moonshine side that produces p-rank-zero covers of a given curve. Two leads only:
- the CMT coverings (row 21) are explicit coverings whose deck group acts faithfully on an F_p-space spanned by the
  roots; they are wild, not prime to p, so they do not enter A.C2.7 as stated, but they are test objects for the
  non-abelian form of the criterion that the intake asks for;
- for F.9 nothing.
No item.

### 4.7 What it suggests the author was working on

In his register, each a hunch:
- *The multiplicity M_{1,1} over Spec ℤ.* The harmonic and equianharmonic points are two sections that meet over
  the primes 2 and 3 (1728 = 2⁶3³), and Δ lives exactly there. The numbers 12 and 24 of the modular group are the
  orders of the automorphism groups of the supersingular curves in characteristics 3 and 2 [memory]. The frames of
  cote 145 at "P and the harmonic points" are his access to this.
- *The cartographic group has the sporadic groups among its quotients* (rows 4, 22), with planar dessins. The
  umbral table is a table of dessins: p + 1 darts, cartographic group PSL₂(p), enlarged to a Mathieu group for
  p = 23, 11.
- *The Lego game was rebuilt in physics* as the Moore-Seiberg equations (row 12), and the Galois side of that
  rebuilding stops at the cyclotomic character. What the author wanted beyond it ("structure « locale »", cote
  143) is what Δ and the 𝔗-maps start to give.

## 5. What I read and what I did not

**Read for this note.** The user's words P5023-P5026; the brief; the main session's notes; the Longue Marche
expert's handoff (all sections) and `UNSTUCK_LM_EXPERT.md`; `KNOWLEDGE_HANDOFF_POINCARE.md` and
`POINCARE_AND_A5_20261114.md` (all); `EXPERT_ON_BOGGI_A5.md`, `NOTE_BOGGI_ZALESSKII_STEP.md`,
`KNOWLEDGE_HANDOFF_ANABELIAN_149.md` (all); `INTAKE_20261114.md` §§9, 10, 11.2, 11.6, 12, 13.4, 13.6, 14.1, 14.2, 15,
16; `INTAKE_ANABELIAN_149_FINAL_20261114.md` §§0, 1.2, 1.3, 3; the outline of `INTAKE_LM6_FINAL_20261114.md` (its
content through the handoff §6). Moonshine side: CDH LaTeX (the two tables, Prop. `prop:TX`, exact divisors,
`def:OmegaMatrices`, Table `ADE1`); TASI (Ogg, Rademacher, optimal mock Jacobi forms, weight 3/2); Gannon §6.3.3;
SPLAG Ch. 8 §2.1-2.2; CMT §1; HGA pp. 484-494 in part; first pages of six papers in `Papors\OS`.

**Not read.** `INTAKE_20261114.md` §§11.3-11.5, 13.1-13.3, 13.5, 14.3, 14.4; the LM6 intake beyond its outline; any
return, section or program of GPT-6 Astra; the referee reports. Moonshine side, not opened: Thurston;
Deligne-Mostow; Allcock; Chenevier-Lannes; Borcherds; *Optimal Mock Jacobi Theta Functions*; *Class numbers,
congruent numbers and umbral moonshine*; *Umbral Moonshine and Linear Codes*; Curtis on M₂₄; the proof of umbral
moonshine beyond what MAP.md used; Dong-Lin-Ng; Drinfeld; Kassel-Turaev. Every statement resting on these is
flagged [memory].

**Most in need of a check before use.** (1) Row 13 beyond the T-matrix: the S-matrix of 30+6,10,15 against
Fibonacci. (2) S7 and 4.2 point 1: the Deligne-Mostow statement at 12 points and the A₅-decomposition. (3) 4.1
point 1: that Δ is the class of the frame in {1,5,7,11}/±1; it is read off the summaries in our intakes, not off
E.65 itself. (4) 4.4 point 1: the unit u and the lifting condition. (5) The 16 of S2 against LM6 F.45, F.46.
