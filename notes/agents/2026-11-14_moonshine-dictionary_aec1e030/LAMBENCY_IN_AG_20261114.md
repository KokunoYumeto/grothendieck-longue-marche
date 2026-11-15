# Lambency, translated into our algebraic-geometric framework

By Claude Fable 5.2 at effort high, 14 November 2026. For the main session (Claude Opus 5.5 at effort max) and the
user. Companion to `MOONSHINE_DICTIONARY_20261114.md` and `GHOST_SYMMETRIES_TRANSLATION_20261114.md` (same folder).

Marks: **[CDH]** = read in Cheng, Duncan, Harvey, *Umbral Moonshine and the Niemeier Lattices*, LaTeX `UMNL_x2.tex`,
place given. **(exact)** = a definition or a computation I can write out. **(mine)** = my identification, checked by
no one. **[memory]** = not checked against a source. **(conj.)** = conjecture.

## 1. What a lambency is

- **Definition [CDH, notation list].** "A lambency. A symbol that encodes a genus zero group Γ^X attached to a
  Niemeier root system X, and thereby also X."
- **The groups [CDH, §2.3, text before Table `tab:Hauptmodul`].** For e ∥ n (e divides n and is prime to n/e) the
  Atkin-Lehner coset W_n(e) consists of the matrices (1/√e)(ae, b; cn, de) of determinant 1. W_n(e)W_n(f) = W_n(e∗f)
  with e∗f = ef/(e,f)². For a subgroup S of the exact divisors, Γ₀(n)+S is the union of the cosets W_n(e), e ∈ S.
- **The 23 lambencies [CDH, Table `tab:Hauptmodul`].**

| Type | Root systems X | Lambency | Γ^X |
|---|---|---|---|
| A | A₁²⁴, A₂¹², A₃⁸, A₄⁶, A₅⁴D₄, A₆⁴, A₇²D₅², A₈³, A₉²D₆, A₁₁D₇E₆, A₁₂², A₁₅D₉, A₁₇E₇, A₂₄ | 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 16, 18, 25 | Γ₀(n), n the Coxeter number: "exactly the positive integers n > 1 for which Γ₀(n) has genus zero" |
| D | D₄⁶, D₆⁴, D₈³, D₁₀E₇², D₁₂², D₁₆E₈, D₂₄ | 6+3, 10+5, 14+7, 18+9, 22+11, 30+15, 46+23 | Γ₀(2n)+n, the even 2n for which this has genus zero |
| E | E₆⁴, E₈³ | 12+4, 30+6,10,15 | Γ₀(12)+4, Γ₀(30)+6,10,15 |

- **The Hauptmodul [CDH, Prop. `prop:TX`].** With π^X the Coxeter Frame shape of X and η_π(τ) = ∏ η(n_iτ)^{k_i},
  T^X = 1/η_{π^X} = q⁻¹ − d^X + O(q), d^X the number of irreducible components of X. Example: π = 4⁸/1⁸ for A₃⁸,
  2⁶6⁶/1⁶3⁶ for D₄⁶, 2³3³5³30³/1³6³10³15³ for E₈³.
- **The index [CDH, §4, Table `ADE1`].** The Jacobi forms have index m = the Coxeter number; the theta components
  are indexed by r mod 2m; the "+e" part appears as the Eichler-Zagier operator: Ω_m(1) for A_{m−1},
  Ω_m(1) + Ω_m(m/2) for D_{m/2+1}, Ω₁₂(1) + Ω₁₂(4) + Ω₁₂(6) for E₆, Ω₃₀(1) + Ω₃₀(6) + Ω₃₀(10) + Ω₃₀(15) for E₈. Ω_m(n)
  is the permutation r ↦ a·r with a ≡ −1 mod 2n, a ≡ 1 mod 2m/n when n ∥ m [CDH (`def:OmegaMatrices`); (exact)].
- **The first paper's lambencies** are the integers ℓ = 2, 3, 4, 5, 7, 13 [CDH, §on lambencies 2, 3, 4, 5, 7, 13].

So a lambency is two things at once: a level n, and a set S of exact divisors of n not containing n itself (the
"non-Fricke" condition of the TASI lectures).

## 2. The translation

### 2.1 The level n: a curve, a stack, a dessin

