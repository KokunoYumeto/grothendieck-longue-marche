# LM_C3-587-605 — research notes, checked against the corrected transcription (scans 587–605)

Source: the first pass's research notes (answers/unzipped/LM_C3-587-605/LM_C3-587-605_notes.md, "Research notes —
English", 67 notes, cited here as FP scan-n), each checked against LM_C3-587-605_checked.tex. Verdicts: keep, correct
(text revised), drop. Notes marked **Claude (second pass)** are new. Kinds: conjecture (Grothendieck's conjectures,
questions, expectations), unproved claim, unpursued implication, own idea. "Unproved" means not proved in the cited
passage.

Setting (§49.V, "Les groupes Mρ,σ généraux (contexte profini)"): Z!_{ρ,σ} = M![0]; S₀Γ!_{ρ,σ} is an extension of Z! by
L_ρ × L_σ ≃ ℤ/6 × ℤ/4 with elements (u, a, b); A is the set-theoretic section u ↦ (u, a = ε₃(τ′)α⁻¹u, b = β⁻¹u) with α
normalised in Π̂_{0τ} = {1, τ}·Π̂₀ (51). Conventions used in the checks, taken from the pages: x(y) = xyx⁻¹ and
[x, y] = xyx⁻¹y⁻¹ (592 expands [u̇′, σ̇] as u̇′(σ̇)σ̇⁻¹); τ′ is an involution (ε₃″(τ′) = ε₃′(τ′)ε₃(τ′), 589);
σ² = ρ³ = −1, central modulo Π̂₀ (presentation on 605). In F₂-coordinates e₃, e₂ ∈ {0, 1}, e = 1 means sign −1.

## Scan 587

- **FP 587-1 — conjecture (question) — correct.** "je me demande si cette section ensembliste … est multiplicative".
  The pages answer it: A is multiplicative over Z^{!′} (ε₃ = 1) and Z^{!‴} (ε₂ = ε₃) but "n'est pas multiplicative au
  dessus de M![0] tout entier" (590); the defect is the sign ε of (60) and (63).
- **FP 587-2 — unproved claim, cancelled — keep.** The struck "Corollaire La section envisagée est multiplicative" is
  exactly what 588–590 refute; the cancellation is justified by them.
- **FP 587-3 — own idea — drop.** Computing the multiplicative defect is what Grothendieck does: (53) on 588, a″ = εa′a
  with ε from (63), and α″ in (65).
- **Claude (second pass) — 587, Proposition (52) — unproved claim.** Sufficiency reduces (52) to σ̇ⁱ = ρ̇ʲ = 1 and then
  concludes i = j = 0; this needs i and j to be read modulo the orders of σ̇ and ρ̇ in the quotient by Π₀ (4 and 6 by
  the presentation on 605). Their ranges are fixed in (50), before this package, and are not restated here.

## Scan 588

- **FP 588-1 — conjecture (expectation), cancelled — keep.** The proposal to replace fibre products over
  G_{ρ,σ}/G⁺_{ρ,σ} by fibre products over the finer G_{ρ,σ}/Π₀ is struck with its paragraph and is not taken up here.
- **FP 588-2 — unproved claim, cancelled — correct.** "un rev. de degré 12": the group of 605,
  Sl(2,ℤ)/Π₀ = ⟨ρ, σ | ρ⁶ = σ⁴ = 1, ρ³ = σ², σρσ⁻¹ = ρ⁻¹⟩, is dicyclic of order 12, which fits a degree-12 covering;
  the abbreviation before "universel" is still unread (rev.|gr.).
- **FP 588-3 — unpursued implication — correct.** The criterion is not symmetric in the pair: A(u′u) = A(u′)A(u) iff
  ε₃(u) = 1 or ε₂(u′)ε₃(u′) = 1 (59 bis). If ε₃(u) = 1, ε₂(u) = −1 and ε₃(u′) = −1, the product u′u is multiplicative
  while uu′ is not. Revised from "check the reversed order".
- **FP 588-4 — own idea — correct (checked).** The cancelled table 54bis agrees with (55) on 589 (ε₃ = 1: always; ε₃ =
  −1: σ(a′) ≡ ε₃′a′) and with (56) (σ(u′) ≡ ±u′). It was struck together with the first (54), which 589 restates.
