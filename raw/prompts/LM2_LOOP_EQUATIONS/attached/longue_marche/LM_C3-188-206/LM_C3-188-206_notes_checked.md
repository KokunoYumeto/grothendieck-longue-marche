# LM_C3-188-206 — research notes, checked against the corrected transcription (scans 188–206)

Source: the first pass's research notes (answers/unzipped/LM_C3-188-206/LM_C3-188-206_notes.md, §5, notes 1–46), each
checked against LM_C3-188-206_checked.tex. Verdicts: keep, correct (text revised), drop. Notes marked **Claude (second
pass)** are new. Kinds: conjecture (Grothendieck's conjectures, questions, expectations, programme), unproved claim,
unpursued implication, own idea. "Unproved" means not proved in the cited passage.

Matrix conventions used in the checks below (C1): ρ acts on Gl(2,Ẑ) as conjugation by R = (0 1; −1 1), σ∞ by
J = (0 1; −1 0), τ∞ = diag(1, −1); then ℓ₀ = (1 −2; 0 1), ℓ₁ = (1 0; 2 1), ε₀ = JR = −(1 −1; 0 1), ε₀² = ℓ₀,
σ∞(ℓ₀) = ρ(ℓ₀) = ℓ₁. These are not stated on these pages; they are the ones for which (62), (66), (68), (76) and (iv)
hold, and all of those identities were verified with them.

## Notes of the first pass

### Scans 188–191

- **N1 — scan 188, (31)–(32) — unproved claim — correct.** The "correspondance biunivoque" between pairs (g, h)
  satisfying (25) and pairs (α₀, β₀) needs two facts not proved here: every ρ- and σ∞-cocycle in the indicated groups
  is a coboundary (existence), and x ↦ xρ(x)⁻¹, x ↦ xσ∞(x)⁻¹ are injective, i.e. ρ and σ∞ have no non-trivial fixed
  points in Π̃^₀,₃ resp. Π̂₀,₃ (uniqueness). The Circle table places "Digression sur les 1-cocycles des groupes
  cycliques" at §43, p. 350, the likely source. Revised: the fixed-point condition was missing.
- **N2 — scan 188, after (34) — unproved claim — keep.** "ν ∈ Ẑ est uniquement déterminé en termes de α₀, β₀"
  requires that ℓ₁ generates a copy of Ẑ (so ℓ₁^ν determines ν) and that the admissible f do not change ν; the same
  claim is made for (29) in the margin of scan 187.
- **N3 — scan 189, left margin — unproved claim — correct.** "c'est un inconvénient mineur, qui va être levé plus
  bas" (now read "du couple" securely; "va être levé" still doubtful). It is taken up on scans 202–204: the
  representatives are normalised by α ≡ β ≡ 1 (2) (corollary, (89)), the residual freedom is a Ẑ-torsor T_Θ, and f is
  read in the twisted product Ť_Θ ∧ Sl(2,Ẑ). Revised: the "plus bas" is located.
- **N4 — scan 190, §4, (41), (44) — unproved claim — correct.** Necessity of (44) is immediate:
  ξρ(ξ)ρ²(ξ) = αρ³(α)⁻¹ = 1 and ησ∞(η) = βσ∞²(β)⁻¹ = 1. The converse ("équivaut") is the existence and uniqueness of
  N1. Revised: necessity checked.
- **N5 — scan 190, (45) — own idea (first pass) — correct.** The consistency check it proposed settles the sign: from
  (36) and (41), α ↦ ℓ₀ⁿα gives ξ ↦ ℓ₀ⁿ ξ ρ(ℓ₀)⁻ⁿ = ℓ₀ⁿ ξ ℓ₁⁻ⁿ and β ↦ ℓ₀ⁿβ gives η ↦ ℓ₀ⁿ η ℓ₁⁻ⁿ; with −n the relations
  (44) are preserved (ℓ₁ = ρ(ℓ₀), so the factors telescope), with +n they are not. The ink shows a single stroke that
  reads n: a probable slip; the transcription keeps `\unsure{\ell_1^n|\ell_1^{-n}}`. Confidence high (computation).
- **N6 — scan 191 — unpursued implication — keep.** For μ = 1 (ν = 0) the loop relation is ξ = η, so one element
  must satisfy both cyclic relations of (44); this simultaneous solution set is not described.
- **N7 — scan 191, margin "mais si" — unpursued implication — keep.** The margin answers the text's "on n'a pas
  d'expression explicite" with (42ter): u is recovered from (ξ, η, f) without solving (47); recovering α, β themselves
  remains the separate problem (47).
- **N8 — scan 191, last paragraph — unproved claim — keep.** The images of ξ, η in Gl(2,Ẑ)^{±′} (even in Sl(2,Ẑ))
  are said not to determine α, β, "cf plus bas"; scans 202–203 make this precise: only (μ, c, d, t, u) survive, a, b,
  r, s move in a Ẑ-torsor.

### Scans 192–193

- **N9 — scan 192, (49) — own idea (first pass) — keep.** α, β depend only on the image of u in Ñ!₀,₃; whether
  (α, β), or (μ, c, d, t, u), is a complete invariant of the outer automorphism is not asked. Confidence medium.
- **N10 — scan 192, (50)–(51) — unpursued implication — keep.** The composition rules follow on scan 193; their
  compatibility with the indeterminacy f ↦ ℓ₀ⁿf is what the end of scan 193 leaves open.
- **N11 — scan 193, left margin — unproved claim — keep.** u′(α₀) and (f′u′)(α) "n'ont de sens a priori que si
  α₀, α ∈ Π̂₀,₃ i.e. μ ≡ 1 (3)"; otherwise α₀″ = u′(α₀)α₀′ "sera fausse !". The correction factor for μ ≢ 1 (3) is not
  given. (The "(52)" the first pass read in this note is the number of the display.)
- **N12 — scan 193, middle paragraph — unproved claim — correct.** The cocycle property is claimed for f, g⁻¹, h⁻¹,
  α₀⁻¹, β₀⁻¹, and for α⁻¹, β⁻¹ on the subgroup f = 1, which consists of automorphisms u ∈ M̃!₀,₃ normalising L₀ (the
  first pass read Ñ!₀,₃; f is defined on M̃ only). The composition order and coefficient action are those of (52).
- **N13 — scan 193, end — conjecture (programme) — keep.** "il faudrait introduire un groupe extension de M̃!₀,₃
  par Ẑ, sur le modèle des groupes de Teichmüller spéciaux", on which f, α, β are unambiguous; "Ça ne s'impose pas
  ici de détailler…". The construction is deferred; scans 204–205 return to it as the "groupe adélique".
- **N14 — scan 193 — own idea (first pass) — keep.** Build that extension as pairs (u, chosen f) with the product
  read from (52); whether it is central, and its kernel, are to be proved. Confidence medium.

### Scans 194–197

- **N15 — scan 194, (54)–(55) — unproved claim — correct.** det α₀ = det α = ε₃ is stated here and derived on
  scan 198: (72) gives c² + cd + d² = δ/μ, and x² + xy + y² takes only the values 0, 1 mod 3, so δ ≡ μ (3), (74)–(75).
  Revised: not unproved in the package.
- **N16 — scan 194, margin and (58) — unpursued implication — keep.** Two choices coexist: the indeterminacy
  (α, β, f) ↦ (ℓ₀ⁿα, ℓ₀ⁿβ, ℓ₀ⁿf) and the three signs of the lifts to Gl(2,Ẑ). The short note now reads "cf p.398|348
  ou mieux formulaire plus bas".
- **N17 — scan 194, (57) — own idea (first pass) — drop.** Exactness of 1 → Sl(2,Ẑ)′ → Gl(2,Ẑ)′ → Ẑ^× → 1 is
  immediate from det(−1) = 1 and the surjectivity of det; the page asks nothing about a splitting.
- **N18 — scan 195, after (59) — unproved claim — correct.** "ξ et η, g, h sont indépendants du choix des signes":
  true and immediate, since ρ and σ∞ act by conjugation, so ρ(−α) = −ρ(α) and the signs cancel in αρ(α)⁻¹,
  βσ∞(β)⁻¹, and likewise in g, h. Revised: checked.
- **N19 — scan 195, (60)–(61) — unproved claim — correct.** That ε ne dépend d'aucun choix follows from N18; its
  value ε = ε₂ is derived on scan 198, (74)–(75), from t² + u² = ε/μ and x² + y² ≡ 1 (4) for odd values (with the
  correction of C3).
- **N20 — scan 195, (59) — own idea (first pass) — correct.** The ink is clear: h = β₀ρ(β₀)⁻¹ = f⁻¹ηρ(f). By (32) and
  (40) it should read β₀σ∞(β₀)⁻¹ = f⁻¹ησ∞(f): a slip, the same ρ that the struck draft above has in η and that the
  author corrected only in the η-line of (59). Confidence high.
- **N21 — scan 196, Remarque — unpursued implication — correct.** The cited notations are those of §44 (p. 356 ff,
  formulaire after p. 364); the letters f, g, h of §44 "ont le même sens qu'ici", α, β etc. do not, and are underlined
  when taken in the old sense: (i) α̲ = α₀, β̲ = β₀; (ii) β = f when β̲ = 1; (iii) φ̲ = η; (iv) ξ̲ = ℓ₀^ν ξ ℓ₁^{−ν};
  (v) α̲₀ = ℓ₀^ν α. Revised: section number and the sentence.
- **N22 — scan 196, (iv) — own idea (first pass) — keep.** ξ̲ = ℓ₀^ν ξ ρ(ℓ₀^ν)⁻¹ is the twist of ξ by the coboundary
  of ℓ₀^ν, so it again satisfies the cyclic relation of (44); this is a direct check. Confidence high.
- **N23 — scan 197, (65)–(68) — unproved claim — correct.** The formulas are cited from p. 342 (§VII "cocycles sous
  ρ" in the Circle table). Verified in this pass with the conventions C1: αRα⁻¹R⁻¹ has the entries (66) and βJβ⁻¹J⁻¹
  the entries (68). Revised: checked.
- **N24 — scan 197, (66)–(69) — own idea (first pass) — drop.** Done (N23): the eight entries agree, and the product in
  (69) is (R + 2νS, S; T + 2νU, U), as written.

### Scans 198–201

- **N25 — scan 198, (72)–(75) — unproved claim — correct.** (69) ⇔ (72) holds: with (70), (71) and S = T, the
  entries A and C follow from D = εU, μD = 1, B = εS. But (73) as written lacks the factor δ in both lines (see C3);
  (74) follows from the corrected relations c² + cd + d² = δ/μ, t² + u² = ε/μ, as (88) on scan 202 states.
- **N26 — scan 198, (73)–(75) — own idea (first pass) — drop.** Done: replaced by C3, which records the mismatch.
- **N27 — scan 199, margin — unproved claim — keep.** u_{α,β} = (μ μB; 0 1) depends only on B and D = 1/μ, so only
  on ξ, indeed on its image in Sl(2,Ẑ)′ with the sign fixed by ξρ(ξ)ρ²(ξ) = +1; "Il faudrait le noter u_ξ, cf.
  p. 410". The sign claim is not argued.
- **N28 — scan 199, (78) — unpursued implication — keep.** The triangular form makes u_{α,β} an element of the
  Borel subgroup; image, fibres and composition law in the coordinates (μ, B) are not described here.
- **N29 — scan 200, right margin — unproved claim — correct.** int(u_{α,β,f}) "a même effet, sur Sl(2,Ẑ)′, que
  l'autom u de Ŝ⁺₀,₃ défini (quand il y en a un), par passage au quotient" (group now read Ŝ⁺₀,₃, still doubtful).
  The statement is made in Sl(2,Ẑ)′, i.e. modulo ±1; see C2 for why that matters.
- **N30 — scan 200, (80)–(83) — unpursued implication — correct.** (82) and (83) carry a sign ε; C2 shows that the
  matrix (78) gives u_{α,β}(ε₀) = ε₀^μ without it, the sign coming from (81), which holds only modulo ±1.
- **N31 — scan 201, Remarque — unpursued implication — correct.** The claim "Toutes ces formules sont valables dans
  Gl(2,Ẑ), sans ambiguïté de signes" fails for (81) (first line) and (83) when ε = −1 (C2); it holds for (78)–(80)
  read modulo ±1 and for the sign rules stated (sign of f changes u_{α,β,f}; signs of α, β do not change u_{α,β}).
- **N32 — scan 201 — own idea (first pass) — keep.** Record the sign changes of (α, β, f) as an action of {±1}³ and
  check which expressions descend; C2 is the first instance. Confidence high.

### Scans 202–206

- **N33 — scan 202, (84)–(87) — unpursued implication — keep.** Verified: ℓ₀ⁿ = (1 −2n; 0 1) changes only the upper
  rows, so c, d, t, u, δ, μ, ε₂, α₂ and f⁻¹α, f⁻¹β are unchanged and (79) gives (87). The ambient quotient is defined
  only on scan 204.
- **N34 — scan 202, Proposition — unproved claim — correct.** Proved in this pass (sketch): under (88), D = εU and
  μD = 1 hold automatically; the (a, b) with ad − bc = δ form the orbit (a, b) + k(c, d), likewise (r, s) + m(t, u),
  and B = εS becomes k = m + (εS − B)/D, so the solutions are a torsor "sous Ẑ" (read so, not "sur"), acted on by
  the unipotent lift of ε₀ⁿ. The cited proposition is on p. 384.
- **N35 — scan 202, margin — unproved claim — correct.** "Pour μ fixé, on peut tjrs trouver c, d, t, u satisfaisant
  (88) — heureusement !" is true: at p ≠ 3 (resp. p ≠ 2) the forms x² + xy + y² (resp. x² + y²) are norms from étale
  algebras and take every unit value; at 3 (resp. 2) their unit values are exactly the units ≡ 1 mod 3 (resp. 4), which
  is what ε₃/μ ≡ 1 (3) and ε₂/μ ≡ 1 (4) give. Choose solutions prime by prime. Confidence high.
- **N36 — scan 202 — own idea (first pass) — drop.** Superseded by the direct proofs in N34–N35.
- **N37 — scan 203, corollary — unproved claim — correct.** Checked: α ≡ β ≡ 1 (2) forces (89); conversely, mod 2 one
  has B ≡ b, S ≡ s, D ≡ 1, so the shift k − m = (εS − B)/D is ≡ b − s and both b and s can be made even at once. Only
  even shifts preserve the congruences, hence the torsor under ℓ₀ⁿ = (ε₀²)ⁿ.
- **N38 — scan 203, Scholie — unpursued implication — keep.** The "invariants adéliques" Θ = (μ, c, d, t, u), up to
  signs, are "ce qu'on peut faire de mieux dans le contexte actuel": a, b, r, s are not invariant. What Θ retains of
  the outer automorphism is not examined.
- **N39 — scan 203, (90)–(91) — own idea (first pass) — keep.** Compare the fibres of u ↦ Θ with the diagonal action
  on (α, β, f). Confidence medium.
- **N40 — scan 204 — unpursued implication — keep.** The datum f is "un peu trop faible pour reconstituer" u̳ = φ(u̲)
  = u_{α,β,f}; the precise loss is the twisting by the torsor described next.
- **N41 — scan 204, display and margin — unproved claim — keep.** The quotient of T_Θ × Sl(2,Ẑ) by the diagonal
  Ẑ is the twist of Sl(2,Ẑ) by Ť_Θ, "un Sl(2,Ẑ)-torseur à droite"; left and right actions are not written out.
- **N42 — scans 204–205 — conjecture (programme) — keep.** "il faudra introduire explicitement et étudier avec un
  minimum de soin le groupe adélique formé par les systèmes (α, β, f) satisfaisant la relation des lacets, et
  l'homomorphisme canonique de M̃!₀,₃ dans ledit groupe"; deferred ("avant cela terminer les gammes notationnelles").
- **N43 — scans 204–205 — own idea (first pass) — keep.** Formulate the diagonal quotient as a moduli problem with
  the sign ±1 kept, and ask whether u̳ is defined as a matrix or as a class; u̳ changes sign with f ↦ −f (scan 204).
  Confidence medium.
- **N44 — scan 206, after (94) — unproved claim — correct.** By (49), β₀′ = γβ₀, and h′ = 1 iff γβ₀ is fixed by σ∞;
  so "un et un seul int(γ)" holds iff σ∞ has no non-trivial fixed point in Π̂₀,₃ (its centraliser there is trivial).
  For the profinite completion of Z/2 ∗ Z/3 this is the expected behaviour of centralisers of torsion in free profinite
  products; to be checked in the literature.
- **N45 — scan 206, (93)–(96) — unpursued implication — keep.** In the case [u, σ∞] = 1 the data reduce to pairs
  (ξ, f) with (95), (96) and ν free with 2ν + 1 ∈ Ẑ*; the margin adds ξ = fgρ(f)⁻¹ (from (39) with h = 1).
- **N46 — scan 206, (95)–(96) — own idea (first pass) — keep.** Study the solutions for fixed ν, starting with ν = 0;
  with N44 the remaining freedom in f is controlled by the fixed points of ρ and σ∞. Confidence medium.

## Notes of the second pass — Claude (second pass)

- **C1 — scans 194–200 — own idea — Claude (second pass).** The matrix conventions stated at the top (ρ ~ R, σ∞ ~ J,
  τ∞ = diag(1, −1), ℓ₀, ℓ₁, ε₀) make (62), (66), (68), (iv), (76) and σ∞(ℓ₀) = ℓ₁ (scan 187) true; τ∞^{α₂} = diag(1, ε)
  agrees with package 169–187 (R171.1). They are presumably fixed in §44; recording them makes every later sign
  checkable. Confidence high.
- **C2 — scans 200–201, (81)–(83) — own idea (sign error) — Claude (second pass).** Since τ∞ J τ∞⁻¹ = −J and tJ + u
  commutes with J, the matrix (78) gives u_{α,β} J u_{α,β}⁻¹ = ε·βJβ⁻¹, while u_{α,β}Ru_{α,β}⁻¹ = αRα⁻¹ exactly; hence
  u_{α,β}(ε₀) = ε₀^μ and u_{α,β,f}(ε₀) = int(f⁻¹)(ε₀^μ), the loop relation (26) of scan 186 without sign. Example:
  μ = −1, α = diag(−1, 1), β = 1 satisfy (64) and (60); u_{α,β} = diag(−1, 1) sends J to −J and ε₀ to ε₀^μ, not
  ε·ε₀^μ. So (81) (first line), (82) and (83) hold only modulo ±1; the check on scan 201 is right for
  int(β)(σ∞)·int(α)(ρ). Confidence high for the computation.
- **C3 — scan 198, (73) — unproved claim (slip) — Claude (second pass).** From (66), (68) and (72), c² + cd + d² =
  δε(t² + u²) = δ/μ and ac + bd + bc = δε(rt + su); the ink (checked: no δ in either line) omits δ. The example of C2
  (δ = ε = −1, c² + cd + d² = 1, ε(t² + u²) = −1) violates the first line as written. (74) and (88) are right.
  Confidence high.
- **C4 — scan 189, (40) — unproved claim (slip) — Claude (second pass).** The middle member f⁻¹(βσ∞(β)⁻¹) lacks the
  factor σ∞(f) that the last member has (h = f⁻¹βσ∞(β)⁻¹σ∞(f)); compare (39), where ρ(f) is written. Confidence
  high.
- **C5 — scan 196, (v) — unproved claim — Claude (second pass).** "comparée à ξ = αρ(α)⁻¹ et à (iv), donne
  α̲₀ = ℓ₀^ν α": from ξ̲ = α̲₀ρ(α̲₀)⁻¹ = (ℓ₀^να)ρ(ℓ₀^να)⁻¹ this follows only if x ↦ xρ(x)⁻¹ is injective, the
  fixed-point condition of N1. Confidence high.
- **C6 — scan 198, (71) — unproved claim (slip?) — Claude (second pass).** The second relation reads "T ▪ S = 1 i.e.
  T = S" with a heavy dash for the operator; (68) gives S = T, so the analogue of C + D − B = 1 is T − S = 0. If the
  dash is a minus, "= 1" is a slip; "i.e. T = S" is right. Ink not settled; confidence low.
- **C7 — scans 188–190 — unpursued implication — Claude (second pass).** The corrected readings put the
  parametrisations (33), (36), (45) on u ∈ M̃!₀,₃ (automorphisms), while (49) shows that α, β, ξ, η depend only on the
  image in Ñ!₀,₃: the four systems (92) mix an outer invariant (α, β or ξ, η) with the inner datum f. Making this a
  fibration M̃!₀,₃ → Ñ!₀,₃ with fibre read through f would organise §46.II. Confidence medium.
