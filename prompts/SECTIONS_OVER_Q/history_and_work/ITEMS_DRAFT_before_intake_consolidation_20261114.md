# SECTIONS_OVER_Q: items draft (mathematics only)

Drafted by Claude Fable 5.2 at effort high (the intake agent of ANABELIAN_149_PUSH and LM6), 14 November 2026,
debate round 1; brought up to date in round 2 (17:26–17:50 UTC) with the papers of the manuscript, cross-run and
Fermat participants, the notes of the two field experts (all Claude Fable 5.2, at effort max or high as their
papers say) and the moonshine dictionary. The state before round 2 is
`ITEMS_DRAFT_before_intake_round2_20261114.md`. The main session (Claude Opus 5.5 at effort max) adds the
procedural frame. Successor of LM6_POINTS_AS_SECTIONS (Parts B, D, F (d), F (e)) and of ANABELIAN_149_PUSH
(Part D), both by GPT-6 Astra (ChatGPT Pro mode), final returns of 14 November 2026. Their statements are cited
as LM6-‹id› and AP-‹id›. Every lead is unchecked by a second reader unless it says otherwise; its author is named.

## What is to be settled

First, and with most of the time: every continuous section of `π_1(P¹_Q ∖ {0, 1, ∞}) → G_Q` that is not cuspidal
is the section of a rational point, and every section lifts to the function field. These are Grothendieck's
Conjecture A (cote 149, scan 56) and his conjecture b) (scans 57–58, 127) for the tripod; the point-source case
of his Conjecture 5.5 (La Longue Marche, cote 140-2, §§5–9, scan 79); LM6-B.27 and LM6-F.15; AP-D.U1 and AP-D.U4.
By the lead L1 below they are one question (Part A). Then: the cyclotomic base he proposes (scans 61–62), the
finiteness of the set of sections of a proper curve (La Longue Marche, cote 140-2, §8, scan 65: "une approche de
la conjecture de Mordell"), and the passage from number fields to finitely generated fields.

## His text (cote 149, second-pass readings)

- Scan 48, for `V` a point, with scan 66: the sections whose `Γ°`-part has trivial centralizer, over every open
  subgroup, are the rational points ("sections admissibles").
- Scans 54–55: the packets at two cusps are distinct "sauf pour le type (0,3), qui mérite un examen approfondi";
  he closes the gap by admitting `π^{Γ°} = L_i`, "à énoncer parmi les conjectures-clefs".
- Scan 56: "*Conjecture A* Soit `U` courbe alg. anabélienne géom. connexe sur corps `K` de type fini sur `Q`. Alors
  toute section de (1) est d'un des deux types précédents, i.e. soit définie par un pt de `U(K)`, soit par une
  section d'une extension (2), avec `i ∈ I(K̄)^Γ` i.e. un pt de `Û ∖ U`, rationnel sur `K`"; margin: "Il y a de plus
  les précisions `π^{Γ°} = (1)` (premier cas) `π^{Γ°} = L_i` (deux. cas)".
- Scans 56–58: for the function field `L` the sections "se grouperaient par paquets"; "c'est la structure
  `E_L → E_K` qui est la plus riche a priori, et de loin plus commode pour le genre 0 et 1"; "la forme
  « modélique » … revient à la forme « birationnelle », quand on y précise cette dernière en disant que tt scindage
  de `E_U − E_K` se remonte en un scindage de `E_L − E_K` (ou aussi, en un scindage de `E_V − E_K`, si `V` est un
  modèle `⊂ U`)".
- Scan 59: Conjecture B, for an action "continue dans un sens convenable"; scan 63, Conjecture B′: "ici on ne
  suppose pas que l'action de `Γ` sur `𝒰` normalise l'action d'un groupe profini `π`". Continuity is kept.
- Scans 61–62: "je me demande … si ces énoncés ne devraient pas être valables … dès que `K` est ext. de type fini
  d'un corps cyclotomique".
- Scans 79–85: the class of `1 → T → N(L_i) → E_S → 1` is the class of the conormal bundle in `Pic(S)`.
- Scans 120, 128, 130: "A-t-on une réciproque ?" (if `I_{x′} → E_U` is trivial, `V` has a centre on `U`); "Dans
  quelle mesure des `V` distinctes définissent-elles des `Δ_V` distinctes ?"; whether a minimal model makes
  `T^{I(x)} → π_{U/K}` injective.
- Scans 126–127: "a) Toute section de `𝓔_L` sur `𝓔_K` … normalise un `I_V` [the ink has `I` written over `N`] associé
  à un anneau de valuation `V` de `L` contenant `K`, à corps résiduel algébrique sur `K` et `V` est uniquement
  [déterminé] … b) Soit `U` un modèle « élémentaire » de `L` sur `K`, anabélien. Alors tte section de `𝓔_U^{L̄}` sur
  `𝓔_K^{K̄}` se relève en une section de `𝓔_L^{L̄}` sur `𝓔_K^{K̄}`."

