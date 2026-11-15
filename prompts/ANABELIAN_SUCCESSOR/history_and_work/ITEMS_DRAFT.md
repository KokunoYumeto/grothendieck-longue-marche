# ANABELIAN_SUCCESSOR: items draft (mathematics only)

Drafted by Claude Fable 5.2 at effort high (the intake agent of ANABELIAN_149_PUSH and LM6), 14 November 2026,
debate round 1; brought up to date in round 2 (17:26–17:45 UTC) with the papers of the manuscript, cross-run and
Fermat participants, the notes of the two field experts (all Claude Fable 5.2, at effort max or high as their
papers say) and the moonshine dictionary. The state before round 2 is
`ITEMS_DRAFT_before_intake_round2_20261114.md`. The main session (Claude Opus 5.5 at effort max) adds the
procedural frame (outcome rules, checks, checkpoints, attachments). Successor of ANABELIAN_149_PUSH (GPT-6 Astra,
ChatGPT Pro mode; final return of 14 November 2026, 221 statements) for Part A (scans 35–36 of cote 149) and item
F2 (scan 52). Its Part D goes to the prompt SECTIONS_OVER_Q. Statements of that return are cited as AP-‹id›.
Every lead below is unchecked by a second reader unless it says otherwise; its author is named.

## What is to be settled

First, and with most of the time: whether two distinct rational points of a smooth proper curve of genus ≥ 2 over
a finite field can have conjugate sections in the geometrically prime-to-`p` fundamental group (Part A). Then the
reconstruction of schemes from their étale topoi as he states it on scan 52, and the fields over which it holds
(Part F).

## His text (second-pass readings of 13 November 2026)

- Scan 34: "si on omet `p`, alors la translation par un point d'ordre `p` donne un contre-exemple".
- Scan 35: "Mais validité sous cette forme du th. 3 ou [en] de son cor. en car. `p>0` nous fait une belle jambe —
  car pour être à l'aise [l'air], il faudrait pouvoir le prouver dans les contextes des groupes fondamentaux
  « premiers à `p` ». Or dans ce contexte, déjà dans le cas d'une courbe elliptique `Y` … l'injectivité de (**)
  est fausse." Margin: "O.K. en se remplaçant d'abord `K` par un [anneau] de type fini sur `F_p`, puis en se
  ramenant au cas d'un corps fini parfait."
- Scan 36: "Il est cependant possible que l'injectivité de (*) reste valable sans hyp. de caractéristique — à
  examiner de plus près…"; "non seulement `Q − P` est un élément de `p`-torsion de la jacobienne gén. `G_Y` de `Y`,
  pour tt rev. étale galoisien fini `Y'` de `X` [his slip for `Y`], de degré premier à `p`, pointé par un `P'` au
  dessus de `P`, il existe `Q'` au dessus de `Q` tel que `Q' − P'` soit un élément de `p`-torsion de `G_{Y'}`. Il se
  pourrait qu'on puisse en déduire `P = Q`." A struck line below tried the covers by the isogenies `_nG`. Margin:
  "ceci montre que le th. 2 reste vrai, sur un corps de base de car. `p>0`, en travaillant avec les groupes
  fondamentaux premiers à `p` — car … on peut supposer que `Y` est un produit de courbes de genre zéro."
- Scans 6–8: for a field that is not finitely generated, "le 2-foncteur `K ↦ B_K` … est cependant loin d'être
  fidèle", and one takes "le système projectif des `B_{K_i}`" over the finitely generated subfields, which "va avoir
  toutes les propriétés de fidélité" of the finitely generated case.
- Scan 52: "Pour un schéma de base `S` loc. noeth. donné, le foncteur `X ⟶ X_et`, allant de la catégorie des schémas
  réduits loc. de prés. finie sur `S`, vers la 2-catégorie des topos au dessus de `X_et` [his slip for `S_et`], est
  1-fidèle … et même peut-être pleinement fidèle, quand on passe à la catégorie des fractions … obtenue en rendant
  inv. les homéom. universels… Expérimenter ceci p.ex. pour les autom d'une courbe alg. propre sur une ext. finie
  de `Q`, en retrouvant le « fait » que tout autom ext. de `E_K` (`K` le corps des fonctions de `X`) qui respecte
  la structure à lacets et qui commute à l'action de `Γ`, provient d'un autom de `X`". Margin: "`S` de car. 0 ?".

