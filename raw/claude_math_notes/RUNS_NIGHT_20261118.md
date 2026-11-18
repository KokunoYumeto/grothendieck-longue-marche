# Notes on four long Pro runs, 18 Nov 2026 (main session, Claude Opus 5.5 at effort max)

Read from each run's newest checkpoint: its report, results table and progress ledger. All four runs are GPT-6 Astra
(ChatGPT Pro mode). These are notes on what each run says it has done. I have not re-checked its proofs; that is the
intake's job. Every run marks its report INCOMPLETE while it runs.

## S6_06_BLIND (account 2; about 34 hours; checkpoint 33, 18 Nov 10:08 UTC)

**What it is:** the blind S6 run. It re-derives and extends the S6 programme's statements from the prompt alone. It
writes one paper, now 1,271 pages with 292 numbered statements and 546 exact source locks (`S6_06_BLIND_paper.pdf`).

**Its prompt items:**
- **Parts 1, 4 and 5: done, with two corrections.**
  - The construction is fully proved: monodromies of orders 5 and 4, charts, van Kampen and Mayer–Vietoris, the full
    Hodge table, automorphisms, tangent cohomology, Chern numbers, the oriented diffeomorphism (including the
    homotopy-sphere issue), the Frobenius minimum, and the miniversal germ. Parts 4 and 5 are proved too, part 5 as
    blind proofs.
  - The first correction: the literal rank-three Hodge formula and the integral primitive identification. Global
    periods are proved, and two numerical methods agree beyond 30 digits.
- **Part 2: proved, with one refutation.**
  - Fillings and their nonexistence are proved: every admissible twist, the coprime higher families, and p = −5.
  - Item 2.3 is a refuted sign: the radial coefficient is −pn.
  - Item 2.6: the proper flat untwisted filling is proved, but the central space proposed in Conjecture 8.2 is
    refuted.
- **Items 3.1–3.3 (the invariants in Θ7 = Z/28):** done.
  - The reference fan has class 0, by two independent methods.
  - **The broader claim that every fan gives 0 is false.** Its 28 explicit fan witnesses realize all of Θ7,
    including class 3.
  - It also corrects the earlier K6 (the meridian-one class restricts to the Hermitian dual of the source line) and
    the physical-versus-descended sign convention.
- **Item 3.4 is the open core.** It computes the Z/28 classes of every family of marked loops and fans (K71–K112).
  It finds closed formulas: for example K93, I_a = 1 − a − 3(a−1)(S−1) − (2a+1)(S−1)(S−3)/4 mod 28 with
  S = x² + xy + y², with the exact image sets; K100; K111/K112, a selected-I3 return Jin(71, −4), class 12.
  - Each nonzero residue is applied as an Eells–Kuiper obstruction to a product mapping torus.
  - Certificates run into the millions of exact checks, for example 2,964,452 primary checks.
  - What remains: the other marked source-moduli generators, further singular sectors, and endpoints outside the
    completed families.

**Its own review (08:48 UTC):** CONTINUE, on the K111/K112 families and the intrinsic-base endpoint extension.

**My note: 3.4 is an enumeration with no natural end.** Each completed family is a new exact result, and the run
counts it as movement. The question for the intake is whether these families reduce the main gate or only add
cases. That's the LM4_SUCCESSOR pattern: the 17 Nov ledger rule counts only status changes or strictly smaller
gates. The comparison table against S6_04's stated values has several rows with "no complete derivation yet"
(B.6.3–B.6.8, B.6.11–B.6.16).

## DER_LOCALIZERS (sent 18 Nov about 01:54 UTC; about 9 hours; checkpoint 08, 09:54 UTC)

**What it is:** the Dérivateurs question of which localizers and derivator axioms are equivalent. It writes a
130-page paper.

**Found:**
- **A.1, refuted** (including the accessible case): the strengthened square and cube axioms are equivalent to
  reversibility. The sphere-null cofiber class satisfies every fundamental axiom. Even so, a seven-object category
  realizing RP² supplies a map in its stable closure that lies outside the class. It re-proves REVLOC's
  torsion-finite realization, using Levy's 2025 spectral Sullivan theorem.
- **A.2, settled:**
  - Either one-sided axiom forces RT-fixedness, through the stable pointed envelope (A2.9).
  - Arbitrary and locally constant coefficients are equivalent, and either one forces RT-fixedness.
  - Constant coefficients are strictly weaker in the unpointed case. A2.12 is a complete accessible counterexample:
    connective integral complexes augmented to Z pass every constant test but fail a locally constant test with
    five objects and seven arrows.
  - In the pointed case all three agree.
  - For complete and cocomplete ∞-categories, either constant half forces RT-fixedness (A2.14).
