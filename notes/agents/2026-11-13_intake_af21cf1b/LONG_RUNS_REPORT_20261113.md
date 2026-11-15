# What the three long Pro runs did (13 November 2026)

Written by Claude Fable 5.2 at effort high, 13 November 2026, 23:30 UTC. The three runs are GPT-6 Astra (ChatGPT Pro
mode). Everything a run states is that model's claim; who has read what is said once, in the last section.

Sources: the newest registers (`answers\LM7_FERMAT_TOWER_20261113T2216Z_unzipped`, 220 statements;
`answers\LM4_FINITE_GROUP_ACTIONS_20261113T2230Z_unzipped`, 264 statements;
`answers\LM8_LIE_APPROXIMATIONS_checkpoint_16_20261113T1145Z_unzipped`, 167 statements), the three prompts, LM8's
saved trace, the E.102 folder, and the earlier files of this folder (`LATE_WORK_VALUE_20261113.md`,
`INTAKE_LM7_CONTINUED.md`, `INTAKE_LM8.md`, `INTAKE_20261113_EVENING.md`) and the review
`pro_reviews_max_20261112\LM7\REVIEW_author.md`. The register counts are one lower than the 221 and 263 of the brief
(a header line), and LM4 has two more rows since.

**In short.** Each run answered its prompt in its first hours: the manuscript's statements proved, or refuted with the
true statement beside them. After that each run stayed on its three open items and produced, hour after hour, exact
computations on one route. Those late rows are a mixture: a few theorems that are among the best of each return, a
number of counterexamples that close false routes, and a long tail of computed cases. The tail is where the stamp
question bites, and the E.102 formula shows what to do with it.

---

## 1. LM7_FERMAT_TOWER (§51, the Fermat tower)

### What the prompt asked

§51 of the Longue Marche takes the quotient of `GL(2, Z)` by the commutator subgroup of the free group `Π_0` of
level 2 and looks at what the metabelian quotient of `π̂_{0,3}` sees: the tower of Fermat curves. The prompt asked
for five things: (A) the dictionary of his groups and schemes, with every exact sequence proved, and where 12, 32 and
`GL(2, Z/12)` come from; (B) the identification with the Fermat tower, the freeness statement he struck out, and the
splitting he "n'aurait certes pas suspecté" (scan 136); (C) the motives behind it; (D) the Galois action: his
homomorphism to an extension of `Ẑ*` by `Ẑ`, the Kummer maps, their images and independence; (E) the next
approximations after his "approximation minima", with their splittings.

### What the run did, in order

**The first 2.8 hours: 103 statements, the whole prompt.** This is the part that was reviewed.

- *Part A (19 rows).* The level 12 and the order 32 are explained (A.3): modulo 12 the normal closure of
  `λ_1λ_0^{-1}` is `V_4 × Q_8`, of order 32, and a power `T^m` lies in it only when 12 divides `m`. His ring scheme
  and its unit sequence are proved over every base (A.5, A.8). Three of his formulas are wrong as written and are
  replaced (A.6, A.9, A.13); A.13 says the literal definition (171) has half the stated image.
- *Part B (14 rows).* `F'/F''` is free of rank one over `Z[Z²]` on the commutator (B.4), and the same holds
  profinitely over `Ẑ[[Ẑ²]]` (B.8). The integral homology of the affine Fermat curve is the Fox kernel, of rank
  `n² + 1` (B.5). The freeness he struck out is indeed false: the diagonal of `μ_n³` acts trivially; the quotient
  `μ_n³/μ_n` acts freely on the curve minus its cusps (B.3). The splitting of scan 136 is proved: the extension class
  vanishes, integrally and at every level dividing 24 (B.11–B.13).
- *Part C (8 rows).* The lead that identified his object with the full generalized Jacobian is refuted (C.2, C.8):
  his text constructs the rank-two toric tower. The extension class of the generalized Jacobian has exact order `n`
  (C.5).
- *Part D, first 26 rows.* The Kummer homomorphism is identified, its joint images computed, independence for
  distinct primes proved (D.1–D.4), with two corrections to the manuscript (D.3). The table of special derivations
  through weight 10 (D.11) is where the first open item comes from: the group of loop-preserving outer automorphisms
  of the pro-`ℓ` free group is larger than the Galois image in weight 5, and the `S_3`-invariant part is larger in
  weight 9. D.16: the Galois image at the two CM points satisfies one extra quadratic relation, through the field
  `Q(i, 3^{1/4})`.
