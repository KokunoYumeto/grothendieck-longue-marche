# Research memo: local averaging, duality, functional equations

Research only, prepared after the transcription was frozen at 2026-11-15 22:48:34 UTC. No cote60 image was viewed for this memo and no transcription or doubt file was edited. Locators `60/NNN:Lx–y` refer to the delivered per-page file `pages/MPL_60_036-070_60_scanNNN.tex`; they are TeX lines, not reconstructed manuscript line numbers. The following are draft research items for integration, not a second transcription.

## Context searches and status discipline

The supplied context transcription is `MPL_16+47+54+44_transcription.tex` (abbreviated CT here); its notes are unreviewed leads. Searches for `inerti`, `unipoten`, `moyenn`, `fonction.*L`, `Frobenius`, `Artin`, `niveau`, `compact`, `infini`, `dual`, `polarisa`, `semi-simple`, `category of motives`, and `poids` were run in the supplied transcription and notes.

- CT16/048 explicitly mentions a natural dual and says that the twist is dropped for simplicity; CT16/049 discusses algebraic inverse maps and conditional semisimplicity of motives. These are genuine comparison points for duals, twists and semisimplicity, not earlier instances of the local averaging construction.
- CT16/018 proposes a duality principle for Lefschetz correspondence rings; CT16/023 treats cohomological/Brauer duality. CT54/002–005 treats cohomological duality for dual abelian varieties and Cartier duality. These differ in category, cohomology theory and support from the curve-boundary duality in60/049–061.
- CT44/002,008–009 asks for polarization/positivity of an autoduality. This provides a useful distinction between a pairing, positivity, and a bare weight statement, but does not establish the implication written on60/053.
- No earlier instance of the present inertia average, α/μ/λ construction, epsilon-sign reduction, or restricted rational involution problem was located in the supplied context transcription. Occurrences of weights in CT44/007 concern root-system terminology on reused typescript and are not weight-theoretic precedents.
- Relevant RESULTS_STATE entries are primarily **Hua, findings register, 60-inertia-average-duality** (AI-produced, conjecture/unsearched; a lead), and, for limited comparisons, **WG2 §2.4 #3**, **WG2 §2.3 #7**, **MPL_14_087-132 M09**, **MPL_14_002-044 M29a**, and **MPL_15_195-228+18_002-017 M03/P09/P14** (all planning guesses or first-pass leads in the supplied register). **WG H9** and **WG2 §2.3 #12** concern the separate positivity/height programme and receive no new proof here. The supplied **LM7 E.23** and **LM7_PUSH D.44** statements concern section problems/modular descent, not the present local averages: these pages do not settle or re-derive them.

## Draft items

### LF01 — Global semisimplification is rejected as a local construction

**Witness:** 60/037:L2. **Kind:** self-flagged / withdrawn approach. **Quote:** “Ceci n'est pas encore satisfaisant”; “ne commutent pas à l'extension … étale”.

The attempt to define factors by the global simple constituents is explicitly rejected because the construction need not commute with the stated étale change near x; scans039–047 replace it with a construction on the local decomposition group. This **adds** a locality criterion absent from CT16/049's conditional semisimplicity discussion, and it bears directly on Hua **60-inertia-average-duality**; the local and global semisimplifications should not be silently identified. A proof or counterexample to the precise étale statement must first specify the category and the allowed covers, since the current text records the objection rather than a worked example.

### LF02 — The stated coefficient hypothesis makes averaging exact

**Witness:** 60/039:L6;041:L4–12;043:L4–6;045:L6–19. **Kind:** unpursued implication. **Quote:** “car. 0”; “foncteur exact”.

