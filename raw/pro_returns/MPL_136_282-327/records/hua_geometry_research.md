# Hua comparison: uniformization, projective connections, and universal constructions

Research dossier prepared on 17 November 2026 after the parent researcher reported the transcription frozen. No page or combined transcription was edited. This dossier reads the frozen TeX as the evidence of the current package; it does not independently reinspect the manuscript images.

## Evidence, attribution, and scope

The supplied context/hua_project/README.md was read first, followed by the complete 136.modern.tex (2,504 physical lines), the complete context/notes/RESULTS_STATE.md, and the relevant portions of *Pursuing Stacks* VI–VII identified below. **“Hua” below means Michel Hua’s project’s AI-produced modernised reading of cote 136, not a diplomatic transcription, a human-verified edition, or a result of this package.** Its subsection titles and page labels are retained as its own locators. The supplied README, lines 3–11, explicitly requires this attribution and asks for a separate note when its subject has no counterpart in our research register.

The present evidence is cote **136, scans 302–318 and 326–327**; scan 325 was also checked to establish the transition of subject. Physical TeX line numbers below refer to pages/MPL_136_282-327_136_scanNNN.tex. The source’s uncertainty and deletion macros remain part of the evidence: a mathematical interpretation below never resolves one of them in the frozen transcription.

The supplied register is dated **2026-11-17 05:13 UTC**. Its statuses are the originating runs’ claims unless a specific intake/referee assessment is recorded; the comparisons below do not promote those claims to independently verified theorems.

## Main conclusion

**There is a genuine conditional obstruction to the literal split-bundle reading of the boxed request on scan 327.** If \(\Omega\) is a holomorphic line bundle of nonzero degree and “connection” means a holomorphic principal \(\mathrm{PGL}_2\)-connection compatible with the displayed holomorphic bundle, then
\[
 \mathbb P(\Omega^{-1}\oplus\Omega)
\]
has no such connection. This also excludes a regular algebraic connection on that bundle over a smooth projective complex curve. It does **not** exclude the flat projective torsor obtained from uniformization, and does not establish what Grothendieck intended by \(\Omega\) or by the displayed splitting.

The appropriate standard comparison is the nonsplit first-jet bundle of an inverse theta characteristic. The source’s principal-parts and differential-operator sketches on scan 326 make this a useful research lead, but no equality with that jet bundle is written in the retained passage. Consequently the result to record is a **checked conditional obstruction plus a candidate interpretation**, not a solved reconstruction of the manuscript.

## 1. Geometric notes: a separate subject deserving its own register note

### G1. Hua identifies a geometric leaf outside the PD research register

**Source:** cote 136, [scan 327](../pages/MPL_136_282-327_136_scan327.tex), lines 2–5, 18–20 and 91–99; [scan 326](../pages/MPL_136_282-327_136_scan326.tex), lines 10–15, 45–47 and 62–79. **Quotation:** “un … torseur canonique”; “Trouver une connexion intégrable / (alg) canonique sur”.

**Hua comparison:** *“Un feuillet étranger : la structure projective d’une courbe (pages 325 à 327)”*, 136.modern.tex, lines 2174–2196, specifically 2177–2188. Hua’s project identifies the uniformization/projective-structure strand, and the current scan 327 **supports** that identification while keeping the existence assertion for a torsor separate from the later boxed construction request. The supplied RESULTS_STATE orientation, lines 14–19, says there is no directly corresponding result or Hua finding listed for this range; targeted searches also found no Atiyah–Weil/projective-connection item in that digest. This deserves a **separate Hua-credited note**, rather than being assigned to the unrelated localizer, GT, or anabelian entries.

**Status and confidence:** source-supported topic identification, high confidence; no claim that the boxed problem has a solution. The geometry is independent of the ordinary additive universal construction of scans 302–318 in the retained text.

### G2. The pointed torsor has a stabilizer group; the source corrects the larger group

**Source:** cote 136, [scan 327](../pages/MPL_136_282-327_136_scan327.tex), lines 11–14. **Exact retained fragment:** `\deleted{\mathrm{GP}(1)_{\mathbb R}\simeq G'_{\mathbb C}}\inserted{S_{\mathbb R}}`.

