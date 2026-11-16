# Lifting and Lie audit: outcome table

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026. This is a research module for incorporation into the main return; it does not claim to decide the main value of Δ on profinite GT.

| Prompt item / attached row | Outcome | Exact local proof |
|---|---|---|
| P.2: strict profinite GT ⊊ GT₀ | **Proved using stipulated R1** | LP.1–LP.5 in `lifting_results.tex`; actual integral pro-ℓ realization, genuine S₃-fixed outer lift, normalized group pair, nonzero pentagon coefficient 16, retained full pro-ℓ image. |
| LM7_PUSH D.51 / D.1 | **Proved** | LB.1; three independent special free-Lie vectors checked and integrated. Rational dimension 3 holds also at 2 and 3 by scaling at 2; no coprime S₃ step is needed here. |
| LM7_PUSH D.52 / D.2 | **Proved for ℓ ≥ 5** | LB.2; all 42 coefficients of 2h₉ checked independently. Full invariant degree-nine kernel has dimension 4, metabelian image dimension 2. |
| D.20 pentagon upper bound, all lifts | **Proved from opened Enriquez theorem** | LB.3: every first-degree-nine class with meta coefficient P₉ is excluded, regardless of the other degree-nine and higher terms. The separate Galois lower-bound assertion of D.20 was not needed and is not asserted proved by this module. |
| D.21 unrestricted weight-five upper bound | **Proved** | LB.1; special equation forces divisibility by X+Y, and the S₃ decomposition gives dimensions 1 or 3 before the explicit realization settles 3. |
| LM6 A.10, A.49 = LM8 A.22 unit construction | **Proved** | LU.1–LU.2 in `lifting_units.tex`; actual automorphisms, composition, peripheral conjugators, continuity, outer injectivity, scalar/S₃ invariance, and cases 2 and 3. |
| LM6 A.56–A.58, next-derived arithmetic obstruction | **Proved by audited argument** | LU.3–LU.5; independent center-free transfer proof, exact arithmetic normalization, finite torsor, Hilbert/Chebotarev specialization, constant-twisted Kummer fiber isolation, and retained cohomology. |
| Reconciliation of metabelian obstruction with D.1 | **Proved** | LU.6. R1 lifts peripheral maps, not the additional Galois-commutation requirement. The unit classes are invisible on every absolute pro-prime quotient. |
| B.5: LM7 D.46 meets R2 and has pair (I,[i]) | **Proved using stipulated R2** | LB.5; repaired arithmetic input needs only Frobenius at 7, not unrefereed LM7 D.35's full 2-adic image theorem. All retained relative conjugators and the mixed base are specified. |
| B.5: complete corrected frame image | **Proved** | LB.4: H → C₆×C₄ is onto; G_Qab has exactly the cyclic order-12 equal-parity subgroup. Exact signed twist comparison from referee R4 is written out. |
| B.5: manuscript (γ,χ), scan-12 β, and β=ρ | **Injectivity proved; unrestricted dictionary corrected; β=ρ false** | LD.1–LD.2 in `lifting_manuscript.tex`: β=(λ−1)/2, normalized g=f⁻¹y^((1−λ)/2), arbitrary-gauge canonical f=yᵇg⁻¹xᵃ. The literal g=f⁻¹ dictionary holds at multiplier one; its general version misses the half-cyclotomic factor. |
| B.6(a): V×F₂ surjectivity | **Proved** | LB.6; R_nil(U) ⊂ R_nil(F) and R2's witness toggle Δ in the kernel. Stronger H → V_H×F₂² follows with the D.46 lift. |
| B.6(e): CM parities equal LM8 B.31 exponent signs | **False** | LB.7; torsion-generator powers are forced by μ via the actual abelianization Z/12. R2 at μ=1 has positive exponent signs but CM parity (1,0). |
| A.7: product decomposition with the pentagon | **Coordinatewise quotient statement proved; full restricted lifting unresolved** | LX.1–LX.4 in `lifting_pentagon_gap.tex`. Word equations commute with actual relative products. R1/R2 do not lift the correlated five-evaluation constraint. No counterexample to the stronger lifting assertion is claimed. |
| A.3: explicit b,d cocycles and the exact forgetting map | **Proved** | LF.1–LF.2 in `lifting_five_cocycles.tex`: full words in f, primitive equations, norm identities, and q(c_b)=f⁻¹, q(c_d)=r⁻¹fr. Their displayed modular relation adds only an existing gentle identity. |
| A.4(a,c): literal positive-marking descent D and Fix D | **Normalized formula proved; claimed Galois fixedness refuted** | LC.1–LC.4 in `lifting_descent.tex`. Actual pure and signed frames are computed. Direct NT identities prove D(σ)=cσc for σ∈G_Qab. A degree-16 Galois commutator has ρ₂=2 mod8 while its descent has ρ₂=6 mod8. The LM2 fixed-point convention requires D*=Ad(c)∘D. |
| Attempt to force Δ∘D=0 from finite evaluations | **Not proved by the exact common-word test** | LC.5; six-evaluation group and seventh original inclusion evaluated exactly, retaining twelve necessary residues in each parity. These are not asserted to lift to any genuine profinite pair or pentagon solution. |
| Kernel of descent and iterated quadratic characters | **Actual profinite theorem proved using R2** | LI.2–LI.4 in `lifting_iterates.tex`: uniform word A₀=[[x⁴,y⁴],z⁴]² lies in every full conjugate φ-kernel but has original frame residue5I. Coprime lifting and compactness give k∈kerD with Δ(k)=1. Thus D is noninjective; both fixed subgroups are proper; every positive iterate ΔDⁿ differs fromΔ. |
| Genuine affine pentagon obstruction and all quadratic iterates | **Actual profinite witness proved using R2** | LI.5–LI.6: explicit S₃-kernel seeds give an actual pair a_f=0,ρ=−1 mod3. Its pro-3 power still fails the genuine affine pentagon, is absolutely pronilpotently invisible, and vanishes under every ΔDⁿ, n≥0. No vanishing of these characters on all GT is assumed. |
| Corrected fixed subgroup versus ker Δ | **Equality refuted** | LI.4: k² is nontrivial by R7, belongs to ker Δ∩ker D, and lies in neither fixed subgroup. The pro-2 component of k generates a closed Z₂ in ker D on which Δ is reduction mod2. No pentagon assertion is made about this subgroup. |
| Full third-derived and cover homology detection | **Actual invisibility proved; derived-length threshold sharp with FP.35** | LI.8: A₁=[[x⁴,y⁴],[y⁴,z⁴]] lies in F″ and every full orbifold kernel, with q₁₂(A₁)=5I. Relative lifting and compactness give f,β∈R_nil(F″)⊂F‴, A∈F″, Dk=1, Δk=1. Thus Δ cannot be detected by any finite B-source action of derived length≤3; the independent length4 detector makes this sharp. Canonical Alexander and stable finite metabelian-cover homology have no Δ-line in characteristic≠2. |
| Full-multiplier canonical congruence homology bound | **Proved with an explicit modulus** | LH.1: Δ factors through GL₉₇(Z/n*) with n*=2^51942·3^14136. The underlying stable modular quotient has order2^5038380·3^1371194. Petrov's genuine tangential specialization proves the necessary unramified statement directly on F/(N′N^576), so no outer orbifold comparison is used. |
| Raw characteristic-zero modular homology | **No Δ constituent** | LH.2: the genuine subgroup N⋊G_Q descends to a degree96 Q-cover. A good Frobenius has no eigenvalue1 on its H1, by the boundary Tate twist and Frobenius−1 isogeny of the Jacobian. Thus raw M⊗Q_l has no trivial G_Q subquotient and no full-GT0 Δ constituent; free Z_l lines are excluded. Finite coefficients and restriction to H are separate questions. |
| New quadratic pentagon equation FP.37 | **Independently audited** | The actual S4 coordinate ν4 is additive on H, and genuine GT_H satisfies ε2(W)=ν4. An independently implemented ring/adjugate certificate checks the marked quotient and all24 matrix identities. Nonvanishing of ε2(W)+ν4 on H is not asserted. |
| Entire adelic primitive-cube-root Burau family | **One actual Δ1 witness passes every level** | LI.9 strengthens LI.8 by compactness. The uniform double-commutator seed with exponent m even and prime to3 retains q12=5I and kills all nonharmonic pairs at any finite list of levels. Integral square-zero and invariant-flag identities handle all primes; the pure3-adic image is pro3. The resulting single actual gentle element has every pentagon factor1 in every congruence level and induced five-point quotient, with Δ1. No full pentagon assertion is made. |

