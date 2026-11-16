# Fourier context comparison — research phase only

Prepared after the root froze the transcription at 2026-11-16 19:18:43 UTC. No current page, source image, or transcript record was edited or visually reinterpreted for this comparison. The source of the present package is the frozen `MPL_57_271-315_transcription.tex`; the source of the earlier witness is the supplied `context/MPL_16+47+54+44_transcription.tex`, not its unavailable manuscript images.

## Evidence status and relevant register IDs

`context/README.md` identifies the earlier transcription and research notes as not second-passed, hence claims. `context/notes/RESULTS_STATE.md` gives **WG2 §2.4 #4** and **WG2 §1.1 #3** the status “question or plan item of the war game (round 2; unchecked)”; the former asks exactly for a second witness of cote 47 with the compatibility check done. The register does not supply a reviewed result settling that Fourier question, and the unrelated reviewed GT/CM results must not be used as evidence for it.

## Exact earlier-witness locator

In `context/MPL_16+47+54+44_transcription.tex`, cote 47 occupies the text from `\cotefile{47}` through the end of scan 11 (file lines 2050–2572). The relevant progression is:

| Earlier witness | Exact object or phrase in supplied transcript | What it establishes as manuscript evidence |
|---|---|---|
| 47:3, opening proposition | `\Phi_\mathcal L(F)=\mathbf R\operatorname{pr}_{2*}(\mathbf L\operatorname{pr}_1^*(F)\otimes\mathcal L)`; “transforme produit de Pontryagin” | A proposed transform, with a proof reducing to the universal Weil bundle and taking convolution to tensor product. |
| 47:4–5, inversion statement | The composite is revised from the identity to inversion with `\tau_A[-n]`; `\tau_A\simeq\Lambda^n t_A\simeq\Lambda^n t_B` | The determinant line and shift are part of the corrected statement; an older identity target remains in the proof. |
| 47:6, Lemma 1 | `\mathbf Rp_*(W)\simeq e_*(\tau_{B^*}[-n])` | The claimed canonical direct-image calculation needed for inversion. |
| 47:7, Lemma 2 | “Nous allons ici admettre le lemme 2” | Vanishing of cohomology of a nontrivial algebraically trivial line bundle is explicitly admitted here. |
| 47:7, lower half | The comparison map to `e_*(\mathcal O_S)\otimes_S\tau_{B^*}[-n]`, induced by the top-cohomology identification with `\Lambda^n t_{B^*}` | A particular canonical map is constructed, rather than only an abstract comparison of two objects. |
| 47:8, first paragraph | At `b=e(s)`, after derived fibre pullback, “à faire une vérification de compatibilité.....” | The unit-section compatibility check is explicitly left unfinished. |
| 47:8–9, remark 2 | `\det^*\circ\Phi_\mathcal L`; a map `\operatorname{Pic}^\delta_{A/S}\to\operatorname{Pic}^{-\delta'}_{B/S}` | A separate Picard/Néron–Severi component calculation, not completion of the preceding comparison map. |
| 47:11, remark 5 | For an automorphism `u`, the contragredient `u'` and “par transport de structure” | A formal equivariance assertion, not the unit-section verification. |

The earlier notes’ **F7** (`context/MPL_16+47+54+44_notes.md`, lines 3279–3283) explicitly call their discussion an “Editorial proof plan”; **F8** (lines 3285–3295) computes the exterior-power cohomology of a derived restriction and explicitly disclaims completing compatibility of the actual map. **F4–F5** (lines 3253–3271) discuss literature and determinant twists but remain part of the supplied unreviewed return; those publications have not been independently reopened here.

## Proposed notes for integration (one item each)

### FCTX-01 — Bounded negative answer to the carry-question

**Current source:** 57:271–315, with the potentially misleading match at 57:310, footer. **Kind:** unpursued implication / documentary comparison. **Bears on:** WG2 §2.4 #4 (unchecked plan question), WG2 §1.1 #3 (unchecked plan question).

