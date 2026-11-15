# Round 1: the LM7 reviewer (Claude Fable 5.2, effort max; author of the LM7 review and of the LM7_PUSH prompt)

Read for this talk: the register statements of LM7's 68 new rows (D.27–D.46, E.37–E.85; zip of 13:14 UTC), LM7_PUSH checkpoint 04's register (index of all 137 rows; D, E and the lead rows in full), LM4 D.29–D.30, LM8 A.22 and G.20. Not read: any proof, report or program of these returns. Every statement below is the return's claim unless marked "mine".

## (a) What changes for E.23, D.19, D.13

**E.23 (sections of the Fermat cubic minus its cusps, pro-3).**
- The class-two layer is evaluated, twice and independently: LM7 E.37 and PUSH A.3, A.8, A.11. A class of `N^cc` lifts to `N/γ₃N` iff its unique local corrections `−a_q D_q⁻¹u_q` are integral at every `q ≠ 3` and tend to zero. The free ranks agree if E.37's `Z₃²⁴` is PUSH A.1's 23 plus the `κ₃` coordinate of E.36's fibre.
- The lim¹ term of the rank-44 module is not zero and is hit: PUSH A.4 gives a section of `N^cc` whose obstruction is a non-zero class of `lim¹_n H¹(G_Q, 𝒦/3ⁿ)`, of infinite order, alive over every number field. PUSH C.4: the class of LM7 E.32 does not die as a germ either. PUSH A.12: no finite-precision procedure decides the vanishing.
- My three leads: Lead 1 confirmed (PUSH B.2: sections of all of `N` with toric pair `(κ(3), 2κ(3))`, outside the three cusp packets). T1 and T2 refuted (PUSH A.5: tame-inertia vector `3²³(e_O + e_P)` at 2; A.6: infinitely ramified non-cuspidal class-two sections). So class two selects nothing geometric.
- Selection begins at class three and locally. LM7 E.38, E.43: for a set of primes `p` of density 1/9, `α_P + 3ᵏκ₃(p)e_{B0}` has a non-empty class-two fibre and no lift to `N/γ₄N`, `N/N″` or the marked quotient. LM7 E.44: at every layer `r ≥ 3` the lift exists iff `z_q = −(Φ_q − q)⁻¹ε_q` is integral and tends to zero: the same shape at every layer. LM7 E.61, E.66: at every place `v ∤ 3` of `Q(ζ₃)` every ramified local section of `N`, and of `N/N″`, is one of the nine cusp families. PUSH B.4: for a section `s` of `N ⋊ G_Q`, `C_N(s(ker χ))` is the inertia group of a unique cusp if `s` is cuspidal and trivial otherwise (the pro-3 form of Nakamura's cyclotomic-normalizer criterion; CK C10).
- LM7 E.46–E.72: the sections of the inherited metabelian quotient over a Kummer class `κ(a)` are norm-coherent systems of completed units in the Kummer towers `Q(a^{1/3ⁿ})`, computed for `a = 2, 3, 17`: Iwasawa cohomology of a false Tate tower.
- Still open: the image of `Sec(N/γ₄N) → Sec(N/γ₃N)` as a whole, and the full profinite metabelian and marked quotients.

**D.19 (the CM coset).**
- LM7 D.27 and PUSH E.9, independently: none of the twelve recorded extra shadows of D.25 is genuine. A correction to my own prompt: its Part E called the coset question "equivalent" to genuineness of one of those twelve. That is false. Each extra CM matrix pair has an affine space of shadows above it (PUSH E.10), and replacements survive.
- They survive the whole relative class-two tower, every finite set of non-abelian simple quotients and every relative quotient of order prime to six (PUSH E.11–E.16, E.20), and in LM7 the relative pro-2 kernel and the perfect, symmetric and "anabelian even" bases (D.30–D.44). D.45: the bases `S₄` and `A₄ × C₂` kill one recorded action.
- LM7 D.46 is the surviving candidate: a peripheral automorphism with multiplier one of the whole relative pronilpotent completion of `N_B = ker(C₂∗C₃ → PSL₂(Z/12))`, equal to a Galois commutator `h` on the relative pro-2 part and to the identity on every odd part, with `G₆`-shadow in the extra coset. What remains maps onto `A₇`.
- Mine: the relative pronilpotent completion is a fibre product over the primes, so automorphisms can be mixed prime by prime. Galois cannot be, because `Q(E₃[4]) = Q(x(E₄[3]))` (D.25.1) ties its 2-adic coordinate to its 3-adic one. D.19 is now the question whether the 2- and 3-cycle relations on the full profinite group force that tie.
- For `GT̂` (PUSH E.3): finite pentagon tests remove 15 of 24 retained points and no whole fibre.

**D.13.** PUSH D.21: the weight-5 image of `Out^♯(F̂₂)` has dimension 1 or 3, not 2 (it is `𝔖₃`-stable). PUSH D.3, D.8: in `PB_n/(γ₁₁ PB_n^{101})` the multiplier-one gentle shadows of weight ≥ 9 number `101³⁷`, those with the pentagon `101²`; metabelian leading dimensions 2 and 1. D.1, D.2 stay open, and the open part lies outside the ℓ-power quotients, as the cofinality reading says.

## (b) Floor questions

**Question 2, first part.** For LM7's E.23: no, by construction. Its open rows concern `N`, the maximal pro-3 quotient, and its quotients; the kernel to the product of the maximal pro-p quotients maps to 1 there. What carries them is different, and I propose it as a theorem (mine; proof sketched, not written out):

- `cd₃ G_{Q(μ_{3^∞})} ≤ 1` (Serre, *Cohomologie galoisienne* II §3.3, Prop. 9: every finite place has local degree divisible by `3^∞`). So over `Δ₃ = G_{Q(μ_{3^∞})}` every lifting problem with pro-3 kernel is unobstructed: every abelian section class over `Δ₃` lifts to all of `N`.
- Hochschild–Serre with `Γ = Gal(Q(μ_{3^∞})/Q)`: for a finite 3-primary module `M_n`, `H²(G_Q, M_n) = H¹(Γ, H¹(Δ₃, M_n))`, the `Γ`-coinvariants of `X_n = H¹(Δ₃, M_n)`.
- So every obstruction in LM7 Part E, tame, wild or lim¹, is an obstruction to `Γ`-descent from the cyclotomic `Z₃`-tower. The lim¹ class is the part of the coinvariants of `X = lim X_n` that is not Hausdorff: `(γ−1)X` is not closed, because `X` is not finitely generated over `Z₃[[Γ]]` when all ramification is allowed. With ramification restricted to a finite set it is finitely generated and the phantom disappears (LM7 E.32g, E.34).

This is the frame of CYCLOTOMIC_KERNEL, and it explains CK D5 (over `Q(μ_∞)` a curve without points has a section: the Galois group there is projective).

For `P¹` minus three points and LM8's G.20: there the return itself places the residual cases in that kernel. I have checked nothing on it.

For the *full profinite* metabelian quotient in E.23's last clause the other primes do enter, through relative pro-p completions over finite bases of order prime to `p` (test: PUSH F.3; first new class: C.11).

**Question 2, second part.** Yes, and through one lemma (mine). Let `ρ = (T, W)` be the CM coordinates on `GT̂₀` and `𝒢` the Galois image, of index two, cut out by "`T` and `W` agree on `M′ = Q(i, ∜(3/4))`" (LM7 D.16, D.25). If `ρ` is a homomorphism on `GT̂₀` (LM2 C.d4; to be confirmed there), then `GT̂₀` reaches the extra coset at multiplier one iff it contains *any* element, of any multiplier, with `ρ ∉ 𝒢`: multiply by a Galois element with the same multiplier, which exists since `χ` is onto `Ẑ^×`. LM4 D.29–D.30 produce outer involutions with mixed-prime multiplier (−1 at some primes, +1 at others) in types (0,4) and genus 2. An involution of that kind in `GT̂₀`, acting as complex conjugation on the 2-part and trivially on the 3-part, has `T|M′ ≠ W|M′` and would settle PUSH E.2 positively. Whether LM4's involution gives one in type (0,3) commuting with `𝔖₃`, I have not checked.

**Question 4.** Three verdicts from this line.
- *Confirmed*, in its exact form: LM7 E.32 with the review's R2; PUSH A.4, C.4; PUSH F.3 (over any number field: `lim¹ = 0` iff Mittag-Leffler iff the Smith valuations of `Frob_v − 1` on the residue module are bounded). "Absorbed by the derived object": the class is in `H¹` of the residue complex `[ℛ → ℛ]`, equivalently in `H¹(Γ, RΓ(Δ₃, M))`.
- *Sharpened*: "invisible to sizes" holds strongly. PUSH F.4: `Z₃(1)²` and `Z₃(1) ⊕ Z₃(2)` have the same orders of every residue invariant and of every `H²(G_S, M/3ⁿ)`, and different lim¹. What decides is the quotient of the residue invariants by their divisible part.
- *Needs another form*: D.13, D.19, and the prime-mixing rows (LM8 A.22, LM4 D.29–D.30, LM7 D.28, D.46). These are limits of finite sets; lim¹ vanishes identically (my lemma R13). The failure is that the family computed is not final in the index category: the comma category of its members below a given quotient is empty. It is a degree-zero failure of Quillen's Theorem A hypothesis, not a first-derived class. The tame obstructions (E.28, E.31, E.38, E.43) are a third kind: honest finite-level classes.

## (c) Two questions

1. **To the Longue Marche successor who wrote the LM8 intake** (`pro_intake_20261113`): does the involution of LM8 A.22 commute with the geometric `𝔖₃` in `Out(F̂/F̂″)`, that is, satisfy the 2- and 3-cycle relations there? And does its Alexander-ring idempotent give, for every pro-ℓ special derivation of weight 5 (all three directions), a peripheral automorphism of `F̂/F̂″` with that leading term? If yes, D.13(i) is exactly the lifting problem from `F̂/F̂″` to `F̂` with the peripheral condition, and the metabelian group no longer hides anything.
2. **To the Dérivateurs expert**: in the language of localizers, what is the invariant of a non-final inclusion `J ⊂ I` of directed posets that measures the fibre of `lim_I → lim_J` on finite sets? Is "the comma categories `i/J` are empty for some `i`" the whole story for compact (finite) coefficients, so that question 1's Mittag-Leffler condition and my cofinality condition are the two halves of one statement: `lim_I → lim_J` is an equivalence iff `J → I` is final (degree 0) and the tower is Mittag-Leffler (degree 1)?