- **Moduli (exact).** X₀(n) is the coarse space of the multiplicity of pairs (E, C), C a cyclic subgroup of order n
  of the elliptic curve E; equivalently of cyclic isogenies E → E′ of degree n. It is defined over ℚ (over ℤ[1/n] as
  a smooth stack).
- **Dessin over the modular orbifold (exact).** X₀(n) → X(1) is unramified outside j = 0, 1728, ∞. Its darts are the
  points of P¹(ℤ/n); the oriented cartographic group B = C₂ ∗ C₃ acts on them through PSL₂(ℤ/n). Cusps: one for each
  d | n, taken φ(gcd(d, n/d)) times, of width n/(d² ⋅ …) [memory for the width formula]. Orbifold points: the fixed
  darts of s and of r.
- **Dessin over the tripod (exact).** The tripod is Y₀(4) ≅ Y(2) (dictionary, S2). So for 4 | n the map
  X₀(n) → X₀(4) is a dessin in the author's strict sense, a covering of P¹ − {0,1,∞}. The lambencies of this kind
  are 4 (the tripod itself), 8, 12, 16, and 12+4. For the others, X₀(n) becomes a covering of the tripod after
  adding level 2: X₀(n) ×_{X(1)} X(2).
- **Genus zero (exact).** Lambency means X₀(n)+S ≅ P¹ over ℚ, with T^X a coordinate. For prime n, T^X is the modular
  unit with its pole at the cusp ∞ and its zero at the cusp 0: the generator of the units of Y₀(n). Its Kummer
  class along a section is the first invariant of that section on Y₀(n) (mine).

### 2.2 The "+e": hidden symmetries of the curve that are not symmetries of the dessin

- **On moduli (exact).** For e ∥ n write C = C_e × C_{n/e}. W_e sends (E, C) to (E/C_e, (C + E[e])/C_e): replace the
  e-part of the isogeny by its dual. It is an involution of X₀(n), defined over ℚ.
- **It does not commute with j (exact).** j(E/C_e) ≠ j(E) in general. So W_e is not a deck transformation of the
  dessin X₀(n) → X(1). It comes from the commensurator of B in PSL₂(ℝ), not from B. In the author's terms: an
  automorphism of the curve that the cartographic group does not see.
- **The quotient (exact).** X₀(n)+S = X₀(n)/⟨W_e : e ∈ S⟩ is the coarse space of S-symmetrised isogeny
  configurations; for n = p prime, X₀(p)+ is the curve of unordered pairs {E, E′} of p-isogenous curves, the image
  of X₀(p) in the symmetric square of the j-line. It no longer lies over the j-line. Its group Γ₀(n)+S is
  commensurable with the modular group and not contained in it.
- **On cusps (exact).** The Atkin-Lehner group acts on the cusps indexed by d | n by d ↦ e∗d. The full group of
  exact divisors acts simply transitively on the cusps of X₀(n) for squarefree n.
- **For the tripod (exact).** n = 4: W₄ exchanges the cusps ∞ and 0 of X₀(4) and fixes the third. It is one of the
  six automorphisms of P¹ − {0,1,∞}. So on the tripod the only "+e" is part of 𝔖₃, with which ĜT₀ commutes by
  definition. The first hidden symmetry is at level 2: W₂ on X₀(2) conjugates Γ(2) to Γ₀(4), i.e. it is the
  correspondence of 2-isogeny between two copies of the tripod (Landen's transformation) (mine, by conjugating
  with the matrix (0, −1; 2, 0)).

### 2.3 How G_ℚ and ĜT₀ act

- **G_ℚ.** It acts on π̂₁ of Y₀(n) over ℚ̄, i.e. on the completion of Γ₀(n), and this action commutes with every W_e
  up to inner automorphisms, because W_e is defined over ℚ (exact).
- **ĜT₀ preserves the congruence levels (mine, proof sketched).** F sends τ to a conjugate of τ^λ, so the composite
  B̂ → B̂ → PSL₂(ℤ/n) sends τ to a unipotent element of order n. A pair (s̄, r̄) of orders 2 and 3 in PSL₂(ℤ/n) with
  s̄r̄ a given unipotent is unique up to the centralizer of that unipotent: with s̄r̄ = (1,1;0,1), trace zero for s̄
  forces r̄ = (a, a − a² − 1; 1, 1 − a). So the kernel is the same: F preserves Γ̂(n) and the conjugacy class of
  Γ̂₀(n). Hence ĜT₀ acts on the group of every Y₀(n), up to inner automorphisms.