No second witness of the cote 47 Fourier argument, and no completion of its canonical-map check, is identified in this package: the explicit “Compatibilité aux spécialisations ???” on 57:310 belongs to the Picard question list. The supplied earlier witness still ends the unit-section reduction with “à faire une vérification de compatibilité.....” at 47:8 (`context/MPL_16+47+54+44_transcription.tex`), and its accompanying notes F7–F8 explicitly leave that actual-map check open. This is a negative answer for these 43 scans, not a claim about the rest of cote 57 or the archive.

**Context search:** `Fourier|Pontryagin|convolution|compatibil`; exact 47:7–8 passage read. The present frozen transcript has no occurrence of Fourier, Pontryagin or convolution; the noun “Compatibilité” occurs at 57:310, while “compatible” elsewhere concerns descent or specialization.

### FCTX-02 — The specific missing check must remain specific

**Current source:** 57:294, 297 (first-order Picard/cohomology diagrams); earlier comparator 47:6–8. **Kind:** unpursued implication / boundary of the comparison. **Bears on:** WG2 §2.4 #4 (unchecked plan question).

The first-order diagrams of 57:294 and 57:297 concern Picard existence or flatness, cohomology maps and tangent factors; they do not display the morphism `\mathbf Rp_*(W)\to e_*(\mathcal O_S)\otimes\tau_{B^*}[-n]` whose derived fibre at the unit remains to be checked in 47:7–8. The earlier notes F7–F8 distinguish the cohomology dimensions/exterior powers from compatibility of this particular map, and the present package supplies no missing identification between those two claims. The two sorts of calculation are thematically related, but they are not interchangeable evidence.

**Context search:** `mapping-cylindres|compatibilité|tangent|Lambda|F7|F8`; compared with current scans 294 and 297 as frozen text.

### FCTX-03 — Relative Picard foundations, not a duplicate Fourier proof

**Current source:** 57:275–277, 279–281, 314–315. **Kind:** unpursued implication. **Bears on:** WG2 §1.1 #3 and WG2 §2.4 #4 (both unchecked plan questions).

The repeated descent and representability conditions in 57:275–281 and the question “Éliminer l’hyp. projective” on 57:314 supply foundational material relevant to using relative Picard objects. The earlier Fourier proposition on 47:3 assumes an abelian scheme and passes from a relatively algebraically trivial rigidified bundle to its classifying map into the dual abelian scheme, while 47:8–9 subsequently works with Picard and Néron–Severi components (`context/MPL_16+47+54+44_transcription.tex`). These pages therefore add a different level of the programme—conditions on the representing objects and their components—without restating the Fourier transform or settling its compatibility check.

**Context search:** `Pic|NS|alg. équivalent|dualité|faisceau de Weil|foncteur`; earlier 47:3 and 47:8–9 read against current definitions. Do not silently equate the numerically trivial `Pic^\tau` of 57:275 with every occurrence of an algebraically trivial component in 47.

### FCTX-04 — Equivariance is a concrete bridge

**Current source:** 57:284–286. **Kind:** own idea. **Confidence:** medium, because the same dual-action mechanism is explicitly named but no transform is applied to the quotient family. **Bears on:** WG2 §2.4 #4 (unchecked plan question).

The action on the dual abelian scheme in 57:284 is defined by “transport de structure,” and 57:286 uses the fixed part of its Picard object. This can be compared with 47:11, remark 5, where an automorphism and its contragredient are said to intertwine the Fourier functor “par transport de structure” (`context/MPL_16+47+54+44_transcription.tex`). An equivariant-kernel comparison on the quotient construction is a concrete follow-up, but neither passage supplies the descent/coherence argument that would turn it into a transform on the quotient, and it does not fill the unit-section gap of 47:8.

**Context search:** `transport de structure|contragrédient|autom.|Gamma`; exact source 47:11, remark 5; contextual notes’ last 47:11 items and F2/F20 inspected as leads.

### FCTX-05 — The Picard product formula and the kernel viewpoint

**Current source:** 57:283–284, especially the pointed-Hom term in the product formula. **Kind:** unpursued implication. **Bears on:** WG2 §1.1 #3 (unchecked plan question).

