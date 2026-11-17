# Research notes — MPL 64, scans 078–115

## 1. Findings, evidence and limits

**The supplied pages do not work out the announced modular cusp. They give a precise smooth moduli problem with Legendre–Jacobi pinning, finite groups of changes of pinning, and a substantial algebraic Weierstrass calculation.** The most concrete B5 connection is the order-twelve central extension in scans 090–092, which matches the abstract group in the supplied Longue Marche discussion of a normal complement in Γ(2); identifying the associated families and monodromy still requires work. The S20 hypothesis receives no explicit manuscript confirmation here, although the family allows a concrete, conventional Picard–Fuchs/Cartier comparison that we compute separately and label as our own addition.

These notes were written after the main transcriber had personally read all 114 supplied images, completed the page-by-page transcription and a second visual audit of all 38 scans, and frozen the 38 page files plus the combined transcription at **2026-11-17 23:01:38 UTC**. Both context READMEs and the full supplied `notes/RESULTS_STATE.md` were read after the freeze; the full Hua modernization was read for research. Post-freeze research was divided among mathematical reviewers, but no image reading, transcription or image audit was delegated. Mathematical diagnoses below do not amend the frozen readings.

| Requested question | Finding within this range | Decisive evidence and limit |
|---|---|---|
| Place at infinity announced in cote 149, scans 099–101? | **Not constructed in scans 078–115.** | The parameter lies in the smooth open `U_{0,3}` at 080 and 085–086; 109 assumes nonzero discriminant. The infinity at 109 and 114 is the image of the origin on the quotient of an individual elliptic curve. No degeneration or inertia calculation accompanies it; B5-01. |
| Congruence levels and B5? | **Explicit level 2; relative level 4 announced; a finite central extension.** | 085–086 (35)–(39), 090–092 (48)–(54), and the unfinished task at 093. The extension matches the supplied LM scan 529 discussion, conditional on that context's claims; no arbitrary-level theorem follows; B5-02 and B5-03. |
| Gauss–Manin, Cartier, projective connections and p-curvature? | **No explicit identification on these pages.** | `Θ_δ` differentiates on an elliptic fibre; a connection differentiates in the parameter. RC01 separates the objects; RC13 gives a checked mathematical bridge beyond the manuscript. |
| Important mathematical qualifications? | **A tensor-square error, degree-dependent derivative symbols, and a false unrestricted characteristic-p kernel; later formulas often check under precise conventions.** | RC06 and ALG01–ALG05. The monic cubic admits a consistent rescaling. The repeated-point determinant objection is already corrected by the author; ALG06. |

**Status discipline.** Register labels remain the earlier runs' claims unless their own entries report a scoped review. No status of LM2 C.d1/C.r1–C.r3, LM4 D.12, EXIT_TOWER E.24, LM4_SUCCESSOR B.38, LM6 A.22 or LM7_PUSH E.3 is changed. The register assigns no specifically settled result to recheck for this package. Its separate claims about GT, CM characters and full towers are not used to fill manuscript gaps.

**Citations.** `64/090 (49)` means cote 64, scan 090, formula (49), in `pages/MPL_64_078-115_64_scan090.tex`; opening, middle, closing and margin are approximate physical locators. Paths beginning `context/` refer to the supplied context ZIP, not recopied here. “Hua” means **Michel Hua's project, AI-produced modernised reading of cote 64**, `context/hua_project/64.modern.tex`; his page n corresponds to scan n+1, not the author's restarted page numbers. The register entry `64-legendre-pinning-moduli` is truncated; comparisons use the complete modernization as well as that credited lead.

Individual notes have one to four substantive sentences and compact source/search metadata. Full proofs and actual computations are preserved in `records/research_root.md`, `research_algebra.md`, `research_b5.md` and `research_connections.md`, using the same stable IDs. A documentary comparison is distinguished from a mathematical proof check in `CHECK_EVENTS.tsv`.

