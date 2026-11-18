# MPL 118 — STRATA and PATHS statement mapping

**Author:** GPT-6 Astra Pro. **Effort:** inherited/not exposed. **Generated:** 2026-11-18T03:18:09+00:00.

This appendix covers all **10 STRATA + 76 PATHS** rows of the supplied dossier against the frozen 118 transcription. Every supplied status remains the originating run’s claim. This work compares texts and definitions; it does not validate proofs or resolve the modern results.

The frozen transcription was read in full, as were `context/README.md` and `context/notes/RESULTS_STATE.md`. Relevant companion and Pursuing Stacks passages are identified below. No images, OCR, manuscript edits, or renewed transcription were used.

## Coverage and interpretation

| Relation | Count |
|---|---:|
| exact | 0 |
| partial | 3 |
| analogue | 10 |
| absent | 73 |
| contradicted | 0 |

**Absent** means no form on the supplied 118 pages; any evidence under an absent row is explicitly **nearest related only**. An **analogue** shares a construction, distinction, or method; a **partial** match identifies a substantive part but not the whole statement. No row is classified exact or contradicted.

The note kind **reading question** denotes the comparison question here, not an attribution of a question to Grothendieck. Confidence on an **own idea** concerns the textual analogy alone. Each comparison note has one to four sentences.

## Material findings

- **STRATA D.3, STRATA D.4, STRATA D.7:** The proper-lift criterion, proper/smooth base-change table, and sufficient open/closed inclusion directions have partial forms on scan009 and scan012.
  Context: `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100).; `context/companion/chunks/DER_I-a.tex` — ms.49–50 dgrb25; ms.58–59 dgrb30, The converse, and why spaces suffice (file lines 1931–1952,2263–2294).; `context/ps_chapters_VI_VII/ps7.tex` — §137, pp.576–577, equation(13) and its asphericity condition (file lines 1035–1085).; `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790).
- **STRATA D.6, PATHS E.3, PATHS E.4, PATHS E.5:** Scan014 explicitly separates proper/smooth Serre properties from strict categorical cofibration/fibration; scans011–012 provide comma replacements with a stated not-yet-Serre limitation, not the later endpoint models.
  Context: `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280).; `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790).
- **PATHS D.16:** Scan029 explicitly identifies unbounded lengths of elementary homotopies in an infinite family; this supports a close analogy with the later bounded-winding obstruction, without supplying its circle-poset or Kaledin claims.
  Context: `context/companion/chunks/DER_XIII-a.tex` — ms.55–56, dgrb709, Localization axioms, stability, and locally constant coefficients (file lines 2241–2253).
- **PATHS B.5, PATHS D.8, PATHS D.17:** Scans024–026 give finite factorization/pushout/interval conditions for left fractions; they do not state the later intrinsic cofibration axioms or rectification theorems.
  Context: `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045).; `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565).
- **STRATA G.2, PATHS A.5, PATHS A.6, PATHS A.7, PATHS E.12:** The product/diagonal usage of total asphericity on scans033–036 must not be identified with the later all-outgoing-functors definition; XII §V.2.3, Definition1, ms.88–89 contains an explicit terminology warning.
  Context: `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197).
- **PATHS C.P3:** The dossier claims that the CATHOT E.26 comparisons are settled, while RESULTS_STATE still labels CATHOT E.26 Open; this is a supplied-record status tension, not a mathematical adjudication from 118.
  Context: `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837).

## Statement-by-statement comparison

### STRATA D.1 — Exceptional adjunction chains and support images

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** A pointed Der 1–4 presheaf derivator has the exceptional adjunction chains j^? ⊣ j_! ⊣ j^* ⊣ j_* and i_! ⊣ i^* ⊣ i_* ⊣ i^!, with the stated support images.

**Supplied locator:** I ms.1–9; Lead 4. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 15.

**Comparison note:** No form of the pointed-derivator adjunction chains is stated on the supplied 118 pages. The nearest material is the open–closed decomposition and its bifunctor H_X on scan017, which concerns ordinary categories and gives neither j^? nor i^! or their support images.

**Nearest related only — 118 scan017, fragment line 5:**

```tex
U\subset X\supset Y\qquad H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.50–52, dgrb26, Fully faithful direct image and extension by a terminal object (file lines 1992–2050). Supplied text and AI commentary; no proof validation.
- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.1.1, ms.59–61, Proposition1; dgrb507, An open–closed cut remembers a profunctor (file lines 9–123). Supplied text and AI commentary; textual matching only.

### STRATA D.2 — Coherent support sequences and stable recollement

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Pointed derivators have coherent support fibre/cofiber sequences and the bicartesian open-closed square; stable strong derivators have the associated triangulated recollement.

**Supplied locator:** I ms.2–9; Lead 4 exactness clauses. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 16.

**Comparison note:** No fibre/cofibre support sequence or stable triangulated recollement appears on the supplied 118 pages. Scan017 supplies category-gluing data, while scans019–023 discuss categorical pushout comparisons; neither is a statement about a pointed derivator’s coherent support square.

**Nearest related only — 118 scan017, fragment line 5:**

```tex
U\subset X\supset Y\qquad H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}
```

**Nearest related only — 118 scan021, fragment line 22:**

```tex
Ce foncteur est une cofibration, à fibres les
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.50–52, dgrb26, Fully faithful direct image and extension by a terminal object (file lines 1992–2050). Supplied text and AI commentary; no proof validation.
- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.1.1, ms.59–61, Proposition1; dgrb507, An open–closed cut remembers a profunctor (file lines 9–123). Supplied text and AI commentary; textual matching only.

### STRATA D.3 — Proper and smooth poset maps via exact lifts

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** unproved claim.

**Dossier statement:** A poset map is W_infinity-proper exactly when all outgoing exact lifting posets are weakly contractible, and smooth exactly when all incoming ones are weakly contractible.

**Supplied locator:** I ms.53–56; Lead 4 map classification. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 17.

**Comparison note:** Scan009 explicitly puts properness in equivalence with asphericity of the category of lifts of a base arrow with prescribed source, so the proper half of the later lift criterion has an identifiable categorical form here. The smooth column is largely left blank and the finite-poset specialization is not separately formulated; the fuller poset statement is in Pursuing Stacks §137.

**Manuscript evidence — 118 scan009, fragment line 14:**

```tex
\text{La cat. des rel. d'une flèche }b\to b',\\\text{de source donnée }a\in\mathrm{Ob}\,\unsure{X_b},\text{ est asph.}
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/ps_chapters_VI_VII/ps7.tex` — §137, pp.576–577, equation(13) and its asphericity condition (file lines 1035–1085). Supplied text on the poset lifting criterion; no proof validation.

### STRATA D.4 — Proper/smooth strict base change and detection

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** unproved claim.

**Dossier statement:** Strict-pullback right base change holds if the vertical functor is proper or the base-change functor smooth; left base change has the dual conditions, and universal space-valued tests detect them.

**Supplied locator:** I ms.49–59; VI ms.162–169; Lead 4. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 18.

**Comparison note:** Scan009 links properness to commutation of R^i f_* with arbitrary base change and places the smooth base-change criterion in the parallel column. It does not state the complete derivator-level dual mate theorem or detection by universal space-valued tests, and its extra implication toward preservation of weak equivalences is marked with a question.

**Manuscript evidence — 118 scan009, fragment line 15:**

```tex
R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}
```

**Manuscript evidence — 118 scan009, fragment line 15:**