## Conventions

`U = P¹_Q ∖ {0, 1, ∞}` with coordinate `t`; `E_U = π_1(U)`, `Π` its geometric subgroup; a section is a continuous
section of `E_U → G_Q`, up to conjugation by `Π`. `𝓔 → U` is the Legendre family `y² = x(x − 1)(x − t)`;
`ρ_{s,ℓ}`, `ρ̄_{s,ℓ}` are the pull-backs along `s` of its `ℓ`-adic and mod-`ℓ` Tate modules, `ρ_Leg : E_U → GL_2(Ẑ)`
its monodromy. `A_s = s^*κ(t)`, `B_s = s^*κ(1 − t)` in `Q̂^× = lim Q^×/n`. The local section `s_p` at a prime `p` is
the section of a point `x_p ∈ U(Q_p)` ("ordinary") or lies in the packet of one of the cusps `0, 1, ∞` (its
"label"). A *ghost* is an object that passes every test at one prime, one nilpotent level or one finite level; a
*ghost solution of the unit equation* is a pair `(A, B)` in `Q̂^×` with a genuine local point `x_p`,
`A_p = κ(x_p)`, `B_p = κ(1 − x_p)`, at every `p`. The *local theorem* is OpenAI, *The p-adic section conjecture*,
6 October 2026, Theorem 1.1 (an unrefereed preprint, attached in LaTeX): use it where the work needs it, check
the steps used, and settle the gap LM6-D.6 reports in its Section 8.

## Results this builds on (confirm each where used, or give the exact error)

- **R1** (local classification; LM6-B.7, AP-D.6; on the local theorem). Over a finite extension of `Q_p` every
  section of a hyperbolic curve is the section of a point or lies in the packet of a rational cusp.
- **R2** (finite support; LM6-B.14 = LM6-E.6; proof followed by the intake and by the Fermat participant). A
  section whose local points lie, at a set of primes of density one, in a finite subscheme `Z` of the
  compactification is the section of a point or a cusp over `Z(Q)` (Harari–Stix, Theorem 2.1; Stoll, Theorem 8.2).
