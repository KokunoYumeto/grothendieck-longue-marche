# Read-only records audit — scans 010–013

An independent auxiliary agent audited the committed records without viewing images, editing files, reading current/future pages, using OCR, browsing or compiling. It was not an additional page reader and made no transcription decision.

At the audited snapshot, the committed decisions and generated outputs agreed: 70 loci against C, 87 against H, 120 changed loci counted once (54 high, 38 medium, 28 low confidence), 213 inventory entries, 43 remaining-doubt entries, 43 notation observations, 30 check events and 12 independent reader runs. All 165 crop JPEGs had populated matching sidecars, all decision crop pointers resolved, and the four stored structural-validation page hashes matched their current files. These are consistency checks, not a new visual proof of the readings.

The CHECK_EVENTS outcomes consistently distinguish conditional local checks from source-background assertions. No theorem-proof overclaim was identified. Brief headers, decision versions, workflow crop counts and recorded image-delivery exceptions agreed.

The audit identified a final-gate gap: a set of sweep `where` identifiers could pass while only one clause of the joint scan014/016 record had been reviewed. The main reader added required `(scan, where)` pairs. The long scan018–026 record now additionally requires a per-page applicability record and an explicit statement/margin locus manifest, populated during those page adjudications. The audit did not inspect those pages or assign their loci.

The existing freeze script already keeps an independent immutable hash manifest and compares its stored values at the end. The main reader strengthened its verify mode to require exactly the expected 18 page files plus the combined transcription; a freshly written syntax report is never used as proof that the frozen state is unchanged.