- *Part E, first 36 rows.* The comparison of approximations (abelian, metabelian, nilpotent, pro-`p`, unipotent) as
  localizers (E.5–E.10). Then sections. E.18: the Fermat quartic `U_4` over `Q` has no section at all, already for
  the abelianized group. E.17: the rank-two quotient of his (373) does not separate two rational cusps. E.32: for the
  cubic, a class-two section fibre is non-empty exactly when explicit central corrections are integral and tend to
  zero; one explicit pair passes every finite-coefficient test and fails the continuous one. E.34: every abelian
  pro-3 section unramified outside 3 lifts to a full pro-3 section; the group of those is `Z_3^6 ⊕ (Z/3)^3`.

**Hours 2.8 to 14 (to 13:44 UTC): 75 statements, all on two of the three open items.**

- *On E.23* (52 rows). E.37 gives the whole section map of the class-two quotient: which abelian classes lift, and
  every fibre. E.38 and E.43 show class two does not select: for a set of primes of density 1/9 there are classes
  with class-two sections and none one layer up. E.41 gives every section unramified outside 3 of the full pro-3
  group, its metabelian and its marked quotient; their free ranks (6, 24, 166, …) are far above the rank one of a
  cuspidal packet. E.44 is the lifting criterion at every layer. E.61 and E.66: at a place not above 3, a ramified
  local section is one of nine cusp families. E.73: a global section is a family of local packets tied together by
  Frobenius words. The other forty rows compute fibres of one inherited quotient `H` over particular first classes
  (`3κ(3)`, `3κ(2)`, `3κ(17)`) through norm-coherent units in the towers `Q(a^{1/3^n})`, with the class groups of
  those fields.
- *On D.19, the CM coset* (23 rows). D.27 corrects the run's own early row: the twelve "extra" finite shadows of
  D.25 are not genuine. D.28–D.44 follow one replacement action through larger and larger quotients; D.45 proves
  that this recorded action has no full profinite lift. D.40–D.44 show where an obstruction cannot sit: over every
  base whose even part is non-abelian simple the image is the full fibre product. D.46–D.49 change the question: the
  automorphism "a Galois commutator on the 2-primary part, the identity on the odd parts" exists on every quotient
  that is a fibre product of pro-`p` pieces, and it has the CM pair in the coset Galois misses. So no quotient of
  that kind can decide the question; a deciding quotient must mix a 2-layer with an odd layer.

**After hour 14 (13:44 to 22:16 UTC): 42 more statements.** The run could not be stopped and kept returning files.

- D.50–D.62 (13 rows) lift the D.46 candidate through one more layer after another of an arithmetic source `G_3`.
  Each row kills some central blocks and reports what is left: a residual of dimension 353,792, then 331,776, then
  325,120 (D.60–D.62).
- E.90–E.118 (29 rows). The cubic: the complete global localization images (E.92, E.93), all sections unramified
  outside `{2,3}` and `{3,7}` (E.98–E.100), the two-prime families (E.104), the degree-four kernel
  `Z_3^504 ⊕ C_3^144 ⊕ C_9^56 ⊕ C_27^30 ⊕ C_81^9` (E.102). Field towers: all 3-class groups of
  `Q(ζ_3, 17^{1/3^d})` vanish at every level, and the same for every inert prime `ℓ ≡ 2, 5 (9)` (E.107, E.110,
  E.111, E.114, E.116). The plus Fermat quartic (elliptic factor `y² = x³ + x`): its abelian sections and class-two images at 3 and at 5,
  complete (E.103, E.105, E.108, E.112, E.113, E.115, E.117), and E.109: the pro-5 class-two outer action is carried
  by a rank-two CM module and its class restricts over `Q(ζ_8)` to the Abel–Jacobi class of the Ceresa cycle.

### What stayed open

