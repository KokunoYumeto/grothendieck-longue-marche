# SECTIONS_OVER_Q: items draft (mathematics only)

Drafted by Claude Fable 5.2 at effort high (the intake agent of ANABELIAN_149_PUSH and LM6), 14 November 2026,
debate round 1. The main session (Claude Opus 5.5 at effort max) adds the procedural frame. Successor of
LM6_POINTS_AS_SECTIONS (Parts B, D, F (e)) and of ANABELIAN_149_PUSH (Part D), both by GPT-6 Astra (ChatGPT Pro
mode), final returns of 14 November 2026. Their statements are cited as LM6-‹id› and AP-‹id›. Lines marked
**(drafter)** are the drafter's own, checked by no one.

## What is to be settled

First: every continuous section of `π_1(P¹_Q ∖ {0, 1, ∞}) → G_Q` that is not cuspidal is the section of a rational
point. It is Grothendieck's Conjecture A (cote 149, scan 56) for the tripod, the point-source case of his Conjecture
5.5 (La Longue Marche, §§5–9, scan 79), LM6-B.27 and AP-D.U1. Then: the birational lifting of sections (his
conjecture b), cote 149, scan 127), the finiteness of the set of sections of a proper curve (scan 65 of La Longue
Marche, "une approche de la conjecture de Mordell"), and the passage from number fields to finitely generated
fields.

## His text

Cote 149, scan 56: "*Conjecture A* Soit `U` courbe alg. anabélienne géom. connexe sur corps `K` de type fini sur
`Q`. Alors toute section de (1) est d'un des deux types précédents, i.e. soit définie par un pt de `U(K)`, soit par
une section d'une extension (2), avec `i ∈ I(K̄)^Γ` i.e. un pt de `Û ∖ U`, rationnel sur `K`", with the margin "Il
y a de plus les précisions `π^{Γ°} = (1)` (premier cas) `π^{Γ°} = L_i` (deux. cas)". Scans 126–127 (second pass:
"normalise un `I_V` [or `N_V`]"; the "ce" before "`V` est uniquement" is struck): "b) Soit `U` un modèle
« élémentaire » de `L` sur `K`, anabélien. Alors tte section de `𝓔_U^{L̄}` sur `𝓔_K^{K̄}` se relève en une section
de `𝓔_L^{L̄}` sur `𝓔_K^{K̄}`." La Longue Marche, scan 65: "Ceci suggère une approche de la conjecture de Mordell".

## Conventions

`U = P¹_Q ∖ {0, 1, ∞}` with coordinate `t`; `E_U = π_1(U)`, `Π` its geometric subgroup; a section is a continuous
section of `E_U → G_Q`, up to conjugation by `Π`. `𝓔 → U` is the Legendre family `y² = x(x − 1)(x − t)`;
`ρ_{s,ℓ}`, `ρ̄_{s,ℓ}` are the pull-backs along `s` of its `ℓ`-adic and mod-`ℓ` Tate modules, and
`ρ_Leg : E_U → GL_2(Ẑ)` its monodromy. `A_s = s^*κ(t)` and `B_s = s^*κ(1 − t)` in `Q̂^× = lim Q^×/n`. The local
section `s_p` of `s` at a prime `p` is the section of a point `x_p ∈ U(Q_p)` ("ordinary") or lies in the packet of
one of the cusps `0, 1, ∞` (its "label"). The *local theorem* is OpenAI, *The p-adic section conjecture*, 6 October
2026, Theorem 1.1, unrefereed; every use of it is to be marked.

## Results this builds on (confirm each where used, or give the exact error)

- **R1** (local classification; LM6-B.7, AP-D.6; on the local theorem). Over a finite extension of `Q_p` every
  section of a hyperbolic curve is the section of a point or lies in the packet of a rational cusp.
- **R2** (finite support; LM6-B.14 = LM6-E.6; proof followed by the intake). A section whose local points lie, at a
  set of primes of density one, in a finite subscheme `Z` of the compactification is the section of a point or a
  cusp over `Z(Q)` (Harari–Stix, Theorem 2.1; Stoll, Theorem 8.2).