## Files and reproducibility

The eight LaTeX modules are intended for direct incorporation after the parent renumbers local labels LP, LB, LU, LX, LD, LF, LC, LI, LH and replaces prose references by its chosen citation keys. No main deliverable was modified.

The exact checks run successfully:

```text
python code/check_lie_witnesses.py
python code/check_invariant_dimensions.py
python code/check_cm_replacement.py
python code/check_metabelian_units.py
python code/check_manuscript_cocycle.py
python code/check_five_cocycles.py
python code/check_descent_marking.py
python code/check_descent_evaluations.py
python code/check_iterated_lifting.py
python code/check_cubic_descent_shadow.py
python code/check_fixed_primitive_shadow.py
python code/check_homology_bound.py
python code/check_quadratic_pentagon_audit.py
python code/check_odd_burau_lifting_seed.py
```

Run from this directory, or use absolute paths. The second, fifth, eighth, tenth and eleventh scripts require SymPy; the others use the standard library. Scripts write their JSON certificates in `records/`. Captured stdout is saved in matching `.out` files.

### Degree seven and nine

`check_lie_witnesses.py` uses associative polynomial dictionaries over exact rational coefficients, standard longest-Lyndon-suffix bracketing, and direct derivation composition. It checks:

- q₇: 62 associative terms; antisymmetry, cabling, special and cyclic equations all zero.
- h₉: 412 associative terms; all four equations zero; meta image exactly X²Y²(X+Y)³[x,y].
- Explicit S₃ inner conjugators on both generators, independently for q₇ and h₉.
- The three special weight-five witnesses and the exact three meta images.
- All 18 infinitesimal braid relations for the actual P₄-conjugation leading derivations on the free rank-three kernel.
- q₇'s pentagon defect: support sizes 880, 882, 808 on a,b,c; coefficient of a⁵bcb in its action on a equals +16. All 2,570 coefficients are retained in `lie_witnesses_exact.json`.