## 2. Moduli, pinnings and finite groups

### RC05 — A deleted asterisk matters

**64/078, opening, (16)–(17); kind: withdrawn in the same text / reading question.** Quote: “un isom.” followed by μ₄ with a deleted asterisk. **Search:** `Q_0`, `Aut`, `carré`; Hua, “L'épinglage de Legendre sur un corps,” lines 1364–1366. **Relationship:** contradicts this modernization detail; **result link:** Hua `64-legendre-pinning-moduli`.

The frozen reading distinguishes the two-element primitive-root torsor μ₄* from the four-element rotation group `Aut⁺(Q₀)≃μ₄`. Hua reintroduces the asterisk in the latter isomorphism, which fails by geometric fibre cardinalities. The refined statement **RC05-R** uses μ₄; it is the distinction preserved by the manuscript's deletion, not a correction to impose on the transcription.

### RC04 — A concrete square torsor, credited to Hua

**64/078, middle and end, (18)–(19); kind: unpursued implication.** Quote: `s_{i'}=i s_i`. **Search:** `Q_0`, `x^4`, `diagonales`; Hua, same subsection, footnote at lines 1371–1376. **Relationship:** adds a credited explicit example; **result link:** Hua `64-legendre-pinning-moduli`.

Hua's `Q₀={x⁴=−4}`, with `s_i=1−i`, is not written on this scan but checks directly: `i(1−i)=1+i`, `(1−i)⁴=−4`, and `−s_i²/2=i`. Over Z[1/2] it is a finite étale μ₄-torsor whose quotient by the central sign is μ₄*. This verifies Hua's example and explains the trivialization after choosing i at 086; no novelty is claimed.

### RC06 — A tensor power is missing in the twist formula

**64/080, lower half, (22)–(23), and 081 (27); kind: unproved claim.** Quote: `M^sharp⊗M^sharp≃M^b`. **Search:** `natural`, `flat`, `tensor`; Hua, “L'épinglage de Legendre sur une base ; le schéma de modules,” lines 1399–1415. **Relationship:** modernization restates the erroneous general formula; the next manuscript specialization has the intended degree; **register:** no exact settled entry.

Since the margin defines `M^sharp=M⊗O_S^sharp`, the corrected identity **RC06-R** is `(M^sharp)^{⊗2}≃(M^{⊗2})^b`. After trivializing the torsors, M=O(1) on P¹_C would otherwise force O(2)≃O(1); rank greater than one gives a rank contradiction as well. The O(2) at 081 (27) has the correct degree, so the error is local to the printed general formula rather than a failure of every subsequent tangent-square construction.

### R03 — Fixed orientation and all orientations give different torsors

**64/083, opening; 087–088, (40)–(44); kind: unpursued implication.** Quote: “Pour α fixé” and “torseur … des épinglages de Legendre.” **Search:** `épinglages de Legendre`, `torseur`, `alpha`; Hua, base/moduli subsection, lines 1424–1447. **Relationship:** restates and makes the distinction explicit; **result link:** Hua `64-legendre-pinning-moduli`.

For fixed α:μ₄*≃ω_J, the compatible pinnings form a μ₂-torsor, whereas allowing α to vary gives the μ₄-torsor L_{E/S}. Its quotient by μ₂ is μ₄*∧ω_J, the orientation datum. Calling both objects simply the pinning torsor loses the distinction needed for the group action and the universal curve.

### R04 — Legendre pinning alone does not rigidify every curve

**64/084–085, opening and continuation; kind: unproved claim.** Quote: “n'est pas rigide” and “exceptionnelle hexagonale.” **Search:** `rigide`, `hexagonal`, `automorphismes`; Hua, base/moduli subsection, lines 1449–1461. **Relationship:** restates the residual even-permutation stabilizer; **result link:** LM4 D.12, scope comparison only.