- **Claude (second pass) — 588, (53) and the NB — unpursued implication.** Cancelling ε₃′(σ) gives ε₃(σ)⁻¹(a′), not
  ε₃(σ)(a′); the NB "ε₃(σ) et ε₃(σ⁻¹) opèrent de la m̄ façon" licenses the change because σ² = −1 is central modulo
  Π̂₀. The blotted exponent at σ in (53) fits this; the checked text reads σ|σ⁻¹.

## Scan 589

- **FP 589-1 — unproved claim — keep.** (35), u̇′(σ̇) = ε₂(u′)σ̇ modulo Π̂₀, is quoted, not proved; (35 bis) is used
  the same way on 598 and 605.
- **FP 589-2 — unpursued implication — correct.** Answered at once: the Proposition (589–590, box d)) makes a″ = a′a
  equivalent to "ε₃ = 1 ou ε₂′ = ε₃′"; only ε₃ = −1 needs (58).
- **FP 589-3 — own idea — correct.** Carried out by Grothendieck: Z^{!‴} = {ε₂(u) = ε₃(u)} in (59), and the kernel of
  (ε₂, ε₃) in (81).

## Scan 590

- **FP 590-1 — unpursued implication — keep.** The gloss "i.e. a(ρ) = ρ" turns ε₃ = 1 into a stabiliser condition;
  whether it depends on the chosen ρ, σ is not discussed.
- **FP 590-2 — unproved claim — correct.** "elle n'est pas multiplicative au dessus de M![0] tout entier" needs u with
  ε₃(u) = −1 and u′ with ε₂(u′)ε₃(u′) = −1. 604 notes that all elements coming from Gl(2,ℤ) have ε₂ε₃ = 1 and turns to
  u = diag(μ, 1), μ ≡ 5 (12), in Gl(2,ℤ̂); the existence of such u in M![0] is the missing input.
- **FP 590-3 — own idea — correct.** Done on 599–600: S₀Γ⁰ = S₀Γ^{!′} ∩ S₀Γ^{!‴} (81), and S₀^{Π₀}Γ^{!0}, of
  index 8 in S₀^ΠΓ!, is shown normal.

## Scan 591

- **FP 591-1 — conjecture (question) — correct.** "Je n'ai pas trouvé de jolie expression analogue" concerns the group
  "caractérisé par la relation ε₂(u)ε₃(u)=1", i.e. S₀Γ^{!‴} of (59); the ink writes S₀Γ^{!″} (two primes), a slip (in
  (81) Γ^{!″} names a third subgroup). The search for an expression is left open.
- **FP 591-2 — unproved claim — keep.** (61) "rend évident que c'est un ss-groupe": compatibility of the congruences with
  the product of triples is not shown on the page.
- **FP 591-3 — unproved claim — correct.** The proof of (62) a), b) follows on 592 (Dém.). What stays unproved there is
  (57), L_ρ ∩ Π̂ = L_σ ∩ Π̂ = μ and L_ρ ∩ Π̂₀ = L_σ ∩ Π̂₀ = {1}, with N*_ρ ∩ 𝒢̃ = L_ρ and N*_σ ∩ 𝒢̃ = L_σ.
- **FP 591-4 — own idea — drop.** Comparing the moduli Π̂₀ and Π̂ is the content of 592, where (56) is read "dans M/Π̂
  (au lieu de M/Π̂₀)".

## Scan 592

- **FP 592-1 — unpursued implication — correct.** Answered on 593 and 600: modulo Π̂ the defect disappears (S₀^ΠΓ! is a
  group), and what survives is the extension of Z! by μ, reduced on 600 to the finite 𝓔.
- **FP 592-2 — unproved claim — keep.** (57) is asserted without derivation; it determines the kernel μ.

## Scan 593

- **FP 593-1 — unproved claim — correct.** Corrected reading: "Les extensions par L₋ρ × L_σ … munies deux sections
  canoniques" (not "munie d'une section"): the extensions by L₋ρ and by L_σ each carry a canonical section, leaving the
  extension by μ. The sections are not constructed on this page, and the splitting of L_ρ × L_σ into μ × L₋ρ × L_σ
  compatibly with the action of Z! is not discussed.