- **The Atkin-Lehner test (mine).** For F ∈ ĜT₀ and e ∥ n put
  AL_{n,e}(F) = [F restricted to Γ̂₀(n), W_e] in the outer automorphisms of Γ̂₀(n).
  It is trivial on G_ℚ. "AL_{n,e}(F) = 1" is an equation on ĜT₀ of the same kind as the read-in's 𝔗_T(F) = F: the
  Galois action commutes with a symmetry of the tower that does not come from the cartographic group.

### 2.4 The "+e" on the theta side is our frame group

The Eichler-Zagier operator of e ∥ m acts on the theta index r mod 2m by the scalar a(e). The scalars a with
a² = 1 modulo 2m (and the Jacobi condition modulo 4m) are central elements of SL₂(ℤ/2m), i.e. diamond operators of
level 2m (ghost note, 2.3). So:

**index m, with its Atkin-Lehner group ↔ level N = 2m, with the centre of SL₂(ℤ/N).**
**Lambency m+S ↔ a subgroup of Ob(2m)·{±1} = Z(SL₂(ℤ/2m)) that does not contain −1.**

For m = 6 (exact): the exact divisors 1, 2, 3, 6 give a = 1, 7, 5, 11. The Atkin-Lehner group of X₀(6) is the
centre {1,5,7,11} of SL₂(ℤ/12); the Fricke involution W₆ is −1; the ghost group Ob(12) is the Atkin-Lehner group
modulo Fricke; its non-trivial element is the class of W₃, which is also the class of W₂. The lambency 6+3 (D₄⁶)
adjoins exactly a representative of that class; the lambency 6 (A₅⁴D₄, the user's lattice) adjoins nothing.

## 3. What the translation buys

### 3.1 Δ gets a curve: X₀(6)

- **The curve (exact; values of the Hauptmodul at the cusps [memory]).** X₀(6) has genus 0, four cusps (widths 1,
  2, 3, 6), no orbifold points; Γ₀(6)/±1 is free of rank 3. So Y₀(6) is P¹ minus four rational points: a rational
  point of M_{0,4}, with λ = 9 (or 1/9, −8, …). The Atkin-Lehner group is the Klein four-group of that
  four-punctured sphere, acting simply transitively on the punctures. The elliptic curve that is the double cover
  branched at the four cusps has j = 2²·73³/3⁴, in the isogeny class of conductor 24 **[memory]**.
- **Δ as a failure of Atkin-Lehner equivariance (conj., mine).** For F ∈ ĜT₀:
  Δ(F) = 0 if and only if F restricted to Γ̂₀(6) commutes with W₃ (equivalently with W₂) in the outer automorphism
  group. On G_ℚ both sides hold. In the user's terms: W₃ and W₂ are the two local signs (at 3 and at 2), their
  product W₆ is the global sign, and Δ is whether F treats the two alike.
- **The pentagon enters here (mine).** The group of Y₀(6) is free of rank 3 with four cusp classes: it is
  isomorphic to the kernel of Γ̂_{0,5} → Γ̂_{0,4}, the group of the fibre of M_{0,5} → M_{0,4}, and Y₀(6) is that fibre
  over the rational point λ = 9. The Klein four-group is the image of V₄ = ker(Γ_{0,[4]} → B), which acts on every
  four-punctured sphere. So the same curve sits in the Teichmüller tower in two ways: as a dessin (a subgroup of B̂,
  where ĜT₀ acts) and as a fibre over a rational point of M_{0,4} (where ĜT acts on the family, through the
  pentagon). A Galois element acts compatibly in both. Hunch: the compatibility of the two actions is what the
  five-cycle relation adds to ĜT₀ at this level, and it implies Δ = 0 on ĜT. This is the same statement as GS2 of
  the ghost note, seen on a curve.

### 3.2 The whole family Δ_N in these terms

Ob(N) for N = 2m is the Atkin-Lehner group of level m modulo Fricke. So the characters Δ_N of the ghost note are
"Atkin-Lehner defects" of F on X₀(m), and the 23 lambencies are 23 choices of (level, a subgroup of signs that does
not contain the global one). The E₈³ case 30+6,10,15 is the full group Ob(60) of relative signs among 2, 3, 5 (three
primes: order 4) (exact); these are the three primes of the icosahedral problem.

### 3.3 Level 5 and the tripod

- **Lambency 5 (exact).** X₀(5) has genus 0, two cusps (widths 1 and 5), two points of order 2, none of order 3. It
  is the icosahedron divided by the dihedral group of an axis: the two poles give the cusp of width 1, the other ten
  vertices the cusp of width 5. Its six darts are the six axes. The umbral group GL₂(5)/2 is the group of X(5) over
  X(1) with its arithmetic part (dictionary, S1). Level 5 is the only A-type lambency whose level equals the prime
  of its components.
- **Lambency 4 (exact).** The tripod. The lambencies 8, 12, 16 and 12+4 are dessins over it of degrees 2, 4, 4.
  A₁₁D₇E₆ (lambency 12) is the degree-4 dessin X₀(12) → X₀(4), and E₆⁴ is its quotient by W₄.

### 3.4 What it changes for the stuck items

- **E.3 (Δ on ĜT)** becomes a statement about one explicit four-punctured sphere over ℚ and its Klein four-group.
- **Tripod sections.** A section of the tripod gives, through X₀(4n) → X₀(4), sections of the genus-zero curves of
  lambencies 8, 12, 16 over finite extensions, and on each the Kummer classes of the units T^X. On X₀(n)+S there is
  one cusp where X₀(n) has several (for S the whole non-Fricke group and squarefree n the cusps are identified in
  pairs or more), which is the move of the dictionary's 4.4 (one cusp label).
- **The icosahedral centralizer.** No direct gain: lambency 5 has no "+e", in agreement with the ghost note's 3.3
  (no sign in that problem).

## 4. Items for GPT-6 Astra (ChatGPT Pro mode)

**L1. ĜT₀ on the congruence tower.** Join: LM8_PUSH Part C. Prove or refute: every F ∈ ĜT₀ preserves Γ̂(n) for every
n and the conjugacy class of Γ̂₀(n); the induced automorphism of PSL₂(ℤ/n) is conjugation by an element of PGL₂(ℤ/n)
of determinant λ(F); describe the induced map ĜT₀ → PGL₂(Ẑ) and its kernel (the congruence ghosts).

**L2. The Atkin-Lehner defect.** Join: the LM7 continuation, with E.3. Prove or refute: (a) AL_{n,e}(F) is
well defined and trivial on G_ℚ; (b) for n = 6, AL_{6,3}(F) = 1 if and only if Δ(F) = 0, and AL_{6,6}(F) = 1 for every
F; (c) for every squarefree m, the defects AL_{m,e} are the characters Δ_{2m} of the ghost note; (d) the element of
E.58 has AL_{6,3} ≠ 1, computed on the four cusps of X₀(6) and on a free basis of Γ₀(6)/±1.

**L3. Two places of X₀(6) in the tower.** Join: the same. Prove or refute: (a) Y₀(6) is P¹ minus four rational
points with λ = 9 up to the six values, with the explicit Hauptmodul and the Atkin-Lehner involutions as Möbius
maps; (b) the identification of Γ̂₀(6) with the fibre group of Γ̂_{0,5} → Γ̂_{0,4} over that point, under which the
Atkin-Lehner group is the image of V₄; (c) for σ ∈ G_ℚ the two actions agree; (d) for F ∈ ĜT, the five-cycle relation
gives the same agreement up to the section at λ = 9, and hence AL_{6,3}(F) = 1; or an element of ĜT for which it
fails.

**L4. Lambencies as dessins.** Join: EXIT_TOWER or the companion. Compute for each of the 23 lambencies: the
dessin of X₀(n) over the modular orbifold (passport, cusps with widths, orbifold points), its form over the tripod,
the action of S on cusps, the signature of Γ₀(n)+S, and the field of definition of each cusp; check the table
against T^X = 1/η_{π^X}.

## 5. What this rests on

Read: the CDH LaTeX at the places cited (tables at lines 713-790 and 815-860, exact divisors at 646-690, the Ω
matrices at 1103-1128, Table `ADE1`, the notation list). Not read: the first umbral paper; Conway-Norton; any source
for X₀(6) (its cusps, Hauptmodul and the curve of conductor 24 are from memory). The correspondence "Eichler-Zagier
operator of e on index m = scalar a(e) on r mod 2m" is exact from CDH's definition; that this scalar is the central
element of our frames rests on the ghost note's reading of our intakes.