An automorphism preserving `(J,t,α)` must be an even permutation of J fixing t, so a nontrivial stabilizer comes from the cyclic order-three subgroup. This is compatible with 079's rigidity statement because that statement already concerns the combined Legendre–Jacobi structure. These geometric stabilizers do not classify torsion in full profinite GT₀ or reverse the D.29 qualification reported under LM4 D.12.

### R05 / RC03 — The fine moduli assertion and its extra datum

**64/082–086, (31)–(39); kind: unproved claim.** Quote: “Pour éliminer les autom.” and “représentable par le schéma.” **Search:** `Jacobi`, `schéma de modules`, `64-legendre-pinning-moduli`; Hua, the two Legendre subsections; `RESULTS_STATE.md`, Hua finding. **Relationship:** supports and sharpens the credited finding; **limit:** rigidity checked, complete reconstruction not supplied here.

Adding the Jacobi ordering of the three nonzero two-torsion points leaves only the level-two automorphisms ±1, and the tangent-line pinning kills the minus sign because 2 is invertible [Conrad, Proposition 2.1]. The manuscript asserts the fine scheme U_{0,3}×μ₄*, with the universal tangent line at 086. The pinning is an isomorphism to a specified twisted line, not an unspecified tangent vector, and the root-of-minus-one datum cannot be dropped. Hua's finding is supported as a manuscript assertion, while 083's request for construction prevents treating these pages alone as a complete proof or novelty certificate.

### R06 — A nonsplit central extension of order twelve

**64/090, (48)–(50); kind: unpursued implication.** Quote: “une extension de D₃ … par … {±1}.” **Search:** `produit fibré`, `extension centrale`, `dicyclique`; Hua, base/moduli subsection, lines 1483–1497; `LM_140-2_notes.md`, LM_P053 S09, scan 529. **Relationship:** restates the abstract group, adds a local verification; **result links:** LM4 D.12, B5-03.

After choosing i, the fibre product is C₃⋊C₄, with generators r³=s⁴=1 and srs⁻¹=r⁻¹. Every lift of a transposition has order four, so the central extension of S₃ by C₂ does not split. Exact enumeration confirms twelve elements and a centre of order two, without identifying this finite group with a full congruence or profinite group.

### R07 — The inserted abelianization is correct

**64/092, final insertion, (54); kind: unproved claim, independently checked.** Quote: `D'_{3,ab}≃μ₄`. **Search:** `abélianisé`, `chi_4`, `caractère canonique`; Hua, base/moduli subsection, lines 1487–1493; LM_P053 S09. **Relationship:** restates and checks; **register:** no separate settled abelianization row.

The commutator subgroup is A₃×{0}: conjugation by a transposition lift inverts a three-cycle and produces a generator as a commutator. The second projection therefore induces the claimed abelianization C₄. This verifies the inserted assertion rather than merely recognizing a group name.

### R08 — The line retains a central sign lost on the base

**64/089–092, (47), (51)–(54); kind: unpursued implication.** Quote: “le caractère mixte” and `T_{g,λ}ξ=λ(g,λ).ξ`. **Search:** `tautologique`, `caractère`, `scalaire`; Hua, base/moduli subsection, lines 1499–1509; `LM2_CONGRUENCE_ROWS.md` C.r1–C.r3. **Relationship:** adds a finite illustration of the context's distinction between kinds of action.

The central element (1,−1) acts trivially on the parameter scheme and by minus one on the indicated line. Squaring its character gives λ², and the tangent multiplier λ²sgn(g) becomes one on D'₃, so the restriction is coherent. This does not recover the arithmetic multiplier of LM2 C.r2: D'₃→μ₄ has a different source and target from an outer congruence action or a character into Ẑ×.

### RC10a — Left and right actions need a stated convention

**64/089, first paragraph; kind: reading question.** Quote: inserted “à g.” **Search:** `action à droite`, `action à gauche`, `opère`; Hua, base/moduli subsection, lines 1478–1480. **Relationship:** differs from the right-action wording; **result link:** Hua `64-legendre-pinning-moduli`.

