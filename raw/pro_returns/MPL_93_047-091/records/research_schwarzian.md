# Research notes: Schwarzian and other one-dimensional differential invariants

**Coverage:** cote 93, frozen scans 072–078, 080–082 and 084; research notes SC01–SC118. Scan 079 is absent from the supplied sequence, and the unrelated homotopy page 083 is handled separately. These notes were written only after the root recorded its freeze at 10:49:51 UTC on 18 November 2026 and opened the context at 10:49:56; this research agent used the frozen text and did not inspect the scan images or edit transcription files.

**Main findings.** The formula in scan 073 is an integral quadratic-differential cocycle, as independently checked by a universal three-jet identity, and its relation to the earlier normalization is G=12G₀. The printed squared-coordinate test is wrong; the correct coefficient is 1/(4t²). The author’s failed surjectivity experiments on 075 and 077, the doubt on 074, the draft diagrams on 081, and the uncertain or revised coefficients on 080/082 are preserved as separate issues rather than absorbed into a polished theorem.

**Hua comparison.** Hua’s findings-register candidate combines two different textual locations: the integral formula is present in 072–074, while the p-versus-p² homography discussion is reported in later unsupplied pages. Our checks prove the monic local model with q=p for p>3 and q=p² for p=2,3, including a new written descent argument for arbitrary α under Pic(A)=0; the root independently reviewed that argument. This does not prove all global sheaf statements or the proposed classifications of differential operators, and it does not establish priority.

**Context discipline.** `context/notes/RESULTS_STATE.md` was read before using the earlier-package notes and Hua’s modernised reading, and all matches below name the relevant files and their local sections/scan locations. The Hua material is credited to his AI-produced project as a lead; P05/P06 are carried as background rather than re-derived, and S20 remains a planning hypothesis. “No matching settled entry” means no matching result in the supplied context, not that the statement is unknown in the literature.

**Supporting records.** Detailed independent arguments are in `research_schwarzian_proofs.md` (C1–C11), the executable exact checks in `schwarzian_checks.py`, and their actual output in `schwarzian_checks_output.json`. The event ledger records what was checked, used, left as background, or refuted; it does not turn a finite enumeration or a cited AI report into a general proof. Each main commentary below is one to four sentences, excluding its metadata.

## Statement-level notes

### SC01 — Existence of the analytic projective invariant

**File/location:** cote 93, scan 072. **Short quote:** “Il existe un morphisme”. **Kind:** unproved claim.

The displayed formula on 073 supplies this existence assertion: its coordinate compatibility follows from the chain identity in C1, and its analytic local properties from C3. The theorem is announced here without a proof; checking this example does not establish the subsequent uniqueness statement.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/same_cote_93/MPL_93_002-046_notes.md`, P01 (scan 036); `context/notes/RESULTS_STATE.md`: **MPL_93_002-046 P01**.

### SC02 — The proposed denominator restriction

**File/location:** cote 93, scan 072. **Short quote:** “On doit pouvoir montrer que”. **Kind:** self-flagged.

**Additional state:** unproved claim.

In a universal polynomial jet algebra over a field, a reduced denominator whose zero set is contained in the union of the two first-derivative divisors is a unit times a product of their powers. Applying that algebraic fact to the stated analytic condition requires a jet-realization argument and care about coefficients varying on U; no proof of that passage is supplied here, so the bracketed claim remains conditional.

**Confidence:** Medium: the algebraic lemma is straightforward, but the analytic-to-universal hypothesis is not proved here.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC03 — The additive cocycle equation

**File/location:** cote 93, scan 072. **Short quote:** “G(f,g)+G(g,h)=G(f,h)”. **Kind:** unproved claim.

For the formula on 073 the equality is literal cancellation of the middle Q-term, with no characteristic restriction for G₀. This is distinct from the coordinate-composition identity needed to make those differences quadratic differentials; C1 verifies both.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC04 — Invariance under the three generators

**File/location:** cote 93, scan 072. **Short quote:** “G(f,1/g)”. **Kind:** unproved claim.

Translation, nonzero scaling and inversion are constant homographies, and their integral Q vanishes by C1. The unit and nonvanishing conditions in the page are essential domains of definition, not cosmetic exceptions.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC05 — Rigidity from equality of the two-jet

**File/location:** cote 93, scan 072. **Short quote:** “coïncident à l'ordre $2$”. **Kind:** unproved claim.

In the complex analytic setting the local Schwarzian equation gives a unique solution with prescribed value, first derivative and second derivative, and analytic continuation gives the stated connected-domain equality. This is the C3 local ODE argument; it must not be transferred unchanged to positive characteristic.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/same_cote_93/MPL_93_002-046_notes.md`, P01/P04 (scan 036); `context/notes/RESULTS_STATE.md`: **MPL_93_002-046 P01**; no settled positive-characteristic rigidity entry.

### SC06 — Uniqueness up to a nowhere-zero function

**File/location:** cote 93, scan 072. **Short quote:** “G'=\varphi G”. **Kind:** unproved claim.

The asserted classification concerns all admissible nonlinear rational differential operators, not only two copies of the displayed formula. Our computations do not prove that classification; the distinction matters because arbitrary additive differential operations would preserve a cocycle but can destroy rigidity or local surjectivity.

**Confidence:** Medium: the claim is plausible in the full analytic hypotheses; classification was not re-proved.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC07 — Descent from affine to projective coordinates

**File/location:** cote 93, scan 072. **Short quote:** “c) implique que $G$ se descend”. **Kind:** unproved claim.

Two affine charts of the projective line differ by the allowed constant homographies, so C1 allows G to glue on projective étale coordinates and descend in both arguments. The uncertain handwritten group abbreviation is not resolved by this mathematical identification; PGL₂ is the group used in the check.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC08 — Opposite torsor-difference conventions

**File/location:** cote 93, scan 072–073. **Short quote:** “G(f,g)=c(f)-c(g)”. **Kind:** reading question.

The margin on 072 uses c(f)−c(g), while the principal equation on 073 uses c(g)−c(f). Either convention can define a torsor after changing the sign of its action, but using them together without that adjustment reverses later differences; both readings remain frozen.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC09 — The quotient map is claimed to be injective

**File/location:** cote 93, scan 072. **Short quote:** “est mono”. **Kind:** unproved claim.

Equality of projective connections first gives a constant Möbius transformation locally; after matching the two-jet, condition d) kills the remaining transformation. This supplies the analytic quotient-level injectivity for the displayed invariant, rather than injectivity of the map on raw coordinates.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/same_cote_93/MPL_93_002-046_notes.md`, P03 (scan 036); `context/notes/RESULTS_STATE.md`: no matching settled quotient theorem.

### SC10 — Local surjectivity of the Schwarzian equation

**File/location:** cote 93, scan 072. **Short quote:** “est un épi”. **Kind:** unproved claim.

C3 solves the prescribed analytic Schwarzian equation locally by a ratio of two independent solutions of a linear second-order ODE. The word “épi” is a sheaf-local assertion; it neither gives a global single-valued solution on every open set nor algebraic étale-local surjectivity in every characteristic.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/same_cote_93/MPL_93_002-046_notes.md`, P04 (scan 036); `context/notes/RESULTS_STATE.md`: no matching settled surjectivity theorem.

### SC11 — Functoriality reduces the scalar ambiguity

**File/location:** cote 93, scan 072. **Short quote:** “c\in\mathbb{C}^{*}”. **Kind:** unproved claim.

If the fixed-curve uniqueness assertion has first been established, a scalar natural for every étale coordinate chart restricts from one scalar on the affine line and is invariant under translations, hence is constant. This verifies the reduction from an already existing φ to a constant, not the missing classification of operators.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC12 — The margin says e) may be omitted

**File/location:** cote 93, scan 072. **Short quote:** “il suffit de supposer d)”. **Kind:** self-flagged.

**Additional state:** unproved claim.

For the displayed nonzero Schwarzian, e) follows from the analytic ODE, but the margin purports to deduce it for every operator in the classification. That stronger redundancy depends on the unproved uniqueness argument and has not been independently established here.

**Confidence:** Medium: true for the explicit invariant, classification-dependent for all operators.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC13 — Universal constant coefficients in the jet expression

**File/location:** cote 93, scan 073. **Short quote:** “des coefficients $\in\mathbb{C}$”. **Kind:** unproved claim.

Compatibility with all charts and translations accounts for independence of the base point, but uniqueness of a rational jet presentation is needed to conclude the exact universal coefficient statement. The sentence is read in the variable-X context of II; a single fixed curve with arbitrary holomorphic coefficients would not justify it.

**Confidence:** Medium: contextual naturality explains the intended statement but no full presentation theorem was checked.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC14 — Normalization relative to the classical Schwarzian

