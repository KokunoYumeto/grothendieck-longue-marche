# EXIT_TOWER's GT theorem and the ghosts of SECTIONS_OVER_Q: the Longue Marche expert's reading

By Claude Fable 5.2 at effort max, the Longue Marche field expert (rolled-back copy a3d0d8f6e092a3fe2 of agent
a125034fd35557818; my knowledge ends 14 Nov 2026, 04:16 UTC), 17 Nov 2026. Both returns are by GPT-6 Astra (ChatGPT
Pro mode) and are reviewed by no one.

**What I read.** Register rows only (statement and notes): EXIT_TOWER E.24, E.37, E.39–E.46, E.49, D.45;
SECTIONS_OVER_Q A.25, A.32, A.42, A.44, A.48, A.50–A.52, A.59, A.62, A.65, A.66, A.68, A.72, A.137, A.139, A.196,
A.207, A.209 (statements cut at about 600 characters) and its four open rows; the two memory notes on ghosts and on
"the obstruction is the definition". **No proof was read.** Line numbers below come from a keyword search. Nothing
from the literature was opened; what I say about it is from memory. "Hunch" marks what is mine and unproved.

## (a) Sense check

**The GT claims hold together, and they fit what was already refereed.** E.46 rebuilds the element of LM7_PUSH E.58
(`T = 5I`, `W = I`, parity `(1,0)`); E.49 says `Δ = 0` on `GT̂`; E.24's note gives the reason in the form I would
expect: the comparison needs one global exponent `k`, and for that element `k` is even modulo 4 and odd modulo 3
(`E_cm_parity_vanishing.tex`, lines 478–533). That is the statement that a frame sign cannot differ at the primes 2
and 3, which is how I read `Δ` (`EXPERT_DELTA_TAU.md`).

**D.45 passes the check I can make.** At the top rank `k = d − 1` its formula gives the connectivity of the curve
complex: `n − 5` in genus 0, `n − 2` in genus 1, `2g − 4 + n` for `g ≥ 2, n ≥ 1`, `2g − 3` for closed surfaces, which
are Harer's values; at `k = 1` connected, at `k = 2` simply connected (the pants complex). Intermediate ranks and the
non-zero homology were not checked.

**Steps I doubt, for the referee.**
- **D1. E.44, `E_branch_fixed_points.tex`, line 14 and what follows.** The theorem cited (Boggi–Zalesskii, Theorem A)
  gives that a finite 2-subgroup of the completion is conjugate to one of the discrete group. The proof needs three
  more things: that an element of `GT̂` carries the `C₂²` into the right one of its two pure classes (the "half-twist"
  correction); that the centralizer in the completed ten-point group is the completion of the discrete centralizer,
  with its topology; and that each of the two actions that descend to `C₂ ∗ Z` is identified with a GT parameter.
- **D2. Where the pentagon is used.** An element of `GT̂₀` also commutes with the involution and acts on the group
  `C₂ ∗ Z` of the harmonic quotient. If E.44 or E.49 used only that, they would give `Δ = 0` on `GT̂₀`, against E.58
  and E.46. The ten-point sphere is where `GT̂` is needed. The referee should name the line where `A ∈ GT̂` and not
  only `A ∈ GT̂₀` is used, and check that the element of E.46 fails exactly there (`E_cm_parity_vanishing.tex`, lines
  210–253 and 529–533 are the candidates).
- **D3. E.42, `E_tower_kernel.tex`: the completion in genus at least 3.** The statement says "full profinite
  completions throughout"; E.45 works with procongruence groups. The congruence subgroup property is open in genus
  ≥ 3. Whether the proof that the genus-zero kernel fixes every crossing arrow uses a normalizer or centralizer
  statement for multitwists in the full completion of a group of genus ≥ 3 must be read off the proof; E.41 proves
  what is needed in genus zero only.
- **D4. E.43, `E_compatible_pairs.tex`, line 5.** The group of compatible pairs is taken from Definition 5.4 and
  Proposition–Definition 5.6 of Lochak 2025 as the equation (E.200). None of us has opened that paper. If (E.200) is
  not his definition word for word, E.43–E.44 are about another group.

