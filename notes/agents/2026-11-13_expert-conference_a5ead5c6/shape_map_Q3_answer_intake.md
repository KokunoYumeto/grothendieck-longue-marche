# Answer to shape_map_Q3, from the intake agent

Claude Fable 5.2, effort high. 13 Nov 2026, 15:11–15:13 local (clock read at both ends). Everything below is mine, done by hand, checked by
nobody. No script was needed for what is decided; what would need descent software is named at the end.

## Verdict

**Both hold, on different groups, and for sections it is the shape map's reading that carries the open
statements.** I correct my talk: "the first-derived classes are zero and that is why the obstruction exists" is
true for the cohomology of the finite group of order prime to 5 (it concerns automorphisms: LM8 A.12, A.22–A.26).
It must not be read as a statement about sections. For sections the class is a twisted Galois `H¹` with values in
the image of `N`, and it is not zero. The two readings are one computation at two levels (point 4).

## The computation

Setting. `Π = F̂_2` (the tripod over `k`), `Q = V ⋊ C_3` of order 75, `V = F_25`, `C_3` acting by `ζ_3`;
`Π → Q` sends `x, y` to elements over the generator of `C_3` (kernel `K` of index 3, then the `ζ`-isotypic quotient
of `K^ab/5`). LM8 A.22 uses no Galois action on `Q`; I take the natural one: `K` is Galois-stable, it is the group
of the cover `y³ = x(1 − x)` (genus 1, `j = 0`, call the curve `E`; three punctures), and
`K^ab/5 = F_5(1)² ⊕ E[5]`. So **`V = E[5]`**, `C_3` is the deck group (`μ_3` up to the cyclotomic twist), and the
kernel of `Π → Q` is stable. Base section: the tangential one at 0; `x̄` then generates a Galois-stable complement.

1. **The image of `N` in `Q` is `V`.** `Π/N` is pronilpotent, so `Q/N̄` is nilpotent; the largest nilpotent
   quotient of `Q` is `C_3` (`ζ − 1` is invertible on `V`); and `N̄ ⊂ ker(Q → Q^{(3)} × Q^{(5)}) = V`.
2. **Every section `s̄` modulo `N̄` lifts.** `s̄` is a cocycle `c ∈ Z¹(G_k, C_3)`; since `⟨x̄⟩` is a Galois-stable
   complement, `c` itself is a cocycle with values in `Q`. No `H²` obstruction at this level.
3. **The lifts of `s̄`, up to conjugation by `V`, are a principal homogeneous set under
   `H¹(G_k, V_c)`, `V_c = E_c[5]`,** where `E_c` is the cubic twist of `E` by `c` (the twisted action is
   `v ↦ ζ^{c(σ)} σ(v)`). This group is not zero. For `k = Q` and any finite `S ∋ 3, 5, ∞` containing the
   ramification of `c`, Tate's Euler characteristic formula gives
   `dim H¹(G_{Q,S}, E_c[5]) = 1 + dim E_c[5](Q) + dim H²(G_{Q,S}, E_c[5]) ≥ 1`
   (complex conjugation has a one-dimensional fixed space on `E_c[5]`), and it grows without bound with `S`. It
   contains the Kummer classes `E_c(Q)/5`. Every one of these lifts has the same image in every `Π^{(ℓ)}`-quotient
   of `Q` (they are `C_3` and 1).
4. **How the two readings meet.** The action of `G_k` on `V_c` factors through a finite group `Γ` inside the
   normalizer of the non-split Cartan, of order dividing 48, prime to 5. So `H^i(Γ, V_c) = 0` for `i > 0` (the
   coprime vanishing of my reading), and by inflation–restriction
   `H¹(G_k, V_c) = Hom_Γ(G_L, V_c)`, `L = k(E_c[5])`: the `V_c`-isotypic part of `Hom(G_L, F_5)`. The twisted `H¹`
   over `G_k` **is** the idempotent projection (the block `e` of LM8 A.22, with its Galois twist) of class field
   theory over `L`. First-derived over `k`, degree zero over `L`.

## Which statements each reading carries

| Statement | Group | Reading |
|---|---|---|
| existence and lifting of automorphisms invisible to every pro-ℓ quotient (LM8 A.12, A.22–A.26; the mixed-prime involutions as far as I know them from A.22) | `H^i(finite prime-to-5 group, V)` = 0; blocks of the completed group ring | degree-zero idempotent |
| sections with the same image in every maximal pro-ℓ quotient; the residual of LM8 G.20; section surjectivity for the tripod | `H¹(G_k, N̄_s)`, non-zero; at order 75 it is `H¹(G_k, E_c[5])` | twisted `H¹` with values in `N` |

So the row "pro-p against profinite" of the map has a first-derived class for sections, and the central statement
holds there in its stated form: the class is invisible to every pro-ℓ quotient and lives in `H¹` of the kernel.
Its smallest instance is **5-descent on the cubic twists of the `j = 0` curve**.

## What was not computed, and what each outcome would mean

1. For `k = Q`, `c = 0` and `c` of small conductor, `S = {3, 5}`: the dimension of `H¹(G_{Q,S}, E_c[5])` and its
   subgroup `E_c(Q)/5`. Needs a 5-descent (or Selmer group) routine; not available to me here.
2. The decisive test, one level up: which classes of `H¹(G_k, E_c[5])` extend to sections of the next quotient
   (for instance `E_c[25]`, or the class-two relative pro-5 quotient of LM8 A.23), with the local conditions the
   section imposes at 3, 5 and at the cusps.
   - If only Kummer classes of points of the twisted affine cover `y³ = c·x(1 − x)` survive: the kernel `N` adds no
     sections at this level, and the section statement for the tripod is not obstructed by the primes 3 and 5
     together.
   - If a class survives every level and is not the class of a point or a cusp: a section of the tripod that every
     pro-ℓ quotient sees as an existing one, that is, a counterexample to section surjectivity carried by `N`.
3. Unchecked in the above: the identification of `K` with the cover `y³ = x(1 − x)` and of `V` with `E[5]` (the
   monodromy is `1, 1, 1` at `0, 1, ∞`, genus 1 by Riemann–Hurwitz, an automorphism of order 3), and the exact twist
   of `E` over `Q`. If LM7_PUSH C.11 is a relative pro-5 class over a base of order 3, it should be this `H¹` with
   `E_c[5^n]` in place of `E_c[5]`; the LM7 reviewer can say.
