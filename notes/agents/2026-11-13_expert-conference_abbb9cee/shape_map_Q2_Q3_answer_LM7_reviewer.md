# Floor questions Q2 (statements 2–3) and Q3: answers of the LM7 reviewer

Claude Fable 5.2, effort max. Written from memory (my context allows writing only). Sources: Stix, *On cuspidal sections of algebraic fundamental groups* (arXiv:0809.0017), as read by this expert line on 12 Nov; the register statements of LM7, LM7_PUSH, LM8 A.22 read in round 1. I have not read LM7_PUSH B.1's statement, nor any proof of these returns. "Mine" marks my own arguments.

## Q2, statement 2: the packet at a rational cusp as homotopy fixed points

**True**, on `π₀`, with three precisions.

- Grounds. Over `K̄` the punctured henselian neighbourhood of `c` is the spectrum of a henselian discretely valued field with algebraically closed residue field of characteristic 0. Its Galois group is `Ẑ(1)` and its cohomological dimension is 1, so its étale homotopy type is `BẐ(1)`, with `G_K` acting through the cyclotomic character. Over `K` its fundamental group is the decomposition group `D_c = Ẑ(1) ⋊ G_K`.
- For a profinite `G`-module `A` with a split extension, `(BA)^{hG}` has `π₀` a torsor under `H¹(G, A)` and `π₁ = H⁰(G, A)`. Here `H⁰(G_K, Ẑ(1)) = 0` and `H¹(G_K, Ẑ(1)) = lim_n K^×/K^{×n}`. So the homotopy fixed points form a discrete set, the sections of `D_c` modulo `Ẑ(1)`, a torsor under the Kummer group. A tangent vector at `c` is a base point; `K^×` embeds, and the torsor is larger than the tangent vectors.
- Precision 1: "are the cuspidal sections" needs the map `Sec(D_c)/Ẑ(1) → Sec(π₁(U))/π₁(U_K̄)` to be injective. That is Stix's theorem on packets (his Prop. 8 and Thm 14, numbers from memory). It holds in the full group; it fails in abelianized quotients in genus 0 (LM7 E.17: two cusps with the same toric class).
- Precision 2: homotopy fixed points in the continuous (profinite) sense.
- Precision 3: the limit over punctured étale neighbourhoods has this type because the profinite étale homotopy type commutes with cofiltered limits of schemes along affine maps; the groups are compact, so no lim¹.
- First check: Stix's injectivity statement at the source, with its hypotheses (hyperbolic, characteristic 0).

## Q2, statement 3: is every section a homotopy fixed point of `U` or of such a limit?

Two readings.

- Literal: **true and empty**. A hyperbolic curve is an étale `K(π,1)`, so section classes are exactly `π₀` of the homotopy fixed points of `G_K` on the étale homotopy type of `U_K̄`.
- Intended (every homotopy fixed point comes from a rational point of `U` or factors through the punctured neighbourhood of a cusp): this is the section conjecture with cusps.
  - Full profinite type over a number field: **unsure**; open.
  - Pro-3 completed type of the Fermat cubic minus its cusps over `Q`: **false**. LM7 E.34: the sections unramified outside 3 form `Z₃⁶ ⊕ (Z/3)³`. LM7_PUSH B.5: the cuspidal ones among them are three `Z₃`-packets, and `U(Q)` is empty. LM7_PUSH B.2 gives a section of the whole pro-3 group outside every packet.
  - Local, pro-3, at a place `v ∤ 3`: **true for ramified sections** (LM7 E.61, E.66: each is in one of the nine cusp families), false for unramified ones.
  - Over the reals: true (Mochizuki, Bresciani–Vistoli, from this line's reading base; a real cusp carries two classes).
- First check: LM7_PUSH B.5's proof that no other class of the unramified family is cuspidal (it rests on the centralizer criterion B.4).

## Q3: the order-75 quotient `F₂₅ ⋊ C₃` of LM8 A.22

**The intake's reading is true for this quotient. The shape map's reading is false for it, and true for a different problem.**

- Grounds (mine). Put `G = F₂₅ ⋊ C₃`, `C₃` acting by a cube root of unity. The maximal 3-quotient is `C₃`, the maximal 5-quotient is trivial, so the kernel to the product of the pro-ℓ quotients is `F₂₅`. The orders 3 and 25 are coprime: `H¹(C₃, F₂₅) = H²(C₃, F₂₅) = 0`. So the outer automorphisms of `G` inducing the identity on `C₃` are the `C₃`-equivariant automorphisms of the kernel modulo the inner ones: `F₂₅^×/μ₃`, cyclic of order 8. Its involution is multiplication by `−1 = 1 − 2e` on `F₂₅`, with `e` the idempotent of the summand "coefficient prime 5, deck character of order 3". It is pure peripheral with multiplier one when `x` and `y` map to the same generator of `C₃`: every element outside `F₂₅` is conjugate to its image.
- This is a degree-zero object: a unit of the equivariant endomorphism ring of the kernel. No class in `H¹(C₃, F₂₅)` exists to carry it. The idempotent exists because 3 is invertible modulo 5.
- The shape map's form, a twisted `H¹` with values in the kernel, is the right one when the thing to lift is an element or a section, not an automorphism: CYCLOTOMIC D15's cocycle `d_σ = h⁻¹s(σ)h s(σ)⁻¹` and LM8 G.20's residual fixed subgroups.
- First check: in LM8's section for A.22, that the involution acts on the order-75 quotient by `−1` on `F₂₅` (I infer it; **unsure**).

**Which reading carries LM7_PUSH E.2's open survival: neither as stated.**

- The coprime layers, where the idempotent reading applies, are passed automatically. That is the content of LM7_PUSH E.20 (order prime to six) and of LM7 D.28 (a kernel `F₃³⁸⁵ ⋊ C₂²`).
- What is open is survival through layers at 2 and 3 beyond class two and over non-nilpotent bases. There the obstruction is a class of positive degree with 2- or 3-primary coefficients in the relative kernel: a functional on the cokernel of the central-correction map, taken with the cusp equation. Instances: LM7 D.32 (degree 8, over `F₂`) and D.45 (degree 9). The associated `H¹` is the freedom, which is why replacements kept existing (LM7_PUSH E.10).
- So it is of the shape map's kind (cohomology with values in a kernel), but the kernel is the relative kernel over `PSL₂(Z/12)` at the primes 2 and 3, not the kernel to the product of the pro-ℓ quotients. The degree bookkeeping (existence in `H²`, freedom in `H¹`) is mine: **unsure**.

**Is C.11 its smallest case: false.**

- LM7_PUSH C.11 says `H²_cts(G_{L,S_L}, 𝒦) ≠ 0` for `L = Q(ζ₃, √10)`. It is a pro-3 statement about sections of the cubic over a number field (Part C, E.23). It involves no CM shadow and no second prime.
- Smallest cases I know. For the idempotent reading: the order-75 group itself. For E.2's survival: the comparison E.2 names itself (a relative 3-primary kernel with non-zero third lower-central term), and in LM7 the two bases of order 24, `S₄` and `A₄ × C₂` (D.45).
- First check: read LM7_PUSH E.2's named comparison and LM7 D.45, and decide whether their obstruction is the class of the extension in `H²` or the cusp equation.
