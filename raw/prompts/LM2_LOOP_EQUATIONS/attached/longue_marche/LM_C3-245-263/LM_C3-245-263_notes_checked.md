# LM_C3-245-263 — research notes, checked against the corrected transcription (scans 245–263)

Source: the first pass's research notes (answers/unzipped/LM_C3-245-263/LM_C3-245-263_notes.md, §5, notes 1–50), each
checked against LM_C3-245-263_checked.tex. Verdicts: keep, correct (text revised), drop. Notes marked **Claude
(second pass)** are new. Kinds: conjecture (Grothendieck's conjectures, questions, expectations, programme), unproved
claim, unpursued implication, own idea. "Unproved" means not proved in the cited passage.

Conventions used in the checks: the matrices of the pages themselves, ρ = (0 1; −1 1) (scans 258, 261) and
σ = σ∞ = (0 −1; 1 0) (scans 258, 260); for the coboundary map ρ(α) = ραρ⁻¹, so [α, ρ] = αρα⁻¹ρ⁻¹. ρ has order 3 and
σ∞ order 2 as automorphisms (in PSL(2, Z)); in the quotient 𝔖₃ of (51), σ̇ρ̇σ̇⁻¹ = ρ̇⁻¹.

## Notes of the first pass

### Scans 245–249 (§47, the parameters α, β)

- **N1 — scan 245, opening — unproved claim — correct.** The "principes généraux (pas encore établis … dans le cadre
  profini)" are used to make the commutant of ρ in Ĝ₀,₃ = Ĝ⁺₀,₃·{1, τ∞} (scan 244) equal to {1, ρ, ρ²}, which turns
  the commutation relation (*) of scan 244 into τ′∞^{α₃}φ̂(f∞)α = ρ^j with j ∈ Z/3Z. The profinite centralizer
  statement is the input to be proved. Revised: the group and the relation are named.
- **N2 — scan 245, upper-left margin — conjecture (programme) — keep.** "il faudrait … formules … précise …!!!" asks
  for explicit formulas; the rest of the note is still unread, so nothing more specific can be attributed to it.
- **N3 — scan 246, (45)–(48) — unpursued implication — keep.** α̃ = ατ∞^{α₃} lies in Π̂₀,₃ in all cases, and for
  α₃ = 1 the coboundary relation becomes the twisted one (46), ξ = α̃ℓ₁⁻¹ρ(α̃)⁻¹. Checked: it follows from
  ξ = αρ(α)⁻¹, α = α̃τ∞ and (**) τ∞ρ(τ∞)⁻¹ = ℓ₁⁻¹.
- **N4 — scan 247, opening — unproved claim — correct.** The equivalence of (47) with (10) = (49) for α, β linked by
  ξ = ηℓ₁^ν "mériterait une vérification directe" and is not given. The ink writes η = βσ∞(η)⁻¹: the argument of σ∞
  is a slip for β (η = βσ∞(β)⁻¹ on scan 249 and in (11) of scan 232). Revised: the palaeographic doubt is settled.
- **N5 — scan 247, (51) — unpursued implication — correct.** Reduction mod Π̂₀,₃ keeps exactly the triple
  (i, α₃, j′) of (51); everything else in (47) and (10) lies in the Π̂₀,₃-components α̃, β. What remains open is how
  these components depend on ξ. Revised: the vague "what information is retained" is answered by the page.
- **N6 — scans 247–248 — conjecture — keep.** "Il faudrait voir si i, j′ peuvent, comme α₃, s'expliciter en termes du
  multiplicateur μ, voire … ε_ℓ(μ)". Data on these pages: u = 1 gives (i, α₃, j′) = (0, 0, 0) with μ = 1; u = τ∞
  gives (1, 1, −1) with μ = −1 ((59)–(60)).
