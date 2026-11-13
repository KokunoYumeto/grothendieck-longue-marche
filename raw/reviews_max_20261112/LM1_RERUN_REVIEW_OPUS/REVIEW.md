# Review of the Pro return LM1_GROUP_SCHEMES, rerun of 12 November 2026

Claude Opus 5.5 (effort max), 12 Nov 2026.

**Reviewed.** The return of GPT-6 Astra (ChatGPT Pro mode) to the resent prompt LM1_GROUP_SCHEMES
(`pro_prompts_done_20261111\LM1_GROUP_SCHEMES\PROMPT.md`), unpacked in
`answers\LM1_GROUP_SCHEMES_rerun_20261112_unzipped\LM1_GROUP_SCHEMES\`: 84 numbered statements (A.1–A.10, B.1–B.18,
C.1–C.11, D.1–D.20, E.1–E.25; the return counts 54 Proved, 5 Known, 16 Refuted, 9 Open), read in `sections\*.tex`,
the report (100 KB, all of it), the results CSV and the 17 mathematical programs. Its `MANIFEST.sha256` checks: 132
files, no mismatch, nothing unlisted.

**Compared with.** The 11 Nov run, which came back only as a text edition. The copy named in the brief, Obsidian
`Untitled 1947.md`, now holds only Pro's closing summary (the note was overwritten at 21:03 UTC on 11 Nov). The full
11 Nov text edition is the 21:03:16 snapshot that the publication agent split into
`answers\LM1_GROUP_SCHEMES\` (RUNBOOK, 12 Nov 00:3x UTC): `results.csv` (97 statements A.1–A.11, B.1–B.23,
C.1–C.11, D.1–D.21, E.1–E.28, F.1–F.3), `sections\*.tex`, `RECOVERY_UPDATE.md` with the added C.12; 72 Proved,
16 Refuted, 4 Known, 5 Open, 1 Unfinished. The comparison below uses that edition; "11 Nov X.n" means its
numbering, "X.n" alone means the rerun. PRO_QUEUE and the RUNBOOK record nothing else about the mathematics of the
11 Nov return (Pro's later work on A.10 and the Stix citation was lost with the overwritten note).

**Context used.** The second-pass text (`second_pass\CURRENT_TEXT_INDEX.tsv`) at the places in §5; the LM7 and LM8
prompts (`pro_prompts_draft_20261111_work`), their BACKGROUND files and `KNOWLEDGE_HANDOFF_LM.md`; the LM4, LM5 and
LM6 prompts (searched: none of them mentions LM1).

**Computations.** The 17 mathematical programs were copied to `rerun\code\`, read in full, and rerun with
`python -I` (Python 3.13.9, SymPy 1.13.1; the return used 3.12.14 and 1.14.0) through `rerun\tools\run_isolated.py`,
which appends only the copied code folder to `sys.path`, for the two helper modules `AB_core.py` and `D_finite.py`.
All exit 0 with empty stderr; every stdout (`rerun\out\*.out`) and every JSON file is identical to the shipped one
after line-ending normalization (`rerun\out\COMPARISON.txt`, 26 of 26; also `AB_enumeration.json`). My own checks,
written without the return's code, are `rerun\indep_checks.py` (output `rerun\indep_checks.out`, 13 checks, all
pass). Manifest check: `rerun\out\MANIFEST_CHECK.txt`. Not run, and why: §4.

## 0. Result in brief

| | Number | Statements |
|---|---|---|
| same as 11 Nov | 44 | listed in §2.1 |
| changed | 28 | A.3, A.9, A.10, B.1, B.5, B.15, B.18, C.4, C.5, C.7, C.8, C.10, C.11, D.4, D.5, D.9, D.11, D.12, D.16, D.19, E.1, E.2, E.6, E.8, E.10, E.14, E.22, E.24 |
| new | 12 | A.5, A.6, A.7, B.8, B.10, B.12, B.13, B.14, B.16, B.17, D.10, E.25 |
| dropped (11 Nov had, rerun lacks) | 8 wholly, 13 in part | §2.2 |

| Verdict on the 84 rerun statements | Number | Statements |
|---|---|---|
| correct | 69 | all others; of these B.13, B.15 (outside its matrix lemma), D.20 were read in outline only (§7) |
| correct with a gap | 1 | E.22 (correct as stated, but it is not the answer to Part E (f); §3.1) |
| known | 5 | A.10, C.2, C.9, D.18, E.23 |
| unproved (open, as the return says) | 9 | A.9, B.8, B.16, B.18, C.11, D.7, D.11, E.11, E.20; D.11 can be closed for M over Z by the 11 Nov argument (§3.2) |
| wrong | 0 | — |

Nothing in the rerun is false. Two things matter for the prompts: the rerun's E.22 ("the modular envelope detects the
three-letter covering") concerns the quotient SL(2,Z) → SL(2,F₂) ≅ 𝔖₃, which is trivial on Π₀; the BISITE covering of
P¹−{0,1,∞} is not seen by the envelope of 𝔖, as the 11 Nov E.23 said and the rerun no longer says. And four checked
11 Nov results are absent from the rerun and should travel with it: E.23, E.28 (Fermat relative completion of rank
n²+1), D.16 (integral μ₂-extensions F₂³) and E.9/E.13 (the positive-power theorem and the universal property for all
affine finitely presented group schemes over Z).

## 1. The new mathematics, stated in full

**N1. Every effective automorphism of the profinite modular group preserves the congruence kernel (B.15; this part
is new, the rest of B.15 continues 11 Nov B.17 and B.22).**
Let C = SL(2,Z)^, q: C → SL(2,Ẑ) the congruence map, r = [[0,1],[−1,1]], s = [[0,−1],[1,0]], ℓ₀ = s⁻¹r
(= −[[1,−1],[0,1]]). Let u be a continuous automorphism of C with u(r) conjugate to r^{±1}, u(s) conjugate to
s^{±1} and u(ℓ₀) = ℓ₀^μ, μ ∈ Ẑ^×. Put a = (q u(s))₁₁ and g = [[μ, aμ],[0,1]] ∈ GL(2,Ẑ). Then q∘u = Ad(g)∘q; in
particular u(ker q) = ker q and q u(s) = [[a, −μ(1+a²)],[μ⁻¹, −a]]. Proof (checked, and recomputed in
`indep_checks`): S = q u(s) and R = q u(r) have traces 0 and 1 and S⁻¹R = q(ℓ₀)^μ = −[[1,−μ],[0,1]]; tr R = 1 forces
S₂₁ = μ⁻¹ and det S = 1 forces S₁₂ = −μ(1+a²); then S = gsg⁻¹ and R = S·q(ℓ₀)^μ = grg⁻¹, and two continuous maps
agreeing on topological generators agree. *Why it matters:* the comparison of Part D(b) sees an effective
automorphism (a Galois element, or an element of GT̂ or GT̂₀ acting through type (1,1)) on congruence quotients only
through the Borel element (μ, a); for Galois this is the cyclotomic description. What the scheme M loses is therefore
exactly the action on the congruence kernel, which D.6 shows is nontrivial (quotient SL(2,F₈)).

**N2. The central sign twist and the linked signs (B.16, new; Open only for its source comparisons R1–R3).**
For C = SL(2,Z)^: Z(C) = ⟨ω⟩, ω = −I; C^ab = Z/12 with r ↦ 2, s ↦ 3; Aut(C) → Aut(C/ω) is onto with kernel {1,Θ},
Θ(x) = x·ω^{sg(x)} (sg = sign of the image in SL(2,F₂) = 𝔖₃), so Θ(r) = r, Θ(s) = s⁻¹. Θ fixes L² (L = closure of
⟨sr⟩) but moves the class of L (mod 3, sr has order 3 and ω·sr order 6), so loop-preserving automorphisms of C and of
C/ω correspond bijectively. For u preserving L and the classes of ⟨r⟩, ⟨s⟩ the signs are functions of the
multiplier: from 2e_r + 3e_s ≡ 5μ (mod 12), u(r) ~ r^{ε₃(μ)}, u(s) ~ s^{ε₂(μ)} (I checked the congruence). *Why:*
for the actual modular group the "linked" and "independent" sign groups of §49.IV–V coincide, and the SL/PSL sign
ambiguity is located exactly in Θ.

**N3. The loop equation does not imply realization (B.12, new).** In PSL(2,F₁₃) take ρ = [[1,2],[5,11]],
σ = [[0,1],[12,0]], ρ′ = [[2,5],[9,10]], σ′ = [[1,4],[6,12]], conjugators α = [[6,6],[10,8]], β = [[6,8],[7,3]].
Both pairs generate (1092 elements), ρ ~ ρ′ (order 3), σ ~ σ′ (order 2), σ′⁻¹ρ′ = (σ⁻¹ρ)² with σ⁻¹ρ of order 7
(2 is a unit mod 7), yet [σ,ρ] has order 7 and [σ′,ρ′] order 6, so no endomorphism sends one pair to the other.
Recomputed independently. *Why:* hypothesis (37)(b) of scan 501 cannot be dropped; for C = SL(2,Z)^ itself, B.8 proves
that each signed numerical triple defines a continuous endomorphism with u(ℓ₀) = ℓ₀^μ and leaves exactly its
surjectivity (B.8.5) open.

**N4. No naive integral realization (B.8, new).** There is no group-scheme morphism from the constant profinite
scheme lim(Z/n)_Z to SL_{2,Z} sending 1 to L₀(1) = [[1,1],[0,1]]: a morphism from a proconstant scheme to a finitely
presented affine one factors through a finite stage, so its Z-points have finite image. Checked. *Why:* the profinite
constructions of §49 do not become integral group schemes by reading profinite groups as constant proschemes; an adic
construction or an envelope (§50) is needed, which is the transition Grothendieck makes.

**N5. A defect in the restricted quotient of §49.VI (B.17, new).** For C = SL(2,Z)^, A = Π̂₀, e₀ = σρ and l = e₀²
(source normalization), l ∉ A, −l ∈ A and Int(l) = Int(−l); so the loop subgroup L_A of scan 658 (18), which the
margin allows to exceed L ∩ A, contains l, its antidiagonal does not lie in A ⋊ Z^A, and the quotient of scan 660 (29)
is undefined. Repair: divide by Δ(L ∩ A); the image of A ⋊ D in (C ⋊ D)/ΔL has kernel AL over D/jL (A when L ⊂ A).
SL(2,Z/4) model: |C| = 48, A = V₄, L = {1,l}, |AL| = 8, automorphism kernel {±I}. Checked (l mod 4 is
[[1,2],[0,1]] ∉ V₄). *Why:* a real error in the late §49 construction that §51 inherits.

**N6. Projective modular pairs over imperfect fields of characteristic 2 (A.7, new).** Over a field k of
characteristic 2 the GL(2,k)-orbits of projective pairs (orders 3 and 2, fppf-locally regular unipotent product,
transversal, no lift specified) are indexed by N_{K/k}(K^×)/k^{×2}, K = k[T]/(T²+T+1); each splits into k^×/k^{×2}
SL(2,k)-orbits. Over F₂(t), ρ = [[0,1],[1,1]] with σ = [[1,t],[t+1,1]] (det t²+t+1, not a square) is not conjugate
to the standard pair. Over Z, Z/4, Z/8, Z/9 there is one GL₂-orbit and 2, 1, 2, 2 SL₂-orbits. Checked. With A.3 (the
projective stabilizer of the standard pair is {[I+τr] : 2τ = τ² = 0}) this proves that projective data alone do not
pin the épinglage, and the qualification of scan 323 is necessary.

**N7. Integral images of the commutator maps (A.5, new; with B.1, changed).** A ↦ [A,z] (z = r or s) is an fppf
T_z-torsor onto the regular part of {Y ∈ SL₂ : tr(Yz) = tr z}; over Z its SL(2,Z)-image is exactly {Y₂₂ > 0}, by
det(A)[A,r]₂₂ = g²+gh+h² and [A,s] = AAᵗ/det A; the points with Y₂₂ < 0 are reached only with det A = −1 (the norm
forms are positive definite, the class numbers are 1). B.1: the simultaneous parametrizations of scans 368 and 371 are
isomorphisms over every ring, the solution scheme being G_a × G_m (η = [[μ(1+B²),B],[B,μ⁻¹]]). Checked. *Why:* the
surjectivity question of scan 370 has an exact answer on points: each single map misses half of the integral points,
the simultaneous map misses none.

**N8. What the literal presentation of scan 336 is on points (C.7, C.8, changed).** The evaluated presentations
⟨s,t | s², (st)³, tⁿ⟩ and ⟨s,t | s⁴, (st)³s⁻², tⁿ⟩ have orders 6, 12, 24, 60 and 6, 24, 48, 120 for n = 2…5
(Todd–Coxeter, rerun). Over F₄ the point group is 𝔖₃ *_{C₂} (C₂×C₂) and its kernel to SL(2,F₄) is free of rank 6
(25 vertices, 30 edges). Over F₇ and Z/9 the kernels are surface groups of genus 3 and 10 (Euler characteristics
168(1/2+1/3+1/7−1) = −4 and 324(1/2+1/3+1/9−1) = −18): at F₇ this is the Klein quartic. The actual sheaf values:
A(F₂) = 𝔖₃, A(F₄) = 𝔖₃ *_{C₂} V₄, A_SL(F₃) infinite (b = x(α)zx(−α), α³ = α+1 in F₂₇, (bz)^m reduced of length 4m),
both values over Z/4 infinite (x(a)y(2)x(−a)y(2)⁻¹ with a = 2b, b²+b+1 = 0), and an extra infinite-order kernel
element over Z/9. Checked. With C.4 (a 12-syllable universal kernel word L, a cyclic conjugate of
h(T)x(U)h(T)⁻¹x(−T²U), and its 24-syllable commutator with x(V), nontrivial on every fppf cover in every
characteristic) and C.5 (four Gaussian-chart relation families present SL₂ over Z, no prime inverted) this refutes
Lead 1 uniformly and replaces it by an integral presentation.

**N9. Central μ₂-extensions and explicit fields (D.9, D.10, D.12, D.16).** Ext_cen(M_C, μ₂) = F₂⁵: the three
inflations of H²(C₂², C₂) through the explicit component section g_{e′} = (a*,I,I), g_e = (a*,diag(1,−1),diag(−1,1)),
a* = (2ρ−I)/√−3, and the Kummer covers along the eigenvalue a₁ and along δ = det U (D.9, checked; it agrees with the
geometric part of 11 Nov D.16). Every central extension 1 → μ₂ → E → μ₂² → 1 over Z₂ or Z is commutative (the
commutator is a morphism from the connected μ₂² to the constant (C₂²)), so the dihedral class has no root-of-unity
model at 2 (D.10, checked). (−3,3) = 0 with the splitting I = [[0,−3],[1,0]], J = [[0,3],[1,0]]; Q(3^{1/4}, i) is a
full D₈ lift of the class u(u+v), u = χ₋₃, v = χ₋₁ (D.12, checked: r has signs (1,0) and order 4, s has (1,1) and
order 2). Full Dic₃ lifts (D.16, checked by hand and by the rerun): the compositum of the splitting field of
x³−12x−14 (disc 2²·3⁴·5, Eisenstein at 2 and, after x ↦ x−1, at 3) with Q(ζ₅), group Dic₃, sign field Q(√5),
ramified at 2, 3, 5 with (e,f,g) = (3,4,1), (3,4,1), (4,1,3); and Q(2^{1/3}, 3^{1/4}, i), degree 24, group 𝔖₃ ×_{C₂} D₈,
full Dic₃ over Q(i), ramified only at 2 and 3 with (12,2,1). *Why:* this is the "exercice plaisant et délectable" of
scan 634 with explicit fields; the second field is ramified only where the modular situation is.

**N10. The automorphisms of the first Fermat example (E.24 changed, E.25 new).** For each sign pair the fine
parameter scheme of scan 41 is Spec Z[a,b,k,(12k+6ν₂+4ν₃+1)⁻¹], open in A³_Z and smooth also at 2 and 3 (the coarse
linear map has maximal-minor gcd 3, Grothendieck's "ce n'est le cas qu'en car. ≠ 3"; with ν′ added the gcd is 1). The
unit is the 11 Nov one (1−12w+6i+4j with w = −k). Over a Q-algebra the automorphisms of 𝔖_M preserving M, with both
conjugators in M and the loop relation, form G_a ⋊ G_m: u(ρ) = (t,ν−t)ρ, u(σ) = (t,−t)σ, u|_M = μI, μ = 1+2ν,
(t,μ)(t′,μ′) = (t+μt′, μμ′) (checked: u(ρ)³ = u(σ)² = ω, u(λ₀) = μe₀). Over F_p[ε]/ε², (v,h) ↦ (v+ε(v^{[p]}−v), h)
is a non-identity automorphism of 𝔖_M fixing 𝔖 pointwise and preserving the loop line, so formula (16) of scan 36
fails over non-reduced bases (it holds once the automorphism is required to be linear on M); and over Q the identity
has ρ-conjugators of both orientations (α = 1 and α = (−1/3,1/3)τ, since (I−R)(−1/3,1/3) = e₁), so ε₃ of scan 37 (18)
is extra data. Checked. *Why:* these are the §51.2 objects LM7 Part A works with.

**N11. The positive-power theorem for linear group schemes over every ring (E.10, changed; E.14, changed).** If
G ⊂ GL_{r,A} is a closed subgroup scheme of finite presentation over any ring A, a section g is fibrewise
quasi-unipotent iff some g^m lies on a homomorphism G_a → G. Proof (checked): constructible compactness gives one a
with N = g^a − I nilpotent on all residue fields, hence N^b = 0; P(t) = Σ_{j<b} binom(dt,j)N^j with d = (b−1)! is an
integral one-parameter subgroup with P(n) = g^{adn}; one more dilation (E.8) kills the finitely many equations of G.
E.14: Hom((E_Γ)_A, G) = {fibrewise quasi-unipotent f: Γ → G(A)} for such G, Hom being a direct limit over the finite
stages (correcting the inverse limit of (58), scan 31). *Why:* the "Théorème (!)" of folio 652′ holds for linear
group schemes over any base, and the envelope has its universal property there. The 11 Nov E.9/E.13 proved the same
for all affine finitely presented group schemes over Z (§3.2); together they cover the integral case Grothendieck
needs; the non-linear case over non-reduced bases (Q[ε]/ε², Z/4) remains (E.11).

**N12. The sharp integral bound (E.6, changed witness).** Over Z_(p), Nᵖ ∈ pM_r and N^r = 0 give an integral
(I+N)^t iff r ≤ p², uniformly in N; sharp for the weighted shift w_i = i/p^{max(v_p(i)−1,0)}, i ≤ p². At p = 2 this is
the shift (1,2,3,2): log(I+N) is integral, X⁴/4! = E₁₅/2, and I+N is a G_a-value on every geometric fibre (N² ≡ 0
mod 2, N³ ≡ 0 mod 3). Recomputed. The 11 Nov witness (1,6,1,6, X⁴/4! = (3/2)E₁₅) is also valid.

## 2. Statement-by-statement comparison with 11 Nov

### 2.1 The 84 statements of the rerun

Class: **S** same, **C** changed (how), **N** new. Verdict: **ok** correct, **gap**, **known**, **open**; "outline"
means the general proof was read in outline (§6).

| Id | Claim | Class | 11 Nov | Verdict |
|---|---|---|---|---|
| A.1 | dictionary of §§48 groups, identities | S | A.1, A.5 | ok (identities rerun) |
| A.2 | lifts differ by 1+τ, 2τ = τ² = 0; unique after base change iff 2 invertible; Z/4 | S | A.4 (was "Refuted", now the exact criterion) | ok |
| A.3 | pinning by specified lifts; projective stabilizer {[I+τr]} | C: adds the stabilizer; absorbs 11 Nov A.2 | A.2, A.3 | ok (stabilizer recomputed) |
| A.4 | normalized triples: one GL₂ orbit, SL₂ orbits R^×/R^×²; counts | S | A.7, A.8 | ok (counts checked) |
| A.5 | commutator maps are torsors; SL(2,Z)-image Y₂₂ > 0 | N | (A.6 had the chart) | ok |
| A.6 | slips: B+D−C, b bᵗ = εI, centrality of ST_s; corrections | N | — | ok (readings §5) |
| A.7 | char-2 projective orbits N(K^×)/k^{×2}; counts 2,1,2,2 | N | — | ok |
| A.8 | θ(g) = det(g)⁻¹g fixes SL₂ | S | A.9 (first half) | ok |
| A.9 | general dictionary §49; residual comparisons | C: Unfinished → Open, dictionary to scan 696 | A.10, A.11 | open |
| A.10 | low types table | C: Proved → Known, moved | F.1 | known (Farb–Margalit, not reopened) |
| B.1 | 𝒳 ≅ G_a × G_m; parametrizations isomorphisms on all rings | C: chart → isomorphism theorem | A.6 | ok |
| B.2 | coordinate ring, monic integral Gröbner basis, flat, dim 6 | S | B.1, B.2 | ok (rerun) |
| B.3 | smooth exactly over Z[1/2], Jacobian ideal (4); fibres at 2, 3 | S (adds ideal (4)) | B.3–B.5 | ok (Jacobian checked by hand) |
| B.4 | group law and exact sequences | S | B.7, B.11, B.14 | ok |
| B.5 | M(0), M[0], normalizer of L₀ = {U upper triangular}, section cycles | C: adds cycles and normalizer | B.10 | ok |
| B.6 | J⁰ → H⁰ μ₂-cover; (J⁰×SL₂)/μ₂ = M⁰; centre | S | B.8, B.9 | ok (F₃: 48 vs 24 checked) |
| B.7 | point counts, commutator complements | S (same numbers) | B.12 | ok (F₅…F₁₃ recomputed by hand) |
| B.8 | realization; endomorphisms of SL(2,Z)^; constant-scheme obstruction | N | — | open (proved parts ok) |
| B.9 | global sign vs μ₂(Ẑ): infinite kernel | S | B.16 | ok |
| B.10 | Lead 2 refuted | N (as a statement) | (B.6) | ok |
| B.11 | general unsigned construction, kernel L₀∩Z(C) | S | B.13, B.19 | ok |
| B.12 | PSL(2,F₁₃) counterexample | N | — | ok (recomputed) |
| B.13 | signed construction | N | — | ok (outline; finite models rerun) |
| B.14 | unrestricted centralizers; left factor at scan 546 refuted | N | — | ok (counterexamples rerun) |
| B.15 | descent criterion, congruence-kernel stability, reconstruction, gluing | C: adds N1; keeps 11 Nov reconstruction and gluing | B.17, B.22 | ok (N1 checked; rest outline) |
| B.16 | central twist, normalized conjugators; R1–R3 | N | — | open (proved parts checked in outline) |
| B.17 | antidiagonal needs L∩A | N | (B.21) | ok |
| B.18 | late sections; restricted conjugators | C: now Open with proved formal cases | B.19–B.21 | open |
| C.1 | literal sheaf pushouts of constant groups | S | C.1 | ok (scan 336 read) |
| C.2 | SL(2,Z) = C₄ *_{C₂} C₆ | S | C.2 | known (Conrad) |
| C.3 | Zariski/fppf epimorphisms; GL₂ cokernel G_m | S | C.3 | ok |
| C.4 | literal presentation false on every base | C: witness of length 12/24 (was 10/21) | C.4 | ok (recomputed) |
| C.5 | four Gaussian families present SL₂ over Z | C: four families for SL₂ (was nine for the signed kernel) | C.5 | ok |
| C.6 | PGL₂ (h(ζ) = 1) and GL₂ presentations | S | C.5, C.6 | ok |
| C.7 | point presentations; kernels free rank 6, genus 3, 10 | C: kernels identified | C.7 | ok |
| C.8 | sheaf values: F₂, F₄; F₃ and Z/4 infinite; Z/9 | C: new witnesses; drops A_P(F₃), F₅, F₇ values | C.8 | ok |
| C.9 | SL(2,Z[1/p]) amalgam | S | C.9 | known (Serre) |
| C.10 | presentations over Z₂, Z₃ | C: separate statement (11 Nov C.10 was the matrix counts) | C.5, C.6 | ok |
| C.11 | remaining descent values | C: residue changed | C.11 | open |
| D.1 | M(R) = SL₂(R) ⋊ H_R; M(Z) = C₆ × (SL(2,Z) ⋊ D₈) | S (adds M(Z)) | D.1 | ok |
| D.2 | local norm images and kernels | S | D.2 | ok |
| D.3 | M(Ẑ), M(A_f) | S | D.2 | ok |
| D.4 | typed comparison; global-sign nonopenness; point at 5 | C: sign argument replaces the rank argument | D.4, D.7 | ok |
| D.5 | finite (I),(II) at n = 2, 3, 4, 6, 12 | C: different computation | D.5 | ok (rerun) |
| D.6 | SL(2,F₈) quotient; congruence kernel nontrivial | S | D.6 | ok |
| D.7 | Galois/GT̂/GT̂₀ comparisons | S | D.8 | open |
| D.8 | eight extensions of V₄; manuscript class D₈ | S | D.9, D.10 | ok |
| D.9 | Ext_cen(M_C, μ₂) = F₂⁵ | C: only over C (11 Nov also Q and Z) | D.16 | ok |
| D.10 | no non-commutative μ₂²-by-μ₂ extension at 2 | N (a step of 11 Nov D.16) | (D.16) | ok |
| D.11 | integral and arithmetic classification | C: 11 Nov Proved → Open | D.16 | open; closable (§3.2) |
| D.12 | (−3,3) = 0; Q(3^{1/4},i) full D₈ lift | C: field changed (was splitting field of X⁴+3) | D.11, D.15 | ok |
| D.13 | (−1,−3) of order 2; C₄ of scan 631 | S | D.12 | ok (scan 631 read) |
| D.14 | no constant Dic₃ lift with sign χ₋₃ | S | D.13 | ok |
| D.15 | criterion (a,−1) = 0 | S | D.14 | ok |
| D.16 | explicit Dic₃ fields | C: new fields (was d = 37) | D.14 | ok |
| D.17 | generation and indices n ≤ 48 | S | D.17 | ok (rerun) |
| D.18 | motivic specialization | S | D.18, D.19 | known (Hain–Matsumoto, not reopened) |
| D.19 | arbitrary integral monodromy insufficient | C: cusp char. poly T²+T−1 (was 2±√3) | D.20 | ok |
| D.20 | descent datum, H¹ of centralizer | S | D.21 | ok (outline) |
| E.1 | G_a-values have order p in char p | C: definitional; drops 11 Nov's imperfect-field non-descent | E.2 | ok |
| E.2 | Q-algebras, closed linear targets: unique exp(t log g) | C: Q-algebras, linear (was char-0 fields, all targets) | E.1 | ok |
| E.3 | torsion-free criterion: all (log g)^i/i! integral | S | E.4 | ok |
| E.4 | rank-3 counterexample X = J−J²/2 | S | E.6 | ok |
| E.5 | rank-4 signed counterexample; repaired with X integral | S | E.5 | ok (scan 9 read) |
| E.6 | rank 5, weights (1,2,3,2); sharp bound p² | C: witness | E.7 | ok (recomputed) |
| E.7 | W₂ and x+y+pC_p over Z/p² | S | E.3 | ok |
| E.8 | binomial basis; dilation lemma; 72 family cases | C: search narrowed (was 8190 words per prime) | E.8 | ok |
| E.9 | affine dilation proposition | S | E.10 | ok |
| E.10 | positive-power theorem, closed linear, every ring | C: scope (was affine over Z) | E.9 | ok |
| E.11 | non-linear residue | S | E.11, E.27 | open |
| E.12 | métabélien = virtually abelian; finite stage | S | E.12 | ok (scan 25 read) |
| E.13 | O(E_Γ), kernel Z+(x)Q[x], F_p-fibres | S | E.14 | ok |
| E.14 | universal property, direct limit | C: scope (was affine over Z) | E.13 | ok (scan 31 read) |
| E.15 | Π₀, H = Dic₃, R, S, 𝔖^ab = Z/12 | S | E.18, E.26 | ok (recomputed) |
| E.16 | finite stage ∏₁₂ Z[x,y], integral cocycle | S | E.19 | ok (recomputed) |
| E.17 | points: Γ, Γ̂, ∏_p Γ̂; Δ-points Γ̂ | S | E.19 | ok (scan 35 read) |
| E.18 | Lead 3 refuted; maps and separating examples | S (label Proved → Refuted) | E.16, E.17 | ok |
| E.19 | relative completion with abelian kernel = finite stage | S | E.20 | ok |
| E.20 | comparison with named M, N; Fermat targets | S | E.21 | open |
| E.21 | Stallings lead | S | E.22 | ok |
| E.22 | modular envelope "detects the three-letter covering" | C: drops the negative half of 11 Nov E.23 | E.23 | gap (§3.1) |
| E.23 | two rational theories on B𝔖 | S | E.24, E.25 | known (RWZ, Toën, not reopened); goodness argument checked |
| E.24 | fine parameter scheme; G_a ⋊ G_m over Q | C: adds the automorphism group | B.23 | ok |
| E.25 | generator images do not determine automorphisms | N | — | ok |

### 2.2 Dropped: 11 Nov statements with no counterpart in the rerun

| 11 Nov | Claim | In the rerun | Checked here |
|---|---|---|---|
| E.23 (half) | the BISITE representation of Π₀ ((12),(13)) does not factor through 𝔖 or its envelope; Π₀/Π₀″ retains it but is not virtually abelian | only the other half (E.22) | yes, correct (§3.1) |
| E.28 | relative completion of F₂ over (Z/n)²: free prounipotent kernel of rank n²+1; abelian-kernel quotient of dimension n²+1 (5 at n = 2); not M_Q, not 𝔖_Q for n ≥ 2 | absent; E.20 only names q₂ as an untested case | yes (Schreier; dimensions) |
| D.16 (Q, Z parts) | CExt_Z(M,μ₂) = F₂³ (z² = δ^a e^b t^c); CExt_Q = F₂⁴ ⊕ (Q^×/Q^{×2})² | integral case Open (D.11); rational part absent | Z part: yes, correct (§3.2); Q part not checked |
| E.9, E.13 (scope) | positive-power theorem and universal property for all affine finitely presented G over Z, no flatness | replaced by the linear versions E.10, E.14 | yes, the E.9 argument is correct (§3.2) |
| C.12 | image of A_P(Z/4) in PGL(2,Z/4) is PSL(2,Z/4) (order 24); diag(3,1) does not lift | absent | not checked (descent argument long) |
| C.8 (part) | A_P(F₃) = A₄ (order 12, C₃ malnormal in A₄); A(F₅), A(F₇) countably infinite | F₃ projective, F₅, F₇ values absent | A_P(F₃) = A₄: correct |
| D.3 | no continuous G_Q → M(Ẑ) with the prescribed cyclotomic determinant | absent | not checked |
| D.4 (argument) | every continuous Galois image in M(Ẑ) is nonopen (Z₇-rank ≥ 2 of M(Z₇)^ab against rank 1 of G_Q^ab) | replaced by the conditional sign argument | correct for G_Q |
| E.2 | over an imperfect field a geometrically additive section need not descend (wound groups) | absent | not checked |
| E.15 | E_Γ → Γ̂_const is fpqc but not an fppf epimorphism (Γ = Z over Z_(p)) | absent | not checked |
| E.1 (part) | char-0 fields: all targets | E.2 is for linear targets over Q-algebras | — |
| E.25 (part) | Q[𝔖] is not the restriction of a comodule | absent | not checked |
| A.9 (part) | weakened commutator conditions do not give chart membership (F₅ pair) | absent | not checked |
| B.6 (part) | norm-one tori at 2 (non-reduced) and 3 (smooth) | partly in B.3, B.10, D.2 | — |
| B.15 | general unit-v model (norms a²+ab−vb², c²−vd²) | only identities in `AB_identities.py` | not checked |
| B.18 | unrestricted normality of cusp complements false (GL(2,F₃)) | absent | not checked |
| B.20 | affine translation cocycles; nonsplit 2Ẑ extension | replaced by the finite nonsplit model in B.18 | — |
| C.10 (part) | missed projective word-image lists | counts only (C.7 table) | — |
| F.2 (part) | the GL(2,Z) quotient is the split orientation extension of 𝔖 | order-24 case in E.19, splitting not stated | not checked |
| F.3 | Klein-bottle lattice model nonsplit over Z and F₂ | absent | not checked |

## 3. Gaps and open items in full

**Wrong: none.**

### 3.1 E.22: the right statement, the wrong covering

E.22 proves that the quotient 𝔖 → 𝔖₃ induced by SL(2,Z) → SL(2,F₂) extends to 𝔖_M and to E_𝔖 as a map to the constant
group, and that the unipotent completion of 𝔖 is trivial. That is correct. But the report's coverage row
(AfterBISITE.Stallings: "nilpotent/pro-p approximations miss the change in the S3 covering, while the modular envelope
retains that quotient") and the title present it as the answer to Part E (f), "prove that the envelope of 𝔖 detects the
covering with group 𝔖₃, or that it does not". The covering of the prompt is BISITE's: the free group F₂ = Π₀ =
π₁(P¹−{0,1,∞}) acting on three letters by x ↦ (12), y ↦ (13). The 𝔖₃ of E.22 kills Π₀ (λ₀ ≡ λ₁ ≡ I mod 2); it is the
covering of the λ-line over the j-line, not a covering of P¹−{0,1,∞}. Every finite quotient of 𝔖 = SL(2,Z)/[Π₀,Π₀]
restricts on Π₀ to an abelian quotient, while (12) and (13) do not commute; so the BISITE covering does not factor
through 𝔖, through 𝔖_M or through E_𝔖. This is the first half of 11 Nov E.23, which the rerun dropped. The covering is
seen by the modern metabelian quotient Π₀/Π₀″ (𝔖₃″ = 1), which is not virtually abelian (E.22's own proof: it maps
onto Z ≀ Z), and by the envelope of the virtually abelian quotient Π₀/[K,K], K the kernel of the covering.
*To close:* add to E.22 the negative statement and its one-line proof; correct the coverage row.

### 3.2 D.11 (open in the rerun) is settled for M over Z by the 11 Nov argument

11 Nov D.16 proves CExt_Z(M, μ₂) = F₂³ with representatives z² = δ(m)^a e(m)^b t(m)^c. I checked the argument:
(1) N = M⁰⁰ = ker(e,t) is smooth over Z with geometrically connected fibres (the norm-one parts at 2 and 3 are smooth
and connected), hence normal and integral; (2) Ext_cen(N_Q, μ₂) = ⟨δ⟩, because over Q̄ the classes are
⟨δ, a₁, z₁⟩ (a₁, z₁ eigenvalues on the Eisenstein and Gaussian tori), the conjugations of Q(√−3) and Q(i) send
a₁ ↦ δ/a₁ and z₁ ↦ δ/z₁, and H¹(Q, Hom(N_Q̄, μ₂)) = 0; (3) after subtracting the δ-cover the
generic splitting over N_Q extends over N, since the finite flat cover's algebra maps into O(N)⊗Q integrally and O(N) is
normal; it stays a homomorphism and normal by density; (4) the quotient by it is a central extension of M/N = μ₂² by μ₂,
commutative by the argument of the rerun's D.10; (5) its Cartier dual is an extension of C₂ by C₂², étale, hence constant
over Spec Z (Minkowski), hence one of the four classes z² = e^b t^c. The eight classes are distinct already over C (D.9).
So CExt_Z(M,μ₂) = F₂³. The rerun's named first instance, Ext_cen(M[0]_{Z₂}, μ₂) → Ext_cen(M[0]_{Q₂}, μ₂), yields to the
same steps except (5): over Z₂ finite étale group schemes need not be constant, so unramified twists (H¹(Z₂, C₂²)) may
add classes; that count I did not do.

### 3.3 The other open items are honest

A.9, B.8 (B.8.5: surjectivity of u_{α,β,μ} for SL(2,Z)^), B.16 (R1–R3), B.18, C.11, D.7 (first instance: n = 3, λ = 1,
f(x,y) = [[1,1],[1,2]]), E.11 (non-linear targets; first tests Q[ε]/ε² and Z/4) and E.20 (first case over F₂; deck test
q₂) each state the proved cases, the computations and the exact first missing step, as the prompt requires.

## 4. Programs

| Program | Rerun | Output vs shipped |
|---|---|---|
| AB_identities, AB_enumerate (+AB_core), AB_general_finite, AB_signed_finite, AB_functoriality, AB_modular_comparison, B_late_sections, C_presentations | exit 0 | stdout and JSON identical |
| D_finite, D_components, D_gt, D_number_fields, D_arithmetic, D_motives | exit 0 | stdout identical |
| E_integrality, E_envelope, E_automorphisms | exit 0 | stdout and JSON identical |

Differences found: none, apart from line endings (CRLF) and SymPy 1.13.1 against 1.14.0, which changed no output.
Some statements are printed, not computed, by the programs (for example the Jacobian ideal (4) and the fibre
descriptions in `AB_identities.py`, the reducedness of the 12-syllable word in `C_presentations.py`); I checked those
by hand (B.3: every 5×5 minor contains the factors 2e·2f of the sign equations, and 4 is reached because (2, c, d) is
the unit ideal on M). `rerun\indep_checks.py` recomputes, independently: B.12, the identity C.4 = I, the matrix lemma of
N1, E.6 and its sharpness family at p = 2, 3, 5, the affine model of E.16, λ₀ ≡ λ₁ ≡ I mod 2 and the non-commuting
BISITE images (§3.1), the splitting of (−3,3), the discriminant and Eisenstein certificates of D.16, the F₂(t)
non-square of A.7, and the Schreier rank of 11 Nov E.28.

Not run: the register and assembly scripts (`AB_registers.py`, `AB_modular_comparison_registers.py`,
`B_late_sections_registers.py`, `D_registers.py`, `E_registers.py`, `assemble_package.py`), which only regenerate the
CSV/JSON registers and the report from the component files; `build_pdf.py` (builds a TeX format and calls LuaLaTeX; on
this MiKTeX host it could trigger on-the-fly package downloads, which the brief excludes); `render_audit.py` and
`package_delivery.py` (PDF rendering, manifest). None computes mathematics. The manifest itself was verified (132/132).

## 5. Readings checked against the second-pass text

| Place (current text) | Return's reading | Finding |
|---|---|---|
| C3 scan 266, (16) (`LM_C3-264-282_checked.tex`) | B+D−C = 1 is a slip for C+D−B = 1 (A.6) | the text reads B+D−C; the same page displays ξρ = [[−B,A+B],[−D,C+D]], whose trace is C+D−B: the slip is the author's |
| C3 scan 336, (62)–(63) (`LM_C3-321-339_checked_fixed.tex`) | constant Z/2, Z/3, Z/4, Z/6, not μ_n; "Gl(2)" (C.1) | confirmed, including "la seule relation" and Gl(2)_Z |
| C3 scan 479, (3) (`LM_C3-473-491_checked.tex`) | M = {det U = det b = ε′ det a} (A.1) | confirmed, with the struck coordinate order |
| C3 scan 480, (12 bis), (14) | ε₃ = det a/det b; b ᵗb = ε omits det b (A.6) | confirmed |
| C3 scan 546, (64) (`LM_C3-530-548_checked.tex`) | β′ = τ′^ν β, left factor (B.14) | confirmed; the return's correction to the right factor is mathematical |
| C3 scan 611, (115) (`LM_C3-606-624_checked.tex`) | cup product of the classes of Q(√−3), Q(√3), claimed ≠ 0, written in H² (D.12) | confirmed; the claim is false for this cup product |
| C3 scan 631 (`LM_C3-625-643_checked.tex`) | "ne peut guère être que Z/4Z" names the inverse-image group ℰ″, not a Brauer order (D.13) | confirmed by the margin ("σ = σ_∞ … est bien d'ordre 4, donc ℰ″ ≃ Z/4Z") |
| C4 scan 9, (9)–(12) (`LM_C4-001-019_checked.tex`) | "pour n = 3 idem" false; (11) drops the linear term (E.4, E.5) | confirmed: (11) is derived "par hyp." from φ(±1) with X ∈ M₄(K) |
| C4 scan 25 (`LM_C4-020-038_checked.tex`) | "métabélien" = finite-index commutative f.g. subgroup (E.12) | confirmed verbatim |
| C4 scan 31, (58) | Hom is printed as lim← (E.14) | confirmed; the correct limit is lim→ |
| C4 scan 35, (13) | 𝒢^Δ(Ẑ) ≃ 𝒢^∧ (E.17) | confirmed |
| C4 scan 41, (31)–(32) (`LM_C4-039-057_checked.tex`) | sign alternatives; epi only in char ≠ 3; finer scheme smooth (E.24) | confirmed: both "−\|+" alternatives, the margin on char 3, and the remark that Z̃ is the better object |

The readings register has 94 rows; these twelve places are the ones the new and changed mathematics depends on. No
reading of the return disagrees with the current text.

## 6. Consequences for the prompts

LM4, LM5 and LM6 do not mention LM1 (searched): nothing changes there. LM7 and LM8 do not cite LM1 statements (they
predate both returns) but ask what Part E answers. Both prompts are generated: Part B (b) of LM8 lives in
`push_rewrite_20261111.py`, the exactness follow-ups in `followups_block.py` (KNOWLEDGE_HANDOFF_LM.md: edit the
scripts, not the prompts); an "After LM1" block would sit beside `after_lm2_block.py`. The texts below are for whoever
edits them; I changed no file.

**Both prompts: a new block "After LM1 (added 12 November 2026)".**

> Package LM1_GROUP_SCHEMES has been answered twice by GPT-6 Astra (ChatGPT Pro mode): on 11 November as a text
> edition (98 statements) and on 12 November as a full package (84 statements: 54 Proved, 5 Known, 16 Refuted,
> 9 Open), reviewed line by line by Claude Opus 5.5 (effort max) (`LM1_review/REVIEW.md`): no statement wrong, one
> with a gap (E.22). Statements are cited as LM1 E.n (12 Nov) and LM1-11Nov E.n. The review is not authority.
> - *The envelope of §50.* "Métabélien" in §50 means finitely generated virtually abelian (C4 scan 25; LM1 E.12). For
>   such Γ with normal lattice M ≅ Z^r and H = Γ/M the finite stage is ∐_{h∈H} A^r_Z with law
>   (m,h)(n,k) = (m + a_h n + c(h,k), hk); E_Γ = lim_n Γ_{nM} has O(E_Γ) = lim→ ∏_{Γ/nM} Z[x₁,…,x_r], kernel
>   Spec(Z + (x)Q[x]) over the proconstant Γ̂, fibres (E_Γ)_{F_p} = Γ̂_{F_p} (E.13), points E_Γ(Z) = Γ,
>   E_Γ(Z_p) = Γ̂, E_Γ(Ẑ) = ∏_p Γ̂ (E.17). Hom((E_Γ)_A, G) is the set of fibrewise quasi-unipotent Γ → G(A) for every
>   ring A and closed finitely presented G ⊂ GL_{r,A} (E.14; Hom is a direct limit, correcting (58), scan 31), and for
>   affine finitely presented G over Z (LM1-11Nov E.13). (E_Γ)_Q is neither the pro-algebraic nor the Malcev
>   completion (E.18).
> - *𝔖 = SL(2,Z)/[Π₀,Π₀].* Π₀ = ⟨λ₀,λ₁⟩ is free, normal of index 12 (24 in GL(2,Z)); SL(2,Z)/Π₀ ≅ SL(2,Z/4)/V₄ ≅ Dic₃;
>   the action on M = Π₀^ab is R = [[0,−1],[1,−1]], S = [[0,1],[1,0]], and τ′ acts by −S; 𝔖^ab = Z/12; the finite
>   stage is ∏₁₂ Z[x,y] with the integral cocycle c(h,k) = t_h + a_h t_k − t_{hk} from ρ ↦ (R,0),
>   σ ↦ (S,(1/3,−1/3)) (E.15, E.16). Its rational relative completion over H with abelianized unipotent kernel is this
>   finite stage, not the envelope (E.19). Over Q the automorphisms of 𝔖_M preserving M, with conjugators in M and
>   the loop relation, form G_a ⋊ G_m; the fine parameter scheme of scan 41 is Spec Z[a,b,k,(12k+6ν₂+4ν₃+1)⁻¹] per sign
>   pair, smooth at 2 and 3 (E.24); generator images do not determine automorphisms over F_p[ε]/ε², and ε₃ is extra
>   data (E.25). The comparison with the signed M_{ρ,σ}, N_{ρ,σ} of §§49–51 is open (E.20; first case over F₂).
> - *Coverings.* LM1 E.21 proves the Stallings lead (checked). The BISITE covering of P¹−{0,1,∞} (x ↦ (12),
>   y ↦ (13)) does not factor through 𝔖 or its envelope (LM1-11Nov E.23; LM1 E.22 concerns the different quotient
>   SL(2,Z) → SL(2,F₂), trivial on Π₀). It is seen by Π₀/Π₀″, which is not virtually abelian (it maps onto Z ≀ Z), and
>   by the envelope of Π₀/[K,K], K its kernel.
> - *Fermat level.* For F₂ → (Z/n)² the relative completion over Q has free prounipotent kernel of rank n²+1 and
>   abelian-kernel quotient of dimension n²+1 (LM1-11Nov E.28, Schreier); it is not M_{ρ,σ,Q} (dimension 6).

**LM8.**

| Place | Action | Text to use |
|---|---|---|
| Lead 1 | correct | after "envelopes of their nilpotent or solvable quotients, as in §50" add: "(§50 itself defines envelopes only of finitely generated virtually abelian groups, LM1 E.12; non-abelian nilpotent quotients and the free metabelian quotient are not virtually abelian, LM1 E.22)" |
| Part B (b) | correct | "from the schematic envelopes of §50 (LM1_GROUP_SCHEMES, Part E, if attached)" → "from the schematic envelopes of §50 (LM1 Part E, attached; see After LM1). §50 covers only virtually abelian groups: either use the virtually abelian quotients π/[K,K], K open normal, or construct the envelope you need and prove its universal property in the form of LM1 E.14" |
| Item 3 and Part D | add | after "integral one-parameter subgroups (scans 210–221)": "LM1 (checked) gives: over a torsion-free base an integral G_a through g exists iff all (log g)^i/i! are integral, and is unique (E.3); a fibrewise unipotent integral section can fail this, first in rank 5 (superdiagonal (1,2,3,2), X⁴/4! = E₁₅/2), and over Z_(p) the sharp bound is rank ≤ p² (E.6); for closed finitely presented G ⊂ GL_r over any ring, g is fibrewise quasi-unipotent iff a power lies on a G_a (E.10), and for affine finitely presented G over Z (LM1-11Nov E.9); open: non-linear G over Q[ε]/ε² or Z/4 (E.11). Apply these to the Dehn twists." |
| Follow-up (2) | correct | "Two leads, unverified: by Stallings's theorem … Prove or refute both. S_3 is metabelian and not nilpotent: decide whether his "approximation minima" (§51) sees this covering where no nilpotent approximation does." → "The first lead is proved (LM1 E.21, checked): the endomorphism induces automorphisms of every F/Γ_{c+1}F, every pro-p completion and the rational prounipotent completion, and pulls the action back to orbits {1,2},{3}. Prove or refute the second (the covering is in Fib_{W_𝔞} for no 𝔞 factoring through the nilpotent quotients). His "approximation minima" (§51) does not see the covering: its finite quotients restrict to abelian quotients of Π₀ (LM1-11Nov E.23; LM1 E.22 is about SL(2,Z) → SL(2,F₂)). The next level π/π″ sees it (𝔖₃″ = 1) but is not virtually abelian, so §50 does not apply to it as written. Decide for each 𝔞 in your list." |
| Follow-up (3) | correct | "identify that relative completion with his M_{ρ,σ} and N_{ρ,σ} or state the exact difference" → "start from LM1: for F₂ → (Z/n)² the abelian-kernel quotient has dimension n²+1 (LM1-11Nov E.28), so it is not M_{ρ,σ,Q}; for SL(2,Z) → H of order 12 (24) it is the finite stage 𝔖_{M,Q} (LM1 E.19); his M_{ρ,σ}, N_{ρ,σ} are built from automorphisms with conjugators (§49; LM1 B.11, B.13, E.24). Construct their action on these relative completions and compute kernel and image, beginning with q₂: F₂ → (Z/2)² (LM1 E.20)" |
| BACKGROUND | update | "If available, the outputs of LM1_GROUP_SCHEMES (Part E) and LM7_FERMAT_TOWER" → attach `LM1_return/` (the 12 Nov package), `LM1_11Nov/sections/E.tex` and `D.tex` (for 11 Nov E.9, E.13, E.23, E.28, D.16) and this review |

**LM7.**

| Place | Action | Text to use |
|---|---|---|
| Part A (c) | add | "LM1 E.15, E.16, E.19 (checked) give Π₀ free on λ₀, λ₁, normal of index 12 (24 in GL(2,Z)), SL(2,Z)/Π₀ ≅ SL(2,Z/4)/V₄ ≅ Dic₃, the matrices R, S, −S and an explicit integral cocycle. Start from these and spend the program on the order 32 of scan 64 and on GL(2,Z/12Z)." |
| Part A (d) | add | "For the §48 groups LM1 B.5 gives M(0) ≅ H via (a,b) ↦ (a,b,diag(det b,1)), M(1/2) = M(s) = {U = b}, M(−j̄) = M(r) = {U = a} only over ε′ = 1, and B.3 gives M smooth exactly over Z[1/2], with F₃-fibre four smooth components and F₂-fibre one component of generic length 4. Identify the §51 groups with these or state the difference (LM1 E.20)." |
| Part B (d) | add | "LM1 E.16–E.17: the extension of Dic₃ by M with its integral cocycle; E_𝔖(Ẑ) = ∏_p 𝔖̂, its Δ-points 𝔖̂ (scan 35 (13))." |
| Part D (d) | add | "LM1 D.2: N(Z₂[i]^×) = 1+4Z₂ and N(Z₃[ζ₃]^×) = 1+3Z₃, so ε₂ = χ₄(μ) at 2 and ε₃ = (μ/3) at 3 on M(Z_p); D.4: an image respecting the global signs lies in a closed subgroup of infinite index of M(Ẑ); B.15 (checked): effective automorphisms act on SL(2,Ẑ) by Ad[[μ, aμ],[0,1]]." |
| Part E (a) | add | "(π/π″ is not virtually abelian, LM1 E.22, so §50's envelope does not apply to it as written: define the envelope you use.)" |
| Follow-ups (2), (3), BACKGROUND | as for LM8 | same replacement texts; BACKGROUND line "If available, the outputs of LM1_GROUP_SCHEMES (Part E: the envelope of 𝔖)" → the attachments named above |

**Outside the prompts.** The LM1 return should be published with a note that four checked 11 Nov results are not in
it (E.23, E.28, D.16 integral part, E.9/E.13 affine scope) and that the 11 Nov text edition remains the source for them.

## 7. Limits of this review

The imported theorems were taken at the statements the return gives and not reopened: Farb–Margalit (A.10), Conrad
(C.2), Serre 1968–69 (C.9), Hain–Matsumoto (D.18), Rivera–Wierstra–Zeinalian and Toën (E.23), Herfort–Ribes 1984
(B.16, an announcement), Milne (D.13–D.15), Schneps's conventions for (I), (II) (D.5). The long formal constructions
B.13, B.15 (outside the matrix lemma N1, which was checked in full), B.16 (proved parts), B.18 (proved parts) and D.20
were read in outline; their finite models were rerun and match. The 11 Nov statements marked "not checked" in §2.2 were
not reviewed; nor was the 11 Nov edition as a whole. The paper PDF was not compiled or inspected.