- **R3** (Stoll's range; LM6-D.4, LM6-B.29, AP-D.22, found by both runs). If the compactification maps
  non-constantly to an abelian variety with finite Mordell–Weil group and trivial divisible part of `Ш`, every
  section of the curve and of each of its hyperbolic open subcurves is a point or cuspidal section. LM6-B.15: every
  section of `Y_1(N)` is cuspidal.
- **R4** (Fermat; LM6-E.7–E.12; proofs followed by the intake and the Fermat participant). The cover `Z_ℓ → U` of
  cyclic subgroups of order `ℓ` of the Legendre curve maps to `Y_0(4ℓ)`, `g(X_0(4ℓ)) = (ℓ − 3)/2`. For a Selmer
  section of the Fermat curve `U_ℓ`, `ℓ ≥ 5`, `ρ̄_ℓ` is unramified outside `2ℓ`, flat at `ℓ`, and reducible
  (Khare–Wintenberger at level dividing 16); every Selmer section of `U_n`, `n ≥ 3` odd, is cuspidal; given the
  local theorem every section is Selmer. LM6-E.10: `Y_1(7)(Q) ≠ ∅`, against Steklov's preprint.
- **R5** (AP-D.25, D.3, D.26, D.27; statement level). The local points of a non-cuspidal section of `U` are integral
  at a set of primes of density one; an element of `Q̂^×` is in `Q^×` exactly when it is locally in `Q_p^×` for all
  `p` and in `Z_p^×` for almost all `p`; local Kummer classes come from one global class exactly when they form a
  restricted-product element orthogonal to the dual characters.
- **R6** (AP-D.30; proof followed). `ρ_{s,ℓ}` is absolutely irreducible for a non-cuspidal `s`. Finite ramification
  of one `ρ_{s,ℓ}`, `ℓ ≥ 5`, is equivalent to: `x_p ∈ U(Z_p)` for almost all `p`; and then `(ρ_{s,ℓ})_ℓ` is the
  system of Tate modules of an elliptic curve over `Q` (Pan 2022, Theorem 1.0.4: to be opened).
- **R7** (AP-D.31; proof followed). If `x_p ∈ U(Z_p)` for almost all `p` and at most one cusp label occurs among the
  local sections, `s` is the section of a rational point: a unit regular and non-zero at the occurring cusps takes
  one rational value at every local point.
- **R8** (AP-D.32; proof followed in its first half). The level-`N` neighbourhoods of `s` with full image
  `GL_2(Z/N)` have three rational cusp orbits and unit rank two: they give no unit regular at two labels.
- **R9** (AP-D.23, D.24, D.28, D.29; statement level). Every section has cuspidally central lifts for every finite
  set of punctures; a lift over a new puncture `a` exists under the reciprocity tests `κ(t − a) ∪ χ`; character-wise
  reciprocity does not force the restricted-product condition.
- **R10** (LM6-F.31 with F.29, F.30; proofs followed; on the local theorem). For `K` finitely generated over `Q`, a
  smooth variety `V` and a hyperbolic curve `U′` over `K`, a `G_K`-homomorphism `π_1(V) → π_1(U′)` has geometric
  image open, trivial, or contained in one cusp inertia group.
- **R11** (LM6-B.35, B.33; statement level). The fibre of `f_*` over a point section, for a dominant `f`, is the
  point sections over the point together with the packets of the cusps mapping to it.
- **R12** (LM6-B.38–B.42; B.38, B.41 followed). Over a finitely generated extension of `Q_p`: generic sections of
  proper families are sections of `π_1(X) → π_1(S)`; isotrivial curves have only point and cuspidal sections; a
  tower over a Tate curve is split at every closed point and has no generic point.
- **R13** (LM6-F.36, F.37, F.42–F.44, F.13, F.25–F.28; statement level). The reduction from finitely generated fields
  to number fields for curves with a geometric cover mapping to a constant abelian variety; birational lifts for
  proper towers and at potentially good boundary; the centralizer test for decomposition groups.
- **R14** (LM6-D.1, D.5, D.6, D.7). `Sec(C/K)` is the finite-descent set; its localizations are finite when `K` has
  no CM subfield; the density step in Section 8 of the local-theorem paper has a gap as stated.
- **R15** (LM6-F.1, F.7; CYCLOTOMIC_KERNEL). For a section over a field finitely generated over `Q`, the fixed
  group of the cyclotomic kernel in `Π` is trivial or a cusp inertia group; a section has at most one fixed
  pro-point on the completed universal cover. This closes his gap of scans 54–55 for type (0,3).
- **R16** (LM6-F.9 = FLAGGED_149 ZCF12; LM6-F.41, F.47; AP-D.11–D.14). A semilinear action on the universal cover in
  which every function has open stabilizer normalizes the group of a finite quotient: Conjecture B′ with his
  continuity is Conjecture B over finite extensions. For abstract actions: there are discontinuous actions with
  exactly one fixed point (LM6) and, by AP-D.12, D.14, one with none. These concern a statement he did not make.
- **R17** (LM6-E.16, E.31–E.34, E.38; LM7 E.32, E.34; LM8 F.21; Hoshi 2010). Every pro-`ℓ` nilpotent quotient and
  the full metabelian quotient of the Fermat curves carry non-cuspidal sections; `H²_cts(G_Q, Z_ℓ(2))` has a `lim¹`
  part of classes that vanish at every place and every finite level; LM6-E.38 builds one as an obstruction.
- **R18** (FLAGGED_149 ZCF7; Clark). Over `Q(μ_∞)` the curve `z⁶ + 2y³ + 4 = 0` has a section and no rational point.

## Leads

**On the shape of the problem.**
- **L1** (manuscript participant; from memory, to be opened first). Stix, *On the birational section conjecture
  with local conditions* (Invent. Math. 2015): over `Q`, a birationally liftable non-cuspidal section of a
  hyperbolic curve comes from a rational point. Then b) implies Conjecture A over `Q`, and since point and cuspidal
  sections lift, the two are equivalent: LM6-B.27 and LM6-F.15 are one item, and his own route to it is b).