```tex
\text{\unsure{Le changt} de base par }f\\\text{commute à }R^i g_*
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449); **BISITE A.19** (Proved (the return's claim); line 381); **GALOIS D.2** (Proved (the return's claim); line 392).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.49–50 dgrb25; ms.58–59 dgrb30, The converse, and why spaces suffice (file lines 1931–1952,2263–2294). Supplied text and AI commentary; later space-detection proof carried as a claim.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### STRATA D.5 — Failure of naive geometric characterizations

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Topological properness, strict-versus-homotopy-fibre comparison, or stratified local product structure characterize categorical properness and smoothness for finite posets.

**Supplied locator:** Ib-C003; I ms.53–59; GALOIS D.9; Lead 4. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 19.

**Comparison note:** No form of the claimed finite-poset counterexamples to the proposed geometric characterizations occurs on the supplied 118 pages. Scan009 supplies categorical lift and base-change criteria, but no comparison with topological properness or a stratified local product structure.

**Nearest related only — 118 scan009, fragment line 14:**

```tex
\text{La cat. des rel. d'une flèche }b\to b',\\\text{de source donnée }a\in\mathrm{Ob}\,\unsure{X_b},\text{ est asph.}
```

**RESULTS_STATE links:** **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/ps_chapters_VI_VII/ps7.tex` — §137, pp.576–577, equation(13) and its asphericity condition (file lines 1035–1085). Supplied text on the poset lifting criterion; no proof validation.

### STRATA D.6 — Diamond: smooth/proper without opfibration or bundle

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** The four-object diamond map to [1] is proper and smooth and a Grothendieck fibration, but is neither an opfibration nor a locally trivial topological fibre bundle.

**Supplied locator:** VIc-C008 strictness comparison; Lead 4. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 20.

**Comparison note:** Own comparison: scan014 explicitly distinguishes proper Serre maps from cofibrations and smooth Serre maps from fibrations, anticipating the need to separate homotopical and strict lifting properties. The four-object diamond and the bundle assertion are absent, so this is a shared distinction rather than the dossier’s example.

**Confidence in this own comparison:** high — The nonimplications are explicit; no identification of a particular witness is made.

**Manuscript evidence — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### STRATA D.7 — Poset inclusions, projections, and image conditions

**Supplied status:** claim (return: Proved). **Relation:** partial. **Kind:** unproved claim.

**Dossier statement:** Full poset inclusions are proper precisely for cosieves and smooth precisely for sieves; product projections have both properties and images obey the stated component conditions.

**Supplied locator:** I ms.54–56; Lead 4 examples and edge cases. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 21.

**Comparison note:** The diagrams in scans009 and012 place open immersions among fibrations and closed immersions among cofibrations, with F⇒Sm and C⇒Pr recorded explicitly. This supplies the sufficient inclusion direction, but not the full necessity statement for poset inclusions, the product-projection assertion, or the stated image conditions.

**Manuscript evidence — 118 scan009, fragment line 29:**

```tex
F\Longrightarrow\mathrm{Sm}\\C\Longrightarrow\mathrm{Pr}
```

**Manuscript evidence — 118 scan012, fragment line 43:**

```tex
\text{open immersions}\longleftrightarrow X^\circ\xrightarrow{\varphi}\Delta^1=[0\longrightarrow1]
```

**Manuscript evidence — 118 scan012, fragment line 49:**

```tex
\text{Closed immersions}\longleftrightarrow X\xrightarrow{\varphi}\Delta^1
```

**RESULTS_STATE links:** **STRATA 0.1** (Proved (the return's claim); line 400); **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### STRATA D.8 — Finite-poset coefficient dictionary and geometric base change

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The finite-poset coefficient dictionary transports intrinsic base change; closed inclusions and finite product projections admit the specified ambient geometric interpretation, while arbitrary monotone maps do not.

**Supplied locator:** Lead 4 constructible base-change comparison. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 22.

**Comparison note:** No form of the finite-poset constructible-coefficient dictionary or its ambient geometric comparison is given on the supplied 118 pages. The nearest item is the categorical proper/smooth base-change table on scan009, without a stratified geometric realization or constructible coefficients.

**Nearest related only — 118 scan009, fragment line 15:**

```tex
R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}
```

**RESULTS_STATE links:** **STRATA A.4** (Proved (the return's claim); line 378); **BISITE G.10** (Proved (the return's claim); line 385); **WG2 §3.2 #7** (question or plan item of the war game (round 2; unchecked); line 449).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.49–50 dgrb25; ms.58–59 dgrb30, The converse, and why spaces suffice (file lines 1931–1952,2263–2294). Supplied text and AI commentary; later space-detection proof carried as a claim.
- `context/ps_chapters_VI_VII/ps7.tex` — §137, pp.576–577, equation(13) and its asphericity condition (file lines 1035–1085). Supplied text on the poset lifting criterion; no proof validation.

### STRATA D.9 — Slice-target and specialization-order corrections

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The smoothness fibre-inclusion target at I ms.54 is y\X; with downsets open, the compatible closure formula at XII ms.59 is y in closure{x} when x<=y.

**Supplied locator:** I ms.54; XII ms.59. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 23.

**Comparison note:** The two corrections refer to different manuscripts, I ms.54 and XII ms.59, and neither corrected formula is stated as such on the supplied 118 pages. Scan009 contains related comma-category notation with marked reading doubts, but that does not authorize importing the later correction into its frozen text.

**Nearest related only — 118 scan009, fragment line 14:**

```tex
\text{La cat. des rel. d'une flèche }b\to b',\\\text{de source donnée }a\in\mathrm{Ob}\,\unsure{X_b},\text{ est asph.}
```

**RESULTS_STATE links:** **STRATA 0.1** (Proved (the return's claim); line 400).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.52–54; dgrb27, Properness as a condition on all lifts; Morphismes homotopiquement propres, homotopiquement lisses (file lines 2054–2100). Supplied text and AI companion commentary; no proof validation in this task.
- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.1.1, ms.59–61, Proposition1; dgrb507, An open–closed cut remembers a profunctor (file lines 9–123). Supplied text and AI commentary; textual matching only.

### STRATA G.2 — Later totality and universal simplicial colimits

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Total W-infinity asphericity is exactly the canonical homotopy-colimit to strict-colimit equivalence for every simplicial diagram on a connected base.

**Supplied locator:** XII ms.88–89; TOTASPHB.11. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 24.

**Comparison note:** No form of the universal simplicial homotopy-colimit/strict-colimit criterion occurs on the supplied 118 pages. Scans033–036 use total asphericity in the product/diagonal sense, whereas XII §2.3 Definition1 at ms.88–89 quantifies over all outgoing functors and expressly warns that its notion differs from Pursuing Stacks, so the shared term is not a match.

**Nearest related only — 118 scan035, fragment line 26:**

```tex
(i)\quad A\text{ tot. }\underline W\text{-asph.}
```

**Nearest related only — 118 scan035, fragment line 12:**

```tex
(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}
```

**RESULTS_STATE links:** **TOTASPH A.2** (Known (the return's claim); line 404); **TOTASPH A.7** (Known (the return's claim); line 405); **TOTASPH C.10** (Refuted (the return's claim); line 408); **TOTASPH D.7** (Open (the return's claim); line 353).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.

### PATHS A.P1 — Path components recover localized Hom

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The full path-category component set is the ordinary localized Hom-set, naturally and compatibly with composition.

**Supplied locator:** VII ms.65–74. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 32.

**Comparison note:** No form of the full path-category component theorem is stated on the supplied 118 pages. Scan024 gives a left-fraction calculus after quotienting by interval homotopy, but it neither defines the all-type path category nor identifies its component set.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS A.P2 — Sequential path model and Grothendieck roof

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The exact sequential model is connected to the all-type category by the specified fibred Grothendieck roof; both legs are weak equivalences for preorder-cofinal path sequences.

**Supplied locator:** VII ms.99–110. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 33.

**Comparison note:** No all-type/sequential path roof occurs on the supplied 118 pages. The sequential system in scan041 is a chain of open immersions used for saturation, not a cofinal sequence of path types.

**Nearest related only — 118 scan041, fragment line 17:**

```tex
système inductif d'imm. ouvertes
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.1 — Fibred/opfibred comparison span

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The fibred and opfibred Grothendieck constructions give the specified span C <- C_u -> C_infinity; no general direct C -> C_infinity functor is supplied.

**Supplied locator:** VII ms.99-110; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 34.

**Comparison note:** No form of the span C←C_u→C_infinity or its missing direct comparison is given on the supplied 118 pages. The Fib(f) factorizations of scans011–014 are different constructions and do not supply that span.

**Nearest related only — 118 scan012, fragment line 13:**

```tex
\uline{but not yet Serre}
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.2 — Filtered Cat-colimit comparison

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** For every filtered indexing category A and every D:A->Cat, the canonical Grothendieck-total-category to Cat-colimit functor is a weak equivalence; the sequential fibred version follows by opposites.

**Supplied locator:** VII ms.108-109; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 35.

**Comparison note:** Own comparison: scans039–040 give an argument for invariance of specified unions of open or closed subcategories by asserting an identification of stage maps with comma maps and invoking L3. The strict-triangle step has the lax-commutation gap addressed by the separate repair in MPL118-C03. This restricted passage-to-the-limit argument does not assert that every filtered Cat-diagram has its Grothendieck total category weakly equivalent to its strict colimit.

**Confidence in this own comparison:** high — The union hypotheses and L3 conclusion are explicit; no universal filtered-diagram conclusion is inferred.

**Manuscript evidence — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**Manuscript evidence — 118 scan040, fragment line 24:**

```tex
donc on gagne par L3.
```

**RESULTS_STATE links:** **RESIDUE F.7** (Open (the return's claim); line 351).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.565–567, discussion of Thomason’s total-category description of integration (file lines 516–615). Supplied Pursuing Stacks text; no theorem attributed to 118 from this separate source.

### PATHS A.3 — Cofinal base functors detected by all fibred diagrams

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** A base functor u:J->T induces weak equivalences of fibred total categories for every strict F:T^op->Cat iff every u/t is weakly contractible.

**Supplied locator:** VII ms.99-110; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 36.

**Comparison note:** Own comparison: the asserted comma-map identification and appeal to L3 on scan040 exhibit the same intended fibrewise-to-total method used in the dossier’s base-change criterion. The strict-triangle step needs the separate lax-commutation repair in MPL118-C03, and the universal quantification over all F and converse characterization of u/t are absent from 118.

**Confidence in this own comparison:** medium — The common method is explicit, but the quantified theorem and its converse are not stated.

**Manuscript evidence — 118 scan040, fragment line 24:**

```tex
donc on gagne par L3.
```

**RESULTS_STATE links:** **GALOIS B.3** (Proved (the return's claim); line 377).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.4 — Preorder cofinality does not suffice

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Preorder cofinality plus homotopy of parallel reindexing maps does not imply the total/sequential comparison is a weak equivalence.

**Supplied locator:** VII ms.99-109; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 37.

**Comparison note:** No form of the counterexample combining preorder cofinality with homotopic reindexing maps occurs on the supplied 118 pages. The ordered-index filtration theorem on scans039–040 adds infimum and intersection hypotheses and does not discuss discarded parallel-arrow information.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.5 — Delta_inj: totality does not ensure Cat-colimit correctness

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Total W_infinity-asphericity of A does not make every Cat-valued colimit homotopically correct: for Delta_inj and D([n])=B N^(n+1), the total category has integral H_k=Z in every degree whereas the Cat colimit has type S1.

**Supplied locator:** After TOTASPH correction; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 38.

**Comparison note:** The Delta_inj diagram and its integral-homology versus circle calculation have no form on the supplied 118 pages. The total-asphericity discussion in scans033–036 is about products of representables, not the later universally quantified totality used by this row.

**Nearest related only — 118 scan035, fragment line 12:**

```tex
(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}
```

**RESULTS_STATE links:** **TOTASPH C.10** (Refuted (the return's claim); line 408); **RESIDUE F.7** (Open (the return's claim); line 351).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.
- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.6 — Delta_inj is exact and total but not filtered

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Delta_inj has exact abelian-group-valued colimits and is totally W_infinity-aspherical but is not filtered.

**Supplied locator:** TOTASPH C.7-C.10 verification. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 39.

**Comparison note:** No Delta_inj example, exactness of abelian-group colimits, or totality-versus-filteredness theorem occurs on the supplied 118 pages. The similarly named condition on scans033–036 belongs to the earlier product/diagonal terminology and cannot be substituted for the dossier’s totality hypothesis.

**Nearest related only — 118 scan035, fragment line 26:**

```tex
(i)\quad A\text{ tot. }\underline W\text{-asph.}
```

**RESULTS_STATE links:** **TOTASPH C.10** (Refuted (the return's claim); line 408); **PRETOT A.12** (Proved (the return's claim); line 398); **RESIDUE F.3** (Proved (the return's claim); line 399).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.

### PATHS A.7 — Filtered, correct-Cat-colimit, and total shape classes

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For nonempty connected shapes, filtered categories are contained in the universally correct Cat-colimit shapes, which are strictly contained in the totally W_infinity-aspherical shapes.

**Supplied locator:** Part A; VIIb-C026. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 40.

**Comparison note:** No form of this chain of shape classes or its strictness assertion appears on the supplied 118 pages. Scans039–040 treat special filtrations, and scans033–036 concern a different total-asphericity notion, so neither gives the requested classification.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**Nearest related only — 118 scan035, fragment line 26:**

```tex
(i)\quad A\text{ tot. }\underline W\text{-asph.}
```

**RESULTS_STATE links:** **RESIDUE F.7** (Open (the return's claim); line 351); **TOTASPH C.10** (Refuted (the return's claim); line 408).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.
- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.

### PATHS A.8 — Open classification of universally correct Cat-colimit shapes

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** An exact intrinsic classification of universally correct Cat-colimit shapes, including whether all connected such shapes are filtered, remains unresolved here.

**Supplied locator:** Part A. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 41.

**Comparison note:** The supplied 118 pages do not formulate or settle the intrinsic classification of universally correct Cat-colimit shapes. Their passage-to-the-limit theorem applies to the specific open/closed filtrations of scans039–040 and does not test arbitrary Cat-valued diagrams.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **RESIDUE F.7** (Open (the return's claim); line 351).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS A.9 — Finite weak equivalence without categorical homotopy inverse

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The last-element map sd P->P for the six-face triangle-boundary poset is a weak equivalence with no inverse modulo zigzags of natural transformations; all 456 reverse monotone maps have degree zero.

**Supplied locator:** POLES D.6 verification; VIIc-A046; V-I066. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 42.

**Comparison note:** The subdivision map of the triangle-boundary face poset and the enumeration of 456 reverse maps have no form on the supplied 118 pages. Scans029–031 distinguish interval homotopy from localization by a different, infinite-family obstruction.

**Nearest related only — 118 scan029, fragment line 7:**

```tex
une suite d'au moins $n$ homotopies él. pour les joindre
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.
- `context/companion/chunks/DER_XIII-a.tex` — ms.55–56, dgrb709, Localization axioms, stability, and locally constant coefficients (file lines 2241–2253). AI commentary distinguishes finite padding from lack of uniform bounds; textual comparison only.

### PATHS B.1 — Full and weak-vertical path diagrams

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The full and weak-vertical path diagrams and their literal inclusion are well-defined and strictly compatible with concatenation.

**Supplied locator:** VII ms.27–78. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 43.

**Comparison note:** No full/weak-vertical path diagram or concatenation-compatible inclusion is defined on the supplied 118 pages. Scan024’s fraction calculus is the nearest localization discussion, without marked internal vertical arrows.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.2 — Restricted paths and hammock localization

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The restricted all-type Grothendieck nerve maps weakly equivalently to the hammock mapping simplicial set by a strict composition-compatible reduction.

**Supplied locator:** Lead1 weak-vertical identification. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 44.

**Comparison note:** No hammock mapping simplicial set or restricted all-type comparison occurs on the supplied 118 pages. The fraction calculus on scan024 does not provide the stronger composition-compatible nerve comparison.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.3 — Full/restricted inclusion need not be an isomorphism

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The inclusion J need not be an isomorphism of categories, even when the marking is saturated.

**Supplied locator:** Lead1 forcing claim. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 45.

**Comparison note:** No form of the inclusion J or its counterexample occurs on the supplied 118 pages. Strong saturation is stated on scan040, but saturation alone is not an occurrence of a theorem about J.

**Nearest related only — 118 scan040, fragment line 31:**

```tex
\uuline{Thm} L'ens. $\underline W$ est saturé
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.4 — Extreme markings make J a weak equivalence

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** If Sigma is contained in the isomorphisms, the full all-type category is discrete in Cat hot and J is a weak equivalence; if all arrows are marked J is the identity.

**Supplied locator:** Lead2. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 46.

**Comparison note:** No statement about the markings consisting of isomorphisms or all arrows, or the resulting path inclusion J, occurs on the supplied 118 pages. The ordinary localization formula on scan024 does not specialize an all-type path construction.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.5 — Homotopy fraction calculi on the restricted side

**Supplied status:** claim (return: Known). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** Homotopy fraction calculi identify the restricted short-fraction categories; two-out-of-three forces their vertical arrows marked.

**Supplied locator:** Part B HCF/model/fibrant-object sufficient statements on restricted side. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 47.

**Comparison note:** Own comparison: scans024–026 develop a left-fraction calculus from factorization, pushout stability, and separating intervals, making a concrete precursor to short-fraction methods. They do not identify restricted path categories or use two-out-of-three to force hammock vertical arrows to be marked.

**Confidence in this own comparison:** high — A fraction calculus and its hypotheses are explicit; the comparison is methodological, not an identification of path models.

**Manuscript evidence — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**Manuscript evidence — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**Manuscript evidence — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.
- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.

### PATHS B.6 — Full path comparison split monic in Hot

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The full path space maps coherently to the localization mapping space; its composite with J is the hammock comparison, so J is split monic in Hot.

**Supplied locator:** VII ms.68–70;PartB partial comparison. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 48.

**Comparison note:** No coherent full-path map, hammock composite, or split monomorphism J in Hot occurs on the supplied 118 pages. Their localization discussion concerns ordinary fraction representatives rather than localization mapping spaces.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.7 — Grid-sweep padding of a backward square

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** An arbitrary backward commuting square becomes a weak-vertical hammock between mixed boundary paths after identity padding.

**Supplied locator:** PartB grid-sweep reduction. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 49.

**Comparison note:** No grid-sweep reduction of an arbitrary backward square to a weak-vertical hammock appears on the supplied 118 pages. The common finite interval used in scan028 serves a coproduct homotopy argument and has no marked-hammock interpretation there.

**Nearest related only — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.8 — Open unrestricted-vertical path comparison

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Whether J is always a weak equivalence, including wide/two-out-of-three/saturated/HCF/model/Brown variants beyond B.4.

**Supplied locator:** PartB central unrestricted-vertical comparison. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 50.

**Comparison note:** The general weak-equivalence question for J is not formulated or settled on the supplied 118 pages. Fraction calculus after homotopy quotienting, as on scan024, does not itself answer the full-versus-restricted path comparison.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS B.9 — Bounded finite search on path comparisons

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** All 132 bounded full/restricted path-category comparisons in the specified finite search have equal H0 and H1 over F2.

**Supplied locator:** PartB requested finite search. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 51.

**Comparison note:** The 132 finite comparisons and their F2 homology calculations have no form on the supplied 118 pages. No finite computational search or numerical path-category homology table occurs in this manuscript.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.P1 — Contractible type-map categories and enriched composition

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The category of increasing endpoint-preserving maps between two types is empty or categorically contractible and supports strict enriched composition.

**Supplied locator:** VII ms.86–94. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 52.

**Comparison note:** No category of endpoint-preserving maps between path types or strict enriched composition is constructed on the supplied 118 pages. The finite interval synchronization on scan028 concerns homotopies of maps from a coproduct, not the category of interval types.

**Nearest related only — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS C.P2 — Reachability-preorder descent of full paths

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The full path-space diagram descends coherently to the reachability preorder; both the ordinary type index and any preorder-cofinal sequence are homotopy final there.

**Supplied locator:** VII ms.99–123. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 53.

**Comparison note:** No full-path diagram over a reachability preorder or comparison with a cofinal type sequence occurs on the supplied 118 pages. The ordered filtration index of scans039–040 is an unrelated construction with explicit infimum assumptions.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS C.P3 — Three CATHOT E.26 comparisons claimed settled

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** All three specified general comparisons in CATHOT E.26 hold for arbitrary wide markings.

**Supplied locator:** CATHOT E.26(1),(2),(3);VIIc-A046 in Hot;V-I066 in Hot. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 54.

**Comparison note:** None of the three general path-type comparisons is stated on the supplied 118 pages. The dossier labels this PATHS row Proved while RESULTS_STATE still lists CATHOT E.26 as Open; both are supplied run statuses, and the filtration argument of scans039–040 does not adjudicate them.

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS C.P4 — Mixed-sign padding and block-independent composition

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Every block containing both signs gives weak padding maps, the canonical associative unital composition in Hot, and block-independent operations.

**Supplied locator:** CATHOT E.27;IX-037 raw path composition;VII ms.125–127. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 55.

**Comparison note:** No mixed-sign block theorem or canonical associative path composition is stated on the supplied 118 pages. Scan028 uses a common interval for finitely many homotopies but contains no block-independent multiplication in Hot.

**Nearest related only — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS C.P5 — Four-object crown defeats Cat-hot invertibility

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The actual q_L need not be invertible in Cat hot, already for a four-object crown with all arrows marked.

**Supplied locator:** VIIc-A046 in Cat hot;V-I066 strong independence inference. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 56.

**Comparison note:** The map q_L and its four-object crown counterexample have no form on the supplied 118 pages. The warning about nonuniform homotopy lengths in scan029 concerns infinite coproducts rather than this finite comparison.

**Nearest related only — 118 scan029, fragment line 7:**

```tex
une suite d'au moins $n$ homotopies él. pour les joindre
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS C.1 — All-type Cat enrichment, nerves, and Segal model

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The raw all-type path categories form a strictly unital associative Cat-enrichment; their nerves and product-preserving Kan replacements give a simplicial category and a Segal model.

**Supplied locator:** IX-037. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 57.

**Comparison note:** No all-type Cat-enrichment, product-preserving Kan replacement, or Segal model is constructed on the supplied 118 pages. The tentative Kan-type condition mentioned on scan031 concerns a common target for fraction representatives, not enrichment.

**Nearest related only — 118 scan031, fragment line 27:**

```tex
\uline{Il faut une condition du type ``\unsure{Kan}'' sur $Y$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS C.2 — Weak-vertical hammocks model simplicial localization

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Weak-vertical hammocks give a composition-compatible model of simplicial localization; this theorem alone does not replace arbitrary vertical arrows.

**Supplied locator:** IX-037. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 58.

**Comparison note:** No weak-vertical hammock model or simplicial-localization theorem occurs on the supplied 118 pages. Scan024 concerns an ordinary category of fractions, a weaker and different level of structure.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.69–70, dgrb354, Relations before higher homotopies (file lines 535–552). AI commentary on path components and vertical-arrow restrictions, carried as background.

### PATHS C.3 — Pointed Cartesian composition versus smash units

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Pointed Cartesian composition cannot give the intended zero-preserving units unless identities equal zero; smash composition has the correct unit S0.

**Supplied locator:** IX-044; IX-049. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 59.

**Comparison note:** The zero-preserving Cartesian-composition obstruction and smash-unit S0 statement have no form on the supplied 118 pages. Their finite-product discussion concerns Hot and presheaf localizations, without pointed mapping objects or absorbing zeros.

**Nearest related only — 118 scan032, fragment line 3:**

```tex
les produits finis existent
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.4 — Pointed simplicial mapping spaces with strict zero

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Cofibrant-fibrant objects in a pointed simplicial model category supply Kan mapping spaces with strict absorbing zero, smash composition, and S0-units.

**Supplied locator:** IX-044; IX-049; IX-052. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 60.

**Comparison note:** No pointed simplicial model category, cofibrant-fibrant mapping space, strict absorbing zero, or smash composition occurs on the supplied 118 pages. The word cofibration in the early classification tables denotes categorical opfibration, so it does not supply this model-categorical result.

**Nearest related only — 118 scan009, fragment line 29:**

```tex
F\Longrightarrow\mathrm{Sm}\\C\Longrightarrow\mathrm{Pr}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS C.5 — Quillen fundamental groupoid of a mapping complex

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Quillen’s fundamental groupoid agrees naturally with that of the derived mapping complex under cofibrant/fibrant replacement; specified vertices and basepoint paths determine the corresponding pi1 comparisons.

**Supplied locator:** IX-040; IX-041; IX-072. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 61.

**Comparison note:** No derived-mapping-complex comparison with Quillen’s fundamental groupoid occurs on the supplied 118 pages. Scan023 mentions equivalence of fundamental groupoids for a proposed pushout property, not the homotopy groups of a mapping space.

**Nearest related only — 118 scan023, fragment line 23:**

```tex
équiv. sur les groupoïdes fondamentaux
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.6 — Coherent loop/suspension identities and adjunction

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Pointed infinity categories with the required pullbacks and pushouts have mapping-space loop/suspension formulas; a pointed derivator has the corresponding adjunction and exact morphisms.

**Supplied locator:** IX-084; IX-087. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 62.

**Comparison note:** No mapping-space loop formula, suspension adjunction in a pointed derivator, or exact morphism theorem occurs on the supplied 118 pages. The cones and cofibres noted in scans011–014 are ordinary categorical constructions and questions, without the claimed pointed formalism.

**Nearest related only — 118 scan012, fragment line 19:**

```tex
and homotopism
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.

### PATHS C.7 — Pi1 representability does not force loop formulas

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Representability of all pi1 mapping functors does not imply the mapping-space loop formulas.

**Supplied locator:** IX-084; tests (a) and (c). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 63.

**Comparison note:** No form of the representability counterexample or the associated loop formulas appears on the supplied 118 pages. The isolated fundamental-groupoid question on scan023 concerns gluing rather than representability of mapping functors.

**Nearest related only — 118 scan023, fragment line 23:**

```tex
équiv. sur les groupoïdes fondamentaux
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.8 — Truncated derived Hom for complexes of modules

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For complexes of modules over a commutative ring k, truncated derived Hom takes values in D^{<=0}(k), with derived-tensor composition, units, and the prescribed mapping-space homotopy groups.

**Supplied locator:** IX-061; IX-065; IX-070. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 64.

**Comparison note:** The derived-Hom object in D^{<=0}(k), derived-tensor composition, and its units and homotopy groups have no form on the supplied 118 pages. No complexes of modules or coefficient-ring construction occurs in the mathematical notes.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.9 — Open additive relative-category enhancement

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The general additive relative-category proposal has not been proved from the manuscript’s unspecified additional axioms, or merely from finite-sum closure of a saturated weak class.

**Supplied locator:** IX-061; IX-065; IX-070. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 65.

**Comparison note:** No additive relative-category construction or its additional axioms is formulated on the supplied 118 pages. Their statements about coproducts and saturation in Cat and presheaf categories do not assert an additive or derived-Hom enhancement.

**Nearest related only — 118 scan027, fragment line 3:**

```tex
les sommes directes finies existent
```

**Nearest related only — 118 scan040, fragment line 31:**

```tex
\uuline{Thm} L'ens. $\underline W$ est saturé
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS C.10 — Open pointed and ind-category full-path refinements

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The literal pointed and pointed-ind-category refinements of stabilized full paths remain unresolved in the stated generality.

**Supplied locator:** IX-044; IX-049; IX-052; IX-072. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 66.

**Comparison note:** No pointed or pointed-ind-category refinement of stabilized full paths occurs on the supplied 118 pages. A sequential open-immersion construction is used for saturation in scan041, without stabilized path ind-objects.

**Nearest related only — 118 scan041, fragment line 17:**

```tex
système inductif d'imm. ouvertes
```

**RESULTS_STATE links:** **CATHOT E.26** (Open (the return's claim); line 357); **PATHS D.22** (Open (the return's claim); line 364).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS D.1 — Typed and size-bounded IX recognition tests

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Typed, size-bounded versions of IX tests (a), (b), (c); distinguish both representability directions and the two readings of homotopes in (b).

**Supplied locator:** IX ms.22-23; IX-080. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 67.

**Comparison note:** No form of the IX tests (a), (b), and (c), their two representability directions, or their size-bounded formulation occurs on the supplied 118 pages. The ordinary fraction calculus on scan024 does not identify these mapping-functor tests.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.2 — Five-arrow identity-marked example rectifies

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The five-arrow pointed category with identity weak equivalences rectifies every small shape and satisfies the tests and Kaledin enhancement; the contrary clause of Lead 3 is false.

**Supplied locator:** IX ms.23; IX-080; Lead 3; CATHOT E.14; Kaledin addendum (iii). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 68.

**Comparison note:** The five-arrow pointed category, its identity marking, and its claimed all-shape rectification have no form on the supplied 118 pages. Thus these pages neither supply the example nor adjudicate the contrary Lead 3 clause.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.3 — Finite products force a finite category to be a preorder

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** A finite category with all finite products is a preorder; if pointed it is equivalent to the terminal category. The IX finite example lacks x times x.

**Supplied locator:** IX ms.23. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 69.

**Comparison note:** No form of the finite-category counting argument, the pointed terminality conclusion, or the missing product in the IX example appears on the supplied 118 pages. Scan032 concerns existence and preservation of finite products in localized presheaf categories, without assuming the category itself finite.

**Nearest related only — 118 scan032, fragment line 3:**

```tex
les produits finis existent
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.4 — Rectifiability yields the constant-diagram mapping formula

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Rectifiability on a specified shape class implies H_ab(A)=[BA,Map_L(M,W)(a,b)] naturally, hence constant-diagram test (b).

**Supplied locator:** IX ms.22; IX-080; Lead 3. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 70.

**Comparison note:** No form of the comparison H_ab(A)=[BA,Map_L(M,W)(a,b)] or its consequence for test (b) occurs on the supplied 118 pages. They do not formulate rectification of diagrams over a specified class of shapes.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.5 — Six-object suspension-poset restriction counterexample

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For a six-object suspension poset X and a weak equivalence Y to the finite parallel-arrow category B, restriction H_ss(B) to H_ss(Y) is not surjective.

**Supplied locator:** VII-c ms.134 companion; IX-080. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 71.

**Comparison note:** The six-object suspension poset, finite parallel-arrow category, and non-surjective restriction map have no form on the supplied 118 pages. Scan023 mentions fundamental groupoids in a pushout question, without this suspension-poset construction.

**Nearest related only — 118 scan023, fragment line 23:**

```tex
équiv. sur les groupoïdes fondamentaux
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.6 — Loop identities imply the corresponding representability

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Each higher loop identity (c) implies its associated representability (a); pointed infinity-category pullbacks/pushouts give the coherent identities; finite-poset (b) does not force both adjoint operations.

**Supplied locator:** IX-081, IX-088; IX ms.22-25. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 72.

**Comparison note:** No form of the higher loop identities, either representability direction, or the finite-poset limitation appears on the supplied 118 pages. Their cone and cofiber questions do not formulate coherent pointed infinity-category pullback or pushout identities.

**Nearest related only — 118 scan012, fragment line 19:**

```tex
and homotopism
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.7 — Known finite and all-shape rectification frameworks

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Cisinski finite derivable categories rectify finite inverse/direct shapes; full ABC categories and suitably complete Quillen model categories rectify all shapes in their universe.

**Supplied locator:** Lead 3; Part D(2). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 73.

**Comparison note:** No Cisinski finite derivable, ABC, or Quillen model-category rectification theorem occurs on the supplied 118 pages. The factorization and interval conditions in scans025–026 are used for a left-fraction calculus, a different conclusion from rectification at inverse/direct or arbitrary shapes.

**Nearest related only — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**Nearest related only — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.
- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.

### PATHS D.8 — Finite intrinsic cofibration axioms imply rectification

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** Initial object, pushouts, two out of three, and enough intrinsic cofibrations imply CF1-CF4 and rectification at finite direct categories; no finite-poset counterexample under those hypotheses.

**Supplied locator:** XII ms.228-234,272; POLES A.8-A.9/G.26 addendum (i)-(iv). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 74.

**Comparison note:** Own comparison: scan025 explicitly combines factorization through a distinguished arrow class, a pushout stability condition, interval endpoint inclusions, and finite colimits to obtain left fractions. This resembles the finite cofibration input of the later result, but 118 neither defines intrinsic cofibrations by their universal preservation property nor states CF1–CF4 or finite-direct rectification.

**Confidence in this own comparison:** medium — Several structural hypotheses overlap explicitly, but the arrow class, exact axioms, and conclusion differ.

**Manuscript evidence — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**Manuscript evidence — 118 scan025, fragment line 31:**

```tex
avec $i\in\unsure{\mathcal M|\mathcal A}$, $h$ homotopisme
```

**Manuscript evidence — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.
- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.

### PATHS D.9 — Enough intrinsic cofibrations does not imply all cofibrancy

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The diamond lattice has enough intrinsic cofibrations but noncofibrant objects; finite sets with isomorphisms show CF5 and CF6 do not follow from the finite axioms.

**Supplied locator:** POLES addendum (i). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 75.

**Comparison note:** No form of the diamond-lattice or finite-set examples, or the independence of CF5 and CF6, appears on the supplied 118 pages. The generic pushout warning on scan023 is not one of these examples and uses the manuscript’s separate categorical setting.

**Nearest related only — 118 scan023, fragment line 5:**

```tex
\uline{Mais attention} Il n'est pas vrai \uline{dans $\mathrm{Cat}$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.

### PATHS D.10 — Cubical rectification does not imply finite-poset rectification

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Rectification at all cubes does not imply finite-poset rectification: the six-element circle face poset with every arrow weak misses degree two at its own shape.

**Supplied locator:** Part D(3) cubical test. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 76.

**Comparison note:** The six-element circle face poset, all-arrow marking, and missed degree-two map have no form on the supplied 118 pages. No implication from cubical tests to finite-poset rectification is formulated there.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.11 — Finite simplicial sets fail rectification at BZ

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Finite simplicial sets rectify finite posets but fail at BZ because strict finite automorphisms have finite order and a Nielsen monodromy has infinite order. The opposite is BK-fibrant with the same failure.

**Supplied locator:** Part D(3) finite posets versus BZ and BK question. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 77.

**Comparison note:** No form of the finite-simplicial-set, infinite-order Nielsen monodromy, or opposite BK-fibrant example appears on the supplied 118 pages. The Kan-type condition proposed on scan031 concerns simultaneous homotopies and does not give this rectification counterexample.

**Nearest related only — 118 scan031, fragment line 27:**

```tex
\uline{Il faut une condition du type ``\unsure{Kan}'' sur $Y$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.12 — Nine-vertex fence rectifies without BK fibrancy

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The nine-vertex contractible fence with all arrows weak rectifies all shapes but fails BK fibrancy through an explicit unfillable inner horn in Ex squared of its nerve.

**Supplied locator:** Part D(3) converse BK question. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 78.

**Comparison note:** The nine-vertex fence, the specified inner horn of Ex squared, and their claimed rectification consequence have no form on the supplied 118 pages. No BK fibrancy test occurs there.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.13 — Ordinary relative-poset localization need not rectify

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** A relative poset localization of an ordinary category need not rectify: finite circle P presents BZ; explicit countable signed-face orbit poset Q presents BC2 and fails rectification at the finite category BC2.

**Supplied locator:** STRATA B.8 addendum; Part D(3). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 79.

**Comparison note:** Neither the finite circle presentation of BZ nor the countable signed-face orbit presentation of BC2 occurs on the supplied 118 pages. Scan024’s ordinary localization and left-fraction statements do not assert that all diagram categories rectify.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.14 — Kaledin shape classes and extension scope

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Audit of Kaledin v3 shapes, definitions, representation and extension scope: Pos is finite chain dimension, Pos+ left-bounded, Pos+- left-finite; finite posets alone are not his base.

**Supplied locator:** Recent results Kaledin; GALOIS F.5 addendum. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 80.

**Comparison note:** No Kaledin Pos, Pos+, or Pos+- shape class, finite-chain-dimension condition, or extension-scope audit occurs on the supplied 118 pages. Their finite-family homotopy argument does not formulate any such recognition theorem.

**Nearest related only — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.15 — Naive Kaledin enhancement and coherent comparisons

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The naive family on Kaledin Pos (respectively Pos+) is enhanced iff its canonical comparisons to coherent L(M,W) diagram categories are equivalences; the representing infinity-category is L(M,W), by Kaledin plus localization universality.

**Supplied locator:** Recent results Kaledin (i),(iv); Part D(3). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 81.

**Comparison note:** No form of the Kaledin enhancement criterion or the representing infinity-category assertion occurs on the supplied 118 pages. They discuss ordinary localizations, without the family of coherent diagram-category comparisons used by this row.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.16 — Unbounded finite zigzags obstruct infinite additivity

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** The circle relative poset fails additivity at the countably infinite discrete poset because finite zigzags yield bounded winding sequences; the finite IX category with W identities fails no enhancement axiom.

**Supplied locator:** Recent results Kaledin (ii),(iii). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 82.

**Comparison note:** Own comparison: scans028–031 isolate the failure of a uniform finite homotopy length in an infinite family, explicitly requiring at least n elementary homotopies for its nth pair on scan029. This is the same bounded-length obstruction that motivates the dossier’s winding-sequence argument, but the circle relative poset, Kaledin additivity axiom, and identity-marked IX example are absent from 118.

**Confidence in this own comparison:** high — The manuscript explicitly names the unbounded lengths and their infinite-coproduct consequence; only that mechanism is compared.

**Manuscript evidence — 118 scan028, fragment line 16:**

```tex
car $J$ est fini
```

**Manuscript evidence — 118 scan029, fragment line 7:**

```tex
une suite d'au moins $n$ homotopies él. pour les joindre
```

**Manuscript evidence — 118 scan031, fragment line 27:**

```tex
\uline{Il faut une condition du type ``\unsure{Kan}'' sur $Y$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIII-a.tex` — ms.55–56, dgrb709, Localization axioms, stability, and locally constant coefficients (file lines 2241–2253). AI commentary distinguishes finite padding from lack of uniform bounds; textual comparison only.

### PATHS D.17 — Later Cof axioms and filtered-colimit upgrades

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** Later Grothendieck Cof0-Cof3 and quillenisable classes imply finite-direct rectification; full Cof4 implies ABC and all-relative-universe rectification and homotopy left Kan extensions. Filtered-colimit stability of W upgrades intrinsic cofibrations.

**Supplied locator:** XIII ms.7-12,50-59; XVII ms.39-40; XIX ms.33-38,48; Part D(4). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 83.

**Comparison note:** Own comparison: scans025–026 give finite factorization/pushout/interval conditions for left fractions, while scans039–041 use special open or closed filtrations and L3 in the saturation argument. These supply related ingredients, but the named Cof0–Cof4 axioms, quillenisable classes, ABC recognition, all-shape rectification, and homotopy Kan extensions are not stated in 118.

**Confidence in this own comparison:** medium — The common finite and limiting ingredients are explicit; the later abstract packages and stronger conclusions are absent.

**Manuscript evidence — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**Manuscript evidence — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**Manuscript evidence — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**Manuscript evidence — 118 scan040, fragment line 24:**

```tex
donc on gagne par L3.
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364); **RESIDUE F.7** (Open (the return's claim); line 351).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.
- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.
- `context/companion/chunks/DER_XIII-a.tex` — ms.55–56, dgrb709, Localization axioms, stability, and locally constant coefficients (file lines 2241–2253). AI commentary distinguishes finite padding from lack of uniform bounds; textual comparison only.

### PATHS D.18 — Accessible Cat localizers and Thomason rectification

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Accessible fundamental localizers on Cat admit left proper Thomason models and rectify all relative-small shapes; enough intrinsic fibrations is a stricter properness condition. Pointed tests are applied to pointed objects.

**Supplied locator:** POLES G.24/E.2 addendum; Part D(2),(3). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 84.

**Comparison note:** No accessibility hypothesis, Thomason model structure, or all-shape rectification theorem occurs on the supplied 118 pages. Their localizer axioms and saturation theorem do not establish model-category existence or the stronger intrinsic-fibration condition.

**Nearest related only — 118 scan015, fragment line 8:**

```tex
si deux parmi $g,f,gf$ dans $\underline W$, le 3e l'est
```

**Nearest related only — 118 scan040, fragment line 31:**

```tex
\uuline{Thm} L'ens. $\underline W$ est saturé
```

**RESULTS_STATE links:** **GALOIS B.13** (Open (the return's claim); line 345); **PATHS D.22** (Open (the return's claim); line 364).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS D.19 — Locally constant Set restriction fails two out of three

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The fully faithful locally constant restriction class for Set fails two out of three on e to BC2 to e, so descent cannot substitute for the finite cofib axioms.

**Supplied locator:** GALOIS A.5 addendum; Part D(1). Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 85.

**Comparison note:** No form of the e→BC2→e counterexample or the fully faithful locally constant Set-restriction class appears on the supplied 118 pages. Scan015 states a two-out-of-three requirement for the chosen localizer, without deriving a descent class or testing this example.

**Nearest related only — 118 scan015, fragment line 8:**

```tex
si deux parmi $g,f,gf$ dans $\underline W$, le 3e l'est
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.20 — Modern references and coherent versus ordinary arrows

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Resolved Arlin and Fuentes-Keuthan-Kedziorek-Rovelli references, with strict versus pseudonatural scope. Coherent arrow homotopy categories differ from arrows in Ho: Z maps versus one.

**Supplied locator:** Recent results references; STRATA C.7 addendum. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 86.

**Comparison note:** The Arlin and Fuentes–Keuthan–Kedziorek–Rovelli reference audit and the Z-versus-one arrow comparison have no form on the supplied 118 pages. Their ordinary homotopy localization does not identify a coherent arrow homotopy category with, or distinguish it from, arrows in Ho.

**Nearest related only — 118 scan024, fragment line 12:**

```tex
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.21 — Kaledin Pos comparisons detect coherent localization

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** If R_(A times J) is an equivalence for every Kaledin Pos shape J, the specified infinity-localization comparison L(M^A) to Fun(NA,L(M)) is an equivalence.

**Supplied locator:** GALOIS mapping-space upgrade suggestion. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 87.

**Comparison note:** No form of the all-J condition on R_(A times J), or the resulting infinity-localization equivalence with Fun(NA,L(M)), occurs on the supplied 118 pages. No canonical coherent diagram comparison is formulated there.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.22 — Remaining intrinsic recognition and IX comparison questions

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Exact unresolved targets: finite-only and cardinal-only intrinsic recognition, finite-product-test upgrade, BK finite-shape sufficiency, intrinsic cofib without initial object, full IX test equivalence/c=>b without path comparison, and nonaccessible Cat localizer derivators.

**Supplied locator:** IX-080; Part D(3); recent/additional unresolved questions. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 88.

**Comparison note:** No form of this list of unresolved finite/cardinal, BK, IX, or nonaccessible-derivator targets occurs on the supplied 118 pages. The finite conditions on scan025 and special limit theorem on scans039–040 give neighboring material but do not settle these tests or remove the initial-object hypothesis.

**Nearest related only — 118 scan025, fragment line 64:**

```tex
moyennant les conditions (i) à (iv)
```

**Nearest related only — 118 scan039, fragment line 10:**

```tex
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.
```

**RESULTS_STATE links:** **PATHS D.22** (Open (the return's claim); line 364); **GALOIS B.13** (Open (the return's claim); line 345).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps6.tex` — §125, Digression on Baues’ cofibration and fibration categories; pp.530–532 (file lines 4465–4565). Supplied Pursuing Stacks text, read as historical context.
- `context/companion/chunks/DER_VII-b.tex` — ms.108–109, dgrb370, The sequential total category is a homotopy colimit; dgrb371, The total category and the telescope (file lines 1805–1837). AI companion proof read as context, not independently validated.

### PATHS D.23 — Nonzero-spectrum homology localizers lack intrinsic fibrations

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For every nonzero spectrum E, its homology localizer lacks enough intrinsic fibrations: free-group nullity plus an identity-homology nonsurjective endomorphism separates W_E from its aspherical generation.

**Supplied locator:** POLES C.4-C.5 addendum; Part D(2) cofibration-fibration asymmetry. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 89.

**Comparison note:** No spectrum-homology localizer, free-group nullity argument, or nonsurjective identity-homology endomorphism appears on the supplied 118 pages. The fibration/cofibration classification there uses categorical lifting notions and does not prove the claimed failure of enough intrinsic fibrations.

**Nearest related only — 118 scan009, fragment line 29:**

```tex
F\Longrightarrow\mathrm{Sm}\\C\Longrightarrow\mathrm{Pr}
```

**RESULTS_STATE links:** **RESIDUE D.9** (Open (the return's claim); line 365).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS D.K1 — Acyclic CW maps are epimorphisms in Hot

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** An acyclic map of small CW spaces is an epimorphism in the unpointed homotopy category, with weakly equivalent double-pushout codiagonal.

**Supplied locator:** GALOIS B.9 verification; CATHOT E.17 reduction. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 90.

**Comparison note:** No form of the small-CW acyclic-map epimorphism theorem or double-pushout codiagonal assertion occurs on the supplied 118 pages. Their categorical pushout comparison and warning do not impose CW hypotheses or analyze this codiagonal.

**Nearest related only — 118 scan022, fragment line 10:**

```tex
diagramme cocartésien dans un $\widehat A$, avec $Y\hookrightarrow X$ mono
```

**Nearest related only — 118 scan023, fragment line 5:**

```tex
\uline{Mais attention} Il n'est pas vrai \uline{dans $\mathrm{Cat}$}
```

**RESULTS_STATE links:** **CATHOT E.17** (Open (the return's claim); line 343).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.K2 — Embedding groups in large simple acyclic groups

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Every small group embeds in a simple nonabelian integrally acyclic group of any prescribed infinite small cardinality at least its size.

**Supplied locator:** GALOIS B.10 verification; KT_mu. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 91.

**Comparison note:** No embedding into a simple nonabelian integrally acyclic group, or prescribed-cardinality construction, occurs on the supplied 118 pages. The groupoid example in scans033–036 concerns a different product/asphericity question.

**Nearest related only — 118 scan036, fragment line 7:**

```tex
alors dans $\widehat A$ $\underline W_A$ est formé des seuls iso
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.K3 — KT_mu acyclic BG presentations

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** KT_mu holds: every connected small CW complex has an acyclic BG presentation whose perfect kernel is killed by every homomorphism to any group of size at most mu.

**Supplied locator:** GALOIS B.11 verification; KT_mu; CATHOT E.17. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 92.

**Comparison note:** No form of KT_mu, acyclic BG presentations of CW complexes, or the specified perfect-kernel annihilation condition appears on the supplied 118 pages. The dossier’s claimed reduction for CATHOT E.17 is therefore carried only as contextual background.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** **CATHOT E.17** (Open (the return's claim); line 343).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.K4 — Homotopy-invariant ind-presheaves factor through groupoids

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** If a presheaf ind-represented by a nonempty small filtered system of categories modulo natural transformations inverts W_infinity on all small shapes, it inverts W_1 and the specified groupoid-completion unit is an ind-isomorphism with the same indexing category.

**Supplied locator:** GALOIS B.12 verification; CATHOT E.17. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 93.

**Comparison note:** No ind-represented presheaf theorem or same-index groupoid-completion ind-isomorphism occurs on the supplied 118 pages. The sequential construction on scan041 serves saturation and does not formulate an all-small-shape invariance assumption.

**Nearest related only — 118 scan041, fragment line 17:**

```tex
système inductif d'imm. ouvertes
```

**RESULTS_STATE links:** **CATHOT E.17** (Open (the return's claim); line 343).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS D.K5 — All-small-shape invariance forces a one-type

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** All-small-shape homotopy invariance of the constant-to-constant localization Hom functor for a small relative category forces factorization through Pi_1; if represented by a space, that space is a 1-type.

**Supplied locator:** V ms.44-46; Lead 3 size correction; CATHOT E.17. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 94.

**Comparison note:** No form of the constant-to-constant localization Hom theorem or its representing-space one-type conclusion occurs on the supplied 118 pages. The fundamental-groupoid question on scan023 concerns a pushout property rather than all-shape invariance.

**Nearest related only — 118 scan023, fragment line 23:**

```tex
équiv. sur les groupoïdes fondamentaux
```

**RESULTS_STATE links:** **CATHOT E.17** (Open (the return's claim); line 343).

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS E.1 — All-arrow endpoint fibres realize path spaces

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The checked CATHOT all-arrows theorem identifies exact endpoint fibres with path spaces, even translation with identity in Hot, and the one-sided constant-tail maps as weak equivalences.

**Supplied locator:** CATHOT E.20-E.25; VIIc-C004; VIIc-C005. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 95.

**Comparison note:** No all-type path category, even-translation comparison, or constant-tail map appears on the supplied 118 pages. The Fib(f) constructions of scans011–014 are ordinary comma constructions and are explicitly marked as not yet Serre.

**Nearest related only — 118 scan012, fragment line 13:**

```tex
\uline{but not yet Serre}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.

### PATHS E.2 — Strictly monoidal categorical loop model

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The all-type categorical loop model is strictly monoidal, natural in pointed functors, and realizes the loop space with its A-infinity multiplication.

**Supplied locator:** Part E; IX-037. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 96.

**Comparison note:** No all-type categorical loop model or claim about its A-infinity multiplication occurs on the supplied 118 pages. Their discussion of intervals and ordinary homotopy does not specify a strictly monoidal loop construction.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

### PATHS E.3 — All-type endpoints need not have strict lifting properties

**Supplied status:** claim (return: Refuted). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** The all-type endpoint functor is smooth but can fail properness and both strict Grothendieck lifting properties, already for X=[1].

**Supplied locator:** VII ms.161-166; Part E; STRATA path test. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 97.

**Comparison note:** Own comparison: scan014 explicitly records that smooth Serre maps need not be fibrations and proper Serre maps need not be cofibrations, distinguishing homotopical properties from strict Grothendieck lifting. It contains neither the all-type endpoint functor nor the X=[1] witness, and does not assert the row’s failure of properness.

**Confidence in this own comparison:** medium — The lifting distinction is explicit, but the endpoint construction and the smooth-versus-proper counterexample are absent.

**Manuscript evidence — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS E.4 — Eventual endpoints smooth and proper without strict bifibration

**Supplied status:** claim (return: Refuted). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** The eventual alternating endpoint functor is smooth and proper but need not be a Grothendieck fibration or opfibration.

**Supplied locator:** Part E; filtered-union lifting distinction. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 98.

**Comparison note:** Own comparison: scan014’s explicit nonimplications already require separating proper/smooth Serre conditions from categorical cofibration/fibration. The eventual alternating path category and its filtered-union endpoint construction are absent, so 118 gives the general distinction rather than this witness.

**Confidence in this own comparison:** high — The relevant nonimplications are written explicitly; no claim of an identical path model is made.

**Manuscript evidence — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS E.5 — Smooth proper categorical mapping-path factorization

**Supplied status:** claim (return: Proved). **Relation:** analogue. **Kind:** own idea.

**Dossier statement:** Every functor has a natural categorical mapping-path factorization into a nerve weak equivalence followed by a smooth proper functor whose strict fibres are homotopy fibres.

**Supplied locator:** Part E; XII ms.188-207. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 99.

**Comparison note:** Own comparison: scans011–014 factor a functor through Fib(f), with a retraction described as a homotopism and a fibration explicitly marked as not yet Serre. This is a categorical replacement construction, but it does not provide the dossier’s simultaneous smooth/proper conclusion or the strict-fibre homotopy-fibre comparison.

**Confidence in this own comparison:** high — The factorization diagram, homotopism, and stated limitation are visible in the frozen text; the later strengthened conclusion is not imported.

**Manuscript evidence — 118 scan012, fragment line 19:**

```tex
and homotopism
```

**Manuscript evidence — 118 scan012, fragment line 13:**

```tex
\uline{but not yet Serre}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.
- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS E.6 — Rectangular-band path endpoints fail strict lifting

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For the five-element rectangular-band monoid of type S2, the eventual path endpoint map is neither a strict fibration nor opfibration; the all-type map is not an opfibration.

**Supplied locator:** STRATA E.11 test case. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 100.

**Comparison note:** The five-element rectangular-band monoid, its S2 homotopy type, and the claimed endpoint counterexamples have no form on the supplied 118 pages. Scan014 supplies only the general distinction between Serre/proper/smooth and strict lifting classes.

**Nearest related only — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.

### PATHS E.7 — Interval pushout-products fail intrinsic cofibration

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** For every n>=1 the specified interval pushout-product is a weak equivalence but not an intrinsic W_infinity-cofibration.

**Supplied locator:** POLES H.6; TOTASPH F.23; Part E. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 101.

**Comparison note:** No form of the specified interval pushout-product counterexample for every n appears on the supplied 118 pages. Scan026 requires a separating interval for its fraction argument, and scan023 warns about a categorical pushout statement, but neither defines or disproves this intrinsic W_infinity-cofibration property.

**Nearest related only — 118 scan026, fragment line 6:**

```tex
un intervalle
$I$ \uline{séparant}
```

**Nearest related only — 118 scan023, fragment line 5:**

```tex
\uline{Mais attention} Il n'est pas vrai \uline{dans $\mathrm{Cat}$}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIc-a.tex` — ms.228–229, dgrb607, An interval with room at both ends; refers to Definition2(c), ms.109–110 (file lines 1975–2045). Intrinsic W-cofibration and cylinder discussion read; proof claims not rechecked.

### PATHS E.8 — Finite interval cotensors can have incorrect endpoint fibres

**Supplied status:** claim (return: Proved). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Finite interval cotensors have a constant-section categorical homotopy equivalence but their exact endpoint fibres need not be the correct path spaces.

**Supplied locator:** Part E; dual interval assertion. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 102.

**Comparison note:** No finite-interval cotensor Fun(I,X), constant-section theorem, or incorrect path-space endpoint-fibre example occurs on the supplied 118 pages. The homotopism of scan012 belongs to the Fib(f) comma replacement and does not assert this cotensor comparison.

**Nearest related only — 118 scan012, fragment line 19:**

```tex
and homotopism
```

**Nearest related only — 118 scan012, fragment line 13:**

```tex
\uline{but not yet Serre}
```

**RESULTS_STATE links:** no additional applicable entry selected.

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_VII-c.tex` — ms.150–152, dgrb404, Why both parities give the endpoint fibration (file lines 1264–1280). AI companion argument on filtered unions and endpoint maps; not independently validated.

### PATHS E.9 — Smooth/proper for one localizer does not control larger ones

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** W_infinity smoothness/properness does not imply universal preservation under strict pullback for a larger localizer.

**Supplied locator:** GALOIS/STRATA localizer qualification; Part E. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 103.

**Comparison note:** No form of the comparison between W_infinity and a larger localizer, or its universal strict-pullback counterexample, occurs on the supplied 118 pages. Scan009 discusses a proper/smooth base-change criterion without making the claimed cross-localizer implication.

**Nearest related only — 118 scan009, fragment line 15:**

```tex
R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}
```

**Nearest related only — 118 scan009, fragment line 15:**

```tex
\text{\unsure{Le changt} de base par }f\\\text{commute à }R^i g_*
```

**RESULTS_STATE links:** **GALOIS B.14** (Open (the return's claim); line 359); **BISITE A.19** (Proved (the return's claim); line 381).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_I-a.tex` — ms.49–50 dgrb25; ms.58–59 dgrb30, The converse, and why spaces suffice (file lines 1931–1952,2263–2294). Supplied text and AI commentary; later space-detection proof carried as a claim.

### PATHS E.10 — Marked components do not determine an exit-path localization

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Components of the marked subcategory alone do not specify a stratification whose exit paths compute general localization mapping spaces.

**Supplied locator:** STRATA proposed general stratified reading. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 104.

**Comparison note:** No form of the proposed stratification by marked-subcategory components, or its failure to compute localization mapping spaces by exit paths, occurs on the supplied 118 pages. The open–closed bifunctor H_X on scan017 glues ordinary categories; it does not encode a marking or an exit-path comparison.

**Nearest related only — 118 scan017, fragment line 5:**

```tex
U\subset X\supset Y\qquad H_X:U^\circ\times Y\mathbin{\text{---}}\mathrm{Ens}
```

**RESULTS_STATE links:** **STRATA B.2** (Proved (the return's claim); line 401).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.1.1, ms.59–61, Proposition1; dgrb507, An open–closed cut remembers a profunctor (file lines 9–123). Supplied text and AI commentary; textual matching only.

### PATHS E.11 — Strict bifibration realizing the rectangular-band path system

**Supplied status:** claim (return: Open). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Existence of another strict bifibration realizing the path local system over the rectangular-band monoid remains unresolved here.

**Supplied locator:** STRATA E.11; VIc-C022. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 105.

**Comparison note:** No form of the rectangular-band existence problem, or a construction or exclusion of another strict bifibration, appears on the supplied 118 pages. Scan014 clarifies why strict lifting must be distinguished from smooth/proper behavior, but supplies no solution of the open BISITE B.21 / RESIDUE A.8 problem.

**Nearest related only — 118 scan014, fragment line 13:**

```tex
\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}
```

**RESULTS_STATE links:** **BISITE B.21** (Open (the return's claim); line 354); **RESIDUE A.8** (Open (the return's claim); line 350).

**Relevant companion / Pursuing Stacks locators:**

- `context/ps_chapters_VI_VII/ps7.tex` — §136, pp.569–570; §137 opening at p.570 (file lines 725–790). Supplied text distinguishes categorical cofibrations from Kan–Quillen cofibrations.

### PATHS E.12 — Fixed-origin paths contractible but not filtered or total

**Supplied status:** claim (return: Known). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** The checked fixed-origin all-type path category may be contractible without being filtered or totally aspherical; its endpoint functor is final over simply connected bases.

**Supplied locator:** TOTASPH G.1-G.6; XIIba-C005. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 106.

**Comparison note:** No fixed-origin all-type path category or simply-connected-base finality assertion occurs on the supplied 118 pages. Their product/diagonal total-asphericity discussion on scans033–036 also uses a different notion from the later totality invoked in this row.

**Nearest related only — 118 scan035, fragment line 26:**

```tex
(i)\quad A\text{ tot. }\underline W\text{-asph.}
```

**RESULTS_STATE links:** **TOTASPH A.7** (Known (the return's claim); line 405); **TOTASPH C.10** (Refuted (the return's claim); line 408).

**Relevant companion / Pursuing Stacks locators:**

- `context/companion/chunks/DER_XIIb-a.tex` — Chapter XII §V.2.3, Definition1, ms.88–89; preceding dgrb522 at ms.87 (file lines 1134–1148,1193–1197). Definition and editorial warning read; no equivalence of historical notions assumed.

### PATHS E.13 — Finite test-object restricted Yoneda is not faithful

**Supplied status:** claim (return: Refuted). **Relation:** absent. **Kind:** reading question.

**Dossier statement:** Finite set-valued restricted Yoneda on finite-category test objects is not faithful: the finitary symmetric-group shift and the identity induce the same tests but are distinct in Hot.

**Supplied locator:** VIIc-C004 faithfulness question; CATHOT F.2 verification. Dossier file `context/DOSSIER_STATEMENTS_WITH_STATUS.md`, line 107.

**Comparison note:** The finitary symmetric-group shift, its agreement with identity on finite set-valued tests, and its distinctness in Hot have no form on the supplied 118 pages. No finite-category restricted-Yoneda faithfulness question is formulated there.

**Manuscript evidence:** no form found and no substantive near-match supplied.

**RESULTS_STATE links:** no additional applicable entry selected.

**Additional context:** none pursued; this row is absent and no further unrelated research was needed.

## Check events and frozen source

The separate `strata_paths_events.tsv` records 122 actual textual matching/background events: 86 assigned dossier rows, 22 additional RESULTS_STATE references, and 14 companion/Pursuing Stacks context items. Every type is **carried as background without fault found**, with an explicit outcome saying that no mathematical proof was validated. No entry is labeled proof-checked, re-proved, or refuted by this task.

The source hash is unchanged:

```text
63b5213a6f4b8790fefa6a9d7d8ce3fdc50723ef67fad682348b36a48845b149
```

The duplicate consecutive cotefile markers in the frozen combined file remain preserved; the primary agent records this mechanical assembly defect.