**File/location:** cote 93, scan 073. **Short quote:** “-2\frac{g'''}{g'}+3\left(\frac{g''}{g'}\right)^2”. **Kind:** unpursued implication.

This is −2 times the classical Schwarzian, agreeing with the earlier scan 036 and P01. C2 rechecks the normalization so that comparisons with ODEs, exponentials and the later factor 12 use the same sign.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Restates earlier P01 and Hua VI’s normalization, with an independent formula check. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/same_cote_93/MPL_93_002-046_notes.md`, P01/P04 (scan 036); `context/notes/RESULTS_STATE.md`: **MPL_93_002-046 P01**.

### SC15 — The canonical torsor and quotient isomorphism

**File/location:** cote 93, scan 073. **Short quote:** “ce dernier morphisme est un iso”. **Kind:** unproved claim.

Transition differences from C1 glue local affine spaces of quadratic differentials into a torsor, and the analytic local injectivity and surjectivity in SC09–SC10 identify the orbit sheaf with it. “Canonical” does not supply a canonical global point; a projective connection is a choice of section.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/same_cote_93/MPL_93_002-046_notes.md`, P01/P03 (scan 036); `context/notes/RESULTS_STATE.md`: **MPL_93_002-046 P01**, no matching settled global torsor construction.

### SC16 — Divided derivatives in the relative problem

**File/location:** cote 93, scan 073. **Short quote:** “il faut maintenant remplacer”. **Kind:** unproved claim.

Hasse derivatives are the coefficients of the Taylor expansion, so their definitions use no factorial inverses. C1 verifies the necessary third-order composition identities on an étale coordinate chart over an arbitrary commutative base; writing D⁽ⁿ⁾ as (1/n!)dⁿ is only a characteristic-zero mnemonic.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Confirms the formula-level part of Hua’s candidate and adds an independent calculation; broader classification claims remain separate. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC17 — Integral coefficients are asserted by naturality

**File/location:** cote 93, scan 073. **Short quote:** “les coefficients doivent être dans”. **Kind:** unproved claim.

The particular formula has integral coefficients in the localized universal Hasse-jet algebra, as C1 shows directly. The stronger claim that every natural operator admits exactly the stated integral presentation belongs to the proposed classification and is not proved merely by that example.

**Confidence:** High for the explicit formula; medium for the unproved general representation statement.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC18 — The integral cocycle exists over every base

**File/location:** cote 93, scan 073. **Short quote:** “On trouve encore l'existence”. **Kind:** unproved claim.

C1 proves an integral polynomial identity before any localization and proves the corresponding Q identity where the first jets are units. Thus the stated G₀ formula is a coordinate-independent quadratic-differential cocycle in characteristics 2 and 3 as well; this verifies the formula-level part of Hua’s candidate, not every universal property attached to it.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Confirms the formula-level part of Hua’s candidate and adds an independent calculation; broader classification claims remain separate. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC19 — The uniqueness up to sign is a separate claim

**File/location:** cote 93, scan 073. **Short quote:** “unicité au signe près”. **Kind:** unproved claim.

The observation that the units of ℤ are ±1 explains the asserted normalization only after uniqueness up to a universal unit has been proved. C1–C2 establish existence and normalization, not this classification of all natural operators.

**Confidence:** Medium: a logical dependency is identified; the general classification remains unverified.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC20 — The classical invariant vanishes in characteristics 2 and 3

**File/location:** cote 93, scan 073. **Short quote:** “identiquement nulle en car. $2$ et $3$”. **Kind:** unproved claim.

This follows from the integral identity G=12G₀, not from replacing integer denominators by illegal inverses. In characteristic 2 the ordinary second derivative vanishes, and in characteristic 3 the ordinary third derivative vanishes while the remaining coefficient is 3.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Confirms the formula-level part of Hua’s candidate and adds an independent calculation; broader classification claims remain separate. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC21 — Meaning of the notation G divided by 12

**File/location:** cote 93, scan 073. **Short quote:** “prendre $\frac1{12}G(f,g)$”. **Kind:** unproved claim.

C2 verifies G=12G₀ over the integers after substituting f''=2D⁽²⁾f and f'''=6D⁽³⁾f. Over a base where 12 is not invertible, the displayed Hasse formula defines G₀ independently; division by the already zero G cannot recover it.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Confirms the formula-level part of Hua’s candidate and adds an independent calculation; broader classification claims remain separate. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC22 — Nonvanishing in small characteristics

**File/location:** cote 93, scan 073. **Short quote:** “non identiquement”. **Kind:** unproved claim.

**Additional state:** marginal nonvanishing condition.

The margin’s nonzero condition is realized by G₀(t,t+t²)=dt² in characteristic 2 and G₀(t,t+t³)=−dt² in characteristic 3, where the first derivatives are 1. These examples are checked in C2 and C9 and also explain why ordinary derivatives lose information.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Confirms the formula-level part of Hua’s candidate and adds an independent calculation; broader classification claims remain separate. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC23 — The squared-coordinate normalization test is wrong as printed

**File/location:** cote 93, scan 073. **Short quote:** “\frac1{2t}dt^2”. **Kind:** own idea.

**Additional state:** reading question.

Direct Hasse differentiation gives G₀(t,t²)=dt²/(4t²), whereas the final frozen text gives dt²/(2t). Hua’s modernised reading makes the same mathematical correction, but it is a research correction to the value, not evidence for replacing the frozen glyphs.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Restates and independently checks Hua VI’s mathematical correction; differs from the final printed test in the frozen page. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074) (footnote on the two tests); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC24 — Why the t-squared test excludes characteristic 2

**File/location:** cote 93, scan 073. **Short quote:** “$t^2$ n'est jamais un uniformisant”. **Kind:** unproved claim.

**Additional state:** restriction on the normalization test.

The author correctly notices that D⁽¹⁾(t²)=2t cannot be a unit where 2 is noninvertible. The test must be restricted to the locus where 2t is a unit; it cannot normalize a nonzero invariant on a characteristic-2 fiber.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074) (test-value footnote); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC25 — The cubed-coordinate test and its limitation

**File/location:** cote 93, scan 073. **Short quote:** “+\frac23\frac1{t^2}dt^2”. **Kind:** unproved claim.

The value is correct where 3t² is invertible, as C2 verifies. It has a meaning in characteristic 2 but becomes zero there, so its role is a characteristic-zero sign check rather than a witness to characteristic-2 nonvanishing.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Confirms the formula-level part of Hua’s candidate and adds an independent calculation; broader classification claims remain separate. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074) (test-value footnote); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC26 — The two signs coincide modulo 2

**File/location:** cote 93, scan 073. **Short quote:** “possibles sur $\mathbb{Z}$ coïncident”. **Kind:** unproved claim.

**Additional state:** clarification of the characteristic-two sign choice.

The author’s bracket correctly observes that −G₀=G₀ on a characteristic-2 base. This removes a sign choice there and does not prove uniqueness among all possible characteristic-2 operators.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC27 — Can quadratic differentials be eliminated from the formulation?

**File/location:** cote 93, scan 073. **Short quote:** “s'il n'y aurait pas moyen d'éliminer ce rôle”. **Kind:** conjecture.

**Additional state:** question.

The proposed universal recipient asks for more than rewriting the known formula: it asks that every admissible coherent-valued invariant factor through ω². A precise answer needs the hypotheses on the target and on local surjectivity stated explicitly; the page announces the result without such a proof.

**Confidence:** Medium: the question and its missing hypotheses are explicit.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC28 — Why an induced map u is not automatically an isomorphism

**File/location:** cote 93, scan 073. **Short quote:** “même un \uline{iso}!”. **Kind:** own idea.

**Additional state:** unproved claim.

If e) is omitted, the map G′=(G,0) into ω²⊕𝒪 satisfies the evident rationality, cocycle, invariance and rigidity conditions, but the inclusion u is not an isomorphism. Thus the stated conclusion needs a surjectivity condition or a minimal/universal-target hypothesis; this counterexample does not refute the version retaining all relevant axioms.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC29 — Functorial coherent recipients

**File/location:** cote 93, scan 074. **Short quote:** “$\mathcal{F}_X\simeq\underline{\omega}_{X/\mathbb{C}}^{\otimes2}$”. **Kind:** unproved claim.

The opening continuation extends the same universal-recipient assertion to a family of coherent sheaves natural in X and then to the relative setting. No new proof is supplied, and the distinction in SC28 between a recipient and a minimal surjective recipient remains necessary.

**Confidence:** Medium: extension is explicit but its classification is not verified.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC30 — Changing the acting group of a torsor by a unit

**File/location:** cote 93, scan 074. **Short quote:** “can. (semi)-isomorphes”. **Kind:** unproved claim.

For a unit φ, contracting a torsor along multiplication by φ produces a canonically φ-semilinear torsor isomorphism, and its transition differences become φG. This checks the displayed square without identifying points of different torsors by an unstated choice of origin.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC31 — The factor-12 torsor and the word finest

**File/location:** cote 93, scan 074. **Short quote:** “un multiple $12$ième”. **Kind:** unproved claim.

Contracted change of group along 12·id makes the transition cocycle 12G₀, so the “multiple” description is valid even where 12 is not a unit. In that situation it is not a torsor isomorphism, and “le plus fin” should be read as the exhibited integral refinement rather than an independently proved optimality theorem.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC32 — Uniqueness in a fixed positive characteristic

**File/location:** cote 93, scan 074. **Short quote:** “cela caractérise”. **Kind:** unproved claim.

The proposed replacement of d) by mere nonvanishing is a substantially stronger classification assertion and is not proved by the integral formula. Its exact functoriality and differential-order hypotheses matter, especially in the presence of additive Frobenius operations.

**Confidence:** Low for the full classification: the author immediately marks it doubtful.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC33 — The explicit faux-question margin must remain visible

