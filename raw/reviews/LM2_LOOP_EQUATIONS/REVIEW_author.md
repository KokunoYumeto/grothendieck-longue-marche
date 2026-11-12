# LM2_LOOP_EQUATIONS: review by the author of the prompt

Claude (Fable 5.2, Anthropic), 12 November 2026. Review of the answer of GPT-6 Astra (OpenAI, ChatGPT Pro mode) to prompt `LM2_LOOP_EQUATIONS`: 79 statements (51 Proved, 12 Known, 10 Refuted, 6 Open), 27 programs with outputs. Return: `answers\LM2_LOOP_EQUATIONS\LM2_LOOP_EQUATIONS\`.

**Verdict in one paragraph.** No statement labelled Proved, Known or Refuted was found false among those I checked. The return is right against my LM3 review on B.g4: the two linear cycle equations do not cut out the special `𝔖_3`-invariant derivations, and the sentence I put into the LM2 prompt ("the solution space of (1.2)–(1.3) alone would exceed `d_n` first in weight 7") is false; the first excess is in weight 4. What stands of my LM3 computation is the other space: the special invariants have dimensions 0, 0, 1, 0, 1, 0, 2, 1 and exceed `grt_1` first in weight 7, and the return proves that this space, not the raw one, is the graded envelope of `GT_0` (B.g1, B.g2). The main results: §46 is exactly the `GT̂_0` system (B.m2); every element of `GT̂_0` acts on `SL_2(Z/n)` by conjugation with a matrix of determinant `μ`, so the congruence images of Galois, `GT̂` and `GT̂_0` coincide (C.d1, C.a16, C.r1); an explicit weight-7 element satisfies the loop and symmetry equations and fails the pentagon (B.g5), with a finite group of order `13^747` carrying it (B.g15); the one family of conditions in §§38–47 not derived from `GT̂` is the compatibility with the map `F̂ → (C_2 * C_3)^` of §47 (E.1–E.5). Below I add: a proof that the weight-7 element lifts to the pro-ℓ group for every `ℓ ≥ 5` (this closes the pro-ℓ half of B.g11 and F.3; mine, unchecked by anyone else), and reductions of E.3, B.f7, D.6 and C.d5.

## What I read and checked

Read: `results.csv` (79 rows), the report (§§1–3 in full), `new_conditions.csv`, `sections/B_graded.tex` (B.g1, B.g2, B.g4, B.g5, B.g11 with proofs), `sections/E_conditions.tex` (E.1–E.4 with proofs), the statements and proofs of B.f5, B.f7, B.f8, C.d5, D.6, D.7. The other sections were read in the register only. No program of the return was run; I read none of them line by line either, since the statements they support are either recomputed below or marked as not followed.

Own checks: `checks_author/check_lm2.py` with `check_lm2.out` (exact rational arithmetic; 2 minutes) and `checks_author/check_psl27.py` with its output.
1. B.g3: dimensions in weights 1–9. Raw two- and three-cycle system: 1, 0, 1, 1, 2, 3, 6, 10, 19. Antisymmetry with `J(ψ) = 0`: 1, 0, 1, 0, 1, 0, 2, 1, 4 (the 1 in weight 1 is the non-normalized solution), and adding the three-cycle equation changes nothing, as B.g2 says. Both rows agree with the return.
2. B.g4: `q_4 = b_xxxy − 4 b_xxyy + b_xyyy` satisfies both linear equations, spans the raw space in weight 4, and `J(q_4)` has Lyndon coordinates (2, −3, 1, −3, −2, 2), as printed in the return.
3. B.g5: `q_7` satisfies antisymmetry, the three-cycle equation and `J = 0`. The eighteen relations of `t_4` hold in the representation on `Lie⟨a, b, c⟩`. The pentagon defect of `q_7` acting on `a` is non-zero (880 words), and the coefficient of `a⁵bcb` is 16. The special solutions of weights 3 and 5 have zero defect on `a`, `b`, `c`. On the 2-dimensional special space of weight 7 the defects have rank 1: so at most one dimension satisfies the pentagon, with no use of the 2026 upper bound.
4. C.r1: `|(Z/n)^×/squares|` = 1, 2, 2, 2, 2, 2, 4, 4, 8 for `n` = 2, 3, 4, 5, 6, 7, 8, 12, 24. C.r2: at level 5 conjugation by `diag(2, 3)` sends the unipotent generator to its 4th power. C.a3: 5 is 1 mod 4 and not a square mod 8. D.5: `det(c + dR) = c² + (tr R) cd + d²`.
5. B.f5: `PSL_2(F_7)` has 57 classes of generating pairs modulo automorphisms; 25 ordered types (orders of `x`, `y`, `xy`) carry one class and 16 carry two.

## Verdicts

Words as in the LM3 review: **proved** (followed, complete given named inputs), **proved in outline**, **confirmed by my computation**, **known, not opened**, **not followed** (statement read; proof not read), **open, honest**, **open, reduced** (I give a reduction or a partial result).

### Part A
| Id | Label | Verdict |
|---|---|---|
| A.1 | Refuted | Not followed in proof; the statement is right in substance: the stack of elliptic curves with full level 2 is the neutral `μ_2`-gerbe over `U`, not `U`, and `F_2` is not `C_2 * C_3`. Corrects the prompt's "`M_{1,1}[2] ≅ U_{0,3}`". |
| A.2 | Proved | Not followed. |
| A.3 | Known | Proved in outline, and it agrees with LM3 E.7: the pure outer quotient of §46 is the centralizer of `𝔖_3`, which is `GT̂_0` (Harbater–Schneps, Main Theorem (a), which I opened for LM3); the genuine group is an extension of it by `F̂_2`; the group of all label-preserving loop automorphisms is larger. This settles Part A (c) of the prompt: `M̃^!_{0,3}` is an extension of `GT̂_0`. |
| A.4, A.5 | Proved, Known | Not followed. |

### Part B, manuscript
| Id | Label | Verdict |
|---|---|---|
| B.m1 | Proved | Not followed; the point that the equations alone give an endomorphism and generation must be kept is right (a level-3 counterexample is claimed). |
| B.m2 | Proved | Proved in outline: the change of variables `f = y^{-b} ξ x^{-a}`, `a + b = ν`, in both directions. **§46 is the system (I), (II).** Lead 1 of the prompt is confirmed in its sharpened form. |
| B.m3 | Proved | Not followed. It isolates the one extra equation (compatibility with `φ`). |
| B.m4, B.m6 | Proved | Not followed. |
| B.m5 | Refuted | Proved in outline: the target of the conjugator at scan 229 must be `B̂`, not `F̂`. A correction to the manuscript's statement, not a reading. |
| B.m7 | Known | Known, not opened (Lochak–Schneps). |

### Part B, graded
| Id | Label | Verdict |
|---|---|---|
| B.g1 | Proved | Proved. The leading-term map into special `𝔖_3`-invariant outer derivations is injective; surjectivity is not claimed. For `ℓ ≥ 5` it is surjective: see "What I proved" below. |
| B.g2 | Proved | Proved, and confirmed by my computation in weights 2–9. |
| B.g3 | Proved | Confirmed by my computation through weight 9 (the return goes to 12). |
| B.g4 | Refuted | **Confirmed by my computation. The return is right and my LM3 review was wrong on this point.** In the LM3 review I called the special invariants "the graded shadow of `GT_0`, relations (I) and (II) without the pentagon; identification not checked", and in the LM2 prompt I drew from it that (1.2)–(1.3) alone exceed `d_n` first in weight 7. The linear equations (1.2), (1.3) are weaker than the group equations: they omit `J(ψ) = 0`, which expresses that `z` goes to a conjugate of itself. Their solution space exceeds in weight 4. I did not re-derive the rank-4-against-5 obstruction in weight 5; `J(q_4) ≠ 0` with B.g1 already gives the conclusion. |
| B.g5 | Proved | Confirmed by my computation, coefficient 16 included. So `dim W_7 = 1` and the graded envelope of `GT_0` is strictly larger than `grt_1` in weight 7. |
| B.g6, B.g7 | Known | Known, not opened. |
| B.g8 | Proved | Not followed in proof. Consistent with my computation: every special solution of weight 3 and 5 satisfies the pentagon, and the pentagon solutions of weight 7 lie in the special space. |
| B.g9 | Proved | Conditional on the unrefereed manuscript 008; the implication was not followed. |
| B.g10 | Proved | Not followed. |
| B.g11 | Open | **Open, reduced: settled for the pro-ℓ group, `ℓ ≥ 5`, below.** The return's remark on "successive approximation" is fair: unrestricted choices at one weight can block the next (its greedy attempt fails in weight 10). My lifting lemma of the LM3 review is for all special automorphisms, where every choice extends; inside the centralizer of `𝔖_3` existence needs another argument. |
| B.g12, B.g13 | Proved | Not followed. B.g13 answers ask 4 of "Recent results": no relation found. |
| B.g14 | Proved | Proved in outline (the additive formal group). Superseded for `ℓ ≥ 5` and over `Q` by the lift below. |
| B.g15 | Proved | Proved in outline; the two ingredients I recomputed (`q_7` solves the graded system; pentagon coefficient 16, which is 3 mod 13) are confirmed. The class-12 solution `q_7 + F_9 + F_11` and its reduction mod 13 were not recomputed. A finite solution of (I), (II) on a group of order `13^747` whose outer class is not arithmetic. |

### Part B, finite
| Id | Label | Verdict |
|---|---|---|
| B.f1 | Refuted | True (substitution is not defined on an arbitrary finite quotient). |
| B.f2–B.f4, B.s4.1, B.s4.2 | Proved | Not followed (finite enumerations; the envelope orders 108 and 442368 not recomputed). |
| B.f5 | Known | The count of 57 classes for `PSL_2(F_7)` is confirmed by my program; the shadow of order 1024 was not recomputed. |
| B.f6 | Proved | Confirmed in the LM3 review (`SL_2(F_8)`). |
| B.f7 | Open | Open, reduced below. |
| B.f8 | Proved | Proved in outline: the endomorphism `x ↦ x`, `y ↦ y[x, y]` is an automorphism on every nilpotent, pro-ℓ and pro-unipotent completion (Stallings) and not profinitely. **This proves the first of the two leads that the follow-up L5 put into LM1, LM7, LM8.** It also notes what the lead missed: the map does not preserve the third loop, so it is not a loop automorphism. |

### Part C
| Id | Label | Verdict |
|---|---|---|
| C.r1 | Proved | Proved in outline; the orders are confirmed. The arithmetic outer image on `SL_2(Z/n)` is `(Z/n)^×` modulo squares. |
| C.r2 | Refuted | Confirmed (level 5): on outer congruence actions the multiplier is defined only modulo squares. |
| C.r3 | Proved | Not followed. |
| C.d1 | Known | Not followed. This is the substantive step behind C.r1 and C.a16 (every element of `GT̂_0` preserves every congruence kernel). **Unverified by me; it carries item 1 of the prompt** (the congruence relations are consequences of the profinite algebra). |
| C.d2–C.d4 | Proved | Not followed. |
| C.d5 | Open | Open, reduced below. |
| C.r4, C.r5 | Proved | Not followed. |
| C.a1, C.a2 | Proved | Not followed; the fields `Q(i)`, `Q(√−3)`, `Q(√3)` are the expected ones. |
| C.a3 | Refuted | Confirmed (5 modulo 8). Corrects scan 152. |
| C.a4, C.a6 | Known | Known, checked for LM3 (Hoshi–Mochizuki, Corollary 6.4; 6.3 (iv) not opened). |
| C.a5, C.a7, C.a8, C.a10, C.a14–C.a16 | Proved | Not followed. |
| C.a9 | Refuted | True: the family he doubts at scan 524 exists (the Legendre family); the manuscript withdraws the doubt itself. |
| C.a11 | Proved | Not followed. If it holds, the anabelian converse of scan 523 needs no section conjecture. |
| C.a12, C.a13 | Known | Known, not opened (Pop; Hoshi–Mochizuki–Tsujimura). |

### Part D
| Id | Label | Verdict |
|---|---|---|
| D.1 | Known | Proved in outline (the Belyi normalization gives a section). |
| D.2 | Refuted | Proved: conjugating by `x` changes the cocycle by `Int(x²)`. |
| D.3 | Refuted | Not recomputed (the mod-7 conjugacy). |
| D.4 | Proved | Not followed. |
| D.5 | Proved | Confirmed: with `tr R = 1` the form is `c² + cd + d²`. The plus sign at scan 209 is what the mathematics supports, given his `ρ` of order 6 in `SL_2`. |
| D.6 | Open | Open, reduced below. |
| D.7 | Refuted | Proved (I followed it): the section centralizing `r` and its conjugate by `k` have the same congruence matrices and differ modulo 9 in `F̂^ab`. |

### Parts E, F
| Id | Label | Verdict |
|---|---|---|
| E.1 | Proved | Proved: the two maps from the tripod to the orbifold `(P¹ ∖ {0}; 2, 3)` are defined over `Q`, so Galois satisfies the compatibility. |
| E.2 | Proved | Not recomputed. |
| E.3 | Open | Open, reduced below. |
| E.4 | Proved | Proved (finite-order elements die in unipotent groups). |
| E.5, E.6 | Proved | Proved in outline. |
| F.1, F.2 | Proved | True. |
| F.3 | Open | Open, reduced: the pro-ℓ half is settled below. |

## What I proved (mine; read by no one else)

**Proposition 1 (B.g11, F.3, pro-ℓ form).** Let `ℓ ≥ 5`, `F` the free pro-ℓ group on `x`, `y`, and `P` the group of outer automorphisms of `F` sending `x`, `y`, `z = (xy)^{-1}` to conjugates of themselves. Then the centralizer `P^{𝔖_3}` of the geometric `𝔖_3` contains an element whose leading term is `q_7`; it is not in the pro-ℓ `GT`. So the pro-ℓ group of solutions of (I), (II) with `λ = 1` is strictly larger than that of (I), (II), (III), for every `ℓ ≥ 5`, and the same holds for the pro-unipotent groups over `Q`.

Proof. Filter `P` by `P_n` = classes with a representative trivial modulo `Γ_{n+1} F`. (a) `P_n/P_{n+1}` is the module of special derivations of degree `n` over `Z_ℓ` modulo inner ones: injectivity is B.g1; surjectivity is the lifting lemma of the LM3 review (for a special derivation, lift the conjugators and correct the defect degree by degree; the linear map `⊕ gr_{m−1} → gr_m` is onto, so any choice at one stage extends). (b) `𝔖_3` normalizes `P` and preserves the filtration, and its order is prime to ℓ, so `H¹(𝔖_3, P_{n+1}) = 1` and `(P_n)^{𝔖_3} → (P_n/P_{n+1})^{𝔖_3}` is onto. (c) `q_7` has integer coefficients and its class is `𝔖_3`-invariant (B.g2; my check 3). So some `g ∈ P^{𝔖_3} ∩ P_7` has leading term `q_7`. (d) An element of the pro-ℓ `GT` in `P_7` has a leading term satisfying the linearized pentagon; `q_7` does not (check 3). Over `Q` the same argument works with invariants of a finite group on a pro-unipotent group.

Not proved: that `P^{𝔖_3}` is the pro-ℓ group of normalized solutions of (I), (II) (the pro-ℓ form of Harbater–Schneps, Theorem 2; I expect the proof to carry over and did not check it); step (d) in the pro-ℓ pure braid group. The primes 2 and 3 are excluded: there `H¹(𝔖_3, gr)` can obstruct. The profinite statement is not reached: it is now exactly whether the image of `GT̂_0` in `P^{𝔖_3}` contains an element with leading term outside `grt_1`. The return's finite group of order `13^747` is the shadow of such a `g` for `ℓ = 13`.

**Reduction of E.3 (does `GT̂` imply the §47 compatibility).** For `g = (λ, f) ∈ GT̂_0` let `A_g` be its action on `B̂ = (C_2 * C_3)^` (C.d1, C.a15) and `F_g = A_g|_{F̂}`. `F_g` preserves `ker φ` (the normal closure of `x²` and `z³`), so it descends along `φ: F̂ → B̂` to an automorphism `D_g` of `B̂`, which sends `s` to `s`, and `r`, `e = sr` to conjugates of `r^{±λ}`, `e^λ`. Automorphisms of `B̂` of this kind, modulo inner ones, are `GT̂_0` again (restriction to the characteristic subgroup `F̂`; C.r5). So `g ↦ D_g` is a continuous endomorphism `δ` of `GT̂_0` with `λ ∘ δ = λ`, and
`C^φ = {g : δ(g) = g}`, a closed subgroup containing the image of Galois. E.3 is the statement `δ|_{GT̂} = id`. Geometrically, `φ^{-1}(F̂)` is the group `K` of the `𝔖_3`-covering of the `j`-tripod by the `λ`-line minus the eight points `0, 1, ∞, −1, 2, 1/2, ζ_6, ζ_6^{-1}`, and `δ(g)` is: restrict `g` to `K`, then fill the five special points. So E.3 asks whether `GT̂` is compatible with removing the two special orbits of `𝔖_3` from `M_{0,4}`: a statement of the "special loci" kind, which the relations (I)–(III) are not known to give and which Nakamura–Schneps add by hand in genus 1. Not checked: that `D_g` is again in the image of `GT̂_0` with the same normalization (the restriction step). Next instance: compute `δ` on the finite shadows of the `𝔖_4`-envelope (order 442368), where a `g` with `δ(g) ≠ g` satisfying the pentagon at that level would be the first evidence against, and its absence the first beyond levels 2 and 3. Hunch: `δ ≠ id` on `GT̂_0` (the weight-7 element is the candidate, but `δ` does not pass to the pro-ℓ quotient, E.4), and `δ = id` on `GT̂` is as hard as the Nakamura–Schneps relations.

**Reduction of D.6.** A section over `C(3)` centralizing `r` is unique (D.7's first step). A section `s'` with matrix image in `T_R` is `c · s_R` with `c: C(3) → F̂` a cocycle whose matrices lie in `T_R(2)`, the norm-one units congruent to 1 modulo 2. Since `T_R` is commutative, `χ = U ∘ c: C(3) → T_R(2)` is a homomorphism, and it does not change under conjugation by an element of `F̂` that keeps the constraint. So `χ` is an invariant of the class, D.7's two sections have the same `χ = 1`, and D.6 splits into: (i) is there a section with `χ ≠ 1`; (ii) for `χ = 1`, the classes of cocycles into the congruence kernel. On the Galois part (i) is an instance of the section conjecture with complex multiplication: a section of the tripod over `Q(√−3)` whose image in `PGL_2(Ẑ)` lies in the torus of `Ẑ[ζ_6]` should be the section of the point `ζ_6` (for a rational point `λ_0` this is immediate: `E_{λ_0}` then has complex multiplication by `Z[ζ_6]`, so `j = 0`). Next instance: (i) modulo 3, that is, homomorphisms `C(3) → T_R(2) ⊗ Z_3`.