The frozen text records a left action, while Hua says the product group acts on the right. Inversion can convert one convention into the other, but the conversion must be stated before comparing characters or composition formulas. This is a convention question, not a reason to reverse an action silently.

### R09 — Exceptional parameters and the hexagonal stabilizer

**64/084–085; kind: unpursued implication.** Quote: “t=ρ(t)” and “hexagonale.” **Search:** `1728`, `hexagonal`, `points fixes`; `LM_140-3_notes.md`, second-pass S4 for scan 009; Hua, base/moduli subsection. **Relationship:** restates the known parameter calculation and applies it to the pinning; **result link:** LM4 D.12, limited geometric evidence.

In a chosen standard Legendre coordinate, an order-three permutation acts by λ↦1/(1−λ) and fixes λ²−λ+1=0, giving the two j=0 parameters when the characteristic is not 2 or 3. The order-two fixed parameters are −1,2,1/2, where j=1728; the formula and ramification picture already occur in the supplied LM scan 009 notes. Our exact substitutions check that comparison and distinguish the residual order-three Legendre-pinned stabilizer from the unpinned automorphism orders 2,4,6 [Milne, IV.7.13].

### R10 — Characteristic three remains in the base

**64/080, base; 084–085, exceptional locus; kind: own idea. Confidence: high for the explicit calculation, because the fixed equation and actions are exact.** **Search:** `caractéristique 3`, `hexagonal`, `points fixes`; Hua, base/moduli subsection; `LM_140-2_notes.md`, notes on scan 542 and meeting special sections. **Relationship:** adds a local refinement; **result links:** MPL_93 E14/E16 only as unavailable comparison targets.

In characteristic three, λ²−λ+1=(λ+1)², so the order-three fixed locus is nonreduced and the harmonic parameters coalesce at λ=−1. All six transformations fix this geometric parameter, with full lifted stabilizer of order twelve; the constant order-three group is still étale. The model y²=x³−x checks the group using x↦x+a for a∈F₃ and (x,y)↦(−x,iy). This does not identify the deformation orders in the missing cote 93 notes or prove a Cartier or p-curvature claim.

### R11 — Universality is relative to fixed branch and orientation data

**64/094–095, (55)–(57), margin; kind: unproved claim.** Quote: “la courbe elliptique universelle, correspondant à J,t.” **Search:** `courbe standard`, `universelle`, `Kummer`, `T_0`; Hua, “La courbe standard E_α,” lines 1521–1542. **Relationship:** restates with a proof boundary; **result link:** Hua `64-legendre-pinning-moduli`.

Once a square root T₀ of T_{Σ,t} is fixed, other square roots form the groupoid of μ₂-torsors by (55). The torsor of square-compatible isomorphisms and its contracted-product inverse check this directly. Identifying those roots with elliptic curves is the manuscript's reconstruction assertion, and “universal” here means universal for fixed `(J,t,α)`, not already extended across a modular cusp.

### R13 — Naïve and twisted conventions agree after choosing i

**64/095 closing–096 opening; kind: unpursued implication.** Quote: “ép. de Legendre ‘naïf’” and “Les deux pts de vue sont équivalents.” **Search:** `naïf`, `Legendre`, `sqrt{-1}`; Hua, “La courbe standard E_α.” **Relationship:** restates the base-change qualification; **result link:** Hua `64-legendre-pinning-moduli`.

An orientation ω∈ω_J and an identification α:μ₄*≃ω_J become interchangeable after a section i of μ₄* is chosen. This explains the change to Z[1/2,i] without identifying the two conventions over the original absolute base. A later descent or monodromy comparison must remember that cyclotomic twist.

### R14 — Choosing i is not a CM condition

