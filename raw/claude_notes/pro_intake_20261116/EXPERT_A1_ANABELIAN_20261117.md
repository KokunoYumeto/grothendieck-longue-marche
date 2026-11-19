# First check of ANABELIAN_SUCCESSOR A.3 = AR.3 (universal injectivity of proper point sections over finite fields)

Check by Claude Fable 5.2 at effort max (copy ab3f12f2 of the Longue Marche expert), reading the proofs, 17 Nov 2026.
The return is by GPT-6 Astra (ChatGPT Pro mode), final of 16 Nov 2026, 12:43 UTC. Brief by the main session
(Claude Opus 5.5 at effort max).

## 1. Verdict

**Sound as read. I found no error and no gap in the parts I read.** The proof is short once its three group
statements are granted, and I re-derived each of its decisive steps myself. It is not a full check: my context
allowed about a third of the reading the brief lists. The verdict is conditional on four things I did not read
(section 3), of which one is an outside theorem that carries real weight: the finiteness of the exceptional set
(Saïdi-Tamagawa 2009, Proposition 1.8 (vi)), which AG.40 uses. The claim "every exceptional set is empty" is then a
strengthening of their finiteness, obtained from it.

**Read:** `sections/A_foundations.tex` lines 96-186 (end of AR.2, AR.3 with its proof);
`agent_geometric/geometric_section.tex` lines 3901-4182 (AG.40, statement and whole proof) and 4204-4353 (AG.41:
statement, steps 1 and 2, start of step 3). **Not read:** AG.39 (3280-3900), AG.41 lines 4354-4494, AG.42
(4495-4687), `sections/A_structure.tex` (AR.8, AR.9), the three audits in `agent_criteria/`. No literature.

## 2. The steps, with what I checked

The proof of AR.3 (`A_foundations.tex` 150-186) has this shape. Let `Π_C` be the arithmetic group with geometric part
prime to `p`, and suppose `s_Q(G_k) = γ s_P(G_k) γ⁻¹` with `γ` geometric.

1. **The fibre trick (AR.3 lines 160-169; AG.42).** In a quotient of the configuration group in which the fibration
   sequence for the second projection is exact, the group of `C − P` is the inverse image of `s_P(G_k)`. Conjugation
   by a lift of `γ` therefore carries the group of `C − P` onto the group of `C − Q`, compatibly with the first
   projection up to an inner automorphism. So the punctured group depends only on the decomposition subgroup of the
   point in `Π_C`. *Checked by my own argument:* the lift can be taken in the decomposition group of the diagonal
   (which maps onto the diagonal copy of `Π_C`); the component of the diagonal through `(P̃, P̃)` is the component
   through `(Q̃, Q̃)`, so one and the same subgroup, "elements of the diagonal group whose projection lies in the
   common decomposition subgroup", is the cusp decomposition group on both sides. I did not read AG.42's own text.
2. **AG.41, exactness (lines 4204-4353).** Definitions: `F = π₁(C − x)^(p′)`, `K_F = ker(F → Δ)`,
   `F_cr = F/ker(K_F → K_F^(r))`, and the same for the configuration space with `Δ × Δ`. The cuspidal kernel is
   taken inside the prime-to-`p` group, which is the right choice (with the kernel of the full profinite group the
   statement would be false: its abelianization is a regular module of the full group).
   - Step 1 (4251-4300): if conjugation on `L/[L,L]L^r` is through an `r`-group, then `L^(r)` injects into `H^(r)`.
     The argument is the standard one (the kernel of `Aut(L^(r)) → Aut` of the Frattini quotient is pro-`r`; a
     non-abelian free pro-`r` group has trivial centre). Correct. This is what replaces unipotence: the brief's
     worry is met by passing first to the cover.
   - Step 2 (4302-4346): for a Galois étale cover `C′ → C` with group `A` of order prime to `p`, the family
     `C′ × C′` minus the graphs of the deck transformations, over `C′`, has labelled punctures and trivial monodromy
     on the homology of the compactified fibre; so the monodromy modulo `r` is a group of shears, an `r`-group.
     Correct.
   - Step 3 (from 4348; I read its first lines and completed it myself): a finite quotient `Q` of `F_cr` is an
     extension of a prime-to-`p` quotient `A` of `Δ` by an `r`-group `R`; `R` is a quotient of `π₁(V′)^(r)`; by
     steps 1-2 an `r`-quotient of `π₁(Y)` dominates it on the fibre; its core in `π₁(U)` gives a quotient of
     `π₁(U)` that is an extension of `A × A` by an `r`-group, hence a quotient of `E_cr`, and it dominates `Q` on
     the fibre. Exactness in the middle and on the right follows from right exactness of completion. I see no gap.