- **L2** (both field experts, the Fermat participant, the intake; each independently). What is left is a section
  ramified at infinitely many primes. Its Kummer coordinates are valuations `a_p → 0` in `Ẑ`; a point has `a_p = 0`
  for almost all `p`; the gap between the two is the gap between the restricted product and the direct sum, the
  non-compactness that produces the `lim¹` classes of R17. No nilpotent or pro-`ℓ` level sees it.
- **L3** (the Poincaré expert; proved on the page there). For each fixed `ℓ`, `ρ̄_{s,ℓ}` is ramified at finitely many
  primes (`ℓ` divides the valuation at almost all primes). So R6 (1) is the statement that the supports `S_ℓ` stay
  bounded as `ℓ` grows: a reverse form of abc for sections. Each prime of the support lies in `S_ℓ` for all large `ℓ`.
- **Hunch of all readers:** the main statement is true.

**Routes to finite ramification (`x_p ∈ U(Z_p)` for almost all `p`).**
- **L4** (intake; residual irreducibility; expected true). For a non-cuspidal `s` and every `ℓ ≥ 5`, `ρ̄_{s,ℓ}` is
  irreducible: an invariant line lifts `s` to `Z_ℓ`, which maps to `X_0(4ℓ)`, in Stoll's range (R3, R4); so `s` is
  a point section by R2; and no point of `U(Q)` has a rational cyclic `ℓ`-isogeny on its Legendre curve (no
  non-cuspidal rational points on `X_0(4ℓ)`, `ℓ ≥ 5`: to be quoted). By Khare–Wintenberger `ρ̄_{s,ℓ}` is then modular
  of a level `N_ℓ` prime to `ℓ`, and R6 (1) is: the `N_ℓ` are supported on one finite set of primes.
- **L5** (intake, Fermat participant). `s` lifts to exactly one twist `a x^ℓ + b y^ℓ = c z^ℓ` of each Fermat cover,
  read off `A_s`, `B_s` modulo `ℓ`; R4 on the twist gives level supported on `2abc`. The tripod statement is Fermat
  for all twists at once, and R6 (1) is: the twist classes have bounded support as `ℓ` varies.
- **L6** (Fermat participant; item 1.16 of the Fermat successor computes the table). A section with Kummer classes
  `(α, β)` modulo cubes lifts to a twist of the Fermat cubic, whose Jacobian has complex multiplication by
  `Z[ζ_3]`. If its `L`-value at 1 is not zero, Rubin gives finite Mordell–Weil and Tate–Shafarevich groups, Stoll
  the finite-descent equality, and R2 makes every Selmer section in that class a point or cusp section. The same
  with the quartic and sextic twists. A rational point gives a point, usually of infinite order, on its own twist:
  the honest points sit in the classes of positive rank, where a Selmer section is a profinite multiple of a
  generator, and the question is which profinite multiples lift to the punctured curve.
- **L7** (the Poincaré expert). The stacky form: for each `n` the section gives an adelic point of the proper
  triangle stack `P¹(n, n, n)`, integral at almost all primes; `N_n` is its stacky height; R6 (1) is "the stacky
  heights are bounded" (Bhargava–Poonen on integral points of stacky curves; Ellenberg–Satriano–Zureick-Brown on
  heights on stacks: from memory).
- **L8** (the Poincaré expert: where ghosts die). Classify the ghost solutions with infinite support that lift to
  (a) the metabelian quotient; (b) the quotients over the genus-0 levels `X(3)`, `X(4)`, `X(5)` (groups `A_4`,
  `S_4`, `A_5`: the first quotients where primes mix; the twists are rational curves); (c) the level `X(7)`, where
  the twists are forms of the Klein quartic and Poonen–Schaefer–Stoll carried out descent (from memory). The first
  level at which a ghost with one extra prime dies is the mechanism to generalize.
- **L9** (intake; the completed unit equation; expected true). A ghost solution is `(± ∏_q q^{a_q}, ± ∏_q q^{b_q})`
  with integers `a_q, b_q → 0` in `Ẑ`, summing to 1 in every `Q_p`. Solutions with infinite support should exist
  (primes by Dirichlet, exponents by the Weil bound, step by step). So no argument on `(A_s, B_s)` alone proves
  finite ramification. The Longue Marche expert asks the same in the form: prove that `a` with honest integer
  valuations at every `q` is rational, or produce the section that refutes it.