- **N7 — scan 247, bottom-left margin — conjecture — keep.** Whether (i, α₃, j′) takes all values ("ttes sortes de
  valeurs", reading still uncertain) in Z/2 × Z/2 × Z/3.
- **N8 — scan 248, (52)–(53) — own idea (first pass) — correct.** The proposed check was carried out. (52) follows from
  (47)·(10) and ρ⁻¹(ξ)ξ = ρ(ξ)⁻¹ (apply ρ² to ξρ(ξ)ρ²(ξ) = 1). Solving (52) for β⁻¹α̃ gives
  σ∞^i φ̂(ρ(ξ)) ρ^{j′} σ∞^{α₃}, while the ink of (53) has σ∞^{α₃}ρ^{j′}; reducing (53) as written mod Π̂₀,₃ with
  (52) gives 1 = ρ̇^{2j′} when α₃ = 1, false for j′ ≠ 0 (e.g. u = τ∞). So (53) has the last two factors in the wrong
  order; the recap (54) keeps the order of (52), which is correct.
- **N9 — scans 248–249 — conjecture (expectation) — keep.** Working with ξ, η alone would dispense with the delicate,
  unproved existence results "du type ξ = αρ(α)⁻¹, η = βσ∞(β)⁻¹" (inserted on scan 249); (57)–(58) on scan 250 are
  a first instance, since they involve ξ only.
- **N10 — scan 249, (56) — unproved claim — correct.** "qui implique déjà la première formule (14)" is immediate:
  ξ = yρ(y)⁻¹ with y = φ̂(ρ⁻¹(ξ⁻¹)) gives ξρ(ξ)ρ²(ξ) = yρ³(y)⁻¹ = 1, ρ³ acting trivially. Formula (14) is
  ξρ(ξ)ρ²(ξ) = 1 (scan 234). Revised: the implication is proved by this telescoping.
- **N11 — scan 249, (55) — own idea (first pass) — correct.** For α₃ = 1 the relation replacing (56) is the twisted
  coboundary (46), ξ = α̃ℓ₁⁻¹ρ(α̃)⁻¹, so (57) has no direct analogue; this is what the margin of scan 250 records
  ("ici α₃ = 1 donc (57) n'est pas valable"). Revised: the obstruction is identified on the pages themselves.

### Scans 250–253 (examples and the commutant of τ)

- **N12 — scan 250, Remarque — unpursued implication — correct.** Now read: "l'unique élément τ ∈ T^!₀,₃ ⊂ N^{!≈}₀,₃,
  qui dans M^{!≈}₀,₃(0) correspond à l'élément τ∞ = u_ξ = u_{ξ,η}" (struck: "aux invariants"). "l'unique" refers to
  the non-trivial element of T^!₀,₃ ≃ Z/2, not to M(0). The remark only records that τ is the one non-trivial element
  the author can write down, even in the larger N^{!~}₀,₃; it does not claim there are no others.
- **N13 — scan 250, lower-left margin — unproved claim (scope) — correct.** Reading: "ici α₃ = 1 donc (57) n'est pas
  valable" (applicable less likely). (57) was derived under (55), α₃ = 0, i.e. μ ≡ 1 (3), and τ∞ has μ = −1; the
  example is to be checked against (54), as the struck lines and the margin "et aux relations (54)" begin to do.
- **N14 — scan 251, Rmq — conjecture (question) — correct.** The question concerns u_{α,β} = u_{ξ,η} ∈ M^{!~}₀,₃[0]
  "pas nécessairement normalisés" (not "inversibles"), i.e. not assumed to commute with φ̂, with f = 1 and β = 1. The
  page answers it: ξ = ℓ₁^ν = (1 0; 2ν 1), the cocycle criterion of p. 344|342 (§VII "cocycles sous ρ") forces
  C + D − B = 2ν + 1 = μ = ±1, so ν ∈ {0, −1} and u ∈ {id, τ∞}.
- **N15 — scan 251, NB — unproved claim — keep.** "On sait déjà que si α = 1 i.e. ξ = 1, alors u = 1" appeals to an
  earlier result (with f = 1); it is distinct from the case β = 1 treated in the remark.
- **N16 — scan 251, diagonal margin — unproved claim — keep.** The multiplier is "(au signe près quand la normalisation
  de ξ n'est pas faite) égal à l'un des 'coefficients …' de ξ, donc égal à ±1"; the qualifier after "coefficients" is
  still unread, so the statement points back to an earlier argument rather than giving one.
- **N17 — scan 252, Proposition — unproved claim — correct.** The commutant of τ in N^{!~}₀,₃ is {1, τ}; the paragraph
  proves more, in "le gros normalisateur de L₀ dans M^{!~}₀,₃", i.e. M^{!~}₀,₃[0] = Norm(L₀) of scan 243 (the first
  pass read "normalisateur N₀|L₀ de M"). The reduction to (62) is explicit; the conclusion uses (64) on scan 253. The
  margin points to §46 VI|II.
- **N18 — scan 252, (61)–(62) — own idea (first pass) — keep.** Separate the particular solution (63) from the
  fixed-point group that measures the ambiguity; checked: (62) follows from (61), u_ξ(ε₁) = int(ξ)(ε₁^μ), ℓ₁ = ε₁²
  and μ = 2ν + 1.
- **N19 — scan 253, (64) — conjecture — keep.** Uniqueness of (63) is conditional on admitting that "les résultats
  discrets se prolongent au cas profini", i.e. (Π̂₀,₃)^{τ∞} = {1}.
- **N20 — scan 253, (64) — own idea (first pass) — keep.** Checked: two solutions x, y of (62) give
  τ∞(yx⁻¹) = yx⁻¹, so the uniqueness of (63) is exactly (64).
- **N21 — scan 253, last line — own idea (first pass) — correct.** Both readings stand in the ink: "ν = 0 ou −1" on
  251 and "ν = ±1, i.e. u ∈ {1, τ∞}" on 253. Since 2ν + 1 = μ = ±1 and τ∞ has ν = −1, the line on 253 is a slip for
  μ = ±1 (ν = 1 would give μ = 3, not a unit of Ẑ); its conclusion u ∈ {1, τ∞} is that of scan 251.

### Scans 254–263 (§48 I, the morphism α ↦ [α, ρ])

- **N22 — scan 254, after (3) — conjecture (programme) — keep.** "Il s'agit de caractériser l'image" of
  G/T_ρ ↪ G; (4) is a first necessary condition, and scans 255–257 give the characterization for forms of Sl(2),
  Gl(2).
- **N23 — scan 254, G_ab — unproved claim — correct.** For Gl(2) the quotient by the derived group Sl(2) is G_m via
  det, and (4) is det ξ = 1 (condition c) of scan 257). For Sl(2), which is semisimple, the derived group is Sl(2) and
  G_ab is the unit group, although the abstract group Sl(2, Z) has abelianization Z/12; (4) is a condition on the
  sheaf, not on the abstract group.