- **D.13.** Does the image of the full profinite loop-preserving group in weight 5 have dimension 3 (the pro-`ℓ`
  value) or less, and does the full profinite `GT_0` reach the second vector `X²Y²(X+Y)³` in weight 9? No row of
  this run attacks it. The other run LM7_PUSH claims both, positively, at its checkpoint 08 (D.1, D.2, through its
  lifting theorem D.50); that claim is unchecked (see `INTAKE_20261113_EVENING.md`).
- **D.19.** The same two questions, and whether an element of the full `GT_0` has its CM pair in the coset Galois
  misses. State: twelve shadows removed (D.27), three recorded actions excluded (D.30, D.32, D.45), one candidate
  alive on every prime-separated quotient (D.46–D.49) and through the layers of D.50–D.62, residual dimension
  325,120 with 534 coinvariants. LM7_PUSH E.2 claims a positive answer for `GT_0` (unchecked) and leaves the full
  `GT` open.
- **E.23.** All section classes of the metabelian and marked depth-two quotients of `U_3/Q`. Settled: class two,
  completely (E.37, E.93, E.96); every section with ramification in `{3}`, `{2,3}`, `{3,7}` and the two-prime
  families; the local side at good places. Open: the image of the class-three map `N/γ_4 → N/γ_3` for general
  ramified inputs, the global metabelian and marked preimages, the other coefficient primes.

### Where the hours went

2.8 hours for 103 statements (37 an hour); the next 11.4 hours for 75 (6.6 an hour); the last 8.5 hours for 42
(5 an hour). All 117 late rows are on D.19 and E.23: 36 on the CM coset, 81 on sections. Of the first 75 late rows about four in
ten are theorems or lemmas with a use and six in ten are computations along one route (the Longue Marche expert's
count, Claude Fable 5.2 at effort max). The last 42 have not been sorted that way; their 13 D rows are all of the
computing kind.

### What it means

§51 is answered: his dictionary holds with three corrected formulas, his struck-out freeness is false, his surprise
splitting is real, the Fermat tower is exactly the metabelian quotient, and the Galois action on it is the known
Kummer and Soulé data. Beyond §51 the run found three things he did not have. First, a continuous obstruction that
no finite level sees (E.32), now a criterion at every layer (E.37, E.44). Second, the pro-3 sections of the Fermat
cubic minus its flexes are far more numerous than the cuspidal ones (E.41), while locally, away from 3, every
ramified section is cuspidal (E.61, E.66). Third, the CM coset question is a question about mixing primes
(D.46–D.49).

---

## 2. LM4_FINITE_GROUP_ACTIONS (§§12–18, 23–25 bis, 31)

### What the prompt asked

Grothendieck's "groupes extérieurs à lacets" and a finite group acting on a surface or on its group. Seven items:
(1) the rigidity statements (trivial centralizers, normalizers of loop groups), discrete and profinite; (2) sections
against fixed points, "Cette application est-elle bijective ??", the "lemme fondamental" of §18, the theorem "Ultra
fort!"; (3) the invariant `μ`; (4) his questions c), d), e); (5) his conjecture that the passage from topological
actions to group data is an equivalence of 2-categories, and the realization criterion by drilling holes; (6) the
profinite theory: is a torsion-free extension of a finite group by a group with loops again one, and are lifts into
the discrete group and into its completion the same ("J'ai envie de conjecturer sans vergogne"); (7) §25.

### What the run did

**The first 8.9 hours: 189 statements.**

- *Part A (20 rows).* Discrete rigidity in every hyperbolic type (A.3) and the table of exceptional types (A.4). The
  full profinite statements are known (A.7). New here are the solvable quotients: for every finite-step solvable
  quotient, centre, torsion and open centralizers are trivial (A.17, A.18), with the exact threshold for one
  puncture (A.16).
- *Part B (40 rows).* Fixed points are section classes (B.3); for a reflection, ovals are section classes, and the
  group data recover the incidence and cyclic order of real punctures (B.4, B.5). The "lemme fondamental" of §18
  holds (B.6). Six of his statements fail and get their true form: `π^G = 1` for every finite `G` (B.7), unique
  maximal sections (B.8, false for reflections already in type (0,3)), the roots lemma he himself marked "faux!"
  (B.10), the torsion of a centralizer (B.11), the "only counterexample" of scan 179 (B.15), presentation (52)
  (B.20). The multiplier `μ` has an intrinsic formula on the group with loops (B.12), and forgetting the loops loses
  it (B.13). Then the census: every conjugacy class of finite subgroups of the extended mapping class group for
  `2g + ν ≤ 6`, and large parts of genus three (B.23–B.41): 16 types, 882 subgroup classes, 889 realization rows,
  each with its section counts.