`check_invariant_dimensions.py` constructs all 56 Lyndon degree-nine vectors. The antisymmetry/cabling/cyclic matrix is 2002×56, with exact kernel dimension 4 and meta rank 2. It supplies an explicit invariant lift of G₉ with denominator 4, so the two-dimensional lower bound does not rely on a separate Galois nonvanishing theorem. The polynomial-only upper-bound matrix has rank 6 on 8 coefficients.

### CM replacement and finite frame image

`check_cm_replacement.py` confirms #E₃(F₇)=12, Frobenius characteristic polynomial T²+4T+7, and

\[
a=2+\sqrt{-3}=3+2\zeta_3,
\quad a\bar a=7,
\quad a/\bar a=(5+8\zeta_3)/7.
\]

In the graph basis where ζ₃² acts by [[0,1],[-1,-1]], the last scalar is [[11,8],[8,3]] modulo 16 and −I modulo 4. The script also enumerates the order-6 and order-4 centralizers over F₃, the cyclic equal-parity subgroup of order 12, and its extension by (−I,I) to all 24 pairs.

### Full metabelian units

`check_metabelian_units.py` constructs the six-character projector in Q[(Z/4)²], verifies its idempotence, augmentation zero, coefficient denominators dividing 8 and the S₃/scalar symmetries. It then checks the explicit noninner peripheral finite images of orders 48, 75 and 324, including all 2,304, 5,625 and 104,976 multiplication pairs respectively. These include coefficient primes 2 and 3. Infinite existence and continuity are proved in LU.2 and are not inferred from finite tests.

