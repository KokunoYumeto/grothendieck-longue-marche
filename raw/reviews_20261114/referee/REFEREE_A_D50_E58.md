# Referee A: LM7_PUSH D.50, E.58 and D.44 (as used)

By Claude Opus 5.5 at effort max (referee A), 14 Nov 2026, launched by the main session (Claude Opus 5.5 at effort max).
Return checked: LM7_PUSH checkpoint 09 by GPT-6 Astra (ChatGPT Pro mode),
`C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped\LM7_PUSH\`.
Files read in full: `sections\D_pronilpotent_lift_agent.tex` (D.50, 638 lines), `sections\E_relative_cm_lift_agent.tex`
(E.58, 468 lines), `sections\D_modular_coprime_agent.tex` (D.44, 925 lines), `sections\E_agent.tex` lines 1-170 (E.1,
E.2), the register rows D.25, D.44, D.50, D.52, E.1, E.2, E.3, E.9, E.58, E.65. Pro's code was not run; two of its
outputs were read for comparison only. Primary sources opened: Herfort-Ribes 1985 (GDZ scan of Crelle 358) and
Turaev, arXiv:0904.2692v1.

## Verdicts

| Row | Verdict |
|---|---|
| **D.44**, the parts D.50 and E.58 use (D.44.1, D.44.6-9, D.44.19-22, the converse paragraph of D.44.26-30) | **Proved as claimed.** The rest of D.44 (the relative-cover theorem through D.42/D.43, D.44.10-18, D.44.23-25, D.44.31-32) is not used by D.50 or E.58 and was not checked. |
| **D.50** (all four assertions: free source, modular source, the full lift of a pro-ℓ gentle pair, the prosolvable version) | **Proved as claimed.** Two places are worded loosely and are closed below (the Hopficity sentence, D.50 lines 454-459; the claim "centrality is used in the joint-generation step", which is true but that step is not needed). No mathematical gap. |
| **E.58** (the relative lifting theorem for every open normal `U`, the product decomposition E.58.2, and the element `(1,f)` with `q(A)=[5I]`, `q(β)=1`, bits `(1,0)`) | **Proved as claimed.** The errors are in the register's dependency list, not in the proof (see "Cited rows"). |
| Herfort-Ribes 1985, Theorem B′ | Statement confirmed from the paper (Section 4, printed p. 159). Its hypotheses hold for `C_2 ∐ C_3`. |
| Turaev 2009 | Not a logical dependency. Its Theorem 1.2 assumes a surface of positive genus, so it does not cover the pants; D.50 proves the genus-zero formula itself (D.50.11), and that proof is correct. |

**What this means for E.58's element.** The element exists as stated: there is a full profinite gentle pair
`(1,f) ∈ ĜT_0` with `f ∈ R_nil(H) ⊂ F′` (`H = F′F³`), whose normalized automorphism `Φ` of `B = C_2 ∐ C_3` fixes `τ`,
induces the identity on `B/R_nil(H)`, and has the unique pure frames `A, β ∈ H` with `q(A) = [5I]`, `q(β) = 1`
modulo 12. In E.1's convention (E_agent.tex lines 71-80, 118-119) its bits are `(1,0)`: the `r`-frame bit is 1
because the V₄-normalized lift of `[5I]` is `5I ≡ −I (mod 3)`, and the `s`-frame bit is 0. The frames are unique by
Herfort-Ribes, so the bits are invariants of the element, not of a choice.

**What it means for E.3.** E.58 shows that the multiplier-one part of `ĜT_0` contains an element in the extra CM
coset of E.1. If E.65 holds (a second referee checks it: that the parity is a continuous character `Δ` of `ĜT_0`,
equal to E.1's parity on the multiplier-one part, and zero on `G_Q`), then `Δ ≠ 0` on `ĜT_0` and E.3 is the genuine
question whether `Δ` vanishes on `ĜT`: if it vanishes, `ĜT ≠ ĜT_0`; if not, `ĜT` has a continuous quadratic
character trivial on `G_Q`, so `ĜT ≠ G_Q`. The failure case named in the brief ("if E.58 fails, Δ may vanish on all
of `ĜT_0`") does not occur: E.58 holds. My verdicts say nothing about E.65's own steps (the character property, the
vanishing on `G_Q`, the identification of the frames with the torsion representations of the CM curves).

## Independent computations

All scripts are mine, standard library only, run with `python -I -B`; they read no file of the return.
Folder: `C:\Users\user\Documents\pro_intake_20261114\referee\checks\`.

1. `check_e58_d44_finite.py` → `check_e58_d44_finite.out`: **52 checks, 0 failed.** D.44.7 (exactly four
   nonidentity Schreier generators `y⁻¹, x, x⁻¹, y` at `(r,s), (r²,s), (sr,s), (sr²,s)`), the D.44.8 table and D.44.9
   (in `PSL_2(Z)`, which is `C_2 * C_3`), the torsion ↔ cycle equivalence D.44.19-20 on 400 random elements of a
   finite quotient, and every finite claim of E.58: `|Q| = 576`; `q(F) ≅ V₄ × SL_2(F_3)` (96, bijective
   homomorphism, equal to the kernel of reduction mod 2); `q(H) = V₄ × Q_8` (32), normal, index 18; the affine model
   of `D = B/H` (54, `x, y` the two unit translations); `|J| = 1728` with kernel `q(H)` over `D`;
   `q([x,y]) = [[1,8],[8,5]]`, `q([x,y]²) = [5I]`, central of order 2, coordinates `(I, −I)`; `(z_0,1)` central in
   `J`; `r` of order 3 in `J`; bits `(1,0)`; `|C_{q(F)}(r)| = 6`, `|C_{q(F)}(s)| = 8`, and 24/24 equal/unequal bits
   over the 48 frame pairs (E.1's table); the chain of `τ¹²`: 24 distinct edges, coefficients ±1, zero boundary, in
   a graph with 576 edges and 480 vertices.
2. `check_d50_finite_theorem.py` → `check_d50_finite_theorem.out`: **19 tests, all pass** (7 s). A brute-force test
   of the finite theorem behind D.50.15-16, the case the evening intake asked for. For a source `Λ` (free on
   `x_1, x_2`, or `C_2 * C_3`), an epimorphism `q_E : Λ ↠ E`, a normal `A`, `D = E/A`, and every triple
   `h ∈ D³` for which `x_i ↦ h_i d_i h_i⁻¹` is a homomorphism, the script computes the obstruction to lifting the
   three conjugators to a peripheral map into `D# = Λ/[Λ,K]` (`K = ker(Λ → D)`; Reidemeister-Schreier and integer
   Hermite reduction). `D#` maps onto every `D†` of the proof compatibly with the source maps, so the theorem
   predicts: whenever the obstruction vanishes, the number of epimorphisms `Λ ↠ E` with `f(x_i) ∈ H_i T_i H_i⁻¹`
   equals the reference number. Every one of the 19 tests confirms this, on every transported class triple:
   - free source: `Q_8` with `A` its centre (`D = V₄`); `S_3 × S_3`, `S_4 × C_2`, `SL_2(F_3) × C_3`, `S_3 ≀ C_2`,
     `F_3² ⋊ Q_8`, `F_5² ⋊ Q_8` with `A = γ_∞(E)` (so `D` nilpotent: `V₄`, `C_3²`, order 8, `Q_8`); `SL_2(F_3)` and
     `GL_2(F_3)` with `A = γ_∞(E)` and with `A` the centre (`D = A_4`, `S_4`); `SL_2(F_5)` with `A` the centre
     (`D = A_5`);
   - modular source: `PSL_2(Z/N)` for `N = 6, 10, 12, 14, 18` with `A = γ_∞` of the pure kernel (the relative setting
     of E.58 with `U = F`; for `N = 12`, `|D| = 72` and 31,104 triples), and `PSL_2(Z/12)` with `A` the pure kernel and
     with `A = q(H)`.

   These triples include all the "centralizer" transports `q_1 = q_0`, `h_i ∈ C_D(d_i)` that E.58 uses.
   In the three non-split projective cases (`Q_8/Z`, `SL_2(F_3)/Z`, `GL_2(F_3)/Z`) the triples with a nonzero
   obstruction give count 0 against a reference count 1: the central refinement `D†` of the proof is necessary, and
   the proof uses it correctly. For `D = (Z/a)²` the Reidemeister-Schreier obstruction agrees on every triple with the
   Heisenberg formula `−v_1 + u_2 + v_3 − u_3 ≡ 0 (mod a)` (0 disagreements), an internal check of the script.