**Reduction of C.d5.** On the Galois part the two torus coordinates are, if my identification is right (not checked), the characters of the elliptic curves with `j = 0` and `j = 1728` on their Tate modules, restricted to the kernel of the congruence action. By the open-image theorem for a product of two non-isogenous CM curves the image of Galois in the pairs `(T, W)` of equal norm is open. So the lead: the image in C.d5 is of finite index in the determinant-one fibre, with index supported at 2 and 3, and the mod-3 instance is a computation with the Grössencharacter of `y² = x³ + 1`. Whether elements of `GT̂_0` outside Galois enlarge the image is the part that needs C.d1's conjugators.

**Reduction of B.f7.** By my enumeration the 57 classes for `PSL_2(F_7)` fall into 41 ordered types; Galois permutes classes within a type after the cyclotomic twist. 25 types have one class. Of the 16 with two classes, those of unordered type (3, 7, 7) and (4, 7, 7) may be separated by the classes 7A, 7B (not checked), and the ones that the branch-cycle argument cannot separate are (3, 3, 4), (4, 4, 4) and (3, 4, 7). So the arithmetic image in the kernel of order 512 is an elementary abelian 2-group acting on at most 16 pairs, and the next instance is: are the two regular dessins with group `PSL_2(F_7)` of type (3, 3, 4) (genus 8) conjugate over a quadratic field, or both defined over `Q`? The same for (4, 4, 4) (genus 22) and (3, 4, 7) (genus 24).

