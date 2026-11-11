# LM_C3-302-320 — research notes, checked against the corrected transcription (scans 302–320)

Source: the first pass's research notes (answers/unzipped/LM_C3-302-320/LM_C3-302-320_notes.md, §4, notes 1–39), each
checked against LM_C3-302-320_checked.tex. Verdicts: keep, correct (text revised), drop. Notes marked **Claude (second
pass)** are new. Kinds: conjecture (Grothendieck's conjectures, questions, programme), unproved claim, unpursued
implication, own idea. "Unproved" means not proved in the cited passage.

Conventions used in the checks (those of the pages): after the normalisation u = 1, ρ = (0 1; v w), σ = (0 −1; −v 1−w)
(on scans 306–307 ρ = (0 v₁; v w), σ = (0 v′₁; v′ w′)), N = ρ + σ = (0 0; 0 1), N₀ = (0 1/v; 0 0),
N₁ = ρN₀ρ⁻¹ = σN₀σ⁻¹ = (0 0; 1 0), ε₀ = 1 + N₀, ε₁ = 1 + N₁, ε₁(t) = 1 + tN₁, [x,y] = xyx⁻¹y⁻¹ and ρ(x) = ρxρ⁻¹. With
these, σ⁻¹ρ = −ε₀ (39 bis), ρσ⁻¹ = −ε₁, (42), (46), (47), (47 bis), ζ = ηε₁(μ−1), (54), (56)–(58) and (36)–(37) of
scan 320 were all recomputed and hold, except for the slips listed below.

## Notes of the first pass

### Scans 302–305

- **N1 — scan 302, lower-left NB — unproved claim — correct.** The claim holds over any base: 1, ρ, N = ρ+σ and
  ρN = (0 1; 0 w) have coordinate determinant v, a unit because det ρ = −v, so they form a basis of M₂(O_S). Hence 1, ρ, σ
  are independent on every fibre, the commutant of {ρ, σ} is O_S, and T_ρ ∩ T_σ = G_m, T̃_ρ ∩ T̃_σ = {1} hold
  scheme-theoretically. (Revised: the first pass only asked for a proof.)
- **N2 — scan 302, last paragraph — unproved claim — correct.** "u = αv" is immediate: the chain gives N = ρN₀ =
  (0 0; 0 vα) and the display gives N = (0 0; 0 u). The inserted "N₀ (= ρN₁ρ⁻¹)" is a different matter, see C1.
- **N3 — scan 302, (37 bis) — own idea — correct.** An idempotent always splits the module, so the proviso "when image
  and kernel are locally direct summands" is automatic; with Tr N = c = 1 both are invertible modules and N gives a
  canonical splitting O_S² = Im N ⊕ Ker N that the normalisation u = 1 turns into coordinates. The question of a
  basis-free reading of the normalisations stands.
- **N4 — scan 303, after the γ display — unpursued implication — keep.** The page gives no reason for preferring
  μ = γ + 1; scan 319 ((31)–(32)) supplies one meaning, μ = det u = δ(ũ), the factor by which ũ acts on N₀ (see N34).
- **N5 — scan 303, (40) — own idea — keep.** P(ζ) = D makes the locus "D invertible" the natural domain, as (42),
  (58) and scan 320 confirm.
- **N6 — scan 304, (41)–(43) — unpursued implication — keep.** Nothing on these pages treats D = 0. The last member of
  (41) reads "Tr σ|α" in the ink (unresolved); only Tr σ fits (II) and the use on scan 309.
- **N7 — scan 304, before (45) — unproved claim — correct.** The announced calculation is complete on scan 305: every
  entry of [u,ρ], [u,σ] and (46)–(48) was recomputed and holds (apart from the slip of C3), and (48) is the inverse on
  the open set where D is invertible.
- **N8 — scan 305, (46)–(48) — own idea — drop.** The manuscript does it itself on scan 306: (47 bis)–(48 bis) recover
  μ, λ from η (S = B, U = D, u = (1/U S/U; 0 1)).

### Scans 306–309

- **N9 — scan 306, NB beside (54) — unproved claim — correct.** Every term of (−δ_α vv₁)B and (−δ_α vv₁)D contains v₁,
  and v₁ is a unit because det ρ = −vv₁ is; so the division is legitimate over any base, and (56) carries it out by
  striking v₁.
- **N10 — scan 306, left margin — own idea — correct.** The margin now reads "On ne pose pas v₁ = 1, pour n'avoir pas à
  refaire le m̄ calcul pour [β,σ] que pour [α,ρ] !": σ has v′₁ = −v₁, which cannot also be 1, so one general computation
  serves both commutators, and (55) is (54) with (a,b,c,d,v,v₁,w) replaced by (r,s,t,u,v′,v′₁,w′).
- **N11 — scan 307, (56)–(58) — unproved claim — correct.** Verified: for v₁ = 1 the numerator −vd² + wcd + c² equals
  det(dρ + c) and the denominator −vδ_α equals det ρ · det α, so (58) holds whenever det α is a unit.
- **N12 — scan 307, (57)–(58) — own idea — keep.** The principal open set det(dρ + c) invertible is exactly the domain
  of u(α) = (1/D B/D; 0 1); see also N39.
- **N13 — scan 308, before (1) — conjecture — keep.** The projective version (1) is posed as a programme; scans 309–319
  carry it out (G̃*_{ρ,σ}, (9)–(13), (30)).
- **N14 — scan 308, last paragraph — unproved claim — correct.** Both points are immediate: [λα,ρ] = [α,ρ] for a unit λ,
  so (2) involves only α̃, β̃, and ε = [α,ρ] ε₁(μ−1)⁻¹ [β,σ]⁻¹ is determined.
- **N15 — scan 309, "ε Tr σ = Tr σ" — unpursued implication — keep.** The condition says (ε − 1)Tr σ = 0 for the given
  ε; the lemma of scan 310 asks for it for all sections of μ₂.
- **N16 — scan 309, compared with scan 310 — own idea — correct.** Resolved: "Tr η" on scan 309 abbreviates Tr(ησ).
  Since η₀σ = βσβ⁻¹, Tr(η₀σ) = Tr σ, so Tr(ησ) = ε Tr σ, which is the underbrace "ε Tr η₀ = ε Tr σ" read with the
  factor σ; (41) and the lemma state the condition in full.

### Scans 310–313

- **N17 — scan 310, "E^{μ₂} = (0)" — unproved claim — keep.** As stated; scan 314 gives the argument over S
  ("faisant varier ε") and with ε = −1 when 2 is invertible.
- **N18 — scan 310, insertion "Enfin …" — unproved claim — correct.** Add the label history: c) "σ² ∈ ΓG_m" was struck,
  the normal-form condition (labelled d) over c), unresolved) became the third condition, and "d) On a σ² ∈ ΓG_m" was
  added in the margin. The sentence "L'équivalence de b) et d) est immédiate, reste à prouver b) ⟺ c)" keeps the labels
  of the first version (c) = σ² scalar, d) = normal form); Hamilton–Cayley gives b) ⇒ σ² scalar and, for σ nowhere
  scalar, the converse.