3. **AG.40, the criterion (3931-4178).** Each step followed.
   - Step 1 (3934-3960): `P − Q` has `p`-power order in the Jacobian; `f` with divisor `p^e(P − Q)`. Correct.
   - Step 2 (3962-3989): corresponding finite covers have the same number of rational points over every constant
     extension. It rests on (AG.39.15), which I did not read; I checked the point it needs (a pro-`r` étale cover
     of the compactification of a visible cover is again visible) and it holds.
   - Step 3 (3991-4033): decomposition groups of non-cuspidal points are carried to decomposition groups of
     non-cuspidal points, by the compactness argument over the whole inverse system of covers. This is whole-group
     recognition: no finite level is substituted. Then **the outside input**: by the finiteness of the exceptional
     set, the target point is the same point `R` for all `R` outside a finite set.
   - Step 4 (4035-4160): the two cuspidally central extensions by `Z_r(1)`; the multiplier of the induced
     isomorphism is one; `χ(u, v) = β̄(u)v⁻¹` is a cocycle with residues `+1, −1` at `P, Q`; `κ_r(f) − p^e χ`
     descends to `H¹(Π_C, Z_r(1))`, which is the constants; on the decomposition group of `R` the cocycle `χ` is a
     coboundary because the normalizer of a point section is itself. All correct as written.
   - Step 5 (4162-4177): take `R` with `f(R) = aζ`, `ζ` a non-trivial root of unity of `r`-power order, outside
     the finite set. Contradiction. Correct.

Answers to the brief's questions: the pro-`r` cuspidal kernel is injected (AG.41), by unipotence on the cover, not
on `C`; a geometric conjugator does lift to the diagonal group, and the puncture group is the intersection; the
isomorphism of AG.40 does force `P = Q`, given the finiteness theorem; the inverse-limit recognition is complete.

## 3. What is not covered, and the one place of real weight

1. **Saïdi-Tamagawa 2009, Proposition 1.8 (vi)** (cited at `geometric_section.tex` 4024-4026). AG.40 needs: for a
   proper curve of genus at least two over a finite field and the primes other than `p`, the set of closed points
   that share their decomposition subgroup in `Π_C` with another closed point is finite, over all constant
   extensions at once. If the published statement is weaker (finite over each fixed field only, or another notion of
   exceptional), step 5 fails, because it needs infinitely many usable points. This is the first thing to open.
2. **(AG.39.15)**, used at 3967; AG.39 not read.
3. **AG.41 lines 4354-4494** (rest of step 3, the statement in characteristic `p`, the arithmetic comparison) and
   **AG.42 lines 4495-4687**: replaced here by my own arguments, not read.
4. The run's audits and AR.8, AR.9 (the equivalence with the emptiness of the exceptional sets): not read.

A caution of another kind: the argument is short. If it is right, it was within reach of the authors who proved
finiteness and worked around the exceptional set. That is a reason to have steps 1 and 2 of section 2 checked by a
second reader before anything is said in public; it is not an objection to any step.

## 4. AG.39 and the literature, from what I know (nothing opened)

- AG.39 is plausible, and the main session's mechanism is the right one. For a set of primes with more than one
  element that is not all primes, a finite quotient of the fibre group can be non-nilpotent, and the base then acts
  on the set of covers of that type through a finite group whose order can involve a prime outside the set. Such a
  quotient of the fibre cannot survive in the completion of the total group, by the same necessary condition I
  used for AG.41 (the action on a surviving finite quotient must be through a group in the class).