For the finite group I/U the displayed idempotent N⁻¹Σg gives an elementary proof of exactness of invariants in characteristic zero, and the D-stable filtration of039 shows why this operation acts on classes even when U acts nontrivially and unipotently. This **differs from**, rather than proves, the semisimplicity programme in CT16/049 (RESULTS **WG2 §2.3 #7**, **MPL_14_087-132 M09**), and **adds** the required local construction to Hua **60-inertia-average-duality**. Deligne (1973, Theorem8.2, p.566) supplies a later precise quasi-unipotence statement in the local ℓ-adic Weil setting; it should not be retroactively used to remove the manuscript's stated hypothesis.

### LF03 — Averaging is not a tensor functor

**Witness:** 60/041:L8–10;043:L6. **Kind:** own idea. **Quote:** “Il induit un hom. … virtuel”.

**Confidence: high**, because if I=C₂ and ε is its nontrivial one-dimensional character over a characteristic-zero field, then εᴵ=0 but (ε⊗ε)ᴵ=1. Thus the additive map of representation groups supplied here is not generally a ring homomorphism or a fibre functor, even though it respects dual classes. This **differs from** CT16/049's proposed category of semisimple motives and limits any attempted connection to **WG2 §2.4 #3** or the Tate-character leads **M03/P14**; it supports Hua's additivity clause but not a stronger tensor claim.

### LF04 — Frobenius lift independence is proved by the filtration, not by naïve averaging of an arbitrary action

**Witness:** 60/045:L17–19;047:L2. **Kind:** unpursued implication. **Quote:** “cette valeur ne dépend pas du choix”.

For a fixed coset in D/U, the trace of any lift to D is the same because the graded factors have trivial U-action and traces add along the D-stable filtration; changing the lift of Frobenius from D/I then permutes the I/U terms in the finite average. This **adds** a concrete verification of Hua **60-inertia-average-duality**, with no direct earlier inertia calculation found in CT. It does not assert that U already acts trivially on E itself or that the actual invariant subspace Eᴵ is exact in E.

### LF05 — The notation Eη(x) changes its apparent role

**Witness:** 60/047:L8;051:L4,32,36. **Kind:** reading question. **Quote:** Eη(x)=Eη^natural(x), then αx=Eη^natural(x)−Eη(x).

Read literally with unchanged notation, the displayed definition on047 makes the later α identically zero, whereas051 explicitly says α is not additive; the likely intended second term on051 is the ordinary invariant stalk, but that is an interpretation rather than the frozen text. No corresponding notation was found in CT, so these pages **add** an unresolved internal naming issue to Hua **60-inertia-average-duality**. All deductions involving α below explicitly assume Eη(x)=Eηᴵ in051 and do not revise047.

### LF06 — Virtual duality does not provide a canonical derived object

**Witness:** 60/047:L12–14;049:L14,19–23;051:L29–36. **Kind:** reading question / unpursued implication. **Quote:** “faisceau virtuel”; cancelled “[2]”.

The constructed object is a class, and049 visibly cancels the even shift [2], which is invisible in a Grothendieck group; a derived-category isomorphism or a canonical complex is a stronger assertion not supplied here. This **differs from** CT54/002–005's duality constructions and qualifies Hua **60-inertia-average-duality**, whose visible register excerpt writes a Verdier-dual expression with [2]. Deligne (1973, §§10.5–10.7, pp.583–586) provides the later derived and local-inertia framework, with its shifts retained at the complex level.

### LF07 — The stated local additivity forces μ to vanish

**Witness:** 60/039:L6;041:L2–12;043:L6;051:L4–8,36. **Kind:** own idea / unpursued implication. **Quote:** “mais μx … l'est”.

**Confidence: high conditional on LF05's ordinary-invariant-stalk interpretation**, because the D-stable U-trivial filtration from039–043 has α=0 on every factor, hence μ=0 on every factor, and the asserted local additivity of μ forces μ(E)=0 in K₀(D/I) for every such E. This **adds** a short consequence not stated in the visible text and not found in CT, and materially qualifies any interpretation of Hua **60-inertia-average-duality** as predicting a nonzero local correction in this setting. It is a consequence of these premises, not a novelty claim, and the next item independently checks the cancellation by monodromy.

### LF08 — A Jordan block checks both the nonadditivity of α and cancellation of μ

**Witness:** 60/051:L4–8,36. **Kind:** own idea. **Quote:** “αx … n'est pas additif”.

**Confidence: high**, by the two-dimensional tame model with geometric Frobenius F=diag(Qx⁻¹,1), N(e₂)=e₁ and N(e₁)=0, where Qx=|k(x)|: E^natural=[Qℓ(1)]+[Qℓ], Eᴵ=[Qℓ(1)], α(E)=[Qℓ], α(E∨)=[Qℓ(−1)], and therefore μ(E)=0 although α(E) differs from the sum of its values on the two one-dimensional factors. More generally N:V→V(−1) is equivariant after taking the finite-inertia invariants of the Weil–Deligne representation, and its kernel/cokernel sequence gives [kerN](1)−[cokerN]=[V](1)−[V], which is the same cancellation. This **adds** a diagnostic example to Hua **60-inertia-average-duality** and **differs from** CT16/049's semisimple correspondence setting; Deligne's §§8.2 and10.7 are the later framework, not evidence that the manuscript itself executed this check.

### LF09 — Weight alone does not imply the written self-duality

**Witness:** 60/051:L38;053:L18–20. **Kind:** own idea / reading question. **Quote:** “Supposons E de poids …, donc”.

**Confidence: high**, because a rank-one finite-order character sending Frobenius to a primitive cube root ζ has weight0 while its dual has eigenvalue ζ⁻¹≠ζ, so purity alone does not give E∨≅E(ρ). Scan051 states the self-duality as an explicit conditional hypothesis, whereas053's “donc” needs an additional pairing or restriction on the meaning of weight. This **differs from** CT16/048's explicitly discussed duality and CT44/002,008–009's polarization questions (RESULTS **WG2 §2.4 #3**, **WG H9**, **WG2 §2.3 #12**), and those prior leads do not supply the missing pairing for this E.

### LF10 — The local denominator and twist disagree under the displayed convention

**Witness:** 60/053:L20,36–40;055:L8,16. **Kind:** reading question. **Quote:** q=p^(1+ρ); αx(E)∨−αx(E)(ρ+1).

Using the twist rule L_{E(ρ)}(t)=L_E(p⁻ρt) explicitly written on053, the μ-expression with twist ρ+1 leads to a denominator Lα(p⁻(ρ+1)t), whereas the frozen lower formula has p⁻ρt. The next page repeats that lower power, so this is a recurring formula/convention question rather than permission to supply an invisible +1. No earlier normalization of these local functions was found in CT; it **adds** a qualification to Hua **60-inertia-average-duality**, and must be settled before equating the manuscript's factors to a published epsilon convention.

### LF11 — The modified Euler characteristic has a precise conductor formula

**Witness:** 60/047:L14;055:L26;059:L2. **Kind:** own idea / unpursued implication. **Quote:** “Donner une formule genre … Ogg”.

**Confidence: high under the ordinary curve and ℓ≠p hypotheses**, since applying the Grothendieck–Ogg–Shafarevich formula to i!E and adding the point terms in047 gives χ(X̄,E^natural)=r(2−2g)−Σx deg(x)[Swx(E)+r−dim E_x^natural] for a smooth proper geometrically connected X over a finite field. Consequently the modified local conductor equals the usual Artin conductor minus rank αx, and purely unipotent tame monodromy contributes zero to it. This **adds** a precise interpretation of055(b)/059 to Hua **60-inertia-average-duality**; CT's occurrences of Artin concern reused module/group-scheme texts, not this formula, while Raynaud (1966, Theorem1, p.133) and Laumon (1987, §§3.1.5.1–3, p.185) give the relevant published conductor frameworks.

### LF12 — Closed-point degree and determinant conventions need to be fixed

**Witness:** 60/047:L6–18;053:L11–14;057:L26–28. **Kind:** reading question. **Quote:** “générateur fx”; “invariant arithm.” on055.

For a closed point of degree d, the local factor in a global variable ordinarily uses tᵈ, while det(Frob on the induced representation) differs from det(Frob_x) by (−1)^((d−1)dimV); using det(−Frob) absorbs that latter discrepancy. The selected pages do not fully specify whether p, χx and δx already include these conventions, so their products should not be compared to a modern product formula by name alone. This **adds** a normalization question to Hua **60-inertia-average-duality** with no exact CT precursor; the nearby **M03/P09/P14** ledger leads likewise do not settle these local arithmetic conventions.

### LF13 — The squared determinant question is followed by a local product, not a sign determination

**Witness:** 60/053:L28–30;057:L4–21;059:L2. **Kind:** self-flagged / unpursued implication. **Quote:** “??”; “modulo un signe”.

The question δnatural²=q^χnatural on053 is followed on057 by δnatural²/q^χnatural=Πx δx²/q^χx, and059 expressly leaves the sign undetermined. Under LF07's hypotheses the local μ-classes vanish; if one also retains the self-duality and determinant conventions required for the displayed relation on057, that relation then makes the product1, but this extra deduction is not written in these pages. This **adds** a distinction between a squared relation and an actual epsilon sign to Hua **60-inertia-average-duality** and has no earlier functional-equation calculation in CT.

### LF14 — One intermediate equality on057 fails a formal consistency check

**Witness:** 60/057:L4,10,15,19,26,28. **Kind:** reading question. **Quote:** “d'où”.

Combining the first identity with δ(μx)=δx⁻²q^χx yields the normalized equation onL19, whileL15 instead has δnatural²q^(Σχx) on its right and does not follow from those two identities. The second equality onL26 also omits the preceding ±, althoughL28 restores ±, so no definite sign should be inferred from that middle step. These are **added** internal consistency questions for Hua **60-inertia-average-duality**, not silent corrections and not claims established by the CT leads.

### LF15 — Splitting an additive factor can conceal its cancellation

**Witness:** 60/055:L20–27. **Kind:** self-flagged / unpursued implication. **Quote:** “on en perd le caractère additif”; “Il vaut sans doute mieux”.

The author's warning is consistent with051: the separate α-pieces need not be additive even when their duality combination μ is, so a product decomposition should retain the exact-sequence cancellations. This **adds** a substantive caution to Hua **60-inertia-average-duality** and **differs from** CT16/049's desired categorical splitting. Laumon (1987, Remark3.1.5.7, p.187) gives a particularly close later comparison by distinguishing the additive ε₀ convention from a generally nonadditive ε convention; it is not an identification of either with λx here.

### LF16 — The local-to-global epsilon problem has later theorems with extra data

**Witness:** 60/055:L22–27;059:L2. **Kind:** unpursued implication. **Quote:** “c) Donner une formule”.

