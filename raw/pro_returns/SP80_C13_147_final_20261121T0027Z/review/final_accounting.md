# Final blind-reading accounting

Reconciled on 2026-11-21 00:24:27 UTC. Root reproduced the counts from canonical records; the independent accounting reader checked the corresponding TSVs, choices, plans, manifests, hashes and progress log without reopening images.

| Scan | Fixed boxes | Token-different comparisons | Changed boxes |
| --- | --- | --- | --- |
| 108 | 32 | 24 | 5 |
| 109 | 20 | 17 | 3 |
| 110 | 19 | 13 | 3 |
| 111 | 13 | 12 | 4 |
| 112 | 18 | 13 | 1 |
| 113 | 23 | 14 | 1 |
| 114 | 19 | 16 | 3 |
| 115 | 22 | 21 | 3 |
| 116 | 16 | 14 | 3 |
| 117 | 19 | 17 | 7 |
| 119 | 22 | 18 | 5 |
| 120 | 22 | 19 | 4 |
| 121 | 18 | 15 | 2 |
| 122 | 23 | 23 | 3 |
| 123 | 17 | 10 | 3 |
| 124 | 17 | 12 | 2 |
| 125 | 10 | 8 | 1 |
| 126 | 14 | 11 | 4 |
| 127 | 27 | 20 | 3 |
| 128 | 23 | 13 | 5 |
| 129 | 9 | 9 | 5 |
| 130 | 26 | 23 | 7 |
| 131 | 12 | 10 | 3 |
| **Total** | **441** | **352** | **80** |

## Reconciled records

There are353 individual root adjudications: all352 differing boxes and128 B15, whose two earlier readings agreed. Their partition is273 retained-first and80 changed. Seventy-nine changed boxes came from differing comparisons; one came from a shared earlier reading. The89 token-equal comparisons include88 raw-string-identical pairs and110 B13, which differs only in whitespace. The unchanged88 token-equal boxes need no disagreement adjudication.

The per-page counts agree across comparison/adjudication TSVs, canonical audit_counts/audit_changes, root choices/plans, and the audit lines in progress.log. Every differing box has an individual evidence statement and a final reading. All80 changed=yes records differ from their frozen first string; all273 changed=no adjudications retain it. Boxes may overlap and their token differences include wrappers and scope, so these are not independent error counts or estimated error rates.

All23 blind assignments use contexts different from the first readers and respect the exposure exclusions documented in review/difference_table_incident.md. The46 frozen baseline hash entries and69 comparison-time entries match the69 unique box/first/second TSV files. Each comparison stores the same reading strings as its frozen inputs. First-review timestamps precede the common baseline freeze, and comparison timestamps precede their respective completed audits.

## Crop inventory and documented exception

Each of the441 fixed boxes has exactly one fresh source-crop ledger entry, matching its frozen coordinates, and the referenced file exists. There are442 second-stage source-crop records because root additionally made crops/147_scan110_second_B03_context.jpg at (770,342,1678,545) for context during adjudication. The fixed B03 crop at (775,346,1480,540) is unchanged. This extra context crop is explicitly recorded in that page’s note, event, choices and adjudication; it did not change the selected first reading.

The two115 view_rot_minus45 images are rotated derivatives of existing B07/B19 crops, documented in the blind reader notes and root adjudications. They are viewing aids, not additional source recrops. Two other historical filenames containing second belong to first-stage crops, as their ledgers record. The package retains374 first-stage source crops,442 second-stage source crops, and2 rotated viewing derivatives:818 JPEGs.

## Equal-reading correction

For128 B15 both frozen readers wrote the component tuple with ldots. Root inspected the saved crop and retained one continuous dash, one certain comma after d_1 and an additional doubtful comma:

```tex
La composante $D_{d_*}=D_{d_0,d_1,\unsure{,}\mathord{-},d_r}$ est
```

Both earlier TSVs remain unchanged. The extra adjudication is counted in80 changed boxes and353 total root decisions, while the original comparison remains equal.

## Scope of verification

This accounting verifies the recorded coverage and consistency, not the correctness of an image reading by itself. The main reader’s per-box visual evidence is preserved separately. Final transcription freeze and unchanged-byte checks are recorded in review/frozen_hashes.json and progress.log; static final validation is retained in review/final_validation.json. No OCR, outside research or TeX compilation was used.

## Witness and doubt accounting

The final log contains563 substantive locations:234 against C and507 against H, with178 counted against both. Those are recorded differences, not estimates of witness error rates. The eleven rows excluded at the final accounting stage remain as complete snapshots in their canonical reports; ten were certainty-only or duplicated a contextual correction, and one concerned a brace scope correctly stated by H in a note. All80 blind-audit changes remain recorded. See `review/witness_count_reconciliation.json`.

All129 supplied marks have decisions: alternative: 13, first: 47, other: 6, undecided: 63. The doubts file contains252 local remaining entries, including newly identified uncertainties beyond the supplied marks. All483 inventory elements are recorded as transcribed.