**File/location:** cote 93, scan 074. **Short quote:** “faux?”. **Kind:** self-flagged.

The margin contains an uncertain qualification ending “d’ordre ≤3”; its uncertainty cannot be resolved by a modern classification theorem. Hua’s VI abbreviates this nearly unreadable end, while the frozen transcription preserves the author’s doubt, so an unqualified uniqueness claim would overstate these pages.

**Confidence:** High that a doubt and order restriction are present; low for the uncertain connecting words.

**Context comparison:** Differs from Hua VI’s abbreviated ending by retaining the explicit faux-question and order-at-most-three qualification. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074) (final nearly-illegible-page footnote); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC34 — Base units and universal nonvanishing

**File/location:** cote 93, scan 074. **Short quote:** “l'indétermination est dans”. **Kind:** unproved claim.

The change from an absolute field scalar to a global base unit is consistent with a functorial invariant that can be multiplied by a scalar pulled back from the base. Nonzero and invertible are different on a general base: multiplication by a nonzero nonunit may vanish on a fiber, so the exact nonvanishing hypothesis is decisive.

**Confidence:** Medium: scalar multiplication is checked; the full classification remains open here.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC35 — The fiberwise condition on a nonintegral base

**File/location:** cote 93, scan 074. **Short quote:** “n'est pas identiquement nul.”. **Kind:** unproved claim.

**Additional state:** added fiberwise qualification.

If the only ambiguity is a base scalar, being nonzero in every residue field makes that scalar a unit, including on a nonreduced base. This explains the added fiberwise requirement but does not rule out extra natural operators with nilpotent coefficients.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds a hypothesis or proof-scope qualification to Hua VI’s announced classification; no settled context result supplies the missing argument. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC36 — The real and finite-regularity extensions

**File/location:** cote 93, scan 075. **Short quote:** “analytique réel, ou le $C^{\infty}$, ou $C^3$”. **Kind:** unproved claim.

The Schwarzian formula and its chain identity make sense for locally invertible real C³ maps, but their output has only continuous coefficients in general. Thus the C³ version requires matching the regularity of the target and the local ODE; it is not literally the same holomorphic sheaf statement, and later even-root constructions also need a sign restriction over the reals.

**Confidence:** Medium: the formula-level extension is clear; the exact category has not been specified.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC37 — Exactness of the analytic derivative sequence

**File/location:** cote 93, scan 075. **Short quote:** “s'annule exactement sur les fonctions loc. constantes”. **Kind:** unproved claim.

A holomorphic one-form has a primitive on a sufficiently small disc, and two primitives differ by a constant on each connected component. This checks local analytic surjectivity and the kernel; it does not assert surjectivity on global sections or in positive characteristic.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC38 — The translation cocycle and its invariance

**File/location:** cote 93, scan 075. **Short quote:** “A(f,g)=dg-df”. **Kind:** unproved claim.

The additive cocycle law follows by cancellation, and adding a constant to g leaves dg unchanged. Both are literal first-derivative identities, with the analytic kernel statement in SC37 supplying the orbit interpretation.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC39 — Translation rigidity with an initial value

**File/location:** cote 93, scan 075. **Short quote:** “g(x)=h(x)”. **Kind:** unproved claim.

Equality A(f,g)=A(f,h) gives d(g−h)=0, and the common initial value removes the locally constant difference. This is a zeroth-order initial condition because the translation group has one parameter; no second-order rigidity is needed here.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC40 — The instruction to replace all functions by étale ones

**File/location:** cote 93, scan 075. **Short quote:** “$\mathcal{E}_X$ plutôt!”. **Kind:** self-flagged.

**Additional state:** withdrawn step.

The marginal change removes functions whose derivative vanishes, but it simultaneously changes the image of d. The next page explicitly replaces the target by the bases of ω and switches from a difference to a ratio, so the earlier target cannot simply be retained.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC41 — The asserted étale-to-all-forms epimorphism fails

**File/location:** cote 93, scan 075. **Short quote:** “\mathcal{E}_X\longrightarrow\underline{\omega}_X\quad\text{épi}”. **Kind:** own idea.

**Additional state:** withdrawn step.

For fixed étale f, the target value −df would force dg=0 and is therefore never reached by an étale g, even locally. C4 gives this direct counterexample, and scan 076 repairs the statement by taking ratios of nonzero forms.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC42 — The translation torsor is said to be trivial

**File/location:** cote 93, scan 075. **Short quote:** “sinon, il est trivial”. **Kind:** unproved claim.

For all analytic functions modulo constants, differentiation identifies the quotient with the vector sheaf ω, whose zero section gives a canonical origin. After restriction to étale coordinates the recipient becomes ω*, an 𝒪*-torsor which need not have a global frame; the triviality remark belongs to the preceding additive construction.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC43 — The corrected multiplicative difference of bases

**File/location:** cote 93, scan 076. **Short quote:** “A'(f,g)=\frac{dg}{df}”. **Kind:** unproved claim.

For étale f and g the ratio is a unit and obeys the multiplicative cocycle A′(f,g)A′(g,h)=A′(f,h). Local integration shows that every unit multiple of df is realized locally, which is exactly the correction missing from the map in SC41.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC44 — The bases of a line bundle form an 𝒪-star torsor

**File/location:** cote 93, scan 076. **Short quote:** “faisceau des bases”. **Kind:** unproved claim.

Any two frames differ by a unique invertible function, so ω* is a torsor under 𝒪*; a frame exists locally by the definition of an invertible sheaf. This is a change in both the target and the acting group from the additive ω-torsor discussed on 075.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC45 — Frames modulo constants and line-bundle connections

**File/location:** cote 93, scan 076. **Short quote:** “L^*/\mathbb C^*\simeq”. **Kind:** unproved claim.

A connection on a line bundle over a small analytic disc has a nonzero horizontal solution of its first-order equation; two horizontal frames differ by a constant. Hence the displayed quotient is an isomorphism of analytic sheaves, while global horizontal frames may be obstructed by monodromy and the assertion is not automatically valid algebraically.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC46 — The logarithmic difference has a convention-sensitive sign

**File/location:** cote 93, scan 076. **Short quote:** “D_g-D_f”. **Kind:** reading question.

**Additional state:** own idea.

With the stated convention that D_f makes f horizontal, C4 gives D_g−D_f=−d log(g/f), whereas the page uses the positive sign. The positive expression remains a valid cocycle, but equating it to that connection difference needs the opposite convention; Hua VI repeats the equality without resolving this issue.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Contradicts the sign identification repeated in Hua VI under the explicitly stated horizontal-frame convention. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (item b, line-bundle connections); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC47 — The logarithmic derivative quotient

**File/location:** cote 93, scan 076. **Short quote:** “g\longmapsto\frac{dg}{g}”. **Kind:** unproved claim.

Locally, any holomorphic one-form a(t)dt is d log(exp∫a(t)dt), and the kernel consists of nonzero constants. This proves the analytic sheaf quotient claimed for the trivial line bundle, but not a global quotient of sections or a characteristic-p analogue.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC48 — The preliminary additive logarithmic cocycle

**File/location:** cote 93, scan 077. **Short quote:** “B'(f,g)=\dfrac{dg}{g}-\dfrac{df}{f}”. **Kind:** unproved claim.

On nonzero functions this is an additive cocycle by cancellation and equals d log(g/f). Its use of all nonzero functions differs from the later restriction to nonvanishing étale coordinates, where d log g must also be a basis.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC49 — The inverse-differential invariant

**File/location:** cote 93, scan 077. **Short quote:** “g\longrightarrow\frac{g}{dg}”. **Kind:** unproved claim.

An étale g has invertible dg, so g/dg is a well-defined vector field and is invariant under multiplication of g by a nonzero constant. Differences of these vector fields satisfy the additive cocycle, even when g itself vanishes.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC50 — The nonzero-value hypothesis in multiplicative rigidity

**File/location:** cote 93, scan 077. **Short quote:** “un pt qui n'est pas un zéro”. **Kind:** unproved claim.

**Additional state:** nonzero-value qualification.

If g/dg=h/dh and g,h are nonzero near the chosen point, equality of logarithmic derivatives implies g=ch, and the common nonzero value forces c=1. The author’s nonzero hypothesis is needed: g=t and h=2t have equal g/dg and agree at their zero without being equal.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC51 — The author rejects the inverse-vector surjectivity

**File/location:** cote 93, scan 077. **Short quote:** “ne peut être id. nul”. **Kind:** withdrawn in same text.

If g/dg were identically zero while dg were invertible, then g would be identically zero, contradicting étaleness. Thus the proposed epimorphism onto all vector fields fails exactly as the author observes; this is an explicit internal retraction, not merely a later objection.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC52 — Restriction to the nonvanishing étale locus

**File/location:** cote 93, scan 077. **Short quote:** “il faut se borner à”. **Kind:** self-flagged.

**Additional state:** withdrawn step.

On E* the logarithmic derivative is a basis, and every such analytic one-form is locally d log g for a nonzero étale g. This gives the revised torsor of bases and the multiplicative ratio, rather than restoring the rejected surjectivity onto all vector fields.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC53 — The ratio has f over g rather than g over f

**File/location:** cote 93, scan 077. **Short quote:** “\frac{dg}{df}\frac{g}{f}”. **Kind:** own idea.

