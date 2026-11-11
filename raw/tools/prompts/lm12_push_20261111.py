# lm12_push_20261111.py -- work file (Claude, Fable 5.2; 11 Nov 2026).
# LM1_GROUP_SCHEMES and LM2_LOOP_EQUATIONS were not sent (user, 11 Nov). This script does for them what
# push_rewrite_20261111.py did for LM4-LM8: before-copy, demands on the items, "After LM3" and "After BISITE" sections,
# new Parts, today's common block; then rebuilds both background zips (old zip kept as _v<n>), and appends to the record.
import io, os, re, sys, shutil, zipfile, hashlib, csv, glob
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from outcome_block import outcome, words
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
STACK = os.path.join(ROOT, "pro_prompts_draft_20261111")
DER = os.path.abspath(os.path.join(ROOT, "..", "derivateurs_companion_20261109"))
RET = os.path.join(ROOT, "pro_returns_20261111", "LM3_TEICHMULLER_TOWER")
REV = os.path.join(ROOT, "pro_reviews_20261111", "LM3_TEICHMULLER_TOWER")
BIS = os.path.join(DER, "pro_returns_20261110", "7_BISITE")
BISR = os.path.join(DER, "pro_reviews_20261110", "7_BISITE")
GAL = os.path.join(DER, "pro_returns_20261110", "4_GALOIS", "GALOIS")
LM3DL = os.path.join(HERE, "LM3_TEICHMULLER_TOWER", "_downloads")
LM3BDL = os.path.join(HERE, "LM3b_TEICHMULLER_PUSH", "_downloads")
VERBS = r"\b(prove|proves|proved|refute|decide|construct|compute|classify|determine|derive|exhibit|enumerate|tabulate|attack|carry out|write a program|by program|find)\b"
rd = lambda p: io.open(p, encoding="utf-8").read()
def wr(p, s): io.open(p, "w", encoding="utf-8", newline="\n").write(s)
sha = lambda b: hashlib.sha256(b).hexdigest()

LM3_STATUS = ("Package `LM3_TEICHMULLER_TOWER` of this series has been answered (GPT-6 Astra, ChatGPT Pro mode; 110 statements: "
 "57 Proved, 30 Known, 11 Refuted, 12 Open) and reviewed by the author of this prompt (Claude, Anthropic): no statement labelled "
 "Proved, Known or Refuted was found false; the review gives a verdict per statement and says which sources were opened (seven of the "
 "thirty Known statements were checked against their sources). The answer is attached under `LM3_return/` (paper, sections, registers, report; its code is not attached) and the review under "
 "`LM3_review/`. Its statements are cited by their numbers. The review is not authority: verify what you use.")
BIS_STATUS = ("All seven packages of the companion work on *Les Dérivateurs* have been answered (GPT-6 Astra, ChatGPT Pro mode) and reviewed by "
 "Claude (Anthropic). The last, BISITE, was reviewed only in part. The files named below are attached under `BISITE_return/` and `BISITE_review/`; "
 "statements are cited by their numbers. Where a combination of these results is an argument of the reviewer, it is called a lead: it is unverified, and is to be proved or refuted.")
PREAMBLE = ("Every part asks for mathematics: a theorem with its proof, or a counterexample or computation with code and output. A known result is cited by theorem number and then used: "
 "derive his statement from it in his form and write the reduction. Where a statement resists, prove the strongest case within reach ({cases}), compute, and state the obstruction as an exact "
 "statement with its smallest undecided instance. Carry each part to where it stops.")

