# Independent source integrity audit

Audit date: 13 November 2026. Scope: the attached French, English and typesetting source bundles; all 116 package pairs and all 245 translation units. No source file was modified.

## Finding

**No source package, unit or scan is omitted, duplicated or reordered.** All 1,022 files match the byte lengths and SHA-256 digests in the three attached archive manifests. Every French unit is the exact recorded character slice, and every English package is reproduced byte for byte by the documented unit assembly algorithm. All 1,588 scans occur once, in manuscript order, in both languages.

**The English mathematical content is not literally byte-identical to the French source.** The supplied checks explicitly mask translated prose, exclude the written-out m-bar shorthand and accept recorded exceptions. The nine residual changed/missing-formula cases are accounted for below. Independent comparison found no additional unexplained mathematical difference; this is a structural integrity finding, not a new scholarly certification of every translated assertion.

Two metadata qualifications matter: 44 French packages use CRLF while their exported units use LF, and the source record for the formula in `LM_P018_s171-180` incorrectly says scan 172; its actual location is scan 179. Neither qualification changes or drops manuscript content.

## Evidence and reproducibility

Primary supplied records: `LM_FR_MANIFEST.tsv`, `LM_EN_MANIFEST.tsv`, `LM_TYPESET_MANIFEST.tsv`; `en/MANIFEST.json`; `fr/records/CURRENT_TEXT_INDEX.tsv`; `en/checks/CHECKS.json`, `FIXES.jsonl` and `WAIVERS.jsonl`; and the visible algorithms in `en/scripts/prepare.py`, `assemble.py` and `check_units.py`. Original manuscript package text is in `fr/texts/` and `en/packages/`; translation inputs and outputs are in `en/french_units/` and `en/units/`.

Run `python work/scripts/source_integrity.py`, then `python work/scripts/write_source_integrity_report.py`. The first script reads source files and writes `work/data/source_integrity.json`; the second creates this report and two tabular inventories. Neither invokes the network or imports the original machine-specific configuration. All emitted paths are relative source references.

The original `check_units.py` cannot be executed unchanged from this attachment: its `scripts/der/check_units.py`, comparison `cmp/` library and external glossary `common.py` are absent. Its `common_lm.py` also points to the originating machine. The visible assembly, annotation-count, m-bar and raised-ending algorithms were reproduced directly; the new formula segmenter and text-box comparison are independent. Historical results are identified separately throughout this report.

## 1. Raw bytes, slice identity and complete assembly

| Check | Result |
|---|---|
| Attached raw manifest rows | 1,022 verified; zero byte/hash discrepancies |
| French source packages | 116 / 116 match their `en/MANIFEST.json` raw hashes |
| French unit slices | 245 / 245 match recorded offsets, normalized UTF-8 hashes and character lengths |
| English package assembly | 116 / 116 match both normalized text and raw bytes |
| French raw unit concatenation | 72 / 116 raw-byte-identical; 44 differ only by CRLF versus LF |
| French normalized concatenation | 116 / 116 exact after the original text reader’s newline normalization |
| Manifest unit inventory | 245 present; no extra unit files, missing units or repeated unit uses |
| Package order | Exactly the order of the supplied current-text index |
| Unit order | Exactly each package’s recorded order and the manifest’s global unit order |
| Historical CHECKS inventory | Exactly the same 245 unit IDs; all recorded PASS |

The current-text index raw SHA-256 is `096d378a0408908ce5262ab5acb2c451ebb11756e1c2b9979a4846b11a517e9e`, exactly the digest recorded by the translation manifest. Raw source hashes remain authoritative: line-ending normalization is used only to reproduce the explicitly text-based slice and assembly algorithms.

For each French unit, the audit verifies `package[start:end] == unit`, contiguous cut offsets, first offset zero, final offset equal to package length, the recorded unit digest, and every scan and manuscript-page anchor. English assembly uses the original algorithm exactly: `lead + english_unit.strip("\n") + trail`, followed by concatenation in the package’s recorded unit order. This is stronger than checking only that all unit filenames exist.