- **L10** (intake, the Longue Marche expert, the Fermat participant; the phantom class; a hunch). For a ghost
  solution, `A ∪ B ∈ H²_cts(G_Q, Ẑ(2))` vanishes at every place and every finite level and lies in the `lim¹` part
  (R17). A section needs `A_s ∪ B_s = 0` to pass to class two. Hunch: for an infinitely supported ghost this
  class, or the one in weight three, is not zero. In the expert's words: over `Q(μ_{ℓ^∞})` nothing is obstructed,
  the sections over `Q` are descent data along the cyclotomic tower, and the phantom class is the non-Hausdorff
  part (Lead 16 of LM8_PUSH).
- **L11** (the Longue Marche expert; local-to-global through cusp colours). (i) At each prime `q` of ramification,
  in each pro-`ℓ` quotient, the local section is one of the cuspidal families (the tripod form of LM7 E.61, E.66).
  (ii) The section is one section for all `ℓ`: the cusp and the local Kummer parameter at `q` do not depend on `ℓ`;
  this is the step no pro-`ℓ` argument gives. (iii) Then L9. (iv) The covers the tripod has of itself
  (`λ ↦ 4λ(1 − λ)`, the `j`-map): the set of sections is stable under them, and a section that is not a point
  should be thrown into a cusp by one of them.

**Routes after finite ramification (the cusp labels).**
- **L12** (intake; congruence rigidity). Under R6 (1) there are `λ₀ ∈ Q ∖ {0, 1}` and an isomorphism of
  `Ẑ[G_Q]`-modules between `s^*T(𝓔)` and `T(𝓔_{λ₀})` respecting the level-two structure (Faltings; the lattices
  agree for almost all `ℓ` by irreducibility). So `ρ_Leg ∘ s` and `ρ_Leg ∘ s_{λ₀}` are conjugate under the closure of
  the geometric monodromy: `s` and `s_{λ₀}` agree modulo the congruence kernel of the level-two group in `Π`. What
  remains is: a section that agrees with a point section modulo that kernel is that point section. The Poincaré
  expert states the same: the two cusp labels live in the congruence kernel, on non-congruence covers, which is
  why R8 finds no unit. The Fermat covers are not congruence covers: `A_s` must be shown equal to `κ(λ₀)`.
- **L13** (the Poincaré expert, with the intake's caution). At a prime of good ordinary reduction the integral Tate
  module should fix the local point through the Serre–Tate parameter; then local-to-global injectivity on a set of
  primes of density one closes the labels without a new cover. Caution (intake): an isomorphism of the local Tate
  modules fixes the Serre–Tate parameter only up to a power in `(Z_p^×)²`, and at a prime of multiplicative
  reduction a cuspidal section with parameter `λ₀^u` has the Legendre representation of the point. Decide which is
  right.
- **L14** (the moonshine dictionary, item M4 (a)). The function `u = 1 − 1728/j` is a unit on `U′`, the tripod minus
  the harmonic points `−1, 1/2, 2` and the two equianharmonic points, and equals 1 at each of the three cusps. If
  `s` lifts to `U′`, R7 with `u` makes `s` a rational point whatever the cusp labels. The lift is the reciprocity
  condition of R9 at the five points. Hunch: the labels reduce to "a non-cuspidal section avoids the harmonic and
  equianharmonic points at almost all places, or is one of them".
- **L15** (intake; two maps). LM6-F.45 recognizes tangential sections by two open homomorphisms from one open
  subgroup. A neighbourhood `Y` of `s` with two different maps to `U` gives two elliptic curves over `Q` by R6, hence
  two rational parameters tied by the correspondence.
- **L16** (the Poincaré expert). The rigid target for both gaps at once is a proper curve over `Q` in which finite
  descent is known, for the twist the section selects: a rational point cannot be two cusps.

**Routes to birational lifting.**
- **L17** (manuscript participant). Prove b) at finite level: lift `s` over one more puncture, compatibly;
  compactness gives the lift. R9 (central lifts) is the first step; his scans 79–82 give the first obstruction as
  a class in `Pic`. With the fibration `M_{0,5} → M_{0,4}`: the fibre `Π_s` of `E_{0,5} → E_{0,4}` over `s(G_Q)` is
  an extension of `G_Q` by a free group of rank 3, "the line with four punctures `0, 1, ∞, x_s`" for a point `x_s`
  that may not exist; `s` lifts over the puncture `x` exactly when the point section of `x` lifts to `Π_s`; R6's
  representation is the `H¹` of the double cover of this virtual curve. The item: an extension that is everywhere
  locally the group of a four-punctured line (R1, R5) and carries all rational point sections is the group of a
  four-punctured line.