P = {}
# ================================================================================== LM1
P["LM1_GROUP_SCHEMES"] = dict(
items={
"1": "**Asked:** write the scheme by equations and compute its dimension, flatness and smooth locus over `Z` by program; prove uniqueness of lifts with the exact condition on `S` and the counterexample without it; prove or refute surjectivity of each parametrization, as a map of fppf sheaves and on points.",
"2": "**Asked:** decide it for `SL_2`, `PGL_2`, `GL_2`: prove the presentation over the largest base where it holds and determine the kernel of the comparison map where it fails.",
"3": "**Asked:** define \"représentation motivique\" so that his construction is a theorem, and prove it for the representations he has; compute the adelic points.",
"4": "**Asked:** classify the central extensions by `μ_2`, compute the Brauer class and its order, carry out the exercise of class field theory with an explicit example, and decide the generation statement of scan 652 by computing the index.",
"5": "**Asked:** decide the question of scan 6 over each base; decide the \"lemme dubitatif\" by a proof or by a counterexample found by program; prove or correct the \"Théorème (!)\"; construct the envelope and prove its universal property.",
},
after_lm3=LM3_STATUS + r"""

- **Which profinite group the scheme is compared with (Part D).** LM3 E.1, E.2, E.7: his group of pairs `(λ, f)` commuting with the geometric `𝔖_3` in the loop-preserving outer automorphisms of `π̂_{0,3}` is `GT̂_0`, the group of Drinfeld's relations (I) and (II) (Harbater–Schneps, Main Theorem (a), checked by the reviewer); the image of `Gal(Q̄/Q)` is a closed subgroup of it (Belyi), and the quotient of the arithmetic image by the geometric one is `Gal(Q̄/Q)` in every type (Hoshi–Mochizuki 2011, Corollary 6.4, checked). E.10: at type `(1,1)` the normalizer group is `GT̂`, through `B_4/Z → B_3/⟨ζ_3²⟩ = SL_2(Z)`. So "the solutions of the profinite equation of loops" in Part D means one of three groups (Galois; `GT̂`; `GT̂_0`): name it in each statement.
- **`SL(2, Z)^` is not `SL(2, Ẑ)` (Part D).** LM3 B.2, B.4: the profinite completion of `SL_2(Z)` acts faithfully on `π̂_{1,1}` (the congruence property in genus 1, Asada), while its map to `SL_2(Ẑ)` has a large kernel; an explicit non-congruence quotient is `SL_2(F_8)`, generated by the images of the elements of order 2 and 3 of `PSL_2(Z)` (reproduced by the reviewer's program). A group scheme over `Z` sees `SL_2(Ẑ)` and its congruence quotients only. What the passage from the equation in `SL(2, Z)^` to the scheme `M_{ρ,σ}` loses is therefore a question with content.
- **Conventions.** LM3 A.11: the table of the groups of the non-hyperbolic types and of `(0,3)`, `(1,1)` (`𝔖_3`; `SL_2(Z)`; `GL_2(Z)` with orientation reversal); D.14: centres.
- Nothing in the leads of this prompt is refuted or settled by LM3.
""",
after_bis=BIS_STATUS + r"""

- **What an envelope can see (Part E).** BISITE B.11 (`BISITE_return/sections/B.tex`): the endomorphism `x ↦ x`, `y ↦ y[x, y]` of the free group of rank 2 is the identity on the abelianization and carries the transitive action `x ↦ (12)`, `y ↦ (13)` on three letters to an intransitive one. A lead of the reviewer, unverified: by Stallings's theorem it is an isomorphism on every nilpotent quotient and on the pro-ℓ and Malcev completions, so no nilpotent or pro-unipotent approximation of the free group sees the covering with group `𝔖_3`; a metabelian envelope does (`𝔖_3` is metabelian). His §50 passes from unipotent to metabelian envelopes for this reason, or for another: Part E asks.
- **Two rational theories (Part E).** GALOIS C.13–C.14 (`GALOIS_return/`; C.13 is Known there, from Rivera–Wierstra–Zeinalian 2021, Theorem 3): locally constant coefficients in `D(Q)` keep the discrete fundamental group; Toën's schematization keeps its pro-algebraic completion, and is strictly coarser. The schematic envelope of §50 is a third object, over `Z`.
- The follow-up on "exactness of the approximations" (item L5 of the reviewer's list, written for LM7_FERMAT_TOWER and LM8_LIE_APPROXIMATIONS) asks to identify the completion of `π_1` of the Fermat tower relative to `(Z/n)²`, or to `𝔖_3 × Ẑ^*`, with his `M_{ρ,σ}` and `N_{ρ,σ}`. The half of that question that concerns these group schemes is asked here, in Part E.
""",
parts="## Parts\n\n" + PREAMBLE.format(cases="one base: `Z[1/6]`, `Z_2`, `Z_3`, `F_2`, `F_3`; one group: `SL_2`; low degree") + r"""

**A. Definitions and dictionary.** (a) All groups and schemes of §§48–49 with his symbols, scans and the corrected formulas (the second-pass corrections for C3-264-282 to C3-682-696 are attached and change many of them: `η = βσ(β)^{-1}`, the definition (13)–(14) of `M_{ρ,σ}` by `det f = det y = ε' det x`, the generators `ε_0, ε_1`, and so on), in one table. (b) Check every formula of the table by computer algebra: write a program that states each identity over the universal ring (`Z` adjoined the coordinates of `α`, `β` and the units that occur) and verifies it, or finds the correction; for each formula whose form depends on an open reading, test every alternative and report which is consistent, with the scan, in `LM1_GROUP_SCHEMES_readings.csv`. (c) Prove the existence and uniqueness of his canonical "épinglage" attached to `ρ`, `σ`, over which bases. (d) Prove his characterization of the "modular" triple `(ε, σ, ρ)`: classify such triples up to conjugacy in `SL_2(R)` and `GL_2(R)` for `R = Z`, a field of each characteristic, `Z/4`, `Z/8`, `Z/9`, by a proof and by enumeration for the finite rings.

**B. The scheme `M_{ρ,σ}` for `SL_2`, `GL_2` (item 1).** (a) Its functor of points; prove representability by writing the equations. (b) Compute by program (Gröbner bases over `Z`, and over `F_2`, `F_3`, `Q`): the relative dimension (compare scans 151 and 393, "dimension 6"), flatness over `Z`, the smooth locus, and for the fibres at 2 and 3 their components, their reducedness and their singular loci; then prove what the computation shows, including smoothness away from 2 and 3 (140-4 scan 41). (c) Prove the group structure, the épinglage, the subgroups `M(0)`, `M[0]`, `M(q)`, and each exact sequence of §48.IX–XI and §49.V–VI, as sequences of fppf sheaves; where a sequence is exact only on points over certain rings, say which. Name and correct every slip of the manuscript. (d) Uniqueness of the lifts (scan 358): prove it with the exact hypothesis on `S`, and construct the counterexample of scan 323 (`τ` with `2τ = 0`, `τ² = 0`) over the smallest ring. (e) Surjectivity of the parametrizations (scan 370): prove it as a statement on fppf sheaves, compute the image on `Z`-points, `F_2`-points, `F_3`-points and `Z/4`-points, and give every point that is missed. (f) Count `M_{ρ,σ}(F_p)` for `p ≤ 13` and `M_{ρ,σ}(Z/n)` for `n = 4, 8, 9` by program and compare with the count predicted by (c). (g) The general `M_{ρ,σ}` "sans signes" and with the signs `ε_2`, `ε_3`: the same, and the passage from `M̃_{0,3}` to `Ñ_{1,1}` and from `GL(2, Ẑ)/{±1}` to `GL(2, Ẑ)` proved as a statement about these schemes.

**C. Presentations over `Z` (item 2, Lead 1).** (a) State the question in fppf sheaves of groups: the amalgam sheaf `A` generated by the finite flat subgroup schemes he names and by `G_a`, with his relations, and the map `A → G`. (b) Prove that it is onto for `SL_2`, `PGL_2`, `GL_2` over `Z`, or determine the cokernel. (c) Determine the kernel. Over a field the relations among elementary matrices are governed by `K_2` (Steinberg; Matsumoto; the central extensions of Deligne and of Brylinski–Deligne, attached): prove whether the kernel of `A → SL_2` is central, and identify it with a sheaf you name, or prove that his relations already kill it. (d) Test on points by program (coset enumeration): `R = F_2, F_3, F_4, F_5, F_7, Z/4, Z/9`, and `Z` itself, where the answer must be Serre's amalgam `Z/4 *_{Z/2} Z/6`; `Z[1/2]` and `Z[1/3]` (Serre's amalgams of two copies of `SL_2(Z)`). (e) Decide the correction at 2 and 3, where `μ_4` and `μ_6` are not étale: prove what the presentation is over `Z_2` and `Z_3`. (f) State the theorem he would have wanted, with proof, and say what remains as an exact statement.

**D. Points and extensions (items 3, 4).** (a) Compute `M_{ρ,σ}(Z)`, `M_{ρ,σ}(Z_p)` for all `p`, `M_{ρ,σ}(Ẑ)` and `M_{ρ,σ}(A_f)` as groups, with the proof. (b) The comparison with §§38–47: construct the map from the solutions of the profinite equation of loops to `M_{ρ,σ}(Ẑ)` for each of the three groups of "After LM3" and compute its image and kernel as far as you can. Prove or refute: the image of `Gal(Q̄/Q)` is open in `M_{ρ,σ}(Ẑ)`; the image of `GT̂_0` is larger. Compute the images modulo 2, 3, 4, 6, 12 by program (the solutions of relations (I), (II) in the finite quotients concerned). Decide what the scheme loses: construct a solution of the profinite equation in `SL(2, Z)^` whose image in every congruence quotient is trivial (use the non-congruence quotient `SL_2(F_8)`), or prove there is none; and what it adds: points of `M_{ρ,σ}(Ẑ)` that come from no solution. (c) The central extensions by `μ_2` (scans 596–605): classify them (compute the relevant `H²` of the group schemes), prove non-triviality, prove or refute the normality of the complements. (d) The Brauer class `c` (scans 610–611): prove that it is the cup product he writes, compute it as a quaternion algebra (Lead 4: the symbol of `−1` and `−3`, or of `ε_2` and `ε_3`), and decide its order and the group it generates against his "ne peut guère être que Z/4Z" (scan 631). (e) The exercise of scan 634: construct a lift with full image, as an explicit Galois extension with its ramification, and verify the local conditions by program; prove the general statement by class field theory. (f) Scan 652: compute the index of the subgroup generated by `ρ`, `σ`, `τ` in `G⁺(Z/n)` for `n ≤ 48` by program, and prove what the finite group is. (g) "Représentations motiviques" (scan 489): give the definition under which his construction is a theorem, prove it for the representations on the torsion of the universal elliptic curve and on the unipotent fundamental group (Hain–Matsumoto: theorem numbers), and state what the general construction would require.

**E. §50 (item 5).** (a) Scan 6: prove that a fibrewise unipotent section is given by a homomorphism `G_a → G` over a `Q`-algebra; give the counterexamples in characteristic `p` (elements of order `p²`; Witt vectors) and over `Z/p²`; prove the correct statement over `Z` with divided powers. (b) The "lemme dubitatif" (scans 10–16): state it exactly in each reading; search by program for a counterexample among signed combinations of divided powers and exponentials of degree at most 12 at the primes 2, 3, 5 (work with bases of integer-valued polynomials; Bhargava's `P`-orderings are attached); then prove the theorem or exhibit the counterexample. (c) Prove or correct the "Théorème (!)" of folio 652'. (d) Construct the schematic envelope of a metabelian group, prove its universal property, and prove for each of the existing hulls (Hochschild–Mostow; the Malcev completion and its integral form of Lazard and Hall; Hain's completion relative to a finite or reductive quotient) whether it maps to, equals, or differs from his, with the map and an example separating them. (e) The worked example: the envelope of `𝔖 = SL(2, Z)/[Π_0, Π_0]` used in §51. Compute its coordinate ring over `Z`, its fibres at 2 and 3, its group of `Ẑ`-points, and the homomorphism from `𝔖`; decide whether it is the completion of `SL(2, Z)` relative to its quotient of order 12 or 24 pushed to the metabelian level, and identify it with his `M_{ρ,σ}`, `N_{ρ,σ}` or state the exact difference (the question of "After BISITE"). Package LM7_FERMAT_TOWER uses this. (f) Prove or refute the lead of "After BISITE" (Stallings), and prove that the envelope of `𝔖` detects the covering with group `𝔖_3`, or that it does not. (g) Compare the envelope with the two rational theories of GALOIS C.13–C.14 on the example `𝔖`: what each keeps.
""")

