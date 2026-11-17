# Oda, Cartier, height-one groups, and Verschiebung: supporting research

Research performed only after the 2026-11-17 11:42:33 UTC transcription freeze. No manuscript image was opened and no page, combined transcription, JSON page record, inventory, or doubts file was edited. The supplied README and RESULTS_STATE were read first; the supplied printed Oda PDF was text-extracted for navigation, and printed pp. 122, 126 and 131 were rendered and visually checked. The report is research support for the main notes, not a replacement transcription or an independent historical witness of the manuscripts.

## Proposed individual notes

### OC01 — The injectivity question has a normal-case answer

**File/scan:** 46:020–021, logarithmic derivative and continuation. **Kind:** self-flagged. **Quote:** “Cet hom est-il injectif?” **Results-state:** no directly matching settled entry; thematic connection to **WG2 §1.1 #3**, not a solution of **WG2 §2.4 #4**.

The manuscript answers its question by taking a rational p-th root and using normality to make it regular; for a unit, the inverse root is likewise integral and regular, which gives the required local unit. Oda (1969, p. 126, immediately before Theorem 5.10) states precisely that the kernel of dlog on a normal scheme over a perfect field is the image of Frobenius on the multiplicative sheaf. This independently supports the injectivity step, while leaving the later surjectivity/regularity argument on scan 021 separate.

### OC02 — The fixed-form converse must keep its hypotheses

**File/scan:** 46:021, “D’après Cartier” through the final reduction. **Kind:** unproved claim. **Quote:** “on est ramené au cas où X est … régulier”. **Results-state:** no directly matching entry; **WG2 §1.1 #3** is a programme-level connection only.

Oda (1969, Definition 5.5(iii), pp. 121–122) identifies Cartier-fixed closed one-forms with locally logarithmic differentials of units when the local rings have p-bases, for example on a smooth scheme over a perfect field. His p. 125 expressly warns that Cartier on rational forms need not preserve regular forms on a nonsmooth normal scheme. Thus the supplied printed witness confirms the smooth local converse but does not justify this leaf’s reduction from normality to regularity; one must also distinguish ordinary Kähler differentials from reflexive differentials before using divisor-class examples.

### OC03 — The smooth proper Picard consequence

**File/scan:** 46:020–021. **Kind:** unpursued implication. **Quote:** “Détermination de … Pic(X)”. **Results-state:** bears on **WG2 §1.1 #3**; no direct settled register result is being rederived.

For smooth proper X over a perfect field, the manuscript’s global-units argument and Oda’s local Cartier criterion combine to identify Pic(X)[p] with the additive group of global closed one-forms fixed by Cartier. This is a precise smooth-case completion of the leaf’s approach, not a proof for arbitrary normal X. The nearby context treats the other prime regime: `MPL_16+47+54+44_transcription.tex`, cote 16, scans 019 and 021, uses the Picard/Néron–Severi decomposition and the prime-to-characteristic Kummer sequence, so these leaves add a characteristic-p differential counterpart rather than restating that argument.

### OC04 — The required transpose has a differential correction

**File/scan:** 46:022(a). **Kind:** conjecture / requested construction. **Quote:** “transposée dans un sens convenable”. **Results-state:** thematic bearing on **LM1_GROUP_SCHEMES_rerun_20261112 A.9** only; the recorded general dictionary question is not settled here.

Cartier’s field-level formula (1958, Chapter II, §6, equation (29), p. 200) is \((C\omega(D))^p=\omega(D^p)-D^{p-1}(\omega(D))\), while his equation (43), p. 203, gives \((aD)^p=a^pD^p+(aD)^{p-1}(a)D\). The correction terms explain why an ordinary linear transpose of \(D\mapsto D^p\) is insufficient. Cartier treats the differential and closed-form constraints explicitly; this comparison supplies a method for the request, not a construction of the manuscript’s unspecified target over every base.

### OC04a — A concrete obstruction to a literal symmetric-power transpose

**File/scan:** `MPL_46_002-048_work/pages/MPL_46_002-048_46_scan022.tex`, part (a). **Kind:** own verification. **Quote:** “\(\mathcal O_X\)-linéaire”; the target begins with a question mark and a deleted uncertain Symmᵖ. **Results-state:** no directly matching entry; the broader **LM1_GROUP_SCHEMES_rerun_20261112 A.9** remains open.

For \(A=\mathbf F_p[t]\) and \(D=\partial/\partial t\), direct evaluation on monomials gives \(D^p=0\) but \((tD)^p=tD\ne0\), since \(n^p=n\) in \(\mathbf F_p\). Hence \(D\mapsto D^p\) is neither A-linear nor Frobenius-semilinear under multiplication by the variable scalar t. An A-linear map \(T:\Omega^1_{A/\mathbf F_p}\to\operatorname{Sym}^p_A\Omega^1_{A/\mathbf F_p}\) cannot directly encode this p-power by the evaluation identity \(T(\omega)(D)=\omega(D^p)\), because evaluation of a degree-p symmetric tensor forces \(T(\omega)(tD)=t^pT(\omega)(D)\). **Confidence high, by the explicit calculation:** this rules out that literal transpose and explains why replacing the manuscript’s “O_X-linear” by “p-linear” would not repair it, while leaving open its explicitly qualified “dans un sens convenable”, unknown target, and the differential correction in Cartier’s formula.