**Additional state:** reading question.

The left-hand ratio (dg/g)/(df/f) equals (dg/df)(f/g), as direct cancellation shows. C4 and C9 test f=t,g=t² and obtain 2 on the left but 2t² from the printed product; the later table on 082 uses the correct unsimplified ratio.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds an explicit counterexample to the expanded ratio; agrees with Hua VI’s later unsimplified ratio. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (multiplicative invariant and table); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC54 — Homogeneity is proposed as a condition of success

**File/location:** cote 93, scan 077. **Short quote:** “ce qui semble”. **Kind:** conjecture.

The failed action of G_m on the whole affine line has a special orbit at zero, whereas its restriction to G_m is transitive, matching the author’s examples. This motivates the conjecture but does not prove that transitivity is necessary or sufficient for such a differential-invariant classification.

**Confidence:** Medium as an explanation of these examples; low for a general criterion.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC55 — The affine action supplies horizontal differentials

**File/location:** cote 93, scan 077–078. **Short quote:** “f\longrightarrow D_{df}”. **Kind:** unproved claim.

Replacing f by af+b multiplies df by a constant and preserves the connection which makes it horizontal. This checks that the proposed construction is affine-invariant, provided the horizontality convention is kept explicit.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC56 — The two quotient stages give the affine connection sheaf

**File/location:** cote 93, scan 078. **Short quote:** “\operatorname{Aff}(1,\mathbb C)\backslash \mathcal E_X”. **Kind:** unproved claim.

The two local analytic arguments are successive integration of a nonzero one-form and finding a horizontal frame for a line connection. They identify the affine orbit sheaf with Conn(ω); the statement concerns sheaves and need not yield one global affine coordinate.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC57 — The affine logarithmic coefficient is correct as an invariant

**File/location:** cote 93, scan 078. **Short quote:** “\frac{g''}{g'}-\frac{f''}{f'}”. **Kind:** unproved claim.

**Additional state:** reading question.

Differentiating log(g′/f′) gives the displayed one-form and its additive cocycle law. The calculation verifies the invariant itself; its identification with D_dg−D_df retains the sign issue identified in SC46.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC58 — The question mark after the affine group of G-m

**File/location:** cote 93, scan 078. **Short quote:** “opérant sur $G_m$.”. **Kind:** self-flagged.

**Additional state:** question.

The indicated transformations z↦cz and z↦c/z form G_m⋊(ℤ/2) over ℂ, so they do act on G_m as written. This answers the elementary action question, while the analogy with an affine group is terminology rather than a new classification proof.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC59 — The squared logarithmic differential quotient

**File/location:** cote 93, scan 078. **Short quote:** “\omega\mapsto\omega^2”. **Kind:** unproved claim.

Locally over ℂ, equality of squares of nonzero one-forms gives a constant sign, so equality of (d log f)² identifies f and g up to g=cf or g=c/f. Conversely a local square root of a nonzero quadratic differential, followed by logarithmic integration, proves surjectivity onto ω²*; these arguments use characteristic zero.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC60 — Taking a root of an n-differential

**File/location:** cote 93, scan 080. **Short quote:** “\omega^{1/n}”. **Kind:** unproved claim.

For n≠0 over ℂ, a nowhere-zero coefficient admits a local analytic n-th root, unique up to a locally constant n-th root of unity. This is a local construction; when n is not invertible on a positive-characteristic base the same argument does not apply.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC61 — The primitive ambiguity gives a well-defined projective point

**File/location:** cote 93, scan 080. **Short quote:** “donc $c_{\int\omega^{1/n}}$ bien défini”. **Kind:** unproved claim.

Two root choices differ by ε with εⁿ=1, and two primitives then differ by εf+b. These are constant affine transformations, so projective invariance proves that the resulting c_n is independent of both choices.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC62 — Checking the c-n coefficient

**File/location:** cote 93, scan 080. **Short quote:** “\frac{2n+1}{n^2}”. **Kind:** unproved claim.

C5 derives the formula from λ=−f′/(nf) and 2λ′+λ², giving exactly (2n+1)/n². The independent symbolic check confirms the coefficient without deciding any other uncertain symbol on the page.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (formula and coefficient footnote); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC63 — The wrong function appears in the second G-m-n term

**File/location:** cote 93, scan 080. **Short quote:** “\frac{2m+1}{m^2}\left(\frac{g'}g\right)^2”. **Kind:** own idea.

**Additional state:** reading question.

Because the second term is c_m(fdtᵐ), its logarithmic square must use f′/f. The test m=1,n=2,f=t,g=t² gives the correct difference 0 but the printed expression −9dt²/t²; Hua VI flags the same error, and C5/C9 independently verify it.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Restates Hua VI’s correction of the second logarithmic-square term and independently tests it. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (final coefficient footnote); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC64 — The mixed-weight cocycle

**File/location:** cote 93, scan 080. **Short quote:** “G_{m,p}(\omega_m,\omega''_p)”. **Kind:** unproved claim.

With the definition G_m,n=c_n−c_m in a common projective-connection torsor, the mixed-weight cocycle is cancellation of c_n. It is valid for the defined difference, independent of the erroneous expanded second term identified in SC63.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC65 — Compatibility with tensor powers

**File/location:** cote 93, scan 080. **Short quote:** “G_{m,nr}(\omega_m,\omega_n^r)”. **Kind:** unproved claim.

C5 proves c_nr(ω_nʳ)=c_n(ω_n) by substitution, so the asserted G identity follows. This also follows geometrically because the local root differentials differ only by constants, but the formula-level calculation is independently recorded.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC66 — The inserted power repairs the type of ds

**File/location:** cote 93, scan 080. **Short quote:** “G_{m,n}(\omega_m,(ds)^n)”. **Kind:** withdrawn in same text.

The earlier line supplies ds where an n-differential is expected, and the insertion replaces it by (ds)ⁿ. The repaired identity then follows because a root is ds and its primitive is s; the incomplete line remains part of the author’s revision history.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC67 — Recovery of the ordinary Schwarzian difference

**File/location:** cote 93, scan 080. **Short quote:** “G_{m,n}((dt)^m,(ds)^n)=G_{0,0}(t,s)”. **Kind:** unproved claim.

The first root differential has primitive t and the second has primitive s, so the difference is c_s−c_t=G(t,s). This also specifies what the page’s index 0 means: a coordinate input, not substitution n=0 into a formula containing 1/n.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC68 — The cancelled denominator in c-prime

**File/location:** cote 93, scan 080. **Short quote:** “c'_n(\omega)=n^2”. **Kind:** self-flagged.

**Additional state:** withdrawn step.

The margin first cancels a 12, while the subsequent rescaling lines again use c_n/12. Since c_n is a torsor point, scalar multiplication must mean contracted change of group, and the inconsistent intermediate notation does not by itself define an integral normalized section.

**Confidence:** Low for the author’s final intended normalization; high that the intermediate changes need preservation.

**Context comparison:** Restates Hua VI’s decision to leave the draft torsor rescaling unresolved and records the cancellation explicitly. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (final footnote explicitly declines to draw a conclusion); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC69 — The rescaled difference has reversed order and a target issue

**File/location:** cote 93, scan 080. **Short quote:** “\alpha^2c'_m(\omega_m)-\beta^2c'_n(\omega'_n)”. **Kind:** reading question.

**Additional state:** own idea.

On the displayed normalization this equals −(δ²/12)G_m,n, rather than its positive multiple, because the order is reversed. Moreover the difference of two points of a common torsor belongs to its acting sheaf, not canonically to the torsor itself; the displayed membership in a power of T therefore needs interpretation.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (rescaling footnote); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC70 — Invariance with parameters pulled back from the base

**File/location:** cote 93, scan 080. **Short quote:** “\Gamma(S,\mathcal O_S^*)”. **Kind:** unproved claim.

The parameters a and b have zero relative Hasse derivatives, so the integral homography calculation C1 proves the displayed three invariances over the base. Allowing arbitrary functions on X in those parameters would change the assertion and is not justified.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC71 — Equal differentials imply equal projective data in characteristic zero

**File/location:** cote 93, scan 080. **Short quote:** “df=dg\Longrightarrow G(f,g)=0”. **Kind:** unproved claim.

Locally analytically, equal differentials give g=f+b, so projective invariance applies. In characteristic 2 or 3 equal ordinary differentials do not force G₀ to agree: C2’s t+t² and t+t³ give explicit failures, so the distinction between G and G₀ must be retained.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds the small-characteristic limitation to Hua VI’s analytic implication, using the independently checked examples reported in Hua IX. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC72 — Equal squared logarithmic differentials

**File/location:** cote 93, scan 080. **Short quote:** “\left(\frac{df}{f}\right)^2=\left(\frac{dg}{g}\right)^2”. **Kind:** unproved claim.

On the connected complex analytic nonzero étale locus, the two logarithmic differentials differ by a constant sign, hence f=cg or f=c/g. Both transformations are homographies and give G(f,g)=0; this is the same local argument as SC59.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC73 — The question about a constant multiple of a logarithmic differential

**File/location:** cote 93, scan 080. **Short quote:** “\frac{df}{f}=c\frac{dg}{g}\qquad ?”. **Kind:** conjecture.

**Additional state:** question.

For a constant c and local choices of logarithm, integration gives f=Cgᶜ, with a multiplicative constant C that the last line suppresses. Such a power is generally not a homography: f=t²,g=t gives G(g,f)=3dt²/t² in characteristic zero, so the preceding vanishing implication does not extend to every c.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC74 — The unfinished product at the foot of 080

**File/location:** cote 93, scan 080. **Short quote:** “(df-dg)”. **Kind:** reading question.

The product of a first-differential difference and a squared-logarithmic-differential difference is written without a proposed equality or target. It cannot be promoted into an additional vanishing criterion merely because each adjacent factor occurs in a valid preceding implication.

**Confidence:** Low: there is no complete asserted relation to check.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft page, no interpretation supplied); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC75 — The first uniformization diagram is only partially specified

**File/location:** cote 93, scan 081. **Short quote:** “\mathbb R\text{-an}”. **Kind:** reading question.

**Additional state:** unproved claim.

The first row labels correspondences among D_X, U(x), B(x), V(x) and a doubtful D′_X as real-analytic or canonical, but these objects and the precise arrows are not defined on this sheet. Hua’s later discussion of homogeneous domains is a possible contextual lead, not enough to certify these particular maps or fill their uncertain directions.

**Confidence:** Low: definitions and several arrow directions are missing.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft page 80 expressly not reconstructed); `context/hua_project/93.modern.tex`, X, “Domaines homogènes et revêtement universel” (pp. 125–129, later scans 126–130 not supplied); `context/same_cote_93/MPL_93_002-046_notes.md`, P03/P09 (scan 036 and cross-cote comparison); `context/notes/RESULTS_STATE.md`: no settled diagram identification; S20 only.

### SC76 — The question between Sigma and the hatted tangent object

**File/location:** cote 93, scan 081. **Short quote:** “\widehat T_X”. **Kind:** self-flagged.

**Additional state:** question.

The paired arrows between Σ(x) and the hatted T-object carry an explicit question mark and a real-analytic label. Without identifying the hatted object and the intended map, one cannot infer an isomorphism from the two-way drawing; this remains an author-unverified diagram question.

**Confidence:** Low: the relevant objects are not fixed by the sheet.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft not reconstructed); `context/hua_project/93.modern.tex`, X, “Domaines homogènes et revêtement universel” (pp. 125–129, later scans 126–130 not supplied); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC77 — The questioned downward map from U to D