- From memory: Mochizuki and Tamagawa (configuration spaces, 2008) state the exactness of the fibration sequence
  for the set of all primes or a single prime. I cannot say from memory which statement of the cuspidalization
  paper of 2007 is worded for an arbitrary set, nor what its 2014 comments change, nor whether Saïdi-Tamagawa's
  proofs use the full prime-to-`p` fibre exactness or only the cuspidally central and abelian quotients (for which
  the action is cyclotomic and exactness is unproblematic). The source check is the main session's.
- If a published proof does rest on full prime-to-`p` exactness, AG.41 is the repair: cuspidally pro-`r` over the
  full proper prime-to-`p` group is exact, and the proof above shows that this quotient is enough for the Kummer
  theory.

## 5. If A1 holds

- **Cote 149, scans 35-36:** the question whether `P = Q` follows is answered yes over finite fields, for the
  prime-to-`p` group, and by the specialization of AR.2 (`A_foundations.tex` 110-133, read) over every finitely
  generated field of characteristic `p`.
- **The mechanism is worth more than the statement.** The punctured-curve group, with its cusp, is determined by
  the decomposition subgroup of the point in `Π_C`, in any quotient where the fibration sequence is exact. That is
  the manuscript's "points as sections" in a usable form, and it is the same shape as the frames in the Longue
  Marche line: data at a point read from a subgroup.
- **Companion:** it may say that over finite fields the prime-to-`p` arithmetic group separates rational points,
  only after item 1 of section 3 is confirmed in the source and a second reader has passed AG.41.
- **SECTIONS_OVER_Q / LM6:** nothing changes in characteristic zero, where injectivity is classical; the fibre
  trick is a tool there too (it turns a coincidence of sections into an isomorphism of punctured groups).
- **A3, A10 (c):** I did not read `A1_downstream_scope_assessment.md` and say nothing on them.

## 6. Items for the next prompt (each to be proved or refuted by the run that uses A1)

- **K1.** Open Saïdi-Tamagawa 2009, Proposition 1.8 (vi), quote it, and prove that it gives what
  `geometric_section.tex` 4024-4033 uses: outside a finite set of closed points, valid over every finite constant
  extension, a decomposition subgroup of `Π_C` belongs to one point only.
- **K2.** Prove (AG.39.15) as used at 3967-3973: for every open subgroup of the geometric cuspidally pro-`r`
  group, the quotient by the cusp inertia groups has as maximal pro-`r` quotient the full pro-`r` group of the
  compactified cover, compatibly with Frobenius.
- **K3.** Write out AG.41 step 3 and the arithmetic comparison (4348-4494): the quotient of the configuration group
  built from the core is a quotient of `E_cr` and dominates the given quotient on the fibre; the statement in
  characteristic `p` by specialization of the tame prime-to-`p` group of `C × C` minus the diagonal.
- **K4.** AG.42 (4495-4687): the cusp decomposition group is the intersection of the fibre with the decomposition
  group of one diagonal component, and that component is the same for `P` and `Q` when their sections coincide.
- **K5.** A finite test of AG.41 by program: for one curve of genus two, one `p`, one `r` and one non-trivial
  prime-to-`p` quotient `A`, compute in the surface braid group that a chosen quotient of the fibre of type
  "`r`-group by `A`" is dominated by a quotient of the configuration group of the stated type.
- **K6.** State AR.3 with its exact hypotheses and derive the emptiness of every exceptional set from it (AR.9),
  with the sets of primes and the fields named.

**Where they go.** They belong to the anabelian line. If ANABELIAN_149_PUSH is still unsent and uses A1, they go
there as its first Part; otherwise into the next consolidated successor of the anabelian cluster. None fits the
Longue Marche prompts.

## 7. Outreach

None from this check. I found no gap in a published proof. Whether AG.39 touches a published statement depends on
the wording in the source, which I have not seen.