- **N24 — scan 254, (2)–(3) — own idea (first pass) — keep.** The fibres of F_ρ are the cosets αT_ρ by (2); existence
  over the base is the separate question settled in the proposition and corollary.
- **N25 — scan 255 — unproved claim — correct.** The inserted quantifier reads "après tt chgt de base" (tout). The
  passage invokes Steinberg for local conjugacy of sections in reductive groups and the invariant scheme I_G with a
  universal property "(sur A, et aussi après tout changement de base)"; for the forms of Sl(2), Gl(2) used here,
  (7)–(8) make I_G explicit.
- **N26 — scan 256, (7) — unproved claim — keep.** G/int(G) → I_G is an epimorphism (fppf) but not a monomorphism;
  e.g. in Sl(2) over a field, 1 and (1 1; 0 1) have the same trace and are not conjugate.
- **N27 — scan 256 — unproved claim — keep.** Equality of invariants suffices for local conjugacy of two regular
  sections, and "aussi si les deux sections sont ½ simples (… une condition sur chaque fibre)"; see N29 for the
  limits of the second statement.
- **N28 — scan 256 — unproved claim — keep.** For groups locally isomorphic to Sl(2), GP(1) or Gl(2), regular sections
  are those central at no point; checked on the field-valued level in all characteristics (a non-central element of
  Sl(2) has a one-dimensional centralizer).
- **N29 — scan 256 — own idea (first pass) — keep.** Over k[ε]/(ε²) the Sl(2)-sections I and I + εE₁₂ have the same
  invariants and the same, semisimple, fibre, but are not conjugate; so the "½ simples … condition sur chaque fibre"
  sufficiency needs a stronger notion of semisimple section over non-reduced bases.
- **N30 — scan 257, (7)–(8) — unproved claim — keep.** I_G ≃ E¹ via the trace for forms of Sl(2), and
  I_G = E^{1*} × E¹ via (det, tr) for forms of Gl(2); the matrix computation must be descended to forms.