### Five-point cocycles and the current-marking descent

`check_five_cocycles.py` checks the two displayed free-word expansions and the norm telescoping identities. The braid action convention is checked directly in Schneps (2006), equation (1.3).

`check_descent_marking.py` enumerates the actual degree-16 group of Q(ζ₈,2^(1/8)). It records σ=(1,2) as the commutator of (3,1) and (5,3), verifies the commutator subgroup of order four, and checks that complex conjugation c=(7,0) changes σ to (1,6). The NT-based proof identifies this with Dσ and proves a genuine Galois counterexample to Fix D in the prompt's literal positive marking.

`check_descent_evaluations.py` uses the faithful actions on primitive vectors modulo three and four, with exact SymPy Schreier–Sims membership. The six-evaluation group has order 8,153,726,976, and its derived group has order 56,623,104. The seventh inclusion evaluation increases these to 65,229,815,808 and 452,984,832. It checks the same-word condition, all six cyclic equations, the signed normalized frame conditions, and the original R3 value required by a fixed point. The opposite sign for the corrected old fixed locus is also checked. Twelve residues survive in each parity in both versions. This calculation identifies a failed sufficient approach; it gives no profinite or pentagon counterexample.

`check_iterated_lifting.py` verifies the finite seeds for two actual R2 constructions. A₀=[[x⁴,y⁴],z⁴]² has six orbifold valuesI and original value5I; its vanishing in the full orbifold kernels is proved from the order-two peripheral, not extrapolated from the matrices. The words b_x=x²yx²y⁻¹ and b_y=y²xy²x⁻¹ vanish on all eighteen generating S₃ pairs and have independent abelian residues modulo3. These give the coprime s-centralizer seed for the actual nonpentagonal pro-3 element. The same script checks the false residual-exclusion proposal: the image of U₀ modulo4 is the group of order48, its nilpotent residual has order12 and contains−U², and an explicit mixed-prime profinite commutator realizes that residue.

The strengthened seed A₁=[[x⁴,y⁴],[y⁴,z⁴]] has the same six orbifold values I and original value 5I, while lying in the full second derived subgroup F″. Its proof and the additional compactness conditions are LI.8. Retaining f,β∈R_nil(M) for every open B-normal M⊃F″ gives f,β∈R_nil(F″)⊂F‴. This is an actual invisibility theorem through the full third-derived actions, with no assertion of invisibility on all solvable quotients.

`check_cubic_descent_shadow.py` constructs the induced quotient B/core ker(F→S₃), with x a three-cycle and y a transposition, as an exact permutation group of degree36 and order648. Its pure subgroup has order108. The six orbifold evaluations and the original S₃ evaluation have joint order171,382,426,877,952 and derived order42,845,606,719,488. Same-word membership, all six cycle equations, and the descended r-conjugacy condition retain 108 residues for each possible value of a_f(D)+a_f. This does not settle whether ψ(D_L)=0 on actual gentle elements: it gives neither a profinite counterexample nor a lift of a surviving residue.

`check_fixed_primitive_shadow.py` strengthens the old-marking necessary finite test by retaining a single source word β with θ(β)β⁻¹=f in all six orbifold evaluations and q₁₂(β)=c_B(q₁₂(β_D)) in the original evaluation. The kernel of projection from the seven-evaluation group to the six-evaluation group has order8. An exact orbit calculation finds all24 targets after examining1,180,566 states: twelve of each Δ parity. This is recorded only as a failed finite sufficiency test. Further shadow-survival refinements were stopped; none supplies a profinite lift or decides C_L⊂kerΔ.