### OC05 — Height one and the missing finiteness boundary

**File/scan:** 46:022(b). **Kind:** unproved claim. **Quote:** “Ω qu. coh.”; “certaines équations”. **Results-state:** bears on **LM1_GROUP_SCHEMES_rerun_20261112 A.9** as a concrete restricted case, without deciding its general programme.

SGA 3, Exposé VII_A, Theorem 7.4 and Remark 7.5 (corrected 2024 compilation, printed pp. 492–494), identifies flat, locally finitely presented height-at-most-one group schemes with finite locally free restricted Lie algebras. Here scalars from O_S are constant along invariant derivations, so the p-operation is homogeneous of degree p; in the finite locally free setting its polynomial dual and the dualized bracket give the displayed data, without the variable-scalar obstruction of OC04a. The leaf has neither those hypotheses nor the required identities, so its arbitrary quasi-coherent formulation remains a broader request.

### OC06 — The commutativity test belongs to the same restricted dictionary

**File/scan:** 46:022(b), right margin. **Kind:** unproved claim. **Quote:** “G est commutatif signifie que d₁=0”. **Results-state:** bears on **LM1_GROUP_SCHEMES_rerun_20261112 A.9** in the limited sense of OC05.

Under the finite locally free height-one correspondence of OC05, the dual map d₁ vanishes exactly when the Lie bracket vanishes, and the restricted enveloping algebra of an abelian restricted Lie algebra is commutative, giving the claimed group commutativity. This is a deduction within that correspondence, not a conclusion for an unrestricted quasi-coherent Ω. **Own verification; confidence high:** both implications follow from the perfect dual pairing and the enveloping-algebra presentation; no claim of novelty is made.

### OC07 — Verschiebung is supplied in a narrower setting

**File/scan:** 46:022(c), 027. **Kind:** unproved claim / later partial fulfilment. **Quote:** “Définir le ‘Verschiebung’”; “V.F=p”. **Results-state:** thematic bearing on **LM1_GROUP_SCHEMES_rerun_20261112 A.9**; no general equalizer result under **B.8** follows.

The supplied final typescript leaf constructs the map through a symmetric product for commutative algebraic groups, giving the displayed factorization of multiplication by p. SGA 3, Exposé VII_A, §4.3–4.3.2 (corrected 2024 compilation, printed pp. 471–472), gives the relative construction for flat commutative group schemes and both identities VF=[p] and FV=[p] on their respective Frobenius twists. The phrase “sur S” on scan 022 does not itself impose flatness, and the omitted scans 024–026 were not supplied in this transcription package, so the full intervening proof cannot be certified from these leaves.

### OC08 — A direct link to the earlier Cartier-duality question

**File/scan:** 46:022(b)–(c), 027, compared with cote 54:005 and 007 in the supplied context. **Kind:** unpursued implication. **Quote:** “V.F=p”. **Results-state:** bears on **WG2 §1.1 #3**; it does not settle the distinct Fourier witness question **WG2 §2.4 #4**.

The earlier first-pass context at 54:005 and 007 places Frobenius kernels in A[p], compares the two transposed F,V sequences, and asks whether a restricted Lie extension can be recovered from A[p]. Oda (1969, Corollary 5.11, p. 131) provides the precise published comparison \(M(A[p])\simeq H^1_{\mathrm{dR}}(A)\) over a perfect field, matching the Hodge subspace with \(\ker F=\operatorname{im}V\). This gives a concrete route from the current Frobenius/Verschiebung construction to that earlier extension question; matching every convention in the context’s symbol S_A still requires a separate check, since that context transcription is unreviewed.

### OC09 — Full Picard p-torsion is more than p-torsion line-bundle classes

**File/scan:** 46:020–022, compared with cote 54:005,007. **Kind:** unpursued implication. **Quote:** “Détermination de … Pic(X)”. **Results-state:** **WG2 §1.1 #3**; no directly matching settled entry.

The group Pic(X)[p] on these leaves records p-torsion line-bundle classes, whereas Oda’s Corollary 5.12 (1969, p. 131) concerns the group-scheme kernel Pic_{X/k}[p] and its dual Dieudonné module. For smooth proper X with a k-point, that corollary injects this module into de Rham cohomology with image \(\bigcap_n\ker(d\circ V^n)\), rather than identifying it with all of \(H^1_{\mathrm{dR}}\) in general. This distinction is essential when using the present calculation to study nonreduced Picard schemes: the logarithmic fixed-form calculation alone does not recover all infinitesimal p-torsion.

### OC10 — A useful comparison test, without an assertion of novelty

**File/scan:** 46:020–022. **Kind:** own idea. **Quote:** “Cω=ω”. **Results-state:** no directly matching result; practical follow-up under **WG2 §1.1 #3**.