These pages formulate a local-to-global determinant problem and reach only a sign ambiguity; Laumon (1987, Theorem3.2.1.1, p.187) later proves a full product formula for constructible complexes on smooth projective connected curves, with local factors normalized by a meromorphic differential and a chosen additive character. Deligne (1973, Theorem9.3 and Proposition9.9, pp.575–580) treats compatible-system cases using local semisimplification, so chronology and hypotheses should remain explicit. This **adds** literature context to Hua **60-inertia-average-duality**; it neither promotes the supplied conjecture-labelled entry to a new theorem nor identifies the manuscript's εnatural without checking LF10/LF12.

### LF17 — Cohomology at infinity is a cone, with a grading question

**Witness:** 60/061:L2–26. **Kind:** unpursued implication / reading question. **Quote:** “Cohomologie à l'infini”; “au décalage d'une unité près”.

The two displayed triangles suggest the boundary cone of Rf!F→Rf*F and its alternative local-cohomology realization; with ordinary cohomological grading its long exact sequence advances from degree i to i+1. The frozen small exponent is i−1|i+1, so the grading convention or reading must be recorded as unsettled rather than repaired from the standard triangle. This **differs from** CT54/002–005's cohomological duality on abelian varieties and **adds** a boundary-support problem not directly represented by a matching RESULTS_STATE result; Deligne (1973, §10.6, p.583) is a published comparison for the !/* duality.