`check_homology_bound.py` checks the exact order valuations of GL₉₇(Z/576) and independently verifies the two cross-characteristic sums by LTE. The valuations are51940 and14135; the full modulus exponents are51942 and14136; the modular quotient order exponents are5038380 and1371194. The arithmetic field and genuine-action transfer are proved in `lifting_homology_bound.tex`, not inferred from the integer calculation.

`check_quadratic_pentagon_audit.py` independently reimplements the modulus-four quadratic ring and projective matrices using an adjugate inverse, importing none of the audited five-agent code. It checks the marked order48 S4 cover, its exact derived A4 complement, the positive level-three map of the harmonic pair group of order192, all central/conjugacy identities, and all24 defect identities in FP.37. The mathematical audit is in `quadratic_pentagon_audit.md`.

`check_odd_burau_lifting_seed.py` proves the symbolic identities behind the uniform LI.9 construction over Z[ω], including the primitive invariant flag, square-zero unipotence, and the residue3 pure-image statement. It checks q12=5I for every even exponent prime to3, and all30 finite pair/core evaluations of the explicit F7 seed ([[x^28,y^28],[y^28,z^28]])^7. The theorem is an actual relative lift plus compactness result; no finite candidate is declared globally liftable without that proof.

The parent's `code/check_congruence_homology.py` was independently rerun with its output redirected into this agent's `records/`. All576 deck traces, the rank97 integral cycle basis, and the primitive24-edge cusp class passed. The independent mathematical audit of RH.1–RH.3 is in `homology_audit.md`.

## Important proof boundaries

1. **No exponentiation shortcut.** LP.1 kills successive peripheral product errors by the integral surjection (u,v) ↦ [u,Y]+[v,−X−Y]. LP.2 uses coprime nonabelian H¹ to obtain genuine S₃ invariance. LP.3 builds and normalizes an actual automorphism of B̂/O^ℓ(F), retaining the sign between the pair parameter and its derivation. Thus the pro-ℓ input to R1 is proved, not assumed from an unrefereed graded row.

2. **Every lift exclusion.** The entire pro-ℓ parameter is retained by R1. For q₇, the leading defect coefficient remains 16. For the weight-nine stratum, Enriquez's characteristic-zero metabelian theorem excludes every leading vector with P₉ coordinate; a different degree-nine representative cannot repair it.

3. **D.46 repaired without a full CM image claim.** One Frobenius at 7 gives −a in the 2-adic CM image. The 2-division field over Q(ζ₃) is pro-2; Q(ζ₃,∛4) is degree 3 and is disjoint. Thus g can have the prescribed 2-adic image and trivial 3-torsion action. A commutator with inertia at 3 has multiplier one and is identity on the actual tangential free pro-2 group. This is enough for the relative replacement. Coprime centralizer lifting aligns the r- and s-conjugators over Q. Their finite frames, not arbitrary replacements of automorphism components, are retained by R2.

4. **Exact Galois frame normalization.** R4 referee section 1 step 9.4 states Tσ=κ(σ)ρ_E3,12(σ), κ=σ(r₀)/r₀, for σ∈G_Qab, in transported bases. Removing ±I removes exactly this twist. This supplies the order-3 projective image from Q(E₃[3])=Q(ζ₃,∛4). The D₄ field Q(i,r₀) gives both parities one and hence a W-value of order 4. Together they prove the complete equal-parity Galois image, not merely its containment.

5. **A.7 does not fail at the product identity.** Relative products do preserve the pentagon as a specified word equation once the five substitution maps descend to compatible bases. What is missing is a theorem lifting that restricted solution space to actual GT. D.50.12 counts a curve surface presentation with independent boundary values; PΓ₀,₅ is instead a configuration-space group F₃⋊F₂. This is not a refutation of the stronger lifting theorem, only an exact identification of the absent theorem.