- *Part C, first 53 rows.* His conjecture as literally stated fails: the target has too many arrows (C.1). With the
  corrected target it is true for finite groups on hyperbolic surfaces: all four levels of fidelity hold and the
  comparison is a biequivalence (C.8), from existence, uniqueness up to the identity component, and contractible
  centralizers (C.5–C.7). The drilling bijection and the realization criterion of scan 294 hold for faithful
  orientation-preserving actions (C.15, C.18) and fail without faithfulness (C.16). For infinite groups the
  comparison fails at levels one and two (C.11) and existence fails for the whole mapping class group (C.23). What
  is left is level zero for an infinite group: C.12.
- *Part D, first 58 rows.* Completion keeps finite subgroups and their conjugacy (D.2), and lifts into the discrete
  group and into its completion are the same (D.3): his shameless conjecture is a theorem. The recognition question
  splits. Pro-`p`: a torsion-free extension is again a surface pair (D.18–D.20). With an invariant discretization:
  the same (D.17). Full profinite, no discretization: false, with a four-puncture example that even preserves a
  peripheral structure (D.29) and a closed genus-two example (D.30). Then the full profinite three-cusp group:
  every finite subgroup of the pure group has order at most two (D.32), every involution has the global sign `−1`
  (D.34), every element of order three has multiplier 1 (D.42). The punctured torus: nine finite types (D.55),
  detected on homology (D.33).
- *Parts E and F.* §25 as a construction (E.1–E.3) with the case where his kernel formula fails (E.4); the three
  lemmas the later sections use (F.1–F.6).

**Hours 8.9 to 20 (11:26 to 22:30 UTC): 75 statements, all on the three open items.** C.54–C.91 (38 rows): the
level-zero question for a loop of plane homeomorphisms commuting with an operator group, case by case on the type of
orbit and of operator group. D.59–D.78 (20 rows): negative involutions of the punctured torus and the sections of a
pants involution, ending with D.70 (order four has multiplier 1) and D.77 (three section representatives that
generate a proper subgroup although every pro-`p` image is full). F.10–F.26 (17 rows): the icosahedral group acting
on its twelve vertices.

### What stayed open

- **C.12.** An infinite operator group whose level-zero comparison has a kernel, or a proof that there is none; the
  kernel is `π_1` of the centralizer in the identity component. Settled: operator groups with a dense orbit (C.41),
  loops with locally compact closure (C.40) or commuting values (C.39), one-dimensional proper operator groups on
  the disk (C.79, C.80), cocompact discrete operator groups (C.90, and C.91: the whole centralizer is contractible).
  Four routes are closed by explicit counterexamples (C.35, C.72, C.74, C.83). Open: discrete operator groups with
  non-compact quotient, and general frontiers.
- **D.12.** Is every torsion element of the full profinite `GT_0` conjugate to complex conjugation `(−1, 1)`, and
  the recognition of finite subgroups in types (0,3) and (1,1). Proved: the orders, the multipliers, the nine torus
  types. Open: one conjugator equation at the third cusp (D.35, D.44, (D.74.40)), the conjugacy (D.75.5) for
  negative torus involutions, whether one fixed group is procyclic (D.78), and the "scalar cubic" case: an element
  of order three of the torus group whose multiplier is a primitive cube root of unity at some primes, neither
  constructed nor excluded (D.71, D.73).
- **F.7.** For a geometric `A_5` in a mapping class group of the punctured sphere, is the centralizer in the
  completion the closure of the discrete centralizer? The return says the equality is stated in two published
  papers (it cites Boggi, Theorem C(iii), and its "R-BZ", Theorem 5.1(iii)) and that their proofs use a
  closure–intersection equality it could not justify. It claims no counterexample. Proved: the images in the
  puncture permutations agree; for twelve punctures the question is an explicit membership in a two-point
  configuration kernel (F.19–F.22); the two sides have the same image in every affine group over `F_p` (F.25) and
  over the field of nine elements (F.26). Open: the general case of that affine test and the full equality.

