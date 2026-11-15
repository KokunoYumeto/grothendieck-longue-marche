MPL_14_087-132 — completed transcription and research notes

Required deliverables
  MPL_14_087-132_transcription.tex  Combined diplomatic LaTeX fragment.
  pages/                          The 41 individual page fragments.
  MPL_14_087-132_doubts.md          Notation register, doubts, abbreviations,
                                  and limitations of legibility/reconstruction.
  MPL_14_087-132_inventory.csv      769 inventoried elements, all transcribed.
  MPL_14_087-132_notes.md           92 research notes, requested comparison table,
                                  standing registers, and primary bibliography.
  progress.log                    Page completion/audit times, freeze hashes,
                                  context-opening time, and final verification.

The transcription was frozen before the supplied context was opened. All 42
protected hashes remain unchanged. The notes discuss mathematical corrections,
contextual alternatives, counterexamples and later results without altering the
transcription. Unreviewed claims in the supplied earlier work remain labelled.

The LaTeX is intentionally a fragment without a preamble, as requested. It uses
the task's editorial macros and TikZ/tikz-cd. The compilation record checks syntax
with a diagnostic macro wrapper; it is not a publication-layout guarantee, and
no diagnostic rendering is presented as the diplomatic edition. All doubtful
readings are explicit in the page fragments and indexed in the doubts file.

Supporting records
  records/frozen_hashes.json and records/final_hash_verification.json
  records/notation_comparison.json
  records/scanNNN.json (initial observations and root's second audit)
  records/validation_final.json
  records/note_context_searches.json
  records/research_notes_audit.json
  records/research_notes_human_review.json
  records/tex_qa_final/report.json and records/qa_macros.tex
  records/delivery_verification.json

The lexical audit reports all searches, including negative matches; a lexical
match alone is not proof of a conceptual parallel. Its eight sentence-count
warnings were manually checked: quoted abbreviations and numbered references
caused overcounts. The full notes each contain one to four actual sentences.

Mechanical checks can be rerun with:
  python scripts/validate_package.py --require-frozen
  python scripts/audit_research_notes.py --help
For the second check, extract the supplied context separately and pass its
location using the documented option. No supplied scans or context source files
are duplicated in this delivery. The hourly checkpoints preserve the complete
work history, including intermediate research and diagnostic files; this final
archive contains the completed deliverables and current compact records.

MANIFEST.sha256 lists every other archive member's SHA-256 hash.
