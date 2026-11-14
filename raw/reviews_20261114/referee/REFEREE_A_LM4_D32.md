# Referee A: LM4 D.32 (the three-cusp rank test and finite pure loop groups)

By Claude Opus 5.5 at effort max (referee A), 14 Nov 2026, second task from the main session (Claude Opus 5.5 at
effort max). Return checked: LM4_FINITE_GROUP_ACTIONS (snapshot 2026-11-14 01:56 UTC) by GPT-6 Astra (ChatGPT Pro
mode), `C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers\LM4_FINITE_GROUP_ACTIONS_20261114T0156Z_unzipped\`.
Read: `LM4_FINITE_GROUP_ACTIONS_paper.tex` lines 31206-31428 (D.32 and the appended Lochak-Schneps source check),
30063-30266 (D.28 in full), 28846-28870 (D.10), 225-241 (A.7), 28889-28903 (D.12, for context); register rows D.32,
A.1, A.7, D.10, D.25, D.28. Primary sources opened: Kochloukova-Zalesskii 2007 (author manuscript), Harbater-Schneps
2000 (authors' preprint), Herfort-Ribes 1985 (GDZ scan), Lochak-Schneps 1997 (Invent. Math., pp. 571-574), Schneps'
1997 survey of `ĜT` and Lochak-Schneps' "Open problems in Grothendieck-Teichmüller theory". Pro's program
`three_cusp_rank_d32.py` was not run.

## Verdict

**D.32: proved as claimed.** Every finite subgroup of the pure three-cusp group `P ⊂ Out(F̂(x,y))` (outer classes
preserving each of the procyclic classes of `x`, `y`, `(xy)⁻¹`) maps injectively by `λ_2` into `{±1}`. So it has order
at most 2, and a nontrivial element of finite order is an involution with `λ_2 = −1`. The same holds for
`ĜT_0 ≤ P` (hence for `ĜT`). For the full three-cusp group, `g ↦ (σ_g, λ_2(g))` is injective on every finite
subgroup. I found no gap. Every step is checked below, with scripts for the finite parts. Three things the proof
does not do, and the claim does not assert: it does not show that an involution is conjugate to `(−1,1)`, it does not
show that its multiplier is `−1` at every prime (that is D.34), and it does not realize the abstract image
geometrically by conjugacy.

**The decisive steps.**
1. *Normalization (lines 31314-31340).* `P` is the Belyi group of Harbater-Schneps eq. (2), through a homomorphic
   section into `Aut F`. So an element of order `p` in `P` is an actual automorphism `α` of order `p`.
2. *D.28 for `P` (lines 31342-31350; D.28 lines 30090-30227).* Suppose `λ_p = 1`, which is automatic for odd `p`.
   - The Magnus argument makes `α` the identity on `F^{(p)}`.
   - Each peripheral normalizer in `E = F ⋊ C_p` then contains an element of order `p`: the extension class is
     `m_i` modulo the norm, and the pro-`p` quotient shows `(m_i)_p ∈ pZ_p`.
   - The profinite Brown theorem (Kochloukova-Zalesskii 2007, Theorem 2, which is Scheiderer's Corollary 12.19) bounds
     `Σ_{[T]} (1 + dim H¹(C_F(T), F_p)) ≤ 3`. The conclusion: there is one class of sections, and the fixed subgroup
     `C` has `dim H¹(C, F_p) = 2` and contains conjugates of all three groups `c_i^{e_p Z_p}`.
   - None of this uses the `GT_0` equations. I checked this line by line.
3. *The closed-subgroup fact (lines 31232-31312).* Suppose `C` is a closed subgroup with `dim H¹(C, F_p) = 2`
   containing conjugates of the three `c_i^{e_p Z_p}`, and `C ≠ F`.
   - Then `C` lies in an open `U` with `p | [F:U]`.
   - In the corresponding cover of the pants, the three boundaries through which the `c_i^{e_p Z_p}` pass have degree
     prime to `p`, and there is at least a fourth boundary.
   - So their classes are independent in `H_1(U, F_p)`.
   - Restricting to `C` gives three independent characters of `C`, which contradicts `dim H¹(C, F_p) = 2`.

   Hence `C = F`, `α = 1`, a contradiction.

**Is it new beyond Lochak-Schneps?**
- *Lochak-Schneps 1997* (Invent. Math. 127, Prop. 4) prove that complex conjugation `(−1,1)` is self-centralizing in
  `ĜT` and that `ι` has trivial fixed points in `F̂_2`. That is a different statement.
- *Schneps' 1997 survey* (`ĜT`: a survey, §1.4, question (4)) lists "Is there any torsion in `ĜT` apart from the
  elements of order 2 given by `(−1,1)` and its conjugates?" as open. The only result it records is the weak one
  (with Pop): such torsion becomes trivial in the pronilpotent quotient.
- *Lochak-Schneps' "Open problems"* (question 1.4) still asks whether the conjugates of `(−1,1)` are the only elements
  of finite order in `ĜT`.
- *The 1994 paper* (Lochak-Schneps, "The Grothendieck-Teichmüller group and automorphisms of braid groups", LMS LN
  200) I could not open. The two later texts by the same authors record the finite-order question as open after it,
  so whatever it proves about involutions, it does not contain D.32's bound.

D.32 therefore goes beyond these sources: it settles the order part of the Lochak-Schneps question, for all of
`ĜT_0` and the Belyi group, and leaves the conjugacy part open. I did not find a later source that proves it. My
search does not exclude one.

## Step-by-step (file `LM4_FINITE_GROUP_ACTIONS_paper.tex`)

### The closed-subgroup fact

| Lines | Claim | Verdict and check |
|---|---|---|
| 31232-31240 | If `C ≤ F` is closed, `dim H¹(C,F_p) = 2`, and `C ⊇ g_i c_i^{e_p Z_p} g_i⁻¹` for `i = 1,2,3`, then `C = F`. | Verified (rows below). |
| 31242-31253 (D.32c) | `colim_{U ⊇ C open} H¹(U,F_p) ≅ H¹(C,F_p)`. | Verified (a character of `C` factors through `C/(C∩V)` and extends to `CV`; injectivity through the open kernel). |
| 31255-31257 | `C` open ⇒ free of rank `1 + [F:C]` ⇒ `[F:C] = 1`. | Verified (Schreier). |
| 31258-31268 | `C` of infinite index ⇒ the `p`-valuations of `[F:U]` are unbounded. | Verified: if bounded, every restriction below a maximizing `U_0` has index prime to `p`, so it is injective on `H¹(−,F_p)` (corestriction). The `H¹(V,F_p)` of dimension `1 + [F:V]` then embed in the 2-dimensional colimit, and the indices are unbounded because `C` is the intersection of the `V` and is not open. |
| 31270-31286 (D.32d) | Cover of degree `n = [F:U]`, `p | n`; `U ∩ g_i L_i g_i⁻¹ = u_i ⟨h_i c_i^{d_i} h_i⁻¹⟩ u_i⁻¹` with `d_i` the boundary degree; `p ∤ d_i`. | Verified: `g_i⁻¹Ug_i = h_i⁻¹Uh_i`, and `h_i⁻¹Uh_i ∩ L_i = d_iẐ` contains `e_pẐ` iff `d_i` is a unit in `Z_p`. |
| 31288-31302 | The three boundaries are distinct; there is a fourth; the boundary classes satisfy only the sum relation; three of them are independent; `H¹(U,F_p) → F_p³` is onto. | Verified by hand (if each `c_i` had one lift, its degree would be `n`, divisible by `p`), and by script on 23,519 transitive actions (all labelled pairs for `n ≤ 5`, 3000 random ones for each of `n = 6,...,9`), with every prime `p | n` (26,519 cover-prime pairs): rank `n+1`, boundary rank `b−1` with zero sum, and every selection of three prime-to-`p` boundaries independent (127,045 selections). |
| 31304-31312 | Restriction to `C` and evaluation at `g_i c_i^{e_p} g_i⁻¹` stays onto (scalars `d_i⁻¹ ∈ F_p^×`): `dim H¹(C,F_p) ≥ 3`, a contradiction. | Verified (`g_i c_i^{e_p} g_i⁻¹ = u_i(h_i c_i^{d_i} h_i⁻¹)^{e_p/d_i}u_i⁻¹`). |

### Normalization and the application

| Lines | Claim | Verdict and check |
|---|---|---|
| 31314-31318 | The three peripheral exponents of an element of `P` are equal. | Verified (abelianization, `[c_1]+[c_2]+[c_3] = 0`). |
| 31319-31337 (D.32e) | Normalized representative `x ↦ x^λ`, `y ↦ f⁻¹y^λ f`, `f = y^{−b}kx^{−a} ∈ F′`; unique; the section is a homomorphism. | Verified (`C_F(x^λ) = ⟨x⟩` and `C_F(y^λ) = ⟨y⟩` by A.7, which here follows from Herfort-Ribes Theorem B′ for `F̂_2 = ⟨x⟩ ∐ ⟨y⟩`; composition gives `(λμ, fα(g))`). |
| 31338-31340 | Its image is the Belyi group of [HS, p. 3120, eq. (2)]. | Verified against the preprint (p. 4, eq. (2): `F(x) = x^λ`, `F(y) = f⁻¹y^λ f`, `F(z) ∼ z^λ`, `f ∈ F̂_2′`). |
| 31342-31350 | For an element of prime order `p` with `λ_p = 1`, D.28's proof applies to `P`: one class of sections, `dim H¹(C,F_p) = 2`. | Verified: every step of D.28 (table below) uses only that `α` is an automorphism of order `p`, the common multiplier, preservation of the three cusp classes, and `λ_p = 1`. |
| 31351-31355 | The three peripheral sections centralize `c_i^{e_p Z_p}`; conjugating them to `S` puts all three groups in `C`; so `C = F`, `α = id`, a contradiction. | Verified (`b_i c_i b_i⁻¹ = c_i^λ` and `λe_p = e_p`). |
| 31357-31365 | No odd prime divides the order of a finite subgroup; `λ_2` lands in `{±1}`; its kernel on a finite subgroup is trivial (Cauchy). | Verified (`μ_{p−1}` is the torsion of `Z_p^×` for odd `p`; the torsion of `Z_2^×` is `{±1}`). |
| 31367-31379 (D.32a) | For the full three-cusp group, `σ` and `λ` are homomorphisms and `(σ, λ_2)` is injective on finite subgroups; every subgroup of `S_3 × C_2` has a geometric realization. | Verified (`λ` is invariant under conjugation by the positively oriented anharmonic `S_3`). The realization: rotations preserving an equilateral triple on the equator, and reflection in the equator. This is attainment, not conjugacy, as stated. |
| 31381-31388 | Program note. | Not run; my own cover script replaces it. |

### D.28 as used (lines 30063-30266)

| Lines | Claim | Verdict and check |
|---|---|---|
| 30091-30095 | The normalized map is a homomorphism, so `α^p = 1`. | Verified (for `P`, by D.32e). |
| 30096-30103 (D.28b) | With `λ_p = 1` the finite-order normalized `α` is the identity on `F^{(p)}`, so `π : E → F^{(p)} × C_p`. | Verified. `α` acts trivially on `F^{ab} ⊗ Z_p`. D.10's Magnus argument (line 28867) is general: the least-degree correction of the `n`th iterate is `n` times the correction, and the graded pieces are torsion-free over `Z_p`. It uses no `GT` equation and holds at `p = 2` too. My own check is the same argument on the lower central series. |
| 30110-30123 (D.28c-d) | `N_E(L_i)` is an extension of `C_p` by `L_i`; `a_i c_i a_i⁻¹ = c_i^λ`, `a_i^p = c_i^{m_i}`, `(λ−1)m_i = 0`. | Verified. `N_F(L_i) = L_i` by A.7, which here follows from Herfort-Ribes B′ with the basis `{x, xy}` for `c_3`. The exponent `λ` is read off in `F^ab`. |
| 30125-30134 (D.28e) | `π(a_i) = (c̄_i^{v_i}, s)` and `(m_i)_p = pv_i`. | Verified (`C_{F^{(p)}}(c̄_i) = ⟨c̄_i⟩`, the pro-`p` case of Herfort-Ribes B′). |
| 30135-30147 | Norm computation: `N_λ u_i = −m_i`, and `b_i = a_i c_i^{u_i}` has order `p`. | Verified: `(ac^u)^p = a^p c^{uN_{λ⁻¹}}` and `N_{λ⁻¹} = N_λ` coordinatewise (`p` or 0). This is exactly the splitting of `H²(C_p, Ẑ(λ))`, whose only possible obstruction, at `q = p`, is removed by (D.28e). |
| 30149-30161 (D.28f) | `S_i` centralizes `c_i^{e_p}`, so `dim H¹(C_F(S_i),F_p) ≥ 1`. | Verified. |
| 30163-30198 (D.28g) | Brown via Kochloukova-Zalesskii Theorem 2: `Σ_{[T]}(1 + dim H¹(C_F(T),F_p)) = dim H^n(E,F_p) ≤ 3` for `n > 1`. | Verified. The theorem's hypotheses hold: `E` has no `C_p × C_p` (finite subgroups inject into `E/F`), and its open subgroup `F` has `cd_p F = 1`. The coefficients `F_p` are finite and `p`-primary, and `n > 1`. The bound is K-Z's (3): `dim H^n ≤ dim H⁰(F) + dim H¹(F) = 3`. "Dense embedding into a finite-dimensional source forces finitely many classes and an isomorphism" is K-Z's (4). Künneth for `N_E(T) = C_F(T) × T` is K-Z's (5). |
| 30200-30213 | All three `S_i` are conjugate; the common fixed subgroup has `dim H¹ = 2`; exactly one class of sections. | Verified (two classes would contribute at least 4). |
| 30215-30227 (D.28a) | `C^{(p)} ≅ F^{(p)}`. | Verified (projectivity of closed subgroups of free profinite groups; Hopfian). D.32 does not need it. |
| 30229-30265 | The limitation example `x ↦ x^u, y ↦ y^u` fails the third cusp in `D_7`. | Verified by script (`u ≡ 9 mod 14`; `x^u y^u ↦ r`, `(xy)^u ↦ r²`, not conjugate). Not used by D.32. |

### The appended source check of Lochak-Schneps Lemma 9 (lines 31391-31427)

Verified. `(λ,f)⁻¹(μ,f) = (λ⁻¹μ, 1)`. Relation (II) for `(ν,1)` with `n = (ν−1)/2` becomes `x^n(xy)^{−n}y^n = 1`.
Its Heisenberg central coordinate is `−n(n+1)/2` (script, `n = −12..12`), so `n_p ∈ {0, −1}` at every prime. The
dihedral evaluation in `D_q` holds exactly when `n` is even and `n ≡ 0 (mod q)`, or `n` is odd and `n ≡ −1 (mod q)`
(script, `q = 3, 5, 7, 11, 13`, all residues). Hence `μ = ±λ` globally. This paragraph is not used by D.32's proof.

## Dependencies, as cited against the register

| Dependency | Use in D.32 | Finding |
|---|---|---|
| A.1 | Presentation of the cover (genus `h`, `b` boundaries) | Standard; matches. |
| A.7 ("Known") | `C_F(x^λ) = ⟨x⟩`, `N_F(L_i) = L_i`, `C_{F^{(p)}}(c̄_i) = ⟨c̄_i⟩` | Holds. For `F̂_2` and `F^{(p)}` these follow from Herfort-Ribes 1985 Theorem B′ (free pro-𝒞 products of procyclic factors; read from the paper), independently of the Mochizuki citations in A.7. |
| D.10 | The Magnus argument | Verified. General: no `GT` equations, all `p`. |
| D.25 | Only through D.28: an alternative citation for the Magnus argument, and the Hensel unit in the limitation example | Not needed by D.32's proof. D.25's register statement cites D.32 for its last sentence. That is a circular citation between the rows, not circular logic in D.32. |
| D.28 | One class of sections; `dim H¹(C,F_p) = 2` | Proved; its proof holds for `P` as D.32 says. Its register statement is only for `GT_0`. D.32's wider use rests on the line-by-line check above, which the register does not record. |
| Harbater-Schneps 2000, eq. (2) | Naming of the image as the Belyi group | Verified (preprint p. 4 = journal p. 3120). Not a logical input. |
| Kochloukova-Zalesskii 2007, Theorem 2 and §1.1 (1)-(6) | Brown bound in D.28 | Verified from the author manuscript (`mat.unb.br/~pz/arquivos/Claus3.pdf`, pp. 3-4): Theorem 2 is quoted from Scheiderer, *Real and étale cohomology*, LNM 1588, Cor. 12.19. The hypotheses hold as stated above. |

## Scripts

`C:\Users\user\Documents\pro_intake_20261114\referee\checks\check_lm4_d32.py` → `check_lm4_d32.out`: **6 checks, 0
failed.**
- The cover rank test on 23,519 transitive actions (26,519 cover-prime pairs) and 127,045 boundary selections.
- The `D_7` certificate and the Hensel unit modulo `7⁶`.
- The Heisenberg and dihedral computations of the Lochak-Schneps source check.

Standard library only, `python -I -B`, reads no file of the return.