The full assembly order, scan ranges, offsets and both unit hashes are in `SOURCE_UNIT_ASSEMBLY.tsv`; the JSON contains all individual checks and every manifest hash.

### Scan coverage

| Cote | Scans | Continuity | Missing / repeated |
|---|---:|---|---:|
| 140-1 | 37 | 1–37, in order | 0 / 0 |
| 140-2 | 575 | 1–575, in order | 0 / 0 |
| 140-3 | 696 | 1–696, in order | 0 / 0 |
| 140-4 | 280 | 1–280, in order | 0 / 0 |

All 245 units have matching French/English scan and manuscript-page anchor sequences, matching comment sequences, matching tag arguments, identical illegible-word-count arguments, and matching environment-name counts. Balanced braces, matched environment counts and closed outer math segments were independently checked in both languages. The simple per-scan blank-line split yields 8,842 nonempty blocks on each side, with no scan-level block-count mismatch; this differs from the historical checker’s 7,623 prose paragraphs because its missing comparison library applies a different prose filter.

## 2. Annotation preservation by scan

The seven primary apparatus macros were counted directly on every scan, with comments excluded and no macro expansion. Every primary macro count agrees between French and English. The bars inside balanced `\unsure{...}` arguments differ only in the three already recorded cases where the translation keeps two possible completions of a damaged French negation.

| Primary macro | French | English |
|---|---:|---:|
| `\deleted` | 6,936 | 6,936 |
| `\inserted` | 4,332 | 4,332 |
| `\unsure` | 17,117 | 17,117 |
| `\illegible` | 1,261 | 1,261 |
| `\margin` | 1,780 | 1,780 |
| `\uline` | 2,369 | 2,369 |
| `\uuline` | 87 | 87 |

| Cote / scan | Source count → English count | Approved reason |
|---|---|---|
| 140-3 / 148 | unsure bars 3 → 4 | `does not occur` / `only occurs`: damaged second half of the negation |
| 140-2 / 396 | unsure bars 7 → 8 | `cannot` / `can only`: damaged second half of the negation |
| 140-3 / 210 | unsure bars 4 → 5 | `does not cover` / `covers only`: damaged second half of the negation |

The total is 6,850 French uncertainty bars and 6,853 English bars. These are explicit source-record waivers, not additions made during this edition. Both alternatives and all illegible spans are retained. The audit does not select a reading.

Among the secondary presentation macros, only five `\textsuperscript` occurrences disappear: two at 140-3:629, two at 140-4:267 and one at 140-4:268. They are raised endings of French abbreviations that are written out in English; the supplied checks list exactly these review points. Counts of `\diagram`, `\figure`, `\texttt`, `\textit`, `\textbf`, `\textcircled` and `\fbox` agree on every scan.

`SOURCE_SCAN_MARKS.tsv` contains all 1,588 paired per-scan counts, source lines and differences. Counts establish preservation of marker incidence; they do not by themselves prove semantic equality of everything inside a marker. The formula and glossary audits provide the additional checks described here and in `GLOSSARY_INCONSISTENCIES.md`.

## 3. Formula comparison: what “identical” means

### Supplied historical results

| Historical field | Count | Interpretation |
|---|---:|---|
| French formulas | 32,175 | After the standalone m-bar exclusion |
| English formulas | 32,163 | Same historical comparison |
| Identical | 32,141 | After the checker’s prose-box masking; not literal source bytes |
| Text-only differences | 16 | Additional wording/marked-word cases retained for review |
| Changed | 6 | The six explicitly waived display/formula cases below |
| Missing | 3 | Three formulas changed into prose or an ordinary equals sign |
| Raised abbreviation endings | 9 | Written out with their French abbreviations |
| Added / moved / spacing-only | 0 / 0 / 0 | Historical fields |

