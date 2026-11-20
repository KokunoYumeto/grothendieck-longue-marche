# Records and packaging audit

## Scope

This is a documentation and packaging QA audit by `/root/final_records_audit`, with a subsidiary script/metadata review. The audit opened no images, OCR, or original witness files and performed no additional transcription or mathematical computation. It mechanically compared the consolidated source's uncertainty tokens with doubt records, inspected final decision metadata and generated tables, and checked file identities and hashes. It provides no additional ink reading beyond the three readers and main adjudicator documented by the project.

## Final record reconciliation

The seven required page files and every required top-level deliverable are present. The combined fragment equals the page files concatenated in order 026, 027, 028, 030, 031, 032, 033. Both `run_state.json` and the completed-page entries in `progress.log` have that order. All 21 reader directories contain `page.tex`, `review.json`, `report.md`, and `crops.tsv`.

| Scan | Changes against C | Changes against H | High | Medium | Low | Inventory | Doubts | Check events |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 026 | 21 | 33 | 20 | 11 | 10 | 35 | 13 | 5 |
| 027 | 22 | 40 | 32 | 4 | 9 | 22 | 9 | 3 |
| 028 | 10 | 25 | 11 | 8 | 9 | 25 | 12 | 1 |
| 030 | 6 | 0 | 2 | 2 | 2 | 24 | 5 | 1 |
| 031 | 5 | 10 | 7 | 4 | 0 | 17 | 1 | 2 |
| 032 | 6 | 17 | 3 | 11 | 3 | 19 | 7 | 3 |
| 033 | 13 | 20 | 13 | 7 | 0 | 21 | 10 | 1 |
| **Total** | **83** | **145** | **88** | **47** | **33** | **163** | **57** | **16** |

Confidence counts cover 168 distinct changed loci; 185 loci in total include retained readings. A locus can differ from both witnesses. The generated changes tables agree with the decision flags and confidence fields.

The 145 H collation rows match the adjudication fields in order and content, with the requested eleven columns, their-page = our-scan minus one, and no scan-030 rows. Exact duplicate rows were absent. The generation rule includes precisely `diff_H` loci; the scan-032 retained hand-state record explicitly documents a macro-only exclusion. The audit checked this recorded classification and its propagation; it did not reopen H to independently recollate it.

The 163 inventory rows match the decisions, use the declared columns and permitted category values, and all have `transcribed = yes`. The doubts file begins with the current notation table. Its 57 doubt rows match the per-page records. The 40 `unsure` tokens and one `illegible` token have corresponding doubt records; additional entries record uncertain inscription methods or the status of drawn traces. The notes, notation table, and doubt records preserve those qualifications.

## Check-event scope

`CHECK_EVENTS.tsv` has the required five columns and equals the recorded event lists: nine background events, three computation events, three targeted proof checks, and one refutation referring to N026.3. The event descriptions agree with the scope stated in the notes and named supporting records. Computation entries expressly identify Python enumeration and distinguish it from a proof-assistant certificate. The notes retain the documented limits concerning the orthogonal-group links, geometric dictionaries, and minimal-order claim. This audit did not rerun or independently prove the mathematics.

## Crop references and workflow

Every cited crop resolves to its specifically named reader or main-reader manifest, including references whose basenames recur in other reader directories. Each manifest records the source filename, numeric bounds, output width, rotation, processing, and creation time. The coordinate and transformation fields are populated and valid as records. No image was reopened to check bounds against pixel dimensions or reproduce the crop.

| Scan | A | B | C | New main-reader crops | Total |
|---|---:|---:|---:|---:|---:|
| 026 | 13 | 14 | 14 | 6 | 47 |
| 027 | 17 | 15 | 13 | 6 | 51 |
| 028 | 13 | 14 | 12 | 9 | 48 |
| 030 | 6 | 6 | 6 | 1 | 19 |
| 031 | 5 | 6 | 4 | 4 | 19 |
| 032 | 10 | 4 | 7 | 0 | 21 |
| 033 | 10 | 10 | 8 | 4 | 32 |
| **Total** | **74** | **69** | **64** | **30** | **237** |

The workflow's crop counts agree with the manifests and `workflow_counts.json`. The complete first and last briefs are embedded in the workflow, and all seven brief versions are present. `scripts/crop.py` implements the documented source-coordinate transformation sequence. `SOURCE_INPUTS.tsv` identifies both supplied attachments by size and SHA-256.

## Corrections completed

The audit found internal alternative separators that broke nine notation-table rows into extra Markdown cells. They have been escaped in the notation source and regenerated doubts file; the final notation, doubts, and changes tables have consistent column counts. The main reader also corrected the 026-04 evidence/reason to agree with its colon-first reading and clarified that confidence counts cover the union of changed loci. No remaining first-alternative or doubt-status contradiction was found in the reviewed decision metadata.

The audit also found an inspection-history ambiguity at S027-05: its earlier evidence said the reading was settled from the half “without a crop,” while its decision and crop reference recorded a main-reader crop inspection. The main reader corrected the evidence and builder source to identify reader B's half-page settlement followed by the main reader's inspection of the cited crop. The generated records were refreshed and record validation passed at 10:22:16 UTC. The corrected evidence is present in the changes log and H collation. No unresolved records inconsistency remains from this audit.

## Freeze and packaging flow

The freeze and unchanged-hash verification are recorded at **2026-11-20 10:21:04 UTC**. This audit independently checked that `frozen_hashes.json` contains exactly the seven required page keys and the combined-transcription key, that all eight current SHA-256 values match, and that the same values appear in `progress.log`. The static validation and record validation both report passed. The documented validation scope is static source checking; no rendered-layout validation is claimed.

`scripts/package.py` excludes ZIPs, PNG/JPEG images, PDFs, `__pycache__`, and the supplied `PREAMBLE.tex`. The README directs the recipient to the supplied preamble and gives crop-reproduction instructions. The package manifest hashes each included file except itself; the archive-prepared progress entry is written before those hashes are computed. The final ZIP itself will be created after this report, so this audit does not claim to have inspected that later archive.

Two script limitations were covered by explicit final checks: final packaging does not itself enforce completion/freeze/verification, and the verification branch does not independently enforce the eight-key set. The completed-page reconciliation, exact-key check, and current-byte hash check above supply those checks for this run. The current eight values are the frozen result inspected here; the subsequent wording correction affected documentation only.