- **L18** (manuscript participant). The two consequences he calls "d'apparence opposée" on scan 49 (`π^{Γ°} ≠ 1`
  for fields, `= 1` for points of models) are related by b): a point section lifts to the function field, where
  its fixed group is an inertia group `I_V`, which dies on the model.

## Parts

**Part A. The tripod over `Q`: Conjecture A and conjecture b). The main question.**
- **A1.** Prove or refute: every section of `E_U → G_Q` lifts to a section of `G_{Q(t)} → G_Q` (LM6-F.15, AP-D.U4);
  and every non-cuspidal section of `E_U → G_Q` is the section of a point of `U(Q)` (LM6-B.27, AP-D.U1). State and
  prove what the two give for Conjecture A with its "précisions", for conjecture a) of scan 126 for `Q(t)/Q`, for
  every finite étale cover of `U`, and so, by Belyi's theorem, for which curves over number fields.
- **A2.** Prove or refute L1 with the theorem opened: what exactly it gives for the tripod over `Q`, and the
  equivalence of the two halves of A1.
- **A3.** Prove or refute L4; then the same for `ℓ = 3` and for the 2-adic representation.
- **A4.** Prove or refute: for every non-cuspidal section, `x_p ∈ U(Z_p)` for almost all `p`. Routes: L4 with L5 (a
  bound on the levels `N_ℓ`); L7; L10; L11. State the result reached also in the forms L3 ("the supports `S_ℓ` are
  bounded") and L7 ("the stacky heights are bounded").
- **A5.** Prove or refute L9: construct a ghost solution of the unit equation with infinite support, or prove that
  none exists. Then carry out L8: determine which ghost solutions lift to the quotient of class two, to class
  three, to the metabelian quotient, and to the quotients over `X(3)`, `X(4)`, `X(5)` and `X(7)`; compute `A ∪ B`
  and the weight-three obstruction as classes in continuous cohomology with their `lim¹` parts (L10); name the
  first level at which every ghost with infinite support dies, or prove that there is none.
- **A6.** Prove or refute L11 (i) and (ii): the local cuspidal families in each pro-`ℓ` quotient, and the
  independence of `ℓ` of the cusp and the Kummer parameter at each prime.
- **A7.** Prove or refute L12 in full, with the twist and the sign fixed; decide L13; then prove or refute: a
  section of `E_U` whose image under `ρ_Leg` is conjugate, under the closure of the geometric monodromy, to that of
  a point section is that point section. Include the case of several cusp labels (R7, R8, R11, L14, L15, L16).
- **A8.** Prove or refute L14 (dictionary M4 (a)): `s` lifts to `U′` exactly under the reciprocity condition of R9
  at each removed point; and if it lifts and its local points are integral at almost all places, `s` is a rational
  point whatever the cusp labels. With A7, restate what is left of A1.
- **A9.** Prove or refute L17: b) for `s` at finite level from R9, and the statement on the extension `Π_s`.
- **A10.** L6 for the tripod: prove that every Selmer section whose twist class at 3, at 4 or at 6 has analytic
  rank zero is a point or cuspidal section; then decide, in a class of positive rank, which profinite multiples of
  a generator lift to the punctured curve.
- **A11.** The same question over a number field `K` (LM6-B.27): prove or refute it; say exactly where `Q` is used
  in A2–A10 (modularity, the unit group, the real place, L1).

**Part B. Sections and valuations (scans 120–130).**
- **B1.** Prove or refute: every section of `G_{Q(t)} → G_Q` lies in the decomposition group of a rational place
  (AP-D.U2; his a) for `Q(t)/Q`).
- **B2.** For a hyperbolic curve fibration `U′ → B` over a hyperbolic curve and a section whose projection is
  cuspidal at a base cusp with bad marked reduction: prove or refute the existence of a birational lift (the case
  LM6-F.44 leaves); and the compatible valuation above all one-variable restrictions (LM6-F.15).