**The ghost claims hold together** and agree with LM8 F.21 and LM7 E.32. For a pair that is locally a solution of
`x + y = 1` the tame symbols vanish exactly, so the class-two criterion holds (A.50) and the cup product is a class
of the lim¹ term (A.25). The deeper ghosts take valuations divisible by `∏_{r ≤ R}(Q^r − 1)` (A.62, A.66): these are
the factors `Frob_Q − 1` on the weights up to `R`. One point of reading: A.65 and A.72 say "for every level there is
a ghost", and the ghost depends on the level. No row has one ghost that survives every level. Not checked: the
recursion that produces the primes, and the explicit numbers of A.137–A.209.

## (b) Placing the GT theorem (from memory)

- Hatcher–Lochak–Schneps and Nakamura–Schneps (2000): a subgroup of `GT̂`, cut out by extra relations coming from
  types (1,1) and (1,2), acts on the whole tower in all genera. Whether it is all of `GT̂` was left open. The quilts
  of E.34–E.39 are Nakamura–Schneps's formalism.
- Hoshi–Minamide–Mochizuki and Minamide–Nakamura: `GT̂` as the outer automorphisms of genus-zero configuration groups
  and of the profinite braid groups; through `B̂₄` modulo its centre it acts on type (1,2).
- Lochak 2025, as E.43 uses it: the automorphisms are compatible pairs `(A, B)`. What it proves about the pairs being
  equal I do not know.
- **Plausibly new, if it holds:** `𝒥(A) = A`, that is, the extra relation of type (1,1) holds on all of `GT̂` (E.44);
  the automorphisms of the ordinary completed tower in all genera are `GT̂` (E.42); `Δ = 0` on `GT̂` (E.49); D.45.
- **To check before anything is called ours.** In Lochak 2025: is (E.200) his definition; does he prove, conjecture
  or leave open that the pairs are diagonal; for which completion is his theorem; is the relation of type (1,2) in
  it. In Nakamura–Schneps: (E.200) with `B = A` against relation (III′), coefficients included. In
  Hoshi–Minamide–Mochizuki and Minamide–Nakamura: whether the two actions on `B̂₃` are already compared there. A
  statement that settles a question open since 2000 needs a full referee pass of E.44 first.

## (c) Implications for the field

- **E.3 is claimed settled: `Δ = 0` on `GT̂`.** With the refereed E.58 and E.65: Galois ⊂ `GT̂` ⊂ `ker Δ` ⊊ `GT̂₀`. My
  implications page withdrew the expectation "Δ = 0" because I knew no way for the pentagon to give compatibility
  with a covering that is not a map of genus-zero moduli. The run's way is the one I had listed as the last
  possibility: quotients by finite subgroups of the groups of spheres with more points. I correct that page: the
  pentagon reaches genus one at level 12.
- **The involution question (LM4_SUCCESSOR (A)).** `Δ` no longer separates classes of involutions inside `GT̂`. My
  construction of an involution with `Δ = 1` (Lead 23 of LM8_PUSH), if it works, lives in `GT̂₀` and outside `GT̂`.
  Hunch: the technique of E.44, applied to the group of order two, is the route to "every involution of `GT̂` is
  conjugate to complex conjugation" (item I4).
- **Genus one adds no freedom.** For the manuscript: the loop equations of §46 alone (`GT̂₀`) are too large, and the
  compatibility of §47 is automatic once the pentagon is imposed. If E.42 holds, the two-level principle of the
  Esquisse holds in its strong form.
- **The unsent prompts.**
  - LM8_PUSH Part C: C.3 (`GT̂ ⊆ C^φ`) follows from E.44 once C.2 identifies §47 with (E.200); the last part of C.8
    cites E.49. Both wait for the referee.
  - The successor of LM7_PUSH: S.1 becomes "referee E.49"; S.11 (a mixed sign in `GT̂`) is refuted by E.49; S.3
    stays.
  - `PUSH_ITEMS_ORDER5_FRAME.md`: turn it from "find further characters" to "prove that every character built from
    frames at special points vanishes on `GT̂`" (item I3).

## (d) The ghosts

- **Strategy for A1.** No fixed finite level separates a ghost from a point, so a proof must use the whole tower at
  once or a map to a rigid target. The rows show three layers. (1) At one fixed class the obstruction is in
  continuous cohomology only: every finite quotient lifts (A.25, A.196). (2) Across the classes: the valuation at `Q`
  of the difference from a point has to be divisible by `Q^r − 1` for each weight `r` reached (A.62, A.66). Over all
  `r` this kills the `ℓ`-part for every `ℓ ≠ Q`; an ordinary integer with that property is zero. **Hunch G1: an
  ordinary ghost that survives the whole pronilpotent tower has finite support, so by A.32 it is a rational point.**
  (3) What can remain is `Q`-primary at `Q`, invisible on covers of degree prime to `Q`; the Selmer and Brauer tests
  on covers (A.137–A.209) are the tests of that mixed kind.