The 476 standalone m-bar forms excluded from comparison are the author’s shorthand for “même”, rendered according to the supplied notation policy. No matching shorthand formula remains in English. These exclusions are not evidence that 476 mathematical variables were dropped. Conversely, saying “every formula is byte-identical” would conceal the documented translation convention and the nine cases below.

### Independent comparison

The new parser finds 32,168 French and 32,156 English outer mathematical/drawing segments after the same 476 exclusions. It pairs 32,143 by exact structure after masking translated text boxes and pure-word apparatus arguments. Of these, 30,933 are literally identical after comments are blanked; the other 1,210 matching pairs have wording or whitespace differences, retained in the JSON.

The parser deliberately treats an entire TikZ picture as one outer segment and preserves nested mathematics in its prose labels. Its total is seven lower than the historical checker’s on each side. That difference in segmentation is reported, not rounded away or presented as a rerun of the missing library.

There are 23 nonmatching groups, all classified: the nine recorded exceptions; nine raised abbreviation endings grouped at seven sites; and seven additional groups whose differences are confined to TikZ node or parbox prose. For those seven groups, the geometry and code outside prose regions match, embedded mathematics matches, and primary apparatus counts inside changed regions match. They occur at 140-1:19 and 32; 140-2:237 and 419; 140-3:600; and 140-4:34 and 35. All changed prose regions and their checks are retained in the JSON.

For each of the six historical changed-formula cases, applying only the recorded exact French→English fragment transformation reproduces the English structural target; the remaining equation and diagram tokens then match after prose masking. For each missing-formula case, the supposedly missing segment is exactly the segment deliberately converted by the recorded wording convention. No additional algebraic correction is introduced or authorized by this audit.

## 4. The nine residual historical formula differences

All nine retain the supplied English wording. The audit supplies the actual cote, scan and source line, and distinguishes mathematical TeX encoding from mathematical content. Each has a corresponding `WAIVERS.jsonl` entry by Claude (Opus 5.5), dated 12 November 2026. The complete original waiver records are preserved in the machine results.

### HISTORICAL-FORMULA-01: 140-2, scan 116

**Classification:** translated connective inside a marked mathematical fragment.

French: `fr/texts/LM_P012.tex`, line 162; English: `en/packages/LM_P012_en.tex`, line 161.

French source fragment:

```tex
$\nu\unsure{\le|=}0\deleted{\unsure{ou 1}}$
```

Supplied English fragment:

```tex
$\nu\unsure{\le|=}0\deleted{\unsure{\text{or }1}}$
```

The connective ou becomes or in a text box. The variable, inequality/equality alternatives, zero and one remain; the deletion and nested uncertainty remain. TeX tokens change; no algebraic symbol or relation is corrected.

**Disposition:** Retain the supplied source; do not silently rewrite the formula or doubt.

### HISTORICAL-FORMULA-02: 140-2, scan 179

**Classification:** translated connective inside a mathematical formula.

French: `fr/texts/LM_P018.tex`, line 314; English: `en/packages/LM_P018_en.tex`, line 314.

French source fragment:

```tex
$U\simeq\unsure{\mathbb C^*} \unsure{ou} S^1\times S^1$
```

Supplied English fragment:

```tex
$U\simeq\unsure{\mathbb C^*} \unsure{\text{or}} S^1\times S^1$
```

The uncertain connective ou becomes an uncertain text-box or. All variables, superscripts, products and the displayed alternatives remain. Both the historical fix and waiver incorrectly say scan 172; the literal occurrence is at scan 179.

**Disposition:** Retain the supplied source; do not silently rewrite the formula or doubt.

### HISTORICAL-FORMULA-03: 140-2, scan 420

**Classification:** prose shorthand expanded; equality sign changed from math mode to text mode.

French: `fr/texts/LM_P042.tex`, line 325; English: `en/packages/LM_P042_en.tex`, line 324.