## Step-by-step: D.50 (`sections\D_pronilpotent_lift_agent.tex`)

| Step (lines) | Claim | Verdict and how checked |
|---|---|---|
| D.50.5 (63-69) | Setting: finite `1 → A → E → D → 1`, source `Λ`, `q_E`, `T_i` the `A`-class of `X_i`. | Verified. The hypothesis `[E,A] = A` is stated here but the count (D.50.11-16) uses only normality of `A`, as line 324 says. |
| Retained `J` (79-81) | `J ≤ E` onto `D` with `T_i ∩ J ≠ ∅`; `M = J ∩ A`, `e = exp J`. | Verified. |
| D.50.6 (82-100) | `J̃_ρ` is a finite group; `de` elements over each `g`; central kernel `μ_{de}`. | Verified by hand: implementers exist by invariance, are scalar multiples by Schur, `det(cB) = c^d det B`, so the fibre is `μ_{de}·B_0` when `det B_0 = 1`. |
| Graph of `M` (102-108) | `m ↦ (m, ρ(m))` is a normal embedding meeting the scalars trivially. | Verified: `det ρ(m)^e = det ρ(m^e) = 1`; conjugation gives the graph of `gmg⁻¹`. |
| D.50.7-8 (109-129) | `Q_ρ` central extension of `D` by `μ_{de}`; `J̃_ρ ≅ J ×_D Q_ρ`; `Ψ_ρ` restricts to `ρ` on `M`. | Verified (kernel and surjectivity as written). |
| Free auxiliary maps (131-135) | Any lifts of `d_1, d_2` define `R⁰_ρ`. | Verified. |
| D.50.9 (137-155) | Modular auxiliary maps with `B_s² = I`, `B_r³ = I`, determinants in `μ_e`. | Verified: `B_s²` implements `a_s² = 1`, hence is scalar; rescale; `det B_s ∈ μ_2 ⊂ μ_e` when `a_s ≠ 1`. Same for `r`. |
| D.50.10 (157-171) | `D†` = joint image; `Z = ker p` finite central. | Verified (`Z` embeds in `∏ μ_{de}`, central in the fibre product). |
| D.50.11 (173-228) | The pants count formula with the factor `(dim ρ)⁻¹`. | Verified by re-derivation: count = coefficient of 1 in `B_1B_2B_3 ∈ C[M]`; `B_i` centralizes `C[M]`; `e_ρ a e_ρ = 0` if `a` moves `[ρ]`; the first two quotient values generate `D` (`χ` onto); lifted sums are scalar by Schur; the product of the three lifts is `ρ(a_1a_2a_3)` because its `Q_ρ`-coordinate is `R_ρ(x_1x_2x_3) = 1`; regular character extracts the identity coefficient. Also tested numerically through its consequence (computation 2). |
| D.50.12-14 (230-264) | Genus-`g` formula, handle factor `(|M|/dim ρ)² I`, vanishing for moved `[ρ]`. | Verified by hand (Schur averaging, then matrix-coefficient orthogonality; `ι(P_{a,b}) = P_{b,a}`, `ι(e_ρ) = e_{ρ^∨}`). Not used by the theorem. |
| Turaev citation (265-269) | "Explicit finite model ... of Turaev Lemma 2.1 and Section 2.3; Theorem 1.2." | Accurate as a comparison. Turaev's Lemma 2.1 is the cocycle `ζ^ρ` of an invariant `ρ`; Section 2.3 defines `t_ρ` and `ζ^{ρ,γ}`; Theorem 1.2 counts sections over a surface **of positive genus** (Turaev p. 1, and §2.4: "Here it is essential that the genus of W is positive"). The pants is genus 0, so Theorem 1.2 does not apply there; D.50 does not need it (lines 268-269 say the pants case is proved in the text). |
| D.50.15 (271-289) | `T_i¹ ∩ J = j_i(T_i⁰ ∩ J)j_i⁻¹`; empty intersections match. | Verified: `j_i⁻¹H_i ∈ A` and `T_i` is `A`-invariant. |
| Transport (291-303) | `(j_i, r̃_i) ∈ J ×_D Q_ρ` conjugates each boundary summand; each trace sum is unchanged. | Verified. This is the only place the hypothesis on `q_1†` enters: its projection to each `Q_ρ` must satisfy `R¹_ρ(x_i) = r̃_i R⁰_ρ(x_i) r̃_i⁻¹` exactly. |
| D.50.16 (305-321) | Möbius inversion from homomorphism counts to epimorphism counts; modular counts factor through `C_2 * C_3`; reference count positive. | Verified (Hall's inversion; subgroups not onto `D` have count 0 since `q_j` is onto). Tested numerically on 19 cases (computation 2). |
| D.50.17 (323-346) | Joint image of `(f, q_1†)` is all of `E ×_D D†`. | Verified (Goursat; `Z` central, so `E` acts trivially on the common quotient, which `[E,A] = A` kills). **Not needed** by the compactness step, which uses only the conjugators in `E_0` and their images in `D_0`. |
| Ordinary conjugator union (348-361) | The full ordinary fibre has `t_1t_2t_3n_0` elements. | Verified: replace `r_i` by `r_i c`, `c ∈ C_{D†}(q†(x_i))`; distinct triples of `A`-classes give disjoint fibres; each has `n_0` by D.50.16. Not used by the theorem. |
| Residuals (363-389) | `R_nil(G) = ⋂ γ_n G` (closed terms); `f(R_nil(G)) = γ_∞(f(G))` for finite images; D.50.18; maximal nilpotent quotient. | Verified (compactness for the image of the intersection). |
| Nilpotent `D, D†` (390-396) | With `A = γ_∞(E)`, `D` and `D†` are nilpotent; auxiliary maps factor through `F_nil`. | Verified (central extension of class `c` has class ≤ `c+1`). |
| Modular residual (398-411) | `A = γ_∞(N)`, `N` the pure image; `[E,A] = A`; pure image of `D†` nilpotent; `B → D†` kills `R_nil(F)`. | Verified. |
| Compactness, free (413-463) | Closed conditions on `F̂³`; one finite `E_0` holds a finite set of them; the twisted map D.50.19; the finite theorem gives conjugators over the images of `b_i` in `D_0`; the limit `Φ` is onto and an automorphism; `q_nil Φ = α q_nil`. | Verified. Every condition is a cylinder condition; every nilpotent condition factors through `D_0 = E_0/γ_∞(E_0)`; `q_nil(h_i) = b_i` gives `q_nil Φ = α q_nil` on the generators. **Wording gap closed:** the Hopficity sentence (454-459, "contradicting its periodicity under preimage") is loose. The standard argument: for onto `Φ`, `U ↦ Φ⁻¹(U)` is injective on the finite set of open subgroups of index `n`, hence bijective, so every open subgroup contains `ker Φ`, and `ker Φ = 1`. |
| Compactness, modular (465-480) | Same with `B³`; `u_1² = u_2³ = 1` literally; Hopficity. | Verified (constraints on `B_nil` have nilpotent pure image, hence kill `γ_∞(q_{E_0}(F))`). |
| Normalization (482-488) | A conjugator that is 1 in the retained quotient lies in its kernel; conjugating by its inverse fixes that peripheral and keeps the induced map. | Verified. |
| D.50.20 (490-505) | `F/R_nil(F) ≅ ∏_p F^{(p)}`. | Verified (Sylow decomposition for the kernel; coprime Goursat and compactness for surjectivity). |
| D.50.21 (507-523) | `B_nil ≅ ∏_{p,S_3} B_p`. | Verified (lift the common `S_3`-value, correct by a pure element). |
| D.50.22 and conjugators (525-541) | The pro-ℓ pair gives `s ↦ sf_ℓ, r ↦ f_ℓ⁻¹r, τ ↦ τ` on `B_ℓ` (D.44.26-32); conjugators in `F^{(ℓ)}` by coprime complement conjugacy, `ℓ ≥ 5`. | Verified, through D.44's converse paragraph (lines 784-801) and profinite Schur-Zassenhaus. |
| Automorphism of `B_nil` (543-557) | `(α_ℓ, id, id, ...)` is a peripheral automorphism fixing `τ`; `f_0 = (f_ℓ, 1, ...) ∈ (F/R_nil F)′`. | Verified (closed derived subgroup of a product is the product of the closed derived subgroups). |
| `f ∈ F′`, literal image (559-569) | `f = sΦ(s) ∈ F`, trivial pure abelianization, image `f_ℓ` at `ℓ`. | Verified (the map `F → F^ab` factors through `F/R_nil F`). |
| D.50.23-24 (570-588) | `Φ(s) = sf`, `Φ(r) = f⁻¹r`, `Φ(x) = x`, `Φ(y) = f⁻¹yf`; torsion relations ⇔ the two gentle cycles. | Verified by hand (`sfs = f⁻¹` from `(sf)² = 1`; `(f⁻¹r)³ = f⁻¹·f(y,z)⁻¹·f(z,x)⁻¹`) and by script (computation 1). |
| Outer centralization (589-596) | `Φ Ad_b Φ⁻¹ = Ad_{Φ(b)b⁻¹} Ad_b`, correcting element in `F`. | Verified. |
| Prosolvable (598-623) | Same proof with derived residuals; for `B` the residual of `F` equals that of `B`. | Verified (perfect residual gives `[E,A] = A`; central extensions of solvable groups are solvable; the two quotient maps identify the residuals). |

## Step-by-step: E.58 (`sections\E_relative_cm_lift_agent.tex`)

| Step (lines) | Claim | Verdict and how checked |
|---|---|---|
| Normality (75-77) | `R_U` characteristic in `U`, normal in `Γ`. | Verified. |
| E.58.6 (85-96) | `E_0 ⊇ D`, `U_0 = ker(E_0 → D)`, `A_0 = γ_∞(U_0)`, `[E_0,A_0] = A_0`. | Verified. |
| E.58.7 (97-110) | D.50.5-17 applied to `A_0 ◁ E_0`; `E_1†` central over `E_1 = E_0/A_0`; image of `U` in `E_1†` nilpotent; `Γ → E_1†` kills `R_U`. | Verified. `E_1` need not be nilpotent; the finite theorem does not need it to be. Tested numerically with non-nilpotent `D` (computation 2, modular cases). |
| Twist and finite step (112-122) | Precompose by `α`; D.50.15-17 give an epimorphism to `E_0` with the conjugators over the images of `b_i`; every relative constraint kills `A_0`; modular source preserved. | Verified (a finite quotient of `Γ_{U,nil}` has nilpotent image of `U`, so kills `γ_∞(U_0)`). |
| Compactness, normalization (124-136) | As in D.50. | Verified. |
| E.58.8, E.58.2 (138-166) | `U/R_nil(U) ≅ ∏ U^{(p)}`; `Γ_{U,nil} ≅ ∏_{p,D} Γ_{U,p}`; componentwise automorphisms with common `D`-values are peripheral automorphisms. | Verified (same arguments as D.50.20-21). |
| `F`, `H` characteristic; E.58.9 (168-180) | Six epimorphisms to `S_3`, one kernel; `[B:H] = 54`, `F/H ≅ (Z/3)²`. | Verified by hand. |
| E.58.10-11 (182-205) | V₄-normalized representatives; `q(F) ≅ V₄ × SL_2(F_3)`; equals the kernel of reduction mod 2. | Verified by script. |
| E.58.12-13 (207-227) | `Q_8` generators; `q(H) = V₄ × Q_8`; `q` factors through `Γ_2 = B/O²(H)`. | Verified by script (`|q(H)| = 32`, a 2-group). |
| E.58.14-15 (229-250) | `J = Q ×_{Q/q(H)} D`, `|J| = 1728`; kernel of `Γ_2 → J` is pro-2. | Verified by script and by hand. |
| E.58.16 (252-269) | Affine model of `D`. | Verified by script (relations, order 54, `x, y` translations, kernel exactly `H`). |
| E.58.17-18 (271-290) | `q([x,y]) = [[1,8],[8,5]]`, `z_0 = q([x,y]²) = [5I]`, central, order 2, in `q(H)` with coordinates `(I,−I)`; `(z_0,1) ∈ C_J(r)`. | Verified by script. |
| Centralizer lifting (292-307) | Pro-`p` kernel, `a` of order prime to `p`: every element of `C_E(ā)` lifts to `C_G(a)`. | Verified (complements to the pro-`p` kernel in the preimage of `⟨ā⟩` are conjugate by the kernel; the generator matches because `⟨a⟩` meets the kernel trivially). |
| E.58.19 (309-323) | `c ∈ C_{Γ_2}(r) ∩ H^{(2)}`, `c ↦ (z_0,1)`, `c = u[x,y]²`. | Verified (`r` has order 3 in `Γ_2` and `J`; `c` has `D`-value 1). |
| E.58.20 (325-339) | `b_s = b_τ = 1`, `b_r = (c` at 2, 1 elsewhere`)` is in the fibre product and centralizes `r`; the identity of `B/R_nil(H)` is peripheral with these conjugators. | Verified. |
| Lift and frames (341-352) | `Φ` fixes `τ`; `β ≡ 1`, `A ≡ b_r` mod `R_nil(H)`; `A, β ∈ H`; `q(β) = 1`, `q(A) = z_0`. | Verified (`q` factors through the 2-primary component `Γ_2` of E.58.2). |
| E.58.21 (354-368) | `f ∈ R_nil(H) ⊂ H′ ⊂ F′`; the four formulas and the two gentle cycles; `(1,f) ∈ ĜT_0`. | Verified (as D.50.23-24; the restriction to the characteristic `F ≅ F̂(x,y)` is an automorphism). |
| E.58.22 (370-389) | Herfort-Ribes Theorem B′ gives `C_B(s) = ⟨s⟩`, `C_B(r) = ⟨r⟩`, both meeting `F` trivially; `A, β` unique. | Verified against the paper (see below). |
| E.58.23 (391-417) | `T = A⁻¹V = [5I]`, `W = 1`; the lift with mod-4 value in V₄ is `5I`, `≡ −I` mod 3; `ker(R − I)` mod 3 is spanned by `(1,2)`, sent to `(2,1)`: bits `(1,0)`. | Verified by script, in E.1's convention (E_agent.tex lines 71-80, 118-119); E.1's 24/24 split over the 48 pairs reproduced. |
| E.58.24-25 (419-443) | `x⁶ = τ⁻¹² ∈ H ∩ N_B` has primitive image in `N_B^ab`, order 6 in `G_6`, so `B → G_6` does not factor through `Γ_2`. | Verified by script (24 distinct edges, coefficients ±1, zero boundary; a cycle with a ±1 coefficient is primitive in the saturated cycle lattice). A side remark, not used. |
| `G_6` shadow (445-455) | `qΦ = q`, so `Φ` induces an automorphism of `G_6` with the frames (E.58.5). | Verified. E.58 rightly does not identify this shadow with any of E.9's twelve excluded representatives. One fact narrows it: `H` has 2-group image in `G_2 = B/N_B′N_B²`, so `Φ` induces the identity on `G_2`. Any recorded extra certificate that is not the identity on `G_2` is therefore a different element. |

## Step-by-step: D.44 as used (`sections\D_modular_coprime_agent.tex`)

| Step (lines) | Used by | Verdict |
|---|---|---|
| D.44.1 conventions (4-12) | D.50, E.58 | Verified (`τ = [[1,−1],[0,1]]`, `x = [[1,2],[0,1]]`, `y = ±[[1,0],[−2,1]]` in `PSL_2(Z)`). |
| D.44.6-7, free basis (105-140) | D.50, E.58 (`F = F̂(x,y)`) | Verified by script (Schreier generators) and by hand (quotient graph with 6 edges and 5 vertices, rank 2; completion of a finite-index subgroup). |
| D.44.8-9 (142-165) | D.50.24, E.58.21 | Verified by script in `PSL_2(Z)`. |
| D.44.19-21 (455-503) | D.50.23-24, E.58.21 | Verified by hand and by script. |
| D.44.22 (505-522) | D.50 (lines 589-595 reprove it) | Verified. |
| Harbater-Schneps identification (524-529) | the name `ĜT_0` | Verified against the authors' preprint (`webusers.imj-prg.fr/~leila.schneps/HS.pdf`, §0.1, p. 2): (I) `f(y,x)f(x,y) = 1`, (II) `f(z,x)z^m f(y,z)y^m f(x,y)x^m = 1` in `F̂_2 = ⟨x,y,z | xyz = 1⟩`, `m = (λ−1)/2`; `ĜT_0` is the set of `(λ,f) ∈ Ẑ^* × F̂_2′` satisfying (I), (II) and inducing an automorphism `x ↦ x^λ, y ↦ f⁻¹y^λ f`. At `λ = 1` these are D.44.5, and the automorphism condition holds for E.58's `f` because `Φ` restricts to an automorphism of `F = F̂(x,y)`. |
| Converse paragraph of D.44.26-30 (784-801) | D.50.22 | Verified: the assignment satisfies `s² = r³ = 1` by the two cycles; its `F`-image is pro-ℓ so it factors through `B_ℓ`; its restriction is `ψ_f` and it is the identity on `S_3`, so it is onto; `B_ℓ` is Hopfian. |
| Coprime torsion conjugacy (575-608) | the same argument as D.50 lines 534-541 | Verified. |

## Outside statements

**Herfort-Ribes 1985** (J. reine angew. Math. 358, 155-161; read from the GDZ scan, PURL
`http://resolver.sub.uni-goettingen.de/purl?PID=PPN243919689_0358|LOG_0014`). Theorem B′, Section 4, printed p. 159:
for pro-𝒞 groups `A_1, ..., A_n` and their free pro-𝒞 product `G`, `A_i ∩ A_i^x = 1` for `x ∈ G \ A_i`, and in
particular `C_G(a) = C_{A_i}(a)` for `a ∈ A_i \ 1`. Here 𝒞 is a class of finite groups closed under subgroups,
quotients and extensions (Section 2). Use in E.58.22: 𝒞 = all finite groups, `n = 2`, `A_1 = C_2`, `A_2 = C_3`, and
`B` is their free profinite product (the profinite completion of `C_2 * C_3`). The hypotheses hold, and E.58's
citation (Theorem B′, Section 4, p. 159) is accurate.

**Turaev 2009** (arXiv:0904.2692v1, "Sections of fiber bundles over surfaces"): Theorem 1.2 is
`|S(p,s_∂)| = |Φ| Σ_{ρ∈I_0} (|Φ|/dim ρ)^{−χ(W)} ζ^{ρ,γ}([W,∂W]) Π_k t_ρ(γ_k)`, for a Serre fibration over a compact
connected oriented surface **of positive genus** with finite `π_1` of the fibre. Lemma 2.1 constructs the 2-cocycle
`ζ^ρ` of an invariant irreducible `ρ`; Section 2.3 defines `t_ρ` and `ζ^{ρ,γ}`. D.50 cites these only for
comparison. Its own pants formula D.50.11 covers genus 0 and is proved in the text.

## Cited rows outside scope: statement as cited against the register

| Row | How E.58 / D.50 cite it | Register | Finding |
|---|---|---|---|
| D.25 | E.58 cites "LM7 D.25" (line 410) for the CM sign convention: the earlier LM7 return. | LM7_PUSH's own D.25 is "An order-five peripheral cycle obstructed by a central kernel of order two" (`A_8⁵`). | **Register error.** E.58's `depends_on` (and E.1's, E.2's, E.65's) points at the wrong row. The convention actually used is restated in E.1's proof (E_agent.tex lines 71-80), which E.58 matches. No effect on the proof. |
| D.44 | D.44.8 and D.44.19-20, D.44.26-32 | as stated | Matches (see the D.44 table). |
| D.50 | D.50.5-17, Hopficity | as stated | Matches. |
| E.1 | `T = A⁻¹V`, `W = β⁻¹V`, the bits | The register statement of E.1 is only the count table; the bit convention is in E.1's proof. | The convention used matches E.1's proof. The register statement does not contain it. |
| E.2 | "Task E.2 has a positive answer" | E.2 depends on E.58, and E.58 on E.2 | **Circular in the register only.** E.58's proof does not use E.2; E.2's proof is a summary of E.58. |
| E.9 | Comparison paragraph only (lines 451-455) | "excludes the twelve recorded extra shadows" | Matches. No logical dependency. |
| Turaev 2009 (D.50) | comparison | `depends_on` of D.50 | Not a logical dependency (genus 0 is outside its Theorem 1.2). |

## Not checked

- D.44 outside the parts listed (its relative-cover theorem via D.42/D.43, D.44.10-18, 23-25, 31-32), D.42, D.43.
- D.52 and D.1/D.2. They use D.50's pro-ℓ statement, which is proved here; their own steps are not checked.
- E.65 and E.61 (the second referee's scope); E.9's finite exclusions.
- Pro's programs `bc_scalar_cover_count.py`, `bc_relative_cm_sources.py` (outputs read for comparison only; they agree
  with mine on every shared number: 576, 96, 32, 18, 1728, `[[1,8],[8,5]]`, `5I`, bits `(1,0)`, 24 edges).