- **FP 593-2 — unpursued implication — keep.** The residual extension is read as the sign ambiguity of α above
  α̃ ∈ Π̂/±1; the normalisation α ∈ Π̂_{0τ} picks a representative but, as 594 says, not a multiplicative one.
- **FP 593-3 — own idea — correct.** The cocycle is computed by Grothendieck on 594–595: A(u′)A(u) and A(u′u) differ by
  ε, with ε = −1 iff ε₃(u) = −1 and ε₂(u′)ε₃(u′) = −1 (63). See the Claude note under 602.

## Scan 594

- **FP 594-1 — unpursued implication — keep.** "pour canonique qu'il soit, n'est pas multiplicatif": a preferred
  set-theoretic section, not a splitting.
- **FP 594-2 — own idea — correct (settled).** The ink of "i.e. si ε₃(u)=−1 et ε₂(u′)ε₃(u′)=+1" is clear (crop); it is a
  slip, since the case contrary to (59 bis) needs −1, which (63) on 595 writes. The diplomatic text keeps +1.
- **FP 594-3 — unproved claim — correct.** (60) follows from the Proposition of 591: A(u″) and the product
  A(u′)A(u) lie in the subgroup S₀^ΠΓ! over the same u″, so they differ by an element (1, ε, 1) of the kernel μ.

## Scan 595

- **FP 595-1 — conjecture — keep.** "Je présume qu'on aura (64)" (no "et" in the ink) with the margin "pas vrai en
  général": a tentative formula, rejected on the same page.
- **FP 595-2 — unpursued implication — keep.** For ε₃ = −1, (64) holds iff a′ commutes with τ′ ("restriction
  draconienne"); the shorter formula is valid exactly on that centraliser.
- **FP 595-3 — own idea — correct (verified).** From (*) α″ = εu′ua⁻¹a′⁻¹st and u′(α)α′ = u′ua⁻¹sa′⁻¹t, with
  s = ε₃(τ′), t = ε₃′(τ′), s² = t² = 1, one gets (εu′(α)α′)⁻¹α″ = t[a′, s]t⁻¹ = [t(a′), s]; this is the page's final
  formula ε₃′(τ′)([a′, ε₃(τ′)]) = [ε₃′(τ′)(a′), ε₃(τ′)].
- **FP 595-4 — own idea — drop.** Merged into FP 594-2 (the sign is settled).

## Scan 596

- **FP 596-1 — conjecture (question) — correct.** Partly answered: 600 reduces the extension S₀^ΠΓ! of Z! by μ to the
  pull-back of the finite central extension 𝓔 of μ × μ by μ, and 603 shows 𝓔 is not split. See the Claude note below
  for what this leaves open.
- **FP 596-2 — unproved claim — correct.** The splittings (67)–(68) follow from the Corollary on 590 (A multiplicative
  over Z^{!′} and Z^{!‴}) and the Rmque on 591 (its values satisfy u ≡ b ≡ ε₃(σ)a mod Π̂₀).
- **FP 596-3 — unpursued implication — keep.** (65) rewrites the correction term through α′⁻¹u′.
- **FP 596-4 — own idea — drop.** The intersection and its normality are worked out on 599–600 ((81), (82),
  Proposition b)).
- **Claude (second pass) — 596, (65) — unpursued implication.** Substituting the product ε₃′(τ′)a′ = α′⁻¹u′ for the
  conjugate ε₃′(τ′)(a′) of 595 is legitimate: for commuting t, s ∈ {1, τ′}, [ta′t⁻¹, s] = [ta′, s].
- **Claude (second pass) — 596, the main question — unpursued implication; confidence medium.** 𝓔 non-split does not
  by itself make S₀^ΠΓ! non-split: its class is the inflation of that of 𝓔 along Z! → μ × μ, and inflation kills the
  transgressions of Z!-invariant homomorphisms Z^{!0} → μ (Hochschild–Serre). The pages do not examine this; the margin
  of 600 only excludes splittings that agree with A on Z^{!′} or on Z^{!‴}.

## Scan 597

