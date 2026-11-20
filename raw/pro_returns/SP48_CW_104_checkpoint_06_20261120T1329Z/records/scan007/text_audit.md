# Text-only implementation audit — scan 007

**Result: PASS.** No source-choice or transcription-implementation discrepancy found.

## Scope

Compared page_draft.tex with main_observations.md decisions 1–26, all three complete reader readings and reports, witness C/H page texts, the reader crosswalk and the current decision_draft.json. No images or PDFs were opened; no OCR, web research, mathematical check, compilation or rendering was performed. No authoritative source file was changed.

## Coverage

| Check | Result |
|---|---|
| Numbered main decisions | 26/26 implemented |
| Decision/crosswalk issue rows | 42/42 present and linked |
| Source reader issues | 115/115 covered: A 39, B 38, C 38 |
| Inventory elements | 28/28 represented in page text |
| Original reader inventory rows | A 28/28, B 27/27, C 26/26; preserved in the union |
| Remaining uncertainties | 10/10 present with exact candidate order |
| C inline doubts | 20/20 mapped to adjudicated decisions |
| Deletions / insertions | Exact ordered sequences: 7 / 5 |
| Structural checks | Balanced groups/environments/math delimiters; no handwriting wrapper or new macro |

## Specific implementation checks

The mapping attaches M below the separately named terminal-m node, indents lower u to the right of the Hom origin, uses a separate barred lower shaft that starts earlier and extends farther, and retains the far-left star between the two row levels. The upper target has no comma. This is a source-code geometry check; no rendered dimensions were assessed.

The retained uncertain readings, in page order, are `modèles|modéles`, `flèche|fléche`, `autom|autom.`, `par`, `(i]|[i]|(i)`, `de`, `\forall|\mathrm H`, `e|s`, `à|:`, and `plui|plus`. The latter deleted group includes the comma and old une, followed by live inserted une. Both isom endpoints lack an abbreviation stop; the classification M and inserted sentence retain separate periods.

The separate oblique is a literal downward-rightward TikZ segment below-right of the à/colon cluster. No therefore candidate or linguistic role is introduced. The full canceled Soit K line, deleted I, deleted D followed by live M, prefix M- insertion, local underline, separate family display and folio/archive numbers are present.

## Inventory evidence

| Element | Present |
|---|---|
| E01: Manuscript folio | Yes |
| E02: Opening sentence | Yes |
| E03: Assumption (i) | Yes |
| E04: Replacement of autom | Yes |
| E05: Assumption (ii) | Yes |
| E06: Short canceled term in (ii) | Yes |
| E07: Example | Yes |
| E08: Subobject-set definition | Yes |
| E09: Introduction of the map | Yes |
| E10: Starred map | Yes |
| E11: Injectivity and image description | Yes |
| E12: Canceled fragment after l’ens | Yes |
| E13: M- prefix insertion | Yes |
| E14: Canceled first class-set start | Yes |
| E15: Préordonné insertion | Yes |
| E16: Class-set definition | Yes |
| E17: Canceled I after N | Yes |
| E18: Orderedness sentence | Yes |
| E19: Choice and family paragraph | Yes |
| E20: Canceled letter after un | Yes |
| E21: Overwritten D | Yes |
| E22: Live M replacing D | Yes |
| E23: Detached oblique mark | Yes |
| E24: Canceled words before famille | Yes |
| E25: Live une above old une | Yes |
| E26: Indexed family | Yes |
| E27: Final sentence continuation | Yes |
| E28: Archive sheet number | Yes |

## Provisional record fields

At this audit snapshot, the decision record still contains staging completion fields, inventory transcribed=pending, pending page guards, CTX12=pending and a residual-question string about pending checks. All corresponding page content is present. Root has confirmed that the builder is finalizing this bookkeeping after the audit. These fields are recorded in the JSON snapshot and are not source-choice discrepancies; this audit does not edit or promote them.

The JSON companion contains checks for each numbered decision, all 42 issue rows, all 28 inventory elements, all 115 reader issue mappings, and SHA-256 hashes of every input read.