- **R3** (Stoll's range; LM6-D.4, LM6-B.29, AP-D.22). If the compactification maps non-constantly to an abelian
  variety with finite Mordell–Weil group and trivial divisible part of `Ш`, every section of the curve and of each
  of its hyperbolic open subcurves is a point or cuspidal section. LM6-B.15: every section of `Y_1(N)` is cuspidal.
- **R4** (Fermat; LM6-E.7, E.8, E.9, E.12; proofs followed). The cover `Z_ℓ → U` of cyclic subgroups of order `ℓ`
  of the Legendre curve maps to `Y_0(4ℓ)`, and `g(X_0(4ℓ)) = (ℓ − 3)/2`. For a section of the Fermat curve `U_ℓ`,
  `ℓ ≥ 5`, the representation `ρ̄_ℓ` is unramified outside `2ℓ`, flat at `ℓ`, and reducible (Khare–Wintenberger at
  level dividing 16); every section of `U_n`, `n ≥ 3` odd, is cuspidal.
- **R5** (AP-D.25, D.3, D.26, D.27; statement level). The local points of a non-cuspidal section of `U` are integral
  at a set of primes of density one; an element of `Q̂^×` is in `Q^×` exactly when it is locally in `Q_p^×` for all
  `p` and in `Z_p^×` for almost all `p`.
- **R6** (AP-D.30; proof followed). `ρ_{s,ℓ}` is absolutely irreducible for a non-cuspidal `s`. Finite ramification
  of one `ρ_{s,ℓ}`, `ℓ ≥ 5`, is equivalent to: `x_p ∈ U(Z_p)` for almost all `p`; and then `(ρ_{s,ℓ})_ℓ` is the
  system of Tate modules of an elliptic curve over `Q` (Pan 2022, Theorem 1.0.4: to be opened).
- **R7** (AP-D.31; proof followed). If `x_p ∈ U(Z_p)` for almost all `p` and at most one cusp label occurs among the
  local sections, `s` is the section of a rational point.
- **R8** (AP-D.32; proof followed in its first half). The level-`N` neighbourhoods of `s` with full image
  `GL_2(Z/N)` have three rational cusp orbits and unit rank two: they give no unit regular at two labels.
- **R9** (AP-D.23, D.29, D.24; statement level). Every section has cuspidally central lifts for every finite set
  of punctures; character-wise reciprocity does not force the restricted-product condition.
- **R10** (LM6-F.31 with F.29, F.30; proofs followed; on the local theorem). For `K` finitely generated over `Q`, a
  smooth variety `V` and a hyperbolic curve `U′` over `K`, a `G_K`-homomorphism `π_1(V) → π_1(U′)` has geometric
  image open, trivial, or contained in one cusp inertia group.
- **R11** (LM6-B.35, B.33; statement level). The fibre of `f_*` over a point section, for a dominant `f`, is the
  point sections over the point together with the packets of the cusps mapping to it.
- **R12** (LM6-B.38–B.42; B.38, B.41 followed). Over a finitely generated extension of `Q_p`: generic sections of
  proper families are sections of `π_1(X) → π_1(S)`; isotrivial curves have only point and cuspidal sections; a
  tower over a Tate curve is split at every closed point and has no generic point.
- **R13** (LM6-F.36, F.37, F.42–F.44, F.13; statement level). The reduction from finitely generated fields to number
  fields for curves with a geometric cover mapping to a constant abelian variety; birational lifts at potentially
  good boundary; the centralizer test for decomposition groups.
- **R14** (LM6-D.1, D.5, D.6, D.7). `Sec(C/K)` is the finite-descent set; its localizations are finite when `K` has
  no CM subfield; the density step in Section 8 of the local-theorem paper has a gap as stated.

## Leads (drafter; each to be proved or refuted where an item uses it)

- **L1** (residual irreducibility; expected true). For a non-cuspidal section `s` of `U` over `Q` and every prime
  `ℓ ≥ 5`, `ρ̄_{s,ℓ}` is irreducible. Reason: an invariant line lifts `s` to `Z_ℓ`; `Z_ℓ` maps to `X_0(4ℓ)`, which
  is in Stoll's range (R3, R4); so `s` is a point section by R2; and no point of `U(Q)` has a rational cyclic
  `ℓ`-isogeny on its Legendre curve (no non-cuspidal rational points on `X_0(4ℓ)`, `ℓ ≥ 5`: to be quoted).
- **L2** (what finite ramification is). By Khare–Wintenberger `ρ̄_{s,ℓ}` is modular of some level `N_ℓ` prime to `ℓ`.
  The condition R6 (1) is: the `N_ℓ` are supported on one finite set of primes. Equivalently: the classes of `A_s`
  and `B_s` modulo `ℓ`, which give the twist `a x^ℓ + b y^ℓ = c z^ℓ` of the Fermat cover to which `s` lifts, are
  supported on one finite set of primes for all `ℓ`. For sections of the Fermat curves the set is `{2}` (R4).
- **L3** (the abelian shadow is not enough; expected true). An element of `Q̂^×` that is locally in `Q_p^×` at every
  `p` is `± ∏_q q^{a_q}` with integers `a_q` tending to 0 in `Ẑ`. Call a pair of such elements with
  `x_p + y_p = 1` in `Q_p` for every `p` a solution of the completed unit equation. Solutions with infinitely many
  `a_q ≠ 0` should exist (successive choice of primes by Dirichlet and of exponents by the Weil bound). So finite
  ramification cannot be proved from `(A_s, B_s)` alone.
- **L4** (the phantom class; a hunch). For a solution of L3 the cup product `A ∪ B ∈ H²_cts(G_Q, Ẑ(2))` is zero at
  every place and at every finite coefficient level, and lies in the `lim¹` part of that group, which is not zero
  (LM7 E.32: `H²_cts(G_Q, Z_3(2))`; LM6-E.38 builds such a class on the Fermat cubic). A section of `U` needs
  `A_s ∪ B_s = 0` to pass to the quotient of class two. Hunch: for an infinitely supported solution this class, or
  the next one in weight three, is not zero; then every section has finitely supported `(A_s, B_s)`.
- **L5** (after finite ramification: congruence rigidity). Under R6 (1) there are `λ₀ ∈ Q ∖ {0, 1}` and an
  isomorphism of `Ẑ[G_Q]`-modules between `s^*T(𝓔)` and `T(𝓔_{λ₀})` respecting the level-two structure (Faltings;
  the lattices agree for almost all `ℓ` by irreducibility). So `ρ_Leg ∘ s` and `ρ_Leg ∘ s_{λ₀}` are conjugate under
  the closure of the geometric monodromy: `s` and `s_{λ₀}` agree modulo the congruence kernel of the level-two
  group in `Π`. What remains of the main question is then: a section that agrees with a point section modulo that
  kernel is that point section. The classes `A_s, B_s` are not congruence data (the Fermat covers are not
  congruence covers), and at a prime of multiplicative reduction of `𝓔_{λ₀}` a cuspidal local section with
  parameter `λ₀^u`, `u ∈ (Ẑ^×)²`, has the same Legendre representation as the point: this is where the cusp labels
  of R7 reappear.
- **L6** (two maps). LM6-F.45 recognizes tangential sections by two open homomorphisms from one open subgroup. The
  same device applies here: a neighbourhood `Y` of `s` with two different maps to `U` gives two elliptic curves
  over `Q` by R6, hence two rational parameters tied by the correspondence.

## Parts

**Part A. The tripod over `Q`. The main question.**
- **A1.** Prove or refute: every non-cuspidal section of `E_U → G_Q` is the section of a point of `U(Q)`. State and
  prove what it gives for Conjecture A with its "précisions" for `U`, for every finite étale cover of `U`, and so,
  by Belyi's theorem, for which curves over number fields.
- **A2.** Prove or refute L1; then the same for `ℓ = 3` and for the 2-adic representation.
- **A3.** Prove or refute: for every non-cuspidal section, `x_p ∈ U(Z_p)` for almost all `p`. Routes: L2 (a bound on
  the levels `N_ℓ`, through the twists of the Fermat covers and R4); L4 (compute `A ∪ B` and the weight-three
  obstruction for the solutions of L3, as classes in continuous cohomology with their `lim¹` parts); R9.
- **A4.** Prove or refute L3: construct a solution of the completed unit equation with infinitely many non-zero
  exponents, or prove that none exists; then determine which of them lift to sections of the quotient of `E_U` by
  the third term of the lower central series of `Π`, and to the metabelian quotient.
- **A5.** Prove or refute L5 in full, with the twist and the sign fixed; then prove or refute: a section of `E_U`
  whose image under `ρ_Leg` is conjugate, under the closure of the geometric monodromy, to that of a point section
  is that point section. Include the case of several cusp labels (R7, R8, R11, L6).
- **A6.** The same question over a number field `K` (LM6-B.27): prove or refute it; say exactly where `Q` is used
  in A2–A5 (modularity, the unit group, the real place).

**Part B. Birational lifting (scan 127; LM6-F.15, AP-D.U4, AP-D.U2).**
- **B1.** Prove or refute: every section of `E_U → G_Q` lifts to a section of `G_{Q(t)} → G_Q`. Start from R9
  (central lifts at every finite puncture set) and R13.
- **B2.** Prove or refute: every section of `G_{Q(t)} → G_Q` lies in the decomposition group of a rational place.
  Prove that B1 with B2 gives A1.
- **B3.** For a hyperbolic curve fibration `U′ → B` over a hyperbolic curve and a section whose projection is
  cuspidal at a base cusp with bad marked reduction: prove or refute the existence of a birational lift
  (the case LM6-F.44 leaves).

**Part C. Finiteness and fields (scan 65; LM6-D.8, LM6-F.6).**
- **C1.** Prove or refute: `Sec(C/K)` is finite for every smooth proper curve `C` of genus ≥ 2 over a number
  field `K`. By R14 it is the finiteness of the finite-descent set; decide the step D.6 names.
- **C2.** Prove or refute: if every section of every hyperbolic curve over every number field is a point or
  cuspidal section, the same holds over every field finitely generated over `Q`. R13 covers the curves with a
  geometric cover mapping to a constant abelian variety; the open step is the reconstruction of a generic section
  of a proper family `X → B` as a morphism `B → X`.
- **C3.** Prove or refute: over a field finitely generated over `Q_p`, every section of a non-isotrivial smooth
  proper curve of genus ≥ 2 is the section of a rational point (R12; the tower of LM6-B.42 is the test).
- **C4.** The section-conjecture form of Fermat's theorem for the classical curve `x⁴ + y⁴ = z⁴` minus its points
  with `xyz = 0`, and for every even exponent: determine the set of sections over `Q`.

## Background files the frame should attach

From LM6: the paper sections of B.7, B.14, B.15, B.29, B.33, B.35, B.38–B.42, D.1–D.11, E.6–E.12, E.38, F.13,
F.15, F.29–F.31, F.36, F.37, F.42–F.47, with the register and the report's "Attempts at the still unresolved
goals". From ANABELIAN: `sections\D*.tex` (D.3, D.6, D.22–D.32), the register, the report's notes on D.30–D.32
and "All-prime Legendre compatibility". From LM7 and LM8: the statements E.32 and F.21 on the `lim¹` classes. The
two intakes (`INTAKE_ANABELIAN_149_FINAL_20261114.md`, `INTAKE_LM6_FINAL_20261114.md`). The transcription of cote
149 with the second-pass files of scans 54–56, 126, 127. Literature in LaTeX where a source exists: the local
theorem paper; Stoll (finite descent; with the erratum), Harari–Stix, Harari–Voloch, Helm–Voloch, Stix
(arXiv:0809.0017, arXiv:1203.3236), Pan 2022, Khare–Wintenberger, Mazur and Kenku on rational isogenies, Steklov
(arXiv:2602.17746), Carlson–Stix 2026, Esnault–Hai, Saïdi–Tyler. Bibliographic data are the returns'; the drafter
verified none.