- **A.5, refuted:** the relative implication without Loc8 fails on an accessible example. Saturation needs neither
  Loc8 nor Loc9.
- **B.1, refuted:** the interval-only claim fails in both manuscript cases. The aspherical-core answer on simplicial
  sets is proved.
- **C.1, refuted in its literal form:** the literal Lemme 3 fails without normalization. The module case is proved
  over every ring, then for AB5 categories, categories with enough injectives and exact resolving functors. The
  unrestricted theorem is refuted by a three-sort monoidal counterexample (C.26).
- **D.1, refuted and repaired:** the naive condition fails. A repaired fundamental localizer and the schematization
  interpretation are proved.

**Open:**
- **A.3, existence:** it reduces to one accessible reversible closure generated by A = QΣ³V, together with a
  noncontractible A-null H-space in the same finite-free stable ideal.
- **A.4, equality:** it reduces to BC2-acyclicity of countable simply connected primary sphere-null H-spaces.
  Intermediate classes and the size question are also open.

**State:** review 6 (09:54 UTC) found no movement, its first such review. If the 10:54 review also finds none, it
writes its final package, so its final should come soon.

## SECTION_GHOSTS (sent 02:51 UTC; about 7 hours; checkpoint 07, 09:48 UTC)

**What it is:** the section-conjecture ghosts. These are sections that pass the finite, nilpotent or single-prime
tests and could fail only where the primes mix. It writes a 316-page paper.

**Found:**
- **GT ⊊ ker Δ ⊊ GT₀, with an actual full profinite witness for each strict inclusion** (E.197–E.198).
  - The automorphism-side CM obstruction, same-parameter covariance and compact finite separation are proved
    (C.3/L.5), and the exact original relative CM family is recovered (E.201).
  - This bears directly on the Longue Marche question of Δ on GT-hat (DELTA_ON_GT).
- **The literature leaves the question open:** neither the 2023 twisted Massey theorem nor the 2026 strong vanishing
  theorem (both opened) gives the retained integral ordinary section (P.14).
- **A.1:** fixed-pair integral-class survival is equivalent to full pronilpotent survival.
- **Necessary conditions on a ghost:**
  - The support of every ordinary pair has density zero (A.33), though finite support is not proved.
  - There are explicit finite point and cusp detectors (E.192–E.194).
  - A pro-three ghost section would force infinitely ramified elliptic-family representations, at least two of them
    absolutely irreducible (E.200).
- **B.1:** the first two five-primary tests reduce to one explicit 2×2 affine system over F₅ (E.202). Its matrix is
  in quintic residue logarithms, and its obstruction is a finite Heisenberg cochain over {2, 3, 5, q₀, r₀, ∞}.
- **A.196:** a nonordinary cubic-field example with an invisible absolute continuous obstruction, independently
  reconstructed. It is not an ordinary counterexample over Q.
- **L.2, refuted:** the compactness of varying ghost survivors fails, because a mod-5 coordinate has infinite
  discrete image.
- **The historical register:** 90 rows, of which 87 are confirmed, 2 repaired and 1 pending (GT_TOWER_CHECK A.4.57,
  a numerical compiler). The 66 enumerated SECTIONS_OVER_Q and GT_TOWER_CHECK Part C claims are all proved (E.2).

**Open:** the main questions. A.2 asks whether one ordinary infinite-support pair survives every class and every
coefficient prime. A.3 is open at the primes 2, 3 and ≥5. The universal first-exclusion table (B.2) is open, and so is
a section-side transfer of the CM obstruction (C.3/L.5).

**State:** review 5 (09:45 UTC) found movement: three GT_TOWER_CHECK rows went from pending to confirmed.

## FRAISSE_EXACT (account 4; about 9.5 hours; checkpoint 08, 10:05 UTC)

Review 06 (09:34 UTC) found movement:
- **G.25–G.28: the G route's structural prerequisites are proved for every candidate.** That covers local cyclicity
  of bounded cut stabilizers, the median tree for every locally free monoid, and unique splitting of central
  extensions. The remaining gate is an equivariant interval or quotient resolution.
- **A.31–A.33: the rational profile of the total amenable ordered-binary-vector example is settled.** It is exact over
  Q and nonexact over F₂ and Z. This eliminates it as a candidate against A.3(iii).
- **Two shortcuts refuted:** G.27 and G.29.

**Next:** stopped on account 4 at the user's word, 18 Nov ~11:0x UTC, after its newest checkpoint. The job goes to a
successor prompt on accounts 1–3, built from that checkpoint.