- **N31 — scan 257, Proposition — unproved claim — correct.** The reference reads "dans l'image de F_ρ ((1) ou (3))":
  the morphism and the monomorphism G/T_ρ ↪ G, not the invariant map (8). Conditions a)–c) (fibrewise
  non-centrality of ξρ, tr ξρ = tr ρ, det ξ = 1 for Gl(2)) are stated "pour mémoire" without proof.
- **N32 — scan 258, Corollaire — unproved claim — keep.** The solutions of [α, ρ] = ξ form a right T_ρ-torsor, T_ρ
  "lisse commutatif" of relative dimension 1 or 2; see N33.
- **N33 — scan 258 — own idea (first pass) — keep.** Checked: the centralizer of (1 1; 0 1) in Sl(2) over F₂ is
  {(a b; 0 a), a² = 1} ≅ μ₂ × G_a, not smooth, although (1 1; 0 1) is non-central; so "lisse" fails for forms of
  Sl(2) in characteristic 2. For the ρ of (12) it holds: at 3 the norm-one equation becomes (a − b)² = 1, étale in
  characteristic 3, and at 2 the fibre is a torus.
- **N34 — scan 258, (9) — unproved claim — correct.** Forms of Sl(2) and of GP(1) are classified by PGL(2)-torsors,
  i.e. Azumaya algebras of rank 4, but Gl(2) has the outer automorphism g ↦ det(g)⁻¹g (it inverts the centre), so
  "une forme de Gl(2) équivaut à … une Algèbre d'Azumaya" holds for inner forms only. Revised: the needed restriction
  is identified.
- **N35 — scan 259, (10) — unproved claim — keep.** Fibrewise regularity makes O_S + O_Sρ = A_ρ a quadratic
  subalgebra, locally a direct factor of M, compatible with base change; not proved here.
- **N36 — scan 259, (11)–(11bis) — unproved claim — keep.** T_ρ is the unit scheme of A_ρ, resp. its norm-one part
  for SG(M); this needs the centralizer computation and the agreement of det with the norm of A_ρ.
- **N37 — scan 259, (12) — unproved claim — correct.** The lower-right entry of (12) is overwritten in the ink;
  ρ⁶ = 1, ρ³ = −1 and the same ρ on scans 258 and 261 give (0 1; −1 1). Its characteristic polynomial x² − x + 1 has
  discriminant −3, so ρ has distinct eigenvalues exactly in characteristic ≠ 3, as stated; the text then reads "donc
  au|en sens strict T_ρ (… sur Spec Z) n'est pas un tore" (first pass: "sur Ainsi").
- **N38 — scan 260 — unproved claim — keep.** Checked: σ has characteristic polynomial x² + 1 (discriminant −4),
  unipotent in characteristic 2, where T_σ ⊗ F₂ = (F₂[x]/(x + 1)²)^* ≅ G_m × G_a; likewise T_ρ ⊗ F₃ for ρ.
- **N39 — scan 260 — unproved claim — keep.** T_ρ is the Weil restriction of G_m from A_ρ, so its torsors are the
  invertible A_ρ-modules and are Zariski-locally trivial; torsors under ST_ρ need not be.
- **N40 — scan 260, last paragraph — conjecture — keep.** "mais peut-être pas dans SG(M)": the determinant-one
  lifting problem, answered on scans 262–263 by the norm obstruction (21).
- **N41 — scan 261, margin — unproved claim — keep.** Trace and determinant conditions (16) give a local solution "du
  moins si on suppose que la condition de régularité n'est violée sur aucune fibre".
- **N42 — scan 261, (17) — conjecture (expectation) — correct.** Checked: A_ρ = Z[ρ] ≅ Z[e^{2iπ/6}], the Eisenstein
  integers, which form a principal ideal domain (class number 1 of Q(√−3)); so Pic(A_ρ) = 1 and the "sauf erreur" is
  confirmed. Reading: "l'obstruction est un A_ρ-Module inversible, or A_ρ est principal".
- **N43 — scan 261, (16) — own idea (first pass) — keep.** Separate the scheme AD − BC = 1, C + D − B = 1 from its
  fibrewise regular open part and determine the excluded locus at 3.