- **FP 597-1 — conjecture (question) — keep.** Answered: neither complement is invariant (598–599); their intersection
  S₀^{Π₀}Γ^{!0} is (600).
- **FP 597-2 — unpursued implication — keep.** Descent to the order-two quotients would need the invariance that fails.
- **FP 597-3 — conjecture (question) — correct.** The classification is carried out for 𝓔 (603: not split, exactly two
  elements of order 4).
- **FP 597-4 — unproved claim — correct.** The argument is complete as written: S₀^ΠΓ^{!′} has index 2 in S₀^ΠΓ!
  (Z!/Z^{!′} ≃ ±1, stated on the page), so S₀^ΠΓ! is generated by it and any x outside it, and S₀^{Π₀}Γ^{!′} is already
  normal in S₀^ΠΓ^{!′}.

## Scan 598

- **FP 598-1 — unproved claim — keep.** "Cette condition n'est pas conséquence de la condition ε₃(u)=1" needs an element
  of Z! with ε₃ = 1, ε₂ = −1 (cf. FP 590-2 and 604).
- **FP 598-2 — conjecture (question) — keep.** The parallel question for S₀^{Π₀}Γ^{!‴}, answered on 599.
- **FP 598-3 — own idea — correct.** Superseded by the F₂ description in the Claude notes under 602–603.

## Scan 599

- **FP 599-1 — unproved claim — drop.** For ε₃ = 1, ε₃[σ] = 1 by the definition on 589, so (79) holds trivially;
  nothing is suppressed.
- **FP 599-2 — unproved claim — correct.** The element of S₀^{Π₀}Γ^{!‴} with ε₃(u) = −1 that the argument needs exists:
  x̲ = (τ, τ′, τ) of (70), with ε₂ = ε₃ = −1. What remains is the element of (75) with ε₃(u₀) = 1, ε₂(u₀) = −1.
- **FP 599-3 — own idea — correct.** The "variations" are slips: (81) writes Ker(S₀Γ⁰ → μ × μ) where the domain must be
  S₀Γ!, and Γ⁰ on the left where (82) has Γ^{!0}.
- **FP 599-4 — unproved claim — correct.** Exactness of (82) follows from 591 b) restricted to Z^{!0}; the ink's third
  term S₀Γ^{!0} is a slip for Z^{!0}, as the splitting S₀^ΠΓ^{!0} = S₀^{Π₀}Γ^{!0} × μ on 600 shows.

## Scan 600

- **FP 600-1 — unpursued implication — keep.** b) reduces the extension to the finite 𝓔 and its pull-back.
- **FP 600-2 — unproved claim — correct.** A two-line argument: a homomorphic section s equal to A on Z^{!′} makes
  s(Z^{!′}) = S₀^{Π₀}Γ^{!′} normal in s(Z!) (Z^{!′} = ker ε₃), hence in S₀^ΠΓ! = s(Z!)·μ with μ central, against a).
  Likewise for Z^{!‴}.
- **FP 600-3 — own idea — correct.** Realised as the commutator pairing on μ × μ (Claude note under 602).

## Scan 601

- **FP 601-1 — conjecture (question) — keep.** "sont ils tous d'ordre 2 (ou 1)?", answered on 602–603: no, exactly two
  elements of order 4.
- **FP 601-2 — unproved claim — keep.** "évidemment diviseurs de 4": quotient μ × μ and central kernel μ both have
  exponent 2.
- **FP 601-3 — unpursued implication — keep.** Recovery of S₀Γ from 𝓔 by pull-back along (ε₃, ε₂) and push-out along
  the "hom. diagonal" −1 ↦ (ρ³, σ²) (reading corrected from "diagonale").
- **FP 601-4 — own idea — correct.** Done by Grothendieck on 602–603; the result is that 𝓔 is dihedral of order 8
  (Claude note under 603).

## Scan 602

- **FP 602-1 — conjecture (question) — keep.** (88) "(?)" is resolved on the same page by (89).
- **FP 602-2 — unpursued implication — keep.** The square criterion is turned into the description (90)–(92).
- **FP 602-3 — own idea — correct (computed).** By (89)–(90) the square map 𝓔 → μ is q(e₃, e₂) = e₃ + e₃e₂; its polar
  form e₃f₂ + e₂f₃ is non-degenerate, so 𝓔 is non-abelian, and q has Arf invariant 0 (it takes the value 1 once).
