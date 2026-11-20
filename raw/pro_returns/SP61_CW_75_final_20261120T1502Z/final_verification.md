# Final mechanical verification

Completed 2026-11-20 15:01:50 UTC after the ten second image readings and the cross-page comparison.

## Result

The existing validator passed in strict macro mode with **0 errors and 0 warnings**. No TeX compiler, renderer, OCR system or image-reading helper was used. These checks establish file and record consistency; they do not establish the correctness of a handwriting reading or mathematical claim.

- Ten expected page fragments, scans 16–25, with one matching scan marker each.
- One ordered combined fragment with a single leading cote marker and the same page contents.
- Balanced braces, math delimiters and environments; no disallowed fragment commands.
- Required reports present; required CSV/TSV headers, values and column counts valid.
- 233 unique, contiguous decision IDs; every row differs from at least one witness according to the canonical flags.
- 225 H collation rows exactly match the corresponding canonical readings, evidence, categories and confidence values.
- 213 unique inventory elements, all transcribed; ten explicitly include the pencilled archive numerals with uncertain hand attribution.
- 78 grouped doubt rows; 83 distinct registered crops; 23 mathematical check events.
- First readings and second image readings each have one completion entry per page in order; all first readings precede the first second reading.
- The eleven frozen SHA-256 values were verified unchanged after the mechanical checks.
- No images, input archives, witness files, compiled artifacts or caches are present in the deliverable directory.

## Final counts

| Measure | Count |
| --- | ---: |
| Difference loci | 233 |
| Against C | 34 |
| Against H | 225 |
| High confidence | 149 |
| Medium confidence | 44 |
| Low confidence | 40 |

Against-C and against-H counts overlap. Confidence includes tentative differences, so these are not counts of proven errors.

## Earlier preflight

`mechanical_preflight.md` is retained as the dated interim snapshot. Its old counts and pending items describe that earlier state. This final verification supersedes those status items; the sheet feedback, completed audits and frozen hashes now exist, and generated Python caches have been removed. The final packaging script verifies the same frozen hashes again and checks ZIP contents after writing.
