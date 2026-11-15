# Implications: TOTAL_EXACT_2 and LM8 read together

Claude Fable 5.2 (Anthropic), effort high, 13 Nov 2026. Rows: T = TOTAL_EXACT_2 (`INTAKE_TOTEX2.md`), L = LM8
(`INTAKE_LM8.md`). "Reader" marks an inference of mine: checked by nobody. Sources named from memory are marked
"not opened".

## Summary

1. The two returns meet in one statement (I1): **exactness of `colim_A` on abelian groups is the vanishing of
   `lim¹_{A^op}` on compact abelian groups.** LM8's "compact towers commute, non-compact ones do not" (L F.15) is
   the case `A = N`. TOTAL_EXACT_2 shows that over a general index compactness is not enough, even when the index
   is total (T A.24, A.17, A.19), and that it is enough under a uniform bound (T A.20) or a Ramsey property (T A.13).
2. The passage to the Galois part (T A.33) and LM8's covering germ (L E.10, E.11) are the same operation: take the
   locally constant (saturated) objects stage by stage, never the limit topos first (I2).
3. Neither the Galois part nor the homotopy-final comparisons give a handle on LM8's six open rows (I4). The
   reason is exact: those rows are not limit problems over a non-filtered index.
4. The closing-gap form B2 covers L F.15's counterexample and L F.21, and through F.21 it gets its first instance
   that obstructs an actual section. It does not cover T's separator (uniform gap, closed range), L E.11 (degree
   zero), L A.22 and G.20 (prime-mixing), or CK E3 against L G.10 (the reverse direction) (I5).

## I1. Exact colimits and compact inverse limits (T A.2, A.3, A.13–A.20, A.24; L F.15, F.21)

Statement (reader; standard duality, proof in two lines). For `M: A → Ab` and `T = R/Z`, `M^∨ = Hom(M, T)` is a
diagram of compact abelian groups on `A^op`, and `lim^i_{A^op} M^∨ = Hom(T_i^A(M), T)` (`T` is injective). So
`colim_A` is exact iff `lim¹_{A^op}` vanishes on every diagram of compact abelian groups; the same over `F_p` with
profinite `F_p`-vector spaces.

- L F.15 (1) is this for `A = N`: towers of compact groups have no `lim¹`; `N` is filtered. F.15's counterexample
  (`Z ⊕ Z/2^n`, `H^1 = Z_2/Z`) and F.21 (`⊕_q Z/5^{min(n, e_q)}`) are non-compact coefficients over `N`.
- T A.24 dualized: over `C_δ^op` the diagram `Q_{F_p}^∨` of **finite-dimensional, compact** `F_p`-spaces has
  `lim¹ = F_p`, and `Q_Z^∨` (compact tori and finite groups) has `lim¹ = R/Z`, although every category of elements
  of `C_δ` is contractible. So LM8's dichotomy has a counterpart with the roles exchanged: fix compact
  coefficients and vary the index.
  - exact index (filtered; `Δ_inj`; ordered graphs, T A.8): compact ⇒ no `lim¹`;
  - Ramsey index (T A.13): every diagram of non-empty compact Hausdorff spaces has a point;
  - quasi-filtered index and a uniform bound on the fibres (T A.15, A.20): no `lim¹`, non-empty limits;
  - total index without a bound (T A.17, A.19, A.24): `lim¹ ≠ 0`, empty limits of compact convex sets.
- Consequence for La Longue Marche: every limit LM8 takes is over a directed set (towers in `n`, finite sets `S` of
  primes, open subgroups), so only the coefficients matter and F.15 is the right criterion. A limit over the
  Teichmüller tower itself (types `(g, ν)` with gluing and filling maps; `GT̂` as automorphisms of the tower) is over
  a non-filtered index; there the index conditions of TOTAL_EXACT_2 apply. See candidate P3.

## I2. The Galois part: T A.33 and L E.10–E.11

- T A.33 in topos terms (reader): for `A = C_δ` the two comparisons `H → H^inj → T_S` are the associated sheaf for
  the atomic topology on `A^op`; `Sh(A^op, atomic) = Cont(G)-Set`, `G = Aut(M)`. The theorem: sheafification is
  homotopy final on categories of elements, and every atom `G/U` is representable (`U = G_F`, T A.32) or terminal.
  So the homotopy types of all slices of the presheaf topos `[A, Set]` are read off in the Galois topos.
- L E.10–E.11: the covering germ of a puncture is the 2-colimit of the categories of coverings of the `D_n^*`
  (`= BZ`); the inverse limit of the full sheaf topoi is empty.
- Common form: the fundamental pro-groupoid is a left adjoint, so it commutes with colimits of topoi and not with
  limits. The Galois part is extracted stage by stage (locally constant objects, saturated actions) and the limit
  is taken afterwards, in pro-groupoids.