French source fragment:

```tex
\unsure{$\overline{\mathrm m}$|$=$}
```

Supplied English fragment:

```tex
\unsure{even|=}
```

The two uncertainty alternatives remain. The m-bar shorthand is rendered even; the equality alternative retains the literal equals sign but loses its dollar delimiters. The historical checker calls $=$ missing because it counts math segments, not visible signs. No equals sign is dropped.

**Disposition:** Retain the supplied source; do not silently rewrite the formula or doubt.

### HISTORICAL-FORMULA-04: 140-2, scan 440

**Classification:** two written forms of prose shorthand expanded.

French: `fr/texts/LM_P044.tex`, line 174; English: `en/packages/LM_P044_en.tex`, line 174.

French source fragment:

```tex
\unsure{$\mathrm m^{\mathrm s}$|$\overline{\mathrm m}^{\mathrm s}$}
```

Supplied English fragment:

```tex
\unsure{same|same}
```

Both source readings are the recorded abbreviation for mêmes. The English deliberately has two same alternatives under the uncertainty mark; it retains their count but not the French graphical distinction between barred and unbarred m. The French source preserves that distinction. This is a documented lexical convention, not deletion of a mathematical parameter.

**Disposition:** Retain the supplied source; do not silently rewrite the formula or doubt.

### HISTORICAL-FORMULA-05: 140-2, scan 557

**Classification:** prose shorthand expanded inside a TikZ diagram label.

French: `fr/texts/LM_P056.tex`, line 255; English: `en/packages/LM_P056_en.tex`, line 255.

French source fragment:

```tex
\overline{\mathrm m}\ \text{grain de sel}
```

Supplied English fragment:

```tex
\text{same grain of salt}
```

The mathematical-looking m-bar is the word même in the diagram annotation. Its command is absorbed into the English text box. Diagram objects, arrows, indices and n-conditions remain.

**Disposition:** Retain the supplied source; do not silently rewrite the formula or doubt.

### HISTORICAL-FORMULA-06: 140-3, scan 332

**Classification:** translated text boxes reordered around the same underlined adjective.

French: `fr/texts/LM_C3-321-339.tex`, line 447; English: `en/packages/LM_C3-321-339_en.tex`, line 447.

French source fragment:

```tex
\text{unipotent }\uline{\text{régulier}}
```

Supplied English fragment:

```tex
\uline{\text{regular}}\text{ unipotent}
```

Display (41) has this adjective/noun order change twice. Underlining remains on régulier/regular. The algebraic expressions for the two epsilon elements are unchanged; the change is the order and wording of adjacent prose boxes.

**Disposition:** Retain the supplied source; do not silently rewrite the formula or doubt.

### HISTORICAL-FORMULA-07: 140-3, scan 457

**Classification:** prose shorthand expanded inside a display and uncertainty alternative.

French: `fr/texts/LM_C3-454-472.tex`, line 225; English: `en/packages/LM_C3-454-472_en.tex`, line 225.

French source fragment:

```tex
\unsure{\text{de}=|\text{de }\overline{\mathrm m}}
```

Supplied English fragment:

```tex
\unsure{\text{of}=|\text{likewise}}
```

The first reading retains its equals sign; de même in the second becomes likewise. The uncertainty alternatives, equations and all algebraic notation around them remain.

**Disposition:** Retain the supplied source; do not silently rewrite the formula or doubt.

### HISTORICAL-FORMULA-08: 140-3, scan 497

**Classification:** prose shorthand expanded beside an equation.

French: `fr/texts/LM_C3-492-510.tex`, line 388; English: `en/packages/LM_C3-492-510_en.tex`, line 388.

French source fragment:

```tex
\text{et de }\overline{\mathrm m}
```

Supplied English fragment:

```tex
\text{and likewise}
```

The note et de même becomes and likewise. The phi, delta, alpha, beta expressions and both defining equalities are unchanged.