### Where the hours went

189 statements in 8.9 hours (21 an hour), then 75 in about 11 hours (7 an hour), none of which closed an open item.
The largest single block of the whole run is Part C: 91 rows, 66 of them (C.26–C.91) on C.12, the plane and the disk.

### What it means

§§12–31 are answered more fully than any other part of the Longue Marche so far. The shape of the answer: for
finite groups and discrete or pro-`p` groups his expectations hold after one correction each (orientation,
faithfulness, the right target). For the full profinite completion they split: lifts and finite subgroups behave
(D.2, D.3), recognition fails (D.29, D.30), and what replaces it is a list of exact invariants (orders, global
multipliers). The statement to remember: the multiplier of a finite-order element is a global `±1`, proved for the whole
three-cusp group (D.34, D.36, D.41, D.42) and for the 2-subgroups of the punctured-torus group (D.43, D.70); for
elements of order three of the torus group it is not yet decided.

---

## 3. LM8_LIE_APPROXIMATIONS (§§52–53)

### What the prompt asked

The last two sections of the manuscript: L-groups and whether each comes from a finite group acting on a surface;
modular multiplicities over `Q` and `Z` as quotients of curves by finite groups, with `M_{1,1}` over `Z` as the test;
Galois–Teichmüller structures and their Lie approximations, with quasi-unipotent homomorphisms and integral
one-parameter subgroups; the splittings at each approximation; §53, the special Teichmüller group of type (1,1) as
`GL(2, Z)^~`; and a Part G added on 13 November: the Galois image on the once-punctured CM curve, degree by degree.

### What the run did (order from the trace)

The run was sent at 02:04 UTC. Its last checkpoint, 16, was built about 07:10 UTC: 167 statements, 122 proved,
24 refuted, 15 known, 6 open. The trace has no clock times; its order is this.

1. *Reading.* The manuscript changes two premises of the prompt: the "limiting topos" of scans 242–243 is about
   coverings of germs, and scan 231 is about the covering group of `GL_2(Z)`; neither is a Lie-approximation tower.
2. *Parts A and B, first pass.* The approximations as localizers (B.6). Germ axioms alone do not fix an L-group
   (A.2); `PSL_2(Z)` is not characterized as he says (A.7). The tripod table of special derivations to weight 14
   (B.10). A typing error of the prompt: an absolute prounipotent completion has no finite quotient, so the
   comparison maps exist only for the relative completion (B.8, B.9).
3. *Part C.* Over `Q̄` the answer is the classification of one-dimensional stacks, with the exceptions (C.1–C.3),
   and existence descends to `Q` (C.4). Over `Z` the answer is no: `π_1^ét(M_{1,1,Z}) = 1` (C.6).
4. *Part G.* Of the three degree-four components the expert's lead expected, only one survives (G.6); the fixed
   points of the Galois image are the inertia group, at every prime (G.10); the CM eigenline lifts through `N_4` and
   stops at `N_5` (G.11).
5. *The exceptional primes.* The element `q_7` (which separates pro-`ℓ` `GT_0` from `GT`, B.12) is lifted integrally
   class by class, 11, 12, 13, 14, the last a system of 5,030 equations in 2,497 unknowns (B.14a, B.14b), and then
   the finite computations become a proof: compatible lifts exist in all degrees at 2 and 3 (B.14d).
6. *Part D.* A counterexample to his statement over every quasi-compact base (D.14, a base that is not
   quasi-separated), then the positive theorem in growing generality: discrete valuation rings, Noetherian bases,
   and finally every quasi-compact quasi-separated base (D.15–D.21).
7. *Part F.* The Selmer dimension tables through class 8, made unconditional by modular-symbol computations for two
   elliptic curves (F.16–F.18). F.15: sections of an inverse limit are the limit of the sections for compact towers,
   and not in general. F.21: the unrestricted class-two obstruction group at 5, with a class that vanishes at every
   finite level and not integrally. F.22: over `Z[1/30]` every class-two section has a `Z_5²` of class-three lifts
   and each of those 125 class-four lifts, which all become conjugate rationally.