- What would make the limit topos right (reader; SGA 4 VI 8.7 and VII 5, not opened): coherent topoi with coherent
  transition maps. That is again the compact case of I1. The étale topoi of punctured henselian neighbourhoods are
  coherent; the classical punctured discs are not. So L E.11 refutes the topological reading of scans 242–243 and
  leaves an algebraic reading in which the manuscript's "limiting topos" is `BẐ(1)`. Candidate P2.
- For LM5 (Part F (d), (g): germs of neighbourhoods, "germe de disque épointé"): L E.10–E.11 are the case of one
  point on a curve. Applied in `PROMPT_IMPACT.md`.

## I3. Results of one return that the other companion can use

- **L B.6, B.9 → Dérivateurs** (GALOIS, POLES, BISITE B.11–B.13). For `𝔞` = abelianization, `π/π''`, `π/Γ_{c+1}`,
  pro-ℓ, rational unipotent, the virtually abelian pro-quotient `V`: `W_𝔞` is a fundamental localizer containing
  `W_1`, and its intrinsic finite coverings are classified (ℓ-group monodromy; trivial; none; none; none; all).
  Reader: `W_𝔞` is the class of maps local for the 1-types `BG`, `𝔞G = G`; so these are the localizers
  "local for a class of groups", and B.9 computes `Fib_W` on finite coverings for each. New examples for
  REVERSIBLE_LOCALIZERS-type questions (is `W_𝔞` of the form `R(L)`; is it accessible; which satisfy Loc (6 b)).
- **T A.22–A.23, A.30 → LM (gluing)**. The cyclic "necklace" and "bridge" constructions show how a cyclic
  amalgam stays inside a class when the circle is long compared with the overlaps. No direct use found.
- **T C.8, C.9 and `notes\finite_pd_route.md` §3 → LM8 B.5, B.21 and LM (free groups under filling and covers)**:
  diagrams of free groups with free-factor transitions can have non-aspherical colimits and non-zero `T_1` of the
  abelianizations, over a quasi-filtered and (in the note) over a total index. A warning for any argument in LM
  that passes a colimit of surface or free groups through abelianization; no row of LM8 does so.
- **L F.21 → LM7 (E.32) and the shape map**: see I5.
- **L A.22 → the torsion question for `GT`** (LM expert, target (vi)): 2-torsion with multiplier one exists in the
  metabelian quotient and in a relative pro-5 tower, invisible in every pro-prime quotient. Candidate P4.

## I4. Do the Galois part and the homotopy-final comparisons reach LM8's open rows?

No. Row by row:

| Row | What is missing | Why TOTAL_EXACT_2 does not reach it |
|---|---|---|
| A.12 | lift of the involution of A.22 to `F̂_2`, or a finite obstruction | an inverse system of finite non-empty sets over a directed set: non-empty limit by compactness (T A.15 with a filtered index); the content is whether each finite level is non-empty, which is a computation |
| B.24d | actions on the higher Fermat stages | no limit involved |
| B.28 | the §47 equation for a given profinite word | a comparison of two actions of one element; no index category |
| F.12 | unrestricted ramification from class 3 on; the Alexander module | limits over `n` and colimits over `S`, both directed; the failure is the non-compact coefficient group (F.15, F.21) |
| G.16 | one arithmetic scalar | a computation |
| G.20 | the common kernel of all maximal pro-ℓ quotients | detection by `F̂ → ∏_ℓ F^{(ℓ)}` fails to be injective: an `H^0`-type failure over a discrete set of primes, not a limit over a category |

What does transfer is the method of T A.31–A.32 as a pattern (reader, an analogy, not a result): classify the open
(or the "peripheral") subgroups as stabilizers by generating `G_{B∩C}` from `G_B` and `G_C`. LM8 G.13 and G.19
recognize inertia among procyclic subgroups by an arithmetic normalizer condition; the two are not instances of
one theorem.

## I5. The closing-gap form (shape map, revision 2, B2): where it fits and where it fails

Form: at every finite level an operator `d_n` with closed range and a gap; in the limit the gap closes and the
obstruction is `closure(im d)/im d`.

Fits.
- **L F.15, counterexample.** `d: Z → Hom_cts(Z_2, Z_2) = Z_2`, `a ↦ (t ↦ ta)`. At level `n`, `d_n: Z → Z/2^n` is
  onto (`H^1 = 0`); in the limit `H^1 = Z_2/Z = closure(im d)/im d = lim¹(2^n Z)`.
- **L F.21.** `d = D = diag(5^{e_q})` on `C(I)`; `H^2 = C(I)/D C(I)`, "the actual image, no closure";
  `inf |5^{e_q}| = 0`. The class `κ(5) ∪ Σ 5^n κ(q_n)` lies in `closure(im D)/im D`. This is LM7 E.32 at the prime
  5, and it adds what E.32 did not have: the class is the obstruction to lifting an actual pair of Kummer classes
  to a class-two section, so every finite quotient has a lift and no integral lift exists. B2's list gains its
  first item where the closing gap obstructs a section.