**File/location:** cote 93, scan 081. **Short quote:** “\mathbb R\text{-anal.}\;?”. **Kind:** self-flagged.

**Additional state:** question.

The arrow U(x)→D_X asks whether the map is real analytic. The available context does not specify a construction or agreed analytic structures for these exact objects, so this arrow remains unverified.

**Confidence:** Low: the map is not defined on the supplied sheet.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft not reconstructed); `context/hua_project/93.modern.tex`, X, “Domaines homogènes et revêtement universel” (pp. 125–129, later scans 126–130 not supplied); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC78 — The questioned downward map from B to the hatted T-object

**File/location:** cote 93, scan 081. **Short quote:** “?\;\mathbb R\text{-anal.}”. **Kind:** self-flagged.

**Additional state:** question.

The middle downward arrow B(x)→the hatted T-object has its own question mark about real analyticity. The path-class description of B later on the page gives no analytic formula for this arrow, so its status cannot be inferred from the neighboring maps.

**Confidence:** Low: neither the target identification nor an analytic map is fixed.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft not reconstructed); `context/hua_project/93.modern.tex`, X, “Domaines homogènes et revêtement universel” (pp. 125–129, later scans 126–130 not supplied); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC79 — The questioned downward map from V to D-prime

**File/location:** cote 93, scan 081. **Short quote:** “?\;\mathbb R\text{-anal.}”. **Kind:** self-flagged.

**Additional state:** question.

The right-hand downward arrow V(x)→D′_X separately asks about real analyticity. A hoped-for conjugate symmetry with the U-arrow would still require a definition of V and D′; the draft and Hua’s summary do not supply that definition.

**Confidence:** Low: the claimed conjugate interpretation is not established.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft not reconstructed); `context/hua_project/93.modern.tex`, X, “Domaines homogènes et revêtement universel” (pp. 125–129, later scans 126–130 not supplied); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC80 — The unfinished product of universal covers

**File/location:** cote 93, scan 081. **Short quote:** “\widetilde X_{(x)}”. **Kind:** reading question.

The product involving X, its conjugate, and a fundamental-group action stops at an equals sign and is followed by disconnected covering-space labels. It suggests an associated or diagonal quotient, but the action and equivalence relation needed to identify that object are not fully given here.

**Confidence:** Low: this is an incomplete formula, not a theorem with settled notation.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft not reconstructed); `context/hua_project/93.modern.tex`, X, “Domaines homogènes et revêtement universel” (pp. 125–129, later scans 126–130 not supplied); `context/same_cote_93/MPL_93_002-046_notes.md`, P03; `context/notes/RESULTS_STATE.md`: no matching settled construction.

### SC81 — The path-class construction of B

**File/location:** cote 93, scan 081. **Short quote:** “(c\lambda,\xi)\simeq(c,\lambda\xi)”. **Kind:** unproved claim.

**Additional state:** reading question.

If the fundamental group acts on the indicated fiber, this is the usual equivalence relation for transporting that fiber along paths and forms an associated local-system bundle. The text does not specify the required action or a compatible analytic structure, so the construction explains the set-theoretic pattern but proves none of the real-analytic arrows.

**Confidence:** Medium for the associated-bundle pattern; low for the intended analytic realization.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft not reconstructed); `context/hua_project/93.modern.tex`, X, “Domaines homogènes et revêtement universel” (pp. 125–129, later scans 126–130 not supplied); `context/same_cote_93/MPL_93_002-046_notes.md`, P03; `context/notes/RESULTS_STATE.md`: no settled B(x) identification.

### SC82 — The proposed rank-two splitting on the draft

**File/location:** cote 93, scan 081. **Short quote:** “=\Omega^{-1}\oplus\Omega^0”. **Kind:** unproved claim.

**Additional state:** reading question.

The visible right-hand side gives a clear split rank-two bundle for the following matrix calculations, but the symbol on the left is uncertain. The subsequent algebra can be checked conditionally with E=Ω⁻¹⊕𝒪 without identifying that E with every hatted or Lie-algebra object earlier in the draft.

**Confidence:** High for the conditional split-bundle calculation; low for the uncertain left-hand identification.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft matrices) and VII (later rank-two constructions); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC83 — The endomorphism matrix and its differential twist

**File/location:** cote 93, scan 081. **Short quote:** “\check E\otimes E”. **Kind:** unproved claim.

For E=Ω⁻¹⊕𝒪, Hom of each ordered pair of summands gives the matrix (𝒪,Ω⁻¹;Ω,𝒪), and tensoring with Ω gives (Ω,𝒪;Ω²,Ω). This verifies both displayed matrices from the stated splitting, with no need to reconstruct the earlier diagrams.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC84 — The trace-zero submatrix and the cancelled numerical matrix

**File/location:** cote 93, scan 081. **Short quote:** “\Omega^2&-\Omega^1”. **Kind:** unproved claim.

**Additional state:** withdrawn step.

Trace zero replaces the two diagonal Ω entries by a single entry and its negative, leaving Ω⊕𝒪⊕Ω² as the associated bundle. The earlier numerical matrix is crossed out and does not establish degrees or dimensions; in characteristic 2 trace-zero matrices contain the scalars, so this complex-analytic notation cannot bypass the later characteristic-2 issue.

**Confidence:** High for the trace calculation; low for interpreting the crossed-out numerical entries.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft matrices) and VII (trace/Lie discussion); `context/notes/RESULTS_STATE.md`: no settled identification for this cancelled matrix.

### SC85 — A conditional interpretation of the genus counts

**File/location:** cote 93, scan 081. **Short quote:** “3g-3”. **Kind:** own idea.

If Ω is the canonical bundle of a compact genus-g curve with g≥2, then h⁰(Ω²)=3g−3, h⁰(Ω)=g and h⁰(𝒪)=1, summing to 4g−2 for the trace-zero differential-twisted matrix. This explains the displayed numbers consistently, but the draft does not itself state compactness, the genus range, or that these are the spaces being counted.

**Confidence:** Medium: Riemann–Roch fits all numbers, but their intended interpretation is not specified.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (explicitly lists g+1, 3g−3, 4g−2 without reconstruction); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

**Primary source:** Stacks Project, Riemann–Roch and duality, Lemma 53.5.2: [source](https://stacks.math.columbia.edu/tag/0B5B) (conditional application, not an identification of the draft notation).

### SC86 — The isolated Omega and omega identification

**File/location:** cote 93, scan 081. **Short quote:** “\Omega^1=\omega^{\otimes2}”. **Kind:** reading question.

This isolated equality sits beside incomplete reciprocal-function calculations and is not reconciled with the Ω-powers used in the matrix block. It could use another convention for Ω, but treating it as a global identification would change all the line-bundle weights; no such convention is established on this sheet.

**Confidence:** Low: the local notation is not explained.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft not reconstructed); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC87 — Inverting f plus its reciprocal

**File/location:** cote 93, scan 081. **Short quote:** “f^2-fh+1=”. **Kind:** self-flagged.

