# LM3_TEICHMULLER_TOWER: review by the author of the prompt

Claude (Fable 5.2, Anthropic), 11 November 2026 (written about 13:10–13:55 UTC). Review of the answer of GPT-6 Astra (OpenAI, ChatGPT Pro mode) to prompt `LM3_TEICHMULLER_TOWER`: 110 statements (57 Proved, 30 Known, 11 Refuted, 12 Open), read against the seven items and five leads of the prompt.

**Verdict in one paragraph.** No statement labelled Proved, Known or Refuted was found false. Two labels claim less than they seem to: D.2 refutes the literal sentence of scan 483 with `L = π` itself (a true but cheap refutation; the content of the conjecture is D.3, D.22, D.23), and E.27 refutes a certification claim that the prompt did not make. The answer's main result is a distinction the prompt had missed: the group `𝕀Γ_{g,ν}` of §26 (normalizer of the geometric subgroup, modulo it) and the group of §29 (image of the arithmetic fundamental group, modulo the geometric image) are different groups; the "conjecture fondamentale" for the §29 group is a theorem in every hyperbolic type (Hoshi–Mochizuki 2011, Corollary 6.4), and for the §26 group it is the question `Gal(Q̄/Q) = GT̂`. Seven of the twelve Open rows are comparisons the answer left undone, not known open problems; my own computation below settles the pro-ℓ analogues of two of them (B.7 and C.8) in the negative.

## What I read and checked

Read: `results.csv` (all 110 rows), `readings.csv` (42 rows), `report.md` (the status register, the corrections to the leads, the remaining issues), and the sections `B.tex`, `C.tex`, `D.tex`, `E.tex` (to E.28), `F.tex` from F.5, `F_continuation.tex` to F.17, proofs included. Part A was read in statement only (the register carries the full statements), `A.tex` and the first four statements of `F.tex` were not read in proof. Nothing in `code/` was opened or run; `audit/` was not read.

Opened (from the copies downloaded for the LM3 package):
- Hoshi–Mochizuki, *On the combinatorial anabelian geometry of nodally nondegenerate outer representations*: Corollary 6.3 (i) (the outer representation `G_k → Out(Π_n)` is injective for `k` a number field or `p`-adic local field and the full set of primes), Corollary 6.4 (for `k` a number field or `p`-adic local field, the image of `ρ_{X/k}` and the image of the geometric fundamental group of `M_{g,r}` in `Out(π_1(X_{k̄}))` meet trivially), Corollary 6.5 (the congruence subgroup problem for `(g, r)` holds if and only if the universal monodromy representation of the arithmetic group is injective). They say what C.5, D.16, D.17 and E.2 take from them.
- Hoshi–Minamide–Mochizuki, *Group-theoreticity of numerical invariants and distinguished subgroups of configuration space groups*: Corollary 2.6 (i), Definition 2.7, Corollary 2.8 (i) (`GT × S_{n+3} ≅ Out(Π_n)` for the configuration spaces of the tripod, `n ≥ 2`). This is E.5.
- Harbater–Schneps, *Fundamental groups of moduli and the Grothendieck–Teichmüller group*: the definitions of `GT̂_0`, `GT̂` and the Main Theorem (`Out^#_4 ≅ GT̂_0`, `Out^#_n ≅ GT̂` for `n ≥ 5`). This is E.4.
- The Lean comparator `DeligneDrinfeld.lean` of the 008 pack: it ends with `theorem main : MainStatement := by sorry` (E.27).
- The transcription at scan 483 (`LM_P049_checked.tex`): the conjecture reads as quoted in D.2 ("Les sous-groupes à lacets `L_i` sont les sous-groupes maximaux dans `π`, tels que `Norm_E(L_i) → Γ⁺` ait comme image un ss-groupe ouvert").