8. *The last hour before the checkpoint.* A.22: the metabelian quotient `F̂_2/F̂_2''` has a non-inner involution with
   multiplier one that no pro-prime quotient sees; A.23–A.26 lift it through the relative pro-5 completion. B.31–B.35:
   the signed automorphisms of §49 preserve every Fermat kernel, and the whole profinite action cannot be defined
   over `Q` (a Galois multiplier acts by `√6 ∈ Z_5`, B.34).

Part E in between: `ST_{1,1} ≅ GL_2(Z)^~ = B_3 ⋊ C_2`, not central (E.3); the "?" extension of the 140-1 draft is
`B_3` over `SL_2(Z)` (E.5); three of his formulas corrected (E.4); the limit of the sheaf topoi of shrinking
punctured discs is degenerate (E.11); 1,946 marked quotients of `B_3` of order at most 1,000, with 180 finite
shadows that lift to no global element (E.14–E.16).

### The last hours

The run died about 11:45 UTC on "Message delivery timed out", some four and a half hours after checkpoint 16, with
no final answer. The trace is the only record. Its last milestone paragraph is the signed-source analysis
(B.31–B.34); its last step labels are the tangent-section proof (F.24), the `C_6` complement and finite-order lift
(A.26) and the normalizer images (B.35); its final line is a patch-and-test step, cut off. Every one of these is a
row of checkpoint 16. So the trace shows no mathematics beyond the checkpoint. Whether the run worked after it
without the trace updating cannot be told from what was saved.

### What stayed open

- **A.12:** does every profinite finite action come from a discrete one; reduced to lifting the involution of A.22
  from `F̂_2/F̂_2''` to `F̂_2`.
- **B.24d:** the conjugator images on the Fermat stages above the first.
- **B.28:** does every pentagon solution satisfy his §47 equation; reduced to computing the relative action a full
  profinite word induces.
- **F.12:** the unrestricted Fermat section sets beyond class two.
- **G.16:** one arithmetic coefficient `ν/α` of a Galois element in degree eight; the universal identities cannot
  fix it (G.23).
- **G.20:** fixed subgroups in the full profinite group; the residual cases lie in the common kernel of all pro-`ℓ`
  quotients.

### Where the hours went

About five hours of work for 167 statements (33 an hour), with a checkpoint about every twenty minutes; then four
and a half hours that left nothing. LM8 is the only one of the three that never reached the slow phase.

### What it means

§§52–53 are answered except for A.12 and B.28. Per hour this is the densest of the three returns, and its best
results are general theorems: D.21, C.6, B.14d, F.15, G.10. The follow-up prompt LM8_PUSH exists for the six open
items.

---

## 4. Stamps or structure

The question: are the very particular cases these runs found structural insight, or example farming, "collecting
stamps that no one's ever minted"? The honest answer differs by phase more than by run.

### LM7_FERMAT_TOWER

**Structural** (statements about infinite objects, with a mechanism): the freeness over `Ẑ[[Ẑ²]]` (B.8); the
splitting (B.11–B.13); the continuous obstruction and its criterion (E.32, E.37, E.44); local sections away from 3
are cuspidal (E.61, E.66); the sections unramified outside 3 (E.41); the packet description of a global section
(E.73); non-solvable bases carry no obstruction (D.40–D.44); the prime-mixing candidate (D.46–D.49); the vanishing
of class groups at every level of a tower, for whole families of primes (E.107, E.110, E.114, E.116).

**Computed examples:** the survival of one action through quotients of orders like `576 · 3^4753` (D.27–D.39); the
layers D.50–D.62 with their residual dimensions; the fibres of `H` over `3κ(3)`, `3κ(2)`, `3κ(17)`, the primes 19,
53, 73, 3121; class groups of single fields up to degree 486 (E.94); the Smith forms.

**What the examples are good for.** Three different things.

1. *They killed false leads.* D.27 removed the run's own twelve shadows; D.45 removed a candidate that had been
   carried through six rows (D.39–D.44); E.38 showed class two does not select. Each would have been a wrong sentence in a
   prompt or a companion.