**Additional state:** unfinished step.

The intended equation has roots governed by h²−4, and h being nonzero alone does not make its roots étale: h=2 forces f=1. Conversely the map f↦f+1/f has critical points f=±1 and can take the value 0, so neither the image nor its local inverse is described just by “h sans zéro”.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft not reconstructed); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC88 — The reciprocal-logarithmic ODE is locally solvable

**File/location:** cote 93, scan 081. **Short quote:** “g=c\exp\int\frac1\varphi”. **Kind:** unproved claim.

For a nonzero holomorphic coefficient φ, the local equation g′/g=1/φ is solved by this exponential with c≠0 and gives a nonzero étale g. The integration constant is necessary, and possible global periods prevent interpreting the formula as an unconditional global solution.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (draft not reconstructed, compare item b logarithmic integration); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC89 — The diagonal cancellation strokes on the draft

**File/location:** cote 93, scan 081. **Short quote:** “f+\frac1f=”. **Kind:** withdrawn in same text.

**Additional state:** reading question.

The frozen page records long diagonal cancellation strokes crossing the working, alongside incomplete formulas and question marks. Their precise scope is not stated by the text, so this sheet is treated as draft exploration rather than a sequence of final theorems; no entire mathematical claim is silently deleted on that basis.

**Confidence:** High that cancellation strokes were recorded in the frozen audit; low for their exact intended scope.

**Context comparison:** Adds a separate question or conditional check for the draft that Hua VI declines to reconstruct; Hua X remains only a later contextual lead. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (calls pages 79–80 drafts and notes the two strokes); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC90 — The powered additive ratio in the table

**File/location:** cote 93, scan 082. **Short quote:** “A_n(f,g)=\left(\frac{dg}{df}\right)^n”. **Kind:** unproved claim.

This is an 𝒪*-valued multiplicative cocycle obtained by taking a power of the ratio of bases. Despite the heading “écart additif”, its displayed operation is a ratio, so its cocycle law is multiplicative rather than the additive law of G.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC91 — The affine sign conflict is repeated in the table

**File/location:** cote 93, scan 082. **Short quote:** “D_{dg}-D_{df}”. **Kind:** reading question.

The table again equates this difference with the positive logarithmic derivative of dg/df. The direct horizontal-frame computation in C4 gives the negative sign, whereas the β_n arrow later on this same page uses the compatible negative coefficient; the internal convention issue is therefore still present.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (table and β_n footnote); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC92 — The missing star in the first powered quotient target

**File/location:** cote 93, scan 082. **Short quote:** “\underline\omega_X^n”. **Kind:** reading question.

**Additional state:** own idea.

The image (df)ⁿ of an étale coordinate is a nowhere-zero n-differential, so the quotient target is ωⁿ* for n≠0, as written in the repeated diagram below. The first target without a star cannot literally include zero while also being described as an 𝒪*-torsor.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (table displays ω^{n*}); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC93 — A possible group-level meaning of the exceptional n-equals-zero arrow

**File/location:** cote 93, scan 082. **Short quote:** “(n=0)”. **Kind:** own idea.

**Additional state:** reading question.

If μ₀ denotes the kernel of the power-zero map G_m→G_m, then μ₀=G_m and μ₀⋊G_a is the affine group, which gives a coherent possible indexing convention for this arrow. This interpretation does not define β₀ by substituting into 1/n or identify (df)⁰ with a connection; the draft supplies no limiting construction.

**Confidence:** High for the elementary kernel identity; medium for identifying the author’s intended convention.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (β_n formula explicitly n≠0); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC94 — Forgetting an affine coordinate gives a projective one

**File/location:** cote 93, scan 082. **Short quote:** “D\mapsto c_D”. **Kind:** unproved claim.

Constant affine transformations form a subgroup of the constant projective transformations, so the map of orbit sheaves exists locally in the analytic setting. With the identifications on 078 and 073 it gives γ:Conn(ω)→Conn_proj(X), whose nonlinear formula is checked below.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC95 — The boxed variation formula

**File/location:** cote 93, scan 082. **Short quote:** “c_{D+\omega_1}=c_D+2D\omega_1+\omega_1^2”. **Kind:** unproved claim.

C5 checks the formula by writing D=D_dt+λdt and ω₁=hdt: the difference of 2λ′+λ² is 2(h′+λh)+h². The term Dω₁ is the induced covariant derivative, so replacing it by an ordinary derivative in a nonhorizontal frame would lose the cross term.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (boxed formula and ensuing computation); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC96 — The exponential respects the sign-affine action

**File/location:** cote 93, scan 082. **Short quote:** “\exp(\pm f+a)”. **Kind:** unproved claim.

The elementary exponential identity gives exp(±f+a)=exp(a)(exp f)^±1. Consequently exponentiation connects the sign-and-translation quotient of additive coordinates with the inversion-and-scaling quotient of nonzero coordinates, locally over ℂ.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC97 — The later multiplicative ratios correct the earlier expansion

**File/location:** cote 93, scan 082. **Short quote:** “\operatorname{Ecmu}_1(f,g)=\frac{dg/g}{df/f}”. **Kind:** unpursued implication.

The table retains the correct unsimplified logarithmic ratio and its square, avoiding the inverted f/g factor on 077. C4’s counterexample therefore concerns the earlier expanded product, not these later formulas.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (table); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC98 — The first projective coefficient needs a quadratic differential factor

**File/location:** cote 93, scan 082. **Short quote:** “\frac{d^3g/df^3}{dg/df}”. **Kind:** reading question.

**Additional state:** own idea.

The first line is a coefficient computed in coordinate f and needs multiplication by (df)² to equal the second line, which is a quadratic differential written in t. The same tensor type favors ω² over the uncertain ω¹/ω² exponent at the end, but mathematical typing is recorded only as a research observation.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (projective entry of the table); `context/same_cote_93/MPL_93_002-046_notes.md`, P01; `context/notes/RESULTS_STATE.md`: **MPL_93_002-046 P01**, no settled reading of this exponent.

### SC99 — The questioned vertical identity between the two omega-star targets

**File/location:** cote 93, scan 082. **Short quote:** “\mathrm{id}”. **Kind:** self-flagged.

**Additional state:** question.

The direct calculation d log(exp f)=df shows that the map induced by exponentiation is the identity on ω* under the two displayed quotient identifications. This answers the diagram’s question locally in the complex analytic category, without requiring a globally chosen logarithm.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (quotient diagram); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC100 — The power arrows alpha-n and alpha-prime-two

**File/location:** cote 93, scan 082. **Short quote:** “\alpha_n(\omega_1)=\omega_1^n”. **Kind:** unproved claim.

The arrows are equivariant for 𝒪*→𝒪*, φ↦φⁿ, and locally surjective over ℂ by root extraction on nowhere-zero coefficients. The n=2 identification in the diagram is compatible with the exponential sign-action identity in SC96; it is not a characteristic-2 root-extraction statement.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC101 — The minus sign in beta-n and Hua’s differing reading

**File/location:** cote 93, scan 082. **Short quote:** “\varphi\mapsto-\frac1n\frac{d\varphi}{\varphi}”. **Kind:** reading question.

**Additional state:** unproved claim.

The group arrow has an explicit minus sign, and the frozen β_n formula lists minus as its first uncertain reading; C4–C5 show that this is the sign making f^{1/n}dt horizontal. Hua’s footnote reports a plus reading for that formula and corrects it mathematically, so its report must not override the newly frozen alternatives.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Differs from Hua VI’s report of the doubtful written sign, while independently agreeing with its required mathematical minus sign. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (β_n sign footnote); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC102 — The local formula for gamma