6. **The manuscript beta is determined.** The supplied frozen transcription at scan 12 writes σ∞(g⁻¹)=l₀^β g l₁^β. Abelianization yields β=−(a+b). Comparing uρ=Inn(g)ρu in the actual free class-two quotient gives a+b=(1−λ)/2. Thus β=(λ−1)/2 and is zero throughout H, whereas the s-frame coordinate ρ is already nonzero on some G_Qab elements, detected in the cubic E₃[3] field. The symbolic calculation and SL₂(F₃) derived-subgroup check run in `check_manuscript_cocycle.py`. This also detects the missing half-cyclotomic factor in R11's unrestricted formula g=f⁻¹; complex conjugation is an immediate consistency check.

7. **The descent marking matters before any fixed-point statement.** The current inclusion has x=τ⁻²,y=sxs; LM2 has x_L=y⁻¹,y_L=x⁻¹. Therefore the old orbifold map becomes x↦τ⁻¹,y↦s on the current basis, whereas the prompt explicitly sets x↦s,y↦τ. The direct NT computation on G_Qab confirms the resulting conjugation by c after every cusp and frame normalization. The safe independent refutation already holds on G_Qab; no assertion about all G_Q is needed to prove it. The formal old-map conversion is written separately, so it can be audited independently of the geometry.

8. **The new kernel theorem uses a uniform full-source seed.** For every finite orbifold targetE, the same A₀ lies in N_E=U₀∩core_B(φ⁻¹kerE) and maps to5I originally. Hence q₁₂(N_E) is a two-group containing5I, and the order-three centralizer lift applies. Cusp normalization uses an element of R_nil(N_E), so it retains the frame residue, f∈R_nil(N_E), andρ=0. The directed finite conditions have an actual compact intersection withφ(f)=1, proving D(k)=1 andΔ(k)=1. This provesΔDⁿ≠Δ; it does not prove a positive iterate is nonzero.

9. **The pro-3 pentagon witness is actual.** For the S₃-kernel coreN, q(N)=F_ab/3 is a three-group and the diagonal translation centralizes the order-two elements. Coprime centralizer lifting and R2 produce the whole pair, not merely its finite residue. The five-point agent's exact affine formula detects its pentagon defect. Taking the prime-idempotent pro-3 power retains that defect and kills every quadratic character. This is a false positive for the joint quadratic/pronilpotent zero locus, with no claim that allGT belongs to that zero locus.

10. **The third-derived strengthening retains all prescribed data.** For every open B-normal M containing F″ and every finite orbifold target J, use N=U₀∩M∩core φ⁻¹J. A₁ belongs to every such N. The prescribed r-conjugator has base coordinate1, so its actual normalized frame A lies in N, as do f and β. The cusp correction lies in R_nil(N). More strongly f,β∈R_nil(N)⊂R_nil(M). The intersection of R_nil(M) over these M equals R_nil(F″): for any finite q killing R_nil(F″), take M=F″ker q, whose image q(F″) is nilpotent. Compactness therefore gives f,β∈R_nil(F″)⊂F‴ and A∈F″, retaining f∈R_nil(U₀), φ(f)=1 and the finite frame values. This makes k identity on F/F‴ and B/B‴. The homology exclusion concerns canonical modules with the normalized genuine action; the full β still determines the gentle element, so only its quotient images have been shown insufficient. FP.35 supplies the independent matching derived-length4 detector.

11. **The cubic descent discrepancy is proved; its next iterate is not settled.** LC.1–2 give ρD=−a_f mod3 and hence ψ=−ρD−ρ. The finite calculation just described does not prove or refute ψD_L=0 on the full group. Likewise χ₁=ΔD is either zero or independent of Δ, but its nonvanishing remains unproved. Identity relative automorphisms and centralizer-only frame changes cannot prescribe χ₁=1 when the full finite evaluation quotient is retained: they force its f-value to1. A genuine nonidentity relative peripheral automorphism would be required for that proposed lift.

## Opened literature and source handles for the parent