Not opened: Boggi 2009, 2020, 2026 (three papers), Boggi–Zalesskii 2019, Boggi–Funar 2023, Paris 2009, Kerckhoff 1983, Nakamura 1994 (both papers), Mochizuki 1999 and 2006, Matsumoto 1996, Belyi 1980, Minamide–Nakamura 2022, Nakamura–Schneps 2000, Hatcher–Lochak–Schneps 2000, Lochak–Nakamura–Schneps 2026, Pop 2018, Hoshi–Mochizuki–Tsujimura 2025, Collas 2026, Hain–Matsumoto 2003, Brown 2012, Drinfeld 1990, Bar-Natan 1998, Willwacher 2026, Jansen 2023 (opened in the STRATA review), Barwick–Glasman–Haine, Hoyois 2018, Koenigsmann 2005, Pop–Stix, Harari–Stix, Stoll 2007 and errata, Stix 2015, Mazur 1977, Uchida 1979 and 1981, Hoshi 2025, Bresciani–Vistoli 2020, and the three proof packs 008, 019, 031 beyond what the prompt already recorded.

Own checks: `checks_author/check_lm3.py`, output `check_lm3.out` (standard library, exact arithmetic, about 10 seconds; written from the statements with my own code).
1. B.4: the two matrices have orders 2 and 3 and generate a group of 504 elements with class sizes 1, 56, 56, 56, 56, 63, 72, 72, 72; no proper union of classes containing the identity has order dividing 504; `|PSL_2(F_p)|` = 60, 168, 660, 1092 for `p` = 5, 7, 11, 13.
2. B.5, D.20: the discriminant of `x³ − 2` is −108; a transposition conjugated by a 3-cycle is another transposition.
3. D.2: `(12345)` and `(123)` generate a group of 60 elements.
4. F.11: the kernel of `(a, b) ↦ a + b` on `(Z/m)²` is the antidiagonal for `2 ≤ m ≤ 24`.
5. E.20: the free Lie algebra on one generator in each odd weight `≥ 3` has dimensions 1, 0, 1, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5 in weights 3 to 16 (the prompt's ten numbers are right).
6. Special derivations (new; see "Two pro-ℓ results of this review").

Verdict words: **proved** (I followed the argument step by step and found it complete, given the named inputs); **proved in outline** (the argument is sound as far as I followed it; a named step or source was not checked); **known, checked** (I opened the cited source and it says this); **known, not opened** (the citation is the answer's; I did not open it); **true, trivial**; **open, honest** (a known open problem); **open, undone** (a comparison the answer did not carry out; the literature or a computation may settle it); **claimed** (rests on one of the three unrefereed 2026 manuscripts).

## Verdict per statement

### Part A (the tower; 13 statements, read in statement only)

| Id | Label | Verdict |
|---|---|---|
| A.1 | Proved | Proved in outline (definitions; the two exact sequences are standard). His unadorned group is neither pure nor orientation-preserving: agrees with scans 204–205, 226 as transcribed. |
| A.2 | Known | Known, not opened (Dehn–Nielsen–Baer, Farb–Margalit 8.1, 8.8). |
| A.3 | Known | Known, not opened (Birman sequence, Farb–Margalit 4.6). The remark that filling on `π_1` and forgetting on mapping class groups are different maps is right and matters for C.7–C.8. |
| A.4 | Proved | Proved in outline. The Riemann–Hurwitz count is right. The report notes its own slip in the folio interval (177–180). |
| A.5 | Known | Known, not opened. `M_{0,[3]} ≃ BS_3` is right. |
| A.6 | Known | Proved in outline; depends on C.2, C.3, D.14. |
| A.7 | Proved | Proved (definition of the congruence kernel). **The double hat is `Out_lac`, not a second completion**: this reading is the one the mathematics supports throughout. |
| A.8 | Proved | Proved in outline; the two-to-one map is right (index 2 of `Σ` in `Σ^±`, by the multiplier). |
| A.9 | Proved | Proved. This is the answer's central observation: `N^arith ⊂ N^norm`, same denominator. |
| A.10 | Proved | Proved in outline. |
| A.11 | Proved | Proved (table checked by hand: `(0,2)`: `Z/2`, extended `(Z/2)²`; `(0,3)`: `S_3`; tori: `SL_2(Z)`, `GL_2(Z)`). Corrects scans 225 and 227 (see readings). |
| A.12 | Proved | True, trivial (scope statement). |
| A.13 | Proved | Proved in outline (not followed). |

### Part B (congruence, normalizers, discretizations; 15 statements)

| Id | Label | Verdict |
|---|---|---|
| B.1 | Proved | Proved. Lead 4 is wrong where it reduces the normality questions to the congruence property. |
| B.2 | Known | Known, not opened (Asada; Boggi 2009 for open genus 2; Boggi 2020, 1.4 (ii) for closed genus 2). The step for the finite extensions (multiplier mod 3) is right. |
| B.3 | Open | Open, honest (congruence subgroup problem, genus `≥ 3`). No attack is recorded beyond C.4. |
| B.4 | Proved | Proved; the finite witness is confirmed by my check 1. |
| B.5 | Refuted | Proved: the extended group `H_{0,3} = S_3 × ⟨c⟩` is not normal in `Out_lac(F̂_2)`, given the faithfulness of `G_Q` on the tripod (Belyi; D.16). The argument is complete: a normal `H` would make `⟨c⟩ = H ∩ G_Q` normal in `G_Q`. |
| B.6 | Proved | Proved. |
| B.7 | Open | Open, undone. **Its pro-ℓ analogue is false at `(0,3)` (this review, below).** |
| B.8 | Proved | Proved, given conjugacy separability and Grossman's Property A for free and surface groups (Paris 2009 not opened; both are classical). |
| B.9 | Proved | Proved (I followed both cases). His corollary of scans 352–353 holds without the congruence hypothesis. |
| B.10 | Proved | Proved in outline (Kerckhoff's Theorem 7 and Boggi–Zalesskii 3.1, 3.6 not opened). |
| B.11 | Refuted | Proved, given B.10: the Baire argument is complete (the centralizer of the deck involution in `P_{0,4}` is trivial, so its closure-centralizer is not open and the conjugacy orbit is uncountable). No finite witness exists and none is claimed. |
| B.12 | Proved | Proved. |
| B.13 | Proved | True, trivial (coset maps). |
| B.14 | Open | Open, undone. The two conditions are exact; no case was tried. |
| B.15 | Refuted | Proved (`h = x^α` with `α` non-integral lies in the kernel of filling and does not normalize `D`). It refutes the raw statement only; the prediscretization statement of item 3 is untouched, as the answer says. |

### Part C (filling a hole; 13 statements)

| Id | Label | Verdict |
|---|---|---|
| C.1 | Proved | Proved. |
| C.2 | Proved | Proved (injectivity through `Aut(π)` and centre-freeness; right-exactness of completion). The exceptions `(1,1) → (1,0)` and `(0,3) → (0,2)` are right. |
| C.3 | Known | Known, not opened (Boggi 2020, 4.7, 2.4 (ii)). |
| C.4 | Proved | Proved, given C.2 and C.3. The congruence kernel does not depend on `ν` for fixed `g`. |
| C.5 | Proved | Proved, **and checked against the source**: Corollary 6.4 says exactly that arithmetic and geometric images meet trivially. The detour through a finite extension and slimness is needed only because a type may have no `Q`-point. |
| C.6 | Proved | Proved in outline (diagram chase with C.3–C.5). His first sequence at scan 399 and condition (f) hold for the §29 groups. |
| C.7 | Proved | Proved, given `N_π(I) = I` (Boggi–Zalesskii 3.6, not opened; classical for free profinite groups). |
| C.8 | Open | Open, undone; the three equivalent forms are proved. **Its pro-ℓ analogue is false at `(0,4) → (0,3)`: the kernel is strictly larger than the point-pushing group (this review, below).** |
| C.9 | Known | Known, not opened (Hoshi–Mochizuki 2011, Theorem 6.1; I opened only its corollaries). |
| C.10 | Refuted | True, trivial (subterminal objects). |
| C.11 | Proved | Proved in outline, given Mochizuki's Theorem A. It reconstructs the curve first and the topos from the curve; it is not his construction from the groupoids of scans 407–430, and the answer says so. |
| C.12 | Proved | True, trivial. |
| C.13 | Refuted | Proved (the diagonal and a constant section of `U × U → U` meet). Agrees with his own withdrawal at scans 433–435. |

### Part D (items 5 and 6; 23 statements)

| Id | Label | Verdict |
|---|---|---|
| D.1 | Proved | Proved. |
| D.2 | Refuted | True as stated, but it refutes only the literal sentence (`L = π` is "maximal"; `[π, π]` also has full normalizer). The sentence of scan 483 does read that way. The question he means (procyclic `L`, no cyclotomic condition given) is not decided here: see D.23. |
| D.3 | Known | Known, not opened (Nakamura 1994, Theorem 2.1.1). |
| D.4 | Known | Known, not opened (Mochizuki 1999, Theorem A). The inertia consequence is proved. |
| D.5 | Proved | Proved, given D.4 and Mochizuki's Theorem C. This is his sentence of scan 485 as a proposition. |
| D.6 | Refuted | Proved (I followed the Kummer argument: the tangential section at 0 has trivial Kummer class, and `∩ (Q^×)^m = {1}`). |
| D.7 | Open | Claimed (OpenAI 019). The audit of §§3–6 is the answer's; I checked none of it. |
| D.8 | Proved | Proved in outline as a conditional statement (the two-valuation argument was followed; Koenigsmann and Pop–Stix not opened). |
| D.9 | Proved | Conditional; not followed (Harari–Stix, Stoll, Stix not opened). |
| D.10 | Proved | Conditional; the deduction is short and sound given D.9, Stoll 8.8 and Mazur. |
| D.11 | Proved | Proved, given that a number field's absolute Galois group has no non-trivial topologically finitely generated closed normal subgroup (Mochizuki 2006, 2.4, not opened; also in Fried–Jarden). |
| D.12 | Proved | Conditional on OpenAI 031; the reduction was followed and is sound. Unconditional for isomorphisms and for source field `Q`. |
| D.13 | Open | Claimed (OpenAI 031). |
| D.14 | Known | Known (classical); the derivation of slimness is proved. Answers "je cale sur a)" of scan 496: both centres are trivial. |
| D.15 | Proved | Proved, given Nakamura 2.1.2 and Boggi–Zalesskii 3.6. |
| D.16 | Known | Known, checked (Corollary 6.3 (i)); the Belyi argument for the tripod is complete. |
| D.17 | Known | Known, checked (Corollary 6.4), with the slimness step. **This decides "peut-être est-ce tout à fait faux ?" (scan 504): it is true**, for the orientation-preserving geometric image. |
| D.18 | Proved | Proved. |
| D.19 | Proved | Proved, given D.4. |
| D.20 | Refuted | Proved (the CM curve `y² = x³ − x` over `Q(i)`). |
| D.21 | Proved | Proved in outline. |
| D.22 | Proved | Proved, given D.3: I followed the step that the image in `π^ab` of a basis element is primitive, which forces the cyclotomic exponent. |
| D.23 | Open | Open, undone. Two things are bundled: uniqueness of the invariant loop structure beyond the tripod (first case `(1,1)`), and the admissible splittings of `N_{g,ν}`. Neither was attacked. |

### Part E (the conjecture fondamentale; 28 statements)

| Id | Label | Verdict |
|---|---|---|
| E.1 | Proved | Proved. |
| E.2 | Known | Known, checked (it is D.17). **Item 1 for the §29 groups is a theorem in every hyperbolic type.** |
| E.3 | Known | Proved from E.2 and Kronecker–Weber. His consequence (abelianization `Ẑ^×`) holds for the §29 groups. |
| E.4 | Known | Known, checked (Harbater–Schneps, Main Theorem). |
| E.5 | Known | Known, checked (Hoshi–Minamide–Mochizuki, 2.6, 2.8). |
| E.6 | Proved | Proved. |
| E.7 | Proved | Proved in outline; I followed it for `n = 3` and `n = 4` and found no gap, given E.4, E.5 and the genus-0 congruence property. **The §26 group is `GT̂_0` at `(0,3)` and `GT̂` at `(0,n)`, `n ≥ 4`.** I did not find this formulation in the sources I opened; the answer makes no novelty claim. |
| E.8 | Open | Open, honest (`G_Q = GT̂`). The remark that the strictness of `GT̂ ⊂ GT̂_0` was not verified is correct caution; my computation gives graded evidence for strictness in weight 7 (below). |
| E.9 | Known | Known, not opened (Minamide–Nakamura 2022). |
| E.10 | Proved | Proved in outline (the characteristic subgroup and the two-chain relation were followed; Minamide–Nakamura 3.2 (iii) not opened). The §26 group at `(1,1)` is `GT̂`. |
| E.11 | Proved | Proved (a reduction). |
| E.12 | Known | Known, not opened. |
| E.13 | Known | Known, not opened; a 2026 preprint of Boggi, which the answer did not audit. |
| E.14 | Open | Open, undone. |
| E.15 | Known | Known, not opened (Pop 2018). |
| E.16 | Known | Known, not opened (Hoshi–Mochizuki–Tsujimura 2025). |
| E.17 | Proved | Conditional (D.10 again). |
| E.18 | Known | Known, not opened. |
| E.19 | Known | Known, not opened (Drinfeld, Bar-Natan, Brown). |
| E.20 | Proved | Proved as a conditional (dimension squeeze); the dimensions agree with my check 5. |
| E.21 | Known | Proved in outline (the non-injectivity of `GT̂ → GT_ℓ` follows from Belyi and the unramifiedness of the pro-ℓ action outside ℓ). |
| E.22 | Proved | True, trivial. |
| E.23 | Refuted | True, trivial (`1 ⊂ C_2`). |
| E.24 | Proved | Proved as a conditional. `GRT^ab = G_m` is the rational counterpart of his abelianization statement. |
| E.25 | Known | Known, not opened. |
| E.26 | Open | Claimed (OpenAI 008); the audit is the answer's. |
| E.27 | Refuted | True: the attached file ends in `sorry` (I opened it). The prompt had called it a "comparator statement" and claimed no proof, so nothing of ours is refuted. |
| E.28 | Known | Not opened: the answer reports a later preprint (Willwacher, arXiv:2610.15592v4) with another proof of the 008 theorem. **Unverified by us; to be opened before it is cited anywhere.** |

### Part F (the tower as one object; 18 statements)

| Id | Label | Verdict |
|---|---|---|
| F.1 | Known | Known, checked in the STRATA review (Jansen 3.18, 3.23, 6.6, 6.7). |
| F.2 | Proved | Not followed (proof not read). |
| F.3 | Refuted | True, trivial (`[1]` against the point). It does not contradict the prompt, which spoke of natural isomorphisms. |
| F.4 | Proved | Not followed. |
| F.5 | Known | Known, not opened (Boggi 2020, 3.3–3.6, 4.2, 4.3). |
| F.6 | Proved | Proved in outline, given F.5. |
| F.7 | Proved | Proved in outline; the cofinality argument was followed and is the substantive step. The transporter formula the prompt proposed is confirmed. |
| F.8 | Proved | Proved in outline. |
| F.9 | Known | Known, not opened (Barwick–Glasman–Haine 12.6.4, 12.6.6–7). |
| F.10 | Proved | Proved in outline; faithfulness for `n ≥ 4` was followed. |
| F.11 | Proved | Proved, given F.5; my check 4. The STRATA result (forgetting a point is not smooth) persists profinitely, with the cyclotomic action on the obstruction. |
| F.12 | Proved | Proved in outline (Boggi–Funar 4.11, 4.12, 7.2 not opened). |
| F.13 | Proved | Proved in outline, given F.12 and E.4. **The automorphism group of the decorated two-level boundary tower is `GT̂`**: this is the theorem Part F asked for, in genus 0. |
| F.14 | Proved | Proved in outline. |
| F.15 | Proved | Not followed beyond the statement. |
| F.16 | Open | Open, undone (types `(1,1)`–`(1,2)`). |
| F.17 | Known | Known, not opened. The caution (the exit category is not a groupoid, so Malcev completion of Hom-sets is not the parenthesized braid groupoid) is right. |
| F.18 | Open | Open, undone. |

## Is anything labelled Proved, Known or Refuted false?

No. The points to keep in mind when the results are used:
- D.2 and E.27 are true and nearly empty (above).
- "Known" covers 30 statements, of which I checked 7 against their sources (D.16, D.17, E.2, E.4, E.5, F.1 and, through C.5, Corollary 6.4). E.13 and E.28 rest on 2026 preprints.
- Eleven "Proved" statements are conditional on the unrefereed 2026 manuscripts or are reductions (D.8–D.10, D.12, E.17, E.20, E.24) or depend on citations not opened (B.10, C.7, D.15, E.10, F.6–F.8, F.12–F.15).
- The answer's "Open" has three meanings, which its report separates: known open problems (B.3, E.8), unverified claims (D.7, D.13, E.26), and comparisons not carried out (B.7, B.14, C.8, D.23, E.14, F.16, F.18). The last seven are where the prompt's wording ("what is open", "say exactly what remains") let it stop. `LM3b_TEICHMULLER_PUSH` attacks them.

## Two pro-ℓ results of this review (mine; program-checked; read by no one else)

Let `F` be the free pro-ℓ group on `x_1, …, x_r`, `x_0 = (x_1 ⋯ x_r)^{-1}`: the pro-ℓ fundamental group of type `(0, r+1)`. A *special* automorphism sends each `x_i` (`0 ≤ i ≤ r`) to a conjugate of itself. Its graded shadow in degree `n` is a special derivation `D(x_i) = [a_i, x_i]` of the free Lie algebra, `a_i` of degree `n`, with `Σ_{i ≥ 1} [a_i, x_i] = [a_0, Σ x_i]`. Write `OutSDer_n` for special derivations modulo inner ones.

**Lifting.** Every special derivation over `Z_ℓ` is the leading term of a special automorphism. Proof: choose lifts `a_i ∈ Γ_n F`; the defect of the equation `Π a_i x_i a_i^{-1} = a_0 (x_1 ⋯ x_r) a_0^{-1}` lies in `Γ_m F` for some `m ≥ n + 2`; replacing `a_i` by `a_i b_i` with `b_i ∈ Γ_{m−1}` changes the defect by `Σ [b_i, x_i] − [b_0, Σ x_i]` in `gr_m`, and this map `⊕ gr_{m−1} → gr_m` is surjective over `Z` for `m ≥ 2`; iterate and pass to the limit. The same works inside the subgroup of automorphisms inducing the identity on `F/⟨⟨x_1⟩⟩`, with `a_i` (`i ≠ 1`) and `b_i` in the normal closure of `x_1`, because the ideal `(x_1)` of the free Lie algebra satisfies `I_m = [Lie_{m−1}, x_1] + Σ_{i ≠ 1} [I_{m−1}, x_i]`. (I believe the first statement is Ihara's; I did not look it up.)

**Dimensions (`check_lm3.out`).** Type `(0,3)`: `dim OutSDer_n = 0, 0, 1, 0, 3, 0, 6, 4` for `n = 1, …, 8` (`= 2 l_n − l_{n+1}` for `n ≥ 2`), and the `S_3`-invariants have dimension `0, 0, 1, 0, 1, 0, 2, 1`. Type `(0,4)`: `dim OutSDer_n = 2, 1, 6, 6` for `n = 1, …, 4`; the Lie algebra generated by the two point-pushing derivations of degree 1 has dimensions `2, 1, 2, 3` (it is free of rank 2 as far as computed); the kernel of filling `x` has dimensions `2, 1, 5, 6`; the image has dimensions `0, 0, 1, 0`, equal to `OutSDer_n(0,3)`.

**Result 1 (pro-ℓ analogue of B.7, item 2).** In `Out_lac` of the pro-ℓ group of type `(0,3)`, the geometric `S_3` is not normal, for every prime ℓ. Proof: in weight 5 the outer special derivations form `1 ⊕ (standard)` as an `S_3`-representation; lift a non-invariant `D` to a special automorphism `σ`; then `θσθ^{-1} ≠ σ` in `Out` for some `θ ∈ S_3`, since the leading terms differ modulo inner derivations. If `S_3` were normal, it would commute with the normal subgroup of label-preserving automorphisms (the two meet trivially). So the pro-ℓ analogues of "`T̂⁺` invariant" and "`N_Σ = T̂̂`" (scans 322–326) fail at `(0,3)`. For the full profinite group the question becomes exact: is the image of `Out_lac^pure(F̂_2)` in `Out_lac^pure` of the maximal pro-ℓ quotient contained in the centralizer of `S_3`? This is not decided.

**Result 2 (pro-ℓ analogue of C.8, the sequence marked "??").** For the pro-ℓ groups of types `(0,4) → (0,3)`, the kernel of the filling map `O_{0,4,i} → O_{0,3}` is strictly larger than the point-pushing group `π_{0,3}`. Proof: in weight 3 the derivations inducing zero on the filled Lie algebra span 3 dimensions modulo inner and point-pushing derivations; lift one inside the kernel (second form of the lifting); if the lift were point-pushing by `γ` up to inner automorphisms, then `γ ∈ Γ_3` by the injectivity of the point-pushing Lie map in degrees 1 and 2, and its leading term would be a point-pushing derivation of degree 3. So his "??" is justified in the pro-ℓ setting: the unrestricted sequence is not exact in the middle. Surjectivity of the filling map holds on graded pieces through weight 4.

**Graded evidence on E.8.** The `S_3`-invariant outer special derivations (the graded shadow of `GT_0`, relations (I) and (II) without the pentagon; identification not checked) have dimension 2 in weight 7, against `dim grt_1 = 1` there. So the inclusion `GT ⊂ GT_0` is strict on graded pieces in weight 7, if that identification holds.

What these do not show: anything about the full profinite groups, which is what Grothendieck's statements are about.

## Readings: where the mathematics supports one reading (for the editors)

From `readings.csv` (42 rows). None is a decision; "inspected" means the answer says it looked at the scan image. Not re-checked by me against the scans.

Supported strongly or decisively, by a type check or a counterexample:
- LM_P021, scan 206: `A_g = A^!_{g,0}` (equality, not `⊃`).
- LM_P023, scan 222: "pointées" (a base point is needed), not "ponctuées". Scan 225: `ν = 2`, `g = 0` in the cylinder paragraph. Scan 226: the pair is `(ρ, χ)` and `z ↦ 1/z` gives `(−1, +1)`. Scan 227: `Γ⁺_{0,3}` (genus 0). Scan 228: `Γ^!_{g,2}` and `Γ_{0,1}`.
- LM_P026, scan 252: `π_1(U_{g,ν})`, not of the universal cover; `A° × Π` (direct product, by A.13). Scan 258: `π_i(M̃) ≅ π_{i−1}(A°)`.
- LM_P027, scan 263: the last extension should carry `ν + 1`. Scan 266: `Π_{B_U}`.
- LM_P033, scan 321: "pré-discrétification" (inspected).
- LM_P036, scan 352: the margin reads `π′ · π_0 = π` with `π′`, not `π′_0` (inspected). Scan 358: the normalizer is taken in the double-hat group (image not available to the answer).
- LM_P040, scan 399: `N` and a right arrow in equation (9) (inspected).

Apparent slips of the author (the reading is not in doubt; the mathematics is):
- Scans 225, 227: the identification of (51) with (51 bis) is false as written (`ρ_π = ρ_perm · ε`), and the determinant-one sentence in rank one is false.
- Scan 261: the chain `M̃_{3,0} → M̃_{2,0} ≃ M̃_{1,0} ≃ M̃_{0,0}` is impossible by dimensions; `M_{0,3} → M_{0,2} → M_{0,1} → M_{0,0}` is what the argument uses.
- Scan 348: the target of the claimed sequence should be `Out_lac(π′)`; the margin condition `2g + ν ≥ 3` should be `≥ 4` (hyperbolic target); the oriented quotient lacks a `+`.
- Scan 352: the deck group is written `π′/π`; it must be `π/π′` (inspected).
- Scan 371: one occurrence of the geometric image lacks `+`. Scan 395: equation (4) lacks `!` in the denominator.
- Scan 418: condition (5) holds over a field and fails for families (C.13), as he finds at scans 433–435.
- Scan 483: the criterion for the `L_i` is false as written (D.2).

No preference from the mathematics: scan 204 (`x_{g,i}` or `a_{g,i}`), 223, 253, 260, 328 (folio), 348 ("anabélien" or "nonabélien"), 357 (`C` or `G`), 485 (font, folio), 496, 500 (`ℓ_i` or `h_i`; `L_i^n` or `ℓ_i^n`: equivalent), 501 ("endom." suffices), 504, 505. Scan 502 (`N_4(π)` or `N_Δ(π)`): unresolved and substantive.

Two observations on the text itself: the phrase the prompt quoted for item 4 ("tout le topos étale d'une courbe algébrique complète …") was not found by the answer as a literal sentence in scans 395–420 (it comes from the author's table of contents); and scans 370–371 change the definition of `N` (arithmetic image, with `G_Q → 𝕀Γ` "surjectif").

## Corrections to the leads and to OVERVIEW.md

1. **Lead 1 is wrong as stated.** It took `𝕀Γ_{0,3}` to be a `GT̂`-like group. There are two groups. For the §29 definition, scan 479's "impression" is a theorem (Belyi for injectivity; surjectivity by definition). For the §26 definition, `𝕀Γ_{0,3} = GT̂_0` and `𝕀Γ_{0,n} = GT̂` for `n ≥ 4` (E.7), and the conjecture is `G_Q = GT̂` (and at `(0,3)` alone it also needs every element of `GT̂_0` to satisfy the pentagon).
2. **Lead 2** stands, with two corrections: the criterion of scan 483 needs the cyclotomic condition (D.2, D.3); the absolute form is conditional on OpenAI 031 except for isomorphisms and source field `Q` (D.12).
3. **Lead 3** stands and is exceeded: faithfulness holds modulo the geometric image (D.17), which he doubted.
4. **Lead 4 is wrong in one clause.** The congruence problem is one of three separate questions (B.1): injectivity of `T̂ → T̂̂`; normality of the image; whether the image is everything. "`T̂ ≠ T̂̂` always" holds for hyperbolic types (B.4). Closed genus 2 is Boggi 2020, not the paper attached.
5. **Lead 5** stands for the geometric and arithmetic rows; the unrestricted row "??" is not a cuspidalization statement in the sense of Hoshi–Mochizuki (C.8, C.9), and its pro-ℓ analogue fails (Result 2).
6. **OVERVIEW §2, "The conjecture fondamentale … [L] Belyi gives injectivity; the rest is the question of `GT̂`, open":** to be replaced by the two-group statement of point 1.
7. **OVERVIEW §3:** "the faithfulness of `Γ → 𝚪_g`, `𝚪_{1,1}` (peut-être est-ce tout à fait faux ?)" is settled: true (D.17). "The centre of `Gal` (je cale, Consulter Deligne)" is settled: trivial, and `Gal` has no finite normal subgroup (D.14). "Centralizers in the profinite anabelian case, pas prouvé pour le moment dans aucun cas" (scan 118): the cases used in §35 are theorems (D.15); the general statement belongs to LM4.
8. **OVERVIEW §2, the category of curves (§34):** "largely theorems now" is right; the precise list is D.4, D.5, D.12, with D.6 as the caution for affine curves (tangential sections).
9. The prompt's item 4 quoted the table of contents as if it were the text of §32.

OVERVIEW.md is in the sent stack and was not edited; these corrections are carried by the "After LM3" sections of LM4–LM8 and by `LM3b_TEICHMULLER_PUSH`.

## Not verified

- Part A's proofs; F.2, F.4, F.15; D.9; the audits of the three 2026 manuscripts (D.7, D.13, E.26); every citation listed under "Not opened".
- The readings against the scans.
- My two pro-ℓ results: the dimension counts are exact computations; the lifting argument and the two deductions are written above and were checked by no one else. The attribution to Ihara is from memory.
- Whether E.7 is in the literature in this form.
