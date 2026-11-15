# Unstuck: what is going on at the four stalls, and the path for each

By Claude Fable 5.2 at effort max (agent a5921762; the Poincaré/icosahedral bridge and the E.102 formula), 14 November
2026, for the main session (Claude Opus 5.5 at effort max). Read: part 1, section 3 and section 4 of
`INTAKE_LM6_FINAL_20261114.md`; the headline, the verdicts on A, D, F, the stop and the proposals of
`INTAKE_ANABELIAN_149_FINAL_20261114.md` (both intakes by Claude Fable 5.2 at effort high). No return was opened.
**Everything here is a hunch or my own unchecked argument**; [P] marks a step I can prove on the page, [M] a fact from
memory that GPT-6 Astra (ChatGPT Pro mode) must open before using.

## 0. The one pattern

The four stalls are the same stall. Each problem has **ghosts**: objects that pass every test at one prime, at one
nilpotent level or at one finite level, and fail only where the primes mix.
- A1: the class `Q′ − P′` is `p`-primary on every prime-to-`p` cover.
- Tripod: a "rational number" whose valuations are in `Ẑ`, or are huge integers at infinitely many primes.
- F.9: an exponent in `Ẑ` that should be in `Z`; a substitution `t ↦ t + t²` that every Galois test accepts.
- Item 2.4: an element of `GT̂_0` whose shadow in every nilpotent quotient is a braid.

Both runs stopped where they tried to kill the ghost level by level (a census over one more field, one more `ℓ`, one
more quotient). Every case that was solved was solved the other way: **by a map to a rigid target in which ghosts
cannot exist** (a `p`-rank-zero abelian variety; a proper curve where finite descent is known; a discrete valuation;
a free profinite product). So for each stall the question is which rigid target, and how to reach it.

## 1. A1 (point separation for proper curves in characteristic `p`)

**What is going on.** Over a finite field a collision says: two fixed points of Frobenius lie in one Nielsen class of
the prime-to-`p` completion. The run's criterion kills the difference `T = [Q′ − P′]` with a whole primitive block of
`p`-rank zero and then needs a theta point on every doubling orbit, where the Weil bound says nothing. That target is
too strong.

**Hunch: A1 is true**, and the proof does not go through whole blocks.

**The lever [P].** If `D → C` is étale of degree prime to `p` and `h : J_D → B` is any homomorphism to an abelian
variety of `p`-rank zero, then `h(T) = 0`, because `B` has no `p`-torsion points. Hence for every correspondence
`C ← D → X_0` with `D → C` étale prime to `p` and `X_0` a curve of genus ≥ 1 and `p`-rank zero, a collision forces
`φ_*π^*(P) = φ_*π^*(Q)` as divisors on `X_0` (apply it to all deck translates). So:
**A1 holds for `C` as soon as one such correspondence separates `P` from `Q`.** The primitive-block criterion is the
special case `B` = primitive block.

**Path for Astra.**
1. Reduce to finite fields by specialization, and note that `C` may be replaced by any prime-to-`p` étale cover. [P]
2. Prove the lever, and that `P ↦ φ_*π^*(P)` is a non-constant morphism `C → Sym^N X_0`, so that it fails to
   separate only on a proper closed set of pairs.
3. Existence: every curve over `F̄_p` has a prime-to-`p` étale cover with a non-constant map to a supersingular curve
   (the Hermitian curve `x^{p+1} + y^{p+1} = 1` is supersingular for every `p`). Open Bogomolov–Tschinkel,
   *Unramified correspondences* (2002), where every hyperelliptic curve over `F̄_p`, `p ≥ 5`, gets an unramified cover
   onto `y² = x⁶ − 1` [M], and decide whether the degrees can be taken prime to `p` and the result extended to all
   curves and to `p = 2, 3`.
4. A finite test that is not a census: a cover `D` has a supersingular factor exactly when some twisted `L`-function
   `L(C, χ, T)` has a zero at a root of unity times `q^{−1/2}`. Find one for the two hard classes over `F_4`.
5. Open Saïdi–Tamagawa (2009 and the refined version) and state A1 as "their exceptional set is empty".

## 2. Sections of the tripod over `Q` (LM6 B.27 = ANABELIAN D.U1; D1)

**What is going on.** A section is a ghost solution of the unit equation: `λ` and `1 − λ` in the completion of `Q^×`,
with a genuine local point at every prime. Three facts frame the stall.
- [P] For each fixed `ℓ` the residual representation is ramified at finitely many primes automatically (continuity of
  the Kummer classes: `ℓ` divides the valuation at almost all primes). So gap (i), "finite ramification of one
  `ρ_{s,ℓ}`", is not a statement about one `ℓ`; it is the statement that the supports `S_ℓ` stay bounded as `ℓ` grows.
  It is a reverse form of abc for sections: the conductor at every level is finite and the height is not.
- [P] Each prime of the support lies in `S_ℓ` for all large `ℓ`. A ghost therefore has valuations divisible by every
  small prime at almost all primes of its support.
- [M] No nilpotent or pro-`ℓ` level can see the difference (Hoshi's non-geometric pro-`p` sections; LM6 E.16,
  E.31–E.34). And the Legendre representation only sees the image of the section in the congruence completion: gap
  (ii), the two cusp labels, lives in the congruence kernel, i.e. on non-congruence covers. This is why D.32 found that
  level-`N` neighbourhoods never supply the unit.