- **The tension is one of order of quantifiers.** "For every level a ghost" and "for this ghost a level" do not
  conflict. And yes: at a fixed class the obstruction lives only at the continuous level; across classes it lives in
  the limit over the weights. A.42 (the rational points are closed and discrete) fits: ghosts crowd towards points as
  the level grows.
- **The obstruction as a definition.** Where it lives: lifting a locally geometric section from class `r − 1` to `r`
  meets a class in `H²_cts(G_Q, gr_r)` that is zero with every finite coefficient module, so it lies in
  `lim¹_n H¹(G_Q, gr_r/n)`, the families `z` over the primes with `(Q^{r−1} − 1) | z_Q` modulo the image of the
  families tending to zero. What cancels it: the family `y_Q = z_Q/(Q^{r−1} − 1)`, and it cancels exactly when it
  tends to zero. So define the ghost class of weight `r` as `y` modulo the families tending to zero: a germ at
  infinity of a family over the primes, a function on the non-principal ultrafilters of the set of primes. The torsor:
  at finite level `n` the trivializations are a torsor under `H¹(G_Q, gr_r/n)`, and the ghost class is the failure of
  these torsors to have a compatible point. The computation that is the theorem: A1 for locally geometric sections
  says that the ghost classes of all weights, with their non-abelian twisting, vanish together only for points and
  cusps; G1 is its first case.
- **For LM6 (points as sections).** Class two and every fixed level select nothing, as LM7 found at the prime 3. LM6
  should ask the limit statements (G1, then the `Q`-primary step), not level-by-level survival. Statement (M1) of
  Lead 19 of LM8_PUSH has the ghosts as its test objects: by A.72 every finite form of (M1) is false.

## (e) Prompt items for GPT-6 Astra (ChatGPT Pro mode), each to be proved or refuted

- **I1 (feeds the successor of LM7_PUSH, S.1; LM8_PUSH C.8).** In the proofs of `𝒥(A) = A` and of `Δ = 0` on `GT̂`:
  the step that uses the pentagon holds for every element of `GT̂` and fails for the element of E.46; and the same
  argument on the four-point sphere, where `GT̂₀` acts, proves nothing about `Δ`.
- **I2 (feeds LM8_PUSH C.2, C.3).** Equation (E.200) with `B = A` is relation (III′) of Nakamura–Schneps and is the
  equation of §47 in the normalization of LM2 B.m3; hence `GT̂ ⊆ C^φ`.
- **I3 (feeds `PUSH_ITEMS_ORDER5_FRAME.md`).** For every `n`, every finite subgroup `H` of prime-power order of the
  full group of the sphere with `n` points and every `A ∈ GT̂`: `A` carries `H` to a conjugate, acts on the completed
  centralizer of `H`, and this action is the action of the same parameter `A` on the tower of the quotient orbifold.
  Consequently every continuous character built from frames at special points vanishes on `GT̂`.
- **I4 (feeds LM4_SUCCESSOR (A); LM8_PUSH B.5).** Every involution of `GT̂` is conjugate in `GT̂` to complex
  conjugation. And: `GT̂₀` has an involution with `Δ = 1` (Lead 23), hence a second conjugacy class.
- **I5 (feeds LM6; ANABELIAN_149_PUSH Part D; LM8_PUSH D.10).** A section of the full pronilpotent quotient of the
  arithmetic fundamental group of `P¹ ∖ {0, 1, ∞}` over `Q` which at every finite prime is conjugate to the section
  of a local point, and whose Kummer coordinates have integer valuations, is the section of a rational point or of a
  cusp. First: the exact divisibility by the factors `Q^r − 1` that a lift to each class imposes on the valuations of
  the difference from a point section.
- **I6 (feeds LM6).** The ghost classes of (d) are well defined, and the trivializations form the torsors stated.
  Determine the classes of the ghosts of A.44, A.59 and A.62 at the first weight where each dies. Determine whether a
  class that is `Q`-primary at `Q` survives the full pronilpotent tower, and the covers of degree divisible by `Q`
  that exclude it.
