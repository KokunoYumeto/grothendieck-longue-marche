# Final pagination verification

This workflow closes the equation-number detachments recorded by actual native
page-pair inspections. It does not treat a source edit, successful compilation,
empty scanner result, or rendered image as a completed visual inspection.

## Frozen historical evidence

`work/data/pagination_review_before_repairs.json` contains 106 primary-book
candidate inspections: 80 confirmed detachments and 26 displays cleared on
their original pages. The original master candidates are duplicates whose
final coverage is established through the separate all-page pixel comparison.

`work/data/layout_pagination_reconciliation.json` identifies all 80 confirmed book
instances with 56 exact source binding IDs, including the reverse trailing tags
at cote 140-3, scans 503 and 506. It distinguishes the second equation (62) at
scan 545 from the first occurrence. The source preflight checks this canonical
mapping against the immutable source, exact binding inventory, and generated
applied-repair records.

The local source repair inventory also includes preventive bindings at the
same literal source patterns. Their existence does not change the count of
80 historically observed detachments.

`work/data/pagination_known_extensions.json` preserves later actual findings
additively. Its revision578 inventory contains three primary witnesses: French
and English apparatus tag(76) at cote140-2 scan573, and French reading inserted
uncertain tag(15) at cote140-3 scan695. Two historical master witnesses at
scan573 are supported by exact PNG identity to actually inspected apparatus
pages. Other unviewed counterparts are not labelled defective. The original
106-inspection baseline remains byte-unchanged.

`work/scripts/pagination_extensions.py` verifies the exact original extension
rows against the immutable revision578 snapshot, every original source fragment
and UTF8 location, the attributed actual observations, and the historical image
identity evidence. Future additions may increase the total while preserving
every earlier row. The final primary closure total is currently83; the two
additive master witnesses are accounted for separately through current full
apparatus/master pixel comparisons.

## Execution

Run these commands from the project root. Do not prepare evidence while any
publication PDF is being rebuilt.

```sh
python work/scripts/verify_pagination_final.py source-preflight
python work/scripts/verify_pagination_final.py prepare
```

The first command does not inspect final PDFs. Its report is explicitly marked
`SOURCE_PREFLIGHT_ONLY_NO_FINAL_PDF_INSPECTION`.

The preparation command freezes all seven PDF hashes, scans every page, reads
archive scan annotations directly from the current PDFs, and renders evidence
for the original80 plus all additive primary instances and every final
primary-book candidate. It
checks all seven hashes again before saving the review queue. Proof directories
include a revision identifier derived from all seven PDF hashes, so earlier
evidence is preserved when the books change.

The complete queue is `work/data/pagination_verification_queue.json`. Its
initial status is `PENDING_VISUAL_REVIEW`. Separate reviewer queues are written
under `work/data/pagination_final_queues/`, one for each of the five primary
books. Every queue contains the corresponding PDF hash and source-qualified
known instances. The machine scanner output is
`work/data/equation_tag_pagination_final_candidates.json`.

Each known instance supplies the original image and observation, the exact
source binding ID and source span, possible final tag positions, and full
native page images. The tag search includes source-linked pages and their
immediate neighbors because an unmarked diagram can move beyond the page
containing its scan link. Candidate positions are localization aids; the
reviewer must identify the correct associated display from the source and
actual image. A prose reference with the same number cannot close the issue.

## Actual observations

Each reviewer writes a JSON list of observations. A typical entry has this
structure; the example values below describe the schema, not an inspection:

```json
{
  "id": "Exact item ID from the prepared queue",
  "status": "RESOLVED_ON_FINAL_PDF",
  "pdf_sha256": "Exact current PDF hash from that queue",
  "reviewer": "Actual reviewer",
  "observation": "What was actually seen, identifying the tag and complete display.",
  "tag_page": 1,
  "display_pages": [1],
  "images": [
    {"path": "Relative path of an actually viewed prepared image", "sha256": "Its exact SHA256"}
  ]
}
```