Fails.
- **T A.24 / A.18 (the separator).** At every object the column `D_X` is injective and the gap is uniform:
  `‖μ_2 − μ_1‖_1 + ‖μ_3 − μ_1‖_1 ≥ 1` for all probability combinations, at all objects. Nothing closes. In the
  dual picture the maps of compact groups have closed range and the obstruction is a full cokernel `R/Z`, so
  `closure(im)/im = 0`. Non-exactness over a total index is a third regime: finite levels obstructed uniformly,
  the limit (the homotopy type) trivial.
- **L E.11.** The limit topos is empty by a covering argument (a join of zeros is 1). No operator and no class:
  degree zero, like the sum-of-squares item of the summary.
- **L A.22–A.26, G.20.** Invisible in every pro-prime quotient: a failure of `F̂ → ∏_ℓ F^{(ℓ)}` to detect, produced
  by an idempotent mixing the primes 3 and 5. Not a tower.
- **CK E3 against L G.10.** Every `N_r` has fixed elements outside inertia in its last layer, and
  `P^{s(Δ)}` is inertia. These are finite-level classes killed by the next transition map: the reverse direction
  named in B2, with a Mittag-Leffler tower and no `lim¹`.

## Candidate prompt items

- **P1 (Dérivateurs; from I1 and T A.13–A.20).** Statement: for a small category `A` with common successors,
  determine the exact position of "`lim¹_{A^op}` vanishes on all diagrams of profinite abelian groups" between
  exact and total, and prove or refute: (a) `colim_A` exact on `Ab^A` iff `lim_{A^op}` is exact on compact abelian
  groups iff it is exact on finite abelian groups of unbounded size; (b) for the embedding category of a Fraïssé
  class with canonical amalgamation, exact iff `Aut(M)` is amenable (T A.13 gives: extremely amenable ⇒ exact, by
  Kechris–Pestov–Todorcevic, not opened; `C_δ` is total and its group is not extremely amenable). Reason: T A.18
  is a statement about probability measures, which is the language of amenability; T A.14 uses only Ramsey.
  Settled by: a proof of (b) or a Fraïssé class with amenable, not extremely amenable group and non-exact colimits
  (or the converse).
- **P2 (Longue Marche, §53.5; from I2 and L E.11).** Statement: prove that the limit of the étale topoi of the
  punctured henselian neighbourhoods of a point of a curve (and of a normal crossings divisor) is the classifying
  topos of the local fundamental group, state the hypothesis under which a cofiltered limit of topoi commutes with
  `Π_1` (coherence), and decide from the text of scans 242–243 which reading he has. Reason: L E.11 refutes one
  reading only. Settled by: the theorem with its hypothesis and the passage quoted.
- **P3 (both; from I1).** Statement: for the index category of the Teichmüller tower used in LM3 (types and
  gluing or filling maps), decide whether it is quasi-filtered, total or exact in the sense of TOTAL_EXACT_2 after
  the passage to its Galois part, and express the two-level principle as a finality statement (the comma categories
  of the inclusion of the first two levels are simply connected). Reason: T A.33 is a theorem about categories of
  embeddings with free amalgamation, and the tower is such a category; the two-level principle is proved in the
  literature by the simple connectivity of the pants complex (Hatcher–Lochak–Schneps, not opened). Settled by: the
  class of the index category, with proofs, and the two-level principle derived from it or shown not to follow.
  Low confidence: neither return touches this; the expert for LM3 should say whether LM3 already contains it.
- **P4 (Longue Marche; from L A.22).** Statement: decide whether the involution of L A.22 satisfies the 2-cycle
  and 3-cycle relations (and the metabelian shadow of the pentagon) in `F̂_2/F̂_2''`, i.e. whether it is the image of
  an element of `GT̂_0` or `GT̂`; compare with the adelic beta function of Anderson–Ihara. Reason: it would be
  multiplier-one 2-torsion in the metabelian image, which Galois elements do not have. Settled by: the relations
  checked on the explicit `u = −2e/((x−1)(y−1))`.
- **P5 (shape map; from I5).** Statement: the three regimes as one trichotomy for a tower (or diagram) of
  complexes: (i) gap closes, class in `closure(im)/im` (F.15, F.21, E.32); (ii) uniform gap, obstruction present at
  every level and of closed range (T A.18, A.24); (iii) finite-level classes killed by later maps, Mittag-Leffler
  (CK E3 / G.10). Prove that for diagrams of Banach or compact groups over a directed set only (i) and (iii)
  occur, and that (ii) needs a non-exact index. Settled by: the statement proved, or an example of (ii) over `N`.