- **N19 — scan 310, fixed points — own idea — keep.** Testing with non-reduced points of μ₂ in characteristic 2 is the
  right check of "a) ⟺ b)"; scan 314 ((e), (f)) separates the two cases in the same way.
- **N20 — scan 311, first paragraph — own idea — correct.** Enlarged, the ink has "Tr σ = 0 ⟹ σ = det σ.1" (no exponent,
  no sign) and "(Tr σ)σ = σ² − det σ.1"; Hamilton–Cayley gives σ² = −det σ · 1 and (Tr σ)σ = σ² + det σ · 1. Both are
  slips of the pen; the argument only uses that both sides are scalars and is unaffected.
- **N21 — scan 311, converse — unproved claim — correct.** The gap closes by Nakayama: if σ is nowhere scalar, 1 and σ
  are independent on every fibre, so O_S · 1 ⊕ O_S · σ is a direct summand of the Azumaya algebra, and (Tr σ)σ ∈ O_S · 1
  forces Tr σ = 0 also over non-reduced bases.
- **N22 — scan 311, (8)–(9) — unproved claim — keep.** The comparison of G* with the inverse image of G̃* needs local
  liftability of PG-sections to G (G → PG is a G_m-torsor), which the page does not discuss.
- **N23 — scan 312, (14)–(15) — unproved claim — keep.** The fibre description is stated, not proved; it is used on
  scan 313.
- **N24 — scan 313, uniqueness — unproved claim — correct.** The subscript reads α in the ink (T_α, a slip for T_ρ,
  see C9), and the intersection T_ρ ∩ B′₀ = {1} holds scheme-theoretically (C9).

### Scans 314–317

- **N25 — scan 314, corollary (e)–(f) — unpursued implication — keep.** The corrected heading reads "les conditions
  équiv. du lemme sont impliquées par les suivantes ; et l'impliquent si σ est régulière :"; the "aussi" of the first
  pass is not in the ink.
- **N26 — scan 315, opening — unproved claim — keep.** The local conjugacy of regular sections with equal trace and
  determinant (for GL₂, fppf or étale locally) is quoted from Steinberg, not proved.