# ================================================================================== LM2
P["LM2_LOOP_EQUATIONS"] = dict(
outcome_extra="The list of Part E is a separate file as well, `LM2_LOOP_EQUATIONS_new_conditions.csv`: one row per condition of §§38–47 not derived from the relations of `GT̂`, with its scan, the proof on `Gal(Q̄/Q)`, and the decision on `GT̂` and on `GT̂_0`.",
items={
"1": "**Asked:** decide each congruence property: derive it from the profinite algebra, or prove it for `Gal(Q̄/Q)` and exhibit a non-arithmetic solution at a finite level that violates it.",
"2": "**Asked:** compute the solutions of his equations in the finite quotients by program, and prove what can be proved about elements of finite order and about solutions other than `1` and `τ_∞`.",
"3": "**Asked:** prove the sign statements by class field theory; determine the \"groupe adélique\"; attack the characterization of `Γ_Q` in `Γ̃` with the group-theoretic descriptions now known.",
"4": "**Asked:** prove or refute the unique splitting; decide the sign of the torus condition from the mathematics.",
"5": "**Asked:** prove faithfulness and say modulo what; decide the lifts through `±1`; prove the anabelian converse or reduce it to a named section statement; decide the existence he doubts.",
},
after_lm3=r"""**The package LM_P060.** LM_P060 (cote 140-3, scans 11–20, the start of §§38–39) has two different first-pass returns. The current text, `longue_marche/LM_P060/LM_P060_checked.tex`, descends from the later one and was checked line by line against the scans in the second pass; which return was meant as the first pass is not recorded, and the second pass did not decide between them as such. Both are attached: `longue_marche/LM_P060_first_pass_returns/return_1_earlier/` and `return_2_later/`. Work from the checked text; where the two returns differ in a formula you use, look at the scan (`scans/140-3/`), and enter the place in `LM2_LOOP_EQUATIONS_readings.csv` with what the mathematics supports.

""" + LM3_STATUS + r"""

- **Lead 1, sharpened.** LM3 A.9, E.1, E.2: his `𝕀Γ_{0,3}` has two definitions: in §26 the normalizer of the geometric `𝔖_3` in `O = Out_lac(π̂_{0,3})`, modulo `𝔖_3`; in §29 the arithmetic image modulo `𝔖_3`, which is `Gal(Q̄/Q)` (Belyi for injectivity; surjectivity by definition). E.7: the first is the centralizer of `𝔖_3` in `O`, and equals `GT̂_0` (Harbater–Schneps, Main Theorem (a): `Out^#_4 ≅ GT̂_0`, checked by the reviewer). So three groups are in play: all label-preserving loop automorphisms `(λ, f)`; those commuting with `𝔖_3` (`GT̂_0`); the image of Galois. E.8: LM3 did not verify that `GT̂ ≠ GT̂_0`. His `M̃_{0,3}` of §§45–46 must be identified with one of them, from his definitions (Part A).
- **Type `(1,1)`.** E.10: the normalizer group at `(1,1)` is `GT̂` (through `P_{1,2} ≅ B_4/Z`, Minamide–Nakamura 2022, not opened by the reviewer; `B_4/Z → B_3/⟨ζ_3²⟩ = SL_2(Z)` with kernel `π_{1,1}`; the peripheral element is `ζ_3²`). E.9: `Out` of the profinite completion of `SL_2(Z)` is not asserted to be `GT̂`. B.2: `SL(2, Z)^ → Out(π̂_{1,1})` is injective (Asada); B.4: `SL(2, Z)^ → SL(2, Ẑ)` is far from injective (the quotient `SL_2(F_8)`).
- **Item 5.** D.17 (Hoshi–Mochizuki 2011, Corollary 6.4, checked by the reviewer): the image of Galois in `Out(π̂_{g,ν})` meets the geometric image trivially, for every hyperbolic type; this is faithfulness "mod" the Teichmüller group, which he doubts at 140-2 scan 504. D.19: the centralizer of the Galois image for the tripod is `𝔖_3`. D.10 (conditional on the unrefereed OpenAI manuscript 019): a section of `π_1(Y_1(N)) → G_Q`, `X_1(N)` of genus at least 2, becomes the section of a rational cusp in `π_1(X_1(N))`.
- **The rational chain.** E.19–E.21, E.26–E.28: as in "Recent results" above; LM3 followed §§2–5 of manuscript 008 without certifying them, found that the attached Lean file is a statement ending in `sorry` (it is a comparator statement, as said above), and reports a later preprint with another proof (Willwacher, arXiv:2610.15592v4; attached under `papers/willwacher_2026/`; not read by the author of this prompt).
- **A computation of the review** (by the author of this prompt; exact dimensions by program, `LM3_review/checks_author/`; read by no one else: recompute). For the free Lie algebra on `x`, `y`, `z = −x−y`, a special derivation of degree `n` is `D(x) = [a, x]`, `D(y) = [b, y]`, `D(z) = [c, z]`. Modulo inner derivations they have dimensions 0, 0, 1, 0, 3, 0, 6, 4 in weights 1 to 8, and their `𝔖_3`-invariants 0, 0, 1, 0, 1, 0, 2, 1. If the invariants are the graded form of relations (I), (II) (not checked), this answers part of ask 1 of "Recent results": the solution space of (1.2)–(1.3) alone would exceed `d_n` first in weight 7 (2 against 1). Every special derivation over `Z_ℓ` lifts to an automorphism of the free pro-ℓ group sending `x`, `y`, `z` to conjugates of themselves (successive approximation), so in the pro-ℓ group there are loop-preserving automorphisms that do not commute with `𝔖_3` (weight 5).
- Lead 1 stands in the sharpened form; Leads 2 and 3 are not settled.
""",
after_bis=BIS_STATUS + r"""

- **What a graded form cannot see (Parts B, E; ask 3 (c) of "Recent results").** BISITE B.11 (`BISITE_return/sections/B.tex`): the endomorphism `x ↦ x`, `y ↦ y[x, y]` of the free group of rank 2 is the identity on the abelianization and carries the transitive action `x ↦ (12)`, `y ↦ (13)` on three letters to an intransitive one. A lead of the reviewer, unverified: by Stallings's theorem it induces an isomorphism on every nilpotent quotient and on the pro-ℓ and pro-unipotent completions. If so, it is an explicit map that every graded or pro-unipotent linearization treats as an automorphism and that changes a covering of `P¹ − {0, 1, ∞}` of degree 3. His conditions stated through finite quotients (`𝔖_3`, `SL(2, Z/n)`) are of the kind such a map can violate.
- Nothing else in the seven returns bears on this prompt.
""",
parts="## Parts\n\n" + PREAMBLE.format(cases="a finite level: `SL(2, Z/n)` for `n` dividing 24; the pro-ℓ quotient; the graded Lie algebra in low weight") + r"""

**A. Dictionary.** (a) One table for §§38–47 and the summary §46: each of his groups (`S_{0,3}`, `S⁺_{0,3}`, `M̃_{0,3}`, `Ñ_{0,3}`, `Ñ^!_{0,3}`, `M̃^!_{0,3}(q)`, `Ñ_{1,1}`, the double-tilde groups), his elements `ρ, σ, τ, ε_i, l_0, l_1, l_∞, ξ, η, ζ, α, β`, with definition, scan, and present-day name. The second-pass corrections for these pages (attached list) change several formulas: use the corrected text and flag every formula whose form still depends on an open reading. (b) Prove the identifications the table rests on: `M_{1,1}[2] ≅ U_{0,3} = M^!_{0,4}` through Legendre, with the groups on both sides; `π_{0,3} ≅ S⁺_{0,3}`; the "avatars" of §42. (c) Identify each of his groups with one of the three groups of "After LM3" or with an extension of one, by a proof from his definitions: in particular decide whether `M̃_{0,3}` is `GT̂_0`, a group containing it, or an extension. (d) Check every formula of the table by program in the finite quotients `SL(2, Z/n)`, `n = 2, 3, 4, 6, 12`, and in `𝔖_3`; for each formula with alternatives, test each and report which holds, with the scan.

**B. The equations (items 2, 4; Lead 1).** (a) Derive the full system of conditions he obtains on `(λ, f)`: the "équation des lacets" in each of its forms, the cocycle conditions under `ρ` and `σ_∞`, the three fundamental cases with the lifts `K_{1/2}`, `K_2`, `K_{−1}`, each from the definitions, correcting slips. (b) Prove Lead 1 in the sharpened form: derive each of his conditions from Drinfeld's relations (I) and (II), and conversely derive (I) and (II) from his system, with the explicit change of variables between his unknowns and `f`; conclude that his group of solutions is `GT̂_0` (Harbater–Schneps, Main Theorem (a)), or give the exact difference. (c) Prove that the "mise en équations" in `SL(2, Ẑ)` is equivalent to the system on `π̂_{0,3}`, or determine what is lost in passing through `F̂_2 → SL(2, Ẑ)` (LM3 B.4: the map is not injective). (d) Carry out asks 1 and 2 of "Recent results"; verify or correct the dimensions of the review (0, 0, 1, 0, 1, 0, 2, 1 for the invariants in weights 1 to 8) and the identification they rest on, and extend them through weight 12. (e) Item 2: write a program that computes all solutions of his system (and of (I), (II), and of (I), (II), (III)) in the finite quotients of `F̂_2` given by `SL(2, Z/n)`, `n` dividing 24, by `𝔖_3`, `𝔖_4`, `A_5` and `PSL_2(F_7)`, together with the image of `Gal(Q̄/Q)` there (through the fields of definition of the corresponding coverings); tabulate, for each quotient, the number of solutions against the size of the Galois image, and give the first quotient in which a non-arithmetic solution appears, or prove that there is none in the range. (f) Prove what is known about explicit elements: complex conjugation is `(−1, 1)`; determine the elements of finite order of his group in the pro-ℓ quotients and in the finite quotients of (e) (compare Lochak–Schneps on torsion in `GT̂`; resolve by title), and decide whether his "seulement deux solutions explicites" can be improved: construct an explicit element of `GT̂_0` that is not in `GT̂`, in the pro-ℓ group by lifting a graded solution of weight 7 if the review's count holds, or prove an obstruction.

**C. Congruences and `SL(2, Ẑ)` (items 1, 3, 5).** (a) Compute the image of his group, of `GT̂_0`, of `GT̂` and of Galois in the automorphisms of `SL(2, Z)^` and of its congruence quotients of levels 2, 3, 4, 5, 6, 7, 8, 12, by program. (b) For each congruence property of §39 and of the "kyrielle" of scan 57 decide: it follows from the profinite algebra (give the derivation from (I), (II)); or it holds for Galois and fails for some solution at a finite level (give the level and the solution, from the program of B (e)); or it needs the pentagon. (c) Prove the sign statements by class field theory: `ε' = +1` if and only if `p ≡ 1 (4)` (scan 155), and each of the others, with the quadratic characters named. (d) Determine the "groupe adélique" of triples satisfying the loop relation (scans 204–205): compute it as a subgroup of a product over the primes, and its relation to the adelic points of the group scheme of §48 (package LM1_GROUP_SCHEMES). (e) The characterization of `Γ_Q` in `Γ̃` that he cannot propose (scans 170, 178, 185): derive from Pop's theorem and from Hoshi–Mochizuki–Tsujimura 2025 (LM3 E.15, E.16; theorem numbers) what such a characterization is in his notation, and say which data beyond his two types it uses. (f) §36: derive from LM3 D.17 the faithfulness of the arithmetic action on `𝒯̂⁺_{1,1} ≅ SL(2, Z)^`, saying exactly modulo what, and decide the stronger statement: is `Gal(Q̄/Q) → Out(SL(2, Z)^)` injective, and what is its centralizer (use Minamide–Nakamura and the results on `Out(B̂_3)`; theorem numbers). (g) The lifts through `±1` compatible with `Γ`: classify them (an `H¹` with coefficients `±1`), by a proof. (h) The anabelian converse of scan 523: prove it, or reduce it to a section statement for `M_{1,1}` or for the curves `Y_1(N)` (LM3 D.10) and prove the reduction; decide whether the rigidification he doubts at scan 524 exists.

**D. Splittings (item 4).** (a) State the extension `M̃^!_{0,3}` and the conjectured unique splitting exactly. (b) Prove or refute existence and uniqueness: compute the splittings at the finite levels of B (e) by program, and in the pro-ℓ quotient through the cohomology of the graded pieces; if uniqueness fails at a finite level, give the two splittings; if it holds in the range, prove it or state the obstruction class. (c) The torus condition (scan 209): `c² + cd + d²` and `c² − cd + d²` are the two norm forms of `Z[ζ_3]` in the bases `(1, ζ_3)` and `(1, ζ_6)`; decide which the mathematics requires from the matrix of `ρ` in his coordinates, verify by program at levels 2, 3, 4, and report it as evidence for the reading.

**E. What is new.** List every condition of §§38–47 that you could not derive from the known relations of `GT̂`. For each: a proof that it holds on `Gal(Q̄/Q)`; then a decision whether it holds on `GT̂`, and on `GT̂_0`: a derivation, or a solution at a finite level that violates it (from the program of B (e), with the level and the solution printed), or, if neither closes, the exact open statement with the smallest level at which it is undecided. Sort the list as in ask 3 of "Recent results" ((a), (b), (c)); for the conditions with no graded form use the finite-level test, and prove or refute the lead of "After BISITE". This list is the main result: it is to be as long as his text allows, and no entry may read "open" without the attack recorded.
""")