**Hua comparison:** the geometry subsection, lines 2179–2182, identifies pointed uniformization isomorphisms with a torsor under the full real projective group; this **differs from the explicit correction in the current transcription**. In the disc model, automorphisms fixing the distinguished point are rotations, a compact point stabilizer, so the extension of structure group in line 14 is essential. This is a high-confidence mathematical distinction and a high-confidence textual discrepancy between the supplied readings; it is not permission to rewrite either source.

**Additional group convention:** the orientation-preserving real group is \(\mathrm{PSL}_2(\mathbb R)\); the real points of the algebraic group \(\mathrm{PGL}_2\) have an additional component. Thus scan 326, line 13, should not silently be interpreted as surjectivity of \(\mathrm{SL}_2(\mathbb R)\to\mathrm{PGL}_2(\mathbb R)\): the determinant sign of a real projective matrix is unchanged by scalar multiplication, and the image has positive determinant. This elementary check leaves open whether \(G'_{\mathbb R}\) in these notes denotes the identity component or a different convention.

### G3. The analytic-to-topological correction prevents an unwarranted holomorphic identification

**Source:** cote 136, [scan 327](../pages/MPL_136_282-327_136_scan327.tex), lines 18–20 and 83–99. **Retained correction:** “fibré principal”, followed by deleted “analytique” and inserted “top.”.

The source identifies the family \(P_x\) with a flat **topological** principal bundle and gives its monodromy description; later it writes the split expression \(\Omega^{-1}\oplus\Omega\). A smooth or topological splitting does not identify the holomorphic bundle underlying a flat projective structure with the corresponding split holomorphic direct sum. **Own inference, high confidence:** this is the first comparison to settle before attempting the boxed algebraic construction; Hua’s short projective-structure/oper interpretation does not supply that identification.

### G4. A nonzero-degree obstruction to the literal boxed request

**Source:** cote 136, [scan 327](../pages/MPL_136_282-327_136_scan327.tex), lines 91–99. **Quotation:** \(\mathrm P(\Omega^{-1}+\Omega)=\overline{\mathrm V(\Omega^2)}\); line 98 explicitly uses \(\Omega^{-1}\oplus\Omega\).

**Own checked deduction:** put \(L=\Omega\), \(E=L^{-1}\oplus L\), and suppose \(\mathbb P(E)\) has a holomorphic principal \(\mathrm{PGL}_2\)-connection. The induced connection on its adjoint vector bundle is a connection on
\[
 \operatorname{End}_0(E)\simeq\mathcal O_X\oplus L^2\oplus L^{-2}.
\]
Projection to the direct summand \(L^2\) after inclusion and covariant differentiation gives a holomorphic connection on \(L^2\). Its degree must therefore be zero, contradicting \(2\deg L\ne0\).

The degree criterion is the line-bundle case of Atiyah (1957, Proposition 18(i), p. 202; Proposition 19 and Theorem 10, p. 203). **Confidence: high in the deduction, conditional on the stated holomorphic meaning and \(\deg\Omega\ne0\).** Neither \(\det E\simeq\mathcal O_X\) nor topological triviality removes the obstruction.

If \(\Omega=K_X\), its degree is \(2g-2\); if \(\Omega^2=K_X\), its degree is \(g-1\), so both common readings are obstructed for \(g\ge2\). Those are alternatives to investigate, not an identification of the manuscript’s notation. Meromorphic connections or connections compatible only with a smooth splitting are different questions from the regular algebraic/holomorphic reading just tested.

### G5. The jet-bundle comparison gives a precise candidate, with a notation caveat

**Source:** cote 136, [scan 326](../pages/MPL_136_282-327_136_scan326.tex), lines 45–47, 62–79; [scan 327](../pages/MPL_136_282-327_136_scan327.tex), lines 74, 81 and 98–99. **Quotation:** \(\mathrm P_{X/h}^n\); \(E\longrightarrow E\otimes\Omega\).

For a theta characteristic \(L^2=K_X\), the standard projective-structure comparison uses
\[
 0\longrightarrow L\longrightarrow J^1(L^{-1})
   \longrightarrow L^{-1}\longrightarrow0.
\]
Biswas, Hurtubise, and Roubtsov (2021, equation (2.6), Lemma 2.2 and Proposition 2.4, pp. 6–7) identify oper bundles with first jets and explicitly state that a projective structure produces a connection on \(J^1(K_X^{-1/2})\); their Corollary 2.6, p. 8, records the nonzero extension class. Its associated graded is \(L\oplus L^{-1}\), but the holomorphic extension does not split.

**Relation to Hua:** this gives precise content to his modern “structure projective (ou oper)” suggestion, credited to his project, and **adds** the distinction between an extension and its associated graded. **Confidence:** high for the cited construction; medium as an explanation of the manuscript’s nearby principal-parts sketches, because the missing identification is not written. If the source’s \(\Omega\) denotes \(K_X\) itself, the standard oper filtration has graded pieces \(K_X^{1/2},K_X^{-1/2}\), not the displayed \(K_X,K_X^{-1}\); replacing “\(+\)” by an extension alone would then be insufficient.

### G6. The uniqueness assertion needs its pointed normalization stated

**Source:** cote 136, [scan 327](../pages/MPL_136_282-327_136_scan327.tex), lines 22–25. **Quotation:** “une et une seule”; “l’image est un disque”; “l’application tangente … est l’identité”.

Hua, geometry subsection, lines 2185–2186, reports this assertion without expanding its normalization. **Own reading question:** if a map \(f\) satisfies only the two displayed conditions literally, then \(f+c\) has the same derivative and a translated disc image, so the standard uniqueness normalization requires both the marked point to map to the origin and the image disc to be centered there, unless both are implicit. **Confidence:** high for this elementary qualification, but only medium that the convention is genuinely omitted rather than implicit in the pointed notation; no change to the frozen wording is justified.

### G7. Hua’s Euler-class passage extends beyond what is verified in these retained scans

**Source:** cote 136, [scan 326](../pages/MPL_136_282-327_136_scan326.tex), lines 8 and 10–15, contains half-class notation and the complex/real group diagram; [scan 327](../pages/MPL_136_282-327_136_scan327.tex), lines 91–99, contains the boxed request. Scan 325 remains the PD-coalgebra list.

Hua’s geometry subsection labels the topic “pages 325 à 327,” locates the exact sequence on its page 325, and at lines 2189–2195 describes Euler classes, a lift obstruction in \(H^2(X,\mathbb Z/2)\), the expression \(2g-2\sim g-1\), and classifying-space cohomology diagrams. **The present package supports only the half-class/group-diagram part of that summary:** the explicit \(H^4(B_{\mathrm{SL}_2},\mathbb Z)\) calculation and \(2g-2\sim g-1\) are not in the frozen text of current scans 326–327. Record a pagination/coverage question and credit the additional material to Hua’s interpretation; do not attribute those calculations or a Milnor–Wood argument to the current retained pages without checking the adjacent source.

**Status and confidence:** high confidence about the difference between the supplied texts; the cause of the page-label mismatch is unresolved. No reading or theorem about omitted scan 328 is asserted.

## 2. Universal constructions: what the current pages add to Hua and to Pursuing Stacks

| Note | Current cote/scan and physical TeX lines | Source phrase | Context and precise comparison |
|---|---|---|---|
| U1. Ordinary cocompletion | 136/305, lines 15–26 and 31–61 | “pas seulement pour \(\boldsymbol\Delta\), et bien connu” | Hua, *“Notations simpliciales. Constructions universelles (pages 300 à 309)”*, lines 2021–2036, reads Proposition 1 as the Yoneda/left-Kan-extension universal property. The frozen text supports that ordinary categorical reading. It does not itself assert a derived universal property or invariance under weak equivalences. |
| U2. The homotopy programme is explicit | 136/302, line 22; 136/306, lines 17–34 | “types d’homotopie”; “catégories de fractions” | Hua, the same subsection, lines 2038–2050, correctly identifies a programme of enriching coarse invariants and then inverting arrows. These words directly explain the homotopy tags in RESULTS_STATE, lines 14–18; there is no need to infer them from the unrelated geometric leaf. |
| U3. The universal invariant is additive | 136/311, lines 43–74; 136/312, lines 3–13 | “l’invariant additif universel”; “la seule connaissance” | Hua, *“L’invariant additif universel (pages 310 à 317)”*, lines 2073–2088, is supported: the free simplicial abelian object and its normalized chain complex represent additive invariants, while recovering multiplication needs additional structure. This does not prove integral homotopy reconstruction from a bare chain complex. |
| U4. The restricted-limit claim retains a gap | 136/316, lines 38–57; 136/318, line 20 | “principes généraux (que je n’ai pas détaillés)”; “faire des projecteurs” | Hua, the additive subsection, lines 2114–2125, notes the undetailed principles but does not mention the projector proviso. The current margin **adds** a necessary warning: restricted operations must permit the required idempotent/projector constructions. The general \(U_{\mathcal L}\) claim should remain a qualified proposal. |
| U5. The monoidal warning is explicit | 136/318, lines 25–27 | “ne se correspondent … pas par DP et ND” | Hua, lines 2127–2139, supports the distinction between additive Dold–Kan equivalence and multiplication. His list at line 2135 has \(\otimes^i\), whereas the frozen line 27 has \(\Gamma^i\), alongside \(\Lambda^i,\mathrm{Sym}^i\); record that difference without changing the source. |

### PS1. Derived abelianization must remain distinct from U1–U3

**Context:** ps_chapters_VI_VII/ps7.tex, §134, *“Back to linearization in the modelizer (Cat): another handful of questions around Kan-Dold-Puppe”*, physical lines 116–219, manuscript pp. 557–559, equations (1)–(8). The discussion constructs \(\mathrm Lp_!^{\mathrm{ab}}\), distinguishes abelian weak equivalences from quasi-isomorphisms of complexes of presheaves, and warns that its displayed chain-level functor is not already the normalized Dold–Kan equivalence. This **adds a later derived comparison problem** to cote 136/305 and 311–314; it does not retroactively prove the original restricted-limit assertion.

**Further context:** ps7.tex, §136, physical lines 519–584, manuscript pp. 565–566, explains the model-dependent descriptions of abelianization and the relation to normalized simplicial chains after localization. Confidence is high in the textual comparison; no claim is made here about the truth of all the conjectures in §134.

### PS2. PD operations require homotopical hypotheses and coherent operations

**Context:** ps_chapters_VI_VII/ps6.tex, §111, physical lines 600–688, manuscript pp. 455–456, especially (y′), warns that applying \(\Gamma_k\) degreewise to an arbitrary complex does not compute its derived functor; the source inserts projective, or conjecturally adequate flat, resolutions. This sharpens the current 136/318 warning that nonlinear tensor operations cannot simply be read off from the additive equivalence.

**Further context:** ps6.tex, §120, *“Digression on the Lazare ‘analyzers’…”*, physical lines 3131–3197, manuscript pp. 506–507, treats PD, lambda, and binomial operations through an analyzer whose composition axioms are not fully written. This is a conceptual continuation of 136/312 and 318, not a constructed comparison with the weighted PD de Rham theory.

### PS3. “Universal torsor” has a separate additive meaning in the later chapter

**Context:** ps6.tex, §122, physical lines 3450–3490, manuscript pp. 511–512, equations (1)–(3), discusses the augmentation-one object in the free abelian object and its asserted universal property as an abelian torsor. This is an additive universal property in a topos, related to the universal abelianization of 136/313–314. It supplies no construction of the geometric projective torsor or connection in 136/327; the shared word “torsor” does not establish a mathematical identification.

## 3. RESULTS_STATE cross-reference ledger

All entries below are quoted with the supplied digest’s status; no status is changed by this dossier.

| Register ID and status | Digest locator | Current evidence and consequence |
|---|---|---|
| No geometry entry identified | Orientation, lines 14–19; targeted search of the full digest | G1–G7 form a separate Hua-credited geometric note. “No entry identified” is a statement about this supplied digest, not about all project records or the literature. |
| **follow-ups @305 — Open** | Line 305, from MPL_136_047-094 R054 | 136/311–312 and 318 explain why additive universality is insufficient for multiplicativity, PD operations on cohomology, or integral homotopy reconstruction. They sharpen the motivation; they do not settle the question. The finding **136-pd-de-rham-shadows** remains credited to Hua’s project. |
| **gap g1048 — Open** | Line 306, from MPL_136_235-281 N39 | 136/318, lines 25–27, distinguishes additive/derived reconstruction from multiplicative compatibility. The digest’s claims about g1031, g1041, g1034–g1035 and g1080 remain attributed claims; this passage supplies no new proof of those statements or of the remaining multiplicativity. |
| **follow-ups @304 — Open** | Line 307, from MPL_136_047-094 R052 | 136/318 and PS VI §120 motivate a comparison preserving nonlinear operations. Neither constructs the requested filtered comparison between weighted PD objects and cosimplicial binomial rings. |
| **gap g1004 — Open** | Line 308, from MPL_136_095-141 §5.1 | 136/305 and 313–316 give ordinary universal properties and a qualified restricted-operation proposal. They do not establish connectedness or simple connectedness of the localized groupoid of admissible PD de Rham theories. |
| **claims #243 — Open** | Line 304, from MPL_136_142-188 N027 | The operation symbol \(\Omega\) in the universal-construction discussion and the line-bundle symbol \(\Omega\) on 326–327 must not identify the PD-functor automorphism group with the geometric projective group. No direct contribution to this classification is established. |

The prior note same_cote_136/MPL_136_189-234_notes.md, R061–R064, physical lines 761–803, concerns algebraic descriptions of **Raynaud/abelian-scheme uniformization and Tate-module maps** on scans 230 and 234. It is useful evidence that “uniformization” already labels a different strand of the folder; it is not an earlier solution of the curve/projective-connection question on current scan 327.

## 4. Primary-source verification and APA references

**Atiyah — verified in the original journal PDF.** Locators used: Theorem 2, p. 188; Proposition 18(i), p. 202; Proposition 19 and Theorem 10, p. 203. G4 is our application of the classical criterion, not a claim of novelty or a theorem attributed to Hua.

Atiyah, M. F. (1957). Complex analytic connections in fibre bundles. *Transactions of the American Mathematical Society, 85*(1), 181–207. https://doi.org/10.1090/S0002-9947-1957-0086359-5  
Original PDF: https://www.ams.org/journals/tran/1957-085-01/S0002-9947-1957-0086359-5/S0002-9947-1957-0086359-5.pdf

**Biswas–Hurtubise–Roubtsov — verified in arXiv v1, not assigned an unverified later journal citation.** See equation (2.6), Lemma 2.2, Proposition 2.4 and Corollary 2.6, pp. 6–8; §9.1, pp. 37–38, distinguishes projective structures from their lifts with a theta characteristic.

Biswas, I., Hurtubise, J., & Roubtsov, V. (2021). *Vector bundles and connections on Riemann surfaces with projective structure* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2107.10440  
Version consulted: https://arxiv.org/pdf/2107.10440v1  
Author/date record: https://arxiv.org/abs/2107.10440

**Supplied interpretive source.** Hua, M. (project). (2026). *Modernised reading of cote 136* [AI-produced interpretive LaTeX file; supplied version downloaded 14 November 2026]. Relevant subsections are named above. Project source: https://github.com/Commutator-IO/grothendieck-project ; supplied file: context/hua_project/136.modern.tex. This credit identifies the project’s reading and does not turn its claims into primary manuscript evidence.

**Supplied manuscript context.** Grothendieck, A. (1983). *Pursuing Stacks*, Chapters VI–VII [Supplied TeX edition]. Locators: VI §§111, 120, 122; VII §§134, 136, with manuscript page numbers given above. No external edition or textual apparatus beyond the supplied files was used for those comparisons.

## 5. Suggested incorporation into the main notes

Retain G1 as the separate note required for Hua’s geometric subject outside the register; attach G2–G3 and G7 as source-comparison qualifications. Record G4 as a proved conditional application of a classical criterion, and G5–G6 as interpretation/normalization questions with their confidence levels. For the universal-construction section, U4’s projector margin and U5’s explicit \(\Gamma^i\) reading are the most concrete additions to Hua’s summary; PS1–PS2 explain why ordinary additive universality does not settle the currently open multiplicative and derived comparisons.