- **N27 — scan 315, (23) — unproved claim — keep.** Exactness at T_σ is the definition of the centraliser; local
  surjectivity onto μ₂ is the argument (e) of scan 314–315 (εσ is regular with the same trace and determinant).
- **N28 — scan 316, after (24) — unpursued implication — correct.** As corrected (changes, row 34), the ink says
  "toute section de N′_σ est en fait une section de N_σ", the trivial inclusion; the argument (2b = 0 with 2 a
  non-zero-divisor gives b = 0, then det gives a² = 1) proves the converse N_σ(S) ⊂ N′_σ(S), which is what is meant. It
  is a statement about sections over S and does not survive base change to a base where 2 becomes a zero-divisor.
- **N29 — scan 316, characteristic 2 — own idea — keep.** Checked: with σ = I + J, τ = diag(a,1), τστ⁻¹ = I + aJ and
  [τ,σ] = I + (a+1)J, scalar only for a = 1; so τ ∈ N_σ but τ ∉ N′_σ for a ≠ 1.
- **N30 — scan 316, the two equations — own idea — keep.** C11 solves the system explicitly.
- **N31 — scan 317, (25)–(26) — unproved claim — correct.** Existence is immediate from the text's own data: given
  (α,β,μ,ε) in G*, take u ∈ B′₀ with ([u,ρ],[u,σ],det u) = ([α,ρ], ε[β,σ], μ) (B′₀ ≅ X_{ρ,σ}); then a = α⁻¹u ∈ T_ρ and
  b = β⁻¹u satisfies bσb⁻¹ = εσ, so b ∈ N′_σ with ε_σ(b) = ε. With the monomorphy proved on the page, (26) is an
  isomorphism.

### Scans 318–320

- **N32 — scan 318, (27)–(28) — own idea — keep.** (28) is sufficient only together with ũ′ = ũ; the necessity
  argument of the page indeed yields ũ = ũ′ first.
- **N33 — scan 318, (29)–(30) — unproved claim — correct.** (29) holds over any base: if x = c + dρ ∈ T_ρ equals λy with
  y ∈ B′₀ and λ a unit, the (2,1) entry gives dv = 0, so d = 0 and x is scalar, x̃ = 1. The rest of the note stands.
- **N34 — scan 319, (31)–(32) — unpursued implication — keep.** With u = (μ λ; 0 1), uN₀u⁻¹ = μN₀, so (32) does give
  δ(ũ) = μ = det u and is independent of the representative; this is the intrinsic meaning of μ asked for in N4.
