# Executed context searches for algebra notes A01–A40

The full supplied context/README.md and context/notes/RESULTS_STATE.md were read before these research notes were drafted. Each of the forty proposed items was searched separately against all four supplied context files: the README, LM2 congruence rows, same-cote notes, and results register. The final two-file search record was expanded to all four by the root reviewer before packaging.

Commands used rg -n -i -e PATTERN -- FILE from the workspace root. Every match is retained in algebra_context_searches.json; this readable record shows the first eight matching lines for each query/file, gives the complete count, and explicitly records negative searches. Long displayed match lines are shortened to 900 characters, with the unabridged text preserved in the JSON.

A hit identifies a comparison to inspect; it is not evidence that the hit proves the proposed note. In particular the earlier same-cote notes remain first-pass leads, the two Hua entries remain claims being checked, and broad words such as 'norm' or 'GT' do not establish an LM connection. Context paragraphs cited in algebra_notes.md were read, rather than inferred from the search snippets.

## A01 — The extension duality includes a checked minus sign

**Context:** C84, E160.2 (scan 160), L174.2 (scan 174), on perfect duality and determinant twists. **Relation:** adds. **RESULTS_STATE:** RS-later; no direct entry for this sign check.

**Executed query:** `Attention au signe|signe.*(dualit|isom)|dualit.*signe`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `dualit|déterminant|L174\.2`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **15 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:22: The packet contains 24 handwritten mathematical pages (even scans 146–192) alternating with 24 fully transcribed reused typescript pages (odd scans 147–193). The mathematical sequence concerns extensions, χ-trivialisations, duality, tensor comparison maps and quadratic algebras of rank two; the reused text concerns the author's reflective treatment of yin/yang, parental figures, creativity and later revisions of that treatment. Its dates belong to the reused text and cannot by themselves date the mathematical writing on the other sides. Archival pencil numbers 145–192, original typescript pagination, footnote numbers, and dates are separate numbering systems.
context/same_cote_84/MPL_84_146-193_notes.md:176: The margin begins “\(L_1,L'_1\) \unsure{qcq} \unsure{ici.}” and immediately responds “\unsure{non.} Mais \unsure{suppos.} \(L'_1,L'_2\) loc. libres de rang fini.” This is evidence of an authorial restriction, not permission to state the later duality for arbitrary modules. The precise scope of local freeness on the other terms still has to be checked against the construction and any earlier pages outside this packet.
context/same_cote_84/MPL_84_146-193_notes.md:178: ### E160.2 — The claimed duality requires a perfect pairing
context/same_cote_84/MPL_84_146-193_notes.md:180: **File/scan/lines:** `MPL_84_146-193_84_scan160.tex`, 160, 27–38. **Kind:** unproved claim. **Context comparison:** additional duality structure not stated in Hua, **84-chi-trivialised-extension-product**.
context/same_cote_84/MPL_84_146-193_notes.md:182: “Je dis que” introduces \(E_1^\vee\wedge E_2^\vee\simeq(E_1\wedge E_2)^\vee\), followed by a tensor–Hom identification. A proof must construct the displayed pairing, show it descends to the named extension products, and establish its perfection under the actual finite-projectivity hypotheses. The notation alone does not let one replace this with the standard duality of an ordinary tensor product.
context/same_cote_84/MPL_84_146-193_notes.md:352: ### L174.2
context/same_cote_84/MPL_84_146-193_notes.md:358: The displayed identifications claim compatibility of the product with duality after determinant-line twists. A proof must specify the canonical rank-two duality maps, the tensor-line identifications, and the hypotheses under which the product is functorial; the written string of isomorphisms supplies no coherence verification.
context/same_cote_84/MPL_84_146-193_notes.md:508: The factorization \(iq=T,qi=2\operatorname{id}\) gives a precise explanation of the tempting half: restriction of the ordinary tensor pairing to the images of \(A\) and its abstract dual is twice the perfect abstract pairing. In characteristic two that restricted pairing can vanish even when abstract duality remains perfect, so trace degeneracy, tensor-embedding failure, and loss of abstract duality are distinct questions. Confidence: high for the stated local model, because the script verifies \(i^{\mathsf T}q^{\mathsf T}=2I\) as a universal matrix identity.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A02 — The discriminant identity is asserted for a bare rank-two form

**Context:** C84, no exact match for `Q_N` or `\delta_N`; compare L182.3 (scan 182) only for the distinct distinction between abstract and induced pairings. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `Q_N|\\delta_N|\\varphi_N`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:44: - **LM7_PUSH E.64** [Proved (the return's claim; refereed 14 Nov 2026: proved as claimed where checkable; E.39, Boggi 2026 and NTY 2010 not opened)] Full hyperelliptic descent and the exact two CM comparison characters. Let $\Phi_{n,F}$ be the standard braid automorphism associated to $F=(\lambda,f)\in\widehat{\mathrm{GT}}$. Write \[ \delta_n=\sigma_1\cdots\sigma_{n-1},\qquad… Where: E.3. (LM7_PUSH_results.csv)
```

**Executed query:** `forme quadratique|rang.?deux|L182\.3`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **1 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:502: ### L182.3
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A03 — The first tensor-transpose attempt is withdrawn and restarted

**Context:** C84, L172.5 (scan 172), the factorization of \(1+\sigma_1\otimes\sigma_2\). **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

**Executed query:** `transpos|inc.*2|xi.*bar`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **16 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:116: The cancelled box is transcribed “`\unsure{2=\chi|2\ne\chi}`,” whereas the subsequent live text includes “\(\gamma\chi=2\)” and the explicit choice “\(\chi=2\qquad\gamma=1\).” Neither the context nor the surrounding mathematics licenses selecting an unmarked reading of the cancelled sign. The live specialization is secure evidence for the calculation’s chosen case, rather than evidence that the cancelled formula states a general obstruction.
context/same_cote_84/MPL_84_146-193_notes.md:158: The display “`\overline{\unsure{X_i|x_i}}=x_i-\pi_i(x_i)=\bigl\{`” stops at an opening brace and is followed by a partly cancelled tensor continuation. It does not supply an additional formula or case distinction that can safely be used in a proof. The preceding completed \(\chi=2\) calculation must therefore be kept separate from this abandoned continuation.
context/same_cote_84/MPL_84_146-193_notes.md:456: **Brief quotation:** `\unsure{les} \unsure{deux} \unsure{sont} \unsure{transposés}`
context/same_cote_84/MPL_84_146-193_notes.md:458: The asserted transposition of the two tensor involutions is consistent with the dual bases displayed in scans 176 and 190. In the local free model, the algebra conjugation has matrix \(\bigl(\begin{smallmatrix}1&-b_i\\0&-1\end{smallmatrix}\bigr)\), and its transpose determines the module-side involution, so the adjoint symmetrizer identity can be checked without inverting two.
context/same_cote_84/MPL_84_146-193_notes.md:508: The factorization \(iq=T,qi=2\operatorname{id}\) gives a precise explanation of the tempting half: restriction of the ordinary tensor pairing to the images of \(A\) and its abstract dual is twice the perfect abstract pairing. In characteristic two that restricted pairing can vanish even when abstract duality remains perfect, so trace degeneracy, tensor-embedding failure, and loss of abstract duality are distinct questions. Confidence: high for the stated local model, because the script verifies \(i^{\mathsf T}q^{\mathsf T}=2I\) as a universal matrix identity.
context/same_cote_84/MPL_84_146-193_notes.md:568: The dual description is reduced from a bilinear form with two auxiliary functionals to a bilinear form with one scalar \(\lambda\). The cancelled conditions labelled a) and b), including the doubled \(2g_i\) restrictions, are replaced by the two trace restrictions; the cancelled version should not be combined with the live one as simultaneous axioms.
context/same_cote_84/MPL_84_146-193_notes.md:950: “par dessus la tête”: He says a reader unfamiliar with yin–yang may miss the recent discussion and proposes striking examples. He dates the preceding day's activity as an increasingly systematic census of pairs; 12 October follows from the dated 13 October note.
context/same_cote_84/MPL_84_146-193_notes.md:1510: “combinaisons possibles”: He identifies the sixty-four hexagrams with all sequences of six binary yin/yang signs, including the two constant sequences. The arithmetic count is 2^6 = 64; it establishes the size of the stated binary model and gives no support by itself to divinatory claims.
```

- `context/notes/RESULTS_STATE.md`: **6 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:20: - **CYCLOTOMIC_KERNEL D13** [Open (the return's claim)] D(e) remains unfinished for discontinuous actions normalizing no finite-level deck group and for the affine commensurator-completion description; the exact abstract-cocycle construction problem is stated for the U03 Poincare curve over Qbar. Where: section 3; pp.30-31; scans 62-63. (CYCLOTOMIC_KERNEL_results.csv)
context/notes/RESULTS_STATE.md:57: - **FLAGGED_149 B5** [Proved (the return's claim)] Corollaries 1(b), 2(c)--(d), and 3 with all comparison maps — A hyperbolic polycurve means a finite tower of smooth pairs whose geometric curve fibres have $2g-2+r>0$, including proper fibres. Over a field finitely generated over… Where: cote 149; section 1; pp. 11–15; scans 24–31. (FLAGGED_149_results.csv)
context/notes/RESULTS_STATE.md:84: - **EXPERT BOGGI_ZALESSKII_STEP §?** [reading of the field expert (Claude Opus 5.5 at effort max), on the returns' claims] Later checks: - **14 November 2026, ~12:35 UTC: the Poincaré read-in** (Claude Fable 5.2 at effort max; its own work, checked by no one; `research_maps_20261112/PRETOT_3D_MODULARITY/POINCARE_AND_A5_20261114.md`, and its block "Added by the Poincaré read-in", R1–R12, under item 2.4 of `PUSH_ITEMS_20261114.md`). - The bridge is e… (NOTE_BOGGI_ZALESSKII_STEP.md)
context/notes/RESULTS_STATE.md:87: - **EXPERT IMPLICATIONS_E65_LM_part2 §3** [reading of the field expert (Claude Fable 5.2 at effort max), on the returns' claims] Why Galois has `Delta = 0`: the harmonic map (hunch, derived for this page, unchecked): The coincidence of the two fields has a geometric source. The modular curves of level 3 and level 4 are both a sphere, with the tetrahedral group `A_4` and the octahedral group `S_4`, and `A_4` lies in `S_4`. The points of level 3 over `j =… (EXPERT_IMPLICATIONS_E65_LM_part2.md)
context/notes/RESULTS_STATE.md:96: - **MPL_84_146-193 §2** [observation (research note of a returned package, first pass; a lead)] Principal findings and their exact limits: - **A precise local algebraic result:** scans 172 and 192 give a quadratic-algebra product whose relation and discriminant formula check over the integer polynomial ring; its local formula matches Voight (2016, Const… (MPL_84_146-193_notes.md)
context/notes/RESULTS_STATE.md:121: - **FLAGGED_149**: RETURNED; returned 12 Nov, INCOMPLETE (B9, ZCF6, ZD10, Z142g open) (MATHS_PROMPTS_TALLY.md)
```

**Executed query:** `L172\.5|factori[sz]|withdraw|retir`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **30 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:96: **File/scan/lines:** `MPL_84_146-193_84_scan150.tex`, 150, 3–7. **Kind:** withdrawn in the same text. **Context comparison:** a caution for Hua, **84-chi-trivialised-extension-product**; the relevant words are already cancelled on scan 150.
context/same_cote_84/MPL_84_146-193_notes.md:108: **File/scan/lines:** `MPL_84_146-193_84_scan152.tex`, 152, 15–16. **Kind:** withdrawn in the same text / self-check completed. **Context comparison:** supplies an explicit internal correction not reported in Hua, **84-chi-trivialised-extension-product**.
context/same_cote_84/MPL_84_146-193_notes.md:114: **File/scan/lines:** `MPL_84_146-193_84_scan152.tex`, 152, 19 and 32–47. **Kind:** reading question / withdrawn in the same text. **Context comparison:** relevant to the all-\(\chi\) wording of Hua, **84-chi-trivialised-extension-product**, without resolving the frozen doubt.
context/same_cote_84/MPL_84_146-193_notes.md:120: **File/scan/lines:** `MPL_84_146-193_84_scan152.tex`, 152, 57–77; `MPL_84_146-193_84_scan156.tex`, 156, 39–42. **Kind:** withdrawn in the same text, subsequently revisited. **Context comparison:** adds the chronology of one local calculation to Hua, **84-chi-trivialised-extension-product**.
context/same_cote_84/MPL_84_146-193_notes.md:174: **File/scan/lines:** `MPL_84_146-193_84_scan160.tex`, 160, 8–10. **Kind:** withdrawn in the same text. **Context comparison:** supplies a hypothesis missing from the short summary of Hua, **84-chi-trivialised-extension-product**.
context/same_cote_84/MPL_84_146-193_notes.md:200: The thick top arrow between the tensor terms is labelled “?”. Its factorization through \(E\), and compatibility with the amalgamated sum below, are precisely what need to be constructed rather than assumed. The four-term polynomial at the foot of the page is an ansatz for this problem, not a finished proof.
context/same_cote_84/MPL_84_146-193_notes.md:234: **File/scan/lines:** `MPL_84_146-193_84_scan166.tex`, 166, 19–28. **Kind:** withdrawn in the same text. **Context comparison:** makes the endpoint convention essential when testing Hua, **84-chi-trivialised-extension-product**.
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A04 — A module transpose is claimed before quadratic algebra structure

**Context:** C84, E160.2 (scan 160), L174.2 (scan 174), and E170.2 (scan 170). **Relation:** adds. **RESULTS_STATE:** RS-χ.

**Executed query:** `transpos|sans.*quadrati`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **2 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:456: **Brief quotation:** `\unsure{les} \unsure{deux} \unsure{sont} \unsure{transposés}`
context/same_cote_84/MPL_84_146-193_notes.md:458: The asserted transposition of the two tensor involutions is consistent with the dual bases displayed in scans 176 and 190. In the local free model, the algebra conjugation has matrix \(\bigl(\begin{smallmatrix}1&-b_i\\0&-1\end{smallmatrix}\bigr)\), and its transpose determines the module-side involution, so the adjoint symmetrizer identity can be checked without inverting two.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `E160\.2|L174\.2|coh[ée]rence`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **15 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:37: | Symmetric monoidal category for every \(\chi\) | No associativity, unit, symmetry, or coherence data are written in these mathematical scans. | R11 independently verifies a strict symmetric monoidal groupoid for fixed trivial rank-one endpoints over a commutative ring, for every \(\chi\), with automorphisms retained as in R13; global descent and identification with the manuscript's category remain unverified, and other ranges cited by Hua were not supplied. |
context/same_cote_84/MPL_84_146-193_notes.md:68: If the scalar in “`b'_i=b_i+\unsure{\chi|\gamma}u_i`” is \(\chi\), then \(b'_1b'_2-b_1b_2=\chi(u_1b_2+b_1u_2+\chi u_1u_2)\), so the product is independent of this change modulo \(\chi\). This suggests separating a residue invariant on \(V(\chi)\) from a globally defined product extension and its coherence data. The computation is compatible with the locus occurring in Hua’s invertibility statement, but neither a section called \(T_0\) nor that invertibility criterion occurs in this interval.
context/same_cote_84/MPL_84_146-193_notes.md:134: The doubtful prose says the two “\unsure{homotopies|contraintes}” are compatible and leave an “\unsure{indétermination}” which is a Hom from \(M_1\otimes M_2\) to \(L_1\otimes L_2\). This is consistent with the familiar freedom to alter an extension morphism fixing its ends by a map from the quotient to the subobject, but existence and compatibility with the chosen \(\chi\)-trivialisations still require proof. In particular, the stated ambiguity cannot itself establish a unique natural comparison or monoidal coherence.
context/same_cote_84/MPL_84_146-193_notes.md:178: ### E160.2 — The claimed duality requires a perfect pairing
context/same_cote_84/MPL_84_146-193_notes.md:256: ### E170.2 — A canonical comparison is asserted, but coherence is not supplied
context/same_cote_84/MPL_84_146-193_notes.md:260: The bullet asserts “une \unsure{application} can. d'\unsure{extensions} de \(E_1\vee E_2\) en \(E_1\wedge E_2\).” The preceding pages expose nontrivial coefficient conditions, a Hom-valued ambiguity, and question-marked arrows; this sentence does not by itself discharge those obligations. No associator, unit constraint, symmetry constraint, or coherence diagram appears in the supplied mathematical scans 146–170. The separate editorial model in R11–R13 does verify a positive local monoidal construction and its local invertibility criterion, while leaving global identification and this particular comparison to be proved.
context/same_cote_84/MPL_84_146-193_notes.md:352: ### L174.2
context/same_cote_84/MPL_84_146-193_notes.md:358: The displayed identifications claim compatibility of the product with duality after determinant-line twists. A proof must specify the canonical rank-two duality maps, the tensor-line identifications, and the hypotheses under which the product is functorial; the written string of isomorphisms supplies no coherence verification.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A05 — The reduced-trace pushout has a concrete compatibility condition

**Context:** C84, L180.1 (scan 180), on the rank-three boundary and rank-two pushout; E170.1 (scan 170), on exactness hypotheses. **Relation:** restates. **RESULTS_STATE:** RS-product, RS-χ.

**Executed query:** `trace réduite|pushout|somme amalgam`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **19 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:18: - **A separate sign obstruction:** for the explicitly fixed endpoint conventions, the pushout and pullback extension cocycles are opposite; a χ=0 elliptic-curve example prevents an isomorphism fixing both ends (E170.4–E170.5). This does not refute a sign-twisted interpretation or the whole ellipsized Hua entry.
context/same_cote_84/MPL_84_146-193_notes.md:39: | Pushout and pullback products agree | Scans 162 and 168 mark comparison arrows “?”; scan 170 asserts a canonical application; scans 148–158 expose \(\gamma\chi=2\) or \(\delta\chi=2\). | Supported as an authorial goal/claim; the fixed-endpoint all-\(\chi\) interpretation has the conditional obstruction in E170.4, and sign conventions or restrictions must be checked in the omitted ranges. |
context/same_cote_84/MPL_84_146-193_notes.md:206: In the three-row extension diagram the middle downward arrow from \(E\) into \(E_1\otimes E_2\) bears “?”, with the right downward map labelled \(\chi\mathrm{id}\). A proof must check this specified map on the quotient as well as its restriction on the left term; verifying only the upper pushout does not suffice. This question is distinct from merely choosing a tensor endomorphism in the preceding diagram.
context/same_cote_84/MPL_84_146-193_notes.md:246: **File/scan/lines:** `MPL_84_146-193_84_scan168.tex`, 168, 4–17. **Kind:** self-flagged: unverified step. **Context comparison:** precise local support for, and limitation on, the pushout–pullback part of Hua, **84-chi-trivialised-extension-product**.
context/same_cote_84/MPL_84_146-193_notes.md:254: “On définit de façon \unsure{can.}” introduces the two extension products, while the margin calls the inclusions “\unsure{univ.} \unsure{injectfs|injectifs}.” The pushout and pullback diagrams give a concrete construction plan, but exactness of their tensor rows requires the stated universal-injectivity or suitable flatness assumptions. This is substantially more specific than an unqualified operation on every extension of arbitrary modules.
context/same_cote_84/MPL_84_146-193_notes.md:270: **File/scan/lines:** `MPL_84_146-193_84_scan168.tex`, 168, 9–13; `MPL_84_146-193_84_scan170.tex`, 170, 19–36; compare `MPL_84_146-193_84_scan166.tex`, 166, 19–28. **Kind:** own idea. **Confidence:** high for the explicitly specified fixed-endpoint interpretation, because the transition matrices and scalar residuals are computed; no claim of novelty or blanket refutation of Hua. **Context comparison:** conditionally contradicts the statement that the pushout and pullback products “agree” in Hua, **84-chi-trivialised-extension-product**, if that means an isomorphism inducing identities on both ends for every \(\chi\).
context/same_cote_84/MPL_84_146-193_notes.md:272: At \(\chi=0\), take \(L_i=M_i=\mathcal O_X\), \(\pi_i=\psi_i\), and \(\varpi_i=-\alpha_i\); the diagrams then give the Baer sum of the two extension classes for the pushout product and its negative for the pullback product. For a nonzero class \(e\in H^1(X,\mathcal O_X)\) on a smooth elliptic curve over a characteristic-zero field and a split second extension, these classes are \(e\) and \(-e\), which differ because \(2e\ne0\) (The Stacks Project Authors, n.d., Tags 0B3A and 072J). Therefore no comparison fixing both ends exists in this example, although a comparison negating the subobject does exist, so an unrecorded sign convention or restriction to \(\chi=2\) can change the verdict. The derivation below separates this precise obstruction from the existence of a product operation or a symmetric-monoidal structure, neither of which the example refutes.
context/same_cote_84/MPL_84_146-193_notes.md:448: The displayed amalgamated sums construct the candidate \(A\) and \(E\) without dividing by two. With locally free rank-two inputs and the standard scalar inclusions, the relevant boundary submodules have rank three and the pushouts have rank two, but this module-rank statement alone does not produce an associative multiplication or all canonical comparison maps.
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:116: - **84-chi-trivialised-extension-product** (cote 84, their pp. 65–79, 123–131, 141–169; our scans 124, 125, 126, 127, 128, 129, 130, 131, 132, 142, 143, 144, 145) [conjecture (candidate: their search found no reference) | L…] For any fixed χ ∈ Γ(𝒪), extensions 0 → L → E → M → 0 equipped with a χ-splitting (π, ϖ) form a symmetric monoidal category under a product built by amalgamated sum without division, with b = b₁ ⊗ b₂ in split coordinates; for M = 𝒪 an object is invertible iff its section T₀ generates L on V(χ), and the pushout and pullback products agree… Our intake: new to us: our package for this cote is waiting
```

**Executed query:** `L180\.1|exact|E170\.1`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **1 matching lines**; shown below.

```text
context/LM2_CONGRUENCE_ROWS.md:12: | LM2 C.d3 | Exact local adelic solution locus, sign compatibility and §48 coboundary schemes | claim (return: Proved) | §46; fols400–401; scans202–205; §48; scans254–266 |
```

- `context/same_cote_84/MPL_84_146-193_notes.md`: **149 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:7: This report contains **208 individually identified items**: 38 early mathematical notes (E146.1–E170.5), 39 later mathematical notes (L172.1–L192.4), 118 notes on reused typescript (T147.1–T193.5), and 13 comparisons or editorial investigations (R01–R13). Source references identify the exact per-scan file; approximate line numbers refer to the frozen TeX rather than physical manuscript lines. Diplomatic doubt macros reproduced in quotations retain their editorial meaning: a `\unsure` is not automatically an uncertainty expressed by the author, and a cancelled claim is not live text.
context/same_cote_84/MPL_84_146-193_notes.md:13: ### Principal findings and their exact limits
context/same_cote_84/MPL_84_146-193_notes.md:35: | Product by amalgamated sum without division | Scans 168 and 170 explicitly mark the relevant squares “cocart”; their structural maps use \(\pi_i\), not division by \(\chi\). | Supported as a construction plan; tensor exactness and the resulting splitting data still need proof in the stated category. |
context/same_cote_84/MPL_84_146-193_notes.md:66: **File/scan/lines:** `MPL_84_146-193_84_scan146.tex`, 146, 31–37. **Kind:** own idea. **Confidence:** high for the conditional algebraic observation, because the polynomial identity is checked exactly; no claim of novelty. **Context comparison:** refines only the local coefficient clause of Hua, **84-chi-trivialised-extension-product**.
context/same_cote_84/MPL_84_146-193_notes.md:86: The phrase “`\mathcal H_i=\text{\unsure{noyau} de}`” is unfinished, followed by the purported sequence from \(\operatorname{Hom}(M,L)\) through \(\mathcal H/\mathrm{id}\) to \((\mathcal O\times\mathcal O)/\mathcal O\). To assess exactness one must specify the omitted map, the action on both ends of the extension, and whether surjectivity is local or global. Hua’s category-level summary does not supply those missing definitions.
context/same_cote_84/MPL_84_146-193_notes.md:218: The four operator rows “\(1,\pi'_1,\pi'_2,\pi'_1\otimes\pi'_2\)” contain three data columns, followed by the boxed equations \(\alpha+(\beta_1+\beta_2)\chi+\gamma\chi^2=\chi\), \(\alpha+\beta_1\chi=0\), and \(\beta_2+\gamma\chi=1\). The missing fourth input summand \(M_1\otimes M_2\) is exactly where scan 154 places the unresolved entries. Consequently these partial restrictions cannot alone verify the full comparison matrix.
context/same_cote_84/MPL_84_146-193_notes.md:222: **File/scan/lines:** `MPL_84_146-193_84_scan164.tex`, 164, 42–63; `MPL_84_146-193_84_scan154.tex`, 154, 34–39; `MPL_84_146-193_84_scan166.tex`, 166, 19–28. **Kind:** own idea. **Confidence:** high for the explicitly fixed local model, because all matrix residuals are computed exactly; no claim of novelty. **Context comparison:** a conditional test of Hua, **84-chi-trivialised-extension-product**, not a refutation of unspecified conventions.
context/same_cote_84/MPL_84_146-193_notes.md:224: For \(F=\alpha I+\beta_1P_1+\beta_2P_2+\delta P_1P_2\), the family \(\alpha=-\chi(1-\delta\chi)\), \(\beta_1=\beta_2=1-\delta\chi\) meets the three-summand restrictions. Against the endpoint-preserving comparison matrix, its remaining entries differ by \((2-\delta\chi)\tau_1\), \((2-\delta\chi)\tau_2\), and \(\chi(\delta\chi-2)\). Thus \(\delta\chi=2\) is sufficient, and necessary for a universal polynomial identity in independent \(\tau_i\), whereas special modules may have additional annihilators; `early_formula_checks.py` records the exact scope.
```

- `context/notes/RESULTS_STATE.md`: **17 matching lines**; shown below (first eight; all in JSON).

```text
context/notes/RESULTS_STATE.md:15: - **LM4 B.12** [Open (the return's claim)] The proposed identities on the full Grothendieck--Teichm\"uller group B.53 below proves P4's exact quadratic-character domain, both quintic homomorphisms, their arithmetic identity, and the kernel inclusion for $\mathcal K$. Its third map has the corrected weighted-orbifold target $\operatorname{Out}_{\partial}(C_3\amalg C_3)$.… Where: B.3.P4;B.3.P5. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:17: - **FLAGGED_149 ZCF6** [Open (the return's claim)] The existence assertions retained after the centralizer computation — \textup{[\S2--3, manuscript pp.\ 22--34 and 51; scans 45, 48--49, 51, 56--57, 59--63, 66--69, 104.]} The following exact assertions are not proved or refuted here. They are recorded separately from the proved uniqueness and centralizer assertions. \begin{enum… Where: 149; sections2–3; manuscript22–34,51; scans45,48–49,51,56–57,59–63,66–69,104. (FLAGGED_149_results.csv)
context/notes/RESULTS_STATE.md:20: - **CYCLOTOMIC_KERNEL D13** [Open (the return's claim)] D(e) remains unfinished for discontinuous actions normalizing no finite-level deck group and for the affine commensurator-completion description; the exact abstract-cocycle construction problem is stated for the U03 Poincare curve over Qbar. Where: section 3; pp.30-31; scans 62-63. (CYCLOTOMIC_KERNEL_results.csv)
context/notes/RESULTS_STATE.md:32: - **LM4 D.10** [Open (the return's claim)] Arbitrary-frontier descent in the exact comparison Let $U$ be a simply connected open orbit in the original surface. The prime-end disk need not map continuously onto its closure. When the interior identification has such an extension, its boundary map may fail to be injective. We have not proved that an intrinsic centralizer f… Where: D.3 arbitrary-frontier descent. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:36: - **LM4 E.10** [Open (the return's claim)] The six congruence-kernel computations in prompt E.1 For each type (E.1.1), determine $K_c^\tau$ and the nonabelian pointed set $H^1(C_2,K_c)$ for $\operatorname{Ad}(\tau)$. E.3 gives the exact class and centralizer formula after these groups and sets are known; E.5 supplies its quotient-centralizer term for the five oval types… Where: E.1: six requested computations unresolved. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:44: - **LM7_PUSH E.64** [Proved (the return's claim; refereed 14 Nov 2026: proved as claimed where checkable; E.39, Boggi 2026 and NTY 2010 not opened)] Full hyperelliptic descent and the exact two CM comparison characters. Let $\Phi_{n,F}$ be the standard braid automorphism associated to $F=(\lambda,f)\in\widehat{\mathrm{GT}}$. Write \[ \delta_n=\sigma_1\cdots\sigma_{n-1},\qquad… Where: E.3. (LM7_PUSH_results.csv)
context/notes/RESULTS_STATE.md:46: - **LM7_PUSH D.44** [Proved (the return's claim; refereed 14 Nov 2026: the parts D.50 and E.58 use proved as claimed)] Exact modular descent and gentle normalization over a coprime base. Let \(\widehat B=C_2\amalg C_3=\langle s,r\mid s^2=r^3=1\rangle\), let \(F=\ker(\widehat B\to\mathfrak S_3)\), and use \[ \tau=sr,\qquad x=\tau^{-2},\qquad y=sxs… Where: D.2. (LM7_PUSH_results.csv)
context/notes/RESULTS_STATE.md:49: - **LM7_PUSH E.69** [Proved (the return's claim)] The Gaussian central layer and its exact common finite fibres. Let $H_3$ be the exponent-three Heisenberg group, written in logarithmic coordinates as \[ (v,c)(w,e)=(v+w,c+e+\tfrac12\det(v,w)), \qquad v,w\in\mathbf F_3^2,\quad c,… Where: E.3. (LM7_PUSH_results.csv)
```

## A06 — Scan 102 gives a conditional invariant-ring identification

**Context:** C84, L172.3–L172.5 (scan 172), L192.1 (scan 192). **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

**Executed query:** `univers.*inject|invariant|étale`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **7 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:34: | Extensions with a fixed \(\chi\)-splitting | Scan 170 gives the extension diagrams and identities; scans 146–168 calculate with them. | Supported as the intended objects, subject to the written universal-injectivity and local-freeness hypotheses and the frozen sign doubt. |
context/same_cote_84/MPL_84_146-193_notes.md:64: ### E146.3 — A residue class is a useful, limited invariant
context/same_cote_84/MPL_84_146-193_notes.md:68: If the scalar in “`b'_i=b_i+\unsure{\chi|\gamma}u_i`” is \(\chi\), then \(b'_1b'_2-b_1b_2=\chi(u_1b_2+b_1u_2+\chi u_1u_2)\), so the product is independent of this change modulo \(\chi\). This suggests separating a residue invariant on \(V(\chi)\) from a globally defined product extension and its coherence data. The computation is compatible with the locus occurring in Hua’s invertibility statement, but neither a section called \(T_0\) nor that invertibility criterion occurs in this interval.
context/same_cote_84/MPL_84_146-193_notes.md:254: “On définit de façon \unsure{can.}” introduces the two extension products, while the margin calls the inclusions “\unsure{univ.} \unsure{injectfs|injectifs}.” The pushout and pullback diagrams give a concrete construction plan, but exactness of their tensor rows requires the stated universal-injectivity or suitable flatness assumptions. This is substantially more specific than an unqualified operation on every extension of arbitrary modules.
context/same_cote_84/MPL_84_146-193_notes.md:1926: | T170.1 / 170 | Input extensions and splitting identities | \(i=1,2\); \(\chi\), universal injectivity | 2 extensions; 3 live displayed identity lines for each \(i\), one with `=\|+` doubt | Script uses the declared equality interpretation; no silent disambiguation. |
context/same_cote_84/MPL_84_146-193_notes.md:2035: For F₂ with `b1=b2=1`, the four ordered pairs `(c1,c2)` give the Artin–Schreier coefficients `c1+c2`: two split products and two nonsplit products. Thus the four rank-one failures among all 16 tuples occur exactly at `b1=b2=0`, and are different from the four étale-input cases. These finite counts illustrate the universally derived criterion and do not replace its proof.
context/same_cote_84/MPL_84_146-193_notes.md:2072: For the concrete case \(\chi=0\), choose \(L_i=M_i=\mathcal O_X\), \(\tau_i=1\), and any locally free extension \(E_i\) of \(\mathcal O_X\) by itself. The globally defined maps \(\pi_i=\psi_i\) and \(\varpi_i=-\alpha_i\) satisfy the displayed splitting identities, and the inclusions are universally injective because the quotient is locally free. If the first extension has a nonzero class \(e\in H^1(X,\mathcal O_X)\) and the second is split, the computed classes are \(e\) and \(-e\). On a smooth elliptic curve over a characteristic-zero field the vector space \(H^1(X,\mathcal O_X)\) is one-dimensional (The Stacks Project Authors, n.d., Tags 0B3A, 072J and 0BY6), so such an \(e\) exists and is not killed by two; hence the two extensions are not isomorphic with both end identifications fixed. Sending the subobject by \(-\mathrm{id}\), however, removes the obstruction. This exact dependence  … [full line in JSON]
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:34: - **LM4 D.12** [Open (the return's claim)] The universal admissible level-zero kernel For an admissible punctured surface, with actual homeomorphism group $A$, a strict action $u:\Gamma\to A$, and $H=u(\Gamma)$, the unresolved comparison of LM4 C.12 is injectivity of \[ \pi_1(C_A(H),1)\longrightarrow\pi_1(A,1)^\Gamma. \] For hyperbolic finite-type surfaces the target is… Where: D.3 general level-zero comparison. (LM4_SUCCESSOR_results.csv)
```

**Executed query:** `L172\.[345]|L192\.1`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **7 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:302: ### L172.3
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
context/same_cote_84/MPL_84_146-193_notes.md:632: ### L192.1
context/same_cote_84/MPL_84_146-193_notes.md:1724: | 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
context/same_cote_84/MPL_84_146-193_notes.md:1741: | 192 | “ça croule si 2=0, b1=b2=0” (the two French words remain doubtful) | Explicit failure warning; L192.1. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A07 — The relative norm must lift through a possibly noninjective map

**Context:** C84, L172.4–L172.5 (scan 172), and L190.2 (scan 190). **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

**Executed query:** `remont|relative norm|norme relative`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `L172\.[45]|L190\.2`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
context/same_cote_84/MPL_84_146-193_notes.md:602: ### L190.2
context/same_cote_84/MPL_84_146-193_notes.md:1724: | 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A08 — The doubt about injectivity is outside the NB's hypothesis

**Context:** C84, L172.4 (scan 172), L192.1 (scan 192), R06 (scans 172/192). **Relation:** restates. **RESULTS_STATE:** RS-product, RS-later.

**Executed query:** `surject|inject|kernel`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **2 matching lines**; shown below.

```text
context/LM2_CONGRUENCE_ROWS.md:10: | LM2 C.d1 | Every actual GT0 loop automorphism preserves all projective congruence kernels | claim (return: Known) | §39; scans21–30; §44; scans150–168; §46; fols398–400,409; scans198–202,218–219 |
context/LM2_CONGRUENCE_ROWS.md:16: | LM2 C.r5 | GT0 injects into Out of the full profinite linear modular group | claim (return: Proved) | §§45–46; fols.384–391; scans170–184 |
```

- `context/same_cote_84/MPL_84_146-193_notes.md`: **15 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:34: | Extensions with a fixed \(\chi\)-splitting | Scan 170 gives the extension diagrams and identities; scans 146–168 calculate with them. | Supported as the intended objects, subject to the written universal-injectivity and local-freeness hypotheses and the frozen sign doubt. |
context/same_cote_84/MPL_84_146-193_notes.md:86: The phrase “`\mathcal H_i=\text{\unsure{noyau} de}`” is unfinished, followed by the purported sequence from \(\operatorname{Hom}(M,L)\) through \(\mathcal H/\mathrm{id}\) to \((\mathcal O\times\mathcal O)/\mathcal O\). To assess exactness one must specify the omitted map, the action on both ends of the extension, and whether surjectivity is local or global. Hua’s category-level summary does not supply those missing definitions.
context/same_cote_84/MPL_84_146-193_notes.md:254: “On définit de façon \unsure{can.}” introduces the two extension products, while the margin calls the inclusions “\unsure{univ.} \unsure{injectfs|injectifs}.” The pushout and pullback diagrams give a concrete construction plan, but exactness of their tensor rows requires the stated universal-injectivity or suitable flatness assumptions. This is substantially more specific than an unqualified operation on every extension of arbitrary modules.
context/same_cote_84/MPL_84_146-193_notes.md:306: **Brief quotation:** `\unsure{injectif} \unsure{sauf si} car. 2 et $b_1=b_2=0$`
context/same_cote_84/MPL_84_146-193_notes.md:308: The marginal qualification singles out precisely the field case in which the indicated image of the abstract generator loses its nonconstant part. Scan 192’s “ça croule” repeats the same exceptional specialization, but neither passage by itself gives the general base-ring injectivity criterion.
context/same_cote_84/MPL_84_146-193_notes.md:318: For the displayed local model, \(i:R[t]/(t^2+bt+c)\to B=A_1\otimes_R A_2\), \(t\mapsto2u_1u_2+b_2u_1+b_1u_2\), has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\), because the four tensor-basis coefficients of \(i(a+dt)\) are \((a,db_2,db_1,2d)\). Thus \(R=\mathbb Z/4\mathbb Z\), \(b_1=b_2=c_1=c_2=0\), gives the nonzero kernel element \(2t\), while a split injection requires the stronger condition \((2,b_1,b_2)=R\). Confidence: high for this conditional algebraic statement, since it is a direct coefficient calculation and the script independently enumerates the small-ring examples.
context/same_cote_84/MPL_84_146-193_notes.md:378: The coefficient calculation concludes that the abstract product generator differs from \(u_1*u_2\) by the scalar \(b_1b_2\), while the scalar coefficient is extracted by pairing with \(x\). Its tensor image agrees with scan 172’s formula, but the abstract element and its potentially noninjective tensor image must be distinguished.
```

- `context/notes/RESULTS_STATE.md`: **16 matching lines**; shown below (first eight; all in JSON).

```text
context/notes/RESULTS_STATE.md:15: - **LM4 B.12** [Open (the return's claim)] The proposed identities on the full Grothendieck--Teichm\"uller group B.53 below proves P4's exact quadratic-character domain, both quintic homomorphisms, their arithmetic identity, and the kernel inclusion for $\mathcal K$. Its third map has the corrected weighted-orbifold target $\operatorname{Out}_{\partial}(C_3\amalg C_3)$.… Where: B.3.P4;B.3.P5. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:16: - **LM4 B.41** [Open (the return's claim)] Parity and further-orbit lifting in the hypothetical nontrivial kernel If $\mathcal K\ne1$, neither the restriction of $\Delta$ to all its elements nor its extension along every required icosahedral marked-orbit locus has been determined. The latter extension would have to be constructed with compatible based maps and then chec… Where: B.7. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:18: - **LM4 B.38** [Open (the return's claim)] The remaining congruence levels No determination of $\mathcal K_N$ for all $N$ is obtained here. In particular $\mathcal K_5=1$ is the main unresolved assertion, and the corresponding level-seven and level-eleven kernels remain undecided. Their quotient compactifications have genera three and twenty-six, respectively. An index-… Where: B.5. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:20: - **CYCLOTOMIC_KERNEL D13** [Open (the return's claim)] D(e) remains unfinished for discontinuous actions normalizing no finite-level deck group and for the affine commensurator-completion description; the exact abstract-cocycle construction problem is stated for the U03 Poincare curve over Qbar. Where: section 3; pp.30-31; scans 62-63. (CYCLOTOMIC_KERNEL_results.csv)
context/notes/RESULTS_STATE.md:30: - **LM4 B.39** [Open (the return's claim)] The nonsolvable direction and the published assertions For a finite solvable subgroup of a genus-zero mapping class group, the centralizer is the closure of the discrete centralizer, by the prime-power normalizer induction in B.30 and the open-kernel argument B.2. This proves the solvable direction of the refined triangle-orbif… Where: B.6;Lead4. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:31: - **LM4 C.4** [Open (the return's claim)] The actual kernel in prompt C.1 In the actual torus setting of C.3, prove or refute $K=1$. The audited structural conclusions of LM4 D.78 imply that $K$ is pro-odd. C.1 shows that any counterexample must have an infinitely generated free pro-$p$ quotient for an odd prime. It would suffice to prove that the actual $K$ is finitel… Where: C.1: requested decision unresolved. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:32: - **LM4 D.10** [Open (the return's claim)] Arbitrary-frontier descent in the exact comparison Let $U$ be a simply connected open orbit in the original surface. The prime-end disk need not map continuously onto its closure. When the interior identification has such an extension, its boundary map may fail to be injective. We have not proved that an intrinsic centralizer f… Where: D.3 arbitrary-frontier descent. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:34: - **LM4 D.12** [Open (the return's claim)] The universal admissible level-zero kernel For an admissible punctured surface, with actual homeomorphism group $A$, a strict action $u:\Gamma\to A$, and $H=u(\Gamma)$, the unresolved comparison of LM4 C.12 is injectivity of \[ \pi_1(C_A(H),1)\longrightarrow\pi_1(A,1)^\Gamma. \] For hyperbolic finite-type surfaces the target is… Where: D.3 general level-zero comparison. (LM4_SUCCESSOR_results.csv)
```

**Executed query:** `L172\.4|L192\.1|R06`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **6 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:632: ### L192.1
context/same_cote_84/MPL_84_146-193_notes.md:1650: ### R06 — Tensor realization and abstract product must be separated
context/same_cote_84/MPL_84_146-193_notes.md:1724: | 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
context/same_cote_84/MPL_84_146-193_notes.md:1741: | 192 | “ça croule si 2=0, b1=b2=0” (the two French words remain doubtful) | Explicit failure warning; L192.1. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A09 — Hua's local formula matches the frozen signs on scan 104

**Context:** C84, L172.1–L172.2 (scan 172), R05 (scan 172), R10 (claim audit). **Relation:** restates. **RESULTS_STATE:** RS-product; RS-later.

**Executed query:** `b_1b_2|b₁b₂|4c_1c_2|4c₁c₂`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **11 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:36: | \(b=b_1\otimes b_2\) in split coordinates | Scan 146 circles \(b=b_1b_2\) and writes coordinate changes. | Direct local evidence; global descent is not proved by the circled formula alone. |
context/same_cote_84/MPL_84_146-193_notes.md:56: The circled “\(b=b_1b_2\)” is accompanied by the changes “`b'_1=b_1+\unsure{\chi|\gamma}u_1`” and “`b'_2=b_2+\unsure{\chi|\gamma}u_2`,” so a proof must check independence of splittings rather than simply multiply two chosen coordinates. This supports the local coefficient part of Hua’s claim, while the tensor interpretation requires the indicated Hom domains and the surviving doubt over the scalar to be respected. It does not itself construct associativity, a unit, or an inverse.
context/same_cote_84/MPL_84_146-193_notes.md:68: If the scalar in “`b'_i=b_i+\unsure{\chi|\gamma}u_i`” is \(\chi\), then \(b'_1b'_2-b_1b_2=\chi(u_1b_2+b_1u_2+\chi u_1u_2)\), so the product is independent of this change modulo \(\chi\). This suggests separating a residue invariant on \(V(\chi)\) from a globally defined product extension and its coherence data. The computation is compatible with the locus occurring in Hua’s invertibility statement, but neither a section called \(T_0\) nor that invertibility criterion occurs in this interval.
context/same_cote_84/MPL_84_146-193_notes.md:288: Under the monic local presentations \(u_i^2+b_i u_i+c_i=0\), the displayed \(u\) satisfies \(u^2+b_1b_2u+b_1^2c_2+b_2^2c_1-4c_1c_2=0\) over every commutative base ring; the accompanying script verifies the universal polynomial remainder over the integers. This establishes the local identity independently of whether the resulting abstract quadratic algebra embeds into the tensor product.
context/same_cote_84/MPL_84_146-193_notes.md:328: The local tensor operator \(T=1+\sigma_1\otimes\sigma_2\) admits maps \(i:A\to B\) and \(q:B\to A\) with \(iq=T\) and \(qi=2\operatorname{id}\); in the basis \((1,u_1,u_2,u_1u_2)\), \(q\) takes the values \((2,-b_1,-b_2,t+b_1b_2)\). These identities explain the displayed factor “2” and imply \(T^2=2T\): \(T\) is generally not idempotent, whereas \(T/2\) is a projector when two is invertible. The script verifies the matrices universally; identification with every doubtful arrow in the drawn diagram remains a reading question.
context/same_cote_84/MPL_84_146-193_notes.md:376: **Brief quotation:** `u_1\ast u_2-b_1b_2=\deleted{\unsure{2}}u`
context/same_cote_84/MPL_84_146-193_notes.md:378: The coefficient calculation concludes that the abstract product generator differs from \(u_1*u_2\) by the scalar \(b_1b_2\), while the scalar coefficient is extracted by pairing with \(x\). Its tensor image agrees with scan 172’s formula, but the abstract element and its potentially noninjective tensor image must be distinguished.
context/same_cote_84/MPL_84_146-193_notes.md:548: The four-entry table agrees with \(1+\sigma_1\otimes\sigma_2\) in the specialization \(b_1=b_2=0\), as also suggested by the nearby relations \(-u_i^2=c_i\). For general coefficients the middle entries are \(-b_1\) and \(-b_2\), and the last is \(2u_1u_2+b_2u_1+b_1u_2+b_1b_2\); the source’s uncertain indices must not be normalized to this interpretation.
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:115: - **84-product-quadratic-algebras-formula** (cote 84, their pp. 62–79, 88–90, 98–105; our scans 099, 100, 101, 102, 103, 104, 105, 106) [literature: Matched for the product of quadratic algebras a…] Over any base, without dividing by 2, quadratic algebras carry a commutative product with L(X₁ * X₂) = L₁ ⊗ L₂ and, in split coordinates, b = b₁b₂, c = c₁b₂² + c₂b₁² − 4c₁c₂, hence δ = δ₁δ₂, the generator mapping to 2U₁U₂ + b₁U₂ + b₂U₁ in A₁ ⊗ A₂. Our intake: new to us: our package for this cote is waiting
```

**Executed query:** `84-product-quadratic-algebras-formula|L172\.1|R05`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:7: This report contains **208 individually identified items**: 38 early mathematical notes (E146.1–E170.5), 39 later mathematical notes (L172.1–L192.4), 118 notes on reused typescript (T147.1–T193.5), and 13 comparisons or editorial investigations (R01–R13). Source references identify the exact per-scan file; approximate line numbers refer to the frozen TeX rather than physical manuscript lines. Diplomatic doubt macros reproduced in quotations retain their editorial meaning: a `\unsure` is not automatically an uncertainty expressed by the author, and a cancelled claim is not live text.
context/same_cote_84/MPL_84_146-193_notes.md:15: - **A precise local algebraic result:** scans 172 and 192 give a quadratic-algebra product whose relation and discriminant formula check over the integer polynomial ring; its local formula matches Voight (2016, Construction 3.14) after an explicit generator shift (L172.1–L172.2, R05).
context/same_cote_84/MPL_84_146-193_notes.md:282: ### L172.1
context/same_cote_84/MPL_84_146-193_notes.md:1644: ### R05 — The local algebra product has a precise published counterpart
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:115: - **84-product-quadratic-algebras-formula** (cote 84, their pp. 62–79, 88–90, 98–105; our scans 099, 100, 101, 102, 103, 104, 105, 106) [literature: Matched for the product of quadratic algebras a…] Over any base, without dividing by 2, quadratic algebras carry a commutative product with L(X₁ * X₂) = L₁ ⊗ L₂ and, in split coordinates, b = b₁b₂, c = c₁b₂² + c₂b₁² − 4c₁c₂, hence δ = δ₁δ₂, the generator mapping to 2U₁U₂ + b₁U₂ + b₂U₁ in A₁ ⊗ A₂. Our intake: new to us: our package for this cote is waiting
```

## A10 — The relative trace factorization contains an essential factor two

**Context:** C84, L172.5 (scan 172). **Relation:** restates. **RESULTS_STATE:** RS-product, RS-later.

**Executed query:** `qi=2|iq=|projector|idempotent`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **3 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:62: For the two displayed matrices “\(\begin{pmatrix}2&0\\-b_1&0\end{pmatrix}\)” and “\(\begin{pmatrix}0&0\\b_1&2\end{pmatrix}\),” direct multiplication gives sum \(2I\), both cross-products zero, and squares equal to twice the respective matrix. These are integral identities, but replacing either matrix by half of itself to obtain an idempotent would require an additional hypothesis. `early_formula_checks.py` verifies the four identities without deciding the doubtful names of the operators.
context/same_cote_84/MPL_84_146-193_notes.md:328: The local tensor operator \(T=1+\sigma_1\otimes\sigma_2\) admits maps \(i:A\to B\) and \(q:B\to A\) with \(iq=T\) and \(qi=2\operatorname{id}\); in the basis \((1,u_1,u_2,u_1u_2)\), \(q\) takes the values \((2,-b_1,-b_2,t+b_1b_2)\). These identities explain the displayed factor “2” and imply \(T^2=2T\): \(T\) is generally not idempotent, whereas \(T/2\) is a projector when two is invertible. The script verifies the matrices universally; identification with every doubtful arrow in the drawn diagram remains a reading question.
context/same_cote_84/MPL_84_146-193_notes.md:508: The factorization \(iq=T,qi=2\operatorname{id}\) gives a precise explanation of the tempting half: restriction of the ordinary tensor pairing to the images of \(A\) and its abstract dual is twice the perfect abstract pairing. In characteristic two that restricted pairing can vanish even when abstract duality remains perfect, so trace degeneracy, tensor-embedding failure, and loss of abstract duality are distinct questions. Confidence: high for the stated local model, because the script verifies \(i^{\mathsf T}q^{\mathsf T}=2I\) as a universal matrix identity.
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:63: - **LM7 E.109** [Proved (the return's claim)] For the actual compact plus-quartic pro-five class-two arithmetic action, the entire outer central action class is carried by the rank-two pure-CM module M. An explicit integral coefficient projector Pi has a left inverse identit… Where: ['LM section51.16; folios733v--736v; scans172--178; the compact factor of the generalized Jacobian and the next arithme…. (LM7_FERMAT_TOWER_results.csv)
```

**Executed query:** `L172\.5|trace`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **12 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:88: ### E148.4 — The trace-like involution needs its algebraic setting
context/same_cote_84/MPL_84_146-193_notes.md:92: The identity “`u+\sigma(u)=\unsure{(\lambda(u)+\mu(u))}\mathrm{id}`” resembles the trace-plus-conjugate identity later used on scans 160 and 172. It gives a candidate trace scalar, but this line alone does not prove multiplicativity or anti-multiplicativity of \(\sigma\), nor identify \(\mathcal H\) with a quadratic algebra. Those extra properties must be checked in the actual endomorphism algebra rather than inferred from the notation.
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
context/same_cote_84/MPL_84_146-193_notes.md:408: The displayed trace reformulation ends at “\(2\cdot\),” and the marginal boxed tensor image also has a doubtful terminal mark. The nearby complete identities can explain the intended calculation, but they do not authorize filling this unfinished line in the frozen text.
context/same_cote_84/MPL_84_146-193_notes.md:488: The cancelled half-trace and the later unfinished \(\tfrac12\)-expression show that normalization by two was considered but not retained as a completed definition here. A division-free proof must use the boundary identities and quotient relations directly, especially in characteristic two.
context/same_cote_84/MPL_84_146-193_notes.md:508: The factorization \(iq=T,qi=2\operatorname{id}\) gives a precise explanation of the tempting half: restriction of the ordinary tensor pairing to the images of \(A\) and its abstract dual is twice the perfect abstract pairing. In characteristic two that restricted pairing can vanish even when abstract duality remains perfect, so trace degeneracy, tensor-embedding failure, and loss of abstract duality are distinct questions. Confidence: high for the stated local model, because the script verifies \(i^{\mathsf T}q^{\mathsf T}=2I\) as a universal matrix identity.
context/same_cote_84/MPL_84_146-193_notes.md:568: The dual description is reduced from a bilinear form with two auxiliary functionals to a bilinear form with one scalar \(\lambda\). The cancelled conditions labelled a) and b), including the doubled \(2g_i\) restrictions, are replaced by the two trace restrictions; the cancelled version should not be combined with the live one as simultaneous axioms.
context/same_cote_84/MPL_84_146-193_notes.md:578: The live trace restrictions are the natural annihilator conditions for the dual of the pushout presentation of \(A\). For the ordinary linear dual this follows from the universal property of the quotient without a projectivity assumption, whereas identifying that dual with the separately constructed \(E\) still requires the product pairing and, for perfect duality, finite local freeness.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A11 — The norm uniqueness assertion needs both values and polarization

**Context:** C84, L172.5 (scan 172), L190.2 (scan 190), with no relative rank-four-to-rank-two norm formula located. **Relation:** adds. **RESULTS_STATE:** RS-product.

**Executed query:** `quadratic.*unique|application quadratique unique|relative norm`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `L172\.5|L190\.2`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **2 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
context/same_cote_84/MPL_84_146-193_notes.md:602: ### L190.2
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A12 — A universal local relative norm completes the missing coefficients

**Context:** C84, L172.1/L172.5 (scan 172), L190.2 (scan 190): the product relation and trace are present, but not this relative form. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later. **Confidence:** high for the local identities, from exact universal monic reduction.

**Executed query:** `relative norm|mixed coefficients|polarization|polarisation`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `L172\.5|L190\.2|rank-four`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **7 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:19: - **No explicit B12 construction in the supplied interval:** no form of P¹, conic, rank-four central Azumaya algebra, or ternary-form/SO(3) identification is constructed here (R01–R04). The folder plan's B5 regular-polyhedron/congruence questions likewise receive no demonstrated step (R09).
context/same_cote_84/MPL_84_146-193_notes.md:44: The per-note searches cover all three supplied files and are recorded in context_queries_typed.json. For these typed leaves, the planning questions about B5 (regular maps/congruence levels) and B12 (conics, rank-four Azumaya algebras, and rank-three quadratic forms) concern different material. The absence of such assertions in the reused typescript does not settle their presence in the mathematical leaves.
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
context/same_cote_84/MPL_84_146-193_notes.md:602: ### L190.2
context/same_cote_84/MPL_84_146-193_notes.md:1624: The positive mathematical evidence is “extensions” on scan 170 and the two equations `u_i^2+b_i u_i+c_i=0` on scan 192: this interval develops rank-two extension and algebra constructions, and contains no explicit identification of forms of P¹ with conics, rank-four Azumaya algebras, or ternary quadratic forms. The query for “SO”, “GP”, “conique”, “Azumaya”, “P¹”, “rang 3”, and related forms finds the proposed bridge in `README.md`, under B12, but not as a construction in these pages. This answers the planning question with a negative finding for the supplied interval, not a claim about the rest of cote 84 or the neighbouring cotes 77 and 82. The context labels B12 an unchecked question inferred from folder titles, so these pages change its placement rather than refute the mathematical correspondences themselves.
context/same_cote_84/MPL_84_146-193_notes.md:1626: ### R02 — A rank-four tensor product here is not a quaternion algebra
context/same_cote_84/MPL_84_146-193_notes.md:1630: Under the displayed quadratic-algebra interpretation, `A₁⊗A₂` has rank four but is commutative; its centre is the entire rank-four algebra, so it is not the degree-two central Azumaya algebra required by B12 over a nonzero base. The distinction matters because rank alone does not connect this tensor product with a quaternion algebra or a conic. The context search finds “Azumaya” only in `README.md`'s proposed B12, while `notes/RESULTS_STATE.md`, Hua's `84-chi-trivialised-extension-product`, instead concerns the rank-two product; the present observation separates those two leads.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A13 — Norm transitivity does not require cancelling the product embedding

**Context:** C84, L172.4–L172.5 (scan 172), L190.2 (scan 190). **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

**Executed query:** `transitiv|four conjugates|quatre conjugu`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `L172\.4|L172\.5`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **3 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
context/same_cote_84/MPL_84_146-193_notes.md:1724: | 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A14 — The new axioms allow nonflat and nonfaithful scalar maps

**Context:** C84, L172.4 (scan 172), on a noninjective map between free algebras, which is a different situation; no “quasi-quadratique” axiomatization located. **Relation:** differs. **RESULTS_STATE:** RS-product concerns actual quadratic algebras; no direct entry for the enlarged axioms.

**Executed query:** `quasi.?quadrati|ni même plat`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `noninject|non-inject|L172\.4`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **3 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:378: The coefficient calculation concludes that the abstract product generator differs from \(u_1*u_2\) by the scalar \(b_1b_2\), while the scalar coefficient is extracted by pairing with \(x\). Its tensor image agrees with scan 172’s formula, but the abstract element and its potentially noninjective tensor image must be distinguished.
context/same_cote_84/MPL_84_146-193_notes.md:1724: | 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A15 — Norm invariance is proved after its separate axiom is withdrawn

**Context:** C84, E148.4 (scan 148), on the distinction between conjugation identities and multiplicativity; no matching derivation of norm invariance located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `norm.*invar|n.*bar.*n|invariance`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **7 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:152: “Si \(\chi=2\), on \unsure{peut} prendre \(\delta=1\)” leads to the expression ending “\(x_1\otimes x_2+\bar x_1\otimes\bar x_2\qquad\text{o.K.}\).” The coefficient expansion is correct when \(\pi_i(x_i)=x_i-\bar x_i\), but one intermediate bar is itself doubtful in the transcription. The check establishes the interpreted polynomial identity, not a reading correction or a global categorical theorem.
context/same_cote_84/MPL_84_146-193_notes.md:154: ### E156.3 — A new bar formula is left unfinished
context/same_cote_84/MPL_84_146-193_notes.md:188: Scan 160 writes “\(\sigma(x)=\operatorname{Tr}(x).1-x\)” and boxes “\(x_1\otimes x_2+\pi'_1(x_1)\otimes\pi'_2(x_2)\),” while scan 162 defines \(\pi'(x)=\pi(x)-(\chi-1)x\). These operators can be related in the special case under discussion, but the notebook’s changes of notation and signs are not a licence to normalize the frozen primes, bars, or \(\sigma\) symbols. A rigorous reconstruction should state each chosen convention before comparing pairings.
context/same_cote_84/MPL_84_146-193_notes.md:436: **Brief quotation:** `\langle f,x+\bar x\rangle=\langle f,\pi(x)\rangle`
context/same_cote_84/MPL_84_146-193_notes.md:1708: | 150 | Crossed-out compatibility sentence and diagram; \(\chi\) visibly specialized to \(2\) in the double-bar calculation. | Withdrawal and local check, E150.1–E150.2. |
context/same_cote_84/MPL_84_146-193_notes.md:1740: | 190 | First coefficient pairing cancelled and replaced | The whole-product element replaces a bare `u` in the evaluation; preserved in L190.3. |
context/same_cote_84/MPL_84_146-193_notes.md:1910: | T154.3 / 154 | Endomorphism factorizations below the table | \(\alpha_i,\pi_i,\psi_i,\varpi_i\), several doubtful primes/bars | 2 factor rows | Recalculate after fixing types and conventions; no independent numerical result. |
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:20: - **CYCLOTOMIC_KERNEL D13** [Open (the return's claim)] D(e) remains unfinished for discontinuous actions normalizing no finite-level deck group and for the affine commensurator-completion description; the exact abstract-cocycle construction problem is stated for the U03 Poincare curve over Qbar. Where: section 3; pp.30-31; scans 62-63. (CYCLOTOMIC_KERNEL_results.csv)
```

**Executed query:** `multiplicativ|E148\.4`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:52: ### E146.1 — The multiplicative coefficient is a local assertion
context/same_cote_84/MPL_84_146-193_notes.md:88: ### E148.4 — The trace-like involution needs its algebraic setting
context/same_cote_84/MPL_84_146-193_notes.md:92: The identity “`u+\sigma(u)=\unsure{(\lambda(u)+\mu(u))}\mathrm{id}`” resembles the trace-plus-conjugate identity later used on scans 160 and 172. It gives a candidate trace scalar, but this line alone does not prove multiplicativity or anti-multiplicativity of \(\sigma\), nor identify \(\mathcal H\) with a quadratic algebra. Those extra properties must be checked in the actual endomorphism algebra rather than inferred from the notation.
context/same_cote_84/MPL_84_146-193_notes.md:1672: The multiplicative discriminant formula is a calculation in quadratic algebras, whereas `LM2_CONGRUENCE_ROWS.md` concerns arithmetic and GT actions on congruence quotients, including the still-open two-coordinate realization problem `LM2 C.d5`. Neither a modular curve X(n), a regular polyhedron over a ring, nor an action of GT is constructed in these pages, so the formula supplies no demonstrated step toward C.d5, `LM2 B.f7`, or `LM2 E.3`. The common vocabulary of determinants, norms, extensions or quadratic data does not establish a map between the problems; B5 remains an unchecked planning bridge here. The other open IDs in `notes/RESULTS_STATE.md` are consequently not reported as settled or advanced by this packet.
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:93: - **MPL_84_146-193 R09** [No demonstrated route to the LM2 congru… (research note of a returned package, first pass; a lead)] R09 — No demonstrated route to the LM2 congruence questions: **Source:** `pages/MPL_84_146-193_84_scan172.tex`, “δ=δ₁δ₂”; comparison across scans 146–193. **Kind:** reading question / context comparison. The multiplicative discriminant formula is a calculatio… (MPL_84_146-193_notes.md)
```

## A16 — When two is invertible the form reconstructs multiplication

**Context:** C84, E148.4 (scan 148), L172.5 (scan 172), for distinct warnings about multiplicativity and division by two. **Relation:** adds. **RESULTS_STATE:** no direct entry for this reconstruction.

**Executed query:** `multiplication.*(form|trace)|facteur.*2`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **1 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:62: For the two displayed matrices “\(\begin{pmatrix}2&0\\-b_1&0\end{pmatrix}\)” and “\(\begin{pmatrix}0&0\\b_1&2\end{pmatrix}\),” direct multiplication gives sum \(2I\), both cross-products zero, and squares equal to twice the respective matrix. These are integral identities, but replacing either matrix by half of itself to obtain an idempotent would require an additional hypothesis. `early_formula_checks.py` verifies the four identities without deciding the doubtful names of the operators.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `E148\.4|division|L172\.5`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **13 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:35: | Product by amalgamated sum without division | Scans 168 and 170 explicitly mark the relevant squares “cocart”; their structural maps use \(\pi_i\), not division by \(\chi\). | Supported as a construction plan; tensor exactness and the resulting splitting data still need proof in the stated category. |
context/same_cote_84/MPL_84_146-193_notes.md:58: ### E146.2 — The two displayed matrices do not require division by two
context/same_cote_84/MPL_84_146-193_notes.md:88: ### E148.4 — The trace-like involution needs its algebraic setting
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
context/same_cote_84/MPL_84_146-193_notes.md:330: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) supplies a conjectural division-free product lead; this scan adds a concrete factorization whose rank behavior needs hypotheses distinct from categorical existence.
context/same_cote_84/MPL_84_146-193_notes.md:450: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) directly predicts a division-free amalgamated construction; these later pages give more explicit presentations while leaving algebra and coherence claims to be checked separately.
context/same_cote_84/MPL_84_146-193_notes.md:488: The cancelled half-trace and the later unfinished \(\tfrac12\)-expression show that normalization by two was considered but not retained as a completed definition here. A division-free proof must use the boundary identities and quotient relations directly, especially in characteristic two.
context/same_cote_84/MPL_84_146-193_notes.md:490: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) explicitly advertises a construction without division; this page is consistent with that aim but records an abandoned or unfinished normalization route rather than completing the proof.
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:116: - **84-chi-trivialised-extension-product** (cote 84, their pp. 65–79, 123–131, 141–169; our scans 124, 125, 126, 127, 128, 129, 130, 131, 132, 142, 143, 144, 145) [conjecture (candidate: their search found no reference) | L…] For any fixed χ ∈ Γ(𝒪), extensions 0 → L → E → M → 0 equipped with a χ-splitting (π, ϖ) form a symmetric monoidal category under a product built by amalgamated sum without division, with b = b₁ ⊗ b₂ in split coordinates; for M = 𝒪 an object is invertible iff its section T₀ generates L on V(χ), and the pushout and pullback products agree… Our intake: new to us: our package for this cote is waiting
```

## A17 — The polarization identity is an extra requirement without faithfulness

**Context:** C84, E148.4 (scan 148), L172.4 (scan 172); no exact quasi-quadratic polarization axiom located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `polarization|polarisation|varphi_n`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `injectiv|E148\.4|L172\.4`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **10 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:34: | Extensions with a fixed \(\chi\)-splitting | Scan 170 gives the extension diagrams and identities; scans 146–168 calculate with them. | Supported as the intended objects, subject to the written universal-injectivity and local-freeness hypotheses and the frozen sign doubt. |
context/same_cote_84/MPL_84_146-193_notes.md:88: ### E148.4 — The trace-like involution needs its algebraic setting
context/same_cote_84/MPL_84_146-193_notes.md:254: “On définit de façon \unsure{can.}” introduces the two extension products, while the margin calls the inclusions “\unsure{univ.} \unsure{injectfs|injectifs}.” The pushout and pullback diagrams give a concrete construction plan, but exactness of their tensor rows requires the stated universal-injectivity or suitable flatness assumptions. This is substantially more specific than an unqualified operation on every extension of arbitrary modules.
context/same_cote_84/MPL_84_146-193_notes.md:308: The marginal qualification singles out precisely the field case in which the indicated image of the abstract generator loses its nonconstant part. Scan 192’s “ça croule” repeats the same exceptional specialization, but neither passage by itself gives the general base-ring injectivity criterion.
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:378: The coefficient calculation concludes that the abstract product generator differs from \(u_1*u_2\) by the scalar \(b_1b_2\), while the scalar coefficient is extracted by pairing with \(x\). Its tensor image agrees with scan 172’s formula, but the abstract element and its potentially noninjective tensor image must be distinguished.
context/same_cote_84/MPL_84_146-193_notes.md:630: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is the related product lead; this page adds a dual-basis construction that must be separated from any claim of tensor-product injectivity.
context/same_cote_84/MPL_84_146-193_notes.md:1724: | 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
```

- `context/notes/RESULTS_STATE.md`: **2 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:32: - **LM4 D.10** [Open (the return's claim)] Arbitrary-frontier descent in the exact comparison Let $U$ be a simply connected open orbit in the original surface. The prime-end disk need not map continuously onto its closure. When the interior identification has such an extension, its boundary map may fail to be injective. We have not proved that an intrinsic centralizer f… Where: D.3 arbitrary-frontier descent. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:34: - **LM4 D.12** [Open (the return's claim)] The universal admissible level-zero kernel For an admissible punctured surface, with actual homeomorphism group $A$, a strict action $u:\Gamma\to A$, and $H=u(\Gamma)$, the unresolved comparison of LM4 C.12 is injectivity of \[ \pi_1(C_A(H),1)\longrightarrow\pi_1(A,1)^\Gamma. \] For hyperbolic finite-type surfaces the target is… Where: D.3 general level-zero comparison. (LM4_SUCCESSOR_results.csv)
```

## A18 — The transitivity condition is optional and concerns forms

**Context:** C84, L190.2 (scan 190), on an ordinary quadratic norm; no matching optional tower axiom located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `facultati|2n.*forme|tower`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **11 matching lines**; shown below (first eight; all in JSON).

```text
context/notes/RESULTS_STATE.md:13: - **LM7 E.23** [Open (the return's claim)] The complete set of continuous section classes for the geometric metabelian and marked depth-two arithmetic quotients of $U_3/\mathbb Q$ is not determined in this return. The remaining calculation is the image and every fiber of their section maps to E.16. E.37 determines the full intrinsic pro-$3$ class-two section map over ev… Where: §51.16; folios 733v–736v; scans 172–178; (369)–(379). (LM7_FERMAT_TOWER_results.csv)
context/notes/RESULTS_STATE.md:22: - **IMPL P5** [candidate prompt item: open] **P5 (shape map; from I5).** Statement: the three regimes as one trichotomy for a tower (or diagram) of complexes: (i) gap closes, class in `closure(im)/im` (F.15, F.21, E.32); (ii) uniform gap, obstruction present at every level and of closed range (T A.18, A.24); (iii) finite-level classes killed by later maps, Mittag-Leffler… (IMPLICATIONS.md)
context/notes/RESULTS_STATE.md:37: - **LM7 D.19** [Open (the return's claim)] The residual GT and full profinite realization questions Where: §51.16; folio734 verso; scan174; residual D tasks. (LM7_FERMAT_TOWER_results.csv)
context/notes/RESULTS_STATE.md:53: - **LM7 D.40** [Proved (the return's claim)] The actual source image R in the product of all finite perfect marked B=C2*C3 quotients has maximal prosolvable quotient exactly the marked C6. D39 extends to an actual continuous multiplier-one peripheral automorphism on T fiber… Where: ['Part D(e); section51.16, folio734 verso, scan174', 'D-after-LM2(1); section51.15, folios725-727, scans156-160']. (LM7_FERMAT_TOWER_results.csv)
context/notes/RESULTS_STATE.md:57: - **FLAGGED_149 B5** [Proved (the return's claim)] Corollaries 1(b), 2(c)--(d), and 3 with all comparison maps — A hyperbolic polycurve means a finite tower of smooth pairs whose geometric curve fibres have $2g-2+r>0$, including proper fibres. Over a field finitely generated over… Where: cote 149; section 1; pp. 11–15; scans 24–31. (FLAGGED_149_results.csv)
context/notes/RESULTS_STATE.md:61: - **LM7 D.41** [Proved (the return's claim)] The actual simultaneous source image over every marked epimorphism B=C2*C3 to a full S_n, n>=5, is the full common-sign fibre product, with even subgroup the product of its marked alternating factors. Its maximal common quotient… Where: ['Part D(e); section51.16, folio734 verso, scan174', 'D-after-LM2(1); section51.15, folios725-727, scans156-160']. (LM7_FERMAT_TOWER_results.csv)
context/notes/RESULTS_STATE.md:62: - **LM7 D.42** [Proved (the return's claim)] The actual D41 PGL2(F7) residual extends through the full relative pronilpotent completion of its rank57 free kernel, simultaneously at every prime. The exact maximal common marked quotient with W is C54=lim B/[L54,L54]L54^(3^n),… Where: ['Part D(e); section51.16, folio734 verso, scan174', 'D-after-LM2(1); section51.15, folios725-727, scans156-160']. (LM7_FERMAT_TOWER_results.csv)
context/notes/RESULTS_STATE.md:63: - **LM7 E.109** [Proved (the return's claim)] For the actual compact plus-quartic pro-five class-two arithmetic action, the entire outer central action class is carried by the rank-two pure-CM module M. An explicit integral coefficient projector Pi has a left inverse identit… Where: ['LM section51.16; folios733v--736v; scans172--178; the compact factor of the generalized Jacobian and the next arithme…. (LM7_FERMAT_TOWER_results.csv)
```

**Executed query:** `norm|L190\.2`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **2 matching lines**; shown below.

```text
context/LM2_CONGRUENCE_ROWS.md:11: | LM2 C.d2 | Correct matrix norm equations and both residual characters | claim (return: Proved) | §46; fols398,400; scans198(73),202–203(88) |
context/LM2_CONGRUENCE_ROWS.md:13: | LM2 C.d4 | Adelic group determined as an intrinsic normalizer fiber product | claim (return: Proved) | §46; fol395 verso,401; scans193,204–205; §48; scans254–266 |
```

- `context/same_cote_84/MPL_84_146-193_notes.md`: **14 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:104: The calculation ending “\(=x_1\)” explicitly places \(2\) beneath \(\chi\), while the page also writes “\(\pi(\pi-\chi)=0\).” Under that latter relation, the map \(s=1-\pi\) satisfies \(s^2-1=(\chi-2)\pi\), so involutivity follows at \(\chi=2\) but need not hold for arbitrary \(\chi\). This explains why the scalar hypothesis must remain visible in any interpretation of the norm-like tensor formula.
context/same_cote_84/MPL_84_146-193_notes.md:118: ### E152.3 — The norm-like tensor formula is cancelled, then checked later
context/same_cote_84/MPL_84_146-193_notes.md:188: Scan 160 writes “\(\sigma(x)=\operatorname{Tr}(x).1-x\)” and boxes “\(x_1\otimes x_2+\pi'_1(x_1)\otimes\pi'_2(x_2)\),” while scan 162 defines \(\pi'(x)=\pi(x)-(\chi-1)x\). These operators can be related in the special case under discussion, but the notebook’s changes of notation and signs are not a licence to normalize the frozen primes, bars, or \(\sigma\) symbols. A rigorous reconstruction should state each chosen convention before comparing pairings.
context/same_cote_84/MPL_84_146-193_notes.md:388: The attempted coefficient value two is cancelled and replaced by the factorwise pairing calculation giving one; the crossed-out twos in the concluding formulas implement that correction. This is a substantive normalization change, not merely a discarded spelling, and it is essential when comparing the product with its tensor symmetrization.
context/same_cote_84/MPL_84_146-193_notes.md:488: The cancelled half-trace and the later unfinished \(\tfrac12\)-expression show that normalization by two was considered but not retained as a completed definition here. A division-free proof must use the boundary identities and quotient relations directly, especially in characteristic two.
context/same_cote_84/MPL_84_146-193_notes.md:490: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) explicitly advertises a construction without division; this page is consistent with that aim but records an abandoned or unfinished normalization route rather than completing the proof.
context/same_cote_84/MPL_84_146-193_notes.md:510: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) provides the broader comparison problem; this is an additional explanation of the normalization obstacle, not a proof of its full monoidal claim.
context/same_cote_84/MPL_84_146-193_notes.md:548: The four-entry table agrees with \(1+\sigma_1\otimes\sigma_2\) in the specialization \(b_1=b_2=0\), as also suggested by the nearby relations \(-u_i^2=c_i\). For general coefficients the middle entries are \(-b_1\) and \(-b_2\), and the last is \(2u_1u_2+b_2u_1+b_1u_2+b_1b_2\); the source’s uncertain indices must not be normalized to this interpretation.
```

- `context/notes/RESULTS_STATE.md`: **7 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:20: - **CYCLOTOMIC_KERNEL D13** [Open (the return's claim)] D(e) remains unfinished for discontinuous actions normalizing no finite-level deck group and for the affine commensurator-completion description; the exact abstract-cocycle construction problem is stated for the U03 Poincare curve over Qbar. Where: section 3; pp.30-31; scans 62-63. (CYCLOTOMIC_KERNEL_results.csv)
context/notes/RESULTS_STATE.md:29: - **LM4 B.27** [Open (the return's claim)] The remaining arithmetic-character calculations The normalized Jacobi-sum values on \(G_{\mathbb Q(\zeta_{15})}\), the values for the R2 lifts at \(U=K\) and level thirty, and vanishing on \(\mathcal K\) remain undecided. B.21 supplies the cover and the precise rational representation; B.22 corrects the domains, the deck ambigu… Where: B.4.e;Lead7. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:30: - **LM4 B.39** [Open (the return's claim)] The nonsolvable direction and the published assertions For a finite solvable subgroup of a genus-zero mapping class group, the centralizer is the closure of the discrete centralizer, by the prime-power normalizer induction in B.30 and the open-kernel argument B.2. This proves the solvable direction of the refined triangle-orbif… Where: B.6;Lead4. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:45: - **LM7_PUSH E.67** [Proved (the return's claim; refereed 14 Nov 2026: general statements proved; the 48 per-word fibre claims not recomputed)] The original Mordell sign and the complete finite Gaussian norm comparison. Retain the separate original orbifold actions $\Omega_3,\Omega_4$ and their Ferrari homology matrices $B_3,B_4$ from E.64.28--29. For every multiplier-on… Where: E.3. (LM7_PUSH_results.csv)
context/notes/RESULTS_STATE.md:46: - **LM7_PUSH D.44** [Proved (the return's claim; refereed 14 Nov 2026: the parts D.50 and E.58 use proved as claimed)] Exact modular descent and gentle normalization over a coprime base. Let \(\widehat B=C_2\amalg C_3=\langle s,r\mid s^2=r^3=1\rangle\), let \(F=\ker(\widehat B\to\mathfrak S_3)\), and use \[ \tau=sr,\qquad x=\tau^{-2},\qquad y=sxs… Where: D.2. (LM7_PUSH_results.csv)
context/notes/RESULTS_STATE.md:50: - **LM7_PUSH E.70** [Proved (the return's claim)] The full Gaussian pro-three source and its compatible norm lifts. Let $P$ be the free pro-three group on $X,Y$, and form the actual relative Gaussian triangle \[ \begin{gathered} \mathfrak G=P\rtimes\langle d\rangle,\qquad d^4=1,… Where: E.3. (LM7_PUSH_results.csv)
context/notes/RESULTS_STATE.md:64: - **LM7 E.122** [Proved (the return's claim)] For beta_d^(3^d)=53*zeta3, B_d=Q(zeta9,beta_d) and S over3,53, every vertical three-primary S-class action is trivial. All actual norms A(B_(d+1))->A(B_d) are isomorphisms from d=2 onward, and the full groups and inverse limit ar… Where: LM section51.16, folios733v--736v, scans172--178, through the actual positional root-cubing and Kummer--Shapiro maps of…. (LM7_FERMAT_TOWER_results.csv)
```

## A19 — The five-axiom recap omits the earlier multiplicativity condition

**Context:** C84, E148.4 (scan 148), a related but different multiplicativity warning; exact searches for “quasi-quadratique” and this five-axiom issue are negative. **Relation:** adds. **RESULTS_STATE:** RS-product concerns actual quadratic algebras and does not settle this axiom question.

**Executed query:** `quasi.?quadrati`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `multiplicativ|five.axiom|E148\.4`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:52: ### E146.1 — The multiplicative coefficient is a local assertion
context/same_cote_84/MPL_84_146-193_notes.md:88: ### E148.4 — The trace-like involution needs its algebraic setting
context/same_cote_84/MPL_84_146-193_notes.md:92: The identity “`u+\sigma(u)=\unsure{(\lambda(u)+\mu(u))}\mathrm{id}`” resembles the trace-plus-conjugate identity later used on scans 160 and 172. It gives a candidate trace scalar, but this line alone does not prove multiplicativity or anti-multiplicativity of \(\sigma\), nor identify \(\mathcal H\) with a quadratic algebra. Those extra properties must be checked in the actual endomorphism algebra rather than inferred from the notation.
context/same_cote_84/MPL_84_146-193_notes.md:1672: The multiplicative discriminant formula is a calculation in quadratic algebras, whereas `LM2_CONGRUENCE_ROWS.md` concerns arithmetic and GT actions on congruence quotients, including the still-open two-coordinate realization problem `LM2 C.d5`. Neither a modular curve X(n), a regular polyhedron over a ring, nor an action of GT is constructed in these pages, so the formula supplies no demonstrated step toward C.d5, `LM2 B.f7`, or `LM2 E.3`. The common vocabulary of determinants, norms, extensions or quadratic data does not establish a map between the problems; B5 remains an unchecked planning bridge here. The other open IDs in `notes/RESULTS_STATE.md` are consequently not reported as settled or advanced by this packet.
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:93: - **MPL_84_146-193 R09** [No demonstrated route to the LM2 congru… (research note of a returned package, first pass; a lead)] R09 — No demonstrated route to the LM2 congruence questions: **Source:** `pages/MPL_84_146-193_84_scan172.tex`, “δ=δ₁δ₂”; comparison across scans 146–193. **Kind:** reading question / context comparison. The multiplicative discriminant formula is a calculatio… (MPL_84_146-193_notes.md)
```

## A20 — A finite counterexample separates the two axiom lists

**Context:** C84, no matching weak-axiom example; E148.4 (scan 148) concerns a different implication. **Relation:** adds. **RESULTS_STATE:** no direct entry; RS-product is about actual quadratic algebras. **Confidence:** high, from the coefficient proof and exhaustive finite check.

**Executed query:** `quasi.?quadrati|five.axiom|Z/4|mathbb Z/4`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **3 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:318: For the displayed local model, \(i:R[t]/(t^2+bt+c)\to B=A_1\otimes_R A_2\), \(t\mapsto2u_1u_2+b_2u_1+b_1u_2\), has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\), because the four tensor-basis coefficients of \(i(a+dt)\) are \((a,db_2,db_1,2d)\). Thus \(R=\mathbb Z/4\mathbb Z\), \(b_1=b_2=c_1=c_2=0\), gives the nonzero kernel element \(2t\), while a split injection requires the stronger condition \((2,b_1,b_2)=R\). Confidence: high for this conditional algebraic statement, since it is a direct coefficient calculation and the script independently enumerates the small-ring examples.
context/same_cote_84/MPL_84_146-193_notes.md:2037: The script also enumerates kernels over `Z/4Z` for `(b1,b2)=(0,0),(2,0),(1,0)` and `Z/6Z` for `(0,0),(3,0)`, always with `c1=c2=0`. The kernel sizes are respectively `2,2,1,2,1`, exactly as predicted by `Ann(2,b1,b2)`.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `multiplicativ|E148\.4`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:52: ### E146.1 — The multiplicative coefficient is a local assertion
context/same_cote_84/MPL_84_146-193_notes.md:88: ### E148.4 — The trace-like involution needs its algebraic setting
context/same_cote_84/MPL_84_146-193_notes.md:92: The identity “`u+\sigma(u)=\unsure{(\lambda(u)+\mu(u))}\mathrm{id}`” resembles the trace-plus-conjugate identity later used on scans 160 and 172. It gives a candidate trace scalar, but this line alone does not prove multiplicativity or anti-multiplicativity of \(\sigma\), nor identify \(\mathcal H\) with a quadratic algebra. Those extra properties must be checked in the actual endomorphism algebra rather than inferred from the notation.
context/same_cote_84/MPL_84_146-193_notes.md:1672: The multiplicative discriminant formula is a calculation in quadratic algebras, whereas `LM2_CONGRUENCE_ROWS.md` concerns arithmetic and GT actions on congruence quotients, including the still-open two-coordinate realization problem `LM2 C.d5`. Neither a modular curve X(n), a regular polyhedron over a ring, nor an action of GT is constructed in these pages, so the formula supplies no demonstrated step toward C.d5, `LM2 B.f7`, or `LM2 E.3`. The common vocabulary of determinants, norms, extensions or quadratic data does not establish a map between the problems; B5 remains an unchecked planning bridge here. The other open IDs in `notes/RESULTS_STATE.md` are consequently not reported as settled or advanced by this packet.
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:93: - **MPL_84_146-193 R09** [No demonstrated route to the LM2 congru… (research note of a returned package, first pass; a lead)] R09 — No demonstrated route to the LM2 congruence questions: **Source:** `pages/MPL_84_146-193_84_scan172.tex`, “δ=δ₁δ₂”; comparison across scans 146–193. **Kind:** reading question / context comparison. The multiplicative discriminant formula is a calculatio… (MPL_84_146-193_notes.md)
```

## A21 — The three intermediate algebras are part of an enlarged formal setup

**Context:** C84, no exact “biquadratique” or three-intermediate-algebra setup located; L172.4 (scan 172) concerns a different noninjective realization map. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `biquadrati|trois.*alg|three.*algebra`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **1 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:44: The per-note searches cover all three supplied files and are recorded in context_queries_typed.json. For these typed leaves, the planning questions about B5 (regular maps/congruence levels) and B12 (conics, rank-four Azumaya algebras, and rank-three quadratic forms) concern different material. The absence of such assertions in the reused typescript does not settle their presence in the mathematical leaves.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `quasi.?quadrati|L172\.4`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **2 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:1724: | 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A22 — The cancelled involution condition returns as a live axiom

**Context:** C84, no matching three-involution compatibility located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `sigma_1.*sigma_2.*sigma_3|three.*involution`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:27: - **LM4 A.14** [Open (the return's claim)] The three full conjugacy assertions We have not decided whether every involution of \(\mathcal P,\widehat{GT}_0,\widehat{GT}\) is conjugate to \(c\) in its respective group. A.2 detects conjugacy of a fixed pair on all relative levels; A.11 identifies the equivalent peripheral generation condition. Neither supplies the compatib… Where: Task A.8. (LM4_SUCCESSOR_results.csv)
```

**Executed query:** `biquadrati|compatibilit`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **1 matching lines**; shown below.

```text
context/LM2_CONGRUENCE_ROWS.md:12: | LM2 C.d3 | Exact local adelic solution locus, sign compatibility and §48 coboundary schemes | claim (return: Proved) | §46; fols400–401; scans202–205; §48; scans254–266 |
```

- `context/same_cote_84/MPL_84_146-193_notes.md`: **22 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:76: ### E148.2 — Three equations in the second ansatz require compatibility
context/same_cote_84/MPL_84_146-193_notes.md:94: ### E150.1 — Compatibility is explicitly crossed out
context/same_cote_84/MPL_84_146-193_notes.md:98: The line beginning “Mais” and containing “\unsure{une} \unsure{compatibilité} \unsure{avec la} `\unsure{\pi|\tau}`-\unsure{trivialisation}” is struck through, together with the adjacent candidate diagram. It therefore records an abandoned formulation, not an accepted compatibility theorem. The later construction on scan 170 must be assessed on its own explicit conditions.
context/same_cote_84/MPL_84_146-193_notes.md:110: The author cancels “\(2\chi=\chi\)” and writes “\(\chi=\chi\quad\text{o.K.!}\).” The preceding polynomial \(-\chi(1-\gamma\chi)+2(1-\gamma\chi)\chi+\gamma\chi^2\) is indeed identically \(\chi\), as the accompanying script checks. This verifies that scalar restriction only, not every compatibility of the full extension map.
context/same_cote_84/MPL_84_146-193_notes.md:130: ### E154.2 — Two compatibilities leave a Hom-valued ambiguity
context/same_cote_84/MPL_84_146-193_notes.md:134: The doubtful prose says the two “\unsure{homotopies|contraintes}” are compatible and leave an “\unsure{indétermination}” which is a Hom from \(M_1\otimes M_2\) to \(L_1\otimes L_2\). This is consistent with the familiar freedom to alter an extension morphism fixing its ends by a map from the quotient to the subobject, but existence and compatibility with the chosen \(\chi\)-trivialisations still require proof. In particular, the stated ambiguity cannot itself establish a unique natural comparison or monoidal coherence.
context/same_cote_84/MPL_84_146-193_notes.md:200: The thick top arrow between the tensor terms is labelled “?”. Its factorization through \(E\), and compatibility with the amalgamated sum below, are precisely what need to be constructed rather than assumed. The four-term polynomial at the foot of the page is an ansatz for this problem, not a finished proof.
context/same_cote_84/MPL_84_146-193_notes.md:230: “Pour définir un hom \(F\), il faut définir” introduces \(F_{11},F_{12},F_{21},F_{22}\) and the marginal “\unsure{ces} 4 \unsure{carrés} commu-\linebreak\unsure{tatifs}.” The page states the conditions \(F_{22}=0\), \(F_{21}=\alpha_1\otimes\alpha_2\), and \(F_{12}=\psi_1\otimes\psi_2\) as necessary and sufficient for successively stronger properties. The remaining block and its two nonautomatic squares still require construction; three specified blocks are not all four compatibilities.
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:25: - **LM2 E.3** [Open (the return's claim)] Does GT imply the corrected additional orbifold compatibility? Where: §41; fols.315–316 verso; scans54–57; §47; fols.415–425; scans229–250 (cote140-3). (LM2_LOOP_EQUATIONS_results.csv)
```

## A23 — Six compatibility squares do not assert tensor-product isomorphisms

**Context:** C84, E170.1 (scan 170), on exactness limitations; no matching six-square system located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `6 diagrammes|six.*(square|diagram)|noyau`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **2 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:86: The phrase “`\mathcal H_i=\text{\unsure{noyau} de}`” is unfinished, followed by the purported sequence from \(\operatorname{Hom}(M,L)\) through \(\mathcal H/\mathrm{id}\) to \((\mathcal O\times\mathcal O)/\mathcal O\). To assess exactness one must specify the omitted map, the action on both ends of the extension, and whether surjectivity is local or global. Hua’s category-level summary does not supply those missing definitions.
context/same_cote_84/MPL_84_146-193_notes.md:1198: “cinq ou six ébauches”: He reports reaching provisional satisfaction after five or six drafts, with a Christmas-tree-like diagram. The text describes that diagram; the supplied typed leaf does not display the complete eighteen-group graph.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `base change|chgt|E170\.1`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **2 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:250: ### E170.1 — Canonical product extensions need the tensor-exactness hypotheses
context/same_cote_84/MPL_84_146-193_notes.md:1718: | 170 | “On définit de façon \unsure{can.}”; “une … application can.”; no literal question mark. | Canonical construction/comparison asserted, E170.1–E170.2; coherence is not supplied. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A24 — The bilinear verification on scan 113 is marked complete

**Context:** C84, no matching relative-norm base-change verification located; compare L190.2 (scan 190) only for ordinary norm coordinates. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `Il reste à vérifier|bilin|polar`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **3 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:518: The two requested boundary values are exactly the tests needed to descend a bilinear form through the two displayed quotient presentations. They are requirements on a proposed form, not a completed proof that a form satisfying both exists and is nondegenerate.
context/same_cote_84/MPL_84_146-193_notes.md:568: The dual description is reduced from a bilinear form with two auxiliary functionals to a bilinear form with one scalar \(\lambda\). The cancelled conditions labelled a) and b), including the doubled \(2g_i\) restrictions, are replaced by the two trace restrictions; the cancelled version should not be combined with the live one as simultaneous axioms.
context/same_cote_84/MPL_84_146-193_notes.md:1954: | T188a | 188 / 20–26 | Data describing an element of the dual | Trial `(f,g1,g2)` replaced by `(f,λ)` | 3 trial data items reduced to 2 live data items | `f` is a bilinear form, not one scalar coordinate; these counts are components, not dimensions. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `relative norm|L190\.2`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **1 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:602: ### L190.2
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A25 — Two literal entries in the norm argument have incompatible types

**Context:** C84, L190.2 (scan 190), explicitly distinguishes trace and norm formulas; no matching discussion of scan 113 located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `t_1\(x_1\)|n_1\(x_1\)|chgt.*base`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `trace.*norm|norm.*trace|L190\.2`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:488: The cancelled half-trace and the later unfinished \(\tfrac12\)-expression show that normalization by two was considered but not retained as a completed definition here. A division-free proof must use the boundary identities and quotient relations directly, especially in characteristic two.
context/same_cote_84/MPL_84_146-193_notes.md:602: ### L190.2
context/same_cote_84/MPL_84_146-193_notes.md:610: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) contains no trace/norm calculation; LM2 C.d2 in `context/LM2_CONGRUENCE_ROWS.md` concerns different matrix-norm equations at cote 140-3 scans 198 and 202–203 and does not settle this local quadratic identity.
context/same_cote_84/MPL_84_146-193_notes.md:1957: | T190a | 190 / 10–12 | Trace and norm of an affine-linear generator | Here `λ` multiplies `u`, `μ` is constant | 2 formulas | Script checks `Tr=-λβ+2μ`, `N=λ²c+μ²−λμβ`; the frozen minus/plus uncertainty is not changed. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A26 — Common absolute trace is assumed when the base map is nonfaithful

**Context:** C84, L172.4 (scan 172), on the danger of cancelling a noninjective map; no common-trace axiom located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `common.*trace|trace.*commune|t_1.*T_1`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `injectiv|L172\.4`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **9 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:34: | Extensions with a fixed \(\chi\)-splitting | Scan 170 gives the extension diagrams and identities; scans 146–168 calculate with them. | Supported as the intended objects, subject to the written universal-injectivity and local-freeness hypotheses and the frozen sign doubt. |
context/same_cote_84/MPL_84_146-193_notes.md:254: “On définit de façon \unsure{can.}” introduces the two extension products, while the margin calls the inclusions “\unsure{univ.} \unsure{injectfs|injectifs}.” The pushout and pullback diagrams give a concrete construction plan, but exactness of their tensor rows requires the stated universal-injectivity or suitable flatness assumptions. This is substantially more specific than an unqualified operation on every extension of arbitrary modules.
context/same_cote_84/MPL_84_146-193_notes.md:308: The marginal qualification singles out precisely the field case in which the indicated image of the abstract generator loses its nonconstant part. Scan 192’s “ça croule” repeats the same exceptional specialization, but neither passage by itself gives the general base-ring injectivity criterion.
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:378: The coefficient calculation concludes that the abstract product generator differs from \(u_1*u_2\) by the scalar \(b_1b_2\), while the scalar coefficient is extracted by pairing with \(x\). Its tensor image agrees with scan 172’s formula, but the abstract element and its potentially noninjective tensor image must be distinguished.
context/same_cote_84/MPL_84_146-193_notes.md:630: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is the related product lead; this page adds a dual-basis construction that must be separated from any claim of tensor-product injectivity.
context/same_cote_84/MPL_84_146-193_notes.md:1724: | 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
context/same_cote_84/MPL_84_146-193_notes.md:1926: | T170.1 / 170 | Input extensions and splitting identities | \(i=1,2\); \(\chi\), universal injectivity | 2 extensions; 3 live displayed identity lines for each \(i\), one with `=\|+` doubt | Script uses the declared equality interpretation; no silent disambiguation. |
```

- `context/notes/RESULTS_STATE.md`: **2 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:32: - **LM4 D.10** [Open (the return's claim)] Arbitrary-frontier descent in the exact comparison Let $U$ be a simply connected open orbit in the original surface. The prime-end disk need not map continuously onto its closure. When the interior identification has such an extension, its boundary map may fail to be injective. We have not proved that an intrinsic centralizer f… Where: D.3 arbitrary-frontier descent. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:34: - **LM4 D.12** [Open (the return's claim)] The universal admissible level-zero kernel For an admissible punctured surface, with actual homeomorphism group $A$, a strict action $u:\Gamma\to A$, and $H=u(\Gamma)$, the unresolved comparison of LM4 C.12 is injectivity of \[ \pi_1(C_A(H),1)\longrightarrow\pi_1(A,1)^\Gamma. \] For hyperbolic finite-type surfaces the target is… Where: D.3 general level-zero comparison. (LM4_SUCCESSOR_results.csv)
```

## A27 — The norm argument proves a scalar equality only under faithfulness

**Context:** C84, E148.4 (scan 148), L172.4 (scan 172), for separate multiplicativity and faithfulness distinctions. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `quatre.*conjugu|four.*conjugate|n_1.*N_1`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `injectiv|multiplicativ|E148\.4`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **11 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:34: | Extensions with a fixed \(\chi\)-splitting | Scan 170 gives the extension diagrams and identities; scans 146–168 calculate with them. | Supported as the intended objects, subject to the written universal-injectivity and local-freeness hypotheses and the frozen sign doubt. |
context/same_cote_84/MPL_84_146-193_notes.md:52: ### E146.1 — The multiplicative coefficient is a local assertion
context/same_cote_84/MPL_84_146-193_notes.md:88: ### E148.4 — The trace-like involution needs its algebraic setting
context/same_cote_84/MPL_84_146-193_notes.md:92: The identity “`u+\sigma(u)=\unsure{(\lambda(u)+\mu(u))}\mathrm{id}`” resembles the trace-plus-conjugate identity later used on scans 160 and 172. It gives a candidate trace scalar, but this line alone does not prove multiplicativity or anti-multiplicativity of \(\sigma\), nor identify \(\mathcal H\) with a quadratic algebra. Those extra properties must be checked in the actual endomorphism algebra rather than inferred from the notation.
context/same_cote_84/MPL_84_146-193_notes.md:254: “On définit de façon \unsure{can.}” introduces the two extension products, while the margin calls the inclusions “\unsure{univ.} \unsure{injectfs|injectifs}.” The pushout and pullback diagrams give a concrete construction plan, but exactness of their tensor rows requires the stated universal-injectivity or suitable flatness assumptions. This is substantially more specific than an unqualified operation on every extension of arbitrary modules.
context/same_cote_84/MPL_84_146-193_notes.md:308: The marginal qualification singles out precisely the field case in which the indicated image of the abstract generator loses its nonconstant part. Scan 192’s “ça croule” repeats the same exceptional specialization, but neither passage by itself gives the general base-ring injectivity criterion.
context/same_cote_84/MPL_84_146-193_notes.md:378: The coefficient calculation concludes that the abstract product generator differs from \(u_1*u_2\) by the scalar \(b_1b_2\), while the scalar coefficient is extracted by pairing with \(x\). Its tensor image agrees with scan 172’s formula, but the abstract element and its potentially noninjective tensor image must be distinguished.
context/same_cote_84/MPL_84_146-193_notes.md:630: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is the related product lead; this page adds a dual-basis construction that must be separated from any claim of tensor-product injectivity.
```

- `context/notes/RESULTS_STATE.md`: **3 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:32: - **LM4 D.10** [Open (the return's claim)] Arbitrary-frontier descent in the exact comparison Let $U$ be a simply connected open orbit in the original surface. The prime-end disk need not map continuously onto its closure. When the interior identification has such an extension, its boundary map may fail to be injective. We have not proved that an intrinsic centralizer f… Where: D.3 arbitrary-frontier descent. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:34: - **LM4 D.12** [Open (the return's claim)] The universal admissible level-zero kernel For an admissible punctured surface, with actual homeomorphism group $A$, a strict action $u:\Gamma\to A$, and $H=u(\Gamma)$, the unresolved comparison of LM4 C.12 is injectivity of \[ \pi_1(C_A(H),1)\longrightarrow\pi_1(A,1)^\Gamma. \] For hyperbolic finite-type surfaces the target is… Where: D.3 general level-zero comparison. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:93: - **MPL_84_146-193 R09** [No demonstrated route to the LM2 congru… (research note of a returned package, first pass; a lead)] R09 — No demonstrated route to the LM2 congruence questions: **Source:** `pages/MPL_84_146-193_84_scan172.tex`, “δ=δ₁δ₂”; comparison across scans 146–193. **Kind:** reading question / context comparison. The multiplicative discriminant formula is a calculatio… (MPL_84_146-193_notes.md)
```

## A28 — The acting group is the even subgroup, and the action may be trivial

**Context:** C84, no matching three-factor parity action; R09 records the absence of a demonstrated LM2 bridge. **Relation:** adds. **RESULTS_STATE:** no direct entry for this action; `MPL_84_146-193 R09` supplies only the context caution.

**Executed query:** `even.*parity|parité|F_2\^3|three.*involution`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:27: - **LM4 A.14** [Open (the return's claim)] The three full conjugacy assertions We have not decided whether every involution of \(\mathcal P,\widehat{GT}_0,\widehat{GT}\) is conjugate to \(c\) in its respective group. A.2 detects conjugacy of a fixed pair on all relative levels; A.11 identifies the equivalent peripheral generation condition. Neither supplies the compatib… Where: Task A.8. (LM4_SUCCESSOR_results.csv)
```

**Executed query:** `GT|LM2|R09`

- `context/README.md`: **2 matching lines**; shown below.

```text
context/README.md:19: ring" is, as a definition, and whether the polyhedron of level n is the map of X(n) (bridge B5; LM2 rows in this zip,
context/README.md:27: - `LM2_CONGRUENCE_ROWS.md`: our return LM2 on congruence levels (regular maps of level n; bridge B5), each row a claim.
```

- `context/LM2_CONGRUENCE_ROWS.md`: **12 matching lines**; shown below (first eight; all in JSON).

```text
context/LM2_CONGRUENCE_ROWS.md:1: # Statements of our research return LM2 (congruence levels; bridge B5), with status
context/LM2_CONGRUENCE_ROWS.md:3: From the results register of the return LM2_LOOP_EQUATIONS (GPT-6 Astra, ChatGPT Pro mode, Nov 2026). Not reviewed: every row is **the return's claim** (its own status in brackets).
context/LM2_CONGRUENCE_ROWS.md:7: | LM2 C.r1 | Arithmetic outer congruence image is units modulo squares at every level | claim (return: Proved) | §39; fols.299–300; scans22–24 |
context/LM2_CONGRUENCE_ROWS.md:8: | LM2 C.r2 | Unique multiplier is lost on outer congruence actions; corrected square-class statement | claim (return: Refuted) | §39; fols.300 verso–301; scans25–26 |
context/LM2_CONGRUENCE_ROWS.md:9: | LM2 C.r3 | Genuine and outer arithmetic actions have different correctly typed images | claim (return: Proved) | §§39,45; fols.299–301,387–388; scans22–26,176–178 |
context/LM2_CONGRUENCE_ROWS.md:10: | LM2 C.d1 | Every actual GT0 loop automorphism preserves all projective congruence kernels | claim (return: Known) | §39; scans21–30; §44; scans150–168; §46; fols398–400,409; scans198–202,218–219 |
context/LM2_CONGRUENCE_ROWS.md:11: | LM2 C.d2 | Correct matrix norm equations and both residual characters | claim (return: Proved) | §46; fols398,400; scans198(73),202–203(88) |
context/LM2_CONGRUENCE_ROWS.md:12: | LM2 C.d3 | Exact local adelic solution locus, sign compatibility and §48 coboundary schemes | claim (return: Proved) | §46; fols400–401; scans202–205; §48; scans254–266 |
```

- `context/same_cote_84/MPL_84_146-193_notes.md`: **131 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:19: - **No explicit B12 construction in the supplied interval:** no form of P¹, conic, rank-four central Azumaya algebra, or ternary-form/SO(3) identification is constructed here (R01–R04). The folder plan's B5 regular-polyhedron/congruence questions likewise receive no demonstrated step (R09).
context/same_cote_84/MPL_84_146-193_notes.md:24: The supplied context consists of only `README.md`, `LM2_CONGRUENCE_ROWS.md`, and `notes/RESULTS_STATE.md`; the larger files named inside the last register were not supplied. A register excerpt can establish what an earlier run claimed and what review status was reported, but cannot substitute for examining its omitted proof. In particular, the claim status of each LM2/LM4/LM7 entry remains as stated in that register; no such theorem is upgraded by these notes.
context/same_cote_84/MPL_84_146-193_notes.md:38: | Invertible iff \(T_0\) generates \(L\) on \(V(\chi)\) for \(M=\mathcal O\) | No \(T_0\), \(V(\chi)\), or inverse criterion appears here. | R12 verifies the precise local-model criterion \((\tau,\chi)=R\), equivalently that \(\tau\bmod\chi\) is a unit, strengthening E146.3's residue observation; identification with the named global section \(T_0\), varying line bundles, and the omitted manuscript passages remains conditional. |
context/same_cote_84/MPL_84_146-193_notes.md:46: The relevant explicitly unreviewed LM2 register is C.r1–C.r5 and C.d1–C.d5. Open-return entries such as LM2 B.f7 and E.3, LM7 D.19 and E.23, and LM7_PUSH E.3 remain mathematical context items with no connection established by these typed notes. The status of specifically refereed LM7_PUSH entries in RESULTS_STATE.md is not reduced to “unreviewed”; none is invoked as support for the psychological, cultural, or medical assertions here.
context/same_cote_84/MPL_84_146-193_notes.md:610: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) contains no trace/norm calculation; LM2 C.d2 in `context/LM2_CONGRUENCE_ROWS.md` concerns different matrix-norm equations at cote 140-3 scans 198 and 202–203 and does not settle this local quadratic identity.
context/same_cote_84/MPL_84_146-193_notes.md:680: **Context check:** No exact phrase/term matches in the three supplied context files; no substantive relation identified to the LM2 congruence rows or the LM7/LM7_PUSH mathematical entries.
context/same_cote_84/MPL_84_146-193_notes.md:688: **Context check:** The sole lexical match is the surname Haine in the unrelated Carlson–Haine–Wolf citation, RESULTS_STATE.md line 94 (INTAKE 20261114 §4.3). It supplies no evidence about the author's mother and no relevant LM2/LM7 connection.
context/same_cote_84/MPL_84_146-193_notes.md:696: **Context check:** No exact phrase/term matches in the three supplied context files; no substantive relation identified to the LM2 congruence rows or the LM7/LM7_PUSH mathematical entries.
```

- `context/notes/RESULTS_STATE.md`: **20 matching lines**; shown below (first eight; all in JSON).

```text
context/notes/RESULTS_STATE.md:14: - **LM4 A.12** [Open (the return's claim)] Dyadic and mixed-prime involution obstructions A.9 does not determine all two-primary classes or all gluing classes over \(U=F'F^3\) and \(U_{12}\). A.25 below constructs an actual involution with parity one in the image of \(\widehat{GT}_0\) at \(U_{12}\), and A.24 proves that this parity descends to that outer image. Thus the… Where: Task A.4; Task A.5; Lead 3. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:19: - **PUSH_20261114 Part2Succe 26** [push item: open, to settle in a follow-up prompt] (S4) The icosahedral characters. Every `F ∈ GT̂₀` with `λ(F) ≡ ±1 mod 5` acts on the `ω`-part of `H₁` of the cyclic cover of degree six of the sphere branched at the twelve cusps, through the centralizer of `A₅`: three characters `χ₁, χ₄, χ₅` with values in the units of `Ẑ[ω]`. Prove or refute: that cover is the fibre product o… (PUSH_ITEMS_20261114.md)
context/notes/RESULTS_STATE.md:23: - **LM1 D.7** [Open (the return's claim)] Actual Galois, GT, and GT0 comparisons, images, and invisible loop solutions remain unresolved Where: 38-47 comparison; 48; 543; 481; After LM3 task D.b. (LM1_GROUP_SCHEMES_results.csv)
context/notes/RESULTS_STATE.md:24: - **LM2 B.f7** [Open (the return's claim)] Remaining PSL2(F7) arithmetic image and compatible finite pentagon data Where: §42; fol.349 verso; scan120. (LM2_LOOP_EQUATIONS_results.csv)
context/notes/RESULTS_STATE.md:25: - **LM2 E.3** [Open (the return's claim)] Does GT imply the corrected additional orbifold compatibility? Where: §41; fols.315–316 verso; scans54–57; §47; fols.415–425; scans229–250 (cote140-3). (LM2_LOOP_EQUATIONS_results.csv)
context/notes/RESULTS_STATE.md:26: - **LM4 A.13** [Open (the return's claim)] Parity on arbitrary involutions For an involution \(\tau=(-1,f)\) in \(\widehat{GT}_0\), R3 gives \(\Delta(\tau)=\delta((1,f))\). It is zero for A.7's continuum family and for every \(\widehat{GT}_0\)-conjugate of \(c\). The cocycle relation alone gives only \(2\Delta(a)=0\) in \(\mathbb F_2\). A.25 gives such an involution in… Where: Task A.6. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:27: - **LM4 A.14** [Open (the return's claim)] The three full conjugacy assertions We have not decided whether every involution of \(\mathcal P,\widehat{GT}_0,\widehat{GT}\) is conjugate to \(c\) in its respective group. A.2 detects conjugacy of a fixed pair on all relative levels; A.11 identifies the equivalent peripheral generation condition. Neither supplies the compatib… Where: Task A.8. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:37: - **LM7 D.19** [Open (the return's claim)] The residual GT and full profinite realization questions Where: §51.16; folio734 verso; scan174; residual D tasks. (LM7_FERMAT_TOWER_results.csv)
```

## A29 — The three-factor exceptional locus is precisely qualified

**Context:** C84, L172.3 (scan 172), L192.1 (scan 192), concerning the two-factor characteristic-two exception. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

**Executed query:** `deux au moins|three.factor|triple|non.étale`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **1 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:2102: The script checks compatibility with composition, strict associativity, symmetry, identity arrows and the unit object 1 as polynomial identities over Z[χ,τ,σ,…]. For example, both triple products have arrow coordinate
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:72: - **LM7_PUSH E.63** [Proved (the return's claim)] The entire binary cover fibre retains the signed, triple-cover and uniform boundary system. Let $U_2=\operatorname{SL}_2(\mathbf F_9)$ with the specified central map to the retained $A_6$. All $212$ free epikernels give the Ferra… Where: E.3. (LM7_PUSH_results.csv)
```

**Executed query:** `L172\.3|L192\.1|car.*2`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **14 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:48: The sole lexical hit among the recorded searches is the surname Haine in the unrelated Carlson–Haine–Wolf reference, RESULTS_STATE.md line 94, INTAKE 20261114 §4.3, matched by the French word “haine.” It is explicitly classified as irrelevant in T147.2. Context scan numbers and folio references from Longue Marche or other cotes must not be reassigned to this cote 84 packet.
context/same_cote_84/MPL_84_146-193_notes.md:230: “Pour définir un hom \(F\), il faut définir” introduces \(F_{11},F_{12},F_{21},F_{22}\) and the marginal “\unsure{ces} 4 \unsure{carrés} commu-\linebreak\unsure{tatifs}.” The page states the conditions \(F_{22}=0\), \(F_{21}=\alpha_1\otimes\alpha_2\), and \(F_{12}=\psi_1\otimes\psi_2\) as necessary and sufficient for successively stronger properties. The remaining block and its two nonautomatic squares still require construction; three specified blocks are not all four compatibilities.
context/same_cote_84/MPL_84_146-193_notes.md:248: The upper construction is marked “cocart,” the lower one “cart,” and the middle arrow \(E_1\vee E_2\to E_1\wedge E_2\) still has “?” above a cancelled doubtful \(F\). This demonstrates the intended comparison but does not prove its existence or canonicity. If the rows are exact and the end maps are identities, an existing such comparison would be an isomorphism; that conditional fact does not remove the question mark.
context/same_cote_84/MPL_84_146-193_notes.md:302: ### L172.3
context/same_cote_84/MPL_84_146-193_notes.md:306: **Brief quotation:** `\unsure{injectif} \unsure{sauf si} car. 2 et $b_1=b_2=0$`
context/same_cote_84/MPL_84_146-193_notes.md:336: **Brief quotation:** `\deleted{... \unsure{dégénéré|dégénère} en car. 2}`
context/same_cote_84/MPL_84_146-193_notes.md:632: ### L192.1
```

- `context/notes/RESULTS_STATE.md`: **4 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:20: - **CYCLOTOMIC_KERNEL D13** [Open (the return's claim)] D(e) remains unfinished for discontinuous actions normalizing no finite-level deck group and for the affine commensurator-completion description; the exact abstract-cocycle construction problem is stated for the U03 Poincare curve over Qbar. Where: section 3; pp.30-31; scans 62-63. (CYCLOTOMIC_KERNEL_results.csv)
context/notes/RESULTS_STATE.md:63: - **LM7 E.109** [Proved (the return's claim)] For the actual compact plus-quartic pro-five class-two arithmetic action, the entire outer central action class is carried by the rank-two pure-CM module M. An explicit integral coefficient projector Pi has a left inverse identit… Where: ['LM section51.16; folios733v--736v; scans172--178; the compact factor of the generalized Jacobian and the next arithme…. (LM7_FERMAT_TOWER_results.csv)
context/notes/RESULTS_STATE.md:84: - **EXPERT BOGGI_ZALESSKII_STEP §?** [reading of the field expert (Claude Opus 5.5 at effort max), on the returns' claims] Later checks: - **14 November 2026, ~12:35 UTC: the Poincaré read-in** (Claude Fable 5.2 at effort max; its own work, checked by no one; `research_maps_20261112/PRETOT_3D_MODULARITY/POINCARE_AND_A5_20261114.md`, and its block "Added by the Poincaré read-in", R1–R12, under item 2.4 of `PUSH_ITEMS_20261114.md`). - The bridge is e… (NOTE_BOGGI_ZALESSKII_STEP.md)
context/notes/RESULTS_STATE.md:115: - **84-product-quadratic-algebras-formula** (cote 84, their pp. 62–79, 88–90, 98–105; our scans 099, 100, 101, 102, 103, 104, 105, 106) [literature: Matched for the product of quadratic algebras a…] Over any base, without dividing by 2, quadratic algebras carry a commutative product with L(X₁ * X₂) = L₁ ⊗ L₂ and, in split coordinates, b = b₁b₂, c = c₁b₂² + c₂b₁² − 4c₁c₂, hence δ = δ₁δ₂, the generator mapping to 2U₁U₂ + b₁U₂ + b₂U₁ in A₁ ⊗ A₂. Our intake: new to us: our package for this cote is waiting
```

## A30 — The stated open locus admits a direct invariant calculation

**Context:** C84, L172.1–L172.5 (scan 172), L192.1 (scan 192), provide the two-factor formula/trace leads but no triple invariant proof. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later. **Confidence:** high for the asserted sufficient locus, from the two explicit local calculations.

**Executed query:** `three.factor|triple|even.*parity|invariant`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **3 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:64: ### E146.3 — A residue class is a useful, limited invariant
context/same_cote_84/MPL_84_146-193_notes.md:68: If the scalar in “`b'_i=b_i+\unsure{\chi|\gamma}u_i`” is \(\chi\), then \(b'_1b'_2-b_1b_2=\chi(u_1b_2+b_1u_2+\chi u_1u_2)\), so the product is independent of this change modulo \(\chi\). This suggests separating a residue invariant on \(V(\chi)\) from a globally defined product extension and its coherence data. The computation is compatible with the locus occurring in Hua’s invertibility statement, but neither a section called \(T_0\) nor that invertibility criterion occurs in this interval.
context/same_cote_84/MPL_84_146-193_notes.md:2102: The script checks compatibility with composition, strict associativity, symmetry, identity arrows and the unit object 1 as polynomial identities over Z[χ,τ,σ,…]. For example, both triple products have arrow coordinate
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:72: - **LM7_PUSH E.63** [Proved (the return's claim)] The entire binary cover fibre retains the signed, triple-cover and uniform boundary system. Let $U_2=\operatorname{SL}_2(\mathbf F_9)$ with the specified central map to the retained $A_6$. All $212$ free epikernels give the Ferra… Where: E.3. (LM7_PUSH_results.csv)
```

**Executed query:** `L172\.[12345]|L192\.1`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **11 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:7: This report contains **208 individually identified items**: 38 early mathematical notes (E146.1–E170.5), 39 later mathematical notes (L172.1–L192.4), 118 notes on reused typescript (T147.1–T193.5), and 13 comparisons or editorial investigations (R01–R13). Source references identify the exact per-scan file; approximate line numbers refer to the frozen TeX rather than physical manuscript lines. Diplomatic doubt macros reproduced in quotations retain their editorial meaning: a `\unsure` is not automatically an uncertainty expressed by the author, and a cancelled claim is not live text.
context/same_cote_84/MPL_84_146-193_notes.md:15: - **A precise local algebraic result:** scans 172 and 192 give a quadratic-algebra product whose relation and discriminant formula check over the integer polynomial ring; its local formula matches Voight (2016, Construction 3.14) after an explicit generator shift (L172.1–L172.2, R05).
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:282: ### L172.1
context/same_cote_84/MPL_84_146-193_notes.md:292: ### L172.2
context/same_cote_84/MPL_84_146-193_notes.md:302: ### L172.3
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A31 — Scalar image is the goal; the fixed-ring equality is sufficient

**Context:** C84, no matching constant-section problem or three-factor fixed-ring criterion located; L192.1 (scan 192) is only a related degeneration warning. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `constant.*section|j'ai envie de prouver|fixed.ring|invariant`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **2 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:64: ### E146.3 — A residue class is a useful, limited invariant
context/same_cote_84/MPL_84_146-193_notes.md:68: If the scalar in “`b'_i=b_i+\unsure{\chi|\gamma}u_i`” is \(\chi\), then \(b'_1b'_2-b_1b_2=\chi(u_1b_2+b_1u_2+\chi u_1u_2)\), so the product is independent of this change modulo \(\chi\). This suggests separating a residue invariant on \(V(\chi)\) from a globally defined product extension and its coherence data. The computation is compatible with the locus occurring in Hua’s invertibility statement, but neither a section called \(T_0\) nor that invertibility criterion occurs in this interval.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `L192\.1`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **3 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:632: ### L192.1
context/same_cote_84/MPL_84_146-193_notes.md:1741: | 192 | “ça croule si 2=0, b1=b2=0” (the two French words remain doubtful) | Explicit failure warning; L192.1. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A32 — A characteristic-two model separates scalar image from fixed ring

**Context:** C84, L192.1/R06 (scans 172/192), distinguish an abstract product from a collapsed tensor realization; no example for the present fixed-ring question located. **Relation:** adds. **RESULTS_STATE:** RS-product is related only through the actual quadratic product. **Confidence:** high, from explicit bases and relative trace/norm formulas.

**Executed query:** `dual.number|e\+f|fixed.ring|invariant`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **2 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:64: ### E146.3 — A residue class is a useful, limited invariant
context/same_cote_84/MPL_84_146-193_notes.md:68: If the scalar in “`b'_i=b_i+\unsure{\chi|\gamma}u_i`” is \(\chi\), then \(b'_1b'_2-b_1b_2=\chi(u_1b_2+b_1u_2+\chi u_1u_2)\), so the product is independent of this change modulo \(\chi\). This suggests separating a residue invariant on \(V(\chi)\) from a globally defined product extension and its coherence data. The computation is compatible with the locus occurring in Hua’s invertibility statement, but neither a section called \(T_0\) nor that invertibility criterion occurs in this interval.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `L192\.1|R06`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:632: ### L192.1
context/same_cote_84/MPL_84_146-193_notes.md:1650: ### R06 — Tensor realization and abstract product must be separated
context/same_cote_84/MPL_84_146-193_notes.md:1741: | 192 | “ça croule si 2=0, b1=b2=0” (the two French words remain doubtful) | Explicit failure warning; L192.1. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A33 — The invertible-two case is discharged by the factor four

**Context:** C84, no matching three-involution averaging argument; L172.5 (scan 172) contains a different factor-two projector. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `frac.14|1/4|4a|common.*trace`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **3 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:1936: | T174a | 174 / 14–18 | Conditions on `f:E→E` | Restriction to `L`, induced quotient action | 2 numbered conditions, second rewritten | Can be checked by a triangular 2×2 matrix once domains are fixed; do not implement the cancelled version as another condition. |
context/same_cote_84/MPL_84_146-193_notes.md:1947: | T184a | 184 / 5–15 | Quotient presentations | Product algebra `A` and product module `E` | 2 presentations | Universal-pushout formulas, with uncertain denominator and subscript readings retained. |
context/same_cote_84/MPL_84_146-193_notes.md:1995: | Printed pagination | Numbered interval 475–500, with 480/481/485 absent, plus 475 bis | 23 + 1 | Exact leaf-to-page mapping |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `L172\.5|projector`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **2 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
context/same_cote_84/MPL_84_146-193_notes.md:328: The local tensor operator \(T=1+\sigma_1\otimes\sigma_2\) admits maps \(i:A\to B\) and \(q:B\to A\) with \(iq=T\) and \(qi=2\operatorname{id}\); in the basis \((1,u_1,u_2,u_1u_2)\), \(q\) takes the values \((2,-b_1,-b_2,t+b_1b_2)\). These identities explain the displayed factor “2” and imply \(T^2=2T\): \(T\) is generally not idempotent, whereas \(T/2\) is a projector when two is invertible. The script verifies the matrices universally; identification with every doubtful arrow in the drawn diagram remains a reading question.
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:63: - **LM7 E.109** [Proved (the return's claim)] For the actual compact plus-quartic pro-five class-two arithmetic action, the entire outer central action class is carried by the rank-two pure-CM module M. An explicit integral coefficient projector Pi has a left inverse identit… Where: ['LM section51.16; folios733v--736v; scans172--178; the compact factor of the generalized Jacobian and the next arithme…. (LM7_FERMAT_TOWER_results.csv)
```

## A34 — The étale proposition needs generation and the inserted fixed-ring condition

**Context:** C84, no matching three-cover twisting proposition; E170.1 (scan 170) is a general exactness caution, not its proof. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `twist|parity|transitive|transitif`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **7 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:18: - **A separate sign obstruction:** for the explicitly fixed endpoint conventions, the pushout and pullback extension cocycles are opposite; a χ=0 elliptic-curve example prevents an isomorphism fixing both ends (E170.4–E170.5). This does not refute a sign-twisted interpretation or the whole ellipsized Hua entry.
context/same_cote_84/MPL_84_146-193_notes.md:268: ### E170.4 — A conditional counterexample distinguishes equality from a sign twist
context/same_cote_84/MPL_84_146-193_notes.md:358: The displayed identifications claim compatibility of the product with duality after determinant-line twists. A proof must specify the canonical rank-two duality maps, the tensor-line identifications, and the hypotheses under which the product is functorial; the written string of isomorphisms supplies no coherence verification.
context/same_cote_84/MPL_84_146-193_notes.md:360: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is related at the categorical level, but contains no determinant-twist formula; this page adds a compatibility claim rather than a proof of the whole symmetric monoidal assertion.
context/same_cote_84/MPL_84_146-193_notes.md:1638: ### R04 — Rank-two module data do not already provide a twisted P¹
context/same_cote_84/MPL_84_146-193_notes.md:1642: If an actual rank-two vector bundle E is given, its projectivization and endomorphism algebra provide a split-type projective bundle/Azumaya example, but that construction alone supplies no nontrivial Brauer class. A proposed B12 reading therefore needs descent data or a genuinely twisted object, not merely the symbols E and A in the displayed dualities. Searching the context for “torsor”, “Azumaya”, “P¹” and “extension” gives B12 as an unchecked target and Hua's extension-product claim as the only direct match to these scans; neither supplies the missing identification. The confidence in this caution comes from the distinction between an endomorphism algebra and an arbitrary degree-two Azumaya algebra, not from an interpretation of unclear ink.
context/same_cote_84/MPL_84_146-193_notes.md:2072: For the concrete case \(\chi=0\), choose \(L_i=M_i=\mathcal O_X\), \(\tau_i=1\), and any locally free extension \(E_i\) of \(\mathcal O_X\) by itself. The globally defined maps \(\pi_i=\psi_i\) and \(\varpi_i=-\alpha_i\) satisfy the displayed splitting identities, and the inclusions are universally injective because the quotient is locally free. If the first extension has a nonzero class \(e\in H^1(X,\mathcal O_X)\) and the second is split, the computed classes are \(e\) and \(-e\). On a smooth elliptic curve over a characteristic-zero field the vector space \(H^1(X,\mathcal O_X)\) is one-dimensional (The Stacks Project Authors, n.d., Tags 0B3A, 072J and 0BY6), so such an \(e\) exists and is not killed by two; hence the two extensions are not isomorphic with both end identifications fixed. Sending the subobject by \(-\mathrm{id}\), however, removes the obstruction. This exact dependence  … [full line in JSON]
```

- `context/notes/RESULTS_STATE.md`: **6 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:14: - **LM4 A.12** [Open (the return's claim)] Dyadic and mixed-prime involution obstructions A.9 does not determine all two-primary classes or all gluing classes over \(U=F'F^3\) and \(U_{12}\). A.25 below constructs an actual involution with parity one in the image of \(\widehat{GT}_0\) at \(U_{12}\), and A.24 proves that this parity descends to that outer image. Thus the… Where: Task A.4; Task A.5; Lead 3. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:16: - **LM4 B.41** [Open (the return's claim)] Parity and further-orbit lifting in the hypothetical nontrivial kernel If $\mathcal K\ne1$, neither the restriction of $\Delta$ to all its elements nor its extension along every required icosahedral marked-orbit locus has been determined. The latter extension would have to be constructed with compatible based maps and then chec… Where: B.7. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:26: - **LM4 A.13** [Open (the return's claim)] Parity on arbitrary involutions For an involution \(\tau=(-1,f)\) in \(\widehat{GT}_0\), R3 gives \(\Delta(\tau)=\delta((1,f))\). It is zero for A.7's continuum family and for every \(\widehat{GT}_0\)-conjugate of \(c\). The cocycle relation alone gives only \(2\Delta(a)=0\) in \(\mathbb F_2\). A.25 gives such an involution in… Where: Task A.6. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:48: - **LM7_PUSH E.65** [Proved (the return's claim; refereed 14 Nov 2026: proved, two gaps closed by the referee)] The CM parity is a continuous character of the full gentle group. Put $\mathcal G=\widehat{\mathrm{GT}}_0$ and $\mathcal H=\ker(\lambda:\mathcal G\to\widehat{\mathbf Z}^{\times})$. Retain the positive generators and actual pure f… Where: E.2; E.3. (LM7_PUSH_results.csv)
context/notes/RESULTS_STATE.md:58: - **LM4 A.24** [Proved (the return's claim)] The parity character descends to the actual outer image at level twelve Let \[ F_{12}=F/R_{\mathrm{nil}}(U_{12}),\qquad G_{12}=\operatorname{im}\!\left( \widehat{GT}_0\longrightarrow \operatorname{Out}^{\sharp}(F_{12})\right). \]… Where: Task A.4; Task A.5; Task A.6; Lead 3. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:59: - **LM4 A.40** [Proved (the return's claim)] A parity-one involution survives an actual noncongruence perfect-socle refinement Put \[ \Pi=\widehat B,\qquad R=R_{\mathrm{nil}}(K_{\mathrm{cong}}),\qquad C=\Pi/R, \qquad \widehat K=\ker(\Pi\longrightarrow A_5). \] There is a fi… Where: Task A.5; Task A.6; Lead 3. (LM4_SUCCESSOR_results.csv)
```

**Executed query:** `étale|E170\.1`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **3 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:250: ### E170.1 — Canonical product extensions need the tensor-exactness hypotheses
context/same_cote_84/MPL_84_146-193_notes.md:1718: | 170 | “On définit de façon \unsure{can.}”; “une … application can.”; no literal question mark. | Canonical construction/comparison asserted, E170.1–E170.2; coherence is not supplied. |
context/same_cote_84/MPL_84_146-193_notes.md:2035: For F₂ with `b1=b2=1`, the four ordered pairs `(c1,c2)` give the Artin–Schreier coefficients `c1+c2`: two split products and two nonsplit products. Thus the four rank-one failures among all 16 tuples occur exactly at `b1=b2=0`, and are different from the four étale-input cases. These finite counts illustrate the universally derived criterion and do not replace its proof.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A35 — The frozen target of lemma 120 makes its injectivity condition vacuous

**Context:** C84, no matching transitive-subschema lemma or \(X_J\) target located. **Relation:** adds. **RESULTS_STATE:** no direct entry.

**Executed query:** `X_J|sous.schéma|subscheme|transiti`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **5 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:164: The transitions from “\((\alpha+\chi\gamma)\mathrm{id}=0\)” to “\(\alpha+\chi\gamma=0\),” and then to “\(\beta=\gamma\),” require justification. A faithful module gives the first implication, while the two scalar equalities \(\alpha=-\chi\gamma=-\chi\beta\) by themselves give only \(\chi(\beta-\gamma)=0\). A universal comparison of coefficients may supply the stronger conclusion, but the page does not state that argument, and scan 160 subsequently revises the module hypotheses.
context/same_cote_84/MPL_84_146-193_notes.md:270: **File/scan/lines:** `MPL_84_146-193_84_scan168.tex`, 168, 9–13; `MPL_84_146-193_84_scan170.tex`, 170, 19–36; compare `MPL_84_146-193_84_scan166.tex`, 166, 19–28. **Kind:** own idea. **Confidence:** high for the explicitly specified fixed-endpoint interpretation, because the transition matrices and scalar residuals are computed; no claim of novelty or blanket refutation of Hua. **Context comparison:** conditionally contradicts the statement that the pushout and pullback products “agree” in Hua, **84-chi-trivialised-extension-product**, if that means an isomorphism inducing identities on both ends for every \(\chi\).
context/same_cote_84/MPL_84_146-193_notes.md:558: The expansion tracks how changing chosen lifts affects the product, with two mixed terms and the \(2u_1\otimes u_2\) term. This is the right type of calculation for independence from splittings, but the frozen line \(b_1\otimes u_2+u_2\otimes b_{1|2}\) has an unresolved variable/type mismatch and cannot be used as an unqualified transition formula.
context/same_cote_84/MPL_84_146-193_notes.md:648: To globalize the scalar formula, track generator changes \(u_i'=a_i u_i+r_i\): the product generator changes by \(u'=a_1a_2u+a_1b_1r_2+a_2b_2r_1-2r_1r_2\), with the corresponding transformed monic coefficients. Confidence: high for this transition identity, verified symbolically over the integer polynomial ring; checking overlap cocycles gives a concrete route to gluing, but a full categorical associator is a further requirement.
context/same_cote_84/MPL_84_146-193_notes.md:650: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) claims a global symmetric monoidal product; this is an additional local transition calculation bearing on descent, not a new proof of its coherence or invertibility assertions.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `kernel|noyau`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **1 matching lines**; shown below.

```text
context/LM2_CONGRUENCE_ROWS.md:10: | LM2 C.d1 | Every actual GT0 loop automorphism preserves all projective congruence kernels | claim (return: Known) | §39; scans21–30; §44; scans150–168; §46; fols398–400,409; scans198–202,218–219 |
```

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:86: The phrase “`\mathcal H_i=\text{\unsure{noyau} de}`” is unfinished, followed by the purported sequence from \(\operatorname{Hom}(M,L)\) through \(\mathcal H/\mathrm{id}\) to \((\mathcal O\times\mathcal O)/\mathcal O\). To assess exactness one must specify the omitted map, the action on both ends of the extension, and whether surjectivity is local or global. Hua’s category-level summary does not supply those missing definitions.
context/same_cote_84/MPL_84_146-193_notes.md:318: For the displayed local model, \(i:R[t]/(t^2+bt+c)\to B=A_1\otimes_R A_2\), \(t\mapsto2u_1u_2+b_2u_1+b_1u_2\), has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\), because the four tensor-basis coefficients of \(i(a+dt)\) are \((a,db_2,db_1,2d)\). Thus \(R=\mathbb Z/4\mathbb Z\), \(b_1=b_2=c_1=c_2=0\), gives the nonzero kernel element \(2t\), while a split injection requires the stronger condition \((2,b_1,b_2)=R\). Confidence: high for this conditional algebraic statement, since it is a direct coefficient calculation and the script independently enumerates the small-ring examples.
context/same_cote_84/MPL_84_146-193_notes.md:2037: The script also enumerates kernels over `Z/4Z` for `(b1,b2)=(0,0),(2,0),(1,0)` and `Z/6Z` for `(0,0),(3,0)`, always with `c1=c2=0`. The kernel sizes are respectively `2,2,1,2,1`, exactly as predicted by `Ann(2,b1,b2)`.
```

- `context/notes/RESULTS_STATE.md`: **14 matching lines**; shown below (first eight; all in JSON).

```text
context/notes/RESULTS_STATE.md:15: - **LM4 B.12** [Open (the return's claim)] The proposed identities on the full Grothendieck--Teichm\"uller group B.53 below proves P4's exact quadratic-character domain, both quintic homomorphisms, their arithmetic identity, and the kernel inclusion for $\mathcal K$. Its third map has the corrected weighted-orbifold target $\operatorname{Out}_{\partial}(C_3\amalg C_3)$.… Where: B.3.P4;B.3.P5. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:16: - **LM4 B.41** [Open (the return's claim)] Parity and further-orbit lifting in the hypothetical nontrivial kernel If $\mathcal K\ne1$, neither the restriction of $\Delta$ to all its elements nor its extension along every required icosahedral marked-orbit locus has been determined. The latter extension would have to be constructed with compatible based maps and then chec… Where: B.7. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:18: - **LM4 B.38** [Open (the return's claim)] The remaining congruence levels No determination of $\mathcal K_N$ for all $N$ is obtained here. In particular $\mathcal K_5=1$ is the main unresolved assertion, and the corresponding level-seven and level-eleven kernels remain undecided. Their quotient compactifications have genera three and twenty-six, respectively. An index-… Where: B.5. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:20: - **CYCLOTOMIC_KERNEL D13** [Open (the return's claim)] D(e) remains unfinished for discontinuous actions normalizing no finite-level deck group and for the affine commensurator-completion description; the exact abstract-cocycle construction problem is stated for the U03 Poincare curve over Qbar. Where: section 3; pp.30-31; scans 62-63. (CYCLOTOMIC_KERNEL_results.csv)
context/notes/RESULTS_STATE.md:30: - **LM4 B.39** [Open (the return's claim)] The nonsolvable direction and the published assertions For a finite solvable subgroup of a genus-zero mapping class group, the centralizer is the closure of the discrete centralizer, by the prime-power normalizer induction in B.30 and the open-kernel argument B.2. This proves the solvable direction of the refined triangle-orbif… Where: B.6;Lead4. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:31: - **LM4 C.4** [Open (the return's claim)] The actual kernel in prompt C.1 In the actual torus setting of C.3, prove or refute $K=1$. The audited structural conclusions of LM4 D.78 imply that $K$ is pro-odd. C.1 shows that any counterexample must have an infinitely generated free pro-$p$ quotient for an odd prime. It would suffice to prove that the actual $K$ is finitel… Where: C.1: requested decision unresolved. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:34: - **LM4 D.12** [Open (the return's claim)] The universal admissible level-zero kernel For an admissible punctured surface, with actual homeomorphism group $A$, a strict action $u:\Gamma\to A$, and $H=u(\Gamma)$, the unresolved comparison of LM4 C.12 is injectivity of \[ \pi_1(C_A(H),1)\longrightarrow\pi_1(A,1)^\Gamma. \] For hyperbolic finite-type surfaces the target is… Where: D.3 general level-zero comparison. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:36: - **LM4 E.10** [Open (the return's claim)] The six congruence-kernel computations in prompt E.1 For each type (E.1.1), determine $K_c^\tau$ and the nonabelian pointed set $H^1(C_2,K_c)$ for $\operatorname{Ad}(\tau)$. E.3 gives the exact class and centralizer formula after these groups and sets are known; E.5 supplies its quotient-centralizer term for the five oval types… Where: E.1: six requested computations unresolved. (LM4_SUCCESSOR_results.csv)
```

## A36 — Even with the target repaired, the lemma requires a closed subscheme

**Context:** C84, no matching closed-subscheme/transitive-action lemma located. **Relation:** adds. **RESULTS_STATE:** no direct entry. **Confidence:** high, from the explicit open-immersion counterexample and the component-ideal proof.

**Executed query:** `sous.schéma|closed.*subscheme|D\(2\)|transiti`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **5 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:164: The transitions from “\((\alpha+\chi\gamma)\mathrm{id}=0\)” to “\(\alpha+\chi\gamma=0\),” and then to “\(\beta=\gamma\),” require justification. A faithful module gives the first implication, while the two scalar equalities \(\alpha=-\chi\gamma=-\chi\beta\) by themselves give only \(\chi(\beta-\gamma)=0\). A universal comparison of coefficients may supply the stronger conclusion, but the page does not state that argument, and scan 160 subsequently revises the module hypotheses.
context/same_cote_84/MPL_84_146-193_notes.md:270: **File/scan/lines:** `MPL_84_146-193_84_scan168.tex`, 168, 9–13; `MPL_84_146-193_84_scan170.tex`, 170, 19–36; compare `MPL_84_146-193_84_scan166.tex`, 166, 19–28. **Kind:** own idea. **Confidence:** high for the explicitly specified fixed-endpoint interpretation, because the transition matrices and scalar residuals are computed; no claim of novelty or blanket refutation of Hua. **Context comparison:** conditionally contradicts the statement that the pushout and pullback products “agree” in Hua, **84-chi-trivialised-extension-product**, if that means an isomorphism inducing identities on both ends for every \(\chi\).
context/same_cote_84/MPL_84_146-193_notes.md:558: The expansion tracks how changing chosen lifts affects the product, with two mixed terms and the \(2u_1\otimes u_2\) term. This is the right type of calculation for independence from splittings, but the frozen line \(b_1\otimes u_2+u_2\otimes b_{1|2}\) has an unresolved variable/type mismatch and cannot be used as an unqualified transition formula.
context/same_cote_84/MPL_84_146-193_notes.md:648: To globalize the scalar formula, track generator changes \(u_i'=a_i u_i+r_i\): the product generator changes by \(u'=a_1a_2u+a_1b_1r_2+a_2b_2r_1-2r_1r_2\), with the corresponding transformed monic coefficients. Confidence: high for this transition identity, verified symbolically over the integer polynomial ring; checking overlap cocycles gives a concrete route to gluing, but a full categorical associator is a further requirement.
context/same_cote_84/MPL_84_146-193_notes.md:650: **Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) claims a global symmetric monoidal product; this is an additional local transition calculation bearing on descent, not a new proof of its coherence or invertibility assertions.
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `closed immersion|immersion ferm`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A37 — The nonétale fibre construction is a stated program

**Context:** C84, L192.1/R06 (scans 172/192), on realization failure; no matching three-cover fibre construction located. **Relation:** adds. **RESULTS_STATE:** RS-product does not settle this further construction.

**Executed query:** `sans condition étale|biquadrati|pi.*varepsilon`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **negative** (no matching line).

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `L192\.1|R06`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:632: ### L192.1
context/same_cote_84/MPL_84_146-193_notes.md:1650: ### R06 — Tensor realization and abstract product must be separated
context/same_cote_84/MPL_84_146-193_notes.md:1741: | 192 | “ça croule si 2=0, b1=b2=0” (the two French words remain doubtful) | Explicit failure warning; L192.1. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A38 — The universal map is finite but need not have flat degree four

**Context:** C84, E170.1 (scan 170), L172.4 (scan 172), L192.1 (scan 192), for distinct flatness and realization issues. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later.

**Executed query:** `plat|flat|surject|univers.*inject`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **7 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:34: | Extensions with a fixed \(\chi\)-splitting | Scan 170 gives the extension diagrams and identities; scans 146–168 calculate with them. | Supported as the intended objects, subject to the written universal-injectivity and local-freeness hypotheses and the frozen sign doubt. |
context/same_cote_84/MPL_84_146-193_notes.md:86: The phrase “`\mathcal H_i=\text{\unsure{noyau} de}`” is unfinished, followed by the purported sequence from \(\operatorname{Hom}(M,L)\) through \(\mathcal H/\mathrm{id}\) to \((\mathcal O\times\mathcal O)/\mathcal O\). To assess exactness one must specify the omitted map, the action on both ends of the extension, and whether surjectivity is local or global. Hua’s category-level summary does not supply those missing definitions.
context/same_cote_84/MPL_84_146-193_notes.md:184: ### E160.3 — The barred and primed operators should not be conflated
context/same_cote_84/MPL_84_146-193_notes.md:254: “On définit de façon \unsure{can.}” introduces the two extension products, while the margin calls the inclusions “\unsure{univ.} \unsure{injectfs|injectifs}.” The pushout and pullback diagrams give a concrete construction plan, but exactness of their tensor rows requires the stated universal-injectivity or suitable flatness assumptions. This is substantially more specific than an unqualified operation on every extension of arbitrary modules.
context/same_cote_84/MPL_84_146-193_notes.md:1582: “un peu hâtivement”: He says later comparisons showed that some of his pairings were superficial and conflated situations that the Chinese dialectic distinguished. The uncertain inserted reference to 112′/112¹ is retained as unresolved provenance.
context/same_cote_84/MPL_84_146-193_notes.md:1926: | T170.1 / 170 | Input extensions and splitting identities | \(i=1,2\); \(\chi\), universal injectivity | 2 extensions; 3 live displayed identity lines for each \(i\), one with `=\|+` doubt | Script uses the declared equality interpretation; no silent disambiguation. |
context/same_cote_84/MPL_84_146-193_notes.md:2072: For the concrete case \(\chi=0\), choose \(L_i=M_i=\mathcal O_X\), \(\tau_i=1\), and any locally free extension \(E_i\) of \(\mathcal O_X\) by itself. The globally defined maps \(\pi_i=\psi_i\) and \(\varpi_i=-\alpha_i\) satisfy the displayed splitting identities, and the inclusions are universally injective because the quotient is locally free. If the first extension has a nonzero class \(e\in H^1(X,\mathcal O_X)\) and the second is split, the computed classes are \(e\) and \(-e\). On a smooth elliptic curve over a characteristic-zero field the vector space \(H^1(X,\mathcal O_X)\) is one-dimensional (The Stacks Project Authors, n.d., Tags 0B3A, 072J and 0BY6), so such an \(e\) exists and is not killed by two; hence the two extensions are not isomorphic with both end identifications fixed. Sending the subobject by \(-\mathrm{id}\), however, removes the obstruction. This exact dependence  … [full line in JSON]
```

- `context/notes/RESULTS_STATE.md`: **2 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:34: - **LM4 D.12** [Open (the return's claim)] The universal admissible level-zero kernel For an admissible punctured surface, with actual homeomorphism group $A$, a strict action $u:\Gamma\to A$, and $H=u(\Gamma)$, the unresolved comparison of LM4 C.12 is injectivity of \[ \pi_1(C_A(H),1)\longrightarrow\pi_1(A,1)^\Gamma. \] For hyperbolic finite-type surfaces the target is… Where: D.3 general level-zero comparison. (LM4_SUCCESSOR_results.csv)
context/notes/RESULTS_STATE.md:85: - **EXPERT IMPLICATIONS_E65_LM §2** [reading of the field expert (Claude Fable 5.2 at effort max), on the returns' claims] What follows: 1. **A theorem now.** `Delta : GT_0-hat -> F_2` is a continuous surjective character that vanishes on the Galois image. The pair of parities maps the multiplier-one part onto `F_2 x F_2`; Galois has the diagonal. The Galois image lies in an open subgroup of index two of `GT_0-hat`. `Delta` is invisible in every pr… (EXPERT_IMPLICATIONS_E65_LM.md)
```

**Executed query:** `L172\.4|L192\.1|E170\.1`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **7 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:250: ### E170.1 — Canonical product extensions need the tensor-exactness hypotheses
context/same_cote_84/MPL_84_146-193_notes.md:312: ### L172.4
context/same_cote_84/MPL_84_146-193_notes.md:632: ### L192.1
context/same_cote_84/MPL_84_146-193_notes.md:1718: | 170 | “On définit de façon \unsure{can.}”; “une … application can.”; no literal question mark. | Canonical construction/comparison asserted, E170.1–E170.2; coherence is not supplied. |
context/same_cote_84/MPL_84_146-193_notes.md:1724: | 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
context/same_cote_84/MPL_84_146-193_notes.md:1741: | 192 | “ça croule si 2=0, b1=b2=0” (the two French words remain doubtful) | Explicit failure warning; L192.1. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A39 — Three dual-number inputs give an explicit nonflat universal map

**Context:** C84, L192.1/R06 (scans 172/192), the two-factor collapse lead; no three-factor nonflat example located. **Relation:** adds. **RESULTS_STATE:** RS-product, RS-later. **Confidence:** high, from the explicit module action and tensor test.

**Executed query:** `dual.number|triple|nonflat|non.flat`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **1 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:2102: The script checks compatibility with composition, strict associativity, symmetry, identity arrows and the unit object 1 as polynomial identities over Z[χ,τ,σ,…]. For example, both triple products have arrow coordinate
```

- `context/notes/RESULTS_STATE.md`: **1 matching lines**; shown below.

```text
context/notes/RESULTS_STATE.md:72: - **LM7_PUSH E.63** [Proved (the return's claim)] The entire binary cover fibre retains the signed, triple-cover and uniform boundary system. Let $U_2=\operatorname{SL}_2(\mathbf F_9)$ with the specified central map to the retained $A_6$. All $212$ free epikernels give the Ferra… Where: E.3. (LM7_PUSH_results.csv)
```

**Executed query:** `L192\.1|R06`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **4 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:632: ### L192.1
context/same_cote_84/MPL_84_146-193_notes.md:1650: ### R06 — Tensor realization and abstract product must be separated
context/same_cote_84/MPL_84_146-193_notes.md:1741: | 192 | “ça croule si 2=0, b1=b2=0” (the two French words remain doubtful) | Explicit failure warning; L192.1. |
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

## A40 — The final relative trace and norm are still to be constructed

**Context:** C84, L172.5 (scan 172) and L190.2 (scan 190), the trace and ordinary norm leads, with no construction for this \(B\to B_1\) setting. **Relation:** adds. **RESULTS_STATE:** no direct entry for this pending relative structure.

**Executed query:** `B_0|B_1|quasi.?quadrati|relative norm`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **24 matching lines**; shown below (first eight; all in JSON).

```text
context/same_cote_84/MPL_84_146-193_notes.md:16: - **An abstract product can survive a failed tensor realization:** the image map has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\) in the declared monic local model, refining the manuscript's characteristic-two warning and producing a concrete \(\mathbb Z/4\mathbb Z\) example (L172.3–L172.6, L192.1).
context/same_cote_84/MPL_84_146-193_notes.md:36: | \(b=b_1\otimes b_2\) in split coordinates | Scan 146 circles \(b=b_1b_2\) and writes coordinate changes. | Direct local evidence; global descent is not proved by the circled formula alone. |
context/same_cote_84/MPL_84_146-193_notes.md:56: The circled “\(b=b_1b_2\)” is accompanied by the changes “`b'_1=b_1+\unsure{\chi|\gamma}u_1`” and “`b'_2=b_2+\unsure{\chi|\gamma}u_2`,” so a proof must check independence of splittings rather than simply multiply two chosen coordinates. This supports the local coefficient part of Hua’s claim, while the tensor interpretation requires the indicated Hom domains and the surviving doubt over the scalar to be respected. It does not itself construct associativity, a unit, or an inverse.
context/same_cote_84/MPL_84_146-193_notes.md:62: For the two displayed matrices “\(\begin{pmatrix}2&0\\-b_1&0\end{pmatrix}\)” and “\(\begin{pmatrix}0&0\\b_1&2\end{pmatrix}\),” direct multiplication gives sum \(2I\), both cross-products zero, and squares equal to twice the respective matrix. These are integral identities, but replacing either matrix by half of itself to obtain an idempotent would require an additional hypothesis. `early_formula_checks.py` verifies the four identities without deciding the doubtful names of the operators.
context/same_cote_84/MPL_84_146-193_notes.md:68: If the scalar in “`b'_i=b_i+\unsure{\chi|\gamma}u_i`” is \(\chi\), then \(b'_1b'_2-b_1b_2=\chi(u_1b_2+b_1u_2+\chi u_1u_2)\), so the product is independent of this change modulo \(\chi\). This suggests separating a residue invariant on \(V(\chi)\) from a globally defined product extension and its coherence data. The computation is compatible with the locus occurring in Hua’s invertibility statement, but neither a section called \(T_0\) nor that invertibility criterion occurs in this interval.
context/same_cote_84/MPL_84_146-193_notes.md:286: **Brief quotation:** `u=2u_1u_2+b_2u_1+b_1u_2`
context/same_cote_84/MPL_84_146-193_notes.md:288: Under the monic local presentations \(u_i^2+b_i u_i+c_i=0\), the displayed \(u\) satisfies \(u^2+b_1b_2u+b_1^2c_2+b_2^2c_1-4c_1c_2=0\) over every commutative base ring; the accompanying script verifies the universal polynomial remainder over the integers. This establishes the local identity independently of whether the resulting abstract quadratic algebra embeds into the tensor product.
context/same_cote_84/MPL_84_146-193_notes.md:306: **Brief quotation:** `\unsure{injectif} \unsure{sauf si} car. 2 et $b_1=b_2=0$`
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

**Executed query:** `L172\.5|L190\.2`

- `context/README.md`: **negative** (no matching line).

- `context/LM2_CONGRUENCE_ROWS.md`: **negative** (no matching line).

- `context/same_cote_84/MPL_84_146-193_notes.md`: **2 matching lines**; shown below.

```text
context/same_cote_84/MPL_84_146-193_notes.md:322: ### L172.5
context/same_cote_84/MPL_84_146-193_notes.md:602: ### L190.2
```

- `context/notes/RESULTS_STATE.md`: **negative** (no matching line).