- **B3.** His three questions: the converse of scan 120; when distinct `V` give distinct `Δ_V` (scan 128); whether
  a minimal model makes `T^{I(x)} → π_{U/K}` injective (scan 130), with AP-G.1, G.2 (the covering-germ criterion).

**Part C. The cyclotomic base and Conjecture B′ (scans 59–63).**
- **C1.** Prove: over a field `K` finitely generated over `Q(μ_∞)`, two points whose sections are conjugate on the
  cyclotomic kernel are equal (the conjugating element is unique by R15, hence equivariant; then his Théorème 3),
  while the abelianized statement fails (`ζ_6` and `ζ_6^{-1}` on the tripod). Then prove or refute Conjecture A for
  the tripod over `Q(μ_∞)`; R18 is the proper case.
- **C2.** State Conjecture B′ with his continuity, with the topology defined, and prove that it is Conjecture B
  over finite extensions (R16); state what AP-D.12, D.14 and LM6-F.41, F.47 say about abstract actions, and decide
  the one clause the two returns leave between them: whether an abstract action with no fixed point exists (check
  AP-D.12 line by line).

**Part D. Finiteness and fields (La Longue Marche §8, scan 65; LM6-D.8, LM6-F.6).**
- **D1.** Prove or refute: `Sec(C/K)` is finite for every smooth proper curve `C` of genus ≥ 2 over a number
  field `K`. By R14 it is the finiteness of the finite-descent set; settle the step LM6-D.6 names in Section 8 of
  the local-theorem paper (prove it, repair it or refute it) and say which results depend on it.
- **D2.** Prove or refute: if every section of every hyperbolic curve over every number field is a point or
  cuspidal section, the same holds over every field finitely generated over `Q`. R13 covers the curves with a
  geometric cover mapping to a constant abelian variety; the open step is the reconstruction of a generic section
  of a proper family `X → B` as a morphism `B → X`.
- **D3.** Prove or refute: over a field finitely generated over `Q_p`, every section of a non-isotrivial smooth
  proper curve of genus ≥ 2 is the section of a rational point (R12; the tower of LM6-B.42 is the test).
- **D4.** The curve `x⁴ + y⁴ = z⁴` minus its points with `xyz = 0`, and every even exponent: determine the set of
  sections over `Q` (dictionary M4 (b): through the elliptic quotients with complex multiplication by `Z[i]` and
  `Z[√−2]`, of rank zero, and R2). Item 1.14 of the Fermat successor asks the same; one of the two prompts keeps it.

## Background files the frame should attach

From LM6: the paper sections of B.7, B.14, B.15, B.29, B.33, B.35, B.38–B.42, D.1–D.11, E.6–E.12, E.16, E.31–E.38,
F.1, F.7, F.9, F.13, F.15, F.25–F.31, F.36, F.37, F.41–F.47, with the register and the report's "Attempts at the
still unresolved goals". From ANABELIAN: `sections\D*.tex` (D.3, D.6, D.11–D.14, D.22–D.32), `sections\local_lead.tex`
(G.1, G.2), the register, the report's notes on D.30–D.32 and "All-prime Legendre compatibility". From LM7, LM7_PUSH
and LM8: the statements E.32, E.34, E.61, E.66 and F.21, and Lead 16 of LM8_PUSH. The two intakes; from the debate
folder `POSITION_INTAKE.md`, `POSITION_MANUSCRIPT.md`, `POSITION_FERMAT.md`, `UNSTUCK_LM_EXPERT.md`,
`UNSTUCK_POINCARE_FERMAT.md`, and section 4.4 of the moonshine dictionary. The second-pass files of cote 149 for
scans 45–66, 79–85, 119–131. The two OpenAI preprints of 5 and 6 October 2026 in LaTeX
(`debate_20261114\background_sources\`). Literature in LaTeX where a source exists: Stix (Invent. Math. 2015;
arXiv:0809.0017; arXiv:1203.3236), Stoll (finite descent, with the erratum), Harari–Stix, Harari–Voloch,
Helm–Voloch, Pan 2022, Khare–Wintenberger, Mazur and Kenku on rational isogenies, Rubin on CM elliptic curves,
Poonen–Schaefer–Stoll, Bhargava–Poonen, Ellenberg–Satriano–Zureick-Brown, Steklov (arXiv:2602.17746),
Carlson–Stix 2026, Esnault–Hai, Saïdi–Tyler, Hoshi 2010. Bibliographic data are the returns' or from memory; the
drafter verified none.