## Conventions

`k` a finite field of characteristic `p`, `C/k` smooth proper geometrically connected of genus `g ≥ 2`,
`E_C^(p′) → G_k` the geometrically prime-to-`p` group, `s_P` the section of `P ∈ C(k)`. A *collision* is a pair
`P ≠ Q` in `C(k)` with `s_P`, `s_Q` conjugate under the geometric group. A cover is *`P`-pointed over `L`* when it
is defined over the finite field `L ⊇ k` with a chosen `L`-rational point over `P`. For a character
`χ : J_C(L) → Z/n`, `D_χ → C_L` is the pull-back, by the Abel map based at `P`, of the quotient of the Lang
isogeny of `J_C` over `L` cut out by `χ`: a `Z/n`-torsor with rational deck group in which `P` splits completely
(class field theory: these are the `P`-split unramified abelian covers over `L`). `L_P(χ, T)` is its twisted
`L`-function. `h(D)` is the class number `#J_D(L)`. `P_n(D) = im ∏_{ℓ∣n}(1 − σ^{n/ℓ}) ⊂ J_D` is the primitive
part. *Reconstruction over a field `k₀`* means: for all finite-type `k₀`-schemes `X, Y`,
`Hom_{k₀}(X^awn, Y) → π₀ Hom^cp_{BG_{k₀}}(X_ét, Y_ét)` is bijective, where `X^awn` is the absolute weak
normalization and `Hom^cp` the morphisms of topoi over `BG_{k₀}` that send closed points to closed points
(Carlson–Haine–Wolf, Definition 2.19: this is their "pinned"). The reading "a morphism given with its commutation
isomorphism", used in the prompt of ANABELIAN_149_PUSH, is wrong.

## Results this builds on (confirm each where used, or give the exact error)

- **R1** (AP-A.1, AP-A.2, AP-A.3; proofs followed by the intake). A collision gives, on every finite étale cover
  `D → C_L` with geometrically prime-to-`p` Galois closure and every `P′ ∈ D(L)` over `P`, a point `Q′ ∈ D(L)` over
  `Q` with `[Q′ − P′] ∈ J_D(L)[p^∞]`; it is the only point over `Q` with a `p`-primary difference; and the
  condition for all such covers is equivalent to the collision. So his covering condition of scan 36 is the
  collision, and "en déduire `P = Q`" is A1.
- **R2** (AP-A.C2.7; proof followed). If a deck transformation `δ ≠ 1` of odd order of a Galois cover as in R1 fixes
  `T = [Q′ − P′]`, then `D` is hyperelliptic, which a free automorphism of odd prime order excludes.
- **R3** (AP-A.10; AP-A.C2.19, AP-A.C2.20, proofs followed). A prime-to-`p` étale cover with jointly
  point-separating maps to abelian varieties of `p`-rank zero excludes a collision. If `C` has, geometrically, a
  connected cyclic étale cover of odd degree `n` prime to `p` with `f_p(P_n) = 0`, there is no collision on `C`:
  `A·T = 0` for `A = ∏_{ℓ∣n}(1 − σ^{n/ℓ})` gives a function of degree `2^{ω(n)}` with divisor in two free orbits;
  the field generated by its translates has a curve of genus one; `C` is a ramified double cover of a genus-one
  curve; for odd `p` that case is AP-A.29l, for `p = 2` the Deuring–Shafarevich formula gives `f_2(P_n) > 0`.
- **R4** (AP-A.13–A.19, AP-A.21, AP-A.29l, AP-A.29m; the intake followed A.21 and A.29l). No collision on:
  hyperelliptic curves in odd characteristic (through étale correspondences to a supersingular elliptic curve);
  prime-to-`p` Galois covers of curves of genus one; solvable prime-to-`p` Galois covers of curves of genus zero;
  and A1 ascends along prime-to-`p` Galois covers. A.29l rests on Boggi–Zalesskii 2019, Lemma 3.1, for pro-`𝒮`
  completions of orbifold groups (`𝒮` = finite groups of order prime to `p`): open it and confirm the class.