**File/location:** cote 93, scan 082. **Short quote:** “c_{pr}(t)+(2f'+f^2)dt^2”. **Kind:** unproved claim.

Using D_dt as the horizontal reference connection gives γ(D_dt+fdt)=c_t+(2f′+f²)dt². This is the λ=f specialization of C5 and is compatible with the boxed variation formula.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (γ and c_n calculation); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC103 — The general gamma-beta coefficient and the final n-one specialization

**File/location:** cote 93, scan 082. **Short quote:** “(2n+1)”. **Kind:** reading question.

**Additional state:** inserted coefficient correction and n-one specialization.

C5 verifies the inserted coefficient 2n+1 and the denominator n². The last line dropping n is correct only for n=1, as the nearby γβ₁ margin indicates; interpreting that line as another equality for arbitrary n would be false.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (c_n coefficient footnote); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC104 — Recovering the Schwarzian from gamma-beta-one-d

**File/location:** cote 93, scan 082. **Short quote:** “\gamma\beta_1d(f)”. **Kind:** unproved claim.

Substitution of the coefficient f′ for a one-form df gives precisely −2f‴/f′+3(f″/f′)². This independently checks the canceled n² denominator and links the diagram back to the normalization on 073 and the earlier scan 036.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Restates earlier P01 and Hua VI’s normalization, with an independent formula check. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/same_cote_93/MPL_93_002-046_notes.md`, P01 (scan 036); `context/notes/RESULTS_STATE.md`: **MPL_93_002-046 P01**.

### SC105 — The delta formula has coefficients minus one and five-fourths

**File/location:** cote 93, scan 082. **Short quote:** “\frac54”. **Kind:** reading question.

**Additional state:** unproved claim.

For ω₂=fdt², C5 gives δ(ω₂)=c_t+[f−f″/f+(5/4)(f′/f)²]dt². This verifies the first alternative for the doubtful f″ coefficient and the stated 5/4, while leaving the uncertain c_pr argument in the diplomatic transcription unchanged.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (coefficient footnote); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC106 — Delta after squaring and the exponential correction

**File/location:** cote 93, scan 082. **Short quote:** “\delta\alpha'_2(\omega_1)”. **Kind:** unproved claim.

Applying the power-compatibility identity gives δ(ω₁²)=γβ₁(ω₁)+ω₁² and the final coefficient f²−2f″/f+3(f′/f)². For ω₁=du this is also G(t,eᵘ)−G(t,u)=(du)², rechecking the earlier P02 correction rather than supplying any p-curvature conclusion.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Restates and rechecks earlier P02’s exponential correction, while retaining the P05/P06 limits on p-curvature inferences. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084); `context/same_cote_93/MPL_93_002-046_notes.md`, P02/P05/P06 (scan 036); `context/notes/RESULTS_STATE.md`: **MPL_93_002-046 P05**, **P06** are background bounds.

### SC107 — The final squared logarithmic ratio is algebraically correct

**File/location:** cote 93, scan 084. **Short quote:** “E(f,g)=\left(\frac{dg}{g}\right)^2”. **Kind:** unproved claim.

Dividing the two squares gives (dg/df)²/(g/f)² exactly, with all denominators units on E*. This is consistent with the table on 082 and corrects the direction of the unsquared product written on 077.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (item d refers to manuscript p.83); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC108 — The blanket claim of axioms a through e needs the adapted meanings

**File/location:** cote 93, scan 084. **Short quote:** “On a\quad a) b) c) d) e)”. **Kind:** unproved claim.

The orbit and local-surjectivity arguments in SC59 establish the intended quotient by scaling and inversion, and E satisfies the multiplicative identity E(f,g)E(g,h)=E(f,h). The earlier additive b) cannot be copied literally into this 𝒪*-valued construction, and a rigidity initial condition must also remove the inversion ambiguity.

**Confidence:** High for the stated check; it uses the displayed formula or an explicit local argument.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (item d and table); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC109 — The deleted translation-quotient fragment

**File/location:** cote 93, scan 084. **Short quote:** “\mathcal E_X/G_a(\mathbb C)”. **Kind:** withdrawn in same text.

**Additional state:** reading question.

The final fragment is deleted and has no completed assertion after the quotient. It does not retract the separately justified translation quotient on 078, nor does it define an additional target for E.

**Confidence:** High that it is a deleted incomplete fragment; no definite mathematical assertion to test.

**Context comparison:** Adds statement-level checks or qualifications to Hua VI; no matching settled RESULTS_STATE theorem is being restated. `context/hua_project/93.modern.tex`, VI, “D’autres groupes” (pp. 74–83 = scans 075–084) (end of other-groups section); `context/notes/RESULTS_STATE.md`: no matching settled entry or earlier proof for this specific assertion; S20 is a planning lead.

### SC110 — What scans 072–074 actually establish about Hua’s candidate

**File/location:** cote 93, scan 072–074. **Short quote:** “G_0(f,g)”. **Kind:** reading question.

**Additional state:** context comparison.

The supplied scans explicitly propose the Hasse-derivative formula, the factor 12, arbitrary-base compatibility and a characteristic-p uniqueness question; they do not state a p-versus-p² homography theorem. Hua’s modernised reading places that theorem in its later IX, pp.121–123, so the two parts of the findings-register claim require different textual attributions.

**Confidence:** High: this is a direct comparison of the frozen pages and the labelled context subsections.

**Context comparison:** Refines Hua’s findings-register attribution by separating the supplied formula pages from its later p-versus-p² claim. `context/hua_project/93.modern.tex`, VI, “L’invariant projectif, et son unicité” (pp. 71–73 = scans 072–074); `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC111 — The relative constants for the first three Hasse derivatives

**File/location:** cote 93, scan 073–074. **Short quote:** “D_t^{(3)}”. **Kind:** own idea.

**Additional state:** check of a contextual lead.

C6 independently proves that on A[t] the common kernel is A[tᵖ] for p>3, A[t⁴] for p=2, and A[t⁹] for p=3, for every 𝔽_p-algebra A. These are relative Frobenius subrings with arbitrary coefficients from A, not necessarily literal powers of elements when A is imperfect; this checks Hua’s later local claim without attributing it to the supplied pages.

**Confidence:** High: direct coefficient proof, including nilpotent coefficients, reviewed by the root agent.

**Context comparison:** Restates Hua IX’s local kernel claim and adds an independent arbitrary-coefficient-ring proof plus the relative-versus-literal-power qualification. `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC112 — Why level p alone loses invariance in characteristics 2 and 3

**File/location:** cote 93, scan 073–074. **Short quote:** “identiquement nulle en car. $2$ et $3$”. **Kind:** own idea.

**Additional state:** check of a contextual lead.

The coordinates t+t² in characteristic 2 and t+t³ in characteristic 3 differ from t by a relative p-th-power translation, yet their G₀-values are 1 and −1. Thus level-p constants are too large for the proposed G₀-invariance in these characteristics; this is an explicit necessity test for the later level-p² refinement, not by itself a proof of all its rigidity claims.

**Confidence:** High: exact Hasse computations, also exercised in the finite-ring script.

**Context comparison:** Restates and independently checks Hua IX’s two counterexamples to level-p invariance. `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied) (examples in the injectivity footnote); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC113 — Rigidity over an arbitrary coefficient ring in the nilpotent model

**File/location:** cote 93, scan 073–074. **Short quote:** “G_0(f,g)”. **Kind:** own idea.

**Additional state:** independent check of a contextual lead.

C7 proves that Q(s)=0 with unit first derivative forces a homography in A[t]/tᵠ for q=p>3, q=4 in characteristic 2, and q=9 in characteristic 3, without a Picard hypothesis. The proof uses a two-jet normalization and the unit binomial coefficients binom(d,3); C9’s exhaustive finite-field tests are only supplementary diagnostics.

**Confidence:** High: a complete arbitrary-ring coefficient proof was checked and separately reviewed by the root agent.

**Context comparison:** Restates Hua IX’s nilpotent-model result and adds an independent written proof; its reported Lean certificate was not executed. `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied) (Hua’s reported α=0 Lean verification, not rerun); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC114 — A new descent argument fills the arbitrary-alpha step for the monic model

**File/location:** cote 93, scan 073–074. **Short quote:** “G_0(f,g)”. **Kind:** own idea.

**Additional state:** refinement of a contextual lead.

C8 supplies the missing written argument for B=A[t]/(tᵠ−α) with Pic(A)=0: a finite faithfully flat root extension reduces to C7, and the rank-one kernel of matrix relations descends to an invertible module which the Picard hypothesis trivializes. Determinant and denominator units then descend, giving a homography over A; the root agent independently reviewed this proof for the stated monic model, without promoting it to an unrestricted global theorem.

**Confidence:** High for the stated monic model: the complete kernel/descent proof was independently reviewed; global generalizations were not checked.

**Context comparison:** Adds the monic-model arbitrary-α descent proof which Hua IX explicitly leaves unchecked; it refines that candidate within the stated Picard hypothesis. `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied) (explicitly leaves the α≠0 descent unchecked); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

**Primary source:** Stacks Project, Proposition 10.83.3 (finite projective descent): [source](https://stacks.math.columbia.edu/tag/058Q); the remaining matrix-kernel argument is our C8.

### SC115 — Determinant one is stronger than projective linearity

**File/location:** cote 93, scan 073–074. **Short quote:** “G_0(f,g)”. **Kind:** own idea.

**Additional state:** check of a contextual correction.

Hua removes a determinant-one assertion from its report of later pages: over 𝔽₅[t]/t⁵, s=2t has Q=0 and unit derivative, but a representing homography has determinant 2d² and cannot have determinant 1. This elementary comparison confirms the need for a unit determinant in C7–C8; it does not establish what the unsupplied original glyphs say.

**Confidence:** High for the counterexample: 2 is a nonsquare in 𝔽₅ and coefficient comparison forces the matrix shape.

**Context comparison:** Restates and independently checks Hua IX’s determinant-one counterexample, without making a new claim about unsupplied manuscript glyphs. `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied) (determinant-one counterexample footnote); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

### SC116 — The limited comparison with Hoshi’s published invariants

**File/location:** cote 93, scan 073–074. **Short quote:** “G_0(f,g)”. **Kind:** own idea.

**Additional state:** literature comparison.

Hoshi’s 2024 paper §3 places the characteristic-2 level-two Sugiyama–Yasuda invariant in the sheaf of locally exact differentials, while §6 discusses the classical Schwarzian variant and its small-characteristic degeneracy. Those constructions cannot be identified with this ω²-valued integral G₀ solely from a shared level label; this comparison neither establishes nor refutes a priority claim.

**Confidence:** High for the cited definitions and target distinction; no novelty claim.

**Context comparison:** Rechecks Hua IX’s Hoshi comparison against the primary definitions; adds no priority claim. `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied) (literature footnote); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