# ---------------------------------------------------------------------------------- prompts
def parts_of(text):
    a = text.index("\n## Parts\n"); b = text.index("\n---\n", a); return text[a+1:b]
def count(s): return len(re.findall(r"\S+", s)), len(re.findall(VERBS, s, flags=re.I))
common = rd(os.path.join(STACK, "_COMMON_BLOCK.md"))
rows = []
OUTW = {}
for name, spec in P.items():
    wd = os.path.join(HERE, name); up = os.path.join(STACK, name)
    bak = os.path.join(wd, "PROMPT_before_push_20261111.md")
    if not os.path.exists(bak): shutil.copyfile(os.path.join(up, "PROMPT.md"), bak)
    old = rd(bak); new = old
    a = new.index("## What is to be settled"); b = new.index("## Leads")
    head = new[a:b].split("\n"); seen = set()
    for i, line in enumerate(head):
        for k, v in spec["items"].items():
            if line.startswith(k + ". "): head[i] = line.rstrip() + " " + v; seen.add(k)
    assert seen == set(spec["items"]), (name, seen)
    new = new[:a] + "\n".join(head) + new[b:]
    OUT = outcome(name, len(spec["items"]), spec.get("outcome_extra", "")); OUTW[name] = words(OUT)
    pa = new.index("\n## Parts\n"); pb = new.index("\n---\n", pa)
    block = ("## After LM3 (added 11 November 2026)\n\n" + spec["after_lm3"].strip() + "\n\n"
             "## After BISITE and the seven Dérivateurs returns (added 11 November 2026)\n\n" + spec["after_bis"].strip() + "\n\n" + OUT + "\n" + spec["parts"].strip() + "\n")
    new = new[:pa+1] + block + "\n---\n\n" + common          # today's common block replaces the old one
    wr(os.path.join(wd, "PROMPT.md"), new); wr(os.path.join(up, "PROMPT.md"), new)
    rows.append((name, count(parts_of(old)), count(parts_of(new)),
                 count(old[old.index("## What is to be settled"):old.index("## Leads")]), count(new[new.index("## What is to be settled"):new.index("## Leads")]),
                 count(spec["after_lm3"])[0], count(spec["after_bis"])[0], count(old)[0], count(new)[0]))

