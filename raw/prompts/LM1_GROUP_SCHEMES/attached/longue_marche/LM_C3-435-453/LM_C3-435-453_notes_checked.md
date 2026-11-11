# LM_C3-435-453 — research notes, checked against the corrected transcription (scans 435–453)

Source: the first pass's research notes (answers/unzipped/LM_C3-435-453/LM_C3-435-453_notes.md, §5, notes 1–46). Each
is checked against LM_C3-435-453_checked.tex. Verdicts: keep, correct (text revised), drop. Notes marked
**Claude (second pass)** are new. Kinds: conjecture (Grothendieck's conjectures, questions, expectations), unproved
claim, unpursued implication, own idea. "Unproved" means not proved in the cited passage.

Notation used in the checks (all read off these pages):
- Θ: M → G and Θ̃ = can∘Θ: M → PG.
- R = Ker Θ̃, SR = Ker Θ, κ: R → G_m ≃ Centr(G) ((112)), and χ = det∘Θ.
- M = (R × SG)/μ₂, with μ₂ embedded by ε ↦ (ε, ε⁻¹). This is (102), called "la définition de M_ρσ" at (148) on 452.
- Elements of T_σ are written cσ + d, with σ² = ν and det = d² − νc² (445).
- On N′_σ the determinant is written δ_σ up to scan 446 and δ′_σ from 448 on; (137) sets δ_σ = δ′_σ|T_σ.

## Notes of the first pass

### Scans 435–439

- **N1 — 435, (99)–(101) — unproved claim — correct.** That R commutes with SG holds by construction: (148) defines M
  as (R × SG)/μ₂ ("c'est ici la définition de M_ρσ", 452), and R ∩ SG = μ₂ is the kernel of that quotient. The author
  first wrote and then struck "mais R_ρσ ne commute plus". The stated reason, "par définition de R comme Ker Θ̃", only
  puts the commutator [r, s] in SR = Ker Θ, because Θ(r) is central. Revised: the definition (148) supplies the
  commutation.
- **N2 — 436, (104)–(105) — unproved claim — correct.** The square is numbered (105), not (105′) (change 7). The chain
  checks out as follows. uf = λ with det f = 1 gives det u = λ² (the author's "d'où λ² = det u"). Then u and
  ε′ = det b/det a are eliminated, which leaves {(a, b, λ) | det b = λ², (det a)² = (det b)²}. That set is the
  displayed iterated fibre product. For the cartesian square, see C1.
- **N3 — 437, after (106) — unpursued implication — correct.** The inserted claim can be checked directly. The inverse
  image of 𝒯⁺ in R is SR·μ₂ = SR × μ₂: μ₂ = Ker(R → 𝒯) meets SR = Ker Θ trivially, because Θ maps that central μ₂
  isomorphically into the centre of G. So the face (*) is not cartesian. The lower square of (106) is the cartesian
  square (105); the cubes (95)–(96) themselves are on earlier pages.
- **N4 — 438, (111)–(114) — unproved claim — correct.** The descent is immediate. The map (r, s) ↦ κ(r)s on R × SG kills
  (ε, ε⁻¹), because κ restricted to μ₂ is the inclusion (the "‖" column of (106)). Exactness of (114) follows from (102)
  together with R/μ₂ ≃ 𝒯 ((151)). Revised: verified.
- **N5 — 439 — conjecture/expectation — keep.** "permettront peut-être de les retrouver" is an expectation. The data
  named in it remain doubtful readings, both the word "entiers" and the argument (w|ω), so the structure meant cannot be
  stated precisely from this page.

### Scans 440–444

- **N6 — 440, end — unproved claim — keep.** The common quotient μ₂ × μ₂ of the vertical inclusions is given on 451 by
  (ε₃, ε₂) ((145)–(146)). That identifies the four quotients the author calls isomorphic. The cartesian and
  cocartesian properties of the lateral faces are still unverified.
- **N7 — 436–438 — own idea (first pass) — keep.** Testing on rings with nilpotents is relevant: the isogeny R → 𝒯 and
  λ ↦ λ² have kernel μ₂, which is not étale over 2. C1 gives the fppf argument for (105).
- **N8 — 438 — own idea (first pass) — keep.** Characters of M that are trivial on SG factor through 𝒯 = M/SG. (107)
  builds 𝒯 together with χ and (ε₃, ε₂), and (143) calls (χ, ε₃, ε₂): M → G_m × μ₂ × μ₂ an epimorphism.
- **N9 — 441, after (117) — unproved claim — correct.** The face is "la face composée antérieure gauche" (change 14): the
  composite of the left faces of the two adjoining cubes (SR → M⁺ → 𝒯⁺ over the ° row). The product formula follows
  from (123): χ(r, s) = κ(r)², so M⁺ = (κ⁻¹(μ₂) × SG)/μ₂ = (SR × μ₂ × SG)/μ₂ ≃ SR × SG. This is (149).
- **N10 — 441, (118) — unpursued implication — correct.** The ink cites "(cf. (107), (103))"; the 7 is probably a slip
  for (102) (change 15). The μ₂-covers M̃ = R × SG and M̃° = R° × SG are the middle terms of (102) and (103). Where μ₂ is
  not étale, "revêtement" has to be read as a μ₂-torsor (fppf).
- **N11 — 442, (118)–(120) — unproved claim — correct.** The corrected text reads "dont le composé avec χ : 𝒯° → G_m
  est donné en effet par λ ↦ λ² (104)" (changes 16, 17). So χ∘i_𝒯 = (λ ↦ λ²), not χ = i_𝒯. R° is the fibre product of
  𝒯° and G_m over χ and λ ↦ λ² (the ° form of (105), C1). The pair (i_𝒯, id) therefore gives a unique i_R with
  can∘i_R = i_𝒯 and κ∘i_R = id, and (120) and (122) record exactly these two conditions.
- **N12 — 442, opening — unproved claim — keep.** That the four squares of the faces sup. and inf. become cartesian and
  cocartesian after passing to the μ₂-covers is not verified on these pages.
- **N13 — 443, (122)–(123) — unproved claim — correct.** The centrality needed for a direct product can be read off
  (124). i_R(λ) = (1, 1, λ) maps to (λ, λ), a pair of scalars, which are central in T_ρ × N′_σ. The kernel of
  R → T_ρ × N′_σ is the central μ₂ of (125), so every commutator [i_R(λ), r] lies in μ₂ and is trivial at λ = 1. That
  makes the product direct over reduced bases; the general case needs the explicit description (104).
- **N14 — 443, (121) — unpursued implication — keep.** Only one row and an unattached vertical stroke are drawn. Nothing
  may be supplied.
- **N15 — 443, (123) — own idea (first pass) — keep.** The inverse r ↦ (r·i_R(κ(r))⁻¹, κ(r)) is right, since Ker κ = SR
  (on R, Θ = incl∘κ by (112)).
- **N16 — 444, (124)–(126) — unpursued implication — keep.** The kernel is computed on points. (126) presents 𝒯 as a
  quotient by the diagonal μ₂; reading it as a quotient of fppf sheaves needs no extra argument.
- **N17 — 444, right margin — own idea (first pass) — correct.** The computation: det(λa) = λ² det a and (det a)² = 1,
  so det(λa)² = λ⁴ = det(λb)², since det b = 1. The equality holds. The label "λ²" under det(λa) is right only up to the
  sign det a = ±1, which the square removes.
- **N18 — 444, (127) — unpursued implication — keep.** Identifying the triple map with (48) needs the earlier page.

### Scans 445–447

- **N19 — 445, (128) — conjecture/question — keep.** The "?" under Cent(SN′_σ) marks the open step. The cancelled
  element-wise computation and the inserted (130) are two successive attempts at it (C3).
- **N20 — 445, inserted (130) — unproved claim — correct.** The step holds over any base (C3). The conjugation action of
  N′_σ/T_σ ≃ μ₂ on T_σ is the μ₂-action d + cσ ↦ d + tcσ. Its scheme-theoretic fixed points are c = 0, i.e. G_m. Hence
  Cent(SN′_σ) = ST_σ ∩ G_m = μ₂ without "si 2 inv.", which the author struck.
- **N21 — 445, cancelled computation — own idea (first pass) — correct.** The comparison it proposed explains the
  revision. The struck argument used the point −1 (acting by x ↦ x⁻¹), so it computed ₂(ST_σ). That equals μ₂ only if
  2 is invertible; for sections it suffices that 2 be a regular section of 𝒪_S (the cancelled hypothesis, change 25).
  The μ₂-fixed-point argument removes the hypothesis.
- **N22 — 445, Cent(M) = Cent(R) — unpursued implication — keep.** Verified on the page's own terms. Cent(M) ⊂ R because
  PG has trivial centre. An element of R commutes with SG, so it is central in M = R·SG iff it is central in R. Then
  R ≃ S′T_ρ × SN′_σ × G_m gives (128).
- **N23 — 446, (130)–(132) — unproved claim — correct.** Assume T_ρ and T_σ are the unit tori of ℤ[ζ₆] and ℤ[i] in the
  modular case; this is not restated here. Then T_ρ(ℤ) ≃ ℤ/6ℤ and T_σ(ℤ) ≃ ℤ/4ℤ, and all these units have norm 1.
  Elements of N′_σ(ℤ) outside T_σ(ℤ) have determinant −1. So S′T_ρ(ℤ) = T_ρ(ℤ) and SN′_σ(ℤ) = T_σ(ℤ), as the labels
  of (130) say.
- **N24 — 446, (133) — unpursued implication — keep.** On ℤ-points the quotients μ₂ × μ₂ and μ₂ of the horizontal
  arrows disappear (N26). The dimensions 3 and 2 are those of the generic fibres.
- **N25 — 446, (131)–(132) — own idea (first pass) — correct.** The orders are 24 and 48. The inclusion is
  Cent(M)(ℤ) = (Cent(M) ∩ M°)(ℤ) ⊂ R°(ℤ), of index 2, as 447 states ("qui en est un sous-groupe d'indice 2").
- **N26 — 447, opening — unproved claim — correct.** Verified given N23. R°(ℤ) → R(ℤ) is bijective because
  S′T_ρ(ℤ) = ST_ρ(ℤ) and SN′_σ(ℤ) = ST_σ(ℤ). The same holds for ST_ρ(ℤ) × μ₂(ℤ) × G_m(ℤ) → S′T_ρ(ℤ) × μ₂(ℤ) × G_m(ℤ).
  This is a statement about ℤ-points only, as written.
- **N27 — 447, (136) — conjecture/expectation — keep.** "on aura un homomorphisme canonique M̃₀,₃ → M_ρσ(Ẑ)/Σ"
  announces a construction that is not given here.
- **N28 — 447, (135)–(136) — own idea (first pass) — keep.** Σ = {±1}³ is exactly the 2-torsion of
  Cent(M)(ℤ) ≃ ℤ/6ℤ × {±1}² ("d'ordre 8, d'indice 3"). Whether it is the right ambiguity group remains open on this page.

### Scans 448–451

- **N29 — 448, after (134) — unproved claim — keep.** "se reconstruit … à partir des données (135)" is announced. The
  checks follow on 449–451 ((137)–(147)).
- **N30 — 448, (134)–(135) — own idea (first pass) — correct.** (137) on 449 settles the notation: SN′_σ = Ker δ′_σ and
  δ_σ = δ′_σ|T_σ. The unprimed δ_σ on N′_σ in (104), (108)–(110), (135) and (152′) is either earlier notation or a slip;
  (144) writes δ′_σΘ_σ.
- **N31 — 449, first paragraph — unproved claim — keep.** M is described as the quotient of the "somme" of the four
  factors by the diagonal μ₂. The struck "amalgamée" shows that the amalgamated sum was replaced by this quotient.
- **N32 — 449, second paragraph — unproved claim — correct.** The inserted wording is "et que leur produit de leurs
  valeurs sur les images d'un ε ∈ Γμ₂ est triv." (change 27). This is the condition for the four composites to descend
  through the diagonal μ₂. (138)–(141) record it as "compatibilités triviales / satisfaites".
- **N33 — 449, (137)–(138) — own idea (first pass) — keep, extended.** Three visible slips are recorded, without
  emendation:
  - "μ₂ ⊂ G_m —i_ρ→ T_σ" in (137); (135) has i_ρ: G_m → T_ρ.
  - "Θ_Gj_μ: G_m → G_m incl. can." in (138); (136) has j: G_m ↪ G.
  - "Θ_ρj_ρ: S′T_σ ↪ T_ρ" in (139) on 450, for S′T_ρ.
- **N34 — 450, (139)–(140) — unproved claim — keep.** "compatibilités triviales" is asserted, not checked.
- **N35 — 450, (143) — unproved claim — keep.** The map is an epimorphism of fppf sheaves at best: on G_m (via j_μ),
  χ is λ ↦ λ², which is not surjective on points.
- **N36 — 450, (142)–(143) — own idea (first pass) — keep.** The arrow M → PG in (142) is a plain map Θ̃ (change 29),
  not a two-headed one.
- **N37 — 451, (144) — unproved claim — correct.** This is consistent with (110): there ε₃ = δ_ρ(a)/δ_σ(b) and
  χ = δ_σ(b), so δ_ρ(a) = ε₃χ, which is the second line of (144). The first line is χ = δ′_σ(b) in the primed notation.
- **N38 — 451, end and (147) — unproved claim — correct.** The word is "dévissages" (change 31), not "clivages". (147)
  lists the four product decompositions; the cartesian and cocartesian claims for (94)–(96), (116), (117) remain
  unverified here.
- **N39 — 451, margin — unproved claim — keep.** "dont le sens est évident sur le diagramme (134)" points to the recap
  diagram.
- **N40 — 451, (145)–(146) — own idea (first pass) — keep.** In R°_ρσ = 'M_ρσ ∩ R_ρσ, the circle of the first M is
  displaced or missing, as the first pass noted.

### Scans 452–453

- **N41 — 452, (148)–(150) — unpursued implication — keep.** (148) is declared the definition of M (see N1). The
  topology in which the exact sequences are meant is not stated.
- **N42 — 453, upper diagonal note — unproved claim — keep.** "Il faudrait expliciter que les égalités (152)′
  caractérisent M_ρσ comme sous-groupe de G × T_ρ × N′_σ — il faudrait faire la vérification" is the author's own
  request. The last clause stays doubtful.
- **N43 — 453, (152′) — unpursued implication — correct.** The second line now reads \unsure{ε′|ε} = ε_σ(b) (change 32).
  With the notation of (104) and (109) (ε′ the sign in δ_σ(b) = ε′δ_ρ(a)), the first-pass reading fits. If the ink's
  ε′ is right, the signs have been renamed.
- **N44 — 453, foot — own idea (first pass) — keep.**
- **N45 — 453, NB — unproved claim — keep.** "multiplicatif" stays doubt-marked.
- **N46 — 453, last note — unpursued implication — keep.** "On pourrait introduire ξ, η, g, h … mais peu nous chaut ici."

## New notes — Claude (second pass)

- **C1 — 436, (105) — unproved claim (checked).** The square "R → 𝒯 over G_m —δ²→ G_m, diagramme cartésien" is
  cartesian as fppf sheaves.
  - Injective: r ↦ (r̄, κ(r)) has kernel Ker(R → 𝒯) ∩ Ker κ = μ₂ ∩ Ker κ = 1, since κ|μ₂ is the inclusion ((106)).
  - Surjective: given (t, λ) with χ(t) = λ², lift t locally to r. Then κ(r)² = λ², so κ(r)λ⁻¹ = ε ∈ μ₂, and rε⁻¹ is
    the required point.
- **C2 — 437, (106) and 442 — own idea.** The author's correction "celle-ci n'est pas cartésienne" (N3) and the later
  "unique hom (118)" (N11) rest on one fact: the cartesian square is the lower square (105), not the upper face (*).
  The second pass's renumbering (105′ → 105) makes the references on 437 and 442 point to that square.
- **C3 — 445, centre of SN′_σ — unproved claim (checked; assumption stated).** Assume ε_σ(n) is defined by
  nσn⁻¹ = ε_σ(n)σ, as T_σ = Ker ε_σ and N′_σ/T_σ ≃ μ₂ suggest. Then n acts on T_σ by d + cσ ↦ d + ε_σ(n)cσ: a μ₂-action,
  i.e. a ℤ/2-grading. Its fixed-point subscheme is c = 0 over every base, because c(t − 1) = 0 in R[t]/(t² − 1) forces
  c = 0. So T_σ^{μ₂} = G_m (the inserted (130)) and Cent(SN′_σ) = ST_σ ∩ G_m = μ₂ hold without "si 2 inv.", provided
  ε_σ: SN′_σ → μ₂ is an epimorphism, as the faithfulness statement asserts. The struck route through the element −1
  gives only ₂(ST_σ), which is larger in characteristic 2. For example, with σ² = −1 (the modular σ), over 𝔽₂ the
  identities g² = d² + c² = det g make every point of ST_σ 2-torsion.
- **C4 — 440–441, (116)/(117) — own idea.** The same arrow R° ↪ M° carries PG in (116) and SG in (117) (change 13). Since
  R° = Ker Θ̃° and Θ̃° is onto (SG → PG is), M°/R° ≃ PG, so "SG" in (117) is probably a slip. The arrow just beside it,
  SR° ↪ M⁺°, rightly carries SG (M⁺°/SR° ≃ SG).
- **C5 — 441–446, numbering — editorial note.**
  - The number (118) is used twice: on 441 for the μ₂-covers M̃, and on 442 for i_R. The "(118)" later on 442 means
    i_R.
  - On 445 the numbers run (128), (129), (130), (131|129); on 446 they restart at (128). So (128)–(131) each occur
    twice, and a reference to one of them is ambiguous unless its page is given.
- **C6 — 448–449, (134)–(138) — unpursued implication.** The recap reconstructs M from the data (135) as a quotient of
  SG × S′T_ρ × SN′_σ × G_m by μ₂ embedded diagonally (four μ₂'s identified). This is equivalent to (102) because
  R ≃ S′T_ρ × SN′_σ × G_m by (123)/(147). The compatibility "produit … triv." of N32 is the descent condition for that
  quotient.
