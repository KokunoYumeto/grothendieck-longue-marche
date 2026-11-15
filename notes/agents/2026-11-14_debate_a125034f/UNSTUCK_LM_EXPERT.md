# Unstuck: A1, the sections of the tripod, F.9

By Claude Fable 5.2 at effort max (Longue Marche field expert, agent a125034fd35557818), 14 Nov 2026. A consultation
from what I know. Read: the table of the 13 open rows of `INTAKE_LM6_FINAL_20261114.md` and the lines on A1, D1, F.9
of `INTAKE_ANABELIAN_149_FINAL_20261114.md` (intakes by Claude Fable 5.2 at effort high; runs by GPT-6 Astra, ChatGPT
Pro mode). My context was at its limit: I did not read the exact statements of A1 and F.9. **All hunches, checked
by no one.**

## One pattern behind all three

Each run stalled where it tried to get a global, full-profinite statement from data that every pro-`ℓ` or abelian
quotient sees one prime at a time. The same thing is behind `Δ`, LM8 A.22, G.20 and the icosahedral centralizer:
what decides these questions sits where primes mix, or in a lim¹ term, and conjugacy classes of local groups carry
no condition there. The way out each time: use the points as sections at finite places (specialization, Frobenius),
where class field theory or the local classification gives a hard invariant, and only then pass to the limit.

## A1 (point separation for proper curves, every genus and characteristic)

- **What is going on.** The run turned A1 into the existence of a cyclic cover whose primitive Prym has `p`-rank
  zero. I think that target is wrong: primitive parts of cyclic covers of degree prime to `p` are ordinary for most
  characters, so rank zero is the rare case, and the search finds it curve by curve (genus two over `F_4`).
- **Hunch: A1 is true, and the proof does not go through Pryms of rank zero.**
- **Path 1 (if A1 is injectivity of points into section classes over a field finitely generated over `F_p`).**
  Specialize. Two rational points `x ≠ y` stay distinct at almost every closed point `v` of a model of the base; a
  conjugacy of their sections by the geometric group specializes to a conjugacy over the finite field `k(v)`; there
  the section of a point is its Frobenius, and in the abelianized fundamental group its class is the class of the
  point in the Picard group; two points of degree one with the same class are equal when the genus is positive.
  Items: (i) the specialization of the section of a point is the section of the reduced point; (ii) conjugacy
  specializes; (iii) the class field theory step. No hypothesis on the `p`-rank.
- **Path 2 (if A1 is geometric, over an algebraically closed field).** Lower the target from "`p`-rank zero" to "not
  ordinary in the eigenspace that carries `x − y`": prove that for every curve of genus at least two the theta
  divisor of the Frobenius bundle (Raynaud) contains torsion points of order prime to `p` in the needed position
  (Raynaud, Tamagawa, Pop–Saïdi, from memory), and redo A.C2.19 with that weaker input.

## The sections of the tripod over `Q` (LM6 B.27 = ANABELIAN D.U1; D1 with its two gaps)

- **What is going on.** Finite support gives global (B.14). What is left is a section ramified at infinitely many
  primes, and that is exactly where the phantom classes are (LM7 E.32, LM8 F.21: every finite level lifts, no
  continuous lift). D1's first gap, finite ramification of one `ρ_{s,ℓ}`, is this.
- **Hunch: true** (every section with trivial cyclotomic centralizer is a point), and the proof is local-to-global
  through cusp colours, not through nilpotent towers.
- **Path.** (i) At each prime `q` where the section is ramified, in each pro-`ℓ` quotient, the local section is one
  of the cuspidal families (the tripod form of LM7 E.61, E.66). (ii) The section is one section for all `ℓ` at
  once: prove that the cusp and the local Kummer parameter at `q` do not depend on `ℓ`. This is the step no pro-`ℓ`
  argument can give and the place to use the full profinite group. (iii) Then the two Kummer classes are
  `κ(a)`, `κ(1 − a)` with `a` in the completed multiplicative group and the valuations of `a`, `1 − a` are honest
  integers at every `q`; prove that `a` is a rational number (a unit-equation statement in the completion), or
  produce the section that refutes it. (iv) In parallel, descent along the cyclotomic tower (Lead 16 of LM8_PUSH):
  over `Q(μ_{ℓ^∞})` nothing is obstructed, and the sections over `Q` are descent data; the phantom class is the
  non-Hausdorff part. (v) Use the covers the tripod has of itself (`λ ↦ 4λ(1 − λ)`, the `j`-map): the set of
  sections is stable under them, and a section that is not a point should be thrown into a cusp by one of them.

## F.9 (the intrinsic converse of reconstruction)

- **What is going on.** Sufficient classes on one side, necessary conditions on the other, and no row moved. My
  reading of the pattern: the necessary conditions found are all of the kind "classes of local groups are
  preserved", which in these groups are automatic (as in cote 143, ⑨, at type (0,3)).
- **Hunch: the converse is false as an intrinsic statement with the conditions now listed**, and becomes true when
  the condition "the sections of the points are preserved" is added.
- **Path.** (i) Refute: with the lifting theorem LM7_PUSH D.50 and the element of E.58, build a system that
  satisfies every listed necessary condition and is not geometric (the element with `Δ = 1` is the model: it
  commutes with `𝔖_3`, preserves every local class, and is not Galois). (ii) Then state and prove the converse with
  the sections of two special points added, starting with the harmonic and equianharmonic points of the tripod.

## For all three prompts

Give GPT-6 Astra (ChatGPT Pro mode) the refereed results D.50, E.58, E.65 as tools, and the instruction to test
every proposed intrinsic condition against the element of E.58 before trying to prove it sufficient.