- **Claude (second pass) — 602 and 595 — own idea; confidence high for the algebra.** The cocycle read off (63),
  c(x′, x) = e₃(x)(e₂(x′) + e₃(x′)), gives c(x, x) = q(x), the squares of 602, and c(x′, x) + c(x, x′) = e₃f₂ + e₂f₃,
  the commutators. So the sign computation of 594–595 and the order computation of 602–603 agree.

## Scan 603

- **FP 603-1 — unproved claim — correct.** Immediate: the two elements over (−1, 1) differ by the central −1 = x², so
  they are x and x³ = x⁻¹; 𝓔″ = {ε₂ = 1} has order 4 and contains both, so it is the cyclic subgroup of order 4.
- **FP 603-2 — unpursued implication — keep.** A split central extension would be (μ × μ) × μ, of exponent 2.
- **FP 603-3 — conjecture (question) — correct.** The sign "qu'il faut déterminer" is forced (Claude note below). The
  ink writes "sur 𝓔′" and "Aut(𝓔′)" where the sense is 𝓔″.
- **FP 603-4 — own idea — correct.** 𝓔 is the dihedral group of order 8.
- **Claude (second pass) — 603, the operation of 𝓔/𝓔″ on 𝓔″ — unpursued implication; confidence high.** A group of
  order 8 and exponent 4 (601) with exactly two elements of order 4 (Corollaire 1) is dihedral (ℤ/4 × ℤ/2 has four, the
  quaternion group six), and there every element outside the cyclic subgroup of order 4 inverts it. So the sign sought
  on 603–605 must be ε = −1 unless Corollaire 1 fails; the matrix calculation (94)–(100) is a check of it.

## Scan 604

- **FP 604-1 — conjecture (question) — keep.** (94) is the congruence that would fix ε.
- **FP 604-2 — conjecture (stated difficulty) — keep.** Elements from Gl(2,ℤ) all have ε₂ε₃ = 1, while the test element
  needs ε₂ = 1, ε₃ = −1.
- **FP 604-3 — unproved claim — keep.** Working in the quotient Gl(2,ℤ̂) needs the sign and the lifting of the chosen
  matrix to survive there; not checked on the page.
- **FP 604-4 — own idea — correct.** Still useful as a check, but by the Claude note under 603 the expected answer is
  ε = −1.
- **Claude (second pass) — 604–605 — own idea; confidence medium.** On the elements used, ε₃ and ε₂ behave like the
  signs of det modulo 3 and modulo 4: det = ±1 on Gl(2,ℤ) gives ε₂ε₃ = 1 as stated, and u = diag(μ, 1) with μ ≡ −1 (3),
  μ ≡ 1 (4) is chosen to have ε₃ = −1, ε₂ = 1. This is an inference from the choices, not a statement of the page.

## Scan 605

- **FP 605-1 — unproved claim (deferred) — keep.** "un peu bref… cf plus bas…" flags the parametrisation (96)–(98).
- **FP 605-2 — unproved claim — correct.** Partly checkable: with ℓ₁ = (1 0; 2 1) as settled, (−ℓ∞)(−ℓ₁)(−ℓ₀) = 1
  exactly, and the presented group is dicyclic of order 12. The identification Sl(2,ℤ̂)/Π̂₀ ≃ Sl(2,ℤ)/Π₀ still needs Π̂₀
  to be the closure of Π₀ with the same finite index.
- **FP 605-3 — unproved claim (deferred) — keep.** T₀ acts through ε₂(ζ|ξ), with reference to pp. 593′, 594, (34), (35),
  (35 bis), outside this package.
- **FP 605-4 — unpursued implication — keep.** The extract stops at σa; the congruence σa ≡ u (Π̂₀) is not yet solved.
- **FP 605-5 — own idea — correct (checked).** det(cρ + d) = c² + cd + d² and det τ′ = −1, so (98) μ = −(c² + cd + d²)
  is det u = det(σa), Π̂₀ lying in Sl(2,ℤ̂); (97) and (100) agree with the matrix products.