### LF18 — The involution condition is a cocycle equation

**Witness:** 60/063:L2–33. **Kind:** unpursued implication. **Quote:** “Faisons opérer le groupe … Z/2Z”.

For q∈K× and σ(t)=1/(qt), a nonzero L∈K(t) satisfies A=σ(L)/L and hence Aσ(A)=1; a constant c in σ(L′)=cL′ must satisfy c²=1. In characteristic different from2 this gives the two signs, whereas in characteristic2 they coincide. This **adds** an elementary cohomological formulation absent from CT; no specific registered theorem or open item in RESULTS_STATE concerns this normalization problem, and it does not bear on **LM7 E.23** or **LM7_PUSH D.44** merely because they also involve group cohomology.

### LF19 — Unrestricted Hilbert90 does not solve the lower-level problem

**Witness:** 60/063:L19–33;065:L7–11;067:L2–13. **Kind:** own idea. **Quote:** “solution triviale”; “niveau … inf.”.

**Confidence: high**, because over K with q∈K× and charK≠2 one has K(t)^σ=K(t+1/(qt)); for c=1 all unrestricted solutions are λ=R(t+1/(qt))/L, and for c=−1 they are λ=(t−1/(qt))R(t+1/(qt))/L, with R nonzero rational. This is the quadratic Hilbert90 situation, but065 explicitly excludes unrestricted trivialization and067 restricts the admissible factors, so vanishing of H¹(C₂,K(t)×) does not settle it. This **adds** a precise separation of the easy and constrained problems, with no direct CT or RESULTS_STATE analogue.