# ---------------------------------------------------------------------------------- zips
def galois_c():
    out = []
    for p in sorted(glob.glob(os.path.join(GAL, "sections", "*.tex"))):
        if "C.13" in rd(p) or os.path.basename(p).startswith("C"): out.append(p)
    return out
EXTRA = {
 "LM1_GROUP_SCHEMES": [],
 "LM2_LOOP_EQUATIONS": [
   ("papers/harbater_schneps/harbater_schneps.pdf", os.path.join(LM3DL, "harbater_schneps", "harbater_schneps.pdf"), "as in the LM3 zip"),
   ("papers/hoshi_mochizuki_nodally/Hoshi_Mochizuki_nodally_nondegenerate.pdf", os.path.join(LM3DL, "hoshi_mochizuki_nodally", "Hoshi_Mochizuki_nodally_nondegenerate.pdf"), "as in the LM3 zip"),
   ("papers/minamide_nakamura/Minamide_Nakamura_1904.06749v2.pdf", os.path.join(LM3BDL, "minamide_nakamura", "Minamide_Nakamura_1904.06749v2.pdf"), "https://arxiv.org/pdf/1904.06749v2, downloaded 11 Nov 2026; first page checked; not read"),
   ("papers/hoshi_mochizuki_tsujimura/HMT_Combinatorial_absolute_Galois_groups.pdf", os.path.join(LM3BDL, "hoshi_mochizuki_tsujimura", "HMT_Combinatorial_absolute_Galois_groups.pdf"), "kurims.kyoto-u.ac.jp/~motizuki, downloaded 11 Nov 2026; first page checked; not read"),
   ("papers/pop_IOM/Pop_Finite_tripod_variants_IOM.pdf", os.path.join(LM3DL, "pop_IOM", "Pop_Finite_tripod_variants_IOM.pdf"), "as in the LM3 zip"),
   ("papers/willwacher_2026/Willwacher_2610.15592v4.pdf", os.path.join(LM3BDL, "willwacher_2026", "Willwacher_2610.15592v4.pdf"), "https://arxiv.org/pdf/2610.15592v4, downloaded 11 Nov 2026; first page checked; not read"),
 ],
}
zrows = []
for name in P:
    wd = os.path.join(HERE, name); up = os.path.join(STACK, name)
    cur = os.path.join(up, name + "_background.zip")
    n = 1
    while os.path.exists(os.path.join(wd, "%s_background_v%d.zip" % (name, n))): n += 1
    prev = os.path.join(wd, "%s_background_v%d.zip" % (name, n - 1)) if n > 1 else None
    marker = os.path.join(wd, ".rebuilt_20261111")
    if not os.path.exists(marker):                     # first run: move the pre-rewrite zip to the work tree
        shutil.move(cur, os.path.join(wd, "%s_background_v%d.zip" % (name, n))); src_zip = os.path.join(wd, "%s_background_v%d.zip" % (name, n))
        shutil.copyfile(os.path.join(wd, "MANIFEST.tsv"), os.path.join(wd, "MANIFEST_v%d.tsv" % n))
        open(marker, "w").write("v%d\n" % n)
    else:
        v = open(marker).read().strip(); src_zip = os.path.join(wd, "%s_background_%s.zip" % (name, v))
    v = open(marker).read().strip()
    oldman = {}
    for r in csv.reader(io.open(os.path.join(wd, "MANIFEST_%s.tsv" % v), encoding="utf-8"), delimiter="\t"):
        if r and not r[0].startswith("#") and r[0] != "path_in_zip" and len(r) >= 2: oldman[r[0]] = r
    files = []
    z = zipfile.ZipFile(src_zip)
    for nm in z.namelist():
        if nm.endswith("/") or nm == "MANIFEST.tsv": continue
        r = oldman.get(nm)
        files.append((nm, r[1] if r else os.path.basename(src_zip), z.read(nm), ((r[4] if r and len(r) > 4 else "") + " [from the previous zip, %s]" % v).strip()))
    def add(zp, src, note): files.append((zp, src, open(src, "rb").read(), note))
    NR = "LM3 answer; AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 11 Nov 2026"
    for f in sorted(os.listdir(RET)):
        if os.path.isfile(os.path.join(RET, f)): add("LM3_return/" + f, os.path.join(RET, f), NR)
    for f in sorted(os.listdir(os.path.join(RET, "sections"))): add("LM3_return/sections/" + f, os.path.join(RET, "sections", f), NR)
    add("LM3_review/REVIEW_author.md", os.path.join(REV, "REVIEW_author.md"), "review by Claude (Fable 5.2, Anthropic), 11 Nov 2026")
    for f in ("check_lm3.py", "check_lm3.out"): add("LM3_review/checks_author/" + f, os.path.join(REV, "checks_author", f), "the reviewer's own program and output (Claude)")
    NB = "BISITE answer (Dérivateurs series); AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)"
    for f in ("BISITE_report.md", "BISITE_results.csv", "BISITE_paper.pdf"): add("BISITE_return/" + f, os.path.join(BIS, f), NB)
    for f in ("00_conventions.tex", "B.tex"): add("BISITE_return/sections/" + f, os.path.join(BIS, "sections", f), NB)
    for f in ("REVIEW_author.md", "COMBINED_REVIEW.md", "FOLLOW_UPS.md"): add("BISITE_review/" + f, os.path.join(BISR, f), "review of BISITE and of the seven returns together, by Claude (Fable 5.2, Anthropic), 11 Nov 2026")
    if name == "LM1_GROUP_SCHEMES":
        for f in ("GALOIS_report.md", "GALOIS_results.csv"): add("GALOIS_return/" + f, os.path.join(GAL, f), "GALOIS answer (Dérivateurs series); AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)")
        for p in galois_c(): add("GALOIS_return/sections/" + os.path.basename(p), p, "GALOIS answer, Part C; AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode)")
    have = {f[0] for f in files}
    for zp, src, note in EXTRA[name]:
        if zp not in have: add(zp, src, note)
    names = [f[0] for f in files]; assert len(names) == len(set(names)), name
    body = "path_in_zip\tsource_path_or_url\tsha256\tbytes\tnote\n" + "".join("\t".join([a, b, sha(c), str(len(c)), d]) + "\n" for a, b, c, d in files)
    with zipfile.ZipFile(cur, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        out.writestr("MANIFEST.tsv", "# MANIFEST of %s_background.zip (%d files besides this one)\n" % (name, len(files)) + body)
        for a, b, c, d in files: out.writestr(a, c)
    zb = open(cur, "rb").read(); t = zipfile.ZipFile(cur); assert t.testzip() is None
    wr(os.path.join(wd, "MANIFEST.tsv"), "# MANIFEST of %s_background.zip (%d files with MANIFEST.tsv, %d bytes zipped), rebuilt 11 Nov 2026 after the push rewrite; previous: %s_background_%s.zip, MANIFEST_%s.tsv\n# zip SHA-256: %s\n" % (name, len(files) + 1, len(zb), name, v, v, sha(zb)) + body)
    tops = sorted({x.split("/")[0] for x in t.namelist()})
    prompt = rd(os.path.join(up, "PROMPT.md"))
    named = sorted(set(re.findall(r"`((?:[A-Za-z0-9_\-]+/)+)[^`]*`", prompt)))
    missing = [d for d in named if not any(x.startswith(d) for x in t.namelist())]
    zrows.append((name, len(t.namelist()), len(zb), v, len(files) - (len(z.namelist())), missing, sorted(os.listdir(up))))
    print(name, "zip:", len(t.namelist()), "files,", len(zb), "bytes; previous kept as", v, "; tops:", tops)
    print("   paths named in PROMPT and absent from the zip:", missing, "; upload folder:", sorted(os.listdir(up)))

# ---------------------------------------------------------------------------------- record
rp = os.path.join(HERE, "PUSH_REWRITE_RECORD_20261111.md"); rec = rd(rp)
M = "## LM1 and LM2 (added 11 November 2026, about 14:40 UTC)"
if M in rec: rec = rec[:rec.index(M)].rstrip() + "\n"
out = [rec.rstrip(), "", M, "",
 "The user corrected the record: LM1_GROUP_SCHEMES and LM2_LOOP_EQUATIONS had not been sent. Both were rewritten by `lm12_push_20261111.py` in the same way (demands on the items; \"After LM3\"; \"After BISITE and the seven Dérivateurs returns\"; new Parts), their shared rules were replaced by today's `_COMMON_BLOCK.md` (rules 9–10), and both zips were rebuilt. Before-copies: `<name>/PROMPT_before_push_20261111.md`; previous zips and manifests: `<name>/<name>_background_v1.zip`, `MANIFEST_v1.tsv`.",
 "", "| Prompt | Parts words before | verbs before | Parts words after | verbs after | Items words before → after | Items verbs before → after | After LM3 words | After BISITE words | Prompt words before → after |", "|---|---|---|---|---|---|---|---|---|---|"]
for r in rows: out.append(f"| {r[0]} | {r[1][0]} | {r[1][1]} | {r[2][0]} | {r[2][1]} | {r[3][0]} → {r[4][0]} | {r[3][1]} → {r[4][1]} | {r[5]} | {r[6]} | {r[7]} → {r[8]} |")
out += ["", "| Zip | files | bytes | previous kept as | files added | paths named in the prompt and absent |", "|---|---|---|---|---|---|"]
for r in zrows: out.append(f"| {r[0]}_background.zip | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {', '.join(r[5]) or 'none'} |")
out += ["", "Both prompts have the section \"What the outcome must be\" (rule 0) before the Parts: " + "; ".join("%s %d words" % kv for kv in OUTW.items()) + ". Rebuilt about 18:45 UTC."]
out.append("")
wr(rp, "\n".join(out)); sys.stdout.reconfigure(encoding="utf-8"); print("\n".join(out[-9:]))
