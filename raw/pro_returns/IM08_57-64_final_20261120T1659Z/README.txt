IM08_57–64: diplomatic transcription corrections

Authoritative deliverables
  placements.tsv: one record for each supplied correction-table row, in its
    original order. Use a TSV parser that honors quoted multiline fields.
    For decision (a), find is a unique exact span of the original supplied
    page; replace gives that entire span after its local correction.
  edited_pages/: every supplied page after the recorded decisions.
  notes.md: retained authorial slips, mathematical/editorial refinements,
    absent placements, and remaining uncertainty relevant to the rows.
  crops/: visually inspected enlarged facsimile details, named by page/row.
  CHECK_EVENTS.tsv: actual visual checks and any separately identified
    conditional mathematical checks. Reading a source row is not a proof.
  progress.log: UTC start time and page-completion records.

Decisions
  a = transcription reading corrected to the visible ink; compound rows may
      also have a preserved mathematical component explained in notes.md.
  b = written text retained; proposed mathematical or editorial refinement
      recorded in notes.md.
  c = already as the supplied row asks.
  d = the specified wording/placement was not found on this page.
  A retained in-place doubt mark is a final editorial decision, not a guessed
  resolution. Confidence may concern the specific corrected part of a
  compound row; the ink description and notes identify remaining doubt.

Documentation and verification
  accepted_reviews/ contains the main reader's accepted record for each page.
  reviews/ contains working reader returns and main-reader resolutions.
  scripts/ contains crop, validation, commit, and packaging helpers.
  page_order.tsv records the supplied processing order, not a proposed
    reconstruction of manuscript reading order.
  audit_report.txt reports coverage and exact reconstruction from placements.
  MANIFEST.tsv lists archived paths, byte sizes, and SHA-256 checksums.

Three readers were assigned one page at a time in the supplied queue order.
The main reader reviewed returned decisions, inspected relevant crops,
resolved open actions, and wrote the final pages and ordered placements.
No OCR, PDF text layer, or text-recognition library was used. Original line
breaks, notation, diplomatic macros, and authorial slips were preserved except
for the explicitly recorded local reading corrections.

Identifiers are keyed by id + cote + scan. L832 occurs in three distinct
source rows and is intentionally retained three times.

The attached input files and earlier ZIP archives are excluded. If resuming
from a checkpoint, restore its contents and the original attached inputs,
placing the input files/folders beneath source/. Run scripts/prepare_packets.py
to recreate missing isolated page packets. Do not reset progress.log or
overwrite an earlier checkpoint. Completion is established by edited_pages,
placements.tsv, accepted_reviews, and the page-completion log together.

The validation scripts use the original supplied source files. They verify
unique nonoverlapping find spans, exact reconstruction of each output page,
line-break counts, control-word spelling against the supplied LaTeX inventory,
row ordering, crop references, notes, and completion coverage. They do not
claim a new proof of all mathematical statements or a full document build.