The bibliography file contains verified metadata and precise portions used. The following URLs can be opened by the parent before using its web citation system:

| Reference | Exact use | Opened source handles |
|---|---|---|
| Harbater & Schneps (2000) | Propositions 3–4 and Theorem 2; direct pro-ℓ analogue supplied here | `turn9view0`, `turn9view1`, `turn9view2`; https://www2.math.upenn.edu/~harbater/lsdhr3b.pdf |
| Enriquez (2006) | Theorem 0.1, Remark 0.2; odd-weight meta line | `turn17view0`, `turn17view1`; https://arxiv.org/pdf/math/0502084 |
| Cohen (2001) | Actual Artin/pure braid action, equations (1.2)–(1.4) | `turn22view1`; https://arxiv.org/pdf/math/9910121 ; metadata `turn102view0` |
| Hain & Matsumoto (2003) | §8.5 before Theorem 8.7; actual tangential pro-ℓ action unramified outside Nℓ | `turn95view0`, `turn95view1`; https://arxiv.org/pdf/math/0006158 ; metadata `turn102view2` |
| Chen & Deligne (2017) | Corollaries 4.1.5–4.1.6, Proposition 4.3.7, Theorem 5.2.4 | `turn79view0`, `turn80view0`, `turn80view1`, `turn80view2`; https://arxiv.org/pdf/1710.05532 |
| Serre (2007, 2nd ed.) | Proposition 3.3.1 and Theorem 3.4.1 | `turn86view0`, `turn87view0`, `turn87view1`; URL in bibliography |
| Milne (2020) | CFT Chapter V, Theorem 3.23 | `turn86view2`, `turn87view2`; https://www.jmilne.org/math/CourseNotes/CFT.pdf |
| Milne (2013) | LEC Theorems 24.1, 29.4 and Proposition 29.9 | `turn86view1`, `turn87view3`, `turn90view0`; https://www.jmilne.org/math/CourseNotes/LEC.pdf |
| Schneps (2006) | Equation (1.3), exact right-conjugator braid action | `turn118view0`; https://webusers.imj-prg.fr/~leila.schneps/automorphisms.pdf |
| Tsunogai & Nakamura (2002) | Theorem1(V) and Theorem2(GF1), used literally in the G_Qab descent proof | `turn122view0`; https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1267-18.pdf |
| Nakamura & Schneps (2000) | Proposition2.4 and Definition5.1, g^ab=(ρ₂,ρ₂) with positive-root Kummer convention | `turn122view1`, `turn127view0`, `turn127view1`; https://webusers.imj-prg.fr/~leila.schneps/newGT.pdf |
| Petrov (2023) | Lemma8.7, genuine tangential prime-to-p specialization; v3 p18 | `turn192view0`, `turn194view0`; metadata `turn195view0`; https://arxiv.org/pdf/2012.13372 |
| Milne, Jacobian Varieties (1986; corrected 2021) | Proposition9.1 and Corollary9.6, geometric H1/Jacobian comparison | `turn204view0`, `turn205view0`; https://www.jmilne.org/math/xnotes/JVs.pdf |
| Milne, Abelian Varieties (1986; corrected 2022) | Theorem15.1, Remark15.5, Proposition20.7, genuine Tate-module comparison and integral prime-to-p torsion | `turn204view1`, `turn205view1`, `turn205view2`; https://www.jmilne.org/math/xnotes/AVs.pdf |
| Milne (2020), additional use | ChapterI, Theorem4.16 and proof, cyclotomic ramification | `turn196view0`, `turn197view1`; https://www.jmilne.org/math/CourseNotes/CFT.pdf |

No literature claim in this module says that Δ vanishes on GT or that the R2 mixed witness fails the full pentagon. The strict inclusion is a new deduction from the stipulated R1 plus the proved pro-ℓ inputs. The manuscript dictionary calculation uses the supplied frozen diplomatic transcription of scans 7–12; no new visual or palaeographic inspection of the original images is claimed.
