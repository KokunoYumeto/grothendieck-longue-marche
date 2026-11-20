IM04_13-16 — diplomatic transcription correction deliverable

Coverage
  All 81 supplied correction-row occurrences are decided, in their original
  order. They refer to 58 pages and contain 77 distinct statement ids.
  Repeated ids are retained separately by cote and scan.

Decisions
  a: 14 rows — transcription corrections applied on 9 pages.
  b: 56 rows — authorial slips or mathematical refinements, preserved in text.
  c:  3 rows — the supplied transcription already has the requested reading.
  d:  8 rows — the quoted passage or external metadata is absent from the page.
  All 58 final LaTeX pages are in edited_pages/, including unchanged pages.

Principal files
  placements.tsv    The requested eight columns, with all 81 row occurrences.
  edited_pages/     Final page files under their original filenames.
  notes.md          Every b and d decision, and 11 rows with residual ink doubt.
  crops/            180 retained image crops and their provenance sidecars.
  CHECK_EVENTS.tsv  169 explicitly scoped check events.
  progress.log      Initial UTC time and one completed-page entry per page.
  AUDIT.json        Final structural, byte-preservation and coverage audit.
  MANIFEST.sha256   SHA-256 hashes of all other delivered files.

Review documentation
  reviews/ contains the page-reader decisions and candidate files, the
  main-reader accepted decisions, the dispatch order, and input hashes.
  The authoritative transcription is edited_pages/; accepted decisions
  and placements.tsv reconstruct it exactly from the supplied originals.
  Each page was assigned to one of three readers, in the given page order,
  and reviewed by the main reader before its completion entry was written.

Method and limits
  The supplied manuscript JPGs were read visually. No OCR, PDF text layer,
  or text-recognition library was used. Crops were enlarged and contrast
  raised; rotations are documented in the corresponding sidecars.
  Only row-local transcription edits were applied. Original CRLF line
  endings and unrelated bytes, macros, cancellations and diagrams remain.
  Unsettled readings at flagged places remain marked and are noted.
  For a b decision, existing uncertainty wrappers were also retained under
  the no-edit rule; where the ink resolves such an alternative, the notes
  say so explicitly. Thus an inherited wrapper does not necessarily mean
  that this review still doubts the stated local reading.
  Visual collation does not constitute a mathematical proof. Check-event
  outcomes distinguish visual verification from the limited calculations
  or targeted arguments that were actually performed. Proposed mathematical
  corrections in the notes are attributed to the supplied correction rows.
  The runtime did not expose a named reasoning-effort setting; the event
  log records this fact instead of inventing one.

TSV handling
  Use a TSV parser that respects quoted fields. Some exact find/replace
  fields contain embedded CRLF line breaks. Do not split the table by raw
  lines or normalize line endings in those fields. Every nonempty find
  span occurs exactly once in its original page. All spans refer to the
  original page, so apply their minimal changes together rather than
  assuming later spans match text already changed by an earlier row.

Reproducing the structural audit
  Place this archive's contents in a folder named deliverable, beside a
  folder named source containing the already-unpacked original inputs.
  Run: python deliverable/scripts/review_workflow.py audit --final
  This checks source hashes, all 81 row identities and their order, exact
  reconstruction from placements, all 58 output pages, CRLF preservation,
  crop provenance, event coverage and completion-log consistency.
  The original attachments are intentionally not included in this archive.
