# Intake: LM7_FERMAT_TOWER, the work after the first return

Claude Fable 5.2 (Anthropic), intake reader, 13 Nov 2026, about 14:10–15:10 UTC (clock read 14:56 and 14:57 UTC).
Asked for by the user on 13 Nov ("Make a 5.2 intake agent check the 9 hours of work by the model").

- Return read: `longue_marche_pro_pilot_20261104\answers\LM7_FERMAT_TOWER_20261113T1435Z_unzipped\LM7_FERMAT_TOWER\`
  (GPT-6 Astra, ChatGPT Pro mode; zip built 13:44 UTC; first line of the report: INCOMPLETE; 178 statements:
  154 Proved, 9 Refuted, 12 Known, 3 Open).
- Compared with the reviewed first return `...\LM7_FERMAT_TOWER_20261113T0227Z_unzipped\` (103 statements).
- Scripts (listing and comparing only): `diff_rows.py`, `rows.py`, `ct.py`, `st.py`, `blk.py` in the session scratchpad
  `C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\9fc52c26-b302-4eb7-b4c2-be7f7bbafcc9\scratchpad\s\`.
  No program of the return was run.

## 1. What is new

- **75 new rows**, all labelled Proved: D.27–D.49 (23 rows), E.37–E.62 and E.64–E.89 (52 rows). There is no E.63
  anywhere in the return (register, sections, code README): a gap in the numbering, nothing more found.
- **No row was removed and no status changed.** The three Open rows are still D.13, D.19, E.23.
- **Changed rows:**
  - D.20 (Known): statement widened from Ihara's cyclic-cover compatibility to the same for all of `GT̂`, with the
    equality `GT̂_K = GT̂_{A'} = GT̂`, cited to Enriquez 2007, Theorem 8.1 and Remark 8.6. Proof text +2.9 KB.
  - D.25 (Proved): the last sentence now says that D.27 proves the twelve selected shadows non-genuine.
  - D.13, D.19 (Open): statement blocks grew by 11.6 KB and 9.9 KB, all of it a record of D.24–D.49.
    **Nothing in them attacks the two questions of D.13 (weight 5, weight 9).**
  - E.23 (Open): statement block grew by 18 KB, a record of E.37–E.89.
  - D.11 (a space), D.26 (notes only). Every other block of `D.tex` differs by a few characters of spacing.
- Sections `A.tex`, `B.tex`, `C.tex` and the old E-sections are byte-identical to the first return.

## 2. What this intake rests on

- **Read with proof (17 rows):** D.27, D.34, D.36, D.45 with its supplement, D.46, D.47, E.37, E.38, E.39, E.40,
  E.41, E.42, E.43, E.44, E.61, E.66, E.73. About 300 KB of TeX. (For D.34 and D.36: the whole proof and most of
  the statement; the displayed formulas (D.34.8)–(D.34.9) and (D.36.6)–(D.36.8) were seen through the proof.)
- **Statement and the first part of the proof (2 rows):** D.48, D.49. They repeat the construction of D.47 over
  larger bases.
- **Statement only (56 rows):** all the others. Reason: the new sections are 1.26 MB of TeX and my bound was
  about 60 % of the context; I chose the rows the open items and the PS items hang on. A statement-level verdict
  says the statement is well formed and agrees with the rows I read; it says nothing about its proof.
- **Programs:** none run. Outputs opened and compared with the text: `d_cm_class2.out`, `d_cm_class2_two.out`,
  `d_cm_arithmetic_replacement.out`, `d_cm_rank2_centralizers.out`, `d_cm_rank2_degree9.out`,
  `d_cm_fermat_relative_tower.out`, `e_intrinsic_class2.out`, `e_next_depth.out`, `e_infinite_obstructions.out`,
  `e_higher_images.out`. Every number I compared agrees with the section text. No `.py` file was read line by line
  (only two greps in `d_cm_shadow.py`, `d_cm_class2*.py` for the centralizer handling).
- **Recomputed by hand here:** in D.46 the norm `a·ā = 7`, `η_* = (−3 − 8ζ²)/7 = (5 + 8ζ)/7`, its matrix
  `(11 8; 8 3)` mod 16, `η_* ≡ −1` mod 4, the Kummer commutator identity (D.46.11) and both vanishings, the
  2-adic image `1 + 2Z_2[ζ_3]` of `G_{Q(ζ_3)}` on `T_2(y² = x³ + 1)` (CM theory, from memory, re-derived);
  in D.47 `|H_12| = 6912`, rank 1153; in E.37 the count `7 + 9 + 5 + 24 = 45`, the minus-space `4·6 = 24`, the
  determinant formula (E37.15); in E.38 the coefficients `81·C(−1/6, n)` = 81, −27/2, 63/8, −91/16, 1729/384 and
  the valuation −1 at `n = 4`; in E.43 the density `1/6 − 1/18 = 1/9` and the list of primes below 320 against
  `p = a² + 27b²`.
- **Sources:** one opened. The arXiv abstract of Enriquez, *Quasi-reflection algebras and cyclotomic associators*
  (math/0408035), says: "Ihara's subgroup GTK ... defined using distribution relations, in fact coincides with it."
  That is D.20's new claim; the theorem numbers 8.1 and 8.6 are from the return. Everything else is "from the
  return", or from memory where the line says so.
- Not read: `report.md` beyond its first lines, the ledgers, `qa\`, the PDF, the manuscript. The PDF check
  (overfull boxes, rendered pages) is not done here.

## 3. Verdict table

Verdict codes: **P** proof read, no gap found; **S** statement level only (reason in section 2); **K** Known, change
read. "R:" names what a second reader should rerun. No row received the verdict gap or error.

### Part D (all 23 new rows concern D.19 (ii), the CM coset; none concerns D.13)

| Row | Statement head | Verdict | Where, and remarks |
|---|---|---|---|
| D.20 | (changed, Known) `GT̂_K = GT̂`; cyclic-cover and distribution identities for all of `GT̂` | K | `D.tex`. The reduction (Enriquez's `δ_n` is the filling map `φ_n`; additivity `c_{mn} = c_m + c_n`) was followed. Source: abstract opened, agrees; theorem numbers not checked. |
| D.27 | The 23 non-identity selected `G_6` actions of D.25 (all twelve extra-CM shadows) have no genuine lift; an alternate homology correction with the same CM pair lifts to `H_2 ×_Q H_3` | P | `D_cm_class2.tex`. Logic followed: Herfort–Ribes makes a genuine action conjugate `s`, `r`; (D.25.6) fixes the `Q`-coordinates of the conjugators; the remaining freedom is the fixed spaces of dimension 52 (at 2) and 34 (at 3) plus central corrections; survivors at 3 are pairs 1–4, at 2 pairs 1 and 17; only the identity is in both (outputs read). Herfort–Ribes Theorems A, A′: from memory, the statement used is right. R: `d_cm_class2.py`, `d_cm_class2_two.py`, `d_cm_quadratic_search.py`; and the claim (D.25.6) in `d_cm_shadow.py`. |
| D.28 | The alternate pair extends over a mixed kernel `F_3^385 ⋊ C_2²` (quotient `J` of order `2304·3^385`) | S | `D_mixed_prime.tex` |
| D.29 | It extends through the whole class-two pro-2 tower `H^(k)` and all odd relative completions | S | `D_cm_class2_tower.tex` |
| D.30 | Rank-4 kernel `K` over `Q_0 = S_3 × C_3`; the recorded representatives of D.27, D.29 have no genuine lift (degree 6); a replacement exists | S | `D_rank4.tex` |
| D.31 | A replacement through degree 7 (`T_2 = B/D_8K`) | S | `D_degree7.tex` |
| D.32 | That recorded action has no lift to `T_3 = B/D_9K` | S | `D_degree8.tex` |
| D.33 | A replacement through degree 8 and the class-two tower | S | `D_degree8_replacement.tex`. Excluded later by D.45. |
| D.34 | `K = π_1` of `w³ = z(z−1)` minus three points; `Aut_{Q_0}(P_2)` = automorphisms of `K^(2)` whose outer class centralizes `Q_0` | P | `D_rank4_geometry.tex`. Followed: genus one from the cycle types, the deck maps, `P_2 ↪ Aut(K^(2))` (trivial centre, faithful action on `H_1(K, F_2)`), the centralizer of `c_0`, determinant = cusp multiplier, the twist `ρ_{ℰ_0} = [ζ]^{−κ_{4,3}}ρ_{E_3}`. The 54 words and the matrix (D.34.16) are the program's. Used by D.46 and in 4.6 (PS-5). |
| D.35 | Every unit `η` of `Z_2[ζ_3]` is realized on `K^(2)` with multiplier `N(η)`; the whole torus by Galois over `Q(ζ_3)` | S | `D_odd_deck_lift.tex`. The Galois image used by D.46 (`1 + 2Z_2[ζ_3]` for `y² = x³ + 1`) was re-derived here. |
| D.36 | Quartic cover `v⁴ = z(z−1) ≅ y² = x³ − x`; the arithmetic joint graph of the cubic-mod-4 and quartic-mod-3 coordinates | P | `D_elliptic_pair.tex`. Followed: the isomorphism and its deck maps, the tangent factor `[i]^{κ_{−1,4}}`, the norm-one kernel of order 6 in `(Z_2[ζ_3]/4)^×`, the graph over `Q(ζ_12)` (sign `−1` on the cubic mod 4 goes with projective `[i]` on the quartic mod 3) through the field `M′` of D.25. Rests on D.25 and D.35. The return notes that the cover-to-fixed-fibre comparison is proved for Galois only (Nakamura–Tsunogai–Yasuda, as quoted by the return). D.46, D.47 rest on this row for "outside the Galois image". |
| D.37 | Fermat-12 joint quotient (order 6912, kernel rank 1153); a finite `GT_0` shadow with the extra pair | S | `D_fermat_joint.tex` |
| D.38 | The same jointly with `T_3` | S | `D_fermat_degree8.tex` |
| D.39 | An automorphism on the all-prime Fermat homology quotient jointly with `T_3` | S | `D_fermat_homology.tex`. This action is the one D.45 excludes. |
| D.40 | Extension by the identity through every finite perfect quotient of `B` | S | `D_perfect_completion.tex` |
| D.41 | … through all `S_n`-quotients, `n ≥ 5` | S | `D_symmetric_completion.tex` |
| D.42 | … through the relative pronilpotent completion over `PGL_2(F_7)` | S | `D_relative_pronilpotent.tex` |
| D.43 | … over every base with simple non-abelian even part | S | `D_simple_even_family.tex` |
| D.44 | … over every base with anabelian even part | S | `D_anabelian_even.tex` |
| D.45 | The recorded D.39 action (hence its extensions D.40–D.44, and the D.33 action) has no full profinite lift: obstruction in degree 9 of the sphere source over `S_4`; the elliptic projection lifts one layer | P | `D_rank2_obstruction.tex`, `D_rank2_transport.tex`. The exhaustion of conjugators (whole lower `s`-centralizer of rank 38, coprime lifting for `r`, 112 central columns, the functional Λ) is complete as an argument; the numbers are the program's (outputs read: rank 47 stays 47, no lift). It excludes one lower action, not the CM pair; the return says so. R: `d_cm_rank2_boundary_test.py` with `d_cm_rank2_magnus.cpp`, `d_cm_rank2_centralizers.py`, `d_cm_rank2_multiplier_transport.py`, `verify_torsion_bridge.py`. |
| D.46 | On `𝒰 = B̂/R_nil` (the relative pronilpotent completion over `Q`, `= ∏_Q P_p`) the automorphism "Galois commutator `h` on the 2-part, identity on the odd parts" is peripheral with multiplier one and has the extra CM pair `T_4 = I`, `W_3 = [i]`; the kernel `R_nil` maps onto `A_7` | P | `D_arithmetic_replacement.tex`. All arithmetic re-derived by hand (section 2). The peripheral conjugators exist by coprime complement conjugacy. `T_4` is read from the `r`-conjugator through `G_3` and `W_3` from the `s`-conjugator through `G_2` (D.25.6); that is how mixing the primes moves the pair to the other coset. Rests on D.34–D.36 (statement level), D.18, D.25. "Unramified at 3 for the based pro-2 action": from memory (Ihara; Hain–Matsumoto), right. R: `d_cm_arithmetic_replacement.py`. |
| D.47 | The same over every Fermat level: source `𝒱 = B̂/R_∞`, base `ℋ_∞ = B̂/(N̂ ∩ F̂′)`; it descends to `F̂/F̂″`; its outer class there is not Galois | P | `D_fermat_relative_tower.tex`. Both inclusions of the inverse limit, the fibre product, the conjugators over the infinite base, the rigidity argument (injectivity of `X − 1` on `Ẑ[[Ẑ²]]`) were followed. "Not Galois" rests on D.36. R: `d_cm_fermat_relative_tower.py`. |
| D.48 | The same over the central double cover `ℰ = B̂/[N̂, B̂]` (order 1152) and the mixed quotient `J_3` | S | `D_central_mixed.tex`. Statement and first part of the proof read. |
| D.49 | The same over the maximal base `ℋ_h` fixed by `h` (`C_h` = normal closure of `f_h`), source `𝒲_h`; identity on all of `SL_2(Ẑ)/±1`; the kernel `𝔯_h` has non-zero image `W = [V_{3,2}, A]` in `J_{3,2} = B̂/(K_3′K_3²)` | S | `D_fixed_parameter.tex`. Statement and first part of the proof read. `dim W` is given by a formula in `|A|`, which the return leaves unevaluated. |

### Part E (all 52 new rows concern E.23)

| Row | Statement head | Verdict | Where, and remarks |
|---|---|---|---|
| E.37 | The whole section map of `N/γ_3N` over every abelian class `α`: a lift exists iff the corrections `c_𝔮 = −d_𝔮⁻¹D_𝔮` (rank 44) are integral at every `𝔮 ∤ 3` and tend to zero; each fibre is a torsor under `ℛ(Z_3) ⊕ Z_3^24 ⊕ (Z/3)^9 ⊕ (Z/9)^5` | P | `E_intrinsic_class2.tex`. Followed: the lattice and Frobenius matrices, the peripheral term (E37.17), the local relation (E37.18), `H²_cts(K, M) ≅ ℛ/dℛ` with the image and no closure, descent from `Q(ζ_3)` to `Q`, the fibre. The step "the restricted sequence `D` is the cochain-level representative" is two sentences here; E.44 gives the full argument (uniform continuity), and it applies. R: `e_intrinsic_class2.py`; and the comparison with LM7_PUSH A.3, A.8 (not done here). |
| E.38 | `α_P + 27κ_3(19)e_Q` has a non-empty class-two fibre and no section in `N/γ_4N`, `N/N″`, `N/γ_3I_marked` | P | `E_next_obstruction.tex`. The quotient `H = 3Z_3 ⋉ (3,U)Z_3[[U]]`, the local equation `T³v(T^19) = v(T)`, its only solution `81·T^{−1/6}`, non-integral at `U⁴`: followed and recomputed. R: `e_next_depth.py`, `e_intrinsic_19.py`. |
| E.39 | `ker(G_K(3) → G_{K,{3}}(3))` is the free pro-3 product of the inertia groups; the Frobenius correction words | P | `E_riemann_coordinates.tex`. The free product is cited to Wingberg, Theorem 2.4 (from the return; it is the Riemann existence theorem as I remember it from Neukirch–Schmidt–Wingberg). The splitting, the section equations and the Chebotarev argument that no splitting normalizes all Frobenii were followed. |
| E.40 | Fibres of `N/γ_{r+1} → N/γ_r`, `r ≥ 3`: torsors under `coker((A_r − 1)(1 + C_r))`; at `r = 3`: `Z_3^166 ⊕ (Z/3)^7 ⊕ (Z/9)^56 ⊕ (Z/27)^25 ⊕ (Z/81)^3` | P | `E_higher_fibers.tex`. Followed: weights exclude ramification and stabilizers, the evaluation at `τ`, the torsion bound `3^{r+b_r}`. Counts recomputed: `73+7+56+25+3 = 164`, minus-space 166. R: `e_lie3_fibers.py`. |
| E.41 | All sections unramified outside 3 of `N`, `N/N″`, `N/γ_3I_Q`: `∏_i 𝒞_i(W)` | P | `E_unramified_sections.tex`. Followed: a normalized cocycle is one element `x = a(τ)`; the metabelian graded pieces by the Koszul complex (ranks `(r−1)C(r+8, r)`, 1485 at `r = 4`, recomputed), the marked ones by Lazard elimination; the normal forms and the inverse limit. R: `e_unramified_sections.py`. |
| E.42 | Local sections of `H` at `𝔮 ∤ 3`: with zero first inertia and second inertia `c ≠ 0` a section exists iff `b/(q − 1) ∈ Z_3`; the case `a ≠ 0` by orbit sums | P | `E_tame_module.tex`. Followed, including (E42.9) and the divisibility argument. R: `e_tame_module.py`. |
| E.43 | `exp coker d_𝔮 = 3^{v_3(q−1)+1}`; for `p ≡ 1 (9)` with 2 a non-cube (density 1/9) the classes `α_P + 3^kκ_3(p)e_Q` have class-two sections and none in `N/N″`, `N`, the marked quotients | P | `E_infinite_obstructions.tex`. Followed; density and prime list recomputed. R: `e_infinite_obstructions.py`. |
| E.44 | For `W ∈ {N, N/N″, N/γ_3I_Q}` and every `r ≥ 3`: a section of `W_{r−1}` lifts to `W_r` iff `z_𝔮 = −(Φ_𝔮 − q)⁻¹ε_𝔮` is integral for all `𝔮 ∤ 3` and tends to zero; fibres `𝒞_r(W)` | P | `E_higher_images.tex`. Followed, including the cochain-level representative and the independence of choices. The error `ε_𝔮` contains the genuine class-`r` Frobenius action, which the return does not evaluate for ramified inputs. R: `e_higher_images.py`. |
| E.45 | All local section classes of `H` in normalized coordinates | S | `E_tame_classes.tex` |
| E.46 | Global sections of `H` with first cocycle `A`: norm-coherent systems of completed units in the étale algebras `E_{A,n}` | S | `E_norm_sections.tex` |
| E.47 | First class zero: coordinates by norm-coherent cyclotomic units | S | `E_global_zero.tex` |
| E.48 | `N(Φ_m(X_{n+1})) = Φ_m(X_n)`; a compact product of independent section classes | S | `E_cyclotomic_norms.tex` |
| E.49 | The whole fibre over first class `3κ_3(3)` | S | `E_first_three.tex` |
| E.50 | `[3]: E ∖ E[3] → E ∖ O` identifies `N` with `ker(F → F^ab/3)`; the ambient-metabelian class-three kernel | S | `E_elliptic_comparison.tex` |
| E.51 | The fibres over `3rκ_3(3)`, every `r ≠ 0` | S | `E_unramified_first.tex` |
| E.52 | The fibres over `3rκ_3(2)` | S | `E_first_two_line.tex` |
| E.53 | Common quotient of the elliptic and the `h`-induced class-three quotients; kernel `Z_3^329` | S | `E_combined_quotient.tex` |
| E.54 | `h = (x+y)/(x+ζy)`: the genuine class-three action and the local fibres at 2 | S | `E_class3_frobenius.tex` |
| E.55 | `ℓ ≡ 2, 5 (9)`: free-product presentation and the mixed first-coordinate fibres | S | `E_two_prime_first.tex` |
| E.56 | The same for split `ℓ` with `v_3(ℓ−1) = 1`, 3 a non-cube | S | `E_split_prime_first.tex` |
| E.57 | First cocycle `3κ_3(17)`: the first complex norm map, `Cl(L) = (Z/3)²` | S | `E_prime17_norm.tex` |
| E.58 | Quotients of rank 5 and 13 from the degree-9 elliptic cover; Frobenius at 2 | S | `E_elliptic_frobenius.tex` |
| E.59 | Frattini field `Q(ζ_9, ∛3)`; Frobenius words of inert `ℓ ≡ 8 (9)` | S | `E_frattini_frobenius.tex` |
| E.60 | Local sections of the rank-13 quotient `R` over `Q_2(ζ_3)` | S | `E_elliptic_local.tex` |
| E.61 | At every `v ∤ 3` of `Q(ζ_3)`: the ramified local sections of the full pro-3 group are exactly nine cusp families `(Z_3 ∖ 0) × Z_3/(q−1)`; the abelian inertia of a metabelian local section lies on a cusp line | P | `E_full_local_cusps.tex`. Followed: specialization (SGA 1 XIII, from memory), Herfort–Ribes B′ for free factors, separation by a characteristic open subgroup, the cover `U′` over `k_v`, eigenvalue `q` on `T_3Jac(C′)` against the Weil bound. Both parts hold. The citation "Stix, Theorem 30" is from the return. R: nothing heavy; `e_full_local_cusps.py` checks 27 lines. |
| E.62 | First cocycle `3κ_3(17)`: a class that lifts through the first norm and not the second | S | `E_second_norm_obstruction.tex` |
| E.64 | Adjacent complex norms in `L_d = K(β_d)`, `β_d^{3^d} = 17ζ` | S | `E_complex_norm_criterion.tex` |
| E.65 | Adjacent norms in `F_d = Q(17^{1/3^d})` | S | `E_pure_norm_criterion.tex` |
| E.66 | Every ramified local metabelian section is cuspidal and has exactly one full lift | P | `E_full_local_metabelian.tex`. Followed: inertia with zero abelian image vanishes (the boundary lattices have zero limit); for non-zero image the boundary limit is `Z_3[[Y]]` and a Frobenius-invariant measure is a multiple of one Dirac measure; the `A`-conjugation; the centralizer by the Magnus embedding. |
| E.67 | Marked quotient: local classes with inertia at the marked cusp; central Frobenius parameter | S | `E_marked_local_cusp.tex` |
| E.68 | Unramified local normal forms for the full, metabelian and marked groups | S | `E_unramified_local_fibers.tex` |
| E.69 | Coherent 3-unit norm groups in the 17-tower (Kato's norm theorem); ranks `3^d` | S | `E_coherent_units.tex`. The integer `h` and the indices are left unevaluated by the return. |
| E.70 | The marked central parameter is `∏_{n≥1} Z_3` | S | `E_marked_central_parameter.tex` |
| E.71 | All ramified local sections of the marked quotient and the fibres of full → marked | S | `E_complete_marked_local.tex` |
| E.72 | The complex divisor norm limit: prime chains and class equations | S | `E_norm_divisors.tex` |
| E.73 | `G_K(3)` presented on `τ, τ′` and one inertia generator per prime with the tame relations `Y_𝔮T_𝔮Y_𝔮⁻¹ = T_𝔮^q`; a global section is a family of local packets satisfying (E73.7) | P | `E_global_packet_gluing.tex`. Followed: `H²(𝒢, F_3) = ⊕_𝔮 F_3` by Shapiro, the relation module, sufficiency of the local equations, the descent to `Q`. The finite example (the value at the prime over 19 is forced) was not recomputed. |
| E.74 | Wild local (at 3) central cohomology for the three groups | S | `E_wild_local_layers.tex` |
| E.75 | The relation module of the wild kernel over `Z_3[[P]]` | S | `E_wild_relation_module.tex` |
| E.76 | `B_d = L_d(ζ_9)`: unramified cubic over `L_d`; `Cl(B_1) = (Z/3)²` | S | `E_cyclotomic_basechange.tex` |
| E.77 | A `c`-equivariant presentation of `G_{Q_3(ζ_3)}(3)` over its free quotient | S | `E_wild_nonlinear.tex` |
| E.78 | The wild class-three `h`-quotient over `Q_3(ζ_3)`; a class-two section with no class-three lift | S | `E_wild_class3.tex` |
| E.79 | Hilbert characters of S-units in `B_{d+r}/B_d`; norm index `n^5` | S | `E_sclass_norms.tex` |
| E.80 | The joint `h`/`h̄` quotient and its wild descent | S | `E_joint_wild.tex` |
| E.81 | The prime-73 class of `B_1` in `B_2` | S | `E_prime73_capitulation.tex` |
| E.82 | The nine cusp-family obstruction maps at the wild prime | S | `E_cusp_family_obstruction.tex` |
| E.83 | The intrinsic-to-joint wild `H²` map | S | `E_joint_intrinsic_image.tex` |
| E.84 | `Cl(B_1) → Cl(B_2){3}`: kernel and image of order 3 | S | `E_ramified_capitulation.tex` |
| E.85 | The compatible joint family image; central comparison of index 9 | S | `E_compatible_joint_fibre.tex` |
| E.86 | `Cl_S(B_d){3} = C_3`, `Cl_S(L_d){3} = C_3²` at every level | S | `E_stable_sclass_towers.tex` |
| E.87 | Local first-degree intrinsic-to-joint map; a free wild obstruction `−7t(U_1 + 21t/2)` | S | `E_abelian_kernel_obstruction.tex` |
| E.88 | The complex multiplicative norm system: divisor image = kernel of two congruences mod 3 | S | `E_global_sdivisors.tex` |
| E.89 | The horizontal class-two obstruction over the `B_0` relative value: image `C_3² ⊕ C_9` | S | `E_full_horizontal_obstruction.tex` |

**Counts.** New rows 75. Proof read, no gap found: 17. Statement level only: 58 (two of them with the first part of
the proof read). Gap: 0. Error: 0. Changed rows read: D.20 (Known, consistent with the source's abstract), D.25,
E.23, D.13, D.19.

## 4. Implications

Lines marked **(mine)** are derived in this intake and checked by no one else.

### 4.1 E.23

- **Settled: the class-two layer.** E.37 gives the image and every fibre of `Sec(N/γ_3N) → H¹(Q, V)`. This is the
  first part of E.23 as the review stated it. The criterion has two conditions: integrality at each prime and
  convergence to zero (the lim¹ check is inside it).
- **Class two does not select; the next layers do.** E.38 and E.43: infinitely many abelian classes
  (`α_P + 3^kκ_3(p)e_Q`, `p` in a set of density 1/9) have class-two sections and none in `N/γ_4N`, `N/N″` or
  the marked quotients. The mechanism is in a metabelian quotient of the tripod group (`H ⊂ F/[I_y, I_y]`):
  with inertia in the `y`-direction a local section exists iff the Frobenius `x`-coordinate `b` has
  `b/(q − 1) ∈ Z_3` (E.42).
- **The local side is done at good places.** E.61 (read): a ramified local section of `N` at `v ∤ 3` is cuspidal;
  E.66 (read) gives the same for `N/N″`, with exactly one full lift; E.67, E.71, E.68 (statement level) the marked
  quotient and the unramified normal forms. E.41 (read) gives every section unramified outside 3 of the three
  groups: `∏_i 𝒞_i(W)`, of free ranks 6, 24, 166, … against rank one for each cuspidal packet, so the pro-3
  section conjecture fails for this curve.
- **The global side is reduced, not solved.** E.44 (read) is the lifting criterion at every layer `r ≥ 3`; E.73
  (read) says a global section is a family of local packets coupled by the Frobenius words `Y_𝔮`. What
  is missing in both is the same thing: the genuine class-`r` Frobenius words for ramified inputs.
- **Still open.** (a) The whole image of `Sec(N/γ_4N) → Sec(N/γ_3N)`. (b) The global section sets of `N/N″` and
  the marked quotients. (c) The other prime components and the mixed finite quotients, which the prompt's
  "metabelian quotient" includes and the return leaves untouched.
- E.46–E.60, E.62–E.72, E.76, E.79, E.81, E.84, E.86, E.88 compute the sections of the one inherited quotient `H`
  through norm-coherent units in the towers `Q(a^{1/3^n})`, and E.74–E.89 the wild local side at 3, for
  particular inputs. They are steps on route (b); none closes it.

### 4.2 D.19

- **Part (i)** (the two questions of D.13): untouched.
- **Part (ii), the CM coset.**
  - D.27 (read): the twelve recorded extra-CM shadows of D.25 are not genuine. This removes twelve points and no
    CM matrix pair (it agrees with the reviewer's note on LM7_PUSH E.9, E.10).
  - D.28–D.44 follow one replacement action through larger and larger quotients; D.30, D.32, D.45 exclude three
    recorded representatives. D.45 (read) kills the D.39 action with all its extensions D.40–D.44.
  - **D.46–D.49 change the shape of the question.** The candidate is now: a Galois commutator `h` on the
    2-primary part, the identity on the odd parts. It exists on every quotient of `B̂` that is a fibre product of
    pro-`p` pieces over a base on which `h` acts trivially: the relative pronilpotent completion over `Q`
    (D.46), over all Fermat levels and on `F̂/F̂″` (D.47), over the maximal `h`-fixed base (D.49). Its CM pair is
    `(I, [i])`, in the coset Galois misses.
  - **So no quotient of that kind can decide D.19 (ii).** The pair is produced by mixing primes, and Galois
    couples `T_4` and `W_3` through the single field `Q(i, (3/4)^{1/4})`, a mixed-prime constraint. A deciding
    quotient must have a 2-layer above an odd layer on which `h` acts non-trivially (or the reverse). The return
    names the first such places: `J_{3,2} = B̂/(K_3′K_3²)`, where the kernel `𝔯_h` has image `[V_{3,2}, A] ≠ 0`
    (D.49.9–11), and the `S_7`-marking (D.46.9), where the kernel maps onto `A_7`.
  - D.45's bases `S_4`, `A_4 × C_2` obstruct one action only: D.46 passes the whole relative pro-2 completions
    over them.

### 4.3 D.13

- No new row attacks it. D.20's new part gives, for all of `GT̂`, the cyclic-cover and distribution identities
  (Enriquez); it adds no dimension count.
- **(mine) The metabelian profinite group cannot decide D.13.** `A = F̂′/F̂″ = ∏_p A_p`, and
  `A_ℓ = Z_ℓ[[Ẑ²]]` splits by the idempotent `e_0` of the trivial character of the prime-to-ℓ part of `Ẑ²`
  into `e_0A_ℓ = (F^(ℓ))′/(F^(ℓ))″` and a complement. Hence `F̂/F̂″ = G_1 ×_{Ẑ²} G_2` with
  `G_1 = (F^(ℓ)/(F^(ℓ))″) ×_{Z_ℓ²} Ẑ²`, and every automorphism of the pro-ℓ metabelian group that is the
  identity on the abelianization extends to `F̂/F̂″` by the identity on `G_2`. It keeps the three conjugacy
  classes: composing with an inner automorphism puts the abelian images of the conjugators of `x`, `y`, `xy` on
  the lines of `x`, `y`, `xy` (for `xy` this follows in the class-two quotient), so the conjugators can be taken
  in `e_0A_ℓ`, which acts trivially on `G_2`. With D.12 the images of the loop-preserving outer automorphisms of
  `F̂/F̂″` in weights 5 and 9 are the pro-ℓ values 3 and 2. This is the reviewer's hunch H4 with a proof sketch;
  D.47 is the same splitting used for coefficient primes. D.13 is therefore a question about lifting from
  `F̂/F̂″` to `F̂`, and nothing else.

### 4.4 LM7_PUSH: D.1, D.2, E.2, E.3 (open at its checkpoint 04)

- **D.1, D.2.** Nothing new from LM7. 4.3 (mine) says where the question lives. First test object: the lift of
  one explicit weight-5 element of `Out^♯(F̂/F̂″)` to the next layer.
- **E.2.** Its sentence "the asserted equivalence ... still requires a proof" can be replaced: the equivalence
  with the twelve representatives is false in every quotient examined (D.27 against D.46–D.49). LM7's D.49 and
  LM7_PUSH's "relative three-primary kernel with a non-zero third lower-central term" should be compared; they
  may be the same residual. Stays open.
- **E.3.** D.20 gives a necessary condition for `GT̂`: `c_{mn}(f) = c_m(f) + c_n(f)`. **(mine)** The D.47 element
  passes it on `F̂/F̂″`: `c_n` is a continuous homomorphism `F̂′/F̂″ → Ẑ`, so it maps the 2-part to `Z_2`, and
  the relation holds for `h`. So the additive distribution relation does not separate `GT̂` from the candidate.
  The non-abelian identity `φ_n(f) = y^{c_n(f)}f` of (D20.1) is the stronger test and is not evaluated. Stays open.

### 4.5 LM8_PUSH (unsent)

- **R14 and task C.7** name LM7 D.46. Add D.47–D.49: the candidate lives on `F̂/F̂″` with every deck level
  (D.47), is the identity on the whole congruence quotient `SL_2(Ẑ)/±1` (D.49.7), and its residual kernel is
  detected in `J_{3,2}` and at `S_7`.
- **Part B (torsion and the metabelian peripheral group, task B.1).** `Out^♯(F̂/F̂″)` now has three known
  sources of non-Galois elements: LM8 A.22 (deck idempotents), D.47 (coefficient primes), and 4.3 (mine: every
  pro-ℓ special automorphism). B.1's description "as units" has to account for all three.
- **Part D (sections of the tripod at 5 beyond class two).** E.38, E.42, E.45 are statements about the tripod
  group itself (`R = F/[I_y, I_y] = Z_ℓ[[U]] ⋊ Z_ℓ`): the equation `T^bv(T^q) = v(T)`, solution `cT^{−b/(q−1)}`.
  They transfer to `ℓ = 5` verbatim. E.44 is the layer-by-layer criterion LM8_PUSH D asks for, and E.61 the local
  classification. Attach `E_higher_images.tex`, `E_tame_module.tex`, `E_next_obstruction.tex`,
  `E_full_local_cusps.tex`, `E_global_packet_gluing.tex`.
- **Lead 16 / task D.7 (H1, descent along the cyclotomic tower):** no LM7 row uses it; unchanged.

### 4.6 PS-1 to PS-5

- **PS-1** (descent along `Q(μ_{3^∞})`): not touched by any new row. E.37 and E.44 state `H²_cts = ℛ/dℛ` over
  the primes; PS-1 would restate it over `Γ`.
- **PS-2** (lim¹ = 0 iff the action on `M(−1)` is finite): consistent evidence only. E.43: the local cokernel
  exponent is `3^{v_3(q−1)+1}`, unbounded; on the line `L ≅ Z_3(1)` the differential is zero.
- **PS-3 is false as worded (mine).** A cuspidal section at a rational cusp `d`, twisted by a class
  `u ∈ H¹(Q, Z_3(1))` with infinitely many non-zero valuations, is a section of `N` ramified at infinitely many
  primes. In E.37's formula its `D_𝔮` is zero: `(k_d + u(F)e_d) ∧ b e_d − b k_d ∧ e_d = 0`. The statement
  needs "non-cuspidal". With E.61 it becomes a question about cusp colourings (push item 2).
- **PS-4.** (a) not touched; D.46 shows how `T_4`, `W_3` are read (from the conjugators, through `G_3` and
  `G_2`), which a proof of (a) must use. (b) open; D.46–D.49 give the candidate and the quotients where it
  lives. (c) is not supported: the obstruction of D.45 is a class in a cokernel on the degree-9 Zassenhaus layer
  for one lower action, and D.46 lifts another action through the whole relative pro-2 completions over those
  bases; no class of the extension obstructs.
- **PS-5 needs rewording (mine).** An element with `λ ≡ 1` mod 3 fixes the class of `r`, so it acts trivially on
  `Q_0 = S_3 × C_3`, so by (D.34.4) it commutes with the deck element `δ` of `w³ = z(z−1)` and acts
  `Z_2[ζ_3]`-linearly on `T_2`. Complex conjugation inverts `δ` and acts antilinearly. So no element that is
  trivial on the 3-adic part acts as complex conjugation on the relative pro-2 completion over `Q_0`. On the
  pure pro-2 completion of `F` there is no such constraint. The norm `−1` is a norm from `Z_2[ζ_3]^×`
  (unramified), so a linear element of multiplier `−1` at 2 is not excluded there.

## 5. For a second reader, in order

1. LM7 E.37 against LM7_PUSH A.3, A.8 (two evaluations of one map; free rank 24 against 23 + 1; torsion).
2. Rerun `d_cm_class2.py`, `d_cm_class2_two.py` (D.27) and the D.45 programs: these two rows carry every
   "not genuine" statement.
3. D.35 with its proof, and D.25 behind D.36: D.46–D.49 rest on them.
4. The three **(mine)** arguments of 4.3, 4.6 (PS-3) and 4.6 (PS-5).
5. D.48, D.49 to the end; E.67, E.71 (the marked quotient).