## Corrections to my own leads and to the prompts

1. LM3 review, "Graded evidence on E.8" and Lead 4 of LM3b: the special invariants are the graded envelope of `GT_0` (true, B.g1–B.g2); they are not the solution space of the two linear cycle equations (B.g4). The dimension 2 against 1 in weight 7 stands.
2. LM2 prompt, "After LM3", last bullet: false as an answer to ask 1 of "Recent results"; the right table is B.g3.
3. LM8 prompt, Part B (d), "is the solution space of the two symmetry equations at `(0,3)`": to be replaced by the special invariants (done in the fold-in).
4. The follow-up L5 lead (Stallings) is proved by B.f8; its use needs the caveat that the map is not a loop automorphism.
5. Prompt item "`M_{1,1}[2] ≅ U_{0,3}`": a neutral `μ_2`-gerbe over `U_{0,3}` (A.1).

## Readings

The return's `readings.csv` was not reviewed row by row. Three points bear on the edition: scan 229, the conjugator must be allowed in `B̂` (B.m5); scan 152, the 2-adic square criterion is false as written (C.a3); scan 209, the plus sign in `c² + cd + d²` is supported (D.5).

## Not verified

Everything marked "not followed"; C.d1 above all. The class-12 jet and the group of order `13^747`. The finite shadows (orders 108, 442368, 1024). My Proposition 1 and the four reductions: written here, checked by no one. The identification of the torus coordinates with CM characters in the reduction of C.d5.