Use `RESOLVED_ON_FINAL_PDF` only for a known detachment whose tag and complete
associated display are now on the same physical page. Use
`CLEARED_ON_FINAL_PDF` for an actually inspected final scanner candidate that
does not represent a detached tag. A remaining defect uses
`DETACHMENT_REMAINS` and prevents a pass. The supplied observations must name
the actual tag page and every page containing its display. Automatic text
positions or source bindings cannot supply an observation.

Review every final primary candidate, including candidates that resemble a
previously cleared item. The finalizer requires the observed tag and complete
display to occupy the same physical page and requires that page to appear in
the evidence images actually viewed.

One narrowly source-verified classification permits an empty visible-display
list: `RETAINED_TAG_AFTER_FULLY_CANCELLED_DISPLAY`. This applies only to a
corrected primary form when an exact immutable display contains one complete
`deleted{...}` group followed solely by the uncancelled matching `tag{...}`.
The reviewer supplies `display_pages: []` and a `source_assessment` containing
the exact source path/hash, cote, scan, source line, full display fragment,
fragment SHA256 and explanation. The finalizer checks all those facts and
the balanced group boundary. It still requires actual current tag-page image
inspection. This preserves the source case at cote140-3 scan559 without
claiming that a cancelled formula remains visibly present.

After the apparatus books have current attributed review ledgers, compare every
page of each apparatus book with its master using `compare_pdf_pixels.py`.
Only exact freshly rendered page identity can transfer an existing review.
The separate master title pages require their own actual inspection. Final
master candidate pairs are cleared by their corresponding actually reviewed
primary pairs only when both pages have exact current pixel identity.

## Finalization and release gate

```sh
python work/scripts/verify_pagination_final.py finalize \
  --observations work/data/actual_reviewer_observations.json
```

Repeat `--observations` for each reviewer file. Duplicate observation IDs are
rejected. Finalization validates current PDF hashes, complete baseline and
scanner inventories, source reconciliation and applied-repair hashes,
immutable source hashes, original and final image hashes, actual observation
fields, and both complete apparatus/master comparisons.

The machine report is `work/data/pagination_verification_final.json`, schema
`pagination-verification-v1`. Its top-level status is `PASS` only when there
are no unresolved checks. An incomplete, stale, or defective result is `FAIL`.
The important fields are:

| Field | Required successful value or coverage |
|---|---|
| `files` | Exactly seven current PDF hashes, page counts, and stable before/after hashes |
| `baseline` | Exact historical report hash; 106 candidates, 80 true detachments, 26 cleared |
| `known_detachments` | All80 original IDs plus every additive primary ID (currently83 total), each `RESOLVED_ON_FINAL_PDF` with actual final observation and image hashes |
| `known_extensions` | Hash-bound additive inventory, retaining all initially frozen revision578 rows |
| `known_master_transfers` | Every additive historical master witness (currently2), `RESOLVED_BY_MASTER_PIXEL_IDENTITY` with its actual primary closure and current comparison hash |
| `final_candidates` | Every final primary candidate `CLEARED_ON_FINAL_PDF`; every master candidate `CLEARED_BY_MASTER_PIXEL_IDENTITY` |
| `master_comparisons` | Current hashes, complete page sequence, matching counts, and exact pixels beyond the separately reviewed title |
| `counts.resolved_known_detachments` | Equals the complete original-plus-additive primary inventory, currently83 |
| `counts.original_known_detachments` | 80 |
| `counts.resolved_extension_master_transfers` | Equals `counts.extension_master_transfers`, currently2 |
| `counts.cleared_primary_candidates` | Equals `counts.final_primary_candidates` |
| `counts.cleared_master_candidates` | Equals `counts.final_master_candidates` |
| `unresolved` | Empty list |
| `observations_generated_by_script` | `false` |

The separate `work/data/heading_closure_final.json` report covers the long marginal
note openings and the cote 140-3, scan 548 V/Preliminary opening. The pagination
report references its hash, status, and current PDF hash; the release gate
checks heading closure separately. Those heading witnesses are not counted
among the original or additive equation-tag instances.

The scanner is a candidate detector, not a mathematical proof of ideal
pagination. Its all-page search is combined with source-qualified closure of
the known defects, actual inspection of every resulting primary candidate,
the required selected-page visual reviews, and exact master comparisons.