**Disposition:** Retain the supplied source; do not silently rewrite the formula or doubt.

### HISTORICAL-FORMULA-09: 140-3, scan 655

**Classification:** uppercase prose shorthand expanded outside an equation.

French: `fr/texts/LM_C3-644-662.tex`, line 689; English: `en/packages/LM_C3-644-662_en.tex`, line 689.

French source fragment:

```tex
$\overline{\mathrm M}$ conclusion
```

Supplied English fragment:

```tex
Same conclusion
```

The capital M-bar is the recorded même shorthand at the beginning of a sentence. It becomes the capitalized English word Same. It is not a parameter removed from the preceding formula.

**Disposition:** Retain the supplied source; do not silently rewrite the formula or doubt.

## 5. Approved fixes and waivers

The attachment contains 41 historical fixes, all literal replacements with required count one. Every final English unit contains its recorded replacement; none still contains its recorded old literal. All these changes are therefore present in the English package reconstruction. The raw model outputs preceding those fixes are not supplied, so this audit cannot replay and independently certify the original execution-time occurrence count. The result is an applied-text witness check, not an invented reconstruction of unavailable raw outputs.

All 34 historical waivers are included verbatim in the JSON, associated with their unit and relevant scan. They cover formula wording and shorthand, expanded abbreviation endings, the three negation alternatives, and glossary matching failures caused by preserved markup or context. A PASS in the historical CHECKS file means these recorded waivers have been applied; it does not erase the underlying review entries.

One location error is independently demonstrated: historical fix 30 and its formula waiver describe scan 172, but their exact old/new formula occurs at scan 179 in `LM_P018`. Both original records are preserved; this report and its machine contextual audit use the verified scan 179. No source wording is altered to repair metadata.

The present edition has one separately proposed, unmarked glossary correction: `EN-GLOSS-140-2-296-001`, `structure with loops` → `loop structure` at `LM_P030`, 140-2:296, English package line 96. It is recorded in `glossary_edits.json` and is not applied to the attached source files. Mathematical notation and all apparatus are untouched. Layout and mechanical changes made in generated edition bodies are governed by the separate build/change records; this audit is of their original source baseline.

## 6. Public source-of-record provenance and its limits

The attached `en/README.md`, in its “Input (source of record)” section, reports a comparison with the public repository at abbreviated commit `671d2cf`: 22 texts identical in `raw/second_pass/`, 18 equal apart from line endings, 50 identical elsewhere in the tree, and 26 not found as identical blobs. These are historical statements in the supplied README, not conclusions newly verified here.

The attached `source_of_record.py` performs `git fetch` and reads a checkout on the originating machine. Its generated `SOURCE_OF_RECORD.json` is not included in any attached bundle, and the referenced checkout is not available. Consequently the independently established provenance is the complete raw-file manifest and exact current-text-index/translation-manifest chain. This report does not substitute an unverified contemporary repository snapshot for the user-supplied source of record.

## 7. Deliverables and limitations

- `source_integrity.json`: every raw hash, package reconstruction, unit order and cut, per-scan annotation count, independent formula pair/difference, historical waiver and contextual exception.
- `SOURCE_UNIT_ASSEMBLY.tsv`: 245 rows in assembly order with offsets and hashes.
- `SOURCE_SCAN_MARKS.tsv`: 1,588 per-scan rows with paired counts and differences.
- `source_integrity_differences.json`: the 23 independently reviewed nonmatching groups, as a compact companion to the full data.

This audit does not claim that a source count proves a printed PDF is complete. Actual PDF links, shipped uncertainty spans, all-page ink bounds, log diagnostics and visual review are checked separately by `verify_pdf.py` and the edition’s verification records. It also does not claim a new reading of the manuscript scans or an independent proof of Grothendieck’s mathematical arguments. Uncertain readings and the source’s mathematical assertions remain preserved.