### LF20 — Formulate the restricted obstruction only after checking stability

**Witness:** 60/065:L13–27;067:L2–20;069:L4–9. **Kind:** own idea. **Quote:** “chaque Li et L′i a une équation fonctionnelle”.

**Confidence: medium**, because if the permitted lower-level functions form a σ-stable multiplicative subgroup H containing the relevant cocycle c/A, the remaining existence question is whether its class vanishes in H¹(C₂,H), and the displayed factorwise functional equations are exactly the sort of data needed to test that stability. The repeated factors, ambiguous primes, and n−ρ|n+ρ exponents in067–069 prevent treating a clean graded factorization as already supplied. This **adds** a testable reformulation beyond CT16/018's distinct graded correspondence-ring problem and beyond the broad **WG2 §2.4 #3** plan; no novelty or complete solution is asserted.

### LF21 — Fixed-point parity is a concrete test for a restricted normalization

**Witness:** 60/063:L17–33;065:L11;069:L12–19. **Kind:** own idea. **Quote:** “niveau … inf.”; “n=1”.

**Confidence: high for the stated algebraic test**, because at a fixed point a with a²=q⁻¹ over an algebraic closure in characteristic≠2, σ has derivative−1 and the limiting value of σ(f)/f is (−1)^ordₐ(f). Thus if the allowed corrections cannot change ordₐL at a top-level fixed point, the resulting constant sign must have that parity; differing required parities at the two fixed points obstruct that restricted choice. This **adds** a small-case test for067–069 absent from CT and from a directly matching RESULTS_STATE entry, not a proof that the manuscript's admissible group actually has such a restriction.

### LF22 — A coefficient field must be stated before half-weight normalization

**Witness:** 60/057:L26–28;065:L16–27. **Kind:** reading question. **Quote:** “puissances de p^(1/2)”.

The normalizations involving p^(χ/2) or p^(ρ/2) may require adjoining a square root to the coefficient field, and changing that choice changes signs when the exponent is odd. This **differs from** CT16/048's deliberate omission of twists for simplicity, and **adds** a concrete scalar convention to the weight/Tate leads **M03/P09/P14** without assuming their first-pass conclusions. It is another reason why the ± in057–059 should not be discarded.

## Assessment of the supplied Hua entry

The supplied RESULTS_STATE excerpt for **Hua, findings register, 60-inertia-average-duality** is itself truncated after a duality-expression continuation; only its visible clauses were assessed. Local averaging after a D-stable unipotent filtration, characteristic-zero exactness, local geometric application, and additivity at the virtual level are supported by039–051. Its [2] should be explained as a conventional even shift at the derived level, not substituted for the crossed shift in049 or promoted into a canonical derived object. Any claim that the written μ necessarily yields nonzero local correction factors requires qualification by LF05–LF08: under the ordinary invariant-stalk interpretation and the author's additivity assertion, μ vanishes. The excerpt is therefore useful as a lead, not an established independent result or proof of novelty.

## Primary literature checked, with exact scope

External statements in this memo are deliberately compact; the manuscript-specific examples and deductions above are our own algebraic checks. All source pages below were opened through web retrieval; no published text was used to change the frozen transcription.