The product formula on 57:283 has a pointed-Hom factor and 57:284 identifies a relative Picard contribution through equivariant morphisms into the dual abelian scheme. The earlier universal reduction in 47:3 likewise classifies a line bundle on a product by a morphism into the dual (`context/MPL_16+47+54+44_transcription.tex`), so this package supplies related line-bundle classification machinery. Its doubtful `\tau|0` superscript on 57:283 remains a reading limitation; the comparison cannot be used to repair it after the freeze.

**Context search:** `pointé|produit|A\times|X\longrightarrow B|faisceau de Weil`; comparator 47:3, final paragraph.

### FCTX-06 — Specialization pathologies delimit a proposed extension

**Current source:** 57:285–288, 310–311. **Kind:** own idea. **Confidence:** medium, because the manuscript itself singles out nonflat fixed parts and specialization failure. **Bears on:** WG2 §1.1 #3 and WG2 §2.4 #4 (unchecked plan questions).

The explicit warning “la formation de Pic variété n’est pas compatible avec la spécialisation” on 57:288, together with the Igusa calculation on 57:285 and the open flatness questions on 57:310–311, gives test cases for any attempted extension of the abelian-scheme Fourier framework to more general relative Picard objects. The earlier Fourier proposition and inversion argument on 47:3–8 begin with abelian schemes; their relative hypotheses cannot simply be replaced by the existence of a fibrewise Picard variety. This is a proposed stress test of a generalization, not a counterexample to the earlier abelian-scheme statement.

**Context search:** `plat|schéma abélien|changement de base|special|spécial`; earlier 47:3–8 and notes F1/F4 compared as supplied claims.

### FCTX-07 — Determinant lines are not interchangeable with tangent bundles

**Current source:** 57:287–288; earlier comparator 47:5–7. **Kind:** unpursued implication. **Bears on:** WG2 §2.4 #4 (unchecked plan question).

The present difference-of-dimensions formula on 57:287 keeps `t_{A'}` separate from `(t_A)'`, and 57:288 seeks failures of symmetry and continuity. The earlier corrected inversion formula uses the determinant identification `\Lambda^n t_A\simeq\Lambda^n t_B` on 47:5–7, not an identification of full tangent bundles (`context/MPL_16+47+54+44_transcription.tex`; the earlier notes F4 make the same distinction as a claimed literature comparison). Thus this package makes the distinction useful to retain when organizing the two arguments, but does not contradict or prove the determinant-line assertion.

**Context search:** `tau_A|Lambda|tangent|determinant|t_B`; earlier 47:5–7 and notes F4 read.

### FCTX-08 — A symbol match in reused typing is not a witness

**Current source:** 57:312, reused typed page 20, numbered remark 3 and Proposition 3. **Kind:** reading question / documentary comparison. **Bears on:** WG2 §2.4 #4 (unchecked plan question).

The `\Phi` and `\Phi'` on 57:312 are explicitly “forme bilinéaire (resp. sesquilinéaire)” under extension of scalars, whereas `\Phi_\mathcal L` on 47:3 is a derived functor defined using the Weil/Poincaré kernel. The shared Greek letter and nearby tensor products therefore do not identify the reused typed leaf as a Fourier-transform draft. No chronology of the two texts follows from their presence in the supplied folders.

**Context search:** `Phi|sesquilinéaire|forme bilinéaire|catégories triangulées`; current 312 and earlier 47:3 read.

## Not established by this comparison

- No claim is made that the gap in 47:8 is mathematically unfillable or unresolved in the literature.
- No earlier source image was opened, and no supplied earlier transcription reading was upgraded to a reviewed reading.
- No completion of the map in 47:7–8 is inferred from the earlier notes’ cited modern results; these are leads within an unreviewed return.
- No historical priority or date ordering is inferred for undated handwritten material.
- No change is proposed to a frozen transcription reading. The `Pic^{\tau|0}` issue on 57:283 belongs in the research notes if the comparison motivates further inspection.