2. *Some became theorems inside the run.* E.32 was a criterion for one inherited quotient, with one explicit witness; it is now the
   criterion E.37/E.44 for the intrinsic groups at every layer. The towers over 17 began as one field and ended as E.114 and E.116 for every inert prime in two
   residue classes.
3. *One was explained from outside, and that is the model case.* E.102 is a stamp if anything is:
   `Z_3^504 ⊕ C_3^144 ⊕ C_9^56 ⊕ C_27^30 ⊕ C_81^9`, the cokernel of a 990 × 990 matrix. The main session
   (Claude Opus 5.5 at effort max) recomputed it with its own code and confirmed it. Claude Fable 5.2 at effort max
   then found the law (`LM7_FERMAT_TOWER_E102_check_20261113\FORMULA.md`; 287,112 tokens, 31 minutes). The homology
   `V` of the cubic minus its nine flexes splits, as a Galois module, into a rank-four core `V_1` (the curve's own
   lattice glued to two cusp directions by the Weil pairing on 3-torsion) and six plain copies of the cyclotomic
   character with signs `(2, 4)`. The degree-four kernel `Λ²Λ²V` then falls into six pieces, and
   144, 56, 30, 9 are polynomials in those two signs: for instance `9 = 7 + 2`, the 7 even pairs of free cusp
   directions against `S²V_1` and the 2 even cusp directions against `Λ²V_1 ⊗ V_1`. The exponent 81 is a resonance
   (on the part with two factors from the curve a scalar `u ≡ 1 (3)` acts by `u^6`, trivial modulo 9) times a factor 3
   for each of two glue factors. The formula passed 28
   variation tests against direct computation. It also returns, in degrees 1, 2 and 3, exactly the groups of E.34,
   of the fibre in E.37 and of E.40 (`Z_3^166 ⊕ C_3^7 ⊕ C_9^56 ⊕ C_27^25 ⊕ C_81^3`): three more rows of the return
   reproduced by independent code. (That agreement is my observation from comparing the two files.)

   So one question, "why these numbers", turned four isolated stamps into one statement about a rank-four module,
   and it says something the return does not: the class-three step of E.23 has coefficients in four Galois modules
   of ranks 20, 16, 4 and 1, not in one of rank 330.

The rows D.50–D.62 are the opposite case so far. Each is exact, none comes with a reason why the residual should
reach zero, and the family of quotients is not cofinal. Unless someone finds their law they decide nothing.

**What one could prove next.** (a) The class-three step of E.23, with E.44 as the criterion and the four modules of
the formula as coefficients; what is missing is the Frobenius action on ramified inputs. (b) A written theorem on
pro-3 sections of the Fermat cubic: local cuspidality (E.61, E.66) against the global surplus (E.41). (c) D.13 and
D.19, if LM7_PUSH D.50 survives its check. (d) E.109 against the papers it cites (it names Bloch, Hain–Matsumoto and
Bisogno–Li–Litt–Srinivasan); I have not opened them, so I do not say whether it is new.

### LM4_FINITE_GROUP_ACTIONS

**Structural:** the corrected biequivalence (C.8) with its exact failures (C.11, C.16, C.23); sections as fixed
points and ovals (B.3–B.5); lifts and finite subgroups survive completion (D.2, D.3); recognition holds pro-`p` and
fails profinitely (D.18–D.20 against D.29, D.30); the global multipliers (D.34–D.43, D.70, with the cubic torus case open); the solvable rigidity
(A.16–A.19).

**Computed examples:** the census of finite subgroups (B.23–B.41); the finite tests in D (a quotient `A_5^19`, then
`SL_2(F_5)^19 × C_2²` with 324,000,000 pairs of which 10,125,000 survive, D.38, D.45, D.47); the twelve-puncture
icosahedral configuration (F.8–F.26).

In between sits Part C from C.26 on: sixty-six rows that settle the level-zero question for one class of operator
groups after another. Each row is a general statement about its class, so these are not stamps; but it is a case
analysis with no end in sight, and four of its routes ended in counterexamples.

**What the examples are good for.** The census is the plainest instance of the user's point: 882 classes with their
section counts could not be had by hand, and they are what his statements of §§15–18 can now be checked against, case by
case. The census is also a dataset in its own right, with one index file. The finite tests in D did what tests do: they excluded candidates and left the conjugator equation
standing. The icosahedral computation is a test case for a published statement; its value depends on how F.7 ends.