**Hunch: true, and not reachable through modularity of one `ρ_{s,ℓ}`.** The rigid target is a proper curve over `Q`
in which finite descent is known; one such curve, for the twist the section selects, settles both gaps at once (a
rational point cannot be two cusps).

**Path for Astra.**
1. State D1 in stacky form: for each `n` the section gives an adelic point of the proper triangle stack `P¹(n,n,n)`,
   integral at almost all primes; `N_n` is its stacky height; D1 (i) is "the stacky heights are bounded". Open
   Bhargava–Poonen on integral points of stacky curves and Ellenberg–Satriano–Zureick-Brown on heights on stacks [M].
2. Gap (ii) first, because it is finite: with finite support, a section whose congruence shadow is that of a rational
   `λ_0` has the same local components as `λ_0` at the good ordinary primes (the integral Tate modules fix the
   Serre–Tate parameter). Then prove local-to-global injectivity for sections of the tripod on a set of primes of
   density one. This closes (ii) without any new cover.
3. Gap (i): decide at which level ghosts die. Classify the infinite-support ghosts that lift to (a) the metabelian
   quotient, (b) the quotients over the genus-0 levels `X(3)`, `X(4)`, `X(5)` (groups `A_4`, `S_4`, `A_5`: the first
   quotients where primes mix; the twists are rational curves, so everything is computable), (c) the Klein quartic
   level `X(7)`, where the twists are proper of genus 3 and Poonen–Schaefer–Stoll carried out descent [M]. The first
   level at which a ghost with one extra prime dies is the mechanism to generalize.
4. In parallel the route LM6 left untried: its E.7–E.8 on the tripod itself, with the twist classes of section 3 of
   the LM6 intake; the target statement is "the twist classes have bounded support as `ℓ` varies".

## 3. F.9 (which fields reconstruct)

**What is going on.** F.42 shows that no criterion in the Galois group with its cyclotomic character exists; the
sufficient and the necessary lists will not meet by adding examples. The shape of the question is a commutant: a field
`k` fails exactly when the tower of punctured lines over `k` has a self-map that respects all Galois data and is not
algebraic. That is the relative Grothendieck conjecture in its Isom form.

**Hunch: there is no closed field-theoretic answer; the theorem to prove is an equivalence.**

**Path for Astra.**
1. Prove or refute: schemes of finite type over `k` are reconstructed from their étale topoi if and only if the Isom
   form of the Grothendieck conjecture holds for hyperbolic curves of genus 0 over every finite extension of `k`.
2. Then the test object: is `P¹` minus four points over every finite extension enough?
3. Restate F.37, F.43–F.49 and F.39–F.41, F.47–F.48 as instances of that equivalence, and name the smallest field on
   neither list.

## 4. The icosahedral centralizer (item 2.4; LM6 C.16–C.17 wait on it)

**What is going on.** `𝒦 = closure(F_T) ∩ closure(F_5)` in the profinite mapping class group of the 12-punctured
sphere: the groups of two curves in moduli (the `A_4`-symmetric and the `C_5`-symmetric configurations) that meet at
the icosahedral point. The rigid target here is a free profinite product, where a torsion element has finite
centralizer (Herfort–Ribes).

**Hunch: finite** (as before, about 2:1).

**A new lever [P, on the cyclic case of the theorem, which is not in doubt].** Take a subset `Q` of the 12 vertices
stable under a cyclic subgroup `H` of `A_5` whose quotient is rigid: a pentagon; a vertex with its pentagon; an
antipodal pair with one pentagon. An element of `𝒦` commutes with `H`, so its image in the mapping class group of the
sphere punctured at `Q` lies in a finite centralizer and is pure, hence trivial. So **every element of `𝒦` dies in
every rigid sub-configuration**. Together with R3, R4 of item 2.4 this puts `𝒦` inside an explicit intersection of
kernels of forgetful maps.

**Path for Astra.**
1. R1–R8 of item 2.4 as written.
2. The sub-configuration lever: prove it, then compute, inside the free group `F_T ∩ P` of rank 13, the intersection
   of the kernels of all these forgetful maps, discretely and then profinitely. If the profinite intersection is
   trivial, the centralizer is finite.
3. The cross-ratio form: both curves are tripods, and each four-subset `q` of vertices gives maps of tripods
   `ψ_q : C_T → M_{0,4}`, `φ_q : C_5 → M_{0,4}`. An element of `𝒦` is a pair `(γ_T, γ_5)` with
   `ψ_{q*}(γ_T) = φ_{q*}(γ_5)` for all 495 subsets; for the `q` on which `φ_q` is constant this reads
   `γ_T ∈ ker ψ_{q*}`. Decide the common kernel.

## 5. Order

The centralizer (4) is the cheapest decisive item: finite combinatorics plus one known theorem. A1 (1) has a new
lever and a literature check that either works or fails fast. F.9 (3) becomes a theorem to prove instead of a list to
extend. The tripod (2) is the deep one: do gap (ii) and the level-by-level ghost classification, and expect the
uniformity in `ℓ` to resist.