**Primary source:** Y. Hoshi, A note on Schwarzian derivatives and Sugiyama–Yasuda locally exact differentials, Osaka Journal of Mathematics 61 (2024), §§3,6: [source](https://ir.library.osaka-u.ac.jp/repo/ouka/all/97634/ojm61_03_313.pdf).

### SC117 — The limited comparison with Frobenius-Ehresmann structures

**File/location:** cote 93, scan 073–074. **Short quote:** “G_0(f,g)”. **Kind:** own idea.

**Additional state:** literature comparison.

Wakabayashi’s 2021 paper develops Frobenius–Ehresmann structures and their relation with flat Cartan geometry over an algebraically closed field of odd characteristic, in its stated smooth and locally noetherian setting. That framework supplies context for higher levels, but it does not directly verify the integral third-jet calculation or our characteristic-2 assertion; a precise functorial identification would still be needed.

**Confidence:** High for the source’s stated scope; low for any unstated equivalence with this G₀.

**Context comparison:** Rechecks Hua IX’s Wakabayashi comparison within the primary source’s stated scope; adds no claimed equivalence of invariants. `context/hua_project/93.modern.tex`, IX, “Le facteur 12” and “L’injectivité en caractéristique p” (pp. 120–123, later scans 121–124 not supplied) (literature footnote); `context/notes/RESULTS_STATE.md`: **Hua 93-integral-schwarzian-level-p2**, candidate, not settled.

**Primary source:** Y. Wakabayashi, Frobenius–Ehresmann structures and Cartan geometries in positive characteristic (2021), introduction and §1.7: [source](https://arxiv.org/pdf/2109.02826).

### SC118 — No p-curvature or Picard-Fuchs conclusion follows from this cluster alone

**File/location:** cote 93, scan 072–084. **Short quote:** “\operatorname{Conn\,proj}(X)”. **Kind:** own idea.

**Additional state:** context comparison.

These pages support a projective-connection and differential-invariant strand of S20, but this cluster specifies neither a Picard–Fuchs family nor a p-curvature computation. Earlier P05 and P06 are carried as background limits on such an inference, while P07–P09 describe additional comparison data that would be required; the present jet and descent checks do not re-prove or supersede those results.

**Confidence:** High for the evidentiary limit; no claim to resolve the larger programme.

**Context comparison:** Restates P05/P06’s evidentiary caution and qualifies the S20 planning hypothesis using this cluster’s actual contents. `context/same_cote_93/MPL_93_002-046_notes.md`, P05/P06/P07/P08/P09 (scan 036 and scans 023,038–046); `context/README.md`, S20; `context/notes/RESULTS_STATE.md`: **MPL_93_002-046 P05**, **P06**, **P07**, **P08**, **P09**, S20.

## Separate author-unverified and withdrawn list

“Author-unverified” here means that the supplied pages explicitly question, withdraw or announce the item without a proof; it does not claim knowledge of what the author may have checked elsewhere. Independent checks in this run are identified in the individual notes and do not erase the manuscript’s provisional status.

### Explicit doubts, questions, proposed repairs and cancellations

- **SC02**, scan 072: The proposed denominator restriction.
- **SC08**, scan 072–073: Opposite torsor-difference conventions.
- **SC12**, scan 072: The margin says e) may be omitted.
- **SC27**, scan 073: Can quadratic differentials be eliminated from the formulation?.
- **SC33**, scan 074: The explicit faux-question margin must remain visible.
- **SC40**, scan 075: The instruction to replace all functions by étale ones.
- **SC41**, scan 075: The asserted étale-to-all-forms epimorphism fails.
- **SC51**, scan 077: The author rejects the inverse-vector surjectivity.
- **SC52**, scan 077: Restriction to the nonvanishing étale locus.
- **SC54**, scan 077: Homogeneity is proposed as a condition of success.
- **SC58**, scan 078: The question mark after the affine group of G-m.
- **SC66**, scan 080: The inserted power repairs the type of ds.
- **SC68**, scan 080: The cancelled denominator in c-prime.
- **SC69**, scan 080: The rescaled difference has reversed order and a target issue.
- **SC73**, scan 080: The question about a constant multiple of a logarithmic differential.
- **SC74**, scan 080: The unfinished product at the foot of 080.
- **SC75**, scan 081: The first uniformization diagram is only partially specified.
- **SC76**, scan 081: The question between Sigma and the hatted tangent object.
- **SC77**, scan 081: The questioned downward map from U to D.
- **SC78**, scan 081: The questioned downward map from B to the hatted T-object.
- **SC79**, scan 081: The questioned downward map from V to D-prime.
- **SC80**, scan 081: The unfinished product of universal covers.
- **SC81**, scan 081: The path-class construction of B.
- **SC84**, scan 081: The trace-zero submatrix and the cancelled numerical matrix.
- **SC86**, scan 081: The isolated Omega and omega identification.
- **SC87**, scan 081: Inverting f plus its reciprocal.
- **SC89**, scan 081: The diagonal cancellation strokes on the draft.
- **SC91**, scan 082: The affine sign conflict is repeated in the table.
- **SC92**, scan 082: The missing star in the first powered quotient target.
- **SC93**, scan 082: A possible group-level meaning of the exceptional n-equals-zero arrow.
- **SC98**, scan 082: The first projective coefficient needs a quadratic differential factor.
- **SC99**, scan 082: The questioned vertical identity between the two omega-star targets.
- **SC101**, scan 082: The minus sign in beta-n and Hua’s differing reading.
- **SC105**, scan 082: The delta formula has coefficients minus one and five-fourths.
- **SC109**, scan 084: The deleted translation-quotient fragment.

Qualifications and coefficient revisions without an explicit nonverification mark are recorded separately as SC22, SC24, SC26, SC35, SC50 and SC103; they are not classified as self-flagged steps.

### Announced claims without a proof on the supplied sheet

- **Scan 072:** SC01, SC03, SC04, SC05, SC06, SC07, SC09, SC10, SC11.
- **Scan 073:** SC13, SC15, SC16, SC17, SC18, SC19, SC20, SC21, SC22, SC24, SC25, SC26.
- **Scan 074:** SC29, SC30, SC31, SC32, SC34, SC35.
- **Scan 075:** SC36, SC37, SC38, SC39, SC42.
- **Scan 076:** SC43, SC44, SC45, SC47.
- **Scan 077:** SC48, SC49, SC50.
- **Scan 078:** SC56, SC57, SC59.
- **Scan 080:** SC60, SC61, SC62, SC64, SC65, SC67, SC70, SC71, SC72.
- **Scan 081:** SC81, SC82, SC83, SC84, SC88.
- **Scan 082:** SC90, SC94, SC95, SC96, SC100, SC102, SC104, SC106.
- **Scan 084:** SC107, SC108.

### Context-only extensions requiring a separate provenance label

- **SC110–SC115:** the later p/p² discussion, kernel calculation, monic-model rigidity, arbitrary-α descent and determinant normalization are comparisons with Hua’s report of later unsupplied pages. They are not explicit claims of scans 072–074.
- **SC06, SC12, SC13, SC17, SC19, SC27–SC29, SC32–SC35:** the full classifications and universal-recipient assertions remain unproved in this run even though the displayed invariant and several consequences were checked.
- **SC75–SC81, SC86, SC93:** the questioned or incomplete diagrams still lack enough definitions for a theorem-level interpretation; each explicit real-analytic question has its own note.
- **SC116–SC118:** the literature comparisons and S20 boundary do not assert novelty, a Picard–Fuchs realization, or zero/nilpotent p-curvature.

## Primary-source register and actual reading scope

1. **Dumas**, *Complex Projective Structures* (2009), §§3.1–3.2, [source](https://arxiv.org/pdf/0902.1951). Read the Schwarzian chain rule, projective-coordinate classification and local second-order ODE construction; these give a conventional reference for C3. Our normalization and the integral computations are independently displayed in C1–C5.
2. **Hoshi**, *A note on Schwarzian derivatives and Sugiyama–Yasuda locally exact differentials* (2024), §§3 and 6, [source](https://ir.library.osaka-u.ac.jp/repo/ouka/all/97634/ojm61_03_313.pdf). Read the definitions/targets and the characteristic restrictions used in SC116; no claim to have identified all historical predecessors.
3. **Wakabayashi**, *Frobenius–Ehresmann structures and Cartan geometries in positive characteristic* (2021), introduction and §1.7, [source](https://arxiv.org/pdf/2109.02826). Read the odd-characteristic setup and the structural comparison used in SC117, not a proof of the integral G₀ formula.
4. **Stacks Project**, Proposition 10.83.3, [source](https://stacks.math.columbia.edu/tag/058Q). Read the finite-projective-descent statement and its proof; this is the one external descent input of C8, which the root also opened and checked.
5. **Stacks Project**, Lemma 53.5.2, [source](https://stacks.math.columbia.edu/tag/0B5B). Read Riemann–Roch/duality for the conditional genus-count inference in SC85. The manuscript’s intended identification remains uncertain.

No extended quotations from these primary sources were used. The per-source discussion is deliberately limited; long calculations above belong to our independent proofs or to the user-supplied manuscript/context. A preliminary Ovsienko–Tabachnikov overview and Stacks module-descent page were also consulted but are not needed as cited inputs here. Hua’s reported Lean checks were not run, and no proof-assistant certification is claimed for this run.