**64/090–096, direct pinnings; kind: unpursued implication.** Quote: “avec un choix fixé de i=√−1.” **Search:** `LM7_PUSH E.3`, `LM6 A.22`, `CM`, `1728`; corresponding `RESULTS_STATE.md` entries. **Relationship:** differs from the required CM-image statement and adds a scope limit.

The root i is chosen for every parameter, while j=1728 singles out special parameters. The common occurrence of Q(i) cannot construct an element of the CM coset in LM7_PUSH E.3 or the procyclic object of LM6 A.22. Both remain their supplied open claims, with no inference from the finite pinning character to their full profinite arithmetic images.

### R12 — Linear equations leave the quadratic scale unfinished

**64/098–100, (71)–(78), especially the last line of 100; kind: self-flagged.** Quote: “Il reste ensuite à exprimer (73).” **Search:** `Explicitation calculatoire`, `forme linéaire`, `73`; Hua, that subsection, lines 1588–1599. **Relationship:** supports incompleteness and adds an independence check; **register:** none.

The equations Σψ_i=0 and Σc_iψ_i=0 place ψ in F_t but allow arbitrary scalar multiples of a nonzero solution. The quadratic relation (73) imposes a separate scale; orientation and inverse-homogeneity transport one valid instance to the others without furnishing its initial value. The abstract lemma appears at 099, while the complete requested coordinate expression is explicitly left unfinished at 100.

### R16 — The ambient basis in the coordinate description

**64/096, left margin by (60), and 100, left margin; kind: reading question.** Quote: “base can.” **Search:** `base canonique`, `k^J`, `V_J`; Hua, “Explicitation calculatoire,” lines 1546–1550,1587–1593. **Relationship:** differs at an uncertain local label, agrees with the later explicit ambient basis; **register:** none.

The frozen 096 margin marks V_J uncertain in a phrase about the indexed basis (e_i), whereas the three standard vectors belong naturally to k^J and scan 100 explicitly names that space. Hua uses the latter convention throughout. This supplies an alternative to investigate, but does not decide the ink or remove the frozen doubt.

### RC10b — Jacobi replaces Torelli, but the old name survives

**64/085 opening and 086 opening; kind: withdrawn in the same text / reading question.** Quote: deleted “Torelli,” inserted “Jacobi”; later “Legendre-Torelli.” **Search:** `Torelli`, `Jacobi`, `Legendre`; Hua, base/moduli subsection, footnote at lines 1465–1467. **Relationship:** adds the exact correction and a surviving terminology difference.

The author replaces Torelli by Jacobi at 085 in the combined level-two structure, yet the frozen reading retains “Legendre-Torelli” at 086. Hua reports that second name as unread. Its later complex Torelli discussion is outside this range and cannot normalize these two occurrences retrospectively.

### RC10c — The twist glyph remains unidentified

**64/080–097, recurring superscript; kind: reading question.** **Search:** `natural`, `zigzag`, `éclair`; Hua, base/moduli subsection, footnote at lines 1405–1406. **Relationship:** corroborates uncertainty, not a decipherment; **register:** none.

The transcription consistently marks the sharp-like superscript uncertain. Hua chooses `natural` but explicitly calls the original zigzag unidentified. This supplies no reason to remove the doubt or replace the glyph after the freeze.

### RC10d — The parameter t needs a branch-order convention

**64/079–080, marked triple; 109 (37); kind: reading question.** **Search:** `lambda`, `Legendre`, `t`, `0,1`; Hua, “L'épinglage de Legendre sur un corps,” lines 1384–1393. **Relationship:** qualifies Hua's λ=t identification; **result link:** B5 family comparison.

The current coordinates label the nonzero two-torsion images by 0,1,∞ and put the origin at t, while standard Legendre coordinates put the origin at infinity. The map x=(1−t)z/(z−t) preserves the first two labels and gives λ=1−t; x=t(z−1)/(z−t) gives λ=t while exchanging them. Hua's equality is an available relabelling convention, not a literal identity established by these scans.