- **N35 — scan 319, right NB — unproved claim — keep.** C13 gives the short proof.
- **N36 — scan 319, left NB — own idea — correct.** The count is consistent: B̃′₀, T̃_ρ, Ñ′_σ have relative dimensions
  2, 1, 1 and α̃ has 3, the remaining 1 being the operation of Ñ′_σ on β̃ inserted in the remark ("mod op. de Ñ′_σ sur
  β"). In the NB the middle factor is a T written over an A.
- **N37 — scan 319, η̃ = ζ̃ε̃₁(μ−1) — own idea — correct.** Verified slip: ζ = ηε₁(μ−1) by (41), and η = ζε₁(1−μ) is
  written on scan 304 and checked on (46); "ε̃₁(μ−1)" on scan 319 should be ε̃₁(1−μ).
- **N38 — scan 320, (33)–(37) — unpursued implication — keep.** The complement det(dρ + c) = 0 is not studied here.
- **N39 — scan 320, (37) — own idea — correct.** Verified: O_S[ρ] = O_S[X]/(X² − wX − v) is free with basis 1, ρ, and
  the norm of c + dρ is c² + cd Tr ρ + d² det ρ = c² + cdw − vd² = det(c + dρ). So (−δv)D is the norm of c + dρ and the
  condition of (58) is independent of the basis.

## Claude (second pass) — new notes

- **C1 — scan 302, insertion "N₀ (= ρN₁ρ⁻¹)" — own idea.** With N₁ = ρN₀ρ⁻¹, stated three lines above, one has
  N₀ = ρ⁻¹N₁ρ; with the normalised ρ, ρN₁ρ⁻¹ = (−w/v 1/v; −w²/v w/v), equal to N₀ only when w = 0. The insertion was
  enlarged and reads ρN₁ρ⁻¹; it is kept as written. Confidence high (direct multiplication).
- **C2 — scan 303, the γ display — own idea.** The recalled form "[α,ρ] = [β,ρ]ε₁(γ)" has ρ in the second bracket (its
  descender is visible); (32), (49) and (*) have [β,σ]. A slip of the pen, kept in the transcription.
- **C3 — scan 305, second factor of [u,σ] — own idea.** (1 −λ; 0 μ)(w′ 1; −v′ 0) has lower-left entry −μv′; the ink's
  −μw′ is a slip, and the next line is computed with −μv′, so no later formula is affected.
- **C4 — scan 306, (52) — own idea.** ρ + σ = N = (0 0; 0 v₁) forces v′ = −v, v′₁ = −v₁ and w + w′ = v₁, the last of
  which is written; the value of v′₁ seems to carry a prime in the ink (−v′, unresolved), which would be a slip, and (55)
  is computed with v′₁ = −v₁ (v′v′₁ = vv₁, v′₁² = v₁²).
- **C5 — scan 307, (55) — own idea.** Recomputing η = [β,σ] gives (−vv₁δ_β)S = −(v₁v)su + v₁²tr − v₁w′st. The enlarged
  ink has no minus before (v₁v)su, while the U formula has it: a sign slip in S only, kept in the transcription.
- **C6 — scan 307, last line — unpursued implication.** After (58) the text breaks off ("mais je m'aperçois que c'est une
  forme plate,", last word unresolved) and §V opens with the projective equation and the condition Tr σ = 0. The explicit
  completion condition returns on scan 320 ((33)–(37)), now with w = 1; what the author noticed is not stated.
- **C7 — scan 308, heading — own idea.** The heading is "V Étude (de l'équation) dans GP(1), et la condition Tr σ = 0",
  while the author's later table (Grothendieck Circle) titles §48.V "L'équation αρ(α⁻¹) = ε(βσβ⁻¹)ε₁(μ−1); le groupe
  G*_{ρ,σ}", naming equation (2) and the group G* that the section introduces on scans 311–317.
- **C8 — scan 312, (13) — own idea.** The relation is written "=" (changes, row 27), but by (12) and "‖ déf ε̃⁻¹(1)",
  G̃_{ρ,σ} is an open and closed subscheme of G̃*_{ρ,σ}, proper as soon as ε̃ takes the value −1, which (23) and (26)
  provide locally when 2 is invertible. "⊂" is meant.
- **C9 — scan 313, uniqueness — own idea.** The display reads T_α ∩ B′₀ = {1}; T_ρ is meant, as on scans 317–318. It
  holds over any base: c + dρ = (c d; dv c+dw) lies in B′₀ iff dv = 0 and c + dw = 1, i.e. (v being a unit) d = 0, c = 1.
- **C10 — scan 316, "donc si b est inv." — own idea.** Enlarged, the letter is the b of "2b", not a 2; the step
  2b = 0 ⇒ b = 0 needs 2 invertible, as (24) ("en car. résiduelle ≠ 2") and the next paragraph show. A slip, kept.
- **C11 — scan 316, the system in characteristic 2 — own idea.** In characteristic 2, −va² + b² = −v reads
  b² = v(a + 1)². Over a field containing s with s² = v every unit a gives b = s(a + 1), a one-parameter family of
  normalising τ outside N′_σ; if v is not a square only a = 1, b = 0 occur on the field's points, and over k[t]/(t²) every
  b = tc with a = 1 occurs. So N_σ ≠ N′_σ as schemes in characteristic 2 even where field points agree. Confidence high.
- **C12 — scan 317, "En effet" — own idea.** The second line reads βρ(β)⁻¹ (ρ with its descender, kept) where βσ(β)⁻¹ is
  computed; the rest of the line, u b⁻¹σ(b⁻¹)⁻¹σ(u)⁻¹ = εuσ(u)⁻¹, concerns σ.
- **C13 — scan 319, right NB — own idea (proof of an unproved claim).** τ̃ centralises σ̃ in PG iff τστ⁻¹ = λσ for a
  unit λ; taking determinants, λ² det σ = det σ, so λ ∈ μ₂ and τ ∈ N′_σ with ε_σ(τ) = λ. Hence the centraliser of σ̃ is
  Ñ′_σ, an extension of μ₂ by T̃_σ by (23).
- **C14 — scan 319, lower-left NB — own idea.** ζ = αρ(α)⁻¹ does not depend on the lift α of α̃: for a unit λ,
  ρ(λα) = λρ(α), so (λα)ρ(λα)⁻¹ = αρ(α)⁻¹. The reading "ζ ne dépend [pas] du choix du relèvement" is the true
  statement; if the heavy bar through "ne" (unresolved) is a strike, the note as corrected would be false.
- **C15 — scan 320, "(α,β,μ,ε) ∈ ΓG…_{ρ,σ}" — own idea.** The scheme meant is the G*_{ρ,σ} of (8) and (26); the
  α-like superscript of the ink (changes, row 41) is a slip or a hasty star.