- **N44 — scan 262 — conjecture — correct.** "les calculs faits par ailleurs suggèrent que ce signe est aussi égal au
  reste de D mod 3": proved below for D ≢ 0 (3), and D ≡ 0 (3) occurs with both signs (C2).
- **N45 — scan 262, last display — own idea (first pass) — correct.** The ink "f ∈ Γ O̲_S^*" is confirmed. The
  argument needs f ∈ Γ(S, T_ρ), the units of A_ρ (as "f ∈ A_ρ^*" for Z on the same page, and as (20)–(21) use,
  det f being a norm from A_ρ); for a scalar f, det f = f² and (20) would not follow. A slip.
- **N46 — scan 262 — unpursued implication — keep.** The sign of det α does not depend on the solution α (det f =
  f f̄ > 0 for f ∈ A_ρ^*); it is an invariant of ξ.
- **N47 — scan 263, (20)–(21) — unpursued implication — keep.** The determinant-one problem becomes the class of det α
  in A^*/N_{A_ρ/A}A_ρ^*; functoriality of these classes is not developed.
- **N48 — scan 263 — conjecture (expectation) — correct.** Checked by local class field theory: for ℓ ≠ 3,
  A_ρ ⊗ Z_ℓ is étale over Z_ℓ (split or unramified), so every unit is a norm; for ℓ = 3 it is the ring of integers of
  the ramified Q₃(√−3), and Z₃^*/N ≅ Z/2 (N(a + bρ) = a² + ab + b² ≡ (a − b)² mod 3, so −1 is not a norm). The
  "sauf erreur" claim is right.
- **N49 — scan 263, margin norm formula — own idea (first pass) — correct.** The formula N(cρ + d) = c² + cd + d² is
  right (ρ ↦ ω with ω + ω̄ = ωω̄ = 1). The proposed computation was done mod 3 for the sign of scan 262 (C2).
- **N50 — scan 263, last sentence — unproved claim (continuation) — keep.** "des calculs immédiats déjà faits montrent
  que" continues on the next page; nothing is inferred here.

## New notes

- **C1 — scan 251, matrix of ±ρ⁻¹ — own idea, Claude (second pass).** The ink writes ξ̲ = ±ρ̲⁻¹ = ±(−1 1; 1 0)
  (lower-left entry 1, checked on a crop). With ρ = (0 1; −1 1), ρ⁻¹ = (1 −1; 1 0), and the written matrix has
  determinant −1, so it is not ±ρ⁻¹; probably a slip for ∓(1 −1; 1 0). It does not affect the argument, since this
  alternative is dismissed ("ce qui manifestement n'est pas le cas").
- **C2 — scan 262, the sign of det α — own idea, Claude (second pass).** For α = (p q; r s) ∈ Gl(2, Z) and
  ξ = [α, ρ] = (A B; C D): mod 3, ρ ≡ −(1 + n) with n = (2 2; 1 1), n² = 0, and a direct computation gives
  D ≡ det(α)·(r − s)² (mod 3). Hence D ≢ 0 (3) implies det α ≡ D (3), which proves the author's suggestion "1 si
  D ≡ 1 (3), −1 si D ≡ −1 (3)". But D ≡ 0 (3) occurs with both signs: α = (1 0; 1 1) gives ξ = (0 1; −1 3) with
  det α = 1, and α = (1 0; −1 −1) gives ξ = (−2 1; 5 −3) with det α = −1; then tr ξ ≡ 0 (3) for det α = 1 and ≡ 1
  for det α = −1 (checked on all 744 α ∈ Gl(2, Z) with entries in [−6, 6]). This is the explicit form of the ℓ = 3
  obstruction Z₃^*/N ≅ Z/2 of scan 263: the sign depends only on ξ mod 3.
- **C3 — scan 250, (57)–(58) — unproved claim, Claude (second pass).** (58) is (15) with ν ≡ 0 (3), and (57) implies
  (14) by the telescoping of N10; the converse, (14) (15) ⟹ (57), goes through α (via (47 bis) with α₃ = 0), so the
  stated equivalence for μ ≡ 1 (3) rests on the existence results that N9 hopes to avoid. Only the conjunction of
  (57) and (58) can be equivalent to (14) (15), which supports the reading "l'ens des deux relations".