- **R5** (AP-A.C2.5, AP-A.C2.8; proofs followed). Genus two, `p = 2`: with `B` the bundle of locally exact
  differentials and `Θ = {L : H⁰(B ⊗ L) ≠ 0}`, Frobenius `H¹(C, Lⁱ) → H¹(C, L²ⁱ)` vanishes exactly when `Lⁱ ∈ Θ`.
- **R6** (AP-A.C2.22–A.C2.26; certificates, reproduced by no one). No collision on any genus-two curve over `F_4`,
  by cyclic covers with primitive 2-rank zero, of conductors up to `7·31·2503·4519`.
- **R7** (AP-A.C2.14, AP-A.C2.21, AP-A.C2.23; statement level). No fixed finite set of primes supplies R3 for all
  curves; a cyclic subgroup of order `n` meets `Θ` in at most about `√(2n)` points; abelian towers add nothing to R3.
- **R8** (the return's report, "Universal primitive-cover existence"). The Weil bound controls points of `Θ` in
  additive cosets and not in a single doubling orbit. The same passage sets the rational form of the criterion
  aside as needing "a new controlled-field endgame".
- **R9** (AP-F.1, F.7, F.17, F.32, F.37–F.49; the intake followed F.45, F.47 and the valuation and detection steps
  of F.43). Reconstruction holds over the subfields of finitely generated extensions of `K^𝒞` (F.37, F.43, F.44),
  over function fields over `Q̄` and their subfields of positive transcendence degree (F.45, F.46), over the fields
  of F.49; it fails over fields with finite Galois group and Laurent series fields (F.41), over the fields of F.42
  (same Galois group and cyclotomic character as `Q`), and over every field of finite transcendence degree with a
  henselian valuation of residue characteristic 0 satisfying the Abhyankar equality (F.47, F.48: `t ↦ t + t²`
  centralizes the Galois group). Necessary: for every finite `E/k₀`, no non-trivial automorphism of `k̄₀`
  centralizes `G_E` (F.39, F.40). It passes down along algebraic extensions (F.32). Without the closed-point
  condition no field of characteristic 0 reconstructs (F.1, F.17: a tangential splitting `G_k → G_{k(t)}`).

## The pattern (both field experts; a guide for every route)

Each open item has *ghosts*: objects that pass every test at one prime, one nilpotent level or one finite level
and fail only where the primes mix (here: the class `Q′ − P′`, `p`-primary on every cover; an exponent in `Ẑ` that
should be in `Z`; the substitution `t ↦ t + t²`). Every case that was settled was settled by a map to a rigid
target in which ghosts cannot exist. For each route name the rigid target, and test each proposed criterion
against the known ghosts before trying to prove it sufficient.

## Leads for Part A: one cluster, four levers

- **L0** (the common form; intake and manuscript participant). *For a `P`-pointed cover `D` over `L` as in R1 and
  any homomorphism `h : J_D → B` of abelian varieties over `L` with `B(L)[p] = 0`, a collision gives `h(T) = 0`.*
  `T` is `L`-rational and `p`-primary. The four levers are four choices of `h`.
- **L1** (lever 1: the relative class number; found independently by the intake and by the manuscript participant,
  whose form is the one stated; each derivation checked by its author only). *Let `D → C_L` be a connected étale
  Galois cover whose group `G` has odd order prime to `p` and is defined over `L`, in which `P` splits completely.
  If `p ∤ h(D)/h(C_L)`, then `P` collides with no point of `C(k)`.* Proof: by R1 there are rational lifts with
  `T` non-zero and `p`-primary in `J_D(L)`; `T = T₀ + T₁` with `T₀` the `G`-invariant part and `T₁` in the new
  part, both rational; the hypothesis kills `T₁`; so `δT = T` for all `δ ∈ G`, against R2. For `G = Z/ℓ` and
  `D = D_χ`: `h(D)/h(C) = N_{Q(ζ_ℓ)/Q} L_P(χ, 1)`. This is what his margin of scan 35 points to: go down to a
  finite field, where only the rational `p`-torsion can carry `T`.
- **L2** (lever 1 as a count; intake and manuscript). Modulo a prime over `p`,
  `L_P(χ, 1) ≡ det(1 − Φ ∣ H¹(C, L_χ))`, `Φ` the `L`-linear Frobenius. In genus two:
  `L_P(χ, 1) ≡ 1 + Σ_{x ∈ C(L)} χ([x − P])`. So in genus two `P` collides with nobody as soon as some character `χ`
  of odd prime order `ℓ ≠ p` of some `J_C(F_{q^r})` has `N(1 + Σ_x χ([x − P]))` prime to `p`. A random `χ` fails
  with probability about `p^{−f}` per prime above `p` (`f` the order of `p` modulo `ℓ`). If `p` is a primitive root
  modulo `ℓ`, a collision forces, for the cosets `b` of `ℓJ_C(L)` and `N_b = #{x ∈ C(L) : [x − P] ∈ b}`:
  `N_b ≡ N_0 + 1 (mod p)` for every `b ≠ 0`.
- **L3** (towards a proof by counting; intake). With more cosets than points and `p` a primitive root modulo `ℓ`,
  every non-zero coset holds a multiple of `p` points of `C(L) − P`. The pairs `x ≠ y` with `x − y ∈ ℓJ_C(L)` number
  at most `N²/ℓ^r + ((2g − 2)² − 1)#L` by the Weil bound and at least `(p − 1)(N − N_0)`. For `p > (2g − 2)²` this
  is a contradiction once such an `ℓ` exists for one `L`.
- **L4** (lever 1 for the primitive part; intake). If `C` is not a separable double cover of a curve of genus
  one, a collision forces `p ∣ #P_n(D_χ)(L)` for every `χ` of odd order `n` prime to `p`: the endgame of R3 uses
  only `A·T = 0`.
- **L5** (lever 2: correspondences; the Poincaré expert, with the rational form by the intake). For a
  correspondence `C ← D → X₀` over `L` with `D → C` étale, `P`-pointed, prime to `p`, and `X₀` a curve of genus ≥ 1
  with `J_{X₀}(L)[p] = 0` (in particular `X₀` supersingular, for instance the Hermitian curve
  `x^{p+1} + y^{p+1} = 1`), a collision forces `φ(Q′) = φ(P′)`, and, applied to all deck translates,
  `φ_*π^*(P) = φ_*π^*(Q)` as divisors. `P ↦ φ_*π^*(P)` is a morphism `C → Sym^N X₀`; if it is not constant it fails
  to separate only on a proper closed set of pairs. Existence: Bogomolov–Tschinkel, *Unramified correspondences*
  (2002), give every hyperelliptic curve over `F̄_p`, `p ≥ 5`, an unramified cover onto `y² = x⁶ − 1` (from memory:
  open it); R4 is the prime-to-`p` form for odd `p`. A finite test: `D` has a supersingular factor exactly when
  some `L(C, χ, T)` has a zero at a root of unity times `q^{−1/2}`.
- **L6** (the closure principle; manuscript). Collisions go up along prime-to-`p` étale covers and forward along
  morphisms of proper curves. So the class of curves with no collision over any finite field contains `C` whenever
  it contains a prime-to-`p` étale cover of `C`, and contains `D` whenever `D` has a point-separating family of
  morphisms to curves in the class. Seeds: R4, R6. L1 and R3 may be applied anywhere in the prime-to-`p` tower.
- **L7** (lever 3: Frobenius at closed points; the Longue Marche expert). Over a finite field the section of a
  point is its Frobenius, and a collision says that two fixed points of Frobenius lie in one Nielsen class of the
  prime-to-`p` homotopy type. In the abelianized prime-to-`p` group the class of a point is its class in the Picard
  group modulo `p`-primary torsion, so on `C` itself this gives only R1 (the intake's remark); applied on the
  covers `D_χ` it is L1.
- **L8** (lever 4: the geometric form; the run, with the Longue Marche expert's weakening). `f_p(P_n) = 0` if and
  only if, for every orbit `O` of multiplication by `p` on the primitive characters, the composite of the `#O`
  Frobenius maps around `O` is nilpotent on the `(g − 1)`-dimensional space `H¹(C, L_χ)`. The expert's target:
  not rank zero, only "not ordinary in the eigenspace that carries `T`", from the torsion points on Raynaud's
  theta divisor (Raynaud, Tamagawa, Pop–Saïdi: from memory).
- **L9** (the literature form; the Poincaré expert). A1 is "the exceptional set of Saïdi–Tamagawa is empty" (their
  2009 paper and the refined version): open them and say what they prove and ask.
- **L10** (test objects; the moonshine dictionary, 4.6). The coverings of Conway–McKay–Trojan type are explicit
  coverings whose deck group acts faithfully on an `F_p`-space; they are wild, so they do not enter R2 as stated,
  but they test a non-abelian form of the criterion.
- **Hunch of all five readers:** A1 is true. The intake and the manuscript participant expect a proof through L1
  in most characteristics, with small `p` relative to the genus (`p = 2`, `g = 2` first) as the hard residue.

## Parts

**Part A. Point sections in the geometrically prime-to-`p` group (scans 35–36). The main question.**
- **A1.** Prove or refute: no smooth proper geometrically connected curve of genus ≥ 2 over a finite field has a
  collision. With R1 and AP-A.8 state and prove the corollary for every hyperbolic curve over every field finitely
  generated over `F_p`, which decides his "Il est cependant possible que l'injectivité de (*) reste valable" and
  "Il se pourrait qu'on puisse en déduire `P = Q`". A refutation is a curve and a pair with the conjugacy proved in
  the whole group.
- **A2.** Prove or refute L0, L1 and L4, with every field of definition and every twist written (the cover must
  have a rational point over `P`; a change of base point twists `χ`), for every finite group `G` of odd order
  prime to `p`; and say why the return's report (R8) set the rational form aside, and whether its reason stands.
- **A3.** Prove or refute: for every `C/k` of genus ≥ 2 and every `P ∈ C(k)` there are a finite `L/k` and a cover as
  in L1 with `p ∤ h(D)/h(C_L)`. With A2 this is A1. Attack it by L2 and L3; determine exactly which pairs `(p, g)`
  L3 settles; close the others.
- **A4.** Compute the test of L1 for every genus-two curve over `F_4`, `F_8` and `F_16`, for every smooth plane
  quartic over `F_3` and `F_5`, and for every rational point of each: for each `(C, P)` the witness `(L, ℓ, χ)` of
  least `ℓ` with its `L`-polynomials, or the list of all `(L, ℓ, χ)` tried with their values. Compare with R6 class
  by class, the classes 203/302 first. These computations test A2 and A3 and do not replace them.
- **A5.** Prove or refute L5 and L6. Then prove or refute: every curve of genus ≥ 2 over `F̄_p` has a prime-to-`p`
  étale cover with a point-separating family of morphisms to curves on which there is no collision; in particular
  the existence of prime-to-`p` unramified correspondences to a supersingular curve for all curves and for
  `p = 2, 3`. Give the list of curves that L6 reaches from R4 and R6.
- **A6.** Prove or refute the existence statement of R3: every curve of genus ≥ 2 over `F̄_p` has a connected cyclic
  étale cover of odd degree prime to `p` whose primitive part has `p`-rank zero; with L8, and for genus two and
  `p = 2` in the theta form of R5 and R8.
- **A7.** The criterion for a Galois cover with non-abelian group of order prime to `p`: state and prove what
  replaces R3, L1 and L4 for an element of `Z[G]` (R2 gives `(1 − δ)T ≠ 0` for every `δ` of odd order), test it on
  the coverings of L10, and decide whether it reaches a curve that A3 does not.
- **A8.** L9: state A1 in the terms of Saïdi–Tamagawa, with what their papers prove about the exceptional set.
- **A9.** His margin of scan 36: prove or refute that his Théorème 2 (the functor `K ↦ Π_K/Π_{F_p}` is faithful on
  finitely generated fields) holds in characteristic `p` with the prime-to-`p` groups, by his reduction to products
  of curves of genus zero.
- **A10.** A1: the ghost module (the ghost-symmetries translation, item GS6, section 3.5; Claude Fable 5.2 at effort high; a hunch, unchecked). Prove or refute: (a) the construction of M and the additivity of T; (b) a collision gives a non-zero Frobenius-fixed norm-compatible element of M with free deck orbits at every level; (c) M has no such element for curves of genus two in characteristic 2, starting with the two classes over F₄ that the run left to certificates; (d) the lever of `UNSTUCK_POINCARE_FERMAT.md` §1 as a vanishing quotient of M.

**Part F. Schemes from their étale topoi (scan 52).**
- **F1.** Scan 52 as he wrote it. (i) Prove that his statement, read with all morphisms of topoi over `S_ét`, is
  false over every field of characteristic 0 (R9, F.1), and prove or refute: for a curve `X` over `k₀`, the
  morphisms `Spec k₀ → X` of topoi that are not closed-point-preserving are exactly the sections of his conjecture
  a) of scans 126–127 (sections through the decomposition group of a valuation). (ii) Prove or refute the
  statement with the closed-point condition and universal homeomorphisms inverted, over a base `S` of finite type
  over `Z`; treat characteristic `p` (his margin: the absolute Frobenius and the identity induce isomorphic
  morphisms of topoi). (iii) Prove or refute the pro-form of scans 6–8: for an arbitrary field `k₀` of
  characteristic 0, reconstruction holds for the pro-system of topoi over the finitely generated subfields.
- **F2.** His experiment: prove or refute, for a smooth proper curve `X` of genus ≥ 2 over a number field `K₀` with
  function field `K`, that every outer automorphism of `G_K` over `G_{K₀}` that preserves the loop structure (the
  conjugacy classes of the inertia and decomposition groups of the closed points) comes from an automorphism of
  `X`; name the theorem of the literature that settles it, with its hypotheses.
- **F3.** The classification of the fields over which reconstruction holds (AP-F.9; our question, not his). Prove
  or refute each of the three candidate answers, and give the one that is right with its proof in both
  directions:
  (a) (intake) `k₀` reconstructs if and only if, for every finite `E/k₀`, no non-trivial automorphism of `k̄₀`
  centralizes `G_E`;
  (b) (the Poincaré expert) `k₀` reconstructs if and only if the Isom form of the Grothendieck conjecture holds for
  hyperbolic curves of genus 0 over every finite extension of `k₀`; and whether `P¹` minus four points over every
  finite extension is enough;
  (c) (manuscript) `k₀` reconstructs if and only if every closed-point-preserving morphism of étale topoi over `k₀`
  descends to a finitely generated subfield.
  Restate R9 (F.37, F.43–F.49 and F.39–F.41, F.47–F.48) as instances, and name the smallest field on neither list.
  By AP-F.42 the answer is not a property of `G_{k₀}` with its cyclotomic character.
- **F4.** Decide reconstruction for a field of finite transcendence degree over `Q` with a henselian valuation of
  residue characteristic 0 with transcendence defect, and for one with residue characteristic `p`.
- **F5.** The check of the chain AP-F.24–F.49 as one argument (finite detection, Kummer integrality by valuations,
  the Albanese span, point functions, Carlson–Haine–Wolf Theorem 4.18 (5), descent along algebraic extensions):
  each step confirmed or its exact error given.
- **F6** (scan 8; manuscript participant). "une description purement algébrique … du pro-pro-groupe fini associé
  … à (`C`, `C`)": describe the pro-system of the Galois groups of all finitely generated subfields of `C`, and
  state F1 (iii) for it.

## Changes of the consolidation (14 November 2026, about 17:40 UTC; the state before is `ITEMS_DRAFT_before_intake_consolidation_20261114.md`)

Taken from the manuscript participant's texts T1 and T3 (round 2), beyond what the round-2 draft already had:
- **To L0 and L1.** Only the least field over which the cover and the lift of `P` are defined matters, since
  larger fields only add rational torsion. Use (E): `B` an elliptic curve over `L` with `p ∤ #B(L)`, ordinary
  allowed: `φ(Q′) = φ(gP′)` for every `L`-morphism `φ : D → B`; so L5 does not need a supersingular target.
- **To L2 (the group-ring form).** For a quotient `A` of `J_C(L)` of odd order prime to `p` put
  `θ = [0] + Σ_{R ∈ C(L)} [R − P]` in `F_p[A]`. In genus two, L1 holds for the cover with group `A` exactly when
  `ψ(θ) ≠ 0` for every non-trivial character `ψ` of `A` with values in `F̄_p`; give the form for every genus
  (effective divisors of degree ≤ `2g − 2`). Item A2 asks for it.
- **To L3 (the singleton lemma).** In genus two, if `ℓ` is an odd prime with `p` a primitive root modulo `ℓ` and
  `χ : J_C(L) → Z/ℓ` is onto with kernel `H`, then at most `2(#H − 1)` points share a coset with another point
  (the count of AP-A.C2.21), so L1 holds for `χ` as soon as `#C(L) ≥ 2 #H` and `ℓ > #C(L)`. Item A3 uses it.
- **Not a route to A1:** class field theory for the full étale `π_1` separates points over finite fields at the
  abelian level; that is his statement of scan 35 for the pro-étale part, and A1 is what remains when the
  `p`-part is removed.
- **Part F.** F3 (b), the Poincaré expert's equivalence, is the lead item of the classification (the manuscript
  participant: it is closest to how he works, reducing everything to `P¹` with holes), with F1 (iii) beside it;
  F3 (a) is a statement to prove or refute under them. F1 (i) includes: the morphisms `Spec(k₀)_ét → X_ét` over
  `k₀` are the `k₀`-points together with the sections of `G_{k₀(x)} → G_{k₀}` at non-closed points `x`. F1 (ii)
  includes `S = Spec Z`.
- **Not added:** an audit of LM5 F.45 (the cross-run participant's proposal). The comparison LM5 F.45 left was
  made in ANABELIAN_149_PUSH (its item F3, row AP-F.15, Proved there, read at statement level); the register
  lists it for the referee.

## Background files the frame should attach

The final return's `sections\A*.tex`, `sections\F*.tex`, its register, and the report passages "Universal
primitive-cover existence" and "R27 and the two definitions"; the second-pass files of cote 149 for scans 6–8,
32–36, 41–52, 124–127; `INTAKE_ANABELIAN_149_FINAL_20261114.md`; from the debate folder
`POSITION_INTAKE.md` (4.1), `POSITION_MANUSCRIPT.md` (2.1, 2.2, 4.1, 4.3), `UNSTUCK_POINCARE_FERMAT.md` (1, 3),
`UNSTUCK_LM_EXPERT.md`; from the first prompt's zip the papers of Saïdi–Tamagawa and Stix. In LaTeX where a source
exists: Raynaud on the theta divisor of `B`; Tamagawa and Pop–Saïdi on tame fundamental groups; Bogomolov–Tschinkel,
*Unramified correspondences*; Ozman–Pries 2019; Poonen 2005 and 2007; Crew 1984; Katz (the congruence formula;
Proposition 9.1.3 as the return cites it); Boggi–Zalesskii 2019; Carlson–Haine–Wolf 2024; Carlson–Stix 2026;
Bary-Soroker–Paran 2013. No row of this prompt rests on the OpenAI preprints of 5 and 6 October 2026. The
bibliographic data are the return's or from memory; the drafter verified none.
For A10: `research_maps_20261114\MOONSHINE_DICTIONARY\GHOST_SYMMETRIES_TRANSLATION_20261114.md` (Claude Fable 5.2 at effort high; hunches, not authority).