1. **Deligne, P. (1973).** Les constantes des équations fonctionnelles des fonctions L. In P. Deligne & W. Kuijk (Eds.), *Modular functions of one variable II* (Lecture Notes in Mathematics, Vol.349, pp.501–597). Springer. https://doi.org/10.1007/BFb0066719 . Author-hosted PDF: https://publications.ias.edu/sites/default/files/Number20.pdf ; bibliographic landing page: https://publications.ias.edu/node/365 . Checked Theorem8.2 p.566 (Grothendieck's local monodromy statement), Theorem9.3 p.575 and Proposition9.9 p.580 (compatible systems and local semisimplification), §§10.5–10.8 pp.583–587 (duality, !/*, and the inertia complex). Tool refs: `turn4view0`, `turn11view3`, `turn26view1`, `turn27view0`. Editor names verified against Springer https://link.springer.com/book/10.1007/978-3-540-37855-6 and its front matter https://link.springer.com/content/pdf/bfm:978-3-540-37855-6/1 (`turn40view0`, `turn43view0`): the title/editor pages give Kuijk, while the preface signature gives Kuyk. The digitized front matter identifies the second corrected printing1986, first edition1973; the chapter PDF's last-page Laumon1984 postscript should not be treated as part of the original1973 state.

2. **Laumon, G. (1987).** Transformation de Fourier, constantes d'équations fonctionnelles et conjecture de Weil. *Publications Mathématiques de l'IHÉS, 65*, 131–210. https://doi.org/10.1007/BF02698937 . Primary PDF: https://www.numdam.org/item/PMIHES_1987__65__131_0.pdf . Checked §§3.1.1.3–5 p.179 (global functional equation), §§3.1.5.1–4 pp.185–186 (conductor and local constants), Remark3.1.5.7 and Theorem3.2.1.1 p.187 (additivity distinction and product formula); §§3.2.1.7–9 pp.188–189 distinguish older finite-monodromy/compatible-system cases. Tool refs: `turn1view0`, `turn5view0`, `turn11view1`, `turn26view0`.

3. **Raynaud, M. (1966).** Caractéristique d'Euler-Poincaré d'un faisceau et cohomologie des variétés abéliennes. In *Séminaire Bourbaki: Années1964/65 et1965/66, exposés277–312* (Exposé286, pp.129–147). Société mathématique de France. https://www.numdam.org/item/SB_1964-1966__9__129_0/ . PDF: https://www.numdam.org/item/SB_1964-1966__9__129_0.pdf . The talk is dated February1965, the archived publication1966; Theorem1 is onp.133, with proofpp.134–137, and the introduction explicitly credits the first part's then-unpublished results to Grothendieck. Tool refs: `turn14search2`, `turn15view0`, `turn16view0`. Its stated coefficients are constructible torsion sheaves prime to the characteristic; LF11 uses the usual ℓ-adic extension, also in Laumon's cited formulation, rather than pretending Raynaud's displayed theorem is word-for-word that version.

4. **Milne, J. S. (2022).** *Fields and Galois theory*. Kea Books. https://www.jmilne.org/math/Books/FT0.pdf . Author-issued book checked at Theorem5.23 pp.92–93 and Corollary5.25 p.93; the author page https://www.jmilne.org/math/CourseNotes/ft.html confirms the book citation and relation to course-note version5.10. This is an author textbook exposition, not the original historical proof, and is optional background because LF18–LF19 give the actual elementary verification needed here. Tool refs: `turn15view1`, `turn16view3`, `turn16view4`, `turn14search0`.

The exact formulas in scanned older PDFs are sometimes poorly represented by the web text extraction; the memo therefore cites the section and page while deriving the specific modern-normalization formulas explicitly rather than copying a garbled text layer. A full historical attribution of the restricted-level construction is not supplied or claimed.

## Follow-up: full Hua register access

A targeted web search for the exact ID `60-inertia-average-duality` and the public repository was attempted after this memo was drafted. The repository README was accessible and identified `src/content/findings.ts` as the register; the deployed `/findings/` page returned no readable text, and both the raw-file and GitHub blob URLs for that register returned `DisabledError`. Therefore the complete finding was not inspected, and the assessment above remains explicitly an assessment of the supplied RESULTS_STATE excerpt, not of unseen continuation clauses. Public repository consulted: https://github.com/Commutator-IO/grothendieck-project (tool ref `turn34view0`); attempted register URLs: https://raw.githubusercontent.com/Commutator-IO/grothendieck-project/main/src/content/findings.ts and https://github.com/Commutator-IO/grothendieck-project/blob/main/src/content/findings.ts .