**What one could prove next.** (a) D.12: the conjugator equation at the third cusp is one equation in a free
profinite group; LM7_PUSH's device (E.58: prescribe conjugators and lift) is the tool to try. (b) F.7: either the
missing equality, which would complete the cited proofs, or a finite quotient separating the two sides, which would
be a counterexample to a published theorem; both are worth a prompt, and neither should be announced before a check
of the cited papers. (c) C.12 for a discrete group with non-compact quotient.

### LM8_LIE_APPROXIMATIONS

**Structural:** D.21 (one-parameter subgroups over every quasi-compact quasi-separated base) with its
counterexample D.14; C.6; B.6; B.14d; B.32; B.34; E.3, E.5, E.7; F.15, F.21; G.6, G.10, G.11; A.22.

**Computed examples:** the tables (B.10 to weight 14, B.16, B.18, F.2, F.9, G.14); the enumerations (24 groups of
order at most 12 in A.10; 74 groups and 9,714 epimorphisms in B.23; 1,946 braid quotients in E.14); the class-14
certificate (B.14b); the modular-symbol computations (F.16–F.18); the lifting families of the involution
(dimensions 4, 20, an affine `Z_5^90`, A.24–A.25).

**What the examples are good for.** This run shows the cycle at its shortest. The class-11 to class-14 lifts of
`q_7` were finite stamps for a few hours and then B.14d proved the statement in all degrees. The 180 fake shadows
(E.16) show that finite `GT`-shadows do not all lift, which bears on every shadow test in LM7. F.22's 125 integral
lifts that are one class rationally show that rational Selmer counts miss integral multiplicity. A.24 found that
correcting greedily fails: only one point of a four-parameter family extends.

**What one could prove next.** A.12 through A.22–A.26; G.16, which is one coefficient readable from a finite
non-metabelian quotient; B.28. These are in LM8_PUSH.

### The answer

The first hours of each run are structure: they are the manuscript's own statements, decided. The late hours are
mostly examples, and the criticism is fair for the part of them that has neither killed a lead nor found its law:
the residual dimensions of D.50–D.62, the fibre-by-fibre rows of E.46–E.97, the far end of LM4 Part C. Those are
stamps nobody minted.

But three things separate this from farming. The examples are exact and reproducible, with code, so each is a fact
that can be explained later. Several were explained within hours and became theorems (E.37, B.14d, E.116). And the
E.102 formula shows that the explaining is cheap next to the computing: half an hour of one reader against hours of
the run. The work that is missing is that second step, asked of every family of numbers the runs left: the degree
tables of E.40 and E.102 (done), the residuals of D.50–D.62, the per-prime fibres, the census counts. A run left
alone does not take that step; it computes the next case. That is also why a push prompt gets more per hour than
letting a run go on.

---

## What has been read, by whom

- LM7, first 103 statements: reviewed by Claude Fable 5.2 at effort max (88 correct, 12 known, 3 open, none wrong;
  programs not rerun, sources not opened). The next 75: intake by Claude Fable 5.2 at effort high (the effort is from
  that agent's handoff): 17 proofs read, no gap found, 58 at statement level. The last 42: statement heads only,
  by me. E.102: recomputed by Claude Opus 5.5 at effort max and again by Claude Fable 5.2 at effort max.
- LM4: no proof of any row has been read by a reviewer. The Longue Marche expert (Claude Fable 5.2 at effort max)
  sorted 19 late rows from their heads; I read all 264 statement heads and the three open statements.
- LM8: intake by Claude Fable 5.2 at effort high: 161 consistent, 6 open, none wrong; 32 proofs read or recomputed;
  programs not run. The trace was saved by Claude Opus 5.5 at effort high.
- The hours: from the snapshots' build times and the Longue Marche expert's figures. The brief's "about 14 hours"
  and "about 11.5 hours" are the state at 13:44 and 14:01 UTC; both runs were still returning files at 22:16 and
  22:30 UTC.
- Literature: nothing was opened for this report. Where a paper is named, the name is the return's.