Compare the logarithmic fixed-form calculation and the full F,V-module in an ordinary and a supersingular elliptic-curve example, keeping Pic(E)[p] distinct from the finite group scheme E[p]. **Confidence high as a diagnostic, not a new theorem:** the fixed subspace only tests one operator condition, whereas Oda’s comparison retains the entire Dieudonné module and the Hodge filtration. This would expose any mistaken replacement of the group scheme by its geometric points before attempting a higher-dimensional example.

### OC11 — The printed witness does not date the manuscript

**File/scan:** 46:020–022,027; context 54:005,007. **Kind:** own idea / historical boundary. **Quote:** “ce qui est l’opération de Cartier”. **Results-state:** **WG2 §1.1 #3** and **WG2 §2.4 #4**, as comparison limits.

Oda’s opening footnote (1969, p. 63) identifies the article as a modification of his June 1967 doctoral dissertation, and the remark following Corollary 5.11 credits a conjecture in Grothendieck’s published 1966 de Rham paper. **Confidence high:** these are explicit printed dates and references, but they do not establish when the undated cote 46 or cote 54 leaves were written. Consequently Oda is a mathematical comparison witness, not an identified second manuscript witness for cote 47 or evidence of an earlier draft of cote 44’s seven theorems.

## Exact supplied-context locators and status

- `MPL_16+47+54+44_transcription.tex`, cote 16, scan 019: Picard scheme, neutral component and Néron–Severi group, with ℓ distinct from the characteristic; scan 021: equations (8.3)–(8.7), Kummer, Tate modules and Brauer group. These are first-pass transcription claims, not independently checked manuscript readings in this task.
- Same file, cote 54, scan 003: universal vector extension and tangent/de Rham extension; scan 005: Cartier duality, A[p], Frobenius kernels and orthogonality; scan 007: transposed F,V sequences and the explicit question whether the restricted Lie extension follows from A[p]. These are first-pass context claims.
- `notes/RESULTS_STATE.md`, “Orientation for this package”: no existing result in the register for this cote; A.9/B.8 are broad possible links, not identifications. The current supplied leaves do not prove a general matrix-equalizer representability theorem and say nothing directly about the unrelated profinite GT headline claims.
- `Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`: printed page n corresponds to PDF page n−61 (one-based); e.g. p. 122 = PDF 61, p. 126 = PDF 65, p. 131 = PDF 70.
- Oda Definition 5.5, pp. 121–122: local p-base assumptions and logarithmic fixed-form criterion; p. 125: rational Cartier does not automatically preserve regular differentials; p. 126: normal-case dlog kernel; Theorem 5.10, pp. 126–131: comparison and image; Corollaries 5.11–5.12, p. 131: abelian and general smooth proper Picard comparisons.

## Verified primary bibliography (APA form)

Cartier, P. (1958). Questions de rationalité des diviseurs en géométrie algébrique. *Bulletin de la Société Mathématique de France, 86*, 177–251. https://doi.org/10.24033/bsmf.1503

Demazure, M., & Grothendieck, A. (Dirs.). (2011). *Schémas en groupes (SGA 3), Tome I: Propriétés générales des schémas en groupes* (P. Gille & P. Polo, Eds.; revised and annotated ed., Documents mathématiques, Vol. 7). Société Mathématique de France. (Original work published 1970.) Exposé VII_A, §§4.3 and 7, checked in the editors’ corrected compilation of October 13, 2024: https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp7A-13oct24.pdf

Oda, T. (1969). The first de Rham cohomology group and Dieudonné modules. *Annales scientifiques de l’École Normale Supérieure, 4e série, 2*(1), 63–135. https://doi.org/10.24033/asens.1175

## Web verification references for the parent

- Oda primary NUMDAM record: https://www.numdam.org/item/?id=ASENS_1969_4_2_1_63_0 (`turn2search5`); PDF https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf (`turn2search13`). Mathematical readings above principally use the supplied PDF, not search snippets; snippets lose the left subscripts in I(X), M(A[p]) and related expressions.
- Cartier primary PDF: https://www.numdam.org/article/BSMF_1958__86__177_0.pdf (`turn11view0`, `turn13view1`, `turn13view2`, `turn15view0`). Formula (29) is on printed p. 200/PDF zero-based 24, logarithmic criterion Proposition 7 on pp. 201–202, formula (43) on p. 203. NUMDAM bibliographic record `turn9search0`/`turn9search1`.
- Editor-hosted SGA3 landing page: https://webusers.imj-prg.fr/~patrick.polo/SGA3/ (`turn13view0`); updated VII_A PDF `turn15view1`, relevant excerpts `turn19view0`, `turn19view1`, `turn19view2`. Current numbering is Theorem 7.4 and editorial Remark 7.5; do not automatically call the theorem 7.4.1 from older citations.
- The SGA publisher record confirming edition: https://smf.emath.fr/node/27707 (`turn11search6`).

The parent must open the cited external pages itself before using these web citation references. The external Cartier and SGA PDF tools expose a 200-word paraphrase allowance per source; keep the main-note formulations compact and use direct mathematical reasoning separately. The supplied Oda attachment is user-provided material and was read directly.
